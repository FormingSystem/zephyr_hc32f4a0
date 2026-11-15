---
id: learning.zephyr-docs.api-file-system-power-reference.page-17
title: zephyr__dt-bindings__sensor__icm42688.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icm42688_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_dt-bindings\_\_sensor\_\_icm42688.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/icm42688_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TDK InvenSense ICM42688 IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "icm4268x.h"
```

查看此文件的源码。

the TDK InvenSense ICM42688 IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_ga87d63526599a8e15867f8a81687143a6"></a>

```c
#define ICM42688_DT_ACCEL_OFF ICM4268X_DT_ACCEL_OFF
```

相关声明：[ICM42688_DT_ACCEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga87d63526599a8e15867f8a81687143a6)、[ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)。

已断电（Powered Down）。

<a id="r_ga7f242cb33068f441e14ab715486b1a0b"></a>

```c
#define ICM42688_DT_ACCEL_LP ICM4268X_DT_ACCEL_LP
```

相关声明：[ICM42688_DT_ACCEL_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7f242cb33068f441e14ab715486b1a0b)、[ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)。

低功耗模式（Low-power Mode）。

<a id="r_gaf5b12997154a39239be0ffa0447534dc"></a>

```c
#define ICM42688_DT_ACCEL_LN ICM4268X_DT_ACCEL_LN
```

相关声明：[ICM42688_DT_ACCEL_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf5b12997154a39239be0ffa0447534dc)、[ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)。

低噪声模式（Low-noise Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_gafc2406c073cc74279fb535c7b0d67227"></a>

```c
#define ICM42688_DT_GYRO_OFF ICM4268X_DT_GYRO_OFF
```

相关声明：[ICM42688_DT_GYRO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gafc2406c073cc74279fb535c7b0d67227)、[ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)。

已断电（Powered Down）。

<a id="r_ga4070c032a474deeb07d1489502f8d897"></a>

```c
#define ICM42688_DT_GYRO_STANDBY ICM4268X_DT_GYRO_STANDBY
```

相关声明：[ICM42688_DT_GYRO_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4070c032a474deeb07d1489502f8d897)、[ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)。

待机（Standby）。

<a id="r_ga3db2e450e940e1e1aee51a0a14789722"></a>

```c
#define ICM42688_DT_GYRO_LN ICM4268X_DT_GYRO_LN
```

相关声明：[ICM42688_DT_GYRO_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga3db2e450e940e1e1aee51a0a14789722)、[ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)。

低噪声模式（Low-noise Mode）。

<a id="define-members-2"></a>

### 加速度计满量程范围选项（Accelerometer Full-scale Range Options）

设备树属性（Devicetree Property）`accel-fs` 的取值。

<a id="r_ga4b0cb96ec7c9111d51dc3e6daa45a454"></a>

```c
#define ICM42688_DT_ACCEL_FS_16 0
```

相关声明：[ICM42688_DT_ACCEL_FS_16](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4b0cb96ec7c9111d51dc3e6daa45a454)。

量程（range）：±16 g。

<a id="r_gae5dc186bc3e9a5b7a8ee472472e7df37"></a>

```c
#define ICM42688_DT_ACCEL_FS_8 1
```

相关声明：[ICM42688_DT_ACCEL_FS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae5dc186bc3e9a5b7a8ee472472e7df37)。

量程（range）：±8 g。

<a id="r_gaa9ba13c727b1f341952d10578dcc896b"></a>

```c
#define ICM42688_DT_ACCEL_FS_4 2
```

相关声明：[ICM42688_DT_ACCEL_FS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa9ba13c727b1f341952d10578dcc896b)。

量程（range）：±4 g。

<a id="r_gae9e6505469f5ea0fc91450357b6066a8"></a>

```c
#define ICM42688_DT_ACCEL_FS_2 3
```

相关声明：[ICM42688_DT_ACCEL_FS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae9e6505469f5ea0fc91450357b6066a8)。

量程（range）：±2 g。

<a id="define-members-3"></a>

### 陀螺仪满量程范围选项（Gyroscope Full-scale Range Options）

设备树属性（Devicetree Property）`gyro-fs` 的取值。

<a id="r_gafd58a6f0d703709fa3405b1fbb735868"></a>

```c
#define ICM42688_DT_GYRO_FS_2000 0
```

相关声明：[ICM42688_DT_GYRO_FS_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gafd58a6f0d703709fa3405b1fbb735868)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga32dec1bd284e4b9bea6c8b0824f621e2"></a>

```c
#define ICM42688_DT_GYRO_FS_1000 1
```

相关声明：[ICM42688_DT_GYRO_FS_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga32dec1bd284e4b9bea6c8b0824f621e2)。

角速度量程：±1000 度／秒（dps）。

<a id="r_gaf3fdf21e86ffd73a1980000dfd076c37"></a>

```c
#define ICM42688_DT_GYRO_FS_500 2
```

相关声明：[ICM42688_DT_GYRO_FS_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf3fdf21e86ffd73a1980000dfd076c37)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga75e7daf434eb7ef267519373c1b355b2"></a>

```c
#define ICM42688_DT_GYRO_FS_250 3
```

相关声明：[ICM42688_DT_GYRO_FS_250](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga75e7daf434eb7ef267519373c1b355b2)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga275d65388f2c20626704c4ec2c3ae9ec"></a>

```c
#define ICM42688_DT_GYRO_FS_125 4
```

相关声明：[ICM42688_DT_GYRO_FS_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga275d65388f2c20626704c4ec2c3ae9ec)。

角速度量程：±125 度／秒（dps）。

<a id="r_gaa5c00905894ce34343859bd79d29cd2b"></a>

```c
#define ICM42688_DT_GYRO_FS_62_5 5
```

相关声明：[ICM42688_DT_GYRO_FS_62_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa5c00905894ce34343859bd79d29cd2b)。

±62.5 度每秒（dps）。

<a id="r_ga8d0d31941b583de0d4168eef66f924b4"></a>

```c
#define ICM42688_DT_GYRO_FS_31_25 6
```

相关声明：[ICM42688_DT_GYRO_FS_31_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8d0d31941b583de0d4168eef66f924b4)。

±31.25 度每秒（dps）。

<a id="r_ga136d5df096dd774eea09da8b1e1692d7"></a>

```c
#define ICM42688_DT_GYRO_FS_15_625 7
```

相关声明：[ICM42688_DT_GYRO_FS_15_625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga136d5df096dd774eea09da8b1e1692d7)。

±15.625 度每秒（dps）。

<a id="define-members-4"></a>

### 加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga9f5b07a7015e71ae5abf347ead6291e3"></a>

```c
#define ICM42688_DT_ACCEL_ODR_32000 ICM4268X_DT_ACCEL_ODR_32000
```

相关声明：[ICM42688_DT_ACCEL_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga9f5b07a7015e71ae5abf347ead6291e3)、[ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)。

频率（Frequency）：32 kHz。

<a id="r_ga105c05bba455b388095ce82a8d36a7c8"></a>

```c
#define ICM42688_DT_ACCEL_ODR_16000 ICM4268X_DT_ACCEL_ODR_16000
```

相关声明：[ICM42688_DT_ACCEL_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga105c05bba455b388095ce82a8d36a7c8)、[ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)。

频率（Frequency）：16 kHz。

<a id="r_gae7066ce06b50bce41f4a4948c2e847bf"></a>

```c
#define ICM42688_DT_ACCEL_ODR_8000 ICM4268X_DT_ACCEL_ODR_8000
```

相关声明：[ICM42688_DT_ACCEL_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae7066ce06b50bce41f4a4948c2e847bf)、[ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)。

频率（Frequency）：8 kHz。

<a id="r_ga8961f60a4dc64f0a0ba6699dddfe9db5"></a>

```c
#define ICM42688_DT_ACCEL_ODR_4000 ICM4268X_DT_ACCEL_ODR_4000
```

相关声明：[ICM42688_DT_ACCEL_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8961f60a4dc64f0a0ba6699dddfe9db5)、[ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)。

频率（Frequency）：4 kHz。

<a id="r_ga436149a059ac4fa46a0dc7d2f2fbf14b"></a>

```c
#define ICM42688_DT_ACCEL_ODR_2000 ICM4268X_DT_ACCEL_ODR_2000
```

相关声明：[ICM42688_DT_ACCEL_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga436149a059ac4fa46a0dc7d2f2fbf14b)、[ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)。

频率（Frequency）：2 kHz。

<a id="r_gab79a2b8bb3375baddbdac25e510390a3"></a>

```c
#define ICM42688_DT_ACCEL_ODR_1000 ICM4268X_DT_ACCEL_ODR_1000
```

相关声明：[ICM42688_DT_ACCEL_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gab79a2b8bb3375baddbdac25e510390a3)、[ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)。

频率（Frequency）：1 kHz。

<a id="r_gaf8207e0143df25ed4a1464bce57c657a"></a>

```c
#define ICM42688_DT_ACCEL_ODR_200 ICM4268X_DT_ACCEL_ODR_200
```

相关声明：[ICM42688_DT_ACCEL_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf8207e0143df25ed4a1464bce57c657a)、[ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)。

频率：200 Hz。

<a id="r_gaf35508e00e03e0e31daa348908463064"></a>

```c
#define ICM42688_DT_ACCEL_ODR_100 ICM4268X_DT_ACCEL_ODR_100
```

相关声明：[ICM42688_DT_ACCEL_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf35508e00e03e0e31daa348908463064)、[ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)。

频率：100 Hz。

<a id="r_ga984bf8f1d3e26a8c97be3353625015c4"></a>

```c
#define ICM42688_DT_ACCEL_ODR_50 ICM4268X_DT_ACCEL_ODR_50
```

相关声明：[ICM42688_DT_ACCEL_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga984bf8f1d3e26a8c97be3353625015c4)、[ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)。

频率：50 Hz。

<a id="r_gab2de64d35ebb0846b745f95ec7b8208f"></a>

```c
#define ICM42688_DT_ACCEL_ODR_25 ICM4268X_DT_ACCEL_ODR_25
```

相关声明：[ICM42688_DT_ACCEL_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gab2de64d35ebb0846b745f95ec7b8208f)、[ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)。

频率：25 Hz。

<a id="r_ga7175704ce1c016283cd04e1bf64302c7"></a>

```c
#define ICM42688_DT_ACCEL_ODR_12_5 ICM4268X_DT_ACCEL_ODR_12_5
```

相关声明：[ICM42688_DT_ACCEL_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7175704ce1c016283cd04e1bf64302c7)、[ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)。

频率：12.5 Hz。

<a id="r_ga7ed7d0e51c7cf673f99876206fa02979"></a>

```c
#define ICM42688_DT_ACCEL_ODR_6_25 ICM4268X_DT_ACCEL_ODR_6_25
```

相关声明：[ICM42688_DT_ACCEL_ODR_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7ed7d0e51c7cf673f99876206fa02979)、[ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)。

频率：6.25 Hz。

<a id="r_ga99fbf31276619831ff2c51d74f87de0e"></a>

```c
#define ICM42688_DT_ACCEL_ODR_3_125 ICM4268X_DT_ACCEL_ODR_3_125
```

相关声明：[ICM42688_DT_ACCEL_ODR_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga99fbf31276619831ff2c51d74f87de0e)、[ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)。

频率（Frequency）：3.125 Hz。

<a id="r_ga884108d1f13010cb7728309d04913c1a"></a>

```c
#define ICM42688_DT_ACCEL_ODR_1_5625 ICM4268X_DT_ACCEL_ODR_1_5625
```

相关声明：[ICM42688_DT_ACCEL_ODR_1_5625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga884108d1f13010cb7728309d04913c1a)、[ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)。

频率（Frequency）：1.5625 Hz。

<a id="r_ga11cbb666797208cf07a7c05172f45328"></a>

```c
#define ICM42688_DT_ACCEL_ODR_500 ICM4268X_DT_ACCEL_ODR_500
```

相关声明：[ICM42688_DT_ACCEL_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga11cbb666797208cf07a7c05172f45328)、[ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)。

频率（Frequency）：500 Hz。

<a id="define-members-5"></a>

### 陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_ga2e17dd4df432f27dad3130ce87145bf3"></a>

```c
#define ICM42688_DT_GYRO_ODR_32000 ICM4268X_DT_GYRO_ODR_32000
```

相关声明：[ICM42688_DT_GYRO_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga2e17dd4df432f27dad3130ce87145bf3)、[ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)。

频率（Frequency）：32 kHz。

<a id="r_gad6771ff80a7458e15fe95ddcb7dd4ddb"></a>

```c
#define ICM42688_DT_GYRO_ODR_16000 ICM4268X_DT_GYRO_ODR_16000
```

相关声明：[ICM42688_DT_GYRO_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad6771ff80a7458e15fe95ddcb7dd4ddb)、[ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)。

频率（Frequency）：16 kHz。

<a id="r_gaa480c0e491e763c7cf432eb5a10e3b61"></a>

```c
#define ICM42688_DT_GYRO_ODR_8000 ICM4268X_DT_GYRO_ODR_8000
```

相关声明：[ICM42688_DT_GYRO_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa480c0e491e763c7cf432eb5a10e3b61)、[ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)。

频率（Frequency）：8 kHz。

<a id="r_ga210eb2555fe74a1856a4d8cf86a98a85"></a>

```c
#define ICM42688_DT_GYRO_ODR_4000 ICM4268X_DT_GYRO_ODR_4000
```

相关声明：[ICM42688_DT_GYRO_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga210eb2555fe74a1856a4d8cf86a98a85)、[ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)。

频率（Frequency）：4 kHz。

<a id="r_ga63914f308453c2b2027c423758c0ac68"></a>

```c
#define ICM42688_DT_GYRO_ODR_2000 ICM4268X_DT_GYRO_ODR_2000
```

相关声明：[ICM42688_DT_GYRO_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga63914f308453c2b2027c423758c0ac68)、[ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)。

频率（Frequency）：2 kHz。

<a id="r_ga1b064df9c50b0bca2f3eb0bd5a1e75c9"></a>

```c
#define ICM42688_DT_GYRO_ODR_1000 ICM4268X_DT_GYRO_ODR_1000
```

相关声明：[ICM42688_DT_GYRO_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga1b064df9c50b0bca2f3eb0bd5a1e75c9)、[ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)。

频率（Frequency）：1 kHz。

<a id="r_ga8f4a769442b8d84eebb686ef36543a87"></a>

```c
#define ICM42688_DT_GYRO_ODR_200 ICM4268X_DT_GYRO_ODR_200
```

相关声明：[ICM42688_DT_GYRO_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8f4a769442b8d84eebb686ef36543a87)、[ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)。

频率：200 Hz。

<a id="r_ga83bf124e7235b4e69b2e4f66057aaee8"></a>

```c
#define ICM42688_DT_GYRO_ODR_100 ICM4268X_DT_GYRO_ODR_100
```

相关声明：[ICM42688_DT_GYRO_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga83bf124e7235b4e69b2e4f66057aaee8)、[ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)。

频率：100 Hz。

<a id="r_gad6e0ba010e01fe8f98bbdd213ef8540c"></a>

```c
#define ICM42688_DT_GYRO_ODR_50 ICM4268X_DT_GYRO_ODR_50
```

相关声明：[ICM42688_DT_GYRO_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad6e0ba010e01fe8f98bbdd213ef8540c)、[ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)。

频率：50 Hz。

<a id="r_gad3588dd673827b2a760185d5925eef8d"></a>

```c
#define ICM42688_DT_GYRO_ODR_25 ICM4268X_DT_GYRO_ODR_25
```

相关声明：[ICM42688_DT_GYRO_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad3588dd673827b2a760185d5925eef8d)、[ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)。

频率：25 Hz。

<a id="r_gaa689b84d321042fdc48c9ea2dc5323c3"></a>

```c
#define ICM42688_DT_GYRO_ODR_12_5 ICM4268X_DT_GYRO_ODR_12_5
```

相关声明：[ICM42688_DT_GYRO_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa689b84d321042fdc48c9ea2dc5323c3)、[ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)。

频率：12.5 Hz。

<a id="r_ga4973fdb062b851dafdc74fc1f87998a1"></a>

```c
#define ICM42688_DT_GYRO_ODR_500 ICM4268X_DT_GYRO_ODR_500
```

相关声明：[ICM42688_DT_GYRO_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4973fdb062b851dafdc74fc1f87998a1)、[ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)。

频率（Frequency）：500 Hz。


## 17.2\_原页交叉引用（Cross References）

- [icm4268x.h](../api_source_reference/P203_icm4268x.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P334_icm42688.h_源码浏览.md)
- [ICM42688_DT_ACCEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga87d63526599a8e15867f8a81687143a6)
- [ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)
- [ICM42688_DT_ACCEL_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7f242cb33068f441e14ab715486b1a0b)
- [ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)
- [ICM42688_DT_ACCEL_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf5b12997154a39239be0ffa0447534dc)
- [ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)
- [ICM42688_DT_GYRO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gafc2406c073cc74279fb535c7b0d67227)
- [ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)
- [ICM42688_DT_GYRO_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4070c032a474deeb07d1489502f8d897)
- [ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)
- [ICM42688_DT_GYRO_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga3db2e450e940e1e1aee51a0a14789722)
- [ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)
- [ICM42688_DT_ACCEL_FS_16](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4b0cb96ec7c9111d51dc3e6daa45a454)
- [ICM42688_DT_ACCEL_FS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae5dc186bc3e9a5b7a8ee472472e7df37)
- [ICM42688_DT_ACCEL_FS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa9ba13c727b1f341952d10578dcc896b)
- [ICM42688_DT_ACCEL_FS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae9e6505469f5ea0fc91450357b6066a8)
- [ICM42688_DT_GYRO_FS_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gafd58a6f0d703709fa3405b1fbb735868)
- [ICM42688_DT_GYRO_FS_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga32dec1bd284e4b9bea6c8b0824f621e2)
- [ICM42688_DT_GYRO_FS_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf3fdf21e86ffd73a1980000dfd076c37)
- [ICM42688_DT_GYRO_FS_250](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga75e7daf434eb7ef267519373c1b355b2)
- [ICM42688_DT_GYRO_FS_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga275d65388f2c20626704c4ec2c3ae9ec)
- [ICM42688_DT_GYRO_FS_62_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa5c00905894ce34343859bd79d29cd2b)
- [ICM42688_DT_GYRO_FS_31_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8d0d31941b583de0d4168eef66f924b4)
- [ICM42688_DT_GYRO_FS_15_625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga136d5df096dd774eea09da8b1e1692d7)
- [ICM42688_DT_ACCEL_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga9f5b07a7015e71ae5abf347ead6291e3)
- [ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)
- [ICM42688_DT_ACCEL_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga105c05bba455b388095ce82a8d36a7c8)
- [ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)
- [ICM42688_DT_ACCEL_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gae7066ce06b50bce41f4a4948c2e847bf)
- [ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)
- [ICM42688_DT_ACCEL_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8961f60a4dc64f0a0ba6699dddfe9db5)
- [ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)
- [ICM42688_DT_ACCEL_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga436149a059ac4fa46a0dc7d2f2fbf14b)
- [ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)
- [ICM42688_DT_ACCEL_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gab79a2b8bb3375baddbdac25e510390a3)
- [ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)
- [ICM42688_DT_ACCEL_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf8207e0143df25ed4a1464bce57c657a)
- [ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)
- [ICM42688_DT_ACCEL_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaf35508e00e03e0e31daa348908463064)
- [ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)
- [ICM42688_DT_ACCEL_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga984bf8f1d3e26a8c97be3353625015c4)
- [ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)
- [ICM42688_DT_ACCEL_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gab2de64d35ebb0846b745f95ec7b8208f)
- [ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)
- [ICM42688_DT_ACCEL_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7175704ce1c016283cd04e1bf64302c7)
- [ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)
- [ICM42688_DT_ACCEL_ODR_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga7ed7d0e51c7cf673f99876206fa02979)
- [ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)
- [ICM42688_DT_ACCEL_ODR_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga99fbf31276619831ff2c51d74f87de0e)
- [ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)
- [ICM42688_DT_ACCEL_ODR_1_5625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga884108d1f13010cb7728309d04913c1a)
- [ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)
- [ICM42688_DT_ACCEL_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga11cbb666797208cf07a7c05172f45328)
- [ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)
- [ICM42688_DT_GYRO_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga2e17dd4df432f27dad3130ce87145bf3)
- [ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)
- [ICM42688_DT_GYRO_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad6771ff80a7458e15fe95ddcb7dd4ddb)
- [ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)
- [ICM42688_DT_GYRO_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa480c0e491e763c7cf432eb5a10e3b61)
- [ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)
- [ICM42688_DT_GYRO_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga210eb2555fe74a1856a4d8cf86a98a85)
- [ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)
- [ICM42688_DT_GYRO_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga63914f308453c2b2027c423758c0ac68)
- [ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)
- [ICM42688_DT_GYRO_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga1b064df9c50b0bca2f3eb0bd5a1e75c9)
- [ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)
- [ICM42688_DT_GYRO_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga8f4a769442b8d84eebb686ef36543a87)
- [ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)
- [ICM42688_DT_GYRO_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga83bf124e7235b4e69b2e4f66057aaee8)
- [ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)
- [ICM42688_DT_GYRO_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad6e0ba010e01fe8f98bbdd213ef8540c)
- [ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)
- [ICM42688_DT_GYRO_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gad3588dd673827b2a760185d5925eef8d)
- [ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)
- [ICM42688_DT_GYRO_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#gaa689b84d321042fdc48c9ea2dc5323c3)
- [ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)
- [ICM42688_DT_GYRO_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42688__interface.html#ga4973fdb062b851dafdc74fc1f87998a1)
- [ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)

<a id="header-details"></a>

---

[上一章](P016_zephyr__dt-bindings__sensor__icm42686.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__dt-bindings__pinctrl__ifx_cat1-pinctrl.h_文件参考.md)
