---
id: learning.zephyr-docs.api-source-reference.page-845
title: error.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第845章\_error.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../storage/P023_PSA存储返回值.md)。

## 845.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="asubsys_2secure__storage_2include_2psa_2error_8h_html_a05676e70ba5c6a7565aff3c36677c1f9"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef PSA_ERROR_H
#define PSA_ERROR_H
#include <stdint.h>

typedef int32_t psa_status_t;

#define PSA_SUCCESS ((psa_status_t)0)

#define PSA_ERROR_GENERIC_ERROR        ((psa_status_t)-132)

#define PSA_ERROR_NOT_PERMITTED        ((psa_status_t)-133)

#define PSA_ERROR_NOT_SUPPORTED        ((psa_status_t)-134)

#define PSA_ERROR_INVALID_ARGUMENT     ((psa_status_t)-135)

#define PSA_ERROR_ALREADY_EXISTS       ((psa_status_t)-139)

#define PSA_ERROR_DOES_NOT_EXIST       ((psa_status_t)-140)

#define PSA_ERROR_INSUFFICIENT_STORAGE ((psa_status_t)-142)

#define PSA_ERROR_STORAGE_FAILURE      ((psa_status_t)-146)

#define PSA_ERROR_INVALID_SIGNATURE    ((psa_status_t)-149)

#define PSA_ERROR_DATA_CORRUPT         ((psa_status_t)-152)

#endif
```

## 845.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 845.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../storage/P023_PSA存储返回值.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [psa_status_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2psa_2error_8h.html#a05676e70ba5c6a7565aff3c36677c1f9)

---

[上一章](P844_settings.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P846_summary.h_源码浏览.md)
