---
id: learning.zephyr-docs.networking.api-195
title: OCPP中央系统信息结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structocpp__cs__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第195章\_OCPP中央系统信息结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structocpp__cs__info.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 195.1\_阅读说明与来源

译注：先读[OCPP 充电桩协议指南](P179_OCPP充电桩协议.md)和[充电桩示例](P182_OCPP充电桩示例.md)，理解充电桩（Charge Point，CP）、中央系统（Central System，CS）、连接器（Connector）、会话（Session）与交易（Transaction）的关系，再按符号查询。

本组：[OCPP完整API参考](P191_OCPP完整API参考.md) · [OCPP头文件参考](P192_OCPP头文件参考.md) · [OCPP头文件源码](P193_OCPP头文件源码.md) · [OCPP充电桩信息结构](P194_OCPP充电桩信息结构.md) · [OCPP中央系统信息结构](P195_OCPP中央系统信息结构.md) · [OCPP的TLS凭据结构](P196_OCPP的TLS凭据结构.md) · [OCPP回调输入输出联合体](P197_OCPP回调输入输出联合体.md)。

传给 `ocpp_init` 的中央系统（Central System，CS）信息参数。

```c
#include <zephyr/net/ocpp.h>
```

传给 `ocpp_init` 的中央系统（Central System，CS）信息参数。

## 195.2\_数据成员（Data Fields）

<a id="r_a99e0021bf753cee1adbc26bb77d44423"></a>

```c
char * cs_ip
```

中央系统的 IP 地址。

<a id="r_a1f4773ddd7d806ed78c737c8e816bfe6"></a>

```c
char * ws_url
```

不包含 IP 地址和端口的 WebSocket URL。

<a id="r_ae08b92eb19e5db6c5a4ee288fd432ac5"></a>

```c
int port
```

中央系统端口号。

<a id="r_ac141083d4bfc61dcb6333527c5c4492b"></a>

```c
net_sa_family_t sa_family
```

IP 协议地址族类型，IPv4 或 IPv6。

## 195.3\_详细说明（Detailed Documentation）

<a id="a99e0021bf753cee1adbc26bb77d44423"></a>

### `cs_ip`

```c
char* ocpp_cs_info::cs_ip
```

中央系统的 IP 地址。

<a id="ae08b92eb19e5db6c5a4ee288fd432ac5"></a>

### `port`

```c
int ocpp_cs_info::port
```

中央系统端口号。

<a id="ac141083d4bfc61dcb6333527c5c4492b"></a>

### `sa_family`

```c
net_sa_family_t ocpp_cs_info::sa_family
```

IP 协议地址族类型，IPv4 或 IPv6。

<a id="a1f4773ddd7d806ed78c737c8e816bfe6"></a>

### `ws_url`

```c
char* ocpp_cs_info::ws_url
```

不包含 IP 地址和端口的 WebSocket URL。

## 195.4\_相关源码与使用边界

声明来自 `<zephyr/net/ocpp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ocpp.h)可用于源码追踪，版本可能与官网 `latest` 不同。源码核对依据为本批保存的[官方协议实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/ocpp.c)、[官方请求实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/ocpp/core.c)及[官方示例](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/ocpp/src/main.c)，摘要见[来源记录](../SOURCES.md)。

> 译注——条件成员（Conditional Member）：本批中央系统结构的 Doxygen 页面只展示 `cs_ip`、`ws_url`、`port` 与 `sa_family`。原始头文件在 `CONFIG_NET_SOCKETS_SOCKOPT_TLS` 启用时，还声明 `struct ocpp_tls_credentials creds`，保存中央系统 TLS 凭据；该成员不在所有配置下都存在。详见[TLS 凭据结构](P196_OCPP的TLS凭据结构.md)。

> 译注：`sa_family` 应填写地址族常量，例如 `NET_AF_INET` 或 `NET_AF_INET6`，不能直接把原文的“4/6”当作整数参数。当前连接代码使用 `zsock_inet_pton()` 解析 `cs_ip`，因此此字段是数字形式的 IP 地址，不能自行当作 DNS 主机名入口。`ws_url` 不含 IP 地址和端口，后者分别由 `cs_ip` 与 `port` 给出。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P194_OCPP充电桩信息结构.md) · [返回大纲](大纲.md) · [下一章](P196_OCPP的TLS凭据结构.md)
