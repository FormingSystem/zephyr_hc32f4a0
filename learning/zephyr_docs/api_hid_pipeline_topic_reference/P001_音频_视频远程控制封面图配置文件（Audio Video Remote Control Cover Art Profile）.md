---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-1
title: 音频_视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_音频\_视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp__cover__art.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile，AVRCP-CA）

<a id="details"></a>

音频/视频远程控制封面图配置文件（Audio Video Remote Control Cover Art Profile，AVRCP-CA）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bt_5Favrcp_5Fcover_5Fart_5Fct"></a>

```c
struct bt_avrcp_cover_art_ct
```

相关声明：[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)。

AVRCP 控制端封面图（Controller Cover Art）结构体。

<a id="r_bt_5Favrcp_5Fcover_5Fart_5Ftg"></a>

```c
struct bt_avrcp_cover_art_tg
```

相关声明：[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)。

AVRCP 目标端封面图（Target Cover Art）结构体。

<a id="r_bt_5Favrcp_5Fcover_5Fart_5Fct_5Fcb"></a>

```c
struct bt_avrcp_cover_art_ct_cb
```

相关声明：[bt_avrcp_cover_art_ct_cb](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md)。

AVRCP 封面图控制端回调结构体（Cover Art Controller Callback Structure）。

<a id="r_bt_5Favrcp_5Fcover_5Fart_5Ftg_5Fcb"></a>

```c
struct bt_avrcp_cover_art_tg_cb
```

相关声明：[bt_avrcp_cover_art_tg_cb](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md)。

AVRCP 封面图目标端回调结构体（Cover Art Target Callback Structure）。

<a id="r_bt_5Favrcp_5Fct"></a>

```c
struct bt_avrcp_ct
```

相关声明：[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)。

AVRCP 控制端（Controller，CT）结构体。

<a id="r_bt_5Favrcp_5Ftg"></a>

```c
struct bt_avrcp_tg
```

相关声明：[bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)。

AVRCP 目标端（Target，TG）结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_ga6456a9ceae773b3490a3a065674e7770"></a>

```c
int bt_avrcp_cover_art_ct_cb_register (struct bt_avrcp_cover_art_ct_cb *cb)
```

