---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-14
title: zephyr_input-double-tap
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-double-tap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第14章\_zephyr_input-double-tap

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-double-tap.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-input-double-tap"></a>
<a id="dtbinding-zephyr-input-double-tap"></a>
<a id="std-dtcompatible-zephyr-input-double-tap"></a>

兼容字符串（Compatible String）：`zephyr,input-double-tap`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,input-double-tap)。

<a id="description"></a>

输入双击伪设备（Input Double-Tap Pseudo-Device）。

监听按键输入事件，生成对应的双击事件，并可选生成单击事件。可以关联特定设备，仅监听该设备的事件。

只有在双击延迟到期仍未发生第二次按下、且期间按键已松开时，才上报单击；持续按住按键不会生成单击事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/input/input-event-codes.h>

double_tap {
        input = <&buttons>;
        compatible = "zephyr,input-double-tap";
        input-codes = <INPUT_KEY_0>, <INPUT_KEY_1>;
        single-tap-codes = <INPUT_KEY_X>, <INPUT_KEY_Y>;
        double-tap-codes = <INPUT_KEY_A>, <INPUT_KEY_B>;
        double-tap-delay-ms = <300>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 14.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）；未指定时监听所有设备的输入。 |
| `input-codes` | `array` | **必需**。输入事件按键码数组（Input Event Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `single-tap-codes` | `array` | 单击时生成的按键码数组（Single-Tap Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `double-tap-codes` | `array` | **必需**。双击时生成的按键码数组（Double-Tap Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `double-tap-delay-ms` | `int` | **必需**。判定为双击所允许的两次点击之间的最大时间间隔（Double-Tap Delay），单位为毫秒。 |

本页没有已弃用的节点专用属性。

---

[上一章](P013_xptek_xpt2046.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P015_zephyr_input-longpress.md)
