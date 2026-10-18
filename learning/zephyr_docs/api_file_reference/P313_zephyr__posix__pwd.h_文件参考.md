---
id: learning.zephyr-docs.api-file-reference.page-313
title: zephyr__posix__pwd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第313章\_zephyr\_\_posix\_\_pwd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/posix/sys/stat.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 313.1\_数据结构（Data Structures）

<a id="r_passwd"></a>

```c
struct passwd
```

相关声明：[passwd](../posix_system_model_reference/P009_passwd_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 313.2\_函数（Functions）

<a id="r_a9848a1faaee1b74dbc399b2d746ef16c"></a>

```c
int getpwnam_r (const char *nam, struct passwd *pwd, char *buffer, size_t bufsize, struct passwd **result)
```

相关声明：[getpwnam_r](#a9848a1faaee1b74dbc399b2d746ef16c)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)。

<a id="r_a171c52c8fac39d01f77ed0d69efbaa61"></a>

```c
int getpwuid_r (uid_t uid, struct passwd *pwd, char *buffer, size_t bufsize, struct passwd **result)
```

相关声明：[getpwuid_r](#a171c52c8fac39d01f77ed0d69efbaa61)、[uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)、[passwd](../posix_system_model_reference/P009_passwd_结构体.md)。

## 313.3\_详细说明（Detailed Documentation）

<a id="a9848a1faaee1b74dbc399b2d746ef16c"></a>

### `getpwnam_r()`

```c
int getpwnam_r ( const char * nam, struct passwd * pwd, char * buffer, size_t bufsize, struct passwd ** result )
```

<a id="a171c52c8fac39d01f77ed0d69efbaa61"></a>

### `getpwuid_r()`

```c
int getpwuid_r ( uid_t uid, struct passwd * pwd, char * buffer, size_t bufsize, struct passwd ** result )
```


## 313.4\_原页交叉引用（Cross References）

- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h_source.html)
- [passwd](../posix_system_model_reference/P009_passwd_结构体.md)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P312_zephyr__posix__posix_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P314_zephyr__drivers__pwm__pwm_mchp_pwm_g1.h_文件参考.md)
