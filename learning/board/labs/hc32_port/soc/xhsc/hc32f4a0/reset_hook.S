/*
 * SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/toolchain.h>
#include <zephyr/linker/sections.h>

	.syntax unified
	.thumb

GTEXT(soc_reset_hook)
SECTION_FUNC(TEXT, soc_reset_hook)
	/* Clear power-on SRAM parity/ECC status before C runtime memory access. */
	ldr r0, =0x40050810
	ldr r1, =0x1ff
	str r1, [r0]
	dsb
	bx lr
