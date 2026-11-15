---
id: learning.zephyr-docs.api-network-time-topic-reference.page-14
title: 互联网组管理协议（IGMP）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_互联网组管理协议（IGMP）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网组管理协议（Internet Group Management Protocol，IGMP）

<a id="details"></a>

互联网组管理协议（Internet Group Management Protocol，IGMP）。自 Zephyr 2.6 起提供；API 版本为 0.8.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.1\_数据结构（Data Structures）

<a id="r_igmp_5Fparam"></a>

```c
struct igmp_param
```

相关声明：[igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)。

互联网组管理协议（IGMP）的参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.2\_函数（Functions）

<a id="r_gad41f6f3d566de753a35e346bb2819a2b"></a>

```c
static int net_ipv4_igmp_join (struct net_if *iface, const struct net_in_addr *addr, const struct igmp_param *param)
```

相关声明：[net_ipv4_igmp_join](#gad41f6f3d566de753a35e346bb2819a2b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)。

加入给定的多播组（Multicast Group）。

<a id="r_gaf694dd42fb040c2aecf4638383f2a919"></a>

```c
static int net_ipv4_igmp_leave (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_ipv4_igmp_leave](#gaf694dd42fb040c2aecf4638383f2a919)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

离开给定的多播组（Multicast Group）。

## 14.3\_详细说明（Detailed Documentation）

<a id="gad41f6f3d566de753a35e346bb2819a2b"></a>

### `net_ipv4_igmp_join()`

```c
int net_ipv4_igmp_join ( struct net_if * iface, const struct net_in_addr * addr, const struct igmp_param * param )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/igmp.h>
```

加入给定的多播组（Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送加入消息（join message）的网络接口。 |
| `addr` | 要加入的多播组（multicast group）。 |
| `param` | 可选参数（optional parameters）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 多播地址已成功注册并加入。 |
| `-ENETDOWN` | 多播地址已注册，但由于网络接口处于关闭状态（down），尚未加入。接口再次启用时会加入该地址。这是非致命返回码；调用方不再需要该地址时，仍应通过 `net_ipv4_igmp_leave()` 释放它。 |
| `Other` | 其他错误均应视为致命错误，意味着该多播地址未在此接口注册。 |

<a id="gaf694dd42fb040c2aecf4638383f2a919"></a>

### `net_ipv4_igmp_leave()`

```c
int net_ipv4_igmp_leave ( struct net_if * iface, const struct net_in_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/igmp.h>
```

离开给定的多播组（Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送离开消息（leave message）的网络接口。 |
| `addr` | 要离开的多播组。 |

**返回（Returns）**：返回值：已完成离开操作时返回 0，否则返回小于 0 的值。


## 14.4\_原页交叉引用（Cross References）

- [igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [zephyr/net/igmp.h](../api_file_configuration_reference/P040_zephyr__net__igmp.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_现场可编程门阵列（FPGA）.md) · [返回大纲](大纲.md) · [下一章](P015_IIS2ICLX API主题.md)
