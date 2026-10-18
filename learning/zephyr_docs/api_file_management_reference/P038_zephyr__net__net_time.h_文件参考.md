---
id: learning.zephyr-docs.api-file-management-reference.page-38
title: zephyr__net__net_time.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_net\_\_net\_time.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__time_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络协议栈中纳秒分辨率的经过时间（Elapsed Time）和时间戳的表示。

<a id="details"></a>

```c
#include <zephyr/sys/clock.h>
```

查看此文件的源码。

网络协议栈中纳秒分辨率（nanosecond resolution）的经过时间与时间戳表示。设计参考 Linux 的 `include/linux/ktime.h` 和 `include/linux/time64.h`／`tools/include/linux/time64.h`；原文给出的源码链接保留在本页“原页交叉引用”中。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.1\_宏定义（Macros）

<a id="r_ga38c90d968fc905093de2db057e6fa199"></a>

```c
#define NET_TIME_MAX INT64_MAX
```

相关声明：[NET_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga38c90d968fc905093de2db057e6fa199)、[INT64_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ad0d744f05898e32d01f73f8af3cd2071)。

`net_time_t` 可表示的最大正时间值。

<a id="r_ga732cb69409953ce0ce08991179afe718"></a>

```c
#define NET_TIME_MIN INT64_MIN
```

相关声明：[NET_TIME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga732cb69409953ce0ce08991179afe718)、[INT64_MIN](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab21f12f372f67b8ff0aa3432336ede67)。

`net_time_t` 可表示的最小负时间值。

<a id="r_gabcd93249b790bea7ed6f8aab9ebe568a"></a>

```c
#define NET_TIME_SEC_MAX (NET_TIME_MAX / NSEC_PER_SEC)
```

相关声明：[NET_TIME_SEC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gabcd93249b790bea7ed6f8aab9ebe568a)、[NET_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga38c90d968fc905093de2db057e6fa199)、[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

`net_time_t` 可安全表示的最大正秒数。

<a id="r_ga1fe8655623f0db550f7ae501b161940b"></a>

```c
#define NET_TIME_SEC_MIN (NET_TIME_MIN / NSEC_PER_SEC)
```

相关声明：[NET_TIME_SEC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga1fe8655623f0db550f7ae501b161940b)、[NET_TIME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga732cb69409953ce0ce08991179afe718)、[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

`net_time_t` 可安全表示的最小负秒数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 38.2\_类型定义（Typedefs）

<a id="r_gaf1da332e3909fca30de991cc2f950e56"></a>

```c
typedef int64_t net_time_t
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)。

`net_time_t` 在任何位置都表示纳秒分辨率的标量时间跨度（scalar time span）、指向未来（正值）或过去（负值）的相对时间，或相对于某个本地网络运行时间参考时钟（network uptime reference clock）的绝对时间戳。该参考时钟在本次运行期间不会回绕（wrap），并且在某种明确规定的意义上为所有本地网络接口所共有，有时甚至也与同一网络中的远端接口共有。


## 38.3\_原页交叉引用（Cross References）

- [zephyr/sys/clock.h](../timer_reference/P091_系统时钟头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P125_net_time.h_源码浏览.md)
- [NET_TIME_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga38c90d968fc905093de2db057e6fa199)
- [INT64_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ad0d744f05898e32d01f73f8af3cd2071)
- [net_time_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gaf1da332e3909fca30de991cc2f950e56)
- [NET_TIME_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga732cb69409953ce0ce08991179afe718)
- [INT64_MIN](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab21f12f372f67b8ff0aa3432336ede67)
- [NET_TIME_SEC_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#gabcd93249b790bea7ed6f8aab9ebe568a)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [NET_TIME_SEC_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html#ga1fe8655623f0db550f7ae501b161940b)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [https://github.com/torvalds/linux/blob/master/include/linux/ktime.h](https://github.com/torvalds/linux/blob/master/include/linux/ktime.h)
- [https://github.com/torvalds/linux/blob/master/](https://github.com/torvalds/linux/blob/master/)

<a id="header-details"></a>

---

[上一章](P037_zephyr__mpipe__mpipe_object.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__dt-bindings__reserved-memory__nordic-owned-memory.h_文件参考.md)
