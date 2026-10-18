---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-44
title: bt_mesh_dfd_srv_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfd__srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_bt\_mesh\_dfd\_srv\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfd__srv.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件分发服务器（Firmware Distribution Server）的实例。

```c
#include <zephyr/bluetooth/mesh/dfd_srv.h>
```

<a id="details"></a>

固件分发服务器（Firmware Distribution Server）的实例。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a7edbfa6bedb887a941b7567b9eeac8fd"></a>

```c
const struct bt_mesh_dfd_srv_cb * cb
```

相关声明：[bt_mesh_dfd_srv_cb](P045_bt_mesh_dfd_srv_cb_结构体.md)、[cb](#a7edbfa6bedb887a941b7567b9eeac8fd)。

<a id="r_a20bce6a528c1ef8433f55e8a4277a0ca"></a>

```c
const struct bt_mesh_model * mod
```

相关声明：[bt_mesh_model](P075_bt_mesh_model_结构体.md)、[mod](#a20bce6a528c1ef8433f55e8a4277a0ca)。

<a id="r_a1d022e6e15350cd85999f0b07e34f519"></a>

```c
struct bt_mesh_dfu_cli dfu
```

相关声明：[bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)、[dfu](#a1d022e6e15350cd85999f0b07e34f519)。

<a id="r_abde92a8837d687ef213836d593bf979d"></a>

```c
struct bt_mesh_dfu_target targets [0]
```

相关声明：[bt_mesh_dfu_target](P057_bt_mesh_dfu_target_结构体.md)、[targets](#abde92a8837d687ef213836d593bf979d)。

<a id="r_a1345da3143b1d3334a55ad8053967bf9"></a>

```c
struct bt_mesh_blob_target_pull pull_ctxs [0]
```

相关声明：[bt_mesh_blob_target_pull](P013_bt_mesh_blob_target_pull_结构体.md)、[pull_ctxs](#a1345da3143b1d3334a55ad8053967bf9)。

<a id="r_a691eb383f51fd6e10b615ab8921005de"></a>

```c
const struct bt_mesh_blob_io * io
```

相关声明：[bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)、[io](#a691eb383f51fd6e10b615ab8921005de)。

<a id="r_a67e4997a4367d9547a0ae9ff6c2017d6"></a>

```c
uint16_t target_cnt
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[target_cnt](#a67e4997a4367d9547a0ae9ff6c2017d6)。

<a id="r_af61665ebb2f46bd3e6277c6ee95ff68c"></a>

```c
uint16_t slot_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[slot_idx](#af61665ebb2f46bd3e6277c6ee95ff68c)。

<a id="r_af1ac88ae8d9e1e42ff8a98d3969c359d"></a>

```c
bool apply
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[apply](#af1ac88ae8d9e1e42ff8a98d3969c359d)。

<a id="r_a4a7847580637713b305918c77210e3c0"></a>

```c
enum bt_mesh_dfd_phase phase
```

相关声明：[bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)、[phase](#a4a7847580637713b305918c77210e3c0)。

<a id="r_a4e28f0e0845d1aeb6ebc03032ecfe813"></a>

```c
struct bt_mesh_blob_cli_inputs inputs
```

相关声明：[bt_mesh_blob_cli_inputs](P006_bt_mesh_blob_cli_inputs_结构体.md)、[inputs](#a4e28f0e0845d1aeb6ebc03032ecfe813)。

```c
struct {
```

<a id="r_a4ec05721598f01e6dd9a070a21be14b3"></a>

```c
enum bt_mesh_dfd_upload_phase phase
```

相关声明：[bt_mesh_dfd_upload_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ga1cce8331a0876c056b25175df32188fb)、[phase](#aa71e5affa0bf002499f3176794c6d9ca)。

<a id="r_ae97cdc6d3be1c513754d7f15b4f410a5"></a>

```c
struct bt_mesh_dfu_slot * slot
```

相关声明：[bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)、[slot](#a02b5ed65738bf08715bbc6a177c6f1ce)。

<a id="r_a7eee2a737298650178bb3fd2f51091ad"></a>

```c
const struct flash_area * area
```

相关声明：[flash_area](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)、[area](#a52b10a938105d0fb22e72e30fc92df5c)。

<a id="r_a1f6969a51c545c4edde135be1ae740d4"></a>

```c
struct bt_mesh_blob_srv blob
```

相关声明：[bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)、[blob](#ab538079d9f6b98f0de65583d6bdfe7f0)。

<a id="r_a26e4b13a8688f26c3330a2b0948bfc8d"></a>

```c
} upload
```

相关声明：[upload](#a26e4b13a8688f26c3330a2b0948bfc8d)。

## 44.2\_详细说明（Detailed Documentation）

<a id="af1ac88ae8d9e1e42ff8a98d3969c359d"></a>

### `apply`

```c
bool bt_mesh_dfd_srv::apply
```

<a id="a52b10a938105d0fb22e72e30fc92df5c"></a>

### `area`

```c
const struct flash_area* bt_mesh_dfd_srv::area
```

<a id="ab538079d9f6b98f0de65583d6bdfe7f0"></a>

### `blob`

```c
struct bt_mesh_blob_srv bt_mesh_dfd_srv::blob
```

<a id="a7edbfa6bedb887a941b7567b9eeac8fd"></a>

### `cb`

```c
const struct bt_mesh_dfd_srv_cb* bt_mesh_dfd_srv::cb
```

<a id="a1d022e6e15350cd85999f0b07e34f519"></a>

### `dfu`

```c
struct bt_mesh_dfu_cli bt_mesh_dfd_srv::dfu
```

<a id="a4e28f0e0845d1aeb6ebc03032ecfe813"></a>

### `inputs`

```c
struct bt_mesh_blob_cli_inputs bt_mesh_dfd_srv::inputs
```

<a id="a691eb383f51fd6e10b615ab8921005de"></a>

### `io`

```c
const struct bt_mesh_blob_io* bt_mesh_dfd_srv::io
```

<a id="a20bce6a528c1ef8433f55e8a4277a0ca"></a>

### `mod`

```c
const struct bt_mesh_model* bt_mesh_dfd_srv::mod
```

<a id="aa71e5affa0bf002499f3176794c6d9ca"></a>

### `phase [1/2]`

```c
enum bt_mesh_dfd_upload_phase bt_mesh_dfd_srv::phase
```

<a id="a4a7847580637713b305918c77210e3c0"></a>

### `phase [2/2]`

```c
enum bt_mesh_dfd_phase bt_mesh_dfd_srv::phase
```

<a id="a1345da3143b1d3334a55ad8053967bf9"></a>

### `pull_ctxs`

```c
struct bt_mesh_blob_target_pull bt_mesh_dfd_srv::pull_ctxs[0]
```

<a id="a02b5ed65738bf08715bbc6a177c6f1ce"></a>

### `slot`

```c
struct bt_mesh_dfu_slot* bt_mesh_dfd_srv::slot
```

<a id="af61665ebb2f46bd3e6277c6ee95ff68c"></a>

### `slot_idx`

```c
uint16_t bt_mesh_dfd_srv::slot_idx
```

<a id="a67e4997a4367d9547a0ae9ff6c2017d6"></a>

### `target_cnt`

```c
uint16_t bt_mesh_dfd_srv::target_cnt
```

<a id="abde92a8837d687ef213836d593bf979d"></a>

### `targets`

```c
struct bt_mesh_dfu_target bt_mesh_dfd_srv::targets[0]
```

<a id="a26e4b13a8688f26c3330a2b0948bfc8d"></a>

### `[struct]`

```c
struct { ... } bt_mesh_dfd_srv::upload
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfd_srv.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfd_srv.h](https://docs.zephyrproject.org/latest/doxygen/html/dfd__srv_8h_source.html)
- [bt_mesh_dfd_srv_cb](P045_bt_mesh_dfd_srv_cb_结构体.md)
- [bt_mesh_model](P075_bt_mesh_model_结构体.md)
- [bt_mesh_dfu_cli](P046_bt_mesh_dfu_cli_结构体.md)
- [bt_mesh_dfu_target](P057_bt_mesh_dfu_target_结构体.md)
- [bt_mesh_blob_target_pull](P013_bt_mesh_blob_target_pull_结构体.md)
- [bt_mesh_blob_io](P007_bt_mesh_blob_io_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_mesh_dfd_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#gab6562d62668ebcdb146be35b909c30c2)
- [bt_mesh_blob_cli_inputs](P006_bt_mesh_blob_cli_inputs_结构体.md)
- [bt_mesh_dfd_upload_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd.html#ga1cce8331a0876c056b25175df32188fb)
- [bt_mesh_dfu_slot](P054_bt_mesh_dfu_slot_结构体.md)
- [flash_area](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)
- [bt_mesh_blob_srv](P009_bt_mesh_blob_srv_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_bt_mesh_dev_capabilities_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_bt_mesh_dfd_srv_cb_结构体.md)
