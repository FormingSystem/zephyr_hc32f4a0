---
id: learning.zephyr-docs.system-service-model-reference.page-88
title: uart_mcumgr_rx_buf_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__mcumgr__rx__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_uart\_mcumgr\_rx\_buf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structuart__mcumgr__rx__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含通过UART接收的mcumgr片段（Fragment）。

```c
#include <zephyr/drivers/console/uart_mcumgr.h>
```

<a id="details"></a>

包含通过UART接收的mcumgr片段（Fragment）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_a8484b842ce240d35dff22f704617d22d"></a>

```c
void * fifo_reserved
```

相关声明：[fifo_reserved](#a8484b842ce240d35dff22f704617d22d)。

<a id="r_a81696c833e2955e6888fcd439a59f786"></a>

```c
uint8_t data [CONFIG_UART_MCUMGR_RX_BUF_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a81696c833e2955e6888fcd439a59f786)。

<a id="r_a6495e78b7f249c6b073c4b0e1c25160a"></a>

```c
int length
```

相关声明：[length](#a6495e78b7f249c6b073c4b0e1c25160a)。

## 88.2\_详细说明（Detailed Documentation）

<a id="a81696c833e2955e6888fcd439a59f786"></a>

### `data`

```c
uint8_t uart_mcumgr_rx_buf::data[CONFIG_UART_MCUMGR_RX_BUF_SIZE]
```

<a id="a8484b842ce240d35dff22f704617d22d"></a>

### `fifo_reserved`

```c
void* uart_mcumgr_rx_buf::fifo_reserved
```

<a id="a6495e78b7f249c6b073c4b0e1c25160a"></a>

### `length`

```c
int uart_mcumgr_rx_buf::length
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/console/uart_mcumgr.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/drivers/console/uart_mcumgr.h](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_tty_serial_结构体.md) · [返回大纲](大纲.md)
