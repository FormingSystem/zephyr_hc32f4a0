---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-7
title: bt_mesh_blob_io_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bt\_mesh\_blob\_io\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__io.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象流（BLOB Stream）。

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

<a id="details"></a>

二进制大对象流（BLOB Stream）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a4666a3fafde0ee9fdd51d27732bec6bc"></a>

```c
int(* open )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, enum bt_mesh_blob_io_mode mode)
```

相关声明：[open](#a4666a3fafde0ee9fdd51d27732bec6bc)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)。

打开回调（Open callback）。

<a id="r_aac42902d0bbbef10a5e9cc35e8a3ea64"></a>

```c
void(* close )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer)
```

相关声明：[close](#aac42902d0bbbef10a5e9cc35e8a3ea64)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)。

关闭回调（Close callback）。

<a id="r_a900f049b6a778d9e0973ee66b46dc046"></a>

```c
int(* block_start )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block)
```

相关声明：[block_start](#a900f049b6a778d9e0973ee66b46dc046)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)。

块开始回调（Block start callback）。

<a id="r_a57381249bf63924b2345ece6e12909cb"></a>

```c
void(* block_end )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block)
```

相关声明：[block_end](#a57381249bf63924b2345ece6e12909cb)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)。

块结束回调（Block end callback）。

<a id="r_ae0b27ea814e5c939d708ae20d452ca09"></a>

```c
int(* wr )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block, const struct bt_mesh_blob_chunk *chunk)
```

相关声明：[wr](#ae0b27ea814e5c939d708ae20d452ca09)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)、[bt_mesh_blob_chunk](P002_bt_mesh_blob_chunk_结构体.md)。

分片数据写入回调（Chunk data write callback）。

<a id="r_a330ec5dcc8d18b84e7fdab9ef6d75f49"></a>

```c
int(* rd )(const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block, const struct bt_mesh_blob_chunk *chunk)
```

相关声明：[rd](#a330ec5dcc8d18b84e7fdab9ef6d75f49)、[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)、[bt_mesh_blob_chunk](P002_bt_mesh_blob_chunk_结构体.md)。

分片数据读取回调（Chunk data read callback）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a57381249bf63924b2345ece6e12909cb"></a>

### `block_end`

```c
void(* bt_mesh_blob_io::block_end) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block)
```

块结束回调（Block end callback）。

当前块（Block）全部发送完成时调用。此后不会再请求此块中的数据，可以丢弃与该块关联的应用数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |
| `block` | 已完成发送的块（Block）。 |

<a id="a900f049b6a778d9e0973ee66b46dc046"></a>

### `block_start`

```c
int(* bt_mesh_blob_io::block_start) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block)
```

块开始回调（Block start callback）。

打开一个新块（Block）以进行发送时调用。每个块只发送一次，且始终按递增顺序发送。单个块中的数据分片（Data chunks）可能被乱序请求，也可能被多次请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |
| `block` | 开始处理的块（Block）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="aac42902d0bbbef10a5e9cc35e8a3ea64"></a>

### `close`

```c
void(* bt_mesh_blob_io::close) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer)
```

关闭回调（Close callback）。

读取器（Reader）关闭时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |

<a id="a4666a3fafde0ee9fdd51d27732bec6bc"></a>

### `open`

```c
int(* bt_mesh_blob_io::open) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, enum bt_mesh_blob_io_mode mode)
```

打开回调（Open callback）。

读取器（Reader）打开并准备读取时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |
| `mode` | 流方向（Stream direction），即读取／写入（Read/write）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="a330ec5dcc8d18b84e7fdab9ef6d75f49"></a>

### `rd`

```c
int(* bt_mesh_blob_io::rd) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block, const struct bt_mesh_blob_chunk *chunk)
```

分片数据读取回调（Chunk data read callback）。

由二进制大对象传输客户端（BLOB Transfer Client）用于获取要发送的数据。

客户端（Client）调用分片数据请求回调（Chunk data request callback），填充即将发送给目标节点的分片消息。对于每个偏移位置，数据请求回调可能乱序调用，也可能调用多次，因此不能将其作为进度指示。

分片数据请求回调（Chunk data request callback）返回非零状态码会导致传输终止。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |
| `block` | 此分片（Chunk）所属的块（Block）。 |
| `chunk` | 要获取数据的分片（Chunk）。回调应填充 `data` 成员所指向的缓冲区。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

<a id="ae0b27ea814e5c939d708ae20d452ca09"></a>

### `wr`

```c
int(* bt_mesh_blob_io::wr) (const struct bt_mesh_blob_io *io, const struct bt_mesh_blob_xfer *xfer, const struct bt_mesh_blob_block *block, const struct bt_mesh_blob_chunk *chunk)
```

分片数据写入回调（Chunk data write callback）。

由二进制大对象传输服务器（BLOB Transfer Server）用于处理传入数据。

每个块（Block）被划分为若干数据分片（Chunks）。收到新分片时调用此回调；同一块中的分片可以按任意顺序到达。

若回调成功返回，此分片（Chunk）将被标记为已接收，此后不再接收，除非由于传输挂起（Transfer suspension）而重新开始该块。若回调返回非零值，分片仍保持未接收状态，二进制大对象传输客户端（BLOB Transfer Client）会在以后尝试重新发送。

注意，客户端（Client）尝试投递某个分片（Chunk）的次数有限；达到限制后，会将目标节点移出传输。客户端执行的重试次数由具体实现决定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `io` | 二进制大对象流（BLOB Stream）。 |
| `xfer` | 二进制大对象传输（BLOB Transfer）。 |
| `block` | 此分片（Chunk）所属的块（Block）。 |
| `chunk` | 接收到的分片（Received chunk）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，否则返回负错误码。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob.h](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)
- [bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)
- [bt_mesh_blob_chunk](P002_bt_mesh_blob_chunk_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_bt_mesh_blob_cli_inputs_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_bt_mesh_blob_io_flash_结构体.md)
