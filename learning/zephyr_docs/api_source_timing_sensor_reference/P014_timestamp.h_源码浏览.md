---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-14
title: timestamp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/timestamp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_timestamp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/timestamp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md)。

## 14.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00033"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00053"></a>
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
<a id="foldopen00070"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
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
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="agroup__clock__apis_html_ga2180f263d149841a7c1fde663edb84c5"></a>
<a id="agroup__clock__apis_html_ga222f9dff749accf8de62bc4b52c7bdcd"></a>
<a id="agroup__clock__apis_html_ga2d66311052e2bddf914610fb7345ff27"></a>
<a id="agroup__clock__apis_html_gad748b2fe83b36884dc087b4af367de80"></a>
<a id="agroup__timeutil__unit__apis_html_ga665d5fc98ffe8bd1cf78ca994f58724a"></a>
<a id="akernel_8h_html"></a>
<a id="alimits_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="atest__asm__inline__gcc_8h_html"></a>
<a id="atest__asm__inline__other_8h_html"></a>
<a id="atest__asm__inline__other_8h_html_ab755b5736ce6118734809b04fe3798b5"></a>
<a id="atimestamp_8h_html_a1b4134f508183af47ef3deff07be4a54"></a>
<a id="atimestamp_8h_html_a2503eba6a8f75337fe8c7ee84b0b3b21"></a>
<a id="atimestamp_8h_html_a54d527f8fde477822ad2044579a7edd3"></a>
<a id="atimestamp_8h_html_a5a399603fca75f3004d45720f03f9d44"></a>
<a id="atimestamp_8h_html_a6555ffaf6ca7b4f5b81477faa8f43f53"></a>
<a id="atimestamp_8h_html_a7d2ae16b9d290b7ab914f71155c5e56d"></a>
<a id="atimestamp_8h_html_a95c5be89ea7bce90d2a8a11472ebd2c6"></a>
<a id="atimestamp_8h_html_abb03327df49c0544f863a239a9af0086"></a>
<a id="atimestamp_8h_html_ac476d41973f921a386c9a8341296dcfd"></a>

```c
/*
 * Copyright (c) 2012-2015 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

/*
 * @file macros for measuring time in benchmarking tests
 *
 * This file contains the macros for taking and converting time for
 * benchmarking tests.
 */

#ifndef _TIMESTAMP_H_
#define _TIMESTAMP_H_
#include <zephyr/kernel.h>

#include <limits.h>
#if defined(__GNUC__)
#include <zephyr/test_asm_inline_gcc.h>
#else
#include <zephyr/test_asm_inline_other.h>
#endif


#define TICK_SYNCH()  k_sleep(K_TICKS(1))

#define OS_GET_TIME() k_cycle_get_32()

/* time necessary to read the time */
extern uint32_t tm_off;

static inline uint32_t TIME_STAMP_DELTA_GET(uint32_t ts)
{
        uint32_t t;

        /* serialize so OS_GET_TIME() is not reordered */
        timestamp_serialize();

        t = OS_GET_TIME();
        uint32_t res = (t >= ts) ? (t - ts) : (ULONG_MAX - ts + t);

        if (ts > 0) {
                res -= tm_off;
        }
        return res;
}

/*
 * Routine initializes the benchmark timing measurement
 * The function sets up the global variable tm_off
 */
static inline void bench_test_init(void)
{
        uint32_t t = OS_GET_TIME();

        tm_off = OS_GET_TIME() - t;
}


/* timestamp for checks */
static int64_t timestamp_check;

/*
 * Routines are invoked before and after the benchmark and check
 * if benchmarking code took less time than necessary for the
 * high precision timer register overflow.
 * Functions modify the timestamp_check global variable.
 */
static inline void bench_test_start(void)
{
        timestamp_check = 0;
        /* before reading time we synchronize to the start of the timer tick */
        TICK_SYNCH();
        timestamp_check = k_uptime_delta(&timestamp_check);
}


/* returns 0 if the completed within a second and -1 if not */
static inline int bench_test_end(void)
{
        timestamp_check = k_uptime_delta(&timestamp_check);

        /* Flag an error if the test ran for more than a second.
         * (Note: Existing benchmarks have CONFIG_SYS_CLOCK_TICKS_PER_SEC=1 set,
         * in such configs this check can be an indicator of whether
         * timer tick interrupt overheads too are getting accounted towards
         * benchmark time)
         */
        if (timestamp_check >= MSEC_PER_SEC) {
                return -1;
        }
        return 0;
}

/*
 * Returns -1 if number of ticks cause high precision timer counter
 * overflow and 0 otherwise
 * Called after bench_test_end to see if we still can use timing
 * results or is it completely invalid
 */
static inline int high_timer_overflow(void)
{
        /* Check if the time elapsed in msec is sufficient to trigger an
         *  overflow of the high precision timer
         */
        if (timestamp_check >= (k_cyc_to_ns_floor64(UINT_MAX) /
                                (NSEC_PER_USEC * USEC_PER_MSEC))) {
                return -1;
        }
        return 0;
}

#endif /* _TIMESTAMP_H_ */
```

