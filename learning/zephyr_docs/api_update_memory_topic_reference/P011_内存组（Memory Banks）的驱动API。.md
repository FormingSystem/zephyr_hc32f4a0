---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-11
title: 内存组（Memory Banks）的驱动API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_内存组（Memory Banks）的驱动API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mm__drv__bank__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

内存组（Memory Banks）的驱动API。

<a id="details"></a>

内存存储体驱动 API（Memory Banks Driver APIs），供系统级内存管理驱动跟踪各存储体（Memory Banks）中的页面使用情况。**注意（Note）：**调用者在使用这些 API 时必须确保正确加锁，以保护数据。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_sys_5Fmm_5Fdrv_5Fbank"></a>

```c
struct sys_mm_drv_bank
```

相关声明：[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

内存组（Memory Banks）的信息。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_gad8f2956ec2346812977abf91506911fb"></a>

```c
void sys_mm_drv_bank_init (struct sys_mm_drv_bank *bank, uint32_t bank_pages)
```

相关声明：[sys_mm_drv_bank_init](#gad8f2956ec2346812977abf91506911fb)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

初始化存储体的数据结构。

<a id="r_ga24f5119ac69d07bdba20fbfb2427939f"></a>

```c
uint32_t sys_mm_drv_bank_page_mapped (struct sys_mm_drv_bank *bank)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sys_mm_drv_bank_page_mapped](#ga24f5119ac69d07bdba20fbfb2427939f)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

跟踪指定存储体中一个内存页的映射（mapping）。

<a id="r_gac1afd8ab934ce15f77de9d3f113cfa43"></a>

```c
uint32_t sys_mm_drv_bank_page_unmapped (struct sys_mm_drv_bank *bank)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sys_mm_drv_bank_page_unmapped](#gac1afd8ab934ce15f77de9d3f113cfa43)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

跟踪指定存储体中一个内存页的解除映射（unmapping）。

<a id="r_ga55404378ab66ef3393e652a57eacc881"></a>

```c
void sys_mm_drv_bank_stats_reset_max (struct sys_mm_drv_bank *bank)
```

相关声明：[sys_mm_drv_bank_stats_reset_max](#ga55404378ab66ef3393e652a57eacc881)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)。

重置该存储体的已映射内存页数最大值。

<a id="r_gaa0ae8be368233f6dfd88a54ae7ae1db0"></a>

```c
void sys_mm_drv_bank_stats_get (struct sys_mm_drv_bank *bank, struct sys_memory_stats *stats)
```

相关声明：[sys_mm_drv_bank_stats_get](#gaa0ae8be368233f6dfd88a54ae7ae1db0)、[sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)、[sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)。

获取指定存储体的内存使用统计（memory usage stats）。

## 11.3\_详细说明（Detailed Documentation）

<a id="gad8f2956ec2346812977abf91506911fb"></a>

### `sys_mm_drv_bank_init()`

```c
void sys_mm_drv_bank_init ( struct sys_mm_drv_bank * bank, uint32_t bank_pages )
```

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

初始化存储体的数据结构。

驱动可能需要跟踪所用内存存储体（Memory Banks）的各种信息。本函数初始化保存这些信息的通用结构体。由于上电时所有存储体均已开启，初始化时将所有页面视为已映射（Mapped）；在后续驱动初始化阶段，会取消未使用页面的映射。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] bank` | 指向用于跟踪的内存存储体结构体的指针。 |
| `[in] bank_pages` | 内存存储体（Memory Bank）中的页面数量。 |

<a id="ga24f5119ac69d07bdba20fbfb2427939f"></a>

### `sys_mm_drv_bank_page_mapped()`

```c
uint32_t sys_mm_drv_bank_page_mapped ( struct sys_mm_drv_bank * bank)
```

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

跟踪指定存储体中一个内存页的映射（mapping）。

本函数更新指定内存存储体中已映射页面（Mapped Pages）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] bank` | 指向内存存储体数据结构的指针。 |

**返回（Returns）**：**返回值（Returns）：**内存存储体中已映射页面（Mapped Pages）的数量。

<a id="gac1afd8ab934ce15f77de9d3f113cfa43"></a>

### `sys_mm_drv_bank_page_unmapped()`

```c
uint32_t sys_mm_drv_bank_page_unmapped ( struct sys_mm_drv_bank * bank)
```

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

跟踪指定存储体中一个内存页的解除映射（unmapping）。

本函数更新指定内存存储体中未映射页面（Unmapped Pages）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] bank` | 指向内存存储体数据结构的指针。 |

**返回（Returns）**：**返回值（Returns）：**内存存储体中未映射页面（Unmapped Pages）的数量。

<a id="gaa0ae8be368233f6dfd88a54ae7ae1db0"></a>

### `sys_mm_drv_bank_stats_get()`

```c
void sys_mm_drv_bank_stats_get ( struct sys_mm_drv_bank * bank, struct sys_memory_stats * stats )
```

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

获取指定存储体的内存使用统计（memory usage stats）。

本函数从内存存储体提取系统内存统计（System Memory Statistics）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] bank` | 指向内存存储体数据结构的指针。 |
| `[in,out] stats` | 指向接收系统内存统计副本的内存的指针。 |

<a id="ga55404378ab66ef3393e652a57eacc881"></a>

### `sys_mm_drv_bank_stats_reset_max()`

```c
void sys_mm_drv_bank_stats_reset_max ( struct sys_mm_drv_bank * bank)
```

```c
#include <zephyr/drivers/mm/mm_drv_bank.h>
```

重置该存储体的已映射内存页数最大值。

本函数将指定内存存储体的已映射页面数最大值，重置为该存储体当前的已映射页面数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] bank` | 指向内存存储体数据结构的指针。 |


## 11.4\_原页交叉引用（Cross References）

- [sys_mm_drv_bank](../kernel_runtime_model_reference/P017_sys_mm_drv_bank_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [sys_memory_stats](../lowheap_reference/P005_内存统计结构.md)
- [zephyr/drivers/mm/mm_drv_bank.h](../api_file_management_reference/P034_zephyr__drivers__mm__mm_drv_bank.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_映像管理回调（Image Management Callbacks）.md) · [返回大纲](大纲.md) · [下一章](P012_调制解调器点对点协议（Modem PPP）.md)
