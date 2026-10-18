---
id: learning.zephyr-docs.usb.binding-117
title: USB音频输入终端绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-input-terminal.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第117章\_USB音频输入终端绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-input-terminal.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 117.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2-input-terminal`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2-input-terminal)。

## 117.2\_描述（Description）

USB 音频类 2 输入终端实体（Input Terminal Entity）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 117.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `terminal-type` | 整数（`int`） | USB 音频终端类型（USB Audio Terminal Types）中规定的终端类型常量。 必需（Required）。 |
| `assoc-terminal` | 节点引用（`phandle`） | 双向终端类型所关联的终端（Associated Terminal）。 |
| `clock-source` | 节点引用（`phandle`） | 连接的时钟实体（Clock Entity）。 必需（Required）。 |
| `copy-protect-control` | 字符串（`string`） | 复制保护控制（Copy Protect Control）能力。 合法值：`read-only`。 |
| `connector-control` | 字符串（`string`） | 连接器控制（Connector Control）能力。 合法值：`read-only`。 |
| `overload-control` | 字符串（`string`） | 过载控制（Overload Control）能力。 合法值：`read-only`。 |
| `cluster-control` | 字符串（`string`） | 声道簇控制（Cluster Control）能力。 合法值：`read-only`。 |
| `underflow-control` | 字符串（`string`） | 下溢控制（Underflow Control）能力。 合法值：`read-only`。 |
| `overflow-control` | 字符串（`string`） | 上溢控制（Overflow Control）能力。 合法值：`read-only`。 |
| `front-left` | 布尔值（`boolean`） | 声道簇中存在前左（Front Left）声道。 |
| `front-right` | 布尔值（`boolean`） | 声道簇中存在前右（Front Right）声道。 |
| `front-center` | 布尔值（`boolean`） | 声道簇中存在前中（Front Center）声道。 |
| `low-frequency-effects` | 布尔值（`boolean`） | 声道簇中存在低频效果（Low Frequency Effects，LFE）声道。 |
| `back-left` | 布尔值（`boolean`） | 声道簇中存在后左（Back Left）声道。 |
| `back-right` | 布尔值（`boolean`） | 声道簇中存在后右（Back Right）声道。 |
| `front-left-of-center` | 布尔值（`boolean`） | 声道簇中存在前中偏左（Front Left of Center）声道。 |
| `front-right-of-center` | 布尔值（`boolean`） | 声道簇中存在前中偏右（Front Right of Center）声道。 |
| `back-center` | 布尔值（`boolean`） | 声道簇中存在后中（Back Center）声道。 |
| `side-left` | 布尔值（`boolean`） | 声道簇中存在侧左（Side Left）声道。 |
| `side-right` | 布尔值（`boolean`） | 声道簇中存在侧右（Side Right）声道。 |
| `top-center` | 布尔值（`boolean`） | 声道簇中存在顶部中央（Top Center）声道。 |
| `top-front-left` | 布尔值（`boolean`） | 声道簇中存在顶部前左（Top Front Left）声道。 |
| `top-front-center` | 布尔值（`boolean`） | 声道簇中存在顶部前中（Top Front Center）声道。 |
| `top-front-right` | 布尔值（`boolean`） | 声道簇中存在顶部前右（Top Front Right）声道。 |
| `top-back-left` | 布尔值（`boolean`） | 声道簇中存在顶部后左（Top Back Left）声道。 |
| `top-back-center` | 布尔值（`boolean`） | 声道簇中存在顶部后中（Top Back Center）声道。 |
| `top-back-right` | 布尔值（`boolean`） | 声道簇中存在顶部后右（Top Back Right）声道。 |
| `top-front-left-of-center` | 布尔值（`boolean`） | 声道簇中存在顶部前中偏左（Top Front Left of Center）声道。 |
| `top-front-right-of-center` | 布尔值（`boolean`） | 声道簇中存在顶部前中偏右（Top Front Right of Center）声道。 |
| `left-low-frequency-effects` | 布尔值（`boolean`） | 声道簇中存在左低频效果（Left Low Frequency Effects）声道。 |
| `right-low-frequency-effects` | 布尔值（`boolean`） | 声道簇中存在右低频效果（Right Low Frequency Effects）声道。 |
| `top-side-left` | 布尔值（`boolean`） | 声道簇中存在顶部侧左（Top Side Left）声道。 |
| `top-side-right` | 布尔值（`boolean`） | 声道簇中存在顶部侧右（Top Side Right）声道。 |
| `bottom-center` | 布尔值（`boolean`） | 声道簇中存在底部中央（Bottom Center）声道。 |
| `back-left-of-center` | 布尔值（`boolean`） | 声道簇中存在后中偏左（Back Left of Center）声道。 |
| `back-right-of-center` | 布尔值（`boolean`） | 声道簇中存在后中偏右（Back Right of Center）声道。 |
| `raw-data` | 布尔值（`boolean`） | 原始数据（Raw Data），与所有其他空间位置（Spatial Locations）互斥。 |

## 117.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 117.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 117.6\_源码核对与关联阅读

> 译注：声道位置属性继承自官方zephyr,uac2-channel-cluster.yaml，下面逐项保留。raw-data与所有空间声道位置互斥。输入终端和输出终端描述音频拓扑，和USB IN／OUT端点方向需结合具体连接理解，不能只按中文“输入／输出”互换。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2-input-terminal.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2-input-terminal.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2-input-terminal.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2-input-terminal"></a>
<a id="dtbinding-zephyr-uac2-input-terminal"></a>
<a id="std-dtcompatible-zephyr-uac2-input-terminal"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P116_USB音频时钟源绑定.md) · [返回大纲](大纲.md) · [下一章](P118_USB音频输出终端绑定.md)
