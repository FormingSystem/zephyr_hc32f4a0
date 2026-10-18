---
id: learning.zephyr-docs.networking.api-184
title: MCP服务器头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mcp__server_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_MCP服务器头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mcp__server_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 184.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

模型上下文协议（Model Context Protocol，MCP）服务器 API。

```c
#include <zephyr/kernel.h>
```

```c
#include <errno.h>
```

模型上下文协议（Model Context Protocol，MCP）服务器 API。

## 184.2\_数据结构（Data Structures）

<a id="r_mcp_5Ftool_5Fmetadata"></a>

```c
struct mcp_tool_metadata
```

工具元数据结构（Tool Metadata Structure）。

相关声明：[mcp_tool_metadata](P189_MCP工具元数据结构.md)。

<a id="r_mcp_5Ftool_5Frecord"></a>

```c
struct mcp_tool_record
```

工具定义结构（Tool Definition Structure）。

相关声明：[mcp_tool_record](P190_MCP工具记录结构.md)。

<a id="r_mcp_5Ftool_5Fmessage"></a>

```c
struct mcp_tool_message
```

工具发送的消息（响应／通知，Response/Notification）。

相关声明：[mcp_tool_message](P188_MCP工具消息结构.md)。

## 184.3\_类型定义（Typedefs）

<a id="r_ga3e08a0cb026f941ca9d68a2636c3f33e"></a>

```c
typedef void * mcp_server_ctx_t
```

服务器上下文句柄（Server Context Handle）。

相关声明：[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

<a id="r_ga5614c519ddad03f9cc51c7354b7029f1"></a>

```c
typedef int(* mcp_tool_callback_t) (enum mcp_tool_event_type event, const char *arguments, const char *execution_token)
```

工具回调函数（Tool Callback Function）。

相关声明：[mcp_tool_callback_t](P183_MCP完整API参考.md#ga5614c519ddad03f9cc51c7354b7029f1)、[mcp_tool_event_type](P183_MCP完整API参考.md#ga4ea4339861b61e14403856a18a8ef065)。

## 184.4\_枚举（Enumerations）

<a id="r_ga9897522e100bc6d84aaaf450871fc30a"></a>

```c
enum mcp_tool_msg_type { MCP_USR_TOOL_RESPONSE , MCP_USR_TOOL_NOTIFICATION , MCP_USR_TOOL_CANCEL_ACK , MCP_USR_TOOL_PING }
```

MCP 工具消息类型（Tool Message Type）。

相关声明：[mcp_tool_msg_type](P183_MCP完整API参考.md#ga9897522e100bc6d84aaaf450871fc30a)、[MCP_USR_TOOL_RESPONSE](P183_MCP完整API参考.md#gga9897522e100bc6d84aaaf450871fc30aa8b38fbd2577eca5a8c9c0e76b39c5ea1)、[MCP_USR_TOOL_NOTIFICATION](P183_MCP完整API参考.md#gga9897522e100bc6d84aaaf450871fc30aaa7435cada70d1ebe4e6f4fef611b152d)、[MCP_USR_TOOL_CANCEL_ACK](P183_MCP完整API参考.md#gga9897522e100bc6d84aaaf450871fc30aaafcad745a3538eba10b081a457941499)、[MCP_USR_TOOL_PING](P183_MCP完整API参考.md#gga9897522e100bc6d84aaaf450871fc30aa5a339272d44f32c7b46039d25e45d814)。

<a id="r_ga4ea4339861b61e14403856a18a8ef065"></a>

```c
enum mcp_tool_event_type { MCP_TOOL_CALL_REQUEST , MCP_TOOL_CANCEL_REQUEST }
```

MCP 工具事件类型（Tool Event Type）。

相关声明：[mcp_tool_event_type](P183_MCP完整API参考.md#ga4ea4339861b61e14403856a18a8ef065)、[MCP_TOOL_CALL_REQUEST](P183_MCP完整API参考.md#gga4ea4339861b61e14403856a18a8ef065a6694d4b9c7f1fe70f5c9e410affbf5d1)、[MCP_TOOL_CANCEL_REQUEST](P183_MCP完整API参考.md#gga4ea4339861b61e14403856a18a8ef065a9ae0010b1615a9febaa953b00b5d3d1e)。

## 184.5\_函数（Functions）

<a id="r_ga90a431894013659b5a9ca7e49ed38f34"></a>

```c
mcp_server_ctx_t mcp_server_init (void)
```

初始化 MCP 服务器。

相关声明：[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)、[mcp_server_init](P183_MCP完整API参考.md#ga90a431894013659b5a9ca7e49ed38f34)。

<a id="r_ga738c6574f367615b8818534a4827258d"></a>

```c
int mcp_server_start (mcp_server_ctx_t server_ctx)
```

启动 MCP 服务器。

相关声明：[mcp_server_start](P183_MCP完整API参考.md#ga738c6574f367615b8818534a4827258d)、[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

<a id="r_gacb8dc5cf60b9f4bad1486f89330e62ad"></a>

```c
int mcp_server_submit_tool_message (mcp_server_ctx_t server_ctx, const struct mcp_tool_message *user_msg, const char *execution_token)
```

提交工具发出的消息（响应／通知）。

相关声明：[mcp_server_submit_tool_message](P183_MCP完整API参考.md#gacb8dc5cf60b9f4bad1486f89330e62ad)、[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)、[mcp_tool_message](P188_MCP工具消息结构.md)。

<a id="r_ga37df157c8a497affb24610d66096f6ae"></a>

```c
int mcp_server_add_tool (mcp_server_ctx_t server_ctx, const struct mcp_tool_record *tool_record)
```

向服务器添加工具。

相关声明：[mcp_server_add_tool](P183_MCP完整API参考.md#ga37df157c8a497affb24610d66096f6ae)、[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)、[mcp_tool_record](P190_MCP工具记录结构.md)。

<a id="r_ga1668b35e8e2e32d1e5e4c1d68561c5fe"></a>

```c
int mcp_server_remove_tool (mcp_server_ctx_t server_ctx, const char *tool_name)
```

从服务器移除工具。

相关声明：[mcp_server_remove_tool](P183_MCP完整API参考.md#ga1668b35e8e2e32d1e5e4c1d68561c5fe)、[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

<a id="r_gadef2d994c7bebd418531b597040a1f7d"></a>

```c
int mcp_server_is_execution_canceled (mcp_server_ctx_t server_ctx, const char *execution_token, bool *is_canceled)
```

用于检查工具执行状态的辅助函数。

相关声明：[mcp_server_is_execution_canceled](P183_MCP完整API参考.md#gadef2d994c7bebd418531b597040a1f7d)、[mcp_server_ctx_t](P183_MCP完整API参考.md#ga3e08a0cb026f941ca9d68a2636c3f33e)。

## 184.6\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P183_MCP完整API参考.md) · [返回大纲](大纲.md) · [下一章](P185_MCP服务器头文件源码.md)
