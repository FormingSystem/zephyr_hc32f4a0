---
id: learning.zephyr-docs.api-source-reference.page-707
title: renesas,ra-sdram.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas_00ra-sdram_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第707章\_renesas,ra-sdram.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas_00ra-sdram_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas_00ra-sdram_8h.html)。

## 707.1\_原始可见代码（Source Code）

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
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_RENESAS_RA_SDRAM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MEMORY_CONTROLLER_RENESAS_RA_SDRAM_H_

#define SDRAM_TRAS_1CYCLES (1)
#define SDRAM_TRAS_2CYCLES (2)
#define SDRAM_TRAS_3CYCLES (3)
#define SDRAM_TRAS_4CYCLES (4)
#define SDRAM_TRAS_5CYCLES (5)
#define SDRAM_TRAS_6CYCLES (6)
#define SDRAM_TRAS_7CYCLES (7)

#define SDRAM_TRCD_1CYCLES (1)
#define SDRAM_TRCD_2CYCLES (2)
#define SDRAM_TRCD_3CYCLES (3)
#define SDRAM_TRCD_4CYCLES (4)

#define SDRAM_TRP_1CYCLES (1)
#define SDRAM_TRP_2CYCLES (2)
#define SDRAM_TRP_3CYCLES (3)
#define SDRAM_TRP_4CYCLES (4)
#define SDRAM_TRP_5CYCLES (5)
#define SDRAM_TRP_6CYCLES (6)
#define SDRAM_TRP_7CYCLES (7)
#define SDRAM_TRP_8CYCLES (8)

#define SDRAM_TWR_1CYCLES (1)
#define SDRAM_TWR_2CYCLES (2)

#define SDRAM_TCL_1CYCLES (1)
#define SDRAM_TCL_2CYCLES (2)
#define SDRAM_TCL_3CYCLES (3)

#define SDRAM_TREFW_1CYCLES  (1)
#define SDRAM_TREFW_2CYCLES  (2)
#define SDRAM_TREFW_3CYCLES  (3)
#define SDRAM_TREFW_4CYCLES  (4)
#define SDRAM_TREFW_5CYCLES  (5)
#define SDRAM_TREFW_6CYCLES  (6)
#define SDRAM_TREFW_7CYCLES  (7)
#define SDRAM_TREFW_8CYCLES  (8)
#define SDRAM_TREFW_9CYCLES  (9)
#define SDRAM_TREFW_10CYCLES (10)
#define SDRAM_TREFW_11CYCLES (11)
#define SDRAM_TREFW_12CYCLES (12)
#define SDRAM_TREFW_13CYCLES (13)
#define SDRAM_TREFW_14CYCLES (14)
#define SDRAM_TREFW_15CYCLES (15)
#define SDRAM_TREFW_16CYCLES (16)

#define SDRAM_AUTO_REFRESH_INTERVAL_3CYCLES  (3)
#define SDRAM_AUTO_REFRESH_INTERVAL_4CYCLES  (4)
#define SDRAM_AUTO_REFRESH_INTERVAL_5CYCLES  (5)
#define SDRAM_AUTO_REFRESH_INTERVAL_6CYCLES  (6)
#define SDRAM_AUTO_REFRESH_INTERVAL_7CYCLES  (7)
#define SDRAM_AUTO_REFRESH_INTERVAL_8CYCLES  (8)
#define SDRAM_AUTO_REFRESH_INTERVAL_9CYCLES  (9)
#define SDRAM_AUTO_REFRESH_INTERVAL_10CYCLES (10)
#define SDRAM_AUTO_REFRESH_INTERVAL_11CYCLES (11)
#define SDRAM_AUTO_REFRESH_INTERVAL_12CYCLES (12)
#define SDRAM_AUTO_REFRESH_INTERVAL_13CYCLES (13)
#define SDRAM_AUTO_REFRESH_INTERVAL_14CYCLES (14)
#define SDRAM_AUTO_REFRESH_INTERVAL_15CYCLES (15)
#define SDRAM_AUTO_REFRESH_INTERVAL_16CYCLES (16)
#define SDRAM_AUTO_REFRESH_INTERVAL_17CYCLES (17)
#define SDRAM_AUTO_REFRESH_INTERVAL_18CYCLES (18)
#define SDRAM_AUTO_REFRESH_INTERVAL_19CYCLES (19)
#define SDRAM_AUTO_REFRESH_INTERVAL_20CYCLES (20)

#define SDRAM_AUTO_REFRESH_COUNT_1TIMES  (1)
#define SDRAM_AUTO_REFRESH_COUNT_2TIMES  (2)
#define SDRAM_AUTO_REFRESH_COUNT_3TIMES  (3)
#define SDRAM_AUTO_REFRESH_COUNT_4TIMES  (4)
#define SDRAM_AUTO_REFRESH_COUNT_5TIMES  (5)
#define SDRAM_AUTO_REFRESH_COUNT_6TIMES  (6)
#define SDRAM_AUTO_REFRESH_COUNT_7TIMES  (7)
#define SDRAM_AUTO_REFRESH_COUNT_8TIMES  (8)
#define SDRAM_AUTO_REFRESH_COUNT_9TIMES  (9)
#define SDRAM_AUTO_REFRESH_COUNT_10TIMES (10)
#define SDRAM_AUTO_REFRESH_COUNT_11TIMES (11)
#define SDRAM_AUTO_REFRESH_COUNT_12TIMES (12)
#define SDRAM_AUTO_REFRESH_COUNT_13TIMES (13)
#define SDRAM_AUTO_REFRESH_COUNT_14TIMES (14)
#define SDRAM_AUTO_REFRESH_COUNT_15TIMES (15)

#define SDRAM_AUTO_PRECHARGE_CYCLE_3CYCLES  (3)
#define SDRAM_AUTO_PRECHARGE_CYCLE_4CYCLES  (4)
#define SDRAM_AUTO_PRECHARGE_CYCLE_5CYCLES  (5)
#define SDRAM_AUTO_PRECHARGE_CYCLE_6CYCLES  (6)
#define SDRAM_AUTO_PRECHARGE_CYCLE_7CYCLES  (7)
#define SDRAM_AUTO_PRECHARGE_CYCLE_8CYCLES  (8)
#define SDRAM_AUTO_PRECHARGE_CYCLE_9CYCLES  (9)
#define SDRAM_AUTO_PRECHARGE_CYCLE_10CYCLES (10)

#endif
```

## 707.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 707.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas_00ra-sdram_8h.html)

---

[上一章](P706_renesas-rzt2m-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P708_renesas_elc.h_源码浏览.md)
