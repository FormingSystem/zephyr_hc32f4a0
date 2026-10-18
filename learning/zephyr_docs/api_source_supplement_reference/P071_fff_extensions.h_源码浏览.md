---
id: learning.zephyr-docs.api-source-supplement-reference.page-71
title: fff_extensions.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fff__extensions_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_fff\_extensions.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fff__extensions_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fff__extensions_8h.html)。

## 71.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00077"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Legrand North America, LLC.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_SUBSYS_TESTSUITE_INCLUDE_ZEPHYR_FFF_EXTENSIONS_H_
#define ZEPHYR_SUBSYS_TESTSUITE_INCLUDE_ZEPHYR_FFF_EXTENSIONS_H_

#include <zephyr/fff.h>
#include <zephyr/sys/util.h> /* for CONTAINER_OF */



#define RETURN_HANDLED_CONTEXT(FUNCNAME, CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY)    \
        if (FUNCNAME##_fake.return_val_seq_len) {                                                  \
                CONTEXTTYPE * const contexts =                                                     \
                        CONTAINER_OF(FUNCNAME##_fake.return_val_seq, CONTEXTTYPE, RESULTFIELD);    \
                size_t const seq_idx =                                                             \
                        (FUNCNAME##_fake.return_val_seq_idx < FUNCNAME##_fake.return_val_seq_len)  \
                                ? FUNCNAME##_fake.return_val_seq_idx++                             \
                                : FUNCNAME##_fake.return_val_seq_idx - 1;                          \
                CONTEXTTYPE * const CONTEXTPTRNAME = &contexts[seq_idx];                           \
                HANDLERBODY;                                                                       \
        }                                                                                          \
        return FUNCNAME##_fake.return_val


#endif /* ZEPHYR_SUBSYS_TESTSUITE_INCLUDE_ZEPHYR_FFF_EXTENSIONS_H_ */
```

## 71.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Legrand North America, LLC.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

供 `CONTAINER_OF` 使用。

### 注释 3：原第 95 行

头文件保护宏（Header guard）标记：`ZEPHYR_SUBSYS_TESTSUITE_INCLUDE_ZEPHYR_FFF_EXTENSIONS_H_`。

## 71.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fff__extensions_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P070_fdc2x1x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P072_focaltech_ft9001_pinctrl.h_源码浏览.md)
