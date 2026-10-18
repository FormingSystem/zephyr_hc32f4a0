---
id: learning.zephyr-docs.network-application-model-reference.page-81
title: rtp_header_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtp__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_rtp\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtp__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RFC 3550第5.1节定义的实时传输协议（RTP）固定头部。

```c
#include <zephyr/net/rtp.h>
```

<a id="details"></a>

RFC 3550第5.1节定义的实时传输协议（RTP）固定头部。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_ad7ee2dd76dd05924c45b766c993f8dcb"></a>

```c
uint8_t vpxcc
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[vpxcc](#ad7ee2dd76dd05924c45b766c993f8dcb)。

版本（Version）、填充（Padding）、扩展（Extension）和CC字段的原始编码。

<a id="r_a2608e48cddd0b18bafc279517cb98e5a"></a>

```c
uint8_t mpt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mpt](#a2608e48cddd0b18bafc279517cb98e5a)。

标记（Marker）及载荷类型（Payload Type）字段的原始编码。

<a id="r_a36f45a621508f9f2c834f6572358fe7f"></a>

```c
uint16_t seq
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[seq](#a36f45a621508f9f2c834f6572358fe7f)。

序列号（Sequence Number），每发送一个RTP数据包递增1。

<a id="r_a967880697606545015c5078dd4af229c"></a>

```c
uint32_t ts
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ts](#a967880697606545015c5078dd4af229c)。

反映载荷首个八位组采样时刻的时间戳（Timestamp）。

<a id="r_ac6307a27e70b53784832ba5cc92ad8cd"></a>

```c
uint32_t ssrc
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ssrc](#ac6307a27e70b53784832ba5cc92ad8cd)。

同步源标识符（Synchronization Source，SSRC），随机选择，目标是全局唯一。

<a id="r_ae9679a49fd44503d8a5a7d74bff98fb4"></a>

```c
uint32_t csrc [CONFIG_RTP_MAX_CSRC_COUNT]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[csrc](#ae9679a49fd44503d8a5a7d74bff98fb4)。

贡献源标识符（Contributing Source，CSRC），最多CONFIG_RTP_MAX_CSRC_COUNT项。

<a id="r_aaff9f61cdfb53a9c43ce416a6ddf08bd"></a>

```c
struct rtp_header_extension header_extension
```

相关声明：[rtp_header_extension](P082_rtp_header_extension_结构体.md)、[header_extension](#aaff9f61cdfb53a9c43ce416a6ddf08bd)。

可选头部扩展（Header Extension），仅在x位被设置时有效。

## 81.2\_详细说明（Detailed Documentation）

<a id="ae9679a49fd44503d8a5a7d74bff98fb4"></a>

### `csrc`

```c
uint32_t rtp_header::csrc[CONFIG_RTP_MAX_CSRC_COUNT]
```

贡献源标识符（Contributing Source，CSRC），最多CONFIG_RTP_MAX_CSRC_COUNT项。

<a id="aaff9f61cdfb53a9c43ce416a6ddf08bd"></a>

### `header_extension`

```c
struct rtp_header_extension rtp_header::header_extension
```

可选头部扩展（Header Extension），仅在x位被设置时有效。

<a id="a2608e48cddd0b18bafc279517cb98e5a"></a>

### `mpt`

```c
uint8_t rtp_header::mpt
```

标记（Marker）及载荷类型（Payload Type）字段的原始编码。

<a id="a36f45a621508f9f2c834f6572358fe7f"></a>

### `seq`

```c
uint16_t rtp_header::seq
```

序列号（Sequence Number），每发送一个RTP数据包递增1。

<a id="ac6307a27e70b53784832ba5cc92ad8cd"></a>

### `ssrc`

```c
uint32_t rtp_header::ssrc
```

同步源标识符（Synchronization Source，SSRC），随机选择，目标是全局唯一。

<a id="a967880697606545015c5078dd4af229c"></a>

### `ts`

```c
uint32_t rtp_header::ts
```

反映载荷首个八位组采样时刻的时间戳（Timestamp）。

<a id="ad7ee2dd76dd05924c45b766c993f8dcb"></a>

### `vpxcc`

```c
uint8_t rtp_header::vpxcc
```

版本（Version）、填充（Padding）、扩展（Extension）和CC字段的原始编码。

本数据类型文档由以下文件生成：

- `zephyr/net/rtp.h`

## 81.3\_原页交叉引用（Cross References）

- [RFC 3550, section-5.1](https://datatracker.ietf.org/doc/html/rfc3550#section-5.1)
- [zephyr/net/rtp.h](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_RTP_MAX_CSRC_COUNT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_MAX_CSRC_COUNT)
- [rtp_header_extension](P082_rtp_header_extension_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_mqtt_utf8_pair_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_rtp_header_extension_结构体.md)
