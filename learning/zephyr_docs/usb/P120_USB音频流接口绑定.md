---
id: learning.zephyr-docs.usb.binding-120
title: USB音频流接口绑定
kind: reference
status: maintained
domains: [zephyr, usb, devicetree]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-audio-streaming.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_USB音频流接口绑定

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/uac2/zephyr,uac2-audio-streaming.html)。读取日期：2026-10-14；保存页面及HTML摘要见[来源记录](../SOURCES.md)。

## 120.1\_概述（Overview）

- 名称（Name）：`zephyr,uac2-audio-streaming`。
- 厂商（Vendor）：[Zephyr Project](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。
- 使用位置（Used in）：[使用此兼容标识的开发板列表](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,uac2-audio-streaming)。

## 120.2\_描述（Description）

USB 音频类 2 音频流接口（Audio Streaming Interface）。

属性类型保留绑定原名。`read-only`表示只读，`host-programmable`表示主机可编程，`not-present`表示对应控制不存在。各属性仅允许其各自行列出的值；未标必需或默认值时，不在译文中推定。

## 120.3\_节点专用属性（Node Specific Properties）

以下属性不继承自基础绑定文件。

| 属性 | 类型 | 完整说明与约束 |
| --- | --- | --- |
| `linked-terminal` | 节点引用（`phandle`） | 此接口连接的输入或输出终端。 必需（Required）。 |
| `active-alternate-setting-control` | 字符串（`string`） | 当前备用设置控制（Active Alternate Setting Control）能力。 合法值：`read-only`。 |
| `valid-alternate-settings-control` | 字符串（`string`） | 有效备用设置控制（Valid Alternate Settings Control）能力。 合法值：`read-only`。 |
| `external-interface` | 布尔值（`boolean`） | 音频流不通过 USB 传输时启用，即 IV 型音频流（Type IV Audio Stream）。 |
| `implicit-feedback` | 布尔值（`boolean`） | 在异步端点（Asynchronous Endpoint）上启用隐式反馈（Implicit Feedback）。对于 IN 端点，将端点行为类型设置为隐式反馈数据端点；对于 OUT 端点，设置此属性会移除显式反馈端点（Explicit Feedback Endpoint）。 |
| `pitch-control` | 字符串（`string`） | 音高控制（Pitch Control）能力。 合法值：`read-only`、`host-programmable`。 |
| `data-overrun-control` | 字符串（`string`） | 数据溢出（Data Overrun）控制能力。 合法值：`read-only`。 |
| `data-underrun-control` | 字符串（`string`） | 数据欠载（Data Underrun）控制能力。 合法值：`read-only`。 |
| `lock-delay` | 整数（`int`） | 此端点可靠锁定内部时钟恢复电路（Clock Recovery Circuitry）所需的时间，单位由 lock-delay-units 字段决定。仅当 linked-terminal 的时钟为 sof-synchronized 时相关。 |
| `lock-delay-units` | 字符串（`string`） | lock-delay 参数的单位。 合法值：`milliseconds`、`decoded-pcm-samples`。 |
| `subslot-size` | 整数（`int`） | 一个音频子时隙（Audio Subslot）占用的字节数，可以为 1、2、3 或 4。 |
| `bit-resolution` | 整数（`int`） | 音频子时隙中实际使用的位数。 |
| `polling-period-us` | 整数（`int`） | 输入或输出端点的轮询周期（Polling Period），单位为微秒。对于 USB 全速，依据取值可能被限制为 1 ms 或 32768 ms；对于 USB 高速，依据取值可能被限制为 125 μs 或 4096 ms。 |

## 120.4\_已弃用的节点专用属性（Deprecated Node Specific Properties）

以下列出不继承自基础绑定文件的已弃用属性。

无（None）。

## 120.5\_基础属性（Base Properties）

以下属性继承自基础绑定文件，该文件定义可用于多个节点的通用属性；并非所有属性都适用于本兼容标识。

无（None）。

## 120.6\_源码核对与关联阅读

> 译注：read-only为只读，host-programmable为主机可编程；lock-delay-units中的milliseconds为毫秒，decoded-pcm-samples为解码后的PCM采样数。subslot-size按字节计量，bit-resolution按有效位计量，两者单位不同。implicit-feedback改变描述符中的反馈端点安排，应用仍须实现相应音频时序和缓冲处理。

官方绑定源码：[dts/bindings/usb/uac2/zephyr,uac2-audio-streaming.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/dts/bindings/usb/uac2/zephyr,uac2-audio-streaming.yaml)；本仓库的[对应绑定](../../../dts/bindings/usb/uac2/zephyr,uac2-audio-streaming.yaml)供源码跟踪，版本可能与网页不同。本批未构建、播放音频或进行MIDI硬件测试。

[USB音频设备API](P089_USB音频2设备API.md) · [显式反馈示例](P091_USB音频显式反馈示例.md) · [隐式反馈示例](P092_USB音频隐式反馈示例.md)。

<a id="zephyr-uac2-audio-streaming"></a>
<a id="dtbinding-zephyr-uac2-audio-streaming"></a>
<a id="std-dtcompatible-zephyr-uac2-audio-streaming"></a>
<a id="description"></a>
<a id="properties"></a>
<a id="tab-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="tab-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="tab-0-QmFzZSBwcm9wZXJ0aWVz"></a>
<a id="panel-0-Tm9kZSBzcGVjaWZpYyBwcm9wZXJ0aWVz"></a>
<a id="panel-0-RGVwcmVjYXRlZCBub2RlIHNwZWNpZmljIHByb3BlcnRpZXM="></a>
<a id="panel-0-QmFzZSBwcm9wZXJ0aWVz"></a>

[上一章](P119_USB音频功能单元绑定.md) · [返回大纲](大纲.md) · [下一章](P121_USBMIDI设备绑定.md)
