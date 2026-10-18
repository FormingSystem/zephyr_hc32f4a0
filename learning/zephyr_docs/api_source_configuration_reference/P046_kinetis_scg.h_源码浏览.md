---
id: learning.zephyr-docs.api-source-configuration-reference.page-46
title: kinetis_scg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kinetis__scg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_kinetis\_scg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__scg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__scg_8h.html)。

## 46.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2019 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SCG_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SCG_H_

/* SCG system oscillator mode */
#define KINETIS_SCG_SOSC_MODE_EXT        0U
#define KINETIS_SCG_SOSC_MODE_LOW_POWER  4U
#define KINETIS_SCG_SOSC_MODE_HIGH_GAIN 12U

/* SCG clock controller clock names */
#define KINETIS_SCG_CORESYS_CLK          0U
#define KINETIS_SCG_BUS_CLK              1U
#define KINETIS_SCG_FLEXBUS_CLK          2U
#define KINETIS_SCG_FLASH_CLK            3U
#define KINETIS_SCG_SOSC_CLK             4U
#define KINETIS_SCG_SIRC_CLK             5U
#define KINETIS_SCG_FIRC_CLK             6U
#define KINETIS_SCG_SPLL_CLK             7U
#define KINETIS_SCG_SOSC_ASYNC_DIV1_CLK  8U
#define KINETIS_SCG_SOSC_ASYNC_DIV2_CLK  9U
#define KINETIS_SCG_SIRC_ASYNC_DIV1_CLK 10U
#define KINETIS_SCG_SIRC_ASYNC_DIV2_CLK 11U
#define KINETIS_SCG_FIRC_ASYNC_DIV1_CLK 12U
#define KINETIS_SCG_FIRC_ASYNC_DIV2_CLK 13U
#define KINETIS_SCG_SPLL_ASYNC_DIV1_CLK 14U
#define KINETIS_SCG_SPLL_ASYNC_DIV2_CLK 15U
#define KINETIS_SCG_LPFLL_CLK           16U

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SCG_H_ */
```

## 46.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Vestas Wind Systems A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

系统时钟发生器（SCG）的系统振荡器模式。

### 注释 3：原第 15 行

SCG 时钟控制器的时钟名称。

### 注释 4：原第 34 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_SCG_H_`。

## 46.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__scg_8h.html)

---

[上一章](P045_ite-it51xxx-clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P047_kinetis_sim.h_源码浏览.md)
