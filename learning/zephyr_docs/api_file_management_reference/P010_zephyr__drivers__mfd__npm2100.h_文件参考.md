---
id: learning.zephyr-docs.api-file-management-reference.page-10
title: zephyr__drivers__mfd__npm2100.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm2100_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_mfd\_\_npm2100.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mfd_2npm2100_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.1\_枚举（Enumerations）

<a id="r_gae7433fd9cb33e7b3ac0b364d29dc6e32"></a>

```c
enum mfd_npm2100_event { NPM2100_EVENT_SYS_DIETEMP_WARN , NPM2100_EVENT_SYS_SHIPHOLD_FALL , NPM2100_EVENT_SYS_SHIPHOLD_RISE , NPM2100_EVENT_SYS_PGRESET_FALL , NPM2100_EVENT_SYS_PGRESET_RISE , NPM2100_EVENT_SYS_TIMER_EXPIRY , NPM2100_EVENT_ADC_VBAT_READY , NPM2100_EVENT_ADC_DIETEMP_READY , NPM2100_EVENT_ADC_DROOP_DETECT , NPM2100_EVENT_ADC_VOUT_READY , NPM2100_EVENT_GPIO0_FALL , NPM2100_EVENT_GPIO0_RISE , NPM2100_EVENT_GPIO1_FALL , NPM2100_EVENT_GPIO1_RISE , NPM2100_EVENT_BOOST_VBAT_WARN , NPM2100_EVENT_BOOST_VOUT_MIN , NPM2100_EVENT_BOOST_VOUT_WARN , NPM2100_EVENT_BOOST_VOUT_DPS , NPM2100_EVENT_BOOST_VOUT_OK , NPM2100_EVENT_LDOSW_OCP , NPM2100_EVENT_LDOSW_VINTFAIL , NPM2100_EVENT_MAX }
```

相关声明：[mfd_npm2100_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gae7433fd9cb33e7b3ac0b364d29dc6e32)、[NPM2100_EVENT_SYS_DIETEMP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88)、[NPM2100_EVENT_SYS_SHIPHOLD_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff)、[NPM2100_EVENT_SYS_SHIPHOLD_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d)、[NPM2100_EVENT_SYS_PGRESET_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443)、[NPM2100_EVENT_SYS_PGRESET_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b)、[NPM2100_EVENT_SYS_TIMER_EXPIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a)、[NPM2100_EVENT_ADC_VBAT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878)、[NPM2100_EVENT_ADC_DIETEMP_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68)、[NPM2100_EVENT_ADC_DROOP_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49)、[NPM2100_EVENT_ADC_VOUT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c)、[NPM2100_EVENT_GPIO0_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333)、[NPM2100_EVENT_GPIO0_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f)、[NPM2100_EVENT_GPIO1_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453)、[NPM2100_EVENT_GPIO1_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25)、[NPM2100_EVENT_BOOST_VBAT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6)、[NPM2100_EVENT_BOOST_VOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948)、[NPM2100_EVENT_BOOST_VOUT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687)、[NPM2100_EVENT_BOOST_VOUT_DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8)、[NPM2100_EVENT_BOOST_VOUT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883)、[NPM2100_EVENT_LDOSW_OCP](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2)、[NPM2100_EVENT_LDOSW_VINTFAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f)、[NPM2100_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81)。

<a id="r_ga6a89922f19450ace9d83a4e110625cfb"></a>

```c
enum mfd_npm2100_timer_mode { NPM2100_TIMER_MODE_GENERAL_PURPOSE , NPM2100_TIMER_MODE_WDT_RESET , NPM2100_TIMER_MODE_WDT_POWER_CYCLE , NPM2100_TIMER_MODE_WAKEUP }
```

相关声明：[mfd_npm2100_timer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga6a89922f19450ace9d83a4e110625cfb)、[NPM2100_TIMER_MODE_GENERAL_PURPOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d)、[NPM2100_TIMER_MODE_WDT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6)、[NPM2100_TIMER_MODE_WDT_POWER_CYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c)、[NPM2100_TIMER_MODE_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.2\_函数（Functions）

<a id="r_gaa684cdb822e0e36fefc74b59bfd2b706"></a>

```c
int mfd_npm2100_set_timer (const struct device *dev, uint32_t time_ms, enum mfd_npm2100_timer_mode mode)
```

相关声明：[mfd_npm2100_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gaa684cdb822e0e36fefc74b59bfd2b706)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mfd_npm2100_timer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga6a89922f19450ace9d83a4e110625cfb)。

写入 nPM2100 定时器寄存器（timer register）。

<a id="r_ga085bc3c2d5d775c55ae598a464c9d265"></a>

```c
int mfd_npm2100_start_timer (const struct device *dev)
```

相关声明：[mfd_npm2100_start_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga085bc3c2d5d775c55ae598a464c9d265)、[device](../device_reference/P002_设备对象结构.md)。

启动 nPM2100 定时器。

<a id="r_gac87a33389dfbf30e7f0059bd6aede7dc"></a>

```c
int mfd_npm2100_reset (const struct device *dev)
```

相关声明：[mfd_npm2100_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gac87a33389dfbf30e7f0059bd6aede7dc)、[device](../device_reference/P002_设备对象结构.md)。

nPM2100 完全电源复位（full power reset）。

