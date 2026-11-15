---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-7
title: zephyr__drivers__sensor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_sensor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器（Sensor）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stdlib.h>
#include <zephyr/device.h>
#include <zephyr/drivers/sensor_data_types.h>
#include <zephyr/dsp/types.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/sys/util.h>
#include <zephyr/types.h>
#include <zephyr/syscalls/sensor.h>
```

查看此文件的源码。

传感器（Sensor）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

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

<a id="r_sensor_5Fdriver_5Fapi"></a>

```c
struct sensor_driver_api
```

相关声明：[sensor_driver_api](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md)。

驱动操作（Driver Operations）：传感器（Sensor）驱动操作。

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

## 7.2\_宏定义（Macros）

<a id="r_ga32f679a4004b5707b2de00eb580d0930"></a>

```c
#define SENSOR_CHANNEL_3_AXIS(chan)
```

相关声明：[SENSOR_CHANNEL_3_AXIS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga32f679a4004b5707b2de00eb580d0930)。

检查给定通道是否为三轴通道（3-axis Channel）。

<a id="r_ga8bec69db645c9f4d58b396f4d025d0d8"></a>

```c
#define SENSOR_CHANNEL_IS_ACCEL(chan)
```

相关声明：[SENSOR_CHANNEL_IS_ACCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8bec69db645c9f4d58b396f4d025d0d8)。

检查给定通道是否为加速度计通道（Accelerometer）。

<a id="r_gafac19bf89f1cca6f9a208676588184ae"></a>

```c
#define SENSOR_CHANNEL_IS_GYRO(chan)
```

相关声明：[SENSOR_CHANNEL_IS_GYRO](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafac19bf89f1cca6f9a208676588184ae)。

检查给定通道是否为陀螺仪通道（Gyroscope）。

<a id="r_gae69ec503df53d2d5ee417e481f9ac9ea"></a>

```c
#define SENSOR_DECODE_CONTEXT_INIT(decoder_, buffer_, channel_type_, channel_index_)
```

相关声明：[SENSOR_DECODE_CONTEXT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae69ec503df53d2d5ee417e481f9ac9ea)。

初始化 `sensor_decode_context`。

<a id="r_ga9b7b0db322121d220b126d2b5bb7eb73"></a>

```c
#define SENSOR_STREAM_TRIGGER_PREP(_trigger, _opt)
```

相关声明：[SENSOR_STREAM_TRIGGER_PREP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9b7b0db322121d220b126d2b5bb7eb73)。

<a id="r_ga0cc1ee28114557e9e00257071c7dfa9f"></a>

```c
#define SENSOR_DT_READ_IODEV(name, dt_node, ...)
```

相关声明：[SENSOR_DT_READ_IODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0cc1ee28114557e9e00257071c7dfa9f)。

定义传感器读取实例（Sensor Reading Instance）。

<a id="r_ga35211c4d908a26f98b1f8d925a9b1374"></a>

```c
#define SENSOR_DT_STREAM_IODEV(name, dt_node, ...)
```

相关声明：[SENSOR_DT_STREAM_IODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga35211c4d908a26f98b1f8d925a9b1374)。

定义传感器流实例（Sensor Stream Instance）。

<a id="r_ga0066e049c4f084305ca2b978e5c7454d"></a>

```c
#define SENSOR_G 9806650LL
```

相关声明：[SENSOR_G](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0066e049c4f084305ca2b978e5c7454d)。

重力加速度常量（Gravitational Constant）的值，以微米每二次方秒（micro m/s²）表示。

<a id="r_ga6ebdc2f6942334de3cc248a53db7df33"></a>

```c
#define SENSOR_PI 3141592LL
```

相关声明：[SENSOR_PI](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ebdc2f6942334de3cc248a53db7df33)。

常量 π（PI）的值，以百万分之一（Micros）为单位表示。

<a id="r_ga7467206da76c3704d2e491d1b1c0973a"></a>

```c
#define SENSOR_INFO_DEFINE(name, ...)
```

相关声明：[SENSOR_INFO_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7467206da76c3704d2e491d1b1c0973a)。

<a id="r_ga9e6acbc580e9223bfb86ee8919cdc778"></a>

```c
#define SENSOR_INFO_DT_DEFINE(node_id)
```

相关声明：[SENSOR_INFO_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e6acbc580e9223bfb86ee8919cdc778)。

<a id="r_gaa67ca630e3931a0c3821ba438c86690c"></a>

```c
#define SENSOR_DEVICE_DT_DEFINE(node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SENSOR_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa67ca630e3931a0c3821ba438c86690c)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

与 `DEVICE_DT_DEFINE()` 类似，但包含传感器专用内容（Sensor Specifics）。

<a id="r_ga284dc3b9018f14161dc0a2b6bed9a37e"></a>

