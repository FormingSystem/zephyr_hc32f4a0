---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-54
title: bt_mesh_dfu_slot_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__slot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_bt\_mesh\_dfu\_slot\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__slot.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备固件更新（DFU）分发使用的映像槽位。

```c
#include <zephyr/bluetooth/mesh/dfu.h>
```

<a id="details"></a>

设备固件更新（DFU）分发使用的映像槽位。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a3f6258793af506b639dd384562fc4a20"></a>

```c
size_t size
```

相关声明：[size](#a3f6258793af506b639dd384562fc4a20)。

固件大小（Firmware size），单位为字节。

<a id="r_a47ab534d52e931155dfc7cf4e2444999"></a>

```c
size_t fwid_len
```

相关声明：[fwid_len](#a47ab534d52e931155dfc7cf4e2444999)。

固件标识符长度（Firmware ID length）。

<a id="r_af3e056bf835365afda82f3ec8342d926"></a>

```c
size_t metadata_len
```

相关声明：[metadata_len](#af3e056bf835365afda82f3ec8342d926)。

元数据长度。

<a id="r_a9ab5db428c7d57803d6bbc5f26f9c7bb"></a>

```c
uint8_t fwid [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[fwid](#a9ab5db428c7d57803d6bbc5f26f9c7bb)。

固件标识符（Firmware ID）。

<a id="r_aa554bde6cdffa419ada8ea7410118947"></a>

```c
uint8_t metadata [0]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[metadata](#aa554bde6cdffa419ada8ea7410118947)。

元数据（Metadata）。

## 54.2\_详细说明（Detailed Documentation）

<a id="a9ab5db428c7d57803d6bbc5f26f9c7bb"></a>

### `fwid`

```c
uint8_t bt_mesh_dfu_slot::fwid[0]
```

固件标识符（Firmware ID）。

<a id="a47ab534d52e931155dfc7cf4e2444999"></a>

### `fwid_len`

```c
size_t bt_mesh_dfu_slot::fwid_len
```

固件标识符长度（Firmware ID length）。

<a id="aa554bde6cdffa419ada8ea7410118947"></a>

### `metadata`

```c
uint8_t bt_mesh_dfu_slot::metadata[0]
```

元数据（Metadata）。

<a id="af3e056bf835365afda82f3ec8342d926"></a>

### `metadata_len`

```c
size_t bt_mesh_dfu_slot::metadata_len
```

元数据长度。

<a id="a3f6258793af506b639dd384562fc4a20"></a>

### `size`

```c
size_t bt_mesh_dfu_slot::size
```

固件大小（Firmware size），单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_bt_mesh_dfu_metadata_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_bt_mesh_dfu_srv_结构体.md)
