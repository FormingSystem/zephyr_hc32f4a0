---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-104
title: bt_l2cap_le_chan_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__chan.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_bt\_l2cap\_le\_chan\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__l2cap__le__chan.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗（LE）L2CAP信道结构。

```c
#include <zephyr/bluetooth/l2cap.h>
```

<a id="details"></a>

低功耗（LE）L2CAP信道结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 104.1\_数据成员（Data Fields）

<a id="r_a980126cabc3824ab623d634d91f7d761"></a>

```c
struct bt_l2cap_chan chan
```

相关声明：[bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)、[chan](#a980126cabc3824ab623d634d91f7d761)。

通用 L2CAP 通道引用对象。

<a id="r_a95808ad9bcd910b65bee31fa6bd4b638"></a>

```c
struct bt_l2cap_le_endpoint rx
```

相关声明：[bt_l2cap_le_endpoint](P105_bt_l2cap_le_endpoint_结构体.md)、[rx](#a95808ad9bcd910b65bee31fa6bd4b638)。

通道接收端点（Receiving Endpoint）。

<a id="r_a55d8ce850f365ac7ab7ff450ecb61f23"></a>

```c
uint16_t pending_rx_mtu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pending_rx_mtu](#a55d8ce850f365ac7ab7ff450ecb61f23)。

增强型基于信用的流控制（ECFC）重新配置期间待应用的接收 MTU，由协议栈内部使用。

<a id="r_a059f98cebf6f43a05937ac82815009e7"></a>

```c
struct bt_l2cap_le_endpoint tx
```

相关声明：[bt_l2cap_le_endpoint](P105_bt_l2cap_le_endpoint_结构体.md)、[tx](#a059f98cebf6f43a05937ac82815009e7)。

通道发送端点（Transmission Endpoint）。

<a id="r_a716ea69cb7261076023d0cf6384b3ebb"></a>

```c
struct k_fifo tx_queue
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[tx_queue](#a716ea69cb7261076023d0cf6384b3ebb)。

通道发送队列（Transmission queue）。

## 104.2\_详细说明（Detailed Documentation）

<a id="a980126cabc3824ab623d634d91f7d761"></a>

### `chan`

```c
struct bt_l2cap_chan bt_l2cap_le_chan::chan
```

通用 L2CAP 通道引用对象。

<a id="a55d8ce850f365ac7ab7ff450ecb61f23"></a>

### `pending_rx_mtu`

```c
uint16_t bt_l2cap_le_chan::pending_rx_mtu
```

增强型基于信用的流控制（ECFC）重新配置期间待应用的接收 MTU，由协议栈内部使用。

<a id="a95808ad9bcd910b65bee31fa6bd4b638"></a>

### `rx`

```c
struct bt_l2cap_le_endpoint bt_l2cap_le_chan::rx
```

通道接收端点（Receiving Endpoint）。

如果应用为通道设置了 `alloc_buf` 回调，以支持接收分段的 L2CAP SDU，则应用应初始化接收端点的 MTU。否则，协议栈会将接收端点的 MTU 初始化为 `BT_L2CAP_SDU_RX_MTU`。

发送 `L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP` 和 `L2CAP_CONFIGURATION_REQ` 时，MTU、MPS 和信用值均来源于此。

<a id="a059f98cebf6f43a05937ac82815009e7"></a>

### `tx`

```c
struct bt_l2cap_le_endpoint bt_l2cap_le_chan::tx
```

通道发送端点（Transmission Endpoint）。

这是对端 `rx` 的镜像。

MTU 和 MPS 由对端通过 `L2CAP_LE_CREDIT_BASED_CONNECTION_REQ/RSP` 或 `L2CAP_CONFIGURATION_REQ` 控制。

<a id="a716ea69cb7261076023d0cf6384b3ebb"></a>

### `tx_queue`

```c
struct k_fifo bt_l2cap_le_chan::tx_queue
```

通道发送队列（Transmission queue）。

内部使用（Internal）。

传给 `bt_l2cap_chan_send` 和 `bt_l2cap_send_pdu` 的 SDU/PDU 保存在此处，直到发送至控制器。

SDU 存入此处之前，会在其前面添加 SDU 头。由于 L2CAP 分段和分片，此列表的头部（下一个要发送的数据）可能只是某个已部分发送的 SDU/PDU 的剩余部分。

这是单个通道的发送队列（outbox）。各通道可以按任意顺序获得服务，发送顺序不会遵循跨通道的 `bt_l2cap_chan_send` 调用顺序。

此处的数据量可能超过通道当前信用数所允许发送的量。发送过程会等待，直到信用可用。

传给 `bt_l2cap_chan_send` 的回调保存在缓冲区的 `user_data` 中。当控制器针对该缓冲区的最后一个 L2CAP PDU 发出已完成缓冲区数量事件（Number of Buffers Complete Event）时，或者通道断开时，必须调用这些回调。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/l2cap.h`

## 104.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/l2cap.h](https://docs.zephyrproject.org/latest/doxygen/html/l2cap_8h_source.html)
- [bt_l2cap_chan](P101_bt_l2cap_chan_结构体.md)
- [bt_l2cap_le_endpoint](P105_bt_l2cap_le_endpoint_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [BT_L2CAP_SDU_RX_MTU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga13b93a8f09157fbcf739fa4949840efe)
- [bt_l2cap_chan_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html#ga97b7909749667f910f83e6fcb54495c3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P103_bt_l2cap_fixed_chan_结构体.md) · [返回大纲](大纲.md) · [下一章](P105_bt_l2cap_le_endpoint_结构体.md)
