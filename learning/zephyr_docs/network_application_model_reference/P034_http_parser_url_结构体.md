---
id: learning.zephyr-docs.network-application-model-reference.page-34
title: http_parser_url_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser__url.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_http\_parser\_url\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhttp__parser__url.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/net/http/parser_url.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a77af61a480f11c41938810dd76ca49eb"></a>

```c
uint16_t field_set
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[field_set](#a77af61a480f11c41938810dd76ca49eb)。

<a id="r_a875fb8faf3ee45707078eda5435fa563"></a>

```c
uint16_t port
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port](#a875fb8faf3ee45707078eda5435fa563)。

```c
struct {
```

<a id="r_aeb34f78c85cdb792e6bcbb67ef35b111"></a>

```c
uint16_t off
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[off](#a6510826f3aa9a1100ac5f714323edeb1)。

<a id="r_a7184ad388073921fed0ee218b8b240f3"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a60fb784a989dd5a95e5bd19d468d22c7)。

<a id="r_a911c18d1fc54309a7665d942c55cfae9"></a>

```c
} field_data [UF_MAX]
```

相关声明：[field_data](#a911c18d1fc54309a7665d942c55cfae9)、[UF_MAX](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h.html#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)。

## 34.2\_详细说明（Detailed Documentation）

<a id="a911c18d1fc54309a7665d942c55cfae9"></a>

### `[struct]`

```c
struct { ... } http_parser_url::field_data[UF_MAX]
```

<a id="a77af61a480f11c41938810dd76ca49eb"></a>

### `field_set`

```c
uint16_t http_parser_url::field_set
```

<a id="a60fb784a989dd5a95e5bd19d468d22c7"></a>

### `len`

```c
uint16_t http_parser_url::len
```

<a id="a6510826f3aa9a1100ac5f714323edeb1"></a>

### `off`

```c
uint16_t http_parser_url::off
```

<a id="a875fb8faf3ee45707078eda5435fa563"></a>

### `port`

```c
uint16_t http_parser_url::port
```

本数据类型文档由以下文件生成：

- `zephyr/net/http/parser_url.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/net/http/parser_url.h](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [UF_MAX](https://docs.zephyrproject.org/latest/doxygen/html/parser__url_8h.html#a9ca1f91c2958091e2ac9e9b2f903d4eba4b40c88291e4fa018de04553e7e1adfd)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_http_parser_settings_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_http_request_结构体.md)
