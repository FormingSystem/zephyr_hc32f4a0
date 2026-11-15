---
id: learning.zephyr-docs.network-service-model-reference.page-16
title: gptp_flags_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structgptp__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_gptp\_flags\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structgptp__flags.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用精确时间协议（gPTP）的消息标志。

```c
#include <zephyr/net/gptp.h>
```

<a id="details"></a>

通用精确时间协议（gPTP）的消息标志。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_afb5736b80c3c41ff021c379e2b432898"></a>

```c
uint8_t octets [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[octets](#a90b2862e78ece1b9b7f5109f5cd5f0fd)。

按字节访问（Byte access）。

<a id="r_aee98e0d20cfe59695f1ed281fc6f48cb"></a>

```c
uint16_t all
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[all](#a36871fbae0484379b00c415affdb3f9d)。

访问整个字段（Whole field access）。

<a id="r_a525f7db2fc70195a8edc3dc0e46b5798"></a>

```c
};
```

## 16.2\_详细说明（Detailed Documentation）

<a id="a525f7db2fc70195a8edc3dc0e46b5798"></a>

### `[union]`

```c
union { ... } gptp_flags
```

<a id="a36871fbae0484379b00c415affdb3f9d"></a>

### `all`

```c
uint16_t gptp_flags::all
```

访问整个字段（Whole field access）。

<a id="a90b2862e78ece1b9b7f5109f5cd5f0fd"></a>

### `octets`

```c
uint8_t gptp_flags::octets[2]
```

按字节访问（Byte access）。

本数据类型文档由以下文件生成：

- `zephyr/net/gptp.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/net/gptp.h](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [gptp_flags](P016_gptp_flags_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_gptp_clk_src_time_invoke_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_gptp_hdr_结构体.md)
