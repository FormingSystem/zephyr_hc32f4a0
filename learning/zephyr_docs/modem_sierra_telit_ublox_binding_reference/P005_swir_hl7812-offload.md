---
id: learning.zephyr-docs.modem-sierra-telit-ublox-binding-reference.page-5
title: swir_hl7812-offload
kind: reference
status: maintained
domains: [zephyr, devicetree, modem]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/modem/swir,hl7812-offload.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_swir_hl7812-offload

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/modem/swir,hl7812-offload.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="swir-hl7812-offload"></a>
<a id="dtbinding-swir-hl7812-offload"></a>
<a id="std-dtcompatible-swir-hl7812-offload"></a>

兼容字符串（Compatible String）：`swir,hl7812-offload`。厂商：[ Sierra Wireless ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-swir)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=swir,hl7812-offload)。

<a id="description"></a>

Sierra Wireless HL7812调制解调器卸载（Modem Offload）。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `max-data-length` | `int` | 调制解调器单次卸载操作可发送／接收的单份数据载荷最大长度（Maximum Payload Length），单位字节。；合法值：`512, 1024, 2048, 4096, 8192` |
| `offload-priority` | `int` | 此卸载调制解调器相对于系统中其他卸载调制解调器的优先级（Priority）。数值越小，优先级越高；有多个可用模块时，系统优先使用数值最低者。 |

本页没有已弃用的节点专用属性。

---

[上一章](P004_swir_hl7812-gnss.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_swir_hl7812.md)
