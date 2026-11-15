---
id: learning.zephyr-docs.api-source-reference.page-834
title: stm32f427_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f427__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第834章\_stm32f427\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32f427__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/stm32f427__clock_8h.html)。

## 834.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="astm32f4__clock_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F427_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F427_CLOCK_H_

#include <zephyr/dt-bindings/clock/stm32f4_clock.h>


#define DCKCFGR_REG             0x8C

#define CKDFSDM2A_SEL(val)      STM32_DT_CLOCK_SELECT((val), 14, 14, DCKCFGR_REG)
#define CKDFSDM1A_SEL(val)      STM32_DT_CLOCK_SELECT((val), 15, 15, DCKCFGR_REG)
#define SAI1A_SEL(val)          STM32_DT_CLOCK_SELECT((val), 21, 20, DCKCFGR_REG)
#define SAI1B_SEL(val)          STM32_DT_CLOCK_SELECT((val), 23, 22, DCKCFGR_REG)
#define CK48M_SEL(val)          STM32_DT_CLOCK_SELECT((val), 27, 27, DCKCFGR_REG)
#define SDMMC_SEL(val)          STM32_DT_CLOCK_SELECT((val), 28, 28, DCKCFGR_REG)
#define DSI_SEL(val)            STM32_DT_CLOCK_SELECT((val), 29, 29, DCKCFGR_REG)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F427_CLOCK_H_ */
```

## 834.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 28 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_STM32F427_CLOCK_H_`。

## 834.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/stm32f427__clock_8h.html)
- [zephyr/dt-bindings/clock/stm32f4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f4__clock_8h.html)
- [stm32f4_clock.h](https://docs.zephyrproject.org/latest/doxygen/html/stm32f4__clock_8h.html)

---

[上一章](P833_stm32_pwm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P835_stm32h5_iocell.h_源码浏览.md)
