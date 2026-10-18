---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-18
title: zephyr_lvgl-encoder-input
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-encoder-input.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第18章\_zephyr_lvgl-encoder-input

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,lvgl-encoder-input.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-lvgl-encoder-input"></a>
<a id="dtbinding-zephyr-lvgl-encoder-input"></a>
<a id="std-dtcompatible-zephyr-lvgl-encoder-input"></a>

兼容字符串（Compatible String）：`zephyr,lvgl-encoder-input`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,lvgl-encoder-input)。

<a id="description"></a>

LVGL编码器输入设备伪设备（Encoder Indev Pseudo-Device）。

监听按钮／编码器输入事件，并将 `lv_indev_data_t` 路由至LVGL管理的底层编码器类型 `lv_indev_t`。

<a id="examples"></a>

官方设备树配置原例：

```dts
encoder {
        compatible = "zephyr,lvgl-encoder-input";
        rotation-input-code = <INPUT_REL_Y>;
        button-input-code = <INPUT_KEY_0>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 18.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `rotation-input-code` | `int` | **必需**。旋转对应的输入事件码（Rotation Input Event Code），使用 `INPUT_REL_*`。 |
| `button-input-code` | `int` | 编码器按钮的输入事件按键码（Encoder Button Key Code），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）。 |
| `display` | `phandle` | 接收输入命令的显示设备节点引用（Display Device Phandle），用于多显示器配置。 |

本页没有已弃用的节点专用属性。

---

[上一章](P017_zephyr_lvgl-button-input.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P019_zephyr_lvgl-keypad-input.md)
