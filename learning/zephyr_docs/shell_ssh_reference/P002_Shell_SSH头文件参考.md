---
id: learning.zephyr-docs.shell-ssh-reference.page-2
title: Shell_SSH头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__ssh_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Shell\_SSH头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__ssh_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SSH后端接口、头文件与关联数据结构。源码跟踪译注与官方原文分开标示。

Shell SSH后端（SSH Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/net/socket.h>
#include <zephyr/net/ssh/server.h>
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

Shell SSH后端（SSH Backend）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_shell_5Fssh_5Fpasswd"></a>

```c
struct shell_ssh_passwd
```

相关声明：[shell_ssh_passwd](P006_Shell_SSH口令结构.md)。

SSH口令存储（Password Storage）。

<a id="r_shell_5Fssh_5Fcontext"></a>

```c
struct shell_ssh_context
```

相关声明：[shell_ssh_context](P005_Shell_SSH上下文结构.md)。

SSH传输用户数据（Transport User Data）。

<a id="r_shell_5Fssh"></a>

```c
struct shell_ssh
```

相关声明：[shell_ssh](P004_Shell_SSH传输结构.md)。

SSH传输API（Transport API）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gae0437a2655471cad3608a9f82e6cb239"></a>

```c
#define SHELL_SSH_MAX_PASSWORD_LEN 32
```

相关声明：[SHELL_SSH_MAX_PASSWORD_LEN](P001_Shell_SSH后端接口.md#gae0437a2655471cad3608a9f82e6cb239)。

Shell SSH传输支持的最大口令长度（Maximum Password Length）。

<a id="r_ga13a7d6a8f20989347c0bd8bfa1916473"></a>

```c
#define SHELL_SSH_GET_NAME(_name)
```

相关声明：[SHELL_SSH_GET_NAME](P001_Shell_SSH后端接口.md#ga13a7d6a8f20989347c0bd8bfa1916473)。

用于构造Shell SSH传输实例内部符号名称的辅助宏（Helper Macro）。

<a id="r_gae35af1180d79e140e1191abf2f1de6de"></a>

```c
#define SHELL_SSH_DEFINE(_name)
```

相关声明：[SHELL_SSH_DEFINE](P001_Shell_SSH后端接口.md#gae35af1180d79e140e1191abf2f1de6de)。

定义Shell SSH传输实例（Transport Instance）。

## 2.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_ssh.h](../../../include/zephyr/shell/shell_ssh.h)、[subsys/shell/backends/shell_ssh.c](../../../subsys/shell/backends/shell_ssh.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：SHELL_SSH_DEFINE创建SSH传输对象与静态上下文，需要与SHELL_DEFINE配合构造Shell实例。宏定义本身不建立网络连接，也不代表一个已认证的SSH会话。

> 译注——源码核对：shell_ssh的in_use标志和shell_ssh_context的in_use标志分别用于Shell实例与服务器上下文池的占用跟踪。当前实现通过互斥锁（Mutex）保护分配和归还；不能把字段值当作对网络连通性的独立检测。

> 译注——源码核对：SHELL_SSH_MAX_PASSWORD_LEN为32，buf数组容量为该值加1。结构另外保存size_t类型的len。字段仅描述存储布局，不能由此推断口令校验、编码或完整的认证策略。

> 译注——源码核对：官方结构描述允许ssh_instance表示客户端或服务器连接；所核对实现中的服务器上下文池和事件回调受CONFIG_SSH_SERVER控制。字段的通用描述不表示所有配置都会构造服务器对象。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h_source.html)
- [zephyr/net/ssh/server.h](https://docs.zephyrproject.org/latest/doxygen/html/ssh_2server_8h_source.html)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P003_Shell_SSH头文件源码.md)
- [shell_ssh_passwd](P006_Shell_SSH口令结构.md)
- [shell_ssh_context](P005_Shell_SSH上下文结构.md)
- [shell_ssh](P004_Shell_SSH传输结构.md)
- [SHELL_SSH_MAX_PASSWORD_LEN](P001_Shell_SSH后端接口.md#gae0437a2655471cad3608a9f82e6cb239)
- [SHELL_SSH_GET_NAME](P001_Shell_SSH后端接口.md#ga13a7d6a8f20989347c0bd8bfa1916473)
- [SHELL_SSH_DEFINE](P001_Shell_SSH后端接口.md#gae35af1180d79e140e1191abf2f1de6de)

<a id="header-details"></a>

---

[上一章](P001_Shell_SSH后端接口.md) · [返回大纲](大纲.md) · [下一章](P003_Shell_SSH头文件源码.md)
