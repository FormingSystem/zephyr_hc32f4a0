---
id: learning.zephyr-docs.timer_reference.api-191
title: 时间感知GPIO公共接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tgpio__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第191章\_时间感知GPIO公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tgpio__interface.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 191.1\_阅读说明与导航

> 译注：本组说明时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）的公共接口、驱动后端（Driver Backend）、结构和源码。对应[周期脉冲与时间戳示例](../driver_samples/P065_时间感知GPIO示例.md)；设备的硬件周期与操作系统时间不能直接混用。

本组：[时间感知GPIO公共接口](P191_时间感知GPIO公共接口.md) · [时间感知GPIO驱动后端](P192_时间感知GPIO驱动后端.md) · [时间感知GPIO驱动接口结构](P193_时间感知GPIO驱动接口结构.md) · [时间感知GPIO头文件参考](P194_时间感知GPIO头文件参考.md) · [时间感知GPIO头文件源码](P195_时间感知GPIO头文件源码.md)。

时间感知GPIO（Time-aware GPIO，TGPIO）控制器接口。

时间感知GPIO（Time-aware GPIO，TGPIO）控制器接口。自Zephyr 3.5起提供（Since）；接口版本（Version）为0.1.0。

## 191.2\_主题（Topics）

<a id="r_tgpio_5Finterface_5Fbackend"></a>

```c
Time-aware GPIO Driver Backend API
```



相关声明：[Time-aware GPIO Driver Backend API](P192_时间感知GPIO驱动后端.md)。

## 191.3\_文件（Files）

<a id="r_timeaware_5Fgpio_2Eh"></a>

```c
file timeaware_gpio.h
```

时间感知GPIO驱动的公共API。

相关声明：[timeaware_gpio.h](P194_时间感知GPIO头文件参考.md)。

## 191.4\_枚举（Enumerations）

<a id="r_gae05efc7d3232c308ae614b73688aa92c"></a>

```c
enum tgpio_pin_polarity { TGPIO_RISING_EDGE = 0 , TGPIO_FALLING_EDGE , TGPIO_TOGGLE_EDGE }
```

事件极性（Event Polarity）。

