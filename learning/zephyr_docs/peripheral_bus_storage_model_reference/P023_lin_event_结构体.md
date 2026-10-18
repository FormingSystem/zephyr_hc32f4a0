---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-23
title: lin_event_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlin__event.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_lin\_event\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlin__event.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

局部互连网络（LIN）的事件结构。

```c
#include <zephyr/drivers/lin.h>
```

<a id="details"></a>

LIN 事件结构体（Event structure）。此结构体用于将 LIN 事件传递给应用程序。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_aa9a3195610f167381e89b28d054ebd10"></a>

```c
enum lin_event_type type
```

相关声明：[lin_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab7aca457453e6e6409c02903bcdf9bab)、[type](#aa9a3195610f167381e89b28d054ebd10)。

LIN 事件类型。

<a id="r_ac5b4c13e4f9cfa2bdf327269013900a8"></a>

```c
int status
```

相关声明：[status](#ac5b4c13e4f9cfa2bdf327269013900a8)。

LIN 状态码（如有）。

```c
union {
```

```c
struct {
```

<a id="r_a4ab72a6515269fe5980a218cec55bfb0"></a>

```c
uint8_t pid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pid](#a1ff71b532d8e117247465d6d330e32bb)。

LIN 受保护标识符（Protected ID，PID）。

<a id="r_a148bbc077dac40dd9d745e7a1dd187e9"></a>

```c
} header
```

相关声明：[header](#ad47886103edb3c8709ec51bfec4905e7)。

LIN 帧头事件上下文（如有）。

```c
struct {
```

<a id="r_a3be8533c3d404c849462689e513c7802"></a>

```c
uint8_t pid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pid](#a1ff71b532d8e117247465d6d330e32bb)。

LIN 受保护标识符（Protected ID，PID）。

<a id="r_a1d5c60279d83266b021ce754fd64c3b1"></a>

```c
uint8_t bytes_received
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bytes_received](#a3b9f0adfcc43c3fed83ea23c10b7e67b)。

已接收的数据字节数。

<a id="r_a7ed763c0bbf5793b96ce1a1a5572165e"></a>

```c
uint8_t checksum
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[checksum](#af401a550032c87c4b1a1e1d1941baee0)。

接收到的校验和（Checksum）。

<a id="r_a5d9a2a052743013a08b145cba19c498b"></a>

```c
} data
```

相关声明：[data](#a17b7f0acfe393d09e58c2548e4f22212)。

LIN 数据事件上下文（如有）。

<a id="r_aed20dfdf7c8a2e130a0da2476eed15ce"></a>

```c
lin_error_flags_t error_flags
```

相关声明：[lin_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga344a6eade12faa423b8bd2718009b0c5)、[error_flags](#a1e82bfb19eddb23a27fcff1bee7e0667)。

LIN 错误事件标志（如有）。

<a id="r_a7338b59711ad3a3a1a2130f69b49a4b2"></a>

```c
};
```

事件特定的上下文信息。

## 23.2\_详细说明（Detailed Documentation）

<a id="a7338b59711ad3a3a1a2130f69b49a4b2"></a>

### `[union]`

```c
union { ... } lin_event
```

事件特定的上下文信息。

<a id="a3b9f0adfcc43c3fed83ea23c10b7e67b"></a>

### `bytes_received`

```c
uint8_t lin_event::bytes_received
```

已接收的数据字节数。

<a id="af401a550032c87c4b1a1e1d1941baee0"></a>

### `checksum`

```c
uint8_t lin_event::checksum
```

接收到的校验和（Checksum）。

<a id="a17b7f0acfe393d09e58c2548e4f22212"></a>

### `[struct]`

```c
struct { ... } lin_event::data
```

LIN 数据事件上下文（如有）。

<a id="a1e82bfb19eddb23a27fcff1bee7e0667"></a>

### `error_flags`

```c
lin_error_flags_t lin_event::error_flags
```

LIN 错误事件标志（如有）。

<a id="ad47886103edb3c8709ec51bfec4905e7"></a>

### `[struct]`

```c
struct { ... } lin_event::header
```

LIN 帧头事件上下文（如有）。

<a id="a1ff71b532d8e117247465d6d330e32bb"></a>

### `pid`

```c
uint8_t lin_event::pid
```

LIN 受保护标识符（Protected ID，PID）。

<a id="ac5b4c13e4f9cfa2bdf327269013900a8"></a>

### `status`

```c
int lin_event::status
```

LIN 状态码（如有）。

<a id="aa9a3195610f167381e89b28d054ebd10"></a>

### `type`

```c
enum lin_event_type lin_event::type
```

LIN 事件类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/lin.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/drivers/lin.h](https://docs.zephyrproject.org/latest/doxygen/html/lin_8h_source.html)
- [lin_event_type](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gab7aca457453e6e6409c02903bcdf9bab)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lin_error_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga344a6eade12faa423b8bd2718009b0c5)
- [lin_event](P023_lin_event_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_lin_driver_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_lin_filter_结构体.md)