```c
#define SENSOR_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[SENSOR_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga284dc3b9018f14161dc0a2b6bed9a37e)。

针对兼容标识符为 `DT_DRV_COMPAT` 的实例，提供与 `SENSOR_DEVICE_DT_DEFINE()` 类似的功能。

<a id="r_a8d3434eb5860c2f2e6fe36b4de920c8c"></a>

```c
#define SENSOR_DECODER_NAME()
```

相关声明：[SENSOR_DECODER_NAME](#a8d3434eb5860c2f2e6fe36b4de920c8c)。

获取当前驱动的解码器名称（Decoder Name）。

<a id="r_a82da2432981c593ed638a21c51fb0873"></a>

```c
#define SENSOR_DECODER_DT_GET(node_id)
```

相关声明：[SENSOR_DECODER_DT_GET](#a82da2432981c593ed638a21c51fb0873)。

静态获取给定节点的解码器（Decoder）。

<a id="r_a78ad4b76be4a6f5347ba82b7db43b7c2"></a>

```c
#define SENSOR_DECODER_API_DT_DEFINE()
```

相关声明：[SENSOR_DECODER_API_DT_DEFINE](#a78ad4b76be4a6f5347ba82b7db43b7c2)。

定义解码器 API（Decoder API）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_ga890c1fb6d6974aea22a2d08829a75902"></a>

```c
typedef void(* sensor_trigger_handler_t) (const struct device *dev, const struct sensor_trigger *trigger)
```

相关声明：[sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)。

触发器触发时的回调 API（Callback API upon Trigger Firing）。

<a id="r_ga38422ace4194a66a9a912a8ef1e088fb"></a>

```c
typedef int(* sensor_attr_set_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value *val)
```

相关声明：[sensor_attr_set_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga38422ace4194a66a9a912a8ef1e088fb)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

设置传感器属性（Sensor Attribute）的回调 API。

<a id="r_ga00d05c82b46e56dca5f6e8f7f01c31b8"></a>

```c
typedef int(* sensor_attr_get_t) (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value *val)
```

相关声明：[sensor_attr_get_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

获取传感器属性（Sensor Attribute）的回调 API。

<a id="r_gad7f7a3d9e714cc16f23656ca06592aa4"></a>

```c
typedef int(* sensor_trigger_set_t) (const struct device *dev, const struct sensor_trigger *trig, sensor_trigger_handler_t handler)
```

相关声明：[sensor_trigger_set_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gad7f7a3d9e714cc16f23656ca06592aa4)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)、[sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)。

设置传感器触发器与处理程序（Sensor Trigger and Handler）的回调 API。

<a id="r_gacae110a4edb6f29dfb457cb1ea8d68c1"></a>

```c
typedef int(* sensor_sample_fetch_t) (const struct device *dev, enum sensor_channel chan)
```

相关声明：[sensor_sample_fetch_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gacae110a4edb6f29dfb457cb1ea8d68c1)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)。

将传感器样本获取到驱动缓冲区（Driver Buffer）的回调 API。

<a id="r_ga5c9b5ed9097464562004b446856043fd"></a>

```c
typedef int(* sensor_channel_get_t) (const struct device *dev, enum sensor_channel chan, struct sensor_value *val)
```

相关声明：[sensor_channel_get_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga5c9b5ed9097464562004b446856043fd)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从驱动缓冲区（Driver Buffer）读取传感器通道（Sensor Channel）的回调 API。

<a id="r_ga21e407d552d140cfb6bfd0d9513c7d42"></a>

```c
typedef int(* sensor_get_decoder_t) (const struct device *dev, const struct sensor_decoder_api **api)
```

相关声明：[sensor_get_decoder_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga21e407d552d140cfb6bfd0d9513c7d42)、[device](../device_reference/P002_设备对象结构.md)、[sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)。

获取传感器解码器实现（Sensor Decoder Implementation）的回调 API。

<a id="r_gad77732c8f0ec5520cdd71c2829787981"></a>

```c
typedef void(* sensor_submit_t) (const struct device *sensor, struct rtio_iodev_sqe *sqe)
```

相关声明：[sensor_submit_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gad77732c8f0ec5520cdd71c2829787981)、[device](../device_reference/P002_设备对象结构.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

处理传感器设备 RTIO 提交（Submission）的回调 API。

<a id="r_gaa8cd6e4fadb5d69e59d101733b4fb462"></a>

```c
typedef void(* sensor_processing_callback_t) (int result, uint8_t *buf, uint32_t buf_len, void *userdata)
```

相关声明：[sensor_processing_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa8cd6e4fadb5d69e59d101733b4fb462)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

与辅助处理函数（Helper Processing Function）配合使用的回调函数（Callback Function）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.4\_枚举（Enumerations）

<a id="r_gaaa1b502bc029b10d7b23b0a25ef4e934"></a>

```c
enum sensor_channel { SENSOR_CHAN_ACCEL_X , SENSOR_CHAN_ACCEL_Y , SENSOR_CHAN_ACCEL_Z , SENSOR_CHAN_ACCEL_XYZ , SENSOR_CHAN_GYRO_X , SENSOR_CHAN_GYRO_Y , SENSOR_CHAN_GYRO_Z , SENSOR_CHAN_GYRO_XYZ , SENSOR_CHAN_MAGN_X , SENSOR_CHAN_MAGN_Y , SENSOR_CHAN_MAGN_Z , SENSOR_CHAN_MAGN_XYZ , SENSOR_CHAN_DIE_TEMP , SENSOR_CHAN_AMBIENT_TEMP , SENSOR_CHAN_PRESS , SENSOR_CHAN_PROX , SENSOR_CHAN_HUMIDITY , SENSOR_CHAN_AMBIENT_LIGHT , SENSOR_CHAN_LIGHT , SENSOR_CHAN_IR , SENSOR_CHAN_RED , SENSOR_CHAN_GREEN , SENSOR_CHAN_BLUE , SENSOR_CHAN_ALTITUDE , SENSOR_CHAN_PM_1_0_CF , SENSOR_CHAN_PM_2_5_CF , SENSOR_CHAN_PM_10_CF , SENSOR_CHAN_PM_1_0 , SENSOR_CHAN_PM_2_5 , SENSOR_CHAN_PM_10 , SENSOR_CHAN_PM_0_3_COUNT , SENSOR_CHAN_PM_0_5_COUNT , SENSOR_CHAN_PM_1_0_COUNT , SENSOR_CHAN_PM_2_5_COUNT , SENSOR_CHAN_PM_5_COUNT , SENSOR_CHAN_PM_10_COUNT , SENSOR_CHAN_DISTANCE , SENSOR_CHAN_CO2 , SENSOR_CHAN_O2 , SENSOR_CHAN_VOC , SENSOR_CHAN_GAS_RES , SENSOR_CHAN_FLOW_RATE , SENSOR_CHAN_VOLUME , SENSOR_CHAN_VOLTAGE , SENSOR_CHAN_VSHUNT , SENSOR_CHAN_CURRENT , SENSOR_CHAN_POWER , SENSOR_CHAN_RESISTANCE , SENSOR_CHAN_ROTATION , SENSOR_CHAN_POS_DX , SENSOR_CHAN_POS_DY , SENSOR_CHAN_POS_DZ , SENSOR_CHAN_POS_DXYZ , SENSOR_CHAN_RPM , SENSOR_CHAN_FREQUENCY , SENSOR_CHAN_GAUGE_VOLTAGE , SENSOR_CHAN_GAUGE_AVG_CURRENT , SENSOR_CHAN_GAUGE_STDBY_CURRENT , SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT , SENSOR_CHAN_GAUGE_TEMP , SENSOR_CHAN_GAUGE_STATE_OF_CHARGE , SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY , SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY , SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY , SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY , SENSOR_CHAN_GAUGE_AVG_POWER , SENSOR_CHAN_GAUGE_STATE_OF_HEALTH , SENSOR_CHAN_GAUGE_TIME_TO_EMPTY , SENSOR_CHAN_GAUGE_TIME_TO_FULL , SENSOR_CHAN_GAUGE_CYCLE_COUNT , SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE , SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE , SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT , SENSOR_CHAN_GAME_ROTATION_VECTOR , SENSOR_CHAN_GRAVITY_VECTOR , SENSOR_CHAN_GBIAS_XYZ , SENSOR_CHAN_ENCODER_COUNT , SENSOR_CHAN_ENCODER_REVOLUTIONS , SENSOR_CHAN_ALL , SENSOR_CHAN_COMMON_COUNT , SENSOR_CHAN_PRIV_START = SENSOR_CHAN_COMMON_COUNT , SENSOR_CHAN_MAX = INT16_MAX }
```

相关声明：[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[SENSOR_CHAN_ACCEL_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)、[SENSOR_CHAN_ACCEL_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)、[SENSOR_CHAN_ACCEL_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)、[SENSOR_CHAN_ACCEL_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)、[SENSOR_CHAN_GYRO_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)、[SENSOR_CHAN_GYRO_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)、[SENSOR_CHAN_GYRO_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)、[SENSOR_CHAN_GYRO_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)、[SENSOR_CHAN_MAGN_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)、[SENSOR_CHAN_MAGN_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)、[SENSOR_CHAN_MAGN_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)、[SENSOR_CHAN_MAGN_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)、[SENSOR_CHAN_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)、[SENSOR_CHAN_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)、[SENSOR_CHAN_PRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)、[SENSOR_CHAN_PROX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)、[SENSOR_CHAN_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)、[SENSOR_CHAN_AMBIENT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127)、[SENSOR_CHAN_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)、[SENSOR_CHAN_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)、[SENSOR_CHAN_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)、[SENSOR_CHAN_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)、[SENSOR_CHAN_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)、[SENSOR_CHAN_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)、[SENSOR_CHAN_PM_1_0_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872)、[SENSOR_CHAN_PM_2_5_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2)、[SENSOR_CHAN_PM_10_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379)、[SENSOR_CHAN_PM_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)、[SENSOR_CHAN_PM_2_5](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)、[SENSOR_CHAN_PM_10](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)、[SENSOR_CHAN_PM_0_3_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a)、[SENSOR_CHAN_PM_0_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c)、[SENSOR_CHAN_PM_1_0_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6)、[SENSOR_CHAN_PM_2_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4)、[SENSOR_CHAN_PM_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2)、[SENSOR_CHAN_PM_10_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060)、[SENSOR_CHAN_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)、[SENSOR_CHAN_CO2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)、[SENSOR_CHAN_O2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9)、[SENSOR_CHAN_VOC](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)、[SENSOR_CHAN_GAS_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)、[SENSOR_CHAN_FLOW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42)、[SENSOR_CHAN_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab)、[SENSOR_CHAN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)、[SENSOR_CHAN_VSHUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)、[SENSOR_CHAN_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)、[SENSOR_CHAN_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)、[SENSOR_CHAN_RESISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)、[SENSOR_CHAN_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)、[SENSOR_CHAN_POS_DX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)、[SENSOR_CHAN_POS_DY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)、[SENSOR_CHAN_POS_DZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)、[SENSOR_CHAN_POS_DXYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)、[SENSOR_CHAN_RPM](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)、[SENSOR_CHAN_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212)、[SENSOR_CHAN_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)、[SENSOR_CHAN_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)、[SENSOR_CHAN_GAUGE_STDBY_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)、[SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)、[SENSOR_CHAN_GAUGE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)、[SENSOR_CHAN_GAUGE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)、[SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)、[SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)、[SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)、[SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)、[SENSOR_CHAN_GAUGE_AVG_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)、[SENSOR_CHAN_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)、[SENSOR_CHAN_GAUGE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)、[SENSOR_CHAN_GAUGE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)、[SENSOR_CHAN_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)、[SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)、[SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)、[SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)、[SENSOR_CHAN_GAME_ROTATION_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)、[SENSOR_CHAN_GRAVITY_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)、[SENSOR_CHAN_GBIAS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)、[SENSOR_CHAN_ENCODER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad)、[SENSOR_CHAN_ENCODER_REVOLUTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e)、[SENSOR_CHAN_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)、[SENSOR_CHAN_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)、[SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)、[SENSOR_CHAN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)。

传感器通道（Sensor Channels）。

<a id="r_ga08215279400e8c9eb05ce4e4f0898ffd"></a>

```c
enum sensor_trigger_type { SENSOR_TRIG_TIMER , SENSOR_TRIG_DATA_READY , SENSOR_TRIG_DELTA , SENSOR_TRIG_NEAR_FAR , SENSOR_TRIG_THRESHOLD , SENSOR_TRIG_TAP , SENSOR_TRIG_DOUBLE_TAP , SENSOR_TRIG_FREEFALL , SENSOR_TRIG_MOTION , SENSOR_TRIG_STATIONARY , SENSOR_TRIG_FIFO_WATERMARK , SENSOR_TRIG_FIFO_FULL , SENSOR_TRIG_TILT , SENSOR_TRIG_OVERFLOW , SENSOR_TRIG_COMMON_COUNT , SENSOR_TRIG_PRIV_START = SENSOR_TRIG_COMMON_COUNT , SENSOR_TRIG_MAX = INT16_MAX }
```

相关声明：[sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)、[SENSOR_TRIG_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)、[SENSOR_TRIG_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)、[SENSOR_TRIG_DELTA](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)、[SENSOR_TRIG_NEAR_FAR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)、[SENSOR_TRIG_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)、[SENSOR_TRIG_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)、[SENSOR_TRIG_DOUBLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)、[SENSOR_TRIG_FREEFALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)、[SENSOR_TRIG_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)、[SENSOR_TRIG_STATIONARY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)、[SENSOR_TRIG_FIFO_WATERMARK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)、[SENSOR_TRIG_FIFO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)、[SENSOR_TRIG_TILT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf)、[SENSOR_TRIG_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409)、[SENSOR_TRIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)、[SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)、[SENSOR_TRIG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)。

传感器触发器类型（Sensor Trigger Types）。

<a id="r_ga0dcb6842bc969492bd1c9eb49708940b"></a>

```c
enum sensor_attribute { SENSOR_ATTR_SAMPLING_FREQUENCY , SENSOR_ATTR_LOWER_THRESH , SENSOR_ATTR_UPPER_THRESH , SENSOR_ATTR_SLOPE_TH , SENSOR_ATTR_SLOPE_DUR , SENSOR_ATTR_HYSTERESIS , SENSOR_ATTR_OVERSAMPLING , SENSOR_ATTR_FULL_SCALE , SENSOR_ATTR_OFFSET , SENSOR_ATTR_CALIB_TARGET , SENSOR_ATTR_CONFIGURATION , SENSOR_ATTR_CALIBRATION , SENSOR_ATTR_FEATURE_MASK , SENSOR_ATTR_ALERT , SENSOR_ATTR_FF_DUR , SENSOR_ATTR_BATCH_DURATION , SENSOR_ATTR_GAIN , SENSOR_ATTR_RESOLUTION , SENSOR_ATTR_CHIP_ID , SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_PRIV_START = SENSOR_ATTR_COMMON_COUNT , SENSOR_ATTR_MAX = INT16_MAX }
```

相关声明：[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[SENSOR_ATTR_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)、[SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)、[SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)、[SENSOR_ATTR_SLOPE_TH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)、[SENSOR_ATTR_SLOPE_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)、[SENSOR_ATTR_HYSTERESIS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)、[SENSOR_ATTR_OVERSAMPLING](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)、[SENSOR_ATTR_FULL_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)、[SENSOR_ATTR_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)、[SENSOR_ATTR_CALIB_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)、[SENSOR_ATTR_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)、[SENSOR_ATTR_CALIBRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)、[SENSOR_ATTR_FEATURE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)、[SENSOR_ATTR_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)、[SENSOR_ATTR_FF_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)、[SENSOR_ATTR_BATCH_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)、[SENSOR_ATTR_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3)、[SENSOR_ATTR_RESOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d)、[SENSOR_ATTR_CHIP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c)、[SENSOR_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)、[SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)、[SENSOR_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)。

传感器属性类型（Sensor Attribute Types）。

<a id="r_ga8613a20521a37d40fd7371dc63ba2dac"></a>

```c
enum sensor_stream_data_opt { SENSOR_STREAM_DATA_INCLUDE = 0 , SENSOR_STREAM_DATA_NOP = 1 , SENSOR_STREAM_DATA_DROP = 2 }
```

相关声明：[sensor_stream_data_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8613a20521a37d40fd7371dc63ba2dac)、[SENSOR_STREAM_DATA_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)、[SENSOR_STREAM_DATA_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)、[SENSOR_STREAM_DATA_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)。

触发器被消费（Trigger Consumed）时，关联数据的处理方式选项（Data Handling Options）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.5\_函数（Functions）

<a id="r_gae95715ffea5da18a9593ec2add029824"></a>

```c
static bool sensor_chan_spec_eq (struct sensor_chan_spec chan_spec0, struct sensor_chan_spec chan_spec1)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[sensor_chan_spec_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae95715ffea5da18a9593ec2add029824)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

