---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-46
title: bt_mesh_dfu_cli_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_bt\_mesh\_dfu\_cli\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__cli.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件更新客户端（Firmware Update Client）的模型实例。

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

固件更新客户端模型实例（Firmware Update Client model instance）。应使用 `BT_MESH_DFU_CLI_INIT` 初始化。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a18d31020aba939826aa34060a4a28121"></a>

```c
const struct bt_mesh_dfu_cli_cb * cb
```

相关声明：[bt_mesh_dfu_cli_cb](P047_bt_mesh_dfu_cli_cb_结构体.md)、[cb](#a18d31020aba939826aa34060a4a28121)。

回调结构体（Callback Structure）。

<a id="r_a945b5c9f70086ca57d3ee77704ece6fd"></a>

```c
struct bt_mesh_blob_cli blob
```

相关声明：[bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)、[blob](#a945b5c9f70086ca57d3ee77704ece6fd)。

底层二进制大对象传输客户端（BLOB Transfer Client）。

<a id="r_a94924c2ad2654a14b23a07ea0351ec1b"></a>

```c
uint32_t op
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[op](#a94924c2ad2654a14b23a07ea0351ec1b)。

<a id="r_ab882e681b4bfc66374503c83237f57dd"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#ab882e681b4bfc66374503c83237f57dd)。

```c
struct {
```

<a id="r_af6dd79ffdfe9386054cd54194e3448ac"></a>

```c
const struct bt_mesh_dfu_slot * slot
```

相关声明：[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)、[slot](#a9396bb9e1245ab2613e3f7dfd753e793)。

<a id="r_a568f0069580d2bce4f2eda784b6aa717"></a>

```c
const struct bt_mesh_blob_io * io
```

相关声明：[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[io](#a29a8240e5d47abaabf9d356bcdcba48d)。

<a id="r_a9ddd90a74ba23bc7458cd522bedca89e"></a>

```c
struct bt_mesh_blob_xfer blob
```

相关声明：[bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)、[blob](#a1848081925dce6ac2083ce5eb8fb0b33)。

<a id="r_ad103552a76c749d2debfb8ffb619c639"></a>

```c
uint8_t state
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[state](#aeaf4f0114a6a47ec6d866ce7b6714d47)。

<a id="r_a86bcd2785fe6b39ccf17f7822f17ac77"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#a3e5d177198a4c57ccd98a53c20490c89)。

<a id="r_a9a8676e704a0346e1030f93d7ab6213c"></a>

```c
} xfer
```

相关声明：[xfer](#a9a8676e704a0346e1030f93d7ab6213c)。

```c
struct {
```

<a id="r_ae80e4a0d9a9a2369b892170e9e9f1fad"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#a463a5c12df5ba3041c46c5c008d473da)。

<a id="r_a09e9874d769fd08f7c6d6c6268ad63f2"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a40b6dfe0c3dc545afc30cd18c5b498b2)。

<a id="r_aff91645a754bca79df3ae65e4814f88d"></a>

```c
uint8_t img_cnt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[img_cnt](#aa6f7be1a8dcd76f519e934654f96c909)。

<a id="r_a225836e940e64867ce630cc98c95694d"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a67450510328c50e52fa97c80903508cd)。

<a id="r_a6a5297a5a67c1294580608949b4d2863"></a>

```c
struct k_sem sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sem](#af7ec498fa49b8e5cc0a3d67ad8dedee5)。

<a id="r_a70ac956b2fbace317ce4ff522e509faa"></a>

```c
void * params
```

相关声明：[params](#ad6cc63e09b15d8471fde2192977be2ed)。

<a id="r_a1d57bdbabb515488c537e22ae93619b7"></a>

```c
bt_mesh_dfu_img_cb_t img_cb
```

相关声明：[bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)、[img_cb](#a9531713e4659188de31015b66dfc38bc)。

<a id="r_a8f5d37bda72f1a112428958404ddce63"></a>

```c
} req
```

相关声明：[req](#a8f5d37bda72f1a112428958404ddce63)。

## 46.2\_详细说明（Detailed Documentation）

<a id="a67450510328c50e52fa97c80903508cd"></a>

### `addr`

```c
uint16_t bt_mesh_dfu_cli::addr
```

<a id="a1848081925dce6ac2083ce5eb8fb0b33"></a>

### `blob [1/2]`

```c
struct bt_mesh_blob_xfer bt_mesh_dfu_cli::blob
```

<a id="a945b5c9f70086ca57d3ee77704ece6fd"></a>

### `blob [2/2]`

```c
struct bt_mesh_blob_cli bt_mesh_dfu_cli::blob
```

底层二进制大对象传输客户端（BLOB Transfer Client）。

<a id="a18d31020aba939826aa34060a4a28121"></a>

### `cb`

```c
const struct bt_mesh_dfu_cli_cb* bt_mesh_dfu_cli::cb
```

回调结构体（Callback Structure）。

<a id="a3e5d177198a4c57ccd98a53c20490c89"></a>

### `flags`

```c
uint8_t bt_mesh_dfu_cli::flags
```

<a id="a9531713e4659188de31015b66dfc38bc"></a>

### `img_cb`

```c
bt_mesh_dfu_img_cb_t bt_mesh_dfu_cli::img_cb
```

<a id="aa6f7be1a8dcd76f519e934654f96c909"></a>

### `img_cnt`

```c
uint8_t bt_mesh_dfu_cli::img_cnt
```

<a id="a29a8240e5d47abaabf9d356bcdcba48d"></a>

### `io`

```c
const struct bt_mesh_blob_io* bt_mesh_dfu_cli::io
```

<a id="ab882e681b4bfc66374503c83237f57dd"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_dfu_cli::mod
```

<a id="a94924c2ad2654a14b23a07ea0351ec1b"></a>

### `op`

```c
uint32_t bt_mesh_dfu_cli::op
```

<a id="ad6cc63e09b15d8471fde2192977be2ed"></a>

### `params`

```c
void* bt_mesh_dfu_cli::params
```

<a id="a8f5d37bda72f1a112428958404ddce63"></a>

### `[struct]`

```c
struct { ... } bt_mesh_dfu_cli::req
```

<a id="af7ec498fa49b8e5cc0a3d67ad8dedee5"></a>

### `sem`

```c
struct k_sem bt_mesh_dfu_cli::sem
```

<a id="a9396bb9e1245ab2613e3f7dfd753e793"></a>

### `slot`

```c
const struct bt_mesh_dfu_slot* bt_mesh_dfu_cli::slot
```

<a id="aeaf4f0114a6a47ec6d866ce7b6714d47"></a>

### `state`

```c
uint8_t bt_mesh_dfu_cli::state
```

<a id="a463a5c12df5ba3041c46c5c008d473da"></a>

### `ttl`

```c
uint8_t bt_mesh_dfu_cli::ttl
```

<a id="a40b6dfe0c3dc545afc30cd18c5b498b2"></a>

### `type`

```c
uint8_t bt_mesh_dfu_cli::type
```

<a id="a9a8676e704a0346e1030f93d7ab6213c"></a>

### `[struct]`

```c
struct { ... } bt_mesh_dfu_cli::xfer
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [bt_mesh_dfu_cli_cb](P047_bt_mesh_dfu_cli_cb_结构体.md)
- [bt_mesh_blob_cli](P003_bt_mesh_blob_cli_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [bt_mesh_blob_xfer](P014_bt_mesh_blob_xfer_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [bt_mesh_dfu_img_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga2967b89e8fc3b848b70e493f6e821761)
- [BT_MESH_DFU_CLI_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu__cli.html#ga0b10a95f9b7c806bfd8649280f535c96)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_bt_mesh_dfd_srv_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_bt_mesh_dfu_cli_cb_结构体.md)
