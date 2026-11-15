---
id: learning.zephyr-docs.networking.api-183
title: MCP完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcp__server.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_MCP完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp__server.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 183.1\_阅读说明与来源

译注：先读[模型上下文协议服务器指南](P178_MCP服务器.md)与[服务器入门示例](P181_MCP服务器入门示例.md)，理解服务器上下文（Server Context）、工具回调（Tool Callback）、执行令牌（Execution Token）和传输层（Transport）的关系，再按符号查询本组参考。

本组：[MCP完整API参考](P183_MCP完整API参考.md) · [MCP服务器头文件参考](P184_MCP服务器头文件参考.md) · [MCP服务器头文件源码](P185_MCP服务器头文件源码.md) · [MCP的HTTP头文件参考](P186_MCP的HTTP头文件参考.md) · [MCP的HTTP头文件源码](P187_MCP的HTTP头文件源码.md) · [MCP工具消息结构](P188_MCP工具消息结构.md) · [MCP工具元数据结构](P189_MCP工具元数据结构.md) · [MCP工具记录结构](P190_MCP工具记录结构.md)。

引入版本（Since）：4.5；API 版本（Version）：`0.1.0`。

## 183.2\_文件（Files）

<a id="r_mcp_5Fserver_2Eh"></a>

```c
file mcp_server.h
```

模型上下文协议（Model Context Protocol，MCP）服务器 API。

相关声明：[mcp_server.h](P184_MCP服务器头文件参考.md)。

## 183.3\_数据结构（Data Structures）

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

## 183.4\_类型定义（Typedefs）

<a id="r_ga3e08a0cb026f941ca9d68a2636c3f33e"></a>

```c
typedef void * mcp_server_ctx_t
```

服务器上下文句柄（Server Context Handle）。

<a id="r_ga5614c519ddad03f9cc51c7354b7029f1"></a>

```c
typedef int(* mcp_tool_callback_t) (enum mcp_tool_event_type event, const char *arguments, const char *execution_token)
```

工具回调函数（Tool Callback Function）。

## 183.5\_枚举（Enumerations）

<a id="r_ga9897522e100bc6d84aaaf450871fc30a"></a>

```c
enum mcp_tool_msg_type { MCP_USR_TOOL_RESPONSE , MCP_USR_TOOL_NOTIFICATION , MCP_USR_TOOL_CANCEL_ACK , MCP_USR_TOOL_PING }
```

MCP 工具消息类型（Tool Message Type）。

<a id="r_ga4ea4339861b61e14403856a18a8ef065"></a>

```c
enum mcp_tool_event_type { MCP_TOOL_CALL_REQUEST , MCP_TOOL_CANCEL_REQUEST }
```

MCP 工具事件类型（Tool Event Type）。

## 183.6\_函数（Functions）

<a id="r_ga90a431894013659b5a9ca7e49ed38f34"></a>

```c
mcp_server_ctx_t mcp_server_init (void)
```

初始化 MCP 服务器。

<a id="r_ga738c6574f367615b8818534a4827258d"></a>

```c
int mcp_server_start (mcp_server_ctx_t server_ctx)
```

启动 MCP 服务器。

<a id="r_gacb8dc5cf60b9f4bad1486f89330e62ad"></a>

```c
int mcp_server_submit_tool_message (mcp_server_ctx_t server_ctx, const struct mcp_tool_message *user_msg, const char *execution_token)
```

提交工具发出的消息（响应／通知）。

相关声明：[mcp_tool_message](P188_MCP工具消息结构.md)。

<a id="r_ga37df157c8a497affb24610d66096f6ae"></a>

```c
int mcp_server_add_tool (mcp_server_ctx_t server_ctx, const struct mcp_tool_record *tool_record)
```

向服务器添加工具。

相关声明：[mcp_tool_record](P190_MCP工具记录结构.md)。

<a id="r_ga1668b35e8e2e32d1e5e4c1d68561c5fe"></a>

```c
int mcp_server_remove_tool (mcp_server_ctx_t server_ctx, const char *tool_name)
```

从服务器移除工具。

<a id="r_gadef2d994c7bebd418531b597040a1f7d"></a>

```c
int mcp_server_is_execution_canceled (mcp_server_ctx_t server_ctx, const char *execution_token, bool *is_canceled)
```

用于检查工具执行状态的辅助函数。

## 183.7\_详细说明（Detailed Documentation）

<a id="ga3e08a0cb026f941ca9d68a2636c3f33e"></a>

### `mcp_server_ctx_t`

