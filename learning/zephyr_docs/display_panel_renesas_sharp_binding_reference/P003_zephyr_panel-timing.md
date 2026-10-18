---
id: learning.zephyr-docs.display-panel-renesas-sharp-binding-reference.page-3
title: zephyr_panel-timing
kind: reference
status: maintained
domains: [zephyr, devicetree, display]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/panel/zephyr,panel-timing.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第3章\_zephyr_panel-timing

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/panel/zephyr,panel-timing.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-panel-timing"></a>
<a id="dtbinding-zephyr-panel-timing"></a>
<a id="std-dtcompatible-zephyr-panel-timing"></a>

兼容字符串（Compatible String）：`zephyr,panel-timing`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,panel-timing)。

<a id="description"></a>

显示面板的通用时序（Timing）设置，可在面板的 `display-timings` 节点下添加。

<a id="examples"></a>

官方设备树配置原例：

```dts
&lcdif {
  display-timings {
    compatible = "zephyr,panel-timing";
    hsync-len = <8>;
    hfront-porch = <32>;
    hback-porch = <32>;
    vsync-len = <2>;
    vfront-porch = <16>;
    vback-porch = <14>;
    hsync-active = <0>;
    vsync-active = <0>;
    de-active = <1>;
    pixelclk-active = <0>;
    clock-frequency = <62346240>;
  };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 3.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `clock-frequency` | `int` | 显示控制器的像素时钟（Pixel Clock），单位为Hz。其频率至少应等于垂直总行数 `(height + vsync-len + vfront-porch + vback-porch)`、水平总像素数 `(width + hsync-len + hfront-porch + hback-porch)` 与期望帧率（Desired Frame Rate）的乘积；完整原式见后文。 |
| `hsync-len` | `int` | **必需**。控制器所驱动面板的水平同步脉冲宽度（Horizontal Synchronization Pulse Duration），单位为像素。 |
| `vsync-len` | `int` | **必需**。控制器所驱动面板的垂直同步脉冲宽度（Vertical Synchronization Pulse Duration），单位为行。 |
| `hback-porch` | `int` | **必需**。控制器所驱动面板的水平后肩（Horizontal Back Porch）长度，单位为像素。 |
| `vback-porch` | `int` | **必需**。控制器所驱动面板的垂直后肩（Vertical Back Porch）长度，单位为行。 |
| `hfront-porch` | `int` | **必需**。控制器所驱动面板的水平前肩（Horizontal Front Porch）长度，单位为像素。 |
| `vfront-porch` | `int` | **必需**。控制器所驱动面板的垂直前肩（Vertical Front Porch）长度，单位为行。 |
| `hsync-active` | `int` | **必需**。水平同步脉冲极性（Horizontal Sync Pulse Polarity）：0为低电平有效，1为高电平有效。；合法值：`0, 1` |
| `vsync-active` | `int` | **必需**。垂直同步脉冲极性（Vertical Sync Pulse Polarity）：0为低电平有效，1为高电平有效。；合法值：`0, 1` |
| `de-active` | `int` | **必需**。每个水平间隔发送的数据使能信号极性（Data Enable Polarity）：0为低电平有效，1为高电平有效。；合法值：`0, 1` |
| `pixelclk-active` | `int` | **必需**。像素时钟极性（Pixel Clock Polarity），选择向显示器驱动数据的边沿。0表示下降沿驱动像素数据、上升沿采样；1表示上升沿驱动像素数据、下降沿采样。；合法值：`0, 1` |
| `syncclk-active` | `int` | 同步信号的驱动／采样边沿（Sync Drive/Sample Edge）。未指定时采用 `pixelclk-active` 的设置。0表示在像素时钟下降沿驱动同步信号、上升沿采样；1表示上升沿驱动同步信号、下降沿采样。；合法值：`0, 1` |

本页没有已弃用的节点专用属性。

## 像素时钟下限原式

```text
(height + vsync-len + vfront-porch + vback-porch) *
(width + hsync-len + hfront-porch + hback-porch) *
desired frame rate
```

---

[上一章](P002_zephyr_panel-color-palette.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_philips_pcd8544.md)
