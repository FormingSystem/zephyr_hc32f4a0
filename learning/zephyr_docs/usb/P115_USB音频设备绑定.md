---
id: learning.zephyr-docs.usb.binding-115
title: USB音频设备绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第115章\_USB音频设备绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 115.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2)。
- 驱动（Driver）：[subsys/usb/device_next/class/usbd_uac2.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_uac2.c)。

## 115.2\_描述（Description）

USB 音频类 2（USB Audio Class 2，UAC2）实例。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 115.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `full-speed` | 布尔值（`boolean`） | 允许此实例以全速（Full-Speed）运行时为 true。 |
| `high-speed` | 布尔值（`boolean`） | 允许此实例以高速（High-Speed）运行时为 true。 |
| `audio-function` | 整数（`int`） | 一个常量，表示制造商为此音频功能指定的主要用途。使用 dt-bindings/usb/audio.h 中定义的音频功能类别代码（Audio Function Category Codes）。 必需（Required）。 |
| `interrupt-endpoint` | 布尔值（`boolean`） | 启用可选中断端点（Interrupt Endpoint），以便将各个可寻址实体（Addressable Entity）发生的动态变化通知主机（Host）。 |
| `latency-control` | 字符串（`string`） | 延迟控制（Latency Control）能力。 合法值：`read-only`、`host-programmable`。 |

## 115.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 115.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 115.6\_源码核对与关联阅读

> 译注：官方绑定源码要求子节点先列出音频控制实体（Audio Control Entities），例如时钟源和输入／输出终端，再列出音频流接口。实体ID取子节点索引加1；将流接口放在末尾可避免在实体数量达到255时消耗可用ID。这里是描述符和实体关系配置，不能由此推定任意控制器都支持所声明的速率。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2"></a>
<a id="dtbinding-zephyr-uac2"></a>
<a id="std-dtcompatible-zephyr-uac2"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P114_UMP功能块设备树配置.md) · [返回大纲](大纲.md) · [下一章](P116_USB音频时钟源绑定.md)
