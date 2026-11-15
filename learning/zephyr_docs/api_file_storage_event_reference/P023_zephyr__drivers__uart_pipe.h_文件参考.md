---
id: learning.zephyr-docs.api-file-storage-event-reference.page-23
title: zephyr__drivers__uart_pipe.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_zephyr\_\_drivers\_\_uart\_pipe.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

管道UART（Pipe UART）驱动的头文件。

<a id="details"></a>

```c
#include <stdlib.h>
```

查看此文件的源码。

管道 UART 驱动头文件（Pipe UART Driver Header）。此驱动允许应用处理所接收协议数据的各个方面。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 23.1\_类型定义（Typedefs）

<a id="r_a8a840645edad0e2ac3da6cfd6f09557f"></a>

```c
typedef uint8_t *(* uart_pipe_recv_cb) (uint8_t *buf, size_t *off)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uart_pipe_recv_cb](#a8a840645edad0e2ac3da6cfd6f09557f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

接收数据回调（Received Data Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 23.2\_函数（Functions）

<a id="r_a0ddac401c01681a22952ae792007b786"></a>

```c
void uart_pipe_register (uint8_t *buf, size_t len, uart_pipe_recv_cb cb)
```

相关声明：[uart_pipe_register](#a0ddac401c01681a22952ae792007b786)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uart_pipe_recv_cb](#a8a840645edad0e2ac3da6cfd6f09557f)。

注册 UART 应用（Application）。

<a id="r_a6136cfc4837939fd56243245f462cc0e"></a>

```c
int uart_pipe_send (const uint8_t *data, int len)
```

相关声明：[uart_pipe_send](#a6136cfc4837939fd56243245f462cc0e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 UART 发送数据（Data）。

## 23.3\_详细说明（Detailed Documentation）

<a id="a8a840645edad0e2ac3da6cfd6f09557f"></a>

### `uart_pipe_recv_cb`

```c
typedef uint8_t *(* uart_pipe_recv_cb) (uint8_t *buf, size_t *off)
```

接收数据回调（Received Data Callback）。

UART 收到新数据时调用本函数。可通过 `off` 参数修改接收数据的存储偏移量（Offset）。通常，当完整数据已接收并提供新缓冲区时，应将 `off` 设为 `0`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含已接收数据（Received Data）的缓冲区。 |
| `off` | 下次接收的数据偏移量（Data Offset）及累计数据长度。 |

**返回（Returns）**：**返回值（Returns）：**下次接收要使用的缓冲区（Buffer）。

<a id="a0ddac401c01681a22952ae792007b786"></a>

### `uart_pipe_register()`

```c
void uart_pipe_register ( uint8_t * buf, size_t len, uart_pipe_recv_cb cb )
```

注册 UART 应用（Application）。

本函数用于注册新的 UART 应用（Application）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 接收数据使用的初始缓冲区（Initial Buffer）。 |
| `len` | 缓冲区大小。 |
| `cb` | 收到数据时调用的回调（Callback）。 |

<a id="a6136cfc4837939fd56243245f462cc0e"></a>

### `uart_pipe_send()`

```c
int uart_pipe_send ( const uint8_t * data, int len )
```

通过 UART 发送数据（Data）。

本函数用于通过 UART 发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 包含待发送数据（Data to Send）的缓冲区。 |
| `len` | 数据大小（Data Size）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，否则返回负错误值（Negative Error）。


## 23.4\_原页交叉引用（Cross References）

- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P882_uart_pipe.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P022_____w__zephyr__zephyr__subsys__secure_storage__include__internal__zephyr__secure_storage__its__transform.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P024_zephyr__net__websocket.h_文件参考.md)
