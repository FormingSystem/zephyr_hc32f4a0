---
id: learning.zephyr-docs.network-service-model-reference.page-34
title: netmidi2_userlist_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__userlist.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_netmidi2\_userlist\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnetmidi2__userlist.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于用户的认证（User-Based Authentication）所用的用户列表。

```c
#include <zephyr/net/midi2.h>
```

<a id="details"></a>

基于用户的认证（User-Based Authentication）所用的用户列表。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 34.1\_数据成员（Data Fields）

<a id="r_a84b04acb7bb17f81f164af79e6b6950d"></a>

```c
size_t n_users
```

相关声明：[n_users](#a84b04acb7bb17f81f164af79e6b6950d)。

列表中的用户数量。

<a id="r_aeca603e7b653c9dd616e32c00783d6dd"></a>

```c
const struct netmidi2_user users []
```

相关声明：[netmidi2_user](P033_netmidi2_user_结构体.md)、[users](#aeca603e7b653c9dd616e32c00783d6dd)。

用户名与密码对。

## 34.2\_详细说明（Detailed Documentation）

<a id="a84b04acb7bb17f81f164af79e6b6950d"></a>

### `n_users`

```c
size_t netmidi2_userlist::n_users
```

列表中的用户数量。

<a id="aeca603e7b653c9dd616e32c00783d6dd"></a>

### `users`

```c
const struct netmidi2_user netmidi2_userlist::users[]
```

用户名与密码对。

本数据类型文档由以下文件生成：

- `zephyr/net/midi2.h`

## 34.3\_原页交叉引用（Cross References）

- [zephyr/net/midi2.h](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html)
- [netmidi2_user](P033_netmidi2_user_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P033_netmidi2_user_结构体.md) · [返回大纲](大纲.md) · [下一章](P035_npf_rule_结构体.md)
