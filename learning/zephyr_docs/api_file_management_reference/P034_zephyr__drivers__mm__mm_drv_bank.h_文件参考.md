---
id: learning.zephyr-docs.api-file-management-reference.page-34
title: zephyr__drivers__mm__mm_drv_bank.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_drivers\_\_mm\_\_mm\_drv\_bank.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mm__drv__bank_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存组（Memory Banks）的驱动API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/mem_stats.h>
#include <stdint.h>
```

查看此文件的源码。

存储体驱动 API（Memory Banks Driver APIs）。这些通用 API 供系统级内存管理驱动使用，用于跟踪各存储体（memory banks）内部的内存页使用情况。注意：调用方使用这些 API 时，需要确保通过适当的锁定来保护数据。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 34.1\_数据结构（Data Structures）

<a id="r_sys_5Fmm_5Fdrv_5Fbank"></a>

```c
struct sys_mm_drv_bank
```

相关声明：[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

内存组（Memory Banks）的信息。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.2\_函数（Functions）

<a id="r_gad8f2956ec2346812977abf91506911fb"></a>

```c
void sys_mm_drv_bank_init (struct sys_mm_drv_bank *bank, uint32_t bank_pages)
```

相关声明：[sys_mm_drv_bank_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gad8f2956ec2346812977abf91506911fb)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化存储体的数据结构。

<a id="r_ga24f5119ac69d07bdba20fbfb2427939f"></a>

```c
uint32_t sys_mm_drv_bank_page_mapped (struct sys_mm_drv_bank *bank)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sys_mm_drv_bank_page_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga24f5119ac69d07bdba20fbfb2427939f)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

跟踪指定存储体中一个内存页的映射（mapping）。

<a id="r_gac1afd8ab934ce15f77de9d3f113cfa43"></a>

```c
uint32_t sys_mm_drv_bank_page_unmapped (struct sys_mm_drv_bank *bank)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sys_mm_drv_bank_page_unmapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gac1afd8ab934ce15f77de9d3f113cfa43)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

跟踪指定存储体中一个内存页的解除映射（unmapping）。

<a id="r_ga55404378ab66ef3393e652a57eacc881"></a>

```c
void sys_mm_drv_bank_stats_reset_max (struct sys_mm_drv_bank *bank)
```

相关声明：[sys_mm_drv_bank_stats_reset_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga55404378ab66ef3393e652a57eacc881)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

重置该存储体的已映射内存页数最大值。

<a id="r_gaa0ae8be368233f6dfd88a54ae7ae1db0"></a>

```c
void sys_mm_drv_bank_stats_get (struct sys_mm_drv_bank *bank, struct sys_memory_stats *stats)
```

相关声明：[sys_mm_drv_bank_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gaa0ae8be368233f6dfd88a54ae7ae1db0)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)、[sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)。

获取指定存储体的内存使用统计（memory usage stats）。


## 34.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/mem_stats.h](../lowheap_reference/P020_内存统计头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P535_mm_drv_bank.h_源码浏览.md)
- [sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)
- [sys_mm_drv_bank_init](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gad8f2956ec2346812977abf91506911fb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sys_mm_drv_bank_page_mapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga24f5119ac69d07bdba20fbfb2427939f)
- [sys_mm_drv_bank_page_unmapped](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gac1afd8ab934ce15f77de9d3f113cfa43)
- [sys_mm_drv_bank_stats_reset_max](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#ga55404378ab66ef3393e652a57eacc881)
- [sys_mm_drv_bank_stats_get](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html#gaa0ae8be368233f6dfd88a54ae7ae1db0)
- [sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)

<a id="header-details"></a>

---

[上一章](P033_zephyr__drivers__mfd__tle9104.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__modem__stats.h_文件参考.md)
