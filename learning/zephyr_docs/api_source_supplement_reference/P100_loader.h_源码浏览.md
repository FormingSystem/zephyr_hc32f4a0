---
id: learning.zephyr-docs.api-source-supplement-reference.page-100
title: loader.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/loader_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第100章\_loader.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)。

## 100.1\_原始可见代码（Source Code）

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
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00055"></a>
<a id="l00062"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="aelf_8h_html"></a>
<a id="agroup__llext__apis_html_gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265"></a>
<a id="agroup__llext__elf_html_gab3695edd628cf868dc4f0d618f86bcbd"></a>
<a id="agroup__llext__elf_html_gab39a1763256a6b9ccccf8b89836cd192"></a>
<a id="agroup__llext__loader__apis_html_ga8e04f364aef19cf45843cc97cc702f24"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b"></a>
<a id="agroup__llext__loader__apis_html_gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0"></a>
<a id="allext_8h_html"></a>
<a id="astructllext__loader_html"></a>
<a id="astructllext__loader_html_a1b82b69501e174b6a0f24ef356abbf16"></a>
<a id="astructllext__loader_html_a2376c3774af219972e164b0ee8a6bb6d"></a>
<a id="astructllext__loader_html_a29a16df55b72bc299b338036437f53e0"></a>
<a id="astructllext__loader_html_a3034e439e3c55a2ed874cf2db6aba46e"></a>
<a id="astructllext__loader_html_a7c0ea7bce0a56ccf98e120a52e362b37"></a>
<a id="astructllext__loader_html_af5452f4b4f1099379d110c1bcd7773f6"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LLEXT_LOADER_H_
#define ZEPHYR_INCLUDE_LLEXT_LOADER_H_

#include <zephyr/llext/elf.h>
#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif


#include <zephyr/llext/llext.h>

struct llext_elf_sect_map; /* defined in llext_internal.h */

enum llext_storage_type {
        LLEXT_STORAGE_TEMPORARY,
        LLEXT_STORAGE_PERSISTENT,
        LLEXT_STORAGE_WRITABLE,
};

struct llext_loader {
        int (*prepare)(struct llext_loader *ldr);

        int (*read)(struct llext_loader *ldr, void *out, size_t len);

        int (*seek)(struct llext_loader *ldr, size_t pos);

        void *(*peek)(struct llext_loader *ldr, size_t pos);

        void (*finalize)(struct llext_loader *ldr);

        enum llext_storage_type storage;

        elf_ehdr_t hdr;
        elf_shdr_t sects[LLEXT_MEM_COUNT];
        struct llext_elf_sect_map *sect_map;
};

static inline int llext_prepare(struct llext_loader *l)
{
        if (l->prepare) {
                return l->prepare(l);
        }

        return 0;
}

static inline int llext_read(struct llext_loader *l, void *buf, size_t len)
{
        return l->read(l, buf, len);
}

static inline int llext_seek(struct llext_loader *l, size_t pos)
{
        return l->seek(l, pos);
}

static inline void *llext_peek(struct llext_loader *l, size_t pos)
{
        if (l->peek) {
                return l->peek(l, pos);
        }

        return NULL;
}

static inline void llext_finalize(struct llext_loader *l)
{
        if (l->finalize) {
                l->finalize(l);
        }
}
/* @endcond */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_LLEXT_LOADER_H_ */
```

## 100.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 32 行

在 `llext_internal.h` 中定义。

### 注释 3：原第 183 行

Doxygen 条件文档块结束标记：`@endcond`。

### 注释 4：原第 193 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_LOADER_H_`。

## 100.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [zephyr/llext/elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html)
- [zephyr/llext/llext.h](../llext/P016_扩展管理头文件.md)
- [llext_storage_type](../llext/P014_ELF加载器API.md#ga8e04f364aef19cf45843cc97cc702f24)
- [LLEXT_STORAGE_TEMPORARY](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24a256d7c93a7232505368ab49713d756e6)
- [LLEXT_STORAGE_PERSISTENT](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ade339a696a5d3b0c1b3ff5ad0d73f8a0)
- [LLEXT_STORAGE_WRITABLE](../llext/P014_ELF加载器API.md#gga8e04f364aef19cf45843cc97cc702f24ad588662b67dcd79213b43dc1ed78b52b)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [prepare](../llext/P025_扩展加载器上下文.md#a3034e439e3c55a2ed874cf2db6aba46e)
- [read](../llext/P025_扩展加载器上下文.md#a29a16df55b72bc299b338036437f53e0)
- [seek](../llext/P025_扩展加载器上下文.md#a2376c3774af219972e164b0ee8a6bb6d)
- [finalize](../llext/P025_扩展加载器上下文.md#a7c0ea7bce0a56ccf98e120a52e362b37)
- [storage](../llext/P025_扩展加载器上下文.md#a1b82b69501e174b6a0f24ef356abbf16)
- [elf_ehdr_t](../llext/P012_ELF常量与类型.md#gab39a1763256a6b9ccccf8b89836cd192)
- [elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)
- [LLEXT_MEM_COUNT](../llext/P011_扩展管理API.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)
- [peek](../llext/P025_扩展加载器上下文.md#af5452f4b4f1099379d110c1bcd7773f6)
- [elf.h](https://docs.zephyrproject.org/latest/doxygen/html/elf_8h.html)
- [llext.h](../llext/P016_扩展管理头文件.md)
- [llext_loader::storage](../llext/P025_扩展加载器上下文.md#a1b82b69501e174b6a0f24ef356abbf16)
- [llext_loader::seek](../llext/P025_扩展加载器上下文.md#a2376c3774af219972e164b0ee8a6bb6d)
- [llext_loader::read](../llext/P025_扩展加载器上下文.md#a29a16df55b72bc299b338036437f53e0)
- [llext_loader::prepare](../llext/P025_扩展加载器上下文.md#a3034e439e3c55a2ed874cf2db6aba46e)
- [llext_loader::finalize](../llext/P025_扩展加载器上下文.md#a7c0ea7bce0a56ccf98e120a52e362b37)
- [llext_loader::peek](../llext/P025_扩展加载器上下文.md#af5452f4b4f1099379d110c1bcd7773f6)

---

[上一章](P099_zms.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P101_lock.h_源码浏览.md)
