---
id: learning.zephyr-docs.api-source-reference.page-274
title: fs_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第274章\_fs\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h.html)。

## 274.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00041"></a>
<a id="foldopen00045"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="agroup__mcumgr__fs__mgmt_html_ga8454e0b2de7a06135134a9a1dc9c3336"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a0138ebd1cb377c32088188caf80d7591"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a01764b9c014357d3e1c8ce074312865a"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a298fc82862c6c07728e6d594b272ebb5"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a4e8547dded66c98175ea78a6764f39ac"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a5369eec52b43efa1e61dd1736220846d"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a593543b563e183d59c34ecdb87d41a9e"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a7c2977f1881591124c7b5d8bc6ddcee2"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a87eee59eb4d4e90cf754a897692e2884"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336a8b00c613d036d6ef98469bc232026a85"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336aa958c3816d6e8b4f06a618b6c3f4c045"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336ab4d5d316372c472ef667afb7f3098d9f"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336ac8f2bad37db1b0f7a1b841c568b47a63"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336ad13220927b7f52606ab6f979d1c4d271"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336addc67708d67eec1df7a6d3ca7affd7cd"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336adf29c34867ac1e2dfe3905330c65ae06"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336ae190565f5456e5f93a67fa60bde3193a"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336ae5c107813bebc859f3f709c4303c9d7f"></a>
<a id="agroup__mcumgr__fs__mgmt_html_gga8454e0b2de7a06135134a9a1dc9c3336aea30e5a6daa452c3815613e9f0ec00d6"></a>

```c
/*
 * Copyright (c) 2018-2022 mcumgr authors
 * Copyright (c) 2022 Laird Connectivity
 * Copyright (c) 2022-2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_H_


#ifdef __cplusplus
extern "C" {
#endif

#define FS_MGMT_ID_FILE                    0
#define FS_MGMT_ID_STAT                    1
#define FS_MGMT_ID_HASH_CHECKSUM           2
#define FS_MGMT_ID_SUPPORTED_HASH_CHECKSUM 3
#define FS_MGMT_ID_OPENED_FILE             4

enum fs_mgmt_err_code_t {
        FS_MGMT_ERR_OK = 0,

        FS_MGMT_ERR_UNKNOWN,

        FS_MGMT_ERR_FILE_INVALID_NAME,

        FS_MGMT_ERR_FILE_NOT_FOUND,

        FS_MGMT_ERR_FILE_IS_DIRECTORY,

        FS_MGMT_ERR_FILE_OPEN_FAILED,

        FS_MGMT_ERR_FILE_SEEK_FAILED,

        FS_MGMT_ERR_FILE_READ_FAILED,

        FS_MGMT_ERR_FILE_TRUNCATE_FAILED,

        FS_MGMT_ERR_FILE_DELETE_FAILED,

        FS_MGMT_ERR_FILE_WRITE_FAILED,

        FS_MGMT_ERR_FILE_OFFSET_NOT_VALID,

        FS_MGMT_ERR_FILE_OFFSET_LARGER_THAN_FILE,

        FS_MGMT_ERR_CHECKSUM_HASH_NOT_FOUND,

        FS_MGMT_ERR_MOUNT_POINT_NOT_FOUND,

        FS_MGMT_ERR_READ_ONLY_FILESYSTEM,

        FS_MGMT_ERR_FILE_EMPTY,

        FS_MGMT_ERR_FILE_CLOSE_FAILED,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_H_ */
```

## 274.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2022 mcumgr authors。

版权（Copyright）：© 2022 Laird Connectivity。

版权（Copyright）：© 2022-2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 115 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_GRP_FS_MGMT_FS_MGMT_H_`。

## 274.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt_8h.html)
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

---

[上一章](P273_fs_loader.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P275_fs_mgmt_callbacks.h_源码浏览.md)
