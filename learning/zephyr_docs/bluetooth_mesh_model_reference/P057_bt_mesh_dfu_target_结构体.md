---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-57
title: bt_mesh_dfu_target_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__target.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_bt\_mesh\_dfu\_target\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__target.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备固件更新（DFU）的目标节点。

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

设备固件更新（DFU）的目标节点。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 57.1\_数据成员（Data Fields）

<a id="r_a96393388212d4bffd8fb00c82e58d364"></a>

```c
struct bt_mesh_blob_target blob
```

相关声明：[bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)、[blob](#a96393388212d4bffd8fb00c82e58d364)。

二进制大对象目标节点（BLOB Target node）。

<a id="r_a986a58915c0b0ab509ddbbbe475976d2"></a>

```c
uint8_t img_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[img_idx](#a986a58915c0b0ab509ddbbbe475976d2)。

目标节点上的镜像索引（Image index）。

<a id="r_a3d18d0ae1d0902cf84402b090a9aaa99"></a>

```c
uint8_t effect
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[effect](#a3d18d0ae1d0902cf84402b090a9aaa99)。

预期的设备固件更新影响（DFU effect），参见 `bt_mesh_dfu_effect`。

<a id="r_a4ad51f9dc3fdb39afeef55e4cd22b968"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a4ad51f9dc3fdb39afeef55e4cd22b968)。

当前设备固件更新状态（DFU status），参见 `bt_mesh_dfu_status`。

<a id="r_a43730ff708da06fe31e801adf7a79c0e"></a>

```c
uint8_t phase
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phase](#a43730ff708da06fe31e801adf7a79c0e)。

当前设备固件更新阶段（DFU phase），参见 `bt_mesh_dfu_phase`。

## 57.2\_详细说明（Detailed Documentation）

<a id="a96393388212d4bffd8fb00c82e58d364"></a>

### `blob`

```c
struct bt_mesh_blob_target bt_mesh_dfu_target::blob
```

二进制大对象目标节点（BLOB Target node）。

<a id="a3d18d0ae1d0902cf84402b090a9aaa99"></a>

### `effect`

```c
uint8_t bt_mesh_dfu_target::effect
```

预期的设备固件更新影响（DFU effect），参见 `bt_mesh_dfu_effect`。

<a id="a986a58915c0b0ab509ddbbbe475976d2"></a>

### `img_idx`

```c
uint8_t bt_mesh_dfu_target::img_idx
```

目标节点上的镜像索引（Image index）。

<a id="a43730ff708da06fe31e801adf7a79c0e"></a>

### `phase`

```c
uint8_t bt_mesh_dfu_target::phase
```

当前设备固件更新阶段（DFU phase），参见 `bt_mesh_dfu_phase`。

<a id="a4ad51f9dc3fdb39afeef55e4cd22b968"></a>

### `status`

```c
uint8_t bt_mesh_dfu_target::status
```

当前设备固件更新状态（DFU status），参见 `bt_mesh_dfu_status`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 57.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P056_bt_mesh_dfu_srv_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P058_bt_mesh_dfu_target_status_结构体.md)
