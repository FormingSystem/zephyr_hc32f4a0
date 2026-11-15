---
id: learning.zephyr-docs.api-source-reference.page-34
title: arducam-ffc-40pin-connector.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arducam-ffc-40pin-connector_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_arducam-ffc-40pin-connector.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arducam-ffc-40pin-connector_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arducam-ffc-40pin-connector_8h.html)。

## 34.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
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
<a id="l00054"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUCAM_FFC_40PIN_CONNECTOR_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUCAM_FFC_40PIN_CONNECTOR_H_


#define ARDUCAM_FFC_40PIN_MIPI_CSI_DL1_P 5
#define ARDUCAM_FFC_40PIN_MIPI_CSI_DL1_N 6
#define ARDUCAM_FFC_40PIN_MIPI_CSI_CL_P  8
#define ARDUCAM_FFC_40PIN_MIPI_CSI_CL_N  9
#define ARDUCAM_FFC_40PIN_MIPI_CSI_DL0_P 11
#define ARDUCAM_FFC_40PIN_MIPI_CSI_DL0_N 12

#define ARDUCAM_FFC_40PIN_D11   2
#define ARDUCAM_FFC_40PIN_D10   3
#define ARDUCAM_FFC_40PIN_D9    5
#define ARDUCAM_FFC_40PIN_D8    6
#define ARDUCAM_FFC_40PIN_D7    8
#define ARDUCAM_FFC_40PIN_D6    9
#define ARDUCAM_FFC_40PIN_D5    11
#define ARDUCAM_FFC_40PIN_D4    12
#define ARDUCAM_FFC_40PIN_D3    14
#define ARDUCAM_FFC_40PIN_D2    15
#define ARDUCAM_FFC_40PIN_D1    17
#define ARDUCAM_FFC_40PIN_D0    18
#define ARDUCAM_FFC_40PIN_VSYNC 23
#define ARDUCAM_FFC_40PIN_HSYNC 24

#define ARDUCAM_FFC_40PIN_SCL   20
#define ARDUCAM_FFC_40PIN_SDA   21
#define ARDUCAM_FFC_40PIN_RESET 25
#define ARDUCAM_FFC_40PIN_XCLK  26
#define ARDUCAM_FFC_40PIN_PCLK  27
#define ARDUCAM_FFC_40PIN_INT   28


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUCAM_FFC_40PIN_CONNECTOR_H_ */
```

## 34.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ARDUCAM_FFC_40PIN_CONNECTOR_H_`。

## 34.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arducam-ffc-40pin-connector_8h.html)

---

[上一章](P033_apds9960.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P035_arducam_mega.h_源码浏览.md)
