---
id: learning.zephyr-docs.api-service-topic-reference.page-7
title: CoAP 管理器事件（CoAP Manager Events）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_CoAP 管理器事件（CoAP Manager Events）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP 管理器事件（CoAP Manager Events）

<a id="details"></a>

CoAP 管理器事件（CoAP Manager Events）。

自 3.6 版提供（Since 3.6）；接口版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_net_5Fevent_5Fcoap_5Fservice"></a>

```c
struct net_event_coap_service
```

相关声明：[net_event_coap_service](../network_core_model_reference/P063_net_event_coap_service_结构体.md)。

CoAP服务（Service）的事件结构。

<a id="r_net_5Fevent_5Fcoap_5Fobserver"></a>

```c
struct net_event_coap_observer
```

相关声明：[net_event_coap_observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md)。

CoAP观察者（Observer）的事件结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga3b46cdbe035664256827049e4913643d"></a>

```c
#define NET_EVENT_COAP_SERVICE_STARTED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STARTED)
```

相关声明：[NET_EVENT_COAP_SERVICE_STARTED](#ga3b46cdbe035664256827049e4913643d)。

服务（Service）启动时产生的 `coap_mgmt` 事件（Event）。

<a id="r_ga9a43c93ef72e152b17992af238507b9d"></a>

```c
#define NET_EVENT_COAP_SERVICE_STOPPED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STOPPED)
```

相关声明：[NET_EVENT_COAP_SERVICE_STOPPED](#ga9a43c93ef72e152b17992af238507b9d)。

服务（Service）停止时产生的 `coap_mgmt` 事件（Event）。

<a id="r_gaf29083f98f6aa9e7f5192ee7f0504959"></a>

```c
#define NET_EVENT_COAP_OBSERVER_ADDED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_ADDED)
```

相关声明：[NET_EVENT_COAP_OBSERVER_ADDED](#gaf29083f98f6aa9e7f5192ee7f0504959)。

向资源（Resource）添加观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。

<a id="r_ga6b56912cf30fa27cc2ccf27805274c69"></a>

```c
#define NET_EVENT_COAP_OBSERVER_REMOVED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_REMOVED)
```

相关声明：[NET_EVENT_COAP_OBSERVER_REMOVED](#ga6b56912cf30fa27cc2ccf27805274c69)。

从资源（Resource）移除观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。

## 7.3\_详细说明（Detailed Documentation）

<a id="gaf29083f98f6aa9e7f5192ee7f0504959"></a>

### `NET_EVENT_COAP_OBSERVER_ADDED`

```c
#define NET_EVENT_COAP_OBSERVER_ADDED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_ADDED)
```

```c
#include <zephyr/net/coap_mgmt.h>
```

向资源（Resource）添加观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。

<a id="ga6b56912cf30fa27cc2ccf27805274c69"></a>

### `NET_EVENT_COAP_OBSERVER_REMOVED`

```c
#define NET_EVENT_COAP_OBSERVER_REMOVED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_REMOVED)
```

```c
#include <zephyr/net/coap_mgmt.h>
```

从资源（Resource）移除观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。

<a id="ga3b46cdbe035664256827049e4913643d"></a>

### `NET_EVENT_COAP_SERVICE_STARTED`

```c
#define NET_EVENT_COAP_SERVICE_STARTED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STARTED)
```

```c
#include <zephyr/net/coap_mgmt.h>
```

服务（Service）启动时产生的 `coap_mgmt` 事件（Event）。

<a id="ga9a43c93ef72e152b17992af238507b9d"></a>

### `NET_EVENT_COAP_SERVICE_STOPPED`

```c
#define NET_EVENT_COAP_SERVICE_STOPPED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STOPPED)
```

```c
#include <zephyr/net/coap_mgmt.h>
```

服务（Service）停止时产生的 `coap_mgmt` 事件（Event）。


## 7.4\_原页交叉引用（Cross References）

- [net_event_coap_service](../network_core_model_reference/P063_net_event_coap_service_结构体.md)
- [net_event_coap_observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md)
- [zephyr/net/coap_mgmt.h](../api_file_service_reference/P004_zephyr__net__coap_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_德州仪器（Texas Instruments）TI SCI.md) · [返回大纲](大纲.md) · [下一章](P008_CS35L5X API主题.md)
