---
id: learning.zephyr-docs.shell-remote-reference.page-2
title: 远端Shell头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_远端Shell头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

支持远端客户端（Remote Clients）。

<a id="details"></a>

```c
#include <zephyr/shell/shell_remote_common.h>
#include <zephyr/shell/shell.h>
#include <zephyr/ipc/ipc_service.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

支持远端客户端（Remote Clients）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_shell_5Fremote_5Fcmd"></a>

```c
struct shell_remote_cmd
```

相关声明：[shell_remote_cmd](P009_远端Shell命令.md)。

用于存储远端Shell命令数据的结构（Command Data Structure）。

<a id="r_shell_5Fremote_5Fdata"></a>

```c
struct shell_remote_data
```

相关声明：[shell_remote_data](P010_远端Shell运行数据.md)。

用于存储远端Shell实例数据的结构（Instance Data Structure）。

<a id="r_shell_5Fremote"></a>

```c
struct shell_remote
```

相关声明：[shell_remote](P008_远端Shell实例.md)。

用于存储远端Shell实例配置的结构（Instance Configuration Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_ga0644f6ba7da5eb5bd4952d3afa6ff536"></a>

```c
#define CONFIG_SHELL_REMOTE_TMP_BUF_SIZE 128
```

相关声明：[CONFIG_SHELL_REMOTE_TMP_BUF_SIZE](P001_远端Shell接口.md#ga0644f6ba7da5eb5bd4952d3afa6ff536)。

远端Shell命令数据临时缓冲区（Temporary Buffer）的默认大小。

<a id="r_gaacd8c876a0f63e1514c6a68337cc944d"></a>

```c
#define SHELL_REMOTE_CONN(_name, ipc_node)
```

相关声明：[SHELL_REMOTE_CONN](P001_远端Shell接口.md#gaacd8c876a0f63e1514c6a68337cc944d)。

定义远端Shell实例（Remote Shell Instance）的宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_ga63fce1cfe8b08c710fafa5cbc8e28a13"></a>

```c
void shell_remote_ep_bound (void *priv)
```

相关声明：[shell_remote_ep_bound](P001_远端Shell接口.md#ga63fce1cfe8b08c710fafa5cbc8e28a13)。

处理远端Shell实例绑定事件（Bound Event）的回调函数。

<a id="r_ga834254727aeba7c1e29cc1e6df22f23f"></a>

```c
void shell_remote_ep_recv (const void *data, size_t len, void *priv)
```

相关声明：[shell_remote_ep_recv](P001_远端Shell接口.md#ga834254727aeba7c1e29cc1e6df22f23f)。

处理远端Shell实例接收事件（Received Event）的回调函数。

## 2.4\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——源码核对：远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——源码核对：打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote_common.h](P007_远端Shell公共头文件源码.md)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [zephyr/ipc/ipc_service.h](../intercore_reference/P118_IPC服务完整头文件.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码](P003_远端Shell头文件源码.md)
- [shell_remote_cmd](P009_远端Shell命令.md)
- [shell_remote_data](P010_远端Shell运行数据.md)
- [shell_remote](P008_远端Shell实例.md)
- [CONFIG_SHELL_REMOTE_TMP_BUF_SIZE](P001_远端Shell接口.md#ga0644f6ba7da5eb5bd4952d3afa6ff536)
- [SHELL_REMOTE_CONN](P001_远端Shell接口.md#gaacd8c876a0f63e1514c6a68337cc944d)
- [shell_remote_ep_bound](P001_远端Shell接口.md#ga63fce1cfe8b08c710fafa5cbc8e28a13)
- [shell_remote_ep_recv](P001_远端Shell接口.md#ga834254727aeba7c1e29cc1e6df22f23f)

<a id="header-details"></a>

---

[上一章](P001_远端Shell接口.md) · [返回大纲](大纲.md) · [下一章](P003_远端Shell头文件源码.md)
