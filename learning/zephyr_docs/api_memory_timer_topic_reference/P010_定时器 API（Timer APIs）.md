---
id: learning.zephyr-docs.api-memory-timer-topic-reference.page-10
title: 定时器 API（Timer APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_定时器 API（Timer APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__timer__apis.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_gaa267fcb0a2e18cd0da29e9f9612510a6"></a>

```c
#define K_TIMER_DEFINE(name, expiry_fn, stop_fn)
```

相关声明：[K_TIMER_DEFINE](#gaa267fcb0a2e18cd0da29e9f9612510a6)。

静态定义并初始化定时器（Timer）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_ga2915762e70454d98c73c179a45cafbde"></a>

```c
typedef void(* k_timer_expiry_t) (struct k_timer *timer)
```

相关声明：[k_timer_expiry_t](#ga2915762e70454d98c73c179a45cafbde)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

定时器到期函数类型（Timer Expiry Function Type）。

<a id="r_ga106733712fc4e62b59bbe6a480bb988c"></a>

```c
typedef void(* k_timer_stop_t) (struct k_timer *timer)
```

相关声明：[k_timer_stop_t](#ga106733712fc4e62b59bbe6a480bb988c)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

定时器停止函数类型（Timer Stop Function Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_ga318c846a740b901e5d56876a47ad7f61"></a>

```c
void k_timer_init (struct k_timer *timer, k_timer_expiry_t expiry_fn, k_timer_stop_t stop_fn)
```

相关声明：[k_timer_init](#ga318c846a740b901e5d56876a47ad7f61)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)、[k_timer_expiry_t](#ga2915762e70454d98c73c179a45cafbde)、[k_timer_stop_t](#ga106733712fc4e62b59bbe6a480bb988c)。

初始化定时器（Timer）。

<a id="r_ga3ba70e9f059ff52fd2057ab89ea7f2ee"></a>

```c
void k_timer_start (struct k_timer *timer, k_timeout_t duration, k_timeout_t period)
```

相关声明：[k_timer_start](#ga3ba70e9f059ff52fd2057ab89ea7f2ee)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

启动定时器（Timer）。

<a id="r_ga8d3e3356a10d36570e16f7920e4c8772"></a>

```c
void k_timer_stop (struct k_timer *timer)
```

相关声明：[k_timer_stop](#ga8d3e3356a10d36570e16f7920e4c8772)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

停止定时器（Timer）。

<a id="r_gad532f4834cd4cf8be27b089e6ea347ce"></a>

```c
uint32_t k_timer_status_get (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_status_get](#gad532f4834cd4cf8be27b089e6ea347ce)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

读取定时器状态（Timer Status）。

<a id="r_ga81d6d95b7021e26ad4cab161318e04f2"></a>

```c
uint32_t k_timer_status_sync (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_status_sync](#ga81d6d95b7021e26ad4cab161318e04f2)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

使线程与定时器到期事件同步（Synchronize Thread to Timer Expiration）。

<a id="r_ga022b4cf5c8d0ee21b6a3b04fd425533f"></a>

```c
k_ticks_t k_timer_expires_ticks (const struct k_timer *timer)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_timer_expires_ticks](#ga022b4cf5c8d0ee21b6a3b04fd425533f)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取定时器下一次到期的时间，以系统节拍（System Tick）为单位。

<a id="r_ga1176b36b960e786f68eaededf99a88b4"></a>

```c
k_ticks_t k_timer_remaining_ticks (const struct k_timer *timer)
```

相关声明：[k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)、[k_timer_remaining_ticks](#ga1176b36b960e786f68eaededf99a88b4)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取距定时器下一次到期的剩余时间，以系统节拍（System Tick）为单位。

<a id="r_ga6c6d8b0aa59bfa0f5924e95ccf756259"></a>

```c
static uint32_t k_timer_remaining_get (struct k_timer *timer)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timer_remaining_get](#ga6c6d8b0aa59bfa0f5924e95ccf756259)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取距定时器下一次到期的剩余时间（Time Remaining）。

<a id="r_gadba1884961e790dd9c5d567de91cc7e2"></a>

```c
void k_timer_user_data_set (struct k_timer *timer, void *user_data)
```

相关声明：[k_timer_user_data_set](#gadba1884961e790dd9c5d567de91cc7e2)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

将用户特定数据（User-specific Data）与定时器关联。

<a id="r_ga19a7d99a01a83828efd7f0d3bf2dd358"></a>

```c
void * k_timer_user_data_get (const struct k_timer *timer)
```

相关声明：[k_timer_user_data_get](#ga19a7d99a01a83828efd7f0d3bf2dd358)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

获取与定时器关联的用户特定数据（User-specific Data）。

<a id="r_ga39d502ccb6f299bf4efd82565684e508"></a>

```c
int k_timer_cleanup (struct k_timer *timer)
```

相关声明：[k_timer_cleanup](#ga39d502ccb6f299bf4efd82565684e508)、[k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)。

在释放动态分配的定时器（Dynamically Allocated Timer）之前，清理该定时器。

## 10.4\_详细说明（Detailed Documentation）

<a id="gaa267fcb0a2e18cd0da29e9f9612510a6"></a>

### `K_TIMER_DEFINE`

```c
#define K_TIMER_DEFINE ( name, expiry_fn, stop_fn )
```

```c
#include <zephyr/kernel.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE(k_timer, name) = \
        Z_TIMER_INITIALIZER(name, expiry_fn, stop_fn)
```

静态定义并初始化定时器（Timer）。

可在定义该定时器的模块之外，使用以下声明访问定时器（Timer）：

原始示例（Example）：

```c
extern struct k_timer <name>;
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 定时器变量名称（Timer Variable Name）。 |
| `expiry_fn` | 每次定时器到期时调用的函数（Expiry Function）。 |
| `stop_fn` | 定时器在运行期间被停止时调用的函数（Stop Function）。 |

<a id="ga2915762e70454d98c73c179a45cafbde"></a>

### `k_timer_expiry_t`

```c
typedef void(* k_timer_expiry_t) (struct k_timer *timer)
```

```c
#include <zephyr/kernel.h>
```

定时器到期函数类型（Timer Expiry Function Type）。

每次定时器到期时，系统时钟中断处理程序（System Clock Interrupt Handler）都会执行其到期函数（Expiry Function）。到期函数是可选的；仅当初始化定时器时指定了到期函数，才会调用该函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

<a id="ga106733712fc4e62b59bbe6a480bb988c"></a>

### `k_timer_stop_t`

```c
typedef void(* k_timer_stop_t) (struct k_timer *timer)
```

```c
#include <zephyr/kernel.h>
```

定时器停止函数类型（Timer Stop Function Type）。

定时器被提前停止时，会执行其停止函数（Stop Function）。该函数运行在停止定时器的调用上下文中。由于 `k_timer_stop()` 可从中断服务程序（ISR）调用，因此停止函数必须能够在中断上下文中调用（`isr-ok`）。

停止函数（Stop Function）是可选的；仅当初始化定时器时指定了停止函数，才会调用该函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

<a id="ga39d502ccb6f299bf4efd82565684e508"></a>

### `k_timer_cleanup()`

```c
int k_timer_cleanup ( struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

在释放动态分配的定时器（Dynamically Allocated Timer）之前，清理该定时器。

如果 `k_timer` 对象是动态分配的，则在释放其存储空间之前，必须取消其超时（Timeout），并等待所有正在执行的到期处理程序（Expiration Handler）结束，否则处理程序会解引用已释放的内存。本函数完成这两项操作：从超时队列（Timeout Queue）移除定时器，并等待其他 CPU 上正在执行的处理程序结束。

与 `k_timer_stop()` 不同，本函数不调用用户的 `stop_fn` 回调，也不修改等待队列（Wait Queue）。如果函数返回 0，则调用者负责管理该存储空间，此时不存在其他仍在使用该定时器的使用方。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器的地址（Timer Address）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EAGAIN` | 当仍有线程在定时器的等待队列（Wait Queue）中挂起时，例如通过 `k_timer_status_sync()` 等待的线程。 |

<a id="ga022b4cf5c8d0ee21b6a3b04fd425533f"></a>

### `k_timer_expires_ticks()`

```c
k_ticks_t k_timer_expires_ticks ( const struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

获取定时器下一次到期的时间，以系统节拍（System Tick）为单位。

本例程返回定时器下一次到期时系统运行时间（System Uptime）将达到的值，单位为系统节拍（System Tick）。如果定时器未运行，则返回最近一次已通告的节拍计数；由于当前节拍中尚未累计满一个节拍的时间，该值可能落后于实际当前运行时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器对象（Timer Object）。 |

**返回（Returns）**：返回值（Returns）：到期时的系统运行时间（Uptime），单位为节拍（Tick）。

<a id="ga318c846a740b901e5d56876a47ad7f61"></a>

### `k_timer_init()`

```c
void k_timer_init ( struct k_timer * timer, k_timer_expiry_t expiry_fn, k_timer_stop_t stop_fn )
```

```c
#include <zephyr/kernel.h>
```

初始化定时器（Timer）。

本例程在定时器首次使用之前将其初始化（Initialize）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |
| `expiry_fn` | 每次定时器到期时调用的函数（Expiry Function）。 |
| `stop_fn` | 定时器在运行期间被停止时调用的函数（Stop Function）。 |

<a id="ga6c6d8b0aa59bfa0f5924e95ccf756259"></a>

### `k_timer_remaining_get()`

```c
uint32_t k_timer_remaining_get ( struct k_timer * timer)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/kernel.h>
```

获取距定时器下一次到期的剩余时间（Time Remaining）。

本例程计算运行中的定时器距下一次到期的大致剩余时间（Time Remaining）。如果定时器未运行，则返回零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

**返回（Returns）**：返回值（Returns）：剩余时间，单位为毫秒（Millisecond）。

<a id="ga1176b36b960e786f68eaededf99a88b4"></a>

### `k_timer_remaining_ticks()`

```c
k_ticks_t k_timer_remaining_ticks ( const struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

获取距定时器下一次到期的剩余时间，以系统节拍（System Tick）为单位。

本例程计算运行中的定时器距下一次到期的剩余时间，单位为系统节拍（System Tick）。如果定时器未运行，则返回零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器对象（Timer Object）。 |

**返回（Returns）**：返回值（Returns）：距到期的剩余时间，单位为节拍（Tick）。

<a id="ga3ba70e9f059ff52fd2057ab89ea7f2ee"></a>

### `k_timer_start()`

```c
void k_timer_start ( struct k_timer * timer, k_timeout_t duration, k_timeout_t period )
```

```c
#include <zephyr/kernel.h>
```

启动定时器（Timer）。

本例程启动定时器，并将其状态（Status）重置为零。定时器使用指定的初始时长（Duration）和周期（Period）开始倒计时。

允许启动已经在运行的定时器。此时会将定时器状态（Status）重置为零，并使用新的初始时长（Duration）和周期（Period）重新开始倒计时。

如果 `duration` 为 `K_FOREVER`，本例程不会更新指定定时器，也不会对其产生任何其他影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |
| `duration` | 定时器的初始时长（Initial Timer Duration）。 |
| `period` | 定时器周期（Timer Period） |

<a id="gad532f4834cd4cf8be27b089e6ea347ce"></a>

### `k_timer_status_get()`

```c
uint32_t k_timer_status_get ( struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

读取定时器状态（Timer Status）。

本例程读取定时器状态（Timer Status），该状态表示自上次读取状态以来定时器到期的次数。

调用本例程会将定时器状态（Timer Status）重置为零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

**返回（Returns）**：返回值（Returns）：定时器状态（Timer Status）。

<a id="ga81d6d95b7021e26ad4cab161318e04f2"></a>

### `k_timer_status_sync()`

```c
uint32_t k_timer_status_sync ( struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

使线程与定时器到期事件同步（Synchronize Thread to Timer Expiration）。

本例程阻塞调用线程，直至定时器状态（Timer Status）变为非零，或定时器被停止。非零状态表示自上次检查状态以来定时器至少已到期一次。如果状态已经为非零，或者定时器已经停止，调用者会直接继续执行，无须等待。

调用本例程会将定时器状态（Timer Status）重置为零。

中断处理程序（Interrupt Handler）不得使用本例程，因为中断处理程序不允许阻塞。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

**返回（Returns）**：返回值（Returns）：定时器状态（Timer Status）。

<a id="ga8d3e3356a10d36570e16f7920e4c8772"></a>

### `k_timer_stop()`

```c
void k_timer_stop ( struct k_timer * timer)
```

声明属性：`isr-ok`（允许从中断服务程序ISR调用）。

```c
#include <zephyr/kernel.h>
```

停止定时器（Timer）。

本例程提前停止正在运行的定时器。如果定时器具有停止函数（Stop Function），则由调用者调用该函数。

允许尝试停止未运行的定时器，但不会对定时器产生任何影响。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

**说明（Note）**：注意（Note）：如果要从中断服务程序（ISR）调用 `k_timer_stop`，则停止处理程序（Stop Handler）也必须能够从 ISR 调用。

<a id="ga19a7d99a01a83828efd7f0d3bf2dd358"></a>

### `k_timer_user_data_get()`

```c
void * k_timer_user_data_get ( const struct k_timer * timer)
```

```c
#include <zephyr/kernel.h>
```

获取与定时器关联的用户特定数据（User-specific Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |

**返回（Returns）**：返回值（Returns）：用户数据（User Data）。

<a id="gadba1884961e790dd9c5d567de91cc7e2"></a>

### `k_timer_user_data_set()`

```c
void k_timer_user_data_set ( struct k_timer * timer, void * user_data )
```

```c
#include <zephyr/kernel.h>
```

将用户特定数据（User-specific Data）与定时器关联。

本例程将 `user_data` 记录在定时器中，以便稍后获取。

例如，当多个子系统（Subsystem）共用同一定时器处理程序时，可借此获取该定时器所属子系统的专用数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timer` | 定时器地址（Timer Address）。 |
| `user_data` | 要与定时器关联的用户数据（User Data）。 |


## 10.5\_原页交叉引用（Cross References）

- [k_timer](../kernel_runtime_model_reference/P007_k_timer_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astructk__timer_html"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_统计信息（Statistics）。.md) · [返回大纲](大纲.md) · [下一章](P011_传输层安全（TLS）的凭据管理。.md)
