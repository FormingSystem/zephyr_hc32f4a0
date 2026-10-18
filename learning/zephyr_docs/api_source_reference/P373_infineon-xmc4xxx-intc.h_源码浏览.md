---
id: learning.zephyr-docs.api-source-reference.page-373
title: infineon-xmc4xxx-intc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第373章\_infineon-xmc4xxx-intc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h.html)。

## 373.1\_原始可见代码（Source Code）

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
<a id="l00034"></a>
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
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00068"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>

```c
/*
 * Copyright (c) 2022 Schlumberger
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INFINEON_XMC4XXX_INTC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INFINEON_XMC4XXX_INTC_H_



#define XMC4XXX_INTC_PORT_POS           0
#define XMC4XXX_INTC_PORT_MASK          0xf

#define XMC4XXX_INTC_PIN_POS            4
#define XMC4XXX_INTC_PIN_MASK           0xf

#define XMC4XXX_INTC_LINE_POS           8
#define XMC4XXX_INTC_LINE_MASK          0x7

#define XMC4XXX_INTC_ERU_SRC_POS        11
#define XMC4XXX_INTC_ERU_SRC_MASK       0x7


#define XMC4XXX_INTC_GET_PORT(mx)    ((mx >> XMC4XXX_INTC_PORT_POS) & XMC4XXX_INTC_PORT_MASK)
#define XMC4XXX_INTC_GET_PIN(mx)     ((mx >> XMC4XXX_INTC_PIN_POS) & XMC4XXX_INTC_PIN_MASK)
#define XMC4XXX_INTC_GET_LINE(mx)    ((mx >> XMC4XXX_INTC_LINE_POS) & XMC4XXX_INTC_LINE_MASK)
#define XMC4XXX_INTC_GET_ERU_SRC(mx) ((mx >> XMC4XXX_INTC_ERU_SRC_POS) & XMC4XXX_INTC_ERU_SRC_MASK)

#define XMC4XXX_INTC_SET_LINE_MAP(port, pin, eru_src, line)                                        \
        ((port) << XMC4XXX_INTC_PORT_POS | (pin) << XMC4XXX_INTC_PIN_POS |                         \
         (eru_src) << XMC4XXX_INTC_ERU_SRC_POS | (line) << XMC4XXX_INTC_LINE_POS)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INFINEON_XMC4XXX_INTC_H_ */
```

## 373.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Schlumberger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_INFINEON_XMC4XXX_INTC_H_`。

## 373.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/infineon-xmc4xxx-intc_8h.html)

---

[上一章](P372_infineon-xmc4xxx-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P374_infineon_mxcrypto.h_源码浏览.md)
