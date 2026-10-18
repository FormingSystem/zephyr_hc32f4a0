---
id: learning.zephyr-docs.api-source-device-reference.page-32
title: renesas-rz-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_renesas-rz-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h.html)。

## 32.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>

```c
/*
 * Copyright (c) 2024-2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZ_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZ_GPIO_H_

/*********************************RZ/A,G,V**************************************/


/* GPIO drive IOLH */
#define RZ_GPIO_IOLH_SHIFT         8U
#define RZ_GPIO_IOLH_SET(iolh_val) (iolh_val << RZ_GPIO_IOLH_SHIFT)

/* GPIO filter */
#define RZ_GPIO_FILTER_SHIFT    10U
#define RZ_GPIO_FILNUM_SHIFT    1U
#define RZ_GPIO_FILCLKSEL_SHIFT 3U
#define RZ_GPIO_FILTER_SET(fillonoff, filnum, filclksel)                                           \
        (((fillonoff) | ((filnum) << RZ_GPIO_FILNUM_SHIFT) |                                       \
          ((filclksel) << RZ_GPIO_FILCLKSEL_SHIFT))                                                \
         << RZ_GPIO_FILTER_SHIFT)

/*******************************************************************************/

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZ_GPIO_H_ */
```

## 32.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

RZ/A、RZ/G、RZ/V 分组分隔线（Section Separator）。

### 注释 3：原第 28 行

GPIO 驱动 IOLH（GPIO Drive IOLH）。

### 注释 4：原第 32 行

GPIO 滤波器（GPIO Filter）。

### 注释 5：原第 41 行

分组分隔线（Section Separator）。

### 注释 6：原第 43 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_RENESAS_RZ_GPIO_H_`。

## 32.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/renesas-rz-gpio_8h.html)

---

[上一章](P031_pwd.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P033_gd32f3x0.h_源码浏览.md)
