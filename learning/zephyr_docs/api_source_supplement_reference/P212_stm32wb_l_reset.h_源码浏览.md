---
id: learning.zephyr-docs.api-source-supplement-reference.page-212
title: stm32wb_l_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32wb__l__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第212章\_stm32wb\_l\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb__l__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb__l__reset_8h.html)。

## 212.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="astm32-common_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Google Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32WB_L_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32WB_L_RESET_H_

#include "stm32-common.h"


/* RCC bus reset register offset */
#define STM32_RESET_BUS_AHB1  0x28
#define STM32_RESET_BUS_AHB2  0x2C
#define STM32_RESET_BUS_AHB3  0x30
#define STM32_RESET_BUS_APB1L 0x38
#define STM32_RESET_BUS_APB1H 0x3C
#define STM32_RESET_BUS_APB2  0x40
#define STM32_RESET_BUS_APB3  0x44


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32WB_L_RESET_H_ */
```

## 212.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 20 行

复位与时钟控制（RCC）总线复位寄存器的偏移量。

### 注释 3：原第 31 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32WB_L_RESET_H_`。

## 212.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32wb__l__reset_8h.html)
- [stm32-common.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32-common_8h.html)

---

[上一章](P211_stm32wb0_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P213_stm32wba_reset.h_源码浏览.md)
