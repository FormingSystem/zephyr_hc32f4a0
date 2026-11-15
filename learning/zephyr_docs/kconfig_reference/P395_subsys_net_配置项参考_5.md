---
id: learning.zephyr-docs.kconfig-reference.page-395
title: "`subsys/net`配置项参考（5/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第395章\_`subsys/net`配置项参考（5/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MCP_SERVER_INFO_TITLE"></a>

## 395.1 `CONFIG_MCP_SERVER_INFO_TITLE`

**提示（Prompt）**：在 serverInfo 中包含服务器标题（title）

**说明（Help）**

在 `serverInfo` 部分包含可选的 `title` 字段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_TITLE_MAX_LEN"></a>

## 395.2 `CONFIG_MCP_SERVER_INFO_TITLE_MAX_LEN`

**提示（Prompt）**：服务器信息中标题的最大长度

**说明（Help）**

`serverInfo` 中服务器标题（title）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER_INFO_TITLE && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → 在 serverInfo 中包含服务器标题（title）

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER_INFO_TITLE`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_SERVER_INFO_TITLE)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_TITLE_VALUE"></a>

## 395.3 `CONFIG_MCP_SERVER_INFO_TITLE_VALUE`

**提示（Prompt）**：服务器标题（Server title）

**说明（Help）**

在 `serverInfo` 中报告的 MCP 服务器标题。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER_INFO_TITLE && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Zephyr MCP Server"
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → 在 serverInfo 中包含服务器标题（title）

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER_INFO_TITLE`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_SERVER_INFO_TITLE)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_VERSION"></a>

## 395.4 `CONFIG_MCP_SERVER_INFO_VERSION`

**提示（Prompt）**：服务器版本（Server version）

**说明（Help）**

在 `serverInfo` 中报告的 MCP 服务器版本。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"1.0.0"
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_VERSION_MAX_LEN"></a>

## 395.5 `CONFIG_MCP_SERVER_INFO_VERSION_MAX_LEN`

**提示（Prompt）**：服务器信息中版本字符串的最大长度

**说明（Help）**

`serverInfo` 中服务器版本（version）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SLAB_LARGE_COUNT"></a>

## 395.6 `CONFIG_MCP_SLAB_LARGE_COUNT`

**提示（Prompt）**：大型内存块池的块数量（Large slab block count）

**说明（Help）**

大型内存块池（large memory slab）的块数量，块大小为 `MCP_MAX_MESSAGE_SIZE`。建议最少数量为：

```text
(MCP_MAX_CLIENTS * MCP_MAX_CLIENT_REQUESTS) + MCP_REQUEST_WORKERS + margin
```

其中余量（margin）用于覆盖排队响应、活动工作线程及健康监控通知的需要。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_ALLOC_SLAB && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
22
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SLAB_MEDIUM_COUNT"></a>

## 395.7 `CONFIG_MCP_SLAB_MEDIUM_COUNT`

**提示（Prompt）**：中型内存块池的块数量（Medium slab block count）

**说明（Help）**

中型内存块池（medium memory slab）的块数量，应至少为 `MCP_MAX_CLIENTS * MCP_MAX_CLIENT_REQUESTS + margin`，其中 `margin` 表示预留余量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_ALLOC_SLAB && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SLAB_MEDIUM_SIZE"></a>

## 395.8 `CONFIG_MCP_SLAB_MEDIUM_SIZE`

**提示（Prompt）**：中型内存块池块大小（字节）

**说明（Help）**

中型内存分配的块大小，例如已解析消息和响应结构体所需空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_ALLOC_SLAB && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SLAB_SMALL_COUNT"></a>

## 395.9 `CONFIG_MCP_SLAB_SMALL_COUNT`

**提示（Prompt）**：小型内存块池的块数量（Small slab block count）

**说明（Help）**

小型内存块池（small memory slab）中的块数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_ALLOC_SLAB && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SLAB_SMALL_SIZE"></a>

## 395.10 `CONFIG_MCP_SLAB_SMALL_SIZE`

**提示（Prompt）**：小型内存块池块大小（字节）

**说明（Help）**

小型内存分配的块大小，例如错误响应和通知参数所需空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_ALLOC_SLAB && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_CANCEL_TIMEOUT_MS"></a>

## 395.11 `CONFIG_MCP_TOOL_CANCEL_TIMEOUT_MS`

**提示（Prompt）**：执行取消超时（毫秒，cancellation timeout）

**说明（Help）**

