---
id: learning.zephyr-docs.networking.api-87
title: TFTP客户端上下文
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtftpc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第87章\_TFTP客户端上下文

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtftpc.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 87.1\_阅读说明与来源

译注：先读[TFTP客户端库](P077_TFTP客户端库.md)和[客户端示例](P078_TFTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P084_TFTP完整API参考.md) · [头文件参考](P085_TFTP头文件参考.md) · [头文件源码](P086_TFTP头文件源码.md)。

TFTP客户端定义，用于保存与客户端相关的信息。

```c
#include <zephyr/net/tftp.h>
```

TFTP客户端定义，用于保存与客户端相关的信息。注意：使用`tftpc`结构体调用GET或PUT接口之前，应用必须初始化服务器地址（Server）和回调（Callback）。

## 87.2\_数据成员（Data Fields）

```c
union {
```

<a id="r_a1329fa7097603e1079f74ba02c87859e"></a>

```c
struct net_sockaddr_storage server_addr
```

指向远端TFTP服务器的套接字地址（Socket Address）。

<a id="r_ab025ed4270b0e40bf64232e83d75c386"></a>

```c
};
```

套接字地址存储（Socket Address Storage）。

<a id="r_a39a04978a6cf3826ef19993989400b60"></a>

```c
tftp_callback_t callback
```

事件通知回调（Event Notification Callback）。

相关声明：[tftp_callback_t](P084_TFTP完整API参考.md#gafc2d0fd730046b0d3781362263e68ddc)。

<a id="r_a23f6f3d19493edbdc050df6d75441f92"></a>

```c
uint8_t tftp_buf [(512+4)]
```

供内部使用的缓冲区（Internal Buffer）。

## 87.3\_详细说明（Detailed Documentation）

<a id="ab025ed4270b0e40bf64232e83d75c386"></a>

### `[union]`

```c
union { ... } tftpc
```

套接字地址存储（Socket Address Storage）。

<a id="a39a04978a6cf3826ef19993989400b60"></a>

### `callback`

```c
tftp_callback_t tftpc::callback
```

事件通知回调（Event Notification Callback）。

为`NULL`时不发送通知。

<a id="af3791441bbcaaaad3c701fc62909bfa7"></a>

### `server_addr`

```c
struct net_sockaddr_storage tftpc::server_addr
```

指向远端TFTP服务器的套接字地址（Socket Address）。

<a id="a23f6f3d19493edbdc050df6d75441f92"></a>

### `tftp_buf`

```c
uint8_t tftpc::tftp_buf[(512+4)]
```

供内部使用的缓冲区（Internal Buffer）。

## 87.4\_匿名联合体与源码对照

译注：结构体摘要中的`union { ... }`是匿名联合体（Anonymous Union），其成员共享地址存储。以下摘自同批官方源码浏览页，保留嵌套关系和没有独立详细条目的内部成员：

```c
struct tftpc {
        union {
                struct net_sockaddr_storage server_addr;
                /* Do not access this directly, use server_addr instead */
                struct net_sockaddr server;
        };

        tftp_callback_t callback;

        uint8_t tftp_buf[TFTPC_MAX_BUF_SIZE];
};
```

译注：概述沿用“初始化server”的表述；源码明确要求应用使用`server_addr`，不要直接访问兼容用成员`server`。

## 87.5\_相关头文件与源码

此页声明来自`<zephyr/net/tftp.h>`。本仓库的[对应头文件](../../../include/zephyr/net/tftp.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P086_TFTP头文件源码.md) · [返回大纲](大纲.md) · [下一章](P088_TFTP事件.md)
