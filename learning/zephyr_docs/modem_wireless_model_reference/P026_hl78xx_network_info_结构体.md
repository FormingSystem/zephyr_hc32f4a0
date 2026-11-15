---
id: learning.zephyr-docs.modem-wireless-model-reference.page-26
title: hl78xx_network_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_hl78xx\_network\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__network__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓存的网络信息（Network Information）。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

缓存的网络信息（Network Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_aa1e49eec0c60b7149ee943853983fc33"></a>

```c
struct hl78xx_network_operator operator_info
```

相关声明：[hl78xx_network_operator](P027_hl78xx_network_operator_结构体.md)、[operator_info](#aa1e49eec0c60b7149ee943853983fc33)。

缓存的网络运营商信息（Network Operator Information）。

<a id="r_a350369fc45a40a80fd563997042fed81"></a>

```c
char ip_address [46]
```

相关声明：[ip_address](#a350369fc45a40a80fd563997042fed81)。

IP 地址（IP address）。

<a id="r_ab7f3c7f60d17167d8406dc977639128e"></a>

```c
char dns_primary [46]
```

相关声明：[dns_primary](#ab7f3c7f60d17167d8406dc977639128e)。

主域名系统（DNS）服务器。

## 26.2\_详细说明（Detailed Documentation）

<a id="ab7f3c7f60d17167d8406dc977639128e"></a>

### `dns_primary`

```c
char hl78xx_network_info::dns_primary[46]
```

主域名系统（DNS）服务器。

<a id="a350369fc45a40a80fd563997042fed81"></a>

### `ip_address`

```c
char hl78xx_network_info::ip_address[46]
```

IP 地址（IP address）。

<a id="aa1e49eec0c60b7149ee943853983fc33"></a>

### `operator_info`

```c
struct hl78xx_network_operator hl78xx_network_info::operator_info
```

缓存的网络运营商信息（Network Operator Information）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_network_operator](P027_hl78xx_network_operator_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_hl78xx_network_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_hl78xx_network_operator_结构体.md)
