---
id: learning.zephyr-docs.api-source-reference.page-350
title: imx943_power.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx943__power_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第350章\_imx943\_power.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx943__power_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx943__power_8h.html)。

## 350.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX943_POWER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX943_POWER_H_

#define IMX943_PD_ANA       0
#define IMX943_PD_AON       1
#define IMX943_PD_BBSM      2
#define IMX943_PD_M7_1      3
#define IMX943_PD_CCMSRCGPC 4
#define IMX943_PD_A55C0     5
#define IMX943_PD_A55C1     6
#define IMX943_PD_A55C2     7
#define IMX943_PD_A55C3     8
#define IMX943_PD_A55P      9
#define IMX943_PD_DDR       10
#define IMX943_PD_DISPLAY   11
#define IMX943_PD_M7_0      12
#define IMX943_PD_HSIO_TOP  13
#define IMX943_PD_HSIO_WAON 14
#define IMX943_PD_NETC      15
#define IMX943_PD_NOC       16
#define IMX943_PD_NPU       17
#define IMX943_PD_WAKEUP    18

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX943_POWER_H_ */
```

## 350.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX943_POWER_H_`。

## 350.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx943__power_8h.html)

---

[上一章](P349_imx943_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P351_imx952_clock.h_源码浏览.md)
