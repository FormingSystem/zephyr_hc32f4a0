---
id: learning.zephyr-docs.api-file-service-reference.page-4
title: zephyr__net__coap_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_net\_\_coap\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP事件代码（Events Code）的公共头文件。

<a id="details"></a>

```c
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

CoAP事件代码（Events Code）的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_ga3b46cdbe035664256827049e4913643d"></a>

```c
#define NET_EVENT_COAP_SERVICE_STARTED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STARTED)
```

相关声明：[NET_EVENT_COAP_SERVICE_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga3b46cdbe035664256827049e4913643d)。

服务（Service）启动时产生的 `coap_mgmt` 事件（Event）。

<a id="r_ga9a43c93ef72e152b17992af238507b9d"></a>

```c
#define NET_EVENT_COAP_SERVICE_STOPPED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STOPPED)
```

相关声明：[NET_EVENT_COAP_SERVICE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga9a43c93ef72e152b17992af238507b9d)。

服务（Service）停止时产生的 `coap_mgmt` 事件（Event）。

<a id="r_gaf29083f98f6aa9e7f5192ee7f0504959"></a>

```c
#define NET_EVENT_COAP_OBSERVER_ADDED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_ADDED)
```

相关声明：[NET_EVENT_COAP_OBSERVER_ADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#gaf29083f98f6aa9e7f5192ee7f0504959)。

向资源（Resource）添加观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。

<a id="r_ga6b56912cf30fa27cc2ccf27805274c69"></a>

```c
#define NET_EVENT_COAP_OBSERVER_REMOVED (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_REMOVED)
```

相关声明：[NET_EVENT_COAP_OBSERVER_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga6b56912cf30fa27cc2ccf27805274c69)。

从资源（Resource）移除观察者（Observer）时产生的 `coap_mgmt` 事件（Event）。


## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P009_coap_mgmt.h_源码浏览.md)
- [net_event_coap_service](../network_core_model_reference/P063_net_event_coap_service_结构体.md)
- [net_event_coap_observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md)
- [NET_EVENT_COAP_SERVICE_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga3b46cdbe035664256827049e4913643d)
- [NET_EVENT_COAP_SERVICE_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga9a43c93ef72e152b17992af238507b9d)
- [NET_EVENT_COAP_OBSERVER_ADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#gaf29083f98f6aa9e7f5192ee7f0504959)
- [NET_EVENT_COAP_OBSERVER_REMOVED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__mgmt.html#ga6b56912cf30fa27cc2ccf27805274c69)

<a id="header-details"></a>

---

[上一章](P003_zephyr__drivers__clock_control__clock_control_silabs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dap__dap_link.h_文件参考.md)
