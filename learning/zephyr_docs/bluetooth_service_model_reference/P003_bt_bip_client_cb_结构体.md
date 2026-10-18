---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-3
title: bt_bip_client_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__client__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bt\_bip\_client\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__bip__client__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

BIP 客户端回调结构体。

```c
#include <zephyr/bluetooth/classic/bip.h>
```

<a id="details"></a>

基本成像规范客户端回调结构（BIP client callback structure）。包含处理 BIP 客户端操作响应的回调函数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_afd9b65b4810a31a8bd48502fcf11eff1"></a>

```c
void(* connect )(struct bt_bip_client *client, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

相关声明：[connect](#afd9b65b4810a31a8bd48502fcf11eff1)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换连接响应（OBEX Connect response）。

<a id="r_a00575e54960da7eadb6c97603c15db76"></a>

```c
void(* disconnect )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[disconnect](#a00575e54960da7eadb6c97603c15db76)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换断开连接响应（OBEX Disconnect response）。

<a id="r_aaedbc7f33eba36d176360c4806a3a27e"></a>

```c
void(* abort )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[abort](#aaedbc7f33eba36d176360c4806a3a27e)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到对象交换中止响应（OBEX Abort response）。

<a id="r_a3f6e8efdbdee62d23532bff52850ddb3"></a>

```c
void(* get_caps )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_caps](#a3f6e8efdbdee62d23532bff52850ddb3)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取能力响应（Get Capabilities response）。

<a id="r_acda8a5a4ae315bf1b65209df9ff6b8e4"></a>

```c
void(* get_image_list )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_image_list](#acda8a5a4ae315bf1b65209df9ff6b8e4)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像列表响应（Get Image List response）。

<a id="r_a16aea4cd3428723afee39332f6112c3e"></a>

```c
void(* get_image_properties )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_image_properties](#a16aea4cd3428723afee39332f6112c3e)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像属性响应（Get Image Properties response）。

<a id="r_aa551eac8ba777bbb7e286e36015a5a72"></a>

```c
void(* get_image )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_image](#aa551eac8ba777bbb7e286e36015a5a72)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取图像响应（Get Image response）。

<a id="r_a9f7713e8e68233c5837edbb46de6c758"></a>

```c
void(* get_linked_thumbnail )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_linked_thumbnail](#a9f7713e8e68233c5837edbb46de6c758)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取关联缩略图响应（Get Linked Thumbnail response）。

<a id="r_a72937856348fabd76696237a55ced1e9"></a>

```c
void(* get_linked_attachment )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_linked_attachment](#a72937856348fabd76696237a55ced1e9)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取关联附件响应（Get Linked Attachment response）。

<a id="r_a9efe5d25e239144bb40e05ff6494f20d"></a>

```c
void(* get_partial_image )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_partial_image](#a9efe5d25e239144bb40e05ff6494f20d)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取部分图像响应（Get Partial Image response）。

<a id="r_a1085306d4098491363df71e82baab9e3"></a>

```c
void(* get_monitoring_image )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_monitoring_image](#a1085306d4098491363df71e82baab9e3)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取监视图像响应（Get Monitoring Image response）。

<a id="r_a287c05808d89726d5a3fbe965b29fd52"></a>

```c
void(* get_status )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[get_status](#a287c05808d89726d5a3fbe965b29fd52)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到获取状态响应（Get Status response）。

<a id="r_a0fb9d1c1bde99fab9f68997dcce31cca"></a>

```c
void(* put_image )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[put_image](#a0fb9d1c1bde99fab9f68997dcce31cca)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置图像响应（Put Image response）。

<a id="r_aec614697e4e4ccd3dd326ecffc311c9b"></a>

```c
void(* put_linked_thumbnail )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[put_linked_thumbnail](#aec614697e4e4ccd3dd326ecffc311c9b)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置关联缩略图响应（Put Linked Thumbnail response）。

<a id="r_a3aae2299cb0779cf517d40368dc9a97e"></a>

```c
void(* put_linked_attachment )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[put_linked_attachment](#a3aae2299cb0779cf517d40368dc9a97e)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到放置关联附件响应（Put Linked Attachment response）。

<a id="r_a3ead32fbbe46d4ec0e73d0a840dc30b0"></a>

```c
void(* remote_display )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[remote_display](#a3ead32fbbe46d4ec0e73d0a840dc30b0)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到远程显示响应（Remote Display response）。

<a id="r_a5bb82c50c8e535457c17726e6133b4ef"></a>

```c
void(* delete_image )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[delete_image](#a5bb82c50c8e535457c17726e6133b4ef)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到删除图像响应（Delete Image response）。

<a id="r_a7228b45ce57155f308d6a9b983074997"></a>

```c
void(* start_print )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[start_print](#a7228b45ce57155f308d6a9b983074997)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到开始打印响应（Start Print response）。

<a id="r_a6ad152e72050d05eb8b47ba00237b6c4"></a>

```c
void(* start_archive )(struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[start_archive](#a6ad152e72050d05eb8b47ba00237b6c4)、[bt_bip_client](P002_bt_bip_client_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

已收到开始归档响应（Start Archive response）。

## 3.2\_详细说明（Detailed Documentation）

<a id="aaedbc7f33eba36d176360c4806a3a27e"></a>

### `abort`

```c
void(* bt_bip_client_cb::abort) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到对象交换中止响应（OBEX Abort response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="afd9b65b4810a31a8bd48502fcf11eff1"></a>

### `connect`

```c
void(* bt_bip_client_cb::connect) (struct bt_bip_client *client, uint8_t rsp_code, uint8_t version, uint16_t mopl, struct net_buf *buf)
```

已收到对象交换连接响应（OBEX Connect response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `version` | 对象交换协议版本（OBEX protocol version）。 |
| `mopl` | OBEX 数据包的最大长度。 |
| `buf` | 响应数据缓冲区。 |

<a id="a5bb82c50c8e535457c17726e6133b4ef"></a>

### `delete_image`

```c
void(* bt_bip_client_cb::delete_image) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到删除图像响应（Delete Image response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a00575e54960da7eadb6c97603c15db76"></a>

### `disconnect`

```c
void(* bt_bip_client_cb::disconnect) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到对象交换断开连接响应（OBEX Disconnect response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a3f6e8efdbdee62d23532bff52850ddb3"></a>

### `get_caps`

```c
void(* bt_bip_client_cb::get_caps) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取能力响应（Get Capabilities response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="aa551eac8ba777bbb7e286e36015a5a72"></a>

### `get_image`

```c
void(* bt_bip_client_cb::get_image) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取图像响应（Get Image response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="acda8a5a4ae315bf1b65209df9ff6b8e4"></a>

### `get_image_list`

```c
void(* bt_bip_client_cb::get_image_list) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取图像列表响应（Get Image List response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a16aea4cd3428723afee39332f6112c3e"></a>

### `get_image_properties`

```c
void(* bt_bip_client_cb::get_image_properties) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取图像属性响应（Get Image Properties response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a72937856348fabd76696237a55ced1e9"></a>

### `get_linked_attachment`

```c
void(* bt_bip_client_cb::get_linked_attachment) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取关联附件响应（Get Linked Attachment response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a9f7713e8e68233c5837edbb46de6c758"></a>

### `get_linked_thumbnail`

```c
void(* bt_bip_client_cb::get_linked_thumbnail) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取关联缩略图响应（Get Linked Thumbnail response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a1085306d4098491363df71e82baab9e3"></a>

### `get_monitoring_image`

```c
void(* bt_bip_client_cb::get_monitoring_image) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取监视图像响应（Get Monitoring Image response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a9efe5d25e239144bb40e05ff6494f20d"></a>

### `get_partial_image`

```c
void(* bt_bip_client_cb::get_partial_image) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取部分图像响应（Get Partial Image response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a287c05808d89726d5a3fbe965b29fd52"></a>

### `get_status`

```c
void(* bt_bip_client_cb::get_status) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到获取状态响应（Get Status response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a0fb9d1c1bde99fab9f68997dcce31cca"></a>

### `put_image`

```c
void(* bt_bip_client_cb::put_image) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到放置图像响应（Put Image response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a3aae2299cb0779cf517d40368dc9a97e"></a>

### `put_linked_attachment`

```c
void(* bt_bip_client_cb::put_linked_attachment) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到放置关联附件响应（Put Linked Attachment response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="aec614697e4e4ccd3dd326ecffc311c9b"></a>

### `put_linked_thumbnail`

```c
void(* bt_bip_client_cb::put_linked_thumbnail) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到放置关联缩略图响应（Put Linked Thumbnail response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a3ead32fbbe46d4ec0e73d0a840dc30b0"></a>

### `remote_display`

```c
void(* bt_bip_client_cb::remote_display) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到远程显示响应（Remote Display response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a6ad152e72050d05eb8b47ba00237b6c4"></a>

### `start_archive`

```c
void(* bt_bip_client_cb::start_archive) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到开始归档响应（Start Archive response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

<a id="a7228b45ce57155f308d6a9b983074997"></a>

### `start_print`

```c
void(* bt_bip_client_cb::start_print) (struct bt_bip_client *client, uint8_t rsp_code, struct net_buf *buf)
```

已收到开始打印响应（Start Print response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | BIP 客户端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/classic/bip.h`

## 3.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/classic/bip.h](https://docs.zephyrproject.org/latest/doxygen/html/bip_8h_source.html)
- [bt_bip_client](P002_bt_bip_client_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_bt_bip_client_结构体.md) · [返回大纲](大纲.md) · [下一章](P004_bt_bip_l2cap_server_结构体.md)