检查通道规格（Channel Specs）是否等价。

<a id="r_ga018bca56056ae2558f9e45aeb2fa5f53"></a>

```c
static int sensor_decode (struct sensor_decode_context *ctx, void *out, uint16_t max_count)
```

相关声明：[sensor_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga018bca56056ae2558f9e45aeb2fa5f53)、[sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

使用 `sensor_decode_context` 解码 N 帧（Frames）。

<a id="r_ga2b045cdbd4d1ca37beed69970093945b"></a>

```c
int sensor_natively_supported_channel_size_info (struct sensor_chan_spec channel, size_t *base_size, size_t *frame_size)
```

相关声明：[sensor_natively_supported_channel_size_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2b045cdbd4d1ca37beed69970093945b)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

<a id="r_gafbf65226a227e9f8824908bc38e336f5"></a>

```c
int sensor_attr_set (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, const struct sensor_value *val)
```

相关声明：[sensor_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

设置传感器属性（Sensor Attribute）。

<a id="r_gaedfdfc71dce702dc1fb1c6e60ff0f73a"></a>

```c
int sensor_attr_get (const struct device *dev, enum sensor_channel chan, enum sensor_attribute attr, struct sensor_value *val)
```

相关声明：[sensor_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaedfdfc71dce702dc1fb1c6e60ff0f73a)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

获取传感器属性（Sensor Attribute）。

<a id="r_ga7c72aca732e0641612d2f9437c2e41b7"></a>

```c
static int sensor_trigger_set (const struct device *dev, const struct sensor_trigger *trig, sensor_trigger_handler_t handler)
```

相关声明：[sensor_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7c72aca732e0641612d2f9437c2e41b7)、[device](../device_reference/P002_设备对象结构.md)、[sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)、[sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)。

激活传感器触发器（Sensor Trigger），并设置触发器处理程序（Trigger Handler）。

<a id="r_gaa75e25d93ee7cac0bf38399f3c006dff"></a>

```c
int sensor_sample_fetch (const struct device *dev)
```

相关声明：[sensor_sample_fetch](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa75e25d93ee7cac0bf38399f3c006dff)、[device](../device_reference/P002_设备对象结构.md)。

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

<a id="r_gac16192826432438a15274cf28d66e8a6"></a>

```c
int sensor_sample_fetch_chan (const struct device *dev, enum sensor_channel type)
```

相关声明：[sensor_sample_fetch_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac16192826432438a15274cf28d66e8a6)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)。

从传感器获取样本（Sample），并存入驱动内部缓冲区（Internal Driver Buffer）。

<a id="r_ga9e0e6c1408d32c52267984bae7cb268d"></a>

```c
int sensor_channel_get (const struct device *dev, enum sensor_channel chan, struct sensor_value *val)
```

相关声明：[sensor_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)、[device](../device_reference/P002_设备对象结构.md)、[sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

从传感器设备获取读数（Reading）。

<a id="r_ga12db6fc43adce48d34c25c16fd2336a3"></a>

```c
int sensor_get_decoder (const struct device *dev, const struct sensor_decoder_api **decoder)
```

相关声明：[sensor_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga12db6fc43adce48d34c25c16fd2336a3)、[device](../device_reference/P002_设备对象结构.md)、[sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)。

获取传感器的解码器 API（Decoder API）。

<a id="r_ga759d6581b83751bab5e56b9f8bb1676d"></a>

```c
int sensor_reconfigure_read_iodev (const struct rtio_iodev *iodev, const struct device *sensor, const struct sensor_chan_spec *channels, size_t num_channels)
```

相关声明：[sensor_reconfigure_read_iodev](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga759d6581b83751bab5e56b9f8bb1676d)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[device](../device_reference/P002_设备对象结构.md)、[sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)。

重新配置读取用输入／输出设备（Reading I/O Device，`iodev`）。

<a id="r_ga58bb95758fc4bd2927c93671727e6080"></a>

```c
static int sensor_stream (const struct rtio_iodev *iodev, struct rtio *ctx, void *userdata, rtio_sqe_handle_t *handle)
```

相关声明：[sensor_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga58bb95758fc4bd2927c93671727e6080)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)。

<a id="r_gace7f20e29b302e607ba274fe40a2c2bd"></a>

```c
static int sensor_read (const struct rtio_iodev *iodev, struct rtio *ctx, uint8_t *buf, size_t buf_len)
```

相关声明：[sensor_read](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gace7f20e29b302e607ba274fe40a2c2bd)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

以阻塞方式（Blocking）从传感器单次读取样本到缓冲区。

<a id="r_gaf53b015c47acab3c3acb4cb1d8ab827d"></a>

```c
static int sensor_read_async_mempool (const struct rtio_iodev *iodev, struct rtio *ctx, void *userdata)
```

相关声明：[sensor_read_async_mempool](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf53b015c47acab3c3acb4cb1d8ab827d)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

使用从缓冲池（Pool）分配的缓冲区，进行单次非阻塞读取（Non-blocking Read）。

<a id="r_gabb076531445e1b128d515b28c7cc9dc8"></a>

```c
void sensor_processing_with_callback (struct rtio *ctx, sensor_processing_callback_t cb)
```

相关声明：[sensor_processing_with_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabb076531445e1b128d515b28c7cc9dc8)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[sensor_processing_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa8cd6e4fadb5d69e59d101733b4fb462)。

用于传感器数据通用处理（Common Processing）的辅助函数。

<a id="r_gab797f2f578b1c9cc44f54ab5d503bbf8"></a>

```c
static int32_t sensor_ms2_to_g (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_g](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab797f2f578b1c9cc44f54ab5d503bbf8)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为标准重力加速度倍数（Gs）的辅助函数。

<a id="r_ga6ab9ce9c6ee2e52d197e5cb4ccd88979"></a>

```c
static void sensor_g_to_ms2 (int32_t g, struct sensor_value *ms2)
```

相关声明：[sensor_g_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从标准重力加速度倍数（Gs）转换为 m/s² 的辅助函数。

<a id="r_ga9e0fb14f84dca02497ce5bff10b51ab8"></a>

```c
static int32_t sensor_ms2_to_mg (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0fb14f84dca02497ce5bff10b51ab8)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为毫重力加速度单位（milli Gs）的辅助函数。

<a id="r_ga3db980100e634310a0a1623136048742"></a>

```c
static int32_t sensor_ms2_to_ug (const struct sensor_value *ms2)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_ms2_to_ug](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga3db980100e634310a0a1623136048742)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从 m/s² 转换为微重力加速度单位（micro Gs）的辅助函数。

<a id="r_ga28a1c6cf74a391712a4697792f759d62"></a>

```c
static void sensor_ug_to_ms2 (int32_t ug, struct sensor_value *ms2)
```

相关声明：[sensor_ug_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga28a1c6cf74a391712a4697792f759d62)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将加速度从微重力加速度单位（micro Gs）转换为 m/s² 的辅助函数。

<a id="r_ga040a907c8934baab66d27b8dfb1ea220"></a>

```c
static int32_t sensor_rad_to_degrees (const struct sensor_value *rad)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_rad_to_degrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga040a907c8934baab66d27b8dfb1ea220)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将弧度（Radian）转换为度（Degree）的辅助函数。