## 14.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2012-2015 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 7 行

@file 基准测试（benchmarking tests）中的时间测量宏。

本文件包含用于在基准测试中获取时间和转换时间的宏。

### 注释 3：原第 30 行

读取时间所需的时间开销。

### 注释 4：原第 37 行

执行串行化（serialize），以免 `OS_GET_TIME()` 被重排序（reordered）。

### 注释 5：原第 49 行

此例程初始化基准测试计时测量（benchmark timing measurement），设置全局变量 `tm_off`。

### 注释 6：原第 61 行

用于检查的时间戳（timestamp）。

### 注释 7：原第 64 行

这些例程在基准测试之前和之后调用，检查基准测试代码所耗时间是否短于高精度定时器寄存器溢出所需时间。函数会修改全局变量 `timestamp_check`。

### 注释 8：原第 73 行

读取时间之前，先同步到定时器节拍（timer tick）的起点。

### 注释 9：原第 79 行

若在一秒内完成则返回 0，否则返回 -1。

### 注释 10：原第 84 行

若测试运行超过一秒，则标记错误。注意：现有基准测试将 `CONFIG_SYS_CLOCK_TICKS_PER_SEC=1`；在这种配置下，此检查可用于判断定时器节拍中断（timer tick interrupt）的开销是否也被计入基准测试时间。

### 注释 11：原第 96 行

如果节拍数量会造成高精度定时器计数器溢出，则返回 -1，否则返回 0。在 `bench_test_end` 之后调用，以判断计时结果是否仍可使用，还是已经完全无效。

### 注释 12：原第 104 行

检查经过的时间（以毫秒表示）是否足以触发高精度定时器溢出（overflow）。

### 注释 13：原第 114 行

头文件保护宏（Header guard）标记：`_TIMESTAMP_H_`。

## 14.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [limits.h](../api_file_reference/P189_____w__zephyr__zephyr__lib__libc__minimal__include__limits.h_文件参考.md)
- [zephyr/test_asm_inline_gcc.h](../api_file_reference/P484_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_gcc.h_文件参考.md)
- [zephyr/test_asm_inline_other.h](../api_file_reference/P485_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_other.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tm_off](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a2503eba6a8f75337fe8c7ee84b0b3b21)
- [TIME_STAMP_DELTA_GET](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#abb03327df49c0544f863a239a9af0086)
- [timestamp_serialize](../api_file_reference/P485_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_other.h_文件参考.md#ab755b5736ce6118734809b04fe3798b5)
- [OS_GET_TIME](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a1b4134f508183af47ef3deff07be4a54)
- [bench_test_init](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a7d2ae16b9d290b7ab914f71155c5e56d)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [timestamp_check](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a5a399603fca75f3004d45720f03f9d44)
- [bench_test_start](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#ac476d41973f921a386c9a8341296dcfd)
- [TICK_SYNCH](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a95c5be89ea7bce90d2a8a11472ebd2c6)
- [k_uptime_delta](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gad748b2fe83b36884dc087b4af367de80)
- [bench_test_end](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a6555ffaf6ca7b4f5b81477faa8f43f53)
- [MSEC_PER_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga222f9dff749accf8de62bc4b52c7bdcd)
- [high_timer_overflow](../api_file_reference/P488_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考.md#a54d527f8fde477822ad2044579a7edd3)
- [k_cyc_to_ns_floor64](../timeutil_reference/P007_时间单位辅助接口.md#ga665d5fc98ffe8bd1cf78ca994f58724a)
- [NSEC_PER_USEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2180f263d149841a7c1fde663edb84c5)
- [USEC_PER_MSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2d66311052e2bddf914610fb7345ff27)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [test_asm_inline_gcc.h](../api_file_reference/P484_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_gcc.h_文件参考.md)
- [test_asm_inline_other.h](../api_file_reference/P485_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_other.h_文件参考.md)

---

[上一章](P013_ti_hdc302x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P015_tisci.h_源码浏览.md)
