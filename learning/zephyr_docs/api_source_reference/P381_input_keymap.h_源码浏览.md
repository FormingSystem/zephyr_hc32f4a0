---
id: learning.zephyr-docs.api-source-reference.page-381
title: input_keymap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__keymap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第381章\_input\_keymap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__keymap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__keymap_8h.html)。

## 381.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>

```c
/*
 * Copyright 2024 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_KEYMAP_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_KEYMAP_H_


#define MATRIX_ROW(keymap_entry) (((keymap_entry) >> 24) & 0xff)

#define MATRIX_COL(keymap_entry) (((keymap_entry) >> 16) & 0xff)

#define MATRIX_CODE(keymap_entry) (keymap_entry & 0xffff)


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_KEYMAP_H_ */
```

## 381.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_KEYMAP_H_`。

## 381.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__keymap_8h.html)

---

[上一章](P380_input_hid.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P382_input_nunchuk.h_源码浏览.md)
