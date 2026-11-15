/*
 * SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
#include <hc32_ll.h>

#define HC32_XTAL_HZ 12000000U
#define HC32_BOOT_CLOCK_HZ CONFIG_SYS_CLOCK_HW_CYCLES_PER_SEC
/* At the MRC maximum of 8.8 MHz, even one cycle per poll allows over 200 ms. */
#define HC32_CLOCK_STABLE_POLLS 2000000U
#define HC32_INIT_PERIPHERALS \
	(LL_PERIPH_PWC_CLK_RMU | LL_PERIPH_FCG | LL_PERIPH_EFM | LL_PERIPH_SRAM | \
	 LL_PERIPH_GPIO)

BUILD_ASSERT(HC32_BOOT_CLOCK_HZ == 12000000U || HC32_BOOT_CLOCK_HZ == 48000000U,
	     "HC32 supports 12 MHz XTAL or 48 MHz PLLH");
BUILD_ASSERT(XTAL_VALUE == HC32_XTAL_HZ, "DDL must match the fitted 12 MHz crystal");
BUILD_ASSERT(!IS_ENABLED(CONFIG_ARM_MPU), "HC32 MPU region configuration is not implemented");

static void clock_wait_stable(uint8_t flag, en_flag_status_t expected)
{
	for (uint32_t count = 0; count < HC32_CLOCK_STABLE_POLLS; count++) {
		if (CLK_GetStableStatus(flag) == expected) {
			return;
		}
	}

	/* Never boot with an RC fallback reported as a 12 MHz system clock. */
	k_panic();
}

void soc_early_init_hook(void)
{
	const stc_clock_xtal_init_t xtal = {
		.u8State = CLK_XTAL_OFF,
		.u8Mode = CLK_XTAL_MD_OSC,
		.u8Drv = CLK_XTAL_DRV_LOW,
		.u8StableTime = CLK_XTAL_STB_31MS,
	};
	int32_t status;

	/* Initialize DDL timing variables without overwriting Zephyr's VTOR/FPU state. */
	SystemCoreClockUpdate();
	LL_PERIPH_WE(HC32_INIT_PERIPHERALS);

	if (CLK_MrcCmd(ENABLE) != LL_OK) {
		k_panic();
	}
	/* MRC startup is at most 3 us; also covers entry with MRC previously stopped. */
	DDL_DelayUS(10U);

	/* Lower the source frequency before reducing Flash or SRAM wait cycles. */
	CLK_SetSysClockSrc(CLK_SYSCLK_SRC_MRC);
	CLK_SetClockDiv(CLK_BUS_CLK_ALL,
			CLK_HCLK_DIV1 | CLK_PCLK0_DIV1 | CLK_PCLK1_DIV1 |
			CLK_PCLK2_DIV1 | CLK_PCLK3_DIV1 | CLK_PCLK4_DIV1 |
			CLK_EXCLK_DIV1);

	/* 0 waits are valid for both the 8 MHz transition and final 12 MHz source. */
	if (EFM_SetWaitCycle(EFM_WAIT_CYCLE0) != LL_OK) {
		k_panic();
	}
	SRAM_SetWaitCycle(SRAM_SRAM_ALL, SRAM_WAIT_CYCLE0, SRAM_WAIT_CYCLE0);

	/* Neither PLL is used; release XTAL before changing its configuration. */
	if (CLK_PLLCmd(DISABLE) != LL_OK || CLK_PLLxCmd(DISABLE) != LL_OK) {
		k_panic();
	}
	clock_wait_stable(CLK_STB_FLAG_PLL, RESET);
	clock_wait_stable(CLK_STB_FLAG_PLLX, RESET);
	if (READ_REG8(CM_CMU->XTALCR) == CLK_XTAL_ON) {
		clock_wait_stable(CLK_STB_FLAG_XTAL, SET);
	}
	if (CLK_XtalCmd(DISABLE) != LL_OK) {
		k_panic();
	}
	clock_wait_stable(CLK_STB_FLAG_XTAL, RESET);

	/* HC32F4A0PITB PH0/PH1 are XTAL_OUT/XTAL_IN (physical pins 12/13). */
	GPIO_AnalogCmd(GPIO_PORT_H, GPIO_PIN_00 | GPIO_PIN_01, ENABLE);
	if (CLK_XtalInit(&xtal) != LL_OK) {
		k_panic();
	}
	status = CLK_XtalCmd(ENABLE);
	if (status != LL_OK && status != LL_ERR_TIMEOUT) {
		k_panic();
	}
	/* The DDL's short loop timeout is insufficient for the 31 ms stable counter. */
	clock_wait_stable(CLK_STB_FLAG_XTAL, SET);
	CLK_SetSysClockSrc(CLK_SYSCLK_SRC_XTAL);
	if (HC32_BOOT_CLOCK_HZ == 48000000U) {
		/* DS Rev1.60: PLLH input 8..25 MHz, VCO 600..1200 MHz.
		 * 12 MHz / 1 * 64 = 768 MHz; P/Q/R divide by 16 = 48 MHz.
		 */
		const stc_clock_pll_init_t pll = {
			.u8PLLState = CLK_PLL_ON,
			.PLLCFGR_f = {
				.PLLM = 0U, .PLLN = 63U, .PLLP = 15U,
				.PLLQ = 15U, .PLLR = 15U, .PLLSRC = CLK_PLL_SRC_XTAL,
			},
		};

		/* Set conservative memory wait cycles before increasing HCLK. */
		if (EFM_SetWaitCycle(EFM_WAIT_CYCLE1) != LL_OK) {
			k_panic();
		}
		SRAM_SetWaitCycle(SRAM_SRAM_ALL, SRAM_WAIT_CYCLE1, SRAM_WAIT_CYCLE1);
		status = CLK_PLLInit(&pll);
		if (status != LL_OK && status != LL_ERR_TIMEOUT) {
			k_panic();
		}
		clock_wait_stable(CLK_STB_FLAG_PLL, SET);
		CLK_SetSysClockSrc(CLK_SYSCLK_SRC_PLL);
		CLK_SetUSBClockSrc(CLK_USBCLK_PLLQ);
	}
	if (CLK_GetBusClockFreq(CLK_BUS_HCLK) != HC32_BOOT_CLOCK_HZ) {
		k_panic();
	}
	LL_PERIPH_WP(HC32_INIT_PERIPHERALS);
}
