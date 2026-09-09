/*
 * SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

ASSERT(CONFIG_FLASH_BASE_ADDRESS == 0, "HC32 ICG requires internal Flash at address zero");
ASSERT(CONFIG_FLASH_LOAD_OFFSET == 0, "HC32 application boot offset is not supported");
ASSERT(. <= 0x400, "HC32 vector table overlaps ICG");
FILL(0xffffffff)
. = 0x400;
__hc32_icg_start = .;
KEEP(*(.icg_sec))
__hc32_icg_end = .;
ASSERT(__hc32_icg_start == 0x400, "HC32 ICG must start at 0x400");
ASSERT(__hc32_icg_end - __hc32_icg_start == 24 * 4, "HC32 ICG requires 24 words");
