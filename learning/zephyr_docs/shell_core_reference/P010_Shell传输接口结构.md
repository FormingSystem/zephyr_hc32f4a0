---
id: learning.zephyr-docs.shell-core-reference.page-10
title: Shell传输接口结构
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__transport__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Shell传输接口结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__transport__api.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell核心接口、实例与传输数据结构和完整头文件源码。源码跟踪译注与官方原文分开标示。

统一的Shell传输接口（Transport Interface）。

```c
#include <zephyr/shell/shell.h>
```

<a id="details"></a>

统一的Shell传输接口（Transport Interface）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a59afba962312a077343b440448d67135"></a>

```c
int(* init )(const struct shell_transport *transport, const void *config, shell_transport_handler_t evt_handler, void *context)
```

相关声明：[init](#a59afba962312a077343b440448d67135)、[shell_transport](P009_Shell传输实例.md)、[shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)。

初始化Shell传输接口的函数。

<a id="r_a94cc7843174a4aba668389a4b46928d3"></a>

```c
int(* uninit )(const struct shell_transport *transport)
```

相关声明：[uninit](#a94cc7843174a4aba668389a4b46928d3)、[shell_transport](P009_Shell传输实例.md)。

反初始化Shell传输接口的函数。

<a id="r_a95535c7195088e68230ecb306f105713"></a>

```c
int(* enable )(const struct shell_transport *transport, bool blocking_tx)
```

相关声明：[enable](#a95535c7195088e68230ecb306f105713)、[shell_transport](P009_Shell传输实例.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

以给定发送（TX）模式启用传输的函数。

<a id="r_a6bbf2905abcbf6ca564ecf3f07d95712"></a>

```c
int(* write )(const struct shell_transport *transport, const void *data, size_t length, size_t *cnt)
```

相关声明：[write](#a6bbf2905abcbf6ca564ecf3f07d95712)、[shell_transport](P009_Shell传输实例.md)。

向传输接口写入数据的函数。

<a id="r_aae0e8ad92065dbff10691c28045d0c8f"></a>

```c
int(* read )(const struct shell_transport *transport, void *data, size_t length, size_t *cnt)
```

相关声明：[read](#aae0e8ad92065dbff10691c28045d0c8f)、[shell_transport](P009_Shell传输实例.md)。

从传输接口读取数据的函数。

<a id="r_a3b447d16d7c30f994c582d67bde57ba8"></a>

```c
void(* update )(const struct shell_transport *transport)
```

相关声明：[update](#a3b447d16d7c30f994c582d67bde57ba8)、[shell_transport](P009_Shell传输实例.md)。

在Shell线程循环中调用的函数。

## 10.2\_详细说明（Detailed Documentation）

<a id="a95535c7195088e68230ecb306f105713"></a>

### `enable`

```c
int(* shell_transport_api::enable) (const struct shell_transport *transport, bool blocking_tx)
```

以给定发送（TX）模式启用传输的函数。

可用此函数重新配置TX，使其以阻塞模式（Blocking Mode）工作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `transport` | 传输实例的指针。 |
| `blocking_tx` | 为true时，以阻塞模式启用传输TX。 |

返回（Returns）：成功为0，失败为负的errno错误码，包括不支持该操作的情形。

<a id="a59afba962312a077343b440448d67135"></a>

### `init`

```c
int(* shell_transport_api::init) (const struct shell_transport *transport, const void *config, shell_transport_handler_t evt_handler, void *context)
```

初始化Shell传输接口的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] transport` | 传输实例的指针。 |
| `[in] config` | 实例配置（Instance Configuration）的指针。 |
| `[in] evt_handler` | 事件处理函数（Event Handler）。 |
| `[in] context` | 传给事件处理函数的上下文指针。 |

返回（Returns）：标准错误码（Standard Error Code）。

<a id="aae0e8ad92065dbff10691c28045d0c8f"></a>

### `read`

```c
int(* shell_transport_api::read) (const struct shell_transport *transport, void *data, size_t length, size_t *cnt)
```

从传输接口读取数据的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] transport` | 传输实例的指针。 |
| `[in] data` | 目标缓冲区（Destination Buffer）的指针。 |
| `[in] length` | 目标缓冲区长度。 |
| `[out] cnt` | 已接收字节计数器的指针。 |

返回（Returns）：标准错误码（Standard Error Code）。

<a id="a94cc7843174a4aba668389a4b46928d3"></a>

### `uninit`

```c
int(* shell_transport_api::uninit) (const struct shell_transport *transport)
```

反初始化Shell传输接口的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] transport` | 传输实例的指针。 |

返回（Returns）：标准错误码（Standard Error Code）。

<a id="a3b447d16d7c30f994c582d67bde57ba8"></a>

### `update`

```c
void(* shell_transport_api::update) (const struct shell_transport *transport)
```

在Shell线程循环中调用的函数。

可用于需要较长执行时间的后端操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] transport` | 传输实例的指针。 |

<a id="a6bbf2905abcbf6ca564ecf3f07d95712"></a>

### `write`

```c
int(* shell_transport_api::write) (const struct shell_transport *transport, const void *data, size_t length, size_t *cnt)
```

向传输接口写入数据的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] transport` | 传输实例的指针。 |
| `[in] data` | 源缓冲区（Source Buffer）的指针。 |
| `[in] length` | 源缓冲区长度。 |
| `[out] cnt` | 已发送字节计数器的指针。 |

返回（Returns）：标准错误码（Standard Error Code）。

## 10.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)、[subsys/shell/shell.c](../../../subsys/shell/shell.c)、[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文。源码与公开接口按本次官方快照核对，未将隐藏的内部条目补造为公开说明。

> 译注——源码核对：传输接口将后端操作表和实例上下文分开。read与write通过计数器返回实际接收或发送字节数，函数状态码与处理字节数不是同一概念。

> 译注——源码核对：传输事件回调收到初始化时提供的不透明上下文。uninit完成回调则在Shell线程退出前调用；不能把这两种回调的生命周期和执行上下文混为一谈。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell.h](P003_Shell核心头文件源码.md)
- [shell_transport](P009_Shell传输实例.md)
- [shell_transport_handler_t](P001_Shell核心接口.md#ga265807c2d8eba7b9ea633968627e085d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_Shell传输实例.md) · [返回大纲](大纲.md) · [下一章](P011_Shell命令条目联合体.md)
