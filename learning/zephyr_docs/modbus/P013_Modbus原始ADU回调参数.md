---
id: learning.zephyr-docs.modbus.api-13
title: Modbus原始ADU回调参数
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__raw__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_Modbus原始ADU回调参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__raw__cb.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 13.1\_概述

原始应用数据单元回调参数（Raw ADU Callback Parameter）。

```c
#include <zephyr/modbus/modbus.h>
```

## 13.2\_成员说明（Field Documentation）

<a id="ab2904f52d7ec1e1a791380ddc334558d"></a>
<a id="r_ab2904f52d7ec1e1a791380ddc334558d"></a>

### `raw_tx_cb`

```c
modbus_raw_cb_t modbus_raw_cb::raw_tx_cb
```

用于发送原始ADU的回调函数（Callback Function）。

<a id="abfa01344b7fc37adb2a3b23d4cc9507f"></a>
<a id="r_abfa01344b7fc37adb2a3b23d4cc9507f"></a>

### `user_data`

```c
void* modbus_raw_cb::user_data
```

指向传递给回调函数的用户数据（User Data）的指针。

## 13.3\_来源与相关类型

此结构体文档由文件[zephyr/modbus/modbus.h](P009_Modbus头文件参考.md)生成。相关类型如下：

| 名称／声明 | 说明 |
| --- | --- |
| [modbus_adu](P011_Modbus应用数据单元.md) | 供内部使用，并用于支持原始应用数据单元（Raw Application Data Unit，Raw ADU）的帧结构体（Frame Structure）。 |
| [modbus_user_callbacks](P016_Modbus服务器用户回调.md) | Modbus服务器用户回调（Server User Callback）结构体。 |
| [modbus_serial_param](P014_Modbus串行线路参数.md) | Modbus串行线路参数（Serial Line Parameter）。 |
| [modbus_server_param](P015_Modbus服务器参数.md) | Modbus服务器参数（Server Parameter）。 |
| [modbus_raw_cb](P013_Modbus原始ADU回调参数.md) | 原始应用数据单元回调参数（Raw ADU Callback Parameter）。 |
| [modbus_iface_param](P012_Modbus接口参数.md) | 用户参数结构体，用于将Modbus接口配置为客户端（Client）或服务器（Server）。 |

回调的参数和返回值见[modbus_raw_cb_t](P008_Modbus完整API参考.md#ga6d74be1fffb9d5697fe5708827aa7ef1)。

<a id="pub-attribs"></a>
<a id="details"></a>
<a id="doc-variable-members"></a>
<a id="header-pub-attribs"></a>
<a id="header-details"></a>
<a id="header-doc-variable-members"></a>

[上一章](P012_Modbus接口参数.md) · [返回大纲](大纲.md) · [下一章](P014_Modbus串行线路参数.md)
