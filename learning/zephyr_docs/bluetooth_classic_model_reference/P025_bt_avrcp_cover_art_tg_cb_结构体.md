---
id: learning.zephyr-docs.bluetooth-classic-model-reference.page-25
title: bt_avrcp_cover_art_tg_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__tg__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_bt\_avrcp\_cover\_art\_tg\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__avrcp__cover__art__tg__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

AVRCP 封面图目标端回调结构体（Cover Art Target Callback Structure）。

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

<a id="details"></a>

AVRCP 封面图目标端回调结构体（Cover Art Target Callback Structure）。该结构体定义在各种 AVRCP 封面图目标端事件发生时调用的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a49ab3dbbfae6ae0ee86ac9646357cd4b"></a>

```c
void(* l2cap_connected )(struct bt_avrcp_tg *tg, struct bt_avrcp_cover_art_tg *cover_art_tg)
```

相关声明：[l2cap_connected](#a49ab3dbbfae6ae0ee86ac9646357cd4b)、[bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)。

L2CAP 连接完成回调。

<a id="r_ae4f3a363e0808807753dcb878916cd8b"></a>

```c
void(* l2cap_disconnected )(struct bt_avrcp_cover_art_tg *tg)
```

相关声明：[l2cap_disconnected](#ae4f3a363e0808807753dcb878916cd8b)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)。

L2CAP 断开连接回调。

<a id="r_a33cf7ee28952df116b8410bd1b7c737d"></a>

```c
void(* connect )(struct bt_avrcp_cover_art_tg *tg, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a33cf7ee28952df116b8410bd1b7c737d)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

OBEX 连接请求回调。

<a id="r_a5debda6bf20c68cb713527777d09e89c"></a>

```c
void(* disconnect )(struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf)
```

相关声明：[disconnect](#a5debda6bf20c68cb713527777d09e89c)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

OBEX 断开连接请求回调。

<a id="r_aad5cd595a1616b2ae2370c328d83cb2e"></a>

```c
void(* abort )(struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf)
```

相关声明：[abort](#aad5cd595a1616b2ae2370c328d83cb2e)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

OBEX 中止请求回调。

<a id="r_a07845b015a7c47b4236d9320f71026cc"></a>

```c
void(* get_image_properties )(struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

相关声明：[get_image_properties](#a07845b015a7c47b4236d9320f71026cc)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取图像属性（Get Image Properties）请求回调。

<a id="r_afe707ed6123c7cb78f94c6669bdfdcd4"></a>

```c
void(* get_image )(struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

相关声明：[get_image](#afe707ed6123c7cb78f94c6669bdfdcd4)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取图像（Get Image）请求回调。

<a id="r_a8d9c712c2cfc8ff106f57b406558b2e8"></a>

```c
void(* get_linked_thumbnail )(struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

相关声明：[get_linked_thumbnail](#a8d9c712c2cfc8ff106f57b406558b2e8)、[bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

获取关联缩略图（Get Linked Thumbnail）请求回调。

## 25.2\_详细说明（Detailed Documentation）

<a id="aad5cd595a1616b2ae2370c328d83cb2e"></a>

### `abort`

```c
void(* bt_avrcp_cover_art_tg_cb::abort) (struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf)
```

OBEX 中止请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `buf` | 请求数据缓冲区。 |

<a id="a33cf7ee28952df116b8410bd1b7c737d"></a>

### `connect`

```c
void(* bt_avrcp_cover_art_tg_cb::connect) (struct bt_avrcp_cover_art_tg *tg, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

OBEX 连接请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `version` | OBEX 版本。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 请求数据缓冲区。 |

<a id="a5debda6bf20c68cb713527777d09e89c"></a>

### `disconnect`

```c
void(* bt_avrcp_cover_art_tg_cb::disconnect) (struct bt_avrcp_cover_art_tg *tg, struct net_buf *buf)
```

OBEX 断开连接请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `buf` | 请求数据缓冲区。 |

<a id="afe707ed6123c7cb78f94c6669bdfdcd4"></a>

### `get_image`

```c
void(* bt_avrcp_cover_art_tg_cb::get_image) (struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

获取图像（Get Image）请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a07845b015a7c47b4236d9320f71026cc"></a>

### `get_image_properties`

```c
void(* bt_avrcp_cover_art_tg_cb::get_image_properties) (struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

获取图像属性（Get Image Properties）请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a8d9c712c2cfc8ff106f57b406558b2e8"></a>

### `get_linked_thumbnail`

```c
void(* bt_avrcp_cover_art_tg_cb::get_linked_thumbnail) (struct bt_avrcp_cover_art_tg *tg, bool final, struct net_buf *buf)
```

获取关联缩略图（Get Linked Thumbnail）请求回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a49ab3dbbfae6ae0ee86ac9646357cd4b"></a>

### `l2cap_connected`

```c
void(* bt_avrcp_cover_art_tg_cb::l2cap_connected) (struct bt_avrcp_tg *tg, struct bt_avrcp_cover_art_tg *cover_art_tg)
```

L2CAP 连接完成回调。

底层传输（L2CAP）连接完成时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 目标端实例。 |
| `cover_art_tg` | AVRCP 封面图目标端实例。 |

<a id="ae4f3a363e0808807753dcb878916cd8b"></a>

### `l2cap_disconnected`

```c
void(* bt_avrcp_cover_art_tg_cb::l2cap_disconnected) (struct bt_avrcp_cover_art_tg *tg)
```

L2CAP 断开连接回调。

底层传输断开连接时调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |

本结构体文档由以下文件生成：

- `zephyr/bluetooth/classic/avrcp_cover_art.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/avrcp_cover_art.h](https://docs.zephyrproject.org/latest/doxygen/html/avrcp__cover__art_8h_source.html)
- [bt_avrcp_tg](P070_bt_avrcp_tg_结构体.md)
- [bt_avrcp_cover_art_tg](P024_bt_avrcp_cover_art_tg_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_bt_avrcp_cover_art_tg_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_bt_avrcp_ct_结构体.md)