<a id="r_ga4d34ac6e2c185976bc696ce0091b375a"></a>

```c
int mfd_npm2100_hibernate (const struct device *dev, uint32_t time_ms, bool pass_through)
```

相关声明：[mfd_npm2100_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga4d34ac6e2c185976bc696ce0091b375a)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

nPM2100 休眠（hibernate）。

<a id="r_ga137976d9909ad6ec179dce5722c4b865"></a>

```c
int mfd_npm2100_add_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm2100_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga137976d9909ad6ec179dce5722c4b865)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

添加 nPM2100 事件回调（event callback）。

<a id="r_ga342de8853f0afd2cdab08d2d42883b47"></a>

```c
int mfd_npm2100_remove_callback (const struct device *dev, struct gpio_callback *callback)
```

相关声明：[mfd_npm2100_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga342de8853f0afd2cdab08d2d42883b47)、[device](../device_reference/P002_设备对象结构.md)、[gpio_callback](../hardware/P270_GPIO回调结构.md)。

移除 nPM2100 事件回调。


## 10.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P163_npm2100.h_源码浏览.md)
- [mfd_npm2100_event](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gae7433fd9cb33e7b3ac0b364d29dc6e32)
- [NPM2100_EVENT_SYS_DIETEMP_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a40949e797419f2e317d49aad99ea5a88)
- [NPM2100_EVENT_SYS_SHIPHOLD_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a51417298380c8aa90363d42370da3eff)
- [NPM2100_EVENT_SYS_SHIPHOLD_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae70e607cc5cab890f3ee0388d192cd8d)
- [NPM2100_EVENT_SYS_PGRESET_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac16dbc92e22bfe720f00c7accd310443)
- [NPM2100_EVENT_SYS_PGRESET_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a15406e035cadb7b3db4ffdcbc5b0dd4b)
- [NPM2100_EVENT_SYS_TIMER_EXPIRY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1cc0fb1202d777d1d15f866ef28eae4a)
- [NPM2100_EVENT_ADC_VBAT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b7adcddff5f20f35c421c9a0e296878)
- [NPM2100_EVENT_ADC_DIETEMP_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a3508143e9a6cc45aab022cb1d41c1f68)
- [NPM2100_EVENT_ADC_DROOP_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a1760e35770442b55a82176fbf8e18b49)
- [NPM2100_EVENT_ADC_VOUT_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a739b885852e147e69b3bf638fd41f11c)
- [NPM2100_EVENT_GPIO0_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a5685e6db1ae012bf52fe84564e6d1333)
- [NPM2100_EVENT_GPIO0_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a2b942a768806d76a82dfcdb5e657f60f)
- [NPM2100_EVENT_GPIO1_FALL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a66f462631778912d296b94639be9e453)
- [NPM2100_EVENT_GPIO1_RISE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a244e3e287d8657bfde5696b9a59d0a25)
- [NPM2100_EVENT_BOOST_VBAT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ada55f1aadb3d0159ca93512fa8ca37e6)
- [NPM2100_EVENT_BOOST_VOUT_MIN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ae903153d89f42a509fb2c12e5d58d948)
- [NPM2100_EVENT_BOOST_VOUT_WARN](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a523b2a318b7d0217d52fc460b9d90687)
- [NPM2100_EVENT_BOOST_VOUT_DPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ad61a6868a4eaf9ae53270da2f617a4d8)
- [NPM2100_EVENT_BOOST_VOUT_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a764671a05e6d92b140c7ac216ca3b883)
- [NPM2100_EVENT_LDOSW_OCP](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a6303f8860213e5de6514b483060354f2)
- [NPM2100_EVENT_LDOSW_VINTFAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32a0bbb9e1c1a73735c734e17527a424f7f)
- [NPM2100_EVENT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ggae7433fd9cb33e7b3ac0b364d29dc6e32ac6f32faf88a0d8f5cf951c00900aca81)
- [mfd_npm2100_timer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga6a89922f19450ace9d83a4e110625cfb)
- [NPM2100_TIMER_MODE_GENERAL_PURPOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfba421611694d6f42d3e0e8ae1bbafbb03d)
- [NPM2100_TIMER_MODE_WDT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad84e4df7668b904c2af3c537775354c6)
- [NPM2100_TIMER_MODE_WDT_POWER_CYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad110b2ee5d1007416dce11faf71ae34c)
- [NPM2100_TIMER_MODE_WAKEUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gga6a89922f19450ace9d83a4e110625cfbad3c74cd6c665f5cc49c57d83f873f276)
- [mfd_npm2100_set_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gaa684cdb822e0e36fefc74b59bfd2b706)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mfd_npm2100_start_timer](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga085bc3c2d5d775c55ae598a464c9d265)
- [mfd_npm2100_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#gac87a33389dfbf30e7f0059bd6aede7dc)
- [mfd_npm2100_hibernate](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga4d34ac6e2c185976bc696ce0091b375a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [mfd_npm2100_add_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga137976d9909ad6ec179dce5722c4b865)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [mfd_npm2100_remove_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__mdf__interface__npm2100.html#ga342de8853f0afd2cdab08d2d42883b47)

---

[上一章](P009_zephyr__drivers__biometrics__emul.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__sensor__tmag5273.h_文件参考.md)
