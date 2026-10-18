---
id: learning.zephyr-docs.api-source-reference.page-584
title: nordic-npm6001-gpio.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第584章\_nordic-npm6001-gpio.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h.html)。

## 584.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00022"></a>
<a id="l00028"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00046"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NORDIC_NPM6001_GPIO_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NORDIC_NPM6001_GPIO_H_



#define NPM6001_GPIO_DRIVE_MSK  0x0100U

#define NPM6001_GPIO_DRIVE_NORMAL       (0U << 8U)
#define NPM6001_GPIO_DRIVE_HIGH         (1U << 8U)



#define NPM6001_GPIO_SENSE_MSK  0x0200U

#define NPM6001_GPIO_SENSE_SCHMITT      (0U << 9U)
#define NPM6001_GPIO_SENSE_CMOS         (1U << 9U)



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NORDIC_NRF_GPIO_H_ */
```

## 584.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 61 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_NORDIC_NRF_GPIO_H_`。

## 584.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h.html)

---

[上一章](P583_nordic-npm2100-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P585_nordic-nrf-gpio.h_源码浏览.md)
