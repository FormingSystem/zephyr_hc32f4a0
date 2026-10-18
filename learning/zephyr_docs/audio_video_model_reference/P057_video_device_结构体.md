---
id: learning.zephyr-docs.audio-video-model-reference.page-57
title: video_device_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structvideo__device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_video\_device\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structvideo__device.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频设备封装类型（Wrapper Type）的存储类型。

```c
#include <zephyr/drivers/video.h>
```

<a id="details"></a>

视频设备包装类型的存储类型。这些对象连接成设备列表，用于沿子设备链传播控制操作。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a1146fe8e0691c82d3d88ef5692dc215e"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#a1146fe8e0691c82d3d88ef5692dc215e)。

此视频设备持有的设备。

<a id="r_a55e683c881dc4d71f765af87050e73ee"></a>

```c
const struct device * src_dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[src_dev](#a55e683c881dc4d71f765af87050e73ee)。

位于链路上游并提供数据的源设备（source device）。

<a id="r_acb7d3ba02fef218329a32e45466b11cb"></a>

```c
sys_dlist_t ctrls
```

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[ctrls](#acb7d3ba02fef218329a32e45466b11cb)。

此设备支持的视频控制项列表。

## 57.2\_详细说明（Detailed Documentation）

<a id="acb7d3ba02fef218329a32e45466b11cb"></a>

### `ctrls`

```c
sys_dlist_t video_device::ctrls
```

此设备支持的视频控制项列表。

<a id="a1146fe8e0691c82d3d88ef5692dc215e"></a>

### `dev`

```c
const struct device* video_device::dev
```

此视频设备持有的设备。

<a id="a55e683c881dc4d71f765af87050e73ee"></a>

### `src_dev`

```c
const struct device* video_device::src_dev
```

位于链路上游并提供数据的源设备（source device）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/video.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/drivers/video.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2video_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_video_ctrl_range_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_video_driver_api_结构体.md)
