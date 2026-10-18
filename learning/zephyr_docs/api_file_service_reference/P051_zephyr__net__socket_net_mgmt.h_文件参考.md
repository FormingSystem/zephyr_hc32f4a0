---
id: learning.zephyr-docs.api-file-service-reference.page-51
title: zephyr__net__socket_net_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_net\_\_socket\_net\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socket__net__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

NET_MGMT套接字（Socket）的定义。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_mgmt.h>
```

查看此文件的源码。

网络管理套接字定义（NET_MGMT Socket Definitions）。用于支持 NET_MGMT 套接字（Sockets）的定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 51.1\_数据结构（Data Structures）

<a id="r_net_5Fmgmt_5Fmsghdr"></a>

```c
struct net_mgmt_msghdr
```

相关声明：[net_mgmt_msghdr](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md)。

每条网络管理消息（Network Management Message）都以前置的此头部开始。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 51.2\_宏定义（Macros）

<a id="r_ga8ae9629a7869b3214f8b2f72aef545ee"></a>

```c
#define NET_MGMT_SOCKET_VERSION_1 0x0001
```

相关声明：[NET_MGMT_SOCKET_VERSION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga8ae9629a7869b3214f8b2f72aef545ee)。

消息版本（Message Version）放置在头部（Header）中。

<a id="define-members-0"></a>

### NET_MGMT 套接字选项（Socket Options）

<a id="r_ga3d81f8a1f284a6ab2ac0a0a42a5dc793"></a>

```c
#define SO_NET_MGMT_ETHERNET_SET_QAV_PARAM 1
```

相关声明：[SO_NET_MGMT_ETHERNET_SET_QAV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga3d81f8a1f284a6ab2ac0a0a42a5dc793)。

设置以太网 Qav 参数（Ethernet Qav Parameters）。

<a id="r_ga6cf79af1501bdcce6e559f7636c1a2d3"></a>

```c
#define SO_NET_MGMT_ETHERNET_GET_QAV_PARAM 2
```

相关声明：[SO_NET_MGMT_ETHERNET_GET_QAV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga6cf79af1501bdcce6e559f7636c1a2d3)。

获取以太网 Qav 参数（Ethernet Qav Parameters）。


## 51.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h_source.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h_source.html)
- [zephyr/net/net_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P054_socket_net_mgmt.h_源码浏览.md)
- [net_mgmt_msghdr](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md)
- [NET_MGMT_SOCKET_VERSION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga8ae9629a7869b3214f8b2f72aef545ee)
- [SO_NET_MGMT_ETHERNET_SET_QAV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga3d81f8a1f284a6ab2ac0a0a42a5dc793)
- [SO_NET_MGMT_ETHERNET_GET_QAV_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html#ga6cf79af1501bdcce6e559f7636c1a2d3)

<a id="header-details"></a>

---

[上一章](P050_zephyr__dt-bindings__pinctrl__si32-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__bluetooth__mesh__sol_pdu_rpl_cli.h_文件参考.md)
