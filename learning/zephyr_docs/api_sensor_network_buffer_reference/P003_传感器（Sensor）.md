---
id: learning.zephyr-docs.api-sensor-network-buffer-reference.page-3
title: 传感器（Sensor）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_传感器（Sensor）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器接口。

<a id="details"></a>

传感器接口（Sensor Interfaces）。引入版本（Since）：1.2。接口版本（Version）：1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_battery_5Fapis"></a>

相关声明：[电池 API（Battery APIs）](../api_service_topic_reference/P001_电池 API（Battery APIs）.md)。

电池 API（Battery API）

<a id="r_sensor_5Finterface_5Fext"></a>

相关声明：[设备专用传感器 API 扩展和设备树常量。](../api_topic_reference/P061_设备专用传感器 API 扩展和设备树常量。.md)。

<a id="r_sensor_5Finterface_5Fbackend"></a>

相关声明：[传感器驱动后端 API](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md)。

<a id="r_sensor_5Femulator_5Fbackend"></a>

相关声明：[传感器仿真器后端 API](../hardware/P494_传感器仿真后端接口.md)。

传感器仿真器后端 API

<a id="header-files"></a>
<a id="files"></a>

## 3.2\_文件（Files）

<a id="r_sensor_2Eh"></a>

```c
file sensor.h
```

相关声明：[sensor.h](../api_file_media_sensor_reference/P007_zephyr__drivers__sensor.h_文件参考.md)。

传感器（Sensor）驱动API的主头文件。

<a id="r_tcs34725_2Eh"></a>

```c
file tcs34725.h
```

相关声明：[tcs34725.h](../api_file_network_device_reference/P041_zephyr__drivers__sensor__tcs34725.h_文件参考.md)。

TCS34725颜色传感器（Color Sensor）的公共头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.3\_数据结构（Data Structures）

<a id="r_sensor_5Fvalue"></a>

```c
struct sensor_value
```

