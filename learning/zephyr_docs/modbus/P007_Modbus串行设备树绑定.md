---
id: learning.zephyr-docs.modbus.binding
title: Modbus串行设备树绑定
kind: reference
status: maintained
domains: [zephyr, modbus, communication]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/zephyr,modbus-serial.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Modbus串行设备树绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/misc/zephyr,modbus-serial.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-modbus-serial-on-uart-bus"></a>
<a id="dtbinding-zephyr-modbus-serial"></a>
<a id="std-dtcompatible-zephyr-modbus-serial"></a>

## 7.1\_概述

- 名称（Name）：`zephyr,modbus-serial`，位于UART总线上。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识符的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,modbus-serial)。
- 驱动（Driver）：[subsys/modbus/modbus_core.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/modbus/modbus_core.c)。

<a id="description"></a>

## 7.2\_描述

通过串行线路通信的Modbus设备。

<a id="properties"></a>

## 7.3\_节点专用属性

以下属性不继承自基础绑定文件。类型名称保留设备树绑定（Devicetree Binding）的原标识。

### `de-gpios`

类型：句柄数组（`phandle-array`）。

驱动器使能引脚（Driver Enable Pin）。这是RS-485收发器的驱动器使能（DE）引脚。若直接连接，微控制器（MCU）引脚应配置为高电平有效（Active High）。

### `re-gpios`

类型：句柄数组（`phandle-array`）。

接收器使能引脚（Receiver Enable Pin）。这是RS-485收发器的接收器使能（nRE）引脚。若直接连接，MCU引脚应配置为低电平有效（Active Low）。

## 7.4\_已弃用的节点专用属性

不继承自基础绑定文件的已弃用属性：无（None）。

## 7.5\_基础属性

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于`zephyr,modbus-serial`兼容标识符。

### `status`

类型：字符串（`string`）。

表示节点所代表的硬件或其他资源的运行状态。具体而言：

- `"okay"`表示资源可用，例如可以由设备驱动使用。
- `"disabled"`表示资源不可用，系统应将其视为不存在。

详见设备树规范（Devicetree Specification）v0.4的“2.3.4 status”。

合法值（Legal values）：`okay`、`disabled`、`reserved`、`fail`、`fail-sss`。

