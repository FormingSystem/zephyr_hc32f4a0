/* SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#ifndef LEARNING_OBJECT_PROBE_H_
#define LEARNING_OBJECT_PROBE_H_

#include <stdint.h>

/* 头文件声明跨文件约定；存储只由 calibration.c 的定义提供。 */
extern uint32_t g_bias;
uint32_t scale_sample(uint32_t value);

#endif
