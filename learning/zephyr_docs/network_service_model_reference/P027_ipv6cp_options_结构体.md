---
id: learning.zephyr-docs.network-service-model-reference.page-27
title: ipv6cp_options_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipv6cp__options.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_ipv6cp\_options\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structipv6cp__options.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv6控制协议（Control Protocol）的选项。

```c
#include <zephyr/net/ppp.h>
```

<a id="details"></a>

IPv6控制协议（Control Protocol）的选项。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a4962f03fcf645257306ceeb95116ddce"></a>

```c
uint8_t iid [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[iid](#a4962f03fcf645257306ceeb95116ddce)。

接口标识符（Interface identifier）。

## 27.2\_详细说明（Detailed Documentation）

<a id="a4962f03fcf645257306ceeb95116ddce"></a>

### `iid`

```c
uint8_t ipv6cp_options::iid[8]
```

接口标识符（Interface identifier）。

本数据类型文档由以下文件生成：

- `zephyr/net/ppp.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/net/ppp.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2ppp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_ipcp_options_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_lcp_options_结构体.md)
