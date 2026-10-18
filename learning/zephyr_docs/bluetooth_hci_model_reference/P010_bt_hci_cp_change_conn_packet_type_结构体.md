---
id: learning.zephyr-docs.bluetooth-hci-model-reference.page-10
title: bt_hci_cp_change_conn_packet_type_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__change__conn__packet__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_bt\_hci\_cp\_change\_conn\_packet\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__hci__cp__change__conn__packet__type.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

主机控制器接口（Host Controller Interface，HCI）的更改连接包类型（Change Connection Packet Type）命令参数。

```c
#include <zephyr/bluetooth/hci_types.h>
```

<a id="details"></a>

主机控制器接口（Host Controller Interface，HCI）的更改连接包类型（Change Connection Packet Type）命令参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a082e5dae5f08a332cf6a1dd23917d87f"></a>

```c
uint16_t handle
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[handle](#a082e5dae5f08a332cf6a1dd23917d87f)。

连接句柄（Connection Handle）。

<a id="r_a0b825740b5ff47db5bfaaea7950e7d53"></a>

```c
uint16_t packet_type
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[packet_type](#a0b825740b5ff47db5bfaaea7950e7d53)。

包类型位掩码（Packet Type Bitmask）。

## 10.2\_详细说明（Detailed Documentation）

<a id="a082e5dae5f08a332cf6a1dd23917d87f"></a>

### `handle`

```c
uint16_t bt_hci_cp_change_conn_packet_type::handle
```

连接句柄（Connection Handle）。

<a id="a0b825740b5ff47db5bfaaea7950e7d53"></a>

### `packet_type`

```c
uint16_t bt_hci_cp_change_conn_packet_type::packet_type
```

包类型位掩码（Packet Type Bitmask）。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/hci_types.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/hci_types.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_bt_hci_cp_auth_requested_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_bt_hci_cp_codec_id_结构体.md)
