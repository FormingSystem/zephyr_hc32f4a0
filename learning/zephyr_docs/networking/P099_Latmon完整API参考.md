---
id: learning.zephyr-docs.networking.api-99
title: Latmon完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__latmon.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_Latmon完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__latmon.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 99.1\_阅读说明与来源

译注：先读[Latmon网络服务](P094_Latmon网络延迟监测服务.md)与[客户端示例](P095_Latmon客户端示例.md)，再查本组接口。

本组：[完整API参考](P099_Latmon完整API参考.md) · [头文件参考](P100_Latmon头文件参考.md) · [头文件源码](P101_Latmon头文件源码.md)。

延迟监测器（Latency Monitor）。

延迟监测器（Latency Monitor）。

## 99.2\_类型定义（Typedefs）

<a id="r_ga16b7b3ed71c2726564875e183a800de7"></a>

```c
typedef int(* net_latmon_measure_t) (uint32_t *delta)
```

用于取得延迟差值（Latency Delta）的回调函数类型（Callback Function Type）。

## 99.3\_函数（Functions）

<a id="r_ga36586599ee161959414097dbbd54a2d3"></a>

```c
void net_latmon_start (int latmus, net_latmon_measure_t measure_func)
```

启动延迟监测器。

<a id="r_ga6c8ad5a0a35ea7ef098c024ec142edc7"></a>

```c
int net_latmon_connect (int socket, struct net_in_addr *ip)
```

等待Latmus服务发起连接。

<a id="r_ga48e9ce13fd948701739fcc2cd9e1a6b0"></a>

```c
int net_latmon_get_socket (struct net_sockaddr *bind_addr)
```

取得用于Latmus服务的套接字。

<a id="r_ga968ebd93287d3968695c0dfebc7493d1"></a>

```c
bool net_latmon_running (void)
```

检查延迟监测器是否正在运行。

## 99.4\_详细说明（Detailed Documentation）

<a id="ga16b7b3ed71c2726564875e183a800de7"></a>

### `net_latmon_measure_t`

```c
typedef int(* net_latmon_measure_t) (uint32_t *delta)
```

```c
#include <zephyr/net/latmon.h>
```

用于取得延迟差值（Latency Delta）的回调函数类型（Callback Function Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `delta` | 指向保存计算所得延迟差值的位置的指针；差值单位为周期（Cycles）。 |

**返回（Returns）**：成功返回`0`，失败返回负的`errno`错误码。

<a id="ga6c8ad5a0a35ea7ef098c024ec142edc7"></a>

### `net_latmon_connect()`

```c
int net_latmon_connect ( int socket, struct net_in_addr * ip )
```

```c
#include <zephyr/net/latmon.h>
```

等待Latmus服务发起连接。

此函数会阻塞（Block），直到Latmus服务连接到指定套接字（Socket）。连接成功后，Latmus服务的IP地址会存入传入的`ip`结构体。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `socket` | 用于监听（Listening）的有效套接字描述符（Socket Descriptor）。 |
| `ip` | 客户端的IP地址。 |

**返回（Returns）**：成功时返回已连接到Latmus的有效客户端套接字描述符，失败时返回负的`errno`错误码。

> 译注（源码核对）：上述原注释将`ip`描述为保存Latmus客户端地址的输出参数，但当前[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/latmon.c)在5秒等待超时后，用该指针广播Latmon本设备地址，未向其写入已接受连接的对端地址。[完整示例](P095_Latmon客户端示例.md)在DHCP绑定后传入`iface->config.dhcpv4.requested_ip`。因此调用前应提供有效的本机IPv4地址，不能传入未初始化变量并等待函数填写。超时且广播成功返回`-EAGAIN`，应继续等待；轮询、广播或接受连接失败的分支实际返回`-1`，不应仅凭原注释把所有负值都当成具体`-errno`。

<a id="ga48e9ce13fd948701739fcc2cd9e1a6b0"></a>

### `net_latmon_get_socket()`

```c
int net_latmon_get_socket ( struct net_sockaddr * bind_addr)
```

```c
#include <zephyr/net/latmon.h>
```

取得用于Latmus服务的套接字。

此函数创建并返回一个用于等待Latmus连接的套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bind_addr` | 套接字要绑定（Bind）的地址。为`NULL`时，套接字绑定到第一个可用地址，并使用构建时配置的Latmus端口。 |

**返回（Returns）**：成功返回有效的套接字描述符，失败返回负的`errno`错误码。

> 译注（源码核对）：原注释的“第一个可用地址”和负`errno`约定按原样保留。当前[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/latmon/latmon.c)在参数为`NULL`时使用IPv4通配地址`NET_INADDR_ANY`和配置端口；创建、绑定、监听失败的分支返回`-1`。非空地址会复制到IPv4地址结构中，不能据通用指针类型推断该实现支持任意地址族。

<a id="ga968ebd93287d3968695c0dfebc7493d1"></a>

### `net_latmon_running()`

```c
bool net_latmon_running ( void )
```

```c
#include <zephyr/net/latmon.h>
```

检查延迟监测器是否正在运行。

此函数检查延迟监测器当前是否处于活动运行状态。

**返回（Returns）**：监测器正在运行时返回`true`；正在等待Latmus连接时返回`false`。

<a id="ga36586599ee161959414097dbbd54a2d3"></a>

### `net_latmon_start()`

```c
void net_latmon_start ( int latmus, net_latmon_measure_t measure_func )
```

```c
#include <zephyr/net/latmon.h>
```

启动延迟监测器。

此函数启动延迟监测器，使用传入的回调计算差值并测量延迟。样本（Samples）发送给已连接的Latmus服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `latmus` | 已连接到Latmus的有效套接字描述符。 |
| `measure_func` | 执行差值计算的回调函数。 |

> 译注（源码核对）：当前实现先把测量回调与连接描述符放入消息队列，再通过`k_sem_take(..., K_FOREVER)`等待本次会话结束。因此“启动”不表示立即返回；示例是在此函数返回后才继续接受下一个连接。

## 99.5\_相关源码与接口边界

此页声明来自`<zephyr/net/latmon.h>`。本仓库的[对应头文件](../../../include/zephyr/net/latmon.h)可用于源码跟踪；仓库版本可能与官网`latest`不同。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P098_zperf确定性回环吞吐量.md) · [返回大纲](大纲.md) · [下一章](P100_Latmon头文件参考.md)
