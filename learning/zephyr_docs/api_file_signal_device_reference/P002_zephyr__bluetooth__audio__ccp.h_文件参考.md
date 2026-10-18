---
id: learning.zephyr-docs.api-file-signal-device-reference.page-2
title: zephyr__bluetooth__audio__ccp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_audio\_\_ccp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ccp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙呼叫控制配置文件（Call Control Profile，CCP）的API。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/assigned_numbers.h>
#include <zephyr/bluetooth/audio/tbs.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

蓝牙呼叫控制配置文件（Call Control Profile，CCP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient_5Fbearers"></a>

```c
struct bt_ccp_call_control_client_bearers
```

相关声明：[bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)。

包含客户端承载信息的结构体。

<a id="r_bt_5Fccp_5Fcall_5Fcontrol_5Fclient_5Fcb"></a>

```c
struct bt_ccp_call_control_client_cb
```

相关声明：[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

保存电话承载服务（Telephone Bearer Service，TBS）客户端回调的结构体。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_ga5e5acb90cc39b5f8a4e25d8ab8a11b10"></a>

```c
int bt_ccp_call_control_server_register_bearer (const struct bt_tbs_register_param *param, struct bt_ccp_call_control_server_bearer **bearer)
```

相关声明：[bt_ccp_call_control_server_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)、[bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

注册电话承载（Telephone Bearer）。

<a id="r_gaa2486dec8a47bd7f4cd4076477e8ac4a"></a>

```c
int bt_ccp_call_control_server_unregister_bearer (struct bt_ccp_call_control_server_bearer *bearer)
```

相关声明：[bt_ccp_call_control_server_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaa2486dec8a47bd7f4cd4076477e8ac4a)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

注销电话承载（Telephone Bearer）。

<a id="r_gaae263e42d76d99d950ac535c22fe64c2"></a>

```c
int bt_ccp_call_control_server_set_bearer_provider_name (struct bt_ccp_call_control_server_bearer *bearer, const char *name)
```

相关声明：[bt_ccp_call_control_server_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaae263e42d76d99d950ac535c22fe64c2)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

设置新的承载提供方名称（Bearer Provider Name）。

<a id="r_ga0b775c233dcfd08f57322afaf6fa9bcf"></a>

```c
int bt_ccp_call_control_server_get_bearer_provider_name (struct bt_ccp_call_control_server_bearer *bearer, char *name, size_t name_size)
```

相关声明：[bt_ccp_call_control_server_get_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga0b775c233dcfd08f57322afaf6fa9bcf)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载提供方名称（Bearer Provider Name）。

<a id="r_ga4c250633e8a9ff479952f9300c8eeddd"></a>

```c
int bt_ccp_call_control_server_get_bearer_uci (struct bt_ccp_call_control_server_bearer *bearer, char uci[6U])
```

相关声明：[bt_ccp_call_control_server_get_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga4c250633e8a9ff479952f9300c8eeddd)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载的统一呼叫者标识符（UCI）。

<a id="r_gac670cf57d2f02df44ea0d82a58524242"></a>

```c
int bt_ccp_call_control_server_set_bearer_tech (struct bt_ccp_call_control_server_bearer *bearer, enum bt_bearer_tech tech)
```

相关声明：[bt_ccp_call_control_server_set_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gac670cf57d2f02df44ea0d82a58524242)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

设置新的承载技术（Bearer Technology）。

<a id="r_ga84efc07e1703536ad6a005b5c5d9fb16"></a>

```c
int bt_ccp_call_control_server_get_bearer_tech (const struct bt_ccp_call_control_server_bearer *bearer, enum bt_bearer_tech *tech)
```

相关声明：[bt_ccp_call_control_server_get_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga84efc07e1703536ad6a005b5c5d9fb16)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)、[bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)。

获取承载技术（Bearer Technology）。

<a id="r_gaf7880d2e467b0931d894231312b7ed9b"></a>

```c
int bt_ccp_call_control_server_set_bearer_uri_schemes (struct bt_ccp_call_control_server_bearer *bearer, const char *uri_schemes)
```

相关声明：[bt_ccp_call_control_server_set_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaf7880d2e467b0931d894231312b7ed9b)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

设置新的承载所支持 URI 方案列表（URI Schemes Supported List）。

<a id="r_gad8525ac242806efd70d6adbd0148a0ba"></a>

```c
int bt_ccp_call_control_server_get_bearer_uri_schemes (struct bt_ccp_call_control_server_bearer *bearer, char *uri_schemes, size_t uri_schemes_size)
```

相关声明：[bt_ccp_call_control_server_get_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gad8525ac242806efd70d6adbd0148a0ba)、[bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)。

获取承载所支持 URI 方案列表（URI Schemes Supported List）。

<a id="r_ga2a5bce65e39ba05625423308f996021d"></a>

```c
int bt_ccp_call_control_client_discover (struct bt_conn *conn, struct bt_ccp_call_control_client **out_client)
```

相关声明：[bt_ccp_call_control_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga2a5bce65e39ba05625423308f996021d)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)。

发现远程设备对电话承载服务（Telephone Bearer Service，TBS）的支持。

<a id="r_ga8c5c3907759fe02745339b9456cca05f"></a>

```c
int bt_ccp_call_control_client_register_cb (struct bt_ccp_call_control_client_cb *cb)
```

