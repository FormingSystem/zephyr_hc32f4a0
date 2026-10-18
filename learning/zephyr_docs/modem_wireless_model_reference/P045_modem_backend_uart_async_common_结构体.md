---
id: learning.zephyr-docs.modem-wireless-model-reference.page-45
title: modem_backend_uart_async_common_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__async__common.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_modem\_backend\_uart\_async\_common\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__async__common.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/uart.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 45.1\_数据成员（Data Fields）

<a id="r_a41f85b18c22fc678ce06b5ea42dd052a"></a>

```c
uint8_t * transmit_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_buf](#a41f85b18c22fc678ce06b5ea42dd052a)。

<a id="r_a37c79230e6f796fa12dfc4eed5e94fcc"></a>

```c
uint32_t transmit_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transmit_buf_size](#a37c79230e6f796fa12dfc4eed5e94fcc)。

<a id="r_a3996a268ebdeefec160ed80d122ce533"></a>

```c
struct k_work rx_disabled_work
```

相关声明：[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)、[rx_disabled_work](#a3996a268ebdeefec160ed80d122ce533)。

<a id="r_a4e542d2880b320f3b843fc3813c0fd0f"></a>

```c
atomic_t state
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[state](#a4e542d2880b320f3b843fc3813c0fd0f)。

## 45.2\_详细说明（Detailed Documentation）

<a id="a3996a268ebdeefec160ed80d122ce533"></a>

### `rx_disabled_work`

```c
struct k_work modem_backend_uart_async_common::rx_disabled_work
```

<a id="a4e542d2880b320f3b843fc3813c0fd0f"></a>

### `state`

```c
atomic_t modem_backend_uart_async_common::state
```

<a id="a41f85b18c22fc678ce06b5ea42dd052a"></a>

### `transmit_buf`

```c
uint8_t* modem_backend_uart_async_common::transmit_buf
```

<a id="a37c79230e6f796fa12dfc4eed5e94fcc"></a>

### `transmit_buf_size`

```c
uint32_t modem_backend_uart_async_common::transmit_buf_size
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/uart.h`

## 45.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/uart.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P044_modem_backend_uart_async_结构体.md) · [返回大纲](大纲.md) · [下一章](P046_modem_backend_uart_config_结构体.md)
