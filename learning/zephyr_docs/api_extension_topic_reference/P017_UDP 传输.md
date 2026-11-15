---
id: learning.zephyr-docs.api-extension-topic-reference.page-17
title: UDP 传输
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_UDP 传输

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__udp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

允许通过 UDP 使用 MCUmgr SMP 协议。

<a id="details"></a>

允许通过 UDP 使用 MCUmgr SMP 协议。

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_smp_5Fudp_2Eh"></a>

```c
file smp_udp.h
```

相关声明：[smp_udp.h](../api_file_runtime_reference/P060_zephyr__mgmt__mcumgr__transport__smp_udp.h_文件参考.md)。

MCUmgr简单管理协议（SMP）的UDP传输。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.2\_函数（Functions）

<a id="r_ga768f36cea02d7d7781113d36516e1763"></a>

```c
int smp_udp_open (void)
```

相关声明：[smp_udp_open](#ga768f36cea02d7d7781113d36516e1763)。

启用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads）；这些线程将打开套接字（Socket）并监听请求（Requests）。

<a id="r_gadd428f3ed2ae0d9e580e45897a98a293"></a>

```c
int smp_udp_close (void)
```

相关声明：[smp_udp_close](#gadd428f3ed2ae0d9e580e45897a98a293)。

禁用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads），并关闭已打开的套接字（Sockets）。

<a id="r_gab11963f5889b4180b6a50e3e2cf46614"></a>

```c
int smp_client_udp_set_host_addr (struct smp_client_object *obj, struct net_sockaddr *addr)
```

相关声明：[smp_client_udp_set_host_addr](#gab11963f5889b4180b6a50e3e2cf46614)、[smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

设置 `smp_client_object` 的主机地址（Host Address）。

## 17.3\_详细说明（Detailed Documentation）

<a id="gab11963f5889b4180b6a50e3e2cf46614"></a>

### `smp_client_udp_set_host_addr()`

```c
int smp_client_udp_set_host_addr ( struct smp_client_object * obj, struct net_sockaddr * addr )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_udp.h>
```

设置 `smp_client_object` 的主机地址（Host Address）。

**说明（Note）**：注意（Note）：只要 `obj` 仍有效，`addr` 就必须保持有效。

返回（Returns）：成功时为 0；失败时为负错误号（`-errno`）。

<a id="gadd428f3ed2ae0d9e580e45897a98a293"></a>

### `smp_udp_close()`

```c
int smp_udp_close ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_udp.h>
```

禁用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads），并关闭已打开的套接字（Sockets）。

**说明（Note）**：注意（Note）：此 API 不是线程安全的（Not Thread Safe）。

返回（Returns）：成功时为 0；失败时为负错误号（`-errno`）。

<a id="ga768f36cea02d7d7781113d36516e1763"></a>

### `smp_udp_open()`

```c
int smp_udp_open ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_udp.h>
```

启用基于 UDP 的 SMP MCUmgr 传输线程（Transport Threads）；这些线程将打开套接字（Socket）并监听请求（Requests）。

**说明（Note）**：注意（Note）：此 API 不是线程安全的（Not Thread Safe）。

返回（Returns）：成功时为 0；失败时为负错误号（`-errno`）。


## 17.4\_原页交叉引用（Cross References）

- [smp_udp.h](../api_file_runtime_reference/P060_zephyr__mgmt__mcumgr__transport__smp_udp.h_文件参考.md)
- [smp_client_object](../system_service_model_reference/P078_smp_client_object_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_操作系统管理客户端（OS Management Client）.md) · [返回大纲](大纲.md) · [下一章](P018_Zephyr 基础管理（Zephyr Basic Management）.md)
