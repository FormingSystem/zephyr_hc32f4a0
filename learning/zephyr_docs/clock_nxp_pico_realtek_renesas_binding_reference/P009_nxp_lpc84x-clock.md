---
id: learning.zephyr-docs.clock-nxp-pico-realtek-renesas-binding-reference.page-9
title: nxp_lpc84x-clock
kind: reference
status: maintained
domains: [zephyr, devicetree, clock]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,lpc84x-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第9章\_nxp_lpc84x-clock

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/nxp,lpc84x-clock.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nxp-lpc84x-clock"></a>
<a id="dtbinding-nxp-lpc84x-clock"></a>
<a id="std-dtcompatible-nxp-lpc84x-clock"></a>

兼容字符串（Compatible String）：`nxp,lpc84x-clock`。厂商：[ NXP Semiconductors ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nxp)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nxp,lpc84x-clock)。

驱动源码（Driver Source）：[drivers/clock_control/clock_control_lpc84x.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_lpc84x.c)。

<a id="description"></a>

NXP LPC84x时钟控制器（Clock Controller）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 9.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `enable-fro` | `boolean` | 为自由运行振荡器（Free-running Oscillator，FRO）上电。 |
| `enable-froout` | `boolean` | 为FRO输出上电（Power Up）。 |
| `fro-freq` | `string` | FRO振荡器输出频率（Output Frequency）：18M为18MHz，24M为24MHz，30M为30MHz。；默认值：`24M`；合法值：`18M, 24M, 30M` |
| `enable-sysosc` | `boolean` | 为系统晶体振荡器（System Crystal Oscillator，SYSOSC）上电。 |
| `extclk-src` | `string` | 外部时钟源（External Clock Source）：sysosc为系统振荡器，clkin为外部时钟输入。；默认值：`sysosc`；合法值：`sysosc, clkin` |
| `fro-low-power-boot` | `boolean` | 启用FRO低功耗启动（Low Power Boot）。 |
| `sysosc-freq` | `int` | 系统振荡器频率（System Oscillator Frequency），单位Hz；enable-sysosc为真时必需。 |
| `extclk-freq` | `int` | 外部时钟频率（External Clock Frequency），单位Hz；使用extclk-clkin时必需。 |
| `ahb-clk-divider` | `int` | AHB时钟分频器（Clock Divider）。；默认值：`1` |
| `mainclk-src` | `string` | 主时钟源（Main Clock Source）：fro为FRO振荡器，extclk为外部时钟，wdosc为看门狗振荡器，frodiv为FRO分频时钟。；默认值：`fro`；合法值：`fro, extclk, wdosc, frodiv` |
| `frg0-clk-src` | `string` | FRG0时钟源（Clock Source）：fro为FRO振荡器，mainclk为主时钟。；合法值：`fro, mainclk` |
| `frg0-mult` | `int` | FRG0倍频系数（Multiplier），范围0～255。 |
| `frg1-clk-src` | `string` | FRG1时钟源（Clock Source）：fro为FRO振荡器，mainclk为主时钟。；合法值：`fro, mainclk` |
| `frg1-mult` | `int` | FRG1倍频系数（Multiplier），范围0～255。 |

本页没有已弃用的节点专用属性。

## 9.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。SYSCON寄存器基址与大小（Register Base Address and Size）。 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

<a id="specifier-cell-names"></a>

## 说明符单元名称

clock cells：`name`。依次为时钟标识。

---

[上一章](P008_nxp_lpc11u6x-syscon.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P010_nxp_mc-cgm.md)
