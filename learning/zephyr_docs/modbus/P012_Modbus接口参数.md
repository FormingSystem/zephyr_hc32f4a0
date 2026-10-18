---
id: learning.zephyr-docs.modbus.api-12
title: Modbus接口参数
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__iface__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_Modbus接口参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__iface__param.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 12.1\_概述

用户参数结构体，用于将Modbus接口配置为客户端（Client）或服务器（Server）。

```c
#include <zephyr/modbus/modbus.h>
```

角色参数（Role-specific Parameters）与传输参数（Transport-specific Parameters）分别使用匿名联合体（Anonymous Union）。以下声明摘自同批官方[源码浏览页](P010_Modbus头文件源码.md)，用于保留成员之间的嵌套关系：

```c
struct modbus_iface_param {
        enum modbus_mode mode;
        union {
                struct modbus_server_param server;
                uint32_t rx_timeout;
        };
        union {
                struct modbus_serial_param serial;
                struct modbus_raw_cb rawcb;
        };
};
```

## 12.2\_成员说明（Field Documentation）

<a id="ad1051fdf8c0a8b094a98bb6f1d953530"></a>
<a id="r_ad1051fdf8c0a8b094a98bb6f1d953530"></a>

### `角色参数匿名联合体`

```c
union { ... } modbus_iface_param
```

接口的角色专用参数（Role-specific Parameter）。

<a id="af97ac97c4970ae077d8e10fa304817fa"></a>
<a id="r_af97ac97c4970ae077d8e10fa304817fa"></a>

### `传输参数匿名联合体`

```c
union { ... } modbus_iface_param
```

接口的传输专用参数（Transport-specific Parameter）。

<a id="ae73f218d8810afb0c2efbf865ba8b3ba"></a>
<a id="r_ae73f218d8810afb0c2efbf865ba8b3ba"></a>

### `mode`

```c
enum modbus_mode modbus_iface_param::mode
```

接口模式（Interface Mode）。

<a id="a6e06fe6fc4ba31b25b5ef461ee0e4f81"></a>

### `rawcb`

```c
struct modbus_raw_cb modbus_iface_param::rawcb
```

指向原始ADU回调函数的指针（Raw ADU Callback Function Pointer）。

> 译注：原文描述使用“Pointer”，但声明中的成员类型是`struct modbus_raw_cb`本身。该结构体保存回调函数及用户数据，详见[原始ADU回调参数](P013_Modbus原始ADU回调参数.md)；不要把`rawcb`当成直接的函数指针。

<a id="a7726b39e43e660adb63e24b4cf2e7ab7"></a>

### `rx_timeout`

```c
uint32_t modbus_iface_param::rx_timeout
```

客户端等待服务器响应的时长（Response Timeout）。

> 译注：本结构体页面没有给出时长单位；译文不自行补造单位。使用时应以所用源码版本的接口注释与实现为准。

<a id="a77ff747b2e789e96691483994be1d596"></a>

### `serial`

```c
struct modbus_serial_param modbus_iface_param::serial
```

接口的串行支持参数（Serial Support Parameter）。

<a id="a77d88f81d11b0f9338ca227930abf53d"></a>

### `server`

```c
struct modbus_server_param modbus_iface_param::server
```

接口的服务器参数（Server Parameter）。

## 12.3\_来源与相关类型

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
<a id="r_ac19139290fc9a4688aa40e08ee07521e"></a>
<a id="r_ad4cc7d68e98d80900ca45df5749a9fbc"></a>
<a id="r_a30849b465de44ffe245bc0e7365f9618"></a>
<a id="r_aa1bdf4a6aa1a4027b04f9c2d1af5e5f6"></a>
<a id="header-pub-attribs"></a>
<a id="header-details"></a>
<a id="header-doc-variable-members"></a>

[上一章](P011_Modbus应用数据单元.md) · [返回大纲](大纲.md) · [下一章](P013_Modbus原始ADU回调参数.md)
