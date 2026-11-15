/*
 * Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_DRIVERS_USB_UDC_DWC2_HC32F4A0_H
#define ZEPHYR_DRIVERS_USB_UDC_DWC2_HC32F4A0_H

#include <hc32_ll.h>

BUILD_ASSERT(CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC == 48000000,
	     "HC32 USBFS requires the SoC 48 MHz PLLH configuration");

static int hc32_usbfs_post_enable(const struct device *dev)
{
	ARG_UNUSED(dev);
	/* RM Rev1.50 USBFS_GUSBCFG: TRDT = 5 at HCLK = PHY = 48 MHz. */
	MODIFY_REG32(CM_USBFS->GUSBCFG, USBFS_GUSBCFG_TRDT, 5U << USBFS_GUSBCFG_TRDT_POS);
	return 0;
}

static int hc32_usbfs_disable(const struct device *dev)
{
	ARG_UNUSED(dev);
	FCG_Fcg1PeriphClockCmd(FCG1_PERIPH_USBFS, DISABLE);
	return 0;
}

static int hc32_usbfs_pre_enable(uint32_t irq, uint32_t source, bool no_vbus_sensing)
{
	stc_pll_clock_freq_t clocks;

	if (CLK_GetPLLClockFreq(&clocks) != LL_OK || clocks.u32PllQ != 48000000U) {
		return -EINVAL;
	}
	GPIO_REG_Unlock();
	GPIO_AnalogCmd(GPIO_PORT_A, GPIO_PIN_11 | GPIO_PIN_12, ENABLE);
	if (!no_vbus_sensing) {
		GPIO_SetFunc(GPIO_PORT_A, GPIO_PIN_09, GPIO_FUNC_10);
	}
	GPIO_REG_Lock();
	FCG_Fcg1PeriphClockCmd(FCG1_PERIPH_USBFS, ENABLE);
	/* Keep Zephyr's vector table and ISR wrapper; only select the HC32 source. */
	sys_write32(source, (mem_addr_t)&CM_INTC->SEL0 + irq * sizeof(uint32_t));
	NVIC_ClearPendingIRQ((IRQn_Type)irq);
	if (no_vbus_sensing) {
		SET_REG32_BIT(CM_USBFS->GVBUSCFG, USBFS_GVBUSCFG_VBUSOVEN | USBFS_GVBUSCFG_VBUSVAL);
	} else {
		CLR_REG32_BIT(CM_USBFS->GVBUSCFG, USBFS_GVBUSCFG_VBUSOVEN);
	}
	return 0;
}

#define QUIRK_HC32_USBFS_DEFINE(n)                                                                 \
	BUILD_ASSERT(DT_INST_IRQN(n) < 32, "USBFS needs a freely routable IRQ slot");              \
	static int hc32_usbfs_pre_enable_##n(const struct device *dev)                             \
	{                                                                                          \
		ARG_UNUSED(dev);                                                                   \
		return hc32_usbfs_pre_enable(DT_INST_IRQN(n), DT_INST_PROP(n, interrupt_source),   \
					     DT_INST_PROP(n, disable_vbus_sensing));               \
	}                                                                                          \
	static const struct dwc2_vendor_quirks dwc2_vendor_quirks_##n = {                          \
		.pre_enable = hc32_usbfs_pre_enable_##n,                                           \
		.post_enable = hc32_usbfs_post_enable,                                             \
		.disable = hc32_usbfs_disable,                                                     \
	};

DT_INST_FOREACH_STATUS_OKAY(QUIRK_HC32_USBFS_DEFINE)

#endif /* ZEPHYR_DRIVERS_USB_UDC_DWC2_HC32F4A0_H */
