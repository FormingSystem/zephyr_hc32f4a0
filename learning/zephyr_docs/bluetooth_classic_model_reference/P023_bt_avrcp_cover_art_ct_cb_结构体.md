---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-23
title: bt_avrcp_cover_art_ct_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__ct__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_bt\_avrcp\_cover\_art\_ct\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__ct__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 封面图控制端回调结构体（Cover Art Controller Callback Structure）。

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

<a id="details"></a>

AVRCP 封面图控制端回调结构体（Cover Art Controller Callback Structure）。该结构体定义在各种 AVRCP 封面图控制端事件发生时调用的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 23.1\_数据成员（Data Fields）

<a id="r_a9e3c5f78b0b187ac7a4d14a7af7f8b9d"></a>

```c
void(* l2cap_connected )(struct bt_avrcp_ct *ct, struct bt_avrcp_cover_art_ct *cover_art_ct)
```

相关声明：[l2cap_connected](#a9e3c5f78b0b187ac7a4d14a7af7f8b9d)、[bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)。

L2CAP 连接完成回调。

<a id="r_a4cd7e7b24297bf1b65756b628470be7f"></a>

```c
void(* l2cap_disconnected )(struct bt_avrcp_cover_art_ct *ct)
```

相关声明：[l2cap_disconnected](#a4cd7e7b24297bf1b65756b628470be7f)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)。

L2CAP 断开连接回调。

<a id="r_a856c77a333c623e42203c62bafd0cb01"></a>

```c
void(* connect )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a856c77a333c623e42203c62bafd0cb01)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

对象交换协议（Object Exchange，OBEX）连接响应回调。

<a id="r_ae931386c504da5182f7d58a785058296"></a>

```c
void(* disconnect )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#ae931386c504da5182f7d58a785058296)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

OBEX 断开连接响应回调。

<a id="r_a763a5bae17a8273b2c472315cdbed153"></a>

```c
void(* abort )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#a763a5bae17a8273b2c472315cdbed153)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

OBEX 中止响应回调。

<a id="r_a875ccc914eefb93e0e30228fb7ca6f9a"></a>

```c
void(* get_image_properties )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_image_properties](#a875ccc914eefb93e0e30228fb7ca6f9a)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取图像属性（Get Image Properties）响应回调。

<a id="r_ac6230b6880b55db094f486d246b0ea8f"></a>

```c
void(* get_image )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_image](#ac6230b6880b55db094f486d246b0ea8f)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取图像（Get Image）响应回调。

<a id="r_a5ff5e206b4ace7e9a1c95a7f77a82591"></a>

```c
void(* get_linked_thumbnail )(struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_linked_thumbnail](#a5ff5e206b4ace7e9a1c95a7f77a82591)、[bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取关联缩略图（Get Linked Thumbnail）响应回调。

## 23.2\_详细说明（Detailed Documentation）

<a id="a763a5bae17a8273b2c472315cdbed153"></a>

### `abort`

```c
void(* bt_avrcp_cover_art_ct_cb::abort) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 中止响应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a856c77a333c623e42203c62bafd0cb01"></a>

### `connect`

```c
void(* bt_avrcp_cover_art_ct_cb::connect) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

对象交换协议（Object Exchange，OBEX）连接响应回调。

从目标端收到连接响应时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `version` | OBEX 版本。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 响应数据缓冲区。 |

<a id="ae931386c504da5182f7d58a785058296"></a>

### `disconnect`

```c
void(* bt_avrcp_cover_art_ct_cb::disconnect) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

OBEX 断开连接响应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="ac6230b6880b55db094f486d246b0ea8f"></a>

### `get_image`

```c
void(* bt_avrcp_cover_art_ct_cb::get_image) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

获取图像（Get Image）响应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含图像数据的响应数据缓冲区。 |

<a id="a875ccc914eefb93e0e30228fb7ca6f9a"></a>

### `get_image_properties`

```c
void(* bt_avrcp_cover_art_ct_cb::get_image_properties) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

获取图像属性（Get Image Properties）响应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含图像属性的响应数据缓冲区。 |

<a id="a5ff5e206b4ace7e9a1c95a7f77a82591"></a>

### `get_linked_thumbnail`

```c
void(* bt_avrcp_cover_art_ct_cb::get_linked_thumbnail) (struct bt_avrcp_cover_art_ct *ct, uint8_t rsp_code, struct net_buf *buf)
```

获取关联缩略图（Get Linked Thumbnail）响应回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含缩略图数据的响应数据缓冲区。 |

<a id="a9e3c5f78b0b187ac7a4d14a7af7f8b9d"></a>

### `l2cap_connected`

```c
void(* bt_avrcp_cover_art_ct_cb::l2cap_connected) (struct bt_avrcp_ct *ct, struct bt_avrcp_cover_art_ct *cover_art_ct)
```

L2CAP 连接完成回调。

底层传输（L2CAP）连接完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端实例。 |
| `cover_art_ct` | AVRCP 封面图控制端实例。 |

<a id="a4cd7e7b24297bf1b65756b628470be7f"></a>

### `l2cap_disconnected`

```c
void(* bt_avrcp_cover_art_ct_cb::l2cap_disconnected) (struct bt_avrcp_cover_art_ct *ct)
```

L2CAP 断开连接回调。

底层传输断开连接时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp_cover_art.h`

## 23.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp_cover_art.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html)
- [bt_avrcp_ct](P026_bt_avrcp_ct_结构体.md)
- [bt_avrcp_cover_art_ct](P022_bt_avrcp_cover_art_ct_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P022_bt_avrcp_cover_art_ct_结构体.md) · [返回大纲](大纲.md) · [下一章](P024_bt_avrcp_cover_art_tg_结构体.md)
