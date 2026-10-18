---
id: learning.zephyr-docs.hardware.ledapi-1
title: LED设备树描述结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第203章\_LED设备树描述结构

原文：[structled__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 203.1\_用途

结构 [`led_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html) 保存 **设备树（Devicetree，DT）**中指定的 **发光二极管（Light-Emitting Diode，LED）**信息，包含 LED 设备指针与其索引（Index）。定义来自官方头文件 `zephyr/drivers/led.h`。

## 203.2\_数据字段（Data Fields）

| 字段 | 原始类型 | 含义 |
| --- | --- | --- |
| [`dev`](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#ad92b9ee24cb31fcc0a2352bcf831cecb) | `const struct device *` | LED 设备实例（Device Instance）。 |
| [`index`](https://docs.zephyrproject.org/latest/doxygen/html/structled__dt__spec.html#a72c5ff64b89344ca9644fd2b4f4c9515) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | LED 在控制器中的索引。 |

可通过宏 [`LED_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga537f733ae3070fbe279834c76cda35ae) 或 [`LED_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gade3059194ce428783ea3e9900ed0be52) 创建静态初始化器，详见[LED公共接口](P202_LED公共接口.md)。

[上一章：LED公共接口](P202_LED公共接口.md) · [下一章：LED信息结构](P204_LED信息结构.md) · [返回大纲](大纲.md)
