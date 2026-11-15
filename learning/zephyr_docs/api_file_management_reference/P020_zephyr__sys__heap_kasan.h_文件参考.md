---
id: learning.zephyr-docs.api-file-management-reference.page-20
title: zephyr__sys__heap_kasan.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_sys\_\_heap\_kasan.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

轻量级堆写入地址检测器（Heap KASAN）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/sys/sys_heap.h>
#include <zephyr/sys/bitarray.h>
#include <zephyr/toolchain.h>
#include <zephyr/init.h>
```

查看此文件的源码。

轻量级堆写入地址检测器（Heap KASAN）的API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_ga9bd0af55bae901bbea20e064d6171ee2"></a>

```c
#define SYS_HEAP_KASAN_SHADOW_BITS(_sz)
```

相关声明：[SYS_HEAP_KASAN_SHADOW_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga9bd0af55bae901bbea20e064d6171ee2)。

大小为 `_sz` 字节的堆所需的影子位（shadow bits），每个粒度单元（granule）对应一位。

<a id="r_ga2714e1169d119a8e50265d2bced8d005"></a>

```c
#define SYS_HEAP_KASAN_SHADOW_BUNDLES(_sz)
```

相关声明：[SYS_HEAP_KASAN_SHADOW_BUNDLES](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga2714e1169d119a8e50265d2bced8d005)。

大小为 `_sz` 字节的堆，其影子存储所需的 `uint32_t` 组数（bundle count）。

<a id="r_ga413c090cc09658ebc9b16406cd25558a"></a>

```c
#define SYS_HEAP_KASAN_ENABLE(_heap_name, _heap_sz)
```

相关声明：[SYS_HEAP_KASAN_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga413c090cc09658ebc9b16406cd25558a)。

对 `struct sys_heap` 启用内核地址消毒器（KASAN）的影子跟踪（shadow tracking）。

<a id="r_ga0dc8b79da83fe6799e3c2c3b08b8c15b"></a>

```c
#define K_HEAP_KASAN_ENABLE(_heap_name, _heap_sz)
```

相关声明：[K_HEAP_KASAN_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga0dc8b79da83fe6799e3c2c3b08b8c15b)。

对 `struct k_heap`（`K_HEAP_DEFINE`）启用 KASAN 影子跟踪。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.2\_函数（Functions）

<a id="r_ga34f66dfa0f04034e756a4c2474a03f1b"></a>

```c
void heap_kasan_report (uintptr_t addr, size_t size)
```

相关声明：[heap_kasan_report](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga34f66dfa0f04034e756a4c2474a03f1b)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

报告堆的 KASAN 违规（violation）。

<a id="r_gad2cbd504b82b27ecf48eba519fc8c9ab"></a>

```c
void heap_kasan_register (struct sys_heap *heap, sys_bitarray_t *ba)
```

相关声明：[heap_kasan_register](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#gad2cbd504b82b27ecf48eba519fc8c9ab)、[sys_heap](../lowheap_reference/P004_底层堆对象.md)、[sys_bitarray_t](../bitarray_reference/P001_位数组公共接口.md#ga168a1da9ac2bee523bdc9778e94fd841)。

将影子位数组（shadow bitarray）与堆关联，以进行 KASAN 跟踪。


## 20.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/sys_heap.h](../lowheap_reference/P012_底层堆头文件源码.md)
- [zephyr/sys/bitarray.h](../memory_source_reference/P001_位数组头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/init.h](../device_reference/P010_系统初始化头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P028_heap_kasan.h_源码浏览.md)
- [SYS_HEAP_KASAN_SHADOW_BITS](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga9bd0af55bae901bbea20e064d6171ee2)
- [SYS_HEAP_KASAN_SHADOW_BUNDLES](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga2714e1169d119a8e50265d2bced8d005)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [SYS_HEAP_KASAN_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga413c090cc09658ebc9b16406cd25558a)
- [sys_heap](../lowheap_reference/P004_底层堆对象.md)
- [K_HEAP_KASAN_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga0dc8b79da83fe6799e3c2c3b08b8c15b)
- [k_heap](../heap_reference/P002_内核堆结构.md)
- [heap_kasan_report](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga34f66dfa0f04034e756a4c2474a03f1b)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)
- [heap_kasan_register](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#gad2cbd504b82b27ecf48eba519fc8c9ab)
- [sys_bitarray_t](../bitarray_reference/P001_位数组公共接口.md#ga168a1da9ac2bee523bdc9778e94fd841)

<a id="header-details"></a>

---

[上一章](P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__net__hostname.h_文件参考.md)
