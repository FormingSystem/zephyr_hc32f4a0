---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-11
title: 串行传输（Serial transport）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_串行传输（Serial transport）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

允许通过串行连接使用 MCUmgr SMP 协议。

<a id="details"></a>

允许通过串行连接使用 MCUmgr SMP 协议。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_serial_2Eh"></a>

```c
file serial.h
```

相关声明：[serial.h](../api_file_transfer_device_reference/P034_zephyr__mgmt__mcumgr__transport__serial.h_文件参考.md)。

MCUmgr串行传输（Serial Transport）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

<a id="r_mcumgr_5Fserial_5Frx_5Fctxt"></a>

```c
struct mcumgr_serial_rx_ctxt
```

相关声明：[mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)。

维护传入mcumgr请求包（Request Packet）的状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.3\_宏定义（Macros）

<a id="r_ga67c8df024da7e6ff3ceaa06fc0b9b168"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT 0x0609
```

相关声明：[MCUMGR_SERIAL_HDR_PKT](#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

串行数据包头（Serial Packet Header）。

<a id="r_ga133a20780bbcd019b00c57d9e6da2884"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG 0x0414
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG](#ga133a20780bbcd019b00c57d9e6da2884)。

串行分片头（Serial Fragment Header）。

<a id="r_ga33ba8e4d44edccce44101888d69eea18"></a>

```c
#define MCUMGR_SERIAL_MAX_FRAME 127
```

相关声明：[MCUMGR_SERIAL_MAX_FRAME](#ga33ba8e4d44edccce44101888d69eea18)。

最大帧大小（Maximum Frame Size）。

<a id="r_gaa54b69e1d1440f957e0a5f7946487871"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT_1 (MCUMGR_SERIAL_HDR_PKT >> 8)
```

