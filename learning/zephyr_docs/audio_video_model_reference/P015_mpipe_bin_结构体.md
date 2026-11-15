---
id: learning.zephyr-docs.audio-video-model-reference.page-15
title: mpipe_bin_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__bin.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_mpipe\_bin\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmpipe__bin.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

容器（Bin）结构。

```c
#include <zephyr/mpipe/mpipe_bin.h>
```

<a id="details"></a>

容器（Bin）结构体。容器元素可包含多个子元素，负责管理子元素的状态变化，并处理其中管线元素的拓扑关系。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_aecf25e2b5010acc8754dc7ae9bd4c222"></a>

```c
struct mpipe_element element
```

相关声明：[mpipe_element](P021_mpipe_element_结构体.md)、[element](#aecf25e2b5010acc8754dc7ae9bd4c222)。

基础元素（base element）结构体。

<a id="r_a40ceee13946c8b9e408cc53e9ecfed09"></a>

```c
int children_num
```

相关声明：[children_num](#a40ceee13946c8b9e408cc53e9ecfed09)。

容器中的子元素数量。

<a id="r_a165735c1d573616e990b8bf707a2567f"></a>

```c
sys_dlist_t children
```

相关声明：[sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)、[children](#a165735c1d573616e990b8bf707a2567f)。

容器中的子元素列表。

<a id="r_a60d49bd3793ea05e14f7c6d959a182d7"></a>

```c
struct zbus_runtime_channel bus
```

相关声明：[zbus_runtime_channel](../intercore_reference/P210_zbus运行时通道结构.md)、[bus](#a60d49bd3793ea05e14f7c6d959a182d7)。

容器的消息总线（message bus）：一个将子元素的消息（Messages）事件传递给应用的 zbus 通道，可通过 `mpipe_element_get_bus_chan` 获取。

## 15.2\_详细说明（Detailed Documentation）

<a id="a60d49bd3793ea05e14f7c6d959a182d7"></a>

### `bus`

```c
struct zbus_runtime_channel mpipe_bin::bus
```

容器的消息总线（message bus）：一个将子元素的消息（Messages）事件传递给应用的 zbus 通道，可通过 `mpipe_element_get_bus_chan` 获取。

参见消息（Messages）。

<a id="a165735c1d573616e990b8bf707a2567f"></a>

### `children`

```c
sys_dlist_t mpipe_bin::children
```

容器中的子元素列表。

<a id="a40ceee13946c8b9e408cc53e9ecfed09"></a>

### `children_num`

```c
int mpipe_bin::children_num
```

容器中的子元素数量。

<a id="aecf25e2b5010acc8754dc7ae9bd4c222"></a>

### `element`

```c
struct mpipe_element mpipe_bin::element
```

基础元素（base element）结构体。

本数据类型文档由以下文件生成：

- `zephyr/mpipe/mpipe_bin.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_bin.h](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__bin_8h_source.html)
- [mpipe_element](P021_mpipe_element_结构体.md)
- [sys_dlist_t](../dlist_reference/P001_双向链表公共接口.md#gaa03f9557215b486fee1039dd4c07e683)
- [zbus_runtime_channel](../intercore_reference/P210_zbus运行时通道结构.md)
- [Messages](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__message.html)
- [mpipe_element_get_bus_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__element.html#gadd1c172f5ce2f4eb6fffeb40ecc931b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_mpipe_app_src_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_mpipe_buffer_meta_结构体.md)
