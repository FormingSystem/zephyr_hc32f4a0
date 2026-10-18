---
id: learning.zephyr-docs.api-platform-topic-reference.page-71
title: OpenThread 协议栈（Stack）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_OpenThread 协议栈（Stack）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

OpenThread协议栈（Stack）的公共头文件。

<a id="details"></a>

OpenThread 协议栈公共头文件（OpenThread Stack Public Header）。

自 1.11 版提供（Since 1.11）；接口版本（Version）0.8.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 71.1\_函数（Functions）

<a id="r_gad975528c91de66cd1054f3584bfcc957"></a>

```c
struct openthread_context * openthread_get_default_context (void)
```

相关声明：[openthread_get_default_context](#gad975528c91de66cd1054f3584bfcc957)。

获取指向默认 OpenThread 上下文（Context）的指针（Pointer）。

## 71.2\_详细说明（Detailed Documentation）

<a id="gad975528c91de66cd1054f3584bfcc957"></a>

### `openthread_get_default_context()`

```c
struct openthread_context * openthread_get_default_context ( void )
```

```c
#include <zephyr/net/openthread.h>
```

获取指向默认 OpenThread 上下文（Context）的指针（Pointer）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `!NULL` | 成功时返回。 |
| `NULL` | 失败。 |


## 71.3\_原页交叉引用（Cross References）

- [zephyr/net/openthread.h](../api_file_supplement_reference/P046_zephyr__net__openthread.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P070_网络（Networking）.md) · [返回大纲](大纲.md) · [下一章](P072_Ambiq Apollo2 引脚控制辅助工具（Pin control helpers）.md)
