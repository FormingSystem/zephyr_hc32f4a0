---
id: learning.zephyr-docs.api-source-supplement-reference.page-97
title: it51xxx-i2c.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/it51xxx-i2c_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_it51xxx-i2c.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx-i2c_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx-i2c_8h.html)。

## 97.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>

```c
/*
 * Copyright (c) 2025 ITE Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT51XXX_I2C_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT51XXX_I2C_H_

/* SMBus channel switch selection */
#define SMB_SWITCH_INTERFACE0  1
#define SMB_SWITCH_INTERFACE1  2
#define SMB_SWITCH_INTERFACE2  3
#define SMB_SWITCH_INTERFACE3  4
#define SMB_SWITCH_INTERFACE4  5
#define SMB_SWITCH_INTERFACE5  6
#define SMB_SWITCH_INTERFACE6  7
#define SMB_SWITCH_INTERFACE7  8
#define SMB_SWITCH_INTERFACE8  9
#define SMB_SWITCH_INTERFACE9  10
#define SMB_SWITCH_INTERFACE10 11
#define SMB_SWITCH_INTERFACE11 12
#define SMB_SWITCH_INTERFACE12 13

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT51XXX_I2C_H_ */
```

## 97.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 ITE Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

SMBus 通道切换选择（Channel switch selection）。

### 注释 3：原第 24 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_I2C_IT51XXX_I2C_H_`。

## 97.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx-i2c_8h.html)

---

[上一章](P096_intel_socfpga_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P098_nvs.h_源码浏览.md)
