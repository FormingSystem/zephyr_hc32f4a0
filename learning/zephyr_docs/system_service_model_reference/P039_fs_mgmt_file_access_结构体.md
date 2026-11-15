---
id: learning.zephyr-docs.system-service-model-reference.page-39
title: fs_mgmt_file_access_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfs__mgmt__file__access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_fs\_mgmt\_file\_access\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfs__mgmt__file__access.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MGMT_EVT_OP_FS_MGMT_FILE_ACCESS通知回调中提供的结构。该回调用于将待处理的文件读写请求通知应用，并授权或拒绝该请求。

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h>
```

<a id="details"></a>

在 `MGMT_EVT_OP_FS_MGMT_FILE_ACCESS` 通知回调中提供的结构体。此回调用于向应用通知待处理的文件读写请求，并允许应用授权或拒绝请求。只有所有通知处理函数都返回 `MGMT_ERR_EOK` 时，才允许访问；只要有一个返回错误，就拒绝访问。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 39.1\_数据成员（Data Fields）

<a id="r_a3aeeaf6d4243c1aaa7d6129a2ef4a064"></a>

```c
enum fs_mgmt_file_access_types access
```

相关声明：[fs_mgmt_file_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga80e18873c1f4d97ea601a33042bc21f9)、[access](#a3aeeaf6d4243c1aaa7d6129a2ef4a064)。

指定所请求操作的类型。

<a id="r_a0155b69d23f3c5044e317eb236ff173c"></a>

```c
char * filename
```

相关声明：[filename](#a0155b69d23f3c5044e317eb236ff173c)。

待访问文件的路径和文件名。必要时，处理函数可以修改它以重定向文件访问，但不能超过路径字符串的最大长度。

## 39.2\_详细说明（Detailed Documentation）

<a id="a3aeeaf6d4243c1aaa7d6129a2ef4a064"></a>

### `access`

```c
enum fs_mgmt_file_access_types fs_mgmt_file_access::access
```

指定所请求操作的类型。

<a id="a0155b69d23f3c5044e317eb236ff173c"></a>

### `filename`

```c
char* fs_mgmt_file_access::filename
```

待访问文件的路径和文件名。必要时，处理函数可以修改它以重定向文件访问，但不能超过路径字符串的最大长度。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h`

## 39.3\_原页交叉引用（Cross References）

- [MGMT_EVT_OP_FS_MGMT_FILE_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)
- [zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h_source.html)
- [fs_mgmt_file_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga80e18873c1f4d97ea601a33042bc21f9)
- [MGMT_ERR_EOK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P038_fota_http_progress_结构体.md) · [返回大纲](大纲.md) · [下一章](P040_fs_mgmt_hash_checksum_group_结构体.md)
