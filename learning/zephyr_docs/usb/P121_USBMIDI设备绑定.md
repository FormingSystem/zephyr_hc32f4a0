---
id: learning.zephyr-docs.usb.binding-121
title: USBMIDI设备绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/zephyr,midi2-device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_USBMIDI设备绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/zephyr,midi2-device.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 121.1\_概述（Overview）

- 名称（Name）：`zephyr,midi2-device`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,midi2-device)。
- 驱动（Driver）：[subsys/usb/device_next/class/usbd_midi2.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_midi2.c)。

## 121.2\_描述（Description）

MIDI2 设备，MIDI 为乐器数字接口（Musical Instrument Digital Interface）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

以下三类属性适用于顶层设备节点；子节点属性另列于后。

## 121.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

无（None）。

## 121.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 121.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `#address-cells` | 整数（`int`） | 固定值：`1`。 |
| `#size-cells` | 整数（`int`） | 固定值：`1`。 |
| `label` | 字符串（`string`） | UMP（MIDI 2.0）端点的名称；UMP 为通用 MIDI 数据包（Universal MIDI Packet）。 详见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。 |

## 121.6\_子节点属性（Child Node Properties）

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `label` | 字符串（`string`） | 对应 UMP 功能块（Function Block）的名称。 详见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。 |
| `reg` | 数组（`array`） | 此 MIDI2 组终端块（Group Terminal Block）中，第一个 MIDI2 组号（地址）与组终端数量（大小）。MIDI2 组 1 至 16 对应地址 0x0 至 0xf。每个 MIDI2 接口最多有 16 个可寻址组，每组包含 16 个通道。 必需（Required）。 详见[重要属性（Important Properties）](../devicetree/P003_语法与结构.md#dt-important-props)。 |
| `protocol` | 字符串（`string`） | 此块内组终端使用的默认 MIDI 协议。 合法值：`use-midi-ci`、`midi1-up-to-64b`、`midi1-up-to-128b`、`midi2`。 |
| `terminal-type` | 字符串（`string`） | 此块内组终端的类型，即数据方向（Data Direction）。 默认值：`bidirectional`。 合法值：`bidirectional`、`input-only`、`output-only`。 |
| `serial-31250bps` | 布尔值（`boolean`） | 表示一个物理 MIDI1 串行端口，其传输速率限制为 31.25 kb/s。 |

## 121.7\_源码核对与关联阅读

> 译注：官方child-binding说明：子节点表示MIDI2组终端块，即一组连续MIDI2组，设备通过这些组与主机交换UMP。reg的两个单元分别是起始组索引与组数量，不是寄存器物理地址和字节长度。bidirectional、input-only、output-only分别为双向、仅输入、仅输出；use-midi-ci表示使用MIDI能力查询，其他protocol值分别指定MIDI1的64／128位上限或MIDI2。顶层label命名端点，子节点label命名功能块。

官方绑定源码：[dts/bindings/usb/zephyr,midi2-device.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/zephyr,midi2-device.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/zephyr,midi2-device.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[MIDI设备API](P094_USBMIDI2设备API.md) · [MIDI示例](P096_USBMIDI2设备示例.md) · [UMP功能块配置](P114_UMP功能块设备树配置.md)。

<a id="zephyr-midi2-device"></a>
<a id="dtbinding-zephyr-midi2-device"></a>
<a id="std-dtcompatible-zephyr-midi2-device"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="top-level-properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="child-node-properties"></a>

[上一章](P120_USB音频流接口绑定.md) · [返回大纲](大纲.md) · [下一章](P122_USB视频设备API.md)
