---
id: learning.zephyr-docs.api-source-reference.page-569
title: mspm0_uart.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第569章\_mspm0\_uart.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__uart_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P357_MSPM0UART设备树常量.md)。

## 569.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>

```c
/*
 * Copyright (c) 2026 Bang & Olufsen A/S, Denmark
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_UART_MSPM0_UART_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_UART_MSPM0_UART_H_


#define MSPM0_UART_RX_FIFO_LEVEL_ONE_ENTRY 0
#define MSPM0_UART_RX_FIFO_LEVEL_1_4_FULL  1
#define MSPM0_UART_RX_FIFO_LEVEL_1_2_FULL  2
#define MSPM0_UART_RX_FIFO_LEVEL_3_4_FULL  3
#define MSPM0_UART_RX_FIFO_LEVEL_FULL      4



#define MSPM0_UART_TX_FIFO_LEVEL_ONE_ENTRY 0
#define MSPM0_UART_TX_FIFO_LEVEL_1_4_EMPTY 1
#define MSPM0_UART_TX_FIFO_LEVEL_1_2_EMPTY 2
#define MSPM0_UART_TX_FIFO_LEVEL_3_4_EMPTY 3
#define MSPM0_UART_TX_FIFO_LEVEL_EMPTY     4


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_UART_MSPM0_UART_H_ */
```

## 569.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Bang & Olufsen A/S, Denmark。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_UART_MSPM0_UART_H_`。

## 569.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P357_MSPM0UART设备树常量.md)

---

[上一章](P568_mspm0_clock_control.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P570_mspm0_vref.h_源码浏览.md)
