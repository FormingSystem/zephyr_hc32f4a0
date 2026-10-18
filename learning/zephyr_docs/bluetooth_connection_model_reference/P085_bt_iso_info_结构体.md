---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-85
title: bt_iso_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_bt\_iso\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时信道（ISO Channel）的信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时信道（ISO Channel）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 85.1\_数据成员（Data Fields）

<a id="r_af01766b8eed556ca165222d19ff05838"></a>

```c
enum bt_iso_chan_type type
```

相关声明：[bt_iso_chan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafcbd720c67c6a6e5f1cae1395e1e06f0)、[type](#af01766b8eed556ca165222d19ff05838)。

通道类型（Channel Type）。

<a id="r_a53c6c8eee63cd674d54dc1d40aa33a43"></a>

```c
uint16_t iso_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[iso_interval](#a53c6c8eee63cd674d54dc1d40aa33a43)。

等时间隔（ISO interval），为 N × 1.25 毫秒。

<a id="r_a02554d9114dc3e34305a8e986d906cbe"></a>

```c
uint8_t max_subevent
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_subevent](#a02554d9114dc3e34305a8e986d906cbe)。

每个等时事件（ISO event）中的最大子事件数。

<a id="r_a4ead7e3c5ab496b6cfc2becfaddb3746"></a>

```c
bool can_send
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[can_send](#a4ead7e3c5ab496b6cfc2becfaddb3746)。

通道能够发送数据（Send data）时为 `true`。

<a id="r_a9e00edb4e09bae39a37956011ccca353"></a>

```c
bool can_recv
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[can_recv](#a9e00edb4e09bae39a37956011ccca353)。

通道能够接收数据（Receive data）时为 `true`。

```c
union {
```

<a id="r_a4dc1660d7583075b07db8fd2b27e673e"></a>

```c
struct bt_iso_unicast_info unicast
```

相关声明：[bt_iso_unicast_info](P090_bt_iso_unicast_info_结构体.md)、[unicast](#a423474bd89ecdc614e6dfb8ea84db27e)。

单播专用信息（Unicast specific Info）。

<a id="r_a3adda1d41db2ad393a7ef817b9955232"></a>

```c
struct bt_iso_broadcaster_info broadcaster
```

相关声明：[bt_iso_broadcaster_info](P076_bt_iso_broadcaster_info_结构体.md)、[broadcaster](#a94e8132738697efa39857612399385b8)。

广播方专用信息（Broadcaster specific Info）。

<a id="r_abc98eef9346e28dc8ee6ef48e027f558"></a>

```c
struct bt_iso_sync_receiver_info sync_receiver
```

相关声明：[bt_iso_sync_receiver_info](P088_bt_iso_sync_receiver_info_结构体.md)、[sync_receiver](#ac1edf09109a5e40a4f675281a7d9e300)。

同步接收方专用信息（Sync receiver specific Info）。

<a id="r_ae86fd6749369f89c990f9a63213386d1"></a>

```c
};
```

连接类型专用信息（Connection Type specific Info）。

## 85.2\_详细说明（Detailed Documentation）

<a id="ae86fd6749369f89c990f9a63213386d1"></a>

### `[union]`

```c
union { ... } bt_iso_info
```

连接类型专用信息（Connection Type specific Info）。

<a id="a94e8132738697efa39857612399385b8"></a>

### `broadcaster`

```c
struct bt_iso_broadcaster_info bt_iso_info::broadcaster
```

广播方专用信息（Broadcaster specific Info）。

仅在启用 `CONFIG_BT_ISO_BROADCASTER` 时可用。`bt_iso_info::type` 为 `BT_ISO_CHAN_TYPE_BROADCASTER` 时使用此项。

<a id="a9e00edb4e09bae39a37956011ccca353"></a>

### `can_recv`

```c
bool bt_iso_info::can_recv
```

通道能够接收数据（Receive data）时为 `true`。

`type` 为 `BT_ISO_CHAN_TYPE_SYNC_RECEIVER` 时，此项始终为 `true`；为 `BT_ISO_CHAN_TYPE_BROADCASTER` 时，此项绝不为 `true`。

<a id="a4ead7e3c5ab496b6cfc2becfaddb3746"></a>

### `can_send`

```c
bool bt_iso_info::can_send
```

通道能够发送数据（Send data）时为 `true`。

`type` 为 `BT_ISO_CHAN_TYPE_BROADCASTER` 时，此项始终为 `true`；为 `BT_ISO_CHAN_TYPE_SYNC_RECEIVER` 时，此项绝不为 `true`。

<a id="a53c6c8eee63cd674d54dc1d40aa33a43"></a>

### `iso_interval`

```c
uint16_t bt_iso_info::iso_interval
```

等时间隔（ISO interval），为 N × 1.25 毫秒。

<a id="a02554d9114dc3e34305a8e986d906cbe"></a>

### `max_subevent`

```c
uint8_t bt_iso_info::max_subevent
```

每个等时事件（ISO event）中的最大子事件数。

<a id="ac1edf09109a5e40a4f675281a7d9e300"></a>

### `sync_receiver`

```c
struct bt_iso_sync_receiver_info bt_iso_info::sync_receiver
```

同步接收方专用信息（Sync receiver specific Info）。

仅在启用 `CONFIG_BT_ISO_SYNC_RECEIVER` 时可用。`bt_iso_info::type` 为 `BT_ISO_CHAN_TYPE_SYNC_RECEIVER` 时使用此项。

<a id="af01766b8eed556ca165222d19ff05838"></a>

### `type`

```c
enum bt_iso_chan_type bt_iso_info::type
```

通道类型（Channel Type）。

<a id="a423474bd89ecdc614e6dfb8ea84db27e"></a>

### `unicast`

```c
struct bt_iso_unicast_info bt_iso_info::unicast
```

单播专用信息（Unicast specific Info）。

仅在启用 `CONFIG_BT_ISO_UNICAST` 时可用。`bt_iso_info::type` 为 `BT_ISO_CHAN_TYPE_CENTRAL` 或 `BT_ISO_CHAN_TYPE_PERIPHERAL` 时使用此项。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 85.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [bt_iso_chan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#gafcbd720c67c6a6e5f1cae1395e1e06f0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_iso_unicast_info](P090_bt_iso_unicast_info_结构体.md)
- [bt_iso_broadcaster_info](P076_bt_iso_broadcaster_info_结构体.md)
- [bt_iso_sync_receiver_info](P088_bt_iso_sync_receiver_info_结构体.md)
- [bt_iso_info](P085_bt_iso_info_结构体.md)
- [CONFIG_BT_ISO_BROADCASTER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCASTER)
- [BT_ISO_CHAN_TYPE_BROADCASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)
- [BT_ISO_CHAN_TYPE_SYNC_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)
- [CONFIG_BT_ISO_SYNC_RECEIVER](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)
- [CONFIG_BT_ISO_UNICAST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_UNICAST)
- [BT_ISO_CHAN_TYPE_CENTRAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)
- [BT_ISO_CHAN_TYPE_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P084_bt_iso_connect_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_bt_iso_recv_info_结构体.md)
