---
id: learning.zephyr-docs.networking.api-100
title: Latmon头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/latmon_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_Latmon头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/latmon_8h.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 100.1\_阅读说明与来源

译注：先读[Latmon网络服务](P094_Latmon网络延迟监测服务.md)与[客户端示例](P095_Latmon客户端示例.md)，再查本组接口。

本组：[完整API参考](P099_Latmon完整API参考.md) · [头文件参考](P100_Latmon头文件参考.md) · [头文件源码](P101_Latmon头文件源码.md)。

延迟监测器应用程序编程接口（Latency Monitor API）。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/net/net_ip.h>
```

延迟监测器应用程序编程接口（Latency Monitor API）。

## 100.2\_类型定义（Typedefs）

<a id="r_ga16b7b3ed71c2726564875e183a800de7"></a>

```c
typedef int(* net_latmon_measure_t) (uint32_t *delta)
```

用于取得延迟差值（Latency Delta）的回调函数类型（Callback Function Type）。

相关声明：[net_latmon_measure_t](P099_Latmon完整API参考.md#ga16b7b3ed71c2726564875e183a800de7)。

## 100.3\_函数（Functions）

<a id="r_ga36586599ee161959414097dbbd54a2d3"></a>

```c
void net_latmon_start (int latmus, net_latmon_measure_t measure_func)
```

启动延迟监测器。

相关声明：[net_latmon_start](P099_Latmon完整API参考.md#ga36586599ee161959414097dbbd54a2d3)、[net_latmon_measure_t](P099_Latmon完整API参考.md#ga16b7b3ed71c2726564875e183a800de7)。

<a id="r_ga6c8ad5a0a35ea7ef098c024ec142edc7"></a>

```c
int net_latmon_connect (int socket, struct net_in_addr *ip)
```

等待Latmus服务发起连接。

相关声明：[net_latmon_connect](P099_Latmon完整API参考.md#ga6c8ad5a0a35ea7ef098c024ec142edc7)。

<a id="r_ga48e9ce13fd948701739fcc2cd9e1a6b0"></a>

```c
int net_latmon_get_socket (struct net_sockaddr *bind_addr)
```

取得用于Latmus服务的套接字。

相关声明：[net_latmon_get_socket](P099_Latmon完整API参考.md#ga48e9ce13fd948701739fcc2cd9e1a6b0)。

<a id="r_ga968ebd93287d3968695c0dfebc7493d1"></a>

```c
bool net_latmon_running (void)
```

检查延迟监测器是否正在运行。

相关声明：[net_latmon_running](P099_Latmon完整API参考.md#ga968ebd93287d3968695c0dfebc7493d1)。

## 100.4\_相关源码与接口边界

此页声明来自`<zephyr/net/latmon.h>`。本仓库的[对应头文件](../../../include/zephyr/net/latmon.h)可用于源码跟踪；仓库版本可能与官网`latest`不同。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P099_Latmon完整API参考.md) · [返回大纲](大纲.md) · [下一章](P101_Latmon头文件源码.md)
