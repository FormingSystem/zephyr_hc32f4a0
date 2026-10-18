---
id: learning.zephyr-docs.clock-esp-infineon-microchip-binding-reference.page-4
title: espressif_esp32-clock
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/espressif,esp32-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第4章\_espressif_esp32-clock

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/espressif,esp32-clock.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="espressif-esp32-clock"></a>
<a id="dtbinding-espressif-esp32-clock"></a>
<a id="std-dtcompatible-espressif-esp32-clock"></a>

兼容字符串（Compatible String）：`espressif,esp32-clock`。厂商：[ Espressif Systems ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-espressif)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=espressif,esp32-clock)。

驱动源码（Driver Source）：[drivers/clock_control/clock_control_esp32.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_esp32.c)。

<a id="description"></a>

ESP32时钟模块，即电源与时钟控制器模块（Power & Clock Controller Module）。

译注：慢速时钟说明中的 `32,768U KHz`、`17,5 MHz` 按原文保留，未擅自更改频率或单位；属性的正式默认值以属性表为准。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 4.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `fast-clk-src` | `int` | **必需**。RTC快速时钟源（RTC Fast Clock Source）：0为 `ESP32_RTC_FAST_CLK_SRC_XTAL_D2`，在C3／S3上将主晶体二分频；ESP32／S2上为 `ESP32_RTC_FAST_CLK_SRC_XTAL_D4`，将主晶体四分频；1为 `ESP32_RTC_FAST_CLK_SRC_RC_FAST`，8MHz。；合法值：`0, 1` |
| `slow-clk-src` | `int` | **必需**。RTC慢速时钟源（RTC Slow Clock Source）。原文列出：0为 `ESP32_RTC_SLOW_CLK_SRC_RC_SLOW`，C3／S3为136kHz、S2为90kHz、ESP32为150kHz；1为 `ESP32_RTC_SLOW_CLK_SRC_XTAL32K`，原文频率写作 `32,768U KHz`；2为 `ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256`，原文写作 `17,5 MHz`；9为 `ESP32_RTC_SLOW_CLK_32K_EXT_OSC`，连接32K_XP引脚的外部32k振荡器。原文以“Default to”引出列表，具体默认值另见属性表。；合法值：`0, 1, 2, 9` |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）中预期的条目数量。；固定值：`1` |

本页没有已弃用的节点专用属性。

## RTC时钟枚举原始对照 1

```text
RTC fast clock source.
- 0: ESP32_RTC_FAST_CLK_SRC_XTAL_D2 - Main XTAL divided by 2 (C3/S3)
ESP32_RTC_FAST_CLK_SRC_XTAL_D4 Main XTAL divided by 4 (ESP32/S2)
- 1: ESP32_RTC_FAST_CLK_SRC_RC_FAST - 8 MHz
```

## RTC时钟枚举原始对照 2

```text
RTC slow clock source. Default to
- 0: ESP32_RTC_SLOW_CLK_SRC_RC_SLOW - 136 KHz (C3/S3) - 90 kHz (S2) - 150 kHz (ESP32)
- 1: ESP32_RTC_SLOW_CLK_SRC_XTAL32K - 32,768U KHz
- 2: ESP32_RTC_SLOW_CLK_SRC_RC_FAST_D256 - 17,5 MHz
- 9: ESP32_RTC_SLOW_CLK_32K_EXT_OSC - External 32k oscillator connected to 32K_XP pin
```

<a id="specifier-cell-names"></a>

## 说明符单元名称

clock cells：`offset`。依次为偏移或总线掩码地址。

---

[上一章](P003_elan_em32-apb.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P005_focaltech_ft9001-cpm.md)
