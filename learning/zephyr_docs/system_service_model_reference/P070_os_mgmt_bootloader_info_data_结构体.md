---
id: learning.zephyr-docs.system-service-model-reference.page-70
title: os_mgmt_bootloader_info_data_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__bootloader__info__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_os\_mgmt\_bootloader\_info\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structos__mgmt__bootloader__info__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO通知回调中提供的结构。该回调用于向引导加载程序信息（Bootloader Info）响应添加新字段。

```c
#include <zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h>
```

<a id="details"></a>

MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO通知回调中提供的结构。该回调用于向引导加载程序信息（Bootloader Info）响应添加新字段。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 70.1\_数据成员（Data Fields）

<a id="r_a0509ede3b6d0b40c0b93700a738f54cf"></a>

```c
zcbor_state_t * zse
```

相关声明：[zse](#a0509ede3b6d0b40c0b93700a738f54cf)。

当前用于输出组信息的 zcbor 编码器，可用它向组信息中添加额外字段。

<a id="r_a19db05235f5b818dfc7e479265beee71"></a>

```c
const size_t * decoded
```

相关声明：[decoded](#a19db05235f5b818dfc7e479265beee71)。

包含已解码参数的数量。

<a id="r_add73c66753d7b66713e9fdac8a1f951f"></a>

```c
struct zcbor_string * query
```

相关声明：[query](#add73c66753d7b66713e9fdac8a1f951f)。

包含 `query` 参数的值。

<a id="r_a2629ccb5b8ecc9da25bed2d0ec695938"></a>

```c
bool * has_output
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[has_output](#a2629ccb5b8ecc9da25bed2d0ec695938)。

必须设为 `true`，以表示已添加响应；否则将返回 `OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER` 错误。

## 70.2\_详细说明（Detailed Documentation）

<a id="a19db05235f5b818dfc7e479265beee71"></a>

### `decoded`

```c
const size_t* os_mgmt_bootloader_info_data::decoded
```

包含已解码参数的数量。

<a id="a2629ccb5b8ecc9da25bed2d0ec695938"></a>

### `has_output`

```c
bool* os_mgmt_bootloader_info_data::has_output
```

必须设为 `true`，以表示已添加响应；否则将返回 `OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER` 错误。

<a id="add73c66753d7b66713e9fdac8a1f951f"></a>

### `query`

```c
struct zcbor_string* os_mgmt_bootloader_info_data::query
```

包含 `query` 参数的值。

<a id="a0509ede3b6d0b40c0b93700a738f54cf"></a>

### `zse`

```c
zcbor_state_t* os_mgmt_bootloader_info_data::zse
```

当前用于输出组信息的 zcbor 编码器，可用它向组信息中添加额外字段。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h`

## 70.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_OS_MGMT_BOOTLOADER_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__os__mgmt.html#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)
- [zephyr/mgmt/mcumgr/grp/os_mgmt/os_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/os__mgmt__callbacks_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [OS_MGMT_ERR_QUERY_YIELDS_NO_ANSWER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__os__mgmt.html#gga14dc9256e6585450ea34b13666aa8765ad28fc3f5aa39ae710d83c9140423cb1d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P069_mgmt_handler_结构体.md) · [返回大纲](大纲.md) · [下一章](P071_os_mgmt_client_结构体.md)
