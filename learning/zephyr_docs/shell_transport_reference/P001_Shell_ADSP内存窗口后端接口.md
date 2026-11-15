---
id: learning.zephyr-docs.shell-transport-reference.page-1
title: Shell_ADSP内存窗口后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__adsp__memory__window.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Shell\_ADSP内存窗口后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__adsp__memory__window.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

通过ADSP内存窗口（Memory Window）访问Shell。

<a id="details"></a>

通过ADSP内存窗口（Memory Window）访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_shell_5Fadsp_5Fmemory_5Fwindow_2Eh"></a>

```c
file shell_adsp_memory_window.h
```

相关声明：[shell_adsp_memory_window.h](P002_Shell_ADSP内存窗口后端头文件参考.md)。

Shell ADSP内存窗口后端的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga2d5483ee279894ca82bc14b41c3d3745"></a>

```c
#define SHELL_ADSP_MEMORY_WINDOW_DEFINE(_name)
```

相关声明：[SHELL_ADSP_MEMORY_WINDOW_DEFINE](#ga2d5483ee279894ca82bc14b41c3d3745)。

定义Shell ADSP内存窗口传输实例（Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga03636e7b928b9c6a21d54270ba95480b"></a>

```c
const struct shell * shell_backend_adsp_memory_window_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_adsp_memory_window_get_ptr](#ga03636e7b928b9c6a21d54270ba95480b)。

此函数提供Shell ADSP内存窗口后端实例的指针。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga2d5483ee279894ca82bc14b41c3d3745"></a>

### `SHELL_ADSP_MEMORY_WINDOW_DEFINE`

```c
#define SHELL_ADSP_MEMORY_WINDOW_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_adsp_memory_window.h>
```

展开值（Value）：

```c
static struct shell_adsp_memory_window _name##_shell_adsp_memory_window;\
struct shell_transport _name = {                                        \
        .api = &shell_adsp_memory_window_transport_api,         \
        .ctx = &_name##_shell_adsp_memory_window,       \
}
```

定义Shell ADSP内存窗口传输实例（Transport Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例名称（Transport Instance Name）。 |

<a id="ga03636e7b928b9c6a21d54270ba95480b"></a>

### `shell_backend_adsp_memory_window_get_ptr()`

```c
const struct shell * shell_backend_adsp_memory_window_get_ptr ( void )
```

```c
#include <zephyr/shell/shell_adsp_memory_window.h>
```

此函数提供Shell ADSP内存窗口后端实例的指针。

函数返回Shell ADSP内存窗口实例的指针。随后可将该实例传给shell_execute_cmd函数，以测试命令行为。

返回（Returns）：Shell实例指针。

## 1.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_adsp_memory_window.h](../../../include/zephyr/shell/shell_adsp_memory_window.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：ADSP内存窗口后端通过sys_winstream写入和读取共享内存字节流（Shared-memory Byte Stream），接收侧维护读取序号（Read Sequence Number）。get_ptr返回静态Shell实例，不创建新的通信端点。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [shell_adsp_memory_window.h](P002_Shell_ADSP内存窗口后端头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructshell__transport_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Shell_ADSP内存窗口后端头文件参考.md)
