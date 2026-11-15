---
id: learning.zephyr-docs.api-service-topic-reference.page-23
title: 套接字 NET_MGMT 库
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_套接字 NET\_MGMT 库

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__socket__net__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

套接字 NET_MGMT 库

<a id="details"></a>

网络管理套接字库（Socket NET_MGMT Library）。

自 2.0 版提供（Since 2.0）；接口版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 23.1\_数据结构（Data Structures）

<a id="r_net_5Fmgmt_5Fmsghdr"></a>

```c
struct net_mgmt_msghdr
```

相关声明：[net_mgmt_msghdr](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md)。

每条网络管理消息（Network Management Message）都以前置的此头部开始。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 23.2\_宏定义（Macros）

<a id="r_ga8ae9629a7869b3214f8b2f72aef545ee"></a>

```c
#define NET_MGMT_SOCKET_VERSION_1 0x0001
```

相关声明：[NET_MGMT_SOCKET_VERSION_1](#ga8ae9629a7869b3214f8b2f72aef545ee)。

消息版本（Message Version）放置在头部（Header）中。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 23.3\_NET_MGMT 套接字选项（Socket Options）

<a id="r_ga3d81f8a1f284a6ab2ac0a0a42a5dc793"></a>

```c
#define SO_NET_MGMT_ETHERNET_SET_QAV_PARAM 1
```

相关声明：[SO_NET_MGMT_ETHERNET_SET_QAV_PARAM](#ga3d81f8a1f284a6ab2ac0a0a42a5dc793)。

设置以太网 Qav 参数（Ethernet Qav Parameters）。

<a id="r_ga6cf79af1501bdcce6e559f7636c1a2d3"></a>

```c
#define SO_NET_MGMT_ETHERNET_GET_QAV_PARAM 2
```

相关声明：[SO_NET_MGMT_ETHERNET_GET_QAV_PARAM](#ga6cf79af1501bdcce6e559f7636c1a2d3)。

获取以太网 Qav 参数（Ethernet Qav Parameters）。

## 23.4\_详细说明（Detailed Documentation）

<a id="ga8ae9629a7869b3214f8b2f72aef545ee"></a>

### `NET_MGMT_SOCKET_VERSION_1`

```c
#define NET_MGMT_SOCKET_VERSION_1 0x0001
```

```c
#include <zephyr/net/socket_net_mgmt.h>
```

消息版本（Message Version）放置在头部（Header）中。

当前有以下版本（Versions）。

网络管理消息版本（Network Management Message Versions）：

`0x0001`：`net_mgmt` 事件信息消息（Event Info Message）紧跟在头部（Header）之后。

<a id="ga6cf79af1501bdcce6e559f7636c1a2d3"></a>

### `SO_NET_MGMT_ETHERNET_GET_QAV_PARAM`

```c
#define SO_NET_MGMT_ETHERNET_GET_QAV_PARAM 2
```

```c
#include <zephyr/net/socket_net_mgmt.h>
```

获取以太网 Qav 参数（Ethernet Qav Parameters）。

<a id="ga3d81f8a1f284a6ab2ac0a0a42a5dc793"></a>

### `SO_NET_MGMT_ETHERNET_SET_QAV_PARAM`

```c
#define SO_NET_MGMT_ETHERNET_SET_QAV_PARAM 1
```

```c
#include <zephyr/net/socket_net_mgmt.h>
```

设置以太网 Qav 参数（Ethernet Qav Parameters）。


## 23.5\_原页交叉引用（Cross References）

- [net_mgmt_msghdr](../network_core_model_reference/P111_net_mgmt_msghdr_结构体.md)
- [zephyr/net/socket_net_mgmt.h](../api_file_service_reference/P051_zephyr__net__socket_net_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P022_nPM10xx 传感器接口（Sensor interface）.md) · [返回大纲](大纲.md) · [下一章](P024_串行线调试端口（SWDP）.md)
