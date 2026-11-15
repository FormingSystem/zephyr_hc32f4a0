---
id: learning.zephyr-docs.network-core-model-reference.page-59
title: net_eth_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_net\_eth\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__eth__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网地址（Ethernet Address）。

```c
#include <zephyr/net/ethernet.h>
```

<a id="details"></a>

以太网地址（Ethernet Address）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 59.1\_数据成员（Data Fields）

<a id="r_af370baeb1f10475331db8628c3c9efbe"></a>

```c
uint8_t addr [6U]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#af370baeb1f10475331db8628c3c9efbe)。

存储地址（Address）的缓冲区。

## 59.2\_详细说明（Detailed Documentation）

<a id="af370baeb1f10475331db8628c3c9efbe"></a>

### `addr`

```c
uint8_t net_eth_addr::addr[6U]
```

存储地址（Address）的缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/net/ethernet.h`

## 59.3\_原页交叉引用（Cross References）

- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P058_net_dplpmtud_path_结构体.md) · [返回大纲](大纲.md) · [下一章](P060_net_eth_mac_config_结构体.md)
