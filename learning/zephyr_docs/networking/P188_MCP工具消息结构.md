---
id: learning.zephyr-docs.networking.api-188
title: MCP工具消息结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__message.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第188章\_MCP工具消息结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__message.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 188.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

工具发送的消息（响应／通知，Response/Notification）。

```c
#include <zephyr/net/mcp/mcp_server.h>
```

工具发送的消息（响应／通知，Response/Notification）。此结构用于将工具执行结果提交回 MCP 服务器。注意：对于工具响应 `MCP_USR_TOOL_RESPONSE`，`data` 应指向包含工具结果的纯文本字符串；服务器自动将其封装为单个 MCP 文本内容项（TextContent）。最大长度为 `CONFIG_MCP_TOOL_RESULT_MAX_LEN`。工具执行失败时，将 `is_error` 设置为 `true`。原文示例：`.data = "Tool execution result"`。

## 188.2\_数据成员（Data Fields）

<a id="r_a78cd6d69444ed412a52ee9bb37b30352"></a>

```c
enum mcp_tool_msg_type type
```

消息类型。

相关声明：[mcp_tool_msg_type](P183_MCP完整API参考.md#ga9897522e100bc6d84aaaf450871fc30a)。

<a id="r_a2dc79941b1942586dd0e266765d6c311"></a>

```c
int length
```

消息长度。

<a id="r_a19e7156f6e167469df002e7725ea4b38"></a>

```c
void * data
```

消息数据指针。

<a id="r_a5d874717b19d6fd604965d3a3ed7be9e"></a>

```c
bool is_error
```

指示该消息是否表示错误。

## 188.3\_详细说明（Detailed Documentation）

<a id="a19e7156f6e167469df002e7725ea4b38"></a>

### `data`

```c
void* mcp_tool_message::data
```

消息数据指针。

<a id="a5d874717b19d6fd604965d3a3ed7be9e"></a>

### `is_error`

```c
bool mcp_tool_message::is_error
```

指示该消息是否表示错误。

<a id="a2dc79941b1942586dd0e266765d6c311"></a>

### `length`

```c
int mcp_tool_message::length
```

消息长度。

<a id="a78cd6d69444ed412a52ee9bb37b30352"></a>

### `type`

```c
enum mcp_tool_msg_type mcp_tool_message::type
```

消息类型。

## 188.4\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

> 译注：`data` 的工具响应内容按原注释传纯文本，由服务器封装为 MCP `TextContent`；本页并未要求预先拼成完整 JSON-RPC 响应。`is_error` 表示工具执行结果是否失败，与提交函数的返回状态不同。通知枚举虽已声明，当前指南与实现仍未提供其完整支持，见[完整 API 参考](P183_MCP完整API参考.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P187_MCP的HTTP头文件源码.md) · [返回大纲](大纲.md) · [下一章](P189_MCP工具元数据结构.md)
