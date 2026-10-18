---
id: learning.zephyr-docs.shell-ssh-reference.page-1
title: Shell_SSH后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__ssh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Shell\_SSH后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__ssh.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SSH后端接口、头文件与关联数据结构。源码跟踪译注与官方原文分开标示。

通过安全外壳协议（Secure Shell，SSH）连接访问Shell。

<a id="details"></a>

通过安全外壳协议（Secure Shell，SSH）连接访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_shell_5Fssh_2Eh"></a>

```c
file shell_ssh.h
```

相关声明：[shell_ssh.h](P002_Shell_SSH头文件参考.md)。

Shell SSH后端（SSH Backend）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

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

## 1.3\_宏定义（Macros）

<a id="r_gae0437a2655471cad3608a9f82e6cb239"></a>

```c
#define SHELL_SSH_MAX_PASSWORD_LEN 32
```

相关声明：[SHELL_SSH_MAX_PASSWORD_LEN](#gae0437a2655471cad3608a9f82e6cb239)。

Shell SSH传输支持的最大口令长度（Maximum Password Length）。

<a id="r_ga13a7d6a8f20989347c0bd8bfa1916473"></a>

```c
#define SHELL_SSH_GET_NAME(_name)
```

相关声明：[SHELL_SSH_GET_NAME](#ga13a7d6a8f20989347c0bd8bfa1916473)。

用于构造Shell SSH传输实例内部符号名称的辅助宏（Helper Macro）。

<a id="r_gae35af1180d79e140e1191abf2f1de6de"></a>

```c
#define SHELL_SSH_DEFINE(_name)
```

相关声明：[SHELL_SSH_DEFINE](#gae35af1180d79e140e1191abf2f1de6de)。

定义Shell SSH传输实例（Transport Instance）。

## 1.4\_详细说明（Detailed Documentation）

<a id="gae35af1180d79e140e1191abf2f1de6de"></a>

### `SHELL_SSH_DEFINE`

```c
#define SHELL_SSH_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_ssh.h>
```

展开值（Value）：

```c
static struct shell_ssh SHELL_SSH_GET_NAME(_name);      \
static struct shell_transport _name = {                 \
        .api = &shell_ssh_transport_api,                \
        .ctx = &_name##_shell_ssh,                      \
}
```

定义Shell SSH传输实例（Transport Instance）。

此宏定义由SSH支持的Shell传输。将其与SHELL_DEFINE()一起使用，可创建能够通过SSH访问的Shell实例。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例的名称。此词法记号（Token）用于构造内部符号名称。 |

<a id="ga13a7d6a8f20989347c0bd8bfa1916473"></a>

### `SHELL_SSH_GET_NAME`

```c
#define SHELL_SSH_GET_NAME ( _name)
```

```c
#include <zephyr/shell/shell_ssh.h>
```

展开值（Value）：

```c
_name##_shell_ssh
```

用于构造Shell SSH传输实例内部符号名称的辅助宏（Helper Macro）。

<a id="gae0437a2655471cad3608a9f82e6cb239"></a>

### `SHELL_SSH_MAX_PASSWORD_LEN`

```c
#define SHELL_SSH_MAX_PASSWORD_LEN 32
```

```c
#include <zephyr/shell/shell_ssh.h>
```

Shell SSH传输支持的最大口令长度（Maximum Password Length）。

## 1.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_ssh.h](../../../include/zephyr/shell/shell_ssh.h)、[subsys/shell/backends/shell_ssh.c](../../../subsys/shell/backends/shell_ssh.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：SHELL_SSH_DEFINE创建SSH传输对象与静态上下文，需要与SHELL_DEFINE配合构造Shell实例。宏定义本身不建立网络连接，也不代表一个已认证的SSH会话。

> 译注——源码核对：shell_ssh的in_use标志和shell_ssh_context的in_use标志分别用于Shell实例与服务器上下文池的占用跟踪。当前实现通过互斥锁（Mutex）保护分配和归还；不能把字段值当作对网络连通性的独立检测。

> 译注——源码核对：SHELL_SSH_MAX_PASSWORD_LEN为32，buf数组容量为该值加1。结构另外保存size_t类型的len。字段仅描述存储布局，不能由此推断口令校验、编码或完整的认证策略。

> 译注——源码核对：官方结构描述允许ssh_instance表示客户端或服务器连接；所核对实现中的服务器上下文池和事件回调受CONFIG_SSH_SERVER控制。字段的通用描述不表示所有配置都会构造服务器对象。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [shell_ssh.h](P002_Shell_SSH头文件参考.md)
- [shell_ssh_passwd](P006_Shell_SSH口令结构.md)
- [shell_ssh_context](P005_Shell_SSH上下文结构.md)
- [shell_ssh](P004_Shell_SSH传输结构.md)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)
- [SHELL_DEFINE()](../shell_core_reference/P001_Shell核心接口.md#ga158405143b49e4888cb135fec83ad22c)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__shell__ssh_html_ga13a7d6a8f20989347c0bd8bfa1916473"></a>
<a id="astructshell__ssh_html"></a>
<a id="astructshell__transport_html"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Shell_SSH头文件参考.md)
