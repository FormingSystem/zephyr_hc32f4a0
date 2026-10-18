---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-3
title: bt_mesh_blob_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_mesh\_blob\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__blob__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BLOB传输客户端（BLOB Transfer Client）的模型实例。

```c
#include <zephyr/bluetooth/mesh/blob_cli.h>
```

<a id="details"></a>

BLOB传输客户端（BLOB Transfer Client）的模型实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a6a0229165fe19af03a26e5cffa1e1486"></a>

```c
const struct bt_mesh_blob_cli_cb * cb
```

相关声明：[bt_mesh_blob_cli_cb](P005_bt_mesh_blob_cli_cb_结构体.md)、[cb](#a6a0229165fe19af03a26e5cffa1e1486)。

事件处理回调（Event handler callbacks）。

<a id="r_ada23952593d2a498ed421895828f461f"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#ada23952593d2a498ed421895828f461f)。

```c
struct {
```

<a id="r_ad08659054bf277ba3240684efd867128"></a>

```c
struct bt_mesh_blob_target * target
```

相关声明：[bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)、[target](#a519aa0aa7aa66ca67cdf813fee1632c3)。

<a id="r_aad091247d49076666b03bd03b1c7afd2"></a>

```c
struct blob_cli_broadcast_ctx ctx
```

相关声明：[ctx](#a850d232b04118d7564537dc6763a476c)。

<a id="r_a5a5696856e241a93aa7d9f6db4a84399"></a>

```c
struct k_work_delayable retry
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[retry](#add07e03f13b276fafabeb9cc4ba94d32)。

<a id="r_af5dad52d03790bcc5af632a8fda9d4d3"></a>

```c
int64_t cli_timestamp
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[cli_timestamp](#a850cc6f4426fec9dc9066953a1b992c8)。

<a id="r_a8228e2293007463f9d51a6f4bc99e379"></a>

```c
struct k_work_delayable complete
```

相关声明：[k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)、[complete](#a21b064cceace34605e42d5c295f12cd5)。

<a id="r_a3e4aa769d4d536f11bbe1c6374f50319"></a>

```c
uint16_t pending
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pending](#a1778ae8975ed4b9bc67616e5a0bdf3a9)。

<a id="r_aec62d2ad969938f376c6ae7c7243ddd6"></a>

```c
uint8_t retries
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[retries](#ab291086be3d9ecf03becd4200d783835)。

<a id="r_a6b936bd7d3d6d211dfc22ead7defc8e4"></a>

```c
uint8_t sending: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sending](#a85fdd17b04a06e880f20a0e2b1319ff0)。

<a id="r_a8a7fabe69df3b38d7c0cd80fed2e50c7"></a>

```c
uint8_t cancelled: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cancelled](#a6d70ac26b7fec22dfdc21f479d867ef7)。

<a id="r_a388183549ed5b1af0d2ac09263611a33"></a>

```c
} tx
```

相关声明：[tx](#a388183549ed5b1af0d2ac09263611a33)。

<a id="r_a49f0d79d76aaea785a5ad9160be40e8a"></a>

```c
const struct bt_mesh_blob_io * io
```

相关声明：[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[io](#a49f0d79d76aaea785a5ad9160be40e8a)。

<a id="r_aa6c79f5476f96a35c731b63723b2c6cc"></a>

```c
const struct bt_mesh_blob_cli_inputs * inputs
```

相关声明：[bt_mesh_blob_cli_inputs](P006_bt_mesh_blob_cli_inputs_结构体.md)、[inputs](#aa6c79f5476f96a35c731b63723b2c6cc)。

<a id="r_a9185cdadba15bce7b2bf2fcc6f85904a"></a>

```c
const struct bt_mesh_blob_xfer * xfer
```

相关声明：[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[xfer](#a9185cdadba15bce7b2bf2fcc6f85904a)。

<a id="r_a2ffd91b68c0aab92f16d9fb4eac79f9d"></a>

```c
uint32_t chunk_interval_ms
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[chunk_interval_ms](#a2ffd91b68c0aab92f16d9fb4eac79f9d)。

<a id="r_a645fdb1f0efb281b1faae4692a3404f1"></a>

```c
uint16_t block_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[block_count](#a645fdb1f0efb281b1faae4692a3404f1)。

<a id="r_aafaf644e30e10a8ad9ca6dc8b680eff6"></a>

```c
uint16_t chunk_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[chunk_idx](#aafaf644e30e10a8ad9ca6dc8b680eff6)。

<a id="r_aafe943fcada25f32b9a31b8d7586032a"></a>

```c
uint16_t mtu_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mtu_size](#aafe943fcada25f32b9a31b8d7586032a)。

<a id="r_ab131637681a0cf0b3ceebad015b28726"></a>

```c
enum bt_mesh_blob_cli_state state
```

相关声明：[bt_mesh_blob_cli_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac86db11f09e53adb2e012bf9e446d073)、[state](#ab131637681a0cf0b3ceebad015b28726)。

<a id="r_ac95970f7fd6b00fca284121394110250"></a>

```c
struct bt_mesh_blob_block block
```

相关声明：[bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)、[block](#ac95970f7fd6b00fca284121394110250)。

<a id="r_aa7713e6ad0183d18946646df7a5cb6ab"></a>

```c
struct bt_mesh_blob_cli_caps caps
```

相关声明：[bt_mesh_blob_cli_caps](P004_bt_mesh_blob_cli_caps_结构体.md)、[caps](#aa7713e6ad0183d18946646df7a5cb6ab)。

## 3.2\_详细说明（Detailed Documentation）

<a id="ac95970f7fd6b00fca284121394110250"></a>

### `block`

```c
struct bt_mesh_blob_block bt_mesh_blob_cli::block
```

<a id="a645fdb1f0efb281b1faae4692a3404f1"></a>

### `block_count`

```c
uint16_t bt_mesh_blob_cli::block_count
```

<a id="a6d70ac26b7fec22dfdc21f479d867ef7"></a>

### `cancelled`

```c
uint8_t bt_mesh_blob_cli::cancelled
```

<a id="aa7713e6ad0183d18946646df7a5cb6ab"></a>

### `caps`

```c
struct bt_mesh_blob_cli_caps bt_mesh_blob_cli::caps
```

<a id="a6a0229165fe19af03a26e5cffa1e1486"></a>

### `cb`

```c
const struct bt_mesh_blob_cli_cb* bt_mesh_blob_cli::cb
```

事件处理回调（Event handler callbacks）。

<a id="aafaf644e30e10a8ad9ca6dc8b680eff6"></a>

### `chunk_idx`

```c
uint16_t bt_mesh_blob_cli::chunk_idx
```

<a id="a2ffd91b68c0aab92f16d9fb4eac79f9d"></a>

### `chunk_interval_ms`

```c
uint32_t bt_mesh_blob_cli::chunk_interval_ms
```

<a id="a850cc6f4426fec9dc9066953a1b992c8"></a>

### `cli_timestamp`

```c
int64_t bt_mesh_blob_cli::cli_timestamp
```

<a id="a21b064cceace34605e42d5c295f12cd5"></a>

### `complete`

```c
struct k_work_delayable bt_mesh_blob_cli::complete
```

<a id="a850d232b04118d7564537dc6763a476c"></a>

### `ctx`

```c
struct blob_cli_broadcast_ctx bt_mesh_blob_cli::ctx
```

<a id="aa6c79f5476f96a35c731b63723b2c6cc"></a>

### `inputs`

```c
const struct bt_mesh_blob_cli_inputs* bt_mesh_blob_cli::inputs
```

<a id="a49f0d79d76aaea785a5ad9160be40e8a"></a>

### `io`

```c
const struct bt_mesh_blob_io* bt_mesh_blob_cli::io
```

<a id="ada23952593d2a498ed421895828f461f"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_blob_cli::mod
```

<a id="aafe943fcada25f32b9a31b8d7586032a"></a>

### `mtu_size`

```c
uint16_t bt_mesh_blob_cli::mtu_size
```

<a id="a1778ae8975ed4b9bc67616e5a0bdf3a9"></a>

### `pending`

```c
uint16_t bt_mesh_blob_cli::pending
```

<a id="ab291086be3d9ecf03becd4200d783835"></a>

### `retries`

```c
uint8_t bt_mesh_blob_cli::retries
```

<a id="add07e03f13b276fafabeb9cc4ba94d32"></a>

### `retry`

```c
struct k_work_delayable bt_mesh_blob_cli::retry
```

<a id="a85fdd17b04a06e880f20a0e2b1319ff0"></a>

### `sending`

```c
uint8_t bt_mesh_blob_cli::sending
```

<a id="ab131637681a0cf0b3ceebad015b28726"></a>

### `state`

```c
enum bt_mesh_blob_cli_state bt_mesh_blob_cli::state
```

<a id="a519aa0aa7aa66ca67cdf813fee1632c3"></a>

### `target`

```c
struct bt_mesh_blob_target* bt_mesh_blob_cli::target
```

<a id="a388183549ed5b1af0d2ac09263611a33"></a>

### `[struct]`

```c
struct { ... } bt_mesh_blob_cli::tx
```

<a id="a9185cdadba15bce7b2bf2fcc6f85904a"></a>

### `xfer`

```c
const struct bt_mesh_blob_xfer* bt_mesh_blob_cli::xfer
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/blob_cli.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/blob_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/blob__cli_8h_source.html)
- [bt_mesh_blob_cli_cb](P005_bt_mesh_blob_cli_cb_结构体.md)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_blob_target](P012_bt_mesh_blob_target_结构体.md)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_blob_cli_inputs](P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_blob_cli_state](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__cli.html#gac86db11f09e53adb2e012bf9e446d073)
- [bt_mesh_blob_block](P001_bt_mesh_blob_block_结构体.md)
- [bt_mesh_blob_cli_caps](P004_bt_mesh_blob_cli_caps_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_mesh_blob_chunk_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_mesh_blob_cli_caps_结构体.md)
