---
id: learning.zephyr-docs.networking.api-84
title: TFTP完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tftp__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第84章\_TFTP完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tftp__client.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 84.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

引入版本（Since）：2.3；API版本（Version）：`0.1.0`。

## 84.2\_数据结构（Data Structures）

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

## 84.3\_宏定义（Macros）

<a id="r_ga762c61f0d58a300c91f7577f65574dd5"></a>

```c
#define TFTP_BLOCK_SIZE 512
```

RFC 1350规定：文件按512字节的固定长度块（Fixed Length Block）发送。

<a id="r_ga0dbc6adc4cb9be4ea86fce61846c2089"></a>

```c
#define TFTP_HEADER_SIZE 4
```

RFC 1350规定：对于非请求类TFTP消息，报头（Header）由2字节操作码（Operation Code）以及2字节块号（Block Number）或错误码（Error Code）组成。

<a id="r_ga4387f92c6327823d655d8aa4f1c65beb"></a>

```c
#define TFTPC_MAX_BUF_SIZE (TFTP_BLOCK_SIZE + TFTP_HEADER_SIZE)
```

可发送或接收的最大数据量。

## 84.4\_类型定义（Typedefs）

<a id="r_gafc2d0fd730046b0d3781362263e68ddc"></a>

```c
typedef void(* tftp_callback_t) (const struct tftp_evt *evt)
```

由应用注册的TFTP事件通知回调（Event Notification Callback）。

相关声明：[tftp_evt](P088_TFTP事件.md)。

## 84.5\_枚举（Enumerations）

<a id="r_ga1ee3d814c6fbaf5570eb5fd9605af7ea"></a>

```c
enum tftp_evt_type { TFTP_EVT_DATA , TFTP_EVT_ERROR }
```

模块通过应用注册的回调，将TFTP异步事件（Asynchronous Events）通知给应用。

## 84.6\_函数（Functions）

<a id="r_ga067de19b4089fbd2c2e49e925b73cfb0"></a>

```c
int tftp_get (struct tftpc *client, const char *remote_file, const char *mode)
```

此函数从远端服务器的“文件”（File）中获取数据。

相关声明：[tftpc](P087_TFTP客户端上下文.md)。

<a id="r_ga692f6a51f2ecd5c3d673ff64f59294b9"></a>

```c
int tftp_put (struct tftpc *client, const char *remote_file, const char *mode, const uint8_t *user_buf, uint32_t user_buf_size)
```

此函数将数据写入远端服务器的“文件”（File）。

相关声明：[tftpc](P087_TFTP客户端上下文.md)。

## 84.7\_TFTP客户端错误码（Client Error Codes）

<a id="r_ga40d1c46aafbf6ea66daa5937ceb1152f"></a>

```c
#define TFTPC_SUCCESS 0
```

成功（Success）。

<a id="r_gac8b5e1f02de73c8cd42849ea0229eed2"></a>

```c
#define TFTPC_DUPLICATE_DATA -1
```

收到重复数据（Duplicate Data）。

<a id="r_ga5ac8121d18b8eceffe281281aca1b700"></a>

```c
#define TFTPC_BUFFER_OVERFLOW -2
```

用户缓冲区（User Buffer）太小。

<a id="r_ga30ad373e8531ba675165bb61620c9a07"></a>

```c
#define TFTPC_UNKNOWN_FAILURE -3
```

未知失败（Unknown Failure）。

<a id="r_ga75729dcb0b640a6fcb2079151cd74f51"></a>

```c
#define TFTPC_REMOTE_ERROR -4
```

远端服务器错误（Remote Server Error）。

<a id="r_ga514eaf5d77587b8719801157adf20566"></a>

```c
#define TFTPC_RETRIES_EXHAUSTED -5
```

重试次数已用尽（Retries Exhausted）。

## 84.8\_详细说明（Detailed Documentation）

<a id="ga762c61f0d58a300c91f7577f65574dd5"></a>

### `TFTP_BLOCK_SIZE`

```c
#define TFTP_BLOCK_SIZE 512
```

