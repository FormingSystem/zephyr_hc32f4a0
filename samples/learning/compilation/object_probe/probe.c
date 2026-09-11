/* SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#include <stddef.h>
#include "probe.h"

#ifndef SCALE
#define SCALE 2U
#endif

/* 普通结构布局不是外部数据格式，成员间可能插入填充。 */
struct sample_record {
	uint8_t tag;
	uint32_t count;
};

_Static_assert(sizeof(uint32_t) == 4, "This experiment requires 32-bit uint32_t");
_Static_assert(offsetof(struct sample_record, count) == 4, "Unexpected member layout");

/* 独立只读段便于提取证据，不依赖调试器或执行目标指令。 */
const uint32_t layout_manifest[] __attribute__((section(".probe_metadata"))) = {
	0x11223344U,
	sizeof(struct sample_record),
	_Alignof(struct sample_record),
	offsetof(struct sample_record, count),
	(uint32_t)-1,
	(uint8_t)256U,
};

static uint32_t multiply_sample(uint32_t value)
{
	return value * SCALE;
}

uint32_t scale_sample(uint32_t value)
{
	return multiply_sample(value) + g_bias;
}
