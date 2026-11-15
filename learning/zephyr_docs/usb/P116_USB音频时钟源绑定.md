---
id: learning.zephyr-docs.usb.binding-116
title: USB音频时钟源绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-clock-source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_USB音频时钟源绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-clock-source.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 116.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2-clock-source`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2-clock-source)。

## 116.2\_描述（Description）

USB 音频类 2 时钟源实体（Clock Source Entity）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 116.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `clock-type` | 字符串（`string`） | 时钟类型（Clock Type），表示时钟源是外部时钟（External Clock），还是固定频率、可变频率或可编程频率的内部时钟（Internal Clock）。 必需（Required）。 合法值：`external`、`internal-fixed`、`internal-variable`、`internal-programmable`。 |
| `sof-synchronized` | 布尔值（`boolean`） | 时钟与 USB 帧起始（Start of Frame，SOF）同步时为 true；时钟自由运行（Free Running）时为 false。外部时钟必须自由运行。 |
| `frequency-control` | 字符串（`string`） | 时钟频率控制（Clock Frequency Control）能力。 合法值：`read-only`、`host-programmable`。 |
| `validity-control` | 字符串（`string`） | 时钟有效性控制（Clock Validity Control）能力。 合法值：`read-only`。 |
| `assoc-terminal` | 节点引用（`phandle`） | 与此时钟源关联的输入或输出终端（Input／Output Terminal）。时钟从 USB OUT 数据端点派生时应设置此属性，将节点引用指向相应输入终端；从 S/PDIF 连接器的输入信号派生时也应设置。 |
| `sampling-frequencies` | 数组（`array`） | 此时钟源实体能够产生的采样频率（Sampling Frequencies），单位为 Hz。 必需（Required）。 |

## 116.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 116.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 116.6\_源码核对与关联阅读

> 译注：external表示外部时钟，internal-fixed、internal-variable、internal-programmable分别表示固定、可变、可编程内部时钟。read-only表示主机只读，host-programmable表示允许主机编程。sampling-frequencies的单位是Hz，不能直接填写以kHz表示的数值。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2-clock-source.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2-clock-source.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2-clock-source.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2-clock-source"></a>
<a id="dtbinding-zephyr-uac2-clock-source"></a>
<a id="std-dtcompatible-zephyr-uac2-clock-source"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P115_USB音频设备绑定.md) · [返回大纲](大纲.md) · [下一章](P117_USB音频输入终端绑定.md)
