---
id: learning.zephyr-docs.shell-backend-reference.page-4
title: Shell虚拟后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__dummy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Shell虚拟后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__dummy.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

用于测试的内存内Shell后端（In-memory Shell Backend）。

<a id="details"></a>

用于测试的内存内Shell后端（In-memory Shell Backend）。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_shell_5Fdummy_2Eh"></a>

```c
file shell_dummy.h
```

相关声明：[shell_dummy.h](P005_Shell虚拟后端头文件参考.md)。

Shell虚拟后端（Dummy Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gab54399f9fbe08aafb9a7bdf540ff1c70"></a>

```c
#define SHELL_DUMMY_DEFINE(_name)
```

相关声明：[SHELL_DUMMY_DEFINE](#gab54399f9fbe08aafb9a7bdf540ff1c70)。

定义Shell虚拟传输实例（Dummy Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga12827fc2f644eb4748408807d763419e"></a>

```c
const struct shell * shell_backend_dummy_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_dummy_get_ptr](#ga12827fc2f644eb4748408807d763419e)。

不应直接使用此函数。

<a id="r_gaa93489d27aab568d3ca04640e9d18391"></a>

```c
const char * shell_backend_dummy_get_output (const struct shell *sh, size_t *sizep)
```

相关声明：[shell_backend_dummy_get_output](#gaa93489d27aab568d3ca04640e9d18391)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

返回Shell中缓存的输出，并重置指针。

<a id="r_ga8eb6e736190c11fe4a6eb6a02a48f44f"></a>

```c
void shell_backend_dummy_clear_output (const struct shell *sh)
```

相关声明：[shell_backend_dummy_clear_output](#ga8eb6e736190c11fe4a6eb6a02a48f44f)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

清空Shell后端的输出缓冲区（Output Buffer）。

<a id="r_ga8f830aaae69ab4bb7ab5115a27566e6d"></a>

```c
int shell_backend_dummy_push_input (const struct shell *sh, const char *data, size_t len)
```

相关声明：[shell_backend_dummy_push_input](#ga8f830aaae69ab4bb7ab5115a27566e6d)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

向Shell虚拟后端推入输入数据（Input Data）。

<a id="r_gaa48156ae134db73dce185be3b461071d"></a>

```c
void shell_backend_dummy_clear_input (const struct shell *sh)
```

相关声明：[shell_backend_dummy_clear_input](#gaa48156ae134db73dce185be3b461071d)、[shell](../shell_core_reference/P004_Shell实例结构.md)。

清空Shell后端的输入缓冲区（Input Buffer）。

## 4.4\_详细说明（Detailed Documentation）

<a id="gab54399f9fbe08aafb9a7bdf540ff1c70"></a>

### `SHELL_DUMMY_DEFINE`

```c
#define SHELL_DUMMY_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_dummy.h>
```

展开值（Value）：

```c
static struct shell_dummy _name##_shell_dummy;                  \
struct shell_transport _name = {                                \
        .api = &shell_dummy_transport_api,                      \
        .ctx = (struct shell_dummy *)&_name##_shell_dummy       \
}
```

定义Shell虚拟传输实例（Dummy Transport Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例名称（Transport Instance Name）。 |

<a id="gaa48156ae134db73dce185be3b461071d"></a>

### `shell_backend_dummy_clear_input()`

```c
void shell_backend_dummy_clear_input ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell_dummy.h>
```

清空Shell后端的输入缓冲区（Input Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell指针。 |

<a id="ga8eb6e736190c11fe4a6eb6a02a48f44f"></a>

### `shell_backend_dummy_clear_output()`

```c
void shell_backend_dummy_clear_output ( const struct shell * sh)
```

```c
#include <zephyr/shell/shell_dummy.h>
```

清空Shell后端的输出缓冲区（Output Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell指针。 |

<a id="gaa93489d27aab568d3ca04640e9d18391"></a>

### `shell_backend_dummy_get_output()`

```c
const char * shell_backend_dummy_get_output ( const struct shell * sh, size_t * sizep )
```

```c
#include <zephyr/shell/shell_dummy.h>
```

返回Shell中缓存的输出，并重置指针。

返回的数据后始终紧接空字符（NUL），终止字符位于索引*sizep处。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell指针。 |
| `sizep` | 返回Shell缓冲区中的数据大小。 |

返回（Returns）：指向Shell输出缓冲区的指针。

<a id="ga12827fc2f644eb4748408807d763419e"></a>

### `shell_backend_dummy_get_ptr()`

```c
const struct shell * shell_backend_dummy_get_ptr ( void )
```

```c
#include <zephyr/shell/shell_dummy.h>
```

不应直接使用此函数。

提供Shell虚拟后端实例的指针。

函数返回Shell虚拟实例的指针。随后可将该实例传给shell_execute_cmd函数，以测试命令行为。

返回（Returns）：Shell实例指针。

<a id="ga8f830aaae69ab4bb7ab5115a27566e6d"></a>

### `shell_backend_dummy_push_input()`

```c
int shell_backend_dummy_push_input ( const struct shell * sh, const char * data, size_t len )
```

```c
#include <zephyr/shell/shell_dummy.h>
```

向Shell虚拟后端推入输入数据（Input Data）。

此函数将输入数据入队，后续读取操作会返回这些数据，可用于测试Shell输入处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `sh` | Shell指针。 |
| `data` | 待推入的输入数据。 |
| `len` | 输入数据长度。 |

返回（Returns）：成功为0；缓冲区已满为-ENOMEM。

## 4.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_dummy.h](../../../include/zephyr/shell/shell_dummy.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：虚拟后端（Dummy Backend）将输出存于内部缓冲。get_output写入NUL终止字符、返回当前长度并把内部长度清零，返回值仍指向同一内部数组。后续输出可能覆盖内容；需长期保存时应在读取后复制。

> 译注——源码核对：当前输出写入会为终止字符保留空间，容量不足时只保存可容纳的部分，但仍向传输调用方报告原请求长度已处理。测试不能只凭写入成功就认定全部输出已保存。

> 译注——源码核对：push_input空间不足时返回-ENOMEM且不追加数据；成功后可通知RX_RDY。读取推进input_pos，而输入已使用总长度直到clear_input才被清零。多轮测试需要按场景清理输入，不能把已经读过误当作容量自动回收。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.6\_原页交叉引用（Cross References）

- [shell_dummy.h](P005_Shell虚拟后端头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructshell__transport_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_Shell后端选择头文件源码.md) · [返回大纲](大纲.md) · [下一章](P005_Shell虚拟后端头文件参考.md)
