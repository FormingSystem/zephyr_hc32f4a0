---
id: learning.zephyr-docs.network-service-model-reference.page-19
title: gptp_port_identity_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__port__identity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_gptp\_port\_identity\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__port__identity.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

端口标识（Port Identity）。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

端口标识（Port Identity）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 19.1\_数据成员（Data Fields）

<a id="r_a6e8473ae6ecb4ec35e3a6b5d79851fc3"></a>

```c
uint8_t clk_id [GPTP_CLOCK_ID_LEN]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[clk_id](#a6e8473ae6ecb4ec35e3a6b5d79851fc3)。

端口的时钟标识（Clock identity）。

<a id="r_a5a0d4038aa88792290bc4619379ee48f"></a>

```c
uint16_t port_number
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[port_number](#a5a0d4038aa88792290bc4619379ee48f)。

端口编号。

## 19.2\_详细说明（Detailed Documentation）

<a id="a6e8473ae6ecb4ec35e3a6b5d79851fc3"></a>

### `clk_id`

```c
uint8_t gptp_port_identity::clk_id[GPTP_CLOCK_ID_LEN]
```

端口的时钟标识（Clock identity）。

<a id="a5a0d4038aa88792290bc4619379ee48f"></a>

### `port_number`

```c
uint16_t gptp_port_identity::port_number
```

端口编号。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 19.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P018_gptp_phase_dis_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P020_gptp_scaled_ns_结构体.md)