相关声明：[tgpio_pin_polarity](P191_时间感知GPIO公共接口.md#gae05efc7d3232c308ae614b73688aa92c)、[TGPIO_RISING_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df)、[TGPIO_FALLING_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98)、[TGPIO_TOGGLE_EDGE](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9)。

## 191.5\_函数（Functions）

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

## 191.6\_详细说明（Detailed Documentation）

<a id="gae05efc7d3232c308ae614b73688aa92c"></a>

### [`tgpio\_pin\_polarity`](P191_时间感知GPIO公共接口.md#gae05efc7d3232c308ae614b73688aa92c)

```c
enum tgpio_pin_polarity
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

事件极性（Event Polarity）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| <a id="ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df"></a>[`TGPIO_RISING_EDGE`](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df) | 上升沿（Rising Edge）。 |
| <a id="ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98"></a>[`TGPIO_FALLING_EDGE`](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98) | 下降沿（Falling Edge）。 |
| <a id="ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9"></a>[`TGPIO_TOGGLE_EDGE`](P191_时间感知GPIO公共接口.md#ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9) | 翻转边沿（Toggle Edge）。 |

<a id="ga4c35c5941848a1b060366e6ccb9e655e"></a>

### `tgpio\_pin\_config\_ext\_timestamp()`

```c
int tgpio_pin_config_ext_timestamp ( const struct device * dev, uint32_t pin, uint32_t event_polarity )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

使能或继续引脚上的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `pin` | TGPIO引脚。 |
| `event_polarity` | TGPIO引脚的事件极性。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

> 译注——源码核对：当前Intel实现先禁用该引脚，再根据event_polarity设置输入捕获极性并使能：0为上升沿、1为下降沿，其他值进入翻转边沿分支。应用应使用已定义枚举值；不要把实现没有拒绝其他值理解为API允许任意整数。

<a id="ga724d1410e73eba65c5d343b534424879"></a>

### `tgpio\_pin\_disable()`

```c
int tgpio_pin_disable ( const struct device * dev, uint32_t pin )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

禁用引脚上的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `pin` | TGPIO引脚。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

<a id="gaec3b6161e701b9f2124470da9c202301"></a>

### `tgpio\_pin\_periodic\_output()`

```c
int tgpio_pin_periodic_output ( const struct device * dev, uint32_t pin, uint64_t start_time, uint64_t repeat_interval, bool periodic_enable )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

使能引脚上的周期脉冲生成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `pin` | TGPIO引脚。 |
| `start_time` | 首个脉冲的开始时间，以硬件周期为单位。 |
| `repeat_interval` | 两个脉冲之间的重复间隔，以硬件周期为单位。 |
| `periodic_enable` | 传入true时启用周期模式。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

> 译注——源码核对：start_time和repeat_interval都使用硬件周期单位。当前Intel实现清除周期模式位时仍然设置引脚使能位，因此periodic_enable=false不等同于禁用引脚；停止引脚操作应使用tgpio_pin_disable()。

<a id="ga2f351d5d09b1f5bc7d71bce18979a0c2"></a>

### `tgpio\_pin\_read\_ts\_ec()`

```c
int tgpio_pin_read_ts_ec ( const struct device * dev, uint32_t pin, uint64_t * timestamp, uint64_t * event_count )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

从TGPIO读取时间戳（Timestamp）与事件计数器（Event Counter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `pin` | TGPIO引脚。 |
| `timestamp` | 最近一次接收到的脉冲的时间戳。 |
| `event_count` | 自引脚使能以来接收到的脉冲数量。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

> 译注——源码核对：当前读取的Intel驱动检查pin范围后，直接从regs(dev)加捕获寄存器偏移读取，没有像其他逐引脚操作那样使用pin_regs(addr, pin)。这是所保存实现的差异，尚未做硬件验证；不能由原API的pin参数说明推断该实现已经正确支持任意引脚的独立读数。

<a id="gaccc8c2ed61ffabed71d5a410f10992da"></a>

### `tgpio\_port\_get\_cycles\_per\_second()`

```c
int tgpio_port_get_cycles_per_second ( const struct device * dev, uint32_t * cycles )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

获取当前运行频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `cycles` | 用于保存当前运行频率的指针。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

> 译注——源码核对：当前Intel驱动返回由设备树timer-clock提供的art_clock_freq，用于解释硬件周期单位；这不是函数每次调用都执行一次频率测量。接口版本0.1.0与Zephyr引入版本3.5也不是同一类版本号。

<a id="gaa40a3fef2a4e4e1326a25cc832ff2fb3"></a>

### `tgpio\_port\_get\_time()`

```c
int tgpio_port_get_time ( const struct device * dev, uint64_t * current_time )
```

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

从ART定时器获取时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | TGPIO设备。 |
| `current_time` | 用于保存定时器周期计数值的指针。 |

**返回（Returns）**：成功返回0，失败返回负的errno错误码。

> 译注——源码核对：ART是此硬件的计时来源；返回的current_time是周期计数，不是Unix时间或毫秒值。当前Intel驱动在启用ART捕获控制且捕获等待超时时可能返回-ETIMEDOUT，调用方应先检查返回码，再使用输出值。

## 191.7\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/timeaware_gpio.h)、[驱动实现](../../../drivers/timeaware_gpio/timeaware_gpio_intel.c)和[系统调用验证包装](../../../drivers/timeaware_gpio/timeaware_gpio_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/timeaware_gpio.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_intel.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-groups"></a>
<a id="groups"></a>
<a id="header-files"></a>
<a id="files"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P190_CH32H41x锁相环时钟绑定.md) · [返回大纲](大纲.md) · [下一章](P192_时间感知GPIO驱动后端.md)
