---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-170
title: bt_sdp_discover_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__discover__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第170章\_bt\_sdp\_discover\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__sdp__discover__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于远端SDP发现（SDP Discovery）的主要用户结构。

```c
#include <zephyr/bluetooth/classic/sdp.h>
```

<a id="details"></a>

用于远端SDP发现（SDP Discovery）的主要用户结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 170.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a01590d6508c8499f4cc111a320cca0bc"></a>

```c
const struct bt_uuid * uuid
```

相关声明：[bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)、[uuid](#a4c6073d7afda09be462902f5a95eaaed)。

要在远端 SDP 实体上发现的 UUID（服务）。

<a id="r_ae12a1dc612025db818165837fdcfdfe5"></a>

```c
uint32_t handle
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[handle](#a2be942f3d0f18c56567dafa45af9c53e)。

服务记录句柄（Service record handle）。

<a id="r_afdb1c56544bf5b97f98d79e26bbf53c0"></a>

```c
};
```

<a id="r_a650143f0733958cf1186543c3469facc"></a>

```c
bt_sdp_discover_func_t func
```

相关声明：[bt_sdp_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad672a89277b276d1b702fe07302c468e)、[func](#a650143f0733958cf1186543c3469facc)。

解析出 SDP 记录后调用的发现（discover）回调。

<a id="r_a6f8728e5b74211852e2ce8872c21e5fb"></a>

```c
struct net_buf_pool * pool
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[pool](#a6f8728e5b74211852e2ce8872c21e5fb)。

用户提供的用于保存 SDP 查询结果的内存缓冲区。

<a id="r_acec0306279408087352804fdf76560de"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#acec0306279408087352804fdf76560de)。

发现类型（Discover type）。

<a id="r_a7854bf938c439af66b4a0d721f2bd1c1"></a>

```c
struct bt_sdp_attribute_id_list * ids
```

相关声明：[bt_sdp_attribute_id_list](P166_bt_sdp_attribute_id_list_结构体.md)、[ids](#a7854bf938c439af66b4a0d721f2bd1c1)。

用于服务属性（Service Attribute）和服务搜索属性（Service Search Attribute）事务的属性 ID 列表。

## 170.2\_详细说明（Detailed Documentation）

<a id="afdb1c56544bf5b97f98d79e26bbf53c0"></a>

### `[union]`

```c
union { ... } bt_sdp_discover_params
```

<a id="a650143f0733958cf1186543c3469facc"></a>

### `func`

```c
bt_sdp_discover_func_t bt_sdp_discover_params::func
```

解析出 SDP 记录后调用的发现（discover）回调。

<a id="a2be942f3d0f18c56567dafa45af9c53e"></a>

### `handle`

```c
uint32_t bt_sdp_discover_params::handle
```

服务记录句柄（Service record handle）。

<a id="a7854bf938c439af66b4a0d721f2bd1c1"></a>

### `ids`

```c
struct bt_sdp_attribute_id_list* bt_sdp_discover_params::ids
```

用于服务属性（Service Attribute）和服务搜索属性（Service Search Attribute）事务的属性 ID 列表。

如果 `ids` 为 `NULL`，或者 `ids->count` 为 0，则使用默认范围 `(0x0000, 0xffff)`。

<a id="a6f8728e5b74211852e2ce8872c21e5fb"></a>

### `pool`

```c
struct net_buf_pool* bt_sdp_discover_params::pool
```

用户提供的用于保存 SDP 查询结果的内存缓冲区。

<a id="acec0306279408087352804fdf76560de"></a>

### `type`

```c
uint8_t bt_sdp_discover_params::type
```

发现类型（Discover type）。

<a id="a4c6073d7afda09be462902f5a95eaaed"></a>

### `uuid`

```c
const struct bt_uuid* bt_sdp_discover_params::uuid
```

要在远端 SDP 实体上发现的 UUID（服务）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/sdp.h`

## 170.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/sdp.h](https://docs.zephyrproject.org/latest/doxygen/html/sdp_8h_source.html)
- [bt_uuid](../bluetooth_connection_model_reference/P131_bt_uuid_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_sdp_discover_func_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html#gad672a89277b276d1b702fe07302c468e)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_sdp_attribute_id_list](P166_bt_sdp_attribute_id_list_结构体.md)
- [bt_sdp_discover_params](P170_bt_sdp_discover_params_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P169_bt_sdp_data_elem_结构体.md) · [返回大纲](大纲.md) · [下一章](P171_bt_sdp_record_结构体.md)
