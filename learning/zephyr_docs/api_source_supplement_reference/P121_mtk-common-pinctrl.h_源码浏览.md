---
id: learning.zephyr-docs.api-source-supplement-reference.page-121
title: mtk-common-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第121章\_mtk-common-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h.html)。

## 121.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2026 MediaTek Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MTK_COMMON_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MTK_COMMON_PINCTRL_H_

#ifdef __cplusplus
extern "C" {
#endif

/*
 * A pinmux entry packs the pin number and the function selected on it into a
 * single cell: the pin number is held above the low four bits, which hold the
 * function.
 */
#define MTK_PIN_NO(x)       ((x) << 8)
#define MTK_GET_PIN_NO(x)   ((x) >> 8)
#define MTK_GET_PIN_FUNC(x) ((x) & 0xf)

#define MTK_PUPD_SET_R1R0_00 100
#define MTK_PUPD_SET_R1R0_01 101
#define MTK_PUPD_SET_R1R0_10 102
#define MTK_PUPD_SET_R1R0_11 103
#define MTK_RSEL_SET_R1R0_00 104
#define MTK_RSEL_SET_R1R0_01 105
#define MTK_RSEL_SET_R1R0_10 106
#define MTK_RSEL_SET_R1R0_11 107

#define MTK_PULL_SET_RSEL_000 200
#define MTK_PULL_SET_RSEL_001 201
#define MTK_PULL_SET_RSEL_010 202
#define MTK_PULL_SET_RSEL_011 203
#define MTK_PULL_SET_RSEL_100 204
#define MTK_PULL_SET_RSEL_101 205
#define MTK_PULL_SET_RSEL_110 206
#define MTK_PULL_SET_RSEL_111 207

#define MTK_DRIVE_2mA  2
#define MTK_DRIVE_4mA  4
#define MTK_DRIVE_6mA  6
#define MTK_DRIVE_8mA  8
#define MTK_DRIVE_10mA 10
#define MTK_DRIVE_12mA 12
#define MTK_DRIVE_14mA 14
#define MTK_DRIVE_16mA 16
#define MTK_DRIVE_20mA 20
#define MTK_DRIVE_24mA 24
#define MTK_DRIVE_28mA 28
#define MTK_DRIVE_32mA 32

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MTK_COMMON_PINCTRL_H_ */
```

## 121.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 MediaTek Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 14 行

一个引脚复用条目（Pinmux entry）将引脚编号及为其选定的功能打包到单个单元（Cell）中：低四位保存功能，其上的各位保存引脚编号。

### 注释 3：原第 58 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_MTK_COMMON_PINCTRL_H_`。

## 121.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mtk-common-pinctrl_8h.html)

---

[上一章](P120_mspm0-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P122_mtk_mt8188_clock.h_源码浏览.md)
