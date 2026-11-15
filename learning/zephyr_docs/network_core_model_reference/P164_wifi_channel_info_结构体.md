---
id: learning.zephyr-docs.network-core-model-reference.page-164
title: wifi_channel_info_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__channel__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第164章\_wifi\_channel\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__channel__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi监听及发送注入模式（Monitor / TX-Injection Modes）的信道设置。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi监听及发送注入模式（Monitor / TX-Injection Modes）的信道设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 164.1\_数据成员（Data Fields）

<a id="r_a799cbc0a67764f6680322ba0f2ad3300"></a>

```c
uint16_t channel
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[channel](#a799cbc0a67764f6680322ba0f2ad3300)。

要设置或获取的信道值（Channel value）。

<a id="r_aeda7667c89ca98c1f45a09331a2bfd47"></a>

```c
enum wifi_frequency_bands band
```

相关声明：[wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)、[band](#aeda7667c89ca98c1f45a09331a2bfd47)。

信道所属频段（Frequency band），为 2.4／5／6 GHz。

<a id="r_a43a7dd8c19d0c6540e3cc0b5d1d6165d"></a>

```c
uint8_t if_index
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[if_index](#a43a7dd8c19d0c6540e3cc0b5d1d6165d)。

接口索引（Interface index）。

<a id="r_aa8ef8a71b49ead3664fff9a4d61b1ce8"></a>

```c
enum wifi_mgmt_op oper
```

相关声明：[wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)、[oper](#aa8ef8a71b49ead3664fff9a4d61b1ce8)。

获取或设置操作（Get or set operation）。

## 164.2\_详细说明（Detailed Documentation）

<a id="aeda7667c89ca98c1f45a09331a2bfd47"></a>

### `band`

```c
enum wifi_frequency_bands wifi_channel_info::band
```

信道所属频段（Frequency band），为 2.4／5／6 GHz。

无歧义时，可使用 `WIFI_FREQ_BAND_UNKNOWN` 让驱动推断频段，例如信道 36–165 属于 5 GHz。信道存在歧义时必须指定频段，例如信道 1–14 可以属于 2.4 GHz 或 6 GHz。

<a id="a799cbc0a67764f6680322ba0f2ad3300"></a>

### `channel`

```c
uint16_t wifi_channel_info::channel
```

要设置或获取的信道值（Channel value）。

<a id="a43a7dd8c19d0c6540e3cc0b5d1d6165d"></a>

### `if_index`

```c
uint8_t wifi_channel_info::if_index
```

接口索引（Interface index）。

<a id="aa8ef8a71b49ead3664fff9a4d61b1ce8"></a>

### `oper`

```c
enum wifi_mgmt_op wifi_channel_info::oper
```

获取或设置操作（Get or set operation）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 164.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [wifi_frequency_bands](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ga1e2f0439a322355fa7368ea880c9c15d)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wifi_mgmt_op](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gae129d0783276e662575af2314eef86cd)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P163_wifi_btwt_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P165_wifi_cipher_desc_结构体.md)
