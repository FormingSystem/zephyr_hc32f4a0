---
id: learning.zephyr-docs.api-file-runtime-reference.page-60
title: zephyr__mgmt__mcumgr__transport__smp_udp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_smp\_udp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smp__udp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr简单管理协议（SMP）的UDP传输。

<a id="details"></a>

```c
#include <zephyr/mgmt/mcumgr/smp/smp_client.h>
#include <zephyr/net/net_ip.h>
```

查看此文件的源码。

MCUmgr简单管理协议（SMP）的UDP传输。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 60.1\_函数（Functions）

<a id="r_ga768f36cea02d7d7781113d36516e1763"></a>

```c
int smp_udp_open (void)
```

相关声明：[smp_udp_open](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#ga768f36cea02d7d7781113d36516e1763)。

启用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads）；这些线程将打开套接字（Socket）并监听请求（Requests）。

<a id="r_gadd428f3ed2ae0d9e580e45897a98a293"></a>

```c
int smp_udp_close (void)
```

相关声明：[smp_udp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gadd428f3ed2ae0d9e580e45897a98a293)。

禁用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads），并关闭已打开的套接字（Sockets）。

<a id="r_gab11963f5889b4180b6a50e3e2cf46614"></a>

```c
int smp_client_udp_set_host_addr (struct smp_client_object *obj, struct net_sockaddr *addr)
```

相关声明：[smp_client_udp_set_host_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gab11963f5889b4180b6a50e3e2cf46614)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

设置 `smp_client_object` 的主机地址（Host Address）。


## 60.2\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/smp/smp_client.h](../api_source_reference/P795_smp_client.h_源码浏览.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P798_smp_udp.h_源码浏览.md)
- [smp_udp_open](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#ga768f36cea02d7d7781113d36516e1763)
- [smp_udp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gadd428f3ed2ae0d9e580e45897a98a293)
- [smp_client_udp_set_host_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html#gab11963f5889b4180b6a50e3e2cf46614)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)

<a id="header-details"></a>

---

[上一章](P059_zephyr__dt-bindings__pinctrl__smartbond-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P061_zephyr__dt-bindings__gpio__snps-designware-gpio.h_文件参考.md)
