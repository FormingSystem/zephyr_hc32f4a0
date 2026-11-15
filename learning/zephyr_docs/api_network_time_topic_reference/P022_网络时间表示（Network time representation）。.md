---
id: learning.zephyr-docs.api-network-time-topic-reference.page-22
title: 网络时间表示（Network time representation）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_网络时间表示（Network time representation）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 Zephyr 3.5 起提供；API 版本为 0.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_ga38c90d968fc905093de2db057e6fa199"></a>

```c
#define NET_TIME_MAX INT64_MAX
```

相关声明：[NET_TIME_MAX](#ga38c90d968fc905093de2db057e6fa199)、[INT64_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ad0d744f05898e32d01f73f8af3cd2071)。

`net_time_t` 可表示的最大正时间值。

<a id="r_ga732cb69409953ce0ce08991179afe718"></a>

```c
#define NET_TIME_MIN INT64_MIN
```

相关声明：[NET_TIME_MIN](#ga732cb69409953ce0ce08991179afe718)、[INT64_MIN](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab21f12f372f67b8ff0aa3432336ede67)。

`net_time_t` 可表示的最小负时间值。

<a id="r_gabcd93249b790bea7ed6f8aab9ebe568a"></a>

```c
#define NET_TIME_SEC_MAX (NET_TIME_MAX / NSEC_PER_SEC)
```

相关声明：[NET_TIME_SEC_MAX](#gabcd93249b790bea7ed6f8aab9ebe568a)、[NET_TIME_MAX](#ga38c90d968fc905093de2db057e6fa199)、[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

`net_time_t` 可安全表示的最大正秒数。

<a id="r_ga1fe8655623f0db550f7ae501b161940b"></a>

```c
#define NET_TIME_SEC_MIN (NET_TIME_MIN / NSEC_PER_SEC)
```

相关声明：[NET_TIME_SEC_MIN](#ga1fe8655623f0db550f7ae501b161940b)、[NET_TIME_MIN](#ga732cb69409953ce0ce08991179afe718)、[NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)。

`net_time_t` 可安全表示的最小负秒数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 22.2\_类型定义（Typedefs）

<a id="r_gaf1da332e3909fca30de991cc2f950e56"></a>

```c
typedef int64_t net_time_t
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[net_time_t](#gaf1da332e3909fca30de991cc2f950e56)。

`net_time_t` 在任何位置都表示纳秒分辨率的标量时间跨度（scalar time span）、指向未来（正值）或过去（负值）的相对时间，或相对于某个本地网络运行时间参考时钟（network uptime reference clock）的绝对时间戳。该参考时钟在本次运行期间不会回绕（wrap），并且在某种明确规定的意义上为所有本地网络接口所共有，有时甚至也与同一网络中的远端接口共有。

## 22.3\_详细说明（Detailed Documentation）

<a id="ga38c90d968fc905093de2db057e6fa199"></a>

### `NET_TIME_MAX`

```c
#define NET_TIME_MAX INT64_MAX
```

```c
#include <zephyr/net/net_time.h>
```

`net_time_t` 可表示的最大正时间值。

<a id="ga732cb69409953ce0ce08991179afe718"></a>

### `NET_TIME_MIN`

```c
#define NET_TIME_MIN INT64_MIN
```

```c
#include <zephyr/net/net_time.h>
```

`net_time_t` 可表示的最小负时间值。

<a id="gabcd93249b790bea7ed6f8aab9ebe568a"></a>

### `NET_TIME_SEC_MAX`

```c
#define NET_TIME_SEC_MAX (NET_TIME_MAX / NSEC_PER_SEC)
```

```c
#include <zephyr/net/net_time.h>
```

`net_time_t` 可安全表示的最大正秒数。

<a id="ga1fe8655623f0db550f7ae501b161940b"></a>

### `NET_TIME_SEC_MIN`

```c
#define NET_TIME_SEC_MIN (NET_TIME_MIN / NSEC_PER_SEC)
```

```c
#include <zephyr/net/net_time.h>
```

`net_time_t` 可安全表示的最小负秒数。

<a id="gaf1da332e3909fca30de991cc2f950e56"></a>

### `net_time_t`

```c
typedef int64_t net_time_t
```

```c
#include <zephyr/net/net_time.h>
```

`net_time_t` 在任何位置都表示纳秒分辨率的标量时间跨度（scalar time span）、指向未来（正值）或过去（负值）的相对时间，或相对于某个本地网络运行时间参考时钟（network uptime reference clock）的绝对时间戳。该参考时钟在本次运行期间不会回绕（wrap），并且在某种明确规定的意义上为所有本地网络接口所共有，有时甚至也与同一网络中的远端接口共有。

此类型为实验性类型（EXPERIMENTAL），目前仅限用于网络子系统内部的时间表示。

定时网络协议（timed network protocols，例如 PTP、TDMA）通常要求多个本地或远端接口在明确规定的容差内，对经过时间具有共同认识。因此，网络运行时间（network uptime）不同于单个硬件计数器外设所表示的时间：它需要由多个频率、准确度（accuracy）及精度（precision）不同的硬件外设共同表示。为了协作，这些硬件计数器需要相对于共同的本地或远端网络参考时间信号进行同频同相校准（syntonized）或驯服（disciplined），即锁定频率和相位。注意，虽然经过这种校准的时钟具有相同频率和相位，但通常并不具有相同纪元（epoch，即零点）。

这也说明了为什么将网络时间表示为某个特定硬件计数器的周期值（cycle value）时，它永远不会绝对“精确”，而只能相对于给定网络协议要求的容差——分辨率（resolution）、漂移（drift）和抖动（jitter）——达到“足够好”。参与定时网络协议的所有计数器外设都必须满足这些容差。

尽可能使用特定的周期／节拍计数器值（cycle/tick counter values），而不是 `net_time_t`，尤其是在引用内核系统时钟或任一单独计数器外设的值时。

`net_time_t` 只能覆盖大约正负 290 年，因此不能表示相对于任意纪元的一般时钟，也不能表示采用更复杂时间尺度（timescale）的时间，例如包含闰秒、时间调整、复杂历法或时区的时间。此时可使用 `timespec`（C11、POSIX.1-2001）、`timeval`（POSIX.1-2001）或 `tm`（C90）所表示的分解时间（broken-down time）。

与这些结构化时间表示相比，`net_time_t` 占用内存更少，标量算术更快、更简单，也更容易与底层硬件计数器值相互转换。此外，`net_time_t` 可同时用于网络协议栈和应用程序，而 POSIX 概念不具备同样适用性。`net_time_t` 与结构化时间表示之间可进行有限转换，但除 `timespec` 外，这些转换需要由更高层 API 实现相应概念。与 `timespec` 相互转换的工具函数将按需作为 `net_time_t` API 的一部分提供。

如果要在网络应用中表示粒度更粗的标量时间，可使用规定以秒表示时间的 `time_t`（C99、POSIX.1-2001），或用于微秒分辨率的 `suseconds_t`（POSIX.1-2001）。内核 `k_ticks_t` 和周期数（cycles）均为 Zephyr 专用，其分辨率未作统一规定，但适合表示内核定时器值和实现高分辨率自旋等待（spinning）。

如果需要更细的时间分辨率，可以参考通用／精确时间协议（(g)PTP）的相关概念，参见 `net_ptp_extended_time`。

网络协议栈不直接使用 `int64_t` 表示纳秒分辨率标量时间，是因为过去的经验表明，采用通用类型的字段常被错误使用，例如采用错误的分辨率，或表示定义不充分、同频同相校准（syntonization）语义不明确的时间概念。

任何暴露或接收 `net_time_t` 值的 API 都必须（SHALL）确保遵守所规定的契约，包括全部协议专用容差，从而使调用方能够依赖此类型的共同语义。这样，来自不同硬件外设、乃至不同网络节点的时间，就可以在明确界定的限制范围内进行比较，因此 `net_time_t` 适合作为定时网络协议的中间构建单元。


## 22.4\_原页交叉引用（Cross References）

- [INT64_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ad0d744f05898e32d01f73f8af3cd2071)
- [INT64_MIN](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab21f12f372f67b8ff0aa3432336ede67)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [zephyr/net/net_time.h](../api_file_management_reference/P038_zephyr__net__net_time.h_文件参考.md)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [timeval](../posix_system_model_reference/P024_timeval_结构体.md)
- [tm](../posix_system_model_reference/P025_tm_结构体.md)
- [time_t](../time_headers_reference/P003_timespec类型头文件参考.md#aa17c461cd5eca7fc12a66daa803c7fd7)
- [suseconds_t](../time_headers_reference/P003_timespec类型头文件参考.md#ad7acf95ceafb15a1d8d86af0c4982995)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [net_ptp_extended_time](../network_core_model_reference/P115_net_ptp_extended_time_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P021_蓝牙传输（Bluetooth transport）.md) · [返回大纲](大纲.md) · [下一章](P023_NXP FlexIO API主题.md)
