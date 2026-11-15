---
id: learning.zephyr-docs.networking.api-189
title: MCP工具元数据结构
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__metadata.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第189章\_MCP工具元数据结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmcp__tool__metadata.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 189.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

工具元数据结构（Tool Metadata Structure）。

```c
#include <zephyr/net/mcp/mcp_server.h>
```

工具元数据结构（Tool Metadata Structure）。

## 189.2\_数据成员（Data Fields）

<a id="r_a6499a3e806f41d568c711c3f0b617515"></a>

```c
char name [CONFIG_MCP_TOOL_NAME_MAX_LEN]
```

工具名称。

<a id="r_acbccf4378024dd406563035b85bfc5d4"></a>

```c
char input_schema [CONFIG_MCP_TOOL_SCHEMA_MAX_LEN]
```

工具输入模式（Input Schema），采用 JSON 表示。

## 189.3\_详细说明（Detailed Documentation）

<a id="acbccf4378024dd406563035b85bfc5d4"></a>

### `input_schema`

```c
char mcp_tool_metadata::input_schema[CONFIG_MCP_TOOL_SCHEMA_MAX_LEN]
```

工具输入模式（Input Schema），采用 JSON 表示。

<a id="a6499a3e806f41d568c711c3f0b617515"></a>

### `name`

```c
char mcp_tool_metadata::name[CONFIG_MCP_TOOL_NAME_MAX_LEN]
```

工具名称。

## 189.4\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

> 译注——条件成员（Conditional Members）：本批 Doxygen 元数据页只展示 `name` 和 `input_schema`。官方原始头文件还在对应 Kconfig 开关启用时定义以下成员；这里是明确的源码补充，不能把它们当作所有配置下均存在的固定结构布局。

| 开关 | 成员声明 | 含义 |
| --- | --- | --- |
| `CONFIG_MCP_TOOL_DESC` | `char description[CONFIG_MCP_TOOL_DESC_MAX_LEN]` | 工具描述（Tool Description） |
| `CONFIG_MCP_TOOL_TITLE` | `char title[CONFIG_MCP_TOOL_NAME_MAX_LEN]` | 工具标题（Tool Title） |
| `CONFIG_MCP_TOOL_OUTPUT_SCHEMA` | `char output_schema[CONFIG_MCP_TOOL_SCHEMA_MAX_LEN]` | 工具输出模式（Output Schema），JSON 格式 |

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P188_MCP工具消息结构.md) · [返回大纲](大纲.md) · [下一章](P190_MCP工具记录结构.md)
