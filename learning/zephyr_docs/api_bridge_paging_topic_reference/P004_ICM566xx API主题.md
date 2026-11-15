---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-4
title: ICM566xx API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__icm566xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_ICM566xx API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__icm566xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TDK InvenSense ICM566xx 六轴惯性测量单元（IMU）。

<a id="details"></a>

TDK InvenSense ICM566xx 六轴惯性测量单元（IMU）。

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_icm566xx_2Eh"></a>

```c
file icm566xx.h
```

相关声明：[icm566xx.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm566xx_8h.html)。

the TDK InvenSense ICM566xx IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 4.2\_加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_gaf5d0235fd419733537fa4cd32821668a"></a>

```c
#define ICM566XX_DT_ACCEL_OFF 0
```

相关声明：[ICM566XX_DT_ACCEL_OFF](#gaf5d0235fd419733537fa4cd32821668a)。

已断电（Powered Down）。

<a id="r_ga50279b4a7eeaec5d322943b50f53e878"></a>

```c
#define ICM566XX_DT_ACCEL_LP 2
```

相关声明：[ICM566XX_DT_ACCEL_LP](#ga50279b4a7eeaec5d322943b50f53e878)。

低功耗模式（Low-power Mode）。

<a id="r_gad40b63ce1173c77ffc35727509efc392"></a>

```c
#define ICM566XX_DT_ACCEL_LN 3
```

相关声明：[ICM566XX_DT_ACCEL_LN](#gad40b63ce1173c77ffc35727509efc392)。

低噪声模式（Low-noise Mode）。

## 4.3\_陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_gaf354f134ca8bf7334b5d684af51100b6"></a>

```c
#define ICM566XX_DT_GYRO_OFF 0
```

相关声明：[ICM566XX_DT_GYRO_OFF](#gaf354f134ca8bf7334b5d684af51100b6)。

已断电（Powered Down）。

<a id="r_ga10f0cdd8f05e3ccd85871b312e870802"></a>

```c
#define ICM566XX_DT_GYRO_STANDBY 1
```

相关声明：[ICM566XX_DT_GYRO_STANDBY](#ga10f0cdd8f05e3ccd85871b312e870802)。

待机（Standby）。

<a id="r_gad4496a59e2a10ad508501d4636a47b19"></a>

```c
#define ICM566XX_DT_GYRO_LP 2
```

相关声明：[ICM566XX_DT_GYRO_LP](#gad4496a59e2a10ad508501d4636a47b19)。

低功耗模式（Low-power Mode）。

<a id="r_gabab45d06bfe9e25ac299c3216f75af0f"></a>

```c
#define ICM566XX_DT_GYRO_LN 3
```

相关声明：[ICM566XX_DT_GYRO_LN](#gabab45d06bfe9e25ac299c3216f75af0f)。

低噪声模式（Low-noise Mode）。

## 4.4\_加速度计量程选项（Accelerometer Scale Options）

设备树属性（Devicetree Property）`accel-fs` 的取值。

<a id="r_ga437a0d53e9b7152a22b6b6b279223479"></a>

```c
#define ICM566XX_DT_ACCEL_FS_32 0
```

相关声明：[ICM566XX_DT_ACCEL_FS_32](#ga437a0d53e9b7152a22b6b6b279223479)。

满量程（Full Scale）：32g。

<a id="r_ga66550f154521e76da491004eb7979451"></a>

```c
#define ICM566XX_DT_ACCEL_FS_16 1
```

相关声明：[ICM566XX_DT_ACCEL_FS_16](#ga66550f154521e76da491004eb7979451)。

满量程（Full Scale）：16g。

<a id="r_ga79be3f79bd227c62e0b8f3e13804378e"></a>

```c
#define ICM566XX_DT_ACCEL_FS_8 2
```

相关声明：[ICM566XX_DT_ACCEL_FS_8](#ga79be3f79bd227c62e0b8f3e13804378e)。

满量程（Full Scale）：8g。

<a id="r_ga4beb14180e50869297f633b004f892a6"></a>

```c
#define ICM566XX_DT_ACCEL_FS_4 3
```

相关声明：[ICM566XX_DT_ACCEL_FS_4](#ga4beb14180e50869297f633b004f892a6)。

满量程（Full Scale）：4g。

<a id="r_ga4f1f08648397f6fd058e586f9f1ea0c9"></a>

```c
#define ICM566XX_DT_ACCEL_FS_2 4
```

相关声明：[ICM566XX_DT_ACCEL_FS_2](#ga4f1f08648397f6fd058e586f9f1ea0c9)。

满量程（Full Scale）：2g。

## 4.5\_陀螺仪量程选项（Gyroscope Scale Options）

设备树属性（Devicetree Property）`gyro-fs` 的取值。

<a id="r_ga4d34d95ee2463dd847bc8fbb848c9f73"></a>

```c
#define ICM566XX_DT_GYRO_FS_4000 0
```

相关声明：[ICM566XX_DT_GYRO_FS_4000](#ga4d34d95ee2463dd847bc8fbb848c9f73)。

满量程（Full Scale）：4000 dps（度／秒）。

<a id="r_ga29836f13c0174d77fdcb725949425e1a"></a>

```c
#define ICM566XX_DT_GYRO_FS_2000 1
```

相关声明：[ICM566XX_DT_GYRO_FS_2000](#ga29836f13c0174d77fdcb725949425e1a)。

满量程（Full Scale）：2000 dps（度／秒）。

<a id="r_ga2b3614b2be6aa85c0566d85781043134"></a>

```c
#define ICM566XX_DT_GYRO_FS_1000 2
```

相关声明：[ICM566XX_DT_GYRO_FS_1000](#ga2b3614b2be6aa85c0566d85781043134)。

满量程（Full Scale）：1000 dps（度／秒）。

<a id="r_ga275d6bdae7765c7d4ffc7b5f0af9a311"></a>

```c
#define ICM566XX_DT_GYRO_FS_500 3
```

相关声明：[ICM566XX_DT_GYRO_FS_500](#ga275d6bdae7765c7d4ffc7b5f0af9a311)。

满量程（Full Scale）：500 dps（度／秒）。

<a id="r_ga74d6dca05eca7c92f2fed67e4262c3a9"></a>

```c
#define ICM566XX_DT_GYRO_FS_250 4
```

相关声明：[ICM566XX_DT_GYRO_FS_250](#ga74d6dca05eca7c92f2fed67e4262c3a9)。

满量程（Full Scale）：250 dps（度／秒）。

<a id="r_gaeb125d4a19491276bc0a45e3622abe0d"></a>

```c
#define ICM566XX_DT_GYRO_FS_125 5
```

相关声明：[ICM566XX_DT_GYRO_FS_125](#gaeb125d4a19491276bc0a45e3622abe0d)。

满量程（Full Scale）：125 dps（度／秒）。

<a id="r_gac15ced8fda07377fbc3b2ad9087831e9"></a>

```c
#define ICM566XX_DT_GYRO_FS_62_5 6
```

相关声明：[ICM566XX_DT_GYRO_FS_62_5](#gac15ced8fda07377fbc3b2ad9087831e9)。

满量程（Full Scale）：62.5 dps（度／秒）。

<a id="r_ga3660b0393736f7b448158307c71b6048"></a>

```c
#define ICM566XX_DT_GYRO_FS_31_25 7
```

相关声明：[ICM566XX_DT_GYRO_FS_31_25](#ga3660b0393736f7b448158307c71b6048)。

满量程（Full Scale）：31.25 dps（度／秒）。

<a id="r_ga3764916c304e3783cd4e00e8123f33f8"></a>

```c
#define ICM566XX_DT_GYRO_FS_15_625 8
```

相关声明：[ICM566XX_DT_GYRO_FS_15_625](#ga3764916c304e3783cd4e00e8123f33f8)。

满量程（Full Scale）：15.625 dps（度／秒）。

## 4.6\_加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga6b7b33acf93a7070231640473e0b276e"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_6400 3
```

相关声明：[ICM566XX_DT_ACCEL_ODR_6400](#ga6b7b33acf93a7070231640473e0b276e)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga7b998728b193fa5f49551c3690e493b5"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_3200 4
```

相关声明：[ICM566XX_DT_ACCEL_ODR_3200](#ga7b998728b193fa5f49551c3690e493b5)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga0908a03f35c371a087f6615f43b843c0"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_1600 5
```

相关声明：[ICM566XX_DT_ACCEL_ODR_1600](#ga0908a03f35c371a087f6615f43b843c0)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gadf0a170ebe013b3fc9d30458e33aadad"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_800 6
```

相关声明：[ICM566XX_DT_ACCEL_ODR_800](#gadf0a170ebe013b3fc9d30458e33aadad)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gac1f4fa91d6dfa74c0b3dca304e937292"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_400 7
```

相关声明：[ICM566XX_DT_ACCEL_ODR_400](#gac1f4fa91d6dfa74c0b3dca304e937292)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga92674f1d54dccf72657f71611062fbc9"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_200 8
```

相关声明：[ICM566XX_DT_ACCEL_ODR_200](#ga92674f1d54dccf72657f71611062fbc9)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gace9ce1ce1dd05c226f79890e3c7d5ae4"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_100 9
```

相关声明：[ICM566XX_DT_ACCEL_ODR_100](#gace9ce1ce1dd05c226f79890e3c7d5ae4)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga9d749134dc24267fd52f76538c853807"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_50 10
```

相关声明：[ICM566XX_DT_ACCEL_ODR_50](#ga9d749134dc24267fd52f76538c853807)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga05185f0a0f72368d4cc16dcfafce0c96"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_25 11
```

相关声明：[ICM566XX_DT_ACCEL_ODR_25](#ga05185f0a0f72368d4cc16dcfafce0c96)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae37790bc7673e43408ecfd6e82ffd7e7"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_12_5 12
```

相关声明：[ICM566XX_DT_ACCEL_ODR_12_5](#gae37790bc7673e43408ecfd6e82ffd7e7)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gac74bb0ad1420cce3e0a9fd248b2ac051"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_6_25 13
```

相关声明：[ICM566XX_DT_ACCEL_ODR_6_25](#gac74bb0ad1420cce3e0a9fd248b2ac051)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gaf07a780bbdaf741cd5f8ab6a7524b077"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_3_125 14
```

相关声明：[ICM566XX_DT_ACCEL_ODR_3_125](#gaf07a780bbdaf741cd5f8ab6a7524b077)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gabe60143ab3faee9d82c5f0a7cb3fde1e"></a>

```c
#define ICM566XX_DT_ACCEL_ODR_1_5625 15
```

相关声明：[ICM566XX_DT_ACCEL_ODR_1_5625](#gabe60143ab3faee9d82c5f0a7cb3fde1e)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

## 4.7\_陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_gacce1ecb914ab26bfb124092cd03256e2"></a>

```c
#define ICM566XX_DT_GYRO_ODR_6400 3
```

相关声明：[ICM566XX_DT_GYRO_ODR_6400](#gacce1ecb914ab26bfb124092cd03256e2)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga72b736f6702a0bf43c49554da2ec8a85"></a>

```c
#define ICM566XX_DT_GYRO_ODR_3200 4
```

相关声明：[ICM566XX_DT_GYRO_ODR_3200](#ga72b736f6702a0bf43c49554da2ec8a85)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gaa41a39d63f171f74915b7c9be0597f5b"></a>

```c
#define ICM566XX_DT_GYRO_ODR_1600 5
```

相关声明：[ICM566XX_DT_GYRO_ODR_1600](#gaa41a39d63f171f74915b7c9be0597f5b)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gad4ce89d9ef3865bdb4a911a7e3e50972"></a>

```c
#define ICM566XX_DT_GYRO_ODR_800 6
```

相关声明：[ICM566XX_DT_GYRO_ODR_800](#gad4ce89d9ef3865bdb4a911a7e3e50972)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga6192cac91455a1fcf42e56264da8242e"></a>

```c
#define ICM566XX_DT_GYRO_ODR_400 7
```

相关声明：[ICM566XX_DT_GYRO_ODR_400](#ga6192cac91455a1fcf42e56264da8242e)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga461e51c57b053ed4e20d410feea6f5dc"></a>

```c
#define ICM566XX_DT_GYRO_ODR_200 8
```

相关声明：[ICM566XX_DT_GYRO_ODR_200](#ga461e51c57b053ed4e20d410feea6f5dc)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga3513a51121482d74a36c87d1c0b11bcd"></a>

```c
#define ICM566XX_DT_GYRO_ODR_100 9
```

相关声明：[ICM566XX_DT_GYRO_ODR_100](#ga3513a51121482d74a36c87d1c0b11bcd)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae5fd553b7a0cd0caf01115d81def276f"></a>

```c
#define ICM566XX_DT_GYRO_ODR_50 10
```

相关声明：[ICM566XX_DT_GYRO_ODR_50](#gae5fd553b7a0cd0caf01115d81def276f)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gad6183a26c7063792b2309e6afde0d7c4"></a>

```c
#define ICM566XX_DT_GYRO_ODR_25 11
```

相关声明：[ICM566XX_DT_GYRO_ODR_25](#gad6183a26c7063792b2309e6afde0d7c4)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gaf6e7d62c7bf1d70e24456ac695c2dcb7"></a>

```c
#define ICM566XX_DT_GYRO_ODR_12_5 12
```

相关声明：[ICM566XX_DT_GYRO_ODR_12_5](#gaf6e7d62c7bf1d70e24456ac695c2dcb7)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gae2b1c4a2443d401f19672ca6094a31ed"></a>

```c
#define ICM566XX_DT_GYRO_ODR_6_25 13
```

相关声明：[ICM566XX_DT_GYRO_ODR_6_25](#gae2b1c4a2443d401f19672ca6094a31ed)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gae9dcf2919e8451ad9043fb459bddc4f8"></a>

```c
#define ICM566XX_DT_GYRO_ODR_3_125 14
```

相关声明：[ICM566XX_DT_GYRO_ODR_3_125](#gae9dcf2919e8451ad9043fb459bddc4f8)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga72e142db33cb62da147b4e1bb1c4ea92"></a>

```c
#define ICM566XX_DT_GYRO_ODR_1_5625 15
```

相关声明：[ICM566XX_DT_GYRO_ODR_1_5625](#ga72e142db33cb62da147b4e1bb1c4ea92)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

## 4.8\_陀螺仪低通滤波选项（Gyroscope Low-pass Filtering Options）

设备树属性（Devicetree Property）`gyro-lpf-bw` 的取值。

<a id="r_ga8a60df60c5ca01421b98b2b22c97eec2"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_OFF 0
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_OFF](#ga8a60df60c5ca01421b98b2b22c97eec2)。

禁用滤波器（Filter Disabled）。

<a id="r_ga8615f0ddec208b4f7dd3d7c470259015"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_4 1
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_4](#ga8615f0ddec208b4f7dd3d7c470259015)。

输出数据速率（ODR）的 1/4。

<a id="r_ga3dedfa654c08300592eedbc9da5110d8"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_8 2
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_8](#ga3dedfa654c08300592eedbc9da5110d8)。

输出数据速率（ODR）的 1/8。

<a id="r_ga79fba6d40c25ef0f009fdd8c97ca9eb1"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_16 3
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_16](#ga79fba6d40c25ef0f009fdd8c97ca9eb1)。

输出数据速率（ODR）的 1/16。

<a id="r_gac0bc2e1428081e330a7e997335ceafa8"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_32 4
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_32](#gac0bc2e1428081e330a7e997335ceafa8)。

输出数据速率（ODR）的 1/32。

<a id="r_gad4605e71889f0c72f354bdf9cc5f83ae"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_64 5
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_64](#gad4605e71889f0c72f354bdf9cc5f83ae)。

输出数据速率（ODR）的 1/64。

<a id="r_ga0b7cf8c4ef1c3f9f9e1605d32d7373bf"></a>

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_128 6
```

相关声明：[ICM566XX_DT_GYRO_LPF_BW_1_128](#ga0b7cf8c4ef1c3f9f9e1605d32d7373bf)。

输出数据速率（ODR）的 1/128。

## 4.9\_加速度计低通滤波选项（Accelerometer Low-pass Filtering Options）

设备树属性（Devicetree Property）`accel-lpf-bw` 的取值。

<a id="r_ga5d0e59c91ba3c2515058ba0c9d3071a4"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_OFF 0
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_OFF](#ga5d0e59c91ba3c2515058ba0c9d3071a4)。

禁用滤波器（Filter Disabled）。

<a id="r_ga7c52f3003c6c5a12f98cb8232e295b9b"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_4 1
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_4](#ga7c52f3003c6c5a12f98cb8232e295b9b)。

输出数据速率（ODR）的 1/4。

<a id="r_ga61268eed123637b32837b7f7d8d2a689"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_8 2
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_8](#ga61268eed123637b32837b7f7d8d2a689)。

输出数据速率（ODR）的 1/8。

<a id="r_ga78ec7bd9579ebdb72c8ef41497790a51"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_16 3
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_16](#ga78ec7bd9579ebdb72c8ef41497790a51)。

输出数据速率（ODR）的 1/16。

<a id="r_ga5b8be207fd78dc659c42bb33984ff416"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_32 4
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_32](#ga5b8be207fd78dc659c42bb33984ff416)。

输出数据速率（ODR）的 1/32。

<a id="r_ga72b0d7e543db3e8dea630fdc811a7417"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_64 5
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_64](#ga72b0d7e543db3e8dea630fdc811a7417)。

输出数据速率（ODR）的 1/64。

<a id="r_gacfb42d7af5e385f9d29d854132b74924"></a>

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_128 6
```

相关声明：[ICM566XX_DT_ACCEL_LPF_BW_1_128](#gacfb42d7af5e385f9d29d854132b74924)。

输出数据速率（ODR）的 1/128。

## 4.10\_详细说明（Detailed Documentation）

<a id="ga66550f154521e76da491004eb7979451"></a>

### `ICM566XX_DT_ACCEL_FS_16`

```c
#define ICM566XX_DT_ACCEL_FS_16 1
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：16g。

<a id="ga4f1f08648397f6fd058e586f9f1ea0c9"></a>

### `ICM566XX_DT_ACCEL_FS_2`

```c
#define ICM566XX_DT_ACCEL_FS_2 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：2g。

<a id="ga437a0d53e9b7152a22b6b6b279223479"></a>

### `ICM566XX_DT_ACCEL_FS_32`

```c
#define ICM566XX_DT_ACCEL_FS_32 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：32g。

<a id="ga4beb14180e50869297f633b004f892a6"></a>

### `ICM566XX_DT_ACCEL_FS_4`

```c
#define ICM566XX_DT_ACCEL_FS_4 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：4g。

<a id="ga79be3f79bd227c62e0b8f3e13804378e"></a>

### `ICM566XX_DT_ACCEL_FS_8`

```c
#define ICM566XX_DT_ACCEL_FS_8 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：8g。

<a id="gad40b63ce1173c77ffc35727509efc392"></a>

### `ICM566XX_DT_ACCEL_LN`

```c
#define ICM566XX_DT_ACCEL_LN 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

低噪声模式（Low-noise Mode）。

<a id="ga50279b4a7eeaec5d322943b50f53e878"></a>

### `ICM566XX_DT_ACCEL_LP`

```c
#define ICM566XX_DT_ACCEL_LP 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

低功耗模式（Low-power Mode）。

<a id="gacfb42d7af5e385f9d29d854132b74924"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_128`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_128 6
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/128。

<a id="ga78ec7bd9579ebdb72c8ef41497790a51"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_16`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_16 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/16。

<a id="ga5b8be207fd78dc659c42bb33984ff416"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_32`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_32 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/32。

<a id="ga7c52f3003c6c5a12f98cb8232e295b9b"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_4`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_4 1
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/4。

<a id="ga72b0d7e543db3e8dea630fdc811a7417"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_64`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_64 5
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/64。

<a id="ga61268eed123637b32837b7f7d8d2a689"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_1_8`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_1_8 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/8。

<a id="ga5d0e59c91ba3c2515058ba0c9d3071a4"></a>

### `ICM566XX_DT_ACCEL_LPF_BW_OFF`

```c
#define ICM566XX_DT_ACCEL_LPF_BW_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

禁用滤波器（Filter Disabled）。

<a id="gace9ce1ce1dd05c226f79890e3c7d5ae4"></a>

### `ICM566XX_DT_ACCEL_ODR_100`

```c
#define ICM566XX_DT_ACCEL_ODR_100 9
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gae37790bc7673e43408ecfd6e82ffd7e7"></a>

### `ICM566XX_DT_ACCEL_ODR_12_5`

```c
#define ICM566XX_DT_ACCEL_ODR_12_5 12
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga0908a03f35c371a087f6615f43b843c0"></a>

### `ICM566XX_DT_ACCEL_ODR_1600`

```c
#define ICM566XX_DT_ACCEL_ODR_1600 5
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="gabe60143ab3faee9d82c5f0a7cb3fde1e"></a>

### `ICM566XX_DT_ACCEL_ODR_1_5625`

```c
#define ICM566XX_DT_ACCEL_ODR_1_5625 15
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="ga92674f1d54dccf72657f71611062fbc9"></a>

### `ICM566XX_DT_ACCEL_ODR_200`

```c
#define ICM566XX_DT_ACCEL_ODR_200 8
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga05185f0a0f72368d4cc16dcfafce0c96"></a>

### `ICM566XX_DT_ACCEL_ODR_25`

```c
#define ICM566XX_DT_ACCEL_ODR_25 11
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga7b998728b193fa5f49551c3690e493b5"></a>

### `ICM566XX_DT_ACCEL_ODR_3200`

```c
#define ICM566XX_DT_ACCEL_ODR_3200 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="gaf07a780bbdaf741cd5f8ab6a7524b077"></a>

### `ICM566XX_DT_ACCEL_ODR_3_125`

```c
#define ICM566XX_DT_ACCEL_ODR_3_125 14
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="gac1f4fa91d6dfa74c0b3dca304e937292"></a>

### `ICM566XX_DT_ACCEL_ODR_400`

```c
#define ICM566XX_DT_ACCEL_ODR_400 7
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga9d749134dc24267fd52f76538c853807"></a>

### `ICM566XX_DT_ACCEL_ODR_50`

```c
#define ICM566XX_DT_ACCEL_ODR_50 10
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga6b7b33acf93a7070231640473e0b276e"></a>

### `ICM566XX_DT_ACCEL_ODR_6400`

```c
#define ICM566XX_DT_ACCEL_ODR_6400 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="gac74bb0ad1420cce3e0a9fd248b2ac051"></a>

### `ICM566XX_DT_ACCEL_ODR_6_25`

```c
#define ICM566XX_DT_ACCEL_ODR_6_25 13
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="gadf0a170ebe013b3fc9d30458e33aadad"></a>

### `ICM566XX_DT_ACCEL_ODR_800`

```c
#define ICM566XX_DT_ACCEL_ODR_800 6
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

800 Hz（仅适用于低噪声（LN）模式）。

<a id="gaf5d0235fd419733537fa4cd32821668a"></a>

### `ICM566XX_DT_ACCEL_OFF`

```c
#define ICM566XX_DT_ACCEL_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

已断电（Powered Down）。

<a id="ga2b3614b2be6aa85c0566d85781043134"></a>

### `ICM566XX_DT_GYRO_FS_1000`

```c
#define ICM566XX_DT_GYRO_FS_1000 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：1000 dps（度／秒）。

<a id="gaeb125d4a19491276bc0a45e3622abe0d"></a>

### `ICM566XX_DT_GYRO_FS_125`

```c
#define ICM566XX_DT_GYRO_FS_125 5
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：125 dps（度／秒）。

<a id="ga3764916c304e3783cd4e00e8123f33f8"></a>

### `ICM566XX_DT_GYRO_FS_15_625`

```c
#define ICM566XX_DT_GYRO_FS_15_625 8
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：15.625 dps（度／秒）。

<a id="ga29836f13c0174d77fdcb725949425e1a"></a>

### `ICM566XX_DT_GYRO_FS_2000`

```c
#define ICM566XX_DT_GYRO_FS_2000 1
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：2000 dps（度／秒）。

<a id="ga74d6dca05eca7c92f2fed67e4262c3a9"></a>

### `ICM566XX_DT_GYRO_FS_250`

```c
#define ICM566XX_DT_GYRO_FS_250 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：250 dps（度／秒）。

<a id="ga3660b0393736f7b448158307c71b6048"></a>

### `ICM566XX_DT_GYRO_FS_31_25`

```c
#define ICM566XX_DT_GYRO_FS_31_25 7
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：31.25 dps（度／秒）。

<a id="ga4d34d95ee2463dd847bc8fbb848c9f73"></a>

### `ICM566XX_DT_GYRO_FS_4000`

```c
#define ICM566XX_DT_GYRO_FS_4000 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：4000 dps（度／秒）。

<a id="ga275d6bdae7765c7d4ffc7b5f0af9a311"></a>

### `ICM566XX_DT_GYRO_FS_500`

```c
#define ICM566XX_DT_GYRO_FS_500 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：500 dps（度／秒）。

<a id="gac15ced8fda07377fbc3b2ad9087831e9"></a>

### `ICM566XX_DT_GYRO_FS_62_5`

```c
#define ICM566XX_DT_GYRO_FS_62_5 6
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

满量程（Full Scale）：62.5 dps（度／秒）。

<a id="gabab45d06bfe9e25ac299c3216f75af0f"></a>

### `ICM566XX_DT_GYRO_LN`

```c
#define ICM566XX_DT_GYRO_LN 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

低噪声模式（Low-noise Mode）。

<a id="gad4496a59e2a10ad508501d4636a47b19"></a>

### `ICM566XX_DT_GYRO_LP`

```c
#define ICM566XX_DT_GYRO_LP 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

低功耗模式（Low-power Mode）。

<a id="ga0b7cf8c4ef1c3f9f9e1605d32d7373bf"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_128`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_128 6
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/128。

<a id="ga79fba6d40c25ef0f009fdd8c97ca9eb1"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_16`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_16 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/16。

<a id="gac0bc2e1428081e330a7e997335ceafa8"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_32`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_32 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/32。

<a id="ga8615f0ddec208b4f7dd3d7c470259015"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_4`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_4 1
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/4。

<a id="gad4605e71889f0c72f354bdf9cc5f83ae"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_64`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_64 5
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/64。

<a id="ga3dedfa654c08300592eedbc9da5110d8"></a>

### `ICM566XX_DT_GYRO_LPF_BW_1_8`

```c
#define ICM566XX_DT_GYRO_LPF_BW_1_8 2
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

输出数据速率（ODR）的 1/8。

<a id="ga8a60df60c5ca01421b98b2b22c97eec2"></a>

### `ICM566XX_DT_GYRO_LPF_BW_OFF`

```c
#define ICM566XX_DT_GYRO_LPF_BW_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

禁用滤波器（Filter Disabled）。

<a id="ga3513a51121482d74a36c87d1c0b11bcd"></a>

### `ICM566XX_DT_GYRO_ODR_100`

```c
#define ICM566XX_DT_GYRO_ODR_100 9
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gaf6e7d62c7bf1d70e24456ac695c2dcb7"></a>

### `ICM566XX_DT_GYRO_ODR_12_5`

```c
#define ICM566XX_DT_GYRO_ODR_12_5 12
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gaa41a39d63f171f74915b7c9be0597f5b"></a>

### `ICM566XX_DT_GYRO_ODR_1600`

```c
#define ICM566XX_DT_GYRO_ODR_1600 5
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="ga72e142db33cb62da147b4e1bb1c4ea92"></a>

### `ICM566XX_DT_GYRO_ODR_1_5625`

```c
#define ICM566XX_DT_GYRO_ODR_1_5625 15
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="ga461e51c57b053ed4e20d410feea6f5dc"></a>

### `ICM566XX_DT_GYRO_ODR_200`

```c
#define ICM566XX_DT_GYRO_ODR_200 8
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gad6183a26c7063792b2309e6afde0d7c4"></a>

### `ICM566XX_DT_GYRO_ODR_25`

```c
#define ICM566XX_DT_GYRO_ODR_25 11
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="ga72b736f6702a0bf43c49554da2ec8a85"></a>

### `ICM566XX_DT_GYRO_ODR_3200`

```c
#define ICM566XX_DT_GYRO_ODR_3200 4
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="gae9dcf2919e8451ad9043fb459bddc4f8"></a>

### `ICM566XX_DT_GYRO_ODR_3_125`

```c
#define ICM566XX_DT_GYRO_ODR_3_125 14
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="ga6192cac91455a1fcf42e56264da8242e"></a>

### `ICM566XX_DT_GYRO_ODR_400`

```c
#define ICM566XX_DT_GYRO_ODR_400 7
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gae5fd553b7a0cd0caf01115d81def276f"></a>

### `ICM566XX_DT_GYRO_ODR_50`

```c
#define ICM566XX_DT_GYRO_ODR_50 10
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="gacce1ecb914ab26bfb124092cd03256e2"></a>

### `ICM566XX_DT_GYRO_ODR_6400`

```c
#define ICM566XX_DT_GYRO_ODR_6400 3
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="gae2b1c4a2443d401f19672ca6094a31ed"></a>

### `ICM566XX_DT_GYRO_ODR_6_25`

```c
#define ICM566XX_DT_GYRO_ODR_6_25 13
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="gad4ce89d9ef3865bdb4a911a7e3e50972"></a>

### `ICM566XX_DT_GYRO_ODR_800`

```c
#define ICM566XX_DT_GYRO_ODR_800 6
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

800 Hz（仅适用于低噪声（LN）模式）。

<a id="gaf354f134ca8bf7334b5d684af51100b6"></a>

### `ICM566XX_DT_GYRO_OFF`

```c
#define ICM566XX_DT_GYRO_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

已断电（Powered Down）。

<a id="ga10f0cdd8f05e3ccd85871b312e870802"></a>

### `ICM566XX_DT_GYRO_STANDBY`

```c
#define ICM566XX_DT_GYRO_STANDBY 1
```

```c
#include <zephyr/dt-bindings/sensor/icm566xx.h>
```

待机（Standby）。


## 4.11\_原页交叉引用（Cross References）

- [icm566xx.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2icm566xx_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_GNSS 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P005_IIS2DLPC API主题.md)