<a id="r_ga39d4b84f5d792e27b2d6d5eb6a2ccb0d"></a>

```c
static void sensor_degrees_to_rad (int32_t d, struct sensor_value *rad)
```

相关声明：[sensor_degrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将度（Degree）转换为弧度（Radian）的辅助函数。

<a id="r_gad80093a6cfe95428dd0ead85547838a6"></a>

```c
static int32_t sensor_rad_to_10udegrees (const struct sensor_value *rad)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_rad_to_10udegrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gad80093a6cfe95428dd0ead85547838a6)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将弧度（Radian）转换为以 10 微度（10 Micro Degrees）为单位的数值的辅助函数。

<a id="r_gab53418e1eb164364663d3ec3f40399a4"></a>

```c
static void sensor_10udegrees_to_rad (int32_t d, struct sensor_value *rad)
```

相关声明：[sensor_10udegrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab53418e1eb164364663d3ec3f40399a4)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将以 10 微度（10 Micro Degrees）为单位的数值转换为弧度（Radian）的辅助函数。

<a id="r_ga29223b754dc436ab1e97ce6209a3ea06"></a>

```c
static double sensor_value_to_double (const struct sensor_value *val)
```

相关声明：[sensor_value_to_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga29223b754dc436ab1e97ce6209a3ea06)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为双精度浮点数（`double`）的辅助函数。

<a id="r_ga2ad1fc2abd1c8c38e7de6e99fa5c1f20"></a>

```c
static float sensor_value_to_float (const struct sensor_value *val)
```

相关声明：[sensor_value_to_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为单精度浮点数（`float`）的辅助函数。

<a id="r_gab4c95b7857294a9148afe6e9bcb5eacf"></a>

```c
static int sensor_value_to_fixed_point (uint32_t *val, struct sensor_value *inp, uint8_t m, uint8_t n, bool is_signed)
```

相关声明：[sensor_value_to_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab4c95b7857294a9148afe6e9bcb5eacf)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将 `struct sensor_value` 转换为定点数（Fixed-point）的辅助函数。

<a id="r_gaf01bbb251ad0c7f6c55c5b702e8a4048"></a>

```c
static int sensor_value_from_double (struct sensor_value *val, double inp)
```

相关声明：[sensor_value_from_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf01bbb251ad0c7f6c55c5b702e8a4048)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将双精度浮点数（`double`）转换为 `struct sensor_value` 的辅助函数。

<a id="r_ga64d5a1725eda200c80daf42b1067c46c"></a>

```c
static int sensor_value_from_float (struct sensor_value *val, float inp)
```

相关声明：[sensor_value_from_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga64d5a1725eda200c80daf42b1067c46c)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将单精度浮点数（`float`）转换为 `struct sensor_value` 的辅助函数。

<a id="r_ga767c7d0147699c556a2f4d429501ff99"></a>

```c
static int sensor_value_from_fixed_point (struct sensor_value *val, uint32_t inp, uint8_t m, uint8_t n, bool is_signed)
```

相关声明：[sensor_value_from_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga767c7d0147699c556a2f4d429501ff99)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

将定点数（Fixed-point）转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabbcb8ad4b9484cba77ae65e2d3ba7457"></a>

```c
static int64_t sensor_value_to_deci (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_deci](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabbcb8ad4b9484cba77ae65e2d3ba7457)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以十分之一单位（Deci Units）计数的整数的辅助函数。

<a id="r_gae812fb481bfe3a8053f0fc23f8617434"></a>

```c
static int64_t sensor_value_to_centi (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_centi](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae812fb481bfe3a8053f0fc23f8617434)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以百分之一单位（Centi Units）计数的整数的辅助函数。

<a id="r_ga6d69a9644e08a9cd7773645fa11293e3"></a>

```c
static int64_t sensor_value_to_milli (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6d69a9644e08a9cd7773645fa11293e3)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以千分之一单位（Milli Units）计数的整数的辅助函数。

<a id="r_ga9bf7faf60aa54a7540e9b73a61864e25"></a>

```c
static int64_t sensor_value_to_micro (const struct sensor_value *val)
```

相关声明：[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)、[sensor_value_to_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9bf7faf60aa54a7540e9b73a61864e25)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `struct sensor_value` 转换为以百万分之一单位（Micro Units）计数的整数的辅助函数。

<a id="r_ga88b2605526e37420db871f066c5053b3"></a>

```c
static int sensor_value_from_milli (struct sensor_value *val, int64_t milli)
```

相关声明：[sensor_value_from_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga88b2605526e37420db871f066c5053b3)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将以千分之一单位（Milli Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabff019c63c89cbc546c0981819040c99"></a>

```c
static int sensor_value_from_micro (struct sensor_value *val, int64_t micro)
```

相关声明：[sensor_value_from_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabff019c63c89cbc546c0981819040c99)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)。

