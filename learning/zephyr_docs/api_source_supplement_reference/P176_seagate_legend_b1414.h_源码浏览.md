---
id: learning.zephyr-docs.api-source-supplement-reference.page-176
title: seagate_legend_b1414.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/seagate__legend__b1414_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第176章\_seagate\_legend\_b1414.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/seagate__legend__b1414_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/seagate__legend__b1414_8h.html)。

## 176.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2021, Seagate Technology LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_LED_SEAGATE_LEGEND_B1414_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_LED_SEAGATE_LEGEND_B1414_H_

/*
 * At 6 MHz: 1 bit in 166.666 ns
 * 1200 ns ->  7.2  bits
 *  300 ns ->  1.8  bits
 *  900 ns ->  5.4  bits
 */
#define SPI_FREQ        6000000
#define ZERO_FRAME      0x60
#define ONE_FRAME       0x7C

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_LED_SEAGATE_LEGEND_B1414_H_ */
```

## 176.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021, Seagate Technology LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

在 6 MHz 下，1 位持续 166.666 ns：

- 1200 ns → 7.2 位。
- 300 ns → 1.8 位。
- 900 ns → 5.4 位。

### 注释 3：原第 20 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_LED_SEAGATE_LEGEND_B1414_H_`。

## 176.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/seagate__legend__b1414_8h.html)

---

[上一章](P175_sar_cfg_cli.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P177_serial_test.h_源码浏览.md)
