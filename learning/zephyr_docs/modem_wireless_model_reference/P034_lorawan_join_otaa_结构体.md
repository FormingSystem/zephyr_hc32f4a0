---
id: learning.zephyr-docs.modem-wireless-model-reference.page-34
title: lorawan_join_otaa_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__otaa.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_lorawan\_join\_otaa\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlorawan__join__otaa.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

空中激活（Over-the-Air Activation，OTAA）方式的LoRaWAN入网参数。

```c
#include <zephyr/lorawan/lorawan.h>
```

<a id="details"></a>

用于空中激活（Over-the-Air Activation，OTAA）的 LoRaWAN 入网参数。注意，所有字段均使用 LoRaWAN 1.1 术语。如果存在安全元件，所有参数均为可选，此时改用安全元件中存储的值。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_aacf3523f615f08fac1993e0bdc354072"></a>

```c
uint8_t * join_eui
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[join_eui](#aacf3523f615f08fac1993e0bdc354072)。

入网扩展唯一标识符（Join EUI）。

<a id="r_af1a96b4fa17ee70ee0e8ba078b02a6bc"></a>

```c
uint8_t * nwk_key
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nwk_key](#af1a96b4fa17ee70ee0e8ba078b02a6bc)。

网络密钥（Network Key）。

<a id="r_a28dd704e28d0bed909c3e85e516c85ea"></a>

```c
uint8_t * app_key
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[app_key](#a28dd704e28d0bed909c3e85e516c85ea)。

应用密钥（Application Key）。

<a id="r_ab83167af58040f95072a95fbaed1ff5d"></a>

```c
uint16_t dev_nonce
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dev_nonce](#ab83167af58040f95072a95fbaed1ff5d)。

设备一次性值（Device Nonce）。

## 34.2\_详细说明（Detailed Documentation）

<a id="a28dd704e28d0bed909c3e85e516c85ea"></a>

### `app_key`

```c
uint8_t* lorawan_join_otaa::app_key
```

应用密钥（Application Key）。

<a id="ab83167af58040f95072a95fbaed1ff5d"></a>

### `dev_nonce`

```c
uint16_t lorawan_join_otaa::dev_nonce
```

设备一次性值（Device Nonce）。

从 LoRaWAN 1.0.4 起，同一个 EUI 的每次 OTAA 入网所使用的 `DevNonce` 都必须单调递增。应用应将 `DevNonce` 保存在非易失性存储器（non-volatile memory）中。

<a id="aacf3523f615f08fac1993e0bdc354072"></a>

### `join_eui`

```c
uint8_t* lorawan_join_otaa::join_eui
```

入网扩展唯一标识符（Join EUI）。

<a id="af1a96b4fa17ee70ee0e8ba078b02a6bc"></a>

### `nwk_key`

```c
uint8_t* lorawan_join_otaa::nwk_key
```

网络密钥（Network Key）。

本数据类型文档由以下文件生成：

- `zephyr/lorawan/lorawan.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/lorawan/lorawan.h](https://docs.zephyrproject.org/latest/doxygen/html/lorawan_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_lorawan_join_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_mdm_hl7800_apn_结构体.md)