允许工具确认取消请求的最长时间，超过后记录错误。默认 10000 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:271`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L271)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_DESC"></a>

## 395.12 `CONFIG_MCP_TOOL_DESC`

**提示（Prompt）**：在 tools/list 响应中包含工具描述（description）

**说明（Help）**

在 `tools/list` 响应中包含可选的 `description` 字段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_DESC_MAX_LEN"></a>

## 395.13 `CONFIG_MCP_TOOL_DESC_MAX_LEN`

**提示（Prompt）**：工具描述最大长度（tool description length）

**说明（Help）**

工具描述（description）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TOOL_DESC && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → 在 tools/list 响应中包含工具描述（description）

**配置项引用（Symbol References）**：[`CONFIG_MCP_TOOL_DESC`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TOOL_DESC)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_EXEC_TIMEOUT_MS"></a>

## 395.14 `CONFIG_MCP_TOOL_EXEC_TIMEOUT_MS`

**提示（Prompt）**：最大执行持续时间（毫秒，execution duration）

**说明（Help）**

工具执行允许的最长时间，超过后取消执行。默认 10 分钟，即 600000 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
600000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_IDLE_TIMEOUT_MS"></a>

## 395.15 `CONFIG_MCP_TOOL_IDLE_TIMEOUT_MS`

**提示（Prompt）**：执行空闲超时（毫秒，execution idle timeout）

**说明（Help）**

工具执行期间，自上次收到消息以来允许的最长无消息时间，超过后取消执行。默认 5000 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_INPUT_ARGS_MAX_LEN"></a>

## 395.16 `CONFIG_MCP_TOOL_INPUT_ARGS_MAX_LEN`

**提示（Prompt）**：输入参数最大长度（input argument length）

**说明（Help）**

工具输入参数的远程过程调用（RPC）字段最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_NAME_MAX_LEN"></a>

## 395.17 `CONFIG_MCP_TOOL_NAME_MAX_LEN`

**提示（Prompt）**：工具名称最大长度（tool name length）

**说明（Help）**

工具名称（name）和标题（title）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_OUTPUT_SCHEMA"></a>

## 395.18 `CONFIG_MCP_TOOL_OUTPUT_SCHEMA`

**提示（Prompt）**：包含工具输出模式字段（output schema）

**说明（Help）**

为工具包含可选的输出模式（output schema）字段，会增加内存开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_RESULT_MAX_LEN"></a>

## 395.19 `CONFIG_MCP_TOOL_RESULT_MAX_LEN`

**提示（Prompt）**：工具执行结果最大长度

**说明（Help）**

工具执行结果（execution result）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_SCHEMA_MAX_LEN"></a>

## 395.20 `CONFIG_MCP_TOOL_SCHEMA_MAX_LEN`

**提示（Prompt）**：输入／输出模式最大长度（schema length）

**说明（Help）**

工具输入和输出模式（input/output schema）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TOOL_TITLE"></a>

## 395.21 `CONFIG_MCP_TOOL_TITLE`

**提示（Prompt）**：包含工具标题字段（title）

**说明（Help）**

为工具包含可选的标题（title）字段，会增加内存开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:226`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L226)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_TRANSPORT"></a>

## 395.22 `CONFIG_MCP_TRANSPORT`

**提示（Prompt）**：MCP 传输机制（Transport Mechanism）

**说明（Help）**

选择 MCP 通信的传输机制（transport mechanism）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MCP_TRANSPORT_HTTP
```

**可选项（Choices）**

```text
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_MCP_TRANSPORT_MOCK
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_TRANSPORT_MOCK`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_MOCK)。

<a id="CONFIG_MCP_TRANSPORT_HTTP"></a>

## 395.23 `CONFIG_MCP_TRANSPORT_HTTP`

**提示（Prompt）**：HTTP 传输（transport）

**说明（Help）**

使用 HTTP 传输 MCP 数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && <choice CONFIG_MCP_TRANSPORT>
```

**主动选择（Selects）**

```text
CONFIG_MIN_HEAP
CONFIG_NET_TCP
CONFIG_NET_IPV6
CONFIG_NET_SOCKETS
CONFIG_HTTP_SERVER
CONFIG_HTTP_SERVER_CAPTURE_HEADERS
CONFIG_UUID
CONFIG_UUID_V4
CONFIG_UUID_BASE64
CONFIG_ENTROPY_GENERATOR
CONFIG_PSA_CRYPTO
CONFIG_MBEDTLS
CONFIG_MBEDTLS_PSA_CRYPTO_C
CONFIG_PSA_WANT_ALG_SHA_1
CONFIG_BASE64
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 传输机制（Transport Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT)、[`CONFIG_MIN_HEAP`](P197_lib_配置项参考_1.md#CONFIG_MIN_HEAP)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_HTTP_SERVER_CAPTURE_HEADERS`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_CAPTURE_HEADERS)、[`CONFIG_UUID`](P199_lib_配置项参考_3.md#CONFIG_UUID)、[`CONFIG_UUID_V4`](P199_lib_配置项参考_3.md#CONFIG_UUID_V4)、[`CONFIG_UUID_BASE64`](P199_lib_配置项参考_3.md#CONFIG_UUID_BASE64)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_PSA_CRYPTO_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PSA_CRYPTO_C)、[`CONFIG_PSA_WANT_ALG_SHA_1`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_1)、[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)。

<a id="CONFIG_MCP_TRANSPORT_MOCK"></a>

## 395.24 `CONFIG_MCP_TRANSPORT_MOCK`

**提示（Prompt）**：模拟传输，仅用于测试（Mock transport）

**说明（Help）**

用于单元测试的模拟传输层（mock transport layer），仅应在测试构建中使用。它实现 `transport_binding` 接口，并跟踪所有发送／断开调用，供测试验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_TRANSPORT>
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L312)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 传输机制（Transport Mechanism）

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT)。

