---
id: learning.zephyr-docs.timer_reference.api-195
title: 时间感知GPIO头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/timeaware__gpio_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第195章\_时间感知GPIO头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/timeaware__gpio_8h_source.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 195.1\_阅读说明与导航

> 译注：本组说明时间感知通用输入输出（Time-aware General-Purpose Input/Output，TGPIO）的公共接口、驱动后端（Driver Backend）、结构和源码。对应[周期脉冲与时间戳示例](../driver_samples/P065_时间感知GPIO示例.md)；设备的硬件周期与操作系统时间不能直接混用。

本组：[时间感知GPIO公共接口](P191_时间感知GPIO公共接口.md) · [时间感知GPIO驱动后端](P192_时间感知GPIO驱动后端.md) · [时间感知GPIO驱动接口结构](P193_时间感知GPIO驱动接口结构.md) · [时间感知GPIO头文件参考](P194_时间感知GPIO头文件参考.md) · [时间感知GPIO头文件源码](P195_时间感知GPIO头文件源码.md)。

下方保留官方Doxygen源码浏览页的全部代码、标识符和版权／许可注释，仅移除展示行号、还原不换行空格并清除行尾空白。网页本身省略了部分用于生成API说明的注释；这里不把展示代码冒充完整原始头文件。被省略的接口说明在本组参考页中翻译。

## 195.2\_官方源码展示

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00050"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__tgpio__interface_html_ga2f351d5d09b1f5bc7d71bce18979a0c2"></a>
<a id="agroup__tgpio__interface_html_ga4c35c5941848a1b060366e6ccb9e655e"></a>
<a id="agroup__tgpio__interface_html_ga724d1410e73eba65c5d343b534424879"></a>
<a id="agroup__tgpio__interface_html_gaa40a3fef2a4e4e1326a25cc832ff2fb3"></a>
<a id="agroup__tgpio__interface_html_gaccc8c2ed61ffabed71d5a410f10992da"></a>
<a id="agroup__tgpio__interface_html_gae05efc7d3232c308ae614b73688aa92c"></a>
<a id="agroup__tgpio__interface_html_gaec3b6161e701b9f2124470da9c202301"></a>
<a id="agroup__tgpio__interface_html_ggae05efc7d3232c308ae614b73688aa92ca086ec340d826c60beaa5e443700835f9"></a>
<a id="agroup__tgpio__interface_html_ggae05efc7d3232c308ae614b73688aa92ca2aa85b802bfd1e321d76811e749198df"></a>
<a id="agroup__tgpio__interface_html_ggae05efc7d3232c308ae614b73688aa92caec8ab610f2d8ad6df38fb59b76471f98"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructdevice_html"></a>
<a id="astructtgpio__driver__api_html"></a>
<a id="astructtgpio__driver__api_html_a08f2c18ce774e191cdee1e1baade3d50"></a>
<a id="astructtgpio__driver__api_html_a9fe883efe6974d570f898b82abb285b9"></a>
<a id="astructtgpio__driver__api_html_aa5f5d8742582025661ad0ac130062994"></a>
<a id="astructtgpio__driver__api_html_ab2a9a49e08670bd0b51ce4ae16a23593"></a>
<a id="astructtgpio__driver__api_html_ae1878de681a0dd76f0ca4310923083f6"></a>
<a id="astructtgpio__driver__api_html_aededd255140f0e525154c2bb82dbd2d1"></a>
<a id="asyscall__handler_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_DRIVERS_MISC_TIMEAWARE_GPIO_TIMEAWARE_GPIO
#define ZEPHYR_DRIVERS_MISC_TIMEAWARE_GPIO_TIMEAWARE_GPIO


#include <zephyr/sys/__assert.h>
#include <zephyr/sys/slist.h>

#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/internal/syscall_handler.h>

