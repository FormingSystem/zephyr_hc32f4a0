---
id: learning.zephyr-docs.lin-dali-mctp-sensor-bus-binding-reference.page-7
title: zephyr_mctp-i2c-gpio-target
kind: reference
status: maintained
domains: [zephyr, devicetree, communication]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/pmci/mctp/zephyr,mctp-i2c-gpio-target.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第7章\_zephyr_mctp-i2c-gpio-target

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/pmci/mctp/zephyr,mctp-i2c-gpio-target.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-mctp-i2c-gpio-target"></a>
<a id="dtbinding-zephyr-mctp-i2c-gpio-target"></a>
<a id="std-dtcompatible-zephyr-mctp-i2c-gpio-target"></a>

兼容字符串（Compatible String）：`zephyr,mctp-i2c-gpio-target`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,mctp-i2c-gpio-target)。

<a id="description"></a>

将MCTP绑定到带GPIO的I²C目标设备（Target）的配置。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 7.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `i2c` | `phandle` | 通过目标模式API（Target Mode API）用作MCTP总线的I²C外设。 |
| `i2c-addr` | `int` | 端点的I²C地址。 |
| `endpoint-id` | `int` | MCTP端点标识。 |
| `endpoint-gpios` | `phandle-array` | 连接到端点的GPIO。 |

本页没有已弃用的节点专用属性。

---

[上一章](P006_zephyr_mctp-i2c-gpio-controller.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_zephyr_mctp-i3c-controller.md)
