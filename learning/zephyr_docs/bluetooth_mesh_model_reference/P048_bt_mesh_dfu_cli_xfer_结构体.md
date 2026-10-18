---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-48
title: bt_mesh_dfu_cli_xfer_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__xfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_bt\_mesh\_dfu\_cli\_xfer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__xfer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新客户端（Firmware Update Client）的传输参数：

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

固件更新客户端（Firmware Update Client）的传输参数：

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 48.1\_数据成员（Data Fields）

<a id="r_adece8c0e0cec2262a7066b27636fc46e"></a>

```c
uint64_t blob_id
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[blob_id](#adece8c0e0cec2262a7066b27636fc46e)。

本次传输使用的二进制大对象标识符（BLOB ID）；设为 `0` 时随机生成。

<a id="r_a3c25a54eb4e557d749a9fb1ba66aecb4"></a>

```c
const struct bt_mesh_dfu_slot * slot
```

相关声明：[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)、[slot](#a3c25a54eb4e557d749a9fb1ba66aecb4)。

要传输的设备固件更新镜像槽位（DFU image slot）。

<a id="r_a6608f683fd94e12f7c3ef5f3de7ec248"></a>

```c
enum bt_mesh_blob_xfer_mode mode
```

相关声明：[bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)、[mode](#a6608f683fd94e12f7c3ef5f3de7ec248)。

传输模式（Transfer mode）：推送模式（Push BLOB Transfer Mode）或拉取模式（Pull BLOB Transfer Mode）。

<a id="r_a2c4feacc090dace0986e533257f9b291"></a>

```c
const struct bt_mesh_dfu_cli_xfer_blob_params * blob_params
```

相关声明：[bt_mesh_dfu_cli_xfer_blob_params](P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)、[blob_params](#a2c4feacc090dace0986e533257f9b291)。

传输使用的二进制大对象参数（BLOB parameters）；设为 `NULL` 时，在发送固件前获取目标节点的能力（Capabilities）。

## 48.2\_详细说明（Detailed Documentation）

<a id="adece8c0e0cec2262a7066b27636fc46e"></a>

### `blob_id`

```c
uint64_t bt_mesh_dfu_cli_xfer::blob_id
```

本次传输使用的二进制大对象标识符（BLOB ID）；设为 `0` 时随机生成。

<a id="a2c4feacc090dace0986e533257f9b291"></a>

### `blob_params`

```c
const struct bt_mesh_dfu_cli_xfer_blob_params* bt_mesh_dfu_cli_xfer::blob_params
```

传输使用的二进制大对象参数（BLOB parameters）；设为 `NULL` 时，在发送固件前获取目标节点的能力（Capabilities）。

<a id="a6608f683fd94e12f7c3ef5f3de7ec248"></a>

### `mode`

```c
enum bt_mesh_blob_xfer_mode bt_mesh_dfu_cli_xfer::mode
```

传输模式（Transfer mode）：推送模式（Push BLOB Transfer Mode）或拉取模式（Pull BLOB Transfer Mode）。

<a id="a3c25a54eb4e557d749a9fb1ba66aecb4"></a>

### `slot`

```c
const struct bt_mesh_dfu_slot* bt_mesh_dfu_cli_xfer::slot
```

要传输的设备固件更新镜像槽位（DFU image slot）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 48.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [bt_mesh_dfu_cli_xfer_blob_params](P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P047_bt_mesh_dfu_cli_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P049_bt_mesh_dfu_cli_xfer_blob_params_结构体.md)
