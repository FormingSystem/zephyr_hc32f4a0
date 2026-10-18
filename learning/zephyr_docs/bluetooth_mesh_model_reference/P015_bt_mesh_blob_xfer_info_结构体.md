---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-15
title: bt_mesh_blob_xfer_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__xfer__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_bt\_mesh\_blob\_xfer\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__xfer__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

二进制大对象传输（BLOB Transfer）的信息。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

二进制大对象传输信息（BLOB transfer information）。若 `phase` 为 `BT_MESH_BLOB_XFER_PHASE_INACTIVE`，则 `phase` 后面的字段未初始化。若 `phase` 为 `BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START`，则 `id` 后面的字段未初始化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 15.1\_数据成员（Data Fields）

<a id="r_aaeda1f5688bfb3cc3708e3797f3190a5"></a>

```c
enum bt_mesh_blob_status status
```

相关声明：[bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)、[status](#aaeda1f5688bfb3cc3708e3797f3190a5)。

二进制大对象传输状态（BLOB transfer status）。

<a id="r_a6cbb21582332cb23125624db5a02731a"></a>

```c
enum bt_mesh_blob_xfer_mode mode
```

相关声明：[bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)、[mode](#a6cbb21582332cb23125624db5a02731a)。

二进制大对象传输模式（BLOB transfer mode）。

<a id="r_a6a8686872018ceb6e4e9fc52eaff5b9e"></a>

```c
enum bt_mesh_blob_xfer_phase phase
```

相关声明：[bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)、[phase](#a6a8686872018ceb6e4e9fc52eaff5b9e)。

二进制大对象传输阶段（BLOB transfer phase）。

<a id="r_a3a19a5f387b53dd32429c9e76e53a87f"></a>

```c
uint64_t id
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[id](#a3a19a5f387b53dd32429c9e76e53a87f)。

二进制大对象标识符（BLOB ID）。

<a id="r_ac03d3ad7a618ee67f9bd7f1d52019cb7"></a>

```c
uint32_t size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[size](#ac03d3ad7a618ee67f9bd7f1d52019cb7)。

二进制大对象大小（BLOB size），以八位组（Octets）为单位。

<a id="r_ad09a0e80202b4953788fcade5788f0ef"></a>

```c
uint8_t block_size_log
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[block_size_log](#ad09a0e80202b4953788fcade5788f0ef)。

块大小的对数表示（Logarithmic representation of block size）。

<a id="r_ae24ed28faaef6187850cb0f04da2b8c7"></a>

```c
uint16_t mtu_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu_size](#ae24ed28faaef6187850cb0f04da2b8c7)。

最大传输单元大小（MTU size），以八位组（Octets）为单位。

<a id="r_a8825fba3258805db956b099ddfa19f9f"></a>

```c
const uint8_t * missing_blocks
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[missing_blocks](#a8825fba3258805db956b099ddfa19f9f)。

指示未收到哪些块的位域（Bit field）。

## 15.2\_详细说明（Detailed Documentation）

<a id="ad09a0e80202b4953788fcade5788f0ef"></a>

### `block_size_log`

```c
uint8_t bt_mesh_blob_xfer_info::block_size_log
```

块大小的对数表示（Logarithmic representation of block size）。

<a id="a3a19a5f387b53dd32429c9e76e53a87f"></a>

### `id`

```c
uint64_t bt_mesh_blob_xfer_info::id
```

二进制大对象标识符（BLOB ID）。

<a id="a8825fba3258805db956b099ddfa19f9f"></a>

### `missing_blocks`

```c
const uint8_t* bt_mesh_blob_xfer_info::missing_blocks
```

指示未收到哪些块的位域（Bit field）。

<a id="a6cbb21582332cb23125624db5a02731a"></a>

### `mode`

```c
enum bt_mesh_blob_xfer_mode bt_mesh_blob_xfer_info::mode
```

二进制大对象传输模式（BLOB transfer mode）。

<a id="ae24ed28faaef6187850cb0f04da2b8c7"></a>

### `mtu_size`

```c
uint16_t bt_mesh_blob_xfer_info::mtu_size
```

最大传输单元大小（MTU size），以八位组（Octets）为单位。

<a id="a6a8686872018ceb6e4e9fc52eaff5b9e"></a>

### `phase`

```c
enum bt_mesh_blob_xfer_phase bt_mesh_blob_xfer_info::phase
```

二进制大对象传输阶段（BLOB transfer phase）。

<a id="ac03d3ad7a618ee67f9bd7f1d52019cb7"></a>

### `size`

```c
uint32_t bt_mesh_blob_xfer_info::size
```

二进制大对象大小（BLOB size），以八位组（Octets）为单位。

<a id="aaeda1f5688bfb3cc3708e3797f3190a5"></a>

### `status`

```c
enum bt_mesh_blob_status bt_mesh_blob_xfer_info::status
```

二进制大对象传输状态（BLOB transfer status）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 15.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_MESH_BLOB_XFER_PHASE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P014_bt_mesh_blob_xfer_结构体.md) · [返回大纲](大纲.md) · [下一章](P016_bt_mesh_brg_cfg_cli_结构体.md)
