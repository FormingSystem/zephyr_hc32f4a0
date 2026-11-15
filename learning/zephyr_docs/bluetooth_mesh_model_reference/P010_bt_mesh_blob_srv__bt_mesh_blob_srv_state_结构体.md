---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-10
title: bt_mesh_blob_srv__bt_mesh_blob_srv_state_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_mesh\_blob\_srv\_\_bt\_mesh\_blob\_srv\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__srv_1_1bt__mesh__blob__srv__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/blob_srv.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_ac5d12eef4c5723af0e19296d75f1c820"></a>

```c
struct bt_mesh_blob_xfer xfer
```

相关声明：[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[xfer](#ac5d12eef4c5723af0e19296d75f1c820)。

<a id="r_a08358fb301e775ed23c0d062676fbf22"></a>

```c
uint16_t cli
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cli](#a08358fb301e775ed23c0d062676fbf22)。

<a id="r_a6273d55eda23f868d51382c56bc41e27"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#a6273d55eda23f868d51382c56bc41e27)。

<a id="r_a0c87b3052680c675303747e805c2990e"></a>

```c
uint16_t timeout_base
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout_base](#a0c87b3052680c675303747e805c2990e)。

<a id="r_aadd08825d36f3ae1e4fe3a7845903f41"></a>

```c
uint16_t mtu_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu_size](#aadd08825d36f3ae1e4fe3a7845903f41)。

<a id="r_a79b0521bbd2473c6b414a24c5a7bf98a"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a79b0521bbd2473c6b414a24c5a7bf98a)。

<a id="r_a0f5d7d310be154f85ee96ccceb12e971"></a>

```c
atomic_t blocks [ATOMIC_BITMAP_SIZE(1)]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[blocks](#a0f5d7d310be154f85ee96ccceb12e971)、[ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)。

## 10.2\_详细说明（Detailed Documentation）

<a id="a6273d55eda23f868d51382c56bc41e27"></a>

### `app_idx`

```c
uint16_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::app_idx
```

<a id="a0f5d7d310be154f85ee96ccceb12e971"></a>

### `blocks`

```c
atomic_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::blocks[ATOMIC_BITMAP_SIZE(1)]
```

<a id="a08358fb301e775ed23c0d062676fbf22"></a>

### `cli`

```c
uint16_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::cli
```

<a id="aadd08825d36f3ae1e4fe3a7845903f41"></a>

### `mtu_size`

```c
uint16_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::mtu_size
```

<a id="a0c87b3052680c675303747e805c2990e"></a>

### `timeout_base`

```c
uint16_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::timeout_base
```

<a id="a79b0521bbd2473c6b414a24c5a7bf98a"></a>

### `ttl`

```c
uint8_t bt_mesh_blob_srv::bt_mesh_blob_srv_state::ttl
```

<a id="ac5d12eef4c5723af0e19296d75f1c820"></a>

### `xfer`

```c
struct bt_mesh_blob_xfer bt_mesh_blob_srv::bt_mesh_blob_srv_state::xfer
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_srv.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__srv_8h_source.html)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [ATOMIC_BITMAP_SIZE](../atomic_reference/P001_原子操作公共接口.md#gafac28874aaad3bcec72c693186e988cb)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_bt_mesh_blob_srv_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_mesh_blob_srv_cb_结构体.md)