```c
typedef void* mcp_server_ctx_t
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

服务器上下文句柄（Server Context Handle）。

<a id="ga5614c519ddad03f9cc51c7354b7029f1"></a>

### `mcp_tool_callback_t`

```c
typedef int(* mcp_tool_callback_t) (enum mcp_tool_event_type event, const char *arguments, const char *execution_token)
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

工具回调函数（Tool Callback Function）。

可考虑为大型缓冲区使用堆分配（Heap Allocation），以减少栈用量。

该回调会占用并阻塞一个 MCP 服务器工作线程。对于长时间操作，建议使用应用自己的线程池异步执行工作，并尽快从该回调返回，避免阻塞 MCP 工作线程、降低服务器响应能力。

是否允许同一工具并发执行，由用户应用决定。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `event` | 工具事件类型，即调用请求或取消请求。 |
| `arguments` | 包含工具参数的 JSON 字符串。 |
| `execution_token` | 唯一执行标识符，即 UUID 字符串；UUID 为通用唯一标识符（Universally Unique Identifier）。 |

**注意（Note）**：注意：回调在 MCP 请求工作线程的上下文中执行，默认栈大小由 `CONFIG_MCP_REQUEST_WORKER_STACK_SIZE` 决定。工具回调需要更多栈空间时，应增大该值。

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

<a id="ga4ea4339861b61e14403856a18a8ef065"></a>

### `mcp_tool_event_type`

```c
enum mcp_tool_event_type
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

MCP 工具事件类型（Tool Event Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MCP_TOOL_CALL_REQUEST` | 调用工具的 JSON-RPC 请求。 |
| `MCP_TOOL_CANCEL_REQUEST` | 工具取消请求。 |

<a id="ga9897522e100bc6d84aaaf450871fc30a"></a>

### `mcp_tool_msg_type`

```c
enum mcp_tool_msg_type
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

MCP 工具消息类型（Tool Message Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MCP_USR_TOOL_RESPONSE` | 对客户端请求的 JSON-RPC 响应。 |
| `MCP_USR_TOOL_NOTIFICATION` | 工具发往客户端的通知。 |
| `MCP_USR_TOOL_CANCEL_ACK` | 向 MCP 核心提交的取消确认（Cancellation Acknowledgment）。 |
| `MCP_USR_TOOL_PING` | 向 MCP 核心表明工具仍在运行的保活消息（Ping）。 |

<a id="ga37df157c8a497affb24610d66096f6ae"></a>

### `mcp_server_add_tool()`

```c
int mcp_server_add_tool ( mcp_server_ctx_t server_ctx, const struct mcp_tool_record * tool_record )
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

向服务器添加工具。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |
| `tool_record` | 包含元数据和回调的工具定义。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | `tool_record` 无效。 |
| `-EEXIST` | 工具名称已经存在。 |
| `-ENOSPC` | 注册表已满。 |

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

> 译注（源码核对）：当前核心实现除检查工具记录外，还检查服务器上下文、工具名称是否为空及回调是否为空；互斥锁获取失败也可能返回错误。原返回值表列出主要错误，不应理解为任意无效输入均已由本页穷举。

<a id="ga90a431894013659b5a9ca7e49ed38f34"></a>

### `mcp_server_init()`

```c
mcp_server_ctx_t mcp_server_init ( void )
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

初始化 MCP 服务器。

**返回（Returns）**：成功返回 `mcp_server_ctx_t`，失败返回 `NULL`。

<a id="gadef2d994c7bebd418531b597040a1f7d"></a>

### `mcp_server_is_execution_canceled()`

```c
int mcp_server_is_execution_canceled ( mcp_server_ctx_t server_ctx, const char * execution_token, bool * is_canceled )
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

用于检查工具执行状态的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |
| `execution_token` | 代表该次执行的令牌（Execution Token），为 UUID 字符串。 |
| `is_canceled` | 用于写入取消状态的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 工具名称无效。 |
| `-ENOENT` | 未找到工具。 |

**注意（Note）**：注意：这是检查取消状态的另一种方式；主要方式应是通过工具调用事件（原文写作 `struct mcp_tool_event_type`）检查。此辅助函数需要使用互斥锁（Mutex）和线性搜索（Linear Search）定位相应执行上下文。

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

> 译注（源码核对）：原注释的 `struct mcp_tool_event_type` 实际应为 `enum mcp_tool_event_type`。此外，原返回值表沿用了“工具名称无效／未找到工具”的文字，但本函数接收的是执行令牌，并不接收工具名称。当前官方实现先检查服务器和输出指针，再按 `execution_token` 查找执行上下文，未找到时返回 `-ENOENT`。必须先检查函数返回值，再解释 `is_canceled`；错误分支写入 `false` 不能证明工具仍在执行。

<a id="ga1668b35e8e2e32d1e5e4c1d68561c5fe"></a>

### `mcp_server_remove_tool()`

```c
int mcp_server_remove_tool ( mcp_server_ctx_t server_ctx, const char * tool_name )
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

