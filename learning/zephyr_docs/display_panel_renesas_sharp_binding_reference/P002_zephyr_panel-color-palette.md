---
id: learning.zephyr-docs.display-panel-renesas-sharp-binding-reference.page-2
title: zephyr_panel-color-palette
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/panel/zephyr,panel-color-palette.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_zephyr_panel-color-palette

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/panel/zephyr,panel-color-palette.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-panel-color-palette"></a>
<a id="dtbinding-zephyr-panel-color-palette"></a>
<a id="std-dtcompatible-zephyr-panel-color-palette"></a>

兼容字符串（Compatible String）：`zephyr,panel-color-palette`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,panel-color-palette)。

<a id="description"></a>

显示面板的通用调色板（Color Palette）设置。

<a id="examples"></a>

官方设备树配置原例：

```dts
color-palette {
  compatible = "zephyr,panel-color-palette";
  colors = <ARGB8888(255, 0, 0, 255)   /* red */
            ARGB8888(0, 255, 0, 128)   /* green, 50% alpha */
            PANEL_COLOR_PALETTE_NULL   /* Empty entry */
            ARGB8888(0, 0, 255, 255)>; /* blue */
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `colors` | `array` | 32位ARGB8888颜色列表（Color List）。每个值对应 `ARGB8888(r, g, b, a)`，其中Alpha分量A位于最高有效字节（Most Significant Byte）。 |

本页没有已弃用的节点专用属性。

---

[上一章](P001_orisetech_otm8009a.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_zephyr_panel-timing.md)
