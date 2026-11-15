---
id: learning.zephyr-docs.network-application-model-reference.page-17
title: coap_transmission_parameters_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__transmission__parameters.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_coap\_transmission\_parameters\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__transmission__parameters.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP传输参数（Transmission Parameters）。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

CoAP传输参数（Transmission Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_aca76954d785d04312fb834dc524f102c"></a>

```c
uint32_t ack_timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ack_timeout](#aca76954d785d04312fb834dc524f102c)。

初始确认超时（ACK Timeout）。

<a id="r_a0b43d9e3adfbf7cac09e1ffbbe1f8ce8"></a>

```c
uint16_t ack_random_percent
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[ack_random_percent](#a0b43d9e3adfbf7cac09e1ffbbe1f8ce8)。

设置CoAP确认随机因子（ACK Random Factor）。

<a id="r_a74c91235bf64fab5e7abc0c9f581e44c"></a>

```c
uint16_t coap_backoff_percent
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_backoff_percent](#a74c91235bf64fab5e7abc0c9f581e44c)。

设置CoAP重试退避因子（Retry Backoff Factor）。

<a id="r_a3a9b8bf0f2e00fc0981acdd86d404190"></a>

```c
uint8_t max_retransmission
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[max_retransmission](#a3a9b8bf0f2e00fc0981acdd86d404190)。

最大重传次数（Maximum Retransmissions）。

## 17.2\_详细说明（Detailed Documentation）

<a id="a0b43d9e3adfbf7cac09e1ffbbe1f8ce8"></a>

### `ack_random_percent`

```c
uint16_t coap_transmission_parameters::ack_random_percent
```

设置CoAP确认随机因子（ACK Random Factor）。

150表示因子1.5。值为0时使用CONFIG_COAP_ACK_RANDOM_PERCENT默认值。该值必须大于等于100。

<a id="aca76954d785d04312fb834dc524f102c"></a>

### `ack_timeout`

```c
uint32_t coap_transmission_parameters::ack_timeout
```

初始确认超时（ACK Timeout）。

该值作为重试待处理CoAP数据包的基值（Base Value）。

<a id="a74c91235bf64fab5e7abc0c9f581e44c"></a>

### `coap_backoff_percent`

```c
uint16_t coap_transmission_parameters::coap_backoff_percent
```

设置CoAP重试退避因子（Retry Backoff Factor）。

200表示因子2.0。

<a id="a3a9b8bf0f2e00fc0981acdd86d404190"></a>

### `max_retransmission`

```c
uint8_t coap_transmission_parameters::max_retransmission
```

最大重传次数（Maximum Retransmissions）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 17.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_COAP_ACK_RANDOM_PERCENT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_ACK_RANDOM_PERCENT)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_coap_resource_结构体.md) · [返回大纲](大纲.md) · [下一章](P018_dns_addrinfo_结构体.md)
