---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-9
title: bt_mesh_blob_srv_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_bt\_mesh\_blob\_srv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输服务器（BLOB Transfer Server）的模型实例。

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

<a id="details"></a>

BLOB传输服务器（BLOB Transfer Server）的模型实例。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Fsrv_5Fstate"></a>

```c
struct bt_mesh_blob_srv_state
```

相关声明：[bt_mesh_blob_srv_state](P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.2\_数据成员（Data Fields）

<a id="r_a65d08187dce1ed86cbfbb4f977cd32df"></a>

```c
const struct bt_mesh_blob_srv_cb * cb
```

相关声明：[bt_mesh_blob_srv_cb](P011_bt_mesh_blob_srv_cb_结构体.md)、[cb](#a65d08187dce1ed86cbfbb4f977cd32df)。

事件处理回调（Event handler callbacks）。

<a id="r_a23d12a803a2414aa1460ea9a862cc78b"></a>

```c
const struct bt_mesh_blob_io * io
```

相关声明：[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[io](#a23d12a803a2414aa1460ea9a862cc78b)。

<a id="r_a82a5c7fc2ad37e531ec10bada27bf10a"></a>

```c
struct k_work_delayable rx_timeout
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[rx_timeout](#a82a5c7fc2ad37e531ec10bada27bf10a)。

<a id="r_a8d6a01849e95c4a26d3270f4320c214f"></a>

```c
struct bt_mesh_blob_block block
```

相关声明：[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)、[block](#a8d6a01849e95c4a26d3270f4320c214f)。

<a id="r_a1066d309b56748223183d39e8fc7fd82"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#a1066d309b56748223183d39e8fc7fd82)。

<a id="r_a75b8ecd846fcf96708d31fb5efb0bea1"></a>

```c
enum bt_mesh_blob_xfer_phase phase
```

相关声明：[bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)、[phase](#a75b8ecd846fcf96708d31fb5efb0bea1)。

<a id="r_a86ed657bc97fc3c299e6fca6cdaee4e4"></a>

```c
struct bt_mesh_blob_srv::bt_mesh_blob_srv_state state
```

相关声明：[bt_mesh_blob_srv::bt_mesh_blob_srv_state](P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)、[state](#a86ed657bc97fc3c299e6fca6cdaee4e4)。

```c
struct {
```

<a id="r_a8e5fb50346168ce3993deb1f21444c3f"></a>

```c
uint16_t chunk_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_idx](#aa3ac872db59f2f1cd67d25e97020d484)。

<a id="r_a318a0e6065e0c717fd1fd0a3ed4f5538"></a>

```c
struct k_work_delayable report
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[report](#aad6ef41a187cc5489d6a8d5f4a5b3003)。

<a id="r_afec2237da95cc7ffbbdeb99d8ffb12b6"></a>

```c
} pull
```

相关声明：[pull](#afec2237da95cc7ffbbdeb99d8ffb12b6)。

## 9.3\_详细说明（Detailed Documentation）

<a id="a8d6a01849e95c4a26d3270f4320c214f"></a>

### `block`

```c
struct bt_mesh_blob_block bt_mesh_blob_srv::block
```

<a id="a65d08187dce1ed86cbfbb4f977cd32df"></a>

### `cb`

```c
const struct bt_mesh_blob_srv_cb* bt_mesh_blob_srv::cb
```

事件处理回调（Event handler callbacks）。

<a id="aa3ac872db59f2f1cd67d25e97020d484"></a>

### `chunk_idx`

```c
uint16_t bt_mesh_blob_srv::chunk_idx
```

<a id="a23d12a803a2414aa1460ea9a862cc78b"></a>

### `io`

```c
const struct bt_mesh_blob_io* bt_mesh_blob_srv::io
```

<a id="a1066d309b56748223183d39e8fc7fd82"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_blob_srv::mod
```

<a id="a75b8ecd846fcf96708d31fb5efb0bea1"></a>

### `phase`

```c
enum bt_mesh_blob_xfer_phase bt_mesh_blob_srv::phase
```

<a id="afec2237da95cc7ffbbdeb99d8ffb12b6"></a>

### `[struct]`

```c
struct { ... } bt_mesh_blob_srv::pull
```

<a id="aad6ef41a187cc5489d6a8d5f4a5b3003"></a>

### `report`

```c
struct k_work_delayable bt_mesh_blob_srv::report
```

<a id="a82a5c7fc2ad37e531ec10bada27bf10a"></a>

### `rx_timeout`

```c
struct k_work_delayable bt_mesh_blob_srv::rx_timeout
```

<a id="a86ed657bc97fc3c299e6fca6cdaee4e4"></a>

### `state`

```c
struct bt_mesh_blob_srv::bt_mesh_blob_srv_state bt_mesh_blob_srv::state
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_srv.h`

## 9.4\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h_source.html)
- [bt_mesh_blob_srv_state](P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)
- [bt_mesh_blob_srv_cb](P011_bt_mesh_blob_srv_cb_结构体.md)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_bt_mesh_blob_io_flash_结构体.md) · [返回大纲](大纲.md) · [下一章](P010_bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体.md)
