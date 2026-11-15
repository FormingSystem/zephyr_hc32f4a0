---
id: learning.zephyr-docs.timer_reference.clockbind-113
title: Infineon固定比例时钟绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/infineon,fixed-factor-clock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第113章\_Infineon固定比例时钟绑定

<a id="dtbinding-infineon-fixed-factor-clock"></a>

原文：[infineon,fixed-factor-clock](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/infineon,fixed-factor-clock.html)。读取日期：2026-10-13，`latest`。

`infineon,fixed-factor-clock`是Infineon Technologies的设备树绑定（Devicetree Binding）。

原页将其描述为通用固定频率时钟提供者（Generic Fixed-rate Clock Provider）。

驱动源码：[`drivers/clock_control/clock_control_infineon_fixed_factor_clock.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/clock_control/clock_control_infineon_fixed_factor_clock.c)。

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,fixed-factor-clock)。

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

## 113.1\_节点专用属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `system-clock` | `int` | **必需**。时钟类型（Clock Type），参考原文路径`include/.../dt-bindings/clock/ifx_clock_source_common.h`；原始类型对应示例见下文 |
| `instance` | `int` | **必需**。给定时钟类型的实例（Instance），原始对应示例见下文 |
| `source-path` | `int` | 指示源时钟的路径（Source Clock Path） |
| `clock-div` | `int` | 固定时钟分频系数（Fixed Clock Divider） |
| `clock-mult` | `int` | 固定时钟倍频系数（Fixed Clock Multiplier） |
| `#clock-cells` | `int` | **必需**。时钟说明符（Clock Specifier）所需的单元数量；固定值：`0` |

本页没有已弃用的节点专用属性。

时钟类型原例中的头文件路径含省略号，按原文保留；对应关系如下：

```text
path_mux5 : system-clock = <IFX_PATHMUX>
clk_hf0   : system-clock = <IFX_HF>
```

给定时钟类型的实例编号原例：

```text
path_mux5 : instance = <5>
clk_hf0   : instance = <0>
```

## 113.2\_基础属性

以下属性继承自基础绑定（Base Binding），是可用于许多节点的通用定义，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clocks` | `phandle-array` | 输入时钟源（Input Clock Source） |


---

[上一章：Infineon固定时钟绑定](P112_Infineon固定时钟绑定.md) · [下一章：Infineon振荡器时钟绑定](P114_Infineon振荡器时钟绑定.md) · [返回大纲](大纲.md)
