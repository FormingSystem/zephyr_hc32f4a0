---
id: learning.zephyr-docs.api-source-reference.page-882
title: uart_pipe.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第882章\_uart\_pipe.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html)。

## 882.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdlib_8h_html"></a>
<a id="auart__pipe_8h_html_a0ddac401c01681a22952ae792007b786"></a>
<a id="auart__pipe_8h_html_a6136cfc4837939fd56243245f462cc0e"></a>
<a id="auart__pipe_8h_html_a8a840645edad0e2ac3da6cfd6f09557f"></a>

```c


/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_UART_PIPE_H_
#define ZEPHYR_INCLUDE_DRIVERS_UART_PIPE_H_

#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef uint8_t *(*uart_pipe_recv_cb)(uint8_t *buf, size_t *off);

void uart_pipe_register(uint8_t *buf, size_t len, uart_pipe_recv_cb cb);

int uart_pipe_send(const uint8_t *data, int len);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_UART_PIPE_H_ */
```

## 882.2\_可见注释译文（Comments）

### 注释 1：原第 8 行

版权（Copyright）：© 2015 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_UART_PIPE_H_`。

## 882.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html)
- [stdlib.h](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uart_pipe_register](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html#a0ddac401c01681a22952ae792007b786)
- [uart_pipe_recv_cb](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html#a8a840645edad0e2ac3da6cfd6f09557f)
- [uart_pipe_send](https://docs.zephyrproject.org/latest/doxygen/html/uart__pipe_8h.html#a6136cfc4837939fd56243245f462cc0e)

---

[上一章](P881_uart_ns16550.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P883_ubx.h_源码浏览.md)
