/* SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#define DT_DRV_COMPAT xhsc_hc32_uart

#include <zephyr/device.h>
#include <zephyr/drivers/gpio/gpio_utils.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/init.h>
#include <zephyr/irq.h>

#include <hc32_ll_fcg.h>
#include <hc32_ll_gpio.h>
#include <hc32_ll_usart.h>

struct uart_hc32_config {
	CM_USART_TypeDef *regs;
	uint32_t baudrate;
	uint32_t tx_pin_mask;
	uint32_t rx_pin_mask;
	uint32_t tx_port;
	uint32_t rx_port;
	uint32_t tx_pin;
	uint32_t rx_pin;
};

static int uart_hc32_poll_in(const struct device *dev, unsigned char *value)
{
	const struct uart_hc32_config *config = dev->config;
	unsigned int key = irq_lock();
	int ret = -1;

	if (USART_GetStatus(config->regs, USART_FLAG_RX_FULL) == SET) {
		*value = (unsigned char)USART_ReadData(config->regs);
		ret = 0;
	}
	irq_unlock(key);
	return ret;
}

static void uart_hc32_poll_out(const struct device *dev, unsigned char value)
{
	const struct uart_hc32_config *config = dev->config;
	unsigned int key = irq_lock();

	/* Serialize the empty-register check and write against interrupt users. */
	while (USART_GetStatus(config->regs, USART_FLAG_TX_EMPTY) == RESET) {
	}
	USART_WriteData(config->regs, value);
	irq_unlock(key);
}

static int uart_hc32_err_check(const struct device *dev)
{
	const struct uart_hc32_config *config = dev->config;
	unsigned int key = irq_lock();
	uint32_t status = config->regs->SR;
	uint32_t errors =
		status & (USART_FLAG_OVERRUN | USART_FLAG_PARITY_ERR | USART_FLAG_FRAME_ERR);
	int result = 0;

	if ((errors & USART_FLAG_OVERRUN) != 0U) {
		result |= UART_ERROR_OVERRUN;
	}
	if ((errors & USART_FLAG_PARITY_ERR) != 0U) {
		result |= UART_ERROR_PARITY;
	}
	if ((errors & USART_FLAG_FRAME_ERR) != 0U) {
		result |= UART_ERROR_FRAMING;
	}
	if (errors != 0U) {
		USART_ClearStatus(config->regs, errors);
	}
	irq_unlock(key);
	return result;
}

static int uart_hc32_init(const struct device *dev)
{
	const struct uart_hc32_config *config = dev->config;
	stc_usart_uart_init_t init;
	stc_gpio_init_t pin_init;
	unsigned int key;
	int32_t ret;

	/* This implementation supports the verified USART1 pin assignment. */
	if (config->regs != CM_USART1 || config->tx_port != GPIO_PORT_A ||
	    config->rx_port != GPIO_PORT_A || config->tx_pin != 9U || config->rx_pin != 10U) {
		return -ENOTSUP;
	}
	if (config->baudrate == 0U || (config->tx_pin_mask & BIT(config->tx_pin)) == 0U ||
	    (config->rx_pin_mask & BIT(config->rx_pin)) == 0U) {
		return -EINVAL;
	}

	ret = GPIO_StructInit(&pin_init);
	if (ret != LL_OK) {
		return -EIO;
	}
	key = irq_lock();
	GPIO_REG_Unlock();
	ret = GPIO_Init(GPIO_PORT_A, GPIO_PIN_09 | GPIO_PIN_10, &pin_init);
	if (ret == LL_OK) {
		GPIO_SubFuncCmd(GPIO_PORT_A, GPIO_PIN_09 | GPIO_PIN_10, DISABLE);
		GPIO_SetFunc(GPIO_PORT_A, GPIO_PIN_09, GPIO_FUNC_32);
		GPIO_SetFunc(GPIO_PORT_A, GPIO_PIN_10, GPIO_FUNC_33);
	}
	GPIO_REG_Lock();
	FCG_Fcg3PeriphClockCmd(FCG3_PERIPH_USART1, ENABLE);
	irq_unlock(key);
	if (ret != LL_OK) {
		return -EIO;
	}

	ret = USART_UART_StructInit(&init);
	if (ret != LL_OK) {
		return -EIO;
	}
	init.u32Baudrate = config->baudrate;
	init.u32ClockDiv = USART_CLK_DIV1;
	init.u32OverSampleBit = USART_OVER_SAMPLE_16BIT;
	init.u32HWFlowControl = USART_HW_FLOWCTRL_NONE;
	ret = USART_UART_Init(config->regs, &init, NULL);
	if (ret != LL_OK) {
		return -EINVAL;
	}
	USART_ClearStatus(config->regs,
			  USART_FLAG_OVERRUN | USART_FLAG_PARITY_ERR | USART_FLAG_FRAME_ERR);
	USART_FuncCmd(config->regs, USART_TX | USART_RX, ENABLE);
	return 0;
}

static DEVICE_API(uart, uart_hc32_api) = {
	.poll_in = uart_hc32_poll_in,
	.poll_out = uart_hc32_poll_out,
	.err_check = uart_hc32_err_check,
};

#define UART_HC32_DEFINE(inst)                                                                     \
	static const struct uart_hc32_config uart_hc32_config_##inst = {                           \
		.regs = (CM_USART_TypeDef *)DT_INST_REG_ADDR(inst),                                \
		.baudrate = DT_INST_PROP(inst, current_speed),                                     \
		.tx_port = DT_PROP(DT_INST_PHANDLE(inst, tx_port), port_index),                    \
		.rx_port = DT_PROP(DT_INST_PHANDLE(inst, rx_port), port_index),                    \
		.tx_pin = DT_INST_PROP(inst, tx_pin),                                              \
		.rx_pin = DT_INST_PROP(inst, rx_pin),                                              \
		.tx_pin_mask = GPIO_PORT_PIN_MASK_FROM_DT_NODE(DT_INST_PHANDLE(inst, tx_port)),    \
		.rx_pin_mask = GPIO_PORT_PIN_MASK_FROM_DT_NODE(DT_INST_PHANDLE(inst, rx_port)),    \
	};                                                                                         \
	DEVICE_DT_INST_DEFINE(inst, uart_hc32_init, NULL, NULL, &uart_hc32_config_##inst,          \
			      PRE_KERNEL_1, CONFIG_SERIAL_INIT_PRIORITY, &uart_hc32_api);

DT_INST_FOREACH_STATUS_OKAY(UART_HC32_DEFINE)
