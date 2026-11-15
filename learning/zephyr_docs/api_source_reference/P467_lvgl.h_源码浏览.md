---
id: learning.zephyr-docs.api-source-reference.page-467
title: lvgl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第467章\_lvgl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html)。

## 467.1\_原始可见代码（Source Code）

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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>

```c
/*
 * Copyright (c) 2023 Fabian Blatz <fabianblatz@gmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_LVGL_LVGL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_LVGL_LVGL_H_


#define LV_KEY_UP        17
#define LV_KEY_DOWN      18
#define LV_KEY_RIGHT     19
#define LV_KEY_LEFT      20
#define LV_KEY_ESC       27
#define LV_KEY_DEL       127
#define LV_KEY_BACKSPACE 8
#define LV_KEY_ENTER     10
#define LV_KEY_NEXT      9
#define LV_KEY_PREV      11
#define LV_KEY_HOME      2
#define LV_KEY_END       3


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_LVGL_LVGL_H_ */
```

## 467.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Fabian Blatz <fabianblatz@gmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 57 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_LVGL_LVGL_H_`。

## 467.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html)

---

[上一章](P466_ltc4286.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P468_lwm2m_send_scheduler.h_源码浏览.md)