相关声明：[MCUMGR_SERIAL_HDR_PKT_1](#gaa54b69e1d1440f957e0a5f7946487871)、[MCUMGR_SERIAL_HDR_PKT](#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

数据包头（Packet Header）的第一个字节。

<a id="r_ga09386427eb67c2e07535b79eb8ca9fbc"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT_2 (MCUMGR_SERIAL_HDR_PKT & 0xff)
```

相关声明：[MCUMGR_SERIAL_HDR_PKT_2](#ga09386427eb67c2e07535b79eb8ca9fbc)、[MCUMGR_SERIAL_HDR_PKT](#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

数据包头（Packet Header）的第二个字节。

<a id="r_ga1edd532f85b7037096b2033b70ea5985"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG_1 (MCUMGR_SERIAL_HDR_FRAG >> 8)
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG_1](#ga1edd532f85b7037096b2033b70ea5985)、[MCUMGR_SERIAL_HDR_FRAG](#ga133a20780bbcd019b00c57d9e6da2884)。

分片头（Fragment Header）的第一个字节。

<a id="r_ga50ca5a231808ab473ea1d2fe89fd53f2"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG_2 (MCUMGR_SERIAL_HDR_FRAG & 0xff)
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG_2](#ga50ca5a231808ab473ea1d2fe89fd53f2)、[MCUMGR_SERIAL_HDR_FRAG](#ga133a20780bbcd019b00c57d9e6da2884)。

分片头（Fragment Header）的第二个字节。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.4\_类型定义（Typedefs）

<a id="r_ga49006881d527ebba84948a913a83c17e"></a>

```c
typedef int(* mcumgr_serial_tx_cb) (const void *data, int len)
```

相关声明：[mcumgr_serial_tx_cb](#ga49006881d527ebba84948a913a83c17e)。

发送一块原始响应数据（Raw Response Data）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.5\_函数（Functions）

<a id="r_gaa510a98df8b01ccf5bae8eacc9c59078"></a>

```c
struct net_buf * mcumgr_serial_process_frag (struct mcumgr_serial_rx_ctxt *rx_ctxt, const uint8_t *frag, int frag_len)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[mcumgr_serial_process_frag](#gaa510a98df8b01ccf5bae8eacc9c59078)、[mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

处理经串行传输（Serial Transport）接收到的 mcumgr 请求分片（Request Fragment）。

<a id="r_gaca191e14700f0c2da9643e7daa582867"></a>

```c
int mcumgr_serial_tx_pkt (const uint8_t *data, int len, mcumgr_serial_tx_cb cb)
```

相关声明：[mcumgr_serial_tx_pkt](#gaca191e14700f0c2da9643e7daa582867)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcumgr_serial_tx_cb](#ga49006881d527ebba84948a913a83c17e)。

对 mcumgr 数据包（Packet）编码并通过串行接口发送。

## 11.6\_详细说明（Detailed Documentation）

<a id="ga133a20780bbcd019b00c57d9e6da2884"></a>

### `MCUMGR_SERIAL_HDR_FRAG`

```c
#define MCUMGR_SERIAL_HDR_FRAG 0x0414
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

串行分片头（Serial Fragment Header）。

<a id="ga1edd532f85b7037096b2033b70ea5985"></a>

### `MCUMGR_SERIAL_HDR_FRAG_1`

```c
#define MCUMGR_SERIAL_HDR_FRAG_1 (MCUMGR_SERIAL_HDR_FRAG >> 8)
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

分片头（Fragment Header）的第一个字节。

<a id="ga50ca5a231808ab473ea1d2fe89fd53f2"></a>

### `MCUMGR_SERIAL_HDR_FRAG_2`

```c
#define MCUMGR_SERIAL_HDR_FRAG_2 (MCUMGR_SERIAL_HDR_FRAG & 0xff)
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

分片头（Fragment Header）的第二个字节。

<a id="ga67c8df024da7e6ff3ceaa06fc0b9b168"></a>

### `MCUMGR_SERIAL_HDR_PKT`

```c
#define MCUMGR_SERIAL_HDR_PKT 0x0609
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

串行数据包头（Serial Packet Header）。

<a id="gaa54b69e1d1440f957e0a5f7946487871"></a>

### `MCUMGR_SERIAL_HDR_PKT_1`

```c
#define MCUMGR_SERIAL_HDR_PKT_1 (MCUMGR_SERIAL_HDR_PKT >> 8)
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

数据包头（Packet Header）的第一个字节。

<a id="ga09386427eb67c2e07535b79eb8ca9fbc"></a>

### `MCUMGR_SERIAL_HDR_PKT_2`

```c
#define MCUMGR_SERIAL_HDR_PKT_2 (MCUMGR_SERIAL_HDR_PKT & 0xff)
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

数据包头（Packet Header）的第二个字节。

<a id="ga33ba8e4d44edccce44101888d69eea18"></a>

### `MCUMGR_SERIAL_MAX_FRAME`

```c
#define MCUMGR_SERIAL_MAX_FRAME 127
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

最大帧大小（Maximum Frame Size）。

<a id="ga49006881d527ebba84948a913a83c17e"></a>

### `mcumgr_serial_tx_cb`

```c
typedef int(* mcumgr_serial_tx_cb) (const void *data, int len)
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

发送一块原始响应数据（Raw Response Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要发送的数据（Data）。 |
| `len` | 要发送的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。

<a id="gaa510a98df8b01ccf5bae8eacc9c59078"></a>

### `mcumgr_serial_process_frag()`

```c
struct net_buf * mcumgr_serial_process_frag ( struct mcumgr_serial_rx_ctxt * rx_ctxt, const uint8_t * frag, int frag_len )
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

处理经串行传输（Serial Transport）接收到的 mcumgr 请求分片（Request Fragment）。

处理通过串行传输（Serial Transport）收到的 mcumgr 请求分片（Request Fragment）。如果该分片是有效 mcumgr 请求的最后一部分，函数返回包含已解码请求的 `net_buf`。调用者负责在处理完毕后释放此 `net_buf`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx_ctxt` | 与所用串行传输（Serial Transport）关联的接收上下文（Receive Context）。 |
| `frag` | 要处理的传入分片（Incoming Fragment）。 |
| `frag_len` | 分片长度（Fragment Length），单位为字节。 |

**返回（Returns）**：**返回值（Returns）：**收到完整且有效的请求时，返回包含已解码请求的 `net_buf`；数据包不完整或无效时返回 `NULL`。

<a id="gaca191e14700f0c2da9643e7daa582867"></a>

### `mcumgr_serial_tx_pkt()`

```c
int mcumgr_serial_tx_pkt ( const uint8_t * data, int len, mcumgr_serial_tx_cb cb )
```

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

对 mcumgr 数据包（Packet）编码并通过串行接口发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要发送的 mcumgr 数据包数据（Packet Data）。 |
| `len` | 未编码的 mcumgr 数据包长度（Unencoded Packet Length）。 |
| `cb` | 用于发送原始字节（Raw Bytes）的回调。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 11.7\_原页交叉引用（Cross References）

- [serial.h](../api_file_transfer_device_reference/P034_zephyr__mgmt__mcumgr__transport__serial.h_文件参考.md)
- [mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_LIS2DS12 API主题.md) · [返回大纲](大纲.md) · [下一章](P012_MFD NPM13XX 接口.md)
