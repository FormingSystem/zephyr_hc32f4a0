---
id: learning.zephyr-docs.hardware.mfdifx-1
title: Infineon自主模拟控制器状态绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-ac-state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第721章\_Infineon自主模拟控制器状态绑定

<a id="dtbinding-infineon-autanalog-ac-state"></a>

原文：[infineon,autanalog-ac-state](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,autanalog-ac-state.html)。读取日期：2026-10-13，`latest`。

`infineon,autanalog-ac-state` 是Infineon Technologies的设备树绑定（Devicetree Binding），属于多功能设备（Multi-Function Device，MFD）目录，描述AutAnalog的自主控制器（Autonomous Controller，AC）状态转换表（State Transition Table，STT）条目。每个节点表示一个AC状态；父AutAnalog设备的 `ac-states` 通过节点引用（Phandle）引用它，列表位置决定状态索引。此绑定覆盖AC、SAR、两个CTB、PTCOMP、两个DAC的STT字段，并在属性中列出PRB控制。所有属性默认0，只需填写该状态相关字段。

本页SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter），DAC指数模转换器（Digital-to-Analog Converter），CTB指连续时间模块（Continuous Time Block），PTCOMP指可编程阈值比较器（Programmable Threshold Comparator），PRB指可编程参考模块（Programmable Reference Block）。通用输入输出（General-Purpose Input/Output，GPIO）与运算放大器（Operational Amplifier，Opamp）相关字段保留原属性名。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,autanalog-ac-state)。

条件、动作、GPIO输出、CTB增益和DAC方向的取值使用 `dt-bindings/mfd/infineon-autanalog.h` 中的常量。

## 721.1\_控制器核心与GPIO

本页 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组。标为0或1的 `int` 属性仍应使用数值单元，不等同于无值的布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ac-unlock` | `int` | AC解锁标志（Unlock Flag），取0或1；为1时允许在本状态修改AC配置；默认值：`0` |
| `ac-lp-mode` | `int` | 低功耗模式（Low-Power Mode）标志，取0或1；为1时子系统在本状态进入低功耗模式；默认值：`0` |
| `ac-condition` | `int` | AC条件编码（Condition Code），使用 `dt-bindings/mfd/infineon-autanalog.h` 中的 `IFX_AUTANALOG_AC_COND_*` 常量；默认FALSE（假，0）；默认值：`0` |
| `ac-action` | `int` | AC动作编码（Action Code），使用 `dt-bindings/mfd/infineon-autanalog.h` 中的 `IFX_AUTANALOG_AC_ACTION_*` 常量；默认STOP（停止，0）；默认值：`0` |
| `branch-state` | `int` | `ac-states` 列表中的分支目标状态索引，范围0至63；动作是 `BRANCH_*` 或 `WAIT_FOR` 类型时使用；默认值：`0` |
| `ac-trig-int` | `int` | 中断触发标志，取0或1；为1时AC在进入本状态时产生中断；默认值：`0` |
| `ac-count` | `int` | 重复计数值，范围0至4095；实际重复次数为配置值加1；默认值：`0` |
| `ac-unlock-gpio-out` | `int` | GPIO输出解锁标志，取0或1；默认值：`0` |
| `ac-gpio-out` | `int` | GPIO输出掩码（Output Mask），使用 `dt-bindings/mfd/infineon-autanalog.h` 中的 `IFX_AUTANALOG_AC_GPIO_OUT_*` 常量。多个输出可按位或（Bitwise OR）组合，例如 `OUT0` 与 `OUT1` 按位或得到 `0x3`；默认值：`0` |

## 721.2\_SAR与参考电压

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sar-unlock` | `int` | SAR解锁标志，取0或1；为1时在本状态解锁SAR配置；默认值：`0` |
| `sar-enable` | `int` | SAR使能标志，取0或1；为1时在本状态启用SAR；默认值：`0` |
| `sar-trigger` | `int` | SAR触发标志，取0或1；为1时在本状态触发SAR转换；默认值：`0` |
| `sar-entry-state` | `int` | SAR入口状态索引，范围0至31；选择本AC状态对应的SAR序列发生器（Sequencer）入口；默认值：`0` |
| `prb-unlock` | `int` | PRB解锁标志，取0或1；为1时下列PRB参考电压字段在本状态生效；默认值：`0` |
| `prb-vref0-fw` | `int` | PRB参考电压Vref0的固件控制标志，取0或1；为0时输出由下列 `prb-vref0-tap` 决定，为1时由静态配置（Static Configuration）中的抽头决定；默认值：`0` |
| `prb-vref0-tap` | `int` | PRB参考电压Vref0的抽头选择器（Tap Selector），范围0至15；选择本状态下的电阻分压抽头；默认值：`0` |
| `prb-vref1-fw` | `int` | PRB参考电压Vref1的固件控制标志，取0或1；为0时输出由下列 `prb-vref1-tap` 决定，为1时由静态配置（Static Configuration）中的抽头决定；默认值：`0` |
| `prb-vref1-tap` | `int` | PRB参考电压Vref1的抽头选择器（Tap Selector），范围0至15；选择本状态下的电阻分压抽头；默认值：`0` |

