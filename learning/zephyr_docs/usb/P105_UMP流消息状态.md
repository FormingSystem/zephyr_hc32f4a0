---
id: learning.zephyr-docs.usb.api-105
title: UMP流消息状态
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第105章\_UMP流消息状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__midi__ump__stream__status.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 105.1\_阅读说明与来源

译注：本页说明MIDI通用数据包的消息类型、命令或流消息字段。MIDI指乐器数字接口（Musical Instrument Digital Interface），UMP指通用MIDI数据包（Universal MIDI Packet）。官方只列声明的字段保持完整，源码补充明确标为译注；[本册大纲](大纲.md)列出对应说明、接口和示例。

参阅《通用 MIDI 数据包（UMP）格式与 MIDI 2.0 协议》第 7.1 节：UMP 流消息。

相关声明：[Universal MIDI Packet (UMP) Format and MIDI 2.0 Protocol](P113_UMP格式与MIDI协议依据.md)。

备注：当 UMP_MT(x)=UMP_MT_UMP_STREAM 时，UMP_STREAM_STATUS(x) 可以是下列值之一。

相关声明：[UMP_MT(x)](P098_通用MIDI数据包定义.md#gafab438886f69fb74a6e058f9343867aa)、[UMP_STREAM_STATUS(x)](P103_UMP流消息字段.md#ga27ee62e9a2c2f6e23de61d8f5c42c0a8)。

## 105.2\_宏定义（Macros）

<a id="r_gab753d923dd8a6045f85f5ac7032fd040"></a>

```c
#define UMP_STREAM_STATUS_EP_DISCOVERY 0x00
```

端点发现消息（Endpoint Discovery Message）。

相关声明：[UMP_STREAM_STATUS_EP_DISCOVERY](P105_UMP流消息状态.md#gab753d923dd8a6045f85f5ac7032fd040)。

<a id="r_ga1ff08a079dd9b84aa297ca73043342db"></a>

```c
#define UMP_STREAM_STATUS_EP_INFO 0x01
```

端点信息通知消息（Endpoint Info Notification Message）。

相关声明：[UMP_STREAM_STATUS_EP_INFO](P105_UMP流消息状态.md#ga1ff08a079dd9b84aa297ca73043342db)。

<a id="r_gaa53b5c80022e1888515f2c0616d9cfc3"></a>

```c
#define UMP_STREAM_STATUS_DEVICE_IDENT 0x02
```

设备身份通知消息（Device Identity Notification Message）。

相关声明：[UMP_STREAM_STATUS_DEVICE_IDENT](P105_UMP流消息状态.md#gaa53b5c80022e1888515f2c0616d9cfc3)。

<a id="r_gac9673eeb745526fd27f0e213ee06caa5"></a>

```c
#define UMP_STREAM_STATUS_EP_NAME 0x03
```

端点名称通知（Endpoint Name Notification）。

相关声明：[UMP_STREAM_STATUS_EP_NAME](P105_UMP流消息状态.md#gac9673eeb745526fd27f0e213ee06caa5)。

<a id="r_ga0edc8d182d71946828609b964bae1da8"></a>

```c
#define UMP_STREAM_STATUS_PROD_ID 0x04
```

产品实例标识通知消息（Product Instance ID Notification Message）。

相关声明：[UMP_STREAM_STATUS_PROD_ID](P105_UMP流消息状态.md#ga0edc8d182d71946828609b964bae1da8)。

<a id="r_gaf28a14d200e97003c248ca1ad452244a"></a>

```c
#define UMP_STREAM_STATUS_CONF_REQ 0x05
```

流配置请求消息（Stream Configuration Request Message）。

相关声明：[UMP_STREAM_STATUS_CONF_REQ](P105_UMP流消息状态.md#gaf28a14d200e97003c248ca1ad452244a)。

<a id="r_ga182a95d09f4bef5976a64e5e02938ff8"></a>

```c
#define UMP_STREAM_STATUS_CONF_NOTIF 0x06
```

流配置通知消息（Stream Configuration Notification Message）。

相关声明：[UMP_STREAM_STATUS_CONF_NOTIF](P105_UMP流消息状态.md#ga182a95d09f4bef5976a64e5e02938ff8)。

<a id="r_gae0e25c309feb67ea77046a7587017b07"></a>

```c
#define UMP_STREAM_STATUS_FB_DISCOVERY 0x10
```

功能块发现消息（Function Block Discovery Message）。

相关声明：[UMP_STREAM_STATUS_FB_DISCOVERY](P105_UMP流消息状态.md#gae0e25c309feb67ea77046a7587017b07)。

<a id="r_ga4634c6db944bd4c582765f23fc7a4f35"></a>

```c
#define UMP_STREAM_STATUS_FB_INFO 0x11
```

功能块信息通知（Function Block Info Notification）。

相关声明：[UMP_STREAM_STATUS_FB_INFO](P105_UMP流消息状态.md#ga4634c6db944bd4c582765f23fc7a4f35)。

<a id="r_gaabf613ea856aa266cfdf13a32f300eee"></a>

```c
#define UMP_STREAM_STATUS_FB_NAME 0x12
```

功能块名称通知（Function Block Name Notification）。

相关声明：[UMP_STREAM_STATUS_FB_NAME](P105_UMP流消息状态.md#gaabf613ea856aa266cfdf13a32f300eee)。

## 105.3\_详细说明（Detailed Documentation）

<a id="ga182a95d09f4bef5976a64e5e02938ff8"></a>

### 105.3.1\_`UMP\_STREAM\_STATUS\_CONF\_NOTIF`

```c
#define UMP_STREAM_STATUS_CONF_NOTIF 0x06
```

```c
#include <zephyr/audio/midi.h>
```

流配置通知消息（Stream Configuration Notification Message）。

<a id="gaf28a14d200e97003c248ca1ad452244a"></a>

### 105.3.2\_`UMP\_STREAM\_STATUS\_CONF\_REQ`

```c
#define UMP_STREAM_STATUS_CONF_REQ 0x05
```

```c
#include <zephyr/audio/midi.h>
```

流配置请求消息（Stream Configuration Request Message）。

<a id="gaa53b5c80022e1888515f2c0616d9cfc3"></a>

### 105.3.3\_`UMP\_STREAM\_STATUS\_DEVICE\_IDENT`

```c
#define UMP_STREAM_STATUS_DEVICE_IDENT 0x02
```

```c
#include <zephyr/audio/midi.h>
```

设备身份通知消息（Device Identity Notification Message）。

<a id="gab753d923dd8a6045f85f5ac7032fd040"></a>

### 105.3.4\_`UMP\_STREAM\_STATUS\_EP\_DISCOVERY`

```c
#define UMP_STREAM_STATUS_EP_DISCOVERY 0x00
```

```c
#include <zephyr/audio/midi.h>
```

端点发现消息（Endpoint Discovery Message）。

<a id="ga1ff08a079dd9b84aa297ca73043342db"></a>

### 105.3.5\_`UMP\_STREAM\_STATUS\_EP\_INFO`

```c
#define UMP_STREAM_STATUS_EP_INFO 0x01
```

```c
#include <zephyr/audio/midi.h>
```

端点信息通知消息（Endpoint Info Notification Message）。

<a id="gac9673eeb745526fd27f0e213ee06caa5"></a>

### 105.3.6\_`UMP\_STREAM\_STATUS\_EP\_NAME`

```c
#define UMP_STREAM_STATUS_EP_NAME 0x03
```

```c
#include <zephyr/audio/midi.h>
```

端点名称通知（Endpoint Name Notification）。

<a id="gae0e25c309feb67ea77046a7587017b07"></a>

### 105.3.7\_`UMP\_STREAM\_STATUS\_FB\_DISCOVERY`

```c
#define UMP_STREAM_STATUS_FB_DISCOVERY 0x10
```

```c
#include <zephyr/audio/midi.h>
```

功能块发现消息（Function Block Discovery Message）。

<a id="ga4634c6db944bd4c582765f23fc7a4f35"></a>

### 105.3.8\_`UMP\_STREAM\_STATUS\_FB\_INFO`

```c
#define UMP_STREAM_STATUS_FB_INFO 0x11
```

```c
#include <zephyr/audio/midi.h>
```

功能块信息通知（Function Block Info Notification）。

<a id="gaabf613ea856aa266cfdf13a32f300eee"></a>

### 105.3.9\_`UMP\_STREAM\_STATUS\_FB\_NAME`

```c
#define UMP_STREAM_STATUS_FB_NAME 0x12
```

```c
#include <zephyr/audio/midi.h>
```

功能块名称通知（Function Block Name Notification）。

<a id="ga0edc8d182d71946828609b964bae1da8"></a>

### 105.3.10\_`UMP\_STREAM\_STATUS\_PROD\_ID`

```c
#define UMP_STREAM_STATUS_PROD_ID 0x04
```

```c
#include <zephyr/audio/midi.h>
```

产品实例标识通知消息（Product Instance ID Notification Message）。

## 105.4\_源码跟踪与使用边界

译注依据保存的[官方MIDI头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/audio/midi.h)，摘要见[来源记录](../SOURCES.md)。本仓库的[对应头文件](../../../include/zephyr/audio/midi.h)可用于源码跟踪，版本可能与网页不同；原注释存在疑点时，在相应条目旁给出核对依据。本批未执行固件构建或MIDI硬件测试。

<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

[上一章](P104_UMP流消息格式.md) · [返回大纲](大纲.md) · [下一章](P106_UMP端点发现过滤位.md)
