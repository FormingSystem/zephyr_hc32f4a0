/* SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#define DT_DRV_COMPAT xhsc_hc32_gpio

#include <zephyr/device.h>
#include <zephyr/drivers/gpio/gpio_utils.h>
#include <zephyr/init.h>
#include <zephyr/irq.h>

#include <hc32_ll_gpio.h>

struct gpio_hc32_config {
	struct gpio_driver_config common;
	uint32_t port;
};

struct gpio_hc32_data {
	struct gpio_driver_data common;
};

static int gpio_hc32_pin_configure(const struct device *dev, gpio_pin_t pin, gpio_flags_t flags)
{
	const struct gpio_hc32_config *config = dev->config;
	const gpio_flags_t supported = GPIO_INPUT | GPIO_OUTPUT | GPIO_OUTPUT_INIT_LOW |
				       GPIO_OUTPUT_INIT_HIGH | GPIO_ACTIVE_LOW | GPIO_PULL_UP |
				       GPIO_OPEN_DRAIN;
	stc_gpio_init_t init;
	unsigned int key;
	uint16_t mask;
	int32_t ret;

	if (pin >= 16U || (config->common.port_pin_mask & BIT(pin)) == 0U) {
		return -EINVAL;
	}
	if ((flags & ~supported) != 0U || (flags & (GPIO_INPUT | GPIO_OUTPUT)) == 0U) {
		return -ENOTSUP;
	}
	if ((flags & GPIO_SINGLE_ENDED) != 0U &&
	    ((flags & GPIO_LINE_OPEN_DRAIN) == 0U || (flags & GPIO_OUTPUT) == 0U)) {
		return -ENOTSUP;
	}
	if (((flags & GPIO_LINE_OPEN_DRAIN) != 0U && (flags & GPIO_SINGLE_ENDED) == 0U) ||
	    ((flags & (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH)) != 0U &&
	     (flags & GPIO_OUTPUT) == 0U) ||
	    (flags & (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH)) ==
		    (GPIO_OUTPUT_INIT_LOW | GPIO_OUTPUT_INIT_HIGH)) {
		return -EINVAL;
	}
	ret = GPIO_StructInit(&init);
	if (ret != LL_OK) {
		return -EIO;
	}
	mask = (uint16_t)BIT(pin);
	init.u16PinDir = (flags & GPIO_OUTPUT) != 0U ? PIN_DIR_OUT : PIN_DIR_IN;
	init.u16PullUp = (flags & GPIO_PULL_UP) != 0U ? PIN_PU_ON : PIN_PU_OFF;
	init.u16PinOutputType = (flags & GPIO_OPEN_DRAIN) == GPIO_OPEN_DRAIN ? PIN_OUT_TYPE_NMOS
									     : PIN_OUT_TYPE_CMOS;

	/* PCR and pin-function registers share one write-protection register. */
	key = irq_lock();
	if ((flags & GPIO_OUTPUT_INIT_HIGH) != 0U) {
		init.u16PinState = PIN_STAT_SET;
	} else if ((flags & GPIO_OUTPUT_INIT_LOW) != 0U) {
		init.u16PinState = PIN_STAT_RST;
	} else {
		init.u16PinState = GPIO_ReadOutputPins(config->port, mask) == PIN_SET
					   ? PIN_STAT_SET
					   : PIN_STAT_RST;
	}
	GPIO_REG_Unlock();
	ret = GPIO_Init(config->port, mask, &init);
	if (ret == LL_OK) {
		GPIO_SubFuncCmd(config->port, mask, DISABLE);
		GPIO_SetFunc(config->port, mask, GPIO_FUNC_0);
	}
	GPIO_REG_Lock();
	irq_unlock(key);
	return ret == LL_OK ? 0 : -EIO;
}

static int gpio_hc32_port_get_raw(const struct device *dev, gpio_port_value_t *value)
{
	const struct gpio_hc32_config *config = dev->config;

	*value = GPIO_ReadInputPort(config->port) & config->common.port_pin_mask;
	return 0;
}

