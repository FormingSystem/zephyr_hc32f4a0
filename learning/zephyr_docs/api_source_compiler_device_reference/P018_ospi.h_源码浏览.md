---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-18
title: ospi.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ospi_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_ospi.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ospi_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P083_zephyr__dt-bindings__flash_controller__ospi.h_文件参考.md)。

## 18.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>

```c
/*
 * Copyright (c) 2022 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_OSPI_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_OSPI_H_


/* OSPI mode operating on 1 line, 2 lines, 4 lines or 8 lines */
/* 1 Cmd Line, 1 Address Line and 1 Data Line    */
#define OSPI_SPI_MODE                     1
/* 2 Cmd Lines, 2 Address Lines and 2 Data Lines */
#define OSPI_DUAL_MODE                    2
/* 4 Cmd Lines, 4 Address Lines and 4 Data Lines */
#define OSPI_QUAD_MODE                    4
/* 8 Cmd Lines, 8 Address Lines and 8 Data Lines */
#define OSPI_OPI_MODE                     8

/* OSPI mode operating on Single or Double Transfer Rate */
/* Single Transfer Rate */
#define OSPI_STR_TRANSFER                 1
/* Double Transfer Rate */
#define OSPI_DTR_TRANSFER                 2

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_OSPI_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

使用 1、2、4 或 8 条线运行的 OSPI 模式。

### 注释 3：原第 18 行

1 条命令线（Cmd Line）、1 条地址线（Address Line）和 1 条数据线（Data Line）。

### 注释 4：原第 20 行

2 条命令线、2 条地址线和 2 条数据线。

### 注释 5：原第 22 行

4 条命令线、4 条地址线和 4 条数据线。

### 注释 6：原第 24 行

8 条命令线、8 条地址线和 8 条数据线。

### 注释 7：原第 27 行

以单倍或双倍传输速率（Single/Double Transfer Rate）运行的 OSPI 模式。

### 注释 8：原第 28 行

单倍传输速率（Single Transfer Rate）。

### 注释 9：原第 30 行

双倍传输速率（Double Transfer Rate）。

### 注释 10：原第 33 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_FLASH_CONTROLLER_OSPI_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P083_zephyr__dt-bindings__flash_controller__ospi.h_文件参考.md)

---

[上一章](P017_tle9104.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_pd.h_源码浏览.md)
