---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-88
title: bt_iso_sync_receiver_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__sync__receiver__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_bt\_iso\_sync\_receiver\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__sync__receiver__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时通信同步接收端（ISO Synchronized Receiver）的信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时通信同步接收端（ISO Synchronized Receiver）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 88.1\_数据成员（Data Fields）

<a id="r_af2857439c483fdd455c7ccaf66f5fb35"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#af2857439c483fdd455c7ccaf66f5fb35)。

广播等时组句柄（Broadcast Isochronous Group handle）。

<a id="r_a55e2d87a45234bce1d54a7330164cd0d"></a>

```c
uint8_t bis_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bis_number](#a55e2d87a45234bce1d54a7330164cd0d)。

广播等时流编号（Broadcast Isochronous Stream number）。

<a id="r_a24bad4231eb214a2c95b1da9ba59c284"></a>

```c
uint32_t latency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[latency](#a24bad4231eb214a2c95b1da9ba59c284)。

传输延迟（Transport latency），单位为微秒。

<a id="r_a80ac6e529491156109955219569fdec6"></a>

```c
uint32_t pto
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pto](#a80ac6e529491156109955219569fdec6)。

预发送偏移量（Pre-transmission offset），为 N × 1.25 毫秒。

<a id="r_a40ff5a4d691a75802f211a63b1e12303"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#a40ff5a4d691a75802f211a63b1e12303)。

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="r_a8be50f8c6d76515ac290407959eaf0e1"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#a8be50f8c6d76515ac290407959eaf0e1)。

突发数量（Burst number）。

<a id="r_a6185a7ac123be930650da6dc84c0c1e0"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#a6185a7ac123be930650da6dc84c0c1e0)。

一个载荷在广播等时流事件（BIS event）中的发送次数。

## 88.2\_详细说明（Detailed Documentation）

<a id="af2857439c483fdd455c7ccaf66f5fb35"></a>

### `big_handle`

```c
uint8_t bt_iso_sync_receiver_info::big_handle
```

广播等时组句柄（Broadcast Isochronous Group handle）。

<a id="a55e2d87a45234bce1d54a7330164cd0d"></a>

### `bis_number`

```c
uint8_t bt_iso_sync_receiver_info::bis_number
```

广播等时流编号（Broadcast Isochronous Stream number）。

<a id="a8be50f8c6d76515ac290407959eaf0e1"></a>

### `bn`

```c
uint8_t bt_iso_sync_receiver_info::bn
```

突发数量（Burst number）。

<a id="a6185a7ac123be930650da6dc84c0c1e0"></a>

### `irc`

```c
uint8_t bt_iso_sync_receiver_info::irc
```

一个载荷在广播等时流事件（BIS event）中的发送次数。

<a id="a24bad4231eb214a2c95b1da9ba59c284"></a>

### `latency`

```c
uint32_t bt_iso_sync_receiver_info::latency
```

传输延迟（Transport latency），单位为微秒。

<a id="a40ff5a4d691a75802f211a63b1e12303"></a>

### `max_pdu`

```c
uint16_t bt_iso_sync_receiver_info::max_pdu
```

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="a80ac6e529491156109955219569fdec6"></a>

### `pto`

```c
uint32_t bt_iso_sync_receiver_info::pto
```

预发送偏移量（Pre-transmission offset），为 N × 1.25 毫秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 88.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P087_bt_iso_server_结构体.md) · [返回大纲](大纲.md) · [下一章](P089_bt_iso_tx_info_结构体.md)
