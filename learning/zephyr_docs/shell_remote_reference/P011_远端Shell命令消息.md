---
id: learning.zephyr-docs.shell-remote-reference.page-11
title: 远端Shell命令消息
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__msg__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_远端Shell命令消息

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__msg__cmd.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

获取命令请求的响应（Response to Get Command）。

```c
#include <zephyr/shell/shell_remote_common.h>
```

<a id="details"></a>

获取命令请求的响应（Response to Get Command）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_aadc28558b4ecbf31c42d886b6f42b2a9"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#aadc28558b4ecbf31c42d886b6f42b2a9)。

消息编号（Message ID）。

<a id="r_afdaf8c8fd47440d0c487d75ae072d468"></a>

```c
const union shell_cmd_entry * subcmd
```

相关声明：[shell_cmd_entry](../shell_core_reference/P011_Shell命令条目联合体.md)、[subcmd](#afdaf8c8fd47440d0c487d75ae072d468)。

子命令（Subcommand）。

<a id="r_a39ed2f88f0bf01a68b327be6067f0818"></a>

```c
const struct shell_static_entry * entry
```

相关声明：[shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)、[entry](#a39ed2f88f0bf01a68b327be6067f0818)。

条目（Entry）。

<a id="r_a04251b73dbc44e09f8dc386fd5128af9"></a>

```c
shell_cmd_handler handler
```

相关声明：[shell_cmd_handler](../shell_core_reference/P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)、[handler](#a04251b73dbc44e09f8dc386fd5128af9)。

命令处理函数（Command Handler）。

<a id="r_a45f35f76aac5f6a29e5b7bbcfc312d2b"></a>

```c
struct shell_static_args args
```

相关声明：[shell_static_args](../shell_core_reference/P007_Shell命令参数约束.md)、[args](#a45f35f76aac5f6a29e5b7bbcfc312d2b)。

命令参数（Command Parameters）。

<a id="r_a400f454b15a9f69463bc79ccfee9a904"></a>

```c
char data [0]
```

相关声明：[data](#a400f454b15a9f69463bc79ccfee9a904)。

数据：以空字符（NUL）结尾的命令语法文本，后接可选的帮助文本。

## 11.2\_详细说明（Detailed Documentation）

<a id="a45f35f76aac5f6a29e5b7bbcfc312d2b"></a>

### `args`

```c
struct shell_static_args shell_remote_msg_cmd::args
```

命令参数（Command Parameters）。

<a id="a400f454b15a9f69463bc79ccfee9a904"></a>

### `data`

```c
char shell_remote_msg_cmd::data[0]
```

数据：以空字符（NUL）结尾的命令语法文本，后接可选的帮助文本。

<a id="a39ed2f88f0bf01a68b327be6067f0818"></a>

### `entry`

```c
const struct shell_static_entry* shell_remote_msg_cmd::entry
```

条目（Entry）。

<a id="a04251b73dbc44e09f8dc386fd5128af9"></a>

### `handler`

```c
shell_cmd_handler shell_remote_msg_cmd::handler
```

命令处理函数（Command Handler）。

<a id="aadc28558b4ecbf31c42d886b6f42b2a9"></a>

### `id`

```c
uint8_t shell_remote_msg_cmd::id
```

消息编号（Message ID）。

<a id="afdaf8c8fd47440d0c487d75ae072d468"></a>

### `subcmd`

```c
const union shell_cmd_entry* shell_remote_msg_cmd::subcmd
```

子命令（Subcommand）。

## 11.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote_common.h](../../../include/zephyr/shell/shell_remote_common.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：消息结构含size_t、int、函数指针和其他对象指针，不能把这些C结构当成天然跨位宽、跨字节序的通用网络格式。指针字段是对应远端命令对象或处理函数的值，不能在错误的地址空间中直接解引用。

> 译注——源码核对：data[0]在原始声明中表示头部后的变长数据位置；它不自带存储容量。命令响应数据依次保存NUL结尾的语法和可选帮助文本，实际长度来自消息，不应由零长数组的sizeof推算。

> 译注——源码核对：消息联合体的成员是各消息类型的指针。应先根据通用头中的消息编号选择成员，再按对应消息格式解析；这不是同时容纳所有消息正文的内嵌结构。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 11.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote_common.h](P007_远端Shell公共头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [shell_cmd_entry](../shell_core_reference/P011_Shell命令条目联合体.md)
- [shell_static_entry](../shell_core_reference/P008_Shell静态命令条目.md)
- [shell_cmd_handler](../shell_core_reference/P001_Shell核心接口.md#ga331e7d19b9b0755486596f5ffc598338)
- [shell_static_args](../shell_core_reference/P007_Shell命令参数约束.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_远端Shell运行数据.md) · [返回大纲](大纲.md) · [下一章](P012_远端Shell获取命令消息.md)
