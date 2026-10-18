---
id: learning.zephyr-docs.api-source-reference.page-6
title: adi-max32-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_adi-max32-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h.html)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00015"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>

```c
/*
 * Copyright (c) 2023-2024 Analog Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_MAX32_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_MAX32_GPIO_H_



#define MAX32_GPIO_VSEL_POS    (8U)
#define MAX32_GPIO_VSEL_MASK   (0x01U << MAX32_GPIO_VSEL_POS)
#define MAX32_GPIO_VSEL_VDDIO  (0U << MAX32_GPIO_VSEL_POS)
#define MAX32_GPIO_VSEL_VDDIOH (1U << MAX32_GPIO_VSEL_POS)

#define MAX32_GPIO_DRV_STRENGTH_POS  (9U)
#define MAX32_GPIO_DRV_STRENGTH_MASK (0x03U << MAX32_GPIO_DRV_STRENGTH_POS)
#define MAX32_GPIO_DRV_STRENGTH_0    (0U << MAX32_GPIO_DRV_STRENGTH_POS)
#define MAX32_GPIO_DRV_STRENGTH_1    (1U << MAX32_GPIO_DRV_STRENGTH_POS)
#define MAX32_GPIO_DRV_STRENGTH_2    (2U << MAX32_GPIO_DRV_STRENGTH_POS)
#define MAX32_GPIO_DRV_STRENGTH_3    (3U << MAX32_GPIO_DRV_STRENGTH_POS)

#define MAX32_GPIO_WEAK_PULL_UP_POS   (11U)
#define MAX32_GPIO_WEAK_PULL_UP       (1U << MAX32_GPIO_WEAK_PULL_UP_POS)
#define MAX32_GPIO_WEAK_PULL_DOWN_POS (12U)
#define MAX32_GPIO_WEAK_PULL_DOWN     (1U << MAX32_GPIO_WEAK_PULL_DOWN_POS)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_MAX32_GPIO_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023-2024 Analog Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 69 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_MAX32_GPIO_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/adi-max32-gpio_8h.html)

---

[上一章](P005_ad559x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_adi-max32-hpb.h_源码浏览.md)
