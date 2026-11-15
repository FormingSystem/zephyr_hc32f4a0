---
id: learning.zephyr-docs.api-source-reference.page-671
title: printk-hooks.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第671章\_printk-hooks.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h.html)。

## 671.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="aprintk-hooks_8h_html_a17d0c01ee515cc6f962dbd56a4c9b36f"></a>

```c
/*
 * Copyright 2024 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SYS_PRINTK_HOOKS_H_
#define ZEPHYR_INCLUDE_SYS_PRINTK_HOOKS_H_

typedef int (*printk_hook_fn_t)(int c);

void __printk_hook_install(printk_hook_fn_t fn);

printk_hook_fn_t __printk_get_hook(void);

#endif /* ZEPHYR_INCLUDE_SYS_PRINTK_HOOKS_H_ */
```

## 671.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 43 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_PRINTK_HOOKS_H_`。

## 671.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h.html)
- [printk_hook_fn_t](https://docs.zephyrproject.org/latest/doxygen/html/printk-hooks_8h.html#a17d0c01ee515cc6f962dbd56a4c9b36f)

---

[上一章](P670_print_format.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P672_priv_beacon_cli.h_源码浏览.md)
