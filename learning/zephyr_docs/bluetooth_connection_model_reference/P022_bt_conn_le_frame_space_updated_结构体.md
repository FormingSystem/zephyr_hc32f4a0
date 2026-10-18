---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-22
title: bt_conn_le_frame_space_updated_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__frame__space__updated.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_bt\_conn\_le\_frame\_space\_updated\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__conn__le__frame__space__updated.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

帧间隔更新完成回调的参数。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

帧间隔更新完成回调的参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 22.1\_数据成员（Data Fields）

<a id="r_a126026dba0cb84ceaf10324212bbf3e0"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a126026dba0cb84ceaf10324212bbf3e0)。

低功耗帧间隔更新完成事件（LE Frame Space Update Complete）的主机控制器接口状态（HCI Status）。

<a id="r_af6b88c108be375ea80466ece72257f2e"></a>

```c
enum bt_conn_le_frame_space_update_initiator initiator
```

相关声明：[bt_conn_le_frame_space_update_initiator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae60f156d2aa01814ad485786e00c4ca7)、[initiator](#af6b88c108be375ea80466ece72257f2e)。

帧间隔更新的发起方（Frame space update initiator）。

<a id="r_af1918fb7b4abc7f7b3eb11c33a3190f6"></a>

```c
uint16_t frame_space
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_space](#af1918fb7b4abc7f7b3eb11c33a3190f6)。

更新后的帧间隔（Frame space），单位为微秒。

<a id="r_a332a93e2d05750bd241e137381186f8b"></a>

```c
uint8_t phys
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phys](#a332a93e2d05750bd241e137381186f8b)。

已更新的物理层掩码（PHY mask）。

<a id="r_a7cb3366670e07d06a466c3c7eb885b09"></a>

```c
uint16_t spacing_types
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[spacing_types](#a7cb3366670e07d06a466c3c7eb885b09)。

已更新的间隔类型掩码（Spacing types mask）。

## 22.2\_详细说明（Detailed Documentation）

<a id="af1918fb7b4abc7f7b3eb11c33a3190f6"></a>

### `frame_space`

```c
uint16_t bt_conn_le_frame_space_updated::frame_space
```

更新后的帧间隔（Frame space），单位为微秒。

<a id="af6b88c108be375ea80466ece72257f2e"></a>

### `initiator`

```c
enum bt_conn_le_frame_space_update_initiator bt_conn_le_frame_space_updated::initiator
```

帧间隔更新的发起方（Frame space update initiator）。

<a id="a332a93e2d05750bd241e137381186f8b"></a>

### `phys`

```c
uint8_t bt_conn_le_frame_space_updated::phys
```

已更新的物理层掩码（PHY mask）。

取值参见 `BT_HCI_LE_FRAME_SPACE_UPDATE_PHY_*`。

<a id="a7cb3366670e07d06a466c3c7eb885b09"></a>

### `spacing_types`

```c
uint16_t bt_conn_le_frame_space_updated::spacing_types
```

已更新的间隔类型掩码（Spacing types mask）。

取值参见 `BT_HCI_LE_FRAME_SPACE_UPDATE_SPACING_TYPE_*` 和 `BT_CONN_LE_FRAME_SPACE_TYPES_MASK_*`。

<a id="a126026dba0cb84ceaf10324212bbf3e0"></a>

### `status`

```c
uint8_t bt_conn_le_frame_space_updated::status
```

低功耗帧间隔更新完成事件（LE Frame Space Update Complete）的主机控制器接口状态（HCI Status）。

若 `status` 不是 `BT_HCI_ERR_SUCCESS`，则其余参数无效。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 22.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn_le_frame_space_update_initiator](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gae60f156d2aa01814ad485786e00c4ca7)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [BT_HCI_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a27c890210eded48f159073cccef8582a)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P021_bt_conn_le_frame_space_update_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P023_bt_conn_le_info_结构体.md)
