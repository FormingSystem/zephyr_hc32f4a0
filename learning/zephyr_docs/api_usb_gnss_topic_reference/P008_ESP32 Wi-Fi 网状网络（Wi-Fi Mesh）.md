---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-8
title: ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ESP32 Wi-Fi 网状网络（Wi-Fi Mesh）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__esp__wifi__mesh.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32 Wi-Fi Mesh API

<a id="details"></a>

ESP32 Wi-Fi Mesh API。起始版本（Since）：4.5。接口版本（Version）：0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_esp_5Fwifi_5Fmesh_2Eh"></a>

```c
file esp_wifi_mesh.h
```

相关声明：[esp_wifi_mesh.h](../api_file_storage_event_reference/P007_zephyr__drivers__wifi__esp_wifi__esp_wifi_mesh.h_文件参考.md)。

ESP32 Wi-Fi Mesh的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

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

## 8.3\_类型定义（Typedefs）

<a id="r_ga3ad7865a96ed96c1a48c9f24e74eadd2"></a>

```c
typedef void(* esp_wifi_mesh_event_cb_t) (enum esp_wifi_mesh_event event, const struct esp_wifi_mesh_event_info *info)
```

相关声明：[esp_wifi_mesh_event_cb_t](#ga3ad7865a96ed96c1a48c9f24e74eadd2)、[esp_wifi_mesh_event](#ga1ac5c3150d24d5f259849ff0193c2523)、[esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)。

应用 Mesh 事件回调（Event Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.4\_枚举（Enumerations）

<a id="r_ga1ac5c3150d24d5f259849ff0193c2523"></a>

```c
enum esp_wifi_mesh_event { ESP_WIFI_MESH_EVENT_STARTED , ESP_WIFI_MESH_EVENT_STOPPED , ESP_WIFI_MESH_EVENT_PARENT_CONNECTED , ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED , ESP_WIFI_MESH_EVENT_CHILD_CONNECTED , ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED , ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND , ESP_WIFI_MESH_EVENT_FIND_NETWORK , ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE , ESP_WIFI_MESH_EVENT_LAYER_CHANGE , ESP_WIFI_MESH_EVENT_TODS_REACHABLE , ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE }
```

相关声明：[esp_wifi_mesh_event](#ga1ac5c3150d24d5f259849ff0193c2523)、[ESP_WIFI_MESH_EVENT_STARTED](#gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2)、[ESP_WIFI_MESH_EVENT_STOPPED](#gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3)、[ESP_WIFI_MESH_EVENT_PARENT_CONNECTED](#gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39)、[ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED](#gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32)、[ESP_WIFI_MESH_EVENT_CHILD_CONNECTED](#gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d)、[ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED](#gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716)、[ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND](#gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05)、[ESP_WIFI_MESH_EVENT_FIND_NETWORK](#gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007)、[ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE](#gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942)、[ESP_WIFI_MESH_EVENT_LAYER_CHANGE](#gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8)、[ESP_WIFI_MESH_EVENT_TODS_REACHABLE](#gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1)、[ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE](#gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8)。

传递给应用回调的 Wi-Fi Mesh 事件（Events）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.5\_函数（Functions）

<a id="r_ga6535544200d1ff000436b5006cbd2724"></a>

```c
void esp_wifi_mesh_event_cb_register (esp_wifi_mesh_event_cb_t cb)
```

相关声明：[esp_wifi_mesh_event_cb_register](#ga6535544200d1ff000436b5006cbd2724)、[esp_wifi_mesh_event_cb_t](#ga3ad7865a96ed96c1a48c9f24e74eadd2)。

注册应用 Mesh 事件回调（Event Callback）。

<a id="r_ga7770e2363bf12c941c47ba5e6d69f105"></a>

```c
int esp_wifi_mesh_set_config (const struct esp_wifi_mesh_config *config)
```

相关声明：[esp_wifi_mesh_set_config](#ga7770e2363bf12c941c47ba5e6d69f105)、[esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)。

设置下次 `esp_wifi_mesh_start()` 使用的 Mesh 配置（Configuration）。

<a id="r_ga75d2c1ccdc4dc058762f1be00517cd22"></a>

```c
void esp_wifi_mesh_get_config (struct esp_wifi_mesh_config *config)
```

相关声明：[esp_wifi_mesh_get_config](#ga75d2c1ccdc4dc058762f1be00517cd22)、[esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)。

获取 `esp_wifi_mesh_start()` 将使用的 Mesh 配置（Configuration）。

<a id="r_ga1839da0700018e749326a870f1de972c"></a>

```c
int esp_wifi_mesh_start (void)
```

相关声明：[esp_wifi_mesh_start](#ga1839da0700018e749326a870f1de972c)。

启动 Wi-Fi Mesh 协议栈（Stack）。

<a id="r_ga68e0258134c3452bdd4c68f26d8a82fa"></a>

```c
int esp_wifi_mesh_send (const uint8_t *data, size_t len)
```

相关声明：[esp_wifi_mesh_send](#ga68e0258134c3452bdd4c68f26d8a82fa)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 Mesh 发送数据缓冲区（Data Buffer）。

<a id="r_ga1b47943d3a51c9a3242d611010471412"></a>

```c
int esp_wifi_mesh_recv (uint8_t *data, size_t *len, int timeout_ms)
```

相关声明：[esp_wifi_mesh_recv](#ga1b47943d3a51c9a3242d611010471412)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 Mesh 接收数据缓冲区（Data Buffer）。

<a id="r_ga56d92972f648a8d741dcc596b5c99919"></a>

```c
void esp_wifi_mesh_get_status (struct esp_wifi_mesh_status *status)
```

相关声明：[esp_wifi_mesh_get_status](#ga56d92972f648a8d741dcc596b5c99919)、[esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)。

读取当前 Mesh 状态（Status）。

<a id="r_ga62b577f30a0fc68e9967284dafb99cf3"></a>

```c
int esp_wifi_mesh_get_routing_table (struct esp_wifi_mesh_addr *macs, size_t max, size_t *count)
```

相关声明：[esp_wifi_mesh_get_routing_table](#ga62b577f30a0fc68e9967284dafb99cf3)、[esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

读取 Mesh 路由表（Routing Table）中的节点地址。

<a id="r_ga274783492b9e005ddfe5c2f6d7b85172"></a>

```c
void esp_wifi_mesh_set_tods_reachable (bool reachable)
```

相关声明：[esp_wifi_mesh_set_tods_reachable](#ga274783492b9e005ddfe5c2f6d7b85172)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

向 Mesh 通告根节点外部网络（toDS）的可达性（Reachability）。

<a id="r_ga2fbe0fb60b71abd4c070f26a1c7fb837"></a>

```c
void esp_wifi_mesh_bind_sta_rx (void)
```

相关声明：[esp_wifi_mesh_bind_sta_rx](#ga2fbe0fb60b71abd4c070f26a1c7fb837)。

将根节点站点上行帧（Root Station Uplink Frames）递送到站点接口（Station Interface）。

<a id="r_ga64a1e694c72b317434559e8f066d971b"></a>

```c
struct net_if * esp_wifi_mesh_netif_get (void)
```

相关声明：[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[esp_wifi_mesh_netif_get](#ga64a1e694c72b317434559e8f066d971b)。

获取 Mesh 承载以太网（Ethernet-over-mesh）的网络接口。

## 8.6\_详细说明（Detailed Documentation）

<a id="ga3ad7865a96ed96c1a48c9f24e74eadd2"></a>

### `esp_wifi_mesh_event_cb_t`

```c
typedef void(* esp_wifi_mesh_event_cb_t) (enum esp_wifi_mesh_event event, const struct esp_wifi_mesh_event_info *info)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

应用 Mesh 事件回调（Event Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | 已发生的事件（Event）。 |
| `info` | 事件详情（Event Details）。 |

<a id="ga1ac5c3150d24d5f259849ff0193c2523"></a>

### `esp_wifi_mesh_event`

```c
enum esp_wifi_mesh_event
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

传递给应用回调的 Wi-Fi Mesh 事件（Events）。

这些定义将底层厂商 Mesh 事件抽象为稳定的 Zephyr 原生事件集合（Zephyr-native Set），使应用无须依赖厂商 Mesh 头文件。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ESP_WIFI_MESH_EVENT_STARTED` | Mesh 协议栈（Mesh Stack）已启动。 |
| `ESP_WIFI_MESH_EVENT_STOPPED` | Mesh 协议栈（Mesh Stack）已停止。 |
| `ESP_WIFI_MESH_EVENT_PARENT_CONNECTED` | 本节点已连接到父节点（Parent），参见信息中的 `is_root`。 |
| `ESP_WIFI_MESH_EVENT_PARENT_DISCONNECTED` | 本节点失去了父节点（Parent）。 |
| `ESP_WIFI_MESH_EVENT_CHILD_CONNECTED` | 一个子节点（Child Node）已连接到本节点。 |
| `ESP_WIFI_MESH_EVENT_CHILD_DISCONNECTED` | 一个子节点（Child Node）已从本节点断开。 |
| `ESP_WIFI_MESH_EVENT_NO_PARENT_FOUND` | 最近一次扫描（Scan）未找到父节点（Parent）。 |
| `ESP_WIFI_MESH_EVENT_FIND_NETWORK` | 节点已开始寻找可加入的网络（Network）。 |
| `ESP_WIFI_MESH_EVENT_ROUTING_TABLE_CHANGE` | 路由表（Routing Table）已改变，参见信息中的 `routing_table_size`。 |
| `ESP_WIFI_MESH_EVENT_LAYER_CHANGE` | 本节点的 Mesh 层级（Mesh Layer），即树深度（Tree Depth），已改变；参见信息中的 `layer`。 |
| `ESP_WIFI_MESH_EVENT_TODS_REACHABLE` | 根节点通往外部网络的路径（`toDS`）已变为可达（Reachable）。 |
| `ESP_WIFI_MESH_EVENT_TODS_UNREACHABLE` | 根节点通往外部网络的路径（`toDS`）已变为不可达（Unreachable）。 |

<a id="ga2fbe0fb60b71abd4c070f26a1c7fb837"></a>

### `esp_wifi_mesh_bind_sta_rx()`

```c
void esp_wifi_mesh_bind_sta_rx ( void )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

将根节点站点上行帧（Root Station Uplink Frames）递送到站点接口（Station Interface）。

Mesh 协议栈会安装自己的站点接收回调（Station Receive Callback）。在根节点（Root）上，站点还承担通往路由器的上行链路（Uplink），因此本操作恢复该接口的驱动接收路径。节点成为 Mesh 根节点后调用。

<a id="ga6535544200d1ff000436b5006cbd2724"></a>

### `esp_wifi_mesh_event_cb_register()`

```c
void esp_wifi_mesh_event_cb_register ( esp_wifi_mesh_event_cb_t cb)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

注册应用 Mesh 事件回调（Event Callback）。

回调运行在共享的 Wi-Fi 事件任务（Event Task）中，不得阻塞。其栈由 `CONFIG_ESP32_WIFI_EVENT_TASK_STACK_SIZE` 配置；启动 IP 协议栈、DHCP、NAT 等繁重工作应在应用自己的线程中执行，或为事件任务配置足以承担这些工作的栈大小。仅支持一个回调，重复注册会替换先前的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | Mesh 事件发生时调用的回调（Callback）；传入 `NULL` 可注销。 |

<a id="ga75d2c1ccdc4dc058762f1be00517cd22"></a>

### `esp_wifi_mesh_get_config()`

```c
void esp_wifi_mesh_get_config ( struct esp_wifi_mesh_config * config)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

获取 `esp_wifi_mesh_start()` 将使用的 Mesh 配置（Configuration）。

返回最近一次传给 `esp_wifi_mesh_set_config()` 的配置（Configuration）；若从未调用，则返回驱动内置默认值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 输出参数，填入当前配置（Configuration）。 |

<a id="ga62b577f30a0fc68e9967284dafb99cf3"></a>

### `esp_wifi_mesh_get_routing_table()`

```c
int esp_wifi_mesh_get_routing_table ( struct esp_wifi_mesh_addr * macs, size_t max, size_t * count )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

读取 Mesh 路由表（Routing Table）中的节点地址。

根节点（Root）的路由表覆盖整个子网络；内部节点（Internal Node）的路由表包含该节点自己的子树。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `macs` | 接收节点地址（Node Address）的输出数组。 |
| `max` | `macs` 可容纳的条目数（Number of Entries）。 |
| `count` | 输出参数，设为已写入的条目数（Number of Entries Written）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数为 `NULL` 时。 |

<a id="ga56d92972f648a8d741dcc596b5c99919"></a>

### `esp_wifi_mesh_get_status()`

```c
void esp_wifi_mesh_get_status ( struct esp_wifi_mesh_status * status)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

读取当前 Mesh 状态（Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 输出参数，填入当前 Mesh 状态（Mesh State）。 |

<a id="ga64a1e694c72b317434559e8f066d971b"></a>

### `esp_wifi_mesh_netif_get()`

```c
struct net_if * esp_wifi_mesh_netif_get ( void )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

获取 Mesh 承载以太网（Ethernet-over-mesh）的网络接口。

Mesh 网络接口（Mesh Netif）通过 Wi-Fi Mesh 传输承载以太网帧（Ethernet Frame），因此 Zephyr 网络协议栈无须修改即可运行在 Mesh 之上。使用返回的接口分配 IP 地址，并运行 DHCP、NAT 和路由。

**返回（Returns）**：返回值（Returns）：Mesh 网络接口（Mesh Network Interface）；初始化前为 `NULL`。

<a id="ga1b47943d3a51c9a3242d611010471412"></a>

### `esp_wifi_mesh_recv()`

```c
int esp_wifi_mesh_recv ( uint8_t * data, size_t * len, int timeout_ms )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

从 Mesh 接收数据缓冲区（Data Buffer）。

最多阻塞 `timeout_ms`，等待发往本节点的 Mesh 帧（Mesh Frame）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 用于接收的缓冲区（Receive Buffer）。 |
| `len` | 输入时为缓冲区大小（Buffer Size），输出时为已接收长度（Received Length）。 |
| `timeout_ms` | 接收超时（Receive Timeout），以毫秒为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时，`len` 更新为已接收大小（Received Size）。 |
| `-EAGAIN` | 超时前未收到帧（Frame）时。 |

**说明（Note）**：注意（Note）：启用 `CONFIG_WIFI_ESP32_MESH_IP` 时不可用，参见 `esp_wifi_mesh_send()`。

<a id="ga68e0258134c3452bdd4c68f26d8a82fa"></a>

### `esp_wifi_mesh_send()`

```c
int esp_wifi_mesh_send ( const uint8_t * data, size_t len )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

通过 Mesh 发送数据缓冲区（Data Buffer）。

在非根节点（Non-root Node）上，缓冲区被向上路由到根节点。在根节点上，缓冲区会发给路由表中的每个节点。这是面向应用消息传递的便捷路径，不使用 Mesh 上的 IP 接口（IP-over-mesh Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要发送的缓冲区（Send Buffer）。 |
| `len` | 要发送的字节数（Number of Bytes）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时，或在根节点（Root）上部分成功时。 |
| `-EIO` | 发生 Mesh 发送错误（Send Error）时。 |

**说明（Note）**：注意（Note）：启用 `CONFIG_WIFI_ESP32_MESH_IP` 时不可用。IP 接口与这条原始数据路径（Raw Path）都会从唯一的 Mesh 接收队列中取走数据，且没有分用（Demultiplexing）机制，因此帧会以不确定方式分配给两个读取方。在接收路径能够根据帧协议标签（Frame Protocol Tag）分用之前，两者保持互斥。

<a id="ga7770e2363bf12c941c47ba5e6d69f105"></a>

### `esp_wifi_mesh_set_config()`

```c
int esp_wifi_mesh_set_config ( const struct esp_wifi_mesh_config * config)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

设置下次 `esp_wifi_mesh_start()` 使用的 Mesh 配置（Configuration）。

验证每个字段；全部有效时，完整替换当前配置，不支持部分更新。失败时保留先前配置。必须在 `esp_wifi_mesh_start()` 之前调用；Mesh 不支持运行时重新配置（Runtime Reconfiguration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `config` | 要应用的配置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 参数为 `NULL`，或任一字段超出文档规定的有效范围时：字符串长度、信道（Channel）、认证模式（`authmode`）、不匹配的 `authmode`／`mesh_password` 组合，或超过编译时 Kconfig 上限的树限制（Tree Limit）。 |
| `-EBUSY` | Mesh 已处于活动状态（Active）时。 |

<a id="ga274783492b9e005ddfe5c2f6d7b85172"></a>

### `esp_wifi_mesh_set_tods_reachable()`

```c
void esp_wifi_mesh_set_tods_reachable ( bool reachable)
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

向 Mesh 通告根节点外部网络（toDS）的可达性（Reachability）。

在根节点（Root）的上行链路（Uplink）接通或断开后调用，使 Mesh 开始或停止接收子节点发往外部网络的流量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reachable` | 根节点能够向外部网络转发时为 `true`。 |

<a id="ga1839da0700018e749326a870f1de972c"></a>

### `esp_wifi_mesh_start()`

```c
int esp_wifi_mesh_start ( void )
```

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

启动 Wi-Fi Mesh 协议栈（Stack）。

执行完整的 Mesh 启动（Bring-up）：将 Wi-Fi 设为 AP+STA 模式，使用当前配置及 Mesh 调优 Kconfig 选项初始化并配置 Mesh 协议栈，禁用省电（Power Save），然后启动 Mesh。当前配置参见 `esp_wifi_mesh_set_config()`／`esp_wifi_mesh_get_config()`。

节点角色由 `WIFI_ESP32_MESH_ROLE` 选择项决定：自动角色（Auto Role）执行自组织选举（Self-organized Election），需要路由器；`WIFI_ESP32_MESH_FORCE_ROOT` 将本节点指定为固定根节点，并停止其自组织父节点搜索；`WIFI_ESP32_MESH_FORCE_CHILD` 防止节点成为根节点。

需要路由器（Router）。树围绕根节点与路由器的关联建立，子节点通过自组织父节点搜索（Self-organized Parent Search）自动接入。完全没有路由器的 Mesh 需要为每个子节点明确指定父节点，本驱动不执行这一操作，因此没有路由器时，子节点不会接入固定根节点。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 使用自动角色（Auto Role），但没有路由器 SSID 时。 |
| `-EIO` | 发生 Mesh 协议栈错误（Mesh Stack Error）时。 |

**说明（Note）**：注意（Note）：Mesh 是启动时模式（Boot-time Mode），不支持运行时拆除（Runtime Teardown）。一旦启动，就在节点的整个生命周期内保持驻留；没有停止或反初始化入口。运行期间，普通站点／软件接入点（Station/SoftAP）的 `wifi_mgmt` 操作，即 `connect`、`disconnect`、`ap_enable`、`scan`，均被拒绝。


## 8.7\_原页交叉引用（Cross References）

- [esp_wifi_mesh.h](../api_file_storage_event_reference/P007_zephyr__drivers__wifi__esp_wifi__esp_wifi_mesh.h_文件参考.md)
- [esp_wifi_mesh_event_info](../modem_wireless_model_reference/P014_esp_wifi_mesh_event_info_结构体.md)
- [esp_wifi_mesh_config](../modem_wireless_model_reference/P013_esp_wifi_mesh_config_结构体.md)
- [esp_wifi_mesh_status](../modem_wireless_model_reference/P015_esp_wifi_mesh_status_结构体.md)
- [esp_wifi_mesh_addr](../modem_wireless_model_reference/P012_esp_wifi_mesh_addr_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a4effc55eec1beaae8b9bed0bf6124ce2"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a746c61eaa6a07b1a308e64a3694cb9d3"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a63d20c75924c35d145c3f6ed76bd2b39"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523af436f81bddf53ae53129fabebfcc4c32"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a051120f6c8e06e8d8af9ced2b1853d3d"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523ad22734779b418a2e0dfcf0afae54e716"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a81544b2e377b5e0119f0c32fe6850a05"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a0aecb5ac826e1bbb299277a866560007"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523a818b192870dc294f3c3e7f9d1ab77942"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523affe5cded5aa5db5d8233dc8ce8f57bb8"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523ab99699382f6712fa0e7a79ccd5cb39a1"></a>
<a id="gga1ac5c3150d24d5f259849ff0193c2523ab830022e61381c7f390dd971b91902f8"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_瑞萨 RA 时钟分频生成器（Clock Divider Generators）.md) · [返回大纲](大纲.md) · [下一章](P009_全球导航卫星系统（GNSS）.md)
