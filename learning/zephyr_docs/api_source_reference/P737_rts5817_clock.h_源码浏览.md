---
id: learning.zephyr-docs.api-source-reference.page-737
title: rts5817_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第737章\_rts5817\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__clock_8h.html)。

## 737.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>

```c
/*
 * Copyright (c) 2025 Realtek Semiconductor, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5817_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5817_CLOCK_H_

#define RTS_FP_CLK_SYS_PLL   0
#define RTS_FP_CLK_BUS       1
#define RTS_FP_CLK_SPI_CACHE 2
#define RTS_FP_CLK_SPI_SSOR  3
#define RTS_FP_CLK_SPI_SSI_M 4
#define RTS_FP_CLK_SPI_SSI_S 5
#define RTS_FP_CLK_SHA       6
#define RTS_FP_CLK_AES       7
#define RTS_FP_CLK_PKE       8
#define RTS_FP_CLK_I2C0      9
#define RTS_FP_CLK_I2C1      10
#define RTS_FP_CLK_TRNG      11
#define RTS_FP_CLK_I2C_S     12
#define RTS_FP_CLK_UART0     13
#define RTS_FP_CLK_UART1     14
#define RTS_FP_CLK_SIE       15
#define RTS_FP_CLK_PUF       16
#define RTS_FP_CLK_GE        17

#define RLX_CLK_NUM_SIZE (RTS_FP_CLK_GE + 1)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5817_CLOCK_H_ */
```

## 737.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Realtek Semiconductor, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RTS5817_CLOCK_H_`。

## 737.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__clock_8h.html)

---

[上一章](P736_rtp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P738_rts5817_intc.h_源码浏览.md)
