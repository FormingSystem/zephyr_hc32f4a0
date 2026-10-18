---
id: learning.zephyr-docs.api-connection-topic-reference.page-14
title: 组播监听发现（Multicast Listener Discovery）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_组播监听发现（Multicast Listener Discovery）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组播监听器发现（Multicast Listener Discovery，MLD）

<a id="details"></a>

多播侦听者发现（Multicast Listener Discovery，MLD）。自 Zephyr 1.8 起提供；API 版本为 0.8.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.1\_函数（Functions）

<a id="r_ga102060070f1165639735487e5bd0dbc2"></a>

```c
static int net_ipv6_mld_join (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_ipv6_mld_join](#ga102060070f1165639735487e5bd0dbc2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

加入给定的多播组（Multicast Group）。

<a id="r_gada558afaf913bc67b7921d3a0de561f7"></a>

```c
static int net_ipv6_mld_leave (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_ipv6_mld_leave](#gada558afaf913bc67b7921d3a0de561f7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

离开给定的多播组（Multicast Group）。

## 14.2\_详细说明（Detailed Documentation）

<a id="ga102060070f1165639735487e5bd0dbc2"></a>

### `net_ipv6_mld_join()`

```c
int net_ipv6_mld_join ( struct net_if * iface, const struct net_in6_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/mld.h>
```

加入给定的多播组（Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送加入消息（join message）的网络接口。 |
| `addr` | 要加入的多播组（multicast group）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 多播地址已成功注册并加入。 |
| `-ENETDOWN` | 多播地址已注册，但由于网络接口处于关闭状态（down），尚未加入。接口再次启用时会加入该地址。这是非致命返回码；调用方不再需要该地址时，仍应通过 `net_ipv6_mld_leave()` 释放它。 |
| `Other` | 其他错误均应视为致命错误，意味着该多播地址未在此接口注册。 |

<a id="gada558afaf913bc67b7921d3a0de561f7"></a>

### `net_ipv6_mld_leave()`

```c
int net_ipv6_mld_leave ( struct net_if * iface, const struct net_in6_addr * addr )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/mld.h>
```

离开给定的多播组（Multicast Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 发送离开消息（leave message）的网络接口。 |
| `addr` | 要离开的多播组。 |

**返回（Returns）**：返回值：已完成离开操作时返回 0，否则返回小于 0 的值。


## 14.3\_原页交叉引用（Cross References）

- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [zephyr/net/mld.h](../api_file_configuration_reference/P054_zephyr__net__mld.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P013_MDIO 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P015_MSPI 驱动后端 API.md)
