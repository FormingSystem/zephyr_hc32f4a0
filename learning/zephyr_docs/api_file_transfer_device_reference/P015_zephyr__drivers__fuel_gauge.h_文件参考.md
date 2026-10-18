---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-15
title: zephyr__drivers__fuel_gauge.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_fuel\_gauge.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fuel__gauge_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电量计（Fuel Gauge）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/fuel_gauge.h>
```

查看此文件的源码。

电量计（Fuel Gauge）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_fuel_5Fgauge_5Fprop_5Fval"></a>

```c
union fuel_gauge_prop_val
```

相关声明：[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

属性字段（Property Field）到值/类型联合体的映射。

<a id="r_sbs_5Fgauge_5Fmanufacturer_5Fname"></a>

```c
struct sbs_gauge_manufacturer_name
```

相关声明：[sbs_gauge_manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md)。

<a id="r_sbs_5Fgauge_5Fdevice_5Fname"></a>

```c
struct sbs_gauge_device_name
```

相关声明：[sbs_gauge_device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md)。

<a id="r_sbs_5Fgauge_5Fdevice_5Fchemistry"></a>

```c
struct sbs_gauge_device_chemistry
```

相关声明：[sbs_gauge_device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md)。

<a id="r_fuel_5Fgauge_5Fdriver_5Fapi"></a>

```c
struct fuel_gauge_driver_api
```

相关声明：[fuel_gauge_driver_api](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md)。

驱动操作（Driver Operations）：电量计（Fuel Gauge）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ga824e00f1d607cdfe2598625f154636f1"></a>

```c
#define SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE 20
```

相关声明：[SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga824e00f1d607cdfe2598625f154636f1)。

用于读取 SBS 缓冲区属性（Buffer Properties）的数据结构。

<a id="r_ga41b8379542b9cbd0b3ee9e1bbe4bc599"></a>

```c
#define SBS_GAUGE_DEVICE_NAME_MAX_SIZE 20
```

相关声明：[SBS_GAUGE_DEVICE_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga41b8379542b9cbd0b3ee9e1bbe4bc599)。

<a id="r_gafe9bdc00d856d4cc787265edb7eb0ed2"></a>

```c
#define SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE 4
```

相关声明：[SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gafe9bdc00d856d4cc787265edb7eb0ed2)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_ga633eb1cb8dd64123252634b833b2f806"></a>

```c
typedef uint16_t fuel_gauge_prop_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

<a id="r_gaf8c7f6c4f49dd420df6841c43c41d615"></a>

```c
typedef int32_t fuel_gauge_custom_value_int_t
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[fuel_gauge_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8c7f6c4f49dd420df6841c43c41d615)。

自定义有符号整数属性值（Signed Integer Property Value）的类型。

<a id="r_ga08e4dae43d5169da58af32ec419ef9e8"></a>

```c
typedef uint32_t fuel_gauge_custom_value_uint_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[fuel_gauge_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga08e4dae43d5169da58af32ec419ef9e8)。

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

<a id="r_ga44fd24de7d165388a87e6dd74f6547af"></a>

