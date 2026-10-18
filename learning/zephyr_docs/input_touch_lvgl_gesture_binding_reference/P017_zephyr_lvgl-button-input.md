---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-17
title: zephyr_lvgl-button-input
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-button-input.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第17章\_zephyr_lvgl-button-input

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-button-input.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-lvgl-button-input"></a>
<a id="dtbinding-zephyr-lvgl-button-input"></a>
<a id="std-dtcompatible-zephyr-lvgl-button-input"></a>

兼容字符串（Compatible String）：`zephyr,lvgl-button-input`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,lvgl-button-input)。

<a id="description"></a>

LVGL按钮输入设备伪设备（Button Indev Pseudo-Device）。

监听按钮输入事件，并将 `lv_indev_data_t` 路由至LVGL管理的底层按钮类型 `lv_indev_t`。

在原例中，设备收到代码为 `INPUT_KEY_0` 的 `input_event` 时，会在坐标 `(120,220)` 执行点击事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
pointer {
        compatible = "zephyr,lvgl-button-input";
        input = <&buttons>;
        input-codes = <INPUT_KEY_0 INPUT_KEY_1>;
        coordinates = <120 220>, <150 250>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 17.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input-codes` | `array` | **必需**。输入事件按键码数组（Input Event Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `coordinates` | `array` | 各输入码映射到的坐标点 `(x,y)` 数组（Coordinate Array）。 |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）。 |
| `display` | `phandle` | 接收输入命令的显示设备节点引用（Display Device Phandle），用于多显示器配置。 |

本页没有已弃用的节点专用属性。

---

[上一章](P016_zephyr_input-sdl-touch.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P018_zephyr_lvgl-encoder-input.md)
