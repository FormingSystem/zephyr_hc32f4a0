---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-4
title: 蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_蓝牙 Mesh 设备固件更新（Device Firmware Update，DFU）元数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 Mesh DFU 元数据的公共类型与函数。

<a id="details"></a>

蓝牙 Mesh DFU 元数据的公共类型与函数。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_dfu_5Fmetadata_2Eh"></a>

```c
file dfu_metadata.h
```

相关声明：[dfu_metadata.h](../api_file_interface_reference/P010_zephyr__bluetooth__mesh__dfu_metadata.h_文件参考.md)。

蓝牙Mesh设备固件更新（DFU）元数据API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fdfu_5Fmetadata_5Ffw_5Fver"></a>

```c
struct bt_mesh_dfu_metadata_fw_ver
```

相关声明：[bt_mesh_dfu_metadata_fw_ver](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)。

固件版本（Firmware Version）。

<a id="r_bt_5Fmesh_5Fdfu_5Fmetadata"></a>

```c
struct bt_mesh_dfu_metadata
```

相关声明：[bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)。

固件元数据（Firmware Metadata）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gaec5fa6e61a6ae88ac7a14f1ec09585b8"></a>

```c
enum bt_mesh_dfu_metadata_fw_core_type { BT_MESH_DFU_FW_CORE_TYPE_APP = (1UL << (0)) , BT_MESH_DFU_FW_CORE_TYPE_NETWORK = (1UL << (1)) , BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB = (1UL << (2)) }
```

相关声明：[bt_mesh_dfu_metadata_fw_core_type](#gaec5fa6e61a6ae88ac7a14f1ec09585b8)、[BT_MESH_DFU_FW_CORE_TYPE_APP](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0)、[BT_MESH_DFU_FW_CORE_TYPE_NETWORK](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692)、[BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB](#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2)。

固件核心类型（firmware core type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.4\_函数（Functions）

<a id="r_ga7f9ab277a7a47ad9cd8e616d3aa810d4"></a>

```c
int bt_mesh_dfu_metadata_decode (struct net_buf_simple *buf, struct bt_mesh_dfu_metadata *metadata)
```

相关声明：[bt_mesh_dfu_metadata_decode](#ga7f9ab277a7a47ad9cd8e616d3aa810d4)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)。

从网络缓冲区（network buffer）中解码固件元数据（firmware metadata）。

<a id="r_ga94de2f3730f600d58ff2102257d7ead9"></a>

```c
int bt_mesh_dfu_metadata_encode (const struct bt_mesh_dfu_metadata *metadata, struct net_buf_simple *buf)
```

相关声明：[bt_mesh_dfu_metadata_encode](#ga94de2f3730f600d58ff2102257d7ead9)、[bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

将固件元数据编码到网络缓冲区。

<a id="r_ga3c5de8cefc6a47805a9c1af166e956c7"></a>

```c
int bt_mesh_dfu_metadata_comp_hash_get (struct net_buf_simple *buf, uint8_t *key, uint32_t *hash)
```

相关声明：[bt_mesh_dfu_metadata_comp_hash_get](#ga3c5de8cefc6a47805a9c1af166e956c7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算组成数据（Composition Data）状态的哈希值（hash）。

<a id="r_gadc818fb83b429b0f1bef0ba83ae7a52a"></a>

```c
int bt_mesh_dfu_metadata_comp_hash_local_get (uint8_t *key, uint32_t *hash)
```

相关声明：[bt_mesh_dfu_metadata_comp_hash_local_get](#gadc818fb83b429b0f1bef0ba83ae7a52a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算本设备的组成数据第 0 页（Composition Data Page 0）的哈希值。

## 4.5\_详细说明（Detailed Documentation）

<a id="gaec5fa6e61a6ae88ac7a14f1ec09585b8"></a>

### `bt_mesh_dfu_metadata_fw_core_type`

```c
enum bt_mesh_dfu_metadata_fw_core_type
```

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

固件核心类型（firmware core type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_DFU_FW_CORE_TYPE_APP` | 应用处理器内核（Application Core）。 |
| `BT_MESH_DFU_FW_CORE_TYPE_NETWORK` | 网络处理器内核（Network Core）。 |
| `BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB` | 应用专用二进制大对象（Application-specific BLOB）。 |

<a id="ga3c5de8cefc6a47805a9c1af166e956c7"></a>

### `bt_mesh_dfu_metadata_comp_hash_get()`

```c
int bt_mesh_dfu_metadata_comp_hash_get ( struct net_buf_simple * buf, uint8_t * key, uint32_t * hash )
```

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

计算组成数据（Composition Data）状态的哈希值（hash）。

组合数据（Composition Data）的格式定义见 MshPRTv1.1 第 4.2.2.1 节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向存放组合数据（Composition Data）的缓冲区的指针。 |
| `key` | 用于哈希计算（Hash Computation）的 128 位密钥。 |
| `hash` | 指向用于保存哈希值的内存位置的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="gadc818fb83b429b0f1bef0ba83ae7a52a"></a>

### `bt_mesh_dfu_metadata_comp_hash_local_get()`

```c
int bt_mesh_dfu_metadata_comp_hash_local_get ( uint8_t * key, uint32_t * hash )
```

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

计算本设备的组成数据第 0 页（Composition Data Page 0）的哈希值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key` | 用于哈希计算（Hash Computation）的 128 位密钥。 |
| `hash` | 指向用于保存哈希值的内存位置的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga7f9ab277a7a47ad9cd8e616d3aa810d4"></a>

### `bt_mesh_dfu_metadata_decode()`

```c
int bt_mesh_dfu_metadata_decode ( struct net_buf_simple * buf, struct bt_mesh_dfu_metadata * metadata )
```

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

从网络缓冲区（network buffer）中解码固件元数据（firmware metadata）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含待解码原始元数据（Raw Metadata）的缓冲区。 |
| `metadata` | 指向待填充的元数据结构体的指针。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ga94de2f3730f600d58ff2102257d7ead9"></a>

### `bt_mesh_dfu_metadata_encode()`

```c
int bt_mesh_dfu_metadata_encode ( const struct bt_mesh_dfu_metadata * metadata, struct net_buf_simple * buf )
```

```c
#include <zephyr/bluetooth/mesh/dfu_metadata.h>
```

将固件元数据编码到网络缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `metadata` | 待编码的固件元数据（Firmware Metadata）。 |
| `buf` | 用于保存编码后元数据的缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。


## 4.6\_原页交叉引用（Cross References）

- [dfu_metadata.h](../api_file_interface_reference/P010_zephyr__bluetooth__mesh__dfu_metadata.h_文件参考.md)
- [bt_mesh_dfu_metadata_fw_ver](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)
- [bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0"></a>
<a id="ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692"></a>
<a id="ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_蓝牙 HCI 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P005_健康服务器模型（Health Server Model）.md)
