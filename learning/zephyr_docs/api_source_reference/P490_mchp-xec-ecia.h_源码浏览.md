---
id: learning.zephyr-docs.api-source-reference.page-490
title: mchp-xec-ecia.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第490章\_mchp-xec-ecia.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h.html)。

## 490.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00058"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>

```c
/*
 * Copyright (c) 2021 Microchip Technology
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MCHP_XEC_ECIA_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MCHP_XEC_ECIA_H_


#define MCHP_XEC_ECIA_GIRQ_ENC(g, b) (((g) & 0x1f) + (((b) & 0x1f) << 8))

#define MCHP_XEC_ECIA(g, gb, na, nd)                                    \
        (((g) & 0x1f) + (((gb) & 0x1f) << 8) + (((na) & 0xff) << 16) +  \
        (((nd) & 0xff) << 24))

#define MCHP_XEC_ECIA_GIRQ(e)           ((e) & 0x1f)
#define MCHP_XEC_ECIA_GIRQ_POS(e)       (((e) >> 8) & 0x1f)
#define MCHP_XEC_ECIA_NVIC_AGGR(e)      (((e) >> 16) & 0xff)
#define MCHP_XEC_ECIA_NVIC_DIRECT(e)    (((e) >> 24) & 0xff)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MCHP_XEC_ECIA_H_ */
```

## 490.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Microchip Technology。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INTERRUPT_CONTROLLER_MCHP_XEC_ECIA_H_`。

## 490.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-ecia_8h.html)

---

[上一章](P489_mc3419.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P491_mchp_clock_pic32ck_sg_gc.h_源码浏览.md)
