---
id: learning.zephyr-docs.api-source-architecture-reference.page-13
title: kinetis_pcc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/kinetis__pcc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_kinetis\_pcc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/kinetis__pcc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P183_zephyr__dt-bindings__clock__kinetis_pcc.h_文件参考.md)。

## 13.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2019 Vestas Wind Systems A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_PCC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_PCC_H_

/* NXP Kinetis Peripheral Clock Controller IP sources */
#define KINETIS_PCC_SRC_NONE_OR_EXT 0 /* Clock off or external clock is used */
#define KINETIS_PCC_SRC_SOSC_ASYNC  1 /* System Oscillator async clock */
#define KINETIS_PCC_SRC_SIRC_ASYNC  2 /* Slow IRC async clock */
#define KINETIS_PCC_SRC_FIRC_ASYNC  3 /* Fast IRC async clock */
#define KINETIS_PCC_SRC_SPLL_ASYNC  6 /* System PLL async clock */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_PCC_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Vestas Wind Systems A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

NXP Kinetis 外设时钟控制器 IP 的时钟源（Peripheral Clock Controller IP Sources）。

### 注释 3：原第 11 行

关闭时钟，或使用外部时钟（External Clock）。

### 注释 4：原第 12 行

系统振荡器异步时钟（System Oscillator Asynchronous Clock）。

### 注释 5：原第 13 行

低速内部 RC 振荡器异步时钟（Slow IRC Asynchronous Clock）。

### 注释 6：原第 14 行

高速内部 RC 振荡器异步时钟（Fast IRC Asynchronous Clock）。

### 注释 7：原第 15 行

系统锁相环异步时钟（System PLL Asynchronous Clock）。

### 注释 8：原第 17 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_KINETIS_PCC_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P183_zephyr__dt-bindings__clock__kinetis_pcc.h_文件参考.md)

---

[上一章](P012_kernel_arch_interface.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_microchip-xec-gpio.h_源码浏览.md)
