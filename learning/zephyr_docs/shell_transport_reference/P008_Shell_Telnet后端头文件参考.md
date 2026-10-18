---
id: learning.zephyr-docs.shell-transport-reference.page-8
title: Shell_Telnet后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__telnet_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Shell\_Telnet后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__telnet_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell Telnet后端（Telnet Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/net/socket.h>
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

Shell Telnet后端（Telnet Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga82cf4289a4a5d724edd2d4d333eafe4e"></a>

```c
#define SHELL_TELNET_DEFINE(_name)
```

相关声明：[SHELL_TELNET_DEFINE](P007_Shell_Telnet后端接口.md#ga82cf4289a4a5d724edd2d4d333eafe4e)。

定义Shell Telnet传输实例（Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_ga628b99d20ef08a0b1165af07aee4888c"></a>

```c
const struct shell * shell_backend_telnet_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_telnet_get_ptr](P007_Shell_Telnet后端接口.md#ga628b99d20ef08a0b1165af07aee4888c)。

此函数提供Shell Telnet后端实例的指针。

## 8.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_telnet.h](../../../include/zephyr/shell/shell_telnet.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：DEFINE宏创建传输对象及静态上下文，get_ptr取得配置好的Shell实例。返回实例地址并不表示已有Telnet客户端连接；连接及输入输出由传输实现负责。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 8.4\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P009_Shell_Telnet后端头文件源码.md)
- [SHELL_TELNET_DEFINE](P007_Shell_Telnet后端接口.md#ga82cf4289a4a5d724edd2d4d333eafe4e)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_telnet_get_ptr](P007_Shell_Telnet后端接口.md#ga628b99d20ef08a0b1165af07aee4888c)

<a id="header-details"></a>

---

[上一章](P007_Shell_Telnet后端接口.md) · [返回大纲](大纲.md) · [下一章](P009_Shell_Telnet后端头文件源码.md)
