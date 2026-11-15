---
id: learning.zephyr-docs.hardware.stepext-5
title: Trinamic堵转检测设置
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第242章\_Trinamic堵转检测设置

原文：[structtmc__stallguard__settings](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html)。读取日期：2026-10-13，`latest`。

## 242.1\_用途

结构 [`tmc_stallguard_settings`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html) 定义 Trinamic 步进电机的 **堵转检测（Stall Detection）**功能 StallGuard 设置，来自 `zephyr/drivers/stepper/stepper_trinamic.h`，用于[Trinamic配置接口](P240_Trinamic步进扩展.md)。StallGuard2 是原字段说明使用的功能名称。

## 242.2\_数据字段（Data Fields）

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| [`is_sg_enabled`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#a953ef8f63bbf5dff74b91723a435cb42) | [`bool`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b) | 启用 StallGuard2 功能。 |
| [`sg_velocity_check_interval_ms`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#aadc55163f314403e5d4cd231d4d209df) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 电机加速起转（Spin-up）时不应启用 StallGuard；通过此延迟检查实际步进速度是否大于 `stallguard-threshold-velocity`，再启用 StallGuard。 |
| [`sg_threshold_velocity`](https://docs.zephyrproject.org/latest/doxygen/html/structtmc__stallguard__settings.html#ac517501bdcb980b2690301bcdce78c98) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | StallGuard2 阈值速度（Threshold Velocity）。 |

> 译注：检查间隔字段名后缀 `_ms` 表示毫秒（Millisecond）；原字段页未给阈值速度的单位，不据名称推断成其他量纲。

---

[上一章：TMCM3216电机状态](P241_TMCM3216电机状态.md) · [下一章：Trinamic斜坡发生器参数](P243_Trinamic斜坡发生器参数.md) · [返回大纲](大纲.md)
