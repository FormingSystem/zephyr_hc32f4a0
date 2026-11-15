---
id: learning.zephyr-docs.shell-remote-reference.page-10
title: 远端Shell运行数据
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_远端Shell运行数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__data.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

用于存储远端Shell实例数据的结构（Instance Data Structure）。

```c
#include <zephyr/shell/shell_remote.h>
```

<a id="details"></a>

用于存储远端Shell实例数据的结构（Instance Data Structure）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a1b411b2f856385e08fc7e915f1ac88da"></a>

```c
struct ipc_ept ept
```

相关声明：[ipc_ept](../intercore_reference/P113_IPC服务端点结构.md)、[ept](#a1b411b2f856385e08fc7e915f1ac88da)。

IPC端点（Endpoint）。

<a id="r_af8872d013a80afeba1201dc82892437e"></a>

```c
struct k_sem sem
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[sem](#af8872d013a80afeba1201dc82892437e)。

用于同步访问远端Shell实例的信号量（Semaphore）。

<a id="r_ab1bade0da8e552b492c0f10448bdf6d6"></a>

```c
struct k_work work
```

相关声明：[k_work](https://docs.zephyrproject.org/latest/doxygen/html/structk__work.html)、[work](#ab1bade0da8e552b492c0f10448bdf6d6)。

处理打印消息的工作队列（Work Queue）。

<a id="r_a97b2cb413dc24aa511e9e7673d031103"></a>

```c
const struct shell * sh
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[sh](#a97b2cb413dc24aa511e9e7673d031103)。

Shell实例指针。

<a id="r_ad007967f92725925d2b66b27bb5e548d"></a>

```c
struct shell_remote_cmd cmds [2]
```

相关声明：[shell_remote_cmd](P009_远端Shell命令.md)、[cmds](#ad007967f92725925d2b66b27bb5e548d)。

存储最近两个命令的空间，即当前命令（Current）和父命令（Parent）。

<a id="r_a098d8b3da108972c75aae512527ee96d"></a>

```c
struct shell_remote_cmd * current_cmd
```

相关声明：[shell_remote_cmd](P009_远端Shell命令.md)、[current_cmd](#a098d8b3da108972c75aae512527ee96d)。

当前命令（Current Command）的指针。

<a id="r_ac5bfd07b113aa7a79eb0bfe9f361db48"></a>

```c
int result
```

相关声明：[result](#ac5bfd07b113aa7a79eb0bfe9f361db48)。

上次命令的结果（Command Result）。

<a id="r_a129256b9fd61a17027362874bae8c87d"></a>

```c
size_t msg_len
```

相关声明：[msg_len](#a129256b9fd61a17027362874bae8c87d)。

打印消息长度（Print Message Length）。

<a id="r_ad0cb7d3a07ad5590a86f559328fed338"></a>

```c
void * msg
```

相关声明：[msg](#ad0cb7d3a07ad5590a86f559328fed338)。

打印消息指针；消息在堆（Heap）上分配。

<a id="r_a76fa224ff7b9e121318c5ed2acccd2f8"></a>

```c
bool ready
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[ready](#a76fa224ff7b9e121318c5ed2acccd2f8)。

表示远端Shell实例已就绪、已绑定（Bound）的标志；原文括号中写作bounded。

## 10.2\_详细说明（Detailed Documentation）

<a id="ad007967f92725925d2b66b27bb5e548d"></a>

### `cmds`

```c
struct shell_remote_cmd shell_remote_data::cmds[2]
```

存储最近两个命令的空间，即当前命令（Current）和父命令（Parent）。

<a id="a098d8b3da108972c75aae512527ee96d"></a>

### `current_cmd`

```c
struct shell_remote_cmd* shell_remote_data::current_cmd
```

当前命令（Current Command）的指针。

<a id="a1b411b2f856385e08fc7e915f1ac88da"></a>

### `ept`

```c
struct ipc_ept shell_remote_data::ept
```

IPC端点（Endpoint）。

<a id="ad0cb7d3a07ad5590a86f559328fed338"></a>

### `msg`

```c
void* shell_remote_data::msg
```

打印消息指针；消息在堆（Heap）上分配。

<a id="a129256b9fd61a17027362874bae8c87d"></a>

### `msg_len`

```c
size_t shell_remote_data::msg_len
```

打印消息长度（Print Message Length）。

<a id="a76fa224ff7b9e121318c5ed2acccd2f8"></a>

### `ready`

```c
bool shell_remote_data::ready
```

表示远端Shell实例已就绪、已绑定（Bound）的标志；原文括号中写作bounded。

<a id="ac5bfd07b113aa7a79eb0bfe9f361db48"></a>

### `result`

```c
int shell_remote_data::result
```

上次命令的结果（Command Result）。

<a id="af8872d013a80afeba1201dc82892437e"></a>

### `sem`

```c
struct k_sem shell_remote_data::sem
```

用于同步访问远端Shell实例的信号量（Semaphore）。

<a id="a97b2cb413dc24aa511e9e7673d031103"></a>

### `sh`

```c
const struct shell* shell_remote_data::sh
```

Shell实例指针。

<a id="ab1bade0da8e552b492c0f10448bdf6d6"></a>

### `work`

```c
struct k_work shell_remote_data::work
```

处理打印消息的工作队列（Work Queue）。

## 10.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——源码核对：远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——源码核对：打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote.h](P003_远端Shell头文件源码.md)
- [ipc_ept](../intercore_reference/P113_IPC服务端点结构.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_work](https://docs.zephyrproject.org/latest/doxygen/html/structk__work.html)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_remote_cmd](P009_远端Shell命令.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_远端Shell命令.md) · [返回大纲](大纲.md) · [下一章](P011_远端Shell命令消息.md)
