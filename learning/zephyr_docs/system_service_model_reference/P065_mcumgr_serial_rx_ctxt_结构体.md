---
id: learning.zephyr-docs.system-service-model-reference.page-65
title: mcumgr_serial_rx_ctxt_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__serial__rx__ctxt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_mcumgr\_serial\_rx\_ctxt\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcumgr__serial__rx__ctxt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

维护传入mcumgr请求包（Request Packet）的状态。

```c
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

<a id="details"></a>

维护传入mcumgr请求包（Request Packet）的状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 65.1\_数据成员（Data Fields）

<a id="r_a5fdf2dd95185a49806c1900184c7bdfc"></a>

```c
struct net_buf * nb
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[nb](#a5fdf2dd95185a49806c1900184c7bdfc)。

包含已部分接收或完整接收的 mcumgr 请求。

<a id="r_a4ded2b7748334b0f3166f4c18cd1d6b0"></a>

```c
uint16_t pkt_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pkt_len](#a4ded2b7748334b0f3166f4c18cd1d6b0)。

从头部读取的完整数据包长度。

## 65.2\_详细说明（Detailed Documentation）

<a id="a5fdf2dd95185a49806c1900184c7bdfc"></a>

### `nb`

```c
struct net_buf* mcumgr_serial_rx_ctxt::nb
```

包含已部分接收或完整接收的 mcumgr 请求。

此缓冲区中存储的数据已经过 Base64 解码。

<a id="a4ded2b7748334b0f3166f4c18cd1d6b0"></a>

### `pkt_len`

```c
uint16_t mcumgr_serial_rx_ctxt::pkt_len
```

从头部读取的完整数据包长度。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/transport/serial.h`

## 65.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/serial.h](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h_source.html)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P064_mcumgr_image_upload_结构体.md) · [返回大纲](大纲.md) · [下一章](P066_mgmt_callback_结构体.md)
