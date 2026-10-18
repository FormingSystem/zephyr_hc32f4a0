---
id: learning.zephyr-docs.api-source-reference.page-380
title: input_hid.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第380章\_input\_hid.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h.html)。

## 380.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="agroup__input__interface_html_ga094b3ccfc2e111c4b2a000e9c2fe133c"></a>
<a id="agroup__input__interface_html_ga86ac2267d08e91bcc09c5b091042cfde"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/*
 * Copyright 2024 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_HID_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_HID_H_


int16_t input_to_hid_code(uint16_t input_code);

uint8_t input_to_hid_modifier(uint16_t input_code);


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_HID_H_ */
```

## 380.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 48 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_HID_H_`。

## 380.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h.html)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [input_to_hid_code](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga094b3ccfc2e111c4b2a000e9c2fe133c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [input_to_hid_modifier](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga86ac2267d08e91bcc09c5b091042cfde)

---

[上一章](P379_input_crsf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P381_input_keymap.h_源码浏览.md)
