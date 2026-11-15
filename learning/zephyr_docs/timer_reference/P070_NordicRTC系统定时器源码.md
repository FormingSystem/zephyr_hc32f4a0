---
id: learning.zephyr-docs.timer_reference.timersample-70
title: NordicRTC系统定时器源码
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__rtc__timer_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第70章\_NordicRTC系统定时器源码

原文：[nrf__rtc__timer_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nrf__rtc__timer_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保存`zephyr/drivers/timer/nrf_rtc_timer.h`官方源码浏览页的全部可见代码、版权和许可，仅移除网页行号及行尾空白。宏的原文说明见[对应参考页](P069_NordicRTC系统定时器接口.md)。

## 70.1\_完整可见源码

```c
/*
 * Copyright (c) 2016-2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_RTC_TIMER_H
#define ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_RTC_TIMER_H

#include <zephyr/sys/clock.h>

#ifdef __cplusplus
extern "C" {
#endif

#define NRF_RTC_TIMER_MAX_SCHEDULE_SPAN BIT(CONFIG_NRF_RTC_COUNTER_BIT_WIDTH - 1)

typedef void (*z_nrf_rtc_timer_compare_handler_t)(int32_t id,
                                                uint64_t expire_time,
                                                void *user_data);

int32_t z_nrf_rtc_timer_chan_alloc(void);

void z_nrf_rtc_timer_chan_free(int32_t chan);

uint64_t z_nrf_rtc_timer_read(void);

uint32_t z_nrf_rtc_timer_compare_evt_address_get(int32_t chan);

uint32_t z_nrf_rtc_timer_capture_task_address_get(int32_t chan);

bool z_nrf_rtc_timer_compare_int_lock(int32_t chan);

void z_nrf_rtc_timer_compare_int_unlock(int32_t chan, bool key);

uint32_t z_nrf_rtc_timer_compare_read(int32_t chan);

int z_nrf_rtc_timer_set(int32_t chan, uint64_t target_time,
                         z_nrf_rtc_timer_compare_handler_t handler,
                         void *user_data);

int z_nrf_rtc_timer_exact_set(int32_t chan, uint64_t target_time,
                              z_nrf_rtc_timer_compare_handler_t handler,
                              void *user_data);

void z_nrf_rtc_timer_abort(int32_t chan);

uint64_t z_nrf_rtc_timer_get_ticks(k_timeout_t t);

int z_nrf_rtc_timer_nrf53net_offset_get(void);

int z_nrf_rtc_timer_trigger_overflow(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_RTC_TIMER_H */
```

## 70.2\_声明范围

源码包含一个最大调度跨度宏、一个比较回调（Compare Callback）类型`z_nrf_rtc_timer_compare_handler_t`以及14个函数声明。回调参数保留`int32_t id``uint64_t expire_time`和`void *user_data`三种原类型与名称。

`z_nrf_rtc_timer_compare_read`的返回类型为`uint32_t`；`z_nrf_rtc_timer_read`和`z_nrf_rtc_timer_get_ticks`则返回`uint64_t`。通道中断锁（Interrupt Lock）接口使用`bool`状态键。文件还保留`z_nrf_rtc_timer_exact_set`、`z_nrf_rtc_timer_nrf53net_offset_get`、`z_nrf_rtc_timer_trigger_overflow`声明，不将其改写为公共计数器API。

本源码页没有额外英文实现注释，也没有函数实现。C++条件包装、头文件保护、参数、类型和包含项均原样保存。

---

[上一章：NordicRTC系统定时器接口](P069_NordicRTC系统定时器接口.md) · [下一章：NordicGRTC系统定时器接口](P071_NordicGRTC系统定时器接口.md) · [返回大纲](大纲.md)