<a id="CONFIG_MDNS_RESOLVER"></a>

## 395.25 `CONFIG_MDNS_RESOLVER`

**提示（Prompt）**：组播 DNS 支持（mDNS support）

**说明（Help）**

启用组播 DNS 客户端支持，详情参见 RFC 6762。未启用 mDNS 响应器时，解析器自行加入 mDNS 组播组（multicast groups）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MDNS_RESPONDER_PROBE
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)。

<a id="CONFIG_MDNS_RESOLVER_ADDITIONAL_BUF_CTR"></a>

## 395.26 `CONFIG_MDNS_RESOLVER_ADDITIONAL_BUF_CTR`

**提示（Prompt）**：附加 DNS 缓冲区（Additional buffers）

**说明（Help）**

mDNS 响应器可用的附加缓冲区数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESOLVER_AUTO_ADD_UNSCOPED"></a>

## 395.27 `CONFIG_MDNS_RESOLVER_AUTO_ADD_UNSCOPED`

**提示（Prompt）**：自动向默认解析器添加未限定接口的 mDNS 服务器

**说明（Help）**

执行 `dns_resolve_init_default()` 时，无论自动初始化还是手动调用，都向默认解析器服务器列表追加未限定接口范围的 mDNS 服务器。在按接口分别配置 mDNS 的多接口系统上，应禁用此项，以避免 UDP/5353 绑定冲突。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESOLVER && CONFIG_DNS_RESOLVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 域名系统解析器（DNS resolver） → 组播 DNS 支持（mDNS support）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESOLVER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESOLVER)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESOLVER_BUF_SIZE"></a>

## 395.28 `CONFIG_MDNS_RESOLVER_BUF_SIZE`

**提示（Prompt）**：net_buf 池中缓冲区的大小

**说明（Help）**

较大的 DNS 服务发现（DNS-SD）TXT 记录和较长的服务实例名称，需要更大的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER"></a>

## 395.29 `CONFIG_MDNS_RESPONDER`

**提示（Prompt）**：组播 DNS 响应器（mDNS responder）

**说明（Help）**

为 Zephyr 启用组播 DNS（mDNS）响应器，监听众所周知的地址 `ff02::fb` 和 `224.0.0.251`。原文此项说明目前仅返回 IP 地址信息。必须将 `CONFIG_NET_HOSTNAME` 设为有意义的值，随后 mDNS 才会响应 `<hostname>.local` 查询。详情参见 RFC 6762。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_HOSTNAME_ENABLE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV4_IGMP if CONFIG_NET_IPV4
CONFIG_NET_IPV6_MLD if CONFIG_NET_IPV6
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_HOSTNAME_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_HOSTNAME_ENABLE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4_IGMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6_MLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)。

<a id="CONFIG_MDNS_RESPONDER_ANNOUNCE_DNS_SD"></a>

## 395.30 `CONFIG_MDNS_RESPONDER_ANNOUNCE_DNS_SD`

**提示（Prompt）**：在 mDNS 通告中包含 DNS-SD 服务记录

**说明（Help）**

RFC 6762 第 8.3 节要求启动通告（startup announcement）包含响应器全部新注册资源记录，而非只有地址记录。这包括通过 `DNS_SD_REGISTER_SERVICE()` 注册的各 DNS-SD 服务的共享 PTR 记录和唯一 SRV／TXT 记录，以及通过 `mdns_responder_set_ext_records()` 设置的记录。

启用可完整满足该要求。禁用时，通告只包含地址记录，启动流量更小、发送更少。主动查询服务的客户端，例如 `avahi-browse`，在两种情况下都不受影响，因为常规查询／响应处理无论本项是否启用，都会回答 DNS-SD 查询。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER_PROBE && CONFIG_MDNS_RESPONDER_DNS_SD && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → 通过 mDNS 进行 DNS 服务发现（DNS Service Discovery）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_MDNS_RESPONDER_DNS_SD`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_DNS_SD)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_DNS_SD"></a>

## 395.31 `CONFIG_MDNS_RESPONDER_DNS_SD`

**提示（Prompt）**：通过 mDNS 进行 DNS 服务发现（DNS Service Discovery）

**说明（Help）**

使 mDNS 响应器按 RFC 6763 处理 PTR、SRV 和 TXT 记录，从而能够发现 Zephyr 网络服务，例如：

```sh
avahi-browse -t -r _greybus._tcp
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_SD && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:362`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L362)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_DNS_SD`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_DNS_SD_SERVICE_TYPE_ENUMERATION"></a>

