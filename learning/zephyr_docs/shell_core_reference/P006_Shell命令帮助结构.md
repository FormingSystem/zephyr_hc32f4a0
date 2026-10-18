---
id: learning.zephyr-docs.shell-core-reference.page-6
title: Shell命令帮助结构
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__cmd__help.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Shell命令帮助结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__cmd__help.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell核心接口、实例与传输数据结构和完整头文件源码。源码跟踪译注与官方原文分开标示。

Shell结构化帮助描述符（Structured Help Descriptor）。

```c
#include <zephyr/shell/shell.h>
```

<a id="details"></a>

Shell结构化帮助描述符（Structured Help Descriptor）。此结构以有组织的形式指定命令帮助，取代自由格式字符串，使帮助消息更一致、更易阅读。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_af9e182e1599c3cfcc42f739d40a511bb"></a>

```c
const char * description
```

相关声明：[description](#af9e182e1599c3cfcc42f739d40a511bb)。

命令描述（Command Description）。

<a id="r_a3735f4afeeea3d968d9e8fc74e0aa68f"></a>

```c
const char * usage
```

相关声明：[usage](#a3735f4afeeea3d968d9e8fc74e0aa68f)。

命令用法字符串（Command Usage String）。

## 6.2\_详细说明（Detailed Documentation）

<a id="af9e182e1599c3cfcc42f739d40a511bb"></a>

### `description`

```c
const char* shell_cmd_help::description
```

命令描述（Command Description）。

<a id="a3735f4afeeea3d968d9e8fc74e0aa68f"></a>

### `usage`

```c
const char* shell_cmd_help::usage
```

命令用法字符串（Command Usage String）。

## 6.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)、[subsys/shell/shell.c](../../../subsys/shell/shell.c)、[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文。源码与公开接口按本次官方快照核对，未将隐藏的内部条目补造为公开说明。

> 译注——源码核对：命令注册中的mandatory包含命令名称本身；optional可使用原文规定的特殊标志。条件宏与表达式宏控制命令是否存在，原宏展开保留，用来核对处理函数和子命令在不同配置下的去留。

> 译注——源码核对：动态命令回调应按索引填入条目、保证语法名称按字母顺序排序，并在没有更多条目时将syntax设为NULL。返回指针或空条目的含义应遵守该回调协议，不能用未初始化字段代替结束标记。

> 译注——源码核对：shell_execute_cmd禁止在Shell命令上下文内调用，而shell_readline要求从Shell线程的命令处理函数调用。二者调用条件不同；异步旁路（Bypass）与同步读行也有明确的互斥使用条件。

> 译注——源码核对：readline提示字符串不会被复制，必须有效到读行返回；返回后提示设置会自动清除。缓冲区容量包含NUL终止字符，成功返回的长度不含该字符。

> 译注——源码核对：字符串转换成功时保留err原值，应预先初始化错误变量。返回0或false既可能是有效结果，也可能是失败时的返回值，需要同时检查err。

> 译注——源码核对：shell和shell_ctx原页只给出结构用途，内部字段由Doxygen隐藏；本册对应页如实保留这个公开范围，完整可见布局另见头文件源码。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell.h](P003_Shell核心头文件源码.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_Shell运行上下文.md) · [返回大纲](大纲.md) · [下一章](P007_Shell命令参数约束.md)
