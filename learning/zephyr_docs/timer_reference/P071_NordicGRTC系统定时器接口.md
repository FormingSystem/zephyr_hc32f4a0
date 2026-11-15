---
id: learning.zephyr-docs.timer_reference.timersample-71
title: NordicGRTC系统定时器接口
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__grtc__timer_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第71章\_NordicGRTC系统定时器接口

原文：[nrf__grtc__timer_8h](https://docs.zephyrproject.org/latest/doxygen/html/nrf__grtc__timer_8h.html)。读取日期：2026-10-13，`latest`。

本页对应`zephyr/drivers/timer/nrf_grtc_timer.h`文件参考，提供Nordic GRTC时钟定时器（Clock Timer）驱动的应用初始化入口。GRTC为全局实时计数器（Global Real Time Counter）。头文件包含：

```c
#include <zephyr/sys/clock.h>
```

> 术语补注：GRTC全称参照[Nordic官方nrfx头文件](https://raw.githubusercontent.com/NordicSemiconductor/nrfx/master/hal/nrf_grtc.h)，这里只补充名称，不引入额外硬件规格。

## 71.1\_从应用函数初始化驱动

`nrf_grtc_timer_clock_driver_init`从应用定义的函数（Application-defined Function）初始化GRTC时钟定时器驱动：

```c
int nrf_grtc_timer_clock_driver_init(void);
```

没有参数。成功返回0，失败返回负错误码`-errno`（Negative Error Code）。

## 71.2\_完整可见声明

原文件参考只详细列出上述函数。[对应源码页](P072_NordicGRTC系统定时器源码.md)还保存其他可见的通道、比较、间隔、捕获和唤醒相关声明；这些声明的更详细行为没有在本参考页公开。

---

[上一章：NordicRTC系统定时器源码](P070_NordicRTC系统定时器源码.md) · [下一章：NordicGRTC系统定时器源码](P072_NordicGRTC系统定时器源码.md) · [返回大纲](大纲.md)
