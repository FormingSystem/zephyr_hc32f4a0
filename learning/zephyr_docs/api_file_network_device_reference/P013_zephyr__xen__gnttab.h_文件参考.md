---
id: learning.zephyr-docs.api-file-network-device-reference.page-13
title: zephyr__xen__gnttab.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_xen\_\_gnttab.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gnttab_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen授权表（Grant Table）的辅助接口。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <xen/public/grant_table.h>
```

查看此文件的源码。

Xen授权表（Grant Table）的辅助接口。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.1\_函数（Functions）

<a id="r_gaa36d64f2cd70dedabc2c7a67ddb497a9"></a>

```c
grant_ref_t gnttab_grant_access (domid_t domid, unsigned long gfn, bool readonly)
```

相关声明：[gnttab_grant_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gaa36d64f2cd70dedabc2c7a67ddb497a9)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

授予另一个域（Domain）访问客户机页帧（Guest Frame）的权限。

<a id="r_ga16013267f3a28da2b672e9d8961b0d9d"></a>

```c
int gnttab_end_access (grant_ref_t gref)
```

相关声明：[gnttab_end_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga16013267f3a28da2b672e9d8961b0d9d)。

释放由 `gnttab_grant_access()` 创建的授权引用（Grant Reference）。

<a id="r_gafedf9bc092852f2fd9f7461b89482634"></a>

```c
int32_t gnttab_alloc_and_grant (void **map, bool readonly)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[gnttab_alloc_and_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafedf9bc092852f2fd9f7461b89482634)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

分配页面并立即授予其访问权限（Grant Access）。

<a id="r_ga423310c4f8f0ff8f9758e33ab004365e"></a>

```c
void * gnttab_get_pages (unsigned int npages)
```

相关声明：[gnttab_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga423310c4f8f0ff8f9758e33ab004365e)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

分配可承载授权映射（Grant Mappings）的页面。

<a id="r_ga4c9b81e0148848d14d1517fcbba4d8e7"></a>

```c
int gnttab_put_pages (void *start_addr, unsigned int npages)
```

相关声明：[gnttab_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga4c9b81e0148848d14d1517fcbba4d8e7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

释放由 `gnttab_get_pages()` 分配的页面。

<a id="r_ga64d478848b93048af3e7de5474cc3c0b"></a>

```c
int gnttab_map_refs (struct gnttab_map_grant_ref *map_ops, unsigned int count)
```

相关声明：[gnttab_map_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga64d478848b93048af3e7de5474cc3c0b)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

映射一个或多个其他域的授权引用（Foreign Grant References）。

<a id="r_gadc5dee1df1b16011a6bb4e6975136092"></a>

```c
int gnttab_unmap_refs (struct gnttab_unmap_grant_ref *unmap_ops, unsigned int count)
```

相关声明：[gnttab_unmap_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gadc5dee1df1b16011a6bb4e6975136092)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

取消一个或多个其他域授权引用（Foreign Grant References）的映射。

<a id="r_ga39c9410cefe90e66b08c297e32e0282c"></a>

```c
int gnttab_query_size (domid_t dom, uint32_t *nr_frames, uint32_t *max_nr_frames, int16_t *status)
```

相关声明：[gnttab_query_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga39c9410cefe90e66b08c297e32e0282c)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

查询某个域（Domain）的当前和最大授权表大小（Grant Table Size）。

<a id="r_gafe3ff541ac6015e39922f34940154724"></a>

```c
const char * gnttabop_error (int16_t status)
```

相关声明：[gnttabop_error](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafe3ff541ac6015e39922f34940154724)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

将 Xen 授权表状态（Grant-table Status）转换为可读文本。


## 13.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P294_gnttab.h_源码浏览.md)
- [gnttab_grant_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gaa36d64f2cd70dedabc2c7a67ddb497a9)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [gnttab_end_access](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga16013267f3a28da2b672e9d8961b0d9d)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [gnttab_alloc_and_grant](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafedf9bc092852f2fd9f7461b89482634)
- [gnttab_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga423310c4f8f0ff8f9758e33ab004365e)
- [gnttab_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga4c9b81e0148848d14d1517fcbba4d8e7)
- [gnttab_map_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga64d478848b93048af3e7de5474cc3c0b)
- [gnttab_unmap_refs](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gadc5dee1df1b16011a6bb4e6975136092)
- [gnttab_query_size](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#ga39c9410cefe90e66b08c297e32e0282c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [gnttabop_error](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__grant__tables.html#gafe3ff541ac6015e39922f34940154724)

<a id="header-details"></a>

---

[上一章](P012_zephyr__bluetooth__audio__gmap.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__bluetooth__hci_pkt.h_文件参考.md)
