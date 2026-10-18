---
id: learning.zephyr-docs.api-file-interface-reference.page-18
title: zephyr__drivers__clock_control__esp32_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_drivers\_\_clock\_control\_\_esp32\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Espressif ESP32设备的时钟控制定义（Clock Control Definitions）。

查看此文件的源码。

<a id="details"></a>

Espressif ESP32设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 18.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.2\_宏定义（Macros）

<a id="define-members-0"></a>

### ESP32 时钟控制子系统标识符（Clock control subsystem identifiers）

<a id="r_gae31484bb65af7e1833b735cdb7b3ee86"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_CPU 50
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gae31484bb65af7e1833b735cdb7b3ee86)。

CPU 时钟。

<a id="r_gaa57dc322f7c168bcdd1a7d36a9113d04"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST 51
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gaa57dc322f7c168bcdd1a7d36a9113d04)。

实时时钟（RTC）的快速时钟。

<a id="r_gac0c86530067504b41c00507cfcaddbdb"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW 52
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gac0c86530067504b41c00507cfcaddbdb)。

RTC 的慢速时钟。

<a id="r_ga84436f132de98914baacfbf4c4db65d7"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL 53
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#ga84436f132de98914baacfbf4c4db65d7)。

标称频率（nominal rate）下的 RTC 快速时钟。

<a id="r_ga8207878d8689cc1937571b725c1f3f2d"></a>

```c
#define ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL 54
```

相关声明：[ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#ga8207878d8689cc1937571b725c1f3f2d)。

标称频率下的 RTC 慢速时钟。


## 18.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P056_esp32_clock_control.h_源码浏览.md)
- [esp32_cpu_clock_config](../device_power_control_model_reference/P009_esp32_cpu_clock_config_结构体.md)
- [esp32_rtc_clock_config](../device_power_control_model_reference/P010_esp32_rtc_clock_config_结构体.md)
- [esp32_clock_config](../device_power_control_model_reference/P008_esp32_clock_config_结构体.md)
- [ESP32_CLOCK_CONTROL_SUBSYS_CPU](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gae31484bb65af7e1833b735cdb7b3ee86)
- [ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gaa57dc322f7c168bcdd1a7d36a9113d04)
- [ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#gac0c86530067504b41c00507cfcaddbdb)
- [ESP32_CLOCK_CONTROL_SUBSYS_RTC_FAST_NOMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#ga84436f132de98914baacfbf4c4db65d7)
- [ESP32_CLOCK_CONTROL_SUBSYS_RTC_SLOW_NOMINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__esp32.html#ga8207878d8689cc1937571b725c1f3f2d)

<a id="header-details"></a>

---

[上一章](P017_zephyr__mgmt__mcumgr__grp__enum_mgmt__enum_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__bluetooth__hci_lockstep.h_文件参考.md)
