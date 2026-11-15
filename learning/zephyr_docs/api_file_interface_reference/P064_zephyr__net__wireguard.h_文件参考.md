---
id: learning.zephyr-docs.api-file-interface-reference.page-64
title: zephyr__net__wireguard.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_zephyr\_\_net\_\_wireguard.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WireGuard虚拟专用网络（VPN）。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/net/socket.h>
```

查看此文件的源码。

WireGuard虚拟专用网络（VPN）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 64.1\_数据结构（Data Structures）

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

## 64.2\_宏定义（Macros）

<a id="r_ga80aaf68ba45ba249ad91fce31bd5b116"></a>

```c
#define WIREGUARD_TIMESTAMP_LEN (sizeof(uint64_t) + sizeof(uint32_t))
```

相关声明：[WIREGUARD_TIMESTAMP_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga80aaf68ba45ba249ad91fce31bd5b116)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

时间戳长度（timestamp length）：64 位秒数加 32 位纳秒数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 64.3\_函数（Functions）

<a id="r_ga0e81f216e6856b6d73be215b32d62114"></a>

```c
int wireguard_peer_add (struct wireguard_peer_config *peer_config, struct net_if **peer_iface)
```

相关声明：[wireguard_peer_add](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga0e81f216e6856b6d73be215b32d62114)、[wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

向系统添加 WireGuard 对等节点（peer）。

<a id="r_gae53430ad266fa487b822bb06c180c38c"></a>

```c
int wireguard_peer_remove (int peer_id)
```

相关声明：[wireguard_peer_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#gae53430ad266fa487b822bb06c180c38c)。

从系统移除 WireGuard 对等节点。

<a id="r_ga6a5d56dbee1d44de463362d7f2345823"></a>

```c
int wireguard_peer_keepalive (int peer_id)
```

相关声明：[wireguard_peer_keepalive](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6a5d56dbee1d44de463362d7f2345823)。

向对等节点发送 WireGuard 保活消息（keepalive message）。

<a id="r_ga6aa52085d382dc8075a870c9a151e1e3"></a>

```c
int wireguard_get_current_time (uint64_t *seconds, uint32_t *nanoseconds)
```

相关声明：[wireguard_get_current_time](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6aa52085d382dc8075a870c9a151e1e3)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取自 Unix 纪元（Unix epoch）起经过的秒数及纳秒数所表示的当前时间。


## 64.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P921_wireguard.h_源码浏览.md)
- [wireguard_allowed_ip](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md)
- [wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)
- [net_stats_vpn](../network_core_model_reference/P152_net_stats_vpn_结构体.md)
- [net_event_vpn_peer](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md)
- [WIREGUARD_TIMESTAMP_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga80aaf68ba45ba249ad91fce31bd5b116)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [wireguard_peer_add](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga0e81f216e6856b6d73be215b32d62114)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [wireguard_peer_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#gae53430ad266fa487b822bb06c180c38c)
- [wireguard_peer_keepalive](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6a5d56dbee1d44de463362d7f2345823)
- [wireguard_get_current_time](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6aa52085d382dc8075a870c9a151e1e3)

<a id="header-details"></a>

---

[上一章](P063_zephyr__usb__class__usbd_hid.h_文件参考.md) · [返回大纲](大纲.md)
