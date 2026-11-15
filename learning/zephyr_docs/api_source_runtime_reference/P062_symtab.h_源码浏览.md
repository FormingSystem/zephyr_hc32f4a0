---
id: learning.zephyr-docs.api-source-runtime-reference.page-62
title: symtab.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_symtab.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h.html)。

## 62.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00034"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="agroup__symtab__apis_html_ga2f1c4fa3cc113c2e5f47c5bbcd337e32"></a>
<a id="agroup__symtab__apis_html_gac5927cf3f4e0bf3e1b27b397290e44c5"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructsymtab__info_html"></a>
<a id="astructsymtab__info_html_a69ad14fd05738735036cab84ddad02bc"></a>
<a id="astructsymtab__info_html_a86d6af07f0ddb6c95ee6db63307a0783"></a>
<a id="astructsymtab__info_html_a8d2bb0574287422a94c5d6074cfda066"></a>

```c
/*
 * Copyright (c) 2024 Meta Platforms
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DEBUG_SYMTAB_H_
#define ZEPHYR_INCLUDE_DEBUG_SYMTAB_H_

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif



struct z_symtab_entry {
        const uint32_t offset;
        const char *const name;
};


struct symtab_info {
        /* Absolute address of the first symbol */
        const uintptr_t first_addr;
        /* Number of symbol entries */
        const uint32_t length;
        /* Symbol entries */
        const struct z_symtab_entry *const entries;
};

const struct symtab_info *symtab_get(void);

const char *symtab_find_symbol_name(uintptr_t addr, uint32_t *offset);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DEBUG_SYMTAB_H_ */
```

## 62.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

第一个符号的绝对地址（Absolute address）。

### 注释 3：原第 38 行

符号条目数量。

### 注释 4：原第 40 行

符号条目（Symbol entries）。

### 注释 5：原第 70 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DEBUG_SYMTAB_H_`。

## 62.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/symtab_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [symtab_info](../observability/P056_符号表信息结构.md)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [first_addr](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a86d6af07f0ddb6c95ee6db63307a0783)
- [length](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a8d2bb0574287422a94c5d6074cfda066)
- [entries](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a69ad14fd05738735036cab84ddad02bc)
- [symtab_get](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#ga2f1c4fa3cc113c2e5f47c5bbcd337e32)
- [symtab_find_symbol_name](https://docs.zephyrproject.org/latest/doxygen/html/group__symtab__apis.html#gac5927cf3f4e0bf3e1b27b397290e44c5)
- [symtab_info::entries](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a69ad14fd05738735036cab84ddad02bc)
- [symtab_info::first_addr](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a86d6af07f0ddb6c95ee6db63307a0783)
- [symtab_info::length](https://docs.zephyrproject.org/latest/doxygen/html/structsymtab__info.html#a8d2bb0574287422a94c5d6074cfda066)

---

[上一章](P061_stm32wb0_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P063_sysconf.h_源码浏览.md)
