---
id: learning.zephyr-docs.api-file-configuration-reference.page-54
title: zephyr__net__mld.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mld_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_net\_\_mld.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mld_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

组播监听发现（Multicast Listener Discovery）的API。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

组播监听发现（Multicast Listener Discovery）的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 54.1\_函数（Functions）

<a id="r_ga102060070f1165639735487e5bd0dbc2"></a>

```c
static int net_ipv6_mld_join (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_ipv6_mld_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#ga102060070f1165639735487e5bd0dbc2)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

加入给定的多播组（Multicast Group）。

<a id="r_gada558afaf913bc67b7921d3a0de561f7"></a>

```c
static int net_ipv6_mld_leave (struct net_if *iface, const struct net_in6_addr *addr)
```

相关声明：[net_ipv6_mld_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#gada558afaf913bc67b7921d3a0de561f7)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)。

离开给定的多播组（Multicast Group）。


## 54.2\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P533_mld.h_源码浏览.md)
- [net_ipv6_mld_join](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#ga102060070f1165639735487e5bd0dbc2)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_in6_addr](../network_core_model_reference/P094_net_in6_addr_结构体.md)
- [net_ipv6_mld_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__mld.html#gada558afaf913bc67b7921d3a0de561f7)

<a id="header-details"></a>

---

[上一章](P053_zephyr__dt-bindings__clock__microchip-smartfusion2-clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__drivers__sensor__mmc56x3.h_文件参考.md)
