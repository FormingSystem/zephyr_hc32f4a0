---
id: learning.zephyr-docs.api-source-reference.page-697
title: realtek-bee-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第697章\_realtek-bee-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h.html)。

## 697.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_BEE_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_BEE_GPIO_H_


#define BEE_GPIO_INPUT_DEBOUNCE_MS_POS 8

#define BEE_GPIO_INPUT_DEBOUNCE_MS_MASK (0xff << BEE_GPIO_INPUT_DEBOUNCE_MS_POS)


#define BEE_GPIO_INPUT_DEBOUNCE_MS(ms) ((0xff & (ms)) << BEE_GPIO_INPUT_DEBOUNCE_MS_POS)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_BEE_GPIO_H_ */
```

## 697.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 41 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_REALTEK_BEE_GPIO_H_`。

## 697.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/realtek-bee-gpio_8h.html)

---

[上一章](P696_rat.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P698_realtek-rts5817-gpio.h_源码浏览.md)