相关声明：[bt_ccp_call_control_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga8c5c3907759fe02745339b9456cca05f)、[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

注册呼叫控制客户端（Call Control Client）的回调。

<a id="r_ga534a15db3e87d63942de6ba4bd8377db"></a>

```c
int bt_ccp_call_control_client_unregister_cb (struct bt_ccp_call_control_client_cb *cb)
```

相关声明：[bt_ccp_call_control_client_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga534a15db3e87d63942de6ba4bd8377db)、[bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)。

注销呼叫控制客户端（Call Control Client）的回调。

<a id="r_gac8aa850b1e77bff1058e63be8c07c4c8"></a>

```c
int bt_ccp_call_control_client_get_bearers (struct bt_ccp_call_control_client *client, struct bt_ccp_call_control_client_bearers *bearers)
```

相关声明：[bt_ccp_call_control_client_get_bearers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac8aa850b1e77bff1058e63be8c07c4c8)、[bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)、[bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)。

获取客户端实例（Client Instance）的承载（Bearers）。

<a id="r_ga31455b659d7b20053624f79c71cefa84"></a>

```c
int bt_ccp_call_control_client_read_bearer_provider_name (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga31455b659d7b20053624f79c71cefa84)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的提供方名称（Bearer Provider Name）。

<a id="r_gac106a4de174d941e6390a1743d11f01d"></a>

```c
int bt_ccp_call_control_client_read_bearer_uci (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac106a4de174d941e6390a1743d11f01d)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的统一呼叫者标识符（Uniform Caller Identifier，UCI）。

<a id="r_gaf8df0504479ac519328d98f2ddf6db15"></a>

```c
int bt_ccp_call_control_client_read_bearer_tech (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gaf8df0504479ac519328d98f2ddf6db15)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载的技术（Bearer Technology）。

<a id="r_ga9b146acb76b6e40ae639da92c5d50941"></a>

```c
int bt_ccp_call_control_client_read_bearer_uri_schemes (struct bt_ccp_call_control_client_bearer *bearer)
```

相关声明：[bt_ccp_call_control_client_read_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga9b146acb76b6e40ae639da92c5d50941)、[bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)。

读取远程 TBS 承载所支持的 URI 方案列表（URI Schemes Supported List）。


## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/assigned_numbers.h](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [zephyr/bluetooth/audio/tbs.h](../api_source_socket_ethernet_reference/P007_tbs.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P010_ccp.h_源码浏览.md)
- [bt_ccp_call_control_client_bearers](../bluetooth_service_model_reference/P052_bt_ccp_call_control_client_bearers_结构体.md)
- [bt_ccp_call_control_client_cb](../bluetooth_service_model_reference/P053_bt_ccp_call_control_client_cb_结构体.md)
- [bt_ccp_call_control_server_register_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)
- [bt_tbs_register_param](../bluetooth_service_model_reference/P177_bt_tbs_register_param_结构体.md)
- [bt_ccp_call_control_server_bearer](../bluetooth_service_model_reference/P054_bt_ccp_call_control_server_bearer_结构体.md)
- [bt_ccp_call_control_server_unregister_bearer](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaa2486dec8a47bd7f4cd4076477e8ac4a)
- [bt_ccp_call_control_server_set_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaae263e42d76d99d950ac535c22fe64c2)
- [bt_ccp_call_control_server_get_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga0b775c233dcfd08f57322afaf6fa9bcf)
- [bt_ccp_call_control_server_get_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga4c250633e8a9ff479952f9300c8eeddd)
- [bt_ccp_call_control_server_set_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gac670cf57d2f02df44ea0d82a58524242)
- [bt_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html#ga4bf3f820b493361a9a3b393d0282420f)
- [bt_ccp_call_control_server_get_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#ga84efc07e1703536ad6a005b5c5d9fb16)
- [bt_ccp_call_control_server_set_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gaf7880d2e467b0931d894231312b7ed9b)
- [bt_ccp_call_control_server_get_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__server.html#gad8525ac242806efd70d6adbd0148a0ba)
- [bt_ccp_call_control_client_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga2a5bce65e39ba05625423308f996021d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_ccp_call_control_client](../bluetooth_service_model_reference/P050_bt_ccp_call_control_client_结构体.md)
- [bt_ccp_call_control_client_register_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga8c5c3907759fe02745339b9456cca05f)
- [bt_ccp_call_control_client_unregister_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga534a15db3e87d63942de6ba4bd8377db)
- [bt_ccp_call_control_client_get_bearers](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac8aa850b1e77bff1058e63be8c07c4c8)
- [bt_ccp_call_control_client_read_bearer_provider_name](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga31455b659d7b20053624f79c71cefa84)
- [bt_ccp_call_control_client_bearer](../bluetooth_service_model_reference/P051_bt_ccp_call_control_client_bearer_结构体.md)
- [bt_ccp_call_control_client_read_bearer_uci](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gac106a4de174d941e6390a1743d11f01d)
- [bt_ccp_call_control_client_read_bearer_tech](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#gaf8df0504479ac519328d98f2ddf6db15)
- [bt_ccp_call_control_client_read_bearer_uri_schemes](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccp__call__control__client.html#ga9b146acb76b6e40ae639da92c5d50941)

<a id="header-details"></a>

---

[上一章](P001_zephyr__dt-bindings__clock__bflb_bl808_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__sensor__ccs811.h_文件参考.md)
