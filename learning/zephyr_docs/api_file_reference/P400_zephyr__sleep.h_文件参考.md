---
id: learning.zephyr-docs.api-file-reference.page-400
title: zephyr__sleep.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sleep_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第400章\_zephyr\_\_sleep.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sleep_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

线程休眠（Thread Sleep）的API。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/sys/clock.h>
#include <zephyr/sys/time_units.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
#include <zephyr/syscalls/sleep.h>
```

查看此文件的源码。

线程休眠（Thread Sleep）的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 400.1\_函数（Functions）

<a id="r_ga5ad6bcbcf89f9a9fbf6929388e2a7842"></a>

```c
k_ticks_t k_sleep_ticks (k_timeout_t timeout)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_sleep_ticks](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

使当前线程睡眠，以时钟节拍为分辨率。

<a id="r_ga093ac91db17ec33696168801d01efe75"></a>

```c
static ALWAYS_INLINE int32_t k_sleep (k_timeout_t timeout)
```

相关声明：[int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_sleep](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

使当前线程睡眠。

<a id="r_gac1f1470dec2e89b4cb8fd8c5433bd101"></a>

```c
static ALWAYS_INLINE int32_t k_msleep (int32_t ms)
```

相关声明：[int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_msleep](../thread_core_reference/P001_线程公共接口.md#gac1f1470dec2e89b4cb8fd8c5433bd101)、[int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使当前线程睡眠。

<a id="r_gab761f90082335d57e3c6cd4013c819e6"></a>

```c
static ALWAYS_INLINE int32_t k_usleep (int32_t us)
```

相关声明：[int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[k_usleep](../thread_core_reference/P001_线程公共接口.md#gab761f90082335d57e3c6cd4013c819e6)、[int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

使当前线程睡眠，以微秒为分辨率。


## 400.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [zephyr/sys/time_units.h](../timeutil_reference/P012_时间单位头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/sleep_8h_source.html)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [k_sleep_ticks](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [int32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [k_sleep](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)
- [k_msleep](../thread_core_reference/P001_线程公共接口.md#gac1f1470dec2e89b4cb8fd8c5433bd101)
- [k_usleep](../thread_core_reference/P001_线程公共接口.md#gab761f90082335d57e3c6cd4013c819e6)

<a id="header-details"></a>

---

[上一章](P399_zephyr__dt-bindings__pinctrl__silabs__six301-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P401_zephyr__net__socket_poll.h_文件参考.md)
