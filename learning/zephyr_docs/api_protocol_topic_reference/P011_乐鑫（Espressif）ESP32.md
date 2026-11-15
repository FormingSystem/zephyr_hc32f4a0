---
id: learning.zephyr-docs.api-protocol-topic-reference.page-11
title: 乐鑫（Espressif）ESP32
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_乐鑫（Espressif）ESP32

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_esp32_5Fclock_5Fcontrol_2Eh"></a>

```c
file esp32_clock_control.h
```

相关声明：[esp32_clock_control.h](../api_file_interface_reference/P018_zephyr__drivers__clock_control__esp32_clock_control.h_文件参考.md)。

Espressif ESP32设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

<a id="r_esp32_5Fcpu_5Fclock_5Fconfig"></a>

```c
struct esp32_cpu_clock_config
```

相关声明：[esp32_cpu_clock_config](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md)。

ESP32的CPU时钟配置。

<a id="r_esp32_5Frtc_5Fclock_5Fconfig"></a>

```c
struct esp32_rtc_clock_config
```

相关声明：[esp32_rtc_clock_config](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md)。

ESP32的实时时钟（RTC）配置。

<a id="r_esp32_5Fclock_5Fconfig"></a>

```c
struct esp32_clock_config
```

相关声明：[esp32_clock_config](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md)。

ESP32的汇总时钟配置（Aggregate Clock Configuration）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.3\_ESP32 时钟控制子系统标识符（Clock control subsystem identifiers）

<a id="r_gae31484bb65af7e1833b735cdb7b3ee86"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_CPU 50
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_CPU](#gae31484bb65af7e1833b735cdb7b3ee86)。

CPU 时钟。

<a id="r_gaa57dc322f7c168bcdd1a7d36a9113d04"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST 51
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST](#gaa57dc322f7c168bcdd1a7d36a9113d04)。

实时时钟（RTC）的快速时钟。

<a id="r_gac0c86530067504b41c00507cfcaddbdb"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW 52
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW](#gac0c86530067504b41c00507cfcaddbdb)。

RTC 的慢速时钟。

<a id="r_ga84436f132de98914baacfbf4c4db65d7"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL 53
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL](#ga84436f132de98914baacfbf4c4db65d7)。

标称频率（nominal rate）下的 RTC 快速时钟。

<a id="r_ga8207878d8689cc1937571b725c1f3f2d"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL 54
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL](#ga8207878d8689cc1937571b725c1f3f2d)。

标称频率下的 RTC 慢速时钟。

## 11.4\_详细说明（Detailed Documentation）

<a id="gae31484bb65af7e1833b735cdb7b3ee86"></a>

### `ESP32_CLOCK_CONTROL_SUBSYS_CPU`

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_CPU 50
```

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

CPU 时钟。

<a id="gaa57dc322f7c168bcdd1a7d36a9113d04"></a>

### `ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST`

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST 51
```

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

实时时钟（RTC）的快速时钟。

<a id="ga84436f132de98914baacfbf4c4db65d7"></a>

### `ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL`

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL 53
```

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

标称频率（nominal rate）下的 RTC 快速时钟。

<a id="gac0c86530067504b41c00507cfcaddbdb"></a>

### `ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW`

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW 52
```

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

RTC 的慢速时钟。

<a id="ga8207878d8689cc1937571b725c1f3f2d"></a>

### `ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL`

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL 54
```

```c
#include <zephyr/drivers/clock_control/esp32_clock_control.h>
```

标称频率下的 RTC 慢速时钟。


## 11.5\_原页交叉引用（Cross References）

- [esp32_clock_control.h](../api_file_interface_reference/P018_zephyr__drivers__clock_control__esp32_clock_control.h_文件参考.md)
- [esp32_cpu_clock_config](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md)
- [esp32_rtc_clock_config](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md)
- [esp32_clock_config](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_Atmel SAM 电源管理控制器（PMC）.md) · [返回大纲](大纲.md) · [下一章](P012_瑞萨（Renesas）RA 时钟生成电路（CGC）.md)
