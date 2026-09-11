/* SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

/* 教学地址，仅用于观察链接，不是 HC32 的启动或存储布局。 */
ENTRY(object_entry)

SECTIONS
{
	. = 0x1000;
	.text : { *(.text*) }
	.rodata : { *(.rodata*) }
	.probe_metadata : { *(.probe_metadata) }
	. = 0x20000000;
	.data : { *(.data*) }
	.bss (NOLOAD) : { *(.bss*) *(COMMON) }
}
