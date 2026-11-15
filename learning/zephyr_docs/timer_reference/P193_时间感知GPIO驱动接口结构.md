---
id: learning.zephyr-docs.timer_reference.api-193
title: 时间感知GPIO驱动接口结构
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtgpio__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第193章\_时间感知GPIO驱动接口结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtgpio__driver__api.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 193.1\_阅读说明与导航

> 译注：本组说明时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）的公共接口、驱动后端（Driver Backend）、结构和源码。对应[周期脉冲与时间戳示例](../driver_samples/P065_时间感知GPIO示例.md)；设备的硬件周期与操作系统时间不能直接混用。

本组：[时间感知GPIO公共接口](P191_时间感知GPIO公共接口.md) · [时间感知GPIO驱动后端](P192_时间感知GPIO驱动后端.md) · [时间感知GPIO驱动接口结构](P193_时间感知GPIO驱动接口结构.md) · [时间感知GPIO头文件参考](P194_时间感知GPIO头文件参考.md) · [时间感知GPIO头文件源码](P195_时间感知GPIO头文件源码.md)。

驱动操作（Driver Operations）：时间感知GPIO驱动操作。

```c
#include <zephyr/drivers/timeaware_gpio.h>
```

驱动操作（Driver Operations）：时间感知GPIO驱动操作。每个时间感知GPIO驱动都需要定义这一驱动API结构。它包含指向驱动实现的操作函数的指针，以及其他驱动专用常量数据。标为`REQ`的成员必须由驱动设置，标为`OPT`的成员则是可选的。另请参阅`DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()`及`DEVICE_API()`。

## 193.2\_数据成员（Data Fields）

<a id="r_aa5f5d8742582025661ad0ac130062994"></a>

```c
int(* pin_disable )(const struct device *dev, uint32_t pin)
```

必需操作（REQ）：禁用引脚上的操作。

相关声明：[pin_disable](P193_时间感知GPIO驱动接口结构.md#aa5f5d8742582025661ad0ac130062994)。

<a id="r_a9fe883efe6974d570f898b82abb285b9"></a>

```c
int(* get_time )(const struct device *dev, uint64_t *current_time)
```

必需操作（REQ）：从ART定时器获取时间。

相关声明：[get_time](P193_时间感知GPIO驱动接口结构.md#a9fe883efe6974d570f898b82abb285b9)。

<a id="r_ab2a9a49e08670bd0b51ce4ae16a23593"></a>

```c
int(* cyc_per_sec )(const struct device *dev, uint32_t *cycles)
```

必需操作（REQ）：获取当前运行频率。

相关声明：[cyc_per_sec](P193_时间感知GPIO驱动接口结构.md#ab2a9a49e08670bd0b51ce4ae16a23593)。

<a id="r_a08f2c18ce774e191cdee1e1baade3d50"></a>

```c
int(* set_perout )(const struct device *dev, uint32_t pin, uint64_t start_time, uint64_t repeat_interval, bool periodic_enable)
```

必需操作（REQ）：使能引脚上的周期脉冲生成。

相关声明：[set_perout](P193_时间感知GPIO驱动接口结构.md#a08f2c18ce774e191cdee1e1baade3d50)。

<a id="r_aededd255140f0e525154c2bb82dbd2d1"></a>

```c
int(* config_ext_ts )(const struct device *dev, uint32_t pin, uint32_t event_polarity)
```

必需操作（REQ）：使能或继续引脚上的操作。

相关声明：[config_ext_ts](P193_时间感知GPIO驱动接口结构.md#aededd255140f0e525154c2bb82dbd2d1)。

<a id="r_ae1878de681a0dd76f0ca4310923083f6"></a>

```c
int(* read_ts_ec )(const struct device *dev, uint32_t pin, uint64_t *timestamp, uint64_t *event_count)
```

必需操作（REQ）：从TGPIO读取时间戳与事件计数器。

相关声明：[read_ts_ec](P193_时间感知GPIO驱动接口结构.md#ae1878de681a0dd76f0ca4310923083f6)。

## 193.3\_详细说明（Detailed Documentation）

<a id="aededd255140f0e525154c2bb82dbd2d1"></a>

### [`config\_ext\_ts`](P193_时间感知GPIO驱动接口结构.md#aededd255140f0e525154c2bb82dbd2d1)

```c
int(* tgpio_driver_api::config_ext_ts) (const struct device *dev, uint32_t pin, uint32_t event_polarity)
```

必需操作（REQ）：使能或继续引脚上的操作。

<a id="ab2a9a49e08670bd0b51ce4ae16a23593"></a>

### [`cyc\_per\_sec`](P193_时间感知GPIO驱动接口结构.md#ab2a9a49e08670bd0b51ce4ae16a23593)

```c
int(* tgpio_driver_api::cyc_per_sec) (const struct device *dev, uint32_t *cycles)
```

必需操作（REQ）：获取当前运行频率。

<a id="a9fe883efe6974d570f898b82abb285b9"></a>

### [`get\_time`](P193_时间感知GPIO驱动接口结构.md#a9fe883efe6974d570f898b82abb285b9)

```c
int(* tgpio_driver_api::get_time) (const struct device *dev, uint64_t *current_time)
```

必需操作（REQ）：从ART定时器获取时间。

<a id="aa5f5d8742582025661ad0ac130062994"></a>

### [`pin\_disable`](P193_时间感知GPIO驱动接口结构.md#aa5f5d8742582025661ad0ac130062994)

```c
int(* tgpio_driver_api::pin_disable) (const struct device *dev, uint32_t pin)
```

必需操作（REQ）：禁用引脚上的操作。

<a id="ae1878de681a0dd76f0ca4310923083f6"></a>

### [`read\_ts\_ec`](P193_时间感知GPIO驱动接口结构.md#ae1878de681a0dd76f0ca4310923083f6)

```c
int(* tgpio_driver_api::read_ts_ec) (const struct device *dev, uint32_t pin, uint64_t *timestamp, uint64_t *event_count)
```

必需操作（REQ）：从TGPIO读取时间戳与事件计数器。

<a id="a08f2c18ce774e191cdee1e1baade3d50"></a>

### [`set\_perout`](P193_时间感知GPIO驱动接口结构.md#a08f2c18ce774e191cdee1e1baade3d50)

```c
int(* tgpio_driver_api::set_perout) (const struct device *dev, uint32_t pin, uint64_t start_time, uint64_t repeat_interval, bool periodic_enable)
```

必需操作（REQ）：使能引脚上的周期脉冲生成。

## 193.4\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/timeaware_gpio.h)、[驱动实现](../../../drivers/timeaware_gpio/timeaware_gpio_intel.c)和[系统调用验证包装](../../../drivers/timeaware_gpio/timeaware_gpio_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/timeaware_gpio.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_intel.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P192_时间感知GPIO驱动后端.md) · [返回大纲](大纲.md) · [下一章](P194_时间感知GPIO头文件参考.md)
