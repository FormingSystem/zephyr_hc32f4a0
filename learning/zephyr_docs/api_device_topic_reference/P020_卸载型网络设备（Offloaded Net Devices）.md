---
id: learning.zephyr-docs.api-device-topic-reference.page-20
title: 卸载型网络设备（Offloaded Net Devices）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_卸载型网络设备（Offloaded Net Devices）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__offloaded__netdev.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

卸载型网络设备（Offloaded Net Devices）

<a id="details"></a>

卸载式网络设备（Offloaded Net Devices）。自 Zephyr 3.4 起提供；API 版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 20.1\_数据结构（Data Structures）

<a id="r_offloaded_5Fif_5Fapi"></a>

```c
struct offloaded_if_api
```

相关声明：[offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)。

供卸载接口/网络设备（Offloaded Interfaces / Network Devices）使用的扩展net_if_api，可处理管理启用/停用状态变化。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.2\_枚举（Enumerations）

<a id="r_gac1980977f6da3ace33ede7949d43f81f"></a>

```c
enum offloaded_net_if_types { L2_OFFLOADED_NET_IF_TYPE_UNKNOWN , L2_OFFLOADED_NET_IF_TYPE_ETHERNET , L2_OFFLOADED_NET_IF_TYPE_MODEM , L2_OFFLOADED_NET_IF_TYPE_WIFI }
```

相关声明：[offloaded_net_if_types](#gac1980977f6da3ace33ede7949d43f81f)、[L2_OFFLOADED_NET_IF_TYPE_UNKNOWN](#ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d)、[L2_OFFLOADED_NET_IF_TYPE_ETHERNET](#ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a)、[L2_OFFLOADED_NET_IF_TYPE_MODEM](#ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21)、[L2_OFFLOADED_NET_IF_TYPE_WIFI](#ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24)。

卸载型网络设备二层类型（Offloaded Netdev L2 Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.3\_函数（Functions）

<a id="r_gad1076eacf1b1e82f70759f9b54937ced"></a>

```c
static bool net_off_is_wifi_offloaded (struct net_if *iface)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_off_is_wifi_offloaded](#gad1076eacf1b1e82f70759f9b54937ced)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

检查卸载型网络接口（Offloaded Network Interface）是否支持 Wi-Fi。

## 20.4\_详细说明（Detailed Documentation）

<a id="gac1980977f6da3ace33ede7949d43f81f"></a>

### `offloaded_net_if_types`

```c
enum offloaded_net_if_types
```

```c
#include <zephyr/net/offloaded_netdev.h>
```

卸载型网络设备二层类型（Offloaded Netdev L2 Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `L2_OFFLOADED_NET_IF_TYPE_UNKNOWN` | 未知，设备尚未注册类型。 |
| `L2_OFFLOADED_NET_IF_TYPE_ETHERNET` | 以太网设备（Ethernet devices）。 |
| `L2_OFFLOADED_NET_IF_TYPE_MODEM` | 调制解调器（Modem）。 |
| `L2_OFFLOADED_NET_IF_TYPE_WIFI` | IEEE 802.11 Wi-Fi。 |

<a id="gad1076eacf1b1e82f70759f9b54937ced"></a>

### `net_off_is_wifi_offloaded()`

```c
bool net_off_is_wifi_offloaded ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/offloaded_netdev.h>
```

检查卸载型网络接口（Offloaded Network Interface）是否支持 Wi-Fi。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向网络接口（network interface）的指针。 |

**返回（Returns）**：返回值：接口支持 Wi-Fi 时为 true，否则为 false。


## 20.5\_原页交叉引用（Cross References）

- [offloaded_if_api](../network_service_model_reference/P038_offloaded_if_api_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/offloaded_netdev.h](../api_file_runtime_reference/P049_zephyr__net__offloaded_netdev.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac1980977f6da3ace33ede7949d43f81fa46a984d855ea5731207274149b12de1d"></a>
<a id="ggac1980977f6da3ace33ede7949d43f81fa532f2d2684118c1c7e78064b5bd7920a"></a>
<a id="ggac1980977f6da3ace33ede7949d43f81fa85328162750725aae17aa0d84a4dab21"></a>
<a id="ggac1980977f6da3ace33ede7949d43f81fab764b4fe8932593599bd26b9ebf11f24"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_接收端（Sinks）.md) · [返回大纲](大纲.md) · [下一章](P021_一次性可编程存储器（One Time Programmable Memory）.md)
