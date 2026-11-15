---
id: learning.zephyr-docs.modem-wireless-model-reference.page-32
title: lorawan_join_abp_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__abp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_lorawan\_join\_abp\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__abp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

个性化激活（Activation by Personalization，ABP）方式的LoRaWAN入网参数。

```c
#include <zephyr/lorawan/lorawan.h>
```

<a id="details"></a>

个性化激活（Activation by Personalization，ABP）方式的LoRaWAN入网参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_ad132826d04b66f145865f9a30ff03fff"></a>

```c
uint32_t dev_addr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dev_addr](#ad132826d04b66f145865f9a30ff03fff)。

设备在网络中的地址。

<a id="r_a8019bead1dfdda7a0b05f35f128edca5"></a>

```c
uint8_t * app_skey
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[app_skey](#a8019bead1dfdda7a0b05f35f128edca5)。

应用会话密钥（Application session key）。

<a id="r_aa389fec6799b12e750d57aaf0b34e6b0"></a>

```c
uint8_t * nwk_skey
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nwk_skey](#aa389fec6799b12e750d57aaf0b34e6b0)。

网络会话密钥（Network session key）。

<a id="r_a7a409fa2f3761c49085818768a62d216"></a>

```c
uint8_t * app_eui
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[app_eui](#a7a409fa2f3761c49085818768a62d216)。

应用扩展唯一标识符（Application EUI）。

## 32.2\_详细说明（Detailed Documentation）

<a id="a7a409fa2f3761c49085818768a62d216"></a>

### `app_eui`

```c
uint8_t* lorawan_join_abp::app_eui
```

应用扩展唯一标识符（Application EUI）。

<a id="a8019bead1dfdda7a0b05f35f128edca5"></a>

### `app_skey`

```c
uint8_t* lorawan_join_abp::app_skey
```

应用会话密钥（Application session key）。

<a id="ad132826d04b66f145865f9a30ff03fff"></a>

### `dev_addr`

```c
uint32_t lorawan_join_abp::dev_addr
```

设备在网络中的地址。

<a id="aa389fec6799b12e750d57aaf0b34e6b0"></a>

### `nwk_skey`

```c
uint8_t* lorawan_join_abp::nwk_skey
```

网络会话密钥（Network session key）。

本数据类型文档由以下文件生成：

- `zephyr/lorawan/lorawan.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/lorawan/lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_lorawan_downlink_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_lorawan_join_config_结构体.md)
