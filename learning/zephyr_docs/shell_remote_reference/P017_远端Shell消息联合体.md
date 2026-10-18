---
id: learning.zephyr-docs.shell-remote-reference.page-17
title: 远端Shell消息联合体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unionshell__remote__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_远端Shell消息联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unionshell__remote__msg.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

远端Shell消息联合体（Message Union）。

```c
#include <zephyr/shell/shell_remote_common.h>
```

<a id="details"></a>

远端Shell消息联合体（Message Union）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 17.1\_数据成员（Data Fields）

<a id="r_a15fd45da0248ebbe781674969d36a866"></a>

```c
struct shell_remote_msg_generic * generic
```

相关声明：[shell_remote_msg_generic](P014_远端Shell通用消息.md)、[generic](#a15fd45da0248ebbe781674969d36a866)。

通用消息（Generic Message）。

<a id="r_a119a705c8f8221dce1f8030ab0f3a66a"></a>

```c
struct shell_remote_msg_print * print
```

相关声明：[shell_remote_msg_print](P015_远端Shell打印消息.md)、[print](#a119a705c8f8221dce1f8030ab0f3a66a)。

打印消息（Print Message）。

<a id="r_a8de3d7b63d61e8f1bcd1642254c7cda6"></a>

```c
struct shell_remote_msg_cmd * cmd
```

相关声明：[shell_remote_msg_cmd](P011_远端Shell命令消息.md)、[cmd](#a8de3d7b63d61e8f1bcd1642254c7cda6)。

命令（Command）。

<a id="r_a33e93c0e2a28c62c3481d201d54d6ef7"></a>

```c
struct shell_remote_msg_cmd_get * cmd_get
```

相关声明：[shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)、[cmd_get](#a33e93c0e2a28c62c3481d201d54d6ef7)。

获取命令（Get Command）。

<a id="r_a1ecdbe4c2e7f7a080839a5d56fd029ba"></a>

```c
struct shell_remote_msg_exec * exec
```

相关声明：[shell_remote_msg_exec](P013_远端Shell执行消息.md)、[exec](#a1ecdbe4c2e7f7a080839a5d56fd029ba)。

执行命令（Execute Command）。

<a id="r_a766c60920a68b0dd29e2c5bb0cce3b09"></a>

```c
struct shell_remote_msg_result * result
```

相关声明：[shell_remote_msg_result](P016_远端Shell结果消息.md)、[result](#a766c60920a68b0dd29e2c5bb0cce3b09)。

结果（Result）。

## 17.2\_详细说明（Detailed Documentation）

<a id="a8de3d7b63d61e8f1bcd1642254c7cda6"></a>

### `cmd`

```c
struct shell_remote_msg_cmd* shell_remote_msg::cmd
```

命令（Command）。

<a id="a33e93c0e2a28c62c3481d201d54d6ef7"></a>

### `cmd_get`

```c
struct shell_remote_msg_cmd_get* shell_remote_msg::cmd_get
```

获取命令（Get Command）。

<a id="a1ecdbe4c2e7f7a080839a5d56fd029ba"></a>

### `exec`

```c
struct shell_remote_msg_exec* shell_remote_msg::exec
```

执行命令（Execute Command）。

<a id="a15fd45da0248ebbe781674969d36a866"></a>

### `generic`

```c
struct shell_remote_msg_generic* shell_remote_msg::generic
```

通用消息（Generic Message）。

<a id="a119a705c8f8221dce1f8030ab0f3a66a"></a>

### `print`

```c
struct shell_remote_msg_print* shell_remote_msg::print
```

打印消息（Print Message）。

<a id="a766c60920a68b0dd29e2c5bb0cce3b09"></a>

### `result`

```c
struct shell_remote_msg_result* shell_remote_msg::result
```

结果（Result）。

## 17.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote_common.h](../../../include/zephyr/shell/shell_remote_common.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：消息结构含size_t、int、函数指针和其他对象指针，不能把这些C结构当成天然跨位宽、跨字节序的通用网络格式。指针字段是对应远端命令对象或处理函数的值，不能在错误的地址空间中直接解引用。

> 译注——源码核对：data[0]在原始声明中表示头部后的变长数据位置；它不自带存储容量。命令响应数据依次保存NUL结尾的语法和可选帮助文本，实际长度来自消息，不应由零长数组的sizeof推算。

> 译注——源码核对：消息联合体的成员是各消息类型的指针。应先根据通用头中的消息编号选择成员，再按对应消息格式解析；这不是同时容纳所有消息正文的内嵌结构。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 17.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote_common.h](P007_远端Shell公共头文件源码.md)
- [shell_remote_msg_generic](P014_远端Shell通用消息.md)
- [shell_remote_msg_print](P015_远端Shell打印消息.md)
- [shell_remote_msg_cmd](P011_远端Shell命令消息.md)
- [shell_remote_msg_cmd_get](P012_远端Shell获取命令消息.md)
- [shell_remote_msg_exec](P013_远端Shell执行消息.md)
- [shell_remote_msg_result](P016_远端Shell结果消息.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P016_远端Shell结果消息.md) · [返回大纲](大纲.md)
