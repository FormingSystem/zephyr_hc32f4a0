---
id: learning.zephyr-docs.api-file-storage-event-reference.page-7
title: zephyr__drivers__wifi__esp_wifi__esp_wifi_mesh.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_wifi\_\_esp\_wifi\_\_esp\_wifi\_mesh.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32 Wi-Fi Mesh的公共API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/wifi.h>
```

查看此文件的源码。

ESP32 Wi-Fi 网状网络（Mesh）公共 API。此 API 为 ESP Wi-Fi Mesh 协议栈提供 Zephyr 原生接口，涵盖 Mesh 启动、应用事件回调、原始发送／接收路径，以及状态和路由表查询（Routing-table Queries）。它隐藏厂商 Mesh 头文件，使应用只依赖本 API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_esp_5Fwifi_5Fmesh_5Fevent_5Finfo"></a>

```c
struct esp_wifi_mesh_event_info
```

相关声明：[esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)。

随Mesh事件提供的信息。

<a id="r_esp_5Fwifi_5Fmesh_5Fconfig"></a>

```c
struct esp_wifi_mesh_config
```

相关声明：[esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)。

运行时可配置的Mesh凭据（Credentials）和树结构限制（Tree Limits）。

<a id="r_esp_5Fwifi_5Fmesh_5Fstatus"></a>

```c
struct esp_wifi_mesh_status
```

相关声明：[esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)。

当前Mesh状态快照（Status Snapshot）。

<a id="r_esp_5Fwifi_5Fmesh_5Faddr"></a>

```c
struct esp_wifi_mesh_addr
```

相关声明：[esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)。

Mesh节点地址（Node Address），即6字节MAC地址。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.2\_类型定义（Typedefs）

<a id="r_ga3ad7865a96ed96c1a48c9f24e74eadd2"></a>

```c
typedef void(* esp_wifi_mesh_event_cb_t) (enum esp_wifi_mesh_event event, const struct esp_wifi_mesh_event_info *info)
```

相关声明：[esp_wifi_mesh_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga3ad7865a96ed96c1a48c9f24e74eadd2)、[esp_wifi_mesh_event](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1ac5c3150d24d5f259849ff0193c2523)、[esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)。

应用 Mesh 事件回调（Event Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.3\_枚举（Enumerations）

<a id="r_ga1ac5c3150d24d5f259849ff0193c2523"></a>

```c
enum esp_wifi_mesh_event { ESP_WIFI_MESH_EVENT_STARTED , ESP_WIFI_MESH_EVENT_STOPPED , ESP_WIFI_MESH_EVENT_PARENT_CONNECTED , ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED , ESP_WIFI_MESH_EVENT_CHILD_CONNECTED , ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED , ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND , ESP_WIFI_MESH_EVENT_FIND_NETWORK , ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE , ESP_WIFI_MESH_EVENT_LAYER_CHANGE , ESP_WIFI_MESH_EVENT_TODS_REACHABLE , ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE }
```

相关声明：[esp_wifi_mesh_event](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1ac5c3150d24d5f259849ff0193c2523)、[ESP_WIFI_MESH_EVENT_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2)、[ESP_WIFI_MESH_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3)、[ESP_WIFI_MESH_EVENT_PARENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39)、[ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32)、[ESP_WIFI_MESH_EVENT_CHILD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d)、[ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716)、[ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05)、[ESP_WIFI_MESH_EVENT_FIND_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007)、[ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942)、[ESP_WIFI_MESH_EVENT_LAYER_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8)、[ESP_WIFI_MESH_EVENT_TODS_REACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1)、[ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8)。

传递给应用回调的 Wi-Fi Mesh 事件（Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga6535544200d1ff000436b5006cbd2724"></a>

```c
void esp_wifi_mesh_event_cb_register (esp_wifi_mesh_event_cb_t cb)
```

相关声明：[esp_wifi_mesh_event_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga6535544200d1ff000436b5006cbd2724)、[esp_wifi_mesh_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga3ad7865a96ed96c1a48c9f24e74eadd2)。

注册应用 Mesh 事件回调（Event Callback）。

<a id="r_ga7770e2363bf12c941c47ba5e6d69f105"></a>

```c
int esp_wifi_mesh_set_config (const struct esp_wifi_mesh_config *config)
```

相关声明：[esp_wifi_mesh_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga7770e2363bf12c941c47ba5e6d69f105)、[esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)。

设置下次 `esp_wifi_mesh_start()` 使用的 Mesh 配置（Configuration）。

<a id="r_ga75d2c1ccdc4dc058762f1be00517cd22"></a>

```c
void esp_wifi_mesh_get_config (struct esp_wifi_mesh_config *config)
```

相关声明：[esp_wifi_mesh_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga75d2c1ccdc4dc058762f1be00517cd22)、[esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)。

获取 `esp_wifi_mesh_start()` 将使用的 Mesh 配置（Configuration）。

<a id="r_ga1839da0700018e749326a870f1de972c"></a>

```c
int esp_wifi_mesh_start (void)
```

相关声明：[esp_wifi_mesh_start](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1839da0700018e749326a870f1de972c)。

启动 Wi-Fi Mesh 协议栈（Stack）。

<a id="r_ga68e0258134c3452bdd4c68f26d8a82fa"></a>

```c
int esp_wifi_mesh_send (const uint8_t *data, size_t len)
```

相关声明：[esp_wifi_mesh_send](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga68e0258134c3452bdd4c68f26d8a82fa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 Mesh 发送数据缓冲区（Data Buffer）。

<a id="r_ga1b47943d3a51c9a3242d611010471412"></a>

```c
int esp_wifi_mesh_recv (uint8_t *data, size_t *len, int timeout_ms)
```

相关声明：[esp_wifi_mesh_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1b47943d3a51c9a3242d611010471412)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 Mesh 接收数据缓冲区（Data Buffer）。

<a id="r_ga56d92972f648a8d741dcc596b5c99919"></a>

```c
void esp_wifi_mesh_get_status (struct esp_wifi_mesh_status *status)
```

相关声明：[esp_wifi_mesh_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga56d92972f648a8d741dcc596b5c99919)、[esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)。

读取当前 Mesh 状态（Status）。

<a id="r_ga62b577f30a0fc68e9967284dafb99cf3"></a>

```c
int esp_wifi_mesh_get_routing_table (struct esp_wifi_mesh_addr *macs, size_t max, size_t *count)
```

相关声明：[esp_wifi_mesh_get_routing_table](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga62b577f30a0fc68e9967284dafb99cf3)、[esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

读取 Mesh 路由表（Routing Table）中的节点地址。

<a id="r_ga274783492b9e005ddfe5c2f6d7b85172"></a>

```c
void esp_wifi_mesh_set_tods_reachable (bool reachable)
```

相关声明：[esp_wifi_mesh_set_tods_reachable](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga274783492b9e005ddfe5c2f6d7b85172)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

向 Mesh 通告根节点外部网络（toDS）的可达性（Reachability）。

<a id="r_ga2fbe0fb60b71abd4c070f26a1c7fb837"></a>

```c
void esp_wifi_mesh_bind_sta_rx (void)
```

相关声明：[esp_wifi_mesh_bind_sta_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga2fbe0fb60b71abd4c070f26a1c7fb837)。

将根节点站点上行帧（Root Station Uplink Frames）递送到站点接口（Station Interface）。

<a id="r_ga64a1e694c72b317434559e8f066d971b"></a>

```c
struct net_if * esp_wifi_mesh_netif_get (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[esp_wifi_mesh_netif_get](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga64a1e694c72b317434559e8f066d971b)。

获取 Mesh 承载以太网（Ethernet-over-mesh）的网络接口。


## 7.5\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/net/net_if.h](../api_source_network_reference/P013_net_if.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/net/wifi.h](../api_source_runtime_reference/P067_wifi.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P066_esp_wifi_mesh.h_源码浏览.md)
- [esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)
- [esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)
- [esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)
- [esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)
- [esp_wifi_mesh_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga3ad7865a96ed96c1a48c9f24e74eadd2)
- [esp_wifi_mesh_event](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1ac5c3150d24d5f259849ff0193c2523)
- [ESP_WIFI_MESH_EVENT_STARTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2)
- [ESP_WIFI_MESH_EVENT_STOPPED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3)
- [ESP_WIFI_MESH_EVENT_PARENT_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39)
- [ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32)
- [ESP_WIFI_MESH_EVENT_CHILD_CONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d)
- [ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716)
- [ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05)
- [ESP_WIFI_MESH_EVENT_FIND_NETWORK](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007)
- [ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942)
- [ESP_WIFI_MESH_EVENT_LAYER_CHANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8)
- [ESP_WIFI_MESH_EVENT_TODS_REACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1)
- [ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8)
- [esp_wifi_mesh_event_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga6535544200d1ff000436b5006cbd2724)
- [esp_wifi_mesh_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga7770e2363bf12c941c47ba5e6d69f105)
- [esp_wifi_mesh_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1839da0700018e749326a870f1de972c)
- [esp_wifi_mesh_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga75d2c1ccdc4dc058762f1be00517cd22)
- [esp_wifi_mesh_send](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga68e0258134c3452bdd4c68f26d8a82fa)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [esp_wifi_mesh_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga1b47943d3a51c9a3242d611010471412)
- [esp_wifi_mesh_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga56d92972f648a8d741dcc596b5c99919)
- [esp_wifi_mesh_get_routing_table](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga62b577f30a0fc68e9967284dafb99cf3)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [esp_wifi_mesh_set_tods_reachable](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga274783492b9e005ddfe5c2f6d7b85172)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [esp_wifi_mesh_bind_sta_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga2fbe0fb60b71abd4c070f26a1c7fb837)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [esp_wifi_mesh_netif_get](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html#ga64a1e694c72b317434559e8f066d971b)

<a id="header-details"></a>

---

[上一章](P006_zephyr__net__dns_sd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__xen__events.h_文件参考.md)
