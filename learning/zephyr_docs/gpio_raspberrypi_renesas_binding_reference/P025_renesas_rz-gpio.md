---
id: learning.zephyr-docs.gpio-raspberrypi-renesas-binding-reference.page-25
title: renesas_rz-gpio
kind: reference
status: maintained
domains: [zephyr, devicetree, gpio]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/gpio/renesas,rz-gpio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第25章\_renesas_rz-gpio

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/gpio/renesas,rz-gpio.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="renesas-rz-gpio"></a>
<a id="dtbinding-renesas-rz-gpio"></a>
<a id="std-dtcompatible-renesas-rz-gpio"></a>

兼容字符串（Compatible String）：`renesas,rz-gpio`。厂商：[ Renesas Electronics Corporation ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-renesas)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=renesas,rz-gpio)。

驱动源码（Driver Source）：[drivers/gpio/gpio_renesas_rz.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/gpio/gpio_renesas_rz.c)。

<a id="description"></a>

Renesas RZ GPIO控制器。

下方原例为端口8的引脚2配置上拉（Pull-Up），并将其映射至GPIO中断TINT10。

对于RZ/T、RZ/N系列（`gpio-common-v2` 兼容字符串），应以一个 `renesas,rz-ext-irq` 节点替换 `&tint10`，从而把引脚映射至外部中断（External Interrupt）。例如，设置 `irqs = <&irq10 2>` 即把该引脚映射至IRQ10。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 25.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `irqs` | `phandle-array` | 与引脚对应的中断（Interrupt）。 |
| `#gpio-cells` | `int` | **必需**。GPIO说明符（GPIO Specifier）所需的单元数量。；固定值：`2` |
| `gpio-controller` | `boolean` | **必需**。表明此节点为GPIO控制器（GPIO Controller）。 |
| `ngpios` | `int` | 此属性表示GPIO可用槽位中被使用部分的范围。典型情况是硬件寄存器宽32位，但仅18位对应实际引脚。驱动通常允许全部32位，同一IP可在不同设计中使用32、18或12位。设置 `ngpios = <18>;` 表示只使用局部偏移0～17的前18个GPIO。若槽位范围存在空洞（Holes），此值应为最大槽位编号加1。；默认值：`32` |
| `gpio-reserved-ranges` | `array` | 当 `ngpios = <N>` 的偏移0～N−1中并非全部GPIO可用时，此属性用额外的元组（Tuples）声明不可用范围的起始偏移和长度。例如 `gpio-reserved-ranges = <3 2>, <10 1>;` 表示GPIO偏移3、4、10不可用，即使ngpios为18也一样。 |
| `gpio-line-names` | `string-array` | 字符串数组（String Array），定义从GPIO控制器引出的各信号线名称（GPIO Line Names）。 |

本页没有已弃用的节点专用属性。

## 25.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `reg` | `array` | **必需**。GPIO端口编号（Port Number）。 |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `gpio-hog` | `boolean` | **必需**。表明此节点为GPIO自动占用节点（GPIO Hog）。 |
| `gpios` | `array` | **必需**。需要由Hog自动占用的GPIO说明符数组（GPIO Specifier Array），例如pin和flags。数组元素数必须是父GPIO控制器说明符单元数的整数倍。 |
| `input` | `boolean` | 设置此属性会将GPIO配置为输入（Input），优先级高于output-low和output-high。 |
| `output-low` | `boolean` | 设置此属性会将GPIO配置为输出并置为逻辑低（Logical Low），优先级高于output-high。 |
| `output-high` | `boolean` | 设置此属性会将GPIO配置为输出并置为逻辑高（Logical High）。 |
| `line-name` | `string` | 可选GPIO信号线名称（GPIO Line Name）。 |

## RZ端口上拉与中断映射原例

```dts
  gpio-consumer {
    out-gpio = <&gpio8 2 (GPIO_PULL_UP)>;
  };
```

```dts
  &gpio8 {
    irqs = <&tint10 2>;
    status = "okay";
  };
```

<a id="specifier-cell-names"></a>

## 说明符单元名称

gpio cells：`pin`, `flags`。依次为引脚编号、配置标志。

---

[上一章](P024_renesas_rz-gpio-mipi-header.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P026_renesas_rza2m-gpio-int.md)
