---
id: learning.zephyr-docs.shell-transport-reference.page-11
title: Shell_WebSocket后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__websocket_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Shell\_WebSocket后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__websocket_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell WebSocket后端（WebSocket Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/net/socket.h>
#include <zephyr/net/http/server.h>
#include <zephyr/net/http/service.h>
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

Shell WebSocket后端（WebSocket Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga726a23776948ff246176c1ac2c88daa6"></a>

```c
#define WEBSOCKET_CONSOLE_DEFINE(_service, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[WEBSOCKET_CONSOLE_DEFINE](P010_Shell_WebSocket后端接口.md#ga726a23776948ff246176c1ac2c88daa6)。

定义WebSocket Shell服务（Service）。

<a id="r_ga134a7de93ded994b49fd781fb289e876"></a>

```c
#define WEBSOCKET_CONSOLE_ENABLE(_service)
```

相关声明：[WEBSOCKET_CONSOLE_ENABLE](P010_Shell_WebSocket后端接口.md#ga134a7de93ded994b49fd781fb289e876)。

启用使用WEBSOCKET_CONSOLE_DEFINE定义的WebSocket Shell服务。

## 11.2\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_websocket.h](../../../include/zephyr/shell/shell_websocket.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：WEBSOCKET_CONSOLE_DEFINE在编译期同时定义Shell传输、Shell实例与HTTP资源。CONFIG_NET_SOCKETS_SOCKOPT_TLS选择HTTPS或普通HTTP分支；未启用TLS时安全标签参数不参与普通HTTP服务定义。

> 译注——源码核对：资源只支持HTTP GET用于WebSocket升级（Upgrade），路径由斜杠和CONFIG_SHELL_WEBSOCKET_ENDPOINT_URL组成。不要把HTTP资源定义理解成已经建立了客户端会话。

> 译注——源码核对：WEBSOCKET_CONSOLE_ENABLE调用shell_websocket_enable，但宏显式丢弃其返回值。底层函数返回shell_init结果；宏调用结束本身不提供可检查的初始化成功状态。

> 译注——源码核对：源码中的输入缓冲、套接字锁和延迟工作属于实现内部结构。原始源码页可见它们不代表官方为全部内部字段提供独立的公共API契约。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h_source.html)
- [zephyr/net/http/service.h](https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P012_Shell_WebSocket后端头文件源码.md)
- [WEBSOCKET_CONSOLE_DEFINE](P010_Shell_WebSocket后端接口.md#ga726a23776948ff246176c1ac2c88daa6)
- [WEBSOCKET_CONSOLE_ENABLE](P010_Shell_WebSocket后端接口.md#ga134a7de93ded994b49fd781fb289e876)

<a id="header-details"></a>

---

[上一章](P010_Shell_WebSocket后端接口.md) · [返回大纲](大纲.md) · [下一章](P012_Shell_WebSocket后端头文件源码.md)