从服务器移除工具。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |
| `tool_name` | 要移除的工具名称。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | 工具名称无效。 |
| `-ENOENT` | 未找到工具。 |
| `-EBUSY` | 工具正在执行，不能移除；请稍后重试。 |

**注意（Note）**：注意：返回 `-EBUSY` 表明工具当前仍在执行，应稍后再次调用。

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

<a id="ga738c6574f367615b8818534a4827258d"></a>

### `mcp_server_start()`

```c
int mcp_server_start ( mcp_server_ctx_t server_ctx)
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

启动 MCP 服务器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

<a id="gacb8dc5cf60b9f4bad1486f89330e62ad"></a>

### `mcp_server_submit_tool_message()`

```c
int mcp_server_submit_tool_message ( mcp_server_ctx_t server_ctx, const struct mcp_tool_message * user_msg, const char * execution_token )
```

```c
#include <zephyr/net/mcp/mcp_server.h>
```

提交工具发出的消息（响应／通知）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `server_ctx` | 服务器上下文句柄。 |
| `user_msg` | 待提交的应用消息。 |
| `execution_token` | 用于跟踪执行的令牌，UUID 字符串。 |

**返回（Returns）**：成功返回 `0`，失败返回负错误码（negative errno）。

> 译注（源码核对）：枚举中保留了 `MCP_USR_TOOL_NOTIFICATION`，但当前指南明确通知尚不受支持，核心提交函数也没有支持此消息类型的处理分支。存在枚举值不等于功能已经实现。工具结果的 `is_error` 与本函数返回的提交状态是两层含义：前者描述工具执行失败，后者描述消息提交是否成功。

## 183.8\_相关源码与使用边界

声明来自 `<zephyr/net/mcp/mcp_server.h>` 及 `<zephyr/net/mcp/mcp_server_http.h>`。本仓库的[核心头文件](../../../include/zephyr/net/mcp/mcp_server.h)和[HTTP 头文件](../../../include/zephyr/net/mcp/mcp_server_http.h)可用于源码追踪，版本可能与官网 `latest` 不同。以下核对依据为本批保存的[官方核心实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server.c)及[官方 HTTP 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/mcp_server_http.c)，源码摘要见[来源记录](../SOURCES.md)。

> 译注——条件成员（Conditional Members）：本批 Doxygen 元数据页只展示 `name` 和 `input_schema`。官方原始头文件还在对应 Kconfig 开关启用时定义以下成员；这里是明确的源码补充，不能把它们当作所有配置下均存在的固定结构布局。

| 开关 | 成员声明 | 含义 |
| --- | --- | --- |
| `CONFIG_MCP_TOOL_DESC` | `char description[CONFIG_MCP_TOOL_DESC_MAX_LEN]` | 工具描述（Tool Description） |
| `CONFIG_MCP_TOOL_TITLE` | `char title[CONFIG_MCP_TOOL_NAME_MAX_LEN]` | 工具标题（Tool Title） |
| `CONFIG_MCP_TOOL_OUTPUT_SCHEMA` | `char output_schema[CONFIG_MCP_TOOL_SCHEMA_MAX_LEN]` | 工具输出模式（Output Schema），JSON 格式 |

<a id="header-files"></a>
<a id="files"></a>
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
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4ea4339861b61e14403856a18a8ef065a6694d4b9c7f1fe70f5c9e410affbf5d1"></a>
<a id="gga4ea4339861b61e14403856a18a8ef065a9ae0010b1615a9febaa953b00b5d3d1e"></a>
<a id="gga9897522e100bc6d84aaaf450871fc30aa8b38fbd2577eca5a8c9c0e76b39c5ea1"></a>
<a id="gga9897522e100bc6d84aaaf450871fc30aaa7435cada70d1ebe4e6f4fef611b152d"></a>
<a id="gga9897522e100bc6d84aaaf450871fc30aaafcad745a3538eba10b081a457941499"></a>
<a id="gga9897522e100bc6d84aaaf450871fc30aa5a339272d44f32c7b46039d25e45d814"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P182_OCPP充电桩示例.md) · [返回大纲](大纲.md) · [下一章](P184_MCP服务器头文件参考.md)
