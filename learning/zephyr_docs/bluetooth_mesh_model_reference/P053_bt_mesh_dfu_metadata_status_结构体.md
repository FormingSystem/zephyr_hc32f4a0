---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-53
title: bt_mesh_dfu_metadata_status_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_bt\_mesh\_dfu\_metadata\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__metadata__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元数据状态（Metadata Status）的响应。

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

元数据状态（Metadata Status）的响应。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a1d41b76b66acadc20f7f9ec1f4bc8b9b"></a>

```c
uint8_t idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[idx](#a1d41b76b66acadc20f7f9ec1f4bc8b9b)。

镜像索引（Image index）。

<a id="r_ae7ad71649f295142e48863b6d884b966"></a>

```c
enum bt_mesh_dfu_status status
```

相关声明：[bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)、[status](#ae7ad71649f295142e48863b6d884b966)。

状态码（Status code）。

<a id="r_a299723f7176938b2900cfdae4550965c"></a>

```c
enum bt_mesh_dfu_effect effect
```

相关声明：[bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)、[effect](#a299723f7176938b2900cfdae4550965c)。

传输影响（Effect of transfer）。

## 53.2\_详细说明（Detailed Documentation）

<a id="a299723f7176938b2900cfdae4550965c"></a>

### `effect`

```c
enum bt_mesh_dfu_effect bt_mesh_dfu_metadata_status::effect
```

传输影响（Effect of transfer）。

<a id="a1d41b76b66acadc20f7f9ec1f4bc8b9b"></a>

### `idx`

```c
uint8_t bt_mesh_dfu_metadata_status::idx
```

镜像索引（Image index）。

<a id="ae7ad71649f295142e48863b6d884b966"></a>

### `status`

```c
enum bt_mesh_dfu_status bt_mesh_dfu_metadata_status::status
```

状态码（Status code）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_bt_mesh_dfu_metadata_fw_ver_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_bt_mesh_dfu_slot_结构体.md)
