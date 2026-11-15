---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-24
title: 网络核心库（Network Core Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_网络核心库（Network Core Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络核心库（Network core library）

<a id="details"></a>

网络核心库（Network Core Library）。**引入版本（Since）：**1.0。**版本（Version）：**1.0.0。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 24.1\_枚举（Enumerations）

<a id="r_ga8e5393f3bdd85491f221324e637c3896"></a>

```c
enum net_verdict { NET_OK , NET_CONTINUE , NET_DROP }
```

相关声明：[net_verdict](#ga8e5393f3bdd85491f221324e637c3896)、[NET_OK](#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)、[NET_CONTINUE](#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)、[NET_DROP](#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)。

网络处理裁决（Net Verdict）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 24.2\_函数（Functions）

<a id="r_ga3421119d2b1797ee5d70f736a61f93b7"></a>

```c
int net_recv_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_recv_data](#ga3421119d2b1797ee5d70f736a61f93b7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

收到网络数据包（network packet）时，由下层网络协议栈或网络设备驱动程序调用。

<a id="r_gaade26b02f8fbac7989fe1b021269b08c"></a>

```c
int net_try_send_data (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_try_send_data](#gaade26b02f8fbac7989fe1b021269b08c)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试向网络发送数据。

<a id="r_ga815b4cf2db95b80bfd9a576f12ebf6ff"></a>

```c
static int net_send_data (struct net_pkt *pkt)
```

相关声明：[net_send_data](#ga815b4cf2db95b80bfd9a576f12ebf6ff)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向网络发送数据。

## 24.3\_详细说明（Detailed Documentation）

<a id="ga8e5393f3bdd85491f221324e637c3896"></a>

### `net_verdict`

```c
enum net_verdict
```

```c
#include <zephyr/net/net_core.h>
```

网络处理裁决（Net Verdict）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_OK` | 数据包（Packet）已得到处理。 |
| `NET_CONTINUE` | 数据包尚未被处理，应由其他部分决定其后续处置。 |
| `NET_DROP` | 必须丢弃数据包。 |

<a id="ga3421119d2b1797ee5d70f736a61f93b7"></a>

### `net_recv_data()`

```c
int net_recv_data ( struct net_if * iface, struct net_pkt * pkt )
```

```c
#include <zephyr/net/net_core.h>
```

收到网络数据包（network packet）时，由下层网络协议栈或网络设备驱动程序调用。

本函数将数据包向上推入网络协议栈（Network Stack），以便进一步处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 接收该数据包的网络接口（Network Interface）。 |
| `pkt` | 网络数据包数据（Network Packet Data）。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga815b4cf2db95b80bfd9a576f12ebf6ff"></a>

### `net_send_data()`

```c
int net_send_data ( struct net_pkt * pkt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/net_core.h>
```

向网络发送数据。

向网络发送数据。应用程序通常不应使用此函数，因为它要求预先正确构造网络数据包。等同于以无限超时（Infinite Timeout）调用 `net_try_send_data`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，出错返回小于 0 的值。若返回值小于 0，调用者必须对 `pkt` 释放引用（Unref），以避免内存泄漏。

<a id="gaade26b02f8fbac7989fe1b021269b08c"></a>

### `net_try_send_data()`

```c
int net_try_send_data ( struct net_pkt * pkt, k_timeout_t timeout )
```

```c
#include <zephyr/net/net_core.h>
```

尝试向网络发送数据。

向网络发送数据。应用程序通常不应使用此函数，因为它要求预先正确构造网络数据包。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet）。 |
| `timeout` | 发送超时（Send Timeout）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，出错返回小于 0 的值。若返回值小于 0，调用者必须对 `pkt` 释放引用（Unref），以避免内存泄漏。


## 24.4\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/net/net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047"></a>
<a id="gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f"></a>
<a id="gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P023_管线（Pipelines）.md) · [返回大纲](大纲.md) · [下一章](P025_PCIe 主机消息信号中断（MSI）接口.md)
