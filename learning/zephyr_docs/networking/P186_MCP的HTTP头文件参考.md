---
id: learning.zephyr-docs.networking.api-186
title: MCP的HTTP头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcp__server__http_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_MCP的HTTP头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcp__server__http_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 186.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

模型上下文协议（Model Context Protocol，MCP）服务器 HTTP API。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

模型上下文协议（Model Context Protocol，MCP）服务器 HTTP API。

## 186.2\_函数（Functions）

<a id="r_ab4f3566a600dfe61026a1e8da0d4c00f"></a>

```c
int mcp_server_http_init (mcp_server_ctx_t server_ctx)
```

初始化 HTTP 服务器。

相关声明：[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

<a id="r_acbc247c51cb231078107ca3e5fb996a0"></a>

```c
int mcp_server_http_start (mcp_server_ctx_t server_ctx)
```

启动 HTTP 服务器。

相关声明：[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

## 186.3\_详细说明（Detailed Documentation）

<a id="ab4f3566a600dfe61026a1e8da0d4c00f"></a>

### `mcp_server_http_init()`

```c
int mcp_server_http_init ( mcp_server_ctx_t server_ctx)
```

初始化 HTTP 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

> 译注（源码核对）：当前 HTTP 实现使用一个静态传输状态；已初始化时直接返回 `0`，不会把状态重新绑定到另一个服务器上下文。应用应按指南使用同一服务器句柄完成初始化与启动，不把重复调用视为重建独立 HTTP 实例。

<a id="acbc247c51cb231078107ca3e5fb996a0"></a>

### `mcp_server_http_start()`

```c
int mcp_server_http_start ( mcp_server_ctx_t server_ctx)
```

启动 HTTP 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

> 译注（源码核对）：当前实现会拒绝空上下文、与初始化时不同的上下文及尚未初始化的状态，返回 `-EINVAL`；随后调用 `http_server_start()` 并传回其错误。启动成功不表示客户端已连接或完成 MCP 初始化。

## 186.4\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P185_MCP服务器头文件源码.md) · [返回大纲](大纲.md) · [下一章](P187_MCP的HTTP头文件源码.md)