## 395.32 `CONFIG_MDNS_RESPONDER_DNS_SD_SERVICE_TYPE_ENUMERATION`

**提示（Prompt）**：DNS-SD 服务类型枚举（Service Type Enumeration）

**说明（Help）**

使 mDNS 响应器按 RFC 6763 第 9 节进行 DNS-SD 服务类型枚举，从而能够发现 Zephyr 网络服务，例如：

```sh
avahi-browse -t -r _services._dns-sd._udp.local
```

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER_DNS_SD && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → 通过 mDNS 进行 DNS 服务发现（DNS Service Discovery）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_DNS_SD`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_DNS_SD)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_IFACE_LIST"></a>

## 395.33 `CONFIG_MDNS_RESPONDER_IFACE_LIST`

**提示（Prompt）**：逗号分隔的接口名称列表（interface names）

**说明（Help）**

接口策略适用的网络接口名称列表，以逗号分隔，例如 `eth0,wlan0`。使用接口名称而非接口索引，是因为索引可能随配置改变。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
(CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST || CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST) && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:311`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L311)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST)、[`CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALL"></a>

## 395.34 `CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALL`

**提示（Prompt）**：所有接口（All interfaces）

**说明（Help）**

mDNS 响应器附着到每个网络接口。这是默认且向后兼容的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:289`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L289)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器接口策略（interface policy）

<a id="CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST"></a>

## 395.35 `CONFIG_MDNS_RESPONDER_IFACE_POLICY_ALLOWLIST`

**提示（Prompt）**：仅列出的接口（Only listed interfaces）

**说明（Help）**

mDNS 响应器仅附着到名称出现在 `MDNS_RESPONDER_IFACE_LIST` 中的接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_NET_INTERFACE_NAME
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:295`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L295)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器接口策略（interface policy）

**配置项引用（Symbol References）**：[`CONFIG_NET_INTERFACE_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_INTERFACE_NAME)。

<a id="CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST"></a>

## 395.36 `CONFIG_MDNS_RESPONDER_IFACE_POLICY_DENYLIST`

**提示（Prompt）**：除所列接口以外的所有接口

**说明（Help）**

mDNS 响应器附着到所有接口，但排除名称出现在 `MDNS_RESPONDER_IFACE_LIST` 中的接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**主动选择（Selects）**

```text
CONFIG_NET_INTERFACE_NAME
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器接口策略（interface policy）

**配置项引用（Symbol References）**：[`CONFIG_NET_INTERFACE_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_INTERFACE_NAME)。

<a id="CONFIG_MDNS_RESPONDER_INIT_PRIO"></a>

## 395.37 `CONFIG_MDNS_RESPONDER_INIT_PRIO`

**提示（Prompt）**：mDNS 响应器初始化的启动优先级

**说明（Help）**

启用 `NET_CONFIG_AUTO_INIT` 时，本值应大于其配置值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
96
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE"></a>

## 395.38 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：mDNS 响应器日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MDNS_RESPONDER_LOG_LEVEL_OFF
CONFIG_MDNS_RESPONDER_LOG_LEVEL_ERR
CONFIG_MDNS_RESPONDER_LOG_LEVEL_WRN
CONFIG_MDNS_RESPONDER_LOG_LEVEL_INF
CONFIG_MDNS_RESPONDER_LOG_LEVEL_DBG
CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_OFF`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_OFF)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_ERR`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_ERR)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_WRN`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_WRN)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_INF`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_INF)、[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_DBG`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_DBG)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_DBG"></a>

## 395.39 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT"></a>

## 395.40 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_ERR"></a>

## 395.41 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_INF"></a>

## 395.42 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_OFF"></a>

## 395.43 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_LOG_LEVEL_WRN"></a>

## 395.44 `CONFIG_MDNS_RESPONDER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 响应器日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MDNS_RESPONDER_PROBE"></a>

## 395.45 `CONFIG_MDNS_RESPONDER_PROBE`

**提示（Prompt）**：mDNS 探测支持（probing support）【实验性 EXPERIMENTAL】

**说明（Help）**

探测功能要求同时启用 mDNS 和 DNS 解析器。将探测设为可选，可减少不需要此功能时的内存占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_CONNECTION_MANAGER
CONFIG_MDNS_RESOLVER
CONFIG_DNS_RESOLVER
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)、[`CONFIG_MDNS_RESOLVER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESOLVER)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL"></a>

## 395.46 `CONFIG_MDNS_RESPONDER_RUNTIME_IFACE_CONTROL`

**提示（Prompt）**：按接口在运行时控制 mDNS 响应器

**说明（Help）**

提供 `mdns_responder_enable_iface()` 和 `mdns_responder_disable_iface()`，让应用在运行时启用或禁用特定网络接口上的 mDNS 响应器。运行时设置覆盖该接口的构建期策略；未启用本项时，响应器只遵循构建期接口策略（build-time interface policy）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:320`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L320)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_RESPONDER_TTL"></a>

