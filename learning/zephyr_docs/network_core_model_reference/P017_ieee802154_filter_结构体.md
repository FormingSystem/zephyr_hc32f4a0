---
id: learning.zephyr-docs.network-core-model-reference.page-17
title: ieee802154_filter_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__filter.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_ieee802154\_filter\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__filter.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

过滤器值（Filter Value），见ieee802154_radio_api::filter。

```c
#include <zephyr/net/ieee802154_radio.h>
```

<a id="details"></a>

过滤器值（Filter Value），见ieee802154_radio_api::filter。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a8390552da62452043f2ff8b0b2869a5b"></a>

```c
uint8_t * ieee_addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ieee_addr](#a636ec85ca79b2880de51ed93f6788909)。

扩展地址（Extended Address），采用小端序。

<a id="r_a5cf75be3d662f50eac5cb46db06d8acb"></a>

```c
uint16_t short_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_addr](#a16a1779ff43accda31bba35b9bdd61c3)。

短地址（Short Address），采用CPU字节序。

<a id="r_ac25f2603771feb5a5d788e496e1b9e1b"></a>

```c
uint16_t pan_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[pan_id](#a40f77239924af29d40f7595e23475e9b)。

个人区域网标识（PAN ID），采用CPU字节序。

<a id="r_a16b217049a2aaa4193a2a994533e235e"></a>

```c
};
```

## 17.2\_详细说明（Detailed Documentation）

<a id="a16b217049a2aaa4193a2a994533e235e"></a>

### `[union]`

```c
union { ... } ieee802154_filter
```

<a id="a636ec85ca79b2880de51ed93f6788909"></a>

### `ieee_addr`

```c
uint8_t* ieee802154_filter::ieee_addr
```

扩展地址（Extended Address），采用小端序。

<a id="a40f77239924af29d40f7595e23475e9b"></a>

### `pan_id`

```c
uint16_t ieee802154_filter::pan_id
```

个人区域网标识（PAN ID），采用CPU字节序。

<a id="a16a1779ff43accda31bba35b9bdd61c3"></a>

### `short_addr`

```c
uint16_t ieee802154_filter::short_addr
```

短地址（Short Address），采用CPU字节序。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio.h`

## 17.3\_原页交叉引用（Cross References）

- [ieee802154_radio_api::filter](P041_ieee802154_radio_api_结构体.md#aa9502e0e014a8d05ffe235567e8c98f3)
- [zephyr/net/ieee802154_radio.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ieee802154_filter](P017_ieee802154_filter_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_ieee802154_fcf_seq_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_ieee802154_frame_params_结构体.md)
