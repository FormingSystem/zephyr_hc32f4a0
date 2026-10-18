---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-20
title: zephyr_lvgl-pointer-input
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-pointer-input.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第20章\_zephyr_lvgl-pointer-input

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-pointer-input.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-lvgl-pointer-input"></a>
<a id="dtbinding-zephyr-lvgl-pointer-input"></a>
<a id="std-dtcompatible-zephyr-lvgl-pointer-input"></a>

兼容字符串（Compatible String）：`zephyr,lvgl-pointer-input`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,lvgl-pointer-input)。

<a id="description"></a>

LVGL指针输入设备伪设备（Pointer Indev Pseudo-Device）。

监听触摸输入事件，并将 `lv_indev_data_t` 路由至LVGL管理的底层指针类型 `lv_indev_t`。必须关联特定设备，以监听该设备的事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
pointer {
        compatible = "zephyr,lvgl-pointer-input";
        input = <&input_sdl_touch>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 20.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）。 |
| `display` | `phandle` | 接收输入命令的显示设备节点引用（Display Device Phandle），用于多显示器配置。 |

### 已弃用的节点专用属性（Deprecated Properties）

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `swap-xy` | `boolean` | 交换X／Y轴（Swap X-Y Axes），使输入与显示对齐。已弃用：改用底层输入设备的 `swapped-x-y` 属性。 |
| `invert-x` | `boolean` | 反转X轴（Invert X Axis），使输入与显示对齐。已弃用：改用底层输入设备的 `inverted-x` 属性。 |
| `invert-y` | `boolean` | 反转Y轴（Invert Y Axis），使输入与显示对齐。已弃用：改用底层输入设备的 `inverted-y` 属性。 |

---

[上一章](P019_zephyr_lvgl-keypad-input.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P021_zephyr_native-linux-evdev.md)
