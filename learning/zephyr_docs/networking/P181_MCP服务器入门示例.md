---
id: learning.zephyr-docs.networking.page-181
title: MCP服务器入门示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/mcp/mcp_server_hello_world/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第181章\_MCP服务器入门示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/mcp/mcp_server_hello_world/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例定义两个工具（Tools）：LED 控制工具，使模型上下文协议（Model Context Protocol，MCP）客户端能够打开、关闭或翻转板载 LED；延迟响应工具，用来触发延迟响应机制，展示服务器在此情况下的行为。

服务器连接网络并获得 IP 地址后，可通过该地址访问，也可使用多播 DNS（Multicast DNS，mDNS）名称，例如 `http://mcp-hello-world.local:8080/mcp`。

官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/mcp/mcp_server_hello_world)提供应用和工具定义。

## 2. 要求（Requirements）

- 支持网络连接的开发板。
- LED 连接到设备树 `led0` 别名的开发板；原文将其列为 LED 控制功能的可选条件。

> 源码边界：当前[main.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/mcp/mcp_server_hello_world/src/main.c)无条件使用 `GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios)` 构造 LED 描述，没有在缺少节点时跳过编译。因此，当前原样构建仍需有效的 `led0` 节点及 GPIO 属性；“可选”不能直接推断为无 LED 设备树节点也可编译通过。运行时的 GPIO 就绪检查与编译时的节点要求是两回事。

## 3. 接线（Wiring）

原文没有特殊接线要求。

## 4. 构建与运行

从读者自己的 Zephyr 源码根目录，在已具备目标板依赖的环境中构建并烧写：

```sh
west build -b <board_name> samples/net/mcp/mcp_server_hello_world
west flash
```

将 `<board_name>` 替换为实际目标。`west build` 生成固件，`west flash` 写入目标设备。

## 5. 测试（Testing）

服务器运行后，通过 HTTP 监听 MCP 客户端连接。原文称可以使用兼容 MCP 的客户端连接，并调用已注册工具。默认配置启用 DHCP 和 mDNS，服务地址为 `http://mcp-hello-world.local:8080/mcp`。

> 译注：该地址要求设备已取得 IP，并且客户端所在网络支持相应名称解析和访问。库目前只支持文本工具结果及有限的延迟响应交付，客户端仍需与这些能力兼容，不能把“兼容 MCP”理解为任意传输和协议特性都得到支持。详细限制见[MCP 服务器指南](P178_MCP服务器.md)。

> 源码对照：当前示例注册 `delayed_response` 和 `led_control`。后者的 `action` 值为 `on`、`off`、`toggle`。前者在工作线程中分四次休眠，每次约 3000 ms，在前三次后发送 PING，约 12000 ms 后提交固定问候文本；`message` 参数用于日志展示，不是原样回显的响应内容。它用于演示延迟交付，并没有把工作转移到独立线程；较长的实际工具仍应遵循库指南的异步回调建议。

## 6. 示例输出（Sample Output）

以下为官方启动输出：

```console
Initializing...
LED initialized successfully
Registering Tool #1: Delayed response tool...
Tool #1 registered.
Registering Tool #2: LED Control...
Tool #2 registered.
Starting...
MCP Server running...
```

调用工具后，会看到类似输出：

```console
Delayed response tool executed with arguments: {"message":"test"}, token: <uuid>
LED control tool executed with arguments: {"action":"on"}, token: <uuid>
```

`<uuid>` 是执行令牌（Execution Token）的占位，不是设备地址。日志中的初始化、工具注册与服务启动是不同阶段，应逐项核对错误返回；原文日志保留不改写为本次测试结果。

## 7. 参考资料（References）

[模型上下文协议规范（Model Context Protocol Specification）](https://modelcontextprotocol.io/specification)。

## 8. 另见（See Also）

[MCP 服务器 API](P183_MCP完整API参考.md)。

> 验证边界：本章已核对官方页面和示例配置／实现，没有构建或烧写固件、运行 MCP 服务、调用 LED 或延迟响应工具。


<a id="mcp-server-hello-world"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="wiring"></a>
<a id="building-and-running"></a>
<a id="testing"></a>
<a id="sample-output"></a>
<a id="references"></a>
<a id="see-also"></a>

[上一章](P180_MCP示例目录.md) · [返回大纲](大纲.md) · [下一章](P182_OCPP充电桩示例.md)
