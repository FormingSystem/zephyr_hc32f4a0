---
id: learning.zephyr-docs.api-file-service-reference.page-39
title: zephyr__net__promiscuous.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_net\_\_promiscuous.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/promiscuous_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络接口混杂模式（Promiscuous Mode）的支持。

<a id="details"></a>

```c
#include <zephyr/net/net_pkt.h>
#include <zephyr/net/net_if.h>
```

查看此文件的源码。

网络接口混杂模式支持（Network Interface Promiscuous Mode Support）。这是供应用程序开始监听网络流量（Network Traffic）的 API，需要网络设备驱动（Network Device Driver）和应用程序双方支持。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.1\_函数（Functions）

<a id="r_ga2fc01f791b635c54e85346cf898b324e"></a>

```c
static struct net_pkt * net_promisc_mode_wait_data (k_timeout_t timeout)
```

相关声明：[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[net_promisc_mode_wait_data](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga2fc01f791b635c54e85346cf898b324e)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

开始等待接收网络数据包（Network Packets）。

<a id="r_gac1a4b50b547d0f4b9396d71eecafd926"></a>

```c
static int net_promisc_mode_on (struct net_if *iface)
```

相关声明：[net_promisc_mode_on](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#gac1a4b50b547d0f4b9396d71eecafd926)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为给定网络接口（Network Interface）启用混杂模式（Promiscuous Mode）。

<a id="r_ga089aebe5ce5b6ffc48b485d361bf9e7a"></a>

```c
static int net_promisc_mode_off (struct net_if *iface)
```

相关声明：[net_promisc_mode_off](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga089aebe5ce5b6ffc48b485d361bf9e7a)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

为给定网络接口（Network Interface）禁用混杂模式（Promiscuous Mode）。


## 39.2\_原页交叉引用（Cross References）

- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P674_promiscuous.h_源码浏览.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_promisc_mode_wait_data](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga2fc01f791b635c54e85346cf898b324e)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_promisc_mode_on](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#gac1a4b50b547d0f4b9396d71eecafd926)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_promisc_mode_off](https://docs.zephyrproject.org/latest/doxygen/html/group__promiscuous.html#ga089aebe5ce5b6ffc48b485d361bf9e7a)

<a id="header-details"></a>

---

[上一章](P038_zephyr__drivers__pinctrl__pinctrl_soc_sam_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__psa__ps_ids.h_文件参考.md)
