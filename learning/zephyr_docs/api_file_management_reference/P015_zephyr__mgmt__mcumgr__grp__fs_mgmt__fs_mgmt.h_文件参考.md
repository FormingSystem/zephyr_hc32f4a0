---
id: learning.zephyr-docs.api-file-management-reference.page-15
title: zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_fs\_mgmt\_\_fs\_mgmt.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr文件系统管理组（File System Management Group）API的头文件。

查看此文件的源码。

<a id="details"></a>

MCUmgr文件系统管理组（File System Management Group）API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 文件系统管理组命令标识符（Command IDs for File System Management group）

<a id="r_ga17b142e59be58d1c83c9ce87f7d84b97"></a>

```c
#define FS_MGMT_ID_FILE 0
```

相关声明：[FS_MGMT_ID_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga17b142e59be58d1c83c9ce87f7d84b97)。

文件下载／上传（download/upload）。

<a id="r_ga89833eac462adda453375482691c9dfa"></a>

```c
#define FS_MGMT_ID_STAT 1
```

相关声明：[FS_MGMT_ID_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga89833eac462adda453375482691c9dfa)。

文件状态（file status）。

<a id="r_gaf8263e56dd044b2ed5f10ce57e6fe2a5"></a>

```c
#define FS_MGMT_ID_HASH_CHECKSUM 2
```

相关声明：[FS_MGMT_ID_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gaf8263e56dd044b2ed5f10ce57e6fe2a5)。

文件哈希／校验和（hash/checksum）。

<a id="r_ga82aefe54b14e74127593f3b3c2e06955"></a>

```c
#define FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM 3
```

相关声明：[FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga82aefe54b14e74127593f3b3c2e06955)。

支持的文件哈希／校验和类型。

<a id="r_gaa5e765a2c844efb494648c8856b91d72"></a>

```c
#define FS_MGMT_ID_OPENED_FILE 4
```

相关声明：[FS_MGMT_ID_OPENED_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gaa5e765a2c844efb494648c8856b91d72)。

关闭文件（file close）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.2\_枚举（Enumerations）

<a id="r_ga8454e0b2de7a06135134a9a1dc9c3336"></a>

```c
enum fs_mgmt_err_code_t { FS_MGMT_ERR_OK = 0 , FS_MGMT_ERR_UNKNOWN , FS_MGMT_ERR_FILE_INVALID_NAME , FS_MGMT_ERR_FILE_NOT_FOUND , FS_MGMT_ERR_FILE_IS_DIRECTORY , FS_MGMT_ERR_FILE_OPEN_FAILED , FS_MGMT_ERR_FILE_SEEK_FAILED , FS_MGMT_ERR_FILE_READ_FAILED , FS_MGMT_ERR_FILE_TRUNCATE_FAILED , FS_MGMT_ERR_FILE_DELETE_FAILED , FS_MGMT_ERR_FILE_WRITE_FAILED , FS_MGMT_ERR_FILE_OFFSET_NOT_VALID , FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE , FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND , FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND , FS_MGMT_ERR_READ_ONLY_FILESYSTEM , FS_MGMT_ERR_FILE_EMPTY , FS_MGMT_ERR_FILE_CLOSE_FAILED }
```

相关声明：[fs_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga8454e0b2de7a06135134a9a1dc9c3336)、[FS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2)、[FS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6)、[FS_MGMT_ERR_FILE_INVALID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d)、[FS_MGMT_ERR_FILE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e)、[FS_MGMT_ERR_FILE_IS_DIRECTORY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac)、[FS_MGMT_ERR_FILE_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591)、[FS_MGMT_ERR_FILE_SEEK_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045)、[FS_MGMT_ERR_FILE_READ_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06)、[FS_MGMT_ERR_FILE_TRUNCATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f)、[FS_MGMT_ERR_FILE_DELETE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85)、[FS_MGMT_ERR_FILE_WRITE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a)、[FS_MGMT_ERR_FILE_OFFSET_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a)、[FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63)、[FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884)、[FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd)、[FS_MGMT_ERR_READ_ONLY_FILESYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271)、[FS_MGMT_ERR_FILE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5)、[FS_MGMT_ERR_FILE_CLOSE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ab4d5d316372c472ef667afb7f3098d9f)。

文件系统管理组（file system management group）的命令结果码。


## 15.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P274_fs_mgmt.h_源码浏览.md)
- [FS_MGMT_ID_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga17b142e59be58d1c83c9ce87f7d84b97)
- [FS_MGMT_ID_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga89833eac462adda453375482691c9dfa)
- [FS_MGMT_ID_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gaf8263e56dd044b2ed5f10ce57e6fe2a5)
- [FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga82aefe54b14e74127593f3b3c2e06955)
- [FS_MGMT_ID_OPENED_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gaa5e765a2c844efb494648c8856b91d72)
- [fs_mgmt_err_code_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#ga8454e0b2de7a06135134a9a1dc9c3336)
- [FS_MGMT_ERR_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2)
- [FS_MGMT_ERR_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6)
- [FS_MGMT_ERR_FILE_INVALID_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d)
- [FS_MGMT_ERR_FILE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e)
- [FS_MGMT_ERR_FILE_IS_DIRECTORY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac)
- [FS_MGMT_ERR_FILE_OPEN_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591)
- [FS_MGMT_ERR_FILE_SEEK_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045)
- [FS_MGMT_ERR_FILE_READ_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06)
- [FS_MGMT_ERR_FILE_TRUNCATE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f)
- [FS_MGMT_ERR_FILE_DELETE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85)
- [FS_MGMT_ERR_FILE_WRITE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a)
- [FS_MGMT_ERR_FILE_OFFSET_NOT_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a)
- [FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63)
- [FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884)
- [FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd)
- [FS_MGMT_ERR_READ_ONLY_FILESYSTEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271)
- [FS_MGMT_ERR_FILE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5)
- [FS_MGMT_ERR_FILE_CLOSE_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__fs__mgmt.html#gga8454e0b2de7a06135134a9a1dc9c3336ab4d5d316372c472ef667afb7f3098d9f)

<a id="header-details"></a>

---

[上一章](P014_zephyr__dfu__flash_img.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__misc__ft8xx__ft8xx.h_文件参考.md)
