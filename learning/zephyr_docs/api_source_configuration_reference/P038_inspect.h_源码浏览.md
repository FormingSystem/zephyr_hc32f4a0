---
id: learning.zephyr-docs.api-source-configuration-reference.page-38
title: inspect.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_inspect.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h.html)。

## 38.1\_原始可见代码（Source Code）

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
<a id="l00031"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="agroup__llext__apis_html_ga9258a6fe4a45aa5dd48c80c7aa07b953"></a>
<a id="agroup__llext__apis_html_gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265"></a>
<a id="agroup__llext__elf_html_gab3695edd628cf868dc4f0d618f86bcbd"></a>
<a id="agroup__llext__inspect__apis_html_ga23121962662f057da004ac1c527716e3"></a>
<a id="agroup__llext__inspect__apis_html_ga655023e915eb0ef60e76c0c1625c63c9"></a>
<a id="agroup__llext__inspect__apis_html_gabef549f07291126f39b5065be3f73599"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="allext_8h_html"></a>
<a id="allext__internal_8h_html"></a>
<a id="aloader_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructllext__loader_html"></a>
<a id="astructllext_html"></a>
<a id="astructllext_html_a47cfcb60d773a6c16d2fda8cc5011a16"></a>
<a id="astructllext_html_ae9d529433f30ed659758c9b29c9b96bd"></a>

```c
/*
 * Copyright (c) 2025 Arduino SA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LLEXT_INSPECT_H_
#define ZEPHYR_INCLUDE_LLEXT_INSPECT_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>
#include <zephyr/llext/llext.h>
#include <zephyr/llext/loader.h>
#include <zephyr/llext/llext_internal.h>


static inline int llext_get_region_info(const struct llext_loader *ldr,
                                        const struct llext *ext,
                                        enum llext_mem region,
                                        const elf_shdr_t **hdr,
                                        const void **addr, size_t *size)
{
        if ((unsigned int)region >= LLEXT_MEM_COUNT) {
                return -EINVAL;
        }

        if (hdr) {
                *hdr = &ldr->sects[region];
        }

        /* address and size compensated for alignment prepad */
        if (addr) {
                *addr = (void *)((uintptr_t)ext->mem[region] + ldr->sects[region].sh_info);
        }
        if (size) {
                *size = ext->mem_size[region] - ldr->sects[region].sh_info;
        }

        return 0;
}

int llext_section_shndx(const struct llext_loader *ldr, const struct llext *ext,
                            const char *section_name);

static inline int llext_get_section_info(const struct llext_loader *ldr,
                                         const struct llext *ext,
                                         unsigned int shndx,
                                         const elf_shdr_t **hdr,
                                         enum llext_mem *region,
                                         size_t *offset)
{
        if (shndx < 0 || shndx >= ext->sect_cnt) {
                return -EINVAL;
        }
        if (!ldr->sect_map) {
                return -ENOTSUP;
        }

        enum llext_mem mem_idx = ldr->sect_map[shndx].mem_idx;

        if (hdr) {
                *hdr = &ext->sect_hdrs[shndx];
        }
        if (region) {
                *region = mem_idx;
        }

        /* offset compensated for alignment prepad */
        if (offset) {
                if (ldr->sect_map[shndx].detached) {
                        *offset = (size_t)-1;
                } else {
                        *offset = ldr->sect_map[shndx].offset - ldr->sects[mem_idx].sh_info;
                }
        }

        return 0;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_LLEXT_INSPECT_H_ */
```

## 38.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Arduino SA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

已补偿对齐前置填充（Alignment prepad）的地址和大小。

### 注释 3：原第 133 行

已补偿对齐前置填充（Alignment prepad）的偏移量。

### 注释 4：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_INSPECT_H_`。

## 38.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/inspect_8h.html)
- [zephyr/llext/llext.h](../llext/P016_扩展管理头文件.md)
- [zephyr/llext/loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [zephyr/llext/llext_internal.h](../llext/P018_扩展内部头文件.md)
- [llext_get_region_info](../llext/P013_ELF检查API.md#gabef549f07291126f39b5065be3f73599)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [llext](../llext/P020_扩展对象.md)
- [llext_mem](../llext/P011_扩展管理API.md#ga9258a6fe4a45aa5dd48c80c7aa07b953)
- [elf_shdr_t](../llext/P012_ELF常量与类型.md#gab3695edd628cf868dc4f0d618f86bcbd)
- [LLEXT_MEM_COUNT](../llext/P011_扩展管理API.md#gga9258a6fe4a45aa5dd48c80c7aa07b953ad6b134939dea35076a41f9c0b81f9265)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [mem](../llext/P020_扩展对象.md#ae9d529433f30ed659758c9b29c9b96bd)
- [mem_size](../llext/P020_扩展对象.md#a47cfcb60d773a6c16d2fda8cc5011a16)
- [llext_section_shndx](../llext/P013_ELF检查API.md#ga655023e915eb0ef60e76c0c1625c63c9)
- [llext_get_section_info](../llext/P013_ELF检查API.md#ga23121962662f057da004ac1c527716e3)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)
- [llext.h](../llext/P016_扩展管理头文件.md)
- [llext_internal.h](../llext/P018_扩展内部头文件.md)
- [loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [llext::mem_size](../llext/P020_扩展对象.md#a47cfcb60d773a6c16d2fda8cc5011a16)
- [llext::mem](../llext/P020_扩展对象.md#ae9d529433f30ed659758c9b29c9b96bd)

---

[上一章](P037_input_kbd_matrix.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P039_intc_rx_icu.h_源码浏览.md)
