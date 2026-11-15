---
id: learning.zephyr-docs.api-file-network-device-reference.page-21
title: zephyr__drivers__sensor__max32664c.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max32664c_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_sensor\_\_max32664c.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max32664c_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX32664C传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/device.h>
```

查看此文件的源码。

MAX32664C传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_max32664c_5Facc_5Fdata_5Ft"></a>

```c
struct max32664c_acc_data_t
```

相关声明：[max32664c_acc_data_t](../device_power_control_model_reference/P024_max32664c_acc_data_t_结构体.md)。

外部加速度计（External Accelerometer）数据的数据结构。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="r_gac9f5586b750b0aac5a769428e05c69b5"></a>

```c
#define MAX32664C_MOTION_TIME(ms)
```

相关声明：[MAX32664C_MOTION_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gac9f5586b750b0aac5a769428e05c69b5)。

将以毫秒表示的运动时间（Motion Time）转换为 MAX32664C 传感器对应的值。

<a id="r_gac29a24ee0d12f0f78b2777e256b02014"></a>

```c
#define MAX32664C_MOTION_THRESHOLD(mg)
```

相关声明：[MAX32664C_MOTION_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gac29a24ee0d12f0f78b2777e256b02014)。

将以毫 g 表示的运动阈值（Motion Threshold，加速度）转换为 MAX32664C 传感器对应的值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.3\_枚举（Enumerations）

<a id="r_ga52fbc189e74d50bf0841c611cc89e60f"></a>

```c
enum sensor_channel_max32664c { SENSOR_CHAN_MAX32664C_HEARTRATE = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_MAX32664C_BLOOD_OXYGEN_SATURATION , SENSOR_CHAN_MAX32664C_RESPIRATION_RATE , SENSOR_CHAN_MAX32664C_SKIN_CONTACT , SENSOR_CHAN_MAX32664C_ACTIVITY , SENSOR_CHAN_MAX32664C_STEP_COUNTER }
```

相关声明：[sensor_channel_max32664c](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga52fbc189e74d50bf0841c611cc89e60f)、[SENSOR_CHAN_MAX32664C_HEARTRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa18fce0c2b90a1b3b7b6c858abc0f146d)、[SENSOR_CHAN_MAX32664C_BLOOD_OXYGEN_SATURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fab9a21912b7a4d4e0e936875cea89f79d)、[SENSOR_CHAN_MAX32664C_RESPIRATION_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa8f5236ba1d83a87dac9c3f2ba0518150)、[SENSOR_CHAN_MAX32664C_SKIN_CONTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa7e05a3690e0b931358a1fb5d4240151c)、[SENSOR_CHAN_MAX32664C_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa3637772914acf3567d835a71baac9edc)、[SENSOR_CHAN_MAX32664C_STEP_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa274ca8282e34239db11d8b33b682c893)。

<a id="r_ga49bffbe46602089606b6d51eb46b7cb6"></a>

```c
enum sensor_attribute_max32664c { SENSOR_ATTR_MAX32664C_GENDER = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_MAX32664C_AGE , SENSOR_ATTR_MAX32664C_WEIGHT , SENSOR_ATTR_MAX32664C_HEIGHT , SENSOR_ATTR_MAX32664C_OP_MODE }
```

相关声明：[sensor_attribute_max32664c](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga49bffbe46602089606b6d51eb46b7cb6)、[SENSOR_ATTR_MAX32664C_GENDER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a1660d557ec24396e9a21326f914eab0d)、[SENSOR_ATTR_MAX32664C_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a005e1b0d7b62a7ec05708852e4265671)、[SENSOR_ATTR_MAX32664C_WEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6aa8843efabd00b375383816b835aee897)、[SENSOR_ATTR_MAX32664C_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6af84b67a4771f72b7cc8b2d11544fdba7)、[SENSOR_ATTR_MAX32664C_OP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a7a0baebbf68c802a46b03ac1cb27bec3)。

<a id="r_ga906ce2770956d586a46caa8d6c6d12be"></a>

```c
enum max32664c_device_mode { MAX32664C_OP_MODE_IDLE , MAX32664C_OP_MODE_RAW , MAX32664C_OP_MODE_ALGO_AEC , MAX32664C_OP_MODE_ALGO_AEC_EXT , MAX32664C_OP_MODE_ALGO_AGC , MAX32664C_OP_MODE_ALGO_AGC_EXT , MAX32664C_OP_MODE_SCD , MAX32664C_OP_MODE_WAKE_ON_MOTION , MAX32664C_OP_MODE_EXIT_WAKE_ON_MOTION , MAX32664C_OP_MODE_STOP_ALGO }
```

相关声明：[max32664c_device_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga906ce2770956d586a46caa8d6c6d12be)、[MAX32664C_OP_MODE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beaae19d259bab6ef5004770d4f8b4626a0)、[MAX32664C_OP_MODE_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea0e762d3b97f22c46d77ac4b01f5761d1)、[MAX32664C_OP_MODE_ALGO_AEC](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beacbf561fd327a3b988e1a4090ba63219e)、[MAX32664C_OP_MODE_ALGO_AEC_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea8db7362f61662b078272c4b435e1e2b6)、[MAX32664C_OP_MODE_ALGO_AGC](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea460dba077adea0baf026428c0ad2ad0c)、[MAX32664C_OP_MODE_ALGO_AGC_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea0001a3584cf3bbe819fc8f728e57ae0e)、[MAX32664C_OP_MODE_SCD](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea14e153eb3be43d8218e4f7360e14b707)、[MAX32664C_OP_MODE_WAKE_ON_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea87d0d5c0dd36f3a6df80b087275c664c)、[MAX32664C_OP_MODE_EXIT_WAKE_ON_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beaabbabbf098acf4a879f069d02ed62078)、[MAX32664C_OP_MODE_STOP_ALGO](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea95547f0e55f8d503d1d37f3739c17f1e)。

设备运行模式（Device Operating Modes）。

<a id="r_ga5fb415a0a706c29f716797f95bdbb5b5"></a>

```c
enum max32664c_algo_mode { MAX32664C_ALGO_MODE_CONT_HR_CONT_SPO2 , MAX32664C_ALGO_MODE_CONT_HR_SHOT_SPO2 , MAX32664C_ALGO_MODE_CONT_HRM }
```

相关声明：[max32664c_algo_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga5fb415a0a706c29f716797f95bdbb5b5)、[MAX32664C_ALGO_MODE_CONT_HR_CONT_SPO2](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5a6425e9c7e3769d25281c19cf5e5fa954)、[MAX32664C_ALGO_MODE_CONT_HR_SHOT_SPO2](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5a2bd5953493a9f8fcae0979b62375c390)、[MAX32664C_ALGO_MODE_CONT_HRM](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5aed19809fc94be1edfef581760f55871d)。

算法模式（Algorithm Modes）。

<a id="r_gaff919cdd89e996b1dd549d5d4c90332b"></a>

```c
enum max32664c_algo_gender { MAX32664_ALGO_GENDER_MALE , MAX32664_ALGO_GENDER_FEMALE }
```

相关声明：[max32664c_algo_gender](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gaff919cdd89e996b1dd549d5d4c90332b)、[MAX32664_ALGO_GENDER_MALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ggaff919cdd89e996b1dd549d5d4c90332bad21e4d729ab1a6fb720cfbada78c3bef)、[MAX32664_ALGO_GENDER_FEMALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ggaff919cdd89e996b1dd549d5d4c90332ba67f7abe973a85199fc4f0bc3288af9d8)。

性别设置（Gender Settings）。

<a id="r_ga133c713a42eaade83d29c47985d8d774"></a>

```c
enum max32664c_algo_activity { MAX32664C_ALGO_ACTIVITY_REST , MAX32664C_ALGO_ACTIVITY_OTHER , MAX32664C_ALGO_ACTIVITY_WALK , MAX32664C_ALGO_ACTIVITY_RUN , MAX32664C_ALGO_ACTIVITY_BIKE }
```

相关声明：[max32664c_algo_activity](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga133c713a42eaade83d29c47985d8d774)、[MAX32664C_ALGO_ACTIVITY_REST](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a5a54e6caa5a7ed1e08b074ecde5d714d)、[MAX32664C_ALGO_ACTIVITY_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a382aa84b2d97e3f2d6a82d1c49b30c24)、[MAX32664C_ALGO_ACTIVITY_WALK](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774aeecd8180b858f916fbdc9e7cde41e076)、[MAX32664C_ALGO_ACTIVITY_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a7ebcfb189e4c50e05ae0f47c73194226)、[MAX32664C_ALGO_ACTIVITY_BIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774ac0f76ceeab95810c5eceb0fb6511441f)。

活动类别（Activity Classes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.4\_函数（Functions）

<a id="r_gadb7194053272676b8e74091afd038153"></a>

```c
int max32664c_bl_enter (const struct device *dev, const uint8_t *firmware, uint32_t size)
```

相关声明：[max32664c_bl_enter](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gadb7194053272676b8e74091afd038153)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

进入引导加载程序模式（Bootloader Mode）并执行固件更新（Firmware Update）。

<a id="r_ga535f5274650f92b4d124f28193b4b08c"></a>

```c
int max32664c_bl_leave (const struct device *dev)
```

相关声明：[max32664c_bl_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga535f5274650f92b4d124f28193b4b08c)、[device](../device_reference/P002_设备对象结构.md)。

退出引导加载程序（Bootloader），进入应用模式（Application Mode）。

<a id="r_ga457886b7ab0d01d0409f658bb98d2478"></a>

```c
int max32664c_acc_fill_fifo (const struct device *dev, struct max32664c_acc_data_t *data, uint8_t length)
```

相关声明：[max32664c_acc_fill_fifo](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga457886b7ab0d01d0409f658bb98d2478)、[device](../device_reference/P002_设备对象结构.md)、[max32664c_acc_data_t](../device_power_control_model_reference/P024_max32664c_acc_data_t_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用加速度计数据填充先进先出缓冲区（FIFO Buffer）。


## 21.5\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_timing_sensor_reference/P007_max32664c.h_源码浏览.md)
- [max32664c_acc_data_t](../device_power_control_model_reference/P024_max32664c_acc_data_t_结构体.md)
- [MAX32664C_MOTION_TIME](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gac9f5586b750b0aac5a769428e05c69b5)
- [MAX32664C_MOTION_THRESHOLD](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gac29a24ee0d12f0f78b2777e256b02014)
- [sensor_channel_max32664c](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga52fbc189e74d50bf0841c611cc89e60f)
- [SENSOR_CHAN_MAX32664C_HEARTRATE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa18fce0c2b90a1b3b7b6c858abc0f146d)
- [SENSOR_CHAN_MAX32664C_BLOOD_OXYGEN_SATURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fab9a21912b7a4d4e0e936875cea89f79d)
- [SENSOR_CHAN_MAX32664C_RESPIRATION_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa8f5236ba1d83a87dac9c3f2ba0518150)
- [SENSOR_CHAN_MAX32664C_SKIN_CONTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa7e05a3690e0b931358a1fb5d4240151c)
- [SENSOR_CHAN_MAX32664C_ACTIVITY](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa3637772914acf3567d835a71baac9edc)
- [SENSOR_CHAN_MAX32664C_STEP_COUNTER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga52fbc189e74d50bf0841c611cc89e60fa274ca8282e34239db11d8b33b682c893)
- [sensor_attribute_max32664c](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga49bffbe46602089606b6d51eb46b7cb6)
- [SENSOR_ATTR_MAX32664C_GENDER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a1660d557ec24396e9a21326f914eab0d)
- [SENSOR_ATTR_MAX32664C_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a005e1b0d7b62a7ec05708852e4265671)
- [SENSOR_ATTR_MAX32664C_WEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6aa8843efabd00b375383816b835aee897)
- [SENSOR_ATTR_MAX32664C_HEIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6af84b67a4771f72b7cc8b2d11544fdba7)
- [SENSOR_ATTR_MAX32664C_OP_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga49bffbe46602089606b6d51eb46b7cb6a7a0baebbf68c802a46b03ac1cb27bec3)
- [max32664c_device_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga906ce2770956d586a46caa8d6c6d12be)
- [MAX32664C_OP_MODE_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beaae19d259bab6ef5004770d4f8b4626a0)
- [MAX32664C_OP_MODE_RAW](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea0e762d3b97f22c46d77ac4b01f5761d1)
- [MAX32664C_OP_MODE_ALGO_AEC](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beacbf561fd327a3b988e1a4090ba63219e)
- [MAX32664C_OP_MODE_ALGO_AEC_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea8db7362f61662b078272c4b435e1e2b6)
- [MAX32664C_OP_MODE_ALGO_AGC](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea460dba077adea0baf026428c0ad2ad0c)
- [MAX32664C_OP_MODE_ALGO_AGC_EXT](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea0001a3584cf3bbe819fc8f728e57ae0e)
- [MAX32664C_OP_MODE_SCD](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea14e153eb3be43d8218e4f7360e14b707)
- [MAX32664C_OP_MODE_WAKE_ON_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea87d0d5c0dd36f3a6df80b087275c664c)
- [MAX32664C_OP_MODE_EXIT_WAKE_ON_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12beaabbabbf098acf4a879f069d02ed62078)
- [MAX32664C_OP_MODE_STOP_ALGO](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga906ce2770956d586a46caa8d6c6d12bea95547f0e55f8d503d1d37f3739c17f1e)
- [max32664c_algo_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga5fb415a0a706c29f716797f95bdbb5b5)
- [MAX32664C_ALGO_MODE_CONT_HR_CONT_SPO2](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5a6425e9c7e3769d25281c19cf5e5fa954)
- [MAX32664C_ALGO_MODE_CONT_HR_SHOT_SPO2](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5a2bd5953493a9f8fcae0979b62375c390)
- [MAX32664C_ALGO_MODE_CONT_HRM](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga5fb415a0a706c29f716797f95bdbb5b5aed19809fc94be1edfef581760f55871d)
- [max32664c_algo_gender](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gaff919cdd89e996b1dd549d5d4c90332b)
- [MAX32664_ALGO_GENDER_MALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ggaff919cdd89e996b1dd549d5d4c90332bad21e4d729ab1a6fb720cfbada78c3bef)
- [MAX32664_ALGO_GENDER_FEMALE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ggaff919cdd89e996b1dd549d5d4c90332ba67f7abe973a85199fc4f0bc3288af9d8)
- [max32664c_algo_activity](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga133c713a42eaade83d29c47985d8d774)
- [MAX32664C_ALGO_ACTIVITY_REST](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a5a54e6caa5a7ed1e08b074ecde5d714d)
- [MAX32664C_ALGO_ACTIVITY_OTHER](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a382aa84b2d97e3f2d6a82d1c49b30c24)
- [MAX32664C_ALGO_ACTIVITY_WALK](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774aeecd8180b858f916fbdc9e7cde41e076)
- [MAX32664C_ALGO_ACTIVITY_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774a7ebcfb189e4c50e05ae0f47c73194226)
- [MAX32664C_ALGO_ACTIVITY_BIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gga133c713a42eaade83d29c47985d8d774ac0f76ceeab95810c5eceb0fb6511441f)
- [max32664c_bl_enter](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#gadb7194053272676b8e74091afd038153)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [max32664c_bl_leave](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga535f5274650f92b4d124f28193b4b08c)
- [max32664c_acc_fill_fifo](https://docs.zephyrproject.org/latest/doxygen/html/group__max32664c__interface.html#ga457886b7ab0d01d0409f658bb98d2478)

<a id="header-details"></a>

---

[上一章](P020_zephyr__dt-bindings__pinctrl__max32-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__mfd__mc146818.h_文件参考.md)