#ifdef __cplusplus
extern "C" {
#endif

enum tgpio_pin_polarity {
        TGPIO_RISING_EDGE = 0,
        TGPIO_FALLING_EDGE,
        TGPIO_TOGGLE_EDGE,
};


__subsystem struct tgpio_driver_api {
        int (*pin_disable)(const struct device *dev, uint32_t pin);
        int (*get_time)(const struct device *dev, uint64_t *current_time);
        int (*cyc_per_sec)(const struct device *dev, uint32_t *cycles);
        int (*set_perout)(const struct device *dev, uint32_t pin, uint64_t start_time,
                          uint64_t repeat_interval, bool periodic_enable);
        int (*config_ext_ts)(const struct device *dev, uint32_t pin, uint32_t event_polarity);
        int (*read_ts_ec)(const struct device *dev, uint32_t pin, uint64_t *timestamp,
                          uint64_t *event_count);
};


__syscall int tgpio_port_get_time(const struct device *dev, uint64_t *current_time);

static inline int z_impl_tgpio_port_get_time(const struct device *dev, uint64_t *current_time)
{
        return DEVICE_API_GET(tgpio, dev)->get_time(dev, current_time);
}

__syscall int tgpio_port_get_cycles_per_second(const struct device *dev, uint32_t *cycles);

static inline int z_impl_tgpio_port_get_cycles_per_second(const struct device *dev,
                                                           uint32_t *cycles)
{
        return DEVICE_API_GET(tgpio, dev)->cyc_per_sec(dev, cycles);
}

__syscall int tgpio_pin_disable(const struct device *dev, uint32_t pin);

static inline int z_impl_tgpio_pin_disable(const struct device *dev, uint32_t pin)
{
        return DEVICE_API_GET(tgpio, dev)->pin_disable(dev, pin);
}

__syscall int tgpio_pin_config_ext_timestamp(const struct device *dev, uint32_t pin,
                                              uint32_t event_polarity);

static inline int z_impl_tgpio_pin_config_ext_timestamp(const struct device *dev, uint32_t pin,
                                                         uint32_t event_polarity)
{
        return DEVICE_API_GET(tgpio, dev)->config_ext_ts(dev, pin, event_polarity);
}

__syscall int tgpio_pin_periodic_output(const struct device *dev, uint32_t pin,
                                         uint64_t start_time, uint64_t repeat_interval,
                                         bool periodic_enable);

static inline int z_impl_tgpio_pin_periodic_output(const struct device *dev, uint32_t pin,
                                                    uint64_t start_time, uint64_t repeat_interval,
                                                    bool periodic_enable)
{
        return DEVICE_API_GET(tgpio, dev)->set_perout(dev, pin, start_time, repeat_interval,
                                                      periodic_enable);
}

__syscall int tgpio_pin_read_ts_ec(const struct device *dev, uint32_t pin, uint64_t *timestamp,
                                    uint64_t *event_count);

static inline int z_impl_tgpio_pin_read_ts_ec(const struct device *dev, uint32_t pin,
                                               uint64_t *timestamp, uint64_t *event_count)
{
        return DEVICE_API_GET(tgpio, dev)->read_ts_ec(dev, pin, timestamp, event_count);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/timeaware_gpio.h>

#endif /* ZEPHYR_DRIVERS_MISC_TIMEAWARE_GPIO_TIMEAWARE_GPIO */
```

## 195.3\_注释与条件说明

版权为2023年Intel Corporation；许可证标识为`Apache-2.0`，原署名保持不变。包含保护宏为`ZEPHYR_DRIVERS_MISC_TIMEAWARE_GPIO_TIMEAWARE_GPIO`。六个操作指针由驱动实现，公共`__syscall`声明及`z_impl_*`转发函数保留；`extern "C"`为C++调用方指定C链接约定，末尾包含生成的系统调用头文件。事件极性、操作参数和驱动必需成员的注释已在本组对应接口与结构页翻译。

## 195.4\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/timeaware_gpio.h)、[驱动实现](../../../drivers/timeaware_gpio/timeaware_gpio_intel.c)和[系统调用验证包装](../../../drivers/timeaware_gpio/timeaware_gpio_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/timeaware_gpio.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_intel.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/timeaware_gpio/timeaware_gpio_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

[上一章](P194_时间感知GPIO头文件参考.md) · [返回大纲](大纲.md)
