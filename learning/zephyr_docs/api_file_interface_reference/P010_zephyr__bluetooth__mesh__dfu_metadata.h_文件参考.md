---
id: learning.zephyr-docs.api-file-interface-reference.page-10
title: zephyr__bluetooth__mesh__dfu_metadata.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_bluetooth\_\_mesh\_\_dfu\_metadata.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dfu__metadata_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh设备固件更新（DFU）元数据API的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <sys/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

蓝牙Mesh设备固件更新（DFU）元数据API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

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

## 10.2\_枚举（Enumerations）

<a id="r_gaec5fa6e61a6ae88ac7a14f1ec09585b8"></a>

```c
enum bt_mesh_dfu_metadata_fw_core_type { BT_MESH_DFU_FW_CORE_TYPE_APP = (1UL << (0)) , BT_MESH_DFU_FW_CORE_TYPE_NETWORK = (1UL << (1)) , BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB = (1UL << (2)) }
```

相关声明：[bt_mesh_dfu_metadata_fw_core_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gaec5fa6e61a6ae88ac7a14f1ec09585b8)、[BT_MESH_DFU_FW_CORE_TYPE_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0)、[BT_MESH_DFU_FW_CORE_TYPE_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692)、[BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2)。

固件核心类型（firmware core type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_ga7f9ab277a7a47ad9cd8e616d3aa810d4"></a>

```c
int bt_mesh_dfu_metadata_decode (struct net_buf_simple *buf, struct bt_mesh_dfu_metadata *metadata)
```

相关声明：[bt_mesh_dfu_metadata_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga7f9ab277a7a47ad9cd8e616d3aa810d4)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)。

从网络缓冲区（network buffer）中解码固件元数据（firmware metadata）。

<a id="r_ga94de2f3730f600d58ff2102257d7ead9"></a>

```c
int bt_mesh_dfu_metadata_encode (const struct bt_mesh_dfu_metadata *metadata, struct net_buf_simple *buf)
```

相关声明：[bt_mesh_dfu_metadata_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga94de2f3730f600d58ff2102257d7ead9)、[bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

将固件元数据编码到网络缓冲区。

<a id="r_ga3c5de8cefc6a47805a9c1af166e956c7"></a>

```c
int bt_mesh_dfu_metadata_comp_hash_get (struct net_buf_simple *buf, uint8_t *key, uint32_t *hash)
```

相关声明：[bt_mesh_dfu_metadata_comp_hash_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga3c5de8cefc6a47805a9c1af166e956c7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算组成数据（Composition Data）状态的哈希值（hash）。

<a id="r_gadc818fb83b429b0f1bef0ba83ae7a52a"></a>

```c
int bt_mesh_dfu_metadata_comp_hash_local_get (uint8_t *key, uint32_t *hash)
```

相关声明：[bt_mesh_dfu_metadata_comp_hash_local_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gadc818fb83b429b0f1bef0ba83ae7a52a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算本设备的组成数据第 0 页（Composition Data Page 0）的哈希值。


## 10.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P127_dfu_metadata.h_源码浏览.md)
- [bt_mesh_dfu_metadata_fw_ver](../bluetooth_mesh_model_reference/P052_bt_mesh_dfu_metadata_fw_ver_结构体.md)
- [bt_mesh_dfu_metadata](../bluetooth_mesh_model_reference/P051_bt_mesh_dfu_metadata_结构体.md)
- [bt_mesh_dfu_metadata_fw_core_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gaec5fa6e61a6ae88ac7a14f1ec09585b8)
- [BT_MESH_DFU_FW_CORE_TYPE_APP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8ab2025499295ce1ed1d8669c954a7b5a0)
- [BT_MESH_DFU_FW_CORE_TYPE_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8a791a8cbc2942ede20174cfc31408f692)
- [BT_MESH_DFU_FW_CORE_TYPE_APP_SPECIFIC_BLOB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ggaec5fa6e61a6ae88ac7a14f1ec09585b8aaf99e24ebcc4d00e4096bf377b441af2)
- [bt_mesh_dfu_metadata_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga7f9ab277a7a47ad9cd8e616d3aa810d4)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [bt_mesh_dfu_metadata_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga94de2f3730f600d58ff2102257d7ead9)
- [bt_mesh_dfu_metadata_comp_hash_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#ga3c5de8cefc6a47805a9c1af166e956c7)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_dfu_metadata_comp_hash_local_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__metadata.html#gadc818fb83b429b0f1bef0ba83ae7a52a)

<a id="header-details"></a>

---

[上一章](P009_zephyr__net__coap_oscore.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__dma__dma_mcux_smartdma.h_文件参考.md)
