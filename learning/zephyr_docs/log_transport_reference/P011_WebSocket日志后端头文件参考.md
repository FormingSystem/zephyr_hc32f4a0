---
id: learning.zephyr-docs.log-transport-reference.page-11
title: WebSocket日志后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/log__backend__ws_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_WebSocket日志后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/log__backend__ws_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙低功耗、MQTT、网络与WebSocket后端的接口和头文件源码。源码跟踪译注与官方原文分开标示。

WebSocket日志后端的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
```

查看此文件的源码。

WebSocket日志后端的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.1\_函数（Functions）

<a id="r_gabf3157cb42022eeea46cbe43c3824de0"></a>

```c
int log_backend_ws_register (int fd)
```

相关声明：[log_backend_ws_register](P010_WebSocket日志后端接口.md#gabf3157cb42022eeea46cbe43c3824de0)。

注册日志输出要发送到的WebSocket套接字（Socket）。

<a id="r_ga6026cf4df6ba455708ca58867dd66b72"></a>

```c
int log_backend_ws_unregister (int fd)
```

相关声明：[log_backend_ws_unregister](P010_WebSocket日志后端接口.md#ga6026cf4df6ba455708ca58867dd66b72)。

注销曾用于发送日志输出的WebSocket套接字（Socket）。

<a id="r_gac502c554b139ba774bf1716126e36110"></a>

```c
const struct log_backend * log_backend_ws_get (void)
```

相关声明：[log_backend](../log_backend_reference/P004_日志后端结构.md)、[log_backend_ws_get](P010_WebSocket日志后端接口.md#gac502c554b139ba774bf1716126e36110)。

取得WebSocket日志后端。

<a id="r_ga5501764d7eefda59e35990671be58387"></a>

```c
void log_backend_ws_start (void)
```

相关声明：[log_backend_ws_start](P010_WebSocket日志后端接口.md#ga5501764d7eefda59e35990671be58387)。

启动WebSocket日志后端。

## 11.2\_源码定位与版本边界

源码定位：[include/zephyr/logging/log_backend_ws.h](../../../include/zephyr/logging/log_backend_ws.h)、[subsys/logging/backends/log_backend_ws.c](../../../subsys/logging/backends/log_backend_ws.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中的官方main文件；所有本地链接均为相对路径。

> 译注——源码核对：WebSocket套接字（WebSocket Socket）的创建与连接由调用者负责。register保存给定描述符，start激活日志后端；这两个操作本身都不建立WebSocket握手。

> 译注——源码核对：当前register与unregister直接访问输出控制块的ctx，而设置该ctx的do_ws_init位于首次process路径。源码中没有在注册处检查空ctx；不能从这两个API的简短说明推断可在任意初始化阶段调用。使用时需结合实际初始化顺序核对上下文已经建立。

> 译注——源码核对：当前unregister即使传入描述符与已保存值不一致，也只记录一条调试信息，然后把保存值设为-1并返回0。它不会关闭套接字；描述符的关闭与连接资源回收仍由持有者处理。

> 译注——源码核对：输出按换行或缓冲区满触发发送，遇到EAGAIN时按配置重试。持续失败时可能丢弃缓冲内容；处理字节数不是远端接收确认。panic路径停止继续处理消息，不提供故障状态下的网络发送保证。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.3\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [查看此文件的源码](P012_WebSocket日志后端头文件源码.md)
- [log_backend_ws_register](P010_WebSocket日志后端接口.md#gabf3157cb42022eeea46cbe43c3824de0)
- [log_backend_ws_unregister](P010_WebSocket日志后端接口.md#ga6026cf4df6ba455708ca58867dd66b72)
- [log_backend](../log_backend_reference/P004_日志后端结构.md)
- [log_backend_ws_get](P010_WebSocket日志后端接口.md#gac502c554b139ba774bf1716126e36110)
- [log_backend_ws_start](P010_WebSocket日志后端接口.md#ga5501764d7eefda59e35990671be58387)

<a id="header-details"></a>

---

[上一章](P010_WebSocket日志后端接口.md) · [返回大纲](大纲.md) · [下一章](P012_WebSocket日志后端头文件源码.md)
