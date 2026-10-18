---
id: learning.zephyr-docs.hardware.mfdifx-5
title: Infineon高性能模拟控制器状态绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,hppass-ac-state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第725章\_Infineon高性能模拟控制器状态绑定

<a id="dtbinding-infineon-hppass-ac-state"></a>

原文：[infineon,hppass-ac-state](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,hppass-ac-state.html)。读取日期：2026-10-13，`latest`。

`infineon,hppass-ac-state` 是Infineon Technologies的设备树绑定（Devicetree Binding），属于多功能设备（Multi-Function Device，MFD）目录，描述高性能可编程模拟子系统（High Performance Programmable Analog Sub-System，HPPASS）的自主控制器（Autonomous Controller，AC）状态转换表（State Transition Table，STT）条目。每个节点表示一个AC状态；父HPPASS设备的 `ac-states` 通过节点引用（Phandle）引用它，列表位置决定状态索引。本绑定覆盖AC内核、GPIO输出、5个CSG切片、SAR以及4路SAR MUX的全部STT字段。所有属性默认0，只需填写该状态相关字段。

本页SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter），CSG指比较器斜坡发生器（Comparator Slope Generator），DAC指数模转换器（Digital-to-Analog Converter），GPIO指通用输入输出（General-Purpose Input/Output），MUX指多路复用器（Multiplexer）。CSG的重复功能单元称为切片（Slice）。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,hppass-ac-state)。

条件、动作、GPIO输出和SAR组掩码的取值使用 `dt-bindings/mfd/infineon-hppass.h` 中的常量。

## 725.1\_控制器核心与GPIO

本页 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组。标为0或1的 `int` 属性仍应使用数值单元，不等同于无值的布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ac-condition` | `int` | AC条件编码，使用 `dt-bindings/mfd/infineon-hppass.h` 中的 `IFX_HPPASS_AC_COND_*` 常量；默认FALSE（假，0）；默认值：`0` |
| `ac-action` | `int` | AC动作编码，使用 `dt-bindings/mfd/infineon-hppass.h` 中的 `IFX_HPPASS_AC_ACTION_*` 常量；默认STOP（停止，0）；默认值：`0` |
| `branch-state-idx` | `int` | `ac-states` 列表内的分支目标状态索引，范围0至15；动作是 `BRANCH_IF_TRUE` 或 `BRANCH_IF_FALSE` 时使用；默认值：`0` |
| `ac-interrupt` | `int` | 中断／触发标志，取0或1；为1时，在进入本状态时产生脉冲触发或中央处理器（Central Processing Unit，CPU）中断；对于 `WAIT_FOR` 动作，在等待条件满足后产生；默认值：`0` |
| `ac-count` | `int` | 定时器／计数器（Timer/Counter）数值，启用时范围1至4096。对于 `WAIT_FOR` 动作，它是间隔定时器；对于 `BRANCH_IF_*` 动作，它是循环计数器；值为0时禁用本状态的定时器／计数器；默认值：`0` |
| `gpio-out-unlock` | `int` | GPIO输出解锁标志，取0或1；为1时在本状态应用GPIO输出掩码；默认值：`0` |
| `gpio-out-msk` | `int` | GPIO输出掩码，使用 `dt-bindings/mfd/infineon-hppass.h` 中的 `IFX_HPPASS_GPIO_OUT_*` 常量；多个输出可按位或（Bitwise OR）组合，例如 `GPIO_OUT_0` 与 `GPIO_OUT_1`；默认值：`0` |

## 725.2\_CSG切片

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `csg0-unlock` | `int` | CSG切片0的解锁标志，取0或1；默认值：`0` |
| `csg0-enable` | `int` | CSG切片0的使能标志，取0或1；要求 `csg0-unlock = 1`；默认值：`0` |
| `csg0-dac-trig` | `int` | CSG切片0的DAC启动／更新触发标志，取0或1；默认值：`0` |
| `csg1-unlock` | `int` | CSG切片1的解锁标志，取0或1；默认值：`0` |
| `csg1-enable` | `int` | CSG切片1的使能标志，取0或1；要求 `csg1-unlock = 1`；默认值：`0` |
| `csg1-dac-trig` | `int` | CSG切片1的DAC启动／更新触发标志，取0或1；默认值：`0` |
| `csg2-unlock` | `int` | CSG切片2的解锁标志，取0或1；默认值：`0` |
| `csg2-enable` | `int` | CSG切片2的使能标志，取0或1；要求 `csg2-unlock = 1`；默认值：`0` |
| `csg2-dac-trig` | `int` | CSG切片2的DAC启动／更新触发标志，取0或1；默认值：`0` |
| `csg3-unlock` | `int` | CSG切片3的解锁标志，取0或1；默认值：`0` |
| `csg3-enable` | `int` | CSG切片3的使能标志，取0或1；要求 `csg3-unlock = 1`；默认值：`0` |
| `csg3-dac-trig` | `int` | CSG切片3的DAC启动／更新触发标志，取0或1；默认值：`0` |
| `csg4-unlock` | `int` | CSG切片4的解锁标志，取0或1；默认值：`0` |
| `csg4-enable` | `int` | CSG切片4的使能标志，取0或1；要求 `csg4-unlock = 1`；默认值：`0` |
| `csg4-dac-trig` | `int` | CSG切片4的DAC启动／更新触发标志，取0或1；默认值：`0` |

## 725.3\_SAR与多路复用采样器

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sar-unlock` | `int` | SAR解锁标志，取0或1；为1时在本状态应用SAR使能状态；默认值：`0` |
| `sar-enable` | `int` | SAR使能标志，取0或1；要求 `sar-unlock = 1`，通常与 `WAIT_FOR` 动作及 `BLOCK_READY` 条件配合使用；默认值：`0` |
| `sar-grp-msk` | `int` | SAR序列发生器的组触发掩码，使用 `dt-bindings/mfd/infineon-hppass.h` 中的 `IFX_HPPASS_SAR_GRP_*` 常量，可按位或组合多个组；仅当SAR已启用且SAR组触发源设为AC时有效；默认值：`0` |
| `sar-mux0-unlock` | `int` | SAR多路复用采样器（MUX Sampler）0的解锁标志，取0或1；默认值：`0` |
| `sar-mux0-chan-idx` | `int` | SAR多路复用采样器0的通道选择，范围0至3；默认值：`0` |
| `sar-mux1-unlock` | `int` | SAR多路复用采样器（MUX Sampler）1的解锁标志，取0或1；默认值：`0` |
| `sar-mux1-chan-idx` | `int` | SAR多路复用采样器1的通道选择，范围0至3；默认值：`0` |
| `sar-mux2-unlock` | `int` | SAR多路复用采样器（MUX Sampler）2的解锁标志，取0或1；默认值：`0` |
| `sar-mux2-chan-idx` | `int` | SAR多路复用采样器2的通道选择，范围0至3；默认值：`0` |
| `sar-mux3-unlock` | `int` | SAR多路复用采样器（MUX Sampler）3的解锁标志，取0或1；默认值：`0` |
| `sar-mux3-chan-idx` | `int` | SAR多路复用采样器3的通道选择，范围0至3；默认值：`0` |

原页未列出已弃用的节点专用属性，也没有继承的基础属性。



---

[上一章：Infineon高性能可编程模拟子系统绑定](P724_Infineon高性能可编程模拟子系统绑定.md) · [下一章：Infineon斜坡发生器绑定](P726_Infineon斜坡发生器绑定.md) · [返回大纲](大纲.md)
