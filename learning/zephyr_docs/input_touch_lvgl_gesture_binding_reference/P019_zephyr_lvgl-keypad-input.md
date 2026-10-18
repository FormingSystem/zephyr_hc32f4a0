---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-19
title: zephyr_lvgl-keypad-input
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-keypad-input.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第19章\_zephyr_lvgl-keypad-input

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-keypad-input.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-lvgl-keypad-input"></a>
<a id="dtbinding-zephyr-lvgl-keypad-input"></a>
<a id="std-dtcompatible-zephyr-lvgl-keypad-input"></a>

兼容字符串（Compatible String）：`zephyr,lvgl-keypad-input`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,lvgl-keypad-input)。

<a id="description"></a>

LVGL键盘输入设备伪设备（Keypad Indev Pseudo-Device）。

监听输入事件，并将 `lv_indev_data_t` 路由至LVGL管理的底层键盘类型 `lv_indev_t`。

`input-codes` 属性可用于建立输入码到LVGL按键的映射；部分LVGL按键具有特殊功能，见[LVGL按键说明](https://lvgl.io/docs/open/main-modules/indev/keypad#keys)。该伪设备可关联特定设备，仅监听该设备的事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/lvgl/lvgl.h>

keypad {
        compatible = "zephyr,lvgl-keypad-input";
        input = <&buttons>;
        input-codes = <INPUT_KEY_1 INPUT_KEY_2>;
        lvgl-codes = <LV_KEY_NEXT LV_KEY_PREV>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 19.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input-codes` | `array` | **必需**。输入事件按键码数组（Input Event Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `lvgl-codes` | `array` | **必需**。映射后的LVGL按键数组（LVGL Key Array）。 |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）。 |
| `display` | `phandle` | 接收输入命令的显示设备节点引用（Display Device Phandle），用于多显示器配置。 |

本页没有已弃用的节点专用属性。

---

[上一章](P018_zephyr_lvgl-encoder-input.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P020_zephyr_lvgl-pointer-input.md)