```c
typedef bool fuel_gauge_custom_value_bool_t
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[fuel_gauge_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga44fd24de7d165388a87e6dd74f6547af)。

自定义布尔属性值（Boolean Property Value）的类型。

<a id="r_gaed940ae925236ad2f25cf05d78304568"></a>

```c
typedef int(* fuel_gauge_get_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val *val)
```

相关声明：[fuel_gauge_get_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gaed940ae925236ad2f25cf05d78304568)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取电量计（Fuel Gauge）属性的回调 API。

<a id="r_gae87a20a20f4f1fbb74d72afb2bcee4c9"></a>

```c
typedef int(* fuel_gauge_set_property_t) (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val)
```

相关声明：[fuel_gauge_set_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电量计（Fuel Gauge）属性的回调 API。

<a id="r_gaf8843b8ba9ff3102ac4d6c0fa2cb3f69"></a>

```c
typedef int(* fuel_gauge_get_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, void *dst, size_t dst_len)
```

相关声明：[fuel_gauge_get_buffer_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

获取电量计缓冲区属性（Buffer Property）的回调 API。

<a id="r_gae5908067ab2a8c70c517d3e12eb364c1"></a>

```c
typedef int(* fuel_gauge_set_buffer_property_t) (const struct device *dev, fuel_gauge_prop_t prop_type, const void *src, size_t src_len)
```

相关声明：[fuel_gauge_set_buffer_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gae5908067ab2a8c70c517d3e12eb364c1)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

设置电量计缓冲区属性（Buffer Property）的回调 API。

<a id="r_ga698c8f84da7d1cbe7db1fc024e2388b7"></a>

```c
typedef int(* fuel_gauge_battery_cutoff_t) (const struct device *dev)
```

相关声明：[fuel_gauge_battery_cutoff_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#ga698c8f84da7d1cbe7db1fc024e2388b7)、[device](../device_reference/P002_设备对象结构.md)。

执行电池切断（Battery Cutoff）的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.4\_枚举（Enumerations）

<a id="r_gae49908857800bdd010d59895cfad9171"></a>

```c
enum fuel_gauge_prop_type { FUEL_GAUGE_AVG_CURRENT_UA = 0 , FUEL_GAUGE_AVG_CURRENT = FUEL_GAUGE_AVG_CURRENT_UA , FUEL_GAUGE_CURRENT_UA , FUEL_GAUGE_CURRENT = FUEL_GAUGE_CURRENT_UA , FUEL_GAUGE_CHARGE_CUTOFF , FUEL_GAUGE_CYCLE_COUNT , FUEL_GAUGE_CONNECT_STATE , FUEL_GAUGE_FLAGS , FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH , FUEL_GAUGE_FULL_CHARGE_CAPACITY = FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH , FUEL_GAUGE_PRESENT_STATE , FUEL_GAUGE_REMAINING_CAPACITY_UAH , FUEL_GAUGE_REMAINING_CAPACITY = FUEL_GAUGE_REMAINING_CAPACITY_UAH , FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS , FUEL_GAUGE_RUNTIME_TO_EMPTY = FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS , FUEL_GAUGE_RUNTIME_TO_FULL_MINS , FUEL_GAUGE_RUNTIME_TO_FULL = FUEL_GAUGE_RUNTIME_TO_FULL_MINS , FUEL_GAUGE_SBS_MFR_ACCESS , FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE = FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE = FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_TEMPERATURE_DK , FUEL_GAUGE_TEMPERATURE = FUEL_GAUGE_TEMPERATURE_DK , FUEL_GAUGE_VOLTAGE_UV , FUEL_GAUGE_VOLTAGE = FUEL_GAUGE_VOLTAGE_UV , FUEL_GAUGE_SBS_MODE , FUEL_GAUGE_CHARGE_CURRENT_UA , FUEL_GAUGE_CHARGE_CURRENT = FUEL_GAUGE_CHARGE_CURRENT_UA , FUEL_GAUGE_CHARGE_VOLTAGE_UV , FUEL_GAUGE_CHARGE_VOLTAGE = FUEL_GAUGE_CHARGE_VOLTAGE_UV , FUEL_GAUGE_STATUS , FUEL_GAUGE_DESIGN_CAPACITY , FUEL_GAUGE_DESIGN_VOLTAGE_MV , FUEL_GAUGE_DESIGN_VOLTAGE = FUEL_GAUGE_DESIGN_VOLTAGE_MV , FUEL_GAUGE_SBS_ATRATE , FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL = FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY = FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS , FUEL_GAUGE_SBS_ATRATE_OK , FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM , FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS , FUEL_GAUGE_SBS_REMAINING_TIME_ALARM = FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS , FUEL_GAUGE_MANUFACTURER_NAME , FUEL_GAUGE_DEVICE_NAME , FUEL_GAUGE_DEVICE_CHEMISTRY , FUEL_GAUGE_CURRENT_DIRECTION , FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT , FUEL_GAUGE_STATE_OF_CHARGE_ALARM = FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT , FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV , FUEL_GAUGE_LOW_VOLTAGE_ALARM = FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV , FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV , FUEL_GAUGE_HIGH_VOLTAGE_ALARM = FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV , FUEL_GAUGE_LOW_CURRENT_ALARM_UA , FUEL_GAUGE_LOW_CURRENT_ALARM = FUEL_GAUGE_LOW_CURRENT_ALARM_UA , FUEL_GAUGE_HIGH_CURRENT_ALARM_UA , FUEL_GAUGE_HIGH_CURRENT_ALARM = FUEL_GAUGE_HIGH_CURRENT_ALARM_UA , FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK , FUEL_GAUGE_LOW_TEMPERATURE_ALARM = FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK , FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK , FUEL_GAUGE_HIGH_TEMPERATURE_ALARM = FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK , FUEL_GAUGE_LOW_GPIO_ALARM_UV , FUEL_GAUGE_LOW_GPIO_ALARM = FUEL_GAUGE_LOW_GPIO_ALARM_UV , FUEL_GAUGE_HIGH_GPIO_ALARM_UV , FUEL_GAUGE_HIGH_GPIO_ALARM = FUEL_GAUGE_HIGH_GPIO_ALARM_UV , FUEL_GAUGE_GPIO_VOLTAGE_UV , FUEL_GAUGE_GPIO_VOLTAGE = FUEL_GAUGE_GPIO_VOLTAGE_UV , FUEL_GAUGE_ADC_MODE , FUEL_GAUGE_CC_CONFIG , FUEL_GAUGE_STATE_OF_HEALTH , FUEL_GAUGE_THERM_VOLTAGE_UV , FUEL_GAUGE_COMMON_COUNT , FUEL_GAUGE_CUSTOM_BEGIN , FUEL_GAUGE_PROP_MAX = UINT16_MAX }
```

相关声明：[fuel_gauge_prop_type](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gae49908857800bdd010d59895cfad9171)、[FUEL_GAUGE_AVG_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904)、[FUEL_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)、[FUEL_GAUGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee)、[FUEL_GAUGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)、[FUEL_GAUGE_CHARGE_CUTOFF](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)、[FUEL_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)、[FUEL_GAUGE_CONNECT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)、[FUEL_GAUGE_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)、[FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174)、[FUEL_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)、[FUEL_GAUGE_PRESENT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)、[FUEL_GAUGE_REMAINING_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828)、[FUEL_GAUGE_REMAINING_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)、[FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e)、[FUEL_GAUGE_RUNTIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)、[FUEL_GAUGE_RUNTIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f)、[FUEL_GAUGE_RUNTIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)、[FUEL_GAUGE_SBS_MFR_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)、[FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce)、[FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)、[FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50)、[FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)、[FUEL_GAUGE_TEMPERATURE_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b)、[FUEL_GAUGE_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)、[FUEL_GAUGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c)、[FUEL_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)、[FUEL_GAUGE_SBS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)、[FUEL_GAUGE_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b)、[FUEL_GAUGE_CHARGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)、[FUEL_GAUGE_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55)、[FUEL_GAUGE_CHARGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)、[FUEL_GAUGE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)、[FUEL_GAUGE_DESIGN_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)、[FUEL_GAUGE_DESIGN_VOLTAGE_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb)、[FUEL_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)、[FUEL_GAUGE_SBS_ATRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)、[FUEL_GAUGE_SBS_ATRATE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)、[FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)、[FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70)、[FUEL_GAUGE_SBS_REMAINING_TIME_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)、[FUEL_GAUGE_MANUFACTURER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)、[FUEL_GAUGE_DEVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)、[FUEL_GAUGE_DEVICE_CHEMISTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)、[FUEL_GAUGE_CURRENT_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21)、[FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8)、[FUEL_GAUGE_STATE_OF_CHARGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae)、[FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772)、[FUEL_GAUGE_LOW_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7)、[FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43)、[FUEL_GAUGE_HIGH_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6)、[FUEL_GAUGE_LOW_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee)、[FUEL_GAUGE_LOW_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4)、[FUEL_GAUGE_HIGH_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78)、[FUEL_GAUGE_HIGH_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a)、[FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f)、[FUEL_GAUGE_LOW_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c)、[FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40)、[FUEL_GAUGE_HIGH_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d)、[FUEL_GAUGE_LOW_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833)、[FUEL_GAUGE_LOW_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9)、[FUEL_GAUGE_HIGH_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6)、[FUEL_GAUGE_HIGH_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783)、[FUEL_GAUGE_GPIO_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2)、[FUEL_GAUGE_GPIO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4)、[FUEL_GAUGE_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa)、[FUEL_GAUGE_CC_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5)、[FUEL_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53)、[FUEL_GAUGE_THERM_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458)、[FUEL_GAUGE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)、[FUEL_GAUGE_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)、[FUEL_GAUGE_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.5\_函数（Functions）

<a id="r_gab84999beab9a43241992945a3b2d37e1"></a>

```c
int fuel_gauge_get_prop (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val *val)
```

相关声明：[fuel_gauge_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gab84999beab9a43241992945a3b2d37e1)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_gaf8a1fed5f6af9c25a12130c481411603"></a>

```c
int fuel_gauge_get_props (const struct device *dev, const fuel_gauge_prop_t *props, union fuel_gauge_prop_val *vals, size_t len)
```

相关声明：[fuel_gauge_get_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8a1fed5f6af9c25a12130c481411603)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取多个电池电量计属性（Battery Fuel-gauge Properties）。

<a id="r_ga936be681a82f173b664ae2187bc5a73d"></a>

```c
int fuel_gauge_set_prop (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val)
```

相关声明：[fuel_gauge_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga936be681a82f173b664ae2187bc5a73d)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_gac8efb10ccb6f510dc92618e218c1df9b"></a>

```c
int fuel_gauge_set_props (const struct device *dev, const fuel_gauge_prop_t *props, const union fuel_gauge_prop_val *vals, size_t len)
```

相关声明：[fuel_gauge_set_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac8efb10ccb6f510dc92618e218c1df9b)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_ga7e6cb77d2d4dd7a0feb25c92d031614c"></a>

```c
int fuel_gauge_get_buffer_prop (const struct device *dev, fuel_gauge_prop_t prop_type, void *dst, size_t dst_len)
```

相关声明：[fuel_gauge_get_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga7e6cb77d2d4dd7a0feb25c92d031614c)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

获取电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

<a id="r_gac63f43b6023b9f2183001d6876fe328a"></a>

```c
int fuel_gauge_set_buffer_prop (const struct device *dev, fuel_gauge_prop_t prop_type, const void *src, size_t src_len)
```

相关声明：[fuel_gauge_set_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac63f43b6023b9f2183001d6876fe328a)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)。

设置电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

<a id="r_ga763a40688dc8fc6a0ba85fdc79178ebc"></a>

```c
int fuel_gauge_battery_cutoff (const struct device *dev)
```

相关声明：[fuel_gauge_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga763a40688dc8fc6a0ba85fdc79178ebc)、[device](../device_reference/P002_设备对象结构.md)。

令电量计（Fuel Gauge）切断（Cut Off）其关联电池。


## 15.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_device_reference/P009_fuel_gauge.h_源码浏览.md)
- [fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)
- [sbs_gauge_manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md)
- [sbs_gauge_device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md)
- [sbs_gauge_device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md)
- [fuel_gauge_driver_api](../device_power_control_model_reference/P011_fuel_gauge_driver_api_结构体.md)
- [SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga824e00f1d607cdfe2598625f154636f1)
- [SBS_GAUGE_DEVICE_NAME_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga41b8379542b9cbd0b3ee9e1bbe4bc599)
- [SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gafe9bdc00d856d4cc787265edb7eb0ed2)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [fuel_gauge_prop_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga633eb1cb8dd64123252634b833b2f806)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [fuel_gauge_custom_value_int_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8c7f6c4f49dd420df6841c43c41d615)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [fuel_gauge_custom_value_uint_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga08e4dae43d5169da58af32ec419ef9e8)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [fuel_gauge_custom_value_bool_t](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga44fd24de7d165388a87e6dd74f6547af)
- [fuel_gauge_get_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gaed940ae925236ad2f25cf05d78304568)
- [device](../device_reference/P002_设备对象结构.md)
- [fuel_gauge_set_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gae87a20a20f4f1fbb74d72afb2bcee4c9)
- [fuel_gauge_get_buffer_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gaf8843b8ba9ff3102ac4d6c0fa2cb3f69)
- [fuel_gauge_set_buffer_property_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#gae5908067ab2a8c70c517d3e12eb364c1)
- [fuel_gauge_battery_cutoff_t](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md#ga698c8f84da7d1cbe7db1fc024e2388b7)
- [fuel_gauge_prop_type](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gae49908857800bdd010d59895cfad9171)
- [FUEL_GAUGE_AVG_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904)
- [FUEL_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)
- [FUEL_GAUGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee)
- [FUEL_GAUGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)
- [FUEL_GAUGE_CHARGE_CUTOFF](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)
- [FUEL_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)
- [FUEL_GAUGE_CONNECT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)
- [FUEL_GAUGE_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)
- [FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174)
- [FUEL_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)
- [FUEL_GAUGE_PRESENT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)
- [FUEL_GAUGE_REMAINING_CAPACITY_UAH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828)
- [FUEL_GAUGE_REMAINING_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)
- [FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e)
- [FUEL_GAUGE_RUNTIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)
- [FUEL_GAUGE_RUNTIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f)
- [FUEL_GAUGE_RUNTIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)
- [FUEL_GAUGE_SBS_MFR_ACCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)
- [FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce)
- [FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)
- [FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50)
- [FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)
- [FUEL_GAUGE_TEMPERATURE_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b)
- [FUEL_GAUGE_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)
- [FUEL_GAUGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c)
- [FUEL_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)
- [FUEL_GAUGE_SBS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)
- [FUEL_GAUGE_CHARGE_CURRENT_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b)
- [FUEL_GAUGE_CHARGE_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)
- [FUEL_GAUGE_CHARGE_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55)
- [FUEL_GAUGE_CHARGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)
- [FUEL_GAUGE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)
- [FUEL_GAUGE_DESIGN_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)
- [FUEL_GAUGE_DESIGN_VOLTAGE_MV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb)
- [FUEL_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)
- [FUEL_GAUGE_SBS_ATRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a)
- [FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)
- [FUEL_GAUGE_SBS_ATRATE_OK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)
- [FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)
- [FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70)
- [FUEL_GAUGE_SBS_REMAINING_TIME_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)
- [FUEL_GAUGE_MANUFACTURER_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)
- [FUEL_GAUGE_DEVICE_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)
- [FUEL_GAUGE_DEVICE_CHEMISTRY](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)
- [FUEL_GAUGE_CURRENT_DIRECTION](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21)
- [FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8)
- [FUEL_GAUGE_STATE_OF_CHARGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae)
- [FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772)
- [FUEL_GAUGE_LOW_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7)
- [FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43)
- [FUEL_GAUGE_HIGH_VOLTAGE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6)
- [FUEL_GAUGE_LOW_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee)
- [FUEL_GAUGE_LOW_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4)
- [FUEL_GAUGE_HIGH_CURRENT_ALARM_UA](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78)
- [FUEL_GAUGE_HIGH_CURRENT_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a)
- [FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f)
- [FUEL_GAUGE_LOW_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c)
- [FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40)
- [FUEL_GAUGE_HIGH_TEMPERATURE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d)
- [FUEL_GAUGE_LOW_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833)
- [FUEL_GAUGE_LOW_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9)
- [FUEL_GAUGE_HIGH_GPIO_ALARM_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6)
- [FUEL_GAUGE_HIGH_GPIO_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783)
- [FUEL_GAUGE_GPIO_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2)
- [FUEL_GAUGE_GPIO_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4)
- [FUEL_GAUGE_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa)
- [FUEL_GAUGE_CC_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5)
- [FUEL_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53)
- [FUEL_GAUGE_THERM_VOLTAGE_UV](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458)
- [FUEL_GAUGE_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)
- [FUEL_GAUGE_CUSTOM_BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)
- [FUEL_GAUGE_PROP_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)
- [fuel_gauge_get_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gab84999beab9a43241992945a3b2d37e1)
- [fuel_gauge_get_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gaf8a1fed5f6af9c25a12130c481411603)
- [fuel_gauge_set_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga936be681a82f173b664ae2187bc5a73d)
- [fuel_gauge_set_props](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac8efb10ccb6f510dc92618e218c1df9b)
- [fuel_gauge_get_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga7e6cb77d2d4dd7a0feb25c92d031614c)
- [fuel_gauge_set_buffer_prop](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#gac63f43b6023b9f2183001d6876fe328a)
- [fuel_gauge_battery_cutoff](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html#ga763a40688dc8fc6a0ba85fdc79178ebc)

<a id="header-details"></a>

---

[上一章](P014_zephyr__dt-bindings__pinctrl__focaltech_ft9001_pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__interrupt_controller__gd32_exti.h_文件参考.md)
