---
id: learning.zephyr-docs.shell-core-reference.page-9
title: Shell传输实例
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structshell__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Shell传输实例

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structshell__transport.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell核心接口、实例与传输数据结构和完整头文件源码。源码跟踪译注与官方原文分开标示。

Shell传输实例（Transport Instance）。

```c
#include <zephyr/shell/shell.h>
```

<a id="details"></a>

Shell传输实例（Transport Instance）。它将传输后端实现shell_transport_api与每个实例各自的上下文绑定。实例由后端的SHELL_*_DEFINE宏创建，Shell实例通过自身的传输接口引用它。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_ab4bee270415b445ded5a8ba6e8cb3a25"></a>

```c
const struct shell_transport_api * api
```

相关声明：[shell_transport_api](P010_Shell传输接口结构.md)、[api](#ab4bee270415b445ded5a8ba6e8cb3a25)。

传输后端操作（Transport Backend Operations）。

<a id="r_a02f44bb376152452f5b5d20f33ccbdf6"></a>

```c
void * ctx
```

相关声明：[ctx](#a02f44bb376152452f5b5d20f33ccbdf6)。

传输实例上下文（Transport Instance Context）。

## 9.2\_详细说明（Detailed Documentation）

<a id="ab4bee270415b445ded5a8ba6e8cb3a25"></a>

### `api`

```c
const struct shell_transport_api* shell_transport::api
```

传输后端操作（Transport Backend Operations）。

<a id="a02f44bb376152452f5b5d20f33ccbdf6"></a>

### `ctx`

```c
void* shell_transport::ctx
```

传输实例上下文（Transport Instance Context）。

## 9.3\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell.h](../../../include/zephyr/shell/shell.h)、[subsys/shell/shell.c](../../../subsys/shell/shell.c)、[subsys/shell/shell_utils.c](../../../subsys/shell/shell_utils.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文。源码与公开接口按本次官方快照核对，未将隐藏的内部条目补造为公开说明。

> 译注——源码核对：传输接口将后端操作表和实例上下文分开。read与write通过计数器返回实际接收或发送字节数，函数状态码与处理字节数不是同一概念。

> 译注——源码核对：传输事件回调收到初始化时提供的不透明上下文。uninit完成回调则在Shell线程退出前调用；不能把这两种回调的生命周期和执行上下文混为一谈。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.4\_原页交叉引用（Cross References）

- [zephyr/shell/shell.h](P003_Shell核心头文件源码.md)
- [shell_transport_api](P010_Shell传输接口结构.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_Shell静态命令条目.md) · [返回大纲](大纲.md) · [下一章](P010_Shell传输接口结构.md)
