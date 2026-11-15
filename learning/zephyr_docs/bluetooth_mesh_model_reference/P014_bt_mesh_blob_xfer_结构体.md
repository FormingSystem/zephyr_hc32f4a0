---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-14
title: bt_mesh_blob_xfer_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__xfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_bt\_mesh\_blob\_xfer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__xfer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象传输（BLOB Transfer）。

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

<a id="details"></a>

二进制大对象传输（BLOB Transfer）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a9b4f37addd1271e26ab90c6e63608867"></a>

```c
uint64_t id
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[id](#a9b4f37addd1271e26ab90c6e63608867)。

二进制大对象标识符（BLOB ID）。

<a id="r_a7a2ca36b08d1d55c2dfbca0120a5274d"></a>

```c
size_t size
```

相关声明：[size](#a7a2ca36b08d1d55c2dfbca0120a5274d)。

二进制大对象总大小（Total BLOB size），单位为字节。

<a id="r_a2c3d9365b5cb6e569d147acae7a74ed6"></a>

```c
enum bt_mesh_blob_xfer_mode mode
```

相关声明：[bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)、[mode](#a2c3d9365b5cb6e569d147acae7a74ed6)。

二进制大对象传输模式（BLOB transfer mode）。

<a id="r_aa971742f85ccd94bbdef6c61203caeba"></a>

```c
uint8_t block_size_log
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[block_size_log](#aa971742f85ccd94bbdef6c61203caeba)。

<a id="r_a646c5c56d5290f6c65e2b9fca89e9835"></a>

```c
uint16_t chunk_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_size](#a646c5c56d5290f6c65e2b9fca89e9835)。

基本分片大小（Base chunk size）。

## 14.2\_详细说明（Detailed Documentation）

<a id="aa971742f85ccd94bbdef6c61203caeba"></a>

### `block_size_log`

```c
uint8_t bt_mesh_blob_xfer::block_size_log
```

<a id="a646c5c56d5290f6c65e2b9fca89e9835"></a>

### `chunk_size`

```c
uint16_t bt_mesh_blob_xfer::chunk_size
```

基本分片大小（Base chunk size）。

最后一个分片（Chunk）可能更小。

<a id="a9b4f37addd1271e26ab90c6e63608867"></a>

### `id`

```c
uint64_t bt_mesh_blob_xfer::id
```

二进制大对象标识符（BLOB ID）。

<a id="a2c3d9365b5cb6e569d147acae7a74ed6"></a>

### `mode`

```c
enum bt_mesh_blob_xfer_mode bt_mesh_blob_xfer::mode
```

二进制大对象传输模式（BLOB transfer mode）。

<a id="a7a2ca36b08d1d55c2dfbca0120a5274d"></a>

### `size`

```c
size_t bt_mesh_blob_xfer::size
```

二进制大对象总大小（Total BLOB size），单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob.h`

## 14.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_bt_mesh_blob_target_pull_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_bt_mesh_blob_xfer_info_结构体.md)
