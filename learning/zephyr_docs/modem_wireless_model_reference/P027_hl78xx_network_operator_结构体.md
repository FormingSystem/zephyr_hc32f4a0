---
id: learning.zephyr-docs.modem-wireless-model-reference.page-27
title: hl78xx_network_operator_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network__operator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_hl78xx\_network\_operator\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network__operator.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓存的网络运营商信息（Network Operator Information）。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

缓存的网络运营商信息（Network Operator Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a775fa702eb42a7d520dff3d3a3a4b208"></a>

```c
bool has_operator
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_operator](#a775fa702eb42a7d520dff3d3a3a4b208)。

运营商（operator）信息可用。

<a id="r_ab28ba8ce52648d02488efe2799d3337a"></a>

```c
char operator_name [32]
```

相关声明：[operator_name](#ab28ba8ce52648d02488efe2799d3337a)。

采用当前选定 `+COPS` 格式表示的运营商名称。

<a id="r_a1024bdecfbe35a84cb9cf6e9c65488ba"></a>

```c
bool has_mcc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_mcc](#a1024bdecfbe35a84cb9cf6e9c65488ba)。

移动国家代码（MCC）可用。

<a id="r_a9ce188616ea483281f6d600d69154cb3"></a>

```c
uint16_t mcc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mcc](#a9ce188616ea483281f6d600d69154cb3)。

移动国家代码（Mobile country code，MCC）。

<a id="r_a17dd8d113a540a311dc381f61a697012"></a>

```c
bool has_mnc
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_mnc](#a17dd8d113a540a311dc381f61a697012)。

移动网络代码（MNC）可用。

<a id="r_a8118ab76929803d7f898a62bce1f4f18"></a>

```c
uint16_t mnc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[mnc](#a8118ab76929803d7f898a62bce1f4f18)。

移动网络代码（Mobile network code，MNC）。

<a id="r_a9ca090484b881fa6343de3f8475982ed"></a>

```c
enum hl78xx_operator_format format
```

相关声明：[hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)、[format](#a9ca090484b881fa6343de3f8475982ed)。

当前 `+COPS` 运营商格式。

## 27.2\_详细说明（Detailed Documentation）

<a id="a9ca090484b881fa6343de3f8475982ed"></a>

### `format`

```c
enum hl78xx_operator_format hl78xx_network_operator::format
```

当前 `+COPS` 运营商格式。

<a id="a1024bdecfbe35a84cb9cf6e9c65488ba"></a>

### `has_mcc`

```c
bool hl78xx_network_operator::has_mcc
```

移动国家代码（MCC）可用。

<a id="a17dd8d113a540a311dc381f61a697012"></a>

### `has_mnc`

```c
bool hl78xx_network_operator::has_mnc
```

移动网络代码（MNC）可用。

<a id="a775fa702eb42a7d520dff3d3a3a4b208"></a>

### `has_operator`

```c
bool hl78xx_network_operator::has_operator
```

运营商（operator）信息可用。

<a id="a9ce188616ea483281f6d600d69154cb3"></a>

### `mcc`

```c
uint16_t hl78xx_network_operator::mcc
```

移动国家代码（Mobile country code，MCC）。

<a id="a8118ab76929803d7f898a62bce1f4f18"></a>

### `mnc`

```c
uint16_t hl78xx_network_operator::mnc
```

移动网络代码（Mobile network code，MNC）。

<a id="ab28ba8ce52648d02488efe2799d3337a"></a>

### `operator_name`

```c
char hl78xx_network_operator::operator_name[32]
```

采用当前选定 `+COPS` 格式表示的运营商名称。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [hl78xx_operator_format](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga2d26ae6044baac5995f4184abe4faad3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_hl78xx_network_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_lora_driver_api_结构体.md)
