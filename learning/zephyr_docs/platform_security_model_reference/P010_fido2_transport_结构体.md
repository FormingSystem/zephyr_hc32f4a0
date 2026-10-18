---
id: learning.zephyr-docs.platform-security-model-reference.page-10
title: fido2_transport_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfido2__transport.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_fido2\_transport\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfido2__transport.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

已注册的FIDO2传输（Transport）。

```c
#include <zephyr/authentication/fido2/fido2_transport.h>
```

<a id="details"></a>

已注册的FIDO2传输（Transport）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a90ea57f7cc443a41bbd9d879bc5f652a"></a>

```c
const char * name
```

相关声明：[name](#a90ea57f7cc443a41bbd9d879bc5f652a)。

传输名称（Transport name）。

<a id="r_acda0c8702b378196f0ef1c86d1c56b44"></a>

```c
const struct fido2_transport_api * api
```

相关声明：[fido2_transport_api](P011_fido2_transport_api_结构体.md)、[api](#acda0c8702b378196f0ef1c86d1c56b44)。

传输驱动（Transport Driver）的API回调。

## 10.2\_详细说明（Detailed Documentation）

<a id="acda0c8702b378196f0ef1c86d1c56b44"></a>

### `api`

```c
const struct fido2_transport_api* fido2_transport::api
```

传输驱动（Transport Driver）的API回调。

<a id="a90ea57f7cc443a41bbd9d879bc5f652a"></a>

### `name`

```c
const char* fido2_transport::name
```

传输名称（Transport name）。

本数据类型文档由以下文件生成：

- `zephyr/authentication/fido2/fido2_transport.h`

## 10.3\_原页交叉引用（Cross References）

- [zephyr/authentication/fido2/fido2_transport.h](https://docs.zephyrproject.org/latest/doxygen/html/fido2__transport_8h_source.html)
- [fido2_transport_api](P011_fido2_transport_api_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_fido2_storage_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P011_fido2_transport_api_结构体.md)