更多说明见[重要属性（Important properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

### `compatible`

类型：字符串数组（`string-array`）。

这是一个字符串列表，主要用于定义设备树节点代表哪种硬件或其他资源。各设备驱动检查特定的`compatible`属性值，以找到其应管理的资源节点。

推荐格式为`"vendor,device"`，其中`vendor`是厂商缩写，`device`通常取自数据手册。

该属性可以包含多个值，按从最具体到最一般的顺序排列。当设备属于更通用系列中的特定实例时，额外的值可让系统匹配当前可用的最具体驱动。

详见设备树规范v0.4的“2.3.1 compatible”。

**此属性为必需项（Required）。**

更多说明见[重要属性（Important properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

### `reg`

类型：数组（`array`）。

用于寻址设备的信息。具体取值由设备决定，即随`compatible`属性而不同。

`reg`通常是一系列“地址、长度”对，每一对称为寄存器块（Register Block），惯例上使用十六进制书写。

详见设备树规范v0.4的“2.3.6 reg”。

更多说明见[重要属性（Important properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

### `reg-names`

类型：字符串数组（`string-array`）。

为`reg`属性中的每个寄存器块指定可选名称。例如：

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

`uart@1000`节点包含两个寄存器块：

- 基地址`0x1000`、大小`0x2000`、名称`"foo"`。
- 基地址`0x3000`、大小`0x4000`、名称`"bar"`。

### `ranges`

类型：复合类型（`compound`）。

定义总线地址空间（子地址空间，Child Address Space）与该总线节点父节点的地址空间（父地址空间，Parent Address Space）之间的映射或转换。

`ranges`通常为空，或是一系列“子总线地址、父总线地址、长度”三元组。

如果`ranges`为空，表示父子地址空间相同，无需地址转换。若总线节点中没有`ranges`属性，则认为该节点的子节点与父地址空间之间不存在映射。

详见设备树规范v0.4的“2.3.8 ranges”。

### `interrupts`

类型：数组（`array`）。

设备产生的中断信息，编码为一个或多个中断说明符（Interrupt Specifier）组成的数组。数据格式取决于设备在中断树中的位置；具有相同`interrupt-parent`的设备，其`interrupts`属性使用相同格式。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

更多说明见[重要属性（Important properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

### `interrupts-extended`

类型：复合类型（`compound`）。

设备的扩展中断说明符，可替代`interrupts`属性。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### `interrupt-names`

类型：字符串数组（`string-array`）。

为设备产生的每个中断指定可选名称。中断本身在`interrupts`或`interrupts-extended`属性中定义。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### `interrupt-parent`

类型：句柄（`phandle`）。

若提供此属性，它指向负责处理本设备所产生中断的节点。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### `label`

类型：字符串（`string`）。

用于描述设备的可读字符串。除按具体情况确有需要外，此属性的使用已弃用（Deprecated）。

详见设备树规范v0.4的“4.1.2 Miscellaneous Properties”。

更多说明见[重要属性（Important properties）](https://docs.zephyrproject.org/latest/build/dts/intro-syntax-structure.html#dt-important-props)。

### `clocks`

类型：句柄数组（`phandle-array`）。

设备时钟提供者（Clock Provider）的信息。一般应遵循[dt-schema时钟绑定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)中的约定。

### `clock-names`

类型：字符串数组（`string-array`）。

为`clocks`属性中的各个时钟提供者指定可选名称。

### `#address-cells`

类型：整数（`int`）。

编码本节点的子节点中，`reg`属性地址字段使用的`<u32>`单元（Cell）数量。

详见设备树规范v0.4的“2.3.5 #address-cells and #size-cells”。

### `#size-cells`

类型：整数（`int`）。

编码本节点的子节点中，`reg`属性大小字段使用的`<u32>`单元数量。

详见设备树规范v0.4的“2.3.5 #address-cells and #size-cells”。

### `dma-coherent`

类型：布尔值（`boolean`）。

表示设备能够执行一致性直接存储器访问（Coherent Direct Memory Access，Coherent DMA）操作。

详见设备树规范v0.4的“2.3.10 dma-coherent”。

### `dmas`

类型：句柄数组（`phandle-array`）。

与设备相关的DMA通道说明符（DMA Channel Specifier）。

### `dma-names`

类型：字符串数组（`string-array`）。

为`dmas`属性中的DMA通道说明符指定可选名称。

### `dma-ranges`

类型：复合类型（`compound`）。

`dma-ranges`用于定义总线物理地址空间与总线父节点物理地址空间之间的映射或转换。

详见设备树规范v0.4的“2.3.9 dma-ranges”。

### `io-channels`

类型：句柄数组（`phandle-array`）。

与设备相关的输入／输出通道说明符（I/O Channel Specifier）。

### `io-channel-names`

类型：字符串数组（`string-array`）。

为`io-channels`属性中的I/O通道说明符指定可选名称。

### `mboxes`

类型：句柄数组（`phandle-array`）。

与设备相关的邮箱（Mailbox）／处理器间消息（Inter-Processor Messaging，IPM）通道说明符。

### `mbox-names`

类型：字符串数组（`string-array`）。

为`mboxes`属性中的邮箱说明符指定可选名称。

### `power-domains`

类型：句柄数组（`phandle-array`）。

与设备相关的电源域说明符（Power Domain Specifier）。

### `power-domain-names`

类型：字符串数组（`string-array`）。

为`power-domains`属性中的电源域说明符指定可选名称。

### `#power-domain-cells`

类型：整数（`int`）。

`power-domains`属性中的单元数量。

### `hwlocks`

类型：句柄数组（`phandle-array`）。

与设备相关的硬件自旋锁（Hardware Spinlock）标识。

### `hwlock-names`

类型：字符串数组（`string-array`）。

为`hwlocks`属性中的硬件自旋锁说明符指定可选名称。

### `zephyr,deferred-init`

类型：布尔值（`boolean`）。

启动时不自动初始化设备。应使用`device_init()`手动初始化。

### `wakeup-source`

类型：布尔值（`boolean`）。

标识设备可用作唤醒源（Wakeup Source）。

提供此属性时，会在设备中设置特定标志，告知系统该设备能够唤醒系统。

具备唤醒能力的设备默认禁用唤醒，即中断不会唤醒系统；必要时可在运行时启用。

### `zephyr,pm-device-runtime-auto`

类型：布尔值（`boolean`）。

初始化函数运行后，自动将设备配置为使用运行时电源管理（Runtime Power Management）。

### `zephyr,disabling-power-states`

类型：句柄列表（`phandles`）。

会关闭此设备供电的电源状态（Power State）列表。

[上一章：Modbus TCP服务器](P006_TCP服务器.md) · [返回大纲](大纲.md) · [下一章：Modbus完整API参考](P008_Modbus完整API参考.md)
