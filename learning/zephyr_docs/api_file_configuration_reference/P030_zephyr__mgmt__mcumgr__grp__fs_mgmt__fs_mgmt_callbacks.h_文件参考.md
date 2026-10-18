---
id: learning.zephyr-docs.api-file-configuration-reference.page-30
title: zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_callbacks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_fs\_mgmt\_\_fs\_mgmt\_callbacks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__callbacks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr文件系统管理回调（File System Management Callback）定义的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr文件系统管理回调（File System Management Callback）定义的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 30.1\_数据结构（Data Structures）

<a id="r_fs_5Fmgmt_5Ffile_5Faccess"></a>

```c
struct fs_mgmt_file_access
```

相关声明：[fs_mgmt_file_access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md)。

MGMT_EVT_OP_FS_MGMT_FILE_ACCESS通知回调中提供的结构。该回调用于将待处理的文件读写请求通知应用，并授权或拒绝该请求。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 30.2\_枚举（Enumerations）

<a id="r_ga324223c20cbefe3400272e2789082c79"></a>

```c
enum fs_mgmt_group_events { MGMT_EVT_OP_FS_MGMT_FILE_ACCESS = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 0) , MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_FS, 1) , MGMT_EVT_OP_FS_MGMT_ALL = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_FS) }
```

相关声明：[fs_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga324223c20cbefe3400272e2789082c79)、[MGMT_EVT_OP_FS_MGMT_FILE_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)、[MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee)、[MGMT_EVT_OP_FS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53)。

文件系统管理组（Filesystem Management Group）的管理事件操作码（MGMT Event Opcodes）。

<a id="r_ga80e18873c1f4d97ea601a33042bc21f9"></a>

```c
enum fs_mgmt_file_access_types { FS_MGMT_FILE_ACCESS_READ , FS_MGMT_FILE_ACCESS_WRITE , FS_MGMT_FILE_ACCESS_STATUS , FS_MGMT_FILE_ACCESS_HASH_CHECKSUM }
```

相关声明：[fs_mgmt_file_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga80e18873c1f4d97ea601a33042bc21f9)、[FS_MGMT_FILE_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a)、[FS_MGMT_FILE_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2)、[FS_MGMT_FILE_ACCESS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2)、[FS_MGMT_FILE_ACCESS_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c)。

给定文件访问回调（File Access Callback）所请求的操作类型（Operation Type）。


## 30.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P275_fs_mgmt_callbacks.h_源码浏览.md)
- [fs_mgmt_file_access](../system_service_model_reference/P039_fs_mgmt_file_access_结构体.md)
- [MGMT_EVT_OP_FS_MGMT_FILE_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)
- [fs_mgmt_group_events](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga324223c20cbefe3400272e2789082c79)
- [MGMT_EVT_OP_FS_MGMT_FILE_ACCESS_DONE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9accc416aa349fd533e51d27fc46b7ee)
- [MGMT_EVT_OP_FS_MGMT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53)
- [fs_mgmt_file_access_types](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#ga80e18873c1f4d97ea601a33042bc21f9)
- [FS_MGMT_FILE_ACCESS_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a5e418a17abdee97e017b0a18ca8dd19a)
- [FS_MGMT_FILE_ACCESS_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a186ef60e6f795584edf7101b74499cb2)
- [FS_MGMT_FILE_ACCESS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9ae500b34f64a8cefed3e9b420127564d2)
- [FS_MGMT_FILE_ACCESS_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__callback__api__fs__mgmt.html#gga80e18873c1f4d97ea601a33042bc21f9a93323901acc3c74dd6ed4752847e195c)

<a id="header-details"></a>

---

[上一章](P029_zephyr__net__prometheus__formatter.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__net__prometheus__gauge.h_文件参考.md)
