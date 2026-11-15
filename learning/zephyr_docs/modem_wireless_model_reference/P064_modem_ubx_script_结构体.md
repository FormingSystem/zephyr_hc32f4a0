---
id: learning.zephyr-docs.modem-wireless-model-reference.page-64
title: modem_ubx_script_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__script.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_modem\_ubx\_script\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__script.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a83a2b5393bf48451a83f9816d90efcb8"></a>

```c
const void * buf
```

相关声明：[buf](#a0f8ffa1d60333e14af7e91d472824e47)。

<a id="r_a19affc8c62269746b30fa5dfcf37547b"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a033047efbf34102985fad507711905ec)。

<a id="r_ab91b22317aa1cfb36f7c24de2b425137"></a>

```c
} request
```

相关声明：[request](#ab91b22317aa1cfb36f7c24de2b425137)。

```c
struct {
```

<a id="r_af11b3acaf064bca51f6207ceb5fd5c8f"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#aa1ffe8666c2e2169c6067710f9b3ccc7)。

<a id="r_a796f95ef62b675bfa8d47d60a47a38b1"></a>

```c
uint16_t buf_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[buf_len](#a9882eb3b10b9739c916f5317fda412ea)。

<a id="r_acf8cbc0bf87866ca2b5c5e0614aa202a"></a>

```c
uint16_t received_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[received_len](#a716f90ed421af01c829cb716d94a9a76)。

<a id="r_a90d08ee6c3832f3d0198cea0aa7b3b8d"></a>

```c
} response
```

相关声明：[response](#a90d08ee6c3832f3d0198cea0aa7b3b8d)。

<a id="r_a1e91925ba17f30685db67d4f326d2f31"></a>

```c
struct modem_ubx_match match
```

相关声明：[modem_ubx_match](P063_modem_ubx_match_结构体.md)、[match](#a1e91925ba17f30685db67d4f326d2f31)。

<a id="r_a4910a3551004f19249c66a5b695795ce"></a>

```c
uint16_t retry_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[retry_count](#a4910a3551004f19249c66a5b695795ce)。

<a id="r_a041de757b5fb26f1cdfb89cb19610f11"></a>

```c
k_timeout_t timeout
```

相关声明：[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[timeout](#a041de757b5fb26f1cdfb89cb19610f11)。

## 64.2\_详细说明（Detailed Documentation）

<a id="aa1ffe8666c2e2169c6067710f9b3ccc7"></a>

### `buf [1/2]`

```c
uint8_t* modem_ubx_script::buf
```

<a id="a0f8ffa1d60333e14af7e91d472824e47"></a>

### `buf [2/2]`

```c
const void* modem_ubx_script::buf
```

<a id="a9882eb3b10b9739c916f5317fda412ea"></a>

### `buf_len`

```c
uint16_t modem_ubx_script::buf_len
```

<a id="a033047efbf34102985fad507711905ec"></a>

### `len`

```c
uint16_t modem_ubx_script::len
```

<a id="a1e91925ba17f30685db67d4f326d2f31"></a>

### `match`

```c
struct modem_ubx_match modem_ubx_script::match
```

<a id="a716f90ed421af01c829cb716d94a9a76"></a>

### `received_len`

```c
uint16_t modem_ubx_script::received_len
```

<a id="ab91b22317aa1cfb36f7c24de2b425137"></a>

### `[struct]`

```c
struct { ... } modem_ubx_script::request
```

<a id="a90d08ee6c3832f3d0198cea0aa7b3b8d"></a>

### `[struct]`

```c
struct { ... } modem_ubx_script::response
```

<a id="a4910a3551004f19249c66a5b695795ce"></a>

### `retry_count`

```c
uint16_t modem_ubx_script::retry_count
```

<a id="a041de757b5fb26f1cdfb89cb19610f11"></a>

### `timeout`

```c
k_timeout_t modem_ubx_script::timeout
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx.h](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [modem_ubx_match](P063_modem_ubx_match_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_modem_ubx_match_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_sim7080_gnss_data_结构体.md)
