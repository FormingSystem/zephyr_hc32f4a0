---
id: learning.zephyr-docs.api-source-reference.page-352
title: imx952_power.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第352章\_imx952\_power.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h.html)。

## 352.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>

```c
/*
 * SPDX-FileCopyrightText: Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX952_POWER_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX952_POWER_H_


#define IMX952_PD_ANA           0
#define IMX952_PD_AON           1
#define IMX952_PD_BBSM          2
#define IMX952_PD_CAMERA        3
#define IMX952_PD_CCMSRCGPC     4
#define IMX952_PD_A55C0         5
#define IMX952_PD_A55C1         6
#define IMX952_PD_A55C2         7
#define IMX952_PD_A55C3         8
#define IMX952_PD_A55P          9
#define IMX952_PD_DDR           10
#define IMX952_PD_DISPLAY       11
#define IMX952_PD_GPU           12
#define IMX952_PD_HSIO_TOP      13
#define IMX952_PD_HSIO_WAON     14
#define IMX952_PD_M7            15
#define IMX952_PD_NETC          16
#define IMX952_PD_NOC           17
#define IMX952_PD_NPU           18
#define IMX952_PD_VPU           19
#define IMX952_PD_WAKEUP        20

#define IMX952_NUM_MIX_SLICE    21


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX952_POWER_H_ */
```

## 352.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：Copyright 2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_POWER_IMX952_POWER_H_`。

## 352.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx952__power_8h.html)

---

[上一章](P351_imx952_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P353_imx95_clock.h_源码浏览.md)
