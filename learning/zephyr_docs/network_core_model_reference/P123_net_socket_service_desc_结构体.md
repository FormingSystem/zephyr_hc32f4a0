---
id: learning.zephyr-docs.network-core-model-reference.page-123
title: net_socket_service_desc_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__socket__service__desc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_net\_socket\_service\_desc\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__socket__service__desc.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存套接字服务配置（Socket Service Configuration）信息的主结构。

```c
#include <zephyr/net/socket_service.h>
```

<a id="details"></a>

保存套接字服务配置信息（Socket service configuration information）的主要结构。创建 `k_work` 工作项后，当这些文件描述符（FDs）有数据到达时，就会调用 `k_work` 回调。工作队列（Workqueue）可设置为 `NULL`，此时使用系统工作队列。服务描述符（Service descriptor）应在构建时创建，再将其作为参数，用于注册需要监视的套接字。用户应创建所需套接字，设置轮询结构（Poll struct），然后在运行时注册待监视的套接字。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 123.1\_数据成员（Data Fields）

<a id="r_a08da5714fafa3f678771ea3d5204971a"></a>

```c
const char * owner
```

相关声明：[owner](#a08da5714fafa3f678771ea3d5204971a)。

所有者名称（Owner name）。

<a id="r_a62104a9136d2abd88c25480eee2b187a"></a>

```c
struct net_socket_service_event * pev
```

相关声明：[net_socket_service_event](P124_net_socket_service_event_结构体.md)、[pev](#a62104a9136d2abd88c25480eee2b187a)。

指向当前监听的服务列表（List of services）的指针。

<a id="r_a5c958339cbc98e7c4490952ce1e9fbc9"></a>

```c
int pev_len
```

相关声明：[pev_len](#a5c958339cbc98e7c4490952ce1e9fbc9)。

此服务可轮询套接字数组（Pollable socket array）的长度。

<a id="r_a480b960a8d130ded4668f355a8e5fd83"></a>

```c
int * idx
```

相关声明：[idx](#a480b960a8d130ded4668f355a8e5fd83)。

本服务的 `pollfd` 项在全局列表（Global list）中的位置。

## 123.2\_详细说明（Detailed Documentation）

<a id="a480b960a8d130ded4668f355a8e5fd83"></a>

### `idx`

```c
int* net_socket_service_desc::idx
```

本服务的 `pollfd` 项在全局列表（Global list）中的位置。

<a id="a08da5714fafa3f678771ea3d5204971a"></a>

### `owner`

```c
const char* net_socket_service_desc::owner
```

所有者名称（Owner name）。

可在调试时用于查看谁注册了此服务（Service）。

<a id="a62104a9136d2abd88c25480eee2b187a"></a>

### `pev`

```c
struct net_socket_service_event* net_socket_service_desc::pev
```

指向当前监听的服务列表（List of services）的指针。

<a id="a5c958339cbc98e7c4490952ce1e9fbc9"></a>

### `pev_len`

```c
int net_socket_service_desc::pev_len
```

此服务可轮询套接字数组（Pollable socket array）的长度。

本数据类型文档由以下文件生成：

- `zephyr/net/socket_service.h`

## 123.3\_原页交叉引用（Cross References）

- [zephyr/net/socket_service.h](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h_source.html)
- [net_socket_service_event](P124_net_socket_service_event_结构体.md)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P122_net_sockaddr_nm_结构体.md) · [返回大纲](大纲.md) · [下一章](P124_net_socket_service_event_结构体.md)
