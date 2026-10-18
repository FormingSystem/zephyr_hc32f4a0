---
id: learning.zephyr-docs.network-core-model-reference.page-174
title: wifi_filter_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__filter__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第174章\_wifi\_filter\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__filter__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi监听、混杂和发送注入模式（Monitor, Promiscuous, TX-Injection Modes）的过滤器设置。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi监听、混杂和发送注入模式（Monitor, Promiscuous, TX-Injection Modes）的过滤器设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 174.1\_数据成员（Data Fields）

<a id="r_ad9560be814299055cfa11b995a7dcf42"></a>

```c
uint8_t filter
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[filter](#ad9560be814299055cfa11b995a7dcf42)。

过滤器设置（Filter setting）。

<a id="r_af9ea91e31e78afcb7ffe1ff9a04277a3"></a>

```c
uint8_t if_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[if_index](#af9ea91e31e78afcb7ffe1ff9a04277a3)。

接口索引（Interface index）。

<a id="r_a1b2d0448fc7f62654e3f5aacfba62f8f"></a>

```c
uint16_t buffer_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[buffer_size](#a1b2d0448fc7f62654e3f5aacfba62f8f)。

过滤器缓冲区大小（Filter buffer size）。

<a id="r_aedd5e220cdde5768cb0f4aff920971cd"></a>

```c
enum wifi_mgmt_op oper
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[oper](#aedd5e220cdde5768cb0f4aff920971cd)。

获取或设置操作（Get or set operation）。

## 174.2\_详细说明（Detailed Documentation）

<a id="a1b2d0448fc7f62654e3f5aacfba62f8f"></a>

### `buffer_size`

```c
uint16_t wifi_filter_info::buffer_size
```

过滤器缓冲区大小（Filter buffer size）。

<a id="ad9560be814299055cfa11b995a7dcf42"></a>

### `filter`

```c
uint8_t wifi_filter_info::filter
```

过滤器设置（Filter setting）。

<a id="af9ea91e31e78afcb7ffe1ff9a04277a3"></a>

### `if_index`

```c
uint8_t wifi_filter_info::if_index
```

接口索引（Interface index）。

<a id="aedd5e220cdde5768cb0f4aff920971cd"></a>

### `oper`

```c
enum wifi_mgmt_op wifi_filter_info::oper
```

获取或设置操作（Get or set operation）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 174.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P173_wifi_enterprise_creds_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P175_wifi_iface_status_结构体.md)
