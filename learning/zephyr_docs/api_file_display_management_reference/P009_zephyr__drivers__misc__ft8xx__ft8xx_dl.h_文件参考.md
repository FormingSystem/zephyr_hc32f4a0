---
id: learning.zephyr-docs.api-file-display-management-reference.page-9
title: zephyr__drivers__misc__ft8xx__ft8xx_dl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_drivers\_\_misc\_\_ft8xx\_\_ft8xx\_dl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__dl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8XX显示列表命令（Display List Commands）。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

FT8XX显示列表命令（Display List Commands）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_ga28f7596c367f67f73d701b792300aa09"></a>

```c
#define FT8XX_BITMAPS 1U
```

相关声明：[FT8XX_BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga28f7596c367f67f73d701b792300aa09)。

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="r_ga1d6f49b3817f9927fa1cd3cd42820490"></a>

```c
#define FT8XX_POINTS 2U
```

相关声明：[FT8XX_POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d6f49b3817f9927fa1cd3cd42820490)。

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="r_ga62bcf30c7a9eae4c468e1c7de144ad01"></a>

```c
#define FT8XX_LINES 3U
```

相关声明：[FT8XX_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga62bcf30c7a9eae4c468e1c7de144ad01)。

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

<a id="r_gac1b1188c36a4078e7db50d3c5aee7d25"></a>

```c
#define FT8XX_LINE_STRIP 4U
```

相关声明：[FT8XX_LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gac1b1188c36a4078e7db50d3c5aee7d25)。

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="r_ga0b3ce2828323978e9648bfd07caa1065"></a>

```c
#define FT8XX_EDGE_STRIP_R 5U
```

相关声明：[FT8XX_EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga0b3ce2828323978e9648bfd07caa1065)。

向右延伸的边缘带（Edge Strips）。

<a id="r_ga97229abf592bba4039f19a98451cdc5b"></a>

```c
#define FT8XX_EDGE_STRIP_L 6U
```

相关声明：[FT8XX_EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga97229abf592bba4039f19a98451cdc5b)。

向左延伸的边缘带（Edge Strips）。

<a id="r_gaf5ad60bbe137dbf64281ad8d0be051e0"></a>

```c
#define FT8XX_EDGE_STRIP_A 7U
```

相关声明：[FT8XX_EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gaf5ad60bbe137dbf64281ad8d0be051e0)。

向上延伸的边缘带（Edge Strips）。

<a id="r_ga9aff3a3c58e12b990130271e845662a8"></a>

```c
#define FT8XX_EDGE_STRIP_B 8U
```

相关声明：[FT8XX_EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga9aff3a3c58e12b990130271e845662a8)。

向下延伸的边缘带（Edge Strips）。

<a id="r_ga05077568fea624ed7e3f9e3f6e8d72b8"></a>

```c
#define FT8XX_RECTS 9U
```

相关声明：[FT8XX_RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga05077568fea624ed7e3f9e3f6e8d72b8)。

圆角矩形（Round-cornered Rectangles），可使用 `FT8XX_LINE_WIDTH` 调整圆角曲率。

<a id="r_ga25324ac604e037baf26cdd37341bee44"></a>

```c
#define FT8XX_BEGIN(prim)
```

相关声明：[FT8XX_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga25324ac604e037baf26cdd37341bee44)。

开始绘制图形图元（Graphics Primitive）。

<a id="r_gab0fb60eec6f4c3b68d47f61886e7b933"></a>

```c
#define FT8XX_CLEAR(c, s, t)
```

相关声明：[FT8XX_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gab0fb60eec6f4c3b68d47f61886e7b933)。

将缓冲区清除为预设值（Preset Values）。

<a id="r_ga180b0ed70243277462cf303bc788e094"></a>

```c
#define FT8XX_CLEAR_COLOR_RGB(red, green, blue)
```

相关声明：[FT8XX_CLEAR_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga180b0ed70243277462cf303bc788e094)。

