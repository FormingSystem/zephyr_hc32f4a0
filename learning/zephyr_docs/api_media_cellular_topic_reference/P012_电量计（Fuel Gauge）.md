---
id: learning.zephyr-docs.api-media-cellular-topic-reference.page-12
title: 电量计（Fuel Gauge）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_电量计（Fuel Gauge）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fuel__gauge__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电量计接口。

<a id="details"></a>

电量计接口（Fuel Gauge Interfaces）。自 3.3 引入，版本 0.9.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 12.1\_主题（Topics）

<a id="r_devicetree-battery"></a>

相关声明：[设备树电池辅助宏（Devicetree Battery Helpers）](../dt_overview_reference/P002_电池开路电压曲线宏.md)。

<a id="r_fuel_5Fgauge_5Finterface_5Fbackend"></a>

相关声明：[电量计驱动后端 API（Fuel Gauge Driver Backend API）](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md)。

<a id="r_fuel_5Fgauge_5Femulator_5Fbackend"></a>

相关声明：[电量计后端仿真器 API（Fuel gauge backend emulator APIs）](../hardware/P492_电量计仿真后端接口.md)。

电量计后端仿真器 API（Fuel gauge backend emulator APIs）

<a id="header-files"></a>
<a id="files"></a>

## 12.2\_文件（Files）

<a id="r_fuel_5Fgauge_2Eh"></a>

```c
file fuel_gauge.h
```

相关声明：[fuel_gauge.h](../api_file_transfer_device_reference/P015_zephyr__drivers__fuel_gauge.h_文件参考.md)。

电量计（Fuel Gauge）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.4\_宏定义（Macros）

<a id="r_ga824e00f1d607cdfe2598625f154636f1"></a>

```c
#define SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE 20
```

