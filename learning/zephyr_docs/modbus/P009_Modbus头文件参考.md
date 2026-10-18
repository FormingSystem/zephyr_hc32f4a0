---
id: learning.zephyr-docs.modbus.api-9
title: Modbus头文件参考
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Modbus头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modbus_8h.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 9.1\_概述与包含文件

MODBUS传输协议应用程序编程接口（Transport Protocol API）的头文件。

```c
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/slist.h>
```

查看[本文件的官方源码浏览译页](P010_Modbus头文件源码.md)。以下保留本页全部声明和简介；参数、返回值与宏展开见[完整API参考](P008_Modbus完整API参考.md)。

## 9.2\_数据结构（Data Structures）

<a id="r_modbus_5Fadu"></a>

```c
struct modbus_adu
```

供内部使用，并用于支持原始应用数据单元（Raw Application Data Unit，Raw ADU）的帧结构体（Frame Structure）。

[详细说明](P011_Modbus应用数据单元.md)。

<a id="r_modbus_5Fuser_5Fcallbacks"></a>

```c
struct modbus_user_callbacks
```

Modbus服务器用户回调（Server User Callback）结构体。

[详细说明](P016_Modbus服务器用户回调.md)。

<a id="r_modbus_5Fserial_5Fparam"></a>

```c
struct modbus_serial_param
```

Modbus串行线路参数（Serial Line Parameter）。

[详细说明](P014_Modbus串行线路参数.md)。

<a id="r_modbus_5Fserver_5Fparam"></a>

```c
struct modbus_server_param
```

Modbus服务器参数（Server Parameter）。

[详细说明](P015_Modbus服务器参数.md)。

<a id="r_modbus_5Fraw_5Fcb"></a>

```c
struct modbus_raw_cb
```

原始应用数据单元回调参数（Raw ADU Callback Parameter）。

[详细说明](P013_Modbus原始ADU回调参数.md)。

<a id="r_modbus_5Fiface_5Fparam"></a>

```c
struct modbus_iface_param
```

用户参数结构体，用于将Modbus接口配置为客户端（Client）或服务器（Server）。

[详细说明](P012_Modbus接口参数.md)。

## 9.3\_宏与异常码（Macros and Exception Codes）

<a id="r_ga1015513d4d3b6621fc18dcfda79116a2"></a>

```c
#define MODBUS_MBAP_LENGTH 7
```

Modbus应用协议报头（Modbus Application Protocol Header，MBAP Header）的长度。

