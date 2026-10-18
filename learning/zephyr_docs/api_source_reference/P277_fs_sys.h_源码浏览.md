---
id: learning.zephyr-docs.api-source-reference.page-277
title: fs_sys.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__sys_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第277章\_fs\_sys.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fs__sys_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P079_文件系统后端头文件.md)。

## 277.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00051"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00070"></a>
<a id="l00077"></a>
<a id="l00085"></a>
<a id="l00092"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00113"></a>
<a id="l00121"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00141"></a>
<a id="l00148"></a>
<a id="l00156"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00174"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="afs__interface_8h_html_a7090a1b41e73d393b8be3e18ab411027"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructfs__dir__t_html"></a>
<a id="astructfs__dirent_html"></a>
<a id="astructfs__file__system__t_html"></a>
<a id="astructfs__file__system__t_html_a04659fbb0096ca2cc5e733d483494ae4"></a>
<a id="astructfs__file__system__t_html_a05b03f33ec51a2444a3a3f05ace8ba68"></a>
<a id="astructfs__file__system__t_html_a086f2d11ff432e3d24887b5b3da2afca"></a>
<a id="astructfs__file__system__t_html_a1039b25b44bc8be1daea19c0d489c0db"></a>
<a id="astructfs__file__system__t_html_a1fcddbdc18673a3c8e183fd070e3d3c3"></a>
<a id="astructfs__file__system__t_html_a3486815c6b1dcf0aef0be7a71a31ffea"></a>
<a id="astructfs__file__system__t_html_a3bac973eb97ecaa51a567b7d69a35142"></a>
<a id="astructfs__file__system__t_html_a3bcb76b13290f7fba54d6d7578e66f9c"></a>
<a id="astructfs__file__system__t_html_a3bcd27d47dca1e10284605434611a231"></a>
<a id="astructfs__file__system__t_html_a3c0e0a91fffdde30802fb5a1cdc22b60"></a>
<a id="astructfs__file__system__t_html_a40b11c282d3b8c30fe1e2d9cc98edd69"></a>
<a id="astructfs__file__system__t_html_a5865d7d64e0ad22a30f1822263f134da"></a>
<a id="astructfs__file__system__t_html_a604aa1045d24ad65e09e524a6adf8809"></a>
<a id="astructfs__file__system__t_html_a8efb04845dbec830f12435a6472b7015"></a>
<a id="astructfs__file__system__t_html_aa31880d03633ed35d060ce2e0ee75d15"></a>
<a id="astructfs__file__system__t_html_ace0bf6d96ddcb61e42bb54eb4388c3dc"></a>
<a id="astructfs__file__system__t_html_ad11c51566b0703f0fd426e37200d7a8e"></a>
<a id="astructfs__file__system__t_html_ad1a427421f3c122885bed8ef1faa56ea"></a>
<a id="astructfs__file__system__t_html_ae1c84b7c651a161e286cfb25aa1bc2fb"></a>
<a id="astructfs__file__system__t_html_affc26f28e560d5e5bdaa1868fe81332e"></a>
<a id="astructfs__file__t_html"></a>
<a id="astructfs__mount__t_html"></a>
<a id="astructfs__statvfs_html"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_FS_FS_SYS_H_
#define ZEPHYR_INCLUDE_FS_FS_SYS_H_

