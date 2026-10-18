---
id: learning.zephyr-docs.network-core-model-reference.page-161
title: wifi_band_channel_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__band__channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第161章\_wifi\_band\_channel\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__band__channel.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于唯一标识频段-信道对（Band-Channel Pair）的Wi-Fi结构。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

用于唯一标识频段-信道对（Band-Channel Pair）的Wi-Fi结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 161.1\_数据成员（Data Fields）

<a id="r_a4a932599429f37231f76c3064ec5efb3"></a>

```c
uint8_t band
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[band](#a4a932599429f37231f76c3064ec5efb3)。

频段（Frequency band）。

<a id="r_acd0dd7366de3650124dad7232a58ade0"></a>

```c
uint8_t channel
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channel](#acd0dd7366de3650124dad7232a58ade0)。

信道（Channel）。

## 161.2\_详细说明（Detailed Documentation）

<a id="a4a932599429f37231f76c3064ec5efb3"></a>

### `band`

```c
uint8_t wifi_band_channel::band
```

频段（Frequency band）。

<a id="acd0dd7366de3650124dad7232a58ade0"></a>

### `channel`

```c
uint8_t wifi_band_channel::channel
```

信道（Channel）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 161.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P160_wifi_ap_sta_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P162_wifi_bgscan_params_结构体.md)
