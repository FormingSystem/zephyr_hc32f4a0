---
id: learning.zephyr-docs.networking.api-85
title: TFTP头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tftp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_TFTP头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tftp_8h.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 85.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

TFTP客户端实现（Client Implementation）。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/net/socket.h>
```

TFTP客户端实现（Client Implementation）。

## 85.2\_数据结构（Data Structures）

<a id="r_tftp_5Fdata_5Fparam"></a>

```c
struct tftp_data_param
```

数据事件参数（Data Event Parameters）。

相关声明：[tftp_data_param](P090_TFTP数据参数.md)。

<a id="r_tftp_5Ferror_5Fparam"></a>

```c
struct tftp_error_param
```

错误事件参数（Error Event Parameters）。

相关声明：[tftp_error_param](P091_TFTP错误参数.md)。

<a id="r_tftp_5Fevt_5Fparam"></a>

```c
union tftp_evt_param
```

定义伴随异步事件一起通知给应用的事件参数（Event Parameters）。

相关声明：[tftp_evt_param](P089_TFTP事件参数联合体.md)。

<a id="r_tftp_5Fevt"></a>

```c
struct tftp_evt
```

定义通知给应用的TFTP异步事件（Asynchronous Event）。

相关声明：[tftp_evt](P088_TFTP事件.md)。

<a id="r_tftpc"></a>

```c
struct tftpc
```

TFTP客户端定义，用于保存与客户端相关的信息。

相关声明：[tftpc](P087_TFTP客户端上下文.md)。

## 85.3\_宏定义（Macros）

<a id="r_ga762c61f0d58a300c91f7577f65574dd5"></a>

```c
#define TFTP_BLOCK_SIZE 512
```

RFC 1350规定：文件按512字节的固定长度块（Fixed Length Block）发送。

相关声明：[TFTP_BLOCK_SIZE](P084_TFTP完整API参考.md#ga762c61f0d58a300c91f7577f65574dd5)。

<a id="r_ga0dbc6adc4cb9be4ea86fce61846c2089"></a>

```c
#define TFTP_HEADER_SIZE 4
```

RFC 1350规定：对于非请求类TFTP消息，报头（Header）由2字节操作码（Operation Code）以及2字节块号（Block Number）或错误码（Error Code）组成。

相关声明：[TFTP_HEADER_SIZE](P084_TFTP完整API参考.md#ga0dbc6adc4cb9be4ea86fce61846c2089)。

<a id="r_ga4387f92c6327823d655d8aa4f1c65beb"></a>

```c
#define TFTPC_MAX_BUF_SIZE (TFTP_BLOCK_SIZE + TFTP_HEADER_SIZE)
```

可发送或接收的最大数据量。

相关声明：[TFTPC_MAX_BUF_SIZE](P084_TFTP完整API参考.md#ga4387f92c6327823d655d8aa4f1c65beb)、[TFTP_BLOCK_SIZE](P084_TFTP完整API参考.md#ga762c61f0d58a300c91f7577f65574dd5)、[TFTP_HEADER_SIZE](P084_TFTP完整API参考.md#ga0dbc6adc4cb9be4ea86fce61846c2089)。

<a id="r_ga40d1c46aafbf6ea66daa5937ceb1152f"></a>

```c
#define TFTPC_SUCCESS 0
```

成功（Success）。

相关声明：[TFTPC_SUCCESS](P084_TFTP完整API参考.md#ga40d1c46aafbf6ea66daa5937ceb1152f)。

<a id="r_gac8b5e1f02de73c8cd42849ea0229eed2"></a>

```c
#define TFTPC_DUPLICATE_DATA -1
```

收到重复数据（Duplicate Data）。

相关声明：[TFTPC_DUPLICATE_DATA](P084_TFTP完整API参考.md#gac8b5e1f02de73c8cd42849ea0229eed2)。

<a id="r_ga5ac8121d18b8eceffe281281aca1b700"></a>

```c
#define TFTPC_BUFFER_OVERFLOW -2
```

用户缓冲区（User Buffer）太小。

相关声明：[TFTPC_BUFFER_OVERFLOW](P084_TFTP完整API参考.md#ga5ac8121d18b8eceffe281281aca1b700)。

<a id="r_ga30ad373e8531ba675165bb61620c9a07"></a>

```c
#define TFTPC_UNKNOWN_FAILURE -3
```

未知失败（Unknown Failure）。

相关声明：[TFTPC_UNKNOWN_FAILURE](P084_TFTP完整API参考.md#ga30ad373e8531ba675165bb61620c9a07)。

<a id="r_ga75729dcb0b640a6fcb2079151cd74f51"></a>

```c
#define TFTPC_REMOTE_ERROR -4
```

远端服务器错误（Remote Server Error）。

相关声明：[TFTPC_REMOTE_ERROR](P084_TFTP完整API参考.md#ga75729dcb0b640a6fcb2079151cd74f51)。

<a id="r_ga514eaf5d77587b8719801157adf20566"></a>

```c
#define TFTPC_RETRIES_EXHAUSTED -5
```

重试次数已用尽（Retries Exhausted）。

相关声明：[TFTPC_RETRIES_EXHAUSTED](P084_TFTP完整API参考.md#ga514eaf5d77587b8719801157adf20566)。

## 85.4\_类型定义（Typedefs）

<a id="r_gafc2d0fd730046b0d3781362263e68ddc"></a>

```c
typedef void(* tftp_callback_t) (const struct tftp_evt *evt)
```

由应用注册的TFTP事件通知回调（Event Notification Callback）。

相关声明：[tftp_callback_t](P084_TFTP完整API参考.md#gafc2d0fd730046b0d3781362263e68ddc)、[tftp_evt](P088_TFTP事件.md)。

## 85.5\_枚举（Enumerations）

<a id="r_ga1ee3d814c6fbaf5570eb5fd9605af7ea"></a>

```c
enum tftp_evt_type { TFTP_EVT_DATA , TFTP_EVT_ERROR }
```

模块通过应用注册的回调，将TFTP异步事件（Asynchronous Events）通知给应用。

相关声明：[tftp_evt_type](P084_TFTP完整API参考.md#ga1ee3d814c6fbaf5570eb5fd9605af7ea)、[TFTP_EVT_DATA](P084_TFTP完整API参考.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d)、[TFTP_EVT_ERROR](P084_TFTP完整API参考.md#gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3)。

## 85.6\_函数（Functions）

<a id="r_ga067de19b4089fbd2c2e49e925b73cfb0"></a>

```c
int tftp_get (struct tftpc *client, const char *remote_file, const char *mode)
```

此函数从远端服务器的“文件”（File）中获取数据。

相关声明：[tftp_get](P084_TFTP完整API参考.md#ga067de19b4089fbd2c2e49e925b73cfb0)、[tftpc](P087_TFTP客户端上下文.md)。

<a id="r_ga692f6a51f2ecd5c3d673ff64f59294b9"></a>

```c
int tftp_put (struct tftpc *client, const char *remote_file, const char *mode, const uint8_t *user_buf, uint32_t user_buf_size)
```

此函数将数据写入远端服务器的“文件”（File）。

相关声明：[tftp_put](P084_TFTP完整API参考.md#ga692f6a51f2ecd5c3d673ff64f59294b9)、[tftpc](P087_TFTP客户端上下文.md)。

## 85.7\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="define-members-0"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P084_TFTP完整API参考.md) · [返回大纲](大纲.md) · [下一章](P086_TFTP头文件源码.md)
