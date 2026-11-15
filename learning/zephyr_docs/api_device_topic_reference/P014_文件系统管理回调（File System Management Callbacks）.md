---
id: learning.zephyr-docs.api-device-topic-reference.page-14
title: 文件系统管理回调（File System Management Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_文件系统管理回调（File System Management Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 文件系统管理回调 API

<a id="details"></a>

MCUmgr 文件系统管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_fs_5Fmgmt_5Fcallbacks_2Eh"></a>

```c
file fs_mgmt_callbacks.h
```

相关声明：[fs_mgmt_callbacks.h](../api_file_configuration_reference/P030_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_callbacks.h_文件参考.md)。

MCUmgr文件系统管理回调（File System Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 14.2\_数据结构（Data Structures）

<a id="r_fs_5Fmgmt_5Ffile_5Faccess"></a>

```c
struct fs_mgmt_file_access
```

相关声明：[fs_mgmt_file_access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md)。

MGMT_EVT_OP_FS_MGMT_FILE_ACCESS通知回调中提供的结构。该回调用于将待处理的文件读写请求通知应用，并授权或拒绝该请求。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 14.3\_枚举（Enumerations）

<a id="r_ga324223c20cbefe3400272e2789082c79"></a>

```c
enum fs_mgmt_group_events { MGMT_EVT_OP_FS_MGMT_FILE_ACCESS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 0) , MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 1) , MGMT_EVT_OP_FS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_FS) }
```

相关声明：[fs_mgmt_group_events](#ga324223c20cbefe3400272e2789082c79)、[MGMT_EVT_OP_FS_MGMT_FILE_ACCESS](#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)、[MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE](#gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee)、[MGMT_EVT_OP_FS_MGMT_ALL](#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53)。

文件系统管理组（Filesystem Management Group）的管理事件操作码（MGMT Event Opcodes）。

<a id="r_ga80e18873c1f4d97ea601a33042bc21f9"></a>

```c
enum fs_mgmt_file_access_types { FS_MGMT_FILE_ACCESS_READ , FS_MGMT_FILE_ACCESS_WRITE , FS_MGMT_FILE_ACCESS_STATUS , FS_MGMT_FILE_ACCESS_HASH_CHECKSUM }
```

相关声明：[fs_mgmt_file_access_types](#ga80e18873c1f4d97ea601a33042bc21f9)、[FS_MGMT_FILE_ACCESS_READ](#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a)、[FS_MGMT_FILE_ACCESS_WRITE](#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2)、[FS_MGMT_FILE_ACCESS_STATUS](#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2)、[FS_MGMT_FILE_ACCESS_HASH_CHECKSUM](#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c)。

给定文件访问回调（File Access Callback）所请求的操作类型（Operation Type）。

## 14.4\_详细说明（Detailed Documentation）

<a id="ga80e18873c1f4d97ea601a33042bc21f9"></a>

### `fs_mgmt_file_access_types`

```c
enum fs_mgmt_file_access_types
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h>
```

给定文件访问回调（File Access Callback）所请求的操作类型（Operation Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FS_MGMT_FILE_ACCESS_READ` | 读取文件的访问权限，即文件下载（file download）。 |
| `FS_MGMT_FILE_ACCESS_WRITE` | 写入文件的访问权限，即文件上传（file upload）。 |
| `FS_MGMT_FILE_ACCESS_STATUS` | 获取文件状态的访问权限。 |
| `FS_MGMT_FILE_ACCESS_HASH_CHECKSUM` | 计算文件哈希或校验和（hash/checksum）的访问权限。 |

<a id="ga324223c20cbefe3400272e2789082c79"></a>

### `fs_mgmt_group_events`

```c
enum fs_mgmt_group_events
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt_callbacks.h>
```

文件系统管理组（Filesystem Management Group）的管理事件操作码（MGMT Event Opcodes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_EVT_OP_FS_MGMT_FILE_ACCESS` | 访问文件时触发的回调，数据为 `fs_mgmt_file_access`。 |
| `MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE` | 文件上传／下载完成时触发的回调，数据为 `fs_mgmt_file_access`。 |
| `MGMT_EVT_OP_FS_MGMT_ALL` | 用于启用全部 `fs_mgmt_group` 事件。 |


## 14.5\_原页交叉引用（Cross References）

- [fs_mgmt_callbacks.h](../api_file_configuration_reference/P030_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_callbacks.h_文件参考.md)
- [fs_mgmt_file_access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a"></a>
<a id="gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2"></a>
<a id="gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2"></a>
<a id="gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c"></a>
<a id="gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3"></a>
<a id="gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee"></a>
<a id="gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53"></a>

---

[上一章](P013_内核 API（Kernel APIs）.md) · [返回大纲](大纲.md) · [下一章](P015_操作系统管理回调（OS Management Callbacks）.md)
