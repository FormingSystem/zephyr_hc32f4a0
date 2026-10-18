---
id: learning.zephyr-docs.hardware.gpioext-3
title: MAX32GPIO标志
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第277章\_MAX32GPIO标志

原文：[group__gpio__interface__max32](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html)。读取日期：2026-10-13，`latest`。

## 277.1\_标志字段

本页定义 MAX32 的通用输入/输出（General Purpose Input/Output，GPIO）专用标志，声明来自 `zephyr/dt-bindings/gpio/adi-max32-gpio.h`。标志编码在设备树（Devicetree）GPIO类型 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) 的高8位。

- 第8位选择引脚电源轨（Supply Voltage Rail）：0为 `VDDIO`，1为 `VDDIOH`；两者是器件供电轨名称。
- 驱动强度（Drive Strength）从第9位开始，编码0、1、2、3分别对应1、2、4、8 mA。
- 第11位选择弱上拉（Weak Pull-up）：原文为通过1 MΩ接到 `VDDIO`，0禁用、1启用。
- 第12位选择弱下拉（Weak Pull-down）：原文为通过1 MΩ接到 `VDDIOH`，0禁用、1启用。

> 译注：原文文字将驱动强度称为“Bit 9”，但掩码为 `0x03U << 9`，即占第9—10位；此处按掩码说明起始位。原文的弱下拉说明确实写作“to VDDIOH”，与通常的下拉描述不符，本译文保留该信息，接线判断应核对具体器件手册。

## 277.2\_宏定义

宏名后缀 `_POS` 表示位位置（Position），`_MASK` 表示掩码（Mask）。

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| [`MAX32_GPIO_VSEL_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga267d4548e80843b5b5678d2050cbef73) | `(8U)` | 电源选择位位置 |
| [`MAX32_GPIO_VSEL_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga57b502aa34453a1af1eb5103221c5bde) | `(0x01U << MAX32_GPIO_VSEL_POS)` | 电源选择掩码 |
| [`MAX32_GPIO_VSEL_VDDIO`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga476d2376c91da2a1cf1bdfd0a7a95198) | `(0U << MAX32_GPIO_VSEL_POS)` | 选择VDDIO供电轨 |
| [`MAX32_GPIO_VSEL_VDDIOH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga964594ce9114dc57a9e50e416e948147) | `(1U << MAX32_GPIO_VSEL_POS)` | 选择VDDIOH供电轨 |
| [`MAX32_GPIO_DRV_STRENGTH_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga8f42437e9d5cbc3bb2d9d58fee643bc5) | `(9U)` | 驱动强度起始位 |
| [`MAX32_GPIO_DRV_STRENGTH_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaefce80e7ae44c9f9397e3b4f02a59893) | `(0x03U << MAX32_GPIO_DRV_STRENGTH_POS)` | 驱动强度掩码 |
| [`MAX32_GPIO_DRV_STRENGTH_0`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaf783f2b803f4772b5bf4c83f616b8a8a) | `(0U << MAX32_GPIO_DRV_STRENGTH_POS)` | 1 mA驱动 |
| [`MAX32_GPIO_DRV_STRENGTH_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga2e0abcd63dbbef23c2368be433c1909d) | `(1U << MAX32_GPIO_DRV_STRENGTH_POS)` | 2 mA驱动 |
| [`MAX32_GPIO_DRV_STRENGTH_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gae7199008d9e034361d80355651128fdd) | `(2U << MAX32_GPIO_DRV_STRENGTH_POS)` | 4 mA驱动 |
| [`MAX32_GPIO_DRV_STRENGTH_3`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gacf1c36bc17e552528ef20d4a8ae67f36) | `(3U << MAX32_GPIO_DRV_STRENGTH_POS)` | 8 mA驱动 |
| [`MAX32_GPIO_WEAK_PULL_UP_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gad20918791adf470f4421a2cbc1c7beaf) | `(11U)` | 弱上拉位位置 |
| [`MAX32_GPIO_WEAK_PULL_UP`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gac3a2881b03a0e130c0dc174a7aad5b04) | `(1U << MAX32_GPIO_WEAK_PULL_UP_POS)` | 启用1 MΩ弱上拉至VDDIO |
| [`MAX32_GPIO_WEAK_PULL_DOWN_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#ga81dd2d4a0dbd87b5346c65e608f5ea45) | `(12U)` | 弱下拉位位置 |
| [`MAX32_GPIO_WEAK_PULL_DOWN`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__max32.html#gaa2a5bc76ccfd583c11ee5f18015871be) | `(1U << MAX32_GPIO_WEAK_PULL_DOWN_POS)` | 启用1 MΩ弱下拉，原文写至VDDIOH |

---

[上一章：nRFGPIO标志](P276_nRFGPIO标志.md) · [下一章：nPM10xxGPIO标志](P278_nPM10xxGPIO标志.md) · [返回大纲](大纲.md)
