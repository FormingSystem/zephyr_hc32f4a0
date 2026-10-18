---
id: learning.zephyr-docs.shell-transport-reference.page-7
title: Shell_Telnet后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__telnet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Shell\_Telnet后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__telnet.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入ADSP内存窗口、MQTT、Telnet和WebSocket后端的参考与源码。源码跟踪译注与官方原文分开标示。

通过TELNET连接访问Shell。

<a id="details"></a>

通过TELNET连接访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_shell_5Ftelnet_2Eh"></a>

```c
file shell_telnet.h
```

相关声明：[shell_telnet.h](P008_Shell_Telnet后端头文件参考.md)。

Shell Telnet后端（Telnet Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga82cf4289a4a5d724edd2d4d333eafe4e"></a>

```c
#define SHELL_TELNET_DEFINE(_name)
```

相关声明：[SHELL_TELNET_DEFINE](#ga82cf4289a4a5d724edd2d4d333eafe4e)。

定义Shell Telnet传输实例（Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga628b99d20ef08a0b1165af07aee4888c"></a>

```c
const struct shell * shell_backend_telnet_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_telnet_get_ptr](#ga628b99d20ef08a0b1165af07aee4888c)。

此函数提供Shell Telnet后端实例的指针。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga82cf4289a4a5d724edd2d4d333eafe4e"></a>

### `SHELL_TELNET_DEFINE`

```c
#define SHELL_TELNET_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_telnet.h>
```

展开值（Value）：

```c
static struct shell_telnet _name##_shell_telnet;                \
struct shell_transport _name = {                                \
        .api = &shell_telnet_transport_api,                     \
        .ctx = (struct shell_telnet *)&_name##_shell_telnet     \
}
```

定义Shell Telnet传输实例（Transport Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例名称（Transport Instance Name）。 |

<a id="ga628b99d20ef08a0b1165af07aee4888c"></a>

### `shell_backend_telnet_get_ptr()`

```c
const struct shell * shell_backend_telnet_get_ptr ( void )
```

```c
#include <zephyr/shell/shell_telnet.h>
```

此函数提供Shell Telnet后端实例的指针。

函数返回Shell Telnet实例的指针。随后可将该实例传给shell_execute_cmd函数，以测试命令行为。

返回（Returns）：Shell实例指针。

## 7.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_telnet.h](../../../include/zephyr/shell/shell_telnet.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：DEFINE宏创建传输对象及静态上下文，get_ptr取得配置好的Shell实例。返回实例地址并不表示已有Telnet客户端连接；连接及输入输出由传输实现负责。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.6\_原页交叉引用（Cross References）

- [shell_telnet.h](P008_Shell_Telnet后端头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructshell__transport_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_Shell_MQTT后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_Shell_Telnet后端头文件参考.md)
