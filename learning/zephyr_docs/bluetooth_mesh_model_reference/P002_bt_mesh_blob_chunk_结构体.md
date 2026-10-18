---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-2
title: bt_mesh_blob_chunk_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__chunk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_bt\_mesh\_blob\_chunk\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__chunk.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象（BLOB）的数据分片（Chunk）。

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

<a id="details"></a>

二进制大对象（BLOB）的数据分片（Chunk）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_aabd55d7c8acf726cbc3470af55cb6bc5"></a>

```c
off_t offset
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[offset](#aabd55d7c8acf726cbc3470af55cb6bc5)。

分片数据相对于块起始位置的偏移量（Chunk data offset）。

<a id="r_afd2be87f4cd91f29eb24ebd0dfd9bccb"></a>

```c
size_t size
```

相关声明：[size](#afd2be87f4cd91f29eb24ebd0dfd9bccb)。

分片数据大小（Chunk data size）。

<a id="r_ad6f5ff266346af1ab0ba29f5339cb83f"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad6f5ff266346af1ab0ba29f5339cb83f)。

分片数据（Chunk data）。

## 2.2\_详细说明（Detailed Documentation）

<a id="ad6f5ff266346af1ab0ba29f5339cb83f"></a>

### `data`

```c
uint8_t* bt_mesh_blob_chunk::data
```

分片数据（Chunk data）。

<a id="aabd55d7c8acf726cbc3470af55cb6bc5"></a>

### `offset`

```c
off_t bt_mesh_blob_chunk::offset
```

分片数据相对于块起始位置的偏移量（Chunk data offset）。

<a id="afd2be87f4cd91f29eb24ebd0dfd9bccb"></a>

### `size`

```c
size_t bt_mesh_blob_chunk::size
```

分片数据大小（Chunk data size）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_bt_mesh_blob_block_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_bt_mesh_blob_cli_结构体.md)
