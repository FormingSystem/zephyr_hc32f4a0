---
id: learning.zephyr-docs.api-file-reference.page-49
title: zephyr__posix__dirent.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dirent_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_posix\_\_dirent.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dirent_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/dirent.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 49.1\_函数（Functions）

<a id="r_aaeac2b41e8c2c3a5f91c9bd511a8c0a6"></a>

```c
int closedir (DIR *dirp)
```

相关声明：[closedir](#aaeac2b41e8c2c3a5f91c9bd511a8c0a6)、[DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)。

<a id="r_a58be90fffc0b5713ea34e39eb26d59f3"></a>

```c
DIR * fdopendir (int fd)
```

相关声明：[DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)、[fdopendir](#a58be90fffc0b5713ea34e39eb26d59f3)。

<a id="r_ae27c7f260a652b74c43296993d14ef0b"></a>

```c
DIR * opendir (const char *dirname)
```

相关声明：[DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)、[opendir](#ae27c7f260a652b74c43296993d14ef0b)。

<a id="r_a824e3b8c5995631b373ddb65cb674318"></a>

```c
struct dirent * readdir (DIR *dirp)
```

相关声明：[dirent](../posix_system_model_reference/P001_dirent_结构体.md)、[readdir](#a824e3b8c5995631b373ddb65cb674318)、[DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)。

<a id="r_ad4fcb58b9194b1a3c1699654de963719"></a>

```c
void rewinddir (DIR *dirp)
```

相关声明：[rewinddir](#ad4fcb58b9194b1a3c1699654de963719)、[DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)。

## 49.2\_详细说明（Detailed Documentation）

<a id="aaeac2b41e8c2c3a5f91c9bd511a8c0a6"></a>

### `closedir()`

```c
int closedir ( DIR * dirp)
```

<a id="a58be90fffc0b5713ea34e39eb26d59f3"></a>

### `fdopendir()`

```c
DIR * fdopendir ( int fd)
```

<a id="ae27c7f260a652b74c43296993d14ef0b"></a>

### `opendir()`

```c
DIR * opendir ( const char * dirname)
```

<a id="a824e3b8c5995631b373ddb65cb674318"></a>

### `readdir()`

```c
struct dirent * readdir ( DIR * dirp)
```

<a id="ad4fcb58b9194b1a3c1699654de963719"></a>

### `rewinddir()`

```c
void rewinddir ( DIR * dirp)
```


## 49.3\_原页交叉引用（Cross References）

- [zephyr/posix/sys/dirent.h](../api_source_reference/P851_dirent.h_源码浏览.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P133_dirent.h_源码浏览.md)
- [DIR](P479_zephyr__posix__sys__dirent.h_文件参考.md#a6808d95339147c6e29523463181854cc)
- [dirent](../posix_system_model_reference/P001_dirent_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P048_____w__zephyr__zephyr__lib__libc__minimal__include__ctype.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__bluetooth__services__dis.h_文件参考.md)
