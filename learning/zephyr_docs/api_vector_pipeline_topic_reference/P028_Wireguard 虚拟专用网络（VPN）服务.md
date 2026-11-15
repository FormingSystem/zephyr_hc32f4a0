---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-28
title: Wireguard 虚拟专用网络（VPN）服务
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_Wireguard 虚拟专用网络（VPN）服务

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wireguard 虚拟专用网络（VPN）服务

<a id="details"></a>

WireGuard 虚拟专用网络（VPN）服务。**引入版本（Since）：**4.4。**版本（Version）：**0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 28.1\_数据结构（Data Structures）

<a id="r_wireguard_5Fallowed_5Fip"></a>

```c
struct wireguard_allowed_ip
```

相关声明：[wireguard_allowed_ip](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md)。

WireGuard允许IP地址（Allowed IP Address）的结构。

<a id="r_wireguard_5Fpeer_5Fconfig"></a>

```c
struct wireguard_peer_config
```

相关声明：[wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)。

WireGuard对端配置（Peer Configuration）信息。

<a id="r_net_5Fstats_5Fvpn"></a>

```c
struct net_stats_vpn
```

相关声明：[net_stats_vpn](../network_core_model_reference/P152_net_stats_vpn_结构体.md)。

WireGuard虚拟专用网络（VPN）统计信息。

<a id="r_net_5Fevent_5Fvpn_5Fpeer"></a>

```c
struct net_event_vpn_peer
```

相关声明：[net_event_vpn_peer](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md)。

网络管理事件信息（Network Management Event Information）结构；启用CONFIG_NET_MGMT_EVENT_INFO且事件生成者提供信息时，用于传递NET_EVENT_VPN_PEER_ADD网络事件的信息。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 28.2\_宏定义（Macros）

<a id="r_ga80aaf68ba45ba249ad91fce31bd5b116"></a>

```c
#define WIREGUARD_TIMESTAMP_LEN (sizeof(uint64_t) + sizeof(uint32_t))
```

相关声明：[WIREGUARD_TIMESTAMP_LEN](#ga80aaf68ba45ba249ad91fce31bd5b116)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

时间戳长度（timestamp length）：64 位秒数加 32 位纳秒数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.3\_函数（Functions）

<a id="r_ga0e81f216e6856b6d73be215b32d62114"></a>

```c
int wireguard_peer_add (struct wireguard_peer_config *peer_config, struct net_if **peer_iface)
```

相关声明：[wireguard_peer_add](#ga0e81f216e6856b6d73be215b32d62114)、[wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

向系统添加 WireGuard 对等节点（peer）。

<a id="r_gae53430ad266fa487b822bb06c180c38c"></a>

```c
int wireguard_peer_remove (int peer_id)
```

相关声明：[wireguard_peer_remove](#gae53430ad266fa487b822bb06c180c38c)。

从系统移除 WireGuard 对等节点。

<a id="r_ga6a5d56dbee1d44de463362d7f2345823"></a>

```c
int wireguard_peer_keepalive (int peer_id)
```

相关声明：[wireguard_peer_keepalive](#ga6a5d56dbee1d44de463362d7f2345823)。

向对等节点发送 WireGuard 保活消息（keepalive message）。

<a id="r_ga6aa52085d382dc8075a870c9a151e1e3"></a>

```c
int wireguard_get_current_time (uint64_t *seconds, uint32_t *nanoseconds)
```

相关声明：[wireguard_get_current_time](#ga6aa52085d382dc8075a870c9a151e1e3)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取自 Unix 纪元（Unix epoch）起经过的秒数及纳秒数所表示的当前时间。

## 28.4\_详细说明（Detailed Documentation）

<a id="ga80aaf68ba45ba249ad91fce31bd5b116"></a>

### `WIREGUARD_TIMESTAMP_LEN`

```c
#define WIREGUARD_TIMESTAMP_LEN (sizeof(uint64_t) + sizeof(uint32_t))
```

```c
#include <zephyr/net/wireguard.h>
```

时间戳长度（timestamp length）：64 位秒数加 32 位纳秒数。

<a id="ga6aa52085d382dc8075a870c9a151e1e3"></a>

### `wireguard_get_current_time()`

```c
int wireguard_get_current_time ( uint64_t * seconds, uint32_t * nanoseconds )
```

```c
#include <zephyr/net/wireguard.h>
```

获取自 Unix 纪元（Unix epoch）起经过的秒数及纳秒数所表示的当前时间。

本函数获取当前时间的秒数和纳秒数，用于计算 WireGuard 握手（Handshake）中的时间戳（Timestamp）。用户可覆盖此函数以提供当前时间；默认实现使用 `k_uptime_get()` 获取当前时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `seconds` | 用于存放当前时间秒数的指针。 |
| `nanoseconds` | 用于存放当前时间纳秒数的指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负的 `errno` 值。

<a id="ga0e81f216e6856b6d73be215b32d62114"></a>

### `wireguard_peer_add()`

```c
int wireguard_peer_add ( struct wireguard_peer_config * peer_config, struct net_if ** peer_iface )
```

```c
#include <zephyr/net/wireguard.h>
```

向系统添加 WireGuard 对等节点（peer）。

成功时返回可用于与对端通信的虚拟网络接口（Virtual Network Interface）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer_config` | 对端配置数据（Peer Configuration Data）。 |
| `peer_iface` | 成功添加对端时，向调用者返回网络接口指针。 |

**返回（Returns）**：**返回值（Returns）：**成功返回大于 0 的对端标识（Peer ID），否则返回负的 `errno` 值。

<a id="ga6a5d56dbee1d44de463362d7f2345823"></a>

### `wireguard_peer_keepalive()`

```c
int wireguard_peer_keepalive ( int peer_id)
```

```c
#include <zephyr/net/wireguard.h>
```

向对等节点发送 WireGuard 保活消息（keepalive message）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer_id` | `wireguard_peer_add()` 返回的对端标识（Peer ID）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负的 `errno` 值。

<a id="gae53430ad266fa487b822bb06c180c38c"></a>

### `wireguard_peer_remove()`

```c
int wireguard_peer_remove ( int peer_id)
```

```c
#include <zephyr/net/wireguard.h>
```

从系统移除 WireGuard 对等节点。

成功时还会移除虚拟网络接口（Virtual Network Interface），用户将无法再与该对端通信。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `peer_id` | `wireguard_peer_add()` 返回的对端标识（Peer ID）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负的 `errno` 值。


## 28.5\_原页交叉引用（Cross References）

- [wireguard_allowed_ip](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md)
- [wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)
- [net_stats_vpn](../network_core_model_reference/P152_net_stats_vpn_结构体.md)
- [net_event_vpn_peer](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/wireguard.h](../api_file_interface_reference/P064_zephyr__net__wireguard.h_文件参考.md)
- [k_uptime_get()](../timer_reference/P086_系统时钟公共接口.md#gae3e992cd3257c23d5b26d765fcbb2b69)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_1-Wire 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P029_Xen Dom0 系统控制（sysctl）.md)
