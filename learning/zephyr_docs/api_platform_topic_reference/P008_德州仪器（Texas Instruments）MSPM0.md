---
id: learning.zephyr-docs.api-platform-topic-reference.page-8
title: 德州仪器（Texas Instruments）MSPM0
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_德州仪器（Texas Instruments）MSPM0

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__mspm0.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_mspm0_5Fclock_5Fcontrol_2Eh"></a>

```c
file mspm0_clock_control.h
```

相关声明：[mspm0_clock_control.h](../api_file_supplement_reference/P076_zephyr__drivers__clock_control__mspm0_clock_control.h_文件参考.md)。

Texas Instruments MSPM0设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.2\_数据结构（Data Structures）

<a id="r_mspm0_5Fsys_5Fclock"></a>

```c
struct mspm0_sys_clock
```

相关声明：[mspm0_sys_clock](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md)。

MSPM0系统时钟子系统选择器（Subsystem Selector）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.3\_宏定义（Macros）

<a id="r_ga438e7623f4a0dde8f48ce81cc9ecb4d5"></a>

```c
#define MSPM0_CLOCK_SUBSYS_FN(index)
```

相关声明：[MSPM0_CLOCK_SUBSYS_FN](#ga438e7623f4a0dde8f48ce81cc9ecb4d5)。

根据设备树实例时钟说明符（DT Instance Clock Specifier）初始化 `mspm0_sys_clock`。

## 8.4\_详细说明（Detailed Documentation）

<a id="ga438e7623f4a0dde8f48ce81cc9ecb4d5"></a>

### `MSPM0_CLOCK_SUBSYS_FN`

```c
#define MSPM0_CLOCK_SUBSYS_FN ( index)
```

```c
#include <zephyr/drivers/clock_control/mspm0_clock_control.h>
```

展开值（Value）：

```c
{.clk = DT_INST_CLOCKS_CELL(index, clk)}
```

根据设备树实例时钟说明符（DT Instance Clock Specifier）初始化 `mspm0_sys_clock`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `index` | 设备树实例编号（DT Instance Number）。 |


## 8.5\_原页交叉引用（Cross References）

- [mspm0_clock_control.h](../api_file_supplement_reference/P076_zephyr__drivers__clock_control__mspm0_clock_control.h_文件参考.md)
- [mspm0_sys_clock](../device_power_control_model_reference/P043_mspm0_sys_clock_结构体.md)
- [DT_INST_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#gad6a9584690066548b8d61489ad615a45)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-clocks_html_gad6a9584690066548b8d61489ad615a45"></a>

---

[上一章](P007_兆易创新（GigaDevice）GD32.md) · [返回大纲](大纲.md) · [下一章](P009_新唐 M48x 时钟控制器设备树辅助功能（Devicetree helpers）.md)