## 395.47 `CONFIG_MDNS_RESPONDER_TTL`

**提示（Prompt）**：返回的 DNS 名称生存时间（Time-to-Live）

**说明（Help）**

DNS 回答使用的生存时间（TTL），单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
600
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder）

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_WORKER_PRIO"></a>

## 395.48 `CONFIG_MDNS_WORKER_PRIO`

**提示（Prompt）**：mDNS 工作队列优先级（work queue priority）

**说明（Help）**

设置处理全部 mDNS 探测的工作队列优先级。原文定义 `0` 为最高优先级；`CONFIG_NET_TC_THREAD_COOPERATIVE = y` 时，最低为 `CONFIG_NUM_COOP_PRIORITIES-1`，否则最低为 `CONFIG_NUM_PREEMPT_PRIORITIES-1`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER_PROBE && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 探测支持（probing support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MDNS_WORKQ_STACK_SIZE"></a>

## 395.49 `CONFIG_MDNS_WORKQ_STACK_SIZE`

**提示（Prompt）**：mDNS 工作队列线程栈大小

**说明（Help）**

设置 mDNS 工作队列线程的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MDNS_RESPONDER_PROBE && CONFIG_MDNS_RESPONDER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1200 if CONFIG_X86
1024
```

**定义位置（Location）**：[`subsys/net/lib/dns/Kconfig:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/dns/Kconfig#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 组播 DNS 响应器（mDNS responder） → mDNS 探测支持（probing support）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)。

<a id="CONFIG_MQTT_CLEAN_SESSION"></a>

## 395.50 `CONFIG_MQTT_CLEAN_SESSION`

**提示（Prompt）**：MQTT 清理会话标志（Clean Session Flag）。

**说明（Help）**

客户端通过持久会话（persistent session）连接 MQTT 消息代理（broker）时，代理保存所有订阅。客户端断开后，代理存储尚未确认的 QoS 1 消息，以及发布到该客户端订阅主题的新 QoS 1 消息。客户端重新连接持久会话时，恢复全部订阅，并向其发送所有已存储消息。将此标志设为 `0`，允许客户端创建持久会话。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_KEEPALIVE"></a>

## 395.51 `CONFIG_MQTT_KEEPALIVE`

**提示（Prompt）**：MQTT 保活时间，秒（原文标题还包含 Maximum number of clients）

**说明（Help）**

MQTT 保活（keep alive）时间，单位为秒。用于维持连接的 Ping 请求发送由此值控制。译注：原文标题混入“最大客户端数量”字样，正文实际描述保活时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_LIB"></a>

## 395.52 `CONFIG_MQTT_LIB`

**提示（Prompt）**：基于套接字的 MQTT 库支持（Socket MQTT Library）

**说明（Help）**

启用 Zephyr MQTT 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
```

**被选择（Selected by）**

```text
CONFIG_SHELL_BACKEND_MQTT
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_SHELL_BACKEND_MQTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_MQTT)。

<a id="CONFIG_MQTT_LIB_CUSTOM_TRANSPORT"></a>

## 395.53 `CONFIG_MQTT_LIB_CUSTOM_TRANSPORT`

**提示（Prompt）**：套接字 MQTT 库的自定义传输支持

**说明（Help）**

启用套接字 MQTT 库的自定义传输（custom transport）支持，用户必须提供传输过程的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_LIB_TLS"></a>

## 395.54 `CONFIG_MQTT_LIB_TLS`

**提示（Prompt）**：套接字 MQTT 库的 TLS 支持

**说明（Help）**

为套接字 MQTT 库启用传输层安全协议（TLS）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_LIB_TLS_USE_ALPN"></a>

## 395.55 `CONFIG_MQTT_LIB_TLS_USE_ALPN`

**提示（Prompt）**：MQTT 的应用层协议协商支持（ALPN）

**说明（Help）**

为套接字 MQTT 库启用应用层协议协商（ALPN）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB_TLS && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → 套接字 MQTT 库的 TLS 支持

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB_TLS`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB_TLS)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_LIB_WEBSOCKET"></a>

## 395.56 `CONFIG_MQTT_LIB_WEBSOCKET`

**提示（Prompt）**：套接字 MQTT 库的 WebSocket 支持

**说明（Help）**

为套接字 MQTT 库启用 WebSocket 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_LOG_LEVEL_CHOICE"></a>

## 395.57 `CONFIG_MQTT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MQTT 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MQTT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MQTT_LOG_LEVEL_OFF
CONFIG_MQTT_LOG_LEVEL_ERR
CONFIG_MQTT_LOG_LEVEL_WRN
CONFIG_MQTT_LOG_LEVEL_INF
CONFIG_MQTT_LOG_LEVEL_DBG
CONFIG_MQTT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MQTT_LOG_LEVEL_DEFAULT`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_DEFAULT)、[`CONFIG_MQTT_LOG_LEVEL_OFF`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_OFF)、[`CONFIG_MQTT_LOG_LEVEL_ERR`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_ERR)、[`CONFIG_MQTT_LOG_LEVEL_WRN`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_WRN)、[`CONFIG_MQTT_LOG_LEVEL_INF`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_INF)、[`CONFIG_MQTT_LOG_LEVEL_DBG`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_DBG)。

<a id="CONFIG_MQTT_LOG_LEVEL_DBG"></a>

## 395.58 `CONFIG_MQTT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_LOG_LEVEL_DEFAULT"></a>

