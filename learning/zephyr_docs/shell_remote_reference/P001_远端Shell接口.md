---
id: learning.zephyr-docs.shell-remote-reference.page-1
title: 远端Shell接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__remote.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_远端Shell接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__remote.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

远端Shell API（Shell Remote API）。

<a id="details"></a>

远端Shell API（Shell Remote API）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_shell_5Fremote_2Eh"></a>

```c
file shell_remote.h
```

相关声明：[shell_remote.h](P002_远端Shell头文件参考.md)。

支持远端客户端（Remote Clients）。

<a id="r_shell_5Fremote_5Fcli_2Eh"></a>

```c
file shell_remote_cli.h
```

相关声明：[shell_remote_cli.h](P004_远端Shell命令行头文件参考.md)。

远端Shell客户端（Remote Shell Client）的API。

<a id="r_shell_5Fremote_5Fcommon_2Eh"></a>

```c
file shell_remote_common.h
```

相关声明：[shell_remote_common.h](P006_远端Shell公共头文件参考.md)。

远端Shell的公共API（Common APIs）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.2\_数据结构（Data Structures）

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

## 1.3\_宏定义（Macros）

<a id="r_ga0644f6ba7da5eb5bd4952d3afa6ff536"></a>

```c
#define CONFIG_SHELL_REMOTE_TMP_BUF_SIZE 128
```

相关声明：[CONFIG_SHELL_REMOTE_TMP_BUF_SIZE](#ga0644f6ba7da5eb5bd4952d3afa6ff536)。

远端Shell命令数据临时缓冲区（Temporary Buffer）的默认大小。

<a id="r_gaacd8c876a0f63e1514c6a68337cc944d"></a>

```c
#define SHELL_REMOTE_CONN(_name, ipc_node)
```

相关声明：[SHELL_REMOTE_CONN](#gaacd8c876a0f63e1514c6a68337cc944d)。

定义远端Shell实例（Remote Shell Instance）的宏。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga63fce1cfe8b08c710fafa5cbc8e28a13"></a>

```c
void shell_remote_ep_bound (void *priv)
```

相关声明：[shell_remote_ep_bound](#ga63fce1cfe8b08c710fafa5cbc8e28a13)。

处理远端Shell实例绑定事件（Bound Event）的回调函数。

<a id="r_ga834254727aeba7c1e29cc1e6df22f23f"></a>

```c
void shell_remote_ep_recv (const void *data, size_t len, void *priv)
```

相关声明：[shell_remote_ep_recv](#ga834254727aeba7c1e29cc1e6df22f23f)。

处理远端Shell实例接收事件（Received Event）的回调函数。

## 1.5\_详细说明（Detailed Documentation）

<a id="ga0644f6ba7da5eb5bd4952d3afa6ff536"></a>

### `CONFIG_SHELL_REMOTE_TMP_BUF_SIZE`

```c
#define CONFIG_SHELL_REMOTE_TMP_BUF_SIZE 128
```

```c
#include <zephyr/shell/shell_remote.h>
```

远端Shell命令数据临时缓冲区（Temporary Buffer）的默认大小。

<a id="gaacd8c876a0f63e1514c6a68337cc944d"></a>

### `SHELL_REMOTE_CONN`

```c
#define SHELL_REMOTE_CONN ( _name, ipc_node )
```

```c
#include <zephyr/shell/shell_remote.h>
```

展开值（Value）：

```c
static struct shell_remote_data shell_remote_data_##_name;                                 \
static const STRUCT_SECTION_ITERABLE(shell_remote, _name) = {                              \
        .name = STRINGIFY(_name), .ipc = DEVICE_DT_GET(ipc_node),                          \
                          .ep_cfg = {.name = CONFIG_SHELL_REMOTE_EP_NAME,                  \
                                     .cb =                                                 \
                                             {                                             \
                                                     .bound = shell_remote_ep_bound,       \
                                                     .received = shell_remote_ep_recv,     \
                                             },                                            \
                                     .priv = &shell_remote_data_##_name}}
```

定义远端Shell实例（Remote Shell Instance）的宏。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 远端Shell实例的名称，即命令语法名称（Command Syntax）。 |
| `ipc_node` | 进程间通信（IPC）设备的设备节点（Device Node）。 |

<a id="ga63fce1cfe8b08c710fafa5cbc8e28a13"></a>

### `shell_remote_ep_bound()`

```c
void shell_remote_ep_bound ( void * priv)
```

```c
#include <zephyr/shell/shell_remote.h>
```

处理远端Shell实例绑定事件（Bound Event）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `priv` | 指向私有数据（Private Data）的指针。 |

<a id="ga834254727aeba7c1e29cc1e6df22f23f"></a>

### `shell_remote_ep_recv()`

```c
void shell_remote_ep_recv ( const void * data, size_t len, void * priv )
```

```c
#include <zephyr/shell/shell_remote.h>
```

处理远端Shell实例接收事件（Received Event）的回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 数据指针（Data Pointer）。 |
| `len` | 数据长度（Data Length）。 |
| `priv` | 指向私有数据（Private Data）的指针。 |

## 1.6\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote.h](../../../include/zephyr/shell/shell_remote.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：远端Shell通过IPC端点传递命令和结果。CONN宏声明静态运行数据及可遍历段中的配置，设备通过DEVICE_DT_GET取得；宏展开本身不证明端点已绑定。ready字段原文写作bounded，这里按绑定事件（Bound Event）解释。

> 译注——源码核对：远端命令运行数据只保留两个命令槽，即当前命令和父命令。语法及帮助文本复制到固定大小临时缓冲区；现有实现对过长帮助文本作截断，并对语法长度使用断言。它不是可无限缓存整棵远端命令树的容器。

> 译注——源码核对：打印消息接收后按8字节对齐在堆上复制，再提交工作项处理；打印结束后释放副本并发送结果确认。字段注释称work为工作队列，而声明实际是struct k_work工作项，由系统工作队列执行。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.7\_原页交叉引用（Cross References）

- [shell_remote.h](P002_远端Shell头文件参考.md)
- [shell_remote_cli.h](P004_远端Shell命令行头文件参考.md)
- [shell_remote_common.h](P006_远端Shell公共头文件参考.md)
- [shell_remote_cmd](P009_远端Shell命令.md)
- [shell_remote_data](P010_远端Shell运行数据.md)
- [shell_remote](P008_远端Shell实例.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__shell__remote_html_ga63fce1cfe8b08c710fafa5cbc8e28a13"></a>
<a id="agroup__shell__remote_html_ga834254727aeba7c1e29cc1e6df22f23f"></a>
<a id="astructshell__remote__data_html"></a>
<a id="astructshell__remote_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_远端Shell头文件参考.md)