#ifdef __cplusplus
extern "C" {
#endif


struct fs_file_system_t {
        int (*open)(struct fs_file_t *filp, const char *fs_path,
                    fs_mode_t flags);
        ssize_t (*read)(struct fs_file_t *filp, void *dest, size_t nbytes);
        ssize_t (*write)(struct fs_file_t *filp,
                                        const void *src, size_t nbytes);
        int (*lseek)(struct fs_file_t *filp, off_t off, int whence);
        off_t (*tell)(struct fs_file_t *filp);
        int (*truncate)(struct fs_file_t *filp, off_t length);
        int (*sync)(struct fs_file_t *filp);
        int (*close)(struct fs_file_t *filp);

        int (*opendir)(struct fs_dir_t *dirp, const char *fs_path);
        int (*readdir)(struct fs_dir_t *dirp, struct fs_dirent *entry);
        int (*closedir)(struct fs_dir_t *dirp);

        int (*mount)(struct fs_mount_t *mountp);
        int (*unmount)(struct fs_mount_t *mountp);
        int (*unlink)(struct fs_mount_t *mountp, const char *name);
        int (*rename)(struct fs_mount_t *mountp, const char *from,
                                        const char *to);
        int (*mkdir)(struct fs_mount_t *mountp, const char *name);
        int (*stat)(struct fs_mount_t *mountp, const char *path,
                                        struct fs_dirent *entry);
        int (*statvfs)(struct fs_mount_t *mountp, const char *path,
                                        struct fs_statvfs *stat);
#if defined(CONFIG_FILE_SYSTEM_GC) || defined(__DOXYGEN__)
        int (*gc)(struct fs_mount_t *mountp);
#endif
#if defined(CONFIG_FILE_SYSTEM_MKFS) || defined(__DOXYGEN__)
        int (*mkfs)(uintptr_t dev_id, void *cfg, int flags);
#endif
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_FS_FS_SYS_H_ */
```

## 277.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 229 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_FS_FS_SYS_H_`。

## 277.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P079_文件系统后端头文件.md)
- [fs_file_system_t](../storage/P040_文件系统驱动操作结构.md)
- [open](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a40b11c282d3b8c30fe1e2d9cc98edd69)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [fs_mode_t](https://docs.zephyrproject.org/latest/doxygen/html/fs__interface_8h.html#a7090a1b41e73d393b8be3e18ab411027)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [read](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a8efb04845dbec830f12435a6472b7015)
- [write](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a1039b25b44bc8be1daea19c0d489c0db)
- [lseek](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a05b03f33ec51a2444a3a3f05ace8ba68)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [tell](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bcb76b13290f7fba54d6d7578e66f9c)
- [truncate](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a604aa1045d24ad65e09e524a6adf8809)
- [sync](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ad1a427421f3c122885bed8ef1faa56ea)
- [close](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ae1c84b7c651a161e286cfb25aa1bc2fb)
- [opendir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3c0e0a91fffdde30802fb5a1cdc22b60)
- [fs_dir_t](../storage/P039_文件系统目录对象.md)
- [readdir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ace0bf6d96ddcb61e42bb54eb4388c3dc)
- [fs_dirent](../storage/P036_文件系统目录项.md)
- [closedir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ad11c51566b0703f0fd426e37200d7a8e)
- [mount](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a086f2d11ff432e3d24887b5b3da2afca)
- [fs_mount_t](../storage/P035_文件系统挂载结构.md)
- [unmount](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a04659fbb0096ca2cc5e733d483494ae4)
- [unlink](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3486815c6b1dcf0aef0be7a71a31ffea)
- [rename](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#affc26f28e560d5e5bdaa1868fe81332e)
- [mkdir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#aa31880d03633ed35d060ce2e0ee75d15)
- [stat](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a5865d7d64e0ad22a30f1822263f134da)
- [statvfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bac973eb97ecaa51a567b7d69a35142)
- [fs_statvfs](../storage/P037_文件系统卷统计.md)
- [gc](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bcd27d47dca1e10284605434611a231)
- [mkfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a1fcddbdc18673a3c8e183fd070e3d3c3)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [fs_file_system_t::unmount](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a04659fbb0096ca2cc5e733d483494ae4)
- [fs_file_system_t::lseek](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a05b03f33ec51a2444a3a3f05ace8ba68)
- [fs_file_system_t::mount](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a086f2d11ff432e3d24887b5b3da2afca)
- [fs_file_system_t::write](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a1039b25b44bc8be1daea19c0d489c0db)
- [fs_file_system_t::mkfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a1fcddbdc18673a3c8e183fd070e3d3c3)
- [fs_file_system_t::unlink](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3486815c6b1dcf0aef0be7a71a31ffea)
- [fs_file_system_t::statvfs](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bac973eb97ecaa51a567b7d69a35142)
- [fs_file_system_t::tell](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bcb76b13290f7fba54d6d7578e66f9c)
- [fs_file_system_t::gc](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3bcd27d47dca1e10284605434611a231)
- [fs_file_system_t::opendir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a3c0e0a91fffdde30802fb5a1cdc22b60)
- [fs_file_system_t::open](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a40b11c282d3b8c30fe1e2d9cc98edd69)
- [fs_file_system_t::stat](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a5865d7d64e0ad22a30f1822263f134da)
- [fs_file_system_t::truncate](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a604aa1045d24ad65e09e524a6adf8809)
- [fs_file_system_t::read](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#a8efb04845dbec830f12435a6472b7015)
- [fs_file_system_t::mkdir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#aa31880d03633ed35d060ce2e0ee75d15)
- [fs_file_system_t::readdir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ace0bf6d96ddcb61e42bb54eb4388c3dc)
- [fs_file_system_t::closedir](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ad11c51566b0703f0fd426e37200d7a8e)
- [fs_file_system_t::sync](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ad1a427421f3c122885bed8ef1faa56ea)
- [fs_file_system_t::close](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#ae1c84b7c651a161e286cfb25aa1bc2fb)
- [fs_file_system_t::rename](https://docs.zephyrproject.org/latest/doxygen/html/structfs__file__system__t.html#affc26f28e560d5e5bdaa1868fe81332e)

---

[上一章](P276_fs_mgmt_hash_checksum.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P278_ft8xx_common.h_源码浏览.md)
