---
id: learning.zephyr-docs.system-service-model-reference.page-8
title: ec_host_cmd_backend_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ec\_host\_cmd\_backend\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入式控制器（EC）的主机命令后端（Host Command Backend）。

```c
#include <zephyr/mgmt/ec_host_cmd/backend.h>
```

<a id="details"></a>

嵌入式控制器（EC）的主机命令后端（Host Command Backend）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_aadf44f4eff331abeca40bc0f69bc173d"></a>

```c
const struct ec_host_cmd_backend_api * api
```

相关声明：[ec_host_cmd_backend_api](P009_ec_host_cmd_backend_api_结构体.md)、[api](#aadf44f4eff331abeca40bc0f69bc173d)。

后端提供的 API。

<a id="r_a57236d69bdc9a99b1cb3acbac0be275b"></a>

```c
void * ctx
```

相关声明：[ctx](#a57236d69bdc9a99b1cb3acbac0be275b)。

后端的上下文。

## 8.2\_详细说明（Detailed Documentation）

<a id="aadf44f4eff331abeca40bc0f69bc173d"></a>

### `api`

```c
const struct ec_host_cmd_backend_api* ec_host_cmd_backend::api
```

后端提供的 API。

<a id="a57236d69bdc9a99b1cb3acbac0be275b"></a>

### `ctx`

```c
void* ec_host_cmd_backend::ctx
```

后端的上下文。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/backend.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/backend.h](https://docs.zephyrproject.org/latest/doxygen/html/backend_8h_source.html)
- [ec_host_cmd_backend_api](P009_ec_host_cmd_backend_api_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_ec_host_cmd_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_ec_host_cmd_backend_api_结构体.md)
