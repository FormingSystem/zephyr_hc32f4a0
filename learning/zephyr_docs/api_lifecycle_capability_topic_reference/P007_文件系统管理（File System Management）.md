---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-7
title: 文件系统管理（File System Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_文件系统管理（File System Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 文件系统管理 API

<a id="details"></a>

MCUmgr 文件系统管理 API

<a id="header-groups"></a>
<a id="groups"></a>

## 7.1\_主题（Topics）

<a id="r_mcumgr_5Fcallback_5Fapi_5Ffs_5Fmgmt"></a>

相关声明：[文件系统管理回调（File System Management Callbacks）](../api_device_topic_reference/P014_文件系统管理回调（File System Management Callbacks）.md)。

MCUmgr 文件系统管理回调 API

<a id="header-files"></a>
<a id="files"></a>

## 7.2\_文件（Files）

<a id="r_fs_5Fmgmt_2Eh"></a>

```c
file fs_mgmt.h
```

相关声明：[fs_mgmt.h](../api_file_management_reference/P015_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt.h_文件参考.md)。

MCUmgr文件系统管理组（File System Management Group）API的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.3\_枚举（Enumerations）

<a id="r_ga8454e0b2de7a06135134a9a1dc9c3336"></a>

```c
enum fs_mgmt_err_code_t { FS_MGMT_ERR_OK = 0 , FS_MGMT_ERR_UNKNOWN , FS_MGMT_ERR_FILE_INVALID_NAME , FS_MGMT_ERR_FILE_NOT_FOUND , FS_MGMT_ERR_FILE_IS_DIRECTORY , FS_MGMT_ERR_FILE_OPEN_FAILED , FS_MGMT_ERR_FILE_SEEK_FAILED , FS_MGMT_ERR_FILE_READ_FAILED , FS_MGMT_ERR_FILE_TRUNCATE_FAILED , FS_MGMT_ERR_FILE_DELETE_FAILED , FS_MGMT_ERR_FILE_WRITE_FAILED , FS_MGMT_ERR_FILE_OFFSET_NOT_VALID , FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE , FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND , FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND , FS_MGMT_ERR_READ_ONLY_FILESYSTEM , FS_MGMT_ERR_FILE_EMPTY , FS_MGMT_ERR_FILE_CLOSE_FAILED }
```

