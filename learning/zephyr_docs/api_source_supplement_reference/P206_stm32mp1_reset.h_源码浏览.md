---
id: learning.zephyr-docs.api-source-supplement-reference.page-206
title: stm32mp1_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32mp1__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第206章\_stm32mp1\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp1__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp1__reset_8h.html)。

## 206.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
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
<a id="l00056"></a>
<a id="l00057"></a>

```c
/*
 * Copyright (c) 2022 Google Inc
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP1_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP1_RESET_H_


#define STM32_RESET(bus, bit)                                                                      \
        (((STM32_RESET_BUS_##bus##_CLR) << 17U) | ((STM32_RESET_BUS_##bus##_SET) << 5U) | (bit))

/* RCC bus reset register offset */
#define STM32_RESET_BUS_AHB2_SET   0x998
#define STM32_RESET_BUS_AHB2_CLR   0x99C
#define STM32_RESET_BUS_AHB3_SET   0x9A0
#define STM32_RESET_BUS_AHB3_CLR   0x9A4
#define STM32_RESET_BUS_AHB4_SET   0x9A8
#define STM32_RESET_BUS_AHB4_CLR   0x9AC
#define STM32_RESET_BUS_AHB5_SET   0x190
#define STM32_RESET_BUS_AHB5_CLR   0x194
#define STM32_RESET_BUS_AHB6_SET   0x198
#define STM32_RESET_BUS_AHB6_CLR   0x19C
#define STM32_RESET_BUS_TZAHB6_SET 0x1A0
#define STM32_RESET_BUS_TZAHB6_CLR 0x1A4
#define STM32_RESET_BUS_APB1_SET   0x980
#define STM32_RESET_BUS_APB1_CLR   0x984
#define STM32_RESET_BUS_APB2_SET   0x988
#define STM32_RESET_BUS_APB2_CLR   0x98C
#define STM32_RESET_BUS_APB3_SET   0x990
#define STM32_RESET_BUS_APB3_CLR   0x994
#define STM32_RESET_BUS_APB4_SET   0x180
#define STM32_RESET_BUS_APB4_CLR   0x184
#define STM32_RESET_BUS_APB5_SET   0x188
#define STM32_RESET_BUS_APB5_CLR   0x18C


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP1_RESET_H_ */
```

## 206.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google Inc。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 31 行

复位与时钟控制（RCC）总线复位寄存器的偏移量。

### 注释 3：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_STM32MP1_RESET_H_`。

## 206.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32mp1__reset_8h.html)

---

[上一章](P205_stm32mp1_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P207_stm32n6_reset.h_源码浏览.md)
