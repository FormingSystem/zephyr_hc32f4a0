---
id: learning.zephyr-docs.network-core-model-reference.page-54
title: net_config_ssh_password_auth_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__config__ssh__password__auth.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_net\_config\_ssh\_password\_auth\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__config__ssh__password__auth.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

包含设备上sshd所用的口令认证（Password Authentication）配置数据。

```c
#include <zephyr/net/net_config.h>
```

<a id="details"></a>

包含设备上sshd所用的口令认证（Password Authentication）配置数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_ae1e2e6c1ddafd2139effc4905f759119"></a>

```c
const char * username
```

相关声明：[username](#ae1e2e6c1ddafd2139effc4905f759119)。

口令认证（Password Authentication）所用的用户名。

<a id="r_a3fda745e9cc9696f301e2cd08c08786a"></a>

```c
const char * password
```

相关声明：[password](#a3fda745e9cc9696f301e2cd08c08786a)。

口令认证（Password Authentication）所用的口令。

## 54.2\_详细说明（Detailed Documentation）

<a id="a3fda745e9cc9696f301e2cd08c08786a"></a>

### `password`

```c
const char* net_config_ssh_password_auth::password
```

口令认证（Password Authentication）所用的口令。

为NULL或空字符串时，禁用口令认证，仅允许公钥认证（Public Key Authentication）。

<a id="ae1e2e6c1ddafd2139effc4905f759119"></a>

### `username`

```c
const char* net_config_ssh_password_auth::username
```

口令认证（Password Authentication）所用的用户名。

为NULL或空字符串时，不使用用户名。用户名（Username）不能包含空格。

本数据类型文档由以下文件生成：

- `zephyr/net/net_config.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/net/net_config.h](https://docs.zephyrproject.org/latest/doxygen/html/net__config_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_net_config_ssh_key_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_net_context_结构体.md)