[详细说明](P008_Modbus完整API参考.md#ga1015513d4d3b6621fc18dcfda79116a2)。

<a id="r_gae8a6fcfc117e7c4b2ac32aef90155698"></a>

```c
#define MODBUS_MBAP_AND_FC_LENGTH (MODBUS_MBAP_LENGTH + 1)
```

MBAP报头加上功能码（Function Code）的长度。

[详细说明](P008_Modbus完整API参考.md#gae8a6fcfc117e7c4b2ac32aef90155698)。

<a id="r_gaa0acc60971d0f773719431173632fd30"></a>

```c
#define MODBUS_CUSTOM_FC_DEFINE(name, user_cb, user_fc, userdata)
```

初始化自定义功能码结构体（Custom Function Code Structure）的辅助宏。

[详细说明](P008_Modbus完整API参考.md#gaa0acc60971d0f773719431173632fd30)。

<a id="r_ga12557dda3e72ac45aefee3f9cbb18960"></a>

```c
#define MODBUS_EXC_NONE 0
```

无异常（No Exception）。

[详细说明](P008_Modbus完整API参考.md#ga12557dda3e72ac45aefee3f9cbb18960)。

<a id="r_ga934994f66a61c0d11d00dd52a748cc78"></a>

```c
#define MODBUS_EXC_ILLEGAL_FC 1
```

非法功能码（Illegal Function Code）。

[详细说明](P008_Modbus完整API参考.md#ga934994f66a61c0d11d00dd52a748cc78)。

<a id="r_ga9ab4fc4caaf2e051ae697d44a9fa98e3"></a>

```c
#define MODBUS_EXC_ILLEGAL_DATA_ADDR 2
```

非法数据地址（Illegal Data Address）。

[详细说明](P008_Modbus完整API参考.md#ga9ab4fc4caaf2e051ae697d44a9fa98e3)。

<a id="r_ga5bcd9c7edd91d59af1453cde2376412f"></a>

```c
#define MODBUS_EXC_ILLEGAL_DATA_VAL 3
```

非法数据值（Illegal Data Value）。

[详细说明](P008_Modbus完整API参考.md#ga5bcd9c7edd91d59af1453cde2376412f)。

<a id="r_ga6bcf75ff2d522f1a542caa41b47a5ac8"></a>

```c
#define MODBUS_EXC_SERVER_DEVICE_FAILURE 4
```

服务器设备故障（Server Device Failure）。

[详细说明](P008_Modbus完整API参考.md#ga6bcf75ff2d522f1a542caa41b47a5ac8)。

<a id="r_ga9cfec884c72b7fc404d82c16f57e858d"></a>

```c
#define MODBUS_EXC_ACK 5
```

确认（Acknowledge）。

[详细说明](P008_Modbus完整API参考.md#ga9cfec884c72b7fc404d82c16f57e858d)。

<a id="r_ga37f02ccee238e7c8ab33f150b2bcd793"></a>

```c
#define MODBUS_EXC_SERVER_DEVICE_BUSY 6
```

服务器设备忙（Server Device Busy）。

[详细说明](P008_Modbus完整API参考.md#ga37f02ccee238e7c8ab33f150b2bcd793)。

<a id="r_gad9b56cf73a31d77cd78d48695ea44659"></a>

```c
#define MODBUS_EXC_MEM_PARITY_ERROR 8
```

存储器奇偶校验错误（Memory Parity Error）。

[详细说明](P008_Modbus完整API参考.md#gad9b56cf73a31d77cd78d48695ea44659)。

<a id="r_ga9903d7d283c11a4b8854ef5706b5aaba"></a>

```c
#define MODBUS_EXC_GW_PATH_UNAVAILABLE 10
```

网关路径不可用（Gateway Path Unavailable）。

[详细说明](P008_Modbus完整API参考.md#ga9903d7d283c11a4b8854ef5706b5aaba)。

<a id="r_gae61e3ee73e2288006f3dd2f081b4d1de"></a>

```c
#define MODBUS_EXC_GW_TARGET_FAILED_TO_RESP 11
```

网关目标设备未响应（Gateway Target Device Failed to Respond）。

[详细说明](P008_Modbus完整API参考.md#gae61e3ee73e2288006f3dd2f081b4d1de)。

## 9.4\_类型定义（Typedefs）

<a id="r_ga6d74be1fffb9d5697fe5708827aa7ef1"></a>

```c
typedef int(* modbus_raw_cb_t) (const int iface, const struct modbus_adu *adu, void *user_data)
```

原始ADU回调函数（Raw ADU Callback）的函数签名。

[详细说明](P008_Modbus完整API参考.md#ga6d74be1fffb9d5697fe5708827aa7ef1)。

<a id="r_ga2a7ba41a2fb7f6bf5194c02dcab07ae3"></a>

```c
typedef bool(* modbus_custom_cb_t) (const int iface, const struct modbus_adu *const rx_adu, struct modbus_adu *const tx_adu, uint8_t *const excep_code, void *const user_data)
```

自定义功能码处理函数（Custom Function Code Handler）的函数签名。

[详细说明](P008_Modbus完整API参考.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)。

## 9.5\_枚举（Enumerations）

<a id="r_ga4bd8913e1c77a1e4b19585caa9f77c2e"></a>

```c
enum modbus_mode { MODBUS_MODE_RTU , MODBUS_MODE_ASCII , MODBUS_MODE_RAW }
```

Modbus接口模式（Interface Mode）。

[详细说明](P008_Modbus完整API参考.md#ga4bd8913e1c77a1e4b19585caa9f77c2e)。

## 9.6\_函数（Functions）

<a id="r_ga05b118dc87ebe3739cac4e9572104ffb"></a>

```c
int modbus_read_coils (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const coil_tbl, const uint16_t num_coils)
```

读取线圈（Coil Read，FC01）。

[详细说明](P008_Modbus完整API参考.md#ga05b118dc87ebe3739cac4e9572104ffb)。

<a id="r_ga921fd6036ff1b8a416dc02e30bb6e653"></a>

```c
int modbus_read_dinputs (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const di_tbl, const uint16_t num_di)
```

读取离散输入（Discrete Inputs，FC02）。

[详细说明](P008_Modbus完整API参考.md#ga921fd6036ff1b8a416dc02e30bb6e653)。

<a id="r_ga7d7221b32fbf2395e69e25ef2dbaa036"></a>

```c
int modbus_read_holding_regs (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs)
```

读取保持寄存器（Holding Registers，FC03）。

[详细说明](P008_Modbus完整API参考.md#ga7d7221b32fbf2395e69e25ef2dbaa036)。

<a id="r_ga5ff31ca21cf2d1b081d172228d6c2154"></a>

```c
int modbus_read_input_regs (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs)
```

读取输入寄存器（Input Registers，FC04）。

[详细说明](P008_Modbus完整API参考.md#ga5ff31ca21cf2d1b081d172228d6c2154)。

<a id="r_gaccac4f72b5d66a5a2e6c444dda251c41"></a>

```c
int modbus_write_coil (const int iface, const uint8_t unit_id, const uint16_t coil_addr, const bool coil_state)
```

写入单个线圈（Write Single Coil，FC05）。

[详细说明](P008_Modbus完整API参考.md#gaccac4f72b5d66a5a2e6c444dda251c41)。

<a id="r_gaf06d2553af8b8e9ab58f54b8b7e2055b"></a>

```c
int modbus_write_holding_reg (const int iface, const uint8_t unit_id, const uint16_t start_addr, const uint16_t reg_val)
```

写入单个保持寄存器（Write Single Holding Register，FC06）。

[详细说明](P008_Modbus完整API参考.md#gaf06d2553af8b8e9ab58f54b8b7e2055b)。

<a id="r_gac924251f66ca6f357d8b7d90075df210"></a>

```c
int modbus_request_diagnostic (const int iface, const uint8_t unit_id, const uint16_t sfunc, const uint16_t data, uint16_t *const data_out)
```

读取诊断（Diagnostic，FC08）。

[详细说明](P008_Modbus完整API参考.md#gac924251f66ca6f357d8b7d90075df210)。

<a id="r_gac0fa22cd0d1fa861fdbc04b65ea60d7e"></a>

```c
int modbus_write_coils (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const coil_tbl, const uint16_t num_coils)
```

写入多个线圈（Write Coils，FC15）。

[详细说明](P008_Modbus完整API参考.md#gac0fa22cd0d1fa861fdbc04b65ea60d7e)。

<a id="r_gadc8273292e0efc8c0d65c00eea7a22c5"></a>

```c
int modbus_write_holding_regs (const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs)
```

写入多个保持寄存器（Write Holding Registers，FC16）。

[详细说明](P008_Modbus完整API参考.md#gadc8273292e0efc8c0d65c00eea7a22c5)。

<a id="r_ga9a8ae6fb4b1aee398f5b19f074d07ea9"></a>

```c
int modbus_read_holding_regs_fp (const int iface, const uint8_t unit_id, const uint16_t start_addr, float *const reg_buf, const uint16_t num_regs)
```

读取浮点保持寄存器（Floating-point Holding Registers，FC03）。

[详细说明](P008_Modbus完整API参考.md#ga9a8ae6fb4b1aee398f5b19f074d07ea9)。

<a id="r_ga762da245db3ca4f60fb3aa6c5783c73d"></a>

```c
int modbus_write_holding_regs_fp (const int iface, const uint8_t unit_id, const uint16_t start_addr, float *const reg_buf, const uint16_t num_regs)
```

写入浮点保持寄存器（Write Floating-point Holding Registers，FC16）。

[详细说明](P008_Modbus完整API参考.md#ga762da245db3ca4f60fb3aa6c5783c73d)。

<a id="r_gaa17880a268d6b3b9553de835c800af27"></a>

```c
int modbus_iface_get_by_name (const char *iface_name)
```

根据接口名称获取Modbus接口索引（Interface Index）。

[详细说明](P008_Modbus完整API参考.md#gaa17880a268d6b3b9553de835c800af27)。

<a id="r_gae4d34276c467bf54e0849a1098e56f8b"></a>

```c
int modbus_init_server (const int iface, struct modbus_iface_param param)
```

将Modbus接口配置为原始ADU服务器（Raw ADU Server）。

[详细说明](P008_Modbus完整API参考.md#gae4d34276c467bf54e0849a1098e56f8b)。

<a id="r_ga943eff819ecf1bc268714783047888ef"></a>

```c
int modbus_init_client (const int iface, struct modbus_iface_param param)
```

将Modbus接口配置为原始ADU客户端（Raw ADU Client）。

[详细说明](P008_Modbus完整API参考.md#ga943eff819ecf1bc268714783047888ef)。

<a id="r_ga32a6319cc51eb5a98dcb58b3231b9d34"></a>

```c
int modbus_disable (const uint8_t iface)
```

禁用Modbus接口（Interface）。

[详细说明](P008_Modbus完整API参考.md#ga32a6319cc51eb5a98dcb58b3231b9d34)。

<a id="r_ga6d40e9eda6b8ead6d071d4192ffe489b"></a>

```c
int modbus_raw_submit_rx (const int iface, const struct modbus_adu *adu)
```

提交原始ADU（Raw ADU）。

[详细说明](P008_Modbus完整API参考.md#ga6d40e9eda6b8ead6d071d4192ffe489b)。

<a id="r_ga8fdae6a92e27a845296c9d8ce4b8078e"></a>

```c
void modbus_raw_put_header (const struct modbus_adu *adu, uint8_t *header)
```

将MBAP报头写入缓冲区。

[详细说明](P008_Modbus完整API参考.md#ga8fdae6a92e27a845296c9d8ce4b8078e)。

<a id="r_ga333072d3536d7b6f0680ceecc2c5bddf"></a>

```c
void modbus_raw_get_header (struct modbus_adu *adu, const uint8_t *header)
```

从缓冲区（Buffer）读取MBAP报头。

[详细说明](P008_Modbus完整API参考.md#ga333072d3536d7b6f0680ceecc2c5bddf)。

<a id="r_gad250c40ba13a7d8c9189de17d1fd31aa"></a>

```c
void modbus_raw_set_server_failure (struct modbus_adu *adu)
```

设置服务器设备故障异常（Server Device Failure Exception）。

[详细说明](P008_Modbus完整API参考.md#gad250c40ba13a7d8c9189de17d1fd31aa)。

<a id="r_ga7aa5dfd6e457980e9e9b8a77810ec31e"></a>

```c
int modbus_raw_backend_txn (const int iface, struct modbus_adu *adu)
```

使用接口作为后端（Backend）发送和接收ADU。

[详细说明](P008_Modbus完整API参考.md#ga7aa5dfd6e457980e9e9b8a77810ec31e)。

<a id="r_gacd88a4f35a13cc6864654927296803c4"></a>

```c
int modbus_register_user_fc (const int iface, struct modbus_custom_fc *custom_fc)
```

注册用户定义的功能码处理函数（User-defined Function Code Handler）。

[详细说明](P008_Modbus完整API参考.md#gacd88a4f35a13cc6864654927296803c4)。

## 9.7\_详细描述（Detailed Description）

MODBUS传输协议应用程序编程接口（Transport Protocol API）的头文件。

<a id="nested-classes"></a>
<a id="define-members"></a>
<a id="typedef-members"></a>
<a id="enum-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="define-members-0"></a>
<a id="header-nested-classes"></a>
<a id="header-define-members"></a>
<a id="header-typedef-members"></a>
<a id="header-enum-members"></a>
<a id="header-func-members"></a>
<a id="header-details"></a>

[上一章](P008_Modbus完整API参考.md) · [返回大纲](大纲.md) · [下一章](P010_Modbus头文件源码.md)
