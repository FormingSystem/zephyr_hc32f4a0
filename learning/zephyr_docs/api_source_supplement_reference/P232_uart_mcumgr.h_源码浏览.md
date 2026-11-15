---
id: learning.zephyr-docs.api-source-supplement-reference.page-232
title: uart_mcumgr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第232章\_uart\_mcumgr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html)。

## 232.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdlib_8h_html"></a>
<a id="astructuart__mcumgr__rx__buf_html"></a>
<a id="astructuart__mcumgr__rx__buf_html_a6495e78b7f249c6b073c4b0e1c25160a"></a>
<a id="astructuart__mcumgr__rx__buf_html_a81696c833e2955e6888fcd439a59f786"></a>
<a id="astructuart__mcumgr__rx__buf_html_a8484b842ce240d35dff22f704617d22d"></a>
<a id="auart__mcumgr_8h_html_a0173a370be3e424b56cdfbb3d4174da1"></a>
<a id="auart__mcumgr_8h_html_a2b31278c4e600bcd10d1a069cc6f5655"></a>
<a id="auart__mcumgr_8h_html_acf906a316bf77fc5cc8768130ce82e66"></a>
<a id="auart__mcumgr_8h_html_ae173ad28a0301c8ddfdd9b8bc5583ba3"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_MCUMGR_H_
#define ZEPHYR_INCLUDE_DRIVERS_CONSOLE_UART_MCUMGR_H_

#include <stdlib.h>
#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

struct uart_mcumgr_rx_buf {
        void *fifo_reserved;   /* 1st word reserved for use by fifo */
        uint8_t data[CONFIG_UART_MCUMGR_RX_BUF_SIZE];
        int length;
};

typedef void uart_mcumgr_recv_fn(struct uart_mcumgr_rx_buf *rx_buf);

int uart_mcumgr_send(const uint8_t *data, int len);

void uart_mcumgr_free_rx_buf(struct uart_mcumgr_rx_buf *rx_buf);

void uart_mcumgr_register(uart_mcumgr_recv_fn *cb);

#ifdef __cplusplus
}
#endif

#endif
```

## 232.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

第一个字（1st word）保留给 FIFO 使用。

## 232.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html)
- [stdlib.h](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uart_mcumgr_rx_buf](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md)
- [fifo_reserved](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a8484b842ce240d35dff22f704617d22d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a81696c833e2955e6888fcd439a59f786)
- [length](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a6495e78b7f249c6b073c4b0e1c25160a)
- [uart_mcumgr_recv_fn](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html#a0173a370be3e424b56cdfbb3d4174da1)
- [uart_mcumgr_send](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html#acf906a316bf77fc5cc8768130ce82e66)
- [uart_mcumgr_free_rx_buf](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html#ae173ad28a0301c8ddfdd9b8bc5583ba3)
- [uart_mcumgr_register](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html#a2b31278c4e600bcd10d1a069cc6f5655)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uart_mcumgr_rx_buf::length](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a6495e78b7f249c6b073c4b0e1c25160a)
- [uart_mcumgr_rx_buf::data](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a81696c833e2955e6888fcd439a59f786)
- [uart_mcumgr_rx_buf::fifo_reserved](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md#a8484b842ce240d35dff22f704617d22d)

---

[上一章](P231_uart_altera.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P233_udp.h_源码浏览.md)
