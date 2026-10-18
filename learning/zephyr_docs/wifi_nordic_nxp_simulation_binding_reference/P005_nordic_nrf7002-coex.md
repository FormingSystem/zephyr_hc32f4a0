---
id: learning.zephyr-docs.wifi-nordic-nxp-simulation-binding-reference.page-5
title: nordic_nrf7002-coex
kind: reference
status: maintained
domains: [zephyr, devicetree, wifi]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/nordic,nrf7002-coex.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第5章\_nordic_nrf7002-coex

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/wifi/nordic,nrf7002-coex.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="nordic-nrf7002-coex"></a>
<a id="dtbinding-nordic-nrf7002-coex"></a>
<a id="std-dtcompatible-nordic-nrf7002-coex"></a>

兼容字符串（Compatible String）：`nordic,nrf7002-coex`。厂商：[ Nordic Semiconductor ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-nordic)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=nordic,nrf7002-coex)。

<a id="description"></a>

带共存接口（Coexistence Interface，COEX）的nRF7002 Wi-Fi芯片。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 5.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `req-gpios` | `phandle-array` | SoC上连接到数据包流量仲裁（Packet Traffic Arbitration，PTA）REQUEST请求引脚的GPIO。 |
| `status0-gpios` | `phandle-array` | SoC上连接到PTA PRIORITY优先级引脚的GPIO，也用于指示发送／接收方向（TX/RX）。 |
| `grant-gpios` | `phandle-array` | SoC上连接到PTA GRANT授权引脚的GPIO。 |
| `swctrl1-gpios` | `phandle-array` | SoC上控制nRF7002优先级引脚Priority／STATUS1的GPIO，适用于四线共存（4-Wire Coexistence）场景。 |

本页没有已弃用的节点专用属性。

---

[上一章](P004_nordic_nrf7001-spi.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P006_nordic_nrf7002-qspi.md)
