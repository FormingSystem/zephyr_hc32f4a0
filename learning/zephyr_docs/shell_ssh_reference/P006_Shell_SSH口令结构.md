---
id: learning.zephyr-docs.shell-ssh-reference.page-6
title: Shell_SSH口令结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__ssh__passwd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell\_SSH口令结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__ssh__passwd.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SSH后端接口、头文件与关联数据结构。源码跟踪译注与官方原文分开标示。

SSH口令存储（Password Storage）。

```c
#include <zephyr/shell/shell_ssh.h>
```

<a id="details"></a>

SSH口令存储（Password Storage）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a64c4777913be1fceb42a576b8c3643af"></a>

```c
char buf [32+1]
```

相关声明：[buf](#a64c4777913be1fceb42a576b8c3643af)。

保存口令的缓冲区（Password Buffer）。

<a id="r_a2354d4ecb613b35744681f1d8aa30c5a"></a>

```c
size_t len
```

相关声明：[len](#a2354d4ecb613b35744681f1d8aa30c5a)。

缓冲区中存储的口令长度（Password Length）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a64c4777913be1fceb42a576b8c3643af"></a>

### `buf`

```c
char shell_ssh_passwd::buf[32+1]
```

保存口令的缓冲区（Password Buffer）。

<a id="a2354d4ecb613b35744681f1d8aa30c5a"></a>

### `len`

```c
size_t shell_ssh_passwd::len
```

缓冲区中存储的口令长度（Password Length）。

## 6.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_ssh.h](../../../include/zephyr/shell/shell_ssh.h)、[subsys/shell/backends/shell_ssh.c](../../../subsys/shell/backends/shell_ssh.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：SHELL_SSH_DEFINE创建SSH传输对象与静态上下文，需要与SHELL_DEFINE配合构造Shell实例。宏定义本身不建立网络连接，也不代表一个已认证的SSH会话。

> 译注——源码核对：shell_ssh的in_use标志和shell_ssh_context的in_use标志分别用于Shell实例与服务器上下文池的占用跟踪。当前实现通过互斥锁（Mutex）保护分配和归还；不能把字段值当作对网络连通性的独立检测。

> 译注——源码核对：SHELL_SSH_MAX_PASSWORD_LEN为32，buf数组容量为该值加1。结构另外保存size_t类型的len。字段仅描述存储布局，不能由此推断口令校验、编码或完整的认证策略。

> 译注——源码核对：官方结构描述允许ssh_instance表示客户端或服务器连接；所核对实现中的服务器上下文池和事件回调受CONFIG_SSH_SERVER控制。字段的通用描述不表示所有配置都会构造服务器对象。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_ssh.h](P003_Shell_SSH头文件源码.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_Shell_SSH上下文结构.md) · [返回大纲](大纲.md)