## 395.59 `CONFIG_MQTT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_LOG_LEVEL_ERR"></a>

## 395.60 `CONFIG_MQTT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_LOG_LEVEL_INF"></a>

## 395.61 `CONFIG_MQTT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_LOG_LEVEL_OFF"></a>

## 395.62 `CONFIG_MQTT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_LOG_LEVEL_WRN"></a>

## 395.63 `CONFIG_MQTT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → MQTT 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_KEEPALIVE"></a>

## 395.64 `CONFIG_MQTT_SN_KEEPALIVE`

**提示（Prompt）**：MQTT-SN 保活时间，秒（原文标题还包含 Maximum number of clients）

**说明（Help）**

MQTT-SN 保活（keep alive）时间，单位为秒。用于维持连接的 Ping 请求发送由此值控制。译注：原文标题混入“最大客户端数量”字样，正文实际描述保活时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
60
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB"></a>

## 395.65 `CONFIG_MQTT_SN_LIB`

**提示（Prompt）**：传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**说明（Help）**

启用 Zephyr MQTT 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MQTT_SN_LIB_BROADCAST_RADIUS"></a>

## 395.66 `CONFIG_MQTT_SN_LIB_BROADCAST_RADIUS`

**提示（Prompt）**：广播消息半径（broadcast radius）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_ADDR_SIZE"></a>

## 395.67 `CONFIG_MQTT_SN_LIB_MAX_ADDR_SIZE`

**提示（Prompt）**：传输地址最大大小（address size）

**说明（Help）**

MQTT_SN 库在内部保存地址，因此必须知道地址长度。应设为所实现传输的地址数据结构最大字节数。UDP 传输在 IPv4 下至少需要 8 字节，在 IPv6 下至少需要 24 字节，分别对应 `sockaddr_in` 和 `sockaddr_in6` 的大小。树外传输（out-of-tree transport）可能需要调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
24 if CONFIG_NET_IPV6
8 if CONFIG_NET_IPV4
21
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)。

<a id="CONFIG_MQTT_SN_LIB_MAX_GATEWAYS"></a>

## 395.68 `CONFIG_MQTT_SN_LIB_MAX_GATEWAYS`

**提示（Prompt）**：内部保存的网关数量上限（gateways）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_MSGS"></a>

## 395.69 `CONFIG_MQTT_SN_LIB_MAX_MSGS`

**提示（Prompt）**：预分配消息数量（preallocated messages）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_PAYLOAD_SIZE"></a>

## 395.70 `CONFIG_MQTT_SN_LIB_MAX_PAYLOAD_SIZE`

**提示（Prompt）**：MQTT-SN 消息载荷最大大小（payload size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_PUBLISH"></a>

## 395.71 `CONFIG_MQTT_SN_LIB_MAX_PUBLISH`

**提示（Prompt）**：可同时在途的发布数量（in-flight publishes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_TOPICS"></a>

## 395.72 `CONFIG_MQTT_SN_LIB_MAX_TOPICS`

**提示（Prompt）**：可管理主题数量（topics）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_MAX_TOPIC_SIZE"></a>

## 395.73 `CONFIG_MQTT_SN_LIB_MAX_TOPIC_SIZE`

**提示（Prompt）**：主题最大长度（topic length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_N_ADV"></a>

## 395.74 `CONFIG_MQTT_SN_LIB_N_ADV`

**提示（Prompt）**：判定网关丢失前允许漏收的 Advertise 消息数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_N_RETRY"></a>

## 395.75 `CONFIG_MQTT_SN_LIB_N_RETRY`

**提示（Prompt）**：消息重试次数（retry count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_T_GWINFO"></a>

## 395.76 `CONFIG_MQTT_SN_LIB_T_GWINFO`

**提示（Prompt）**：发送 GWINFO 前的最长等待时间（秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_T_RETRY"></a>

## 395.77 `CONFIG_MQTT_SN_LIB_T_RETRY`

**提示（Prompt）**：等待响应的时间（秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LIB_T_SEARCHGW"></a>

## 395.78 `CONFIG_MQTT_SN_LIB_T_SEARCHGW`

**提示（Prompt）**：发送 SEARCHGW 前的最长等待时间（秒）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_CHOICE"></a>

