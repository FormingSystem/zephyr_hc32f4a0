---
id: learning.zephyr-docs.networking.api-190
title: MCP工具记录结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__record.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第190章\_MCP工具记录结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__record.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 190.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

工具定义结构（Tool Definition Structure）。

```c
#include <zephyr/net/mcp/mcp_server.h>
```

工具定义结构（Tool Definition Structure）。注意：MCP 服务器在内部使用 `refcount` 跟踪工具执行状态，防止工具仍在执行时被移除。

## 190.2\_数据成员（Data Fields）

<a id="r_a73b011610654fc8bf1fffd07c0ff9dde"></a>

```c
struct mcp_tool_metadata metadata
```

工具元数据。

相关声明：[mcp_tool_metadata](P189_MCP工具元数据结构.md)。

<a id="r_a170d9355504262208defe6e4cb75f509"></a>

```c
atomic_t refcount
```

内部引用计数（Reference Count）。

<a id="r_a24e2b950dedb31b39ff503d1c8966b78"></a>

```c
mcp_tool_callback_t callback
```

工具回调，对应 `tools/call`。

相关声明：[mcp_tool_callback_t](P183_MCP完整API参考.md#ga5614c519ddad03f9cc51c7354b7029f1)。

## 190.3\_详细说明（Detailed Documentation）

<a id="a24e2b950dedb31b39ff503d1c8966b78"></a>

### `callback`

```c
mcp_tool_callback_t mcp_tool_record::callback
```

工具回调，对应 `tools/call`。

<a id="a73b011610654fc8bf1fffd07c0ff9dde"></a>

### `metadata`

```c
struct mcp_tool_metadata mcp_tool_record::metadata
```

工具元数据。

<a id="a170d9355504262208defe6e4cb75f509"></a>

### `refcount`

```c
atomic_t mcp_tool_record::refcount
```

内部引用计数（Reference Count）。

## 190.4\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

> 译注：`refcount` 是服务器内部维护的原子引用计数（Atomic Reference Count），用于保护正在执行的工具；应用不应靠手动改写它强制移除工具。应使用移除接口并处理 `-EBUSY`，参见[完整 API 参考](P183_MCP完整API参考.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P189_MCP工具元数据结构.md) · [返回大纲](大纲.md) · [下一章](P191_OCPP完整API参考.md)