static int gpio_hc32_port_set_masked_raw(const struct device *dev, gpio_port_pins_t mask,
					 gpio_port_value_t value)
{
	const struct gpio_hc32_config *config = dev->config;
	unsigned int key;
	uint16_t state;

	if ((mask & ~config->common.port_pin_mask) != 0U) {
		return -EINVAL;
	}
	if (mask == 0U) {
		return 0;
	}
	key = irq_lock();
	state = GPIO_ReadOutputPort(config->port);
	GPIO_WritePort(config->port, (uint16_t)((state & ~mask) | (value & mask)));
	irq_unlock(key);
	return 0;
}

static int gpio_hc32_port_set_bits_raw(const struct device *dev, gpio_port_pins_t pins)
{
	const struct gpio_hc32_config *config = dev->config;
	unsigned int key;

	if ((pins & ~config->common.port_pin_mask) != 0U) {
		return -EINVAL;
	}
	if (pins == 0U) {
		return 0;
	}
	key = irq_lock();
	GPIO_SetPins(config->port, (uint16_t)pins);
	irq_unlock(key);
	return 0;
}

static int gpio_hc32_port_clear_bits_raw(const struct device *dev, gpio_port_pins_t pins)
{
	const struct gpio_hc32_config *config = dev->config;
	unsigned int key;

	if ((pins & ~config->common.port_pin_mask) != 0U) {
		return -EINVAL;
	}
	if (pins == 0U) {
		return 0;
	}
	key = irq_lock();
	GPIO_ResetPins(config->port, (uint16_t)pins);
	irq_unlock(key);
	return 0;
}

static int gpio_hc32_port_toggle_bits(const struct device *dev, gpio_port_pins_t pins)
{
	const struct gpio_hc32_config *config = dev->config;
	unsigned int key;

	if ((pins & ~config->common.port_pin_mask) != 0U) {
		return -EINVAL;
	}
	if (pins == 0U) {
		return 0;
	}
	key = irq_lock();
	GPIO_TogglePins(config->port, (uint16_t)pins);
	irq_unlock(key);
	return 0;
}

static int gpio_hc32_pin_interrupt_configure(const struct device *dev, gpio_pin_t pin,
					     enum gpio_int_mode mode, enum gpio_int_trig trig)
{
	ARG_UNUSED(dev);
	ARG_UNUSED(pin);
	ARG_UNUSED(mode);
	ARG_UNUSED(trig);
	return -ENOTSUP;
}

static int gpio_hc32_init(const struct device *dev)
{
	const struct gpio_hc32_config *config = dev->config;
	/* HC32F4A0PITB LQFP100 bonded GPIOs, independent of overlay reservations. */
	static const uint16_t package_pins[] = {
		0xFFFFU, 0xFFFFU, 0xFFFFU, 0xFFFFU, 0xFFFFU, 0U, 0U, 0x0003U, 0x2000U,
	};

	if (config->port >= ARRAY_SIZE(package_pins) ||
	    (config->common.port_pin_mask & ~(uint32_t)package_pins[config->port]) != 0U) {
		return -EINVAL;
	}
	return 0;
}

static DEVICE_API(gpio, gpio_hc32_api) = {
	.pin_configure = gpio_hc32_pin_configure,
	.port_get_raw = gpio_hc32_port_get_raw,
	.port_set_masked_raw = gpio_hc32_port_set_masked_raw,
	.port_set_bits_raw = gpio_hc32_port_set_bits_raw,
	.port_clear_bits_raw = gpio_hc32_port_clear_bits_raw,
	.port_toggle_bits = gpio_hc32_port_toggle_bits,
	.pin_interrupt_configure = gpio_hc32_pin_interrupt_configure,
};

#define GPIO_HC32_DEFINE(inst)                                                                     \
	static struct gpio_hc32_data gpio_hc32_data_##inst;                                        \
	static const struct gpio_hc32_config gpio_hc32_config_##inst = {                           \
		.common = GPIO_COMMON_CONFIG_FROM_DT_INST(inst),                                   \
		.port = DT_INST_PROP(inst, port_index),                                            \
	};                                                                                         \
	DEVICE_DT_INST_DEFINE(inst, gpio_hc32_init, NULL, &gpio_hc32_data_##inst,                  \
			      &gpio_hc32_config_##inst, PRE_KERNEL_1, CONFIG_GPIO_INIT_PRIORITY,   \
			      &gpio_hc32_api);

DT_INST_FOREACH_STATUS_OKAY(GPIO_HC32_DEFINE)
