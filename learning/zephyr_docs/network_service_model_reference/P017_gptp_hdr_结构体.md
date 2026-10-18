---
id: learning.zephyr-docs.network-service-model-reference.page-17
title: gptp_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_gptp\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用精确时间协议（gPTP）的消息头部。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

通用精确时间协议（gPTP）的消息头部。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_adbc9eed0fdaf07410542780c3794d642"></a>

```c
uint8_t message_type:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[message_type](#adbc9eed0fdaf07410542780c3794d642)。

消息类型。

<a id="r_acc57b0662f64bda3bc21c9c8b6286052"></a>

```c
uint8_t transport_specific:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transport_specific](#acc57b0662f64bda3bc21c9c8b6286052)。

传输专用字段（Transport specific），始终为 1。

<a id="r_aab942e44507bcff9af8e0a168b9fb810"></a>

```c
uint8_t ptp_version:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ptp_version](#aab942e44507bcff9af8e0a168b9fb810)。

精确时间协议（PTP）版本，始终为 2。

<a id="r_af9f79833695719ef42ecf0536bdfc317"></a>

```c
uint8_t reserved0:4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved0](#af9f79833695719ef42ecf0536bdfc317)。

保留字段。

<a id="r_ab58626c44b57827266606a4b85bf25cc"></a>

```c
uint16_t message_length
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[message_length](#ab58626c44b57827266606a4b85bf25cc)。

从头部到最后一个 TLV 的消息总长度。

<a id="r_a435a37858ba67222f22d4cfde3322511"></a>

```c
uint8_t domain_number
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[domain_number](#a435a37858ba67222f22d4cfde3322511)。

域编号（Domain number），始终为 0。

<a id="r_aec4214f5392123bb3cd328b94aea8d2a"></a>

```c
uint8_t reserved1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved1](#aec4214f5392123bb3cd328b94aea8d2a)。

保留字段。

<a id="r_a4c6eadb27839a3b45461df5e2078b5a7"></a>

```c
struct gptp_flags flags
```

相关声明：[gptp_flags](P016_gptp_flags_结构体.md)、[flags](#a4c6eadb27839a3b45461df5e2078b5a7)。

消息标志。

<a id="r_a38d80a7ef0ed94c50baf6285b735cf4d"></a>

```c
int64_t correction_field
```

相关声明：[int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)、[correction_field](#a38d80a7ef0ed94c50baf6285b735cf4d)。

校正字段（Correction Field）。

<a id="r_ac6340bd434fad75f7faa8386bb591412"></a>

```c
uint32_t reserved2
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[reserved2](#ac6340bd434fad75f7faa8386bb591412)。

保留字段。

<a id="r_a7e89c039b956b5fa7229b58dde855a20"></a>

```c
struct gptp_port_identity port_id
```

相关声明：[gptp_port_identity](P019_gptp_port_identity_结构体.md)、[port_id](#a7e89c039b956b5fa7229b58dde855a20)。

发送方的端口标识（Port Identity）。

<a id="r_a50f192fb70ae8633c80fa5eeb178f852"></a>

```c
uint16_t sequence_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sequence_id](#a50f192fb70ae8633c80fa5eeb178f852)。

序列 ID（Sequence ID）。

<a id="r_a68f6642239b801f2fe602a4331743d83"></a>

```c
uint8_t control
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[control](#a68f6642239b801f2fe602a4331743d83)。

控制项值。

<a id="r_a5fab00d293c3fb38fedf483b11f72890"></a>

```c
int8_t log_msg_interval
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[log_msg_interval](#a5fab00d293c3fb38fedf483b11f72890)。

同步（Sync）和宣告（Announce）消息的间隔，以以 2 为底的对数（Log2）表示。

## 17.2\_详细说明（Detailed Documentation）

<a id="a68f6642239b801f2fe602a4331743d83"></a>

### `control`

```c
uint8_t gptp_hdr::control
```

控制项值。

Sync 为 0，Follow-up 为 2，其他为 5。

<a id="a38d80a7ef0ed94c50baf6285b735cf4d"></a>

### `correction_field`

```c
int64_t gptp_hdr::correction_field
```

校正字段（Correction Field）。

内容取决于消息类型。

<a id="a435a37858ba67222f22d4cfde3322511"></a>

### `domain_number`

```c
uint8_t gptp_hdr::domain_number
```

域编号（Domain number），始终为 0。

<a id="a4c6eadb27839a3b45461df5e2078b5a7"></a>

### `flags`

```c
struct gptp_flags gptp_hdr::flags
```

消息标志。

<a id="a5fab00d293c3fb38fedf483b11f72890"></a>

### `log_msg_interval`

```c
int8_t gptp_hdr::log_msg_interval
```

同步（Sync）和宣告（Announce）消息的间隔，以以 2 为底的对数（Log2）表示。

<a id="ab58626c44b57827266606a4b85bf25cc"></a>

### `message_length`

```c
uint16_t gptp_hdr::message_length
```

从头部到最后一个 TLV 的消息总长度。

<a id="adbc9eed0fdaf07410542780c3794d642"></a>

### `message_type`

```c
uint8_t gptp_hdr::message_type
```

消息类型。

<a id="a7e89c039b956b5fa7229b58dde855a20"></a>

### `port_id`

```c
struct gptp_port_identity gptp_hdr::port_id
```

发送方的端口标识（Port Identity）。

<a id="aab942e44507bcff9af8e0a168b9fb810"></a>

### `ptp_version`

```c
uint8_t gptp_hdr::ptp_version
```

精确时间协议（PTP）版本，始终为 2。

<a id="af9f79833695719ef42ecf0536bdfc317"></a>

### `reserved0`

```c
uint8_t gptp_hdr::reserved0
```

保留字段。

<a id="aec4214f5392123bb3cd328b94aea8d2a"></a>

### `reserved1`

```c
uint8_t gptp_hdr::reserved1
```

保留字段。

<a id="ac6340bd434fad75f7faa8386bb591412"></a>

### `reserved2`

```c
uint32_t gptp_hdr::reserved2
```

保留字段。

<a id="a50f192fb70ae8633c80fa5eeb178f852"></a>

### `sequence_id`

```c
uint16_t gptp_hdr::sequence_id
```

序列 ID（Sequence ID）。

<a id="acc57b0662f64bda3bc21c9c8b6286052"></a>

### `transport_specific`

```c
uint8_t gptp_hdr::transport_specific
```

传输专用字段（Transport specific），始终为 1。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gptp_flags](P016_gptp_flags_结构体.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [gptp_port_identity](P019_gptp_port_identity_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_gptp_flags_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_gptp_phase_dis_cb_结构体.md)
