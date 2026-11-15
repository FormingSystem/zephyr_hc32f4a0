---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-33
title: bt_cap_handover_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_bt\_cap\_handover\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__cap__handover__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

```c
#include <zephyr/bluetooth/audio/cap.h>
```

<a id="details"></a>

通用音频配置文件（Common Audio Profile，CAP）过程的回调结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a46892bfd9ac055ae73634520b385fa51"></a>

```c
void(* unicast_to_broadcast_created )(struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[unicast_to_broadcast_created](#a46892bfd9ac055ae73634520b385fa51)、[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)。

已为切换（Handover）创建广播源（Broadcast source）。

<a id="r_abd00a0e3ebc35be604194de00986d6d2"></a>

```c
void(* unicast_to_broadcast_complete )(int err, struct bt_conn *conn, struct bt_cap_unicast_group *unicast_group, struct bt_cap_broadcast_source *broadcast_source)
```

相关声明：[unicast_to_broadcast_complete](#abd00a0e3ebc35be604194de00986d6d2)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_cap_unicast_group](P045_bt_cap_unicast_group_结构体.md)、[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)。

单播到广播切换过程（Unicast to broadcast handover）已结束。

<a id="r_a0506740ed704332c3f86648bfbdd5a24"></a>

```c
void(* broadcast_to_unicast_complete )(int err, struct bt_conn *conn, struct bt_cap_broadcast_source *broadcast_source, struct bt_cap_unicast_group *unicast_group)
```

相关声明：[broadcast_to_unicast_complete](#a0506740ed704332c3f86648bfbdd5a24)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)、[bt_cap_unicast_group](P045_bt_cap_unicast_group_结构体.md)。

广播到单播切换过程（Broadcast to unicast handover）已结束。

## 33.2\_详细说明（Detailed Documentation）

<a id="a0506740ed704332c3f86648bfbdd5a24"></a>

### `broadcast_to_unicast_complete`

```c
void(* bt_cap_handover_cb::broadcast_to_unicast_complete) (int err, struct bt_conn *conn, struct bt_cap_broadcast_source *broadcast_source, struct bt_cap_unicast_group *unicast_group)
```

广播到单播切换过程（Broadcast to unicast handover）已结束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时为 `0`，否则为负的错误编号（errno）。 |
| `conn` | 指向发生错误的连接（Connection）的指针；本地失败时为 `NULL`。 |
| `broadcast_source` | 若广播源（Broadcast source）在过程中已删除，则为 `NULL`；否则指向参数中提供的广播源。 |
| `unicast_group` | 指向新建单播组（Unicast group）的指针；若在创建前发生错误，则为 `NULL`。 |

<a id="abd00a0e3ebc35be604194de00986d6d2"></a>

### `unicast_to_broadcast_complete`

```c
void(* bt_cap_handover_cb::unicast_to_broadcast_complete) (int err, struct bt_conn *conn, struct bt_cap_unicast_group *unicast_group, struct bt_cap_broadcast_source *broadcast_source)
```

单播到广播切换过程（Unicast to broadcast handover）已结束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `err` | 成功时为 `0`，否则为负的错误编号（errno）。 |
| `conn` | 指向发生错误的连接（Connection）的指针；本地失败时为 `NULL`。 |
| `unicast_group` | 若单播组（Unicast group）在过程中已删除，则为 `NULL`；否则指向参数中提供的单播组。 |
| `broadcast_source` | 指向新建广播源（Broadcast source）的指针；若在创建前发生错误，则为 `NULL`。 |

<a id="a46892bfd9ac055ae73634520b385fa51"></a>

### `unicast_to_broadcast_created`

```c
void(* bt_cap_handover_cb::unicast_to_broadcast_created) (struct bt_cap_broadcast_source *broadcast_source)
```

已为切换（Handover）创建广播源（Broadcast source）。

调用此回调时，广播源（Broadcast source）已经创建，可以通过 `bt_cap_initiator_broadcast_get_base()` 生成基本音频宣告（BASE）。要继续执行此过程的广播接收部分，应用必须启用扩展广播（Extended advertising）和周期广播（Periodic advertising），并通过 `bt_le_per_adv_set_data()` 在周期广播数据中设置 BASE。通用音频规范接受方（CAP acceptors）同步到新建广播源后，此过程即完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `broadcast_source` | 指向新建广播源（Broadcast source）的指针。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/cap.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/cap.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2audio_2cap_8h_source.html)
- [bt_cap_broadcast_source](P017_bt_cap_broadcast_source_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_cap_unicast_group](P045_bt_cap_unicast_group_结构体.md)
- [bt_cap_initiator_broadcast_get_base()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html#ga71b1a73b9fd4b1be8a63a79e05c1c0aa)
- [bt_le_per_adv_set_data()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html#gafd0e7ccca93a8347a4ca6cca88e77899)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_bt_cap_handover_broadcast_to_unicast_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_bt_cap_handover_unicast_to_broadcast_param_结构体.md)
