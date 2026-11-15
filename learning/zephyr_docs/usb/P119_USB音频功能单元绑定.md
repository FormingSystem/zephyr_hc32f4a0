---
id: learning.zephyr-docs.usb.binding-119
title: USB音频功能单元绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-feature-unit.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_USB音频功能单元绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-feature-unit.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 119.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2-feature-unit`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2-feature-unit)。

## 119.2\_描述（Description）

USB 音频类 2 功能单元实体（Feature Unit Entity）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 119.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `data-source` | 节点引用（`phandle`） | 此功能单元连接的单元或终端。 |
| `mute-control` | 字符串数组（`string-array`） | 静音控制（Mute Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `volume-control` | 字符串数组（`string-array`） | 音量控制（Volume Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `bass-control` | 字符串数组（`string-array`） | 低音控制（Bass Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `mid-control` | 字符串数组（`string-array`） | 中音控制（Mid Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `treble-control` | 字符串数组（`string-array`） | 高音控制（Treble Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `graphic-equalizer-control` | 字符串数组（`string-array`） | 图示均衡器（Graphic Equalizer）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `automatic-gain-control` | 字符串数组（`string-array`） | 自动增益控制（Automatic Gain Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `delay-control` | 字符串数组（`string-array`） | 延时控制（Delay Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `bass-boost-control` | 字符串数组（`string-array`） | 低音增强控制（Bass Boost Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `loundness-control` | 字符串数组（`string-array`） | 响度控制能力，原文写作 Loundness Control。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `input-gain-control` | 字符串数组（`string-array`） | 输入增益控制（Input Gain Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `input-gain-pad-control` | 字符串数组（`string-array`） | 输入增益衰减控制（Input Gain Pad Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `phase-inverter-control` | 字符串数组（`string-array`） | 相位反转控制（Phase Inverter Control）能力。 合法值：`read-only`、`host-programmable`、`not-present`。 |
| `underflow-control` | 字符串数组（`string-array`） | 下溢控制（Underflow Control）能力。 合法值：`read-only`、`not-present`。 |
| `overflow-control` | 字符串数组（`string-array`） | 上溢控制（Overflow Control）能力。 合法值：`read-only`、`not-present`。 |

## 119.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 119.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 119.6\_源码核对与关联阅读

> 译注：官方YAML注释说明，string-array从主声道0（Primary Channel 0）开始，随后依次为逻辑声道（Logical Channels）。not-present用于主声道不存在、而某些逻辑声道存在该控制等情况；它与省略整个属性不同。loundness-control是当前官方属性的原始拼写，表达响度（Loudness）控制，配置中须保留原名。data-source在此绑定未标required；不要因其他终端绑定同名属性必需就擅自补写这一限制。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2-feature-unit.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2-feature-unit.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2-feature-unit.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2-feature-unit"></a>
<a id="dtbinding-zephyr-uac2-feature-unit"></a>
<a id="std-dtcompatible-zephyr-uac2-feature-unit"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P118_USB音频输出终端绑定.md) · [返回大纲](大纲.md) · [下一章](P120_USB音频流接口绑定.md)
