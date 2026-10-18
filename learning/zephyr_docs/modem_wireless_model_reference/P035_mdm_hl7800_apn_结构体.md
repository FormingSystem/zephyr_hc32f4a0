---
id: learning.zephyr-docs.modem-wireless-model-reference.page-35
title: mdm_hl7800_apn_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__apn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_mdm\_hl7800\_apn\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdm__hl7800__apn.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接入点名称（Access Point Name，APN）的配置。

```c
#include <zephyr/drivers/modem/hl7800.h>
```

<a id="details"></a>

接入点名称（Access Point Name，APN）的配置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 35.1\_数据成员（Data Fields）

<a id="r_a37f48ac1e950f0df59d07a6a83bb5cc9"></a>

```c
char value [64]
```

相关声明：[value](#a37f48ac1e950f0df59d07a6a83bb5cc9)。

接入点名称（APN）。

<a id="r_abfe087e7989513937c43a28dd83deb21"></a>

```c
char username [65]
```

相关声明：[username](#abfe087e7989513937c43a28dd83deb21)。

APN 用户名。

<a id="r_a876db3a5fdf4ce805536d84b96213495"></a>

```c
char password [65]
```

相关声明：[password](#a876db3a5fdf4ce805536d84b96213495)。

APN 密码。

## 35.2\_详细说明（Detailed Documentation）

<a id="a876db3a5fdf4ce805536d84b96213495"></a>

### `password`

```c
char mdm_hl7800_apn::password[65]
```

APN 密码。

<a id="abfe087e7989513937c43a28dd83deb21"></a>

### `username`

```c
char mdm_hl7800_apn::username[65]
```

APN 用户名。

<a id="a37f48ac1e950f0df59d07a6a83bb5cc9"></a>

### `value`

```c
char mdm_hl7800_apn::value[64]
```

接入点名称（APN）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl7800.h`

## 35.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl7800.h](https://docs.zephyrproject.org/latest/doxygen/html/hl7800_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P034_lorawan_join_otaa_结构体.md) · [返回大纲](大纲.md) · [下一章](P036_mdm_hl7800_callback_agent_结构体.md)
