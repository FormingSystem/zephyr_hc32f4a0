---
id: learning.zephyr-docs.timer_reference.api-194
title: 时间感知GPIO头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/timeaware__gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第194章\_时间感知GPIO头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/timeaware__gpio_8h.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 194.1\_阅读说明与导航

> 译注：本组说明时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）的公共接口、驱动后端（Driver Backend）、结构和源码。对应[周期脉冲与时间戳示例](../driver_samples/P065_时间感知GPIO示例.md)；设备的硬件周期与操作系统时间不能直接混用。

本组：[时间感知GPIO公共接口](P191_时间感知GPIO公共接口.md) · [时间感知GPIO驱动后端](P192_时间感知GPIO驱动后端.md) · [时间感知GPIO驱动接口结构](P193_时间感知GPIO驱动接口结构.md) · [时间感知GPIO头文件参考](P194_时间感知GPIO头文件参考.md) · [时间感知GPIO头文件源码](P195_时间感知GPIO头文件源码.md)。

时间感知GPIO驱动的公共API。

```c
#include <zephyr/sys/__assert.h>
```

```c
#include <zephyr/sys/slist.h>
```

```c
#include <zephyr/types.h>
```

```c
#include <stddef.h>
```

```c
#include <zephyr/device.h>
```

```c
#include <zephyr/internal/syscall_handler.h>
```

```c
#include <zephyr/syscalls/timeaware_gpio.h>
```

时间感知GPIO驱动的公共API。

## 194.2\_数据结构（Data Structures）

<a id="r_tgpio_5Fdriver_5Fapi"></a>

```c
struct tgpio_driver_api
```

驱动操作（Driver Operations）：时间感知GPIO驱动操作。

相关声明：[tgpio_driver_api](P193_时间感知GPIO驱动接口结构.md)。

## 194.3\_枚举（Enumerations）

<a id="r_gae05efc7d3232c308ae614b73688aa92c"></a>

```c
enum tgpio_pin_polarity { TGPIO_RISING_EDGE = 0 , TGPIO_FALLING_EDGE , TGPIO_TOGGLE_EDGE }
```

事件极性（Event Polarity）。

相关声明：[tgpio_pin_polarity](P191_时间感知GPIO公共接口.md#gae05efc7d3232c308ae614b73688aa92c)、[TGPIO_RISING_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df)、[TGPIO_FALLING_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98)、[TGPIO_TOGGLE_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9)。

## 194.4\_函数（Functions）

<a id="r_gaa40a3fef2a4e4e1326a25cc832ff2fb3"></a>

```c
int tgpio_port_get_time (const struct device *dev, uint64_t *current_time)
```

从ART定时器获取时间。

相关声明：[tgpio_port_get_time](P191_时间感知GPIO公共接口.md#gaa40a3fef2a4e4e1326a25cc832ff2fb3)。

<a id="r_gaccc8c2ed61ffabed71d5a410f10992da"></a>

```c
int tgpio_port_get_cycles_per_second (const struct device *dev, uint32_t *cycles)
```

获取当前运行频率。

相关声明：[tgpio_port_get_cycles_per_second](P191_时间感知GPIO公共接口.md#gaccc8c2ed61ffabed71d5a410f10992da)。

<a id="r_ga724d1410e73eba65c5d343b534424879"></a>

```c
int tgpio_pin_disable (const struct device *dev, uint32_t pin)
```

禁用引脚上的操作。

相关声明：[tgpio_pin_disable](P191_时间感知GPIO公共接口.md#ga724d1410e73eba65c5d343b534424879)。

<a id="r_ga4c35c5941848a1b060366e6ccb9e655e"></a>

```c
int tgpio_pin_config_ext_timestamp (const struct device *dev, uint32_t pin, uint32_t event_polarity)
```

使能或继续引脚上的操作。

相关声明：[tgpio_pin_config_ext_timestamp](P191_时间感知GPIO公共接口.md#ga4c35c5941848a1b060366e6ccb9e655e)。

<a id="r_gaec3b6161e701b9f2124470da9c202301"></a>

```c
int tgpio_pin_periodic_output (const struct device *dev, uint32_t pin, uint64_t start_time, uint64_t repeat_interval, bool periodic_enable)
```

使能引脚上的周期脉冲生成。

相关声明：[tgpio_pin_periodic_output](P191_时间感知GPIO公共接口.md#gaec3b6161e701b9f2124470da9c202301)。

<a id="r_ga2f351d5d09b1f5bc7d71bce18979a0c2"></a>

```c
int tgpio_pin_read_ts_ec (const struct device *dev, uint32_t pin, uint64_t *timestamp, uint64_t *event_count)
```

从TGPIO读取时间戳（Timestamp）与事件计数器（Event Counter）。

相关声明：[tgpio_pin_read_ts_ec](P191_时间感知GPIO公共接口.md#ga2f351d5d09b1f5bc7d71bce18979a0c2)。

## 194.5\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/timeaware_gpio.h)、[驱动实现](../../../drivers/timeaware_gpio/timeaware_gpio_intel.c)和[系统调用验证包装](../../../drivers/timeaware_gpio/timeaware_gpio_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/timeaware_gpio.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_intel.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P193_时间感知GPIO驱动接口结构.md) · [返回大纲](大纲.md) · [下一章](P195_时间感知GPIO头文件源码.md)
