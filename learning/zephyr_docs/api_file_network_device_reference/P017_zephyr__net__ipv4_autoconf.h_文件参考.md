---
id: learning.zephyr-docs.api-file-network-device-reference.page-17
title: zephyr__net__ipv4_autoconf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_net\_\_ipv4\_autoconf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ipv4__autoconf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

IPv4自动配置（Autoconfiguration）。

查看此文件的源码。

<a id="details"></a>

IPv4自动配置（Autoconfiguration）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.1\_枚举（Enumerations）

<a id="r_abdf8bb08f12768aad2ff95b902bdc899"></a>

```c
enum net_ipv4_autoconf_state { NET_IPV4_AUTOCONF_INIT , NET_IPV4_AUTOCONF_ASSIGNED , NET_IPV4_AUTOCONF_RENEW }
```

相关声明：[net_ipv4_autoconf_state](#abdf8bb08f12768aad2ff95b902bdc899)、[NET_IPV4_AUTOCONF_INIT](#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b)、[NET_IPV4_AUTOCONF_ASSIGNED](#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2)、[NET_IPV4_AUTOCONF_RENEW](#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674)。

IPv4 自动配置（Autoconfiguration）的当前状态。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.2\_函数（Functions）

<a id="r_a5cbac9cab526f57c9b4a8ec141dbfb99"></a>

```c
static void net_ipv4_autoconf_start (struct net_if *iface)
```

相关声明：[net_ipv4_autoconf_start](#a5cbac9cab526f57c9b4a8ec141dbfb99)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

启动 RFC 3927 定义的 IPv4 自动配置，即 IPv4 链路本地地址（Link Local）。

<a id="r_a4845fd81288d96d72bbf7e8001fd31a5"></a>

```c
static void net_ipv4_autoconf_reset (struct net_if *iface)
```

相关声明：[net_ipv4_autoconf_reset](#a4845fd81288d96d72bbf7e8001fd31a5)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

重置自动配置过程（Autoconfiguration Process）。

## 17.3\_详细说明（Detailed Documentation）

<a id="abdf8bb08f12768aad2ff95b902bdc899"></a>

### `net_ipv4_autoconf_state`

```c
enum net_ipv4_autoconf_state
```

IPv4 自动配置（Autoconfiguration）的当前状态。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NET_IPV4_AUTOCONF_INIT` | 初始化状态（Initialization State）。 |
| `NET_IPV4_AUTOCONF_ASSIGNED` | 已分配状态（Assigned State）。 |
| `NET_IPV4_AUTOCONF_RENEW` | 续期状态（Renew State）。 |

<a id="a4845fd81288d96d72bbf7e8001fd31a5"></a>

### `net_ipv4_autoconf_reset()`

```c
void net_ipv4_autoconf_reset ( struct net_if * iface)
```

声明属性：`inline`、`static`。

重置自动配置过程（Autoconfiguration Process）。

重置 IPv4 IP 自动配置（Autoconfiguration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |

<a id="a5cbac9cab526f57c9b4a8ec141dbfb99"></a>

### `net_ipv4_autoconf_start()`

```c
void net_ipv4_autoconf_start ( struct net_if * iface)
```

声明属性：`inline`、`static`。

启动 RFC 3927 定义的 IPv4 自动配置，即 IPv4 链路本地地址（Link Local）。

启动 IPv4 IP 自动配置（Autoconfiguration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 指向接口（Interface）的有效指针。 |


## 17.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P409_ipv4_autoconf.h_源码浏览.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [RFC 3927](https://datatracker.ietf.org/doc/html/rfc3927)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b"></a>
<a id="abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2"></a>
<a id="abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_zephyr__drivers__sensor__icm42x70.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__dt-bindings__sensor__lis2du12.h_文件参考.md)