相关声明：[fs_mgmt_err_code_t](#ga8454e0b2de7a06135134a9a1dc9c3336)、[FS_MGMT_ERR_OK](#gga8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2)、[FS_MGMT_ERR_UNKNOWN](#gga8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6)、[FS_MGMT_ERR_FILE_INVALID_NAME](#gga8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d)、[FS_MGMT_ERR_FILE_NOT_FOUND](#gga8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e)、[FS_MGMT_ERR_FILE_IS_DIRECTORY](#gga8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac)、[FS_MGMT_ERR_FILE_OPEN_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591)、[FS_MGMT_ERR_FILE_SEEK_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045)、[FS_MGMT_ERR_FILE_READ_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06)、[FS_MGMT_ERR_FILE_TRUNCATE_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f)、[FS_MGMT_ERR_FILE_DELETE_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85)、[FS_MGMT_ERR_FILE_WRITE_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a)、[FS_MGMT_ERR_FILE_OFFSET_NOT_VALID](#gga8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a)、[FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE](#gga8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63)、[FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND](#gga8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884)、[FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND](#gga8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd)、[FS_MGMT_ERR_READ_ONLY_FILESYSTEM](#gga8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271)、[FS_MGMT_ERR_FILE_EMPTY](#gga8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5)、[FS_MGMT_ERR_FILE_CLOSE_FAILED](#gga8454e0b2de7a06135134a9a1dc9c3336ab4d5d316372c472ef667afb7f3098d9f)。

文件系统管理组（file system management group）的命令结果码。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.4\_文件系统管理组命令标识符（Command IDs for File System Management group）

<a id="r_ga17b142e59be58d1c83c9ce87f7d84b97"></a>

```c
#define FS_MGMT_ID_FILE 0
```

相关声明：[FS_MGMT_ID_FILE](#ga17b142e59be58d1c83c9ce87f7d84b97)。

文件下载／上传（download/upload）。

<a id="r_ga89833eac462adda453375482691c9dfa"></a>

```c
#define FS_MGMT_ID_STAT 1
```

相关声明：[FS_MGMT_ID_STAT](#ga89833eac462adda453375482691c9dfa)。

文件状态（file status）。

<a id="r_gaf8263e56dd044b2ed5f10ce57e6fe2a5"></a>

```c
#define FS_MGMT_ID_HASH_CHECKSUM 2
```

相关声明：[FS_MGMT_ID_HASH_CHECKSUM](#gaf8263e56dd044b2ed5f10ce57e6fe2a5)。

文件哈希／校验和（hash/checksum）。

<a id="r_ga82aefe54b14e74127593f3b3c2e06955"></a>

```c
#define FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM 3
```

相关声明：[FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM](#ga82aefe54b14e74127593f3b3c2e06955)。

支持的文件哈希／校验和类型。

<a id="r_gaa5e765a2c844efb494648c8856b91d72"></a>

```c
#define FS_MGMT_ID_OPENED_FILE 4
```

相关声明：[FS_MGMT_ID_OPENED_FILE](#gaa5e765a2c844efb494648c8856b91d72)。

关闭文件（file close）。

## 7.5\_详细说明（Detailed Documentation）

<a id="ga17b142e59be58d1c83c9ce87f7d84b97"></a>

### `FS_MGMT_ID_FILE`

```c
#define FS_MGMT_ID_FILE 0
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

文件下载／上传（download/upload）。

<a id="gaf8263e56dd044b2ed5f10ce57e6fe2a5"></a>

### `FS_MGMT_ID_HASH_CHECKSUM`

```c
#define FS_MGMT_ID_HASH_CHECKSUM 2
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

文件哈希／校验和（hash/checksum）。

<a id="gaa5e765a2c844efb494648c8856b91d72"></a>

### `FS_MGMT_ID_OPENED_FILE`

```c
#define FS_MGMT_ID_OPENED_FILE 4
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

关闭文件（file close）。

<a id="ga89833eac462adda453375482691c9dfa"></a>

### `FS_MGMT_ID_STAT`

```c
#define FS_MGMT_ID_STAT 1
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

文件状态（file status）。

<a id="ga82aefe54b14e74127593f3b3c2e06955"></a>

### `FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM`

```c
#define FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM 3
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

支持的文件哈希／校验和类型。

<a id="ga8454e0b2de7a06135134a9a1dc9c3336"></a>

### `fs_mgmt_err_code_t`

```c
enum fs_mgmt_err_code_t
```

```c
#include <zephyr/mgmt/mcumgr/grp/fs_mgmt/fs_mgmt.h>
```

文件系统管理组（file system management group）的命令结果码。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FS_MGMT_ERR_OK` | 没有错误；如果响应中没有ret值，就隐含表示此结果。 |
| `FS_MGMT_ERR_UNKNOWN` | 发生未知错误（Unknown Error）。 |
| `FS_MGMT_ERR_FILE_INVALID_NAME` | 指定的文件名（File Name）无效。 |
| `FS_MGMT_ERR_FILE_NOT_FOUND` | 指定的文件（File）不存在。 |
| `FS_MGMT_ERR_FILE_IS_DIRECTORY` | 指定路径是目录（Directory），不是文件（File）。 |
| `FS_MGMT_ERR_FILE_OPEN_FAILED` | 尝试打开文件（Open a File）时出错。 |
| `FS_MGMT_ERR_FILE_SEEK_FAILED` | 尝试定位到文件内偏移量（Seek to an Offset）时出错。 |
| `FS_MGMT_ERR_FILE_READ_FAILED` | 尝试从文件读取数据（Read Data）时出错。 |
| `FS_MGMT_ERR_FILE_TRUNCATE_FAILED` | 尝试截断文件（Truncate File）时出错。 |
| `FS_MGMT_ERR_FILE_DELETE_FAILED` | 尝试删除文件（Delete File）时出错。 |
| `FS_MGMT_ERR_FILE_WRITE_FAILED` | 尝试向文件写入数据（Write Data）时出错。 |
| `FS_MGMT_ERR_FILE_OFFSET_NOT_VALID` | 指定的数据偏移量（Data Offset）无效；这可能表示设备上的文件在上次命令之后发生了变化。设备上当前文件的长度以 `len` 返回，用户应用需要决定如何处理。例如，可以请求该文件的散列值（Hash），并与正在上传的文件中相同长度部分的散列值比较，判断是否匹配。 |
| `FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE` | 请求的偏移量（Offset）超过设备上文件的大小。 |
| `FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND` | 未找到请求的校验和或散列类型（Checksum or Hash Type），或当前构建不支持它。 |
| `FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND` | 未找到指定挂载点（Mount Point），或该挂载点尚未挂载。 |
| `FS_MGMT_ERR_READ_ONLY_FILESYSTEM` | 指定挂载点（Mount Point）属于只读文件系统（Read-only Filesystem）。 |
| `FS_MGMT_ERR_FILE_EMPTY` | 文件为空，没有内容，因此无法执行操作。 |
| `FS_MGMT_ERR_FILE_CLOSE_FAILED` | 尝试关闭文件（Close a File）时出错。 |


## 7.6\_原页交叉引用（Cross References）

- [文件系统管理回调（File System Management Callbacks）](../api_device_topic_reference/P014_文件系统管理回调（File System Management Callbacks）.md)
- [fs_mgmt.h](../api_file_management_reference/P015_zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5"></a>
<a id="gga8454e0b2de7a06135134a9a1dc9c3336ab4d5d316372c472ef667afb7f3098d9f"></a>

---

[上一章](P006_LIS2DH API主题.md) · [返回大纲](大纲.md) · [下一章](P008_操作系统管理（OS Management）.md)
