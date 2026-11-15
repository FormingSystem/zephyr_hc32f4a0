/* SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#include "probe.h"

volatile uint32_t g_result;

/* 仅提供完整引用链；没有复位向量和启动初始化，不能作为板卡固件。 */
void object_entry(void)
{
	g_result = scale_sample(7U);
	for (;;) {
		/* 本专题不运行这个入口；观察对象文件和最终链接结果。 */
	}
}
