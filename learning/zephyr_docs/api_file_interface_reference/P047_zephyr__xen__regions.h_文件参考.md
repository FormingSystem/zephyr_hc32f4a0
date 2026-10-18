---
id: learning.zephyr-docs.api-file-interface-reference.page-47
title: zephyr__xen__regions.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regions_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_xen\_\_regions.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/regions_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Xen扩展区域管理（Extended Region Management）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stddef.h>
```

查看此文件的源码。

Xen扩展区域管理（Extended Region Management）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.1\_函数（Functions）

<a id="r_gabe293a88ca167b9a52709c7e94af73b3"></a>

```c
bool xen_region_is_addr_extreg (void *ptr)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[xen_region_is_addr_extreg](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gabe293a88ca167b9a52709c7e94af73b3)。

检查地址是否属于已配置的扩展区域（extended region）。

<a id="r_ga4853ade09ca37b66ad484ad1cbab6cf3"></a>

```c
void * xen_region_get_pages (size_t nr_pages)
```

相关声明：[xen_region_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga4853ade09ca37b66ad484ad1cbab6cf3)。

从扩展区域分配一个或多个连续内存页（contiguous pages）。

<a id="r_gaa82b399b305dc279da8fb8206da77d3b"></a>

```c
int xen_region_put_pages (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaa82b399b305dc279da8fb8206da77d3b)。

释放先前从扩展区域分配的内存页。

<a id="r_ga65b8fda79f7b6e4db26cccc818c69c79"></a>

```c
int xen_region_map (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_map](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga65b8fda79f7b6e4db26cccc818c69c79)。

将扩展区域的缓冲区映射到内核地址空间（kernel address space）。

<a id="r_gaf576c75a5b01b1a8b6f2be3b48a25886"></a>

```c
int xen_region_unmap (void *ptr, size_t nr_pages)
```

相关声明：[xen_region_unmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaf576c75a5b01b1a8b6f2be3b48a25886)。

从内核地址空间解除扩展区域缓冲区的映射。


## 47.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P699_regions.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [xen_region_is_addr_extreg](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gabe293a88ca167b9a52709c7e94af73b3)
- [xen_region_get_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga4853ade09ca37b66ad484ad1cbab6cf3)
- [xen_region_put_pages](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaa82b399b305dc279da8fb8206da77d3b)
- [xen_region_map](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#ga65b8fda79f7b6e4db26cccc818c69c79)
- [xen_region_unmap](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__regions.html#gaf576c75a5b01b1a8b6f2be3b48a25886)

<a id="header-details"></a>

---

[上一章](P046_zephyr__dt-bindings__gpio__realtek-bee-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__dt-bindings__gpio__renesas-rz-gpio.h_文件参考.md)
