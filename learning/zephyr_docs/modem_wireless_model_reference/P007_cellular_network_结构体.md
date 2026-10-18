---
id: learning.zephyr-docs.modem-wireless-model-reference.page-7
title: cellular_network_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcellular__network.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_cellular\_network\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcellular__network.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蜂窝网络（Cellular Network）结构。

```c
#include <zephyr/drivers/cellular.h>
```

<a id="details"></a>

蜂窝网络（Cellular Network）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_ad7afde61da3322e80f935c2b963eacf0"></a>

```c
enum cellular_access_technology technology
```

相关声明：[cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)、[technology](#ad7afde61da3322e80f935c2b963eacf0)。

蜂窝网络接入技术（Cellular access technology）。

<a id="r_a9313dcce10911b0febd56022c380f283"></a>

```c
uint16_t * bands
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bands](#a9313dcce10911b0febd56022c380f283)。

要启用的频段列表，频段由指定的蜂窝接入技术定义。

<a id="r_ab54057fc7cea1387c5ad3694103b0686"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#ab54057fc7cea1387c5ad3694103b0686)。

`bands` 的大小。

## 7.2\_详细说明（Detailed Documentation）

<a id="a9313dcce10911b0febd56022c380f283"></a>

### `bands`

```c
uint16_t* cellular_network::bands
```

要启用的频段列表，频段由指定的蜂窝接入技术定义。

如果未提供频段列表，则启用所有支持的频段。

<a id="ab54057fc7cea1387c5ad3694103b0686"></a>

### `size`

```c
uint16_t cellular_network::size
```

`bands` 的大小。

<a id="ad7afde61da3322e80f935c2b963eacf0"></a>

### `technology`

```c
enum cellular_access_technology cellular_network::technology
```

蜂窝网络接入技术（Cellular access technology）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/cellular.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/drivers/cellular.h](https://docs.zephyrproject.org/latest/doxygen/html/cellular_8h_source.html)
- [cellular_access_technology](https://docs.zephyrproject.org/latest/doxygen/html/group__cellular__interface.html#ga168002533ce39996e68bda2c2e92428e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_cellular_evt_registration_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_cellular_stats_结构体.md)
