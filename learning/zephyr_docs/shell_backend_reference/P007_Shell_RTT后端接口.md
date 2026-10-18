---
id: learning.zephyr-docs.shell-backend-reference.page-7
title: Shell_RTT后端接口
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__rtt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_Shell\_RTT后端接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__rtt.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

通过SEGGER实时传输（Real Time Transfer，RTT）通道访问Shell。

<a id="details"></a>

通过SEGGER实时传输（Real Time Transfer，RTT）通道访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_shell_5Frtt_2Eh"></a>

```c
file shell_rtt.h
```

相关声明：[shell_rtt.h](P008_Shell_RTT后端头文件参考.md)。

Shell RTT后端（RTT Backend）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_ga58deb777f206a6afbc77c9d047204c7a"></a>

```c
#define SHELL_RTT_DEFINE(_name)
```

相关声明：[SHELL_RTT_DEFINE](#ga58deb777f206a6afbc77c9d047204c7a)。

定义Shell RTT传输实例（RTT Transport Instance）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.3\_函数（Functions）

<a id="r_ga74ccc10cf40cd54f6d4d28f5e62f3091"></a>

```c
const struct shell * shell_backend_rtt_get_ptr (void)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_rtt_get_ptr](#ga74ccc10cf40cd54f6d4d28f5e62f3091)。

提供Shell RTT后端实例的指针。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga58deb777f206a6afbc77c9d047204c7a"></a>

### `SHELL_RTT_DEFINE`

```c
#define SHELL_RTT_DEFINE ( _name)
```

```c
#include <zephyr/shell/shell_rtt.h>
```

展开值（Value）：

```c
static struct shell_rtt _name##_shell_rtt;                      \
struct shell_transport _name = {                                \
        .api = &shell_rtt_transport_api,                        \
        .ctx = (struct shell_rtt *)&_name##_shell_rtt           \
}
```

定义Shell RTT传输实例（RTT Transport Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 传输实例名称（Transport Instance Name）。 |

<a id="ga74ccc10cf40cd54f6d4d28f5e62f3091"></a>

### `shell_backend_rtt_get_ptr()`

```c
const struct shell * shell_backend_rtt_get_ptr ( void )
```

```c
#include <zephyr/shell/shell_rtt.h>
```

提供Shell RTT后端实例的指针。

函数返回Shell RTT实例的指针。随后可将该实例传给shell_execute_cmd函数，以测试命令行为。

返回（Returns）：Shell实例指针。

## 7.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_rtt.h](../../../include/zephyr/shell/shell_rtt.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：RTT（Real Time Transfer）通过调试通道传输数据；get_ptr取得已定义的Shell实例地址，不负责建立调试探针连接。DEFINE宏创建传输对象及其上下文，Shell实例和传输实例不要混为一谈。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.6\_原页交叉引用（Cross References）

- [shell_rtt.h](P008_Shell_RTT后端头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_transport](../shell_core_reference/P009_Shell传输实例.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astructshell__transport_html"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P006_Shell虚拟后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P008_Shell_RTT后端头文件参考.md)
