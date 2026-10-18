---
id: learning.zephyr-docs.shell-backend-reference.page-5
title: Shell虚拟后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__dummy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_Shell虚拟后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__dummy_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell虚拟后端（Dummy Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/shell/shell.h>
```

查看此文件的源码。

Shell虚拟后端（Dummy Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_gab54399f9fbe08aafb9a7bdf540ff1c70"></a>

```c
#define SHELL_DUMMY_DEFINE(_name)
```

相关声明：[SHELL_DUMMY_DEFINE](P004_Shell虚拟后端接口.md#gab54399f9fbe08aafb9a7bdf540ff1c70)。

定义Shell虚拟传输实例（Dummy Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.2\_函数（Functions）

<a id="r_ga12827fc2f644eb4748408807d763419e"></a>

```c
const struct shell * shell_backend_dummy_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_dummy_get_ptr](P004_Shell虚拟后端接口.md#ga12827fc2f644eb4748408807d763419e)。

不应直接使用此函数。

<a id="r_gaa93489d27aab568d3ca04640e9d18391"></a>

```c
const char * shell_backend_dummy_get_output (const struct shell *sh, size_t *sizep)
```

相关声明：[shell_backend_dummy_get_output](P004_Shell虚拟后端接口.md#gaa93489d27aab568d3ca04640e9d18391)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

返回Shell中缓存的输出，并重置指针。

<a id="r_ga8eb6e736190c11fe4a6eb6a02a48f44f"></a>

```c
void shell_backend_dummy_clear_output (const struct shell *sh)
```

相关声明：[shell_backend_dummy_clear_output](P004_Shell虚拟后端接口.md#ga8eb6e736190c11fe4a6eb6a02a48f44f)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

清空Shell后端的输出缓冲区（Output Buffer）。

<a id="r_ga8f830aaae69ab4bb7ab5115a27566e6d"></a>

```c
int shell_backend_dummy_push_input (const struct shell *sh, const char *data, size_t len)
```

相关声明：[shell_backend_dummy_push_input](P004_Shell虚拟后端接口.md#ga8f830aaae69ab4bb7ab5115a27566e6d)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

向Shell虚拟后端推入输入数据（Input Data）。

<a id="r_gaa48156ae134db73dce185be3b461071d"></a>

```c
void shell_backend_dummy_clear_input (const struct shell *sh)
```

相关声明：[shell_backend_dummy_clear_input](P004_Shell虚拟后端接口.md#gaa48156ae134db73dce185be3b461071d)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

清空Shell后端的输入缓冲区（Input Buffer）。

## 5.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_dummy.h](../../../include/zephyr/shell/shell_dummy.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：虚拟后端（Dummy Backend）将输出存于内部缓冲。get_output写入NUL终止字符、返回当前长度并把内部长度清零，返回值仍指向同一内部数组。后续输出可能覆盖内容；需长期保存时应在读取后复制。

> 译注——源码核对：当前输出写入会为终止字符保留空间，容量不足时只保存可容纳的部分，但仍向传输调用方报告原请求长度已处理。测试不能只凭写入成功就认定全部输出已保存。

> 译注——源码核对：push_input空间不足时返回-ENOMEM且不追加数据；成功后可通知RX_RDY。读取推进input_pos，而输入已使用总长度直到clear_input才被清零。多轮测试需要按场景清理输入，不能把已经读过误当作容量自动回收。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [查看此文件的源码](P006_Shell虚拟后端头文件源码.md)
- [SHELL_DUMMY_DEFINE](P004_Shell虚拟后端接口.md#gab54399f9fbe08aafb9a7bdf540ff1c70)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_dummy_get_ptr](P004_Shell虚拟后端接口.md#ga12827fc2f644eb4748408807d763419e)
- [shell_backend_dummy_get_output](P004_Shell虚拟后端接口.md#gaa93489d27aab568d3ca04640e9d18391)
- [shell_backend_dummy_clear_output](P004_Shell虚拟后端接口.md#ga8eb6e736190c11fe4a6eb6a02a48f44f)
- [shell_backend_dummy_push_input](P004_Shell虚拟后端接口.md#ga8f830aaae69ab4bb7ab5115a27566e6d)
- [shell_backend_dummy_clear_input](P004_Shell虚拟后端接口.md#gaa48156ae134db73dce185be3b461071d)

<a id="header-details"></a>

---

[上一章](P004_Shell虚拟后端接口.md) · [返回大纲](大纲.md) · [下一章](P006_Shell虚拟后端头文件源码.md)
