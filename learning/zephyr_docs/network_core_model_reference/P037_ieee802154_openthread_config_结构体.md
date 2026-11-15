---
id: learning.zephyr-docs.network-core-model-reference.page-37
title: ieee802154_openthread_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__openthread__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_ieee802154\_openthread\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structieee802154__openthread__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ieee802154驱动中OpenThread专用的配置数据。

```c
#include <zephyr/net/ieee802154_radio_openthread.h>
```

<a id="details"></a>

ieee802154驱动中OpenThread专用的配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 37.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_acb8e46a8efcfeafc84fb1c4405736401"></a>

```c
struct ieee802154_config common
```

相关声明：[ieee802154_config](P014_ieee802154_config_结构体.md)、[common](#ab18500f5926c8fb0bb068aca86b169d4)。

通用配置（Common Configuration）。

<a id="r_aad0af198406d9cf457dba9bf3b5b2839"></a>

```c
uint8_t max_extra_cca_attempts
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_extra_cca_attempts](#ab4cbfdddf55a95958b9df1c0f9ac70f9)。

配置项：IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS。

<a id="r_a6d8b701aed8ce9b53378cfcc0ded0c65"></a>

```c
uint32_t cst_period
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cst_period](#a774c58d56cf2cb37253051c346e67222)。

配置项：IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD。

<a id="r_af6f47dab691d7cac227e2e3d34d5f8a9"></a>

```c
net_time_t expected_tx_time
```

相关声明：[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)、[expected_tx_time](#a29d3c8793578ba47124e1931077d8c98)。

配置项：IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME。

<a id="r_ab55c167032b6a9f85036ee809e442f04"></a>

```c
};
```

## 37.2\_详细说明（Detailed Documentation）

<a id="ab55c167032b6a9f85036ee809e442f04"></a>

### `[union]`

```c
union { ... } ieee802154_openthread_config
```

<a id="ab18500f5926c8fb0bb068aca86b169d4"></a>

### `common`

```c
struct ieee802154_config ieee802154_openthread_config::common
```

通用配置（Common Configuration）。

<a id="a774c58d56cf2cb37253051c346e67222"></a>

### `cst_period`

```c
uint32_t ieee802154_openthread_config::cst_period
```

配置项：IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD。

协调采样发送（CST）的周期，采用CPU字节序。

<a id="a29d3c8793578ba47124e1931077d8c98"></a>

### `expected_tx_time`

```c
net_time_t ieee802154_openthread_config::expected_tx_time
```

配置项：IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME。

预期发送帧（TX Frame）发出的时间点。

<a id="ab4cbfdddf55a95958b9df1c0f9ac70f9"></a>

### `max_extra_cca_attempts`

```c
uint8_t ieee802154_openthread_config::max_extra_cca_attempts
```

配置项：IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS。

以IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA模式请求发送时，额外执行空闲信道评估（CCA）的最大次数。

本数据类型文档由以下文件生成：

- `zephyr/net/ieee802154_radio_openthread.h`

## 37.3\_原页交叉引用（Cross References）

- [zephyr/net/ieee802154_radio_openthread.h](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h_source.html)
- [ieee802154_config](P014_ieee802154_config_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [IEEE802154_OPENTHREAD_CONFIG_MAX_EXTRA_CCA_ATTEMPTS](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [IEEE802154_OPENTHREAD_CONFIG_CST_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525a2b1436aa0d7fdded8fda38b4ee8f2af7)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [IEEE802154_OPENTHREAD_CONFIG_EXPECTED_TX_TIME](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#ab11e7d5ec46577a0259d68349ac19525a7ee21cd052527506e860b4a3bc772a04)
- [ieee802154_openthread_config](P037_ieee802154_openthread_config_结构体.md)
- [IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA](https://docs.zephyrproject.org/latest/doxygen/html/ieee802154__radio__openthread_8h.html#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P036_ieee802154_openthread_attr_value_结构体.md) · [返回大纲](大纲.md) · [下一章](P038_ieee802154_pas_spec_结构体.md)