## 395.79 `CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MQTT-SN 日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MQTT_SN_LOG_LEVEL_OFF
CONFIG_MQTT_SN_LOG_LEVEL_ERR
CONFIG_MQTT_SN_LOG_LEVEL_WRN
CONFIG_MQTT_SN_LOG_LEVEL_INF
CONFIG_MQTT_SN_LOG_LEVEL_DBG
CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT)、[`CONFIG_MQTT_SN_LOG_LEVEL_OFF`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_OFF)、[`CONFIG_MQTT_SN_LOG_LEVEL_ERR`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_ERR)、[`CONFIG_MQTT_SN_LOG_LEVEL_WRN`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_WRN)、[`CONFIG_MQTT_SN_LOG_LEVEL_INF`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_INF)、[`CONFIG_MQTT_SN_LOG_LEVEL_DBG`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_DBG)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_DBG"></a>

## 395.80 `CONFIG_MQTT_SN_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT"></a>

## 395.81 `CONFIG_MQTT_SN_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_ERR"></a>

## 395.82 `CONFIG_MQTT_SN_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_INF"></a>

## 395.83 `CONFIG_MQTT_SN_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_OFF"></a>

## 395.84 `CONFIG_MQTT_SN_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_LOG_LEVEL_WRN"></a>

## 395.85 `CONFIG_MQTT_SN_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_SN_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】 → MQTT-SN 日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LOG_LEVEL_CHOICE`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MQTT_SN_TRANSPORT_UDP"></a>

## 395.86 `CONFIG_MQTT_SN_TRANSPORT_UDP`

**提示（Prompt）**：MQTT-SN 的 UDP 传输（transport）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_SN_LIB && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_SOCKETS
CONFIG_NET_IPV4_IGMP if CONFIG_NET_IPV4
CONFIG_NET_IPV6_MLD if CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/net/lib/mqtt_sn/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt_sn/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 传感器网络 MQTT 库支持（MQTT-SN）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MQTT_SN_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_IPV4_IGMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6_MLD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)。

<a id="CONFIG_MQTT_SUBSCRIPTION_ID_PROPERTIES_MAX"></a>

## 395.87 `CONFIG_MQTT_SUBSCRIPTION_ID_PROPERTIES_MAX`

**提示（Prompt）**：Publish 数据包中订阅 ID 属性数量上限

**说明（Help）**

客户端处理发布消息（Publish message）时，可解析的订阅 ID（Subscription ID）属性数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_VERSION_5_0 && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_5_0`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_5_0)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_TOPIC_ALIAS_MAX"></a>

## 395.88 `CONFIG_MQTT_TOPIC_ALIAS_MAX`

**提示（Prompt）**：支持的主题别名数量上限（topic aliases）

**说明（Help）**

PUBLISH 数据包可使用的主题别名（topic aliases）数量上限。设为 `0` 可禁用主题别名。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_VERSION_5_0 && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_5_0`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_5_0)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_TOPIC_ALIAS_STRING_MAX"></a>

## 395.89 `CONFIG_MQTT_TOPIC_ALIAS_STRING_MAX`

**提示（Prompt）**：可使用别名的主题名称最大长度

**说明（Help）**

指定用于存储已建立别名的主题（aliased topics）的缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_VERSION_5_0 && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[8, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_5_0`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_5_0)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_USER_PROPERTIES_MAX"></a>

## 395.90 `CONFIG_MQTT_USER_PROPERTIES_MAX`

**提示（Prompt）**：数据包用户属性数量上限（user properties）

**说明（Help）**

客户端可在数据包中加入，或在接收时解析的用户属性（user properties）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_VERSION_5_0 && CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_5_0`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_5_0)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MQTT_VERSION_3_1_1"></a>

## 395.91 `CONFIG_MQTT_VERSION_3_1_1`

**提示（Prompt）**：最高支持 MQTT 协议版本 3.1.1

**说明（Help）**

库默认选择 MQTT 3.1.1。应用仍可通过相应的运行时 MQTT 客户端配置选择较旧协议版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_VERSION_SUPPORT>
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → 支持的最高 MQTT 协议版本

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_SUPPORT`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_SUPPORT)。

<a id="CONFIG_MQTT_VERSION_5_0"></a>

## 395.92 `CONFIG_MQTT_VERSION_5_0`

**提示（Prompt）**：最高支持 MQTT 协议版本 5.0【实验性 EXPERIMENTAL】

**说明（Help）**

库默认选择 MQTT 5.0。应用仍可通过相应的运行时 MQTT 客户端配置选择较旧协议版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MQTT_VERSION_SUPPORT>
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library） → 支持的最高 MQTT 协议版本

**配置项引用（Symbol References）**：[`CONFIG_MQTT_VERSION_SUPPORT`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_SUPPORT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_MQTT_VERSION_SUPPORT"></a>

## 395.93 `CONFIG_MQTT_VERSION_SUPPORT`

**提示（Prompt）**：支持的最高 MQTT 协议版本

**说明（Help）**

库支持的最高 MQTT 协议版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MQTT_LIB && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MQTT_VERSION_3_1_1
```