相关声明：[bt_avrcp_cover_art_ct_cb_register](#ga6456a9ceae773b3490a3a065674e7770)、[bt_avrcp_cover_art_ct_cb](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md)。

注册音视频远程控制配置文件（AVRCP）的封面图控制端（Cover Art Controller）回调。

<a id="r_ga12c27e417b4c16ed6f9c31f018bdce65"></a>

```c
int bt_avrcp_cover_art_tg_cb_register (struct bt_avrcp_cover_art_tg_cb *cb)
```

相关声明：[bt_avrcp_cover_art_tg_cb_register](#ga12c27e417b4c16ed6f9c31f018bdce65)、[bt_avrcp_cover_art_tg_cb](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md)。

注册 AVRCP 封面图目标端（Cover Art Target）回调。

<a id="r_ga0b724c5eff89386663781a2d55048b60"></a>

```c
int bt_avrcp_cover_art_ct_l2cap_connect (struct bt_avrcp_ct *ct, struct bt_avrcp_cover_art_ct **cover_art_ct, uint16_t psm)
```

相关声明：[bt_avrcp_cover_art_ct_l2cap_connect](#ga0b724c5eff89386663781a2d55048b60)、[bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为 AVRCP 封面图控制端（Cover Art Controller）连接 L2CAP 通道。

<a id="r_ga9a87234df456d8005ac1b160242f8be6"></a>

```c
int bt_avrcp_cover_art_ct_l2cap_disconnect (struct bt_avrcp_cover_art_ct *ct)
```

相关声明：[bt_avrcp_cover_art_ct_l2cap_disconnect](#ga9a87234df456d8005ac1b160242f8be6)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)。

断开 AVRCP 封面图控制端（Cover Art Controller）的 L2CAP 通道。

<a id="r_ga2fa73ceca47131564f2c16d00e88eda1"></a>

```c
int bt_avrcp_cover_art_tg_l2cap_disconnect (struct bt_avrcp_cover_art_tg *tg)
```

相关声明：[bt_avrcp_cover_art_tg_l2cap_disconnect](#ga2fa73ceca47131564f2c16d00e88eda1)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)。

断开 AVRCP 封面图目标端（Cover Art Target）的 L2CAP 通道。

<a id="r_ga8e035c3c1d6fce40aac194ca556307d7"></a>

```c
struct net_buf * bt_avrcp_cover_art_ct_create_pdu (struct bt_avrcp_cover_art_ct *ct, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_cover_art_ct_create_pdu](#ga8e035c3c1d6fce40aac194ca556307d7)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

创建 AVRCP 封面图控制端（Cover Art Controller）的协议数据单元（PDU）缓冲区。

<a id="r_gadeeb8f39a8a8f6e44eb51f6487309e97"></a>

```c
struct net_buf * bt_avrcp_cover_art_tg_create_pdu (struct bt_avrcp_cover_art_tg *tg, struct net_buf_pool *pool)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[bt_avrcp_cover_art_tg_create_pdu](#gadeeb8f39a8a8f6e44eb51f6487309e97)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

创建 AVRCP 封面图目标端（Cover Art Target）的协议数据单元（PDU）缓冲区。

<a id="r_gabcce60bdcce46b8e1b7de69152b93273"></a>

```c
int bt_avrcp_cover_art_ct_connect (struct bt_avrcp_cover_art_ct *ct)
```

相关声明：[bt_avrcp_cover_art_ct_connect](#gabcce60bdcce46b8e1b7de69152b93273)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)。

发送对象交换协议（OBEX）连接请求（Connect Request）。

<a id="r_gae822bb08fca3ae8e8c7e1d946490922e"></a>

```c
int bt_avrcp_cover_art_tg_connect (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code)
```

相关声明：[bt_avrcp_cover_art_tg_connect](#gae822bb08fca3ae8e8c7e1d946490922e)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 OBEX 连接响应（Connect Response）。

<a id="r_gad7a0efe86750b95e94e7f18ab8720bcb"></a>

```c
int bt_avrcp_cover_art_ct_disconnect (struct bt_avrcp_cover_art_ct *ct)
```

相关声明：[bt_avrcp_cover_art_ct_disconnect](#gad7a0efe86750b95e94e7f18ab8720bcb)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)。

发送 OBEX 断开请求（Disconnect Request）。

<a id="r_ga5fedcfbbe99925fa8b61272ba40ebe05"></a>

```c
int bt_avrcp_cover_art_tg_disconnect (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code)
```

相关声明：[bt_avrcp_cover_art_tg_disconnect](#ga5fedcfbbe99925fa8b61272ba40ebe05)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送 OBEX 断开响应（Disconnect Response）。

<a id="r_gac9982c9227d5ced224aa3f13065128d2"></a>

```c
int bt_avrcp_cover_art_ct_abort (struct bt_avrcp_cover_art_ct *ct, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_ct_abort](#gac9982c9227d5ced224aa3f13065128d2)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止请求（Abort Request）。

<a id="r_ga301c1475df0c136220548d9979e4eec1"></a>

```c
int bt_avrcp_cover_art_tg_abort (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_tg_abort](#ga301c1475df0c136220548d9979e4eec1)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送 OBEX 中止响应（Abort Response）。

<a id="r_ga4ee3725ebf771ca6afa93ec0ab9b0096"></a>

```c
int bt_avrcp_cover_art_ct_get_image_properties (struct bt_avrcp_cover_art_ct *ct, bool final, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_ct_get_image_properties](#ga4ee3725ebf771ca6afa93ec0ab9b0096)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性请求（Get Image Properties Request）。

<a id="r_gab10e1b0b9ba4ebe2a41372b5e4cedbc0"></a>

```c
int bt_avrcp_cover_art_tg_get_image_properties (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_tg_get_image_properties](#gab10e1b0b9ba4ebe2a41372b5e4cedbc0)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像属性响应（Get Image Properties Response）。

<a id="r_gaf60f588b44b2f94f5af562c2f0408fa2"></a>

```c
int bt_avrcp_cover_art_ct_get_image (struct bt_avrcp_cover_art_ct *ct, bool final, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_ct_get_image](#gaf60f588b44b2f94f5af562c2f0408fa2)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像请求（Get Image Request）。

<a id="r_gacb58f20f3b7aa8993d9fae851bad8b15"></a>

```c
int bt_avrcp_cover_art_tg_get_image (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_tg_get_image](#gacb58f20f3b7aa8993d9fae851bad8b15)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取图像响应（Get Image Response）。

<a id="r_ga47c4b70799634de73e7adb812dc439fd"></a>

```c
int bt_avrcp_cover_art_ct_get_linked_thumbnail (struct bt_avrcp_cover_art_ct *ct, bool final, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_ct_get_linked_thumbnail](#ga47c4b70799634de73e7adb812dc439fd)、[bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图请求（Get Linked Thumbnail Request）。

<a id="r_gad7a25376e1d6c6910dee15b758b3970d"></a>

```c
int bt_avrcp_cover_art_tg_get_linked_thumbnail (struct bt_avrcp_cover_art_tg *tg, uint8_t rsp_code, struct net_buf *buf)
```

相关声明：[bt_avrcp_cover_art_tg_get_linked_thumbnail](#gad7a25376e1d6c6910dee15b758b3970d)、[bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

发送获取关联缩略图响应（Get Linked Thumbnail Response）。

## 1.3\_详细说明（Detailed Documentation）

<a id="gac9982c9227d5ced224aa3f13065128d2"></a>

### `bt_avrcp_cover_art_ct_abort()`

```c
int bt_avrcp_cover_art_ct_abort ( struct bt_avrcp_cover_art_ct * ct, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送 OBEX 中止请求（Abort Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `buf` | 请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga6456a9ceae773b3490a3a065674e7770"></a>

### `bt_avrcp_cover_art_ct_cb_register()`

```c
int bt_avrcp_cover_art_ct_cb_register ( struct bt_avrcp_cover_art_ct_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

注册音视频远程控制配置文件（AVRCP）的封面图控制端（Cover Art Controller）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gabcce60bdcce46b8e1b7de69152b93273"></a>

### `bt_avrcp_cover_art_ct_connect()`

```c
int bt_avrcp_cover_art_ct_connect ( struct bt_avrcp_cover_art_ct * ct)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送对象交换协议（OBEX）连接请求（Connect Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga8e035c3c1d6fce40aac194ca556307d7"></a>

### `bt_avrcp_cover_art_ct_create_pdu()`

```c
struct net_buf * bt_avrcp_cover_art_ct_create_pdu ( struct bt_avrcp_cover_art_ct * ct, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

创建 AVRCP 封面图控制端（Cover Art Controller）的协议数据单元（PDU）缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；失败返回 `NULL`。

<a id="gad7a0efe86750b95e94e7f18ab8720bcb"></a>

### `bt_avrcp_cover_art_ct_disconnect()`

```c
int bt_avrcp_cover_art_ct_disconnect ( struct bt_avrcp_cover_art_ct * ct)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送 OBEX 断开请求（Disconnect Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gaf60f588b44b2f94f5af562c2f0408fa2"></a>

### `bt_avrcp_cover_art_ct_get_image()`

```c
int bt_avrcp_cover_art_ct_get_image ( struct bt_avrcp_cover_art_ct * ct, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取图像请求（Get Image Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 包含图像描述符（Image Descriptor）的请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga4ee3725ebf771ca6afa93ec0ab9b0096"></a>

### `bt_avrcp_cover_art_ct_get_image_properties()`

```c
int bt_avrcp_cover_art_ct_get_image_properties ( struct bt_avrcp_cover_art_ct * ct, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取图像属性请求（Get Image Properties Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 包含图像句柄（Image Handle）的请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga47c4b70799634de73e7adb812dc439fd"></a>

### `bt_avrcp_cover_art_ct_get_linked_thumbnail()`

```c
int bt_avrcp_cover_art_ct_get_linked_thumbnail ( struct bt_avrcp_cover_art_ct * ct, bool final, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取关联缩略图请求（Get Linked Thumbnail Request）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |
| `final` | 如果这是请求中的最后一个数据包，则为 `true`。 |
| `buf` | 包含图像句柄（Image Handle）的请求数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga0b724c5eff89386663781a2d55048b60"></a>

### `bt_avrcp_cover_art_ct_l2cap_connect()`

```c
int bt_avrcp_cover_art_ct_l2cap_connect ( struct bt_avrcp_ct * ct, struct bt_avrcp_cover_art_ct ** cover_art_ct, uint16_t psm )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

为 AVRCP 封面图控制端（Cover Art Controller）连接 L2CAP 通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 控制端实例。 |
| `cover_art_ct` | 用于保存已创建封面图控制端实例（Cover Art Controller Instance）的指针。 |
| `psm` | L2CAP 连接的协议／服务复用器（Protocol Service Multiplexer）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga9a87234df456d8005ac1b160242f8be6"></a>

### `bt_avrcp_cover_art_ct_l2cap_disconnect()`

```c
int bt_avrcp_cover_art_ct_l2cap_disconnect ( struct bt_avrcp_cover_art_ct * ct)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

断开 AVRCP 封面图控制端（Cover Art Controller）的 L2CAP 通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ct` | AVRCP 封面图控制端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga301c1475df0c136220548d9979e4eec1"></a>

### `bt_avrcp_cover_art_tg_abort()`

```c
int bt_avrcp_cover_art_tg_abort ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送 OBEX 中止响应（Abort Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga12c27e417b4c16ed6f9c31f018bdce65"></a>

### `bt_avrcp_cover_art_tg_cb_register()`

```c
int bt_avrcp_cover_art_tg_cb_register ( struct bt_avrcp_cover_art_tg_cb * cb)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

注册 AVRCP 封面图目标端（Cover Art Target）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gae822bb08fca3ae8e8c7e1d946490922e"></a>

### `bt_avrcp_cover_art_tg_connect()`

```c
int bt_avrcp_cover_art_tg_connect ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送 OBEX 连接响应（Connect Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gadeeb8f39a8a8f6e44eb51f6487309e97"></a>

### `bt_avrcp_cover_art_tg_create_pdu()`

```c
struct net_buf * bt_avrcp_cover_art_tg_create_pdu ( struct bt_avrcp_cover_art_tg * tg, struct net_buf_pool * pool )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

创建 AVRCP 封面图目标端（Cover Art Target）的协议数据单元（PDU）缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `pool` | 用于分配的缓冲池（Buffer Pool）。 |

**返回（Returns）**：返回值：已分配的缓冲区（Allocated Buffer）；失败返回 `NULL`。

<a id="ga5fedcfbbe99925fa8b61272ba40ebe05"></a>

### `bt_avrcp_cover_art_tg_disconnect()`

```c
int bt_avrcp_cover_art_tg_disconnect ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送 OBEX 断开响应（Disconnect Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gacb58f20f3b7aa8993d9fae851bad8b15"></a>

### `bt_avrcp_cover_art_tg_get_image()`

```c
int bt_avrcp_cover_art_tg_get_image ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取图像响应（Get Image Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含图像数据的响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gab10e1b0b9ba4ebe2a41372b5e4cedbc0"></a>

### `bt_avrcp_cover_art_tg_get_image_properties()`

```c
int bt_avrcp_cover_art_tg_get_image_properties ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取图像属性响应（Get Image Properties Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含图像属性的响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="gad7a25376e1d6c6910dee15b758b3970d"></a>

### `bt_avrcp_cover_art_tg_get_linked_thumbnail()`

```c
int bt_avrcp_cover_art_tg_get_linked_thumbnail ( struct bt_avrcp_cover_art_tg * tg, uint8_t rsp_code, struct net_buf * buf )
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

发送获取关联缩略图响应（Get Linked Thumbnail Response）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |
| `rsp_code` | OBEX 响应码（Response Code）。 |
| `buf` | 包含缩略图数据的响应数据缓冲区。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga2fa73ceca47131564f2c16d00e88eda1"></a>

### `bt_avrcp_cover_art_tg_l2cap_disconnect()`

```c
int bt_avrcp_cover_art_tg_l2cap_disconnect ( struct bt_avrcp_cover_art_tg * tg)
```

```c
#include <zephyr/bluetooth/classic/avrcp_cover_art.h>
```

断开 AVRCP 封面图目标端（Cover Art Target）的 L2CAP 通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tg` | AVRCP 封面图目标端实例。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 1.4\_原页交叉引用（Cross References）

- [bt_avrcp_cover_art_ct](../bluetooth_classic_model_reference/P022_bt_avrcp_cover_art_ct_结构体.md)
- [bt_avrcp_cover_art_tg](../bluetooth_classic_model_reference/P024_bt_avrcp_cover_art_tg_结构体.md)
- [bt_avrcp_cover_art_ct_cb](../bluetooth_classic_model_reference/P023_bt_avrcp_cover_art_ct_cb_结构体.md)
- [bt_avrcp_cover_art_tg_cb](../bluetooth_classic_model_reference/P025_bt_avrcp_cover_art_tg_cb_结构体.md)
- [bt_avrcp_ct](../bluetooth_classic_model_reference/P026_bt_avrcp_ct_结构体.md)
- [bt_avrcp_tg](../bluetooth_classic_model_reference/P070_bt_avrcp_tg_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/bluetooth/classic/avrcp_cover_art.h](../api_file_display_management_reference/P002_zephyr__bluetooth__classic__avrcp_cover_art.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙 HID 设备（Device）.md)