相关声明：[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

传感器读出值（Sensor Readout Value）的表示。

<a id="r_sensor_5Ftrigger"></a>

```c
struct sensor_trigger
```

相关声明：[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)。

传感器触发器规格（Sensor Trigger Spec）。

<a id="r_sensor_5Fchan_5Fspec"></a>

```c
struct sensor_chan_spec
```

相关声明：[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

传感器通道规格（Sensor Channel Specification）。

<a id="r_sensor_5Fdecoder_5Fapi"></a>

```c
struct sensor_decoder_api
```

相关声明：[sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)。

解码单个原始数据缓冲区。

<a id="r_sensor_5Fdecode_5Fcontext"></a>

```c
struct sensor_decode_context
```

相关声明：[sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)。

用于通过sensor_decoder_api遍历数据帧（Data Frames）。

<a id="r_sensor_5Fstream_5Ftrigger"></a>

```c
struct sensor_stream_trigger
```

相关声明：[sensor_stream_trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md)。

<a id="r_sensor_5Fread_5Fconfig"></a>

```c
struct sensor_read_config
```

相关声明：[sensor_read_config](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md)。

<a id="r_sensor_5Fdata_5Fgeneric_5Fheader"></a>

```c
struct sensor_data_generic_header
```

相关声明：[sensor_data_generic_header](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.4\_宏定义（Macros）

<a id="r_ga32f679a4004b5707b2de00eb580d0930"></a>

```c
#define SENSOR_CHANNEL_3_AXIS(chan)
```

相关声明：[SENSOR_CHANNEL_3_AXIS](#ga32f679a4004b5707b2de00eb580d0930)。

检查给定通道是否为三轴通道（3-axis Channel）。

<a id="r_ga8bec69db645c9f4d58b396f4d025d0d8"></a>

```c
#define SENSOR_CHANNEL_IS_ACCEL(chan)
```

相关声明：[SENSOR_CHANNEL_IS_ACCEL](#ga8bec69db645c9f4d58b396f4d025d0d8)。

检查给定通道是否为加速度计通道（Accelerometer）。

<a id="r_gafac19bf89f1cca6f9a208676588184ae"></a>

```c
#define SENSOR_CHANNEL_IS_GYRO(chan)
```

相关声明：[SENSOR_CHANNEL_IS_GYRO](#gafac19bf89f1cca6f9a208676588184ae)。

检查给定通道是否为陀螺仪通道（Gyroscope）。

<a id="r_gae69ec503df53d2d5ee417e481f9ac9ea"></a>

```c
#define SENSOR_DECODE_CONTEXT_INIT(decoder_, buffer_, channel_type_, channel_index_)
```

相关声明：[SENSOR_DECODE_CONTEXT_INIT](#gae69ec503df53d2d5ee417e481f9ac9ea)。

初始化 `sensor_decode_context`。

<a id="r_ga9b7b0db322121d220b126d2b5bb7eb73"></a>

```c
#define SENSOR_STREAM_TRIGGER_PREP(_trigger, _opt)
```

相关声明：[SENSOR_STREAM_TRIGGER_PREP](#ga9b7b0db322121d220b126d2b5bb7eb73)。

<a id="r_ga0cc1ee28114557e9e00257071c7dfa9f"></a>

```c
#define SENSOR_DT_READ_IODEV(name, dt_node, ...)
```

相关声明：[SENSOR_DT_READ_IODEV](#ga0cc1ee28114557e9e00257071c7dfa9f)。

定义传感器读取实例（Sensor Reading Instance）。

<a id="r_ga35211c4d908a26f98b1f8d925a9b1374"></a>

```c
#define SENSOR_DT_STREAM_IODEV(name, dt_node, ...)
```

相关声明：[SENSOR_DT_STREAM_IODEV](#ga35211c4d908a26f98b1f8d925a9b1374)。

定义传感器流实例（Sensor Stream Instance）。

<a id="r_ga0066e049c4f084305ca2b978e5c7454d"></a>

```c
#define SENSOR_G 9806650LL
```

相关声明：[SENSOR_G](#ga0066e049c4f084305ca2b978e5c7454d)。

重力加速度常量（Gravitational Constant）的值，以微米每二次方秒（micro m/s²）表示。

<a id="r_ga6ebdc2f6942334de3cc248a53db7df33"></a>

```c
#define SENSOR_PI 3141592LL
```

相关声明：[SENSOR_PI](#ga6ebdc2f6942334de3cc248a53db7df33)。

常量 π（PI）的值，以百万分之一（Micros）为单位表示。

<a id="r_ga7467206da76c3704d2e491d1b1c0973a"></a>

```c
#define SENSOR_INFO_DEFINE(name, ...)
```

相关声明：[SENSOR_INFO_DEFINE](#ga7467206da76c3704d2e491d1b1c0973a)。

<a id="r_ga9e6acbc580e9223bfb86ee8919cdc778"></a>

```c
#define SENSOR_INFO_DT_DEFINE(node_id)
```

相关声明：[SENSOR_INFO_DT_DEFINE](#ga9e6acbc580e9223bfb86ee8919cdc778)。

<a id="r_gaa67ca630e3931a0c3821ba438c86690c"></a>

```c
#define SENSOR_DEVICE_DT_DEFINE(node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SENSOR_DEVICE_DT_DEFINE](#gaa67ca630e3931a0c3821ba438c86690c)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

与 `DEVICE_DT_DEFINE()` 类似，但包含传感器专用内容（Sensor Specifics）。

<a id="r_ga284dc3b9018f14161dc0a2b6bed9a37e"></a>

```c
#define SENSOR_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[SENSOR_DEVICE_DT_INST_DEFINE](#ga284dc3b9018f14161dc0a2b6bed9a37e)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `SENSOR_DEVICE_DT_DEFINE()` 类似的功能。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.5\_类型定义（Typedefs）

<a id="r_ga890c1fb6d6974aea22a2d08829a75902"></a>

```c
typedef void(* sensor_trigger_handler_t) (const struct device *dev, const struct sensor_trigger *trigger)
```

相关声明：[sensor_trigger_handler_t](#ga890c1fb6d6974aea22a2d08829a75902)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)。

触发器触发时的回调 API（Callback API upon Trigger Firing）。

<a id="r_gaa8cd6e4fadb5d69e59d101733b4fb462"></a>

```c
typedef void(* sensor_processing_callback_t) (int result, uint8_t *buf, uint32_t buf_len, void *userdata)
```

相关声明：[sensor_processing_callback_t](#gaa8cd6e4fadb5d69e59d101733b4fb462)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

与辅助处理函数（Helper Processing Function）配合使用的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.6\_枚举（Enumerations）

<a id="r_gaaa1b502bc029b10d7b23b0a25ef4e934"></a>

```c
enum sensor_channel { SENSOR_CHAN_ACCEL_X , SENSOR_CHAN_ACCEL_Y , SENSOR_CHAN_ACCEL_Z , SENSOR_CHAN_ACCEL_XYZ , SENSOR_CHAN_GYRO_X , SENSOR_CHAN_GYRO_Y , SENSOR_CHAN_GYRO_Z , SENSOR_CHAN_GYRO_XYZ , SENSOR_CHAN_MAGN_X , SENSOR_CHAN_MAGN_Y , SENSOR_CHAN_MAGN_Z , SENSOR_CHAN_MAGN_XYZ , SENSOR_CHAN_DIE_TEMP , SENSOR_CHAN_AMBIENT_TEMP , SENSOR_CHAN_PRESS , SENSOR_CHAN_PROX , SENSOR_CHAN_HUMIDITY , SENSOR_CHAN_AMBIENT_LIGHT , SENSOR_CHAN_LIGHT , SENSOR_CHAN_IR , SENSOR_CHAN_RED , SENSOR_CHAN_GREEN , SENSOR_CHAN_BLUE , SENSOR_CHAN_ALTITUDE , SENSOR_CHAN_PM_1_0_CF , SENSOR_CHAN_PM_2_5_CF , SENSOR_CHAN_PM_10_CF , SENSOR_CHAN_PM_1_0 , SENSOR_CHAN_PM_2_5 , SENSOR_CHAN_PM_10 , SENSOR_CHAN_PM_0_3_COUNT , SENSOR_CHAN_PM_0_5_COUNT , SENSOR_CHAN_PM_1_0_COUNT , SENSOR_CHAN_PM_2_5_COUNT , SENSOR_CHAN_PM_5_COUNT , SENSOR_CHAN_PM_10_COUNT , SENSOR_CHAN_DISTANCE , SENSOR_CHAN_CO2 , SENSOR_CHAN_O2 , SENSOR_CHAN_VOC , SENSOR_CHAN_GAS_RES , SENSOR_CHAN_FLOW_RATE , SENSOR_CHAN_VOLUME , SENSOR_CHAN_VOLTAGE , SENSOR_CHAN_VSHUNT , SENSOR_CHAN_CURRENT , SENSOR_CHAN_POWER , SENSOR_CHAN_RESISTANCE , SENSOR_CHAN_ROTATION , SENSOR_CHAN_POS_DX , SENSOR_CHAN_POS_DY , SENSOR_CHAN_POS_DZ , SENSOR_CHAN_POS_DXYZ , SENSOR_CHAN_RPM , SENSOR_CHAN_FREQUENCY , SENSOR_CHAN_GAUGE_VOLTAGE , SENSOR_CHAN_GAUGE_AVG_CURRENT , SENSOR_CHAN_GAUGE_STDBY_CURRENT , SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT , SENSOR_CHAN_GAUGE_TEMP , SENSOR_CHAN_GAUGE_STATE_OF_CHARGE , SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY , SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY , SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY , SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY , SENSOR_CHAN_GAUGE_AVG_POWER , SENSOR_CHAN_GAUGE_STATE_OF_HEALTH , SENSOR_CHAN_GAUGE_TIME_TO_EMPTY , SENSOR_CHAN_GAUGE_TIME_TO_FULL , SENSOR_CHAN_GAUGE_CYCLE_COUNT , SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE , SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE , SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT , SENSOR_CHAN_GAME_ROTATION_VECTOR , SENSOR_CHAN_GRAVITY_VECTOR , SENSOR_CHAN_GBIAS_XYZ , SENSOR_CHAN_ENCODER_COUNT , SENSOR_CHAN_ENCODER_REVOLUTIONS , SENSOR_CHAN_ALL , SENSOR_CHAN_COMMON_COUNT , SENSOR_CHAN_PRIV_START = SENSOR_CHAN_COMMON_COUNT , SENSOR_CHAN_MAX = INT16_MAX }
```

相关声明：[sensor_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934)、[SENSOR_CHAN_ACCEL_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)、[SENSOR_CHAN_ACCEL_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)、[SENSOR_CHAN_ACCEL_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)、[SENSOR_CHAN_ACCEL_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)、[SENSOR_CHAN_GYRO_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)、[SENSOR_CHAN_GYRO_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)、[SENSOR_CHAN_GYRO_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)、[SENSOR_CHAN_GYRO_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)、[SENSOR_CHAN_MAGN_X](#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)、[SENSOR_CHAN_MAGN_Y](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)、[SENSOR_CHAN_MAGN_Z](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)、[SENSOR_CHAN_MAGN_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)、[SENSOR_CHAN_DIE_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)、[SENSOR_CHAN_AMBIENT_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)、[SENSOR_CHAN_PRESS](#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)、[SENSOR_CHAN_PROX](#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)、[SENSOR_CHAN_HUMIDITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)、[SENSOR_CHAN_AMBIENT_LIGHT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127)、[SENSOR_CHAN_LIGHT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)、[SENSOR_CHAN_IR](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)、[SENSOR_CHAN_RED](#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)、[SENSOR_CHAN_GREEN](#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)、[SENSOR_CHAN_BLUE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)、[SENSOR_CHAN_ALTITUDE](#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)、[SENSOR_CHAN_PM_1_0_CF](#ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872)、[SENSOR_CHAN_PM_2_5_CF](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2)、[SENSOR_CHAN_PM_10_CF](#ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379)、[SENSOR_CHAN_PM_1_0](#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)、[SENSOR_CHAN_PM_2_5](#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)、[SENSOR_CHAN_PM_10](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)、[SENSOR_CHAN_PM_0_3_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a)、[SENSOR_CHAN_PM_0_5_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c)、[SENSOR_CHAN_PM_1_0_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6)、[SENSOR_CHAN_PM_2_5_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4)、[SENSOR_CHAN_PM_5_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2)、[SENSOR_CHAN_PM_10_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060)、[SENSOR_CHAN_DISTANCE](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)、[SENSOR_CHAN_CO2](#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)、[SENSOR_CHAN_O2](#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9)、[SENSOR_CHAN_VOC](#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)、[SENSOR_CHAN_GAS_RES](#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)、[SENSOR_CHAN_FLOW_RATE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42)、[SENSOR_CHAN_VOLUME](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab)、[SENSOR_CHAN_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)、[SENSOR_CHAN_VSHUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)、[SENSOR_CHAN_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)、[SENSOR_CHAN_POWER](#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)、[SENSOR_CHAN_RESISTANCE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)、[SENSOR_CHAN_ROTATION](#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)、[SENSOR_CHAN_POS_DX](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)、[SENSOR_CHAN_POS_DY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)、[SENSOR_CHAN_POS_DZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)、[SENSOR_CHAN_POS_DXYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)、[SENSOR_CHAN_RPM](#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)、[SENSOR_CHAN_FREQUENCY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212)、[SENSOR_CHAN_GAUGE_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)、[SENSOR_CHAN_GAUGE_AVG_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)、[SENSOR_CHAN_GAUGE_STDBY_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)、[SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)、[SENSOR_CHAN_GAUGE_TEMP](#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)、[SENSOR_CHAN_GAUGE_STATE_OF_CHARGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)、[SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)、[SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)、[SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)、[SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY](#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)、[SENSOR_CHAN_GAUGE_AVG_POWER](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)、[SENSOR_CHAN_GAUGE_STATE_OF_HEALTH](#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)、[SENSOR_CHAN_GAUGE_TIME_TO_EMPTY](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)、[SENSOR_CHAN_GAUGE_TIME_TO_FULL](#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)、[SENSOR_CHAN_GAUGE_CYCLE_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)、[SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)、[SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE](#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)、[SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)、[SENSOR_CHAN_GAME_ROTATION_VECTOR](#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)、[SENSOR_CHAN_GRAVITY_VECTOR](#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)、[SENSOR_CHAN_GBIAS_XYZ](#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)、[SENSOR_CHAN_ENCODER_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad)、[SENSOR_CHAN_ENCODER_REVOLUTIONS](#ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e)、[SENSOR_CHAN_ALL](#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)、[SENSOR_CHAN_COMMON_COUNT](#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)、[SENSOR_CHAN_PRIV_START](#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)、[SENSOR_CHAN_MAX](#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)。

传感器通道（Sensor Channels）。

<a id="r_ga08215279400e8c9eb05ce4e4f0898ffd"></a>

```c
enum sensor_trigger_type { SENSOR_TRIG_TIMER , SENSOR_TRIG_DATA_READY , SENSOR_TRIG_DELTA , SENSOR_TRIG_NEAR_FAR , SENSOR_TRIG_THRESHOLD , SENSOR_TRIG_TAP , SENSOR_TRIG_DOUBLE_TAP , SENSOR_TRIG_FREEFALL , SENSOR_TRIG_MOTION , SENSOR_TRIG_STATIONARY , SENSOR_TRIG_FIFO_WATERMARK , SENSOR_TRIG_FIFO_FULL , SENSOR_TRIG_TILT , SENSOR_TRIG_OVERFLOW , SENSOR_TRIG_COMMON_COUNT , SENSOR_TRIG_PRIV_START = SENSOR_TRIG_COMMON_COUNT , SENSOR_TRIG_MAX = INT16_MAX }
```

相关声明：[sensor_trigger_type](#ga08215279400e8c9eb05ce4e4f0898ffd)、[SENSOR_TRIG_TIMER](#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)、[SENSOR_TRIG_DATA_READY](#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)、[SENSOR_TRIG_DELTA](#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)、[SENSOR_TRIG_NEAR_FAR](#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)、[SENSOR_TRIG_THRESHOLD](#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)、[SENSOR_TRIG_TAP](#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)、[SENSOR_TRIG_DOUBLE_TAP](#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)、[SENSOR_TRIG_FREEFALL](#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)、[SENSOR_TRIG_MOTION](#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)、[SENSOR_TRIG_STATIONARY](#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)、[SENSOR_TRIG_FIFO_WATERMARK](#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)、[SENSOR_TRIG_FIFO_FULL](#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)、[SENSOR_TRIG_TILT](#gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf)、[SENSOR_TRIG_OVERFLOW](#gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409)、[SENSOR_TRIG_COMMON_COUNT](#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)、[SENSOR_TRIG_PRIV_START](#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)、[SENSOR_TRIG_MAX](#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)。

传感器触发器类型（Sensor Trigger Types）。

<a id="r_ga0dcb6842bc969492bd1c9eb49708940b"></a>

```c
enum sensor_attribute { SENSOR_ATTR_SAMPLING_FREQUENCY , SENSOR_ATTR_LOWER_THRESH , SENSOR_ATTR_UPPER_THRESH , SENSOR_ATTR_SLOPE_TH , SENSOR_ATTR_SLOPE_DUR , SENSOR_ATTR_HYSTERESIS , SENSOR_ATTR_OVERSAMPLING , SENSOR_ATTR_FULL_SCALE , SENSOR_ATTR_OFFSET , SENSOR_ATTR_CALIB_TARGET , SENSOR_ATTR_CONFIGURATION , SENSOR_ATTR_CALIBRATION , SENSOR_ATTR_FEATURE_MASK , SENSOR_ATTR_ALERT , SENSOR_ATTR_FF_DUR , SENSOR_ATTR_BATCH_DURATION , SENSOR_ATTR_GAIN , SENSOR_ATTR_RESOLUTION , SENSOR_ATTR_CHIP_ID , SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_PRIV_START = SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_MAX = INT16_MAX }
```

相关声明：[sensor_attribute](#ga0dcb6842bc969492bd1c9eb49708940b)、[SENSOR_ATTR_SAMPLING_FREQUENCY](#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)、[SENSOR_ATTR_LOWER_THRESH](#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)、[SENSOR_ATTR_UPPER_THRESH](#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)、[SENSOR_ATTR_SLOPE_TH](#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)、[SENSOR_ATTR_SLOPE_DUR](#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)、[SENSOR_ATTR_HYSTERESIS](#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)、[SENSOR_ATTR_OVERSAMPLING](#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)、[SENSOR_ATTR_FULL_SCALE](#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)、[SENSOR_ATTR_OFFSET](#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)、[SENSOR_ATTR_CALIB_TARGET](#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)、[SENSOR_ATTR_CONFIGURATION](#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)、[SENSOR_ATTR_CALIBRATION](#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)、[SENSOR_ATTR_FEATURE_MASK](#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)、[SENSOR_ATTR_ALERT](#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)、[SENSOR_ATTR_FF_DUR](#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)、[SENSOR_ATTR_BATCH_DURATION](#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)、[SENSOR_ATTR_GAIN](#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3)、[SENSOR_ATTR_RESOLUTION](#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d)、[SENSOR_ATTR_CHIP_ID](#gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c)、[SENSOR_ATTR_COMMON_COUNT](#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)、[SENSOR_ATTR_PRIV_START](#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)、[SENSOR_ATTR_MAX](#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)。

传感器属性类型（Sensor Attribute Types）。

<a id="r_ga8613a20521a37d40fd7371dc63ba2dac"></a>

```c
enum sensor_stream_data_opt { SENSOR_STREAM_DATA_INCLUDE = 0 , SENSOR_STREAM_DATA_NOP = 1 , SENSOR_STREAM_DATA_DROP = 2 }
```

相关声明：[sensor_stream_data_opt](#ga8613a20521a37d40fd7371dc63ba2dac)、[SENSOR_STREAM_DATA_INCLUDE](#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)、[SENSOR_STREAM_DATA_NOP](#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)、[SENSOR_STREAM_DATA_DROP](#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)。

触发器被消费（Trigger Consumed）时，关联数据的处理方式选项（Data Handling Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.7\_函数（Functions）

<a id="r_gae95715ffea5da18a9593ec2add029824"></a>

```c
static bool sensor_chan_spec_eq (struct sensor_chan_spec chan_spec0, struct sensor_chan_spec chan_spec1)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sensor_chan_spec_eq](#gae95715ffea5da18a9593ec2add029824)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

检查通道规格（Channel Specs）是否等价。

<a id="r_ga018bca56056ae2558f9e45aeb2fa5f53"></a>

```c
static int sensor_decode (struct sensor_decode_context *ctx, void *out, uint16_t max_count)
```

相关声明：[sensor_decode](#ga018bca56056ae2558f9e45aeb2fa5f53)、[sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用 `sensor_decode_context` 解码 N 帧（Frames）。

<a id="r_ga2b045cdbd4d1ca37beed69970093945b"></a>

```c
int sensor_natively_supported_channel_size_info (struct sensor_chan_spec channel, size_t *base_size, size_t *frame_size)
```

相关声明：[sensor_natively_supported_channel_size_info](#ga2b045cdbd4d1ca37beed69970093945b)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

<a id="r_gafbf65226a227e9f8824908bc38e336f5"></a>

```c
int sensor_attr_set (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value *val)
```

相关声明：[sensor_attr_set](#gafbf65226a227e9f8824908bc38e336f5)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

设置传感器属性（Sensor Attribute）。

<a id="r_gaedfdfc71dce702dc1fb1c6e60ff0f73a"></a>

```c
int sensor_attr_get (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value *val)
```

相关声明：[sensor_attr_get](#gaedfdfc71dce702dc1fb1c6e60ff0f73a)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

获取传感器属性（Sensor Attribute）。

<a id="r_ga7c72aca732e0641612d2f9437c2e41b7"></a>

```c
static int sensor_trigger_set (const struct device *dev, const struct sensor_trigger *trig, sensor_trigger_handler_t handler)
```

相关声明：[sensor_trigger_set](#ga7c72aca732e0641612d2f9437c2e41b7)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)、[sensor_trigger_handler_t](#ga890c1fb6d6974aea22a2d08829a75902)。

激活传感器触发器（Sensor Trigger），并设置触发器处理程序（Trigger Handler）。

<a id="r_gaa75e25d93ee7cac0bf38399f3c006dff"></a>

```c
int sensor_sample_fetch (const struct device *dev)
```

相关声明：[sensor_sample_fetch](#gaa75e25d93ee7cac0bf38399f3c006dff)、[device](../device_reference/P002_设备对象结构.md)。

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

<a id="r_gac16192826432438a15274cf28d66e8a6"></a>

```c
int sensor_sample_fetch_chan (const struct device *dev, enum sensor_channel type)
```

相关声明：[sensor_sample_fetch_chan](#gac16192826432438a15274cf28d66e8a6)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934)。

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

<a id="r_ga9e0e6c1408d32c52267984bae7cb268d"></a>

```c
int sensor_channel_get (const struct device *dev, enum sensor_channel chan, struct sensor_value *val)
```

相关声明：[sensor_channel_get](#ga9e0e6c1408d32c52267984bae7cb268d)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从传感器设备获取读数（Reading）。

<a id="r_ga12db6fc43adce48d34c25c16fd2336a3"></a>

```c
int sensor_get_decoder (const struct device *dev, const struct sensor_decoder_api **decoder)
```

相关声明：[sensor_get_decoder](#ga12db6fc43adce48d34c25c16fd2336a3)、[device](../device_reference/P002_设备对象结构.md)、[sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)。

获取传感器的解码器 API（Decoder API）。

<a id="r_ga759d6581b83751bab5e56b9f8bb1676d"></a>

```c
int sensor_reconfigure_read_iodev (const struct rtio_iodev *iodev, const struct device *sensor, const struct sensor_chan_spec *channels, size_t num_channels)
```

相关声明：[sensor_reconfigure_read_iodev](#ga759d6581b83751bab5e56b9f8bb1676d)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[device](../device_reference/P002_设备对象结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

重新配置读取用输入／输出设备（Reading I/O Device，`iodev`）。

<a id="r_ga58bb95758fc4bd2927c93671727e6080"></a>

```c
static int sensor_stream (const struct rtio_iodev *iodev, struct rtio *ctx, void *userdata, rtio_sqe_handle_t *handle)
```

相关声明：[sensor_stream](#ga58bb95758fc4bd2927c93671727e6080)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)。

<a id="r_gace7f20e29b302e607ba274fe40a2c2bd"></a>

```c
static int sensor_read (const struct rtio_iodev *iodev, struct rtio *ctx, uint8_t *buf, size_t buf_len)
```

相关声明：[sensor_read](#gace7f20e29b302e607ba274fe40a2c2bd)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以阻塞方式（Blocking）从传感器单次读取样本到缓冲区。

<a id="r_gaf53b015c47acab3c3acb4cb1d8ab827d"></a>

```c
static int sensor_read_async_mempool (const struct rtio_iodev *iodev, struct rtio *ctx, void *userdata)
```

相关声明：[sensor_read_async_mempool](#gaf53b015c47acab3c3acb4cb1d8ab827d)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

使用从缓冲池（Pool）分配的缓冲区，进行单次非阻塞读取（Non-blocking Read）。

<a id="r_gabb076531445e1b128d515b28c7cc9dc8"></a>

```c
void sensor_processing_with_callback (struct rtio *ctx, sensor_processing_callback_t cb)
```

相关声明：[sensor_processing_with_callback](#gabb076531445e1b128d515b28c7cc9dc8)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[sensor_processing_callback_t](#gaa8cd6e4fadb5d69e59d101733b4fb462)。

用于传感器数据通用处理（Common Processing）的辅助函数。

<a id="r_gab797f2f578b1c9cc44f54ab5d503bbf8"></a>

```c
static int32_t sensor_ms2_to_g (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_g](#gab797f2f578b1c9cc44f54ab5d503bbf8)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为标准重力加速度倍数（Gs）的辅助函数。

<a id="r_ga6ab9ce9c6ee2e52d197e5cb4ccd88979"></a>

```c
static void sensor_g_to_ms2 (int32_t g, struct sensor_value *ms2)
```

相关声明：[sensor_g_to_ms2](#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从标准重力加速度倍数（Gs）转换为 m/s² 的辅助函数。

<a id="r_ga9e0fb14f84dca02497ce5bff10b51ab8"></a>

```c
static int32_t sensor_ms2_to_mg (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_mg](#ga9e0fb14f84dca02497ce5bff10b51ab8)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为毫重力加速度单位（milli Gs）的辅助函数。

<a id="r_ga3db980100e634310a0a1623136048742"></a>

```c
static int32_t sensor_ms2_to_ug (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_ug](#ga3db980100e634310a0a1623136048742)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为微重力加速度单位（micro Gs）的辅助函数。

<a id="r_ga28a1c6cf74a391712a4697792f759d62"></a>

```c
static void sensor_ug_to_ms2 (int32_t ug, struct sensor_value *ms2)
```

相关声明：[sensor_ug_to_ms2](#ga28a1c6cf74a391712a4697792f759d62)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从微重力加速度单位（micro Gs）转换为 m/s² 的辅助函数。

<a id="r_ga040a907c8934baab66d27b8dfb1ea220"></a>

```c
static int32_t sensor_rad_to_degrees (const struct sensor_value *rad)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_rad_to_degrees](#ga040a907c8934baab66d27b8dfb1ea220)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将弧度（Radian）转换为度（Degree）的辅助函数。

<a id="r_ga39d4b84f5d792e27b2d6d5eb6a2ccb0d"></a>

```c
static void sensor_degrees_to_rad (int32_t d, struct sensor_value *rad)
```

相关声明：[sensor_degrees_to_rad](#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将度（Degree）转换为弧度（Radian）的辅助函数。

<a id="r_gad80093a6cfe95428dd0ead85547838a6"></a>

```c
static int32_t sensor_rad_to_10udegrees (const struct sensor_value *rad)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_rad_to_10udegrees](#gad80093a6cfe95428dd0ead85547838a6)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将弧度（Radian）转换为以 10 微度（10 Micro Degrees）为单位的数值的辅助函数。

<a id="r_gab53418e1eb164364663d3ec3f40399a4"></a>

```c
static void sensor_10udegrees_to_rad (int32_t d, struct sensor_value *rad)
```

相关声明：[sensor_10udegrees_to_rad](#gab53418e1eb164364663d3ec3f40399a4)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将以 10 微度（10 Micro Degrees）为单位的数值转换为弧度（Radian）的辅助函数。

<a id="r_ga29223b754dc436ab1e97ce6209a3ea06"></a>

```c
static double sensor_value_to_double (const struct sensor_value *val)
```

相关声明：[sensor_value_to_double](#ga29223b754dc436ab1e97ce6209a3ea06)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为双精度浮点数（`double`）的辅助函数。

<a id="r_ga2ad1fc2abd1c8c38e7de6e99fa5c1f20"></a>

```c
static float sensor_value_to_float (const struct sensor_value *val)
```

相关声明：[sensor_value_to_float](#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为单精度浮点数（`float`）的辅助函数。

<a id="r_gab4c95b7857294a9148afe6e9bcb5eacf"></a>

```c
static int sensor_value_to_fixed_point (uint32_t *val, struct sensor_value *inp, uint8_t m, uint8_t n, bool is_signed)
```

相关声明：[sensor_value_to_fixed_point](#gab4c95b7857294a9148afe6e9bcb5eacf)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将 `struct sensor_value` 转换为定点数（Fixed-point）的辅助函数。

<a id="r_gaf01bbb251ad0c7f6c55c5b702e8a4048"></a>

```c
static int sensor_value_from_double (struct sensor_value *val, double inp)
```

相关声明：[sensor_value_from_double](#gaf01bbb251ad0c7f6c55c5b702e8a4048)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将双精度浮点数（`double`）转换为 `struct sensor_value` 的辅助函数。

<a id="r_ga64d5a1725eda200c80daf42b1067c46c"></a>

```c
static int sensor_value_from_float (struct sensor_value *val, float inp)
```

相关声明：[sensor_value_from_float](#ga64d5a1725eda200c80daf42b1067c46c)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将单精度浮点数（`float`）转换为 `struct sensor_value` 的辅助函数。

<a id="r_ga767c7d0147699c556a2f4d429501ff99"></a>

```c
static int sensor_value_from_fixed_point (struct sensor_value *val, uint32_t inp, uint8_t m, uint8_t n, bool is_signed)
```

相关声明：[sensor_value_from_fixed_point](#ga767c7d0147699c556a2f4d429501ff99)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将定点数（Fixed-point）转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabbcb8ad4b9484cba77ae65e2d3ba7457"></a>

```c
static int64_t sensor_value_to_deci (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_deci](#gabbcb8ad4b9484cba77ae65e2d3ba7457)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以十分之一单位（Deci Units）计数的整数的辅助函数。

<a id="r_gae812fb481bfe3a8053f0fc23f8617434"></a>

```c
static int64_t sensor_value_to_centi (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_centi](#gae812fb481bfe3a8053f0fc23f8617434)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以百分之一单位（Centi Units）计数的整数的辅助函数。

<a id="r_ga6d69a9644e08a9cd7773645fa11293e3"></a>

```c
static int64_t sensor_value_to_milli (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_milli](#ga6d69a9644e08a9cd7773645fa11293e3)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以千分之一单位（Milli Units）计数的整数的辅助函数。

<a id="r_ga9bf7faf60aa54a7540e9b73a61864e25"></a>

```c
static int64_t sensor_value_to_micro (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_micro](#ga9bf7faf60aa54a7540e9b73a61864e25)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以百万分之一单位（Micro Units）计数的整数的辅助函数。

<a id="r_ga88b2605526e37420db871f066c5053b3"></a>

```c
static int sensor_value_from_milli (struct sensor_value *val, int64_t milli)
```

相关声明：[sensor_value_from_milli](#ga88b2605526e37420db871f066c5053b3)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将以千分之一单位（Milli Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabff019c63c89cbc546c0981819040c99"></a>

```c
static int sensor_value_from_micro (struct sensor_value *val, int64_t micro)
```

相关声明：[sensor_value_from_micro](#gabff019c63c89cbc546c0981819040c99)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将以百万分之一单位（Micro Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabf3b46a1e88e65575e25acc1a43aba10"></a>

```c
static int sensor_value_add (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_add](#gabf3b46a1e88e65575e25acc1a43aba10)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相加的辅助函数。

<a id="r_gac17a55d53ccd2a2e8b45109e984cc80b"></a>

```c
static int sensor_value_subtract (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_subtract](#gac17a55d53ccd2a2e8b45109e984cc80b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相减的辅助函数。

<a id="r_gacdb8dc2095e6a15db0a58233cab8ffe2"></a>

```c
static int sensor_value_multiply (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_multiply](#gacdb8dc2095e6a15db0a58233cab8ffe2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相乘的辅助函数。

<a id="r_ga8d6f33eeda04bdb648bd03a92e981b1d"></a>

```c
static int sensor_value_scale (struct sensor_value *inp, int32_t scalar, struct sensor_value *out)
```

相关声明：[sensor_value_scale](#ga8d6f33eeda04bdb648bd03a92e981b1d)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

缩放（Scale）`struct sensor_value` 的辅助函数。

## 3.8\_详细说明（Detailed Documentation）

<a id="ga32f679a4004b5707b2de00eb580d0930"></a>

### `SENSOR_CHANNEL_3_AXIS`

```c
#define SENSOR_CHANNEL_3_AXIS ( chan)
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
((chan) == SENSOR_CHAN_ACCEL_XYZ || (chan) == SENSOR_CHAN_GYRO_XYZ ||                      \
 (chan) == SENSOR_CHAN_MAGN_XYZ || (chan) == SENSOR_CHAN_POS_DXYZ)
```

检查给定通道是否为三轴通道（3-axis Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chan` | 要检查的通道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 当 `chan` 为 `SENSOR_CHAN_ACCEL_XYZ`、`SENSOR_CHAN_GYRO_XYZ`、`SENSOR_CHAN_MAGN_XYZ` 或 `SENSOR_CHAN_POS_DXYZ` 时。 |
| `false` | 其他情况。 |

<a id="ga8bec69db645c9f4d58b396f4d025d0d8"></a>

### `SENSOR_CHANNEL_IS_ACCEL`

```c
#define SENSOR_CHANNEL_IS_ACCEL ( chan)
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
((chan) == SENSOR_CHAN_ACCEL_XYZ || (chan) == SENSOR_CHAN_ACCEL_X ||   \
 (chan) == SENSOR_CHAN_ACCEL_Y || (chan) == SENSOR_CHAN_ACCEL_Z)
```

检查给定通道是否为加速度计通道（Accelerometer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chan` | 要检查的通道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 当 `chan` 为 `SENSOR_CHAN_ACCEL_XYZ`、`SENSOR_CHAN_ACCEL_X`、`SENSOR_CHAN_ACCEL_Y` 或 `SENSOR_CHAN_ACCEL_Z` 时。 |
| `false` | 其他情况。 |

<a id="gafac19bf89f1cca6f9a208676588184ae"></a>

### `SENSOR_CHANNEL_IS_GYRO`

```c
#define SENSOR_CHANNEL_IS_GYRO ( chan)
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
((chan) == SENSOR_CHAN_GYRO_XYZ || (chan) == SENSOR_CHAN_GYRO_X ||     \
 (chan) == SENSOR_CHAN_GYRO_Y || (chan) == SENSOR_CHAN_GYRO_Z)
```

检查给定通道是否为陀螺仪通道（Gyroscope）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] chan` | 要检查的通道（Channel）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 当 `chan` 为 `SENSOR_CHAN_GYRO_XYZ`、`SENSOR_CHAN_GYRO_X`、`SENSOR_CHAN_GYRO_Y` 或 `SENSOR_CHAN_GYRO_Z` 时。 |
| `false` | 其他情况。 |

<a id="gae69ec503df53d2d5ee417e481f9ac9ea"></a>

### `SENSOR_DECODE_CONTEXT_INIT`

```c
#define SENSOR_DECODE_CONTEXT_INIT ( decoder_, buffer_, channel_type_, channel_index_ )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
{                                                                                          \
        .decoder = (decoder_),                                                             \
        .buffer = (buffer_),                                                               \
        .channel = {.chan_type = (channel_type_), .chan_idx = (channel_index_)},           \
        .fit = 0,                                                                          \
}
```

初始化 `sensor_decode_context`。

<a id="gaa67ca630e3931a0c3821ba438c86690c"></a>

### `SENSOR_DEVICE_DT_DEFINE`

```c
#define SENSOR_DEVICE_DT_DEFINE ( node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ... )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
DEVICE_DT_DEFINE(node_id, init_fn, pm_device,                   \
                 data_ptr, cfg_ptr, level, prio,                \
                 api_ptr, __VA_ARGS__);                         \
                                                                \
SENSOR_INFO_DT_DEFINE(node_id);
```

与 `DEVICE_DT_DEFINE()` 类似，但包含传感器专用内容（Sensor Specifics）。

定义实现传感器 API（Sensor API）的设备。还可能在传感器信息可迭代段（Sensor Info Iterable Section）中定义一个元素，用于枚举所有传感器设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `init_fn` | 驱动初始化函数（Init Function）的名称。 |
| `pm_device` | 电源管理（PM）设备资源引用；设备不使用 PM 时为 `NULL`。 |
| `data_ptr` | 指向设备私有数据（Private Data）的指针。 |
| `cfg_ptr` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `level` | 初始化级别（Initialization Level），详情参见 `SYS_INIT()`。 |
| `prio` | 所选初始化级别内的优先级（Priority），详情参见 `SYS_INIT()`。 |
| `api_ptr` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |

<a id="ga284dc3b9018f14161dc0a2b6bed9a37e"></a>

### `SENSOR_DEVICE_DT_INST_DEFINE`

```c
#define SENSOR_DEVICE_DT_INST_DEFINE ( inst, ... )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
SENSOR_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `SENSOR_DEVICE_DT_DEFINE()` 类似的功能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号（Instance Number）。调用 `SENSOR_DEVICE_DT_DEFINE()` 时，会将它替换为 `DT_DRV_INST(inst)`。 |
| `...` | `SENSOR_DEVICE_DT_DEFINE()` 所要求的其他参数（Parameters）。 |

<a id="ga0cc1ee28114557e9e00257071c7dfa9f"></a>

### `SENSOR_DT_READ_IODEV`

```c
#define SENSOR_DT_READ_IODEV ( name, dt_node, ... )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
static struct sensor_chan_spec _CONCAT(__channel_array_, name)[] = {__VA_ARGS__};          \
static struct sensor_read_config _CONCAT(__sensor_read_config_, name) = {                  \
        .sensor = DEVICE_DT_GET(dt_node),                                                  \
        .is_streaming = false,                                                             \
        .channels = _CONCAT(__channel_array_, name),                                       \
        .count = ARRAY_SIZE(_CONCAT(__channel_array_, name)),                              \
        .max = ARRAY_SIZE(_CONCAT(__channel_array_, name)),                                \
};                                                                                         \
RTIO_IODEV_DEFINE(name, &__sensor_iodev_api, _CONCAT(&__sensor_read_config_, name))
```

定义传感器读取实例（Sensor Reading Instance）。

使用此宏生成用于读取指定通道的 `rtio_iodev`。示例（Example）：

原始示例（Example）：

```c
 (.c)
SENSOR_DT_READ_IODEV(icm42688_accelgyro, DT_NODELABEL(icm42688),
    { SENSOR_CHAN_ACCEL_XYZ, 0 },
    { SENSOR_CHAN_GYRO_XYZ, 0 });

int main(void) {
  sensor_read_async_mempool(&icm42688_accelgyro, &rtio);
}
```

<a id="ga35211c4d908a26f98b1f8d925a9b1374"></a>

### `SENSOR_DT_STREAM_IODEV`

```c
#define SENSOR_DT_STREAM_IODEV ( name, dt_node, ... )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
static struct sensor_stream_trigger _CONCAT(__trigger_array_, name)[] = {__VA_ARGS__};     \
static struct sensor_read_config _CONCAT(__sensor_read_config_, name) = {                  \
        .sensor = DEVICE_DT_GET(dt_node),                                                  \
        .is_streaming = true,                                                              \
        .triggers = _CONCAT(__trigger_array_, name),                                       \
        .count = ARRAY_SIZE(_CONCAT(__trigger_array_, name)),                              \
        .max = ARRAY_SIZE(_CONCAT(__trigger_array_, name)),                                \
};                                                                                         \
RTIO_IODEV_DEFINE(name, &__sensor_iodev_api, &_CONCAT(__sensor_read_config_, name))
```

定义传感器流实例（Sensor Stream Instance）。

使用此宏生成 `rtio_iodev`，用于启动由指定中断触发的数据流（Stream）。示例：

原始示例（Example）：

```c
 (.c)
SENSOR_DT_STREAM_IODEV(imu_stream, DT_ALIAS(imu),
    {SENSOR_TRIG_FIFO_WATERMARK, SENSOR_STREAM_DATA_INCLUDE},
    {SENSOR_TRIG_FIFO_FULL, SENSOR_STREAM_DATA_NOP});

int main(void) {
  rtio_sqe_handle_t handle;
  sensor_stream(&imu_stream, &rtio, NULL, &handle);
  k_msleep(1000);
  rtio_sqe_cancel(&rtio, handle);
}
```

<a id="ga0066e049c4f084305ca2b978e5c7454d"></a>

### `SENSOR_G`

```c
#define SENSOR_G 9806650LL
```

```c
#include <zephyr/drivers/sensor.h>
```

重力加速度常量（Gravitational Constant）的值，以微米每二次方秒（micro m/s²）表示。

<a id="ga7467206da76c3704d2e491d1b1c0973a"></a>

### `SENSOR_INFO_DEFINE`

```c
#define SENSOR_INFO_DEFINE ( name, ... )
```

```c
#include <zephyr/drivers/sensor.h>
```

<a id="ga9e6acbc580e9223bfb86ee8919cdc778"></a>

### `SENSOR_INFO_DT_DEFINE`

```c
#define SENSOR_INFO_DT_DEFINE ( node_id)
```

```c
#include <zephyr/drivers/sensor.h>
```

<a id="ga6ebdc2f6942334de3cc248a53db7df33"></a>

### `SENSOR_PI`

```c
#define SENSOR_PI 3141592LL
```

```c
#include <zephyr/drivers/sensor.h>
```

常量 π（PI）的值，以百万分之一（Micros）为单位表示。

<a id="ga9b7b0db322121d220b126d2b5bb7eb73"></a>

### `SENSOR_STREAM_TRIGGER_PREP`

```c
#define SENSOR_STREAM_TRIGGER_PREP ( _trigger, _opt )
```

```c
#include <zephyr/drivers/sensor.h>
```

展开值（Value）：

```c
{                                                                                          \
        .trigger = (_trigger), .opt = (_opt),                                              \
}
```

<a id="gaa8cd6e4fadb5d69e59d101733b4fb462"></a>

### `sensor_processing_callback_t`

```c
typedef void(* sensor_processing_callback_t) (int result, uint8_t *buf, uint32_t buf_len, void *userdata)
```

```c
#include <zephyr/drivers/sensor.h>
```

与辅助处理函数（Helper Processing Function）配合使用的回调函数（Callback Function）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] result` | 读取操作的结果码（Result Code），`0` 表示成功。 |
| `[in] buf` | 保存传感器数据的数据缓冲区（Data Buffer）。 |
| `[in] buf_len` | `buf` 的长度（Length），单位为字节。 |
| `[in] userdata` | 传给 `sensor_read_async_mempool()` 的可选用户数据（Userdata）。 |

**参阅（See Also）**：另请参见（See Also）：`sensor_processing_with_callback`。

<a id="ga890c1fb6d6974aea22a2d08829a75902"></a>

### `sensor_trigger_handler_t`

```c
typedef void(* sensor_trigger_handler_t) (const struct device *dev, const struct sensor_trigger *trigger)
```

```c
#include <zephyr/drivers/sensor.h>
```

触发器触发时的回调 API（Callback API upon Trigger Firing）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `trigger` | 触发器（Trigger）。 |

<a id="ga0dcb6842bc969492bd1c9eb49708940b"></a>

### `sensor_attribute`

```c
enum sensor_attribute
```

```c
#include <zephyr/drivers/sensor.h>
```

传感器属性类型（Sensor Attribute Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_SAMPLING_FREQUENCY` | 传感器采样频率（Sampling Frequency），即传感器每秒进行测量的次数。 |
| `SENSOR_ATTR_LOWER_THRESH` | 触发下限阈值（Lower Threshold）。 |
| `SENSOR_ATTR_UPPER_THRESH` | 触发上限阈值（Upper Threshold）。 |
| `SENSOR_ATTR_SLOPE_TH` | 任意运动（Any-motion，即斜率 Slope）触发器的阈值。 |
| `SENSOR_ATTR_SLOPE_DUR` | 斜率值（Slope Values）必须持续处于阈值之外的时长，满足后触发。 |
| `SENSOR_ATTR_HYSTERESIS` |  |
| `SENSOR_ATTR_OVERSAMPLING` | 过采样因子（Oversampling Factor）。 |
| `SENSOR_ATTR_FULL_SCALE` | 传感器量程（Sensor Range），采用国际单位制（SI）单位。 |
| `SENSOR_ATTR_OFFSET` | 返回的传感器值将按偏移量（Offset）调整：`final_value = sensor_value + offset`。 |
| `SENSOR_ATTR_CALIB_TARGET` | 校准目标（Calibration Target）。芯片内部算法使用此值，对某个轴或全部轴进行自校准。 |
| `SENSOR_ATTR_CONFIGURATION` | 配置传感器的工作模式（Operating Modes）。 |
| `SENSOR_ATTR_CALIBRATION` | 设置传感器所需的校准值（Calibration Value）。 |
| `SENSOR_ATTR_FEATURE_MASK` | 启用／禁用传感器特性（Sensor Features）。 |
| `SENSOR_ATTR_ALERT` | 告警阈值（Alert Threshold），或启用／禁用告警。 |
| `SENSOR_ATTR_FF_DUR` | 自由落体持续时间（Free-fall Duration），单位为毫秒。如果运行期间改变采样频率，应设置此属性，使自由落体持续时间适应新的采样频率。 |
| `SENSOR_ATTR_BATCH_DURATION` | 硬件批处理持续时间（Hardware Batch Duration），单位为时钟节拍（Ticks）。 |
| `SENSOR_ATTR_GAIN` | 配置传感器增益（Gain）。 |
| `SENSOR_ATTR_RESOLUTION` | 配置传感器分辨率（Resolution）。 |
| `SENSOR_ATTR_CHIP_ID` | 传感器的芯片标识符（Chip ID）。 |
| `SENSOR_ATTR_COMMON_COUNT` | 全部通用传感器属性（Common Sensor Attributes）的数量。 |
| `SENSOR_ATTR_PRIV_START` | 此值及更高值由具体传感器定义（Sensor Specific）。参见传感器头文件。 |
| `SENSOR_ATTR_MAX` | 表示传感器属性类型（Sensor Attribute Type）的最大值。 |

<a id="gaaa1b502bc029b10d7b23b0a25ef4e934"></a>

### `sensor_channel`

```c
enum sensor_channel
```

```c
#include <zephyr/drivers/sensor.h>
```

传感器通道（Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_ACCEL_X` | X 轴加速度（Acceleration），单位为 m/s^2。 |
| `SENSOR_CHAN_ACCEL_Y` | Y 轴加速度（Acceleration），单位为 m/s^2。 |
| `SENSOR_CHAN_ACCEL_Z` | Z 轴加速度（Acceleration），单位为 m/s^2。 |
| `SENSOR_CHAN_ACCEL_XYZ` | X、Y、Z 轴加速度（Acceleration）。 |
| `SENSOR_CHAN_GYRO_X` | 绕 X 轴的角速度（Angular Velocity），单位为 rad/s。 |
| `SENSOR_CHAN_GYRO_Y` | 绕 Y 轴的角速度（Angular Velocity），单位为 rad/s。 |
| `SENSOR_CHAN_GYRO_Z` | 绕 Z 轴的角速度（Angular Velocity），单位为 rad/s。 |
| `SENSOR_CHAN_GYRO_XYZ` | 绕 X、Y、Z 轴的角速度（Angular Velocity）。 |
| `SENSOR_CHAN_MAGN_X` | X 轴磁场（Magnetic Field），单位为高斯（G）。 |
| `SENSOR_CHAN_MAGN_Y` | Y 轴磁场（Magnetic Field），单位为高斯（G）。 |
| `SENSOR_CHAN_MAGN_Z` | Z 轴磁场（Magnetic Field），单位为高斯（G）。 |
| `SENSOR_CHAN_MAGN_XYZ` | X、Y、Z 轴磁场（Magnetic Field）。 |
| `SENSOR_CHAN_DIE_TEMP` | 器件芯片温度（Die Temperature），单位为摄氏度。 |
| `SENSOR_CHAN_AMBIENT_TEMP` | 环境温度（Ambient Temperature），单位为摄氏度。 |
| `SENSOR_CHAN_PRESS` | 压力（Pressure），单位为千帕（kPa）。 |
| `SENSOR_CHAN_PROX` | 接近程度（Proximity），无量纲（Adimensional）。值为 `1` 表示物体靠近。 |
| `SENSOR_CHAN_HUMIDITY` | 湿度（Humidity），单位为百分比。 |
| `SENSOR_CHAN_AMBIENT_LIGHT` | 可见光谱范围内的环境照度（Ambient Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_LIGHT` | 可见光谱范围内的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_IR` | 红外光谱范围内的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_RED` | 红色光谱范围内的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_GREEN` | 绿色光谱范围内的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_BLUE` | 蓝色光谱范围内的照度（Illuminance），单位为勒克斯（lux）。 |
| `SENSOR_CHAN_ALTITUDE` | 海拔高度（Altitude），单位为米。 |
| `SENSOR_CHAN_PM_1_0_CF` | PM1.0 浓度（Concentration），标准颗粒物（Standard Particle），`CF=1`，单位为 µg/m³。 |
| `SENSOR_CHAN_PM_2_5_CF` | PM2.5 浓度（Concentration），标准颗粒物（Standard Particle），`CF=1`，单位为 µg/m³。 |
| `SENSOR_CHAN_PM_10_CF` | PM10 浓度（Concentration），标准颗粒物（Standard Particle），`CF=1`，单位为 µg/m³。 |
| `SENSOR_CHAN_PM_1_0` | 1.0 微米颗粒物（Particulate Matter），单位为 ug/m^3。 |
| `SENSOR_CHAN_PM_2_5` | 2.5 微米颗粒物（Particulate Matter），单位为 ug/m^3。 |
| `SENSOR_CHAN_PM_10` | 10 微米颗粒物（Particulate Matter），单位为 ug/m^3。 |
| `SENSOR_CHAN_PM_0_3_COUNT` | 每 0.1 升空气中粒径 ≥ 0.3 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_PM_0_5_COUNT` | 每 0.1 升空气中粒径 ≥ 0.5 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_PM_1_0_COUNT` | 每 0.1 升空气中粒径 ≥ 1.0 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_PM_2_5_COUNT` | 每 0.1 升空气中粒径 ≥ 2.5 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_PM_5_COUNT` | 每 0.1 升空气中粒径 ≥ 5.0 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_PM_10_COUNT` | 每 0.1 升空气中粒径 ≥ 10.0 µm 的颗粒数量（Particle Count）。 |
| `SENSOR_CHAN_DISTANCE` | 距离（Distance），从传感器到目标，单位为米。 |
| `SENSOR_CHAN_CO2` | 二氧化碳（CO2）浓度，单位为百万分之一（ppm）。 |
| `SENSOR_CHAN_O2` | 氧气（O2）浓度，单位为百万分之一（ppm）。 |
| `SENSOR_CHAN_VOC` | 挥发性有机化合物（VOC）浓度，单位为十亿分之一（ppb）。 |
| `SENSOR_CHAN_GAS_RES` | 气体传感器电阻（Gas Sensor Resistance），单位为欧姆。 |
| `SENSOR_CHAN_FLOW_RATE` | 流量（Flow Rate），单位为升／分钟。 |
| `SENSOR_CHAN_VOLUME` | 流体体积（Flow Volume），单位为升。 |
| `SENSOR_CHAN_VOLTAGE` | 电压（Voltage），单位为伏特。 |
| `SENSOR_CHAN_VSHUNT` | 电流分流器电压（Current Shunt Voltage），单位为毫伏。 |
| `SENSOR_CHAN_CURRENT` | 电流（Current），单位为安培。 |
| `SENSOR_CHAN_POWER` | 功率（Power），单位为瓦特。 |
| `SENSOR_CHAN_RESISTANCE` | 电阻（Resistance），单位为欧姆（Ohm）。 |
| `SENSOR_CHAN_ROTATION` | 角位移（Angular Rotation），单位为度。 |
| `SENSOR_CHAN_POS_DX` | X 轴位置变化（Position Change），单位为点（Points）。 |
| `SENSOR_CHAN_POS_DY` | Y 轴位置变化（Position Change），单位为点（Points）。 |
| `SENSOR_CHAN_POS_DZ` | Z 轴位置变化（Position Change），单位为点（Points）。 |
| `SENSOR_CHAN_POS_DXYZ` | X、Y、Z 轴位置变化（Position Change），单位为点（Points）。 |
| `SENSOR_CHAN_RPM` | 每分钟转数（Revolutions per Minute），单位为 RPM。 |
| `SENSOR_CHAN_FREQUENCY` | 频率（Frequency），单位为 Hz。 |
| `SENSOR_CHAN_GAUGE_VOLTAGE` | 电压（Voltage），单位为伏特。 |
| `SENSOR_CHAN_GAUGE_AVG_CURRENT` | 平均电流（Average Current），单位为安培；负值表示放电。 |
| `SENSOR_CHAN_GAUGE_STDBY_CURRENT` | 待机电流（Standby Current），单位为安培；负值表示放电。 |
| `SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT` | 最大负载电流（Max Load Current），单位为安培；负值表示放电。 |
| `SENSOR_CHAN_GAUGE_TEMP` | 电量计温度（Gauge Temperature）。 |
| `SENSOR_CHAN_GAUGE_STATE_OF_CHARGE` | 荷电状态测量值（State of Charge），单位为 %。 |
| `SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY` | 满充容量（Full Charge Capacity），单位为 mAh。 |
| `SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY` | 剩余电荷容量（Remaining Charge Capacity），单位为 mAh。 |
| `SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY` | 标称可用容量（Nominal Available Capacity），单位为 mAh。 |
| `SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY` | 全部可用容量（Full Available Capacity），单位为 mAh。 |
| `SENSOR_CHAN_GAUGE_AVG_POWER` | 平均功率（Average Power），单位为 mW。 |
| `SENSOR_CHAN_GAUGE_STATE_OF_HEALTH` | 健康状态测量值（State of Health），单位为 %。 |
| `SENSOR_CHAN_GAUGE_TIME_TO_EMPTY` | 到放空所需的时间（Time to Empty），单位为分钟。 |
| `SENSOR_CHAN_GAUGE_TIME_TO_FULL` | 到充满所需的时间（Time to Full），单位为分钟。 |
| `SENSOR_CHAN_GAUGE_CYCLE_COUNT` | 循环计数（Cycle Count），即充放电循环的总次数。 |
| `SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE` | 电芯设计电压（Design Voltage），即最大电压，单位为 V。 |
| `SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE` | 电芯期望电压（Desired Voltage），即标称电压，单位为 V。 |
| `SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT` | 期望充电电流（Desired Charging Current），单位为 mA。 |
| `SENSOR_CHAN_GAME_ROTATION_VECTOR` | 游戏旋转向量（Game Rotation Vector），采用单位四元数的 X/Y/Z/W 分量。 |
| `SENSOR_CHAN_GRAVITY_VECTOR` | 重力向量（Gravity Vector），X/Y/Z 分量单位为 m/s^2。 |
| `SENSOR_CHAN_GBIAS_XYZ` | 陀螺仪偏置（Gyroscope Bias），X/Y/Z 分量单位为 rad/s。 |
| `SENSOR_CHAN_ENCODER_COUNT` | 正交解码器原始计数（Raw Quadrature Decoder Count），单位为计数值（Counts）。 |
| `SENSOR_CHAN_ENCODER_REVOLUTIONS` | 正交解码器转数（Number of Revolutions）。 |
| `SENSOR_CHAN_ALL` | 全部声道（All Channels）。 |
| `SENSOR_CHAN_COMMON_COUNT` | 全部通用传感器通道（Common Sensor Channels）的数量。 |
| `SENSOR_CHAN_PRIV_START` | 此值及更高值由具体传感器定义（Sensor Specific）。参见传感器头文件。 |
| `SENSOR_CHAN_MAX` | 表示传感器通道类型（Sensor Channel Type）的最大值。 |

<a id="ga8613a20521a37d40fd7371dc63ba2dac"></a>

### `sensor_stream_data_opt`

```c
enum sensor_stream_data_opt
```

```c
#include <zephyr/drivers/sensor.h>
```

触发器被消费（Trigger Consumed）时，关联数据的处理方式选项（Data Handling Options）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_STREAM_DATA_INCLUDE` | 包含与触发器关联的所有数据（Trigger Data）。 |
| `SENSOR_STREAM_DATA_NOP` | 不处理关联的触发器数据（Trigger Data）；这些数据可以稍后使用。 |
| `SENSOR_STREAM_DATA_DROP` | 冲刷／清除（Flush/Clear）与触发器关联的所有数据。 |

<a id="ga08215279400e8c9eb05ce4e4f0898ffd"></a>

### `sensor_trigger_type`

```c
enum sensor_trigger_type
```

```c
#include <zephyr/drivers/sensor.h>
```

传感器触发器类型（Sensor Trigger Types）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_TRIG_TIMER` | 基于定时器的触发器（Timer-based Trigger），适用于传感器没有中断线的情况。 |
| `SENSOR_TRIG_DATA_READY` | 每当新数据就绪（Data Ready）时触发。 |
| `SENSOR_TRIG_DELTA` | 所选通道出现显著变化时触发。对于加速度或陀螺仪通道，这包括任意运动检测（Any-motion Detection）。如果检测依据是相邻两次通道读数之间的斜率，则通过 `SENSOR_ATTR_SLOPE_TH` 和 `SENSOR_ATTR_SLOPE_DUR` 属性配置斜率阈值。 |
| `SENSOR_TRIG_NEAR_FAR` | 检测到近／远事件（Near/Far Event）时触发。 |
| `SENSOR_TRIG_THRESHOLD` | 通道读数跨越已配置阈值时触发。通过 `SENSOR_ATTR_LOWER_THRESH`、`SENSOR_ATTR_UPPER_THRESH` 和 `SENSOR_ATTR_HYSTERESIS` 属性配置阈值（Thresholds）。 |
| `SENSOR_TRIG_TAP` | 检测到单击（Single Tap）时触发。 |
| `SENSOR_TRIG_DOUBLE_TAP` | 检测到双击（Double Tap）时触发。 |
| `SENSOR_TRIG_FREEFALL` | 检测到自由落体（Free Fall）时触发。 |
| `SENSOR_TRIG_MOTION` | 检测到运动（Motion）时触发。 |
| `SENSOR_TRIG_STATIONARY` | 一段时间内未检测到运动（No Motion）时触发。 |
| `SENSOR_TRIG_FIFO_WATERMARK` | 达到先进先出队列水位线（FIFO Watermark）时触发。 |
| `SENSOR_TRIG_FIFO_FULL` | 先进先出队列（FIFO）变满时触发。 |
| `SENSOR_TRIG_TILT` | 检测到倾斜（Tilt）时触发。 |
| `SENSOR_TRIG_OVERFLOW` | 数据溢出（Data Overflow）时触发。 |
| `SENSOR_TRIG_COMMON_COUNT` | 全部通用传感器触发器（Common Sensor Triggers）的数量。 |
| `SENSOR_TRIG_PRIV_START` | 此值及更高值由具体传感器定义（Sensor Specific）。参见传感器头文件。 |
| `SENSOR_TRIG_MAX` | 表示传感器触发器类型（Sensor Trigger Type）的最大值。 |

<a id="gab53418e1eb164364663d3ec3f40399a4"></a>

### `sensor_10udegrees_to_rad()`

```c
void sensor_10udegrees_to_rad ( int32_t d, struct sensor_value * rad )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将以 10 微度（10 Micro Degrees）为单位的数值转换为弧度（Radian）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 待转换的值（Value），单位为 10 微度（10 Micro Degrees）。 |
| `rad` | 指向 `sensor_value` 结构的指针，用于保存结果（Result）。 |

<a id="gaedfdfc71dce702dc1fb1c6e60ff0f73a"></a>

### `sensor_attr_get()`

```c
int sensor_attr_get ( const struct device * dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value * val )
```

```c
#include <zephyr/drivers/sensor.h>
```

获取传感器属性（Sensor Attribute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `chan` | 属性所属的通道（Channel），如果有的话。根据设备能力，某些属性只能针对设备的全部通道设置。 |
| `attr` | 要获取的属性（Attribute）。 |
| `val` | 指向属性存储位置的指针（Pointer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gafbf65226a227e9f8824908bc38e336f5"></a>

### `sensor_attr_set()`

```c
int sensor_attr_set ( const struct device * dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value * val )
```

```c
#include <zephyr/drivers/sensor.h>
```

设置传感器属性（Sensor Attribute）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `chan` | 属性所属的通道（Channel），如果有的话。根据设备能力，某些属性只能针对设备的全部通道设置。 |
| `attr` | 要设置的属性（Attribute）。 |
| `val` | 要设置的属性值（Attribute Value）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gae95715ffea5da18a9593ec2add029824"></a>

### `sensor_chan_spec_eq()`

```c
bool sensor_chan_spec_eq ( struct sensor_chan_spec chan_spec0, struct sensor_chan_spec chan_spec1 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

检查通道规格（Channel Specs）是否等价。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chan_spec0` | 第一个通道规格（Channel Specification）。 |
| `chan_spec1` | 第二个通道规格（Channel Specification）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 如果等价（Equivalent）。 |
| `false` | 如果不等价（Not Equivalent）。 |

<a id="ga9e0e6c1408d32c52267984bae7cb268d"></a>

### `sensor_channel_get()`

```c
int sensor_channel_get ( const struct device * dev, enum sensor_channel chan, struct sensor_value * val )
```

```c
#include <zephyr/drivers/sensor.h>
```

从传感器设备获取读数（Reading）。

从驱动内部数据返回指定通道的可用值。调用此函数之前，必须先调用 `sensor_sample_fetch` 或 `sensor_sample_fetch_chan` 获取样本（Sample）。如果两次调用之间未调用这两个采样函数，则保证对同一通道连续调用此函数两次会得到相同的值。

对于向量数据样本（Vectorial Data Samples），可以传入带 `_XYZ` 后缀的指定通道，在一次调用中请求全部轴。样本分别通过 `val[0]`、`val[1]`、`val[2]` 返回，顺序为 X、Y、Z。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `chan` | 要读取的通道（Channel）。 |
| `val` | 保存数值的位置（Value Storage）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga018bca56056ae2558f9e45aeb2fa5f53"></a>

### `sensor_decode()`

```c
int sensor_decode ( struct sensor_decode_context * ctx, void * out, uint16_t max_count )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

使用 `sensor_decode_context` 解码 N 帧（Frames）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in,out] ctx` | 解码使用的上下文（Decoding Context）。 |
| `[out] out` | 输出缓冲区（Output Buffer）。 |
| `[in] max_count` | 要解码的最大帧数。 |

**返回（Returns）**：返回值（Returns）：`sensor_decoder_api` 的 `decode` 函数返回的解码结果。

<a id="ga39d4b84f5d792e27b2d6d5eb6a2ccb0d"></a>

### `sensor_degrees_to_rad()`

```c
void sensor_degrees_to_rad ( int32_t d, struct sensor_value * rad )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将度（Degree）转换为弧度（Radian）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `d` | 待转换的值（Value），单位为度（Degrees）。 |
| `rad` | 指向 `sensor_value` 结构的指针，用于保存结果（Result）。 |

<a id="ga6ab9ce9c6ee2e52d197e5cb4ccd88979"></a>

### `sensor_g_to_ms2()`

```c
void sensor_g_to_ms2 ( int32_t g, struct sensor_value * ms2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将加速度从标准重力加速度倍数（Gs）转换为 m/s² 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `g` | 待转换的 G 值（G Value）。 |
| `ms2` | 指向 `sensor_value` 结构的指针，用于保存结果（Result）。 |

<a id="ga12db6fc43adce48d34c25c16fd2336a3"></a>

### `sensor_get_decoder()`

```c
int sensor_get_decoder ( const struct device * dev, const struct sensor_decoder_api ** decoder )
```

```c
#include <zephyr/drivers/sensor.h>
```

获取传感器的解码器 API（Decoder API）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | 传感器设备（Sensor Device）。 |
| `[in] decoder` | 指向解码器指针的指针；成功时设置该解码器（Decoder）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时小于 `0`。

<a id="gab797f2f578b1c9cc44f54ab5d503bbf8"></a>

### `sensor_ms2_to_g()`

```c
int32_t sensor_ms2_to_g ( const struct sensor_value * ms2)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将加速度从 m/s² 转换为标准重力加速度倍数（Gs）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ms2` | 指向 `sensor_value` 结构的指针，结构保存加速度（Acceleration），单位为 m/s^2。 |

**返回（Returns）**：返回值（Returns）：转换后的值，单位为 G。

<a id="ga9e0fb14f84dca02497ce5bff10b51ab8"></a>

### `sensor_ms2_to_mg()`

```c
int32_t sensor_ms2_to_mg ( const struct sensor_value * ms2)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将加速度从 m/s² 转换为毫重力加速度单位（milli Gs）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ms2` | 指向 `sensor_value` 结构的指针，结构保存加速度（Acceleration），单位为 m/s^2。 |

**返回（Returns）**：返回值（Returns）：转换后的值，单位为毫 G（Milli G）。

<a id="ga3db980100e634310a0a1623136048742"></a>

### `sensor_ms2_to_ug()`

```c
int32_t sensor_ms2_to_ug ( const struct sensor_value * ms2)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将加速度从 m/s² 转换为微重力加速度单位（micro Gs）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ms2` | 指向 `sensor_value` 结构的指针，结构保存加速度（Acceleration），单位为 m/s^2。 |

**返回（Returns）**：返回值（Returns）：转换后的值，单位为微 G（Micro G）。

<a id="ga2b045cdbd4d1ca37beed69970093945b"></a>

### `sensor_natively_supported_channel_size_info()`

```c
int sensor_natively_supported_channel_size_info ( struct sensor_chan_spec channel, size_t * base_size, size_t * frame_size )
```

```c
#include <zephyr/drivers/sensor.h>
```

<a id="gabb076531445e1b128d515b28c7cc9dc8"></a>

### `sensor_processing_with_callback()`

```c
void sensor_processing_with_callback ( struct rtio * ctx, sensor_processing_callback_t cb )
```

```c
#include <zephyr/drivers/sensor.h>
```

用于传感器数据通用处理（Common Processing）的辅助函数。

此函数可在 `sensor_read()` 之后以阻塞方式调用，也可在专门处理数据的独立线程中调用。它会等待实时 I/O（RTIO）上下文中的完成队列条目（CQE）；收到后解析用户数据（Userdata），并调用 `cb`。`cb` 返回后，如果 `ctx` 提供内存池（Mempool），缓冲区会被释放回该内存池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ctx` | 要等待的 RTIO 上下文（Context）。 |
| `[in] cb` | 数据准备好处理时调用的回调（Callback）。 |

<a id="gad80093a6cfe95428dd0ead85547838a6"></a>

### `sensor_rad_to_10udegrees()`

```c
int32_t sensor_rad_to_10udegrees ( const struct sensor_value * rad)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将弧度（Radian）转换为以 10 微度（10 Micro Degrees）为单位的数值的辅助函数。

以 1 微度（Micro Degree）为单位时，`int32_t` 可表示的范围为 ±2147.483 度。为扩大范围，此处采用 10 微度为单位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rad` | 指向 `sensor_value` 结构的指针，其中保存的值以弧度（Radians）为单位。 |

**返回（Returns）**：返回值（Returns）：转换后的值，单位为 10 微度（10 Micro Degrees）。

<a id="ga040a907c8934baab66d27b8dfb1ea220"></a>

### `sensor_rad_to_degrees()`

```c
int32_t sensor_rad_to_degrees ( const struct sensor_value * rad)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将弧度（Radian）转换为度（Degree）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rad` | 指向 `sensor_value` 结构的指针，其中保存的值以弧度（Radians）为单位。 |

**返回（Returns）**：返回值（Returns）：转换后的值，单位为度（Degrees）。

<a id="gace7f20e29b302e607ba274fe40a2c2bd"></a>

### `sensor_read()`

```c
int sensor_read ( const struct rtio_iodev * iodev, struct rtio * ctx, uint8_t * buf, size_t buf_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

以阻塞方式（Blocking）从传感器单次读取样本到缓冲区。

通过 `iodev`，使用所提供的 RTIO 上下文 `ctx` 从设备读取数据。此调用生成一个 `rtio_sqe`，并将提供的缓冲区交给它。调用会等待读取完成，再返回调用方。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] iodev` | 由 `SENSOR_DT_READ_IODEV` 创建的 `iodev`。 |
| `[in] ctx` | 负责处理读取操作的 RTIO 上下文（Context）。 |
| `[in] buf` | 指向内存的指针，用于接收读取的样本数据（Sample Data）。 |
| `[in] buf_len` | 所提供内存中可用于接收读取数据的有效大小（Size），单位为字节。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时小于 `0`。

<a id="gaf53b015c47acab3c3acb4cb1d8ab827d"></a>

### `sensor_read_async_mempool()`

```c
int sensor_read_async_mempool ( const struct rtio_iodev * iodev, struct rtio * ctx, void * userdata )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

使用从缓冲池（Pool）分配的缓冲区，进行单次非阻塞读取（Non-blocking Read）。

通过 `iodev`，使用所提供的 RTIO 上下文 `ctx` 从设备读取一次数据快照（Snapshot）。此调用生成一个 `rtio_sqe`；实际处理读取操作时，该条目使用 RTIO 内部内存池（Mempool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] iodev` | 由 `SENSOR_DT_READ_IODEV` 创建的 `iodev`。 |
| `[in] ctx` | 负责处理读取操作的 RTIO 上下文（Context）。 |
| `[in] userdata` | 可选的用户数据（Userdata），在读取完成时可用。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时小于 `0`。

<a id="ga759d6581b83751bab5e56b9f8bb1676d"></a>

### `sensor_reconfigure_read_iodev()`

```c
int sensor_reconfigure_read_iodev ( const struct rtio_iodev * iodev, const struct device * sensor, const struct sensor_chan_spec * channels, size_t num_channels )
```

```c
#include <zephyr/drivers/sensor.h>
```

重新配置读取用输入／输出设备（Reading I/O Device，`iodev`）。

允许重新配置用于从传感器读取样本的 `iodev`（Reconfiguration）。

重要提示（Important）：如果 `iodev` 当前正在处理读取操作，数据很可能无效。配置变更后，务必先冲刷（Flush）或等待全部待处理操作完成，再使用数据。

还需确保 `iodev` 的 `data` 字段为 `sensor_read_config`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] iodev` | 要重新配置的 `iodev`。 |
| `[in] sensor` | 要读取的传感器（Sensor）。 |
| `[in] channels` | 要读取的一个或多个通道（Channels）。 |
| `[in] num_channels` | `channels` 中的通道数量（Number of Channels）。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，出错时小于 `0`。

<a id="gaa75e25d93ee7cac0bf38399f3c006dff"></a>

### `sensor_sample_fetch()`

```c
int sensor_sample_fetch ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor.h>
```

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

读取传感器的全部活动通道（Active Channels），必要时执行使数值可用所需的额外操作。随后，用户可以调用 `sensor_channel_get` 获取各通道的值。

此函数阻塞（Block），直到采样获取操作完成。

此函数会与传感器设备通信；如果设备通过 I2C 或 SPI 连接，在中断服务程序（ISR）中调用是不安全的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gac16192826432438a15274cf28d66e8a6"></a>

### `sensor_sample_fetch_chan()`

```c
int sensor_sample_fetch_chan ( const struct device * dev, enum sensor_channel type )
```

```c
#include <zephyr/drivers/sensor.h>
```

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

读取某一类传感器数据，例如磁力计（Magnetometer）、加速度计（Accelerometer）等，并计算补偿。随后，用户可以调用 `sensor_channel_get` 获取各通道的值。

此接口主要由多功能设备（Multi-function Devices）实现，以支持按不同采样率读取。

此函数阻塞（Block），直到采样获取操作完成。

此函数会与传感器设备通信；如果设备通过 I2C 或 SPI 连接，在中断服务程序（ISR）中调用是不安全的。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `type` | 需要更新的通道（Channel）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga58bb95758fc4bd2927c93671727e6080"></a>

### `sensor_stream()`

```c
int sensor_stream ( const struct rtio_iodev * iodev, struct rtio * ctx, void * userdata, rtio_sqe_handle_t * handle )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="ga7c72aca732e0641612d2f9437c2e41b7"></a>

### `sensor_trigger_set()`

```c
int sensor_trigger_set ( const struct device * dev, const struct sensor_trigger * trig, sensor_trigger_handler_t handler )
```

声明属性：`inline`、`static`、`supervisor`。

```c
#include <zephyr/drivers/sensor.h>
```

激活传感器触发器（Sensor Trigger），并设置触发器处理程序（Trigger Handler）。

处理函数（Handler）在线程中调用，因此执行 I2C 或 SPI 操作是安全的。但线程栈空间有限，由驱动定义。目前由调用方负责确保处理函数不会导致栈溢出（Stack Overflow）。

驱动以指针形式保存用户分配的触发器（Trigger），不会复制对象，并将该指针传回处理函数。当触发器嵌入较大结构时，处理函数可使用 `CONTAINER_OF` 获取上下文指针；这也要求触发器不能分配在线程栈上。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |
| `trig` | 要激活的触发器（Trigger）。 |
| `handler` | 触发器触发时应调用的函数（Handler）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga28a1c6cf74a391712a4697792f759d62"></a>

### `sensor_ug_to_ms2()`

```c
void sensor_ug_to_ms2 ( int32_t ug, struct sensor_value * ms2 )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将加速度从微重力加速度单位（micro Gs）转换为 m/s² 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ug` | 待转换的微 G 值（Micro G Value）。 |
| `ms2` | 指向 `sensor_value` 结构的指针，用于保存结果（Result）。 |

<a id="gabf3b46a1e88e65575e25acc1a43aba10"></a>

### `sensor_value_add()`

```c
int sensor_value_add ( struct sensor_value * inp1, struct sensor_value * inp2, struct sensor_value * out )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将两个 `struct sensor_value` 相加的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inp1` | 第一个加数（First Addend）。 |
| `inp2` | 第二个加数（Second Addend）。 |
| `out` | 所得的和（Resulting Sum）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gaf01bbb251ad0c7f6c55c5b702e8a4048"></a>

### `sensor_value_from_double()`

```c
int sensor_value_from_double ( struct sensor_value * val, double inp )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将双精度浮点数（`double`）转换为 `struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `inp` | 转换后的值（Converted Value）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga767c7d0147699c556a2f4d429501ff99"></a>

### `sensor_value_from_fixed_point()`

```c
int sensor_value_from_fixed_point ( struct sensor_value * val, uint32_t inp, uint8_t m, uint8_t n, bool is_signed )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将定点数（Fixed-point）转换为 `struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `inp` | Qm.n 格式的定点数（Fixed-point Value）。 |
| `m` | 整数位数量（Number of Integer Bits）。 |
| `n` | 小数位数量（Number of Fractional Bits）。 |
| `is_signed` | 指示定点数（Fixed-point Value）为有符号还是无符号。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga64d5a1725eda200c80daf42b1067c46c"></a>

### `sensor_value_from_float()`

```c
int sensor_value_from_float ( struct sensor_value * val, float inp )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将单精度浮点数（`float`）转换为 `struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `inp` | 转换后的值（Converted Value）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gabff019c63c89cbc546c0981819040c99"></a>

### `sensor_value_from_micro()`

```c
int sensor_value_from_micro ( struct sensor_value * val, int64_t micro )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将以百万分之一单位（Micro Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `micro` | 转换后的值（Converted Value）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga88b2605526e37420db871f066c5053b3"></a>

### `sensor_value_from_milli()`

```c
int sensor_value_from_milli ( struct sensor_value * val, int64_t milli )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将以千分之一单位（Milli Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `milli` | 转换后的值（Converted Value）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gacdb8dc2095e6a15db0a58233cab8ffe2"></a>

### `sensor_value_multiply()`

```c
int sensor_value_multiply ( struct sensor_value * inp1, struct sensor_value * inp2, struct sensor_value * out )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将两个 `struct sensor_value` 相乘的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inp1` | 第一个因数（First Factor）。 |
| `inp2` | 第二个因数（Second Factor）。 |
| `out` | 所得的积（Resulting Product）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga8d6f33eeda04bdb648bd03a92e981b1d"></a>

### `sensor_value_scale()`

```c
int sensor_value_scale ( struct sensor_value * inp, int32_t scalar, struct sensor_value * out )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

缩放（Scale）`struct sensor_value` 的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inp` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `scalar` | 整数标量（Integer Scalar）。 |
| `out` | 缩放后的输出（Scaled Output）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gac17a55d53ccd2a2e8b45109e984cc80b"></a>

### `sensor_value_subtract()`

```c
int sensor_value_subtract ( struct sensor_value * inp1, struct sensor_value * inp2, struct sensor_value * out )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将两个 `struct sensor_value` 相减的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inp1` | 被减数（Minuend）。 |
| `inp2` | 减数（Subtrahend）。 |
| `out` | 所得的差（Resulting Difference）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gae812fb481bfe3a8053f0fc23f8617434"></a>

### `sensor_value_to_centi()`

```c
int64_t sensor_value_to_centi ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为以百分之一单位（Centi Units）计数的整数的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。

<a id="gabbcb8ad4b9484cba77ae65e2d3ba7457"></a>

### `sensor_value_to_deci()`

```c
int64_t sensor_value_to_deci ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为以十分之一单位（Deci Units）计数的整数的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。

<a id="ga29223b754dc436ab1e97ce6209a3ea06"></a>

### `sensor_value_to_double()`

```c
double sensor_value_to_double ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为双精度浮点数（`double`）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。

<a id="gab4c95b7857294a9148afe6e9bcb5eacf"></a>

### `sensor_value_to_fixed_point()`

```c
int sensor_value_to_fixed_point ( uint32_t * val, struct sensor_value * inp, uint8_t m, uint8_t n, bool is_signed )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为定点数（Fixed-point）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 Qm.n 格式定点数（Fixed-point Value）的指针。 |
| `inp` | 指向 `sensor_value` 结构的指针（Pointer）。 |
| `m` | 整数位数量（Number of Integer Bits）。 |
| `n` | 小数位数量（Number of Fractional Bits）。 |
| `is_signed` | 指示定点数（Fixed-point Value）为有符号还是无符号。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga2ad1fc2abd1c8c38e7de6e99fa5c1f20"></a>

### `sensor_value_to_float()`

```c
float sensor_value_to_float ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为单精度浮点数（`float`）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。

<a id="ga9bf7faf60aa54a7540e9b73a61864e25"></a>

### `sensor_value_to_micro()`

```c
int64_t sensor_value_to_micro ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为以百万分之一单位（Micro Units）计数的整数的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。

<a id="ga6d69a9644e08a9cd7773645fa11293e3"></a>

### `sensor_value_to_milli()`

```c
int64_t sensor_value_to_milli ( const struct sensor_value * val)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor.h>
```

将 `struct sensor_value` 转换为以千分之一单位（Milli Units）计数的整数的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `val` | 指向 `sensor_value` 结构的指针（Pointer）。 |

**返回（Returns）**：返回值（Returns）：转换后的值。


## 3.9\_原页交叉引用（Cross References）

- [电池 API（Battery APIs）](../api_service_topic_reference/P001_电池 API（Battery APIs）.md)
- [设备专用传感器 API 扩展和设备树常量。](../api_topic_reference/P061_设备专用传感器 API 扩展和设备树常量。.md)
- [传感器驱动后端 API](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md)
- [传感器仿真器后端 API](../hardware/P494_传感器仿真后端接口.md)
- [sensor.h](../api_file_media_sensor_reference/P007_zephyr__drivers__sensor.h_文件参考.md)
- [tcs34725.h](../api_file_network_device_reference/P041_zephyr__drivers__sensor__tcs34725.h_文件参考.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)
- [sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)
- [sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)
- [sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)
- [sensor_stream_trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md)
- [sensor_read_config](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md)
- [sensor_data_generic_header](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)
- [SYS_INIT()](../device_reference/P005_系统初始化接口.md#gaf507cc0613add8113c41896bd631254f)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_ALIAS](../dt_identity_reference/P001_设备树节点标识宏.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)
- [k_msleep](../thread_core_reference/P001_线程公共接口.md#gac1f1470dec2e89b4cb8fd8c5433bd101)
- [rtio_sqe_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga9e04f43dc23a142ce3ec18e8b8552d69)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015"></a>
<a id="agroup__device__model_html_gac49e26fbe91a14307d5ea08d41561dd1"></a>
<a id="astructpm__device_html"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__sensor__interface_html_gaa67ca630e3931a0c3821ba438c86690c"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="astructsensor__chan__spec_html"></a>
<a id="astructsensor__read__config_html"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__sensor__interface_html_ga0cc1ee28114557e9e00257071c7dfa9f"></a>
<a id="agroup__sensor__interface_html_gaf53b015c47acab3c3acb4cb1d8ab827d"></a>
<a id="astructrtio_html"></a>
<a id="astructsensor__stream__trigger_html"></a>
<a id="agroup__devicetree-generic-id_html_gaa49e19bbc39dc0d6f16b78a5d02482c9"></a>
<a id="agroup__rtio_html_ga7ff7d0337e43b0a9380bb94a4a143a47"></a>
<a id="agroup__rtio_html_ga9e04f43dc23a142ce3ec18e8b8552d69"></a>
<a id="agroup__sensor__interface_html_ga35211c4d908a26f98b1f8d925a9b1374"></a>
<a id="agroup__sensor__interface_html_ga58bb95758fc4bd2927c93671727e6080"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c"></a>
<a id="agroup__sensor__interface_html_gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4"></a>
<a id="agroup__sensor__interface_html_gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315"></a>
<a id="agroup__sensor__interface_html_gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d"></a>
<a id="agroup__thread__apis_html_gac1f1470dec2e89b4cb8fd8c5433bd101"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1"></a>
<a id="gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315"></a>
<a id="gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d"></a>
<a id="gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921"></a>
<a id="gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_网络接口抽象层（Network Interface abstraction layer）.md) · [返回大纲](大纲.md)
