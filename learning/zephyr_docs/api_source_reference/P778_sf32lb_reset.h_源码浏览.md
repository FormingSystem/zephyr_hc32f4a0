---
id: learning.zephyr-docs.api-source-reference.page-778
title: sf32lb_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第778章\_sf32lb\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb__reset_8h.html)。

## 778.1\_原始可见代码（Source Code）

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
 * Copyright (c) 2025 Qingsong Gou <gouqs@hotmail.com>
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SF32LB_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SF32LB_RESET_H_

#define SF32LB_RESET_DMAC1          (0U)
#define SF32LB_RESET_MAILBOX1       (1U)
#define SF32LB_RESET_PINMUX1        (2U)
#define SF32LB_RESET_USART1         (3U)
#define SF32LB_RESET_USART2         (4U)
#define SF32LB_RESET_EZIP           (5U)
#define SF32LB_RESET_EPIC           (6U)
#define SF32LB_RESET_LCDC1          (7U)
#define SF32LB_RESET_I2S1           (8U)
#define SF32LB_RESET_SYSCFG1        (10U)
#define SF32LB_RESET_EFUSEC         (11U)
#define SF32LB_RESET_AES            (12U)
#define SF32LB_RESET_CRC1           (13U)
#define SF32LB_RESET_TRNG           (14U)
#define SF32LB_RESET_GPTIM1         (15U)
#define SF32LB_RESET_GPTIM2         (16U)
#define SF32LB_RESET_BTIM1          (17U)
#define SF32LB_RESET_BTIM2          (18U)
#define SF32LB_RESET_SPI1           (20U)
#define SF32LB_RESET_SPI2           (21U)
#define SF32LB_RESET_EXTDMA         (22U)
#define SF32LB_RESET_PDM1           (25U)
#define SF32LB_RESET_I2C1           (27U)
#define SF32LB_RESET_I2C2           (28U)
#define SF32LB_RESET_PTC1           (31U)

#define SF32LB_RESET_GPIO1          (32U)
#define SF32LB_RESET_MPI1           (33U)
#define SF32LB_RESET_MPI2           (34U)
#define SF32LB_RESET_SDMMC1         (36U)
#define SF32LB_RESET_USBC           (38U)
#define SF32LB_RESET_I2C3           (40U)
#define SF32LB_RESET_ATIM1          (41U)
#define SF32LB_RESET_USART3         (44U)
#define SF32LB_RESET_AUDCODEC       (51U)
#define SF32LB_RESET_AUDPRC         (52U)
#define SF32LB_RESET_GPADC          (54U)
#define SF32LB_RESET_TSEN           (55U)
#define SF32LB_RESET_I2C4           (57U)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SF32LB_RESET_H_ */
```

## 778.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Qingsong Gou <gouqs@hotmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_SF32LB_RESET_H_`。

## 778.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb__reset_8h.html)

---

[上一章](P777_sf32lb52x-dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P779_sgp40.h_源码浏览.md)
