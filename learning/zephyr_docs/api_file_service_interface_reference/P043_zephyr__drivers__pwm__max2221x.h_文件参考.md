---
id: learning.zephyr-docs.api-file-service-interface-reference.page-43
title: zephyr__drivers__pwm__max2221x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm_2max2221x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_drivers\_\_pwm\_\_max2221x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwm_2max2221x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX2221X脉宽调制（PWM）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

MAX2221X脉宽调制（PWM）驱动的公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 43.1\_枚举（Enumerations）

<a id="r_ga8f702fe056959c707d495a5b49ec7647"></a>

```c
enum max2221x_master_chop_freq { MAX2221X_FREQ_100KHZ = 0 , MAX2221X_FREQ_80KHZ , MAX2221X_FREQ_60KHZ , MAX2221X_FREQ_50KHZ , MAX2221X_FREQ_40KHZ , MAX2221X_FREQ_30KHZ , MAX2221X_FREQ_25KHZ , MAX2221X_FREQ_20KHZ , MAX2221X_FREQ_15KHZ , MAX2221X_FREQ_10KHZ , MAX2221X_FREQ_7500HZ , MAX2221X_FREQ_5000HZ , MAX2221X_FREQ_2500HZ , MAX2221X_FREQ_INVALID }
```

相关声明：[max2221x_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647)、[MAX2221X_FREQ_100KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)、[MAX2221X_FREQ_80KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f)、[MAX2221X_FREQ_60KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8)、[MAX2221X_FREQ_50KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980)、[MAX2221X_FREQ_40KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612)、[MAX2221X_FREQ_30KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed)、[MAX2221X_FREQ_25KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef)、[MAX2221X_FREQ_20KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15)、[MAX2221X_FREQ_15KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4)、[MAX2221X_FREQ_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5)、[MAX2221X_FREQ_7500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb)、[MAX2221X_FREQ_5000HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc)、[MAX2221X_FREQ_2500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9)、[MAX2221X_FREQ_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa)。

主斩波频率（Master Chopping Frequency）选项。

<a id="r_ga41010c75c9cb6ed23e06cfec0ebbe413"></a>

```c
enum max2221x_individual_chop_freq { MAX2221X_FREQ_M = 0 , MAX2221X_FREQ_M_2 , MAX2221X_FREQ_M_4 , MAX2221X_FREQ_M_8 , MAX2221X_FREQ_M_INVALID }
```

相关声明：[max2221x_individual_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga41010c75c9cb6ed23e06cfec0ebbe413)、[MAX2221X_FREQ_M](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)、[MAX2221X_FREQ_M_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1)、[MAX2221X_FREQ_M_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a)、[MAX2221X_FREQ_M_8](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd)、[MAX2221X_FREQ_M_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2)。

独立通道斩波频率分频系数（Chopping Frequency Divisor）选项。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.2\_函数（Functions）

<a id="r_gad283a38e9b32e9e721163feb2a7dc036"></a>

```c
int max2221x_get_master_chop_freq (const struct device *dev)
```

相关声明：[max2221x_get_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gad283a38e9b32e9e721163feb2a7dc036)、[device](../device_reference/P002_设备对象结构.md)。

获取 MAX2221X 设备的主斩波频率（Master Chop Frequency）。

<a id="r_ga70b9870d016b7db7d616f3f393e4e427"></a>

```c
int max2221x_get_channel_freq (const struct device *dev, uint32_t channel, uint32_t *channel_freq)
```

相关声明：[max2221x_get_channel_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga70b9870d016b7db7d616f3f393e4e427)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 MAX2221X 设备的独立通道频率（Individual Channel Frequency）。

<a id="r_gadc23c2818b49d4387b6641217603ca78"></a>

```c
int max2221x_calculate_duty_cycle (uint32_t pulse, uint32_t period, uint16_t *duty_cycle)
```

相关声明：[max2221x_calculate_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gadc23c2818b49d4387b6641217603ca78)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

计算占空比（Duty Cycle）。

<a id="r_ga21eb84d347badc0905f27c4d86621226"></a>

```c
int max2221x_calculate_master_freq_divisor (uint32_t master_freq, uint32_t period, int *freq_divisor)
```

相关声明：[max2221x_calculate_master_freq_divisor](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga21eb84d347badc0905f27c4d86621226)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

计算用于推算独立通道频率的主频率分频系数（Master Frequency Divisor）。

<a id="r_gabfc15fdf828ab5bcad2c4ef7f208e599"></a>

```c
int max2221x_get_cycles_per_sec (const struct device *dev, uint32_t channel, uint64_t *cycles)
```

相关声明：[max2221x_get_cycles_per_sec](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gabfc15fdf828ab5bcad2c4ef7f208e599)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取脉宽调制（PWM）通道每秒的周期数。

<a id="r_ga8c202d4ecf8908c5f40124dddf7d40d6"></a>

```c
int max2221x_set_cycles (const struct device *dev, uint32_t channel, uint32_t period, uint32_t pulse, pwm_flags_t flags)
```

相关声明：[max2221x_set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8c202d4ecf8908c5f40124dddf7d40d6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

设置 PWM 通道的占空比（Duty Cycle）。


## 43.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P682_max2221x.h_源码浏览.md)
- [max2221x_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647)
- [MAX2221X_FREQ_100KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)
- [MAX2221X_FREQ_80KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f)
- [MAX2221X_FREQ_60KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8)
- [MAX2221X_FREQ_50KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980)
- [MAX2221X_FREQ_40KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612)
- [MAX2221X_FREQ_30KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed)
- [MAX2221X_FREQ_25KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef)
- [MAX2221X_FREQ_20KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15)
- [MAX2221X_FREQ_15KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4)
- [MAX2221X_FREQ_10KHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5)
- [MAX2221X_FREQ_7500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb)
- [MAX2221X_FREQ_5000HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc)
- [MAX2221X_FREQ_2500HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9)
- [MAX2221X_FREQ_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa)
- [max2221x_individual_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga41010c75c9cb6ed23e06cfec0ebbe413)
- [MAX2221X_FREQ_M](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)
- [MAX2221X_FREQ_M_2](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1)
- [MAX2221X_FREQ_M_4](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a)
- [MAX2221X_FREQ_M_8](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd)
- [MAX2221X_FREQ_M_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2)
- [max2221x_get_master_chop_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gad283a38e9b32e9e721163feb2a7dc036)
- [device](../device_reference/P002_设备对象结构.md)
- [max2221x_get_channel_freq](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga70b9870d016b7db7d616f3f393e4e427)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [max2221x_calculate_duty_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gadc23c2818b49d4387b6641217603ca78)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [max2221x_calculate_master_freq_divisor](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga21eb84d347badc0905f27c4d86621226)
- [max2221x_get_cycles_per_sec](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gabfc15fdf828ab5bcad2c4ef7f208e599)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [max2221x_set_cycles](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8c202d4ecf8908c5f40124dddf7d40d6)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="header-details"></a>

---

[上一章](P042_zephyr__drivers__misc__pio_rpi_pico__pio_rpi_pico.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__sensing__sensing_sensor_types.h_文件参考.md)
