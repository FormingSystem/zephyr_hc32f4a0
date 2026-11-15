---
id: learning.zephyr-docs.api-source-reference.page-713
title: renesas_rz_cgc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第713章\_renesas\_rz\_cgc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h.html)。

## 713.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00038"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="aclock__control_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RZ_CGC_H_
#define ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RZ_CGC_H_

#include <zephyr/drivers/clock_control.h>


#define RZ_CGC_SUBCLK_DIV(subclk)                                                                  \
        UTIL_CAT(RZ_CGC_DIV_, DT_NODE_FULL_NAME_UPPER_TOKEN(subclk))                               \
        (DT_PROP(subclk, div))

#define RZ_CGC_SUBCLK_MUL(subclk)                                                                  \
        UTIL_CAT(RZ_CGC_MUL_, DT_NODE_FULL_NAME_UPPER_TOKEN(subclk))                               \
        (DT_PROP(subclk, mul))

#define RZ_CGC_DIV_CKIO(n)    UTIL_CAT(BSP_CLOCKS_CKIO_ICLK_DIV, n)
#define RZ_CGC_MUL_CPU0CLK(n) UTIL_CAT(BSP_CLOCKS_FSELCPU0_ICLK_MUL, n)
#define RZ_CGC_MUL_CPU1CLK(n) UTIL_CAT(BSP_CLOCKS_FSELCPU1_ICLK_MUL, n)


#endif /* ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RZ_CGC_H_ */
```

## 713.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 51 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CLOCK_CONTROL_RENESAS_RZ_CGC_H_`。

## 713.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__cgc_8h.html)
- [zephyr/drivers/clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)
- [clock_control.h](../timer_reference/P095_时钟控制头文件参考.md)

---

[上一章](P712_renesas_rx_external_interrupt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P714_renesas_rza2m_dma.h_源码浏览.md)
