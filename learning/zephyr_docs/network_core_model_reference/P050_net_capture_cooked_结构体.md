---
id: learning.zephyr-docs.network-core-model-reference.page-50
title: net_capture_cooked_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__capture__cooked.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_net\_capture\_cooked\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__capture__cooked.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

处理后模式捕获（Cooked Mode Capture）的上下文信息。

```c
#include <zephyr/net/capture.h>
```

<a id="details"></a>

处理后模式捕获（Cooked Mode Capture）的上下文信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_a17d3b9b877451bb809e6b23314117952"></a>

```c
uint16_t hatype
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[hatype](#a17d3b9b877451bb809e6b23314117952)。

链路层地址类型（Link-Layer Address Type）。

<a id="r_a953de700c9bb28dd350a7ad3b89d900b"></a>

```c
uint16_t halen
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[halen](#a953de700c9bb28dd350a7ad3b89d900b)。

链路层地址长度（Link-Layer Address Length）。

<a id="r_a30df8c6901fb132c77482b08d1a9d8a7"></a>

```c
uint8_t addr [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#a30df8c6901fb132c77482b08d1a9d8a7)。

链路层地址（Link-Layer Address）。

## 50.2\_详细说明（Detailed Documentation）

<a id="a30df8c6901fb132c77482b08d1a9d8a7"></a>

### `addr`

```c
uint8_t net_capture_cooked::addr[8]
```

链路层地址（Link-Layer Address）。

<a id="a953de700c9bb28dd350a7ad3b89d900b"></a>

### `halen`

```c
uint16_t net_capture_cooked::halen
```

链路层地址长度（Link-Layer Address Length）。

<a id="a17d3b9b877451bb809e6b23314117952"></a>

### `hatype`

```c
uint16_t net_capture_cooked::hatype
```

链路层地址类型（Link-Layer Address Type）。

本数据类型文档由以下文件生成：

- `zephyr/net/capture.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/net/capture.h](https://docs.zephyrproject.org/latest/doxygen/html/capture_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_net_buf_simple_state_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_net_capture_info_结构体.md)
