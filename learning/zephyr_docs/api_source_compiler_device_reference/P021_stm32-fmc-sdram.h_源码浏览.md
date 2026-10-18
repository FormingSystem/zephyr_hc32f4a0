---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-21
title: stm32-fmc-sdram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-fmc-sdram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_stm32-fmc-sdram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stm32-fmc-sdram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P412_zephyr__dt-bindings__memory-controller__stm32-fmc-sdram.h_文件参考.md)。

## 21.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2020 Teslabs Engineering S.L.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_SDRAM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_STM32_FMC_SDRAM_H_

/* Number of column address bits */
#define STM32_FMC_SDRAM_NC_8 0x00000000UL
#define STM32_FMC_SDRAM_NC_9 0x00000001UL
#define STM32_FMC_SDRAM_NC_10 0x00000002UL
#define STM32_FMC_SDRAM_NC_11 0x00000003UL

/* Number of row address bits */
#define STM32_FMC_SDRAM_NR_11 0x00000000UL
#define STM32_FMC_SDRAM_NR_12 0x00000004UL
#define STM32_FMC_SDRAM_NR_13 0x00000008UL

/* Memory data bus width. */
#define STM32_FMC_SDRAM_MWID_8 0x00000000UL
#define STM32_FMC_SDRAM_MWID_16 0x00000010UL
#define STM32_FMC_SDRAM_MWID_32 0x00000020UL

/* Number of internal banks */
#define STM32_FMC_SDRAM_NB_2 0x00000000UL
#define STM32_FMC_SDRAM_NB_4 0x00000040UL

/* CAS Latency */
#define STM32_FMC_SDRAM_CAS_1 0x00000080UL
#define STM32_FMC_SDRAM_CAS_2 0x00000100UL
#define STM32_FMC_SDRAM_CAS_3 0x00000180UL

/* SDRAM clock configuration */
#define STM32_FMC_SDRAM_SDCLK_DISABLE 0x00000000UL
#define STM32_FMC_SDRAM_SDCLK_PERIOD_2 0x00000800UL
#define STM32_FMC_SDRAM_SDCLK_PERIOD_3 0x00000C00UL

/* Burst read */
#define STM32_FMC_SDRAM_RBURST_DISABLE 0x00000000UL
#define STM32_FMC_SDRAM_RBURST_ENABLE 0x00001000UL

/* Read pipe */
#define STM32_FMC_SDRAM_RPIPE_0 0x00000000UL
#define STM32_FMC_SDRAM_RPIPE_1 0x00002000UL
#define STM32_FMC_SDRAM_RPIPE_2 0x00004000UL

#endif
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Teslabs Engineering S.L.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

列地址位数（column address bits）。

### 注释 3：原第 16 行

行地址位数（row address bits）。

### 注释 4：原第 21 行

存储器数据总线宽度（memory data bus width）。

### 注释 5：原第 26 行

内部存储体（internal banks）的数量。

### 注释 6：原第 30 行

列地址选通延迟（CAS Latency）。

### 注释 7：原第 35 行

同步动态随机存取存储器（SDRAM）时钟配置。

### 注释 8：原第 40 行

突发读取（burst read）。

### 注释 9：原第 44 行

读取流水线（read pipe）。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P412_zephyr__dt-bindings__memory-controller__stm32-fmc-sdram.h_文件参考.md)

---

[上一章](P020_rtl87x2g-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_stm32mp2_clock.h_源码浏览.md)
