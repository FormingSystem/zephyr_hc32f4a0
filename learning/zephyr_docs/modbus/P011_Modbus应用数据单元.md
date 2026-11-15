---
id: learning.zephyr-docs.modbus.api-11
title: Modbus应用数据单元
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__adu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Modbus应用数据单元

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__adu.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 11.1\_概述

供内部使用，并用于支持原始应用数据单元（Raw Application Data Unit，Raw ADU）的帧结构体（Frame Structure）。

```c
#include <zephyr/modbus/modbus.h>
```

## 11.2\_成员说明（Field Documentation）

<a id="a78b8008e05c8d588d0ecba71e432d14e"></a>
<a id="r_a78b8008e05c8d588d0ecba71e432d14e"></a>

### `crc`

```c
uint16_t modbus_adu::crc
```

RTU循环冗余校验（Cyclic Redundancy Check，CRC）。

<a id="a7e94e4a0557717445ab2d791f8a97b7b"></a>
<a id="r_a7e94e4a0557717445ab2d791f8a97b7b"></a>

### `data`

```c
uint8_t modbus_adu::data[CONFIG_MODBUS_BUFFER_SIZE - 4]
```

事务数据（Transaction Data）。

<a id="a015e7b842349dc5567cc51cbf1f87420"></a>
<a id="r_a015e7b842349dc5567cc51cbf1f87420"></a>

### `fc`

```c
uint8_t modbus_adu::fc
```

功能码（Function Code）。

<a id="aa33f175677a0100c1f8a84a72c5ca247"></a>
<a id="r_aa33f175677a0100c1f8a84a72c5ca247"></a>

### `length`

```c
uint16_t modbus_adu::length
```

仅数据部分的长度（Data Length），不是单元标识符加协议数据单元（Unit ID + Protocol Data Unit，PDU）的总长度。

<a id="ae0422aacfe323ce6ca83069a54315fa0"></a>
<a id="r_ae0422aacfe323ce6ca83069a54315fa0"></a>

### `proto_id`

```c
uint16_t modbus_adu::proto_id
```

协议标识符（Protocol Identifier）。

<a id="a04f0aa95985cc491649ba47f8ba064c8"></a>
<a id="r_a04f0aa95985cc491649ba47f8ba064c8"></a>

### `trans_id`

```c
uint16_t modbus_adu::trans_id
```

事务标识符（Transaction Identifier）。

<a id="ab1fc3e76f3f406c8a0715055088d290d"></a>
<a id="r_ab1fc3e76f3f406c8a0715055088d290d"></a>

### `unit_id`

```c
uint8_t modbus_adu::unit_id
```

单元标识符（Unit Identifier）。

## 11.3\_来源与相关类型

此结构体文档由文件[zephyr/modbus/modbus.h](P009_Modbus头文件参考.md)生成。相关类型如下：

| 名称／声明 | 说明 |
| --- | --- |
| [modbus_adu](P011_Modbus应用数据单元.md) | 供内部使用，并用于支持原始应用数据单元（Raw Application Data Unit，Raw ADU）的帧结构体（Frame Structure）。 |
| [modbus_user_callbacks](P016_Modbus服务器用户回调.md) | Modbus服务器用户回调（Server User Callback）结构体。 |
| [modbus_serial_param](P014_Modbus串行线路参数.md) | Modbus串行线路参数（Serial Line Parameter）。 |
| [modbus_server_param](P015_Modbus服务器参数.md) | Modbus服务器参数（Server Parameter）。 |
| [modbus_raw_cb](P013_Modbus原始ADU回调参数.md) | 原始应用数据单元回调参数（Raw ADU Callback Parameter）。 |
| [modbus_iface_param](P012_Modbus接口参数.md) | 用户参数结构体，用于将Modbus接口配置为客户端（Client）或服务器（Server）。 |

<a id="pub-attribs"></a>
<a id="details"></a>
<a id="doc-variable-members"></a>
<a id="header-pub-attribs"></a>
<a id="header-details"></a>
<a id="header-doc-variable-members"></a>

[上一章](P010_Modbus头文件源码.md) · [返回大纲](大纲.md) · [下一章](P012_Modbus接口参数.md)
