---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-23
title: bt_mesh_cdb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_bt\_mesh\_cdb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/cdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a48b3cf852a42b580f911e193a9764517"></a>

```c
uint32_t iv_index
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[iv_index](#a48b3cf852a42b580f911e193a9764517)。

网络初始化向量索引（Network IV Index）。

<a id="r_acb7f3ae85a5929b9cfc18531e1d98ab5"></a>

```c
uint16_t lowest_avail_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[lowest_avail_addr](#acb7f3ae85a5929b9cfc18531e1d98ab5)。

可用于配网（Provisioning）的最低单播地址（Unicast address）。

<a id="r_aa2526502debab1add405fe6e2c475475"></a>

```c
atomic_t flags [(((((unsigned long)(BT_MESH_CDB_FLAG_COUNT)+((unsigned long)(ATOMIC_BITS) - 1))/(unsigned long)(ATOMIC_BITS)) *(unsigned long)(ATOMIC_BITS))/ATOMIC_BITS)]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flags](#aa2526502debab1add405fe6e2c475475)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[BT_MESH_CDB_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

配置数据库状态标志（CDB state flags），私有。

<a id="r_a7af2ac65c8919c594b8283ff57b5b7fc"></a>

```c
struct bt_mesh_cdb_node nodes [0]
```

相关声明：[bt_mesh_cdb_node](P025_bt_mesh_cdb_node_结构体.md)、[nodes](#a7af2ac65c8919c594b8283ff57b5b7fc)。

Mesh 网络中的节点（Nodes）。

<a id="r_ae391c898d11257c484c4e8d1b38fd9dc"></a>

```c
struct bt_mesh_cdb_subnet subnets [0]
```

相关声明：[bt_mesh_cdb_subnet](P026_bt_mesh_cdb_subnet_结构体.md)、[subnets](#ae391c898d11257c484c4e8d1b38fd9dc)。

Mesh 网络中的子网（Subnets）。

<a id="r_a59a130ffed26c362dc72d57d1ac7d7fd"></a>

```c
struct bt_mesh_cdb_app_key app_keys [0]
```

相关声明：[bt_mesh_cdb_app_key](P024_bt_mesh_cdb_app_key_结构体.md)、[app_keys](#a59a130ffed26c362dc72d57d1ac7d7fd)。

Mesh 网络中的应用密钥（Application keys）。

## 23.2\_详细说明（Detailed Documentation）

<a id="a59a130ffed26c362dc72d57d1ac7d7fd"></a>

### `app_keys`

```c
struct bt_mesh_cdb_app_key bt_mesh_cdb::app_keys[0]
```

Mesh 网络中的应用密钥（Application keys）。

<a id="aa2526502debab1add405fe6e2c475475"></a>

### `flags`

```c
atomic_t bt_mesh_cdb::flags[(((((unsigned long)(BT_MESH_CDB_FLAG_COUNT)+((unsigned long)(ATOMIC_BITS) - 1))/(unsigned long)(ATOMIC_BITS)) *(unsigned long)(ATOMIC_BITS))/ATOMIC_BITS)]
```

配置数据库状态标志（CDB state flags），私有。

<a id="a48b3cf852a42b580f911e193a9764517"></a>

### `iv_index`

```c
uint32_t bt_mesh_cdb::iv_index
```

网络初始化向量索引（Network IV Index）。

<a id="acb7f3ae85a5929b9cfc18531e1d98ab5"></a>

### `lowest_avail_addr`

```c
uint16_t bt_mesh_cdb::lowest_avail_addr
```

可用于配网（Provisioning）的最低单播地址（Unicast address）。

<a id="a7af2ac65c8919c594b8283ff57b5b7fc"></a>

### `nodes`

```c
struct bt_mesh_cdb_node bt_mesh_cdb::nodes[0]
```

Mesh 网络中的节点（Nodes）。

<a id="ae391c898d11257c484c4e8d1b38fd9dc"></a>

### `subnets`

```c
struct bt_mesh_cdb_subnet bt_mesh_cdb::subnets[0]
```

Mesh 网络中的子网（Subnets）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cdb.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [BT_MESH_CDB_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)
- [bt_mesh_cdb_node](P025_bt_mesh_cdb_node_结构体.md)
- [bt_mesh_cdb_subnet](P026_bt_mesh_cdb_subnet_结构体.md)
- [bt_mesh_cdb_app_key](P024_bt_mesh_cdb_app_key_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_bt_mesh_brg_cfg_table_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_bt_mesh_cdb_app_key_结构体.md)
