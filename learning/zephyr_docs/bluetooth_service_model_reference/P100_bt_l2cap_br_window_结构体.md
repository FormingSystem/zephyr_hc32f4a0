---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-100
title: bt_l2cap_br_window_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__window.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_bt\_l2cap\_br\_window\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__br__window.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

非基本模式（non-BASIC mode）L2CAP已连接信道的信息帧（I-Frame）发送窗口。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

非基本模式（non-BASIC mode）L2CAP已连接信道的信息帧（I-Frame）发送窗口。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 100.1\_数据成员（Data Fields）

<a id="r_acff85df74b031445a69c75cad1765e90"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#acff85df74b031445a69c75cad1765e90)。

<a id="r_afb66e50f934e763680200ce209ca940c"></a>

```c
uint16_t tx_seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_seq](#afb66e50f934e763680200ce209ca940c)。

发送序号（TX sequence）。

<a id="r_a781e76efc763c70a9c716f4737fb9243"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#a781e76efc763c70a9c716f4737fb9243)。

数据长度。

<a id="r_a3332cc2a424d1e2d1438232594b81a95"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#a3332cc2a424d1e2d1438232594b81a95)。

数据地址。

<a id="r_ab7bb9eb3949b37973228630b8acacd2f"></a>

```c
uint8_t transmit_counter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transmit_counter](#ab7bb9eb3949b37973228630b8acacd2f)。

发送计数器（Transmit Counter）。

<a id="r_ac2deea3f4fd7893408412ff6599c1a1a"></a>

```c
uint8_t sar
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sar](#ac2deea3f4fd7893408412ff6599c1a1a)。

分段与重组（SAR）标志。

<a id="r_a39456c041bd7d8badde949008835f891"></a>

```c
bool srej
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[srej](#a39456c041bd7d8badde949008835f891)。

选择性拒绝（SREJ）标志。

<a id="r_af34fbcec08495401b2516dd7e2ca6190"></a>

```c
bool retransmit
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[retransmit](#af34fbcec08495401b2516dd7e2ca6190)。

重传（retransmit）标志。

<a id="r_a65acb18fd339978960419ffb2c95111e"></a>

```c
struct net_buf_simple_state sdu_state
```

相关声明：[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)、[sdu_state](#a65acb18fd339978960419ffb2c95111e)。

<a id="r_affc53286b080a6914935577ffc15959c"></a>

```c
struct net_buf * sdu
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[sdu](#affc53286b080a6914935577ffc15959c)。

## 100.2\_详细说明（Detailed Documentation）

<a id="a3332cc2a424d1e2d1438232594b81a95"></a>

### `data`

```c
uint8_t* bt_l2cap_br_window::data
```

数据地址。

<a id="a781e76efc763c70a9c716f4737fb9243"></a>

### `len`

```c
uint16_t bt_l2cap_br_window::len
```

数据长度。

<a id="acff85df74b031445a69c75cad1765e90"></a>

### `node`

```c
sys_snode_t bt_l2cap_br_window::node
```

<a id="af34fbcec08495401b2516dd7e2ca6190"></a>

### `retransmit`

```c
bool bt_l2cap_br_window::retransmit
```

重传（retransmit）标志。

<a id="ac2deea3f4fd7893408412ff6599c1a1a"></a>

### `sar`

```c
uint8_t bt_l2cap_br_window::sar
```

分段与重组（SAR）标志。

<a id="affc53286b080a6914935577ffc15959c"></a>

### `sdu`

```c
struct net_buf* bt_l2cap_br_window::sdu
```

<a id="a65acb18fd339978960419ffb2c95111e"></a>

### `sdu_state`

```c
struct net_buf_simple_state bt_l2cap_br_window::sdu_state
```

<a id="a39456c041bd7d8badde949008835f891"></a>

### `srej`

```c
bool bt_l2cap_br_window::srej
```

选择性拒绝（SREJ）标志。

<a id="ab7bb9eb3949b37973228630b8acacd2f"></a>

### `transmit_counter`

```c
uint8_t bt_l2cap_br_window::transmit_counter
```

发送计数器（Transmit Counter）。

<a id="afb66e50f934e763680200ce209ca940c"></a>

### `tx_seq`

```c
uint16_t bt_l2cap_br_window::tx_seq
```

发送序号（TX sequence）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 100.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P099_bt_l2cap_br_endpoint_结构体.md) · [返回大纲](大纲.md) · [下一章](P101_bt_l2cap_chan_结构体.md)
