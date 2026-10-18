---
id: learning.zephyr-docs.api-source-supplement-reference.page-241
title: utsname.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第241章\_utsname.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h.html)。

## 241.1\_原始可见代码（Source Code）

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
<a id="foldopen00021"></a>
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
<a id="astructutsname_html"></a>
<a id="astructutsname_html_a708b512fcd536a51fa7266899eec3964"></a>
<a id="astructutsname_html_a8bfca811eed8101b2310200a96e9757e"></a>
<a id="astructutsname_html_abe146e9be86c55a25881e6c58ba3ddf0"></a>
<a id="astructutsname_html_afc4ee8a38fc0d85ac4f8fe1b669c3f74"></a>
<a id="astructutsname_html_afcc31cc768b481d10c887dcf56d64a1c"></a>
<a id="autil__macro_8h_html"></a>
<a id="autsname_8h_html_a1ad7a68f28b58669758da1b12061a81f"></a>

```c
/*
 * Copyright (c) 2023 Meta
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SYS_UTSNAME_H_
#define ZEPHYR_INCLUDE_POSIX_SYS_UTSNAME_H_

#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif

/* These are for compatibility / practicality */
#define _UTSNAME_NODENAME_LENGTH                                                                   \
        COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS, (CONFIG_POSIX_UNAME_VERSION_LEN), (0))
#define _UTSNAME_VERSION_LENGTH                                                                    \
        COND_CODE_1(CONFIG_POSIX_SINGLE_PROCESS, (CONFIG_POSIX_UNAME_VERSION_LEN), (0))

struct utsname {
        char sysname[sizeof("Zephyr")];
        char nodename[_UTSNAME_NODENAME_LENGTH + 1];
        char release[sizeof("99.99.99-rc1")];
        char version[_UTSNAME_VERSION_LENGTH + 1];
        char machine[sizeof(CONFIG_ARCH)];
};

int uname(struct utsname *name);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SYS_UTSNAME_H_ */
```

## 241.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Meta。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 15 行

这些内容用于兼容性或实际使用便利。

### 注释 3：原第 35 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SYS_UTSNAME_H_`。

## 241.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [utsname](../posix_system_model_reference/P028_utsname_结构体.md)
- [sysname](../posix_system_model_reference/P028_utsname_结构体.md#a8bfca811eed8101b2310200a96e9757e)
- [nodename](../posix_system_model_reference/P028_utsname_结构体.md#afc4ee8a38fc0d85ac4f8fe1b669c3f74)
- [release](../posix_system_model_reference/P028_utsname_结构体.md#afcc31cc768b481d10c887dcf56d64a1c)
- [version](../posix_system_model_reference/P028_utsname_结构体.md#abe146e9be86c55a25881e6c58ba3ddf0)
- [machine](../posix_system_model_reference/P028_utsname_结构体.md#a708b512fcd536a51fa7266899eec3964)
- [uname](https://docs.zephyrproject.org/latest/doxygen/html/utsname_8h.html#a1ad7a68f28b58669758da1b12061a81f)
- [utsname::machine](../posix_system_model_reference/P028_utsname_结构体.md#a708b512fcd536a51fa7266899eec3964)
- [utsname::sysname](../posix_system_model_reference/P028_utsname_结构体.md#a8bfca811eed8101b2310200a96e9757e)
- [utsname::version](../posix_system_model_reference/P028_utsname_结构体.md#abe146e9be86c55a25881e6c58ba3ddf0)
- [utsname::nodename](../posix_system_model_reference/P028_utsname_结构体.md#afc4ee8a38fc0d85ac4f8fe1b669c3f74)
- [utsname::release](../posix_system_model_reference/P028_utsname_结构体.md#afcc31cc768b481d10c887dcf56d64a1c)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P240_usbh.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P242_virtqueue.h_源码浏览.md)
