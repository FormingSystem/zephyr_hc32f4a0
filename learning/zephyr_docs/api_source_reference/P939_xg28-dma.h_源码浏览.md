---
id: learning.zephyr-docs.api-source-reference.page-939
title: xg28-dma.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg28-dma_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第939章\_xg28-dma.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xg28-dma_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xg28-dma_8h.html)。

## 939.1\_原始可见代码（Source Code）

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
<a id="l00032"></a>
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
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="acommon-dma_8h_html"></a>
<a id="adt-util_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SILABS_XG28_DMA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SILABS_XG28_DMA_H_

#include <zephyr/dt-bindings/dt-util.h>
#include "common-dma.h"

#define DMA_REQSEL_NONE               (FIELD_PREP(DMA_SRC_MASK, 0) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_LDMAXBARPRSREQ0    (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_LDMAXBARPRSREQ1    (FIELD_PREP(DMA_SRC_MASK, 1) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER0CC0          (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER0CC1          (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER0CC2          (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_TIMER0UFOF         (FIELD_PREP(DMA_SRC_MASK, 2) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_TIMER1CC0          (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER1CC1          (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER1CC2          (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_TIMER1UFOF         (FIELD_PREP(DMA_SRC_MASK, 3) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_USART0RXDATAV      (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_USART0RXDATAVRIGHT (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_USART0TXBL         (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_USART0TXBLRIGHT    (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_USART0TXEMPTY      (FIELD_PREP(DMA_SRC_MASK, 4) | FIELD_PREP(DMA_SIG_MASK, 4))
#define DMA_REQSEL_I2C0RXDATAV        (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_I2C0TXBL           (FIELD_PREP(DMA_SRC_MASK, 5) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_I2C1RXDATAV        (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_I2C1TXBL           (FIELD_PREP(DMA_SRC_MASK, 6) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_IADC0IADC_SCAN     (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_IADC0IADC_SINGLE   (FIELD_PREP(DMA_SRC_MASK, 10) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_MSCWDATA           (FIELD_PREP(DMA_SRC_MASK, 11) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER2CC0          (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER2CC1          (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER2CC2          (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_TIMER2UFOF         (FIELD_PREP(DMA_SRC_MASK, 12) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_TIMER3CC0          (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER3CC1          (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER3CC2          (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_TIMER3UFOF         (FIELD_PREP(DMA_SRC_MASK, 13) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_TIMER4CC0          (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_TIMER4CC1          (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_TIMER4CC2          (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 2))
#define DMA_REQSEL_TIMER4UFOF         (FIELD_PREP(DMA_SRC_MASK, 14) | FIELD_PREP(DMA_SIG_MASK, 3))
#define DMA_REQSEL_VDAC0CH0_REQ       (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_VDAC0CH1_REQ       (FIELD_PREP(DMA_SRC_MASK, 15) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_EUSART0RXFL        (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_EUSART0TXFL        (FIELD_PREP(DMA_SRC_MASK, 16) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_EUSART1RXFL        (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_EUSART1TXFL        (FIELD_PREP(DMA_SRC_MASK, 17) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_EUSART2RXFL        (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_EUSART2TXFL        (FIELD_PREP(DMA_SRC_MASK, 18) | FIELD_PREP(DMA_SIG_MASK, 1))
#define DMA_REQSEL_LESENSEFIFO        (FIELD_PREP(DMA_SRC_MASK, 19) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_LCD                (FIELD_PREP(DMA_SRC_MASK, 20) | FIELD_PREP(DMA_SIG_MASK, 0))
#define DMA_REQSEL_MVPREQ             (FIELD_PREP(DMA_SRC_MASK, 21) | FIELD_PREP(DMA_SIG_MASK, 0))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SILABS_XG28_DMA_H_ */
```

## 939.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DMA_SILABS_XG28_DMA_H_`。

## 939.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xg28-dma_8h.html)
- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)
- [common-dma.h](https://docs.zephyrproject.org/latest/doxygen/html/common-dma_8h.html)
- [dt-util.h](../dt_bus_binding_reference/P005_设备树绑定工具头文件参考.md)

---

[上一章](P938_xg27-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P940_xg29-dma.h_源码浏览.md)
