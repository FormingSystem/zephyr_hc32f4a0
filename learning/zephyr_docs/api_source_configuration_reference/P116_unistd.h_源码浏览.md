---
id: learning.zephyr-docs.api-source-configuration-reference.page-116
title: unistd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_unistd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html)。

## 116.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="aconfstr_8h_html"></a>
<a id="afs_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_adb8322e115035a284aab704909e63d00"></a>
<a id="aposix__features_8h_html"></a>
<a id="aposix__signal_8h_html_a114f9c2461df851d2ad00aad8dcfa3f7"></a>
<a id="aposix__types_8h_html"></a>
<a id="aposix__types_8h_html_a1cf3c794977f92f3ccf2e041a68f3342"></a>
<a id="astat_8h_html"></a>
<a id="astat_8h_html_a0f949e7f97dc8e3e4ea1142cda8be155"></a>
<a id="astat_8h_html_afa4a4f346213cdc5ae4cfc9aedf7ef2e"></a>
<a id="astructstat_html"></a>
<a id="asysconf_8h_html"></a>
<a id="aunistd_8h_html_a59715f1a0a2ee4dc75e8343aca15c1dd"></a>
<a id="aunistd_8h_html_a599f55d9eaa01b6921367233437b9b13"></a>
<a id="aunistd_8h_html_a5d88641f86c8a447fefd1e531758a3c0"></a>
<a id="aunistd_8h_html_aaa1de6debea33c41fbfaa909e813c2f4"></a>
<a id="aunistd_8h_html_ac61b207337ca21b3b309593fd1a0cb82"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_UNISTD_H_
#define ZEPHYR_INCLUDE_POSIX_UNISTD_H_

#include <time.h>

#include <zephyr/posix/posix_types.h>

#ifdef CONFIG_POSIX_API
#include <zephyr/fs/fs.h>
#endif
#include <zephyr/posix/sys/confstr.h>
#include <zephyr/posix/sys/stat.h>
#include <zephyr/posix/sys/sysconf.h>

#include "posix_features.h"

#ifdef __cplusplus
extern "C" {
#endif

#ifdef CONFIG_POSIX_API
/* File related operations */
int close(int file);
ssize_t write(int file, const void *buffer, size_t count);
ssize_t read(int file, void *buffer, size_t count);
off_t lseek(int file, off_t offset, int whence);
int fsync(int fd);
int ftruncate(int fd, off_t length);

#ifdef CONFIG_POSIX_SYNCHRONIZED_IO
int fdatasync(int fd);
#endif /* CONFIG_POSIX_SYNCHRONIZED_IO */

/* File System related operations */
int rename(const char *old, const char *newp);
int unlink(const char *path);
int stat(const char *path, struct stat *buf);
int mkdir(const char *path, mode_t mode);
int rmdir(const char *path);

FUNC_NORETURN void _exit(int status);

int gethostname(char *buf, size_t len);

#endif /* CONFIG_POSIX_API */

#ifdef CONFIG_POSIX_C_LIB_EXT
int getopt(int argc, char *const argv[], const char *optstring);
extern char *optarg;
extern int opterr, optind, optopt;
#endif

int getentropy(void *buffer, size_t length);
pid_t getpid(void);
unsigned sleep(unsigned int seconds);
int usleep(useconds_t useconds);
#if _POSIX_C_SOURCE >= 2
size_t confstr(int name, char *buf, size_t len);
#endif

#ifdef CONFIG_POSIX_SYSCONF_IMPL_MACRO
#define sysconf(x) (long)CONCAT(__z_posix_sysconf, x)
#else
long sysconf(int opt);
#endif /* CONFIG_POSIX_SYSCONF_IMPL_FULL */

#if _XOPEN_SOURCE >= 500
long gethostid(void);
#endif

#ifdef __cplusplus
}
#endif

#endif  /* ZEPHYR_INCLUDE_POSIX_UNISTD_H_ */
```

## 116.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 27 行

文件相关操作（File related operations）。

### 注释 3：原第 37 行

条件编译配置（Configuration）标记：`CONFIG_POSIX_SYNCHRONIZED_IO`。

### 注释 4：原第 39 行

文件系统相关操作（File System related operations）。

### 注释 5：原第 50 行

条件编译配置（Configuration）标记：`CONFIG_POSIX_API`。

### 注释 6：原第 70 行

条件编译配置（Configuration）标记：`CONFIG_POSIX_SYSCONF_IMPL_FULL`。

### 注释 7：原第 80 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_UNISTD_H_`。

## 116.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [zephyr/fs/fs.h](../storage/P077_文件系统公共头文件.md)
- [zephyr/posix/sys/confstr.h](https://docs.zephyrproject.org/latest/doxygen/html/confstr_8h.html)
- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [zephyr/posix/sys/sysconf.h](https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h.html)
- [posix_features.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__features_8h.html)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [stat](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html#a0f949e7f97dc8e3e4ea1142cda8be155)
- [stat](../posix_system_model_reference/P022_stat_结构体.md)
- [mkdir](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html#afa4a4f346213cdc5ae4cfc9aedf7ef2e)
- [mode_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#adb8322e115035a284aab704909e63d00)
- [getentropy](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#a5d88641f86c8a447fefd1e531758a3c0)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [getpid](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#ac61b207337ca21b3b309593fd1a0cb82)
- [sleep](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#aaa1de6debea33c41fbfaa909e813c2f4)
- [usleep](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#a59715f1a0a2ee4dc75e8343aca15c1dd)
- [useconds_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a1cf3c794977f92f3ccf2e041a68f3342)
- [sysconf](https://docs.zephyrproject.org/latest/doxygen/html/unistd_8h.html#a599f55d9eaa01b6921367233437b9b13)
- [confstr.h](https://docs.zephyrproject.org/latest/doxygen/html/confstr_8h.html)
- [fs.h](../storage/P077_文件系统公共头文件.md)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [sysconf.h](https://docs.zephyrproject.org/latest/doxygen/html/sysconf_8h.html)

---

[上一章](P115_uart_console.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P117_xg21-clock.h_源码浏览.md)
