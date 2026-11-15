---
id: learning.zephyr-docs.api-source-reference.page-654
title: pinctrl-rzn-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzn-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第654章\_pinctrl-rzn-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzn-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzn-common_8h.html)。

## 654.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00019"></a>
<a id="l00057"></a>
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
<a id="l00095"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>

```c
/*
 * Copyright (c) 2025-2026 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZN_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZN_COMMON_H_




#define PORT_00 0x0000
#define PORT_01 0x0100
#define PORT_02 0x0200
#define PORT_03 0x0300
#define PORT_04 0x0400
#define PORT_05 0x0500
#define PORT_06 0x0600
#define PORT_07 0x0700
#define PORT_08 0x0800
#define PORT_09 0x0900
#define PORT_10 0x0A00
#define PORT_11 0x0B00
#define PORT_12 0x0C00
#define PORT_13 0x0D00
#define PORT_14 0x0E00
#define PORT_15 0x0F00
#define PORT_16 0x1000
#define PORT_17 0x1100
#define PORT_18 0x1200
#define PORT_19 0x1300
#define PORT_20 0x1400
#define PORT_21 0x1500
#define PORT_22 0x1600
#define PORT_23 0x1700
#define PORT_24 0x1800
#define PORT_25 0x1900
#define PORT_26 0x1A00
#define PORT_27 0x1B00
#define PORT_29 0x1D00
#define PORT_30 0x1E00
#define PORT_31 0x1F00
#define PORT_33 0x2100
#define PORT_34 0x2200


#define RZN_PINMUX(port, pin, func) (port | pin | (func << 16))


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZN_COMMON_H_ */
```

## 654.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025-2026 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 109 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZN_COMMON_H_`。

## 654.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzn-common_8h.html)

---

[上一章](P653_pinctrl-rzg3e.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P655_pinctrl-zynq.h_源码浏览.md)
