---
id: learning.zephyr-docs.timeutil-reference.page-8
title: timespec时间工具接口
kind: reference
status: maintained
domains: [zephyr, time, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__timeutil__timespec__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_timespec时间工具接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__timeutil__timespec__apis.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：先读[时间工具指南](../kernel/P037_时间工具.md)，再按[本册大纲](大纲.md)查时间表示、同步、单位换算及timespec接口。源码跟踪译注与官方原文分开标示。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga2426889e703021e8b6f8a0ccab885bb6"></a>

```c
static bool timespec_is_valid (const struct timespec *ts)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_is_valid](#ga2426889e703021e8b6f8a0ccab885bb6)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

检查timespec是否有效。

<a id="r_ga57f165604525ef6b680f646d97a38538"></a>

```c
bool timespec_normalize (struct timespec *ts)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_normalize](#ga57f165604525ef6b680f646d97a38538)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

规范化timespec，使tv_nsec位于有效范围内。

<a id="r_ga81026756e417d086b4f53306d04c8d10"></a>

```c
static bool timespec_add (struct timespec *a, const struct timespec *b)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_add](#ga81026756e417d086b4f53306d04c8d10)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

将一个timespec加到另一个timespec上。

<a id="r_ga38216267ef6ca24e2b05d77104f5837a"></a>

```c
static bool timespec_negate (struct timespec *ts)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_negate](#ga38216267ef6ca24e2b05d77104f5837a)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

对timespec对象取负。

<a id="r_gae0511602aea1fecc0b204e28ae91e7d0"></a>

```c
static bool timespec_sub (struct timespec *a, const struct timespec *b)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_sub](#gae0511602aea1fecc0b204e28ae91e7d0)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

从一个timespec中减去另一个timespec。

<a id="r_gafa281a298f8b2f011875bb00094260fc"></a>

```c
static int timespec_compare (const struct timespec *a, const struct timespec *b)
```

相关声明：[timespec_compare](#gafa281a298f8b2f011875bb00094260fc)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

比较两个timespec对象。

<a id="r_gaedc15d71f9eee8e243c070a3e07d919f"></a>

```c
static bool timespec_equal (const struct timespec *a, const struct timespec *b)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[timespec_equal](#gaedc15d71f9eee8e243c070a3e07d919f)、[timespec](../time_headers_reference/P005_timespec时间结构.md)、[timespec](../time_headers_reference/P005_timespec时间结构.md)。

检查两个timespec对象是否相等。

## 8.2\_详细说明（Detailed Documentation）

<a id="ga81026756e417d086b4f53306d04c8d10"></a>

### `timespec_add()`

```c
bool timespec_add ( struct timespec * a, const struct timespec * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

将一个timespec加到另一个timespec上。

此函数将a和b所指的两个timespec相加，并把结果写入a所指的timespec。

如果操作会导致整数溢出，返回false。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 用于累加并接收结果的timespec。 |
| `b` | 要加上的timespec。 |

**说明（Note）**：a和b必须非NULL，且已规范化（Normalized）。

**返回（Returns）**：操作成功时返回true，否则返回false。

<a id="gafa281a298f8b2f011875bb00094260fc"></a>

### `timespec_compare()`

```c
int timespec_compare ( const struct timespec * a, const struct timespec * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

比较两个timespec对象。

此函数比较a和b所指的两个timespec对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 要比较的第一个timespec。 |
| `b` | 要比较的第二个timespec。 |

**说明（Note）**：a和b必须非NULL，且已规范化（Normalized）。

**返回（Returns）**：a小于、等于或大于b时，分别返回-1、0或+1。

<a id="gaedc15d71f9eee8e243c070a3e07d919f"></a>

### `timespec_equal()`

```c
bool timespec_equal ( const struct timespec * a, const struct timespec * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

检查两个timespec对象是否相等。

此函数检查a和b所指的两个timespec对象是否相等。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 要比较的第一个timespec。 |
| `b` | 要比较的第二个timespec。 |

**说明（Note）**：a和b必须非NULL，但无须规范化。

**返回（Returns）**：两个timespec对象相等时返回true，否则返回false。

<a id="ga2426889e703021e8b6f8a0ccab885bb6"></a>

### `timespec_is_valid()`

```c
bool timespec_is_valid ( const struct timespec * ts)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

检查timespec是否有效。

通过检查tv_nsec是否位于[0, NSEC_PER_SEC-1]范围内，判断timespec是否有效，即是否已经规范化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ts` | 要检查的timespec。 |

**说明（Note）**：ts不得为NULL。

**返回（Returns）**：timespec有效时返回true，否则返回false。

<a id="ga38216267ef6ca24e2b05d77104f5837a"></a>

### `timespec_negate()`

```c
bool timespec_negate ( struct timespec * ts)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

对timespec对象取负。

对ts所指的timespec对象取负，并将结果写回同一位置。

如果操作会导致整数溢出，返回false。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ts` | 要取负的timespec对象。 |

**返回（Returns）**：操作成功时返回true，否则返回false。

<a id="ga57f165604525ef6b680f646d97a38538"></a>

### `timespec_normalize()`

```c
bool timespec_normalize ( struct timespec * ts)
```

```c
#include <zephyr/sys/timeutil.h>
```

规范化timespec，使tv_nsec位于有效范围内。

通过调整tv_sec和tv_nsec，将tv_nsec规范化到[0, NSEC_PER_SEC-1]范围内。做法是把纳秒换算成秒：tv_nsec大于NSEC_PER_SEC时向正方向累加秒数，tv_nsec小于0时向负方向累加秒数。

规范化过程可用以下伪代码表示：

原始示例（Example）：

```c
if ts.tv_nsec >= NSEC_PER_SEC:
    sec = ts.tv_nsec / NSEC_PER_SEC
    ts.tv_sec += sec
    ts.tv_nsec -= sec * NSEC_PER_SEC
elif ts.tv_nsec < 0:
     # div_round_up(abs(ts->tv_nsec), NSEC_PER_SEC)
         sec = (NSEC_PER_SEC - ts.tv_nsec - 1) / NSEC_PER_SEC
         ts.tv_sec -= sec;
         ts.tv_nsec += sec * NSEC_PER_SEC;
```

- tv_nsec为负且tv_sec已经处于最小值时。
- tv_nsec大于等于NSEC_PER_SEC且tv_sec已经处于最大值时。

如果操作会导致整数溢出，返回false。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ts` | 要规范化的timespec。 |

**说明（Note）**：规范化可能在两种情况下导致整数溢出。它们不仅适用于tv_sec多出或减少一秒的情况，也可以扩展到任何可表示的NSEC_PER_SEC整数倍。

**说明（Note）**：ts必须非NULL。

**返回（Returns）**：操作顺利完成时返回true，否则返回false。

<a id="gae0511602aea1fecc0b204e28ae91e7d0"></a>

### `timespec_sub()`

```c
bool timespec_sub ( struct timespec * a, const struct timespec * b )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/sys/timeutil.h>
```

从一个timespec中减去另一个timespec。

此函数从a所指的timespec中减去b所指的timespec，并将结果写入a所指的timespec。

如果操作会导致整数溢出，返回false。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 作为被减数并接收结果的timespec。 |
| `b` | 要减去的timespec。 |

**说明（Note）**：a和b必须非NULL。

**返回（Returns）**：操作成功时返回true，否则返回false。

## 8.3\_源码定位与版本边界

本册提供[时间表示](P002_时间表示接口.md)、[时间同步](P003_时间同步接口.md)、[单位换算](P007_时间单位辅助接口.md)与[timespec工具](P008_timespec时间工具接口.md)。头文件相对定位：[timeutil.h](../../../include/zephyr/sys/timeutil.h)、[time_units.h](../../../include/zephyr/sys/time_units.h)，实现定位：[timeutil.c](../../../lib/utils/timeutil.c)。

配置与构建定位：[Kconfig](../../../lib/utils/Kconfig)、[CMakeLists.txt](../../../lib/utils/CMakeLists.txt)。本次[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/timeutil.h)、[单位换算头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/time_units.h)及[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/utils/timeutil.c)摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：阅读边界：时间表示（Time Representation）处理UTC日历字段与POSIX秒数，时间同步（Time Synchronization）映射两个计数时钟，单位换算（Unit Conversion）处理时长的单位与舍入，timespec工具处理秒／纳秒二元组。它们不自动校准RTC、选择时区或建立网络授时服务。

> 译注——源码核对：版本与定位：以下译注核对本次官方main源码，链接中的本仓库源码只是相对定位入口，不保证读者的本地版本与滚动更新的latest相同。官方原文、原始代码及法律注释保留；译注不修改接口契约。

> 译注——源码核对：规范化（Normalization）要求0≤tv_nsec<10^9，秒字段可以为负。timespec_is_valid只检查纳秒范围；它不判断是否为正时长。normalize把溢出的纳秒进位或借位到秒；原描述使用大于NSEC_PER_SEC，当前代码实际在大于等于时进位。

> 译注——源码核对：add、negate和compare要求输入已规范化；sub通过negate及add也继承这一前提。equal只比较两个原始字段，数值等价但表示未规范化的二元组未必相等。断言（Assertion）不能替代应用的输入检查。

> 译注——源码核对：算术接口返回false不一律保证目标对象不变，例如内建溢出操作或相加后规范化失败可能已写入字段。调用者需要保留原值时，应对临时副本操作，成功后再采用结果；也须避免原始纳秒为最小long等导致中间取负无法表示的输入。

> 译注——源码核对：SYS_TIMESPEC对秒字段做范围夹取（Clamp），纳秒字段只是转换，不能代替规范化。宏参数可能被重复求值，避免传入自增或带其他副作用的表达式。

> 译注——源码核对：timespec_from_timeout接受相对超时（Relative Timeout）及永久等待哨兵；绝对期限（Absolute Deadline）不属于该接口的常规输入。普通节拍按向下换算分解为秒与纳秒；K_FOREVER映射到专用timespec值。

> 译注——源码核对：timespec_to_timeout把正时长向上对齐到节拍边界，并限制到可表达的最大节拍数。rem按“请求值减换算后时长”计算，向上舍入时可能为负，封顶时可能为正；它不是一律非负的余数。rem与req必须采用不同存储，当前实现会先写rem再读取req计算差值，重叠会破坏输入。

本次验证范围为文档与源码对照，未编译或执行时间同步、计时精度及实板实验。

## 8.4\_原页交叉引用（Cross References）

- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [timespec](../time_headers_reference/P005_timespec时间结构.md)
- [zephyr/sys/timeutil.h](P009_时间工具头文件参考.md)
- [false](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)
- [true](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [NSEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga0501e82515b2bdf36453c4cc80f5e0cc)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_时间单位辅助接口.md) · [返回大纲](大纲.md) · [下一章](P009_时间工具头文件参考.md)
