---
id: learning.zephyr-docs.api-source-reference.page-642
title: panel.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/panel_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第642章\_panel.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html)。

## 642.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>

```c
/*
 * Copyright 2023-2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_DISPLAY_PANEL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_DISPLAY_PANEL_H_


#define PANEL_PIXEL_FORMAT_RGB_888   (0x1 << 0)
#define PANEL_PIXEL_FORMAT_MONO01    (0x1 << 1)
#define PANEL_PIXEL_FORMAT_MONO10    (0x1 << 2)
#define PANEL_PIXEL_FORMAT_ARGB_8888 (0x1 << 3)
#define PANEL_PIXEL_FORMAT_RGB_565   (0x1 << 4)
#define PANEL_PIXEL_FORMAT_RGB_565X  (0x1 << 5)
#define PANEL_PIXEL_FORMAT_L_8       (0x1 << 6)
#define PANEL_PIXEL_FORMAT_AL_88     (0x1 << 7)
#define PANEL_PIXEL_FORMAT_XRGB_8888 (0x1 << 8)
#define PANEL_PIXEL_FORMAT_BGR_888   (0x1 << 9)
#define PANEL_PIXEL_FORMAT_ABGR_8888 (0x1 << 10)
#define PANEL_PIXEL_FORMAT_RGBA_8888 (0x1 << 11)
#define PANEL_PIXEL_FORMAT_BGRA_8888 (0x1 << 12)
#define PANEL_PIXEL_FORMAT_I_4       (0x1 << 13)
#define PANEL_PIXEL_FORMAT_L_4       (0x1 << 14)
#define PANEL_PIXEL_FORMAT_YUYV      (0x1 << 15)

#define ARGB8888(r, g, b, a) (((b) << 0) | ((g) << 8) | ((r) << 16) | ((a) << 24))

#define PANEL_COLOR_PALETTE_NULL 0


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_DISPLAY_PANEL_H_ */
```

## 642.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023-2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_DISPLAY_PANEL_H_`。

## 642.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html)

---

[上一章](P641_pacs.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P643_pat9136.h_源码浏览.md)
