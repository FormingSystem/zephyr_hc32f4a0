---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-4
title: bt_mesh_blob_cli_caps_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__caps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_bt\_mesh\_blob\_cli\_caps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli__caps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

目标节点（Target Node）的传输能力。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

目标节点（Target Node）的传输能力。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_ae16411b1a36854d6f638a2bca1dc4c3b"></a>

```c
size_t max_size
```

相关声明：[max_size](#ae16411b1a36854d6f638a2bca1dc4c3b)。

二进制大对象最大大小（Max BLOB size）。

<a id="r_ac446317efdeca9edbb7df924d4e5a995"></a>

```c
uint8_t min_block_size_log
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_block_size_log](#ac446317efdeca9edbb7df924d4e5a995)。

最小块大小的对数表示（Logarithmic representation of minimum block size）。

<a id="r_a5d44b3b9bf7e47af2e6ba930b2826b15"></a>

```c
uint8_t max_block_size_log
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_block_size_log](#a5d44b3b9bf7e47af2e6ba930b2826b15)。

最大块大小的对数表示（Logarithmic representation of maximum block size）。

<a id="r_a318c96b89597dfdf9b68fbc8b999af11"></a>

```c
uint16_t max_chunks
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_chunks](#a318c96b89597dfdf9b68fbc8b999af11)。

每块最多包含的分片数（Max chunks per block）。

<a id="r_ad149164240e7c20a57a28c25109079df"></a>

```c
uint16_t max_chunk_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_chunk_size](#ad149164240e7c20a57a28c25109079df)。

最大分片大小（Max chunk size）。

<a id="r_a89d6e1bbc55086cee410835edd6baf3a"></a>

```c
uint16_t mtu_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu_size](#a89d6e1bbc55086cee410835edd6baf3a)。

最大传输单元的最大大小（Max MTU size）。

<a id="r_a1c848a3a2a2ece3764df5cbf6cbfec6b"></a>

```c
enum bt_mesh_blob_xfer_mode modes
```

相关声明：[bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)、[modes](#a1c848a3a2a2ece3764df5cbf6cbfec6b)。

支持的传输模式（Supported transfer modes）。

## 4.2\_详细说明（Detailed Documentation）

<a id="a5d44b3b9bf7e47af2e6ba930b2826b15"></a>

### `max_block_size_log`

```c
uint8_t bt_mesh_blob_cli_caps::max_block_size_log
```

最大块大小的对数表示（Logarithmic representation of maximum block size）。

<a id="ad149164240e7c20a57a28c25109079df"></a>

### `max_chunk_size`

```c
uint16_t bt_mesh_blob_cli_caps::max_chunk_size
```

最大分片大小（Max chunk size）。

<a id="a318c96b89597dfdf9b68fbc8b999af11"></a>

### `max_chunks`

```c
uint16_t bt_mesh_blob_cli_caps::max_chunks
```

每块最多包含的分片数（Max chunks per block）。

<a id="ae16411b1a36854d6f638a2bca1dc4c3b"></a>

### `max_size`

```c
size_t bt_mesh_blob_cli_caps::max_size
```

二进制大对象最大大小（Max BLOB size）。

<a id="ac446317efdeca9edbb7df924d4e5a995"></a>

### `min_block_size_log`

```c
uint8_t bt_mesh_blob_cli_caps::min_block_size_log
```

最小块大小的对数表示（Logarithmic representation of minimum block size）。

<a id="a1c848a3a2a2ece3764df5cbf6cbfec6b"></a>

### `modes`

```c
enum bt_mesh_blob_xfer_mode bt_mesh_blob_cli_caps::modes
```

支持的传输模式（Supported transfer modes）。

<a id="a89d6e1bbc55086cee410835edd6baf3a"></a>

### `mtu_size`

```c
uint16_t bt_mesh_blob_cli_caps::mtu_size
```

最大传输单元的最大大小（Max MTU size）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_bt_mesh_blob_cli_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_bt_mesh_blob_cli_cb_结构体.md)
