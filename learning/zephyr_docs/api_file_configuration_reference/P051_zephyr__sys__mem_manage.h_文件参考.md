---
id: learning.zephyr-docs.api-file-configuration-reference.page-51
title: zephyr__sys__mem_manage.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_zephyr\_\_sys\_\_mem\_manage.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mem__manage_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存管理辅助接口（Memory Management Helpers）。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
```

查看此文件的源码。

内存管理辅助接口（Memory Management Helpers）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 51.1\_函数（Functions）

<a id="r_gaef71defc60c1d898d5ece56c6826a2e1"></a>

```c
bool sys_mm_is_phys_addr_in_range (uintptr_t phys)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sys_mm_is_phys_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#gaef71defc60c1d898d5ece56c6826a2e1)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

检查物理地址（Physical Address）是否位于物理内存（Physical Memory）的范围内。

<a id="r_ga1a4b707eae142c8f871a198b865e3d16"></a>

```c
bool sys_mm_is_virt_addr_in_range (void *virt)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sys_mm_is_virt_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#ga1a4b707eae142c8f871a198b865e3d16)。

检查虚拟地址（Virtual Address）是否位于虚拟内存（Virtual Memory）的范围内。


## 51.2\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P110_mem_manage.h_源码浏览.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [sys_mm_is_phys_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#gaef71defc60c1d898d5ece56c6826a2e1)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [sys_mm_is_virt_addr_in_range](https://docs.zephyrproject.org/latest/doxygen/html/group__memory__management.html#ga1a4b707eae142c8f871a198b865e3d16)

<a id="header-details"></a>

---

[上一章](P050_zephyr__drivers__flash__mchp_nvmctrl_g2.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P052_zephyr__drivers__mfd__bd8lb600fs.h_文件参考.md)
