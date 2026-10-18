---
id: learning.zephyr-docs.api-file-runtime-reference.page-9
title: zephyr__net__dhcpv6.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_net\_\_dhcpv6.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dhcpv6_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

DHCPv6客户端（Client）。

查看此文件的源码。

<a id="details"></a>

DHCPv6客户端（Client）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

<a id="r_net_5Fdhcpv6_5Fparams"></a>

```c
struct net_dhcpv6_params
```

相关声明：[net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)。

DHCPv6客户端（Client）的配置参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.2\_函数（Functions）

<a id="r_gab607a476c947d0335a254304e5dc2a24"></a>

```c
void net_dhcpv6_start (struct net_if *iface, struct net_dhcpv6_params *params)
```

相关声明：[net_dhcpv6_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gab607a476c947d0335a254304e5dc2a24)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)。

在接口（Interface，`iface`）上启动 DHCPv6 客户端（Client）。

<a id="r_gaf0b903bdcd0becf06ed6b212c74097a0"></a>

```c
void net_dhcpv6_stop (struct net_if *iface)
```

相关声明：[net_dhcpv6_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gaf0b903bdcd0becf06ed6b212c74097a0)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

停止接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。

<a id="r_ga99642b89c14cb17f35b45a03a2286441"></a>

```c
void net_dhcpv6_restart (struct net_if *iface)
```

相关声明：[net_dhcpv6_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#ga99642b89c14cb17f35b45a03a2286441)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

重新启动接口（Interface，`iface`）上的 DHCPv6 客户端（Client）。


## 9.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P130_dhcpv6.h_源码浏览.md)
- [net_dhcpv6_params](../network_core_model_reference/P056_net_dhcpv6_params_结构体.md)
- [net_dhcpv6_start](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gab607a476c947d0335a254304e5dc2a24)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_dhcpv6_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#gaf0b903bdcd0becf06ed6b212c74097a0)
- [net_dhcpv6_restart](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv6.html#ga99642b89c14cb17f35b45a03a2286441)

<a id="header-details"></a>

---

[上一章](P008_zephyr__bluetooth__mesh__dfd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__drivers__otp__npm10xx.h_文件参考.md)
