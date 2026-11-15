---
id: learning.zephyr-docs.timer_reference.clockbind-115
title: Alif时钟多路复用绑定
kind: reference
status: maintained
domains: [zephyr, timer_reference]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/alif,clock-mux.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第115章\_Alif时钟多路复用绑定

<a id="dtbinding-alif-clock-mux"></a>

原文：[alif,clock-mux](https://docs.zephyrproject.org/latest/build/dts/api/bindings/clock/alif,clock-mux.html)。读取日期：2026-10-13，`latest`。

`alif,clock-mux`是Alif Semiconductor的设备树绑定（Devicetree Binding）。

它描述 Alif 时钟源多路复用器（Clock Source Multiplexer）当前切换到的输入。**节点自身没有寄存器**；它记录选择结果，使使用多路复用器输出的设备能够确定时钟频率。**除非驱动会根据此记录编程多路复用器，否则记录必须与硬件实际状态一致**。

第一个使用者是`S32K_CLK`多路复用器，它在`LFRC`与`LFXO`振荡器（Oscillator）之间选择，配置在 Zephyr 之外完成。例如，某开发板的`S32K_CLK`来自`LFXO`时，使用以下记录：

```dts
    &clk_s32k {
            clocks = <&clk_lfxo>;
    };
```

采用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=alif,clock-mux)。

属性类型：`int`为整数，`boolean`为布尔属性，`string`为字符串，`string-array`为字符串数组，`array`为数值数组，`compound`为复合类型；`phandle`为节点引用（Phandle），`phandles`为节点引用列表，`phandle-array`为节点引用与说明符单元数组。

## 115.1\_节点专用属性

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

## 115.2\_基础属性

以下属性继承自基础绑定（Base Binding），是可用于许多节点的通用定义，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clocks` | `phandle-array` | **必需**。多路复用器当前切换到的输入（Selected Input） |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |


---

[上一章：Infineon振荡器时钟绑定](P114_Infineon振荡器时钟绑定.md) · [下一章：nRF时钟控制示例](P116_nRF时钟控制示例.md) · [返回大纲](大纲.md)
