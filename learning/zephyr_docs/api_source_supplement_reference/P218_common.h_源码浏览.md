---
id: learning.zephyr-docs.api-source-supplement-reference.page-218
title: common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第218章\_common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html)。

## 218.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="foldopen00013"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="asubsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_html_ac3c7c0ba918fe964b4c39ae0d8047bdd"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef SECURE_STORAGE_COMMON_H
#define SECURE_STORAGE_COMMON_H

#include <stdint.h>

/* A size-optimized version of `psa_storage_create_flags_t`. Used for storing the `create_flags`. */
typedef uint8_t secure_storage_packed_create_flags_t;

#define SECURE_STORAGE_ALL_CREATE_FLAGS \
        (PSA_STORAGE_FLAG_NONE | \
         PSA_STORAGE_FLAG_WRITE_ONCE | \
         PSA_STORAGE_FLAG_NO_CONFIDENTIALITY | \
         PSA_STORAGE_FLAG_NO_REPLAY_PROTECTION)

#endif
```

## 218.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

针对大小优化的 `psa_storage_create_flags_t` 版本，用于存储 `create_flags`。

## 218.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [secure_storage_packed_create_flags_t](https://docs.zephyrproject.org/latest/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.html#ac3c7c0ba918fe964b4c39ae0d8047bdd)

---

[上一章](P217_strings.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P219_sy1xx-pinctrl.h_源码浏览.md)
