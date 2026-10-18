---
id: learning.zephyr-docs.usb.page-126
title: USB视频设备绑定
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/zephyr,uvc-device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_USB视频设备绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/zephyr,uvc-device.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 126.1\_概述（Overview）

- 名称（Name）：`zephyr,uvc-device`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uvc-device)。
- 驱动（Driver）：[subsys/usb/device_next/class/usbd_uvc.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_uvc.c)。

## 126.2\_描述（Description）

USB 视频类（USB Video Class，UVC）设备实例。

每个添加到 USB 设备控制器（USB Device Controller，UDC）节点中的 UVC 实例，在主机看来都会成为一台新摄像头。

## 126.3\_节点专用属性（Node Specific Properties）

不继承自基础绑定文件的属性：无（None）。

## 126.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

不继承自基础绑定文件的已弃用属性：无（None）。

## 126.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于 `zephyr,uvc-device` 兼容标识。

### 126.5.1\_`status`

类型：字符串（`string`）。

表示节点所代表的硬件或其他资源的运行状态。具体而言：

- `"okay"`表示资源可用，例如可以由设备驱动使用。
- `"disabled"`表示资源不可用，系统应将其视为不存在。

详见设备树规范（Devicetree Specification）v0.4的“2.3.4 status”。

合法值（Legal Values）：`okay`、`disabled`、`reserved`、`fail`、`fail-sss`。

更多说明见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。

### 126.5.2\_`compatible`

类型：字符串数组（`string-array`）。

这是一个字符串列表，主要用于定义设备树节点代表哪种硬件或其他资源。各设备驱动检查特定的`compatible`属性值，以找到其应管理的资源节点。

推荐格式为`"vendor,device"`，其中`vendor`是厂商缩写，`device`通常取自数据手册。

该属性可以包含多个值，按从最具体到最一般的顺序排列。当设备属于更通用系列中的特定实例时，额外的值可让系统匹配当前可用的最具体驱动。

详见设备树规范v0.4的“2.3.1 compatible”。

**此属性为必需项（Required）。**

更多说明见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。

### 126.5.3\_`reg`

类型：数组（`array`）。

用于寻址设备的信息。具体取值由设备决定，即随`compatible`属性而不同。

`reg`通常是一系列“地址、长度”对，每一对称为寄存器块（Register Block），惯例上使用十六进制书写。

详见设备树规范v0.4的“2.3.6 reg”。

更多说明见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。

### 126.5.4\_`reg-names`

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

### 126.5.5\_`ranges`

类型：复合类型（`compound`）。

定义总线地址空间（子地址空间，Child Address Space）与该总线节点父节点的地址空间（父地址空间，Parent Address Space）之间的映射或转换。

`ranges`通常为空，或是一系列“子总线地址、父总线地址、长度”三元组。

如果`ranges`为空，表示父子地址空间相同，无需地址转换。若总线节点中没有`ranges`属性，则认为该节点的子节点与父地址空间之间不存在映射。

详见设备树规范v0.4的“2.3.8 ranges”。

### 126.5.6\_`interrupts`

类型：数组（`array`）。

设备产生的中断信息，编码为一个或多个中断说明符（Interrupt Specifier）组成的数组。数据格式取决于设备在中断树中的位置；具有相同`interrupt-parent`的设备，其`interrupts`属性使用相同格式。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

更多说明见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。

### 126.5.7\_`interrupts-extended`

类型：复合类型（`compound`）。

设备的扩展中断说明符，可替代`interrupts`属性。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### 126.5.8\_`interrupt-names`

类型：字符串数组（`string-array`）。

为设备产生的每个中断指定可选名称。中断本身在`interrupts`或`interrupts-extended`属性中定义。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### 126.5.9\_`interrupt-parent`

类型：节点引用（`phandle`）。

若提供此属性，它指向负责处理本设备所产生中断的节点。

详见设备树规范v0.4的“2.4 Interrupts and Interrupt Mapping”。

### 126.5.10\_`label`

类型：字符串（`string`）。

用于描述设备的可读字符串。除按具体情况确有需要外，此属性的使用已弃用（Deprecated）。

详见设备树规范v0.4的“4.1.2 Miscellaneous Properties”。

更多说明见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。

### 126.5.11\_`clocks`

类型：节点引用数组（`phandle-array`）。

