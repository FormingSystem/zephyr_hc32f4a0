---
id: learning.zephyr-docs.usb.api-106
title: UMP端点发现过滤位
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__ep__disc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第106章\_UMP端点发现过滤位

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__ep__disc.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 106.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1.1 节图 12：端点发现消息过滤位图字段。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_UMP_STREAM 且 UMP_STREAM_STATUS(x)=UMP_STREAM_STATUS_EP_DISCOVERY 时，UMP_STREAM_EP_DISCOVERY_FILTER(x) 可以是下列值按位或（Bitwise OR）的组合。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_STREAM_STATUS(x)](P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)、[UMP_STREAM_EP_DISCOVERY_FILTER(x)](P103_UMP流消息字段.md#gacbefffaacf70b546d5b7055bcefe7f16)。

## 106.2\_宏定义（Macros）

<a id="r_ga6a234420b601ba9899b9a0c81e10daee"></a>

```c
#define UMP_EP_DISC_FILTER_EP_INFO BIT(0)
```

请求端点信息通知（Endpoint Info Notification）。

相关声明：[UMP_EP_DISC_FILTER_EP_INFO](P106_UMP端点发现过滤位.md#ga6a234420b601ba9899b9a0c81e10daee)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga07a1a713e27f2e1d59531f51699e65c8"></a>

```c
#define UMP_EP_DISC_FILTER_DEVICE_ID BIT(1)
```

请求设备身份通知（Device Identity Notification）。

相关声明：[UMP_EP_DISC_FILTER_DEVICE_ID](P106_UMP端点发现过滤位.md#ga07a1a713e27f2e1d59531f51699e65c8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gadc49c22e63a6119aa19fc655cbdd75f2"></a>

```c
#define UMP_EP_DISC_FILTER_EP_NAME BIT(2)
```

请求端点名称通知（Endpoint Name Notification）。

相关声明：[UMP_EP_DISC_FILTER_EP_NAME](P106_UMP端点发现过滤位.md#gadc49c22e63a6119aa19fc655cbdd75f2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_gad0a5a402d072dc843453cf4416dcb571"></a>

```c
#define UMP_EP_DISC_FILTER_PRODUCT_ID BIT(3)
```

请求产品实例标识通知（Product Instance ID Notification）。

相关声明：[UMP_EP_DISC_FILTER_PRODUCT_ID](P106_UMP端点发现过滤位.md#gad0a5a402d072dc843453cf4416dcb571)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_ga72d2233a8760e3127bd7b4d133e12b3b"></a>

```c
#define UMP_EP_DISC_FILTER_STREAM_CFG BIT(4)
```

请求流配置通知（Stream Configuration Notification）。

相关声明：[UMP_EP_DISC_FILTER_STREAM_CFG](P106_UMP端点发现过滤位.md#ga72d2233a8760e3127bd7b4d133e12b3b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

## 106.3\_详细说明（Detailed Documentation）

<a id="ga07a1a713e27f2e1d59531f51699e65c8"></a>

### 106.3.1\_`UMP\_EP\_DISC\_FILTER\_DEVICE\_ID`

```c
#define UMP_EP_DISC_FILTER_DEVICE_ID BIT(1)
```

```c
#include <zephyr/audio/midi.h>
```

请求设备身份通知（Device Identity Notification）。

<a id="ga6a234420b601ba9899b9a0c81e10daee"></a>

### 106.3.2\_`UMP\_EP\_DISC\_FILTER\_EP\_INFO`

```c
#define UMP_EP_DISC_FILTER_EP_INFO BIT(0)
```

```c
#include <zephyr/audio/midi.h>
```

请求端点信息通知（Endpoint Info Notification）。

<a id="gadc49c22e63a6119aa19fc655cbdd75f2"></a>

### 106.3.3\_`UMP\_EP\_DISC\_FILTER\_EP\_NAME`

```c
#define UMP_EP_DISC_FILTER_EP_NAME BIT(2)
```

```c
#include <zephyr/audio/midi.h>
```

请求端点名称通知（Endpoint Name Notification）。

<a id="gad0a5a402d072dc843453cf4416dcb571"></a>

### 106.3.4\_`UMP\_EP\_DISC\_FILTER\_PRODUCT\_ID`

```c
#define UMP_EP_DISC_FILTER_PRODUCT_ID BIT(3)
```

```c
#include <zephyr/audio/midi.h>
```

请求产品实例标识通知（Product Instance ID Notification）。

<a id="ga72d2233a8760e3127bd7b4d133e12b3b"></a>

### 106.3.5\_`UMP\_EP\_DISC\_FILTER\_STREAM\_CFG`

```c
#define UMP_EP_DISC_FILTER_STREAM_CFG BIT(4)
```

```c
#include <zephyr/audio/midi.h>
```

请求流配置通知（Stream Configuration Notification）。

> 译注（源码核对）：该位请求返回流配置通知，不表示发送方已经改变流配置；配置请求与配置通知还有独立的UMP流状态值。

## 106.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P105_UMP流消息状态.md) · [返回大纲](大纲.md) · [下一章](P107_UMP功能块发现过滤位.md)
