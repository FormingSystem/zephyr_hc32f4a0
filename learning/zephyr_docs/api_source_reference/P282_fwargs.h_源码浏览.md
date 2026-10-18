---
id: learning.zephyr-docs.api-source-reference.page-282
title: fwargs.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第282章\_fwargs.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h.html)。

## 282.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="afwargs_8h_html_adb1a5f394ddae4582b7a522e9b0a80bc"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * Copyright (c) 2026 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ZEPHYR_PLATFORM_FWARGS_H_
#define ZEPHYR_INCLUDE_ZEPHYR_PLATFORM_FWARGS_H_

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_FWARGS_HANDLER_HOOK) || defined(__DOXYGEN__)
void fwargs_handler_hook(const uintptr_t *args, size_t argc);
#endif

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZEPHYR_PLATFORM_FWARGS_H_ */
```

## 282.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_PLATFORM_FWARGS_H_`。

## 282.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [fwargs_handler_hook](https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h.html#adb1a5f394ddae4582b7a522e9b0a80bc)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)

---

[上一章](P281_ft8xx_memory.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P283_gauge.h_源码浏览.md)
