---
id: learning.zephyr-docs.api-source-reference.page-294
title: gnttab.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第294章\_gnttab.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h.html)。

## 294.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00027"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="agroup__xen__grant__tables_html_ga16013267f3a28da2b672e9d8961b0d9d"></a>
<a id="agroup__xen__grant__tables_html_ga39c9410cefe90e66b08c297e32e0282c"></a>
<a id="agroup__xen__grant__tables_html_ga423310c4f8f0ff8f9758e33ab004365e"></a>
<a id="agroup__xen__grant__tables_html_ga4c9b81e0148848d14d1517fcbba4d8e7"></a>
<a id="agroup__xen__grant__tables_html_ga64d478848b93048af3e7de5474cc3c0b"></a>
<a id="agroup__xen__grant__tables_html_gaa36d64f2cd70dedabc2c7a67ddb497a9"></a>
<a id="agroup__xen__grant__tables_html_gadc5dee1df1b16011a6bb4e6975136092"></a>
<a id="agroup__xen__grant__tables_html_gafe3ff541ac6015e39922f34940154724"></a>
<a id="agroup__xen__grant__tables_html_gafedf9bc092852f2fd9f7461b89482634"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/*
 * Copyright (c) 2021-2024 EPAM Systems
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_XEN_GNTTAB_H_
#define ZEPHYR_INCLUDE_XEN_GNTTAB_H_

#include <stdbool.h>
#include <stdint.h>

#include <xen/public/grant_table.h>


grant_ref_t gnttab_grant_access(domid_t domid, unsigned long gfn,
                                bool readonly);

int gnttab_end_access(grant_ref_t gref);

int32_t gnttab_alloc_and_grant(void **map, bool readonly);

void *gnttab_get_pages(unsigned int npages);

int gnttab_put_pages(void *start_addr, unsigned int npages);

int gnttab_map_refs(struct gnttab_map_grant_ref *map_ops, unsigned int count);

int gnttab_unmap_refs(struct gnttab_unmap_grant_ref *unmap_ops, unsigned int count);

int gnttab_query_size(domid_t dom, uint32_t *nr_frames, uint32_t *max_nr_frames,
                      int16_t *status);

const char *gnttabop_error(int16_t status);


#endif /* ZEPHYR_INCLUDE_XEN_GNTTAB_H_ */
```

## 294.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2024 EPAM Systems。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 167 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_XEN_GNTTAB_H_`。

## 294.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [gnttab_grant_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gaa36d64f2cd70dedabc2c7a67ddb497a9)
- [gnttab_end_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga16013267f3a28da2b672e9d8961b0d9d)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [gnttab_alloc_and_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafedf9bc092852f2fd9f7461b89482634)
- [gnttab_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga423310c4f8f0ff8f9758e33ab004365e)
- [gnttab_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga4c9b81e0148848d14d1517fcbba4d8e7)
- [gnttab_map_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga64d478848b93048af3e7de5474cc3c0b)
- [gnttab_unmap_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gadc5dee1df1b16011a6bb4e6975136092)
- [gnttab_query_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga39c9410cefe90e66b08c297e32e0282c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [gnttabop_error](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafe3ff541ac6015e39922f34940154724)

---

[上一章](P293_gnss_publish.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P295_gpio_ambiq.h_源码浏览.md)
