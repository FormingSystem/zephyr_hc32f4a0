---
id: learning.zephyr-docs.platform-security-model-reference.page-60
title: tee_open_session_arg_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__open__session__arg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_tee\_open\_session\_arg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__open__session__arg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

打开会话（Open Session）的参数。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

打开会话（Open Session）的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_a9f4c56fe45f5ad9313bdc1f457d31f9a"></a>

```c
uint8_t uuid [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#a9f4c56fe45f5ad9313bdc1f457d31f9a)。

[in] 可信应用的 UUID。

<a id="r_aff38cc02e83936e23965ee2e4e44ff26"></a>

```c
uint8_t clnt_uuid [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clnt_uuid](#aff38cc02e83936e23965ee2e4e44ff26)。

[in] 客户端的 UUID。

<a id="r_a226c617eae1b959025a0232eed48aa41"></a>

```c
uint32_t clnt_login
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[clnt_login](#a226c617eae1b959025a0232eed48aa41)。

客户端登录类别（Login class），取上述 `TEE_IOCTL_LOGIN_*` 值。

<a id="r_adf8bfaaf5059de617a7139b5f06a0ac6"></a>

```c
uint32_t cancel_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cancel_id](#adf8bfaaf5059de617a7139b5f06a0ac6)。

[in] 取消 ID（Cancellation ID），用于唯一标识此请求。

<a id="r_a5e28bb77990ce6d050a57daa419760e1"></a>

```c
uint32_t session
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[session](#a5e28bb77990ce6d050a57daa419760e1)。

[out] 会话 ID。

<a id="r_a3be6d6ea6aeff1a8f27051fe30f21347"></a>

```c
uint32_t ret
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ret](#a3be6d6ea6aeff1a8f27051fe30f21347)。

[out] 返回值。

<a id="r_a73a7e82fb0b589eed327ab8f4217e6fc"></a>

```c
uint32_t ret_origin
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ret_origin](#a73a7e82fb0b589eed327ab8f4217e6fc)。

[out] 返回值来源（Origin）。

## 60.2\_详细说明（Detailed Documentation）

<a id="adf8bfaaf5059de617a7139b5f06a0ac6"></a>

### `cancel_id`

```c
uint32_t tee_open_session_arg::cancel_id
```

[in] 取消 ID（Cancellation ID），用于唯一标识此请求。

<a id="a226c617eae1b959025a0232eed48aa41"></a>

### `clnt_login`

```c
uint32_t tee_open_session_arg::clnt_login
```

客户端登录类别（Login class），取上述 `TEE_IOCTL_LOGIN_*` 值。

<a id="aff38cc02e83936e23965ee2e4e44ff26"></a>

### `clnt_uuid`

```c
uint8_t tee_open_session_arg::clnt_uuid[16]
```

[in] 客户端的 UUID。

<a id="a3be6d6ea6aeff1a8f27051fe30f21347"></a>

### `ret`

```c
uint32_t tee_open_session_arg::ret
```

[out] 返回值。

<a id="a73a7e82fb0b589eed327ab8f4217e6fc"></a>

### `ret_origin`

```c
uint32_t tee_open_session_arg::ret_origin
```

[out] 返回值来源（Origin）。

<a id="a5e28bb77990ce6d050a57daa419760e1"></a>

### `session`

```c
uint32_t tee_open_session_arg::session
```

[out] 会话 ID。

<a id="a9f4c56fe45f5ad9313bdc1f457d31f9a"></a>

### `uuid`

```c
uint8_t tee_open_session_arg::uuid[16]
```

[in] 可信应用的 UUID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_tee_invoke_func_arg_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_tee_param_结构体.md)
