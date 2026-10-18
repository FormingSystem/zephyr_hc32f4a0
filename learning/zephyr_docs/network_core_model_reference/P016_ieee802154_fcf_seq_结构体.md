---
id: learning.zephyr-docs.network-core-model-reference.page-16
title: ieee802154_fcf_seq_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__fcf__seq.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_ieee802154\_fcf\_seq\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__fcf__seq.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAC头部（MHR）中的帧控制（Frame Control）字段与序列号。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

MAC头部（MHR）中的帧控制（Frame Control）字段和序列号。位布局遵循图7-3，八位组顺序遵循第4.3节，采用小端主机字节序。见第7.2.2节。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a0a7f5d4cadc27cd7921e4bf7dc16f213"></a>

```c
uint16_t reserved: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved](#a3ad3dbf5ba7cd8b32b7ae5804c692f24)。

保留字段（Reserved），应为0。

<a id="r_a75c9eaa1d82a62d8e405e744f21b8c37"></a>

```c
uint16_t pan_id_comp: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id_comp](#ad0f95976a3d42731c4b71cf69ea7f60c)。

PAN ID压缩（PAN ID Compression），见第7.2.2.5节。

<a id="r_ae80f1c47f3073f290ac25aa0c0b3001c"></a>

```c
uint16_t ar: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ar](#ac2233d00a5fa2fefc055d1630ba3f3d9)。

确认请求（Acknowledgment Request）：发送方请求立即确认（Imm-Ack）或增强确认（Enh-Ack）。

<a id="r_a224900397991e11d30c3e462fb12e948"></a>

```c
uint16_t frame_pending: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_pending](#a6410a742c781cfa7bd4c29c14d9d9a4f)。

帧待处理（Frame Pending）：还有发送给接收方的数据。

<a id="r_a5dbfe8ce83b3cc2f3cb915692cef0f0c"></a>

```c
uint16_t security_enabled: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[security_enabled](#adc0f9964a40343d4f35f3c1ac9cc2fac)。

安全使能（Security Enabled）：存在辅助安全头（Auxiliary Security Header）时为1。

<a id="r_a02f7191bfc102f6dc4d63376e0bf282e"></a>

```c
uint16_t frame_type: 3
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_type](#a4e3c453eff92ade1c9e7a80fa6773c1c)。

帧类型（Frame Type），见ieee802154_frame_type。

<a id="r_ad744678b8a29f01d86a556cf2a72bcb1"></a>

```c
uint16_t src_addr_mode: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[src_addr_mode](#a432cd5c18caf466acab4b1274fcbd2dc)。

源寻址模式（Source Addressing Mode），见ieee802154_addressing_mode。

<a id="r_a4e5b2cc51e7c56f77207345d4816a497"></a>

```c
uint16_t frame_version: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[frame_version](#a610345dda1d427d03a3e3c633f64d39d)。

帧版本（Frame Version），见ieee802154_version。

<a id="r_a39c7225693c42227c3d1bfa4349ee6c2"></a>

```c
uint16_t dst_addr_mode: 2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dst_addr_mode](#acf2a20dee02831538a456ef9d2932ddb)。

目的寻址模式（Destination Addressing Mode），见ieee802154_addressing_mode。

<a id="r_aa4151165d9e4dc8455fb4b82febf78bd"></a>

```c
uint16_t ie_list: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ie_list](#aca5c9dfc868ea8cfcfa36e07efe5c98a)。

存在信息元素列表（IE List / Information Elements Present）；设置后，后面跟有头部/载荷信息元素（Header / Payload IEs）。

<a id="r_ab621fe52775865134823552353f67b70"></a>

```c
uint16_t seq_num_suppr: 1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[seq_num_suppr](#ad531668d097300994f36b10b8beb5110)。

序列号抑制（Sequence Number Suppression）；设置后不包含序列号字段。

<a id="r_acc6ddee048e3a443b6d8d577d32c3bfd"></a>

```c
} fc
```

相关声明：[fc](#acc6ddee048e3a443b6d8d577d32c3bfd)。

帧控制字段（Frame Control Field），即MAC头部（MHR）的前两个八位组。

<a id="r_a49c3f394fc0fdc2d6eeb965204880aab"></a>

```c
uint8_t sequence
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sequence](#a49c3f394fc0fdc2d6eeb965204880aab)。

出站帧的数据序列号（Data Sequence Number，DSN），或接收到的序列号；见第7.2.2.4节。

## 16.2\_详细说明（Detailed Documentation）

<a id="ac2233d00a5fa2fefc055d1630ba3f3d9"></a>

### `ar`

```c
uint16_t ieee802154_fcf_seq::ar
```

确认请求（Acknowledgment Request）：发送方请求立即确认（Imm-Ack）或增强确认（Enh-Ack）。

<a id="acf2a20dee02831538a456ef9d2932ddb"></a>

### `dst_addr_mode`

```c
uint16_t ieee802154_fcf_seq::dst_addr_mode
```

目的寻址模式（Destination Addressing Mode），见ieee802154_addressing_mode。

<a id="acc6ddee048e3a443b6d8d577d32c3bfd"></a>

### `[struct]`

```c
struct { ... } ieee802154_fcf_seq::fc
```

帧控制字段（Frame Control Field），即MAC头部（MHR）的前两个八位组。

子字段（Subfields）如图7-3所示。

<a id="a6410a742c781cfa7bd4c29c14d9d9a4f"></a>

### `frame_pending`

```c
uint16_t ieee802154_fcf_seq::frame_pending
```

帧待处理（Frame Pending）：还有发送给接收方的数据。

<a id="a4e3c453eff92ade1c9e7a80fa6773c1c"></a>

### `frame_type`

```c
uint16_t ieee802154_fcf_seq::frame_type
```

帧类型（Frame Type），见ieee802154_frame_type。

<a id="a610345dda1d427d03a3e3c633f64d39d"></a>

### `frame_version`

```c
uint16_t ieee802154_fcf_seq::frame_version
```

帧版本（Frame Version），见ieee802154_version。

<a id="aca5c9dfc868ea8cfcfa36e07efe5c98a"></a>

### `ie_list`

```c
uint16_t ieee802154_fcf_seq::ie_list
```

存在信息元素列表（IE List / Information Elements Present）；设置后，后面跟有头部/载荷信息元素（Header / Payload IEs）。

<a id="ad0f95976a3d42731c4b71cf69ea7f60c"></a>

### `pan_id_comp`

```c
uint16_t ieee802154_fcf_seq::pan_id_comp
```

PAN ID压缩（PAN ID Compression），见第7.2.2.5节。

<a id="a3ad3dbf5ba7cd8b32b7ae5804c692f24"></a>

### `reserved`

```c
uint16_t ieee802154_fcf_seq::reserved
```

保留字段（Reserved），应为0。

<a id="adc0f9964a40343d4f35f3c1ac9cc2fac"></a>

### `security_enabled`

```c
uint16_t ieee802154_fcf_seq::security_enabled
```

安全使能（Security Enabled）：存在辅助安全头（Auxiliary Security Header）时为1。

<a id="ad531668d097300994f36b10b8beb5110"></a>

### `seq_num_suppr`

```c
uint16_t ieee802154_fcf_seq::seq_num_suppr
```

序列号抑制（Sequence Number Suppression）；设置后不包含序列号字段。

<a id="a49c3f394fc0fdc2d6eeb965204880aab"></a>

### `sequence`

```c
uint8_t ieee802154_fcf_seq::sequence
```

出站帧的数据序列号（Data Sequence Number，DSN），或接收到的序列号；见第7.2.2.4节。

<a id="a432cd5c18caf466acab4b1274fcbd2dc"></a>

### `src_addr_mode`

```c
uint16_t ieee802154_fcf_seq::src_addr_mode
```

源寻址模式（Source Addressing Mode），见ieee802154_addressing_mode。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ieee802154_frame_type](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a16702b800d3e4a51df6cb6f909ff79fd)
- [ieee802154_addressing_mode](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#a49f3241733da0a6dd0003d7bcaf55965)
- [ieee802154_version](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h.html#aa6a4b34e9722f5ccd06b65cf64efe053)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_ieee802154_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_ieee802154_filter_结构体.md)
