---
id: learning.zephyr-docs.network-service-model-reference.page-33
title: netmidi2_user_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__user.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_netmidi2\_user\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__user.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于用户的认证（User-Based Authentication）所用的用户名/口令对。

```c
#include <zephyr/net/midi2.h>
```

<a id="details"></a>

基于用户的认证（User-Based Authentication）所用的用户名/口令对。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 33.1\_数据成员（Data Fields）

<a id="r_a71fb204799bd53af65899e46ea771844"></a>

```c
const char * name
```

相关声明：[name](#a71fb204799bd53af65899e46ea771844)。

用于身份验证的用户名。

<a id="r_aa334b6f3b82e86e90b6c8c298cf094f6"></a>

```c
const char * password
```

相关声明：[password](#aa334b6f3b82e86e90b6c8c298cf094f6)。

用于身份验证的密码。

## 33.2\_详细说明（Detailed Documentation）

<a id="a71fb204799bd53af65899e46ea771844"></a>

### `name`

```c
const char* netmidi2_user::name
```

用于身份验证的用户名。

<a id="aa334b6f3b82e86e90b6c8c298cf094f6"></a>

### `password`

```c
const char* netmidi2_user::password
```

用于身份验证的密码。

本数据类型文档由以下文件生成：

- `zephyr/net/midi2.h`

## 33.3\_原页交叉引用（Cross References）

- [zephyr/net/midi2.h](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P032_netmidi2_session_结构体.md) · [返回大纲](大纲.md) · [下一章](P034_netmidi2_userlist_结构体.md)
