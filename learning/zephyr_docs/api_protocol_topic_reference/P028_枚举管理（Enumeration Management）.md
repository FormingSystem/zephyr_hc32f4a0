---
id: learning.zephyr-docs.api-protocol-topic-reference.page-28
title: 枚举管理（Enumeration Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_枚举管理（Enumeration Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__enum__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 枚举管理 API

<a id="details"></a>

MCUmgr 枚举管理 API

<a id="header-groups"></a>
<a id="groups"></a>

## 28.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Fenum_5Fmgmt"></a>

相关声明：[枚举管理回调（Enumeration Management Callbacks）](../api_extension_topic_reference/P014_枚举管理回调（Enumeration Management Callbacks）.md)。

MCUmgr 枚举管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 28.2\_文件（Files）

<a id="r_enum_5Fmgmt_2Eh"></a>

```c
file enum_mgmt.h
```

相关声明：[enum_mgmt.h](../api_file_interface_reference/P017_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt.h_文件参考.md)。

MCUmgr枚举管理组（Enumeration Management Group）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 28.3\_枚举（Enumerations）

<a id="r_gaceaae2d8284b4a64b1303513e6aa3099"></a>

```c
enum enum_mgmt_err_code_t { ENUM_MGMT_ERR_OK = 0 , ENUM_MGMT_ERR_UNKNOWN , ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES , ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES , ENUM_MGMT_ERR_INDEX_TOO_LARGE }
```

相关声明：[enum_mgmt_err_code_t](#gaceaae2d8284b4a64b1303513e6aa3099)、[ENUM_MGMT_ERR_OK](#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0)、[ENUM_MGMT_ERR_UNKNOWN](#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f)、[ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES](#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e)、[ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES](#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153)、[ENUM_MGMT_ERR_INDEX_TOO_LARGE](#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72)。

枚举管理组（enumeration management group）的命令结果码。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 28.4\_枚举管理组命令标识符（Command IDs for enumeration management group）

<a id="r_gab16f2823b9bb4140a2fc336af5d16d2b"></a>

```c
#define ENUM_MGMT_ID_COUNT 0
```

相关声明：[ENUM_MGMT_ID_COUNT](#gab16f2823b9bb4140a2fc336af5d16d2b)。

所支持组（groups）的数量。

<a id="r_ga9b6c5a3021a30f8f6a83694ff9a07bf4"></a>

```c
#define ENUM_MGMT_ID_LIST 1
```

相关声明：[ENUM_MGMT_ID_LIST](#ga9b6c5a3021a30f8f6a83694ff9a07bf4)。

列出所支持的组。

<a id="r_ga5b08e51b1e32c27da5597fab4f68f94e"></a>

```c
#define ENUM_MGMT_ID_SINGLE 2
```

相关声明：[ENUM_MGMT_ID_SINGLE](#ga5b08e51b1e32c27da5597fab4f68f94e)。

获取单个组标识符（group ID）。

<a id="r_ga03edf25ed33ccdf00b0a21ee574e1b4d"></a>

```c
#define ENUM_MGMT_ID_DETAILS 3
```

相关声明：[ENUM_MGMT_ID_DETAILS](#ga03edf25ed33ccdf00b0a21ee574e1b4d)。

所支持组的详细信息。

## 28.5\_详细说明（Detailed Documentation）

<a id="gab16f2823b9bb4140a2fc336af5d16d2b"></a>

### `ENUM_MGMT_ID_COUNT`

```c
#define ENUM_MGMT_ID_COUNT 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt.h>
```

所支持组（groups）的数量。

<a id="ga03edf25ed33ccdf00b0a21ee574e1b4d"></a>

### `ENUM_MGMT_ID_DETAILS`

```c
#define ENUM_MGMT_ID_DETAILS 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt.h>
```

所支持组的详细信息。

<a id="ga9b6c5a3021a30f8f6a83694ff9a07bf4"></a>

### `ENUM_MGMT_ID_LIST`

```c
#define ENUM_MGMT_ID_LIST 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt.h>
```

列出所支持的组。

<a id="ga5b08e51b1e32c27da5597fab4f68f94e"></a>

### `ENUM_MGMT_ID_SINGLE`

```c
#define ENUM_MGMT_ID_SINGLE 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt.h>
```

获取单个组标识符（group ID）。

<a id="gaceaae2d8284b4a64b1303513e6aa3099"></a>

### `enum_mgmt_err_code_t`

```c
enum enum_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/enum_mgmt/enum_mgmt.h>
```

枚举管理组（enumeration management group）的命令结果码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ENUM_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `ENUM_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `ENUM_MGMT_ERR_TOO_MANY_GROUP_ENTRIES` | 提供的条目（entries）过多。 |
| `ENUM_MGMT_ERR_INSUFFICIENT_HEAP_FOR_ENTRIES` | 堆内存（heap memory）不足，无法存储条目数据。 |
| `ENUM_MGMT_ERR_INDEX_TOO_LARGE` | 提供的索引大于所支持组的数量。 |


## 28.6\_原页交叉引用（Cross References）

- [枚举管理回调（Enumeration Management Callbacks）](../api_extension_topic_reference/P014_枚举管理回调（Enumeration Management Callbacks）.md)
- [enum_mgmt.h](../api_file_interface_reference/P017_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0"></a>
<a id="ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f"></a>
<a id="ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e"></a>
<a id="ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153"></a>
<a id="ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72"></a>

---

[上一章](P027_向量按位异或（Vector bitwise XOR）.md) · [返回大纲](大纲.md) · [下一章](P029_MFD BD8LB600FS 接口.md)
