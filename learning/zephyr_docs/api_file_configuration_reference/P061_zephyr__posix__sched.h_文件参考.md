---
id: learning.zephyr-docs.api-file-configuration-reference.page-61
title: zephyr__posix__sched.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_zephyr\_\_posix\_\_sched.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sched_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/posix/posix_types.h>
#include <time.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 61.1\_宏定义（Macros）

<a id="r_a44c9baaf6f3c286f76783265b4938881"></a>

```c
#define SCHED_OTHER 0
```

相关声明：[SCHED_OTHER](#a44c9baaf6f3c286f76783265b4938881)。

<a id="r_ab998332c6538a029b4eed398b7a423da"></a>

```c
#define SCHED_FIFO 1
```

相关声明：[SCHED_FIFO](#ab998332c6538a029b4eed398b7a423da)。

<a id="r_a2a29482379f591144ace39cbd659a257"></a>

```c
#define SCHED_RR 2
```

相关声明：[SCHED_RR](#a2a29482379f591144ace39cbd659a257)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 61.2\_函数（Functions）

<a id="r_a357cd4b34c13011749dfffb42b489f09"></a>

```c
int sched_yield (void)
```

相关声明：[sched_yield](#a357cd4b34c13011749dfffb42b489f09)。

让出处理器（Yield the Processor）。

<a id="r_af1f370fc36ea6b22ed42b5ee3cf82a81"></a>

```c
int sched_get_priority_min (int policy)
```

相关声明：[sched_get_priority_min](#af1f370fc36ea6b22ed42b5ee3cf82a81)。

<a id="r_afaebd1698caeb9b9b9e614ad84edd609"></a>

```c
int sched_get_priority_max (int policy)
```

相关声明：[sched_get_priority_max](#afaebd1698caeb9b9b9e614ad84edd609)。

<a id="r_a563c7ac53bac2c1b51379147e66c44ec"></a>

```c
int sched_getparam (pid_t pid, struct sched_param *param)
```

相关声明：[sched_getparam](#a563c7ac53bac2c1b51379147e66c44ec)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a99fcb2532b1482d236dc04495a3f194d"></a>

```c
int sched_getscheduler (pid_t pid)
```

相关声明：[sched_getscheduler](#a99fcb2532b1482d236dc04495a3f194d)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a06b497c4ea6bbabd2b62ba1a8a848a1b"></a>

```c
int sched_setparam (pid_t pid, const struct sched_param *param)
```

相关声明：[sched_setparam](#a06b497c4ea6bbabd2b62ba1a8a848a1b)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a84ad29a6f2ad27370df09c664ac65eac"></a>

```c
int sched_setscheduler (pid_t pid, int policy, const struct sched_param *param)
```

相关声明：[sched_setscheduler](#a84ad29a6f2ad27370df09c664ac65eac)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)。

<a id="r_a484f0eb93529d29a66e24485725c4c7b"></a>

```c
int sched_rr_get_interval (pid_t pid, struct timespec *interval)
```

相关声明：[sched_rr_get_interval](#a484f0eb93529d29a66e24485725c4c7b)、[pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

## 61.3\_详细说明（Detailed Documentation）

<a id="ab998332c6538a029b4eed398b7a423da"></a>

### `SCHED_FIFO`

```c
#define SCHED_FIFO 1
```

<a id="a44c9baaf6f3c286f76783265b4938881"></a>

### `SCHED_OTHER`

```c
#define SCHED_OTHER 0
```

<a id="a2a29482379f591144ace39cbd659a257"></a>

### `SCHED_RR`

```c
#define SCHED_RR 2
```

<a id="afaebd1698caeb9b9b9e614ad84edd609"></a>

### `sched_get_priority_max()`

```c
int sched_get_priority_max ( int policy)
```

<a id="af1f370fc36ea6b22ed42b5ee3cf82a81"></a>

### `sched_get_priority_min()`

```c
int sched_get_priority_min ( int policy)
```

<a id="a563c7ac53bac2c1b51379147e66c44ec"></a>

### `sched_getparam()`

```c
int sched_getparam ( pid_t pid, struct sched_param * param )
```

<a id="a99fcb2532b1482d236dc04495a3f194d"></a>

### `sched_getscheduler()`

```c
int sched_getscheduler ( pid_t pid)
```

<a id="a484f0eb93529d29a66e24485725c4c7b"></a>

### `sched_rr_get_interval()`

```c
int sched_rr_get_interval ( pid_t pid, struct timespec * interval )
```

<a id="a06b497c4ea6bbabd2b62ba1a8a848a1b"></a>

### `sched_setparam()`

```c
int sched_setparam ( pid_t pid, const struct sched_param * param )
```

<a id="a84ad29a6f2ad27370df09c664ac65eac"></a>

### `sched_setscheduler()`

```c
int sched_setscheduler ( pid_t pid, int policy, const struct sched_param * param )
```

<a id="a357cd4b34c13011749dfffb42b489f09"></a>

### `sched_yield()`

```c
int sched_yield ( void )
```

让出处理器（Yield the Processor）。

参见 IEEE 1003.1。


## 61.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/posix/posix_types.h](https://docs.zephyrproject.org/latest/doxygen/html/posix__types_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P050_sched.h_源码浏览.md)
- [pid_t](https://docs.zephyrproject.org/latest/doxygen/html/posix__signal_8h.html#a114f9c2461df851d2ad00aad8dcfa3f7)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P062_zephyr__dsp__print_format.h_文件参考.md)
