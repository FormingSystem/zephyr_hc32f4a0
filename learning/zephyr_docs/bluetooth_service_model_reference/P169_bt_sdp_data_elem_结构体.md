---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-169
title: bt_sdp_data_elem_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__data__elem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_bt\_sdp\_data\_elem\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__data__elem.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

服务发现协议（SDP）的通用数据元素值（Generic Data Element Value）。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

服务发现协议（SDP）的通用数据元素值（Generic Data Element Value）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 169.1\_数据成员（Data Fields）

<a id="r_ac6d5cbc71d1133f30bc20919ffd2d263"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#ac6d5cbc71d1133f30bc20919ffd2d263)。

数据元素（data element）的类型。

<a id="r_a88b38121f91d55ca796dedb99b1e18d6"></a>

```c
uint32_t data_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[data_size](#a88b38121f91d55ca796dedb99b1e18d6)。

数据元素的大小。

<a id="r_a8b7f4943ad968953edb7a3a6f541369b"></a>

```c
uint32_t total_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[total_size](#a8b7f4943ad968953edb7a3a6f541369b)。

数据元素的总大小。

<a id="r_a0572a0c34ddf3ba340ee63d28c330dd1"></a>

```c
const void * data
```

相关声明：[data](#a0572a0c34ddf3ba340ee63d28c330dd1)。

## 169.2\_详细说明（Detailed Documentation）

<a id="a0572a0c34ddf3ba340ee63d28c330dd1"></a>

### `data`

```c
const void* bt_sdp_data_elem::data
```

<a id="a88b38121f91d55ca796dedb99b1e18d6"></a>

### `data_size`

```c
uint32_t bt_sdp_data_elem::data_size
```

数据元素的大小。

<a id="a8b7f4943ad968953edb7a3a6f541369b"></a>

### `total_size`

```c
uint32_t bt_sdp_data_elem::total_size
```

数据元素的总大小。

<a id="ac6d5cbc71d1133f30bc20919ffd2d263"></a>

### `type`

```c
uint8_t bt_sdp_data_elem::type
```

数据元素（data element）的类型。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 169.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P168_bt_sdp_client_result_结构体.md) · [返回大纲](大纲.md) · [下一章](P170_bt_sdp_discover_params_结构体.md)
