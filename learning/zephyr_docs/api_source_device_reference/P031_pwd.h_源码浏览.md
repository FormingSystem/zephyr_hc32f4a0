---
id: learning.zephyr-docs.api-source-device-reference.page-31
title: pwd.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_pwd.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pwd_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P313_zephyr__posix__pwd.h_文件参考.md)。

## 31.1\_原始可见代码（Source Code）

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
<a id="foldopen00015"></a>
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
<a id="aposix__signal_8h_html_afc544433253791fc5f87b8203c9b6e63"></a>
<a id="aposix__types_8h_html_a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>
<a id="apwd_8h_html_a171c52c8fac39d01f77ed0d69efbaa61"></a>
<a id="apwd_8h_html_a9848a1faaee1b74dbc399b2d746ef16c"></a>
<a id="astat_8h_html"></a>
<a id="astructpasswd_html"></a>
<a id="astructpasswd_html_a6de92e6d2e3dd348ee82472d2b219556"></a>
<a id="astructpasswd_html_aa0584dc9fdf7920c25b6326b5fdb5416"></a>
<a id="astructpasswd_html_aa6e0e62ee3cf5152f2697a0104f627c1"></a>
<a id="astructpasswd_html_aefbacfb7dc7f7f47313d08707253e4c6"></a>
<a id="astructpasswd_html_afa7bb51f592e9199dc776ccc763352a7"></a>

```c
/*
 * Copyright (c) 2024 Meta Platforms
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_PWD_H_
#define ZEPHYR_INCLUDE_POSIX_PWD_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/posix/sys/stat.h>

struct passwd {
        /* user's login name */
        char *pw_name;
        /* numerical user ID */
        uid_t pw_uid;
        /* numerical group ID */
        gid_t pw_gid;
        /* initial working directory */
        char *pw_dir;
        /* program to use as shell */
        char *pw_shell;
};

int getpwnam_r(const char *nam, struct passwd *pwd, char *buffer, size_t bufsize,
               struct passwd **result);
int getpwuid_r(uid_t uid, struct passwd *pwd, char *buffer, size_t bufsize, struct passwd **result);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_PWD_H_ */
```

## 31.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

用户登录名（User Login Name）。

### 注释 3：原第 18 行

数值用户标识（Numerical User ID）。

### 注释 4：原第 20 行

数值形式的组 ID（group ID）。

### 注释 5：原第 22 行

初始工作目录（Initial Working Directory）。

### 注释 6：原第 24 行

用作命令解释器（Shell）的程序。

### 注释 7：原第 36 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_PWD_H_`。

## 31.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P313_zephyr__posix__pwd.h_文件参考.md)
- [zephyr/posix/sys/stat.h](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md)
- [passwd](../posix_system_model_reference/P009_passwd_结构体.md)
- [pw_name](../posix_system_model_reference/P009_passwd_结构体.md#a6de92e6d2e3dd348ee82472d2b219556)
- [uid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#afc544433253791fc5f87b8203c9b6e63)
- [pw_uid](../posix_system_model_reference/P009_passwd_结构体.md#aa6e0e62ee3cf5152f2697a0104f627c1)
- [gid_t](../api_file_reference/P312_zephyr__posix__posix_types.h_文件参考.md#a3a7834be1a79bb0c5a65d3546c2e3bd8)
- [pw_gid](../posix_system_model_reference/P009_passwd_结构体.md#aefbacfb7dc7f7f47313d08707253e4c6)
- [pw_dir](../posix_system_model_reference/P009_passwd_结构体.md#afa7bb51f592e9199dc776ccc763352a7)
- [pw_shell](../posix_system_model_reference/P009_passwd_结构体.md#aa0584dc9fdf7920c25b6326b5fdb5416)
- [getpwnam_r](../api_file_reference/P313_zephyr__posix__pwd.h_文件参考.md#a9848a1faaee1b74dbc399b2d746ef16c)
- [getpwuid_r](../api_file_reference/P313_zephyr__posix__pwd.h_文件参考.md#a171c52c8fac39d01f77ed0d69efbaa61)
- [stat.h](../api_file_reference/P405_zephyr__posix__sys__stat.h_文件参考.md)
- [passwd::pw_name](../posix_system_model_reference/P009_passwd_结构体.md#a6de92e6d2e3dd348ee82472d2b219556)
- [passwd::pw_shell](../posix_system_model_reference/P009_passwd_结构体.md#aa0584dc9fdf7920c25b6326b5fdb5416)
- [passwd::pw_uid](../posix_system_model_reference/P009_passwd_结构体.md#aa6e0e62ee3cf5152f2697a0104f627c1)
- [passwd::pw_gid](../posix_system_model_reference/P009_passwd_结构体.md#aefbacfb7dc7f7f47313d08707253e4c6)
- [passwd::pw_dir](../posix_system_model_reference/P009_passwd_结构体.md#afa7bb51f592e9199dc776ccc763352a7)

---

[上一章](P030_pinctrl_rcar_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P032_renesas-rz-gpio.h_源码浏览.md)
