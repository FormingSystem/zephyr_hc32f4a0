---
id: learning.zephyr-docs.api-file-configuration-reference.page-40
title: zephyr__net__igmp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_net\_\_igmp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/igmp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

互联网组管理协议（IGMP）的API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
```

查看此文件的源码。

互联网组管理协议（IGMP）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 40.1\_数据结构（Data Structures）

<a id="r_igmp_5Fparam"></a>

```c
struct igmp_param
```

相关声明：[igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)。

互联网组管理协议（IGMP）的参数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 40.2\_函数（Functions）

<a id="r_gad41f6f3d566de753a35e346bb2819a2b"></a>

```c
static int net_ipv4_igmp_join (struct net_if *iface, const struct net_in_addr *addr, const struct igmp_param *param)
```

相关声明：[net_ipv4_igmp_join](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gad41f6f3d566de753a35e346bb2819a2b)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)、[igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)。

加入给定的多播组（Multicast Group）。

<a id="r_gaf694dd42fb040c2aecf4638383f2a919"></a>

```c
static int net_ipv4_igmp_leave (struct net_if *iface, const struct net_in_addr *addr)
```

相关声明：[net_ipv4_igmp_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gaf694dd42fb040c2aecf4638383f2a919)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)。

离开给定的多播组（Multicast Group）。


## 40.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P344_igmp.h_源码浏览.md)
- [igmp_param](../network_service_model_reference/P025_igmp_param_结构体.md)
- [net_ipv4_igmp_join](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gad41f6f3d566de753a35e346bb2819a2b)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in_addr](../network_core_model_reference/P096_net_in_addr_结构体.md)
- [net_ipv4_igmp_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__igmp.html#gaf694dd42fb040c2aecf4638383f2a919)

<a id="header-details"></a>

---

[上一章](P039_zephyr__drivers__i2c_emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__drivers__sensor__ina2xx.h_文件参考.md)
