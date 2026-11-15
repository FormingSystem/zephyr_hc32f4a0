---
id: learning.zephyr-docs.shell-ssh-reference.page-5
title: Shell_SSH上下文结构
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__ssh__context.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Shell\_SSH上下文结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__ssh__context.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SSH后端接口、头文件与关联数据结构。源码跟踪译注与官方原文分开标示。

SSH传输用户数据（Transport User Data）。

```c
#include <zephyr/shell/shell_ssh.h>
```

<a id="details"></a>

SSH传输用户数据（Transport User Data）。此结构保存Shell SSH传输的用户数据。它会传给传输事件回调（Transport Event Callback），可用于保存传输所需的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_ad1846f871029db1640789cf51c116903"></a>

```c
const struct shell * sh
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[sh](#ad1846f871029db1640789cf51c116903)。

与此传输关联的Shell实例（Shell Instance）。

<a id="r_a6def2564fe322935e757a450564caab6"></a>

```c
struct shell_ssh * ssh
```

相关声明：[shell_ssh](P004_Shell_SSH传输结构.md)、[ssh](#a6def2564fe322935e757a450564caab6)。

Shell SSH传输API（Transport API）。

<a id="r_aa631cab0b48ebf311472e23aded0c074"></a>

```c
struct ssh_channel * channel
```

相关声明：[channel](#aa631cab0b48ebf311472e23aded0c074)。

与此传输关联的SSH通道（SSH Channel）。

<a id="r_a98b995de48367e233f8df075db07c01b"></a>

```c
struct ssh_transport * transport
```

相关声明：[transport](#a98b995de48367e233f8df075db07c01b)。

与此用户数据关联的SSH传输（SSH Transport）。

<a id="r_adc0068e62576bd921459a3a826a1db84"></a>

```c
struct shell_ssh_passwd password
```

相关声明：[shell_ssh_passwd](P006_Shell_SSH口令结构.md)、[password](#adc0068e62576bd921459a3a826a1db84)。

SSH服务器口令存储（Server Password Storage）。

<a id="r_a28b05473d9d45f699b8ec310fb0433f6"></a>

```c
int ssh_instance
```

相关声明：[ssh_instance](#a28b05473d9d45f699b8ec310fb0433f6)。

SSH连接实例（Connection Instance），可以是客户端或服务器。

<a id="r_a8ed84276247f827d8a577b3e4723490b"></a>

```c
bool in_use
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[in_use](#a8ed84276247f827d8a577b3e4723490b)。

此上下文是否正在使用，用于服务器端池跟踪（Server-side Pool Tracking）。

## 5.2\_详细说明（Detailed Documentation）

<a id="aa631cab0b48ebf311472e23aded0c074"></a>

### `channel`

```c
struct ssh_channel* shell_ssh_context::channel
```

与此传输关联的SSH通道（SSH Channel）。

<a id="a8ed84276247f827d8a577b3e4723490b"></a>

### `in_use`

```c
bool shell_ssh_context::in_use
```

此上下文是否正在使用，用于服务器端池跟踪（Server-side Pool Tracking）。

<a id="adc0068e62576bd921459a3a826a1db84"></a>

### `password`

```c
struct shell_ssh_passwd shell_ssh_context::password
```

SSH服务器口令存储（Server Password Storage）。

<a id="ad1846f871029db1640789cf51c116903"></a>

### `sh`

```c
const struct shell* shell_ssh_context::sh
```

与此传输关联的Shell实例（Shell Instance）。

<a id="a6def2564fe322935e757a450564caab6"></a>

### `ssh`

```c
struct shell_ssh* shell_ssh_context::ssh
```

Shell SSH传输API（Transport API）。

<a id="a28b05473d9d45f699b8ec310fb0433f6"></a>

### `ssh_instance`

```c
int shell_ssh_context::ssh_instance
```

SSH连接实例（Connection Instance），可以是客户端或服务器。

<a id="a98b995de48367e233f8df075db07c01b"></a>

### `transport`

```c
struct ssh_transport* shell_ssh_context::transport
```

与此用户数据关联的SSH传输（SSH Transport）。

## 5.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_ssh.h](../../../include/zephyr/shell/shell_ssh.h)、[subsys/shell/backends/shell_ssh.c](../../../subsys/shell/backends/shell_ssh.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：SHELL_SSH_DEFINE创建SSH传输对象与静态上下文，需要与SHELL_DEFINE配合构造Shell实例。宏定义本身不建立网络连接，也不代表一个已认证的SSH会话。

> 译注——源码核对：shell_ssh的in_use标志和shell_ssh_context的in_use标志分别用于Shell实例与服务器上下文池的占用跟踪。当前实现通过互斥锁（Mutex）保护分配和归还；不能把字段值当作对网络连通性的独立检测。

> 译注——源码核对：SHELL_SSH_MAX_PASSWORD_LEN为32，buf数组容量为该值加1。结构另外保存size_t类型的len。字段仅描述存储布局，不能由此推断口令校验、编码或完整的认证策略。

> 译注——源码核对：官方结构描述允许ssh_instance表示客户端或服务器连接；所核对实现中的服务器上下文池和事件回调受CONFIG_SSH_SERVER控制。字段的通用描述不表示所有配置都会构造服务器对象。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_ssh.h](P003_Shell_SSH头文件源码.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_ssh](P004_Shell_SSH传输结构.md)
- [shell_ssh_passwd](P006_Shell_SSH口令结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_Shell_SSH传输结构.md) · [返回大纲](大纲.md) · [下一章](P006_Shell_SSH口令结构.md)
