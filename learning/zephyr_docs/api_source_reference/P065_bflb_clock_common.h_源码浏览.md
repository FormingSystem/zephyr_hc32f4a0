---
id: learning.zephyr-docs.api-source-reference.page-65
title: bflb_clock_common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_bflb\_clock\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html)。

## 65.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>

```c
/*
 * Copyright (c) 2025-2026 MASSDRIVER EI (massdriver.space)
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_CLOCK_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_CLOCK_COMMON_H_


#ifndef DT_FREQ_M
#define DT_FREQ_M MHZ
#endif


#define BFLB_CLKID_CLK_ROOT     0
#define BFLB_CLKID_CLK_RC32M    1
#define BFLB_CLKID_CLK_CRYSTAL  2
#define BFLB_CLKID_CLK_BCLK     3
#define BFLB_CLKID_CLK_F32K     4
#define BFLB_CLKID_CLK_XTAL32K  5
#define BFLB_CLKID_CLK_RC32K    6
#define BFLB_CLKID_CLK_PRIVATE  7

#define BFLB_FORCE_ROOT_RC32M   32
#define BFLB_FORCE_ROOT_CRYSTAL 33
#define BFLB_FORCE_ROOT_PLL     34

#define BFLB_RC32M_FREQUENCY    (DT_FREQ_M(32))

#define BFLB_F32K_FREQUENCY     32768U

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_CLOCK_COMMON_H_ */
```

## 65.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 MASSDRIVER EI (massdriver.space)。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_BFLB_CLOCK_COMMON_H_`。

## 65.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bflb__clock__common_8h.html)

---

[上一章](P064_bflb_bl808_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P066_biometrics.h_源码浏览.md)
