---
id: learning.zephyr-docs.api-file-bluetooth-media-reference.page-2
title: zephyr__bluetooth__mesh__cdb.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_mesh\_\_cdb.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh配置数据库（Configuration Database，CDB）API的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/bluetooth/mesh.h>
```

查看此文件的源码。

蓝牙Mesh配置数据库（Configuration Database，CDB）API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fcdb_5Fnode"></a>

```c
struct bt_mesh_cdb_node
```

相关声明：[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)。

<a id="r_bt_5Fmesh_5Fcdb_5Fsubnet"></a>

```c
struct bt_mesh_cdb_subnet
```

相关声明：[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)。

<a id="r_bt_5Fmesh_5Fcdb_5Fapp_5Fkey"></a>

```c
struct bt_mesh_cdb_app_key
```

相关声明：[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)。

<a id="r_bt_5Fmesh_5Fcdb"></a>

```c
struct bt_mesh_cdb
```

相关声明：[bt_mesh_cdb](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ae49e5e1ae89eef30538ae9f45c772b64"></a>

```c
#define NODE_COUNT 0
```

相关声明：[NODE_COUNT](#ae49e5e1ae89eef30538ae9f45c772b64)。

<a id="r_a5ab07a907049974c089a4b0dd706ef77"></a>

```c
#define SUBNET_COUNT 0
```

相关声明：[SUBNET_COUNT](#a5ab07a907049974c089a4b0dd706ef77)。

<a id="r_aab65f293c17c657d670e802bbfe389d7"></a>

```c
#define APP_KEY_COUNT 0
```

相关声明：[APP_KEY_COUNT](#aab65f293c17c657d670e802bbfe389d7)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 2.3\_类型定义（Typedefs）

<a id="r_a5d00af9f4c971f31c3016824757ebf66"></a>

```c
typedef uint8_t(* bt_mesh_cdb_node_func_t) (struct bt_mesh_cdb_node *node, void *user_data)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_cdb_node_func_t](#a5d00af9f4c971f31c3016824757ebf66)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)。

节点迭代器回调（Node Iterator Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.4\_枚举（Enumerations）

<a id="r_a159f4eec3bbcaed25a4369b67e6937f1"></a>

```c
enum { BT_MESH_CDB_NODE_CONFIGURED , BT_MESH_CDB_NODE_FLAG_COUNT }
```

相关声明：[BT_MESH_CDB_NODE_CONFIGURED](#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12)、[BT_MESH_CDB_NODE_FLAG_COUNT](#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)。

<a id="r_a0e45ffdd001e9fac31b74949a004e8f5"></a>

```c
enum { BT_MESH_CDB_VALID , BT_MESH_CDB_SUBNET_PENDING , BT_MESH_CDB_KEYS_PENDING , BT_MESH_CDB_NODES_PENDING , BT_MESH_CDB_IVU_IN_PROGRESS , BT_MESH_CDB_FLAG_COUNT }
```

相关声明：[BT_MESH_CDB_VALID](#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d)、[BT_MESH_CDB_SUBNET_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd)、[BT_MESH_CDB_KEYS_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8)、[BT_MESH_CDB_NODES_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1)、[BT_MESH_CDB_IVU_IN_PROGRESS](#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6)、[BT_MESH_CDB_FLAG_COUNT](#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)。

<a id="r_a2ec5612f827a95662f18bc9e012048cd"></a>

```c
enum { BT_MESH_CDB_ITER_STOP = 0 , BT_MESH_CDB_ITER_CONTINUE }
```

相关声明：[BT_MESH_CDB_ITER_STOP](#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb)、[BT_MESH_CDB_ITER_CONTINUE](#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.5\_函数（Functions）

<a id="r_a00490e69b96e88cdf7336ca22e63617d"></a>

```c
int bt_mesh_cdb_create (const uint8_t key[16])
```

相关声明：[bt_mesh_cdb_create](#a00490e69b96e88cdf7336ca22e63617d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

创建 Mesh 配置数据库（Mesh Configuration Database）。

<a id="r_a4bf4f49fbd75ee33876ffd34f6c6f76f"></a>

```c
void bt_mesh_cdb_clear (void)
```

相关声明：[bt_mesh_cdb_clear](#a4bf4f49fbd75ee33876ffd34f6c6f76f)。

清空 Mesh 配置数据库（Mesh Configuration Database）。

<a id="r_aa6d124339002c43fc35f301a9eef3e7c"></a>

```c
void bt_mesh_cdb_iv_update (uint32_t iv_index, bool iv_update)
```

相关声明：[bt_mesh_cdb_iv_update](#aa6d124339002c43fc35f301a9eef3e7c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置并存储 IV 索引（IV Index）和 IV 更新标志（IV Update Flag）。

<a id="r_ab0dc86dd674f57a820aa3f5cebf77895"></a>

```c
struct bt_mesh_cdb_node * bt_mesh_cdb_node_alloc (const uint8_t uuid[16], uint16_t addr, uint8_t num_elem, uint16_t net_idx)
```

相关声明：[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[bt_mesh_cdb_node_alloc](#ab0dc86dd674f57a820aa3f5cebf77895)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](../data_utilities/P026_UUID二进制结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

分配节点（Node）。

<a id="r_aa10c4ec973e61626ba6424e443fb0b88"></a>

```c
uint16_t bt_mesh_cdb_free_addr_get (uint8_t num_elem)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[bt_mesh_cdb_free_addr_get](#aa10c4ec973e61626ba6424e443fb0b88)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

获取适合给定元素数量（Element Count）的第一个可用地址。

<a id="r_a6d9cc2d360075b6b3e939a4979e08895"></a>

```c
void bt_mesh_cdb_node_del (struct bt_mesh_cdb_node *node, bool store)
```

相关声明：[bt_mesh_cdb_node_del](#a6d9cc2d360075b6b3e939a4979e08895)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

删除节点（Node）。

<a id="r_ad4333e02b866589f7ca2b155cf814ca4"></a>

```c
void bt_mesh_cdb_node_update (struct bt_mesh_cdb_node *node, uint16_t addr, uint8_t num_elem)
```

相关声明：[bt_mesh_cdb_node_update](#ad4333e02b866589f7ca2b155cf814ca4)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新节点（Node）。

<a id="r_a3d0034ec500d3964dd4b428e518abfb9"></a>

```c
struct bt_mesh_cdb_node * bt_mesh_cdb_node_get (uint16_t addr)
```

相关声明：[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[bt_mesh_cdb_node_get](#a3d0034ec500d3964dd4b428e518abfb9)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据地址获取节点（Node）。

<a id="r_ac775f3d1be745aeba2979b9ae4b42c4f"></a>

```c
void bt_mesh_cdb_node_store (const struct bt_mesh_cdb_node *node)
```

相关声明：[bt_mesh_cdb_node_store](#ac775f3d1be745aeba2979b9ae4b42c4f)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)。

将节点保存到持久化存储（Persistent Storage）。

<a id="r_a26b1e5560998cc37e2a627c44326db62"></a>

```c
int bt_mesh_cdb_node_key_import (struct bt_mesh_cdb_node *node, const uint8_t in[16])
```

相关声明：[bt_mesh_cdb_node_key_import](#a26b1e5560998cc37e2a627c44326db62)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为选定节点导入设备密钥（Device Key）。

<a id="r_a4a0f7577f1a8df96e4dcab6f682abf23"></a>

```c
int bt_mesh_cdb_node_key_export (const struct bt_mesh_cdb_node *node, uint8_t out[16])
```

相关声明：[bt_mesh_cdb_node_key_export](#a4a0f7577f1a8df96e4dcab6f682abf23)、[bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从选定节点导出设备密钥（Device Key）。

<a id="r_ae8ed0ef1a00e973d864c944c9d9400bc"></a>

```c
void bt_mesh_cdb_node_foreach (bt_mesh_cdb_node_func_t func, void *user_data)
```

相关声明：[bt_mesh_cdb_node_foreach](#ae8ed0ef1a00e973d864c944c9d9400bc)、[bt_mesh_cdb_node_func_t](#a5d00af9f4c971f31c3016824757ebf66)。

节点迭代器（Node Iterator）。

<a id="r_aeba4ed506e30ab8d91746b36e7e5f968"></a>

```c
struct bt_mesh_cdb_subnet * bt_mesh_cdb_subnet_alloc (uint16_t net_idx)
```

相关声明：[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)、[bt_mesh_cdb_subnet_alloc](#aeba4ed506e30ab8d91746b36e7e5f968)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

分配子网（Subnet）。

<a id="r_a66df2f6b6363af595181fe722122996d"></a>

```c
void bt_mesh_cdb_subnet_del (struct bt_mesh_cdb_subnet *sub, bool store)
```

相关声明：[bt_mesh_cdb_subnet_del](#a66df2f6b6363af595181fe722122996d)、[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

删除子网（Subnet）。

<a id="r_a34dcf031e675235cdcbe0e1f76c00cf3"></a>

```c
struct bt_mesh_cdb_subnet * bt_mesh_cdb_subnet_get (uint16_t net_idx)
```

相关声明：[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)、[bt_mesh_cdb_subnet_get](#a34dcf031e675235cdcbe0e1f76c00cf3)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据 NetIdx 获取子网（Subnet）。

<a id="r_a59e6b7da8c91df35ce6f8268da35c933"></a>

```c
void bt_mesh_cdb_subnet_store (const struct bt_mesh_cdb_subnet *sub)
```

相关声明：[bt_mesh_cdb_subnet_store](#a59e6b7da8c91df35ce6f8268da35c933)、[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)。

将子网保存到持久化存储（Persistent Storage）。

<a id="r_a121a30fd546ccb887c2c49ceef65c2d6"></a>

```c
uint8_t bt_mesh_cdb_subnet_flags (const struct bt_mesh_cdb_subnet *sub)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bt_mesh_cdb_subnet_flags](#a121a30fd546ccb887c2c49ceef65c2d6)、[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)。

获取子网标志（Subnet Flags）。

<a id="r_aba737b508e0e40dfb5ad9da9d7b6fd11"></a>

```c
int bt_mesh_cdb_subnet_key_import (struct bt_mesh_cdb_subnet *sub, int key_idx, const uint8_t in[16])
```

相关声明：[bt_mesh_cdb_subnet_key_import](#aba737b508e0e40dfb5ad9da9d7b6fd11)、[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为选定子网导入网络密钥（Network Key）。

<a id="r_ac361a17a704195e852faecda09881203"></a>

```c
int bt_mesh_cdb_subnet_key_export (const struct bt_mesh_cdb_subnet *sub, int key_idx, uint8_t out[16])
```

相关声明：[bt_mesh_cdb_subnet_key_export](#ac361a17a704195e852faecda09881203)、[bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从选定子网导出网络密钥（Network Key）。

<a id="r_ab82dcdf26d66ea4ab0df34bc23421f39"></a>

```c
struct bt_mesh_cdb_app_key * bt_mesh_cdb_app_key_alloc (uint16_t net_idx, uint16_t app_idx)
```

相关声明：[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)、[bt_mesh_cdb_app_key_alloc](#ab82dcdf26d66ea4ab0df34bc23421f39)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

分配应用密钥（Application Key）。

<a id="r_a692c6980c9b0d2da18e8f47d67757f07"></a>

```c
void bt_mesh_cdb_app_key_del (struct bt_mesh_cdb_app_key *key, bool store)
```

相关声明：[bt_mesh_cdb_app_key_del](#a692c6980c9b0d2da18e8f47d67757f07)、[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

删除应用密钥（Application Key）。

<a id="r_ab728a20fdb1535cc7059a39e8490a736"></a>

```c
struct bt_mesh_cdb_app_key * bt_mesh_cdb_app_key_get (uint16_t app_idx)
```

相关声明：[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)、[bt_mesh_cdb_app_key_get](#ab728a20fdb1535cc7059a39e8490a736)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据 AppIdx 获取应用密钥（Application Key）。

<a id="r_a4e9470adfa797be85b7f4df43b63d6d2"></a>

```c
void bt_mesh_cdb_app_key_store (const struct bt_mesh_cdb_app_key *key)
```

相关声明：[bt_mesh_cdb_app_key_store](#a4e9470adfa797be85b7f4df43b63d6d2)、[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)。

将应用密钥保存到持久化存储（Persistent Storage）。

<a id="r_a9ad0651ccaa7ff1f86402ce8c05c9410"></a>

```c
int bt_mesh_cdb_app_key_import (struct bt_mesh_cdb_app_key *key, int key_idx, const uint8_t in[16])
```

相关声明：[bt_mesh_cdb_app_key_import](#a9ad0651ccaa7ff1f86402ce8c05c9410)、[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

导入应用密钥（Application Key）。

<a id="r_a87cfce7316efabe4c8b24be6c3b6d8b4"></a>

```c
int bt_mesh_cdb_app_key_export (const struct bt_mesh_cdb_app_key *key, int key_idx, uint8_t out[16])
```

相关声明：[bt_mesh_cdb_app_key_export](#a87cfce7316efabe4c8b24be6c3b6d8b4)、[bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

导出应用密钥（Application Key）。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 2.6\_变量（Variables）

<a id="r_afa51505628405a3778d1bdb4fd905ca0"></a>

```c
struct bt_mesh_cdb bt_mesh_cdb
```

相关声明：[bt_mesh_cdb](#afa51505628405a3778d1bdb4fd905ca0)。

可通过此变量访问全局配置数据库（CDB）实例。

## 2.7\_详细说明（Detailed Documentation）

<a id="aab65f293c17c657d670e802bbfe389d7"></a>

### `APP_KEY_COUNT`

```c
#define APP_KEY_COUNT 0
```

<a id="ae49e5e1ae89eef30538ae9f45c772b64"></a>

### `NODE_COUNT`

```c
#define NODE_COUNT 0
```

<a id="a5ab07a907049974c089a4b0dd706ef77"></a>

### `SUBNET_COUNT`

```c
#define SUBNET_COUNT 0
```

<a id="a5d00af9f4c971f31c3016824757ebf66"></a>

### `bt_mesh_cdb_node_func_t`

```c
typedef uint8_t(* bt_mesh_cdb_node_func_t) (struct bt_mesh_cdb_node *node, void *user_data)
```

节点迭代器回调（Node Iterator Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 找到的节点（Node）。 |
| `user_data` | 所给数据（Data）。 |

**返回（Returns）**：返回：BT_MESH_CDB_ITER_CONTINUE 表示继续遍历节点，BT_MESH_CDB_ITER_STOP 表示停止。

<a id="a2ec5612f827a95662f18bc9e012048cd"></a>

### `anonymous enum`

```c
anonymous enum
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_CDB_ITER_STOP` |  |
| `BT_MESH_CDB_ITER_CONTINUE` |  |

<a id="a0e45ffdd001e9fac31b74949a004e8f5"></a>

### `anonymous enum`

```c
anonymous enum
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_CDB_VALID` |  |
| `BT_MESH_CDB_SUBNET_PENDING` |  |
| `BT_MESH_CDB_KEYS_PENDING` |  |
| `BT_MESH_CDB_NODES_PENDING` |  |
| `BT_MESH_CDB_IVU_IN_PROGRESS` |  |
| `BT_MESH_CDB_FLAG_COUNT` |  |

<a id="a159f4eec3bbcaed25a4369b67e6937f1"></a>

### `anonymous enum`

```c
anonymous enum
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_CDB_NODE_CONFIGURED` |  |
| `BT_MESH_CDB_NODE_FLAG_COUNT` |  |

<a id="ab82dcdf26d66ea4ab0df34bc23421f39"></a>

### `bt_mesh_cdb_app_key_alloc()`

```c
struct bt_mesh_cdb_app_key * bt_mesh_cdb_app_key_alloc ( uint16_t net_idx, uint16_t app_idx )
```

分配应用密钥（Application Key）。

在配置数据库（CDB）中分配新的应用密钥（Application Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 应用密钥绑定的网络密钥（NetKey）的 NetIdx。 |
| `app_idx` | 应用密钥（Application Key）的 AppIdx。 |

**返回（Returns）**：返回：新应用密钥；若因资源不足无法分配，或该密钥已分配，则返回 NULL。

<a id="a692c6980c9b0d2da18e8f47d67757f07"></a>

### `bt_mesh_cdb_app_key_del()`

```c
void bt_mesh_cdb_app_key_del ( struct bt_mesh_cdb_app_key * key, bool store )
```

删除应用密钥（Application Key）。

从配置数据库（CDB）删除应用密钥（Application Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 要删除的应用密钥（Application Key）。 |
| `store` | 若为 true，将从持久化存储（Persistent Storage）清除该密钥。 |

<a id="a87cfce7316efabe4c8b24be6c3b6d8b4"></a>

### `bt_mesh_cdb_app_key_export()`

```c
int bt_mesh_cdb_app_key_export ( const struct bt_mesh_cdb_app_key * key, int key_idx, uint8_t out[16] )
```

导出应用密钥（Application Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导出（Export）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 配置数据库（CDB）的应用密钥结构体（Application Key Structure）。 |
| `key_idx` | 取值为 0 或 1。密钥刷新过程（Key Refresh Procedure）进行中时，有两个可用密钥：旧密钥索引为 0，新密钥索引为 1。否则，仅存在索引为 0 的密钥。 |
| `out` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ab728a20fdb1535cc7059a39e8490a736"></a>

### `bt_mesh_cdb_app_key_get()`

```c
struct bt_mesh_cdb_app_key * bt_mesh_cdb_app_key_get ( uint16_t app_idx)
```

根据 AppIdx 获取应用密钥（Application Key）。

尝试查找具有指定 AppIdx 的应用密钥（Application Key）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `app_idx` | 要查找的应用密钥（Application Key）的 AppIdx。 |

**返回（Returns）**：返回：具有指定 AppIdx 的应用密钥；不存在时为 NULL。

<a id="a9ad0651ccaa7ff1f86402ce8c05c9410"></a>

### `bt_mesh_cdb_app_key_import()`

```c
int bt_mesh_cdb_app_key_import ( struct bt_mesh_cdb_app_key * key, int key_idx, const uint8_t in[16] )
```

导入应用密钥（Application Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导入（Import）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 配置数据库（CDB）的应用密钥结构体（Application Key Structure）。 |
| `key_idx` | 取值为 0 或 1。密钥刷新过程（Key Refresh Procedure）进行中时，有两个可用密钥：旧密钥索引为 0，新密钥索引为 1。否则，仅存在索引为 0 的密钥。 |
| `in` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="a4e9470adfa797be85b7f4df43b63d6d2"></a>

### `bt_mesh_cdb_app_key_store()`

```c
void bt_mesh_cdb_app_key_store ( const struct bt_mesh_cdb_app_key * key)
```

将应用密钥保存到持久化存储（Persistent Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 要存储的应用密钥（Application Key）。 |

<a id="a4bf4f49fbd75ee33876ffd34f6c6f76f"></a>

### `bt_mesh_cdb_clear()`

```c
void bt_mesh_cdb_clear ( void )
```

清空 Mesh 配置数据库（Mesh Configuration Database）。

移除数据库中存储的全部节点、子网和应用密钥（Nodes, Subnets, App-keys），并将数据库标记为无效。若启用 CONFIG_BT_SETTINGS，还会从持久化存储清除这些数据。

<a id="a00490e69b96e88cdf7336ca22e63617d"></a>

### `bt_mesh_cdb_create()`

```c
int bt_mesh_cdb_create ( const uint8_t key[16])
```

创建 Mesh 配置数据库（Mesh Configuration Database）。

创建并初始化 Mesh 配置数据库（Mesh Configuration Database）。添加一个主子网（Primary Subnet），即 NetIdx 为 0 的子网，并使用所提供的密钥作为该子网的 NetKey。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 用于主子网（Primary Subnet）的 NetKey。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="aa10c4ec973e61626ba6424e443fb0b88"></a>

### `bt_mesh_cdb_free_addr_get()`

```c
uint16_t bt_mesh_cdb_free_addr_get ( uint8_t num_elem)
```

获取适合给定元素数量（Element Count）的第一个可用地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `num_elem` | 需要容纳的元素数量（Number of Elements）。 |

**返回（Returns）**：返回：能容纳具有给定元素数量的节点的地址区间中的第一个单播地址（Unicast Address）。

<a id="aa6d124339002c43fc35f301a9eef3e7c"></a>

### `bt_mesh_cdb_iv_update()`

```c
void bt_mesh_cdb_iv_update ( uint32_t iv_index, bool iv_update )
```

设置并存储 IV 索引（IV Index）和 IV 更新标志（IV Update Flag）。

配置数据库（CDB）保存的 IV 索引（IV Index）将用于新节点配网（Provisioning）。此函数一般仅在协议栈内部使用。

若启用 CONFIG_BT_SETTINGS，此函数会将数据保存到持久化存储（Persistent Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iv_index` | 要使用的新 IV 索引（IV Index）。 |
| `iv_update` | 有正在进行的 IV 更新过程（IV Update Procedure）时为 true。 |

<a id="ab0dc86dd674f57a820aa3f5cebf77895"></a>

### `bt_mesh_cdb_node_alloc()`

```c
struct bt_mesh_cdb_node * bt_mesh_cdb_node_alloc ( const uint8_t uuid[16], uint16_t addr, uint8_t num_elem, uint16_t net_idx )
```

分配节点（Node）。

在配置数据库（CDB）中分配新节点（Node）。

addr 为 0 时，使用 bt_mesh_cdb_free_addr_get 分配空闲地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `uuid` | 节点的通用唯一标识符（UUID）。 |
| `addr` | 节点主元素（Primary Element）的地址。为 0 时，将最低的可用地址分配给该节点。 |
| `num_elem` | 节点具有的元素数量（Number of Elements）。 |
| `net_idx` | 节点配网（Provisioning）所属子网的 NetIdx。 |

**返回（Returns）**：返回：新节点。若 CDB 已分配 CONFIG_BT_MESH_CDB_NODE_COUNT 个节点、已达到单播地址范围末端，或非零 addr 小于最低可用地址或与已分配地址冲突，则返回 NULL。

<a id="a6d9cc2d360075b6b3e939a4979e08895"></a>

### `bt_mesh_cdb_node_del()`

```c
void bt_mesh_cdb_node_del ( struct bt_mesh_cdb_node * node, bool store )
```

删除节点（Node）。

从配置数据库（CDB）删除节点。删除时，若被删节点最后一个元素的地址大于最低可用地址，CDB 将更新最低可用地址。只有在 IV 索引（IV Index）更新后，最低可用地址才会重置，被删地址才可复用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 要删除的节点（Node）。 |
| `store` | 若为 true，将从持久化存储（Persistent Storage）清除该节点。 |

<a id="ae8ed0ef1a00e973d864c944c9d9400bc"></a>

### `bt_mesh_cdb_node_foreach()`

```c
void bt_mesh_cdb_node_foreach ( bt_mesh_cdb_node_func_t func, void * user_data )
```

节点迭代器（Node Iterator）。

遍历 Mesh 配置数据库（Mesh Configuration Database）中的节点。只对有效节点，即已分配节点，调用回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 回调函数（Callback function）。 |
| `user_data` | 传给回调（Callback）的数据。 |

<a id="a3d0034ec500d3964dd4b428e518abfb9"></a>

### `bt_mesh_cdb_node_get()`

```c
struct bt_mesh_cdb_node * bt_mesh_cdb_node_get ( uint16_t addr)
```

根据地址获取节点（Node）。

尝试查找其某个元素被分配了给定地址的节点（Node）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr` | 要查找的元素地址（Element Address）。 |

**返回（Returns）**：返回：包含地址为 addr 的元素的节点；不存在时为 NULL。

<a id="a4a0f7577f1a8df96e4dcab6f682abf23"></a>

### `bt_mesh_cdb_node_key_export()`

```c
int bt_mesh_cdb_node_key_export ( const struct bt_mesh_cdb_node * node, uint8_t out[16] )
```

从选定节点导出设备密钥（Device Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导出（Export）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 选定节点（Selected Node）。 |
| `out` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="a26b1e5560998cc37e2a627c44326db62"></a>

### `bt_mesh_cdb_node_key_import()`

```c
int bt_mesh_cdb_node_key_import ( struct bt_mesh_cdb_node * node, const uint8_t in[16] )
```

为选定节点导入设备密钥（Device Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导入（Import）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 选定节点（Selected Node）。 |
| `in` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="ac775f3d1be745aeba2979b9ae4b42c4f"></a>

### `bt_mesh_cdb_node_store()`

```c
void bt_mesh_cdb_node_store ( const struct bt_mesh_cdb_node * node)
```

将节点保存到持久化存储（Persistent Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 要存储的节点（Node）。 |

<a id="ad4333e02b866589f7ca2b155cf814ca4"></a>

### `bt_mesh_cdb_node_update()`

```c
void bt_mesh_cdb_node_update ( struct bt_mesh_cdb_node * node, uint16_t addr, uint8_t num_elem )
```

更新节点（Node）。

为节点分配新地址，并清除先前的持久化存储条目（Persistent Storage Entry）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 要更新的节点（Node）。 |
| `addr` | 节点的新单播地址（Unicast Address）。 |
| `num_elem` | 节点更新后的元素数量（Number of Elements）。 |

<a id="aeba4ed506e30ab8d91746b36e7e5f968"></a>

### `bt_mesh_cdb_subnet_alloc()`

```c
struct bt_mesh_cdb_subnet * bt_mesh_cdb_subnet_alloc ( uint16_t net_idx)
```

分配子网（Subnet）。

在配置数据库（CDB）中分配新子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 子网（Subnet）的 NetIdx。 |

**返回（Returns）**：返回：新子网；若因资源不足无法分配，或该子网已分配，则返回 NULL。

<a id="a66df2f6b6363af595181fe722122996d"></a>

### `bt_mesh_cdb_subnet_del()`

```c
void bt_mesh_cdb_subnet_del ( struct bt_mesh_cdb_subnet * sub, bool store )
```

删除子网（Subnet）。

从配置数据库（CDB）删除子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 要删除的子网（Subnet）。 |
| `store` | 若为 true，将从持久化存储（Persistent Storage）清除该子网。 |

<a id="a121a30fd546ccb887c2c49ceef65c2d6"></a>

### `bt_mesh_cdb_subnet_flags()`

```c
uint8_t bt_mesh_cdb_subnet_flags ( const struct bt_mesh_cdb_subnet * sub)
```

获取子网标志（Subnet Flags）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 要获取其标志（Flags）的子网。 |

**返回（Returns）**：返回：子网的标志（Subnet Flags）。

<a id="a34dcf031e675235cdcbe0e1f76c00cf3"></a>

### `bt_mesh_cdb_subnet_get()`

```c
struct bt_mesh_cdb_subnet * bt_mesh_cdb_subnet_get ( uint16_t net_idx)
```

根据 NetIdx 获取子网（Subnet）。

尝试查找具有指定 NetIdx 的子网（Subnet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `net_idx` | 要查找的子网（Subnet）的 NetIdx。 |

**返回（Returns）**：返回：具有指定 NetIdx 的子网；不存在时为 NULL。

<a id="ac361a17a704195e852faecda09881203"></a>

### `bt_mesh_cdb_subnet_key_export()`

```c
int bt_mesh_cdb_subnet_key_export ( const struct bt_mesh_cdb_subnet * sub, int key_idx, uint8_t out[16] )
```

从选定子网导出网络密钥（Network Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导出（Export）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 选定子网（Selected Subnetwork）。 |
| `key_idx` | 取值为 0 或 1。密钥刷新过程（Key Refresh Procedure）进行中时，有两个可用密钥：旧密钥索引为 0，新密钥索引为 1。否则，仅存在索引为 0 的密钥。 |
| `out` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="aba737b508e0e40dfb5ad9da9d7b6fd11"></a>

### `bt_mesh_cdb_subnet_key_import()`

```c
int bt_mesh_cdb_subnet_key_import ( struct bt_mesh_cdb_subnet * sub, int key_idx, const uint8_t in[16] )
```

为选定子网导入网络密钥（Network Key）。

使用 PSA 实现的安全库（Security Library）时，密钥隐藏在库中，通过指针访问密钥不能获得有效值；应用必须导入（Import）密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 选定子网（Selected Subnetwork）。 |
| `key_idx` | 取值为 0 或 1。密钥刷新过程（Key Refresh Procedure）进行中时，有两个可用密钥：旧密钥索引为 0，新密钥索引为 1。否则，仅存在索引为 0 的密钥。 |
| `in` | 密钥值（Key Value）。 |

**返回（Returns）**：返回：成功时为 0，失败时为负错误码（Error Code）。

<a id="a59e6b7da8c91df35ce6f8268da35c933"></a>

### `bt_mesh_cdb_subnet_store()`

```c
void bt_mesh_cdb_subnet_store ( const struct bt_mesh_cdb_subnet * sub)
```

将子网保存到持久化存储（Persistent Storage）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sub` | 要存储的子网（Subnet）。 |

<a id="afa51505628405a3778d1bdb4fd905ca0"></a>

### `bt_mesh_cdb`

```c
struct bt_mesh_cdb bt_mesh_cdb
```

声明属性：`extern`。

可通过此变量访问全局配置数据库（CDB）实例。


## 2.8\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/bluetooth/mesh.h](../api_source_reference/P514_mesh.h_源码浏览.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P003_cdb.h_源码浏览.md)
- [bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)
- [bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)
- [bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)
- [bt_mesh_cdb](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb"></a>
<a id="a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6"></a>
<a id="a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41"></a>
<a id="a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12"></a>
<a id="a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P001_zephyr__bluetooth__bluetooth.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__sensor__max30009.h_文件参考.md)
