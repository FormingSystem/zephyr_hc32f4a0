---
id: learning.zephyr-docs.api-source-reference.page-119
title: cst8xx-gesture-codes.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第119章\_cst8xx-gesture-codes.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h.html)。

## 119.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>

```c
/*
 * Copyright (c) 2024 Felipe Neves.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_CST8XX_GESTURE_CODES_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_CST8XX_GESTURE_CODES_H_

#define CST8XX_GESTURE_CODE_NONE         0x00

#define CST8XX_GESTURE_CODE_SWIPE_UP     0x01

#define CST8XX_GESTURE_CODE_SWIPE_DOWN   0x02

#define CST8XX_GESTURE_CODE_SWIPE_LEFT   0x03

#define CST8XX_GESTURE_CODE_SWIPE_RIGHT  0x04

#define CST8XX_GESTURE_CODE_SINGLE_CLICK 0x05

#define CST8XX_GESTURE_CODE_DOUBLE_CLICK 0x0B

#define CST8XX_GESTURE_CODE_LONG_PRESS   0x0C

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_CST8XX_GESTURE_CODES_H_ */
```

## 119.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Felipe Neves.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 55 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_INPUT_CST8XX_GESTURE_CODES_H_`。

## 119.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cst8xx-gesture-codes_8h.html)

---

[上一章](P118_cpu_freq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P120_dai.h_源码浏览.md)
