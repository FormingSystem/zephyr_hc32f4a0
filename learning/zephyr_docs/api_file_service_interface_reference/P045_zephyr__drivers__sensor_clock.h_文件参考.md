---
id: learning.zephyr-docs.api-file-service-interface-reference.page-45
title: zephyr__drivers__sensor_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_zephyr\_\_drivers\_\_sensor\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 45.1\_函数（Functions）

<a id="r_a337e06f1eecc2700268f803cf2eecefb"></a>

```c
int sensor_clock_get_cycles (uint64_t *cycles)
```

相关声明：[sensor_clock_get_cycles](#a337e06f1eecc2700268f803cf2eecefb)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

取得传感器当前的时钟周期计数（Clock Cycles）。

<a id="r_afe8b63ce73b7a40276996b1ee5408cd6"></a>

```c
uint64_t sensor_clock_cycles_to_ns (uint64_t cycles)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[sensor_clock_cycles_to_ns](#afe8b63ce73b7a40276996b1ee5408cd6)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

将时钟周期数（Clock Cycles）转换为纳秒。

## 45.2\_详细说明（Detailed Documentation）

<a id="afe8b63ce73b7a40276996b1ee5408cd6"></a>

### `sensor_clock_cycles_to_ns()`

```c
uint64_t sensor_clock_cycles_to_ns ( uint64_t cycles)
```

将时钟周期数（Clock Cycles）转换为纳秒。

本函数根据时钟频率（Clock Frequency）将时钟周期数转换为纳秒。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cycles` | 要转换的时钟周期数（Clock Cycles）。 |

**返回（Returns）**：**返回值（Returns）：**以纳秒为单位的时间。

<a id="a337e06f1eecc2700268f803cf2eecefb"></a>

### `sensor_clock_get_cycles()`

```c
int sensor_clock_get_cycles ( uint64_t * cycles)
```

取得传感器当前的时钟周期计数（Clock Cycles）。

本函数从所选传感器时钟源（Sensor Clock Source）获取当前周期计数。时钟源可根据配置选择系统时钟（System Clock）或外部时钟（External Clock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] cycles` | 指向 64 位无符号整数的指针，用于保存当前时钟周期计数（Clock Cycle Count）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，失败返回错误码（Error Code）。


## 45.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P767_sensor_clock.h_源码浏览.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P044_zephyr__sensing__sensing_sensor_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P046_zephyr__drivers__firmware__scmi__shmem.h_文件参考.md)
