---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-82
title: bt_mesh_msg_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第82章\_bt\_mesh\_msg\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

消息发送上下文（Message Sending Context）。

```c
#include <zephyr/bluetooth/mesh/msg.h>
```

<a id="details"></a>

消息发送上下文（Message Sending Context）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 82.1\_数据成员（Data Fields）

<a id="r_a106a615ce13040e99413a15ff74bb0a9"></a>

```c
uint16_t net_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[net_idx](#a106a615ce13040e99413a15ff74bb0a9)。

发送消息所用子网的网络密钥索引（NetKey Index）。

<a id="r_a58de4d7cef6a8236a6517fc0bd961917"></a>

```c
uint16_t app_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[app_idx](#a58de4d7cef6a8236a6517fc0bd961917)。

加密消息所用的应用密钥索引（AppKey Index）。

<a id="r_a2ead7791000e9a55ed1b92c40b84bc7a"></a>

```c
uint16_t addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[addr](#a2ead7791000e9a55ed1b92c40b84bc7a)。

远端地址（Remote address）。

<a id="r_a682b192d416620a33a12b248b299b31e"></a>

```c
uint16_t recv_dst
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[recv_dst](#a682b192d416620a33a12b248b299b31e)。

接收消息的目的地址（Destination address）。

<a id="r_a548cab1ea578b29d6adf36afcf5d0299"></a>

```c
const uint8_t * uuid
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uuid](#a548cab1ea578b29d6adf36afcf5d0299)。

远端地址为虚拟地址（Virtual address）时使用的标签通用唯一标识符（Label UUID），否则为 `NULL`。

<a id="r_a1838579bb63c1976322e8eda039052db"></a>

```c
int8_t recv_rssi
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[recv_rssi](#a1838579bb63c1976322e8eda039052db)。

接收数据包的接收信号强度指示（RSSI）。

<a id="r_af8ff3238c184c541ff5417f37dd2c1e4"></a>

```c
uint8_t recv_ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recv_ttl](#af8ff3238c184c541ff5417f37dd2c1e4)。

接收到的生存时间值（TTL）。

<a id="r_a21cfb308ed8c718303bb2bc414c50753"></a>

```c
bool send_rel
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[send_rel](#a21cfb308ed8c718303bb2bc414c50753)。

通过分段确认（Segment acknowledgment）强制可靠发送（Reliable sending）。

<a id="r_acb5b5de55f35b37ba4f34ffc08943184"></a>

```c
bool rnd_delay
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rnd_delay](#acb5b5de55f35b37ba4f34ffc08943184)。

按照接入层发送规则（Access layer transmitting rules），使用随机延迟发送消息。

<a id="r_a43b0ebfdc3c8018a02886d93dfe2f21b"></a>

```c
uint8_t send_ttl
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[send_ttl](#a43b0ebfdc3c8018a02886d93dfe2f21b)。

生存时间（TTL）；设为 `BT_MESH_TTL_DEFAULT` 时使用默认 TTL。

## 82.2\_详细说明（Detailed Documentation）

<a id="a2ead7791000e9a55ed1b92c40b84bc7a"></a>

### `addr`

```c
uint16_t bt_mesh_msg_ctx::addr
```

远端地址（Remote address）。

<a id="a58de4d7cef6a8236a6517fc0bd961917"></a>

### `app_idx`

```c
uint16_t bt_mesh_msg_ctx::app_idx
```

加密消息所用的应用密钥索引（AppKey Index）。

<a id="a106a615ce13040e99413a15ff74bb0a9"></a>

### `net_idx`

```c
uint16_t bt_mesh_msg_ctx::net_idx
```

发送消息所用子网的网络密钥索引（NetKey Index）。

<a id="a682b192d416620a33a12b248b299b31e"></a>

### `recv_dst`

```c
uint16_t bt_mesh_msg_ctx::recv_dst
```

接收消息的目的地址（Destination address）。

发送时不使用（Not used for sending）。

<a id="a1838579bb63c1976322e8eda039052db"></a>

### `recv_rssi`

```c
int8_t bt_mesh_msg_ctx::recv_rssi
```

接收数据包的接收信号强度指示（RSSI）。

发送时不使用（Not used for sending）。

<a id="af8ff3238c184c541ff5417f37dd2c1e4"></a>

### `recv_ttl`

```c
uint8_t bt_mesh_msg_ctx::recv_ttl
```

接收到的生存时间值（TTL）。

发送时不使用（Not used for sending）。

<a id="acb5b5de55f35b37ba4f34ffc08943184"></a>

### `rnd_delay`

```c
bool bt_mesh_msg_ctx::rnd_delay
```

按照接入层发送规则（Access layer transmitting rules），使用随机延迟发送消息。

<a id="a21cfb308ed8c718303bb2bc414c50753"></a>

### `send_rel`

```c
bool bt_mesh_msg_ctx::send_rel
```

通过分段确认（Segment acknowledgment）强制可靠发送（Reliable sending）。

<a id="a43b0ebfdc3c8018a02886d93dfe2f21b"></a>

### `send_ttl`

```c
uint8_t bt_mesh_msg_ctx::send_ttl
```

生存时间（TTL）；设为 `BT_MESH_TTL_DEFAULT` 时使用默认 TTL。

<a id="a548cab1ea578b29d6adf36afcf5d0299"></a>

### `uuid`

```c
const uint8_t* bt_mesh_msg_ctx::uuid
```

远端地址为虚拟地址（Virtual address）时使用的标签通用唯一标识符（Label UUID），否则为 `NULL`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/msg.h`

## 82.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/msg.h](https://docs.zephyrproject.org/latest/doxygen/html/msg_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P081_bt_mesh_msg_ack_ctx_结构体.md) · [返回大纲](大纲.md) · [下一章](P083_bt_mesh_od_priv_proxy_cli_结构体.md)
