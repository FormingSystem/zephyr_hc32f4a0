---
id: learning.zephyr-docs.network-application-model-reference.page-1
title: coap_block_context_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__block__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_coap\_block\_context\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__block__context.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

表示分块事务（Block-Wise Transaction）的当前状态。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

表示分块事务（Block-Wise Transaction）的当前状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a27db79dc3a2af6dd9f41e3008dcde87a"></a>

```c
size_t total_size
```

相关声明：[total_size](#a27db79dc3a2af6dd9f41e3008dcde87a)。

分块事务（Block-Wise Transaction）的总大小。

<a id="r_a474f54e2a29d41b9d449f8574e747067"></a>

```c
size_t current
```

相关声明：[current](#a474f54e2a29d41b9d449f8574e747067)。

分块事务（Block-Wise Transaction）的当前大小。

<a id="r_a27eb897fa2d455eb79220f1654509da3"></a>

```c
enum coap_block_size block_size
```

相关声明：[coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)、[block_size](#a27eb897fa2d455eb79220f1654509da3)。

块大小（Block Size）。

## 1.2\_详细说明（Detailed Documentation）

<a id="a27eb897fa2d455eb79220f1654509da3"></a>

### `block_size`

```c
enum coap_block_size coap_block_context::block_size
```

块大小（Block Size）。

<a id="a474f54e2a29d41b9d449f8574e747067"></a>

### `current`

```c
size_t coap_block_context::current
```

分块事务（Block-Wise Transaction）的当前大小。

<a id="a27db79dc3a2af6dd9f41e3008dcde87a"></a>

### `total_size`

```c
size_t coap_block_context::total_size
```

分块事务（Block-Wise Transaction）的总大小。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_coap_client_结构体.md)
