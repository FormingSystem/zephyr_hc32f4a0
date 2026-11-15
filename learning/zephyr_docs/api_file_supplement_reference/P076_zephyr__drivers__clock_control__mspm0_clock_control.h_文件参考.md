---
id: learning.zephyr-docs.api-file-supplement-reference.page-76
title: zephyr__drivers__clock_control__mspm0_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_zephyr\_\_drivers\_\_clock\_control\_\_mspm0\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspm0__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments MSPM0设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/dt-bindings/clock/mspm0_clock.h>
```

查看此文件的源码。

Texas Instruments MSPM0设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 76.1\_数据结构（Data Structures）

<a id="r_mspm0_5Fsys_5Fclock"></a>

```c
struct mspm0_sys_clock
```

相关声明：[mspm0_sys_clock](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md)。

MSPM0系统时钟子系统选择器（Subsystem Selector）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 76.2\_宏定义（Macros）

<a id="r_ga438e7623f4a0dde8f48ce81cc9ecb4d5"></a>

```c
#define MSPM0_CLOCK_SUBSYS_FN(index)
```

相关声明：[MSPM0_CLOCK_SUBSYS_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html#ga438e7623f4a0dde8f48ce81cc9ecb4d5)。

根据设备树实例时钟说明符（DT Instance Clock Specifier）初始化 `mspm0_sys_clock`。


## 76.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/clock/mspm0_clock.h](../api_source_configuration_reference/P059_mspm0_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P568_mspm0_clock_control.h_源码浏览.md)
- [mspm0_sys_clock](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md)
- [MSPM0_CLOCK_SUBSYS_FN](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html#ga438e7623f4a0dde8f48ce81cc9ecb4d5)

<a id="header-details"></a>

---

[上一章](P075_zephyr__dt-bindings__clock__mspm0_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P077_zephyr__net__net_compat.h_文件参考.md)
