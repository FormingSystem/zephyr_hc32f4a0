---
id: learning.zephyr-docs.network-core-model-reference.page-21
title: ieee802154_gts_request_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__request.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_ieee802154\_gts\_request\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__gts__request.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保证时隙请求（GTS Request）命令的载荷。

```c
#include <zephyr/net/ieee802154_frame.h>
```

<a id="details"></a>

保证时隙请求（GTS Request）命令的载荷。见第7.5.11节及图7-32。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 21.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a270fefe63b8bb357e18628a7d3df7123"></a>

```c
uint8_t reserved: 2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#a1acd3d9aed7f810920a65648bddf382c)。

保留字段（Reserved），应为0。

<a id="r_adc55f072007a511cdfd6c91309f5747c"></a>

```c
uint8_t type: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#a83571302ed121202cd86cf4e3e66995c)。

特性类型（Characteristics Type）。

<a id="r_a152a7dde669dbfabc07f2d0d648bd8fd"></a>

```c
uint8_t direction: 1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[direction](#a92613246fdbb6ea22760cf973afb8c9e)。

保证时隙方向（GTS Direction）：接收或发送。

<a id="r_a3b20302216a9ff7d0bed7f7f8b6b874b"></a>

```c
uint8_t length: 4
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[length](#a4ac97f1eb0825cc2a0f7710fed1ddd05)。

保证时隙长度（GTS Length）。

<a id="r_a1a74a41c410151b226d70811c60de7e2"></a>

```c
} gts
```

相关声明：[gts](#a1a74a41c410151b226d70811c60de7e2)。

保证时隙请求描述符（GTS Request Descriptor）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a92613246fdbb6ea22760cf973afb8c9e"></a>

### `direction`

```c
uint8_t ieee802154_gts_request::direction
```

保证时隙方向（GTS Direction）：接收或发送。

<a id="a1a74a41c410151b226d70811c60de7e2"></a>

### `[struct]`

```c
struct { ... } ieee802154_gts_request::gts
```

保证时隙请求描述符（GTS Request Descriptor）。

<a id="a4ac97f1eb0825cc2a0f7710fed1ddd05"></a>

### `length`

```c
uint8_t ieee802154_gts_request::length
```

保证时隙长度（GTS Length）。

<a id="a1acd3d9aed7f810920a65648bddf382c"></a>

### `reserved`

```c
uint8_t ieee802154_gts_request::reserved
```

保留字段（Reserved），应为0。

<a id="a83571302ed121202cd86cf4e3e66995c"></a>

### `type`

```c
uint8_t ieee802154_gts_request::type
```

特性类型（Characteristics Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_frame.h`

## 21.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_frame.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__frame_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P020_ieee802154_gts_dir_结构体.md) · [返回大纲](大纲.md) · [下一章](P022_ieee802154_gts_spec_结构体.md)
