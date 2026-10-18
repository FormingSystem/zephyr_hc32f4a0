---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-1
title: bt_mesh_blob_block_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__block.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_bt\_mesh\_blob\_block\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__block.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象（BLOB）传输的数据块（Block）。

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

<a id="details"></a>

二进制大对象（BLOB）传输的数据块（Block）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 1.1\_数据成员（Data Fields）

<a id="r_a67632460e4a37407074105f8ff3f97fd"></a>

```c
size_t size
```

相关声明：[size](#a67632460e4a37407074105f8ff3f97fd)。

块大小（Block size），单位为字节。

<a id="r_a7521b8121a2a1f280d14e9e222b7d6cf"></a>

```c
off_t offset
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[offset](#a7521b8121a2a1f280d14e9e222b7d6cf)。

相对于二进制大对象（BLOB）起始位置的偏移量，单位为字节。

<a id="r_a57f92c3b0ef68128d44a90802788dfa3"></a>

```c
uint16_t number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[number](#a57f92c3b0ef68128d44a90802788dfa3)。

块编号（Block number）。

<a id="r_a6bd9a432a789edeafc5d425232a32b4e"></a>

```c
uint16_t chunk_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_count](#a6bd9a432a789edeafc5d425232a32b4e)。

块中的分片数量（Number of chunks）。

<a id="r_ad7527108bd3e41a3965bff0ab3ee82b1"></a>

```c
uint8_t missing [(((0)+(8) - 1)/(8))]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[missing](#ad7527108bd3e41a3965bff0ab3ee82b1)。

缺失分片位图（Bitmap of missing chunks）。

## 1.2\_详细说明（Detailed Documentation）

<a id="a6bd9a432a789edeafc5d425232a32b4e"></a>

### `chunk_count`

```c
uint16_t bt_mesh_blob_block::chunk_count
```

块中的分片数量（Number of chunks）。

<a id="ad7527108bd3e41a3965bff0ab3ee82b1"></a>

### `missing`

```c
uint8_t bt_mesh_blob_block::missing[(((0)+(8) - 1)/(8))]
```

缺失分片位图（Bitmap of missing chunks）。

<a id="a57f92c3b0ef68128d44a90802788dfa3"></a>

### `number`

```c
uint16_t bt_mesh_blob_block::number
```

块编号（Block number）。

<a id="a7521b8121a2a1f280d14e9e222b7d6cf"></a>

### `offset`

```c
off_t bt_mesh_blob_block::offset
```

相对于二进制大对象（BLOB）起始位置的偏移量，单位为字节。

<a id="a67632460e4a37407074105f8ff3f97fd"></a>

### `size`

```c
size_t bt_mesh_blob_block::size
```

块大小（Block size），单位为字节。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob.h`

## 1.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_bt_mesh_blob_chunk_结构体.md)
