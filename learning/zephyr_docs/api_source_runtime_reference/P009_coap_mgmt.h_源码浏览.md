---
id: learning.zephyr-docs.api-source-runtime-reference.page-9
title: coap_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_coap\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h.html)。

## 9.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="foldopen00081"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="agroup__wifi__mgmt_html_ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6"></a>
<a id="anet__mgmt_8h_html"></a>
<a id="astructcoap__observer_html"></a>
<a id="astructcoap__resource_html"></a>
<a id="astructnet__event__coap__observer_html"></a>
<a id="astructnet__event__coap__observer_html_a4522acf85fff0a65def80f3a7d794d2b"></a>
<a id="astructnet__event__coap__observer_html_af15a9f085271fdc5e88180980013bfd2"></a>
<a id="astructnet__event__coap__service_html"></a>
<a id="astructnet__event__coap__service_html_a66ad94d50eaf25c3dd3fa5f989a08392"></a>

```c
/*
 * Copyright (c) 2023 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_COAP_MGMT_H_
#define ZEPHYR_INCLUDE_NET_COAP_MGMT_H_

#include <zephyr/net/net_mgmt.h>

#ifdef __cplusplus
extern "C" {
#endif



/* CoAP events */
#define NET_COAP_LAYER          NET_MGMT_LAYER_L4
#define NET_COAP_CODE           NET_MGMT_LAYER_CODE_COAP
#define NET_COAP_IF_BASE        (NET_MGMT_EVENT_BIT |                   \
                                 NET_MGMT_LAYER(NET_COAP_LAYER) |       \
                                 NET_MGMT_LAYER_CODE(NET_COAP_CODE))

struct coap_service;
struct coap_resource;
struct coap_observer;

enum {
        NET_EVENT_COAP_CMD_SERVICE_STARTED_VAL,
        NET_EVENT_COAP_CMD_SERVICE_STOPPED_VAL,
        NET_EVENT_COAP_CMD_OBSERVER_ADDED_VAL,
        NET_EVENT_COAP_CMD_OBSERVER_REMOVED_VAL,

        NET_EVENT_COAP_CMD_MAX
};

BUILD_ASSERT(NET_EVENT_COAP_CMD_MAX <= NET_MGMT_MAX_COMMANDS,
             "Number of events in net_event_coap_cmd exceeds the limit");

enum net_event_coap_cmd {
        /* Service events */
        NET_MGMT_CMD(NET_EVENT_COAP_CMD_SERVICE_STARTED),
        NET_MGMT_CMD(NET_EVENT_COAP_CMD_SERVICE_STOPPED),
        /* Observer events */
        NET_MGMT_CMD(NET_EVENT_COAP_CMD_OBSERVER_ADDED),
        NET_MGMT_CMD(NET_EVENT_COAP_CMD_OBSERVER_REMOVED),
};


#define NET_EVENT_COAP_SERVICE_STARTED                  \
        (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STARTED)

#define NET_EVENT_COAP_SERVICE_STOPPED                  \
        (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_SERVICE_STOPPED)

#define NET_EVENT_COAP_OBSERVER_ADDED                   \
        (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_ADDED)

#define NET_EVENT_COAP_OBSERVER_REMOVED                 \
        (NET_COAP_IF_BASE | NET_EVENT_COAP_CMD_OBSERVER_REMOVED)

struct net_event_coap_service {
        const struct coap_service *service;
};

struct net_event_coap_observer {
        struct coap_resource *resource;
        struct coap_observer *observer;
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_COAP_MGMT_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

CoAP 事件（Events）。

### 注释 3：原第 56 行

服务事件（Service events）。

### 注释 4：原第 59 行

观察者事件（Observer events）。

### 注释 5：原第 116 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_MGMT_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__mgmt_8h.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)
- [NET_MGMT_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#ggac2638308cbb0d268831f1618cf8e1fa8ae731884669e9ee832e36b8280e9c58c6)
- [net_event_coap_service](../network_core_model_reference/P063_net_event_coap_service_结构体.md)
- [service](../network_core_model_reference/P063_net_event_coap_service_结构体.md#a66ad94d50eaf25c3dd3fa5f989a08392)
- [net_event_coap_observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md)
- [resource](../network_core_model_reference/P062_net_event_coap_observer_结构体.md#a4522acf85fff0a65def80f3a7d794d2b)
- [observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md#af15a9f085271fdc5e88180980013bfd2)
- [net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [net_event_coap_observer::resource](../network_core_model_reference/P062_net_event_coap_observer_结构体.md#a4522acf85fff0a65def80f3a7d794d2b)
- [net_event_coap_observer::observer](../network_core_model_reference/P062_net_event_coap_observer_结构体.md#af15a9f085271fdc5e88180980013bfd2)
- [net_event_coap_service::service](../network_core_model_reference/P063_net_event_coap_service_结构体.md#a66ad94d50eaf25c3dd3fa5f989a08392)

---

[上一章](P008_cleanup.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_conn_mgr_connectivity.h_源码浏览.md)
