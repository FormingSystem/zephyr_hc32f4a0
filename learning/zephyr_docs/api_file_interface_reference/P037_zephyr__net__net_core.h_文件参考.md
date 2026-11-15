---
id: learning.zephyr-docs.api-file-interface-reference.page-37
title: zephyr__net__net_core.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_net\_\_net\_core.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__core_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络核心定义（Network Core Definitions）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <string.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/kernel.h>
#include <zephyr/net/net_timeout.h>
#include <zephyr/net/net_linkaddr.h>
```

查看此文件的源码。

网络核心定义（Network core definitions）：用于网络支持的定义。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 37.1\_枚举（Enumerations）

<a id="r_ga8e5393f3bdd85491f221324e637c3896"></a>

```c
enum net_verdict { NET_OK , NET_CONTINUE , NET_DROP }
```

相关声明：[net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)、[NET_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)、[NET_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)、[NET_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)。

网络处理裁决（Net Verdict）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.2\_函数（Functions）

<a id="r_ga3421119d2b1797ee5d70f736a61f93b7"></a>

```c
int net_recv_data (struct net_if *iface, struct net_pkt *pkt)
```

相关声明：[net_recv_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga3421119d2b1797ee5d70f736a61f93b7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

收到网络数据包（network packet）时，由下层网络协议栈或网络设备驱动程序调用。

<a id="r_gaade26b02f8fbac7989fe1b021269b08c"></a>

```c
int net_try_send_data (struct net_pkt *pkt, k_timeout_t timeout)
```

相关声明：[net_try_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gaade26b02f8fbac7989fe1b021269b08c)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

尝试向网络发送数据。

<a id="r_ga815b4cf2db95b80bfd9a576f12ebf6ff"></a>

```c
static int net_send_data (struct net_pkt *pkt)
```

相关声明：[net_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga815b4cf2db95b80bfd9a576f12ebf6ff)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

向网络发送数据。


## 37.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [string.h](../api_source_supplement_reference/P216_string.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net/net_timeout.h](../time_headers_reference/P010_网络超时头文件源码.md)
- [zephyr/net/net_linkaddr.h](../api_source_reference/P576_net_linkaddr.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [NET_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047)
- [NET_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f)
- [NET_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3)
- [net_recv_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga3421119d2b1797ee5d70f736a61f93b7)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_try_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#gaade26b02f8fbac7989fe1b021269b08c)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_send_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga815b4cf2db95b80bfd9a576f12ebf6ff)

<a id="header-details"></a>

---

[上一章](P036_zephyr__drivers__mfd__nct38xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__dt-bindings__gpio__nordic-npm6001-gpio.h_文件参考.md)
