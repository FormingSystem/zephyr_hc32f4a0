---
id: learning.zephyr-docs.api-source-reference.page-191
title: mipi_dbi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_mipi\_dbi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html)。

## 191.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
<a id="l00032"></a>
<a id="l00053"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00126"></a>
<a id="l00133"></a>
<a id="l00140"></a>
<a id="l00155"></a>
<a id="l00161"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00221"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>

```c
/*
 * Copyright 2024,2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MIPI_DBI_MIPI_DBI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MIPI_DBI_MIPI_DBI_H_


#define MIPI_DBI_MODE_SPI_3WIRE 0x1
#define MIPI_DBI_MODE_SPI_4WIRE 0x2
#define MIPI_DBI_MODE_6800_BUS_16_BIT 0x3
#define MIPI_DBI_MODE_6800_BUS_9_BIT  0x4
#define MIPI_DBI_MODE_6800_BUS_8_BIT  0x5
#define MIPI_DBI_MODE_8080_BUS_16_BIT 0x6
#define MIPI_DBI_MODE_8080_BUS_9_BIT  0x7
#define MIPI_DBI_MODE_8080_BUS_8_BIT  0x8

#define MIPI_DBI_MODE_RGB332 (0x1 << 4U)
#define MIPI_DBI_MODE_RGB444 (0x2 << 4U)
#define MIPI_DBI_MODE_RGB565 (0x3 << 4U)
#define MIPI_DBI_MODE_RGB666_1 (0x4 << 4U)
#define MIPI_DBI_MODE_RGB666_2 (0x5 << 4U)
#define MIPI_DBI_MODE_RGB888_1 (0x6 << 4U)
#define MIPI_DBI_MODE_RGB888_2 (0x7 << 4U)

#define MIPI_DBI_TE_NO_EDGE 0x0

#define MIPI_DBI_TE_RISING_EDGE 0x1

#define MIPI_DBI_TE_FALLING_EDGE 0x2

#define MIPI_DBI_SPI_XFR_8BIT 8
#define MIPI_DBI_SPI_XFR_16BIT 16



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MIPI_DBI_MIPI_DBI_H_ */
```

## 191.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024,2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 249 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MIPI_DBI_MIPI_DBI_H_`。

## 191.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2mipi__dbi_2mipi__dbi_8h.html)

---

[上一章](P190_dma_smartbond.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P192_mipi_dsi.h_源码浏览.md)