设备时钟提供者（Clock Provider）的信息。一般应遵循[dt-schema时钟绑定](https://github.com/devicetree-org/dt-schema/blob/main/dtschema/schemas/clock/clock.yaml)中的约定。

### 126.5.12\_`clock-names`

类型：字符串数组（`string-array`）。

为`clocks`属性中的各个时钟提供者指定可选名称。

### 126.5.13\_`#address-cells`

类型：整数（`int`）。

编码本节点的子节点中，`reg`属性地址字段使用的`<u32>`单元（Cell）数量。

详见设备树规范v0.4的“2.3.5 #address-cells and #size-cells”。

### 126.5.14\_`#size-cells`

类型：整数（`int`）。

编码本节点的子节点中，`reg`属性大小字段使用的`<u32>`单元数量。

详见设备树规范v0.4的“2.3.5 #address-cells and #size-cells”。

### 126.5.15\_`dma-coherent`

类型：布尔值（`boolean`）。

表示设备能够执行一致性直接存储器访问（Coherent Direct Memory Access，Coherent DMA）操作。

详见设备树规范v0.4的“2.3.10 dma-coherent”。

### 126.5.16\_`dmas`

类型：节点引用数组（`phandle-array`）。

与设备相关的DMA通道说明符（DMA Channel Specifier）。

### 126.5.17\_`dma-names`

类型：字符串数组（`string-array`）。

为`dmas`属性中的DMA通道说明符指定可选名称。

### 126.5.18\_`dma-ranges`

类型：复合类型（`compound`）。

`dma-ranges`用于定义总线物理地址空间与总线父节点物理地址空间之间的映射或转换。

详见设备树规范v0.4的“2.3.9 dma-ranges”。

### 126.5.19\_`io-channels`

类型：节点引用数组（`phandle-array`）。

与设备相关的输入／输出通道说明符（I/O Channel Specifier）。

### 126.5.20\_`io-channel-names`

类型：字符串数组（`string-array`）。

为`io-channels`属性中的I/O通道说明符指定可选名称。

### 126.5.21\_`mboxes`

类型：节点引用数组（`phandle-array`）。

与设备相关的邮箱（Mailbox）／处理器间消息（Inter-Processor Messaging，IPM）通道说明符。

### 126.5.22\_`mbox-names`

类型：字符串数组（`string-array`）。

为`mboxes`属性中的邮箱说明符指定可选名称。

### 126.5.23\_`power-domains`

类型：节点引用数组（`phandle-array`）。

与设备相关的电源域说明符（Power Domain Specifier）。

### 126.5.24\_`power-domain-names`

类型：字符串数组（`string-array`）。

为`power-domains`属性中的电源域说明符指定可选名称。

### 126.5.25\_`#power-domain-cells`

类型：整数（`int`）。

`power-domains`属性中的单元数量。

### 126.5.26\_`hwlocks`

类型：节点引用数组（`phandle-array`）。

与设备相关的硬件自旋锁（Hardware Spinlock）标识。

### 126.5.27\_`hwlock-names`

类型：字符串数组（`string-array`）。

为`hwlocks`属性中的硬件自旋锁说明符指定可选名称。

### 126.5.28\_`zephyr,deferred-init`

类型：布尔值（`boolean`）。

启动时不自动初始化设备。应使用`device_init()`手动初始化。

### 126.5.29\_`wakeup-source`

类型：布尔值（`boolean`）。

标识设备可用作唤醒源（Wakeup Source）。

提供此属性时，会在设备中设置特定标志，告知系统该设备能够唤醒系统。

具备唤醒能力的设备默认禁用唤醒，即中断不会唤醒系统；必要时可在运行时启用。

### 126.5.30\_`zephyr,pm-device-runtime-auto`

类型：布尔值（`boolean`）。

初始化函数运行后，自动将设备配置为使用运行时电源管理（Runtime Power Management）。

### 126.5.31\_`zephyr,disabling-power-states`

类型：节点引用列表（`phandles`）。

会关闭此设备供电的电源状态（Power State）列表。

## 126.6\_关联阅读

[USB视频设备API](P122_USB视频设备API.md) · [USB视频摄像头示例](P124_USB视频摄像头示例.md)。


译注核对来源：[dts/bindings/usb/zephyr,uvc-device.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/zephyr,uvc-device.yaml)。

本仓库的[对应源码](../../../dts/bindings/usb/zephyr,uvc-device.yaml)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="zephyr-uvc-device"></a>
<a id="dtbinding-zephyr-uvc-device"></a>
<a id="std-dtcompatible-zephyr-uvc-device"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P125_USB主机摄像头示例.md) · [返回大纲](大纲.md) · [下一章](P127_旧版USB设备API入口.md)
