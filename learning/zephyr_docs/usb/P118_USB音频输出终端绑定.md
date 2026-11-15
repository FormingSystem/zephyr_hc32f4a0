---
id: learning.zephyr-docs.usb.binding-118
title: USB音频输出终端绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-output-terminal.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第118章\_USB音频输出终端绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-output-terminal.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 118.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2-output-terminal`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2-output-terminal)。

## 118.2\_描述（Description）

USB 音频类 2 输出终端实体（Output Terminal Entity）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 118.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `terminal-type` | 整数（`int`） | USB 音频终端类型（USB Audio Terminal Types）中规定的终端类型常量。 必需（Required）。 |
| `assoc-terminal` | 节点引用（`phandle`） | 关联终端，例如双向终端类型对应的终端。 |
| `data-source` | 节点引用（`phandle`） | 此终端接收数据的来源单元或终端（Unit or Terminal）。 必需（Required）。 |
| `clock-source` | 节点引用（`phandle`） | 连接的时钟实体（Clock Entity）。 必需（Required）。 |
| `copy-protect-control` | 字符串（`string`） | 复制保护控制（Copy Protect Control）能力。 合法值：`host-programmable`。 |
| `connector-control` | 字符串（`string`） | 连接器控制（Connector Control）能力。 合法值：`read-only`。 |
| `overload-control` | 字符串（`string`） | 过载控制（Overload Control）能力。 合法值：`read-only`。 |
| `underflow-control` | 字符串（`string`） | 下溢控制（Underflow Control）能力。 合法值：`read-only`。 |
| `overflow-control` | 字符串（`string`） | 上溢控制（Overflow Control）能力。 合法值：`read-only`。 |

## 118.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 118.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 118.6\_源码核对与关联阅读

> 译注：本页copy-protect-control的合法值为host-programmable；输入终端相同名称属性的合法值为read-only。应分别遵循各自绑定，不将同名属性的允许值合并。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2-output-terminal.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2-output-terminal.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2-output-terminal.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2-output-terminal"></a>
<a id="dtbinding-zephyr-uac2-output-terminal"></a>
<a id="std-dtcompatible-zephyr-uac2-output-terminal"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P117_USB音频输入终端绑定.md) · [返回大纲](大纲.md) · [下一章](P119_USB音频功能单元绑定.md)
