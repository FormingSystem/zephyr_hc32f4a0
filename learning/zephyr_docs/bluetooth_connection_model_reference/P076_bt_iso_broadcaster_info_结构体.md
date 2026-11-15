---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-76
title: bt_iso_broadcaster_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__broadcaster__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_bt\_iso\_broadcaster\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__iso__broadcaster__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

等时通信广播端（ISO Broadcaster）的信息结构。

```c
#include <zephyr/bluetooth/iso.h>
```

<a id="details"></a>

等时通信广播端（ISO Broadcaster）的信息结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_a1defaab3c9fbbe1c91f076ece50ad7b0"></a>

```c
uint8_t big_handle
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[big_handle](#a1defaab3c9fbbe1c91f076ece50ad7b0)。

广播等时组句柄（Broadcast Isochronous Group Handle）。

<a id="r_aae07a2b0b2a56a5abb290f9345127c4f"></a>

```c
uint8_t bis_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bis_number](#aae07a2b0b2a56a5abb290f9345127c4f)。

广播等时流编号（Broadcast Isochronous Stream number）。

<a id="r_a577370ab24ebd4d80db4d8ffdb918483"></a>

```c
uint32_t sync_delay
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sync_delay](#a577370ab24ebd4d80db4d8ffdb918483)。

一个广播等时组事件（BIG event）中，所有广播等时流（BIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

<a id="r_a71388f9b64510ab91c3147f05f775aeb"></a>

```c
uint32_t latency
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[latency](#a71388f9b64510ab91c3147f05f775aeb)。

传输延迟（Transport latency），单位为微秒。

<a id="r_a9f93161fb7f81d5eb3a55f955be1b85d"></a>

```c
uint32_t pto
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[pto](#a9f93161fb7f81d5eb3a55f955be1b85d)。

预发送偏移量（Pre-transmission offset），为 N × 1.25 毫秒。

<a id="r_aa57b6e08cf4d3d154762c8c43de0f2cf"></a>

```c
uint16_t max_pdu
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[max_pdu](#aa57b6e08cf4d3d154762c8c43de0f2cf)。

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="r_a3d4e44a1da54e5ca0f2002ca3f6e7a13"></a>

```c
uint8_t phy
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[phy](#a3d4e44a1da54e5ca0f2002ca3f6e7a13)。

传输物理层（Transport PHY）。

<a id="r_ab3cb80e6b362e093e6924ab11b8737e9"></a>

```c
uint8_t bn
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bn](#ab3cb80e6b362e093e6924ab11b8737e9)。

突发数量（Burst number）。

<a id="r_ac1feade59bbad1e08418e1808619f775"></a>

```c
uint8_t irc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[irc](#ac1feade59bbad1e08418e1808619f775)。

一个载荷在广播等时流事件（BIS event）中的发送次数。

## 76.2\_详细说明（Detailed Documentation）

<a id="a1defaab3c9fbbe1c91f076ece50ad7b0"></a>

### `big_handle`

```c
uint8_t bt_iso_broadcaster_info::big_handle
```

广播等时组句柄（Broadcast Isochronous Group Handle）。

<a id="aae07a2b0b2a56a5abb290f9345127c4f"></a>

### `bis_number`

```c
uint8_t bt_iso_broadcaster_info::bis_number
```

广播等时流编号（Broadcast Isochronous Stream number）。

<a id="ab3cb80e6b362e093e6924ab11b8737e9"></a>

### `bn`

```c
uint8_t bt_iso_broadcaster_info::bn
```

突发数量（Burst number）。

<a id="ac1feade59bbad1e08418e1808619f775"></a>

### `irc`

```c
uint8_t bt_iso_broadcaster_info::irc
```

一个载荷在广播等时流事件（BIS event）中的发送次数。

<a id="a71388f9b64510ab91c3147f05f775aeb"></a>

### `latency`

```c
uint32_t bt_iso_broadcaster_info::latency
```

传输延迟（Transport latency），单位为微秒。

<a id="aa57b6e08cf4d3d154762c8c43de0f2cf"></a>

### `max_pdu`

```c
uint16_t bt_iso_broadcaster_info::max_pdu
```

最大协议数据单元大小（Maximum PDU size），以八位组（Octets）为单位。

<a id="a3d4e44a1da54e5ca0f2002ca3f6e7a13"></a>

### `phy`

```c
uint8_t bt_iso_broadcaster_info::phy
```

传输物理层（Transport PHY）。

<a id="a9f93161fb7f81d5eb3a55f955be1b85d"></a>

### `pto`

```c
uint32_t bt_iso_broadcaster_info::pto
```

预发送偏移量（Pre-transmission offset），为 N × 1.25 毫秒。

<a id="a577370ab24ebd4d80db4d8ffdb918483"></a>

### `sync_delay`

```c
uint32_t bt_iso_broadcaster_info::sync_delay
```

一个广播等时组事件（BIG event）中，所有广播等时流（BIS）的全部协议数据单元（PDUs）所用的最长时间，单位为微秒。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/iso.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/iso.h](https://docs.zephyrproject.org/latest/doxygen/html/iso_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_bt_iso_biginfo_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_bt_iso_chan_结构体.md)