```c
#include <zephyr/net/tftp.h>
```

RFC 1350规定：文件按512字节的固定长度块（Fixed Length Block）发送。

每个数据包包含一个数据块，必须先收到确认包（Acknowledgment Packet）才能发送下一包。数据长度小于512字节的数据包表示传输结束。

<a id="ga0dbc6adc4cb9be4ea86fce61846c2089"></a>

### `TFTP_HEADER_SIZE`

```c
#define TFTP_HEADER_SIZE 4
```

```c
#include <zephyr/net/tftp.h>
```

RFC 1350规定：对于非请求类TFTP消息，报头（Header）由2字节操作码（Operation Code）以及2字节块号（Block Number）或错误码（Error Code）组成。

<a id="ga5ac8121d18b8eceffe281281aca1b700"></a>

### `TFTPC_BUFFER_OVERFLOW`

```c
#define TFTPC_BUFFER_OVERFLOW -2
```

```c
#include <zephyr/net/tftp.h>
```

用户缓冲区（User Buffer）太小。

<a id="gac8b5e1f02de73c8cd42849ea0229eed2"></a>

### `TFTPC_DUPLICATE_DATA`

```c
#define TFTPC_DUPLICATE_DATA -1
```

```c
#include <zephyr/net/tftp.h>
```

收到重复数据（Duplicate Data）。

<a id="ga4387f92c6327823d655d8aa4f1c65beb"></a>

### `TFTPC_MAX_BUF_SIZE`

```c
#define TFTPC_MAX_BUF_SIZE (TFTP_BLOCK_SIZE + TFTP_HEADER_SIZE)
```

```c
#include <zephyr/net/tftp.h>
```

可发送或接收的最大数据量。

<a id="ga75729dcb0b640a6fcb2079151cd74f51"></a>

### `TFTPC_REMOTE_ERROR`

```c
#define TFTPC_REMOTE_ERROR -4
```

```c
#include <zephyr/net/tftp.h>
```

远端服务器错误（Remote Server Error）。

<a id="ga514eaf5d77587b8719801157adf20566"></a>

### `TFTPC_RETRIES_EXHAUSTED`

```c
#define TFTPC_RETRIES_EXHAUSTED -5
```

```c
#include <zephyr/net/tftp.h>
```

重试次数已用尽（Retries Exhausted）。

<a id="ga40d1c46aafbf6ea66daa5937ceb1152f"></a>

### `TFTPC_SUCCESS`

```c
#define TFTPC_SUCCESS 0
```

```c
#include <zephyr/net/tftp.h>
```

成功（Success）。

<a id="ga30ad373e8531ba675165bb61620c9a07"></a>

### `TFTPC_UNKNOWN_FAILURE`

```c
#define TFTPC_UNKNOWN_FAILURE -3
```

```c
#include <zephyr/net/tftp.h>
```

未知失败（Unknown Failure）。

<a id="gafc2d0fd730046b0d3781362263e68ddc"></a>

### `tftp_callback_t`

```c
typedef void(* tftp_callback_t) (const struct tftp_evt *evt)
```

```c
#include <zephyr/net/tftp.h>
```

由应用注册的TFTP事件通知回调（Event Notification Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] evt` | 事件描述，以及结果和关联参数（如有）。 |

> 译注（源码核对）：当前实现直接调用回调，并使用局部事件结构体；数据指针和错误消息指向客户端内部复用缓冲区。回调若需在返回后继续使用这些内容，应复制到应用拥有的存储中。原文的“异步事件”不表示GET／PUT函数本身非阻塞。

<a id="ga1ee3d814c6fbaf5570eb5fd9605af7ea"></a>

### `tftp_evt_type`

```c
enum tftp_evt_type
```

```c
#include <zephyr/net/tftp.h>
```

模块通过应用注册的回调，将TFTP异步事件（Asynchronous Events）通知给应用。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TFTP_EVT_DATA` | 从远端服务器收到数据时产生DATA事件（Data Event）。注意：DATA事件结构体包含有效载荷数据（Payload Data）及其大小。 |
| `TFTP_EVT_ERROR` | 从远端服务器收到错误时产生ERROR事件（Error Event）。注意：ERROR事件结构体包含错误码及错误消息。 |

