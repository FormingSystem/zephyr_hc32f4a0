---
id: learning.zephyr-docs.network-core-model-reference.page-62
title: net_event_coap_observer_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__coap__observer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_net\_event\_coap\_observer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__event__coap__observer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP观察者（Observer）的事件结构。

```c
#include <zephyr/net/coap_mgmt.h>
```

<a id="details"></a>

CoAP观察者（Observer）的事件结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_a4522acf85fff0a65def80f3a7d794d2b"></a>

```c
struct coap_resource * resource
```

相关声明：[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[resource](#a4522acf85fff0a65def80f3a7d794d2b)。

触发此事件的CoAP资源（Resource）。

<a id="r_af15a9f085271fdc5e88180980013bfd2"></a>

```c
struct coap_observer * observer
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[observer](#af15a9f085271fdc5e88180980013bfd2)。

添加或移除的观察者（Observer）。

## 62.2\_详细说明（Detailed Documentation）

<a id="af15a9f085271fdc5e88180980013bfd2"></a>

### `observer`

```c
struct coap_observer* net_event_coap_observer::observer
```

添加或移除的观察者（Observer）。

<a id="a4522acf85fff0a65def80f3a7d794d2b"></a>

### `resource`

```c
struct coap_resource* net_event_coap_observer::resource
```

触发此事件的CoAP资源（Resource）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_mgmt.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h_source.html)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_net_eth_mcast_addr_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_net_event_coap_service_结构体.md)
