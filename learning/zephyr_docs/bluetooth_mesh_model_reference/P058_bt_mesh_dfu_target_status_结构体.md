---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-58
title: bt_mesh_dfu_target_status_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__target__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_bt\_mesh\_dfu\_target\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__dfu__target__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

设备固件更新（DFU）目标节点的状态参数。

```c
#include <zephyr/bluetooth/mesh/dfu_cli.h>
```

<a id="details"></a>

设备固件更新（DFU）目标节点的状态参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 58.1\_数据成员（Data Fields）

<a id="r_a25b2198ad4970d50707ff7994c9d1415"></a>

```c
enum bt_mesh_dfu_status status
```

相关声明：[bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)、[status](#a25b2198ad4970d50707ff7994c9d1415)。

前一次操作的状态（Status of previous operation）。

<a id="r_aedbbfc07a68e60236901a3c79377fe65"></a>

```c
enum bt_mesh_dfu_phase phase
```

相关声明：[bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)、[phase](#aedbbfc07a68e60236901a3c79377fe65)。

当前设备固件更新传输的阶段（DFU transfer phase）。

<a id="r_aef5cbadbdd7b4b006dc304cd94c1bca4"></a>

```c
enum bt_mesh_dfu_effect effect
```

相关声明：[bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)、[effect](#aef5cbadbdd7b4b006dc304cd94c1bca4)。

更新将对目标设备状态产生的影响（Update effect）。

<a id="r_a2848ad866fbd437164b73a7504b75518"></a>

```c
uint64_t blob_id
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[blob_id](#a2848ad866fbd437164b73a7504b75518)。

传输使用的二进制大对象标识符（BLOB ID）。

<a id="r_aedbd5c0a04460656d0a78eb49fd047b2"></a>

```c
uint8_t img_idx
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[img_idx](#aedbd5c0a04460656d0a78eb49fd047b2)。

要传输的镜像索引（Image index）。

<a id="r_ab2e77b63918bb9a735a4ab20a4ca9333"></a>

```c
uint8_t ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ttl](#ab2e77b63918bb9a735a4ab20a4ca9333)。

传输使用的生存时间（TTL）。

<a id="r_a13505201dbafeff54c0b35b445fd4f85"></a>

```c
uint16_t timeout_base
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timeout_base](#a13505201dbafeff54c0b35b445fd4f85)。

目标节点的额外响应时间（Additional response time），以 10 秒为增量。

## 58.2\_详细说明（Detailed Documentation）

<a id="a2848ad866fbd437164b73a7504b75518"></a>

### `blob_id`

```c
uint64_t bt_mesh_dfu_target_status::blob_id
```

传输使用的二进制大对象标识符（BLOB ID）。

<a id="aef5cbadbdd7b4b006dc304cd94c1bca4"></a>

### `effect`

```c
enum bt_mesh_dfu_effect bt_mesh_dfu_target_status::effect
```

更新将对目标设备状态产生的影响（Update effect）。

<a id="aedbd5c0a04460656d0a78eb49fd047b2"></a>

### `img_idx`

```c
uint8_t bt_mesh_dfu_target_status::img_idx
```

要传输的镜像索引（Image index）。

<a id="aedbbfc07a68e60236901a3c79377fe65"></a>

### `phase`

```c
enum bt_mesh_dfu_phase bt_mesh_dfu_target_status::phase
```

当前设备固件更新传输的阶段（DFU transfer phase）。

<a id="a25b2198ad4970d50707ff7994c9d1415"></a>

### `status`

```c
enum bt_mesh_dfu_status bt_mesh_dfu_target_status::status
```

前一次操作的状态（Status of previous operation）。

<a id="a13505201dbafeff54c0b35b445fd4f85"></a>

### `timeout_base`

```c
uint16_t bt_mesh_dfu_target_status::timeout_base
```

目标节点的额外响应时间（Additional response time），以 10 秒为增量。

额外时间可用于给目标节点（Target nodes）更多时间响应客户端（Client）的消息。实际超时值按以下公式计算：

原始示例（Example）：

```c
*  timeout = 20 seconds + (10 seconds * timeout_base) + (100 ms * TTL)
*
```

如果目标节点（Target node）未能在配置的传输超时内响应客户端（Client）的消息，则将其移出本次传输。

<a id="ab2e77b63918bb9a735a4ab20a4ca9333"></a>

### `ttl`

```c
uint8_t bt_mesh_dfu_target_status::ttl
```

传输使用的生存时间（TTL）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/dfu_cli.h`

## 58.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/dfu_cli.h](https://docs.zephyrproject.org/latest/doxygen/html/dfu__cli_8h_source.html)
- [bt_mesh_dfu_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga9e627a3c15de782faa11ef6c4ec5e05d)
- [bt_mesh_dfu_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#ga99919dcee1e41bc74bd59e33bec2ded2)
- [bt_mesh_dfu_effect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfu.html#gae7d7ef4ed1e65e5f8e1641a9c00bb7e8)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P057_bt_mesh_dfu_target_结构体.md) · [返回大纲](大纲.md) · [下一章](P059_bt_mesh_elem_结构体.md)
