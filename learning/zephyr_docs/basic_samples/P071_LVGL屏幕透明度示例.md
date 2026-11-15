---
id: learning.zephyr-docs.basic_samples.page-71
title: LVGL屏幕透明度示例
kind: reference
status: maintained
domains: [zephyr, basic_samples, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/modules/lvgl/screen_transparency/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="lvgl-screen-transparency"></a>

# 第71章\_LVGL屏幕透明度示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/modules/lvgl/screen_transparency/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 71.1 概述（Overview）

本示例演示如何使用LVGL向支持透明度（Transparency）的屏幕渲染，例如屏幕显示叠加层（On-screen display overlay，OSD overlay）。

<a id="requirements"></a>

## 71.2 要求（Requirements）

一块带显示器、且显示器支持ARGB8888颜色格式的开发板。

<a id="building-and-running"></a>
<a id="lvgl-screen-transparency-building-and-running"></a>

## 71.3 构建与运行（Building and Running）

可按以下方式构建并运行演示：

```sh
west build -b native_sim samples/modules/lvgl/screen_transparency
west build -t run
```

<a id="see-also"></a>

## 71.4 另请参阅（See also）

[显示接口（Display）](../hardware/P214_显示公共接口.md)。


对应官方文档源码：[samples/modules/lvgl/screen_transparency/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/modules/lvgl/screen_transparency/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/modules/lvgl/screen_transparency/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/modules/lvgl/screen_transparency/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P070_LVGL多显示器示例.md) · [返回大纲](大纲.md) · [下一章](P072_TensorFlowLiteMicro示例目录.md)