## 721.3\_运算放大器

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ctb0-unlock` | `int` | CTB0解锁标志，取0或1；为1时下列运算放大器字段在本状态生效；默认值：`0` |
| `ctb0-enable-opamp0` | `int` | CTB0中Opamp0的使能标志，取0或1；默认值：`0` |
| `ctb0-cfg-opamp0` | `int` | CTB0中Opamp0的动态配置选择器（Dynamic Configuration Selector），范围0至7；从CTB动态配置表中选择；默认值：`0` |
| `ctb0-gain-opamp0` | `int` | CTB0中Opamp0的增益（Gain），使用 `IFX_AUTANALOG_CTB_OA_GAIN_*` 常量；默认值：`0` |
| `ctb0-enable-opamp1` | `int` | CTB0中Opamp1的使能标志，取0或1；默认值：`0` |
| `ctb0-cfg-opamp1` | `int` | CTB0中Opamp1的动态配置选择器（Dynamic Configuration Selector），范围0至7；默认值：`0` |
| `ctb0-gain-opamp1` | `int` | CTB0中Opamp1的增益（Gain），使用 `IFX_AUTANALOG_CTB_OA_GAIN_*` 常量；默认值：`0` |
| `ctb1-unlock` | `int` | CTB1解锁标志，取0或1；为1时下列运算放大器字段在本状态生效；默认值：`0` |
| `ctb1-enable-opamp0` | `int` | CTB1中Opamp0的使能标志，取0或1；默认值：`0` |
| `ctb1-cfg-opamp0` | `int` | CTB1中Opamp0的动态配置选择器（Dynamic Configuration Selector），范围0至7；默认值：`0` |
| `ctb1-gain-opamp0` | `int` | CTB1中Opamp0的增益（Gain），使用 `IFX_AUTANALOG_CTB_OA_GAIN_*` 常量；默认值：`0` |
| `ctb1-enable-opamp1` | `int` | CTB1中Opamp1的使能标志，取0或1；默认值：`0` |
| `ctb1-cfg-opamp1` | `int` | CTB1中Opamp1的动态配置选择器（Dynamic Configuration Selector），范围0至7；默认值：`0` |
| `ctb1-gain-opamp1` | `int` | CTB1中Opamp1的增益（Gain），使用 `IFX_AUTANALOG_CTB_OA_GAIN_*` 常量；默认值：`0` |

## 721.4\_阈值比较器

PTCOMP0是本绑定使用的可编程阈值比较器实例标识，Comp0／Comp1是其中两个比较器。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ptcomp0-unlock` | `int` | PTCOMP0解锁标志，取0或1；为1时下列比较器字段在本状态生效；默认值：`0` |
| `ptcomp0-enable-comp0` | `int` | PTCOMP0中Comp0的使能标志，取0或1；默认值：`0` |
| `ptcomp0-dyn-cfg-idx-comp0` | `int` | PTCOMP0中Comp0的动态配置选择器，范围0至7；默认值：`0` |
| `ptcomp0-enable-comp1` | `int` | PTCOMP0中Comp1的使能标志，取0或1；默认值：`0` |
| `ptcomp0-dyn-cfg-idx-comp1` | `int` | PTCOMP0中Comp1的动态配置选择器，范围0至7；默认值：`0` |

## 721.5\_数模转换器

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `dac0-unlock` | `int` | DAC0解锁标志，取0或1；为1时下列DAC0字段在本状态生效；默认值：`0` |
| `dac0-enable` | `int` | DAC0使能标志，取0或1；默认值：`0` |
| `dac0-trigger` | `int` | DAC0触发标志，取0或1；默认值：`0` |
| `dac0-channel` | `int` | DAC0通道选择器（Channel Selector）；默认值：`0` |
| `dac0-direction` | `int` | DAC0方向（Direction），使用 `IFX_AUTANALOG_DAC_DIR_*` 常量；默认值：`0` |
| `dac1-unlock` | `int` | DAC1解锁标志，取0或1；为1时下列DAC1字段在本状态生效；默认值：`0` |
| `dac1-enable` | `int` | DAC1使能标志，取0或1；默认值：`0` |
| `dac1-trigger` | `int` | DAC1触发标志，取0或1；默认值：`0` |
| `dac1-channel` | `int` | DAC1通道选择器（Channel Selector）；默认值：`0` |
| `dac1-direction` | `int` | DAC1方向（Direction），使用 `IFX_AUTANALOG_DAC_DIR_*` 常量；默认值：`0` |

原页未列出已弃用的节点专用属性，也没有继承的基础属性。



---

[上一章：Infineon自主模拟子系统绑定](P720_Infineon自主模拟子系统绑定.md) · [下一章：Infineon连续时间模块绑定](P722_Infineon连续时间模块绑定.md) · [返回大纲](大纲.md)
