---
id: learning.zephyr-docs.timer_reference.timersample-72
title: NordicGRTC系统定时器源码
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__grtc__timer_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第72章\_NordicGRTC系统定时器源码

原文：[nrf__grtc__timer_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/nrf__grtc__timer_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保存`zephyr/drivers/timer/nrf_grtc_timer.h`官方源码浏览页的全部可见代码、版权和许可，仅移除网页行号及行尾空白。应用初始化入口的说明见[文件参考](P071_NordicGRTC系统定时器接口.md)。

## 72.1\_完整可见源码

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_GRTC_TIMER_H
#define ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_GRTC_TIMER_H

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/sys/clock.h>

typedef void (*z_nrf_grtc_timer_compare_handler_t)(int32_t id, uint64_t expire_time,
                                                   void *user_data);

int32_t z_nrf_grtc_timer_chan_alloc(void);

int32_t z_nrf_grtc_timer_ext_chan_alloc(void);

void z_nrf_grtc_timer_chan_free(int32_t chan);

uint64_t z_nrf_grtc_timer_read(void);

bool z_nrf_grtc_timer_compare_evt_check(int32_t chan);

uint32_t z_nrf_grtc_timer_compare_evt_address_get(int32_t chan);

uint32_t z_nrf_grtc_timer_capture_task_address_get(int32_t chan);

bool z_nrf_grtc_timer_compare_int_lock(int32_t chan);

void z_nrf_grtc_timer_compare_int_unlock(int32_t chan, bool key);

int z_nrf_grtc_timer_compare_read(int32_t chan, uint64_t *val);

int z_nrf_grtc_timer_set(int32_t chan, uint64_t target_time,
                                z_nrf_grtc_timer_compare_handler_t handler, void *user_data);

int z_nrf_grtc_timer_interval_set(int32_t chan, uint32_t initial_value, uint32_t interval_value,
                                z_nrf_grtc_timer_compare_handler_t handler, void *user_data);

void z_nrf_grtc_timer_interval_stop(int32_t chan);

void z_nrf_grtc_timer_abort(int32_t chan);

uint64_t z_nrf_grtc_timer_get_ticks(k_timeout_t t);

int z_nrf_grtc_timer_capture_prepare(int32_t chan);

int z_nrf_grtc_timer_capture_read(int32_t chan, uint64_t *captured_time);

int z_nrf_grtc_wakeup_prepare(uint64_t wake_time_us);

uint64_t z_nrf_grtc_timer_startup_value_get(void);

int nrf_grtc_timer_clock_driver_init(void);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_TIMER_NRF_GRTC_TIMER_H */
```

## 72.2\_声明范围

源码保留比较回调（Compare Callback）类型`z_nrf_grtc_timer_compare_handler_t`及20个函数声明。回调参数为`int32_t id``uint64_t expire_time`和`void *user_data`。

比较读取（Compare Read）声明`z_nrf_grtc_timer_compare_read`返回`int`，通过`uint64_t *val`指针传递读数；捕获读取（Capture Read）声明`z_nrf_grtc_timer_capture_read`同样返回`int`，输出指针为`uint64_t *captured_time`。间隔设置（Interval Set）的初值`initial_value`和间隔值`interval_value`均为`uint32_t`。

源码还保留外部通道分配、间隔停止、捕获准备、唤醒准备（Wake-up Preparation）及启动值读取等声明。原页没有这些函数的实现与额外英文注释；接口参数单位或错误码没有仅凭名字补写。头文件保护、C++条件包装和包含项均保持原样。

---

[上一章：NordicGRTC系统定时器接口](P071_NordicGRTC系统定时器接口.md) · [下一章：实时时钟驱动头文件目录](P073_实时时钟驱动头文件目录.md) · [返回大纲](大纲.md)