相关声明：[SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE](#ga824e00f1d607cdfe2598625f154636f1)。

用于读取 SBS 缓冲区属性（Buffer Properties）的数据结构。

<a id="r_ga41b8379542b9cbd0b3ee9e1bbe4bc599"></a>

```c
#define SBS_GAUGE_DEVICE_NAME_MAX_SIZE 20
```

相关声明：[SBS_GAUGE_DEVICE_NAME_MAX_SIZE](#ga41b8379542b9cbd0b3ee9e1bbe4bc599)。

<a id="r_gafe9bdc00d856d4cc787265edb7eb0ed2"></a>

```c
#define SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE 4
```

相关声明：[SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE](#gafe9bdc00d856d4cc787265edb7eb0ed2)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.5\_类型定义（Typedefs）

<a id="r_ga633eb1cb8dd64123252634b833b2f806"></a>

```c
typedef uint16_t fuel_gauge_prop_t
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)。

<a id="r_gaf8c7f6c4f49dd420df6841c43c41d615"></a>

```c
typedef int32_t fuel_gauge_custom_value_int_t
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[fuel_gauge_custom_value_int_t](#gaf8c7f6c4f49dd420df6841c43c41d615)。

自定义有符号整数属性值（Signed Integer Property Value）的类型。

<a id="r_ga08e4dae43d5169da58af32ec419ef9e8"></a>

```c
typedef uint32_t fuel_gauge_custom_value_uint_t
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[fuel_gauge_custom_value_uint_t](#ga08e4dae43d5169da58af32ec419ef9e8)。

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

<a id="r_ga44fd24de7d165388a87e6dd74f6547af"></a>

```c
typedef bool fuel_gauge_custom_value_bool_t
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[fuel_gauge_custom_value_bool_t](#ga44fd24de7d165388a87e6dd74f6547af)。

自定义布尔属性值（Boolean Property Value）的类型。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.6\_枚举（Enumerations）

<a id="r_gae49908857800bdd010d59895cfad9171"></a>

```c
enum fuel_gauge_prop_type { FUEL_GAUGE_AVG_CURRENT_UA = 0 , FUEL_GAUGE_AVG_CURRENT = FUEL_GAUGE_AVG_CURRENT_UA , FUEL_GAUGE_CURRENT_UA , FUEL_GAUGE_CURRENT = FUEL_GAUGE_CURRENT_UA , FUEL_GAUGE_CHARGE_CUTOFF , FUEL_GAUGE_CYCLE_COUNT , FUEL_GAUGE_CONNECT_STATE , FUEL_GAUGE_FLAGS , FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH , FUEL_GAUGE_FULL_CHARGE_CAPACITY = FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH , FUEL_GAUGE_PRESENT_STATE , FUEL_GAUGE_REMAINING_CAPACITY_UAH , FUEL_GAUGE_REMAINING_CAPACITY = FUEL_GAUGE_REMAINING_CAPACITY_UAH , FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS , FUEL_GAUGE_RUNTIME_TO_EMPTY = FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS , FUEL_GAUGE_RUNTIME_TO_FULL_MINS , FUEL_GAUGE_RUNTIME_TO_FULL = FUEL_GAUGE_RUNTIME_TO_FULL_MINS , FUEL_GAUGE_SBS_MFR_ACCESS , FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE = FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE = FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT , FUEL_GAUGE_TEMPERATURE_DK , FUEL_GAUGE_TEMPERATURE = FUEL_GAUGE_TEMPERATURE_DK , FUEL_GAUGE_VOLTAGE_UV , FUEL_GAUGE_VOLTAGE = FUEL_GAUGE_VOLTAGE_UV , FUEL_GAUGE_SBS_MODE , FUEL_GAUGE_CHARGE_CURRENT_UA , FUEL_GAUGE_CHARGE_CURRENT = FUEL_GAUGE_CHARGE_CURRENT_UA , FUEL_GAUGE_CHARGE_VOLTAGE_UV , FUEL_GAUGE_CHARGE_VOLTAGE = FUEL_GAUGE_CHARGE_VOLTAGE_UV , FUEL_GAUGE_STATUS , FUEL_GAUGE_DESIGN_CAPACITY , FUEL_GAUGE_DESIGN_VOLTAGE_MV , FUEL_GAUGE_DESIGN_VOLTAGE = FUEL_GAUGE_DESIGN_VOLTAGE_MV , FUEL_GAUGE_SBS_ATRATE , FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL = FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS , FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY = FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS , FUEL_GAUGE_SBS_ATRATE_OK , FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM , FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS , FUEL_GAUGE_SBS_REMAINING_TIME_ALARM = FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS , FUEL_GAUGE_MANUFACTURER_NAME , FUEL_GAUGE_DEVICE_NAME , FUEL_GAUGE_DEVICE_CHEMISTRY , FUEL_GAUGE_CURRENT_DIRECTION , FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT , FUEL_GAUGE_STATE_OF_CHARGE_ALARM = FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT , FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV , FUEL_GAUGE_LOW_VOLTAGE_ALARM = FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV , FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV , FUEL_GAUGE_HIGH_VOLTAGE_ALARM = FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV , FUEL_GAUGE_LOW_CURRENT_ALARM_UA , FUEL_GAUGE_LOW_CURRENT_ALARM = FUEL_GAUGE_LOW_CURRENT_ALARM_UA , FUEL_GAUGE_HIGH_CURRENT_ALARM_UA , FUEL_GAUGE_HIGH_CURRENT_ALARM = FUEL_GAUGE_HIGH_CURRENT_ALARM_UA , FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK , FUEL_GAUGE_LOW_TEMPERATURE_ALARM = FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK , FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK , FUEL_GAUGE_HIGH_TEMPERATURE_ALARM = FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK , FUEL_GAUGE_LOW_GPIO_ALARM_UV , FUEL_GAUGE_LOW_GPIO_ALARM = FUEL_GAUGE_LOW_GPIO_ALARM_UV , FUEL_GAUGE_HIGH_GPIO_ALARM_UV , FUEL_GAUGE_HIGH_GPIO_ALARM = FUEL_GAUGE_HIGH_GPIO_ALARM_UV , FUEL_GAUGE_GPIO_VOLTAGE_UV , FUEL_GAUGE_GPIO_VOLTAGE = FUEL_GAUGE_GPIO_VOLTAGE_UV , FUEL_GAUGE_ADC_MODE , FUEL_GAUGE_CC_CONFIG , FUEL_GAUGE_STATE_OF_HEALTH , FUEL_GAUGE_THERM_VOLTAGE_UV , FUEL_GAUGE_COMMON_COUNT , FUEL_GAUGE_CUSTOM_BEGIN , FUEL_GAUGE_PROP_MAX = UINT16_MAX }
```

相关声明：[fuel_gauge_prop_type](#gae49908857800bdd010d59895cfad9171)、[FUEL_GAUGE_AVG_CURRENT_UA](#ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904)、[FUEL_GAUGE_AVG_CURRENT](#ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396)、[FUEL_GAUGE_CURRENT_UA](#ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee)、[FUEL_GAUGE_CURRENT](#ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354)、[FUEL_GAUGE_CHARGE_CUTOFF](#ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f)、[FUEL_GAUGE_CYCLE_COUNT](#ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984)、[FUEL_GAUGE_CONNECT_STATE](#ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d)、[FUEL_GAUGE_FLAGS](#ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c)、[FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH](#ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174)、[FUEL_GAUGE_FULL_CHARGE_CAPACITY](#ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9)、[FUEL_GAUGE_PRESENT_STATE](#ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b)、[FUEL_GAUGE_REMAINING_CAPACITY_UAH](#ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828)、[FUEL_GAUGE_REMAINING_CAPACITY](#ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4)、[FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS](#ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e)、[FUEL_GAUGE_RUNTIME_TO_EMPTY](#ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd)、[FUEL_GAUGE_RUNTIME_TO_FULL_MINS](#ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f)、[FUEL_GAUGE_RUNTIME_TO_FULL](#ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399)、[FUEL_GAUGE_SBS_MFR_ACCESS](#ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd)、[FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT](#ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce)、[FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE](#ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee)、[FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT](#ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50)、[FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE](#ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b)、[FUEL_GAUGE_TEMPERATURE_DK](#ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b)、[FUEL_GAUGE_TEMPERATURE](#ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009)、[FUEL_GAUGE_VOLTAGE_UV](#ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c)、[FUEL_GAUGE_VOLTAGE](#ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71)、[FUEL_GAUGE_SBS_MODE](#ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae)、[FUEL_GAUGE_CHARGE_CURRENT_UA](#ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b)、[FUEL_GAUGE_CHARGE_CURRENT](#ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e)、[FUEL_GAUGE_CHARGE_VOLTAGE_UV](#ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55)、[FUEL_GAUGE_CHARGE_VOLTAGE](#ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920)、[FUEL_GAUGE_STATUS](#ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40)、[FUEL_GAUGE_DESIGN_CAPACITY](#ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67)、[FUEL_GAUGE_DESIGN_VOLTAGE_MV](#ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb)、[FUEL_GAUGE_DESIGN_VOLTAGE](#ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf)、[FUEL_GAUGE_SBS_ATRATE](#ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS](#ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL](#ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS](#ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a)、[FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY](#ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0)、[FUEL_GAUGE_SBS_ATRATE_OK](#ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec)、[FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM](#ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2)、[FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS](#ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70)、[FUEL_GAUGE_SBS_REMAINING_TIME_ALARM](#ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a)、[FUEL_GAUGE_MANUFACTURER_NAME](#ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8)、[FUEL_GAUGE_DEVICE_NAME](#ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10)、[FUEL_GAUGE_DEVICE_CHEMISTRY](#ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9)、[FUEL_GAUGE_CURRENT_DIRECTION](#ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21)、[FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT](#ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8)、[FUEL_GAUGE_STATE_OF_CHARGE_ALARM](#ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae)、[FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV](#ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772)、[FUEL_GAUGE_LOW_VOLTAGE_ALARM](#ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7)、[FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV](#ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43)、[FUEL_GAUGE_HIGH_VOLTAGE_ALARM](#ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6)、[FUEL_GAUGE_LOW_CURRENT_ALARM_UA](#ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee)、[FUEL_GAUGE_LOW_CURRENT_ALARM](#ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4)、[FUEL_GAUGE_HIGH_CURRENT_ALARM_UA](#ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78)、[FUEL_GAUGE_HIGH_CURRENT_ALARM](#ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a)、[FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK](#ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f)、[FUEL_GAUGE_LOW_TEMPERATURE_ALARM](#ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c)、[FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK](#ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40)、[FUEL_GAUGE_HIGH_TEMPERATURE_ALARM](#ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d)、[FUEL_GAUGE_LOW_GPIO_ALARM_UV](#ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833)、[FUEL_GAUGE_LOW_GPIO_ALARM](#ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9)、[FUEL_GAUGE_HIGH_GPIO_ALARM_UV](#ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6)、[FUEL_GAUGE_HIGH_GPIO_ALARM](#ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783)、[FUEL_GAUGE_GPIO_VOLTAGE_UV](#ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2)、[FUEL_GAUGE_GPIO_VOLTAGE](#ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4)、[FUEL_GAUGE_ADC_MODE](#ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa)、[FUEL_GAUGE_CC_CONFIG](#ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5)、[FUEL_GAUGE_STATE_OF_HEALTH](#ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53)、[FUEL_GAUGE_THERM_VOLTAGE_UV](#ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458)、[FUEL_GAUGE_COMMON_COUNT](#ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815)、[FUEL_GAUGE_CUSTOM_BEGIN](#ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584)、[FUEL_GAUGE_PROP_MAX](#ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.7\_函数（Functions）

<a id="r_gab84999beab9a43241992945a3b2d37e1"></a>

```c
int fuel_gauge_get_prop (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val *val)
```

相关声明：[fuel_gauge_get_prop](#gab84999beab9a43241992945a3b2d37e1)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_gaf8a1fed5f6af9c25a12130c481411603"></a>

```c
int fuel_gauge_get_props (const struct device *dev, const fuel_gauge_prop_t *props, union fuel_gauge_prop_val *vals, size_t len)
```

相关声明：[fuel_gauge_get_props](#gaf8a1fed5f6af9c25a12130c481411603)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

获取多个电池电量计属性（Battery Fuel-gauge Properties）。

<a id="r_ga936be681a82f173b664ae2187bc5a73d"></a>

```c
int fuel_gauge_set_prop (const struct device *dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val)
```

相关声明：[fuel_gauge_set_prop](#ga936be681a82f173b664ae2187bc5a73d)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_gac8efb10ccb6f510dc92618e218c1df9b"></a>

```c
int fuel_gauge_set_props (const struct device *dev, const fuel_gauge_prop_t *props, const union fuel_gauge_prop_val *vals, size_t len)
```

相关声明：[fuel_gauge_set_props](#gac8efb10ccb6f510dc92618e218c1df9b)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)、[fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)。

设置电池电量计属性（Battery Fuel-gauge Property）。

<a id="r_ga7e6cb77d2d4dd7a0feb25c92d031614c"></a>

```c
int fuel_gauge_get_buffer_prop (const struct device *dev, fuel_gauge_prop_t prop_type, void *dst, size_t dst_len)
```

相关声明：[fuel_gauge_get_buffer_prop](#ga7e6cb77d2d4dd7a0feb25c92d031614c)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)。

获取电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

<a id="r_gac63f43b6023b9f2183001d6876fe328a"></a>

```c
int fuel_gauge_set_buffer_prop (const struct device *dev, fuel_gauge_prop_t prop_type, const void *src, size_t src_len)
```

相关声明：[fuel_gauge_set_buffer_prop](#gac63f43b6023b9f2183001d6876fe328a)、[device](../device_reference/P002_设备对象结构.md)、[fuel_gauge_prop_t](#ga633eb1cb8dd64123252634b833b2f806)。

设置电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

<a id="r_ga763a40688dc8fc6a0ba85fdc79178ebc"></a>

```c
int fuel_gauge_battery_cutoff (const struct device *dev)
```

相关声明：[fuel_gauge_battery_cutoff](#ga763a40688dc8fc6a0ba85fdc79178ebc)、[device](../device_reference/P002_设备对象结构.md)。

令电量计（Fuel Gauge）切断（Cut Off）其关联电池。

## 12.8\_详细说明（Detailed Documentation）

<a id="gafe9bdc00d856d4cc787265edb7eb0ed2"></a>

### `SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE`

```c
#define SBS_GAUGE_DEVICE_CHEMISTRY_MAX_SIZE 4
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="ga41b8379542b9cbd0b3ee9e1bbe4bc599"></a>

### `SBS_GAUGE_DEVICE_NAME_MAX_SIZE`

```c
#define SBS_GAUGE_DEVICE_NAME_MAX_SIZE 20
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="ga824e00f1d607cdfe2598625f154636f1"></a>

### `SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE`

```c
#define SBS_GAUGE_MANUFACTURER_NAME_MAX_SIZE 20
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

用于读取 SBS 缓冲区属性（Buffer Properties）的数据结构。

<a id="ga44fd24de7d165388a87e6dd74f6547af"></a>

### `fuel_gauge_custom_value_bool_t`

```c
typedef bool fuel_gauge_custom_value_bool_t
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

自定义布尔属性值（Boolean Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 FUEL_GAUGE_CUSTOM_BEGIN）使用，通常用于特性／状态标志。

<a id="gaf8c7f6c4f49dd420df6841c43c41d615"></a>

### `fuel_gauge_custom_value_int_t`

```c
typedef int32_t fuel_gauge_custom_value_int_t
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

自定义有符号整数属性值（Signed Integer Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 FUEL_GAUGE_CUSTOM_BEGIN）使用。

<a id="ga08e4dae43d5169da58af32ec419ef9e8"></a>

### `fuel_gauge_custom_value_uint_t`

```c
typedef uint32_t fuel_gauge_custom_value_uint_t
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

自定义无符号整数属性值（Unsigned Integer Property Value）的类型。

仅供下游自定义属性（Downstream Custom Properties，值大于或等于 FUEL_GAUGE_CUSTOM_BEGIN）使用。

<a id="ga633eb1cb8dd64123252634b833b2f806"></a>

### `fuel_gauge_prop_t`

```c
typedef uint16_t fuel_gauge_prop_t
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

<a id="gae49908857800bdd010d59895cfad9171"></a>

### `fuel_gauge_prop_type`

```c
enum fuel_gauge_prop_type
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FUEL_GAUGE_AVG_CURRENT_UA` | 运行时动态电池参数（Runtime Dynamic Battery Parameters）。提供电池电流的 1 分钟平均值。不检查标志，也不检查这些值是否为异常读数。实现细节及平均值计算方法参见驱动实例头文件。单位为 µA，负值表示放电（Discharging）。 |
| `FUEL_GAUGE_AVG_CURRENT` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_AVG_CURRENT_UA`。 |
| `FUEL_GAUGE_CURRENT_UA` | 电池电流（Battery Current），单位为 µA；负值表示放电。 |
| `FUEL_GAUGE_CURRENT` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_CURRENT_UA`。 |
| `FUEL_GAUGE_CHARGE_CUTOFF` | 电量计对应的电池是否已切断充电（Cut Off from Charge）。 |
| `FUEL_GAUGE_CYCLE_COUNT` | 充放电循环次数（Charge/Discharge Cycle Count）。 |
| `FUEL_GAUGE_CONNECT_STATE` | 电池连接状态（Battery Connect State）。 |
| `FUEL_GAUGE_FLAGS` | 通用错误／运行时标志（General Error / Runtime Flags）。 |
| `FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH` | 满充容量（Full Charge Capacity），单位为 µAh；某些实现中，此值可能变化，用于判断老化程度。 |
| `FUEL_GAUGE_FULL_CHARGE_CAPACITY` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH`。 |
| `FUEL_GAUGE_PRESENT_STATE` | 电池是否物理存在（Physically Present）。 |
| `FUEL_GAUGE_REMAINING_CAPACITY_UAH` | 剩余容量（Remaining Capacity），单位为 µAh。 |
| `FUEL_GAUGE_REMAINING_CAPACITY` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_REMAINING_CAPACITY_UAH`。 |
| `FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS` | 电池剩余续航时间（Remaining Battery Life Time），单位为分钟。 |
| `FUEL_GAUGE_RUNTIME_TO_EMPTY` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS`。 |
| `FUEL_GAUGE_RUNTIME_TO_FULL_MINS` | 距电池充满的剩余时间（Remaining Time to Full Charge），单位为分钟。 |
| `FUEL_GAUGE_RUNTIME_TO_FULL` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_RUNTIME_TO_FULL_MINS`。 |
| `FUEL_GAUGE_SBS_MFR_ACCESS` | 从智能电池规范 SBS 1.1 的 ManufacturerAccess 获取一个字（Word）。 |
| `FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT` | 绝对荷电状态（Absolute State of Charge），百分比为 0–100，表示设计容量的百分比。 |
| `FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT`。 |
| `FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT` | 相对荷电状态（Relative State of Charge），百分比为 0–100，表示满充容量的百分比。 |
| `FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT`。 |
| `FUEL_GAUGE_TEMPERATURE_DK` | 温度（Temperature），单位为 0.1 K。 |
| `FUEL_GAUGE_TEMPERATURE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_TEMPERATURE_DK`。 |
| `FUEL_GAUGE_VOLTAGE_UV` | 电池电压（Battery Voltage），单位为 µV。 |
| `FUEL_GAUGE_VOLTAGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_VOLTAGE_UV`。 |
| `FUEL_GAUGE_SBS_MODE` | 电池模式（Battery Mode），以标志表示。 |
| `FUEL_GAUGE_CHARGE_CURRENT_UA` | 电池期望的最大充电电流（Max Charging Current），单位为 µA。 |
| `FUEL_GAUGE_CHARGE_CURRENT` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_CHARGE_CURRENT_UA`。 |
| `FUEL_GAUGE_CHARGE_VOLTAGE_UV` | 电池期望的最大充电电压（Max Charging Voltage），单位为 µV。 |
| `FUEL_GAUGE_CHARGE_VOLTAGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_CHARGE_VOLTAGE_UV`。 |
| `FUEL_GAUGE_STATUS` | 报警、状态和错误码（Alarm, Status and Error Codes），以标志表示。 |
| `FUEL_GAUGE_DESIGN_CAPACITY` | 设计容量（Design Capacity），单位为 mAh 或 10 mWh。 |
| `FUEL_GAUGE_DESIGN_VOLTAGE_MV` | 设计电压（Design Voltage），单位为 mV。 |
| `FUEL_GAUGE_DESIGN_VOLTAGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_DESIGN_VOLTAGE_MV`。 |
| `FUEL_GAUGE_SBS_ATRATE` | 指定速率（AtRate），单位为 mA 或 10 mW。 |
| `FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS` | 指定速率下充满时间（AtRateTimeToFull），单位为分钟。 |
| `FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS`。 |
| `FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS` | 指定速率下耗尽时间（AtRateTimeToEmpty），单位为分钟。 |
| `FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS`。 |
| `FUEL_GAUGE_SBS_ATRATE_OK` | 指定速率是否可满足（AtRateOK），布尔值。 |
| `FUEL_GAUGE_SBS_REMAINING_CAPACITY_ALARM` | 剩余容量报警（Remaining Capacity Alarm），单位为 mAh 或 10 mWh。 |
| `FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS` | 剩余时间报警（Remaining Time Alarm），单位为分钟。 |
| `FUEL_GAUGE_SBS_REMAINING_TIME_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS`。 |
| `FUEL_GAUGE_MANUFACTURER_NAME` | 电池组制造商（Manufacturer of Pack），1 字节长度加 20 字节数据。 |
| `FUEL_GAUGE_DEVICE_NAME` | 电池组名称（Name of Pack），1 字节长度加 20 字节数据。 |
| `FUEL_GAUGE_DEVICE_CHEMISTRY` | 化学体系（Chemistry），1 字节长度加 4 字节数据。 |
| `FUEL_GAUGE_CURRENT_DIRECTION` | 电池电流方向（Battery Current Direction），以标志表示。 |
| `FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT` | 剩余荷电状态报警（Remaining State of Charge Alarm），百分比为 0–100。 |
| `FUEL_GAUGE_STATE_OF_CHARGE_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT`。 |
| `FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV` | 电芯低电压报警（Low Cell Voltage Alarm），单位为 µV。 |
| `FUEL_GAUGE_LOW_VOLTAGE_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV`。 |
| `FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV` | 电芯高电压报警（High Cell Voltage Alarm），单位为 µV。 |
| `FUEL_GAUGE_HIGH_VOLTAGE_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV`。 |
| `FUEL_GAUGE_LOW_CURRENT_ALARM_UA` | 电芯低电流报警（Low Cell Current Alarm），单位为 µA。 |
| `FUEL_GAUGE_LOW_CURRENT_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_CURRENT_ALARM_UA`。 |
| `FUEL_GAUGE_HIGH_CURRENT_ALARM_UA` | 电芯高电流报警（High Cell Current Alarm），单位为 µA。 |
| `FUEL_GAUGE_HIGH_CURRENT_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_CURRENT_ALARM_UA`。 |
| `FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK` | 电芯低温报警（Low Cell Temperature Alarm），单位为 dK。 |
| `FUEL_GAUGE_LOW_TEMPERATURE_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK`。 |
| `FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK` | 电芯高温报警（High Cell Temperature Alarm），单位为 dK。 |
| `FUEL_GAUGE_HIGH_TEMPERATURE_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK`。 |
| `FUEL_GAUGE_LOW_GPIO_ALARM_UV` | GPIO 低电压报警（Low GPIO Voltage Alarm），单位为 µV。 |
| `FUEL_GAUGE_LOW_GPIO_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_GPIO_ALARM_UV`。 |
| `FUEL_GAUGE_HIGH_GPIO_ALARM_UV` | GPIO 高电压报警（High GPIO Voltage Alarm），单位为 µV。 |
| `FUEL_GAUGE_HIGH_GPIO_ALARM` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_GPIO_ALARM_UV`。 |
| `FUEL_GAUGE_GPIO_VOLTAGE_UV` | GPIO 电压（Voltage），单位为 µV。 |
| `FUEL_GAUGE_GPIO_VOLTAGE` | 已弃用（Deprecated）：请改用 `FUEL_GAUGE_GPIO_VOLTAGE_UV`。 |
| `FUEL_GAUGE_ADC_MODE` | 模数转换器模式（ADC Mode），以标志表示。 |
| `FUEL_GAUGE_CC_CONFIG` | 库仑计配置（Coulomb Counter Config），以标志表示。 |
| `FUEL_GAUGE_STATE_OF_HEALTH` | 健康状态（State of Health，SoH），百分比为 0–100。 |
| `FUEL_GAUGE_THERM_VOLTAGE_UV` | 热敏电阻电压检测读数（Thermistor Voltage Sense Reading），单位为 µV。 |
| `FUEL_GAUGE_COMMON_COUNT` | 保留值，用于界定通用电量计属性（Common Fuel Gauge Properties）的结束位置。 |
| `FUEL_GAUGE_CUSTOM_BEGIN` | 保留值，用于界定下游自定义属性（Downstream Custom Properties）。应使用此符号值，因为其实际数值可能随 API 后续版本改变。 |
| `FUEL_GAUGE_PROP_MAX` | 保留值，用于界定有效枚举属性（Valid Enum Properties）的结束位置。 |

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_AVG_CURRENT_UA`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_CURRENT_UA`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_FULL_CHARGE_CAPACITY_UAH`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_REMAINING_CAPACITY_UAH`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_RUNTIME_TO_EMPTY_MINS`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_RUNTIME_TO_FULL_MINS`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_ABSOLUTE_STATE_OF_CHARGE_PCT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_RELATIVE_STATE_OF_CHARGE_PCT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_TEMPERATURE_DK`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_VOLTAGE_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_CHARGE_CURRENT_UA`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_CHARGE_VOLTAGE_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_DESIGN_VOLTAGE_MV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_ATRATE_TIME_TO_FULL_MINS`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_ATRATE_TIME_TO_EMPTY_MINS`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_SBS_REMAINING_TIME_ALARM_MINS`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_STATE_OF_CHARGE_ALARM_PCT`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_VOLTAGE_ALARM_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_VOLTAGE_ALARM_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_CURRENT_ALARM_UA`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_CURRENT_ALARM_UA`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_TEMPERATURE_ALARM_DK`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_TEMPERATURE_ALARM_DK`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_LOW_GPIO_ALARM_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_HIGH_GPIO_ALARM_UV`。

**已弃用（Deprecated）**：已弃用（Deprecated）：请改用 `FUEL_GAUGE_GPIO_VOLTAGE_UV`。

<a id="ga763a40688dc8fc6a0ba85fdc79178ebc"></a>

### `fuel_gauge_battery_cutoff()`

```c
int fuel_gauge_battery_cutoff ( const struct device * dev)
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

令电量计（Fuel Gauge）切断（Cut Off）其关联电池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |

**返回（Returns）**：返回：成功且电池切断（Battery Cutoff）已开始进行时为 0；切断失败时小于 0。

<a id="ga7e6cb77d2d4dd7a0feb25c92d031614c"></a>

### `fuel_gauge_get_buffer_prop()`

```c
int fuel_gauge_get_buffer_prop ( const struct device * dev, fuel_gauge_prop_t prop_type, void * dst, size_t dst_len )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

获取电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `prop_type` | 要从设备获取的属性类型（Property Type）。 |
| `dst` | 用于保存从电量计读取的缓冲区数据的字节数组或结构体（Byte Array / Struct）。 |
| `dst_len` | 目标数组长度，单位为字节。 |

**返回（Returns）**：返回：成功时为 0，获取属性失败时小于 0；原文重复说明成功时返回 0。

<a id="gab84999beab9a43241992945a3b2d37e1"></a>

### `fuel_gauge_get_prop()`

```c
int fuel_gauge_get_prop ( const struct device * dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val * val )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

获取电池电量计属性（Battery Fuel-gauge Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `prop` | 要从设备获取的属性类型（Property Type）。 |
| `val` | 指向 union fuel_gauge_prop_val 的指针，用于保存从电量计设备读取的属性。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gaf8a1fed5f6af9c25a12130c481411603"></a>

### `fuel_gauge_get_props()`

```c
int fuel_gauge_get_props ( const struct device * dev, const fuel_gauge_prop_t * props, union fuel_gauge_prop_val * vals, size_t len )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

获取多个电池电量计属性（Battery Fuel-gauge Properties）。

默认实现等同于多次调用 fuel_gauge_get_prop()。驱动可实现电量计驱动 API 结构体中的 get_properties 字段，以覆盖该实现。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `props` | 要从设备获取的属性类型数组（Property Type Array），每个索引与输入 vals 数组的相同索引对应。 |
| `vals` | 指向 union fuel_gauge_prop_val 数组的指针，用于保存从电量计设备读取的属性。vals 数组的顺序不会重排（Permute）。 |
| `len` | props 与 vals 数组中的属性数量（Number of Properties）。 |

**返回（Returns）**：返回：成功时为 0，否则为第一个失败属性的负 errno 错误码。

<a id="gac63f43b6023b9f2183001d6876fe328a"></a>

### `fuel_gauge_set_buffer_prop()`

```c
int fuel_gauge_set_buffer_prop ( const struct device * dev, fuel_gauge_prop_t prop_type, const void * src, size_t src_len )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

设置电池电量计缓冲区属性（Battery Fuel-gauge Buffer Property）。

向电量计设备写入变长缓冲区属性（Variable Length Buffer Property），例如配置映像或厂商定义的数据块。

源数据是一个不透明且不含指针的字节缓冲区（Opaque, Pointer-free Byte Buffer）。从用户模式（User Mode）调用时，只验证从 src 开始的 src_len 个字节，然后交给驱动；因此缓冲区不得包含驱动会解引用的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `prop_type` | 写入电量计设备的属性类型（Property Type）。 |
| `src` | 保存要写入电量计的数据的字节缓冲区（Byte Buffer）。 |
| `src_len` | 源缓冲区长度，单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga936be681a82f173b664ae2187bc5a73d"></a>

### `fuel_gauge_set_prop()`

```c
int fuel_gauge_set_prop ( const struct device * dev, fuel_gauge_prop_t prop, union fuel_gauge_prop_val val )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

设置电池电量计属性（Battery Fuel-gauge Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `prop` | 要设置的属性类型（Property Type）。 |
| `val` | 要为对应 prop 属性设置的值（Value）。 |

**返回（Returns）**：返回：成功时为 0，否则为第一个失败属性的负 errno 错误码。

<a id="gac8efb10ccb6f510dc92618e218c1df9b"></a>

### `fuel_gauge_set_props()`

```c
int fuel_gauge_set_props ( const struct device * dev, const fuel_gauge_prop_t * props, const union fuel_gauge_prop_val * vals, size_t len )
```

```c
#include <zephyr/drivers/fuel_gauge.h>
```

设置电池电量计属性（Battery Fuel-gauge Property）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向电池电量计设备（Battery Fuel-gauge Device）的指针。 |
| `props` | 要设置的属性类型数组（Property Type Array），每个索引与输入 vals 数组的相同索引对应。 |
| `vals` | 指向 union fuel_gauge_prop_val 数组的指针，用于将属性写入电量计设备。vals 数组的顺序不会重排（Permute）。 |
| `len` | props 数组中的属性数量（Number of Properties）。 |

**返回（Returns）**：返回：成功时为 0，否则为第一个失败属性的负 errno 错误码。


## 12.9\_原页交叉引用（Cross References）

- [设备树电池辅助宏（Devicetree Battery Helpers）](../dt_overview_reference/P002_电池开路电压曲线宏.md)
- [电量计驱动后端 API（Fuel Gauge Driver Backend API）](../api_vector_pipeline_topic_reference/P009_电量计驱动后端 API（Fuel Gauge Driver Backend API）.md)
- [电量计后端仿真器 API（Fuel gauge backend emulator APIs）](../hardware/P492_电量计仿真后端接口.md)
- [fuel_gauge.h](../api_file_transfer_device_reference/P015_zephyr__drivers__fuel_gauge.h_文件参考.md)
- [fuel_gauge_prop_val](../device_power_control_model_reference/P106_fuel_gauge_prop_val_联合体.md)
- [sbs_gauge_manufacturer_name](../device_power_control_model_reference/P084_sbs_gauge_manufacturer_name_结构体.md)
- [sbs_gauge_device_name](../device_power_control_model_reference/P083_sbs_gauge_device_name_结构体.md)
- [sbs_gauge_device_chemistry](../device_power_control_model_reference/P082_sbs_gauge_device_chemistry_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000013)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000014)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000015)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000016)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000017)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000018)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000019)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000020)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000021)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000022)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000023)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000024)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000025)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000026)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000027)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000028)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000029)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000030)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000031)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000032)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000033)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000034)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000035)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000036)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000037)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000038)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae49908857800bdd010d59895cfad9171a1dc93924386cfd048fb9a1865adb9904"></a>
<a id="ggae49908857800bdd010d59895cfad9171a5e09b018af5608a965396ef1e2378396"></a>
<a id="ggae49908857800bdd010d59895cfad9171a7ca368502befbe58ac68c1aaa24d32ee"></a>
<a id="ggae49908857800bdd010d59895cfad9171a03d7a777cb5ba91b30ccfd70f2088354"></a>
<a id="ggae49908857800bdd010d59895cfad9171aa0b8ca2efc61616b506cd7cfacd4565f"></a>
<a id="ggae49908857800bdd010d59895cfad9171a283ff8ac8f5a631f945978f9406a9984"></a>
<a id="ggae49908857800bdd010d59895cfad9171a172b412826714ecb2646b6ad2b58f36d"></a>
<a id="ggae49908857800bdd010d59895cfad9171a1d6a0e858e2dc84cb6f4075e2a65e83c"></a>
<a id="ggae49908857800bdd010d59895cfad9171afa3d404c62c20357d29954c25b8df174"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac062721584d09b505459578d48920eb9"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac1d52a779ab0839940b1c0425021211b"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac265b9e9137c4dbd424d833c50b2d828"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac72a3d57ec3180f4c9f2f935d0e7e7d4"></a>
<a id="ggae49908857800bdd010d59895cfad9171a3515db092af7dfa2d9a8b879e0b56d1e"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac1662da61e51fb388ba2e6e0258c8abd"></a>
<a id="ggae49908857800bdd010d59895cfad9171a8d0ac3331a389394b603a00d0a47498f"></a>
<a id="ggae49908857800bdd010d59895cfad9171a60cf8dd1cebd9c40182f18248e931399"></a>
<a id="ggae49908857800bdd010d59895cfad9171a12d7ce8ed1c981a621023b4dbb870dfd"></a>
<a id="ggae49908857800bdd010d59895cfad9171a4feeb0b0add43143c8f99299af5859ce"></a>
<a id="ggae49908857800bdd010d59895cfad9171ab32e931d41dfc627de3433e4f492a7ee"></a>
<a id="ggae49908857800bdd010d59895cfad9171ad4d9f765c0e0e388b71ef1db09034f50"></a>
<a id="ggae49908857800bdd010d59895cfad9171aedfb02866740abf97c6fef10b9e4540b"></a>
<a id="ggae49908857800bdd010d59895cfad9171a2026a7272e1a6c301ea53282f919980b"></a>
<a id="ggae49908857800bdd010d59895cfad9171abd2a87b1ddd0ac5506dbf84d56d4c009"></a>
<a id="ggae49908857800bdd010d59895cfad9171afa8f22eecf3cbc2b5b50a69ce974f99c"></a>
<a id="ggae49908857800bdd010d59895cfad9171a82f58acbd7fdaeaed139d53c08f8dd71"></a>
<a id="ggae49908857800bdd010d59895cfad9171a30f2844c658ee409c3fde351fec19aae"></a>
<a id="ggae49908857800bdd010d59895cfad9171a76ca40b38e4326237c94b4f38dc1680b"></a>
<a id="ggae49908857800bdd010d59895cfad9171a65233c86587ffc944fb0a1f28983932e"></a>
<a id="ggae49908857800bdd010d59895cfad9171aec015967b3aef33ca2728058d6d73b55"></a>
<a id="ggae49908857800bdd010d59895cfad9171aa502c87d68bbeba611155d46dc8aa920"></a>
<a id="ggae49908857800bdd010d59895cfad9171a05746558404244618b7ee9a57c501c40"></a>
<a id="ggae49908857800bdd010d59895cfad9171a7fec7cceee788775b47b6535850b0e67"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac1ea4d609b9286807c9c589ed0b731eb"></a>
<a id="ggae49908857800bdd010d59895cfad9171a46fecbace06cd8fd5450c47446c5adaf"></a>
<a id="ggae49908857800bdd010d59895cfad9171a41aed4740cdf0737e1e142455c5dac58"></a>
<a id="ggae49908857800bdd010d59895cfad9171a4c66491e317f6b27b2f3db0cdda89b1b"></a>
<a id="ggae49908857800bdd010d59895cfad9171abc91a9d5b61293499dea5f2d3da28f70"></a>
<a id="ggae49908857800bdd010d59895cfad9171a4b599ee88b5ddbb0bdb8f30c1fe2796a"></a>
<a id="ggae49908857800bdd010d59895cfad9171a7854fb201a819939868f972e7f89ebd0"></a>
<a id="ggae49908857800bdd010d59895cfad9171af764a8c2759ce4d9628a2381fcd13fec"></a>
<a id="ggae49908857800bdd010d59895cfad9171ad0d24fa3a82a8ec8f2c2a92e8abc75e2"></a>
<a id="ggae49908857800bdd010d59895cfad9171a6d6fa90dd558d14f039b9cd9fcb15b70"></a>
<a id="ggae49908857800bdd010d59895cfad9171a8db1eb3711ad274b042346b6eb3eb38a"></a>
<a id="ggae49908857800bdd010d59895cfad9171a2a968512cd81ed5abb731a1d7709fcf8"></a>
<a id="ggae49908857800bdd010d59895cfad9171ab5cb1ee4ad9445d77a66c88d57f42b10"></a>
<a id="ggae49908857800bdd010d59895cfad9171a6cef175aee0bc2d095d32853c94206d9"></a>
<a id="ggae49908857800bdd010d59895cfad9171ae29582cdad457499ad83cee06ca3ff21"></a>
<a id="ggae49908857800bdd010d59895cfad9171a0a5d8d32ccf8658f88642f33872d94b8"></a>
<a id="ggae49908857800bdd010d59895cfad9171abd2a4cc73d651fa54c9dab634198aeae"></a>
<a id="ggae49908857800bdd010d59895cfad9171a84b472b072be9494cf7d5f9027421772"></a>
<a id="ggae49908857800bdd010d59895cfad9171ad1a57cfd758250b2e3f4b5c4abeac9e7"></a>
<a id="ggae49908857800bdd010d59895cfad9171a367b0beb959a116e81de9cd5f2adbe43"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac7e9e36e2c622474129cf4f51b1782c6"></a>
<a id="ggae49908857800bdd010d59895cfad9171a923809dbcdd526822ffde000137eccee"></a>
<a id="ggae49908857800bdd010d59895cfad9171a58c1b0a39345a7006a8ee0ad6ce01bb4"></a>
<a id="ggae49908857800bdd010d59895cfad9171a09809ae39a4c79e1a35095300d838c78"></a>
<a id="ggae49908857800bdd010d59895cfad9171a4bcd9bf3d2c9c081d9186d30e39ab32a"></a>
<a id="ggae49908857800bdd010d59895cfad9171a328886a8b2318367bb968e4a6c9eba1f"></a>
<a id="ggae49908857800bdd010d59895cfad9171a55cf7fcc30be436fd51d79f9ad675d5c"></a>
<a id="ggae49908857800bdd010d59895cfad9171ae8a61b0db58687634ff57f3c536dfd40"></a>
<a id="ggae49908857800bdd010d59895cfad9171a3c5e7d0ede99656b407f25f114adf24d"></a>
<a id="ggae49908857800bdd010d59895cfad9171a9b300c9edad178b7563f7d5ea3b88833"></a>
<a id="ggae49908857800bdd010d59895cfad9171abfc512152bf56f62d1d67660e03dc2e9"></a>
<a id="ggae49908857800bdd010d59895cfad9171a53744eaac0496db3619baa3b42f96ce6"></a>
<a id="ggae49908857800bdd010d59895cfad9171aa993fbb1a9e04554fff73c7e59cd3783"></a>
<a id="ggae49908857800bdd010d59895cfad9171aa7351ed7cc8ece7cacb97c4308048fb2"></a>
<a id="ggae49908857800bdd010d59895cfad9171aea985dd0c89e41bdd018a2dce143d9b4"></a>
<a id="ggae49908857800bdd010d59895cfad9171aeba3b1d8a5239d4afbe8f1d4753583aa"></a>
<a id="ggae49908857800bdd010d59895cfad9171ac0754d083fa22c7f07cfd8846b3bdbd5"></a>
<a id="ggae49908857800bdd010d59895cfad9171a34dbed1768f1787d8269ef30c2478c53"></a>
<a id="ggae49908857800bdd010d59895cfad9171aae228a0e3ab76368fbddeff8dd5d1458"></a>
<a id="ggae49908857800bdd010d59895cfad9171a28e13cd37929f2a6f9d781fc0e73b815"></a>
<a id="ggae49908857800bdd010d59895cfad9171a6701a1d959a3e7f8312db43e3ea23584"></a>
<a id="ggae49908857800bdd010d59895cfad9171a7540e8f2dc74eb66630ab44b5621bd81"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_以太网介质无关接口支持函数（Ethernet MII Support Functions）.md) · [返回大纲](大纲.md) · [下一章](P013_MAX30009 API主题.md)
