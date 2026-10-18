---
id: learning.zephyr-docs.modem-wireless-model-reference.page-47
title: modem_backend_uart_isr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__isr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_modem\_backend\_uart\_isr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__isr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/uart.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

<a id="r_afacd3e6c890a30188987e6cffae03981"></a>

```c
struct ring_buf receive_rdb [2]
```

相关声明：[ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)、[receive_rdb](#afacd3e6c890a30188987e6cffae03981)。

<a id="r_a69aa3fbffb2bfbd8d5ca16effb8f4f17"></a>

```c
struct ring_buf transmit_rb
```

相关声明：[ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)、[transmit_rb](#a69aa3fbffb2bfbd8d5ca16effb8f4f17)。

<a id="r_a4d270cc8e2260c349c588109a3c4ddae"></a>

```c
atomic_t transmit_buf_len
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[transmit_buf_len](#a4d270cc8e2260c349c588109a3c4ddae)。

<a id="r_a2c50ecd1dad68ee2aa2ad57b1b746831"></a>

```c
atomic_t receive_buf_len
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[receive_buf_len](#a2c50ecd1dad68ee2aa2ad57b1b746831)。

<a id="r_ac7a373618e4dc5dfda02bbc9d09a11a3"></a>

```c
uint8_t receive_rdb_used
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_rdb_used](#ac7a373618e4dc5dfda02bbc9d09a11a3)。

<a id="r_a3b0413caf39e82a52e2bbab6ba42ac3b"></a>

```c
uint32_t transmit_buf_put_limit
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[transmit_buf_put_limit](#a3b0413caf39e82a52e2bbab6ba42ac3b)。

## 47.2\_详细说明（Detailed Documentation）

<a id="a2c50ecd1dad68ee2aa2ad57b1b746831"></a>

### `receive_buf_len`

```c
atomic_t modem_backend_uart_isr::receive_buf_len
```

<a id="afacd3e6c890a30188987e6cffae03981"></a>

### `receive_rdb`

```c
struct ring_buf modem_backend_uart_isr::receive_rdb[2]
```

<a id="ac7a373618e4dc5dfda02bbc9d09a11a3"></a>

### `receive_rdb_used`

```c
uint8_t modem_backend_uart_isr::receive_rdb_used
```

<a id="a4d270cc8e2260c349c588109a3c4ddae"></a>

### `transmit_buf_len`

```c
atomic_t modem_backend_uart_isr::transmit_buf_len
```

<a id="a3b0413caf39e82a52e2bbab6ba42ac3b"></a>

### `transmit_buf_put_limit`

```c
uint32_t modem_backend_uart_isr::transmit_buf_put_limit
```

<a id="a69aa3fbffb2bfbd8d5ca16effb8f4f17"></a>

### `transmit_rb`

```c
struct ring_buf modem_backend_uart_isr::transmit_rb
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/uart.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/uart.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)
- [ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_modem_backend_uart_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_modem_cellular_board_init_结构体.md)
