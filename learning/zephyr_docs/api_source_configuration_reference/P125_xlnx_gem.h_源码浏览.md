---
id: learning.zephyr-docs.api-source-configuration-reference.page-125
title: xlnx_gem.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xlnx__gem_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_xlnx\_gem.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xlnx__gem_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xlnx__gem_8h.html)。

## 125.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2021-2022, Weidmueller Interface GmbH & Co. KG
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_ETHERNET_XLNX_GEM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_ETHERNET_XLNX_GEM_H_

/* AMBA AHB burst length */
#define XLNX_GEM_AMBA_AHB_BURST_SINGLE 1
#define XLNX_GEM_AMBA_AHB_BURST_INCR4  4
#define XLNX_GEM_AMBA_AHB_BURST_INCR8  8
#define XLNX_GEM_AMBA_AHB_BURST_INCR16 16

/* Hardware RX buffer size */
#define XLNX_GEM_HW_RX_BUFFER_SIZE_1KB 0
#define XLNX_GEM_HW_RX_BUFFER_SIZE_2KB 1
#define XLNX_GEM_HW_RX_BUFFER_SIZE_4KB 2
#define XLNX_GEM_HW_RX_BUFFER_SIZE_8KB 3

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_ETHERNET_XLNX_GEM_H_ */
```

## 125.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2022, Weidmueller Interface GmbH & Co. KG。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

AMBA 高性能总线（AHB）的突发长度（Burst length）。

### 注释 3：原第 15 行

硬件接收（RX）缓冲区大小。

### 注释 4：原第 21 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_ETHERNET_XLNX_GEM_H_`。

## 125.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xlnx__gem_8h.html)

---

[上一章](P124_xg29-clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P126_xmc4xxx-pinctrl.h_源码浏览.md)
