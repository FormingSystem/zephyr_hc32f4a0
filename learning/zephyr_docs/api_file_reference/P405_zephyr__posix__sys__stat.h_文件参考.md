---
id: learning.zephyr-docs.api-file-reference.page-405
title: zephyr__posix__sys__stat.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第405章\_zephyr\_\_posix\_\_sys\_\_stat.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <time.h>
#include <sys/cdefs.h>
#include <zephyr/posix/posix_types.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 405.1\_数据结构（Data Structures）

<a id="r_stat"></a>

```c
struct stat
```

相关声明：[stat](../posix_system_model_reference/P022_stat_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 405.2\_宏定义（Macros）

<a id="r_a4ce306737c3153a7e2e99272c0a92ec5"></a>

```c
#define st_atime st_atim.tv_sec
```

相关声明：[st_atime](#a4ce306737c3153a7e2e99272c0a92ec5)。

<a id="r_a2dd9b364b84aee095dc6208ff18de4f5"></a>

```c
#define st_ctime st_ctim.tv_sec
```

相关声明：[st_ctime](#a2dd9b364b84aee095dc6208ff18de4f5)。

<a id="r_aecd62777ab7c6c1d6d23e4967632c5ef"></a>

```c
#define st_mtime st_mtim.tv_sec
```

相关声明：[st_mtime](#aecd62777ab7c6c1d6d23e4967632c5ef)。

<a id="r_a7906181b09581ff1e44f07891a1a627b"></a>

```c
#define S_BLKSIZE 1024 /* size of a block */
```

相关声明：[S_BLKSIZE](#a7906181b09581ff1e44f07891a1a627b)。

<a id="r_a30384a8cd2feb1615efd5eadc243684b"></a>

```c
#define S_ISUID 0004000 /* set user id on execution */
```

相关声明：[S_ISUID](#a30384a8cd2feb1615efd5eadc243684b)。

<a id="r_a9c9e4cc0a8acc43c99ae6c3d972ae2d8"></a>

```c
#define S_ISGID 0002000 /* set group id on execution */
```

相关声明：[S_ISGID](#a9c9e4cc0a8acc43c99ae6c3d972ae2d8)、[group](../posix_system_model_reference/P003_group_结构体.md)。

<a id="r_a97b5e445a72c99b37dc5b8d620fbd14e"></a>

```c
#define S_ISVTX 0001000 /* save swapped text even after use */
```

相关声明：[S_ISVTX](#a97b5e445a72c99b37dc5b8d620fbd14e)。

<a id="r_ab5bee51e9ee68b83ab11d4b340f7200b"></a>

```c
#define S_IFMT _IFMT
```

相关声明：[S_IFMT](#ab5bee51e9ee68b83ab11d4b340f7200b)。

<a id="r_a11fb0652b963a735f3377eb1c9239f2d"></a>

```c
#define S_IFDIR _IFDIR
```

相关声明：[S_IFDIR](#a11fb0652b963a735f3377eb1c9239f2d)。

<a id="r_aef3a1d1ba22c83e30b5c834dd343b2a8"></a>

```c
#define S_IFCHR _IFCHR
```

相关声明：[S_IFCHR](#aef3a1d1ba22c83e30b5c834dd343b2a8)。

<a id="r_a5c5b74a1cb1a1ae83572500b94e1938f"></a>

```c
#define S_IFBLK _IFBLK
```

相关声明：[S_IFBLK](#a5c5b74a1cb1a1ae83572500b94e1938f)。

<a id="r_a1aaa48b192a5dd3b6d7ee91fc98cd17d"></a>

```c
#define S_IFREG _IFREG
```

相关声明：[S_IFREG](#a1aaa48b192a5dd3b6d7ee91fc98cd17d)。

<a id="r_afef163ce62372757e84bd9fc88c07aad"></a>

```c
#define S_IFLNK _IFLNK
```

相关声明：[S_IFLNK](#afef163ce62372757e84bd9fc88c07aad)。

<a id="r_a28e80cd43106882904be148b2a397d42"></a>

```c
#define S_IFSOCK _IFSOCK
```

相关声明：[S_IFSOCK](#a28e80cd43106882904be148b2a397d42)。

<a id="r_a4966f25d9f03a7a06bc47ac729fd86cf"></a>

```c
#define S_IFIFO _IFIFO
```

相关声明：[S_IFIFO](#a4966f25d9f03a7a06bc47ac729fd86cf)。

<a id="r_afe3da42e762f6362c93454682fad5eb5"></a>

```c
#define S_IRWXU (S_IRUSR | S_IWUSR | S_IXUSR)
```

相关声明：[S_IRWXU](#afe3da42e762f6362c93454682fad5eb5)、[S_IRUSR](#a84c7dbf5cf2fdfb690f76348b60a8cb7)、[S_IWUSR](#ad70001754261c15a1bdc8e876c6d09d7)、[S_IXUSR](#af10a35e3950795d6ee4e07157d000131)。

<a id="r_a84c7dbf5cf2fdfb690f76348b60a8cb7"></a>

```c
#define S_IRUSR 0000400 /* read permission, owner */
```

相关声明：[S_IRUSR](#a84c7dbf5cf2fdfb690f76348b60a8cb7)。

<a id="r_ad70001754261c15a1bdc8e876c6d09d7"></a>

```c
#define S_IWUSR 0000200 /* write permission, owner */
```

相关声明：[S_IWUSR](#ad70001754261c15a1bdc8e876c6d09d7)。

<a id="r_af10a35e3950795d6ee4e07157d000131"></a>

```c
#define S_IXUSR 0000100 /* execute/search permission, owner */
```

相关声明：[S_IXUSR](#af10a35e3950795d6ee4e07157d000131)。

<a id="r_a230c642d2bb81f15f85c122b1883de5c"></a>

```c
#define S_IRWXG (S_IRGRP | S_IWGRP | S_IXGRP)
```

相关声明：[S_IRWXG](#a230c642d2bb81f15f85c122b1883de5c)、[S_IRGRP](#a4f5f280b929768113739fb34d6f7be8a)、[S_IWGRP](#ae6774871a90d9442f00abe18b87fee6e)、[S_IXGRP](#a042e69ac0e7dd56e5cfcd9e97d010323)。

<a id="r_a4f5f280b929768113739fb34d6f7be8a"></a>

```c
#define S_IRGRP 0000040 /* read permission, group */
```

相关声明：[S_IRGRP](#a4f5f280b929768113739fb34d6f7be8a)、[group](../posix_system_model_reference/P003_group_结构体.md)。

<a id="r_ae6774871a90d9442f00abe18b87fee6e"></a>

```c
#define S_IWGRP 0000020 /* write permission, grougroup */
```

相关声明：[S_IWGRP](#ae6774871a90d9442f00abe18b87fee6e)。

<a id="r_a042e69ac0e7dd56e5cfcd9e97d010323"></a>

```c
#define S_IXGRP 0000010 /* execute/search permission, group */
```

相关声明：[S_IXGRP](#a042e69ac0e7dd56e5cfcd9e97d010323)、[group](../posix_system_model_reference/P003_group_结构体.md)。

<a id="r_a5b93e0da7fe32bbd4926626bffad96b1"></a>

```c
#define S_IRWXO (S_IROTH | S_IWOTH | S_IXOTH)
```

相关声明：[S_IRWXO](#a5b93e0da7fe32bbd4926626bffad96b1)、[S_IROTH](#a071147a0cb995036967c80f64b1f74b9)、[S_IWOTH](#a5303f49f26293acdb9533756c78322fb)、[S_IXOTH](#a40223db1b95a04f5b28cceb3c34cfebd)。

<a id="r_a071147a0cb995036967c80f64b1f74b9"></a>

```c
#define S_IROTH 0000004 /* read permission, other */
```

相关声明：[S_IROTH](#a071147a0cb995036967c80f64b1f74b9)。

<a id="r_a5303f49f26293acdb9533756c78322fb"></a>

```c
#define S_IWOTH 0000002 /* write permission, other */
```

相关声明：[S_IWOTH](#a5303f49f26293acdb9533756c78322fb)。

<a id="r_a40223db1b95a04f5b28cceb3c34cfebd"></a>

```c
#define S_IXOTH 0000001 /* execute/search permission, other */
```

相关声明：[S_IXOTH](#a40223db1b95a04f5b28cceb3c34cfebd)。

<a id="r_a722eba7370eb3b0aafb3272182e08520"></a>

```c
#define S_ISBLK(m)
```

相关声明：[S_ISBLK](#a722eba7370eb3b0aafb3272182e08520)。

<a id="r_a767b5d0691f435f8a9b7f5e0fa97a645"></a>

```c
#define S_ISCHR(m)
```

相关声明：[S_ISCHR](#a767b5d0691f435f8a9b7f5e0fa97a645)。

<a id="r_a70b64ed67c0ab484b4ba09487da34e91"></a>

```c
#define S_ISDIR(m)
```

相关声明：[S_ISDIR](#a70b64ed67c0ab484b4ba09487da34e91)。

<a id="r_a777b706bbe9e7920c091aaa2b547b093"></a>

```c
#define S_ISFIFO(m)
```

相关声明：[S_ISFIFO](#a777b706bbe9e7920c091aaa2b547b093)。

<a id="r_abf68371159fa46b5cc47d0f3ac9ab723"></a>

```c
#define S_ISREG(m)
```

相关声明：[S_ISREG](#abf68371159fa46b5cc47d0f3ac9ab723)。

<a id="r_a835359614ec43fbd96f53993cde84ef2"></a>

```c
#define S_ISLNK(m)
```

相关声明：[S_ISLNK](#a835359614ec43fbd96f53993cde84ef2)。

<a id="r_a765304585be8c05f7fa72495e6d5881f"></a>

```c
#define S_ISSOCK(m)
```

相关声明：[S_ISSOCK](#a765304585be8c05f7fa72495e6d5881f)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 405.3\_函数（Functions）

<a id="r_aa0a896031839c30189c42617ebc5aaeb"></a>

```c
int chmod (const char *__path, mode_t __mode)
```

相关声明：[chmod](#aa0a896031839c30189c42617ebc5aaeb)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

<a id="r_a6a5c46cd35365436fb3bb5e034be78e2"></a>

```c
int fchmod (int __fd, mode_t __mode)
```

相关声明：[fchmod](#a6a5c46cd35365436fb3bb5e034be78e2)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

<a id="r_a276d3b2ba668bdc06f78fccc16b956fe"></a>

```c
int fstat (int __fd, struct stat *__sbuf)
```

相关声明：[fstat](#a276d3b2ba668bdc06f78fccc16b956fe)、[stat](../posix_system_model_reference/P022_stat_结构体.md)。

<a id="r_afa4a4f346213cdc5ae4cfc9aedf7ef2e"></a>

```c
int mkdir (const char *_path, mode_t __mode)
```

相关声明：[mkdir](#afa4a4f346213cdc5ae4cfc9aedf7ef2e)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

<a id="r_acce8c726e07337e0581d74699e2324fe"></a>

```c
int mkfifo (const char *__path, mode_t __mode)
```

相关声明：[mkfifo](#acce8c726e07337e0581d74699e2324fe)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

<a id="r_a0f949e7f97dc8e3e4ea1142cda8be155"></a>

```c
int stat (const char *__restrict __path, struct stat *__restrict __sbuf)
```

相关声明：[stat](#a0f949e7f97dc8e3e4ea1142cda8be155)。

<a id="r_a90e6dc0189b82ecf0e2da52d74d2a149"></a>

```c
mode_t umask (mode_t __mask)
```

相关声明：[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)、[umask](#a90e6dc0189b82ecf0e2da52d74d2a149)、[mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)。

## 405.4\_详细说明（Detailed Documentation）

<a id="a7906181b09581ff1e44f07891a1a627b"></a>

### `S_BLKSIZE`

```c
#define S_BLKSIZE 1024 /* size of a block */
```

<a id="a5c5b74a1cb1a1ae83572500b94e1938f"></a>

### `S_IFBLK`

```c
#define S_IFBLK _IFBLK
```

<a id="aef3a1d1ba22c83e30b5c834dd343b2a8"></a>

### `S_IFCHR`

```c
#define S_IFCHR _IFCHR
```

<a id="a11fb0652b963a735f3377eb1c9239f2d"></a>

### `S_IFDIR`

```c
#define S_IFDIR _IFDIR
```

<a id="a4966f25d9f03a7a06bc47ac729fd86cf"></a>

### `S_IFIFO`

```c
#define S_IFIFO _IFIFO
```

<a id="afef163ce62372757e84bd9fc88c07aad"></a>

### `S_IFLNK`

```c
#define S_IFLNK _IFLNK
```

<a id="ab5bee51e9ee68b83ab11d4b340f7200b"></a>

### `S_IFMT`

```c
#define S_IFMT _IFMT
```

<a id="a1aaa48b192a5dd3b6d7ee91fc98cd17d"></a>

### `S_IFREG`

```c
#define S_IFREG _IFREG
```

<a id="a28e80cd43106882904be148b2a397d42"></a>

### `S_IFSOCK`

```c
#define S_IFSOCK _IFSOCK
```

<a id="a4f5f280b929768113739fb34d6f7be8a"></a>

### `S_IRGRP`

```c
#define S_IRGRP 0000040 /* read permission, group */
```

<a id="a071147a0cb995036967c80f64b1f74b9"></a>

### `S_IROTH`

```c
#define S_IROTH 0000004 /* read permission, other */
```

<a id="a84c7dbf5cf2fdfb690f76348b60a8cb7"></a>

### `S_IRUSR`

```c
#define S_IRUSR 0000400 /* read permission, owner */
```

<a id="a230c642d2bb81f15f85c122b1883de5c"></a>

### `S_IRWXG`

```c
#define S_IRWXG (S_IRGRP | S_IWGRP | S_IXGRP)
```

<a id="a5b93e0da7fe32bbd4926626bffad96b1"></a>

### `S_IRWXO`

```c
#define S_IRWXO (S_IROTH | S_IWOTH | S_IXOTH)
```

<a id="afe3da42e762f6362c93454682fad5eb5"></a>

### `S_IRWXU`

```c
#define S_IRWXU (S_IRUSR | S_IWUSR | S_IXUSR)
```

<a id="a722eba7370eb3b0aafb3272182e08520"></a>

### `S_ISBLK`

```c
#define S_ISBLK ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFBLK)
```

<a id="a767b5d0691f435f8a9b7f5e0fa97a645"></a>

### `S_ISCHR`

```c
#define S_ISCHR ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFCHR)
```

<a id="a70b64ed67c0ab484b4ba09487da34e91"></a>

### `S_ISDIR`

```c
#define S_ISDIR ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFDIR)
```

<a id="a777b706bbe9e7920c091aaa2b547b093"></a>

### `S_ISFIFO`

```c
#define S_ISFIFO ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFIFO)
```

<a id="a9c9e4cc0a8acc43c99ae6c3d972ae2d8"></a>

### `S_ISGID`

```c
#define S_ISGID 0002000 /* set group id on execution */
```

<a id="a835359614ec43fbd96f53993cde84ef2"></a>

### `S_ISLNK`

```c
#define S_ISLNK ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFLNK)
```

<a id="abf68371159fa46b5cc47d0f3ac9ab723"></a>

### `S_ISREG`

```c
#define S_ISREG ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFREG)
```

<a id="a765304585be8c05f7fa72495e6d5881f"></a>

### `S_ISSOCK`

```c
#define S_ISSOCK ( m)
```

展开值（Value）：

```c
(((m)&_IFMT) == _IFSOCK)
```

<a id="a30384a8cd2feb1615efd5eadc243684b"></a>

### `S_ISUID`

```c
#define S_ISUID 0004000 /* set user id on execution */
```

<a id="a97b5e445a72c99b37dc5b8d620fbd14e"></a>

### `S_ISVTX`

```c
#define S_ISVTX 0001000 /* save swapped text even after use */
```

<a id="ae6774871a90d9442f00abe18b87fee6e"></a>

### `S_IWGRP`

```c
#define S_IWGRP 0000020 /* write permission, grougroup */
```

<a id="a5303f49f26293acdb9533756c78322fb"></a>

### `S_IWOTH`

```c
#define S_IWOTH 0000002 /* write permission, other */
```

<a id="ad70001754261c15a1bdc8e876c6d09d7"></a>

### `S_IWUSR`

```c
#define S_IWUSR 0000200 /* write permission, owner */
```

<a id="a042e69ac0e7dd56e5cfcd9e97d010323"></a>

### `S_IXGRP`

```c
#define S_IXGRP 0000010 /* execute/search permission, group */
```

<a id="a40223db1b95a04f5b28cceb3c34cfebd"></a>

### `S_IXOTH`

```c
#define S_IXOTH 0000001 /* execute/search permission, other */
```

<a id="af10a35e3950795d6ee4e07157d000131"></a>

### `S_IXUSR`

```c
#define S_IXUSR 0000100 /* execute/search permission, owner */
```

<a id="a4ce306737c3153a7e2e99272c0a92ec5"></a>

### `st_atime`

```c
#define st_atime st_atim.tv_sec
```

<a id="a2dd9b364b84aee095dc6208ff18de4f5"></a>

### `st_ctime`

```c
#define st_ctime st_ctim.tv_sec
```

<a id="aecd62777ab7c6c1d6d23e4967632c5ef"></a>

### `st_mtime`

```c
#define st_mtime st_mtim.tv_sec
```

<a id="aa0a896031839c30189c42617ebc5aaeb"></a>

### `chmod()`

```c
int chmod ( const char * __path, mode_t __mode )
```

<a id="a6a5c46cd35365436fb3bb5e034be78e2"></a>

### `fchmod()`

```c
int fchmod ( int __fd, mode_t __mode )
```

<a id="a276d3b2ba668bdc06f78fccc16b956fe"></a>

### `fstat()`

```c
int fstat ( int __fd, struct stat * __sbuf )
```

<a id="afa4a4f346213cdc5ae4cfc9aedf7ef2e"></a>

### `mkdir()`

```c
int mkdir ( const char * _path, mode_t __mode )
```

<a id="acce8c726e07337e0581d74699e2324fe"></a>

### `mkfifo()`

```c
int mkfifo ( const char * __path, mode_t __mode )
```

<a id="a0f949e7f97dc8e3e4ea1142cda8be155"></a>

### `stat()`

```c
int stat ( const char *__restrict __path, struct stat *__restrict __sbuf )
```

<a id="a90e6dc0189b82ecf0e2da52d74d2a149"></a>

### `umask()`

```c
mode_t umask ( mode_t __mask)
```


## 405.5\_原页交叉引用（Cross References）

- [time.h](../api_source_supplement_reference/P093_time.h_源码浏览.md)
- [sys/cdefs.h](../api_source_reference/P086_cdefs.h_源码浏览.md)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [stat](../posix_system_model_reference/P022_stat_结构体.md)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [mode_t](P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#adb8322e115035a284aab704909e63d00)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P404_zephyr__debug__stack.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P406_zephyr__net__http__status.h_文件参考.md)
