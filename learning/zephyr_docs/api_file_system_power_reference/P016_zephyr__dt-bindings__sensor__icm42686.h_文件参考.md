---
id: learning.zephyr-docs.api-file-system-power-reference.page-16
title: zephyr__dt-bindings__sensor__icm42686.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icm42686_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_dt-bindings\_\_sensor\_\_icm42686.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/icm42686_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TDK InvenSense ICM42686 IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "icm4268x.h"
```

查看此文件的源码。

the TDK InvenSense ICM42686 IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_gaab2358d3812334977177bc43ff85c649"></a>

```c
#define ICM42686_DT_ACCEL_OFF ICM4268X_DT_ACCEL_OFF
```

相关声明：[ICM42686_DT_ACCEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaab2358d3812334977177bc43ff85c649)、[ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)。

已断电（Powered Down）。

<a id="r_ga4f65f2e1487071d5a2c671236e79b548"></a>

```c
#define ICM42686_DT_ACCEL_LP ICM4268X_DT_ACCEL_LP
```

相关声明：[ICM42686_DT_ACCEL_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga4f65f2e1487071d5a2c671236e79b548)、[ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)。

低功耗模式（Low-power Mode）。

<a id="r_gadfd468cfac2f4c603c91fce87364bc8d"></a>

```c
#define ICM42686_DT_ACCEL_LN ICM4268X_DT_ACCEL_LN
```

相关声明：[ICM42686_DT_ACCEL_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gadfd468cfac2f4c603c91fce87364bc8d)、[ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)。

低噪声模式（Low-noise Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_gaecf9d86d270328922ee8aa7fac02e099"></a>

```c
#define ICM42686_DT_GYRO_OFF ICM4268X_DT_GYRO_OFF
```

相关声明：[ICM42686_DT_GYRO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaecf9d86d270328922ee8aa7fac02e099)、[ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)。

已断电（Powered Down）。

<a id="r_ga8d38b71305bc5df2b00495bccaf4170b"></a>

```c
#define ICM42686_DT_GYRO_STANDBY ICM4268X_DT_GYRO_STANDBY
```

相关声明：[ICM42686_DT_GYRO_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga8d38b71305bc5df2b00495bccaf4170b)、[ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)。

待机（Standby）。

<a id="r_ga8dcb695ebe2e014c95ab6e4c9fe4c295"></a>

```c
#define ICM42686_DT_GYRO_LN ICM4268X_DT_GYRO_LN
```

相关声明：[ICM42686_DT_GYRO_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga8dcb695ebe2e014c95ab6e4c9fe4c295)、[ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)。

低噪声模式（Low-noise Mode）。

<a id="define-members-2"></a>

### 加速度计满量程范围选项（Accelerometer Full-scale Range Options）

设备树属性（Devicetree Property）`accel-fs` 的取值。

<a id="r_ga9cebe564f334b193a945df4285a99292"></a>

```c
#define ICM42686_DT_ACCEL_FS_32 0
```

相关声明：[ICM42686_DT_ACCEL_FS_32](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga9cebe564f334b193a945df4285a99292)。

量程（range）：±32 g。

<a id="r_gafcabad1dbc14dafb440523f70dae55c7"></a>

```c
#define ICM42686_DT_ACCEL_FS_16 1
```

相关声明：[ICM42686_DT_ACCEL_FS_16](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gafcabad1dbc14dafb440523f70dae55c7)。

量程（range）：±16 g。

<a id="r_gad4b5d0c0b8d83827d13492277496cd15"></a>

```c
#define ICM42686_DT_ACCEL_FS_8 2
```

相关声明：[ICM42686_DT_ACCEL_FS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad4b5d0c0b8d83827d13492277496cd15)。

量程（range）：±8 g。

<a id="r_gaf2501f7539192df5ac1d6c7cc7456240"></a>

```c
#define ICM42686_DT_ACCEL_FS_4 3
```

相关声明：[ICM42686_DT_ACCEL_FS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf2501f7539192df5ac1d6c7cc7456240)。

量程（range）：±4 g。

<a id="r_gac264593afd53d9429d1c1b44cd5c823f"></a>

```c
#define ICM42686_DT_ACCEL_FS_2 4
```

相关声明：[ICM42686_DT_ACCEL_FS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gac264593afd53d9429d1c1b44cd5c823f)。

量程（range）：±2 g。

<a id="define-members-3"></a>

### 陀螺仪满量程范围选项（Gyroscope Full-scale Range Options）

设备树属性（Devicetree Property）`gyro-fs` 的取值。

<a id="r_ga13bf6d9c9ab41da66e04b79c2747d5e0"></a>

```c
#define ICM42686_DT_GYRO_FS_4000 0
```

相关声明：[ICM42686_DT_GYRO_FS_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga13bf6d9c9ab41da66e04b79c2747d5e0)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="r_ga56ac41b52b4850acfd36f7be87a455b7"></a>

```c
#define ICM42686_DT_GYRO_FS_2000 1
```

相关声明：[ICM42686_DT_GYRO_FS_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga56ac41b52b4850acfd36f7be87a455b7)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gac098d209098f991a9397184a8ed628fa"></a>

```c
#define ICM42686_DT_GYRO_FS_1000 2
```

相关声明：[ICM42686_DT_GYRO_FS_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gac098d209098f991a9397184a8ed628fa)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga3d5589bbabcd77ee83ef84594af6d9ae"></a>

```c
#define ICM42686_DT_GYRO_FS_500 3
```

相关声明：[ICM42686_DT_GYRO_FS_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3d5589bbabcd77ee83ef84594af6d9ae)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga7a614489f7bb1dee7a256eee9b9ff68f"></a>

```c
#define ICM42686_DT_GYRO_FS_250 4
```

相关声明：[ICM42686_DT_GYRO_FS_250](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7a614489f7bb1dee7a256eee9b9ff68f)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga880851c54e386a4ea59f64a2ac30e69a"></a>

```c
#define ICM42686_DT_GYRO_FS_125 5
```

相关声明：[ICM42686_DT_GYRO_FS_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga880851c54e386a4ea59f64a2ac30e69a)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga2d9366883bb38d77ffcd3d274912f51d"></a>

```c
#define ICM42686_DT_GYRO_FS_62_5 6
```

相关声明：[ICM42686_DT_GYRO_FS_62_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2d9366883bb38d77ffcd3d274912f51d)。

±62.5 度每秒（dps）。

<a id="r_gae998824d53c3f50c7f18ca37ae60bfae"></a>

```c
#define ICM42686_DT_GYRO_FS_31_25 7
```

相关声明：[ICM42686_DT_GYRO_FS_31_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gae998824d53c3f50c7f18ca37ae60bfae)。

±31.25 度每秒（dps）。

<a id="define-members-4"></a>

### 加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga625f1df6ef6e22fef1b24989cceda243"></a>

```c
#define ICM42686_DT_ACCEL_ODR_32000 ICM4268X_DT_ACCEL_ODR_32000
```

相关声明：[ICM42686_DT_ACCEL_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga625f1df6ef6e22fef1b24989cceda243)、[ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)。

频率（Frequency）：32 kHz。

<a id="r_gad2bb69689667ddc36ce5b6976d297594"></a>

```c
#define ICM42686_DT_ACCEL_ODR_16000 ICM4268X_DT_ACCEL_ODR_16000
```

相关声明：[ICM42686_DT_ACCEL_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad2bb69689667ddc36ce5b6976d297594)、[ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)。

频率（Frequency）：16 kHz。

<a id="r_ga9d3dc68385c3cc4f86923bc8399bc0a5"></a>

```c
#define ICM42686_DT_ACCEL_ODR_8000 ICM4268X_DT_ACCEL_ODR_8000
```

相关声明：[ICM42686_DT_ACCEL_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga9d3dc68385c3cc4f86923bc8399bc0a5)、[ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)。

频率（Frequency）：8 kHz。

<a id="r_ga1c2d0d0f910b36ddefc9135f90884abb"></a>

```c
#define ICM42686_DT_ACCEL_ODR_4000 ICM4268X_DT_ACCEL_ODR_4000
```

相关声明：[ICM42686_DT_ACCEL_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga1c2d0d0f910b36ddefc9135f90884abb)、[ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)。

频率（Frequency）：4 kHz。

<a id="r_ga7fff6c8ca5c1fbacaf03d87cb49a4ae3"></a>

```c
#define ICM42686_DT_ACCEL_ODR_2000 ICM4268X_DT_ACCEL_ODR_2000
```

相关声明：[ICM42686_DT_ACCEL_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7fff6c8ca5c1fbacaf03d87cb49a4ae3)、[ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)。

频率（Frequency）：2 kHz。

<a id="r_gad1a1f1ff011690cc3b56b7ff86336a3b"></a>

```c
#define ICM42686_DT_ACCEL_ODR_1000 ICM4268X_DT_ACCEL_ODR_1000
```

相关声明：[ICM42686_DT_ACCEL_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad1a1f1ff011690cc3b56b7ff86336a3b)、[ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)。

频率（Frequency）：1 kHz。

<a id="r_ga3f9eded7e8846a4e88275e5b6938c496"></a>

```c
#define ICM42686_DT_ACCEL_ODR_200 ICM4268X_DT_ACCEL_ODR_200
```

相关声明：[ICM42686_DT_ACCEL_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3f9eded7e8846a4e88275e5b6938c496)、[ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)。

频率：200 Hz。

<a id="r_ga646476319872dee9f9aad7b81bbd5224"></a>

```c
#define ICM42686_DT_ACCEL_ODR_100 ICM4268X_DT_ACCEL_ODR_100
```

相关声明：[ICM42686_DT_ACCEL_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga646476319872dee9f9aad7b81bbd5224)、[ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)。

频率：100 Hz。

<a id="r_ga07bd4b377204b75acbc34ebad27ed19e"></a>

```c
#define ICM42686_DT_ACCEL_ODR_50 ICM4268X_DT_ACCEL_ODR_50
```

相关声明：[ICM42686_DT_ACCEL_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga07bd4b377204b75acbc34ebad27ed19e)、[ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)。

频率：50 Hz。

<a id="r_gaf0101542510ee1dcfda88709d426cbaf"></a>

```c
#define ICM42686_DT_ACCEL_ODR_25 ICM4268X_DT_ACCEL_ODR_25
```

相关声明：[ICM42686_DT_ACCEL_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf0101542510ee1dcfda88709d426cbaf)、[ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)。

频率：25 Hz。

<a id="r_gafb5acfc89e580cec600bfe3cad20c8a2"></a>

```c
#define ICM42686_DT_ACCEL_ODR_12_5 ICM4268X_DT_ACCEL_ODR_12_5
```

相关声明：[ICM42686_DT_ACCEL_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gafb5acfc89e580cec600bfe3cad20c8a2)、[ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)。

频率：12.5 Hz。

<a id="r_ga2d5d7996d2a99293759a1eef2f1bae4b"></a>

```c
#define ICM42686_DT_ACCEL_ODR_6_25 ICM4268X_DT_ACCEL_ODR_6_25
```

相关声明：[ICM42686_DT_ACCEL_ODR_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2d5d7996d2a99293759a1eef2f1bae4b)、[ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)。

频率：6.25 Hz。

<a id="r_gace7b5b17fce265c174c9db2fe19c4520"></a>

```c
#define ICM42686_DT_ACCEL_ODR_3_125 ICM4268X_DT_ACCEL_ODR_3_125
```

相关声明：[ICM42686_DT_ACCEL_ODR_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gace7b5b17fce265c174c9db2fe19c4520)、[ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)。

频率（Frequency）：3.125 Hz。

<a id="r_ga6fb220853ef49be013ff6d475e14a17d"></a>

```c
#define ICM42686_DT_ACCEL_ODR_1_5625 ICM4268X_DT_ACCEL_ODR_1_5625
```

相关声明：[ICM42686_DT_ACCEL_ODR_1_5625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga6fb220853ef49be013ff6d475e14a17d)、[ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)。

频率（Frequency）：1.5625 Hz。

<a id="r_ga7de3aee656da50ad36340f8757510723"></a>

```c
#define ICM42686_DT_ACCEL_ODR_500 ICM4268X_DT_ACCEL_ODR_500
```

相关声明：[ICM42686_DT_ACCEL_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7de3aee656da50ad36340f8757510723)、[ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)。

频率（Frequency）：500 Hz。

<a id="define-members-5"></a>

### 陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_ga1909f71adf7d0deb04842e2d569acf1b"></a>

```c
#define ICM42686_DT_GYRO_ODR_32000 ICM4268X_DT_GYRO_ODR_32000
```

相关声明：[ICM42686_DT_GYRO_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga1909f71adf7d0deb04842e2d569acf1b)、[ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)。

频率（Frequency）：32 kHz。

<a id="r_gabf0897e9a07625890ed8f75dbb88ca9e"></a>

```c
#define ICM42686_DT_GYRO_ODR_16000 ICM4268X_DT_GYRO_ODR_16000
```

相关声明：[ICM42686_DT_GYRO_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gabf0897e9a07625890ed8f75dbb88ca9e)、[ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)。

频率（Frequency）：16 kHz。

<a id="r_ga406b26d9ad6b0a2db6ced76844efdb39"></a>

```c
#define ICM42686_DT_GYRO_ODR_8000 ICM4268X_DT_GYRO_ODR_8000
```

相关声明：[ICM42686_DT_GYRO_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga406b26d9ad6b0a2db6ced76844efdb39)、[ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)。

频率（Frequency）：8 kHz。

<a id="r_ga3f922bb1d6a2c0f1e8cf3430d46ad4ac"></a>

```c
#define ICM42686_DT_GYRO_ODR_4000 ICM4268X_DT_GYRO_ODR_4000
```

相关声明：[ICM42686_DT_GYRO_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3f922bb1d6a2c0f1e8cf3430d46ad4ac)、[ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)。

频率（Frequency）：4 kHz。

<a id="r_gaf237aa46d8900fbbbc915a9f994a9a4e"></a>

```c
#define ICM42686_DT_GYRO_ODR_2000 ICM4268X_DT_GYRO_ODR_2000
```

相关声明：[ICM42686_DT_GYRO_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf237aa46d8900fbbbc915a9f994a9a4e)、[ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)。

频率（Frequency）：2 kHz。

<a id="r_gada5ca8e905c61e5b9d5ad31c38f04bb5"></a>

```c
#define ICM42686_DT_GYRO_ODR_1000 ICM4268X_DT_GYRO_ODR_1000
```

相关声明：[ICM42686_DT_GYRO_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gada5ca8e905c61e5b9d5ad31c38f04bb5)、[ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)。

频率（Frequency）：1 kHz。

<a id="r_gae72fc8d11696187690b188f9ab32a81e"></a>

```c
#define ICM42686_DT_GYRO_ODR_200 ICM4268X_DT_GYRO_ODR_200
```

相关声明：[ICM42686_DT_GYRO_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gae72fc8d11696187690b188f9ab32a81e)、[ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)。

频率：200 Hz。

<a id="r_ga80dddd00891d085232f71476b25f3d34"></a>

```c
#define ICM42686_DT_GYRO_ODR_100 ICM4268X_DT_GYRO_ODR_100
```

相关声明：[ICM42686_DT_GYRO_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga80dddd00891d085232f71476b25f3d34)、[ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)。

频率：100 Hz。

<a id="r_ga14fe9aaaa2b784fde911348ecda0b2f9"></a>

```c
#define ICM42686_DT_GYRO_ODR_50 ICM4268X_DT_GYRO_ODR_50
```

相关声明：[ICM42686_DT_GYRO_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga14fe9aaaa2b784fde911348ecda0b2f9)、[ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)。

频率：50 Hz。

<a id="r_ga09b72d55bd41fa776c911aa87ff009dc"></a>

```c
#define ICM42686_DT_GYRO_ODR_25 ICM4268X_DT_GYRO_ODR_25
```

相关声明：[ICM42686_DT_GYRO_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga09b72d55bd41fa776c911aa87ff009dc)、[ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)。

频率：25 Hz。

<a id="r_ga86309657f593e3cb695817f18f9c1e2d"></a>

```c
#define ICM42686_DT_GYRO_ODR_12_5 ICM4268X_DT_GYRO_ODR_12_5
```

相关声明：[ICM42686_DT_GYRO_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga86309657f593e3cb695817f18f9c1e2d)、[ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)。

频率：12.5 Hz。

<a id="r_ga2205a9906948b3dc6a131bd20ca93f42"></a>

```c
#define ICM42686_DT_GYRO_ODR_500 ICM4268X_DT_GYRO_ODR_500
```

相关声明：[ICM42686_DT_GYRO_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2205a9906948b3dc6a131bd20ca93f42)、[ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)。

频率（Frequency）：500 Hz。


## 16.2\_原页交叉引用（Cross References）

- [icm4268x.h](../api_source_reference/P203_icm4268x.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P333_icm42686.h_源码浏览.md)
- [ICM42686_DT_ACCEL_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaab2358d3812334977177bc43ff85c649)
- [ICM4268X_DT_ACCEL_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf62125a80155dc35e6e4f2515e8612fb)
- [ICM42686_DT_ACCEL_LP](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga4f65f2e1487071d5a2c671236e79b548)
- [ICM4268X_DT_ACCEL_LP](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga57ec4d12a7591211a0a0b86bc82fe231)
- [ICM42686_DT_ACCEL_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gadfd468cfac2f4c603c91fce87364bc8d)
- [ICM4268X_DT_ACCEL_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga15803e78f53d4cd6b1a73977d9a2d7f2)
- [ICM42686_DT_GYRO_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaecf9d86d270328922ee8aa7fac02e099)
- [ICM4268X_DT_GYRO_OFF](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0ed5ffc1cad9f3a93fc6b35481a6bc0f)
- [ICM42686_DT_GYRO_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga8d38b71305bc5df2b00495bccaf4170b)
- [ICM4268X_DT_GYRO_STANDBY](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac39cbda0e1ea17f416a6b93c87a8307f)
- [ICM42686_DT_GYRO_LN](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga8dcb695ebe2e014c95ab6e4c9fe4c295)
- [ICM4268X_DT_GYRO_LN](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga2dbd021704b4480f8529e63e1a6c7bbf)
- [ICM42686_DT_ACCEL_FS_32](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga9cebe564f334b193a945df4285a99292)
- [ICM42686_DT_ACCEL_FS_16](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gafcabad1dbc14dafb440523f70dae55c7)
- [ICM42686_DT_ACCEL_FS_8](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad4b5d0c0b8d83827d13492277496cd15)
- [ICM42686_DT_ACCEL_FS_4](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf2501f7539192df5ac1d6c7cc7456240)
- [ICM42686_DT_ACCEL_FS_2](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gac264593afd53d9429d1c1b44cd5c823f)
- [ICM42686_DT_GYRO_FS_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga13bf6d9c9ab41da66e04b79c2747d5e0)
- [ICM42686_DT_GYRO_FS_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga56ac41b52b4850acfd36f7be87a455b7)
- [ICM42686_DT_GYRO_FS_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gac098d209098f991a9397184a8ed628fa)
- [ICM42686_DT_GYRO_FS_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3d5589bbabcd77ee83ef84594af6d9ae)
- [ICM42686_DT_GYRO_FS_250](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7a614489f7bb1dee7a256eee9b9ff68f)
- [ICM42686_DT_GYRO_FS_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga880851c54e386a4ea59f64a2ac30e69a)
- [ICM42686_DT_GYRO_FS_62_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2d9366883bb38d77ffcd3d274912f51d)
- [ICM42686_DT_GYRO_FS_31_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gae998824d53c3f50c7f18ca37ae60bfae)
- [ICM42686_DT_ACCEL_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga625f1df6ef6e22fef1b24989cceda243)
- [ICM4268X_DT_ACCEL_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d921e728429957ebf06b39b28e4aee4)
- [ICM42686_DT_ACCEL_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad2bb69689667ddc36ce5b6976d297594)
- [ICM4268X_DT_ACCEL_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga1b30ff257f338277142adad272d3fb61)
- [ICM42686_DT_ACCEL_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga9d3dc68385c3cc4f86923bc8399bc0a5)
- [ICM4268X_DT_ACCEL_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac28b1215367f9a571aa3db1cf1760649)
- [ICM42686_DT_ACCEL_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga1c2d0d0f910b36ddefc9135f90884abb)
- [ICM4268X_DT_ACCEL_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga6124a2372e403657672e838121b24016)
- [ICM42686_DT_ACCEL_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7fff6c8ca5c1fbacaf03d87cb49a4ae3)
- [ICM4268X_DT_ACCEL_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7711f8b4ce0e8c9375a9ab054b4d3653)
- [ICM42686_DT_ACCEL_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gad1a1f1ff011690cc3b56b7ff86336a3b)
- [ICM4268X_DT_ACCEL_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga002b562a990715f7718aa008b2025cbb)
- [ICM42686_DT_ACCEL_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3f9eded7e8846a4e88275e5b6938c496)
- [ICM4268X_DT_ACCEL_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gac057ecd6a55247301e311f89f16ccfef)
- [ICM42686_DT_ACCEL_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga646476319872dee9f9aad7b81bbd5224)
- [ICM4268X_DT_ACCEL_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga018b11db318c78827ac5ddb1d28354bf)
- [ICM42686_DT_ACCEL_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga07bd4b377204b75acbc34ebad27ed19e)
- [ICM4268X_DT_ACCEL_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga9c1b503304efbecd6e43998cd76fca3f)
- [ICM42686_DT_ACCEL_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf0101542510ee1dcfda88709d426cbaf)
- [ICM4268X_DT_ACCEL_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga0318e0340cb82663ddc779c5928163ca)
- [ICM42686_DT_ACCEL_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gafb5acfc89e580cec600bfe3cad20c8a2)
- [ICM4268X_DT_ACCEL_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gadd58206e7413d43fb5d132116a7a5365)
- [ICM42686_DT_ACCEL_ODR_6_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2d5d7996d2a99293759a1eef2f1bae4b)
- [ICM4268X_DT_ACCEL_ODR_6_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gad20d9cfa5bb90c7a165abf9f7ab3664f)
- [ICM42686_DT_ACCEL_ODR_3_125](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gace7b5b17fce265c174c9db2fe19c4520)
- [ICM4268X_DT_ACCEL_ODR_3_125](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3e1a90cbb6580992ed201ecb0b5345d0)
- [ICM42686_DT_ACCEL_ODR_1_5625](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga6fb220853ef49be013ff6d475e14a17d)
- [ICM4268X_DT_ACCEL_ODR_1_5625](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gab37631e21578afd1de24eaefc49d5aa6)
- [ICM42686_DT_ACCEL_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga7de3aee656da50ad36340f8757510723)
- [ICM4268X_DT_ACCEL_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga19a61dfae5899d0839cffb16194e60e8)
- [ICM42686_DT_GYRO_ODR_32000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga1909f71adf7d0deb04842e2d569acf1b)
- [ICM4268X_DT_GYRO_ODR_32000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8cef750fe17171662da932b0123027ff)
- [ICM42686_DT_GYRO_ODR_16000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gabf0897e9a07625890ed8f75dbb88ca9e)
- [ICM4268X_DT_GYRO_ODR_16000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga8a1915f4ec22be71d0460b5e4b104f18)
- [ICM42686_DT_GYRO_ODR_8000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga406b26d9ad6b0a2db6ced76844efdb39)
- [ICM4268X_DT_GYRO_ODR_8000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaaea9abea12bd6fbfb5336d9cb523dd82)
- [ICM42686_DT_GYRO_ODR_4000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga3f922bb1d6a2c0f1e8cf3430d46ad4ac)
- [ICM4268X_DT_GYRO_ODR_4000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga21d6c35ee4059840fe1a1f6e5b53f50a)
- [ICM42686_DT_GYRO_ODR_2000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gaf237aa46d8900fbbbc915a9f994a9a4e)
- [ICM4268X_DT_GYRO_ODR_2000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga81483ad0a4a847460af6e3b34cde489e)
- [ICM42686_DT_GYRO_ODR_1000](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gada5ca8e905c61e5b9d5ad31c38f04bb5)
- [ICM4268X_DT_GYRO_ODR_1000](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga5d5738a58c499b1bb8853471ec3d357e)
- [ICM42686_DT_GYRO_ODR_200](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#gae72fc8d11696187690b188f9ab32a81e)
- [ICM4268X_DT_GYRO_ODR_200](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga37ed7fc033b31067f5331734e98ac906)
- [ICM42686_DT_GYRO_ODR_100](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga80dddd00891d085232f71476b25f3d34)
- [ICM4268X_DT_GYRO_ODR_100](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#gaf79aa174e89c3c22128bd298cfab3805)
- [ICM42686_DT_GYRO_ODR_50](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga14fe9aaaa2b784fde911348ecda0b2f9)
- [ICM4268X_DT_GYRO_ODR_50](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga7d1438b46e72745204b0b37c57e57cf5)
- [ICM42686_DT_GYRO_ODR_25](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga09b72d55bd41fa776c911aa87ff009dc)
- [ICM4268X_DT_GYRO_ODR_25](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga3788cbbf8b8e7ccded755ab52a5abe53)
- [ICM42686_DT_GYRO_ODR_12_5](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga86309657f593e3cb695817f18f9c1e2d)
- [ICM4268X_DT_GYRO_ODR_12_5](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga319a7710d327b82b39cee2a9d2348702)
- [ICM42686_DT_GYRO_ODR_500](https://docs.zephyrproject.org/latest/doxygen/html/group__icm42686__interface.html#ga2205a9906948b3dc6a131bd20ca93f42)
- [ICM4268X_DT_GYRO_ODR_500](../api_transport_control_topic_reference/P008_ICM4268X API主题.md#ga638d6c4de6d0eea72a31a14bdf18df01)

<a id="header-details"></a>

---

[上一章](P015_zephyr__bluetooth__mesh__health_cli.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__dt-bindings__sensor__icm42688.h_文件参考.md)