将以百万分之一单位（Micro Units）计数的整数转换为 `struct sensor_value` 的辅助函数。

<a id="r_gabf3b46a1e88e65575e25acc1a43aba10"></a>

```c
static int sensor_value_add (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_add](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabf3b46a1e88e65575e25acc1a43aba10)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相加的辅助函数。

<a id="r_gac17a55d53ccd2a2e8b45109e984cc80b"></a>

```c
static int sensor_value_subtract (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_subtract](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac17a55d53ccd2a2e8b45109e984cc80b)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相减的辅助函数。

<a id="r_gacdb8dc2095e6a15db0a58233cab8ffe2"></a>

```c
static int sensor_value_multiply (struct sensor_value *inp1, struct sensor_value *inp2, struct sensor_value *out)
```

相关声明：[sensor_value_multiply](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gacdb8dc2095e6a15db0a58233cab8ffe2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将两个 `struct sensor_value` 相乘的辅助函数。

<a id="r_ga8d6f33eeda04bdb648bd03a92e981b1d"></a>

```c
static int sensor_value_scale (struct sensor_value *inp, int32_t scalar, struct sensor_value *out)
```

相关声明：[sensor_value_scale](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8d6f33eeda04bdb648bd03a92e981b1d)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

缩放（Scale）`struct sensor_value` 的辅助函数。

## 7.6\_详细说明（Detailed Documentation）

<a id="a78ad4b76be4a6f5347ba82b7db43b7c2"></a>

### `SENSOR_DECODER_API_DT_DEFINE`

```c
#define SENSOR_DECODER_API_DT_DEFINE ( )
```

展开值（Value）：

```c
COND_CODE_1(DT_HAS_COMPAT_STATUS_OKAY(DT_DRV_COMPAT), (), (static))                        \
const STRUCT_SECTION_ITERABLE(sensor_decoder_api, SENSOR_DECODER_NAME())
```

定义解码器 API（Decoder API）。

每个传感器兼容字符串（Compatible String）应使用本宏创建一次定义，它会创建可静态引用的解码器 API（Statically Referenceable Decoder API）。

原始示例（Example）：

```c
SENSOR_DECODER_API_DT_DEFINE() = {
  .get_frame_count = my_driver_get_frame_count,
  .get_timestamp = my_driver_get_timestamp,
  .get_shift = my_driver_get_shift,
  .decode = my_driver_decode,
};
```

<a id="a82da2432981c593ed638a21c51fb0873"></a>

### `SENSOR_DECODER_DT_GET`

```c
#define SENSOR_DECODER_DT_GET ( node_id)
```

展开值（Value）：

```c
&UTIL_CAT(DT_STRING_TOKEN_BY_IDX(node_id, compatible, 0), __decoder_api)
```

静态获取给定节点的解码器（Decoder）。

原始示例（Example）：

```c
static const sensor_decoder_api *decoder = SENSOR_DECODER_DT_GET(DT_ALIAS(accel));
```

<a id="a8d3434eb5860c2f2e6fe36b4de920c8c"></a>

### `SENSOR_DECODER_NAME`

```c
#define SENSOR_DECODER_NAME ( )
```

展开值（Value）：

```c
UTIL_CAT(DT_DRV_COMPAT, __decoder_api)
```

获取当前驱动的解码器名称（Decoder Name）。

本函数依赖已定义的 `DT_DRV_COMPAT`。


## 7.7\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sensor_data_types.h](../api_source_reference/P768_sensor_data_types.h_源码浏览.md)
- [zephyr/dsp/types.h](../api_source_reference/P364_types.h_源码浏览.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)
- [sensor_driver_api](../sensor_navigation_model_reference/P040_sensor_driver_api_结构体.md)
- [sensor_chan_spec](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md)
- [sensor_decoder_api](../sensor_navigation_model_reference/P039_sensor_decoder_api_结构体.md)
- [sensor_decode_context](../sensor_navigation_model_reference/P038_sensor_decode_context_结构体.md)
- [sensor_stream_trigger](../sensor_navigation_model_reference/P048_sensor_stream_trigger_结构体.md)
- [sensor_read_config](../sensor_navigation_model_reference/P047_sensor_read_config_结构体.md)
- [sensor_data_generic_header](../sensor_navigation_model_reference/P036_sensor_data_generic_header_结构体.md)
- [SENSOR_CHANNEL_3_AXIS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga32f679a4004b5707b2de00eb580d0930)
- [SENSOR_CHANNEL_IS_ACCEL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8bec69db645c9f4d58b396f4d025d0d8)
- [SENSOR_CHANNEL_IS_GYRO](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafac19bf89f1cca6f9a208676588184ae)
- [SENSOR_DECODE_CONTEXT_INIT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae69ec503df53d2d5ee417e481f9ac9ea)
- [SENSOR_STREAM_TRIGGER_PREP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9b7b0db322121d220b126d2b5bb7eb73)
- [SENSOR_DT_READ_IODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0cc1ee28114557e9e00257071c7dfa9f)
- [SENSOR_DT_STREAM_IODEV](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga35211c4d908a26f98b1f8d925a9b1374)
- [SENSOR_G](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0066e049c4f084305ca2b978e5c7454d)
- [SENSOR_PI](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ebdc2f6942334de3cc248a53db7df33)
- [SENSOR_INFO_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7467206da76c3704d2e491d1b1c0973a)
- [SENSOR_INFO_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e6acbc580e9223bfb86ee8919cdc778)
- [SENSOR_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa67ca630e3931a0c3821ba438c86690c)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [SENSOR_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga284dc3b9018f14161dc0a2b6bed9a37e)
- [sensor_trigger_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga890c1fb6d6974aea22a2d08829a75902)
- [device](../device_reference/P002_设备对象结构.md)
- [sensor_attr_set_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga38422ace4194a66a9a912a8ef1e088fb)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga0dcb6842bc969492bd1c9eb49708940b)
- [sensor_attr_get_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)
- [sensor_trigger_set_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gad7f7a3d9e714cc16f23656ca06592aa4)
- [sensor_sample_fetch_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gacae110a4edb6f29dfb457cb1ea8d68c1)
- [sensor_channel_get_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga5c9b5ed9097464562004b446856043fd)
- [sensor_get_decoder_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#ga21e407d552d140cfb6bfd0d9513c7d42)
- [sensor_submit_t](../api_lifecycle_capability_topic_reference/P020_传感器驱动后端 API.md#gad77732c8f0ec5520cdd71c2829787981)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [sensor_processing_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa8cd6e4fadb5d69e59d101733b4fb462)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [SENSOR_CHAN_ACCEL_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)
- [SENSOR_CHAN_ACCEL_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)
- [SENSOR_CHAN_ACCEL_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)
- [SENSOR_CHAN_ACCEL_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)
- [SENSOR_CHAN_GYRO_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)
- [SENSOR_CHAN_GYRO_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)
- [SENSOR_CHAN_GYRO_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)
- [SENSOR_CHAN_GYRO_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)
- [SENSOR_CHAN_MAGN_X](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)
- [SENSOR_CHAN_MAGN_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)
- [SENSOR_CHAN_MAGN_Z](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)
- [SENSOR_CHAN_MAGN_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)
- [SENSOR_CHAN_DIE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)
- [SENSOR_CHAN_AMBIENT_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)
- [SENSOR_CHAN_PRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)
- [SENSOR_CHAN_PROX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)
- [SENSOR_CHAN_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)
- [SENSOR_CHAN_AMBIENT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a39b13669a3006ead32275d1578677127)
- [SENSOR_CHAN_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)
- [SENSOR_CHAN_IR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)
- [SENSOR_CHAN_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)
- [SENSOR_CHAN_GREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)
- [SENSOR_CHAN_BLUE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)
- [SENSOR_CHAN_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)
- [SENSOR_CHAN_PM_1_0_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0893cbc829c2a3b896f12874cc96c872)
- [SENSOR_CHAN_PM_2_5_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4d8c9e992c590bb17291471d8634a3a2)
- [SENSOR_CHAN_PM_10_CF](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a9e45f64b48f96650f0e75c3728324379)
- [SENSOR_CHAN_PM_1_0](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)
- [SENSOR_CHAN_PM_2_5](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)
- [SENSOR_CHAN_PM_10](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)
- [SENSOR_CHAN_PM_0_3_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aadd0d7e0e77db8bd11da1866786b3a6a)
- [SENSOR_CHAN_PM_0_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3afc97258f1340ef047a055dc5a69e4c)
- [SENSOR_CHAN_PM_1_0_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aabd79bd1d8600c852260c0a8afc372e6)
- [SENSOR_CHAN_PM_2_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934adcef73d7ea6cac2e251f96ecf9fa8ea4)
- [SENSOR_CHAN_PM_5_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7746b596d101dde6afbf73f5994b5ec2)
- [SENSOR_CHAN_PM_10_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaee5947abb6490ec06d9f5984bfa4060)
- [SENSOR_CHAN_DISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)
- [SENSOR_CHAN_CO2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)
- [SENSOR_CHAN_O2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9)
- [SENSOR_CHAN_VOC](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)
- [SENSOR_CHAN_GAS_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)
- [SENSOR_CHAN_FLOW_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6d19454f164337c9cf163dc1dfaf2b42)
- [SENSOR_CHAN_VOLUME](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6dfcb28f053feeb7fca51a6c92b6c4ab)
- [SENSOR_CHAN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)
- [SENSOR_CHAN_VSHUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)
- [SENSOR_CHAN_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)
- [SENSOR_CHAN_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)
- [SENSOR_CHAN_RESISTANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)
- [SENSOR_CHAN_ROTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)
- [SENSOR_CHAN_POS_DX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)
- [SENSOR_CHAN_POS_DY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)
- [SENSOR_CHAN_POS_DZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)
- [SENSOR_CHAN_POS_DXYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)
- [SENSOR_CHAN_RPM](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)
- [SENSOR_CHAN_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212)
- [SENSOR_CHAN_GAUGE_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)
- [SENSOR_CHAN_GAUGE_AVG_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)
- [SENSOR_CHAN_GAUGE_STDBY_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)
- [SENSOR_CHAN_GAUGE_MAX_LOAD_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)
- [SENSOR_CHAN_GAUGE_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)
- [SENSOR_CHAN_GAUGE_STATE_OF_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)
- [SENSOR_CHAN_GAUGE_FULL_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)
- [SENSOR_CHAN_GAUGE_REMAINING_CHARGE_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)
- [SENSOR_CHAN_GAUGE_NOM_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)
- [SENSOR_CHAN_GAUGE_FULL_AVAIL_CAPACITY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)
- [SENSOR_CHAN_GAUGE_AVG_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)
- [SENSOR_CHAN_GAUGE_STATE_OF_HEALTH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)
- [SENSOR_CHAN_GAUGE_TIME_TO_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)
- [SENSOR_CHAN_GAUGE_TIME_TO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)
- [SENSOR_CHAN_GAUGE_CYCLE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)
- [SENSOR_CHAN_GAUGE_DESIGN_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)
- [SENSOR_CHAN_GAUGE_DESIRED_VOLTAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)
- [SENSOR_CHAN_GAUGE_DESIRED_CHARGING_CURRENT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)
- [SENSOR_CHAN_GAME_ROTATION_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)
- [SENSOR_CHAN_GRAVITY_VECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)
- [SENSOR_CHAN_GBIAS_XYZ](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)
- [SENSOR_CHAN_ENCODER_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934a486ea8968daed9d1c3802a3babcdcfad)
- [SENSOR_CHAN_ENCODER_REVOLUTIONS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934aa659bdadf3905703afe9bcf6dd0be82e)
- [SENSOR_CHAN_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)
- [SENSOR_CHAN_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)
- [sensor_trigger_type](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga08215279400e8c9eb05ce4e4f0898ffd)
- [SENSOR_TRIG_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)
- [SENSOR_TRIG_DATA_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)
- [SENSOR_TRIG_DELTA](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)
- [SENSOR_TRIG_NEAR_FAR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)
- [SENSOR_TRIG_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)
- [SENSOR_TRIG_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)
- [SENSOR_TRIG_DOUBLE_TAP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)
- [SENSOR_TRIG_FREEFALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)
- [SENSOR_TRIG_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)
- [SENSOR_TRIG_STATIONARY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)
- [SENSOR_TRIG_FIFO_WATERMARK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)
- [SENSOR_TRIG_FIFO_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)
- [SENSOR_TRIG_TILT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffdabbdff0ba5072a376190c4a1272b2c4cf)
- [SENSOR_TRIG_OVERFLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda2bc31b6e790488eb7c9031107676b409)
- [SENSOR_TRIG_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)
- [SENSOR_TRIG_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)
- [SENSOR_TRIG_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)
- [SENSOR_ATTR_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)
- [SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)
- [SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)
- [SENSOR_ATTR_SLOPE_TH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)
- [SENSOR_ATTR_SLOPE_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)
- [SENSOR_ATTR_HYSTERESIS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)
- [SENSOR_ATTR_OVERSAMPLING](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)
- [SENSOR_ATTR_FULL_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)
- [SENSOR_ATTR_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)
- [SENSOR_ATTR_CALIB_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)
- [SENSOR_ATTR_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)
- [SENSOR_ATTR_CALIBRATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)
- [SENSOR_ATTR_FEATURE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)
- [SENSOR_ATTR_ALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)
- [SENSOR_ATTR_FF_DUR](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)
- [SENSOR_ATTR_BATCH_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)
- [SENSOR_ATTR_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3)
- [SENSOR_ATTR_RESOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d)
- [SENSOR_ATTR_CHIP_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba87d853ad38f41c897bda106a7c66c08c)
- [SENSOR_ATTR_COMMON_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)
- [sensor_stream_data_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8613a20521a37d40fd7371dc63ba2dac)
- [SENSOR_STREAM_DATA_INCLUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)
- [SENSOR_STREAM_DATA_NOP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)
- [SENSOR_STREAM_DATA_DROP](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [sensor_chan_spec_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae95715ffea5da18a9593ec2add029824)
- [sensor_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga018bca56056ae2558f9e45aeb2fa5f53)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [sensor_natively_supported_channel_size_info](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2b045cdbd4d1ca37beed69970093945b)
- [sensor_attr_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)
- [sensor_attr_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaedfdfc71dce702dc1fb1c6e60ff0f73a)
- [sensor_trigger_set](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga7c72aca732e0641612d2f9437c2e41b7)
- [sensor_sample_fetch](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaa75e25d93ee7cac0bf38399f3c006dff)
- [sensor_sample_fetch_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac16192826432438a15274cf28d66e8a6)
- [sensor_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)
- [sensor_get_decoder](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga12db6fc43adce48d34c25c16fd2336a3)
- [sensor_reconfigure_read_iodev](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga759d6581b83751bab5e56b9f8bb1676d)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [sensor_stream](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga58bb95758fc4bd2927c93671727e6080)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_sqe_handle_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio.html#ga7ff7d0337e43b0a9380bb94a4a143a47)
- [sensor_read](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gace7f20e29b302e607ba274fe40a2c2bd)
- [sensor_read_async_mempool](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf53b015c47acab3c3acb4cb1d8ab827d)
- [sensor_processing_with_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabb076531445e1b128d515b28c7cc9dc8)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [sensor_ms2_to_g](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab797f2f578b1c9cc44f54ab5d503bbf8)
- [sensor_g_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)
- [sensor_ms2_to_mg](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0fb14f84dca02497ce5bff10b51ab8)
- [sensor_ms2_to_ug](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga3db980100e634310a0a1623136048742)
- [sensor_ug_to_ms2](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga28a1c6cf74a391712a4697792f759d62)
- [sensor_rad_to_degrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga040a907c8934baab66d27b8dfb1ea220)
- [sensor_degrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)
- [sensor_rad_to_10udegrees](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gad80093a6cfe95428dd0ead85547838a6)
- [sensor_10udegrees_to_rad](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab53418e1eb164364663d3ec3f40399a4)
- [sensor_value_to_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga29223b754dc436ab1e97ce6209a3ea06)
- [sensor_value_to_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)
- [sensor_value_to_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gab4c95b7857294a9148afe6e9bcb5eacf)
- [sensor_value_from_double](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaf01bbb251ad0c7f6c55c5b702e8a4048)
- [sensor_value_from_float](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga64d5a1725eda200c80daf42b1067c46c)
- [sensor_value_from_fixed_point](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga767c7d0147699c556a2f4d429501ff99)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [sensor_value_to_deci](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabbcb8ad4b9484cba77ae65e2d3ba7457)
- [sensor_value_to_centi](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gae812fb481bfe3a8053f0fc23f8617434)
- [sensor_value_to_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga6d69a9644e08a9cd7773645fa11293e3)
- [sensor_value_to_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9bf7faf60aa54a7540e9b73a61864e25)
- [sensor_value_from_milli](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga88b2605526e37420db871f066c5053b3)
- [sensor_value_from_micro](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabff019c63c89cbc546c0981819040c99)
- [sensor_value_add](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gabf3b46a1e88e65575e25acc1a43aba10)
- [sensor_value_subtract](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gac17a55d53ccd2a2e8b45109e984cc80b)
- [sensor_value_multiply](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gacdb8dc2095e6a15db0a58233cab8ffe2)
- [sensor_value_scale](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga8d6f33eeda04bdb648bd03a92e981b1d)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_HAS_COMPAT_STATUS_OKAY](../dt_identity_reference/P002_设备树存在性与状态宏.md#ga916e11b66fdaab46e93c25241b62b52a)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [DT_STRING_TOKEN_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga583e5e2e3c897f1095073e6192061d3a)
- [DT_ALIAS](../dt_identity_reference/P001_设备树节点标识宏.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_ga916e11b66fdaab46e93c25241b62b52a"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="asensor_8h_html_a8d3434eb5860c2f2e6fe36b4de920c8c"></a>
<a id="astructsensor__decoder__api_html"></a>
<a id="asensor_8h_html_a78ad4b76be4a6f5347ba82b7db43b7c2"></a>
<a id="agroup__devicetree-generic-prop_html_ga583e5e2e3c897f1095073e6192061d3a"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-generic-id_html_gaa49e19bbc39dc0d6f16b78a5d02482c9"></a>
<a id="asensor_8h_html_a82da2432981c593ed638a21c51fb0873"></a>

---

[上一章](P006_zephyr__dt-bindings__clock__rx_clock.h_文件参考.md) · [返回大纲](大纲.md)
