---
id: learning.zephyr-docs.shell-remote-reference.page-14
title: 远端Shell通用消息
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__msg__generic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_远端Shell通用消息

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__remote__msg__generic.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入远端Shell接口、命令行接口与消息数据结构。源码跟踪译注与官方原文分开标示。

通用消息（Generic Message）。

```c
#include <zephyr/shell/shell_remote_common.h>
```

<a id="details"></a>

通用消息（Generic Message）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a8e020f1dd46da8efecc8b3d362fda0e1"></a>

```c
uint8_t id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[id](#a8e020f1dd46da8efecc8b3d362fda0e1)。

消息编号（Message ID）。

## 14.2\_详细说明（Detailed Documentation）

<a id="a8e020f1dd46da8efecc8b3d362fda0e1"></a>

### `id`

```c
uint8_t shell_remote_msg_generic::id
```

消息编号（Message ID）。

## 14.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_remote_common.h](../../../include/zephyr/shell/shell_remote_common.h)、[subsys/shell/shell_remote.c](../../../subsys/shell/shell_remote.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：消息结构含size_t、int、函数指针和其他对象指针，不能把这些C结构当成天然跨位宽、跨字节序的通用网络格式。指针字段是对应远端命令对象或处理函数的值，不能在错误的地址空间中直接解引用。

> 译注——源码核对：data[0]在原始声明中表示头部后的变长数据位置；它不自带存储容量。命令响应数据依次保存NUL结尾的语法和可选帮助文本，实际长度来自消息，不应由零长数组的sizeof推算。

> 译注——源码核对：消息联合体的成员是各消息类型的指针。应先根据通用头中的消息编号选择成员，再按对应消息格式解析；这不是同时容纳所有消息正文的内嵌结构。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 14.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell_remote_common.h](P007_远端Shell公共头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_远端Shell执行消息.md) · [返回大纲](大纲.md) · [下一章](P015_远端Shell打印消息.md)
