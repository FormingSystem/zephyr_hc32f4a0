---
id: learning.zephyr-docs.shell-backend-reference.page-1
title: Shell后端目录
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__backends.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Shell后端目录

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__backends.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

将Shell实例连接到通信通道（Communication Channel）的传输后端（Transport Backend）。

<a id="details"></a>

将Shell实例连接到通信通道（Communication Channel）的传输后端（Transport Backend）。

Shell实例由UART、RTT、Telnet、MQTT、WebSocket、SSH、RPMsg等传输后端驱动。通常通过相应Kconfig选项选择并启用后端，例如CONFIG_SHELL_BACKEND_SERIAL；Shell子系统会自动实例化所配置的后端。应用通常不会直接引用本组中的符号。

因此，每个后端头文件只暴露少量、主要面向实现的接口：

- `SHELL_<name>_DEFINE()`宏用于实例化传输对象，由后端实现自身使用，也可用于自定义实例。
- `shell_backend_<name>_get_ptr()`访问函数返回该后端的Shell实例，供少数需要指定后端的调用者使用，例如测试中的虚拟后端或管理代码中的UART后端。
- 某些后端还提供专用辅助函数。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_shell_5Fadsp_5Fmemory_5Fwindow"></a>

相关声明：[ADSP内存窗口后端（Memory Window Backend）](../shell_transport_reference/P001_Shell_ADSP内存窗口后端接口.md)。

通过ADSP内存窗口（Memory Window）访问Shell。

<a id="r_shell_5Fdummy"></a>

相关声明：[虚拟后端（Dummy Backend）](P004_Shell虚拟后端接口.md)。

用于测试的内存内Shell后端（In-memory Shell Backend）。

<a id="r_shell_5Fmqtt"></a>

相关声明：[MQTT后端（MQTT Backend）](../shell_transport_reference/P004_Shell_MQTT后端接口.md)。

通过MQTT连接访问Shell。

<a id="r_shell_5Frpmsg"></a>

相关声明：[RPMsg后端（RPMsg Backend）](../intercore_reference/P178_RPMsg命令行后端接口.md)。

通过RPMsg端点（Endpoint）访问Shell。

<a id="r_shell_5Frtt"></a>

相关声明：[RTT后端（RTT Backend）](P007_Shell_RTT后端接口.md)。

通过SEGGER实时传输（Real Time Transfer，RTT）通道访问Shell。

<a id="r_shell_5Fssh"></a>

相关声明：[SSH后端（SSH Backend）](../shell_ssh_reference/P001_Shell_SSH后端接口.md)。

通过SSH连接访问Shell。

<a id="r_shell_5Ftelnet"></a>

相关声明：[Telnet后端（Telnet Backend）](../shell_transport_reference/P007_Shell_Telnet后端接口.md)。

通过TELNET连接访问Shell。

<a id="r_shell_5Fuart"></a>

相关声明：[UART后端（UART Backend）](P010_Shell_UART后端接口.md)。

通过通用异步收发器（UART）串行连接访问Shell。

<a id="r_shell_5Fwebsocket"></a>

相关声明：[WebSocket后端（WebSocket Backend）](../shell_transport_reference/P010_Shell_WebSocket后端接口.md)。

通过WebSocket连接访问Shell。

<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_shell_5Fbackend_2Eh"></a>

```c
file shell_backend.h
```

相关声明：[shell_backend.h](P002_Shell后端选择头文件参考.md)。

Shell后端访问函数（Backend Accessors）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gad299b24f7d116d733c3f9ccc839fdb2b"></a>

```c
static const struct shell * shell_backend_get (uint32_t idx)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_get](#gad299b24f7d116d733c3f9ccc839fdb2b)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

按索引取得Shell后端（Backend）。

<a id="r_gafcf533acf3e0540c6798e58d4c1f7528"></a>

```c
static int shell_backend_count_get (void)
```

相关声明：[shell_backend_count_get](#gafcf533acf3e0540c6798e58d4c1f7528)。

取得后端数量（Backend Count）。

<a id="r_ga34edbd459f8acce386a2f953bc6c795f"></a>

```c
const struct shell * shell_backend_get_by_name (const char *backend_name)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_get_by_name](#ga34edbd459f8acce386a2f953bc6c795f)。

按名称取得后端（Backend）。

## 1.4\_详细说明（Detailed Documentation）

<a id="gafcf533acf3e0540c6798e58d4c1f7528"></a>

### `shell_backend_count_get()`

```c
int shell_backend_count_get ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/shell/shell_backend.h>
```

取得后端数量（Backend Count）。

返回（Returns）：后端数量。

<a id="gad299b24f7d116d733c3f9ccc839fdb2b"></a>

### `shell_backend_get()`

```c
const struct shell * shell_backend_get ( uint32_t idx)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/shell/shell_backend.h>
```

按索引取得Shell后端（Backend）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] idx` | 后端索引，范围为0至shell_backend_count_get() - 1。 |

返回（Returns）：给定索引处的后端实例指针。

<a id="ga34edbd459f8acce386a2f953bc6c795f"></a>

### `shell_backend_get_by_name()`

```c
const struct shell * shell_backend_get_by_name ( const char * backend_name)
```

```c
#include <zephyr/shell/shell_backend.h>
```

按名称取得后端（Backend）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] backend_name` | 由SHELL_DEFINE定义的后端名称（Backend Name）。 |

返回（Returns）：找到时返回后端实例指针；未找到时返回NULL。

## 1.5\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_backend.h](../../../include/zephyr/shell/shell_backend.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：后端索引（Backend Index）来自可遍历链接段（Iterable Section）。应先读取count并保证索引落在接口约定范围内；接口没有承诺越界时返回NULL。按名称查找则遍历Shell实例并用strcmp精确比较，未找到返回NULL。

> 译注——源码核对：传输后端（Transport Backend）连接Shell与通信通道；日志后端（Log Backend）将日志交给Shell输出。两者职责不同，启用某种传输本身不等价于启用日志输出。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [ADSP内存窗口后端（Memory Window Backend）](../shell_transport_reference/P001_Shell_ADSP内存窗口后端接口.md)
- [虚拟后端（Dummy Backend）](P004_Shell虚拟后端接口.md)
- [MQTT后端（MQTT Backend）](../shell_transport_reference/P004_Shell_MQTT后端接口.md)
- [RPMsg后端（RPMsg Backend）](../intercore_reference/P178_RPMsg命令行后端接口.md)
- [RTT后端（RTT Backend）](P007_Shell_RTT后端接口.md)
- [SSH后端（SSH Backend）](../shell_ssh_reference/P001_Shell_SSH后端接口.md)
- [Telnet后端（Telnet Backend）](../shell_transport_reference/P007_Shell_Telnet后端接口.md)
- [UART后端（UART Backend）](P010_Shell_UART后端接口.md)
- [WebSocket后端（WebSocket Backend）](../shell_transport_reference/P010_Shell_WebSocket后端接口.md)
- [shell_backend.h](P002_Shell后端选择头文件参考.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [CONFIG_SHELL_BACKEND_SERIAL](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Shell后端选择头文件参考.md)
