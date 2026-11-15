---
id: learning.zephyr-docs.modbus.api-14
title: Modbus串行线路参数
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__serial__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_Modbus串行线路参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__serial__param.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 14.1\_概述

Modbus串行线路参数（Serial Line Parameter）。

```c
#include <zephyr/modbus/modbus.h>
```

## 14.2\_成员说明（Field Documentation）

<a id="af3989f5e20eb96080d456114ef4d86e5"></a>
<a id="r_af3989f5e20eb96080d456114ef4d86e5"></a>

### `baud`

```c
uint32_t modbus_serial_param::baud
```

串行线路的波特率（Baud Rate）。

<a id="a337a18f3ad923bf758cb432b9a2d8ada"></a>
<a id="r_a337a18f3ad923bf758cb432b9a2d8ada"></a>

### `parity`

```c
enum uart_config_parity modbus_serial_param::parity
```

`parity`：UART奇偶校验（Parity）设置，可取`UART_CFG_PARITY_NONE`、`UART_CFG_PARITY_EVEN`、`UART_CFG_PARITY_ODD`。

<a id="a35249f2fa65030e22ec2b221f872e06f"></a>
<a id="r_a35249f2fa65030e22ec2b221f872e06f"></a>

### `stop_bits`

```c
enum uart_config_stop_bits modbus_serial_param::stop_bits
```

`stop_bits`：非合规模式（Non-compliant Mode）下的UART停止位（Stop Bits）设置，可取`UART_CFG_STOP_BITS_0_5`、`UART_CFG_STOP_BITS_1`、`UART_CFG_STOP_BITS_1_5`、`UART_CFG_STOP_BITS_2`。

## 14.3\_来源与相关类型

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

[上一章](P013_Modbus原始ADU回调参数.md) · [返回大纲](大纲.md) · [下一章](P015_Modbus服务器参数.md)