指定红、绿、蓝通道的清除值（Clear Values）。

<a id="r_ga3bc794705028fc7e8e1b742db180055d"></a>

```c
#define FT8XX_COLOR_RGB(red, green, blue)
```

相关声明：[FT8XX_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga3bc794705028fc7e8e1b742db180055d)。

设置当前红、绿、蓝颜色（Current Color）。

<a id="r_ga135472b1cdf30d4bd69372e36c9960ce"></a>

```c
#define FT8XX_DISPLAY()
```

相关声明：[FT8XX_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga135472b1cdf30d4bd69372e36c9960ce)。

结束显示列表（Display List）。

<a id="r_ga8a9d0eb6521459eb7ce50b397de194d9"></a>

```c
#define FT8XX_END()
```

相关声明：[FT8XX_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga8a9d0eb6521459eb7ce50b397de194d9)。

结束图形图元（Graphics Primitive）的绘制。

<a id="r_ga1d22204625ef070a6b8d16af7ad97578"></a>

```c
#define FT8XX_LINE_WIDTH(width)
```

相关声明：[FT8XX_LINE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d22204625ef070a6b8d16af7ad97578)。

指定使用 `FT8XX_LINES` 图元绘制的线宽（Line Width）。

<a id="r_gab0721051bb3f3cb9f555f696f36dfbbf"></a>

```c
#define FT8XX_TAG(s)
```

相关声明：[FT8XX_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gab0721051bb3f3cb9f555f696f36dfbbf)。

为后续图形对象附加标签值（Tag Value）。

<a id="r_ga2648ab069991c02b2e8de62bf13913ab"></a>

```c
#define FT8XX_VERTEX2F(x, y)
```

相关声明：[FT8XX_VERTEX2F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga2648ab069991c02b2e8de62bf13913ab)。

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

<a id="r_ga560836cd8c85599f24e5623a3e286b12"></a>

```c
#define FT8XX_VERTEX2II(x, y, handle, cell)
```

相关声明：[FT8XX_VERTEX2II](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga560836cd8c85599f24e5623a3e286b12)。

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。


## 9.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P280_ft8xx_dl.h_源码浏览.md)
- [FT8XX_BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga28f7596c367f67f73d701b792300aa09)
- [FT8XX_POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d6f49b3817f9927fa1cd3cd42820490)
- [FT8XX_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga62bcf30c7a9eae4c468e1c7de144ad01)
- [FT8XX_LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gac1b1188c36a4078e7db50d3c5aee7d25)
- [FT8XX_EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga0b3ce2828323978e9648bfd07caa1065)
- [FT8XX_EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga97229abf592bba4039f19a98451cdc5b)
- [FT8XX_EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gaf5ad60bbe137dbf64281ad8d0be051e0)
- [FT8XX_EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga9aff3a3c58e12b990130271e845662a8)
- [FT8XX_RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga05077568fea624ed7e3f9e3f6e8d72b8)
- [FT8XX_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga25324ac604e037baf26cdd37341bee44)
- [FT8XX_CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gab0fb60eec6f4c3b68d47f61886e7b933)
- [FT8XX_CLEAR_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga180b0ed70243277462cf303bc788e094)
- [FT8XX_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga3bc794705028fc7e8e1b742db180055d)
- [FT8XX_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga135472b1cdf30d4bd69372e36c9960ce)
- [FT8XX_END](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga8a9d0eb6521459eb7ce50b397de194d9)
- [FT8XX_LINE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d22204625ef070a6b8d16af7ad97578)
- [FT8XX_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gab0721051bb3f3cb9f555f696f36dfbbf)
- [FT8XX_VERTEX2F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga2648ab069991c02b2e8de62bf13913ab)
- [FT8XX_VERTEX2II](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga560836cd8c85599f24e5623a3e286b12)

<a id="header-details"></a>

---

[上一章](P008_zephyr__dt-bindings__mipi_dbi__mipi_dbi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__sys__kobject.h_文件参考.md)
