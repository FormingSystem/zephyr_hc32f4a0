---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-130
title: bt_obex_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第130章\_bt\_obex\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__obex__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象交换协议（OBEX）的头部结构。

```c
#include <zephyr/bluetooth/classic/obex.h>
```

<a id="details"></a>

对象交换协议（OBEX）的头部结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 130.1\_数据成员（Data Fields）

<a id="r_aa453f73fd7a159d92b193dc53c10d995"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#aa453f73fd7a159d92b193dc53c10d995)。

头部 ID（Header ID），类型为 `bt_obex_header_id`。

<a id="r_a039bc4f46929c1f9e6c12012fee1e88b"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a039bc4f46929c1f9e6c12012fee1e88b)。

头部值的长度。

<a id="r_ad1f539c20ef8f9e8849326b7d8b64101"></a>

```c
const uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad1f539c20ef8f9e8849326b7d8b64101)。

头部值（Header value）。

## 130.2\_详细说明（Detailed Documentation）

<a id="ad1f539c20ef8f9e8849326b7d8b64101"></a>

### `data`

```c
const uint8_t* bt_obex_hdr::data
```

头部值（Header value）。

<a id="aa453f73fd7a159d92b193dc53c10d995"></a>

### `id`

```c
uint8_t bt_obex_hdr::id
```

头部 ID（Header ID），类型为 `bt_obex_header_id`。

<a id="a039bc4f46929c1f9e6c12012fee1e88b"></a>

### `len`

```c
uint16_t bt_obex_hdr::len
```

头部值的长度。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/obex.h`

## 130.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/obex.h](https://docs.zephyrproject.org/latest/doxygen/html/obex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_obex_header_id](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html#ga3c893652eb9a5f0bf699d357caf40948)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P129_bt_obex_client_ops_结构体.md) · [返回大纲](大纲.md) · [下一章](P131_bt_obex_server_结构体.md)
