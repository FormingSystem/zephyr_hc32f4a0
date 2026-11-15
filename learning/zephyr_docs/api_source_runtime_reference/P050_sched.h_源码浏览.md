---
id: learning.zephyr-docs.api-source-runtime-reference.page-50
title: sched.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_sched.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html)。

## 50.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
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
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="akernel_8h_html"></a>
<a id="aposix_2sched_8h_html_a06b497c4ea6bbabd2b62ba1a8a848a1b"></a>
<a id="aposix_2sched_8h_html_a357cd4b34c13011749dfffb42b489f09"></a>
<a id="aposix_2sched_8h_html_a484f0eb93529d29a66e24485725c4c7b"></a>
<a id="aposix_2sched_8h_html_a563c7ac53bac2c1b51379147e66c44ec"></a>
<a id="aposix_2sched_8h_html_a84ad29a6f2ad27370df09c664ac65eac"></a>
<a id="aposix_2sched_8h_html_a99fcb2532b1482d236dc04495a3f194d"></a>
<a id="aposix_2sched_8h_html_af1f370fc36ea6b22ed42b5ee3cf82a81"></a>
<a id="aposix_2sched_8h_html_afaebd1698caeb9b9b9e614ad84edd609"></a>
<a id="aposix__signal_8h_html_a114f9c2461df851d2ad00aad8dcfa3f7"></a>
<a id="aposix__types_8h_html"></a>
<a id="astructtimespec_html"></a>

```c
/*
 * Copyright (c) 2018-2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_POSIX_SCHED_H_
#define ZEPHYR_INCLUDE_POSIX_SCHED_H_

#include <zephyr/kernel.h>
#include <zephyr/posix/posix_types.h>

#include <time.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Other mandatory scheduling policy. Must be numerically distinct. May
 * execute identically to SCHED_RR or SCHED_FIFO. For Zephyr this is a
 * pseudonym for SCHED_RR.
 */
#define SCHED_OTHER 0

/* Cooperative scheduling policy */
#define SCHED_FIFO 1

/* Priority based preemptive scheduling policy */
#define SCHED_RR 2

#if defined(CONFIG_MINIMAL_LIBC) || defined(CONFIG_PICOLIBC) || defined(CONFIG_ARMCLANG_STD_LIBC) \
        || defined(CONFIG_ARCMWDT_LIBC)
struct sched_param {
        int sched_priority;
};
#endif

int sched_yield(void);

int sched_get_priority_min(int policy);
int sched_get_priority_max(int policy);

int sched_getparam(pid_t pid, struct sched_param *param);
int sched_getscheduler(pid_t pid);

int sched_setparam(pid_t pid, const struct sched_param *param);
int sched_setscheduler(pid_t pid, int policy, const struct sched_param *param);
int sched_rr_get_interval(pid_t pid, struct timespec *interval);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_POSIX_SCHED_H_ */
```

## 50.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 18 行

另一种必需的调度策略（Scheduling policy）。其数值必须与其他策略不同，但执行行为可以与 `SCHED_RR` 或 `SCHED_FIFO` 相同。在 Zephyr 中，它是 `SCHED_RR` 的别名。

### 注释 3：原第 25 行

协作式调度策略（Cooperative scheduling policy）。

### 注释 4：原第 28 行

基于优先级的抢占式调度策略（Priority based preemptive scheduling policy）。

### 注释 5：原第 59 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_POSIX_SCHED_H_`。

## 50.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)
- [sched_yield](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a357cd4b34c13011749dfffb42b489f09)
- [sched_get_priority_min](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#af1f370fc36ea6b22ed42b5ee3cf82a81)
- [sched_get_priority_max](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#afaebd1698caeb9b9b9e614ad84edd609)
- [sched_getparam](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a563c7ac53bac2c1b51379147e66c44ec)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [sched_getscheduler](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a99fcb2532b1482d236dc04495a3f194d)
- [sched_setparam](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a06b497c4ea6bbabd2b62ba1a8a848a1b)
- [sched_setscheduler](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a84ad29a6f2ad27370df09c664ac65eac)
- [sched_rr_get_interval](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html#a484f0eb93529d29a66e24485725c4c7b)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h.html)

---

[上一章](P049_pinctrl_rp1_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P051_printk.h_源码浏览.md)
