---
id: learning.zephyr-docs.modbus.api-16
title: Modbus服务器用户回调
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__user__callbacks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_Modbus服务器用户回调

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodbus__user__callbacks.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 16.1\_概述

Modbus服务器用户回调（Server User Callback）结构体。

```c
#include <zephyr/modbus/modbus.h>
```

## 16.2\_成员说明（Field Documentation）

<a id="a3353b3aa0ec073fb9031a5c151e9995b"></a>
<a id="r_a3353b3aa0ec073fb9031a5c151e9995b"></a>

### `coil_rd`

```c
int(* modbus_user_callbacks::coil_rd) (uint16_t addr, bool *state)
```

线圈读取回调（Coil Read Callback）。

<a id="a0dad31490d8b5d454f06a8b7805a09fd"></a>
<a id="r_a0dad31490d8b5d454f06a8b7805a09fd"></a>

### `coil_wr`

```c
int(* modbus_user_callbacks::coil_wr) (uint16_t addr, bool state)
```

线圈写入回调（Coil Write Callback）。

<a id="aa6fd8fc2663c6a982ec17a162ae56961"></a>
<a id="r_aa6fd8fc2663c6a982ec17a162ae56961"></a>

### `discrete_input_rd`

```c
int(* modbus_user_callbacks::discrete_input_rd) (uint16_t addr, bool *state)
```

离散输入读取回调（Discrete Input Read Callback）。

<a id="acf5fe90fab9765bd83d1ab2075d073a2"></a>
<a id="r_acf5fe90fab9765bd83d1ab2075d073a2"></a>

### `holding_reg_rd`

```c
int(* modbus_user_callbacks::holding_reg_rd) (uint16_t addr, uint16_t *reg)
```

保持寄存器读取回调（Holding Register Read Callback）。

<a id="a821e0aacd7c90eff5e7c0047cc88a855"></a>
<a id="r_a821e0aacd7c90eff5e7c0047cc88a855"></a>

### `holding_reg_rd_fp`

```c
int(* modbus_user_callbacks::holding_reg_rd_fp) (uint16_t addr, float *reg)
```

浮点保持寄存器读取回调（Floating Point Holding Register Read Callback）。

<a id="a4ca1ed4bfc93b36d939f847d7ac9f8da"></a>
<a id="r_a4ca1ed4bfc93b36d939f847d7ac9f8da"></a>

### `holding_reg_wr`

```c
int(* modbus_user_callbacks::holding_reg_wr) (uint16_t addr, uint16_t reg)
```

保持寄存器写入回调（Holding Register Write Callback）。

<a id="a333b5781c35e781e7021f53d5a357482"></a>
<a id="r_a333b5781c35e781e7021f53d5a357482"></a>

### `holding_reg_wr_fp`

```c
int(* modbus_user_callbacks::holding_reg_wr_fp) (uint16_t addr, float reg)
```

浮点保持寄存器写入回调（Floating Point Holding Register Write Callback）。

<a id="a91a9270bd945935b74c6f5e021429d42"></a>
<a id="r_a91a9270bd945935b74c6f5e021429d42"></a>

### `input_reg_rd`

```c
int(* modbus_user_callbacks::input_reg_rd) (uint16_t addr, uint16_t *reg)
```

输入寄存器读取回调（Input Register Read Callback）。

<a id="ae315e76c3ceefbd65ef8cea500b43df5"></a>
<a id="r_ae315e76c3ceefbd65ef8cea500b43df5"></a>

### `input_reg_rd_fp`

```c
int(* modbus_user_callbacks::input_reg_rd_fp) (uint16_t addr, float *reg)
```

浮点输入寄存器读取回调（Floating Point Input Register Read Callback）。

## 16.3\_来源与相关类型

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

[上一章](P015_Modbus服务器参数.md) · [返回大纲](大纲.md)
