---
id: learning.zephyr-docs.api-file-service-interface-reference.page-3
title: zephyr__drivers__clock_control__adi_max32_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_drivers\_\_clock\_control\_\_adi\_max32\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adi__max32__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices MAX32设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/drivers/clock_control.h>
#include <zephyr/dt-bindings/clock/adi_max32_clock.h>
#include <wrap_max32_sys.h>
```

查看此文件的源码。

Analog Devices MAX32设备的时钟控制定义（Clock Control Definitions）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_max32_5Fperclk"></a>

```c
struct max32_perclk
```

相关声明：[max32_perclk](../device_power_control_model_reference/P025_max32_perclk_结构体.md)。

MAX32设备的外设时钟描述符（Peripheral Clock Descriptor）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_ga41eab4d492a019700d1e1d4714932cd9"></a>

```c
#define ADI_MAX32_SYSCLK_PRESCALER DT_PROP_OR(DT_NODELABEL(gcr), sysclk_prescaler, 1)
```

相关声明：[ADI_MAX32_SYSCLK_PRESCALER](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga41eab4d492a019700d1e1d4714932cd9)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

系统时钟预分频值（prescaler）；设备树未设置时默认为 1。

<a id="r_ga31a7fbb2f0c1ce1f5b9899b49b6324ec"></a>

```c
#define ADI_MAX32_CLK_IPO_FREQ DT_PROP(DT_NODELABEL(clk_ipo), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_IPO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga31a7fbb2f0c1ce1f5b9899b49b6324ec)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部主振荡器（IPO）频率，单位为 Hz。

<a id="r_ga56a549a210a78cb99f019f85fa15807b"></a>

```c
#define ADI_MAX32_CLK_ERFO_FREQ DT_PROP_OR(DT_NODELABEL(clk_erfo), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_ERFO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga56a549a210a78cb99f019f85fa15807b)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部射频振荡器（ERFO）频率，单位为 Hz；不存在时为 0。

<a id="r_gae5e0473609734b17bcdd2ce6f4e7a63a"></a>

```c
#define ADI_MAX32_CLK_IBRO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ibro), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_IBRO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gae5e0473609734b17bcdd2ce6f4e7a63a)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部波特率振荡器（IBRO）频率，单位为 Hz；不存在时为 0。

<a id="r_gace96ad0d7564ad0fe326992257686820"></a>

```c
#define ADI_MAX32_CLK_ISO_FREQ DT_PROP_OR(DT_NODELABEL(clk_iso), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_ISO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gace96ad0d7564ad0fe326992257686820)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部次级振荡器（ISO）频率，单位为 Hz；不存在时为 0。

<a id="r_gabb3947e441021737ca566e89fd56cb0c"></a>

```c
#define ADI_MAX32_CLK_INRO_FREQ DT_PROP(DT_NODELABEL(clk_inro), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_INRO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gabb3947e441021737ca566e89fd56cb0c)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部纳米环形振荡器（INRO）频率，单位为 Hz。

<a id="r_ga664282617e29d44f951a48da1ac1ae9d"></a>

```c
#define ADI_MAX32_CLK_ERTCO_FREQ DT_PROP(DT_NODELABEL(clk_ertco), clock_frequency)
```

相关声明：[ADI_MAX32_CLK_ERTCO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga664282617e29d44f951a48da1ac1ae9d)、[DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部实时时钟振荡器（ERTCO）频率，单位为 Hz。

<a id="r_gaa58ed1a1d381f11cd6410797449b17ba"></a>

```c
#define ADI_MAX32_CLK_IPLL_FREQ DT_PROP_OR(DT_NODELABEL(clk_ipll), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_IPLL_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gaa58ed1a1d381f11cd6410797449b17ba)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

内部锁相环（IPLL）频率，单位为 Hz；不存在时为 0。

<a id="r_ga47709e72b60d70e0d07576b8787118e0"></a>

```c
#define ADI_MAX32_CLK_EBO_FREQ DT_PROP_OR(DT_NODELABEL(clk_ebo), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_EBO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga47709e72b60d70e0d07576b8787118e0)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部蓝牙低功耗振荡器（EBO）频率，单位为 Hz；不存在时为 0。

<a id="r_ga158271c4ced07ddeda9e677f7fd028c7"></a>

```c
#define ADI_MAX32_CLK_EXTCLK_FREQ DT_PROP_OR(DT_NODELABEL(clk_extclk), clock_frequency, 0)
```

相关声明：[ADI_MAX32_CLK_EXTCLK_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga158271c4ced07ddeda9e677f7fd028c7)、[DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

外部时钟输入频率，单位为 Hz；不存在时为 0。


## 3.3\_原页交叉引用（Cross References）

- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [zephyr/dt-bindings/clock/adi_max32_clock.h](../api_source_timing_sensor_reference/P001_adi_max32_clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P008_adi_max32_clock_control.h_源码浏览.md)
- [max32_perclk](../device_power_control_model_reference/P025_max32_perclk_结构体.md)
- [ADI_MAX32_SYSCLK_PRESCALER](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga41eab4d492a019700d1e1d4714932cd9)
- [DT_PROP_OR](../dt_property_reference/P001_设备树属性读取宏.md#ga5e5bfc9b1a6627b3f73014329e96340f)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [ADI_MAX32_CLK_IPO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga31a7fbb2f0c1ce1f5b9899b49b6324ec)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [ADI_MAX32_CLK_ERFO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga56a549a210a78cb99f019f85fa15807b)
- [ADI_MAX32_CLK_IBRO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gae5e0473609734b17bcdd2ce6f4e7a63a)
- [ADI_MAX32_CLK_ISO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gace96ad0d7564ad0fe326992257686820)
- [ADI_MAX32_CLK_INRO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gabb3947e441021737ca566e89fd56cb0c)
- [ADI_MAX32_CLK_ERTCO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga664282617e29d44f951a48da1ac1ae9d)
- [ADI_MAX32_CLK_IPLL_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#gaa58ed1a1d381f11cd6410797449b17ba)
- [ADI_MAX32_CLK_EBO_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga47709e72b60d70e0d07576b8787118e0)
- [ADI_MAX32_CLK_EXTCLK_FREQ](../api_network_time_topic_reference/P006_亚德诺（Analog Devices）MAX32.md#ga158271c4ced07ddeda9e677f7fd028c7)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__mfd__ad559x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__sensor__adxl313.h_文件参考.md)
