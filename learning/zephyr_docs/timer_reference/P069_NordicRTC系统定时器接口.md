---
id: learning.zephyr-docs.timer_reference.timersample-69
title: NordicRTC系统定时器接口
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__rtc__timer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第69章\_NordicRTC系统定时器接口

原文：[nrf__rtc__timer_8h](https://docs.zephyrproject.org/latest/doxygen/html/nrf__rtc__timer_8h.html)。读取日期：2026-10-13，`latest`。

本页对应`zephyr/drivers/timer/nrf_rtc_timer.h`的文件参考。Nordic RTC系统定时器（System Timer）使用实时时钟（Real-Time Clock，RTC），头文件包含：

```c
#include <zephyr/sys/clock.h>
```

## 69.1\_可判定为未来的最大时间跨度

`NRF_RTC_TIMER_MAX_SCHEDULE_SPAN`宏定义允许被视为未来时间的最大跨度（Maximum Schedule Span）：

```c
#define NRF_RTC_TIMER_MAX_SCHEDULE_SPAN BIT(CONFIG_NRF_RTC_COUNTER_BIT_WIDTH - 1)
```

原文件参考仅详细列出此宏，表达式完整保留。`CONFIG_NRF_RTC_COUNTER_BIT_WIDTH`是表达式使用的计数位宽配置名称。

## 69.2\_对应完整声明

该文件的[源码浏览页](P070_NordicRTC系统定时器源码.md)还可见一个比较回调（Compare Callback）类型与14个函数声明，包含通道、读取、比较、中断控制、时间设置及偏移量相关操作。源码中可见的这些声明全部保留；本文件参考页没有为它们提供参数或错误码契约。

---

[上一章：nRF53同步实时时钟示例](P068_nRF53同步实时时钟示例.md) · [下一章：NordicRTC系统定时器源码](P070_NordicRTC系统定时器源码.md) · [返回大纲](大纲.md)