**可选项（Choices）**

```text
CONFIG_MQTT_VERSION_3_1_1
CONFIG_MQTT_VERSION_5_0
```

**定义位置（Location）**：[`subsys/net/lib/mqtt/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mqtt/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 基于套接字的 MQTT 库支持（Socket MQTT Library）

**配置项引用（Symbol References）**：[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MQTT_VERSION_3_1_1`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_3_1_1)、[`CONFIG_MQTT_VERSION_5_0`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_VERSION_5_0)。

<a id="CONFIG_NETMIDI2_HOST"></a>

## 395.94 `CONFIG_NETMIDI2_HOST`

**提示（Prompt）**：网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】

**说明（Help）**

用于通过用户数据报协议（UDP）传输通用 MIDI 数据包（Universal MIDI Packets，UMP）的主机库，提供：

- 通过 UDP 暴露 UMP 端点（endpoint）。
- 接受客户端入站邀请（inbound invitations）。
- 发送／接收通用 MIDI 数据包。

遵循《Network MIDI 2.0 (UDP) Transport Specification》v1.0。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_IPV4 || CONFIG_NET_IPV6) && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_NET_UDP
CONFIG_NET_SOCKETS
CONFIG_NET_SOCKETS_SERVICE
```

**弱选择（Implies）**

```text
CONFIG_NET_IPV4_MAPPING_TO_IPV6 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**定义位置（Location）**：[`subsys/net/lib/midi2/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/midi2/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_NET_SOCKETS_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_IPV4_MAPPING_TO_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_MAPPING_TO_IPV6)。

<a id="CONFIG_NETMIDI2_HOST_AUTH"></a>

## 395.95 `CONFIG_NETMIDI2_HOST_AUTH`

**提示（Prompt）**：认证支持，共享密钥或用户名／密码（authentication）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETMIDI2_HOST && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_CRYPTO
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`subsys/net/lib/midi2/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/midi2/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_NETMIDI2_HOST_MAX_CLIENTS"></a>

## 395.96 `CONFIG_NETMIDI2_HOST_MAX_CLIENTS`

**提示（Prompt）**：Network MIDI2 主机支持的客户端数量上限

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETMIDI2_HOST && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/midi2/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/midi2/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NETWORKING"></a>

## 395.97 `CONFIG_NETWORKING`

**提示（Prompt）**：链路层与网络功能（Link layer and networking，含 IP）

**说明（Help）**

启用通用链路层（link layer）及网络支持，是 IP 等高层协议的基础。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NET_BUF
CONFIG_POLL
CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`subsys/net/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_POLL`](P002_kernel_配置项参考_2.md#CONFIG_POLL)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_NET_6LO"></a>

## 395.98 `CONFIG_NET_6LO`

**提示（Prompt）**：低功耗无线个域网 IPv6 压缩库（6LoWPAN）

**说明（Help）**

提供 6LoWPAN 压缩与分片（compression and fragmentation）。存在 IEEE 802.15.4 时默认启用，因为在其上使用 IPv6 需要这些功能。若要在 802.15.4 媒体访问控制（MAC，即 L2）层上实现非 IP 自定义协议，可禁用本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_L2_IEEE802154
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:587`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L587)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_6LO_CONTEXT"></a>

## 395.99 `CONFIG_NET_6LO_CONTEXT`

**提示（Prompt）**：基于上下文的 6LoWPAN 压缩（context based compression）

**说明（Help）**

依据路由器通告（Router Advertisement，RA）消息中的信息，启用基于上下文的 6LoWPAN 压缩。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_6LO && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:597`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L597)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_6LO_LOG_LEVEL_CHOICE"></a>

## 395.100 `CONFIG_NET_6LO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：6LoWPAN 库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_6LO && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_6LO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_6LO_LOG_LEVEL_OFF
CONFIG_NET_6LO_LOG_LEVEL_ERR
CONFIG_NET_6LO_LOG_LEVEL_WRN
CONFIG_NET_6LO_LOG_LEVEL_INF
CONFIG_NET_6LO_LOG_LEVEL_DBG
CONFIG_NET_6LO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)、[`CONFIG_NET_6LO`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_6LO_LOG_LEVEL_DEFAULT`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_6LO_LOG_LEVEL_OFF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_OFF)、[`CONFIG_NET_6LO_LOG_LEVEL_ERR`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_ERR)、[`CONFIG_NET_6LO_LOG_LEVEL_WRN`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_WRN)、[`CONFIG_NET_6LO_LOG_LEVEL_INF`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_INF)、[`CONFIG_NET_6LO_LOG_LEVEL_DBG`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_6LO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<!-- kconfig-navigation -->

[上一章](P394_subsys_net_配置项参考_4.md) · [返回大纲](大纲.md) · [下一章](P396_subsys_net_配置项参考_6.md)
