---
id: learning.zephyr-docs.api-source-configuration-reference.page-28
title: heap_kasan.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_heap\_kasan.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h.html)。

## 28.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00033"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="foldopen00091"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="foldopen00123"></a>
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
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="abitarray_8h_html"></a>
<a id="agroup__bitarray__apis_html_ga168a1da9ac2bee523bdc9778e94fd841"></a>
<a id="agroup__heap__kasan__apis_html_ga34f66dfa0f04034e756a4c2474a03f1b"></a>
<a id="agroup__heap__kasan__apis_html_gad2cbd504b82b27ecf48eba519fc8c9ab"></a>
<a id="ainit_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astructsys__heap_html"></a>
<a id="asys__heap_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SYS_HEAP_KASAN_H_
#define ZEPHYR_INCLUDE_SYS_HEAP_KASAN_H_

#include <stdint.h>
#include <stddef.h>
#include <zephyr/sys/sys_heap.h>
#include <zephyr/sys/bitarray.h>
#include <zephyr/toolchain.h>
#include <zephyr/init.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_SYS_HEAP_KASAN) || defined(__DOXYGEN__)


#define SYS_HEAP_KASAN_GRANULE             ((size_t)CONFIG_SYS_HEAP_KASAN_GRANULE)

#define SYS_HEAP_KASAN_SHADOW_BITS(_sz)    ((_sz) / SYS_HEAP_KASAN_GRANULE)
#define SYS_HEAP_KASAN_SHADOW_BUNDLES(_sz) DIV_ROUND_UP(SYS_HEAP_KASAN_SHADOW_BITS(_sz), 32)

void heap_kasan_report(uintptr_t addr, size_t size);

void heap_kasan_register(struct sys_heap *heap, sys_bitarray_t *ba);

#define SYS_HEAP_KASAN_ENABLE(_heap_name, _heap_sz) \
        static uint32_t \
                _heap_name##_kasan_bundles[SYS_HEAP_KASAN_SHADOW_BUNDLES(_heap_sz)] __noinit \
                __aligned(4); \
        static sys_bitarray_t _heap_name##_kasan_ba = { \
                .num_bits = SYS_HEAP_KASAN_SHADOW_BITS(_heap_sz), \
                .num_bundles = SYS_HEAP_KASAN_SHADOW_BUNDLES(_heap_sz), \
                .bundles = _heap_name##_kasan_bundles, \
        }; \
        static int _heap_name##_kasan_init_fn(void) \
        { \
                heap_kasan_register(&(_heap_name), &_heap_name##_kasan_ba); \
                return 0; \
        } \
        SYS_INIT(_heap_name##_kasan_init_fn, PRE_KERNEL_1, 0)

#define K_HEAP_KASAN_ENABLE(_heap_name, _heap_sz) \
        static uint32_t _heap_name##_kasan_bundles[SYS_HEAP_KASAN_SHADOW_BUNDLES( \
                MAX(_heap_sz, Z_HEAP_MIN_SIZE))] __noinit __aligned(4); \
        static sys_bitarray_t _heap_name##_kasan_ba = { \
                .num_bits = SYS_HEAP_KASAN_SHADOW_BITS(MAX(_heap_sz, Z_HEAP_MIN_SIZE)), \
                .num_bundles = SYS_HEAP_KASAN_SHADOW_BUNDLES(MAX(_heap_sz, Z_HEAP_MIN_SIZE)), \
                .bundles = _heap_name##_kasan_bundles, \
        }; \
        static int _heap_name##_kasan_init_fn(void) \
        { \
                heap_kasan_register(&(_heap_name).heap, &_heap_name##_kasan_ba); \
                return 0; \
        } \
        SYS_INIT(_heap_name##_kasan_init_fn, PRE_KERNEL_1, 0)


#else                                              /* !CONFIG_SYS_HEAP_KASAN */

#define SYS_HEAP_KASAN_ENABLE(_heap_name, _heap_sz) /* no-op */
#define K_HEAP_KASAN_ENABLE(_heap_name, _heap_sz)   /* no-op */

#endif /* CONFIG_SYS_HEAP_KASAN */

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_HEAP_KASAN_H_ */
```

## 28.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© Qualcomm Technologies, Inc. and/or its subsidiaries.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 140 行

条件编译表达式：`!CONFIG_SYS_HEAP_KASAN`。

### 注释 3：原第 143 行

空操作（No-op）。

### 注释 4：原第 144 行

空操作（No-op）。

### 注释 5：原第 147 行

条件编译配置（Configuration）标记：`CONFIG_SYS_HEAP_KASAN`。

### 注释 6：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_HEAP_KASAN_H_`。

## 28.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/heap__kasan_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/sys_heap.h](../lowheap_reference/P011_底层堆头文件参考.md)
- [zephyr/sys/bitarray.h](../bitarray_reference/P002_位数组头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [zephyr/init.h](../device_reference/P009_系统初始化头文件参考.md)
- [heap_kasan_report](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#ga34f66dfa0f04034e756a4c2474a03f1b)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [heap_kasan_register](https://docs.zephyrproject.org/latest/doxygen/html/group__heap__kasan__apis.html#gad2cbd504b82b27ecf48eba519fc8c9ab)
- [sys_heap](../lowheap_reference/P004_底层堆对象.md)
- [sys_bitarray_t](../bitarray_reference/P001_位数组公共接口.md#ga168a1da9ac2bee523bdc9778e94fd841)
- [bitarray.h](../bitarray_reference/P002_位数组头文件参考.md)
- [init.h](../device_reference/P009_系统初始化头文件参考.md)
- [sys_heap.h](../lowheap_reference/P011_底层堆头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P027_ft8xx_reference_api.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P029_hl7800.h_源码浏览.md)
