---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-7
title: bt_bip_server_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__server__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bt\_bip\_server\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__server__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BIP 服务器回调结构体。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范服务器回调结构（BIP server callback structure）。包含处理 BIP 服务器操作的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a094c1d805d9e099cacb9b91315c799e7"></a>

```c
void(* connect )(struct bt_bip_server *server, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#a094c1d805d9e099cacb9b91315c799e7)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换连接请求（OBEX Connect request）。

<a id="r_aefa142e33e50b8d23f89c732fd79a125"></a>

```c
void(* disconnect )(struct bt_bip_server *server, struct net_buf *buf)
```

相关声明：[disconnect](#aefa142e33e50b8d23f89c732fd79a125)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换断开连接请求（OBEX Disconnect request）。

<a id="r_a877caeb43927ab27b360cd27b628b683"></a>

```c
void(* abort )(struct bt_bip_server *server, struct net_buf *buf)
```

相关声明：[abort](#a877caeb43927ab27b360cd27b628b683)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换中止请求（OBEX Abort request）。

<a id="r_a6c93a136a7677aa05928e762415af2de"></a>

```c
void(* get_caps )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_caps](#a6c93a136a7677aa05928e762415af2de)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取能力请求（Get Capabilities request）。

<a id="r_ad2630977d48b11da5c70762f4e6cb49e"></a>

```c
void(* get_image_list )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_image_list](#ad2630977d48b11da5c70762f4e6cb49e)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像列表请求（Get Image List request）。

<a id="r_af41d62e8ff812c9ace9a5c916c08314d"></a>

```c
void(* get_image_properties )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_image_properties](#af41d62e8ff812c9ace9a5c916c08314d)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像属性请求（Get Image Properties request）。

<a id="r_a27710e3871c031d4d787dc6f2223e71d"></a>

```c
void(* get_image )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_image](#a27710e3871c031d4d787dc6f2223e71d)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像请求（Get Image request）。

<a id="r_afc3ba204dd51bdc758cf3a6da9d72185"></a>

```c
void(* get_linked_thumbnail )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_linked_thumbnail](#afc3ba204dd51bdc758cf3a6da9d72185)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取关联缩略图请求（Get Linked Thumbnail request）。

<a id="r_ac38d13107bbd18400690196efeddb228"></a>

```c
void(* get_linked_attachment )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_linked_attachment](#ac38d13107bbd18400690196efeddb228)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取关联附件请求（Get Linked Attachment request）。

<a id="r_a755b097ab450d312a3e29f5b1a75dadf"></a>

```c
void(* get_partial_image )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_partial_image](#a755b097ab450d312a3e29f5b1a75dadf)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取部分图像请求（Get Partial Image request）。

<a id="r_a904935d6a327b9eba0ea68e924d8c1c5"></a>

```c
void(* get_monitoring_image )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_monitoring_image](#a904935d6a327b9eba0ea68e924d8c1c5)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取监视图像请求（Get Monitoring Image request）。

<a id="r_a40c07a467ff5573400cc10ba58ee54f2"></a>

```c
void(* get_status )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[get_status](#a40c07a467ff5573400cc10ba58ee54f2)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取状态请求（Get Status request）。

<a id="r_a7b0c02fd0c1546e730df162b14db745b"></a>

```c
void(* put_image )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[put_image](#a7b0c02fd0c1546e730df162b14db745b)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置图像请求（Put Image request）。

<a id="r_a4c8bf0f0791766e8c547ea10630e0948"></a>

```c
void(* put_linked_thumbnail )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[put_linked_thumbnail](#a4c8bf0f0791766e8c547ea10630e0948)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置关联缩略图请求（Put Linked Thumbnail request）。

<a id="r_a48d411ddb30784a729204080420c203d"></a>

```c
void(* put_linked_attachment )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[put_linked_attachment](#a48d411ddb30784a729204080420c203d)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置关联附件请求（Put Linked Attachment request）。

<a id="r_a81f786528f0db0afc54f7518f3765df0"></a>

```c
void(* remote_display )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[remote_display](#a81f786528f0db0afc54f7518f3765df0)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到远程显示请求（Remote Display request）。

<a id="r_a0f8052f0ee8a4e5130b538e25231fc1b"></a>

```c
void(* delete_image )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[delete_image](#a0f8052f0ee8a4e5130b538e25231fc1b)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到删除图像请求（Delete Image request）。

<a id="r_a6ca521f03e917b7354eaefac20b5b33f"></a>

```c
void(* start_print )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[start_print](#a6ca521f03e917b7354eaefac20b5b33f)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到开始打印请求（Start Print request）。

<a id="r_a6514602bea0d066abdf41d6f021d4d51"></a>

```c
void(* start_archive )(struct bt_bip_server *server, bool final, struct net_buf *buf)
```

相关声明：[start_archive](#a6514602bea0d066abdf41d6f021d4d51)、[bt_bip_server](P006_bt_bip_server_结构体.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到开始归档请求（Start Archive request）。

## 7.2\_详细说明（Detailed Documentation）

<a id="a877caeb43927ab27b360cd27b628b683"></a>

### `abort`

```c
void(* bt_bip_server_cb::abort) (struct bt_bip_server *server, struct net_buf *buf)
```

已收到对象交换中止请求（OBEX Abort request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `buf` | 请求数据缓冲区。 |

<a id="a094c1d805d9e099cacb9b91315c799e7"></a>

### `connect`

```c
void(* bt_bip_server_cb::connect) (struct bt_bip_server *server, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

已收到对象交换连接请求（OBEX Connect request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `version` | 对象交换协议版本（OBEX protocol version）。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 请求数据缓冲区。 |

<a id="a0f8052f0ee8a4e5130b538e25231fc1b"></a>

### `delete_image`

```c
void(* bt_bip_server_cb::delete_image) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到删除图像请求（Delete Image request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="aefa142e33e50b8d23f89c732fd79a125"></a>

### `disconnect`

```c
void(* bt_bip_server_cb::disconnect) (struct bt_bip_server *server, struct net_buf *buf)
```

已收到对象交换断开连接请求（OBEX Disconnect request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `buf` | 请求数据缓冲区。 |

<a id="a6c93a136a7677aa05928e762415af2de"></a>

### `get_caps`

```c
void(* bt_bip_server_cb::get_caps) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取能力请求（Get Capabilities request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a27710e3871c031d4d787dc6f2223e71d"></a>

### `get_image`

```c
void(* bt_bip_server_cb::get_image) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取图像请求（Get Image request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="ad2630977d48b11da5c70762f4e6cb49e"></a>

### `get_image_list`

```c
void(* bt_bip_server_cb::get_image_list) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取图像列表请求（Get Image List request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="af41d62e8ff812c9ace9a5c916c08314d"></a>

### `get_image_properties`

```c
void(* bt_bip_server_cb::get_image_properties) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取图像属性请求（Get Image Properties request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="ac38d13107bbd18400690196efeddb228"></a>

### `get_linked_attachment`

```c
void(* bt_bip_server_cb::get_linked_attachment) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取关联附件请求（Get Linked Attachment request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="afc3ba204dd51bdc758cf3a6da9d72185"></a>

### `get_linked_thumbnail`

```c
void(* bt_bip_server_cb::get_linked_thumbnail) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取关联缩略图请求（Get Linked Thumbnail request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a904935d6a327b9eba0ea68e924d8c1c5"></a>

### `get_monitoring_image`

```c
void(* bt_bip_server_cb::get_monitoring_image) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取监视图像请求（Get Monitoring Image request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a755b097ab450d312a3e29f5b1a75dadf"></a>

### `get_partial_image`

```c
void(* bt_bip_server_cb::get_partial_image) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取部分图像请求（Get Partial Image request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a40c07a467ff5573400cc10ba58ee54f2"></a>

### `get_status`

```c
void(* bt_bip_server_cb::get_status) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到获取状态请求（Get Status request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a7b0c02fd0c1546e730df162b14db745b"></a>

### `put_image`

```c
void(* bt_bip_server_cb::put_image) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到放置图像请求（Put Image request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a48d411ddb30784a729204080420c203d"></a>

### `put_linked_attachment`

```c
void(* bt_bip_server_cb::put_linked_attachment) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到放置关联附件请求（Put Linked Attachment request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a4c8bf0f0791766e8c547ea10630e0948"></a>

### `put_linked_thumbnail`

```c
void(* bt_bip_server_cb::put_linked_thumbnail) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到放置关联缩略图请求（Put Linked Thumbnail request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a81f786528f0db0afc54f7518f3765df0"></a>

### `remote_display`

```c
void(* bt_bip_server_cb::remote_display) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到远程显示请求（Remote Display request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a6514602bea0d066abdf41d6f021d4d51"></a>

### `start_archive`

```c
void(* bt_bip_server_cb::start_archive) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到开始归档请求（Start Archive request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

<a id="a6ca521f03e917b7354eaefac20b5b33f"></a>

### `start_print`

```c
void(* bt_bip_server_cb::start_print) (struct bt_bip_server *server, bool final, struct net_buf *buf)
```

已收到开始打印请求（Start Print request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server` | BIP 服务器实例。 |
| `final` | 这是最终数据包（Final packet）时为 `true`。 |
| `buf` | 请求数据缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_bip_server](P006_bt_bip_server_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_bt_bip_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_bt_bip_transport_ops_结构体.md)
