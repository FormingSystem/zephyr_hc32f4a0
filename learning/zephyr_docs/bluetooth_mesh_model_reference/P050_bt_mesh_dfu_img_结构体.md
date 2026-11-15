---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-50
title: bt_mesh_dfu_img_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__img.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_bt\_mesh\_dfu\_img\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__img.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备固件更新（DFU）的映像实例。

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="details"></a>

设备固件更新镜像实例（DFU image instance）。每个 DFU 镜像代表一个可更新的固件镜像（Firmware image）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_aa4d91e47dd4c20939d8ef8ada0b86f83"></a>

```c
const void * fwid
```

相关声明：[fwid](#aa4d91e47dd4c20939d8ef8ada0b86f83)。

固件标识符（Firmware ID）。

<a id="r_a97e17c59a0528462d554d6bbe78858da"></a>

```c
size_t fwid_len
```

相关声明：[fwid_len](#a97e17c59a0528462d554d6bbe78858da)。

固件标识符长度（Firmware ID length）。

<a id="r_a578b2932efb07a3e4eb80043902cc7a0"></a>

```c
const char * uri
```

相关声明：[uri](#a578b2932efb07a3e4eb80043902cc7a0)。

更新统一资源标识符（Update URI），或 `NULL`。

## 50.2\_详细说明（Detailed Documentation）

<a id="aa4d91e47dd4c20939d8ef8ada0b86f83"></a>

### `fwid`

```c
const void* bt_mesh_dfu_img::fwid
```

固件标识符（Firmware ID）。

<a id="a97e17c59a0528462d554d6bbe78858da"></a>

### `fwid_len`

```c
size_t bt_mesh_dfu_img::fwid_len
```

固件标识符长度（Firmware ID length）。

<a id="a578b2932efb07a3e4eb80043902cc7a0"></a>

### `uri`

```c
const char* bt_mesh_dfu_img::uri
```

更新统一资源标识符（Update URI），或 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_bt_mesh_dfu_metadata_结构体.md)
