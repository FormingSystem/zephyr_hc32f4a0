---
id: learning.zephyr-docs.api-file-runtime-reference.page-18
title: zephyr__net__hdlc_rcp_if__hdlc_rcp_if.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_net\_\_hdlc\_rcp\_if\_\_hdlc\_rcp\_if.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hdlc__rcp__if_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HDLC RCP通信接口（Communication Interface）的公共API。

<a id="details"></a>

```c
#include <zephyr/sys/util.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

高级数据链路控制无线电协处理器通信接口（HDLC RCP Communication Interface）的公共 API。本文件提供供 RCP 主机（Host）使用的 HDLC API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

<a id="r_hdlc_5Fapi"></a>

```c
struct hdlc_api
```

相关声明：[hdlc_api](../network_service_model_reference/P023_hdlc_api_结构体.md)。

高级数据链路控制（HDLC）接口的配置数据。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.2\_类型定义（Typedefs）

<a id="r_a31b4a1434d2faad2878344367caf1b53"></a>

```c
typedef void(* hdlc_rx_callback_t) (const uint8_t *data, uint16_t len, void *param)
```

相关声明：[hdlc_rx_callback_t](#a31b4a1434d2faad2878344367caf1b53)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

OpenThread 无线电协处理器的 HDLC 接收回调函数（OT RCP HDLC RX Callback Function）。

## 18.3\_详细说明（Detailed Documentation）

<a id="a31b4a1434d2faad2878344367caf1b53"></a>

### `hdlc_rx_callback_t`

```c
typedef void(* hdlc_rx_callback_t) (const uint8_t *data, uint16_t len, void *param)
```

OpenThread 无线电协处理器的 HDLC 接收回调函数（OT RCP HDLC RX Callback Function）。

**说明（Note）**：注意（Note）：本函数在无线电 Spinel 的 HDLC 层（Radio Spinel HDLC Level）调用。


## 18.4\_原页交叉引用（Cross References）

- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P086_hdlc_rcp_if.h_源码浏览.md)
- [hdlc_api](../network_service_model_reference/P023_hdlc_api_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P017_zephyr__bluetooth__hci_vs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__i3c__hdr_ddr.h_文件参考.md)
