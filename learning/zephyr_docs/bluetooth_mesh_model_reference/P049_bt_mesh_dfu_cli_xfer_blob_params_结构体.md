---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-49
title: bt_mesh_dfu_cli_xfer_blob_params_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__xfer__blob__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_bt\_mesh\_dfu\_cli\_xfer\_blob\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli__xfer__blob__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新客户端（Firmware Update Client）传输所用的BLOB参数：

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

固件更新客户端（Firmware Update Client）传输所用的BLOB参数：

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 49.1\_数据成员（Data Fields）

<a id="r_a45452ae73f585ffba5c76291d41dd1ed"></a>

```c
uint8_t block_size_log
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[block_size_log](#a45452ae73f585ffba5c76291d41dd1ed)。

<a id="r_a1015b239306bd5eb1c9648b5c1d59481"></a>

```c
uint16_t chunk_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_size](#a1015b239306bd5eb1c9648b5c1d59481)。

基本分片大小（Base chunk size）。

## 49.2\_详细说明（Detailed Documentation）

<a id="a45452ae73f585ffba5c76291d41dd1ed"></a>

### `block_size_log`

```c
uint8_t bt_mesh_dfu_cli_xfer_blob_params::block_size_log
```

<a id="a1015b239306bd5eb1c9648b5c1d59481"></a>

### `chunk_size`

```c
uint16_t bt_mesh_dfu_cli_xfer_blob_params::chunk_size
```

基本分片大小（Base chunk size）。

最后一个分片（Chunk）可能更小。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 49.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P048_bt_mesh_dfu_cli_xfer_结构体.md) · [返回大纲](大纲.md) · [下一章](P050_bt_mesh_dfu_img_结构体.md)
