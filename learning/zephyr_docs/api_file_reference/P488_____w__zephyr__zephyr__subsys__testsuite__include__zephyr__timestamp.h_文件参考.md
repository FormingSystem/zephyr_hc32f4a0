---
id: learning.zephyr-docs.api-file-reference.page-488
title: ____w__zephyr__zephyr__subsys__testsuite__include__zephyr__timestamp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/timestamp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第488章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_include\_\_zephyr\_\_timestamp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/timestamp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <limits.h>
#include <zephyr/test_asm_inline_other.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 488.1\_宏定义（Macros）

<a id="r_a95c5be89ea7bce90d2a8a11472ebd2c6"></a>

```c
#define TICK_SYNCH()
```

相关声明：[TICK_SYNCH](#a95c5be89ea7bce90d2a8a11472ebd2c6)。

<a id="r_a1b4134f508183af47ef3deff07be4a54"></a>

```c
#define OS_GET_TIME()
```

相关声明：[OS_GET_TIME](#a1b4134f508183af47ef3deff07be4a54)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 488.2\_函数（Functions）

<a id="r_abb03327df49c0544f863a239a9af0086"></a>

```c
static uint32_t TIME_STAMP_DELTA_GET (uint32_t ts)
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[TIME_STAMP_DELTA_GET](#abb03327df49c0544f863a239a9af0086)、[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a7d2ae16b9d290b7ab914f71155c5e56d"></a>

```c
static void bench_test_init (void)
```

相关声明：[bench_test_init](#a7d2ae16b9d290b7ab914f71155c5e56d)。

<a id="r_ac476d41973f921a386c9a8341296dcfd"></a>

```c
static void bench_test_start (void)
```

相关声明：[bench_test_start](#ac476d41973f921a386c9a8341296dcfd)。

<a id="r_a6555ffaf6ca7b4f5b81477faa8f43f53"></a>

```c
static int bench_test_end (void)
```

相关声明：[bench_test_end](#a6555ffaf6ca7b4f5b81477faa8f43f53)。

<a id="r_a54d527f8fde477822ad2044579a7edd3"></a>

```c
static int high_timer_overflow (void)
```

相关声明：[high_timer_overflow](#a54d527f8fde477822ad2044579a7edd3)。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 488.3\_变量（Variables）

<a id="r_a2503eba6a8f75337fe8c7ee84b0b3b21"></a>

```c
uint32_t tm_off
```

相关声明：[uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[tm_off](#a2503eba6a8f75337fe8c7ee84b0b3b21)。

<a id="r_a5a399603fca75f3004d45720f03f9d44"></a>

```c
static int64_t timestamp_check
```

相关声明：[int64_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[timestamp_check](#a5a399603fca75f3004d45720f03f9d44)。

## 488.4\_详细说明（Detailed Documentation）

<a id="a1b4134f508183af47ef3deff07be4a54"></a>

### `OS_GET_TIME`

```c
#define OS_GET_TIME ( )
```

展开值（Value）：

```c
k_cycle_get_32()
```

<a id="a95c5be89ea7bce90d2a8a11472ebd2c6"></a>

### `TICK_SYNCH`

```c
#define TICK_SYNCH ( )
```

展开值（Value）：

```c
k_sleep(K_TICKS(1))
```

<a id="a6555ffaf6ca7b4f5b81477faa8f43f53"></a>

### `bench_test_end()`

```c
int bench_test_end ( void )
```

声明属性：`inline`、`static`。

<a id="a7d2ae16b9d290b7ab914f71155c5e56d"></a>

### `bench_test_init()`

```c
void bench_test_init ( void )
```

声明属性：`inline`、`static`。

<a id="ac476d41973f921a386c9a8341296dcfd"></a>

### `bench_test_start()`

```c
void bench_test_start ( void )
```

声明属性：`inline`、`static`。

<a id="a54d527f8fde477822ad2044579a7edd3"></a>

### `high_timer_overflow()`

```c
int high_timer_overflow ( void )
```

声明属性：`inline`、`static`。

<a id="abb03327df49c0544f863a239a9af0086"></a>

### `TIME_STAMP_DELTA_GET()`

```c
uint32_t TIME_STAMP_DELTA_GET ( uint32_t ts)
```

声明属性：`inline`、`static`。

<a id="a5a399603fca75f3004d45720f03f9d44"></a>

### `timestamp_check`

```c
int64_t timestamp_check
```

声明属性：`static`。

<a id="a2503eba6a8f75337fe8c7ee84b0b3b21"></a>

### `tm_off`

```c
uint32_t tm_off
```

声明属性：`extern`。


## 488.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [limits.h](../api_source_runtime_reference/P039_limits.h_源码浏览.md)
- [zephyr/test_asm_inline_other.h](../api_source_supplement_reference/P222_test_asm_inline_other.h_源码浏览.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/timestamp_8h_source.html)
- [uint32_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [int64_t](P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [k_cycle_get_32](../timer_reference/P086_系统时钟公共接口.md#ga208687de625e0036558343b4e66143d3)
- [k_sleep](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)
- [K_TICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#gaeda983960bd25f1dba7a386ad720e395)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__clock__apis_html_ga208687de625e0036558343b4e66143d3"></a>
<a id="agroup__clock__apis_html_gaeda983960bd25f1dba7a386ad720e395"></a>
<a id="agroup__thread__apis_html_ga093ac91db17ec33696168801d01efe75"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P487_zephyr__posix__sys__times.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P489_zephyr__arch__tricore__arch_inlines.h_文件参考.md)
