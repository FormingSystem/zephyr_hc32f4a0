---
id: learning.zephyr-docs.hardware.mfdifx-4
title: Infineon高性能可编程模拟子系统绑定
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,hppass-analog.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第724章\_Infineon高性能可编程模拟子系统绑定

<a id="dtbinding-infineon-hppass-analog"></a>

原文：[infineon,hppass-analog](https://docs.zephyrproject.org/latest/build/dts/api/bindings/mfd/infineon,hppass-analog.html)。读取日期：2026-10-13，`latest`。

`infineon,hppass-analog` 是Infineon Technologies的设备树绑定（Devicetree Binding），属于多功能设备（Multi-Function Device，MFD）目录，描述高性能可编程模拟子系统（High Performance Programmable Analog Sub-System，HPPASS），包含SAR ADC和CSG等模拟外设，由自主控制器（Autonomous Controller，AC）状态机协调。本MFD设备管理子系统初始化、AC生命周期（Lifecycle）、状态转换表（State Transition Table，STT）及合并的MCPASS中断，后者覆盖AC状态和错误条件。MCPASS保留原中断标识。各SAR ADC、CSG外设表示为子节点，并各自拥有独立中断线。

本页SAR ADC指逐次逼近寄存器型模数转换器（Successive Approximation Register Analog-to-Digital Converter），CSG指比较器斜坡发生器（Comparator Slope Generator），DAC指数模转换器（Digital-to-Analog Converter），GPIO指通用输入输出（General-Purpose Input/Output），MUX指多路复用器（Multiplexer）。CSG的重复功能单元称为切片（Slice）。

驱动为 [`drivers/mfd/mfd_infineon_hppass.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mfd/mfd_infineon_hppass.c)。

使用此兼容字符串的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=infineon,hppass-analog)。

## 724.1\_原始设备树示例

以下完整保留官方设备树源码（Devicetree Source，DTS）示例。

译注：示例中的配置宏按[官方HPPASS头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/mfd/infineon-hppass.h)说明如下。

| 配置宏 | 含义 |
| --- | --- |
| `IFX_HPPASS_AC_COND_BLOCK_READY` | 已启用的SAR／CSG功能块就绪 |
| `IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE` | SAR组0完成 |
| `IFX_HPPASS_AC_COND_FALSE` | 恒假条件（False） |
| `IFX_HPPASS_AC_ACTION_WAIT_FOR` | 等待条件为真（Wait For） |
| `IFX_HPPASS_AC_ACTION_STOP` | 停止AC（Stop） |
| `IFX_HPPASS_SAR_GRP_0` | SAR组0触发掩码 |
| `IFX_HPPASS_TR_FW_PULSE` | 固件脉冲触发（Firmware Pulse Trigger） |

常量来自 `dt-bindings/mfd/infineon-hppass.h`。基本模式省略 `ac-states`，驱动自动生成2状态SAR启动序列并自动识别SAR子节点。高级示例有3个状态：等待功能块就绪并启用SAR；触发SAR组0、等待完成并循环到状态1；停止。

```dts
#include <dt-bindings/mfd/infineon-hppass.h>

/* Basic mode: no ac-states property.
 * Driver auto-generates 2-state SAR startup sequence.
 */
&hppass_analog0 {
    status = "okay";
    /* SAR child auto-detected, no AC config needed */
};
```

```dts
#include <dt-bindings/mfd/infineon-hppass.h>

/*
 * Advanced mode: custom 3-state sequence.
 * State 0: Wait for blocks ready, enable SAR
 * State 1: Trigger SAR group 0, wait for done, loop to 1
 * State 2: Stop
 */

/ {
    hppass_state0: hppass-ac-state-0 {
        compatible = "infineon,hppass-ac-state";
        ac-condition = <IFX_HPPASS_AC_COND_BLOCK_READY>;
        ac-action = <IFX_HPPASS_AC_ACTION_WAIT_FOR>;
        sar-unlock = <1>;
        sar-enable = <1>;
    };

    hppass_state1: hppass-ac-state-1 {
        compatible = "infineon,hppass-ac-state";
        ac-condition = <IFX_HPPASS_AC_COND_SAR_GROUP_0_DONE>;
        ac-action = <IFX_HPPASS_AC_ACTION_WAIT_FOR>;
        branch-state-idx = <1>;
        sar-unlock = <1>;
        sar-enable = <1>;
        sar-grp-msk = <IFX_HPPASS_SAR_GRP_0>;
    };

    hppass_state2: hppass-ac-state-2 {
        compatible = "infineon,hppass-ac-state";
        ac-condition = <IFX_HPPASS_AC_COND_FALSE>;
        ac-action = <IFX_HPPASS_AC_ACTION_STOP>;
    };
};

&hppass_analog0 {
    ac-states = <&hppass_state0 &hppass_state1 &hppass_state2>;
    startup-clk-div = <4>;
    trig-in-0-type = <IFX_HPPASS_TR_FW_PULSE>;
};
```

## 724.2\_控制器与启动时序

本页 `int` 为整数，`boolean` 为布尔属性，`array` 为数值数组，`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明单元数组。标为0或1的 `int` 属性仍应使用数值单元，不等同于无值的布尔属性。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `ac-states` | `phandles` | 高级模式的有序AC状态节点引用列表，驱动据此构建完整STT；各被引用节点必须具有兼容字符串 `infineon,hppass-ac-state`。省略时使用内建2状态启动序列（基本模式），并按子节点状态自动填入SAR／CSG字段 |
| `ac-gpio-out-en-msk` | `int` | AC的GPIO输出使能掩码，使用 `dt-bindings/mfd/infineon-hppass.h` 中的 `IFX_HPPASS_GPIO_OUT_*` 常量，为AC状态机控制启用GPIO输出；默认值：`0` |
| `startup-clk-div` | `int` | 启动时钟分频值（Startup Clock Divider），范围1至256；将HPPASS时钟分频后供启动序列发生器使用；默认值：`1` |
| `startup-0-count` | `int` | 启动阶段0的计数值，以HPPASS时钟周期为单位，范围0至255；实际周期数为计数值加1；默认值：`0` |
| `startup-0-sar` | `int` | 启动阶段0的SAR使能标志，取0或1；默认值：`0` |
| `startup-0-csg-chan` | `int` | 启动阶段0的CSG通道使能标志，取0或1；默认值：`0` |
| `startup-0-csg-slice` | `int` | 启动阶段0的CSG切片（Slice）使能标志，取0或1；默认值：`0` |
| `startup-0-csg-ready` | `int` | 启动阶段0的CSG自动调零／比较器门控（Auto-Zero/Comparator Gate）使能标志，取0或1；默认值：`0` |
| `startup-1-count` | `int` | 启动阶段1的计数值，以HPPASS时钟周期为单位，范围0至255；默认值：`0` |
| `startup-1-sar` | `int` | 启动阶段1的SAR使能标志，取0或1；默认值：`0` |
| `startup-1-csg-chan` | `int` | 启动阶段1的CSG通道使能标志，取0或1；默认值：`0` |
| `startup-1-csg-slice` | `int` | 启动阶段1的CSG切片（Slice）使能标志，取0或1；默认值：`0` |
| `startup-1-csg-ready` | `int` | 启动阶段1的CSG自动调零／比较器门控（Auto-Zero/Comparator Gate）使能标志，取0或1；默认值：`0` |
| `startup-2-count` | `int` | 启动阶段2的计数值，以HPPASS时钟周期为单位，范围0至255；默认值：`0` |
| `startup-2-sar` | `int` | 启动阶段2的SAR使能标志，取0或1；默认值：`0` |
| `startup-2-csg-chan` | `int` | 启动阶段2的CSG通道使能标志，取0或1；默认值：`0` |
| `startup-2-csg-slice` | `int` | 启动阶段2的CSG切片（Slice）使能标志，取0或1；默认值：`0` |
| `startup-2-csg-ready` | `int` | 启动阶段2的CSG自动调零／比较器门控（Auto-Zero/Comparator Gate）使能标志，取0或1；默认值：`0` |
| `startup-3-count` | `int` | 启动阶段3的计数值，以HPPASS时钟周期为单位，范围0至255；默认值：`0` |
| `startup-3-sar` | `int` | 启动阶段3的SAR使能标志，取0或1；默认值：`0` |
| `startup-3-csg-chan` | `int` | 启动阶段3的CSG通道使能标志，取0或1；默认值：`0` |
| `startup-3-csg-slice` | `int` | 启动阶段3的CSG切片（Slice）使能标志，取0或1；默认值：`0` |
| `startup-3-csg-ready` | `int` | 启动阶段3的CSG自动调零／比较器门控（Auto-Zero/Comparator Gate）使能标志，取0或1；默认值：`0` |

## 724.3\_触发输入

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `trig-in-0-type` | `int` | 触发输入（Trigger Input）0的类型，使用 `IFX_HPPASS_TR_*` 常量；默认DISABLED（禁用，0）；默认值：`0` |
| `trig-in-0-hw-mode` | `int` | 触发输入0的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；仅在 `trig-in-0-type` 为 `HW_A` 或 `HW_B` 时有效；默认值：`0` |
| `trig-in-1-type` | `int` | 触发输入（Trigger Input）1的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-1-hw-mode` | `int` | 触发输入1的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-2-type` | `int` | 触发输入（Trigger Input）2的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-2-hw-mode` | `int` | 触发输入2的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-3-type` | `int` | 触发输入（Trigger Input）3的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-3-hw-mode` | `int` | 触发输入3的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-4-type` | `int` | 触发输入（Trigger Input）4的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-4-hw-mode` | `int` | 触发输入4的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-5-type` | `int` | 触发输入（Trigger Input）5的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-5-hw-mode` | `int` | 触发输入5的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-6-type` | `int` | 触发输入（Trigger Input）6的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-6-hw-mode` | `int` | 触发输入6的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |
| `trig-in-7-type` | `int` | 触发输入（Trigger Input）7的类型，使用 `IFX_HPPASS_TR_*` 常量；默认值：`0` |
| `trig-in-7-hw-mode` | `int` | 触发输入7的硬件模式（Hardware Mode），使用 `IFX_HPPASS_TR_HW_*` 常量；默认值：`0` |

## 724.4\_脉冲触发输出

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `trig-pulse-0` | `int` | 触发输出（Trigger Output）0的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认DISABLED（禁用，0）；默认值：`0` |
| `trig-pulse-1` | `int` | 触发输出（Trigger Output）1的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-2` | `int` | 触发输出（Trigger Output）2的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-3` | `int` | 触发输出（Trigger Output）3的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-4` | `int` | 触发输出（Trigger Output）4的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-5` | `int` | 触发输出（Trigger Output）5的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-6` | `int` | 触发输出（Trigger Output）6的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |
| `trig-pulse-7` | `int` | 触发输出（Trigger Output）7的脉冲源，使用 `IFX_HPPASS_TR_OUT_*` 常量；默认值：`0` |

## 724.5\_电平触发输出

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `trig-level-0-sync-bypass` | `int` | 触发输出电平0的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-0-comp-msk` | `int` | 触发输出电平0的CSG比较器掩码；共5位，每个CSG切片对应一位；默认值：`0` |
| `trig-level-0-limit-msk` | `int` | 触发输出电平0的SAR限值检测器（Limit Detector）掩码；共8位；默认值：`0` |
| `trig-level-1-sync-bypass` | `int` | 触发输出电平1的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-1-comp-msk` | `int` | 触发输出电平1的CSG比较器掩码；默认值：`0` |
| `trig-level-1-limit-msk` | `int` | 触发输出电平1的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-2-sync-bypass` | `int` | 触发输出电平2的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-2-comp-msk` | `int` | 触发输出电平2的CSG比较器掩码；默认值：`0` |
| `trig-level-2-limit-msk` | `int` | 触发输出电平2的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-3-sync-bypass` | `int` | 触发输出电平3的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-3-comp-msk` | `int` | 触发输出电平3的CSG比较器掩码；默认值：`0` |
| `trig-level-3-limit-msk` | `int` | 触发输出电平3的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-4-sync-bypass` | `int` | 触发输出电平4的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-4-comp-msk` | `int` | 触发输出电平4的CSG比较器掩码；默认值：`0` |
| `trig-level-4-limit-msk` | `int` | 触发输出电平4的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-5-sync-bypass` | `int` | 触发输出电平5的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-5-comp-msk` | `int` | 触发输出电平5的CSG比较器掩码；默认值：`0` |
| `trig-level-5-limit-msk` | `int` | 触发输出电平5的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-6-sync-bypass` | `int` | 触发输出电平6的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-6-comp-msk` | `int` | 触发输出电平6的CSG比较器掩码；默认值：`0` |
| `trig-level-6-limit-msk` | `int` | 触发输出电平6的SAR限值检测器（Limit Detector）掩码；默认值：`0` |
| `trig-level-7-sync-bypass` | `int` | 触发输出电平7的同步旁路标志（Sync Bypass Flag），取0或1；默认值：`0` |
| `trig-level-7-comp-msk` | `int` | 触发输出电平7的CSG比较器掩码；默认值：`0` |
| `trig-level-7-limit-msk` | `int` | 触发输出电平7的SAR限值检测器（Limit Detector）掩码；默认值：`0` |

## 724.6\_专用寄存器与中断资源

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `interrupts` | `array` | **必需**。合并的MCPASS中断，涵盖AC状态转换和错误条件 |

没有已弃用的节点专用属性。以下完整保留继承的基础属性，不保证全部适用于本绑定；`compatible` 为必需属性。

## 724.7\_状态、兼容字符串与寄存器

本页 `int` 为整数，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`boolean` 为布尔属性，`compound` 为复合类型。**节点引用（Phandle）**用来指向其他节点；`phandle-array` 表示节点引用及其说明单元，`phandles` 表示节点引用列表。

`status` 的类型为 `string`，描述节点所代表硬件或其他资源的运行状态。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将它视为不存在。合法值为 `okay`、`disabled`、`reserved`、`fail`、`fail-sss`。详见《设备树规范》（Devicetree Specification）v0.4 第 2.3.4 节。

`compatible` 的类型为 `string-array`，是**必需属性**。它用字符串列表定义节点代表的硬件或其他资源类型；设备驱动检查特定兼容字符串，以寻找应由自己管理的节点。推荐格式为 `vendor,device`，其中 `vendor` 是厂商简称，`device` 通常取自数据手册。多个值应按从最具体到最通用排列，使某一通用家族的具体设备能匹配当前可用的最具体驱动。详见规范 v0.4 第 2.3.1 节。

`reg` 的类型为 `array`，是**必需属性**，给出寻址设备所需的信息，其含义取决于设备及 `compatible`。通常是一组“地址、长度”对，每对称为**寄存器块（Register Block）**，数值惯常写成十六进制。详见规范 v0.4 第 2.3.6 节。

`reg-names` 的类型为 `string-array`，为 `reg` 中各寄存器块提供可选名称。以下保留官方示例；`#address-cells` 和 `#size-cells` 分别声明地址与长度使用的 32 位单元数。

```dts
  / {
       soc {
           #address-cells = <1>;
           #size-cells = <1>;

           uart@1000 {
               reg = <0x1000 0x2000>, <0x3000 0x4000>;
               reg-names = "foo", "bar";
           };
       };
  };
```

`uart@1000` 节点有两个寄存器块：名称 `foo` 对应基址 `0x1000`、大小 `0x2000`；名称 `bar` 对应基址 `0x3000`、大小 `0x4000`。这里 uart 是**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**节点名称，示例只是演示寄存器块命名。

## 724.8\_地址映射与中断

`ranges` 的类型为 `compound`，定义总线子地址空间与总线节点父地址空间之间的映射或转换。它通常为空，或由“子总线地址、父总线地址、长度”三元组构成。**空属性表示两侧地址空间相同，不需要转换；总线节点没有此属性时，则认为子节点与父地址空间之间不存在映射。**详见规范 v0.4 第 2.3.8 节。

下列属性描述**中断（Interrupt）**，参见规范 v0.4 第 2.4 节“中断与中断映射”。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `interrupts-extended` | `compound` | 扩展中断说明符，可替代 `interrupts` |
| `interrupt-names` | `string-array` | 设备各中断的可选名称；中断本身在 `interrupts` 或 `interrupts-extended` 中定义 |
| `interrupt-parent` | `phandle` | 若存在，引用负责处理此设备所产生中断的节点 |

## 724.9\_标签、时钟与地址单元

**时钟提供者（Clock Provider）**提供设备使用的时钟。下表同时保留标签和子节点地址编码相关属性。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `clocks` | `phandle-array` | 设备的时钟提供者信息，通常应遵守下述 dt-schema 时钟绑定约定 |
| `clock-names` | `string-array` | `clocks` 中各时钟提供者的可选名称 |
| `#address-cells` | `int` | 固定值：`1`。子节点 `reg` 地址字段所用的 `<u32>` 单元数量 |
| `#size-cells` | `int` | 固定值：`1`。子节点 `reg` 大小字段所用的 `<u32>` 单元数量 |

`<u32>` 是 32 位无符号单元，两个 cells 属性见规范 v0.4 第 2.3.5 节。时钟约定见 [dt-schema 的 clock.yaml](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)。`status`、`compatible`、`reg`、`interrupts` 和 `label` 另见官方[重要属性（Important Properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

## 724.10\_DMA、输入输出与邮箱通道

**直接存储器访问（Direct Memory Access，DMA）**属性描述设备的 DMA 能力、通道和地址映射；输入输出（Input/Output，I/O）及邮箱（Mailbox）属性描述关联通道。IPM 是**处理器间消息（Inter-Processor Messaging）**接口。

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `dma-coherent` | `boolean` | 表示设备支持一致性 DMA 操作，见规范 v0.4 第 2.3.10 节 |
| `dmas` | `phandle-array` | 与设备相关的 DMA 通道说明符 |
| `dma-names` | `string-array` | `dmas` 中各 DMA 通道说明符的可选名称 |
| `dma-ranges` | `compound` | 定义总线物理地址空间与其父总线物理地址空间之间的映射或转换，见规范 v0.4 第 2.3.9 节 |
| `io-channels` | `phandle-array` | 与设备相关的 I/O 通道说明符 |
| `io-channel-names` | `string-array` | `io-channels` 中各通道说明符的可选名称 |
| `mboxes` | `phandle-array` | 与设备相关的邮箱/IPM 通道说明符 |
| `mbox-names` | `string-array` | `mboxes` 中各邮箱说明符的可选名称 |

## 724.11\_电源域与硬件锁

**电源域（Power Domain）**描述设备所属供电域；**硬件自旋锁（Hardware Spinlock）**为硬件提供的锁资源。属性如下：

| 属性 | 类型 | 中文说明 |
| --- | --- | --- |
| `power-domains` | `phandle-array` | 与设备相关的电源域说明符 |
| `power-domain-names` | `string-array` | `power-domains` 中各电源域说明符的可选名称 |
| `#power-domain-cells` | `int` | `power-domains` 属性中的单元数量 |
| `hwlocks` | `phandle-array` | 与设备相关的硬件自旋锁标识 |
| `hwlock-names` | `string-array` | `hwlocks` 中各锁说明符的可选名称 |

## 724.12\_初始化、唤醒和运行时电源管理

`zephyr,deferred-init` 为 `boolean` 属性：启动时不自动初始化设备，应使用 `device_init()` 手动初始化。

`wakeup-source` 为 `boolean` 属性，标识设备可以作为**唤醒源（Wakeup Source）**。提供它后，设备会设置一个专门标志，告知系统该设备具备唤醒系统的能力。这类设备的唤醒功能默认禁用，即其中断不会唤醒系统，必要时可在运行期间启用。

`zephyr,pm-device-runtime-auto` 为 `boolean` 属性，在初始化函数执行后自动为设备配置**运行时电源管理（Runtime Power Management）**。

`zephyr,disabling-power-states` 的类型为 `phandles`，列出会关闭此设备电源的电源状态。

---

[上一章：Infineon可编程阈值比较器绑定](P723_Infineon可编程阈值比较器绑定.md) · [下一章：Infineon高性能模拟控制器状态绑定](P725_Infineon高性能模拟控制器状态绑定.md) · [返回大纲](大纲.md)
