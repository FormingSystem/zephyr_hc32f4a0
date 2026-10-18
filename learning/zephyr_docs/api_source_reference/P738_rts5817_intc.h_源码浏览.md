---
id: learning.zephyr-docs.api-source-reference.page-738
title: rts5817_intc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第738章\_rts5817\_intc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html)。

## 738.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>

```c
/*
 * Copyright (c) 2025 Realtek Semiconductor, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_RTS5817_INTC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_RTS5817_INTC_H_


#define IRQ_NUM_SIE        0
#define IRQ_NUM_MC         1
#define IRQ_NUM_SENSOR_SPI 4
#define IRQ_NUM_SPI_MASTER 5
#define IRQ_NUM_AES        6
#define IRQ_NUM_SHA        7
#define IRQ_NUM_GPIO       11
#define IRQ_NUM_SP_GPIO    12
#define IRQ_NUM_UART0      15
#define IRQ_NUM_UART1      16
#define IRQ_NUM_SPI_SLAVE  23


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_RTS5817_INTC_H_ */
```

## 738.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Realtek Semiconductor, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_RTS5817_INTC_H_`。

## 738.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__intc_8h.html)

---

[上一章](P737_rts5817_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P739_rts5817_pinctrl.h_源码浏览.md)
