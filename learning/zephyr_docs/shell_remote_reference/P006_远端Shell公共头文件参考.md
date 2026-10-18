---
id: learning.zephyr-docs.shell-remote-reference.page-6
title: 远端Shell公共头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_远端Shell公共头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__remote__common_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

远端Shell的公共API（Common APIs）。

<a id="details"></a>

```c
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

远端Shell的公共API（Common APIs）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_shell_5Fremote_5Fmsg_5Fgeneric"></a>

```c
struct shell_remote_msg_generic
```

相关声明：[shell_remote_msg_generic](P014_远端Shell通用消息.md)。

通用消息（Generic Message）。

<a id="r_shell_5Fremote_5Fmsg_5Fprint"></a>

```c
struct shell_remote_msg_print
```

相关声明：[shell_remote_msg_print](P015_远端Shell打印消息.md)。

打印消息（Print Message）。

<a id="r_shell_5Fremote_5Fmsg_5Fexec"></a>

```c
struct shell_remote_msg_exec
```

相关声明：[shell_remote_msg_exec](P013_远端Shell执行消息.md)。

执行命令（Execute Command）。

<a id="r_shell_5Fremote_5Fmsg_5Fresult"></a>

```c
struct shell_remote_msg_result
```

相关声明：[shell_remote_msg_result](P016_远端Shell结果消息.md)。

结果（Result）。

<a id="r_shell_5Fremote_5Fmsg_5Fcmd_5Fget"></a>

```c
struct shell_remote_msg_cmd_get
```

相关声明：[shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)。

获取命令（Get Command）。

<a id="r_shell_5Fremote_5Fmsg_5Fcmd"></a>

```c
struct shell_remote_msg_cmd
```

相关声明：[shell_remote_msg_cmd](P011_远端Shell命令消息.md)。

获取命令请求的响应（Response to Get Command）。

<a id="r_shell_5Fremote_5Fmsg"></a>

```c
union shell_remote_msg
```

相关声明：[shell_remote_msg](P017_远端Shell消息联合体.md)。

远端Shell消息联合体（Message Union）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="define-members-0"></a>

### 远端Shell消息编号（Message IDs）



<a id="r_a696447b939ff13a62cbcfea5edc95b67"></a>

```c
#define SHELL_REMOTE_MSG_PRINT 1
```

相关声明：[SHELL_REMOTE_MSG_PRINT](#a696447b939ff13a62cbcfea5edc95b67)。

打印消息（Print Message）。

<a id="r_ad32019c7d203e617c4bab81d72f41efd"></a>

```c
#define SHELL_REMOTE_MSG_CMD_GET 2
```

相关声明：[SHELL_REMOTE_MSG_CMD_GET](#ad32019c7d203e617c4bab81d72f41efd)。

获取命令（Get Command）。

<a id="r_a779be19f5392ff97ea04025ca10974ca"></a>

```c
#define SHELL_REMOTE_MSG_CMD 3
```

相关声明：[SHELL_REMOTE_MSG_CMD](#a779be19f5392ff97ea04025ca10974ca)。

获取命令请求的响应（Response to Get Command）。

<a id="r_a3d2c1f36ebe88993b50a24faa59c3e10"></a>

```c
#define SHELL_REMOTE_MSG_EXEC 4
```

相关声明：[SHELL_REMOTE_MSG_EXEC](#a3d2c1f36ebe88993b50a24faa59c3e10)。

执行命令（Execute Command）。

<a id="r_a87befcd3bc280e96de8558e317389586"></a>

```c
#define SHELL_REMOTE_MSG_RESULT 5
```

相关声明：[SHELL_REMOTE_MSG_RESULT](#a87befcd3bc280e96de8558e317389586)。

结果（Result）。

## 6.3\_详细说明（Detailed Documentation）

<a id="a779be19f5392ff97ea04025ca10974ca"></a>

### `SHELL_REMOTE_MSG_CMD`

```c
#define SHELL_REMOTE_MSG_CMD 3
```

获取命令请求的响应（Response to Get Command）。

<a id="ad32019c7d203e617c4bab81d72f41efd"></a>

### `SHELL_REMOTE_MSG_CMD_GET`

```c
#define SHELL_REMOTE_MSG_CMD_GET 2
```

获取命令（Get Command）。

<a id="a3d2c1f36ebe88993b50a24faa59c3e10"></a>

### `SHELL_REMOTE_MSG_EXEC`

```c
#define SHELL_REMOTE_MSG_EXEC 4
```

执行命令（Execute Command）。

<a id="a696447b939ff13a62cbcfea5edc95b67"></a>

### `SHELL_REMOTE_MSG_PRINT`

```c
#define SHELL_REMOTE_MSG_PRINT 1
```

打印消息（Print Message）。

<a id="a87befcd3bc280e96de8558e317389586"></a>

### `SHELL_REMOTE_MSG_RESULT`

```c
#define SHELL_REMOTE_MSG_RESULT 5
```

结果（Result）。

## 6.4\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote_common.h](../../../include/zephyr/shell/shell_remote_common.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：消息结构含size_t、int、函数指针和其他对象指针，不能把这些C结构当成天然跨位宽、跨字节序的通用网络格式。指针字段是对应远端命令对象或处理函数的值，不能在错误的地址空间中直接解引用。

> 译注——源码核对：data[0]在原始声明中表示头部后的变长数据位置；它不自带存储容量。命令响应数据依次保存NUL结尾的语法和可选帮助文本，实际长度来自消息，不应由零长数组的sizeof推算。

> 译注——源码核对：消息联合体的成员是各消息类型的指针。应先根据通用头中的消息编号选择成员，再按对应消息格式解析；这不是同时容纳所有消息正文的内嵌结构。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P007_远端Shell公共头文件源码.md)
- [shell_remote_msg_generic](P014_远端Shell通用消息.md)
- [shell_remote_msg_print](P015_远端Shell打印消息.md)
- [shell_remote_msg_exec](P013_远端Shell执行消息.md)
- [shell_remote_msg_result](P016_远端Shell结果消息.md)
- [shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)
- [shell_remote_msg_cmd](P011_远端Shell命令消息.md)
- [shell_remote_msg](P017_远端Shell消息联合体.md)

<a id="SHELL_REMOTE_MSG_IDS"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_远端Shell命令行头文件源码.md) · [返回大纲](大纲.md) · [下一章](P007_远端Shell公共头文件源码.md)
