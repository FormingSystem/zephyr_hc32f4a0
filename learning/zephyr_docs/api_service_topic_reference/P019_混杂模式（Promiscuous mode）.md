---
id: learning.zephyr-docs.api-service-topic-reference.page-19
title: 混杂模式（Promiscuous mode）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_混杂模式（Promiscuous mode）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

混杂模式支持。

<a id="details"></a>

混杂模式支持（Promiscuous Mode Support）。

自 1.13 版提供（Since 1.13）；接口版本（Version）0.8.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_ga2fc01f791b635c54e85346cf898b324e"></a>

```c
static struct net_pkt * net_promisc_mode_wait_data (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_promisc_mode_wait_data](#ga2fc01f791b635c54e85346cf898b324e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

开始等待接收网络数据包（Network Packets）。

<a id="r_gac1a4b50b547d0f4b9396d71eecafd926"></a>

```c
static int net_promisc_mode_on (struct net_if *iface)
```

相关声明：[net_promisc_mode_on](#gac1a4b50b547d0f4b9396d71eecafd926)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为给定网络接口（Network Interface）启用混杂模式（Promiscuous Mode）。

<a id="r_ga089aebe5ce5b6ffc48b485d361bf9e7a"></a>

```c
static int net_promisc_mode_off (struct net_if *iface)
```

相关声明：[net_promisc_mode_off](#ga089aebe5ce5b6ffc48b485d361bf9e7a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为给定网络接口（Network Interface）禁用混杂模式（Promiscuous Mode）。

## 19.2\_详细说明（Detailed Documentation）

<a id="ga089aebe5ce5b6ffc48b485d361bf9e7a"></a>

### `net_promisc_mode_off()`

```c
int net_promisc_mode_off ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/promiscuous.h>
```

为给定网络接口（Network Interface）禁用混杂模式（Promiscuous Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

返回（Returns）：成功时为0，出错时小于0。

<a id="gac1a4b50b547d0f4b9396d71eecafd926"></a>

### `net_promisc_mode_on()`

```c
int net_promisc_mode_on ( struct net_if * iface)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/promiscuous.h>
```

为给定网络接口（Network Interface）启用混杂模式（Promiscuous Mode）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga2fc01f791b635c54e85346cf898b324e"></a>

### `net_promisc_mode_wait_data()`

```c
struct net_pkt * net_promisc_mode_wait_data ( k_timeout_t timeout)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/promiscuous.h>
```

开始等待接收网络数据包（Network Packets）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 返回前等待的时长（Wait Duration）。 |

返回（Returns）：收到的 `net_pkt`；若未收到任何数据包（Packet），则返回 `NULL`。


## 19.3\_原页交叉引用（Cross References）

- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [zephyr/net/promiscuous.h](../api_file_service_reference/P039_zephyr__net__promiscuous.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P018_PMW3610 API主题.md) · [返回大纲](大纲.md) · [下一章](P020_PTP 支持.md)
