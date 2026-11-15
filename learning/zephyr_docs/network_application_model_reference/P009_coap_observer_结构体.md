---
id: learning.zephyr-docs.network-application-model-reference.page-9
title: coap_observer_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__observer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_coap\_observer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__observer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示正在观察（Observe）本地资源的远端设备。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

表示正在观察（Observe）本地资源的远端设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a24a9f853db17ff623f4c510fd0892eb5"></a>

```c
sys_snode_t list
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[list](#a24a9f853db17ff623f4c510fd0892eb5)。

观察者（Observer）的列表节点。

<a id="r_a5d5e9494804ef64bc705f2bb08ac7afd"></a>

```c
struct net_sockaddr_storage addr
```

相关声明：[addr](#a5d5e9494804ef64bc705f2bb08ac7afd)。

观察者连接端点（Connection End Point）的信息。

<a id="r_a6d7d792120b935bf61c739f95dd7361c"></a>

```c
uint8_t token [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[token](#a6d7d792120b935bf61c739f95dd7361c)。

观察者令牌（Observer Token）。

<a id="r_a901f148d2eb697206fde732050c3d8b4"></a>

```c
uint8_t tkl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tkl](#a901f148d2eb697206fde732050c3d8b4)。

扩展令牌长度（Extended Token Length）。

<a id="r_a7486199db30c9aaaba693ce64fd46879"></a>

```c
struct coap_oscore_context * oscore_ctx
```

相关声明：[oscore_ctx](#a7486199db30c9aaaba693ce64fd46879)。

观察者（Observer）受OSCORE保护时非NULL。

## 9.2\_详细说明（Detailed Documentation）

<a id="a5d5e9494804ef64bc705f2bb08ac7afd"></a>

### `addr`

```c
struct net_sockaddr_storage coap_observer::addr
```

观察者连接端点（Connection End Point）的信息。

<a id="a24a9f853db17ff623f4c510fd0892eb5"></a>

### `list`

```c
sys_snode_t coap_observer::list
```

观察者（Observer）的列表节点。

<a id="a7486199db30c9aaaba693ce64fd46879"></a>

### `oscore_ctx`

```c
struct coap_oscore_context* coap_observer::oscore_ctx
```

观察者（Observer）受OSCORE保护时非NULL。

**注意（Attention）**：注意（Attention）：仅在启用Kconfig选项CONFIG_COAP_OSCORE时可用。

<a id="a901f148d2eb697206fde732050c3d8b4"></a>

### `tkl`

```c
uint8_t coap_observer::tkl
```

扩展令牌长度（Extended Token Length）。

<a id="a6d7d792120b935bf61c739f95dd7361c"></a>

### `token`

```c
uint8_t coap_observer::token[8]
```

观察者令牌（Observer Token）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 9.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_coap_core_metadata_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_coap_option_结构体.md)
