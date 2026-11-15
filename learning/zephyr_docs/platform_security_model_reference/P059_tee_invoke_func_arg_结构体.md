---
id: learning.zephyr-docs.platform-security-model-reference.page-59
title: tee_invoke_func_arg_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__invoke__func__arg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_tee\_invoke\_func\_arg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__invoke__func__arg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调用可信应用（Trusted Application）中的函数。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

调用可信应用（Trusted Application）中的函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_a17aa094ca0a6c6d9a72d2fae9c0c66ef"></a>

```c
uint32_t func
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[func](#a17aa094ca0a6c6d9a72d2fae9c0c66ef)。

[in] 可信应用（Trusted Application，TA）函数，具体含义由该 TA 定义。

<a id="r_af110327354b1ca48dedf22855c3a7afc"></a>

```c
uint32_t session
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[session](#af110327354b1ca48dedf22855c3a7afc)。

[in] 会话 ID。

<a id="r_a457daf2221f9520aecb42667acc4ccd1"></a>

```c
uint32_t cancel_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cancel_id](#a457daf2221f9520aecb42667acc4ccd1)。

[in] 取消 ID（Cancellation ID），用于唯一标识此请求。

<a id="r_af63bd284a7397d4086ac17f83d6b1e93"></a>

```c
uint32_t ret
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ret](#af63bd284a7397d4086ac17f83d6b1e93)。

[out] 返回值。

<a id="r_ae806e940e463321b3de31bad2e05bf60"></a>

```c
uint32_t ret_origin
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ret_origin](#ae806e940e463321b3de31bad2e05bf60)。

[out] 返回值来源（Origin）。

## 59.2\_详细说明（Detailed Documentation）

<a id="a457daf2221f9520aecb42667acc4ccd1"></a>

### `cancel_id`

```c
uint32_t tee_invoke_func_arg::cancel_id
```

[in] 取消 ID（Cancellation ID），用于唯一标识此请求。

<a id="a17aa094ca0a6c6d9a72d2fae9c0c66ef"></a>

### `func`

```c
uint32_t tee_invoke_func_arg::func
```

[in] 可信应用（Trusted Application，TA）函数，具体含义由该 TA 定义。

<a id="af63bd284a7397d4086ac17f83d6b1e93"></a>

### `ret`

```c
uint32_t tee_invoke_func_arg::ret
```

[out] 返回值。

<a id="ae806e940e463321b3de31bad2e05bf60"></a>

### `ret_origin`

```c
uint32_t tee_invoke_func_arg::ret_origin
```

[out] 返回值来源（Origin）。

<a id="af110327354b1ca48dedf22855c3a7afc"></a>

### `session`

```c
uint32_t tee_invoke_func_arg::session
```

[in] 会话 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_tee_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_tee_open_session_arg_结构体.md)
