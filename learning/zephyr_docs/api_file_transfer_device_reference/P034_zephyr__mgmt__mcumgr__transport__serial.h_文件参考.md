---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-34
title: zephyr__mgmt__mcumgr__transport__serial.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_serial.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr串行传输（Serial Transport）API的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
```

查看此文件的源码。

MCUmgr串行传输（Serial Transport）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.1\_数据结构（Data Structures）

<a id="r_mcumgr_5Fserial_5Frx_5Fctxt"></a>

```c
struct mcumgr_serial_rx_ctxt
```

相关声明：[mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)。

维护传入mcumgr请求包（Request Packet）的状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 34.2\_宏定义（Macros）

<a id="r_ga67c8df024da7e6ff3ceaa06fc0b9b168"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT 0x0609
```

相关声明：[MCUMGR_SERIAL_HDR_PKT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

串行数据包头（Serial Packet Header）。

<a id="r_ga133a20780bbcd019b00c57d9e6da2884"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG 0x0414
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga133a20780bbcd019b00c57d9e6da2884)。

串行分片头（Serial Fragment Header）。

<a id="r_ga33ba8e4d44edccce44101888d69eea18"></a>

```c
#define MCUMGR_SERIAL_MAX_FRAME 127
```

相关声明：[MCUMGR_SERIAL_MAX_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga33ba8e4d44edccce44101888d69eea18)。

最大帧大小（Maximum Frame Size）。

<a id="r_gaa54b69e1d1440f957e0a5f7946487871"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT_1 (MCUMGR_SERIAL_HDR_PKT >> 8)
```

相关声明：[MCUMGR_SERIAL_HDR_PKT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaa54b69e1d1440f957e0a5f7946487871)、[MCUMGR_SERIAL_HDR_PKT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

数据包头（Packet Header）的第一个字节。

<a id="r_ga09386427eb67c2e07535b79eb8ca9fbc"></a>

```c
#define MCUMGR_SERIAL_HDR_PKT_2 (MCUMGR_SERIAL_HDR_PKT & 0xff)
```

相关声明：[MCUMGR_SERIAL_HDR_PKT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga09386427eb67c2e07535b79eb8ca9fbc)、[MCUMGR_SERIAL_HDR_PKT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga67c8df024da7e6ff3ceaa06fc0b9b168)。

数据包头（Packet Header）的第二个字节。

<a id="r_ga1edd532f85b7037096b2033b70ea5985"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG_1 (MCUMGR_SERIAL_HDR_FRAG >> 8)
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga1edd532f85b7037096b2033b70ea5985)、[MCUMGR_SERIAL_HDR_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga133a20780bbcd019b00c57d9e6da2884)。

分片头（Fragment Header）的第一个字节。

<a id="r_ga50ca5a231808ab473ea1d2fe89fd53f2"></a>

```c
#define MCUMGR_SERIAL_HDR_FRAG_2 (MCUMGR_SERIAL_HDR_FRAG & 0xff)
```

相关声明：[MCUMGR_SERIAL_HDR_FRAG_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga50ca5a231808ab473ea1d2fe89fd53f2)、[MCUMGR_SERIAL_HDR_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga133a20780bbcd019b00c57d9e6da2884)。

分片头（Fragment Header）的第二个字节。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 34.3\_类型定义（Typedefs）

<a id="r_ga49006881d527ebba84948a913a83c17e"></a>

```c
typedef int(* mcumgr_serial_tx_cb) (const void *data, int len)
```

相关声明：[mcumgr_serial_tx_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga49006881d527ebba84948a913a83c17e)。

发送一块原始响应数据（Raw Response Data）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.4\_函数（Functions）

<a id="r_gaa510a98df8b01ccf5bae8eacc9c59078"></a>

```c
struct net_buf * mcumgr_serial_process_frag (struct mcumgr_serial_rx_ctxt *rx_ctxt, const uint8_t *frag, int frag_len)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[mcumgr_serial_process_frag](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaa510a98df8b01ccf5bae8eacc9c59078)、[mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

处理经串行传输（Serial Transport）接收到的 mcumgr 请求分片（Request Fragment）。

<a id="r_gaca191e14700f0c2da9643e7daa582867"></a>

```c
int mcumgr_serial_tx_pkt (const uint8_t *data, int len, mcumgr_serial_tx_cb cb)
```

相关声明：[mcumgr_serial_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaca191e14700f0c2da9643e7daa582867)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mcumgr_serial_tx_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga49006881d527ebba84948a913a83c17e)。

对 mcumgr 数据包（Packet）编码并通过串行接口发送。


## 34.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P770_serial.h_源码浏览.md)
- [mcumgr_serial_rx_ctxt](../system_service_model_reference/P065_mcumgr_serial_rx_ctxt_结构体.md)
- [MCUMGR_SERIAL_HDR_PKT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga67c8df024da7e6ff3ceaa06fc0b9b168)
- [MCUMGR_SERIAL_HDR_FRAG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga133a20780bbcd019b00c57d9e6da2884)
- [MCUMGR_SERIAL_MAX_FRAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga33ba8e4d44edccce44101888d69eea18)
- [MCUMGR_SERIAL_HDR_PKT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaa54b69e1d1440f957e0a5f7946487871)
- [MCUMGR_SERIAL_HDR_PKT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga09386427eb67c2e07535b79eb8ca9fbc)
- [MCUMGR_SERIAL_HDR_FRAG_1](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga1edd532f85b7037096b2033b70ea5985)
- [MCUMGR_SERIAL_HDR_FRAG_2](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga50ca5a231808ab473ea1d2fe89fd53f2)
- [mcumgr_serial_tx_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#ga49006881d527ebba84948a913a83c17e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [mcumgr_serial_process_frag](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaa510a98df8b01ccf5bae8eacc9c59078)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mcumgr_serial_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__serial.html#gaca191e14700f0c2da9643e7daa582867)

<a id="header-details"></a>

---

[上一章](P033_zephyr__dt-bindings__sensor__rm3100.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__dt-bindings__pinctrl__stm32f1-pinctrl.h_文件参考.md)
