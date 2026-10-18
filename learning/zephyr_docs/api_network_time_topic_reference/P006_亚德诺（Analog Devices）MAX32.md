---
id: learning.zephyr-docs.api-network-time-topic-reference.page-6
title: 亚德诺（Analog Devices）MAX32
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adi__max32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_亚德诺（Analog Devices）MAX32

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__adi__max32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_adi_5Fmax32_5Fclock_5Fcontrol_2Eh"></a>

```c
file adi_max32_clock_control.h
```

相关声明：[adi_max32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html)。

Analog Devices MAX32设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_max32_5Fperclk"></a>

```c
struct max32_perclk
```

相关声明：[max32_perclk](../device_power_control_model_reference/P025_max32_perclk_结构体.md)。

MAX32设备的外设时钟描述符（Peripheral Clock Descriptor）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga41eab4d492a019700d1e1d4714932cd9"></a>

```c
#define ADI_MAX32_SYSCLK_PRESCALER DT_PROP_OR(DT_NODELABEL(gcr), sysclk_prescaler, 1)
```

相关声明：[ADI_MAX32_SYSCLK_PRESCALER](#ga41eab4d492a019700d1e1d4714932cd9)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

系统时钟预分频值（prescaler）；设备树未设置时默认为 1。

<a id="r_ga31a7fbb2f0c1ce1f5b9899b49b6324ec"></a>

```c
#define ADI_MAX32_CLK_IPO_FREQ DT_PROP(DT_NODELABEL(clk_ipo), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_IPO_FREQ](#ga31a7fbb2f0c1ce1f5b9899b49b6324ec)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部主振荡器（IPO）频率，单位为 Hz。

<a id="r_ga56a549a210a78cb99f019f85fa15807b"></a>

```c
#define ADI_MAX32_CLK_ERFO_FREQ DT_PROP_OR(DT_NODELABEL(clk_erfo), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_ERFO_FREQ](#ga56a549a210a78cb99f019f85fa15807b)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部射频振荡器（ERFO）频率，单位为 Hz；不存在时为 0。

<a id="r_gae5e0473609734b17bcdd2ce6f4e7a63a"></a>

```c
#define ADI_MAX32_CLK_IBRO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ibro), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_IBRO_FREQ](#gae5e0473609734b17bcdd2ce6f4e7a63a)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部波特率振荡器（IBRO）频率，单位为 Hz；不存在时为 0。

<a id="r_gace96ad0d7564ad0fe326992257686820"></a>

```c
#define ADI_MAX32_CLK_ISO_FREQ DT_PROP_OR(DT_NODELABEL(clk_iso), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_ISO_FREQ](#gace96ad0d7564ad0fe326992257686820)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部次级振荡器（ISO）频率，单位为 Hz；不存在时为 0。

<a id="r_gabb3947e441021737ca566e89fd56cb0c"></a>

```c
#define ADI_MAX32_CLK_INRO_FREQ DT_PROP(DT_NODELABEL(clk_inro), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_INRO_FREQ](#gabb3947e441021737ca566e89fd56cb0c)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部纳米环形振荡器（INRO）频率，单位为 Hz。

<a id="r_ga664282617e29d44f951a48da1ac1ae9d"></a>

```c
#define ADI_MAX32_CLK_ERTCO_FREQ DT_PROP(DT_NODELABEL(clk_ertco), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_ERTCO_FREQ](#ga664282617e29d44f951a48da1ac1ae9d)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部实时时钟振荡器（ERTCO）频率，单位为 Hz。

<a id="r_gaa58ed1a1d381f11cd6410797449b17ba"></a>

```c
#define ADI_MAX32_CLK_IPLL_FREQ DT_PROP_OR(DT_NODELABEL(clk_ipll), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_IPLL_FREQ](#gaa58ed1a1d381f11cd6410797449b17ba)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部锁相环（IPLL）频率，单位为 Hz；不存在时为 0。

<a id="r_ga47709e72b60d70e0d07576b8787118e0"></a>

```c
#define ADI_MAX32_CLK_EBO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ebo), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_EBO_FREQ](#ga47709e72b60d70e0d07576b8787118e0)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部蓝牙低功耗振荡器（EBO）频率，单位为 Hz；不存在时为 0。

<a id="r_ga158271c4ced07ddeda9e677f7fd028c7"></a>

```c
#define ADI_MAX32_CLK_EXTCLK_FREQ DT_PROP_OR(DT_NODELABEL(clk_extclk), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_EXTCLK_FREQ](#ga158271c4ced07ddeda9e677f7fd028c7)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部时钟输入频率，单位为 Hz；不存在时为 0。

## 6.4\_详细说明（Detailed Documentation）

<a id="ga47709e72b60d70e0d07576b8787118e0"></a>

### `ADI_MAX32_CLK_EBO_FREQ`

```c
#define ADI_MAX32_CLK_EBO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ebo), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

外部蓝牙低功耗振荡器（EBO）频率，单位为 Hz；不存在时为 0。

<a id="ga56a549a210a78cb99f019f85fa15807b"></a>

### `ADI_MAX32_CLK_ERFO_FREQ`

```c
#define ADI_MAX32_CLK_ERFO_FREQ DT_PROP_OR(DT_NODELABEL(clk_erfo), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

外部射频振荡器（ERFO）频率，单位为 Hz；不存在时为 0。

<a id="ga664282617e29d44f951a48da1ac1ae9d"></a>

### `ADI_MAX32_CLK_ERTCO_FREQ`

```c
#define ADI_MAX32_CLK_ERTCO_FREQ DT_PROP(DT_NODELABEL(clk_ertco), clock_frequency)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

外部实时时钟振荡器（ERTCO）频率，单位为 Hz。

<a id="ga158271c4ced07ddeda9e677f7fd028c7"></a>

### `ADI_MAX32_CLK_EXTCLK_FREQ`

```c
#define ADI_MAX32_CLK_EXTCLK_FREQ DT_PROP_OR(DT_NODELABEL(clk_extclk), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

外部时钟输入频率，单位为 Hz；不存在时为 0。

<a id="gae5e0473609734b17bcdd2ce6f4e7a63a"></a>

### `ADI_MAX32_CLK_IBRO_FREQ`

```c
#define ADI_MAX32_CLK_IBRO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ibro), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

内部波特率振荡器（IBRO）频率，单位为 Hz；不存在时为 0。

<a id="gabb3947e441021737ca566e89fd56cb0c"></a>

### `ADI_MAX32_CLK_INRO_FREQ`

```c
#define ADI_MAX32_CLK_INRO_FREQ DT_PROP(DT_NODELABEL(clk_inro), clock_frequency)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

内部纳米环形振荡器（INRO）频率，单位为 Hz。

<a id="gaa58ed1a1d381f11cd6410797449b17ba"></a>

### `ADI_MAX32_CLK_IPLL_FREQ`

```c
#define ADI_MAX32_CLK_IPLL_FREQ DT_PROP_OR(DT_NODELABEL(clk_ipll), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

内部锁相环（IPLL）频率，单位为 Hz；不存在时为 0。

<a id="ga31a7fbb2f0c1ce1f5b9899b49b6324ec"></a>

### `ADI_MAX32_CLK_IPO_FREQ`

```c
#define ADI_MAX32_CLK_IPO_FREQ DT_PROP(DT_NODELABEL(clk_ipo), clock_frequency)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

内部主振荡器（IPO）频率，单位为 Hz。

<a id="gace96ad0d7564ad0fe326992257686820"></a>

### `ADI_MAX32_CLK_ISO_FREQ`

```c
#define ADI_MAX32_CLK_ISO_FREQ DT_PROP_OR(DT_NODELABEL(clk_iso), clock_frequency, 0)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

内部次级振荡器（ISO）频率，单位为 Hz；不存在时为 0。

<a id="ga41eab4d492a019700d1e1d4714932cd9"></a>

### `ADI_MAX32_SYSCLK_PRESCALER`

```c
#define ADI_MAX32_SYSCLK_PRESCALER DT_PROP_OR(DT_NODELABEL(gcr), sysclk_prescaler, 1)
```

```c
#include <zephyr/drivers/clock_control/adi_max32_clock_control.h>
```

系统时钟预分频值（prescaler）；设备树未设置时默认为 1。


## 6.5\_原页交叉引用（Cross References）

- [adi_max32_clock_control.h](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html)
- [max32_perclk](../device_power_control_model_reference/P025_max32_perclk_结构体.md)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_蜂窝通信驱动后端 API（Cellular Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P007_德州仪器（TI）.md)
