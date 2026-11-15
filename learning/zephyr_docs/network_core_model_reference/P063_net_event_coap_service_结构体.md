---
id: learning.zephyr-docs.network-core-model-reference.page-63
title: net_event_coap_service_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__coap__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_net\_event\_coap\_service\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__coap__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP服务（Service）的事件结构。

```c
#include <zephyr/net/coap_mgmt.h>
```

<a id="details"></a>

CoAP服务（Service）的事件结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_a66ad94d50eaf25c3dd3fa5f989a08392"></a>

```c
const struct coap_service * service
```

相关声明：[service](#a66ad94d50eaf25c3dd3fa5f989a08392)。

触发此事件的CoAP服务（Service）。

## 63.2\_详细说明（Detailed Documentation）

<a id="a66ad94d50eaf25c3dd3fa5f989a08392"></a>

### `service`

```c
const struct coap_service* net_event_coap_service::service
```

触发此事件的CoAP服务（Service）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_mgmt.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_net_event_coap_observer_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_net_event_ipv4_pmtu_info_结构体.md)
