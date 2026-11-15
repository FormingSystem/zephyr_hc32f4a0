---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-51
title: bt_mesh_dfu_metadata_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_bt\_mesh\_dfu\_metadata\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件元数据（Firmware Metadata）。

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

<a id="details"></a>

固件元数据（Firmware Metadata）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_a48a680b1c3a802e15d4212865fa1d0df"></a>

```c
struct bt_mesh_dfu_metadata_fw_ver fw_ver
```

相关声明：[bt_mesh_dfu_metadata_fw_ver](P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)、[fw_ver](#a48a680b1c3a802e15d4212865fa1d0df)。

新固件版本（New firmware version）。

<a id="r_a624e2e30f31d2d2f2554eb22c6950ebc"></a>

```c
uint32_t fw_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[fw_size](#a624e2e30f31d2d2f2554eb22c6950ebc)。

新固件大小（New firmware size）。

<a id="r_a82719aefc21e1fac5a6e8813af23e131"></a>

```c
enum bt_mesh_dfu_metadata_fw_core_type fw_core_type
```

相关声明：[bt_mesh_dfu_metadata_fw_core_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gaec5fa6e61a6ae88ac7a14f1ec09585b8)、[fw_core_type](#a82719aefc21e1fac5a6e8813af23e131)。

新固件核心类型（New firmware core type）。

<a id="r_af4d02eeccb2537b81738ffd186c7d9ed"></a>

```c
uint32_t comp_hash
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[comp_hash](#af4d02eeccb2537b81738ffd186c7d9ed)。

传入组成数据的哈希值（Hash of incoming Composition Data）。

<a id="r_ac487e125632b55b8477f648759dbbba0"></a>

```c
uint16_t elems
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[elems](#ac487e125632b55b8477f648759dbbba0)。

更新后的节点元素数量（New number of node elements）。

<a id="r_ac3e6dd2b069785ae359d49162d33e104"></a>

```c
uint8_t * user_data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[user_data](#ac3e6dd2b069785ae359d49162d33e104)。

新固件的应用专用数据（Application-specific data）。

<a id="r_ae4853b55fda6ec8c4c8609d5648890ab"></a>

```c
uint32_t user_data_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[user_data_len](#ae4853b55fda6ec8c4c8609d5648890ab)。

应用专用字段长度（Application-specific field length）。

## 51.2\_详细说明（Detailed Documentation）

<a id="af4d02eeccb2537b81738ffd186c7d9ed"></a>

### `comp_hash`

```c
uint32_t bt_mesh_dfu_metadata::comp_hash
```

传入组成数据的哈希值（Hash of incoming Composition Data）。

<a id="ac487e125632b55b8477f648759dbbba0"></a>

### `elems`

```c
uint16_t bt_mesh_dfu_metadata::elems
```

更新后的节点元素数量（New number of node elements）。

<a id="a82719aefc21e1fac5a6e8813af23e131"></a>

### `fw_core_type`

```c
enum bt_mesh_dfu_metadata_fw_core_type bt_mesh_dfu_metadata::fw_core_type
```

新固件核心类型（New firmware core type）。

<a id="a624e2e30f31d2d2f2554eb22c6950ebc"></a>

### `fw_size`

```c
uint32_t bt_mesh_dfu_metadata::fw_size
```

新固件大小（New firmware size）。

<a id="a48a680b1c3a802e15d4212865fa1d0df"></a>

### `fw_ver`

```c
struct bt_mesh_dfu_metadata_fw_ver bt_mesh_dfu_metadata::fw_ver
```

新固件版本（New firmware version）。

<a id="ac3e6dd2b069785ae359d49162d33e104"></a>

### `user_data`

```c
uint8_t* bt_mesh_dfu_metadata::user_data
```

新固件的应用专用数据（Application-specific data）。

此字段为可选（Optional）。

<a id="ae4853b55fda6ec8c4c8609d5648890ab"></a>

### `user_data_len`

```c
uint32_t bt_mesh_dfu_metadata::user_data_len
```

应用专用字段长度（Application-specific field length）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_metadata.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_metadata.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h_source.html)
- [bt_mesh_dfu_metadata_fw_ver](P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_dfu_metadata_fw_core_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gaec5fa6e61a6ae88ac7a14f1ec09585b8)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_bt_mesh_dfu_img_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)
