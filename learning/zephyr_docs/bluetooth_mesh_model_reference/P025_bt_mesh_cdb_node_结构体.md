---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-25
title: bt_mesh_cdb_node_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__node.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_mesh\_cdb\_node\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__cdb__node.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/bluetooth/mesh/cdb.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a751671f52c4fdf3f42b6f71193976dd5"></a>

```c
uint8_t uuid [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#a751671f52c4fdf3f42b6f71193976dd5)。

节点通用唯一标识符（Node UUID）。

<a id="r_a8c9941929a8ce6228817d76fe4e2375c"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a8c9941929a8ce6228817d76fe4e2375c)。

主元素地址（Primary element address）。

<a id="r_aa936534676ef7e256670d356eff7ac17"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#aa936534676ef7e256670d356eff7ac17)。

配网（Provisioning）时使用的网络密钥索引（Network key index）。

<a id="r_a2313e29b756344a493989f39ba1ec726"></a>

```c
uint8_t num_elem
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_elem](#a2313e29b756344a493989f39ba1ec726)。

元素数量（Number of elements）。

<a id="r_a54e5130d7dabedf09e23419a40f6778b"></a>

```c
struct bt_mesh_key dev_key
```

相关声明：[bt_mesh_key](P068_bt_mesh_key_结构体.md)、[dev_key](#a54e5130d7dabedf09e23419a40f6778b)。

设备密钥（Device key）。

<a id="r_a32f48db827713e53e02c0c1574476835"></a>

```c
atomic_t flags [(((((unsigned long)(BT_MESH_CDB_NODE_FLAG_COUNT)+((unsigned long)(ATOMIC_BITS) - 1))/(unsigned long)(ATOMIC_BITS)) *(unsigned long)(ATOMIC_BITS))/ATOMIC_BITS)]
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[flags](#a32f48db827713e53e02c0c1574476835)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[BT_MESH_CDB_NODE_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

节点标志（Node flags）。

## 25.2\_详细说明（Detailed Documentation）

<a id="a8c9941929a8ce6228817d76fe4e2375c"></a>

### `addr`

```c
uint16_t bt_mesh_cdb_node::addr
```

主元素地址（Primary element address）。

<a id="a54e5130d7dabedf09e23419a40f6778b"></a>

### `dev_key`

```c
struct bt_mesh_key bt_mesh_cdb_node::dev_key
```

设备密钥（Device key）。

<a id="a32f48db827713e53e02c0c1574476835"></a>

### `flags`

```c
atomic_t bt_mesh_cdb_node::flags[(((((unsigned long)(BT_MESH_CDB_NODE_FLAG_COUNT)+((unsigned long)(ATOMIC_BITS) - 1))/(unsigned long)(ATOMIC_BITS)) *(unsigned long)(ATOMIC_BITS))/ATOMIC_BITS)]
```

节点标志（Node flags）。

<a id="aa936534676ef7e256670d356eff7ac17"></a>

### `net_idx`

```c
uint16_t bt_mesh_cdb_node::net_idx
```

配网（Provisioning）时使用的网络密钥索引（Network key index）。

<a id="a2313e29b756344a493989f39ba1ec726"></a>

### `num_elem`

```c
uint8_t bt_mesh_cdb_node::num_elem
```

元素数量（Number of elements）。

<a id="a751671f52c4fdf3f42b6f71193976dd5"></a>

### `uuid`

```c
uint8_t bt_mesh_cdb_node::uuid[16]
```

节点通用唯一标识符（Node UUID）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/cdb.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/cdb.h](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_key](P068_bt_mesh_key_结构体.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [BT_MESH_CDB_NODE_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_mesh_cdb_app_key_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_mesh_cdb_subnet_结构体.md)