<a id="ga067de19b4089fbd2c2e49e925b73cfb0"></a>

### `tftp_get()`

```c
int tftp_get ( struct tftpc * client, const char * remote_file, const char * mode )
```

```c
#include <zephyr/net/tftp.h>
```

此函数从远端服务器的“文件”（File）中获取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 类型为`tftpc`的客户端信息（Client Information）。 |
| `remote_file` | 要获取的远端文件名称。 |
| `mode` | TFTP客户端的模式（Mode）设置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `TFTPC_BUFFER_OVERFLOW` | 文件大于用户缓冲区。 |
| `TFTPC_REMOTE_ERROR` | 服务器未能处理本客户端的请求。 |
| `TFTPC_RETRIES_EXHAUSTED` | 客户端等待服务器时超时。 |
| `-EINVAL` | `client`为`NULL`，或者`remote_file`或`mode`过长、无法装入一个请求。在此情况下不会发送任何内容。 |

**返回（Returns）**：操作成功完成时，返回接收到的数据量。

**注意（Note）**：此函数会阻塞（Block），直到传输完成或发生网络错误。在函数返回之前，必须确保客户端结构体完整有效。

> 译注（源码核对）：原文的`TFTPC_BUFFER_OVERFLOW`说明按原样保留。当前[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/tftp/tftp_client.c)在`client->callback == NULL`且收到数据时发送磁盘已满错误并返回该值；此接口没有接收整份文件的用户缓冲区参数。正常接收通过回调逐块交付，不应据这句原注释推断“文件必须放入一个512字节缓冲区”。

> 译注（源码核对）：`mode == NULL`时实现默认使用`octet`；`remote_file`必须是有效的字符串指针，不能因`-EINVAL`条目只列出部分检查就假定空文件名指针也会被安全处理。

<a id="ga692f6a51f2ecd5c3d673ff64f59294b9"></a>

### `tftp_put()`

```c
int tftp_put ( struct tftpc * client, const char * remote_file, const char * mode, const uint8_t * user_buf, uint32_t user_buf_size )
```

```c
#include <zephyr/net/tftp.h>
```

此函数将数据写入远端服务器的“文件”（File）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 类型为`tftpc`的客户端信息（Client Information）。 |
| `remote_file` | 要写入的远端文件名称。 |
| `mode` | TFTP客户端的模式（Mode）设置。 |
| `user_buf` | 包含待写入数据的数据缓冲区。 |
| `user_buf_size` | 待写入数据的长度。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `TFTPC_REMOTE_ERROR` | 服务器未能处理本客户端的请求。 |
| `TFTPC_RETRIES_EXHAUSTED` | 客户端等待服务器时超时。 |
| `-EINVAL` | `client`或`user_buf`为`NULL`、`user_buf_size`为零，或者`remote_file`或`mode`过长、无法装入一个请求。在此情况下不会发送任何内容。 |

**返回（Returns）**：操作成功完成时，返回发送的数据量。

**注意（Note）**：此函数会阻塞（Block），直到传输完成或发生网络错误。在函数返回之前，必须确保客户端结构体完整有效。

> 译注（源码核对）：`mode == NULL`时实现默认使用`octet`；`remote_file`必须是有效的字符串指针，不能因`-EINVAL`条目只列出部分检查就假定空文件名指针也会被安全处理。

## 84.9\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="header-member-group"></a>
<a id="member-group"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1ee3d814c6fbaf5570eb5fd9605af7eaa7bd0226d62c9b49a8381705bc1d5875d"></a>
<a id="gga1ee3d814c6fbaf5570eb5fd9605af7eaa317d58f986f6f2f65b44fdaa5b655eb3"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P083_FTP客户端上下文.md) · [返回大纲](大纲.md) · [下一章](P085_TFTP头文件参考.md)
