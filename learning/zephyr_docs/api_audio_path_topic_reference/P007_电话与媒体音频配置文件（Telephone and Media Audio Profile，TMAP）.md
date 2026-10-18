---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-7
title: 电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）

<a id="details"></a>

电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）。自 3.4 起提供，版本 0.8.0。TMAP 使用一组蓝牙功能和配置文件（Profiles），使设备能在电话和媒体音频场景中互操作（Interoperability）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_bt_5Ftmap_5Fcb"></a>

```c
struct bt_tmap_cb
```

相关声明：[bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)。

电话与媒体音频配置文件（TMAP）的回调结构。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_ga4ef8a550bb374a5f257860082e1411d4"></a>

```c
enum bt_tmap_role { BT_TMAP_ROLE_CG = (1UL << (0U)) , BT_TMAP_ROLE_CT = (1UL << (1U)) , BT_TMAP_ROLE_UMS = (1UL << (2U)) , BT_TMAP_ROLE_UMR = (1UL << (3U)) , BT_TMAP_ROLE_BMS = (1UL << (4U)) , BT_TMAP_ROLE_BMR = (1UL << (5U)) }
```

相关声明：[bt_tmap_role](#ga4ef8a550bb374a5f257860082e1411d4)、[BT_TMAP_ROLE_CG](#gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6)、[BT_TMAP_ROLE_CT](#gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d)、[BT_TMAP_ROLE_UMS](#gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501)、[BT_TMAP_ROLE_UMR](#gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22)、[BT_TMAP_ROLE_BMS](#gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308)、[BT_TMAP_ROLE_BMR](#gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8)。

TMAP 角色（TMAP Role）特征。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga2c93d1bce7db000cef76c42e5cab48cb"></a>

```c
int bt_tmap_register (enum bt_tmap_role role)
```

相关声明：[bt_tmap_register](#ga2c93d1bce7db000cef76c42e5cab48cb)、[bt_tmap_role](#ga4ef8a550bb374a5f257860082e1411d4)。

向数据库添加电话与媒体音频服务（TMAS）实例，并设置接收到的一个或多个 TMAP 角色。

<a id="r_gacb52c3e4c56f6b042398ac992628d521"></a>

```c
int bt_tmap_discover (struct bt_conn *conn, const struct bt_tmap_cb *tmap_cb)
```

相关声明：[bt_tmap_discover](#gacb52c3e4c56f6b042398ac992628d521)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)。

以 TMAP 客户端身份执行服务发现（service discovery）。

<a id="r_ga0b51b305d5a5d87df9f4082951bd28a5"></a>

```c
void bt_tmap_set_role (enum bt_tmap_role role)
```

相关声明：[bt_tmap_set_role](#ga0b51b305d5a5d87df9f4082951bd28a5)、[bt_tmap_role](#ga4ef8a550bb374a5f257860082e1411d4)。

动态设置一个或多个 TMAP 角色。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga4ef8a550bb374a5f257860082e1411d4"></a>

### `bt_tmap_role`

```c
enum bt_tmap_role
```

```c
#include <zephyr/bluetooth/audio/tmap.h>
```

TMAP 角色（TMAP Role）特征。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_TMAP_ROLE_CG` | TMAP 通话网关角色（Call Gateway Role）。此角色面向电话及 IP 语音（VoIP）应用，使用呼叫控制配置文件（Call Control Profile）来控制远端 TMAP 通话终端（Call Terminal）上的呼叫。此角色的音频流通常为双向（Bi-directional）。 |
| `BT_TMAP_ROLE_CT` | TMAP 通话终端角色（Call Terminal Role）。此角色面向电话及 IP 语音（VoIP）应用，使用呼叫控制配置文件（Call Control Profile）向远端 TMAP 通话网关（Call Gateway）公开呼叫。此角色的音频流通常为双向（Bi-directional）。 |
| `BT_TMAP_ROLE_UMS` | TMAP 单播媒体发送端角色（Unicast Media Sender Role）。此角色用于向 TMAP 单播媒体接收端（Unicast Media Receiver）发送媒体音频。此角色的音频流通常为单向（Uni-directional）。 |
| `BT_TMAP_ROLE_UMR` | TMAP 单播媒体接收端角色（Unicast Media Receiver Role）。此角色用于接收 TMAP 单播媒体发送端（Unicast Media Sender）的媒体音频。此角色的音频流通常为单向（Uni-directional）。译注：原文此句使用了 `receive ... to`，此处结合角色名称译为接收发送端的音频。 |
| `BT_TMAP_ROLE_BMS` | TMAP 广播媒体发送端角色（Broadcast Media Sender Role）。此角色用于向 TMAP 广播媒体接收端（Broadcast Media Receiver）发送媒体音频。此角色的音频流始终为单向（Uni-directional）。 |
| `BT_TMAP_ROLE_BMR` | TMAP 广播媒体接收端角色（Broadcast Media Receiver Role）。此角色用于接收来自 TMAP 广播媒体发送端（Broadcast Media Sender）的媒体音频。此角色的音频流始终为单向（Uni-directional）。 |

<a id="gacb52c3e4c56f6b042398ac992628d521"></a>

### `bt_tmap_discover()`

```c
int bt_tmap_discover ( struct bt_conn * conn, const struct bt_tmap_cb * tmap_cb )
```

```c
#include <zephyr/bluetooth/audio/tmap.h>
```

以 TMAP 客户端身份执行服务发现（service discovery）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 指向连接的指针。 |
| `tmap_cb` | 指向 TMAP 回调结构体（Callback Struct）的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga2c93d1bce7db000cef76c42e5cab48cb"></a>

### `bt_tmap_register()`

```c
int bt_tmap_register ( enum bt_tmap_role role)
```

```c
#include <zephyr/bluetooth/audio/tmap.h>
```

向数据库添加电话与媒体音频服务（TMAS）实例，并设置接收到的一个或多个 TMAP 角色。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role` | 设备的 TMAP 角色（Roles），可以是一个或多个。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，失败返回负错误值（Negative Error Value）。

<a id="ga0b51b305d5a5d87df9f4082951bd28a5"></a>

### `bt_tmap_set_role()`

```c
void bt_tmap_set_role ( enum bt_tmap_role role)
```

```c
#include <zephyr/bluetooth/audio/tmap.h>
```

动态设置一个或多个 TMAP 角色。

先前注册的值将被覆盖（Overwritten）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `role` | TMAP 角色（Roles）。 |


## 7.5\_原页交叉引用（Cross References）

- [bt_tmap_cb](../bluetooth_service_model_reference/P178_bt_tmap_cb_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/audio/tmap.h](../api_file_interface_reference/P058_zephyr__bluetooth__audio__tmap.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4a7262b5c3d711c49afc29aceea3e41ff6"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4ac09b686e750538387aa267d0161e177d"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4a60e70c130c36e95cb2f35e2d4bcd3501"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4a0fe256733164b603c2e9c8c4d8a04b22"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4ab7c4fae3617cd88f9ca8e1f2cbfb7308"></a>
<a id="gga4ef8a550bb374a5f257860082e1411d4aefc5a62198ea9c09ebb189544d1478e8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_健康客户端模型（Health Client Model）.md) · [返回大纲](大纲.md) · [下一章](P008_gPTP 支持.md)
