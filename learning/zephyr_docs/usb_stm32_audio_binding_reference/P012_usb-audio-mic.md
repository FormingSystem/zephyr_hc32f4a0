---
id: learning.zephyr-docs.usb-stm32-audio-binding-reference.page-12
title: usb-audio-mic
kind: reference
status: maintained
domains: [zephyr, devicetree, usb]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/usb-audio-mic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第12章\_usb-audio-mic

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/usb/usb-audio-mic.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="usb-audio-mic"></a>
<a id="dtbinding-usb-audio-mic"></a>
<a id="std-dtcompatible-usb-audio-mic"></a>

兼容字符串（Compatible String）：`usb-audio-mic`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=usb-audio-mic)。

<a id="description"></a>

USB音频麦克风（USB Audio Microphone）的专用字段。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 12.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `resolution` | `int` | 原文没有提供文字说明；默认值：`16`；合法值：`8, 16, 24, 32` |
| `sync-type` | `string` | IN设备的端点同步类型（Endpoint Synchronization Type），默认为同步（Synchronous）；不支持自适应（Adaptive）；默认值：`Synchronous`；合法值：`No Synchronization, Asynchronous, Adaptive, Synchronous` |
| `sample-rate-hz` | `int` | 原文没有提供文字说明；默认值：`48000` |
| `polling-interval` | `int` | 原文没有提供文字说明；默认值：`1` |
| `channel-l` | `boolean` | 使能l声道（Channel）；保留原文的声道缩写 |
| `channel-r` | `boolean` | 使能r声道（Channel）；保留原文的声道缩写 |
| `channel-c` | `boolean` | 使能c声道（Channel）；保留原文的声道缩写 |
| `channel-lfe` | `boolean` | 使能lfe声道（Channel）；保留原文的声道缩写 |
| `channel-ls` | `boolean` | 使能ls声道（Channel）；保留原文的声道缩写 |
| `channel-rs` | `boolean` | 使能rs声道（Channel）；保留原文的声道缩写 |
| `channel-lc` | `boolean` | 使能lc声道（Channel）；保留原文的声道缩写 |
| `channel-rc` | `boolean` | 使能rc声道（Channel）；保留原文的声道缩写 |
| `channel-s` | `boolean` | 使能s声道（Channel）；保留原文的声道缩写 |
| `channel-sl` | `boolean` | 使能sl声道（Channel）；保留原文的声道缩写 |
| `channel-sr` | `boolean` | 使能sr声道（Channel）；保留原文的声道缩写 |
| `channel-t` | `boolean` | 使能t声道（Channel）；保留原文的声道缩写 |
| `channel-cfg` | `boolean` | 使能cfg声道（Channel）；保留原文的声道缩写 |
| `feature-mute` | `boolean` | **必需**。使能静音（Mute）功能 |
| `feature-volume` | `boolean` | 使能音量（Volume）功能，当前不支持 |
| `feature-tone-control` | `boolean` | 使能音调控制（Tone Control），包括低音（Bass）、中音（Mid）和高音（Treble）；当前不支持 |
| `feature-graphic-equalizer` | `boolean` | 使能图形均衡器（Graphic Equalizer）功能，当前不支持 |
| `feature-automatic-gain-control` | `boolean` | 使能自动增益控制（Automatic Gain Control）功能，当前不支持 |
| `feature-delay` | `boolean` | 使能延迟（Delay）功能，当前不支持 |
| `feature-bass-boost` | `boolean` | 使能低音增强（Bass Boost）功能，当前不支持 |
| `feature-loudness` | `boolean` | 使能响度（Loudness）功能，当前不支持 |

本页没有已弃用的节点专用属性。

---

[上一章](P011_usb-audio-hs.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P013_usb-audio.md)
