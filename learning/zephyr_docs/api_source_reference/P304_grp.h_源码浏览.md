---
id: learning.zephyr-docs.api-source-reference.page-304
title: grp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/grp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第304章\_grp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html)。

## 304.1\_原始可见代码（Source Code）

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
<a id="foldopen00018"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00022"></a>
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
<a id="agrp_8h_html_a64e84dfb3f386daaa7530fc8177a6056"></a>
<a id="agrp_8h_html_acf054c85917adbbc3687004d51317685"></a>
<a id="aposix__types_8h_html_a3a7834be1a79bb0c5a65d3546c2e3bd8"></a>
<a id="astat_8h_html"></a>
<a id="astructgroup_html"></a>
<a id="astructgroup_html_a00f124d1201a4de3cc885fe87a91431f"></a>
<a id="astructgroup_html_a338a8153e1e47d345a0bb578f3c2656c"></a>
<a id="astructgroup_html_a828b9f3708aa76cecd8fda0a20b61e98"></a>

```c
/*
 * Copyright (c) 2024 Meta Platforms
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_GRP_H_
#define ZEPHYR_INCLUDE_POSIX_GRP_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/posix/sys/stat.h>

struct group {
        char *gr_name;
        gid_t gr_gid;
        char **gr_mem;
};

int getgrnam_r(const char *name, struct group *grp, char *buffer, size_t bufsize,
               struct group **result);
int getgrgid_r(gid_t gid, struct group *grp, char *buffer, size_t bufsize, struct group **result);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_GRP_H_ */
```

## 304.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_GRP_H_`。

## 304.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html)
- [zephyr/posix/sys/stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [gr_name](../posix_system_model_reference/P003_group_结构体.md#a828b9f3708aa76cecd8fda0a20b61e98)
- [gid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html#a3a7834be1a79bb0c5a65d3546c2e3bd8)
- [gr_gid](../posix_system_model_reference/P003_group_结构体.md#a00f124d1201a4de3cc885fe87a91431f)
- [gr_mem](../posix_system_model_reference/P003_group_结构体.md#a338a8153e1e47d345a0bb578f3c2656c)
- [getgrnam_r](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html#acf054c85917adbbc3687004d51317685)
- [getgrgid_r](https://docs.zephyrproject.org/latest/doxygen/html/grp_8h.html#a64e84dfb3f386daaa7530fc8177a6056)
- [stat.h](https://docs.zephyrproject.org/latest/doxygen/html/stat_8h.html)
- [group::gr_gid](../posix_system_model_reference/P003_group_结构体.md#a00f124d1201a4de3cc885fe87a91431f)
- [group::gr_mem](../posix_system_model_reference/P003_group_结构体.md#a338a8153e1e47d345a0bb578f3c2656c)
- [group::gr_name](../posix_system_model_reference/P003_group_结构体.md#a828b9f3708aa76cecd8fda0a20b61e98)

---

[上一章](P303_gpio_sx1509b.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P305_h4.h_源码浏览.md)
