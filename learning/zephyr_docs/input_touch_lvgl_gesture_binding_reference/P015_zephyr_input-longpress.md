---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-15
title: zephyr_input-longpress
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-longpress.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第15章\_zephyr_input-longpress

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/zephyr,input-longpress.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-input-longpress"></a>
<a id="dtbinding-zephyr-input-longpress"></a>
<a id="std-dtcompatible-zephyr-input-longpress"></a>

兼容字符串（Compatible String）：`zephyr,input-longpress`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,input-longpress)。

<a id="description"></a>

输入长按伪设备（Input Longpress Pseudo-Device）。

监听按键输入事件，并生成对应短按和长按的按键输出事件。可以关联特定设备，仅监听该设备的事件。

后文保留完整输出原例：短按在一秒内松开后生成 `INPUT_KEY_A` 的按下与释放；长按持续超过一秒时生成 `INPUT_KEY_X` 按下，等待原按键松开后再生成其释放事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/input/input-event-codes.h>

longpress {
        input = <&buttons>;
        compatible = "zephyr,input-longpress";
        input-codes = <INPUT_KEY_0>, <INPUT_KEY_1>;
        short-codes = <INPUT_KEY_A>, <INPUT_KEY_B>;
        long-codes = <INPUT_KEY_X>, <INPUT_KEY_Y>;
        long-delay-ms = <1000>;
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 15.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `input` | `phandle` | 输入设备节点引用（Input Device Phandle）；未指定时监听所有设备的输入。 |
| `input-codes` | `array` | **必需**。输入事件按键码数组（Input Event Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `short-codes` | `array` | 可选的短按按键码数组（Short-Press Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `long-codes` | `array` | **必需**。长按时生成的按键码数组（Long-Press Key Code Array），使用 `INPUT_KEY_*` 或 `INPUT_BTN_*`。 |
| `long-delay-ms` | `int` | **必需**。判定为长按的时间延迟（Long-Press Delay），单位为毫秒。 |

本页没有已弃用的节点专用属性。

## 短按与长按输出原例

```text
# short press
input event: dev=buttons          SYN type= 1 code= 11 value=1 # INPUT_KEY_0 press
# release before one second
input event: dev=buttons          SYN type= 1 code= 11 value=0 # INPUT_KEY_0 release
input event: dev=longpress        SYN type= 1 code= 30 value=1 # INPUT_KEY_A press
input event: dev=longpress        SYN type= 1 code= 30 value=0 # INPUT_KEY_A release

# long press
input event: dev=buttons          SYN type= 1 code= 11 value=1 # INPUT_KEY_0 press
# hold for more than one second
input event: dev=longpress        SYN type= 1 code= 45 value=1 # INPUT_KEY_X press
# wait for release
input event: dev=buttons          SYN type= 1 code= 11 value=0 # INPUT_KEY_0 release
input event: dev=longpress        SYN type= 1 code= 45 value=0 # INPUT_KEY_X release
```

---

[上一章](P014_zephyr_input-double-tap.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P016_zephyr_input-sdl-touch.md)
