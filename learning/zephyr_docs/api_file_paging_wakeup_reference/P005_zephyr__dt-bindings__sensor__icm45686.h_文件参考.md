---
id: learning.zephyr-docs.api-file-paging-wakeup-reference.page-5
title: zephyr__dt-bindings__sensor__icm45686.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icm45686_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_sensor\_\_icm45686.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/icm45686_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the TDK InvenSense ICM45686 IMU的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the TDK InvenSense ICM45686 IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pwr-mode` 的取值。

<a id="r_ga8b33a42ca2ee186c644481a20681599d"></a>

```c
#define ICM45686_DT_ACCEL_OFF 0
```

相关声明：[ICM45686_DT_ACCEL_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga8b33a42ca2ee186c644481a20681599d)。

已断电（Powered Down）。

<a id="r_gab87a06cbd382b4d3b781cb3d00907fa9"></a>

```c
#define ICM45686_DT_ACCEL_LP 2
```

相关声明：[ICM45686_DT_ACCEL_LP](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab87a06cbd382b4d3b781cb3d00907fa9)。

低功耗模式（Low-power Mode）。

<a id="r_gaaef05bb2b940ce73d5afaf28ce14d9ce"></a>

```c
#define ICM45686_DT_ACCEL_LN 3
```

相关声明：[ICM45686_DT_ACCEL_LN](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaaef05bb2b940ce73d5afaf28ce14d9ce)。

低噪声模式（Low-noise Mode）。

<a id="define-members-1"></a>

### 陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pwr-mode` 的取值。

<a id="r_gade7adbaae8ac2eba67a8fa3f97ef0415"></a>

```c
#define ICM45686_DT_GYRO_OFF 0
```

相关声明：[ICM45686_DT_GYRO_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gade7adbaae8ac2eba67a8fa3f97ef0415)。

已断电（Powered Down）。

<a id="r_gadae95f6a41154f1984da037fb83258d5"></a>

```c
#define ICM45686_DT_GYRO_STANDBY 1
```

相关声明：[ICM45686_DT_GYRO_STANDBY](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gadae95f6a41154f1984da037fb83258d5)。

待机（Standby）。

<a id="r_gaee3b6201bb6d391c52f62d7b81e12fbc"></a>

```c
#define ICM45686_DT_GYRO_LP 2
```

相关声明：[ICM45686_DT_GYRO_LP](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaee3b6201bb6d391c52f62d7b81e12fbc)。

低功耗模式（Low-power Mode）。

<a id="r_gaa3cce06238e725b6aabe749cb9a9b0d4"></a>

```c
#define ICM45686_DT_GYRO_LN 3
```

相关声明：[ICM45686_DT_GYRO_LN](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa3cce06238e725b6aabe749cb9a9b0d4)。

低噪声模式（Low-noise Mode）。

<a id="define-members-2"></a>

### 加速度计满量程范围选项（Accelerometer Full-scale Range Options）

设备树属性（Devicetree Property）`accel-fs` 的取值。

<a id="r_gaf790544808b65f948d0b53cb0de7cb54"></a>

```c
#define ICM45686_DT_ACCEL_FS_32 0
```

相关声明：[ICM45686_DT_ACCEL_FS_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaf790544808b65f948d0b53cb0de7cb54)。

量程（range）：±32 g。

<a id="r_ga7690e5863f8437e6e30e8dd26f5d3dc1"></a>

```c
#define ICM45686_DT_ACCEL_FS_16 1
```

相关声明：[ICM45686_DT_ACCEL_FS_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7690e5863f8437e6e30e8dd26f5d3dc1)。

量程（range）：±16 g。

<a id="r_ga1f2974e42fb6af6e2f94eeefaad8fdc2"></a>

```c
#define ICM45686_DT_ACCEL_FS_8 2
```

相关声明：[ICM45686_DT_ACCEL_FS_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga1f2974e42fb6af6e2f94eeefaad8fdc2)。

量程（range）：±8 g。

<a id="r_ga5349fe55ec137b9eddb2e37454321486"></a>

```c
#define ICM45686_DT_ACCEL_FS_4 3
```

相关声明：[ICM45686_DT_ACCEL_FS_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5349fe55ec137b9eddb2e37454321486)。

量程（range）：±4 g。

<a id="r_gad37d83f116fde8bb5ba419e8db209ad1"></a>

```c
#define ICM45686_DT_ACCEL_FS_2 4
```

相关声明：[ICM45686_DT_ACCEL_FS_2](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gad37d83f116fde8bb5ba419e8db209ad1)。

量程（range）：±2 g。

<a id="define-members-3"></a>

### 陀螺仪满量程范围选项（Gyroscope Full-scale Range Options）

设备树属性（Devicetree Property）`gyro-fs` 的取值。

<a id="r_ga02e33c717d16c4f6e8ad39f41098a368"></a>

```c
#define ICM45686_DT_GYRO_FS_4000 0
```

相关声明：[ICM45686_DT_GYRO_FS_4000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga02e33c717d16c4f6e8ad39f41098a368)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="r_ga7eada42888012443169b722b68590e30"></a>

```c
#define ICM45686_DT_GYRO_FS_2000 1
```

相关声明：[ICM45686_DT_GYRO_FS_2000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7eada42888012443169b722b68590e30)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga573e9a7c2517f47690a2bb57fa02e9e4"></a>

```c
#define ICM45686_DT_GYRO_FS_1000 2
```

相关声明：[ICM45686_DT_GYRO_FS_1000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga573e9a7c2517f47690a2bb57fa02e9e4)。

角速度量程：±1000 度／秒（dps）。

<a id="r_gacd9c8c364e136f66e0dac901f5a8d470"></a>

```c
#define ICM45686_DT_GYRO_FS_500 3
```

相关声明：[ICM45686_DT_GYRO_FS_500](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gacd9c8c364e136f66e0dac901f5a8d470)。

角速度量程：±500 度／秒（dps）。

<a id="r_gadc7a6ca2050179c0049f03797988d3e3"></a>

```c
#define ICM45686_DT_GYRO_FS_250 4
```

相关声明：[ICM45686_DT_GYRO_FS_250](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gadc7a6ca2050179c0049f03797988d3e3)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga9cc1fe4f1738e8695c7e7e6fa7df44e9"></a>

```c
#define ICM45686_DT_GYRO_FS_125 5
```

相关声明：[ICM45686_DT_GYRO_FS_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9cc1fe4f1738e8695c7e7e6fa7df44e9)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga27956d51388dea37fd9f1d8e4ca286b6"></a>

```c
#define ICM45686_DT_GYRO_FS_62_5 6
```

相关声明：[ICM45686_DT_GYRO_FS_62_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga27956d51388dea37fd9f1d8e4ca286b6)。

±62.5 度每秒（dps）。

<a id="r_ga2dfe38c6ebef4b45f95b9383450b6799"></a>

```c
#define ICM45686_DT_GYRO_FS_31_25 7
```

相关声明：[ICM45686_DT_GYRO_FS_31_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga2dfe38c6ebef4b45f95b9383450b6799)。

±31.25 度每秒（dps）。

<a id="r_gaef81e5104573864864de5781692df31d"></a>

```c
#define ICM45686_DT_GYRO_FS_15_625 8
```

相关声明：[ICM45686_DT_GYRO_FS_15_625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaef81e5104573864864de5781692df31d)。

±15.625 度每秒（dps）。

<a id="define-members-4"></a>

### 加速度计数据速率选项（Accelerometer Data Rate Options）

设备树（Devicetree）属性 `accel-odr` 的取值。

<a id="r_ga60693a4e030bca38e742735cd082a46e"></a>

```c
#define ICM45686_DT_ACCEL_ODR_6400 3
```

相关声明：[ICM45686_DT_ACCEL_ODR_6400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga60693a4e030bca38e742735cd082a46e)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gaf91570280567f8b094c10d665b32cdf8"></a>

```c
#define ICM45686_DT_ACCEL_ODR_3200 4
```

相关声明：[ICM45686_DT_ACCEL_ODR_3200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaf91570280567f8b094c10d665b32cdf8)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gab22b9e6b25a80b5629536cb3014e1582"></a>

```c
#define ICM45686_DT_ACCEL_ODR_1600 5
```

相关声明：[ICM45686_DT_ACCEL_ODR_1600](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab22b9e6b25a80b5629536cb3014e1582)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga3ff3f2111a8ab2f4420aa31db8813da4"></a>

```c
#define ICM45686_DT_ACCEL_ODR_800 6
```

相关声明：[ICM45686_DT_ACCEL_ODR_800](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga3ff3f2111a8ab2f4420aa31db8813da4)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga7cb0cad42bb0eda5a694b195f49868b5"></a>

```c
#define ICM45686_DT_ACCEL_ODR_400 7
```

相关声明：[ICM45686_DT_ACCEL_ODR_400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7cb0cad42bb0eda5a694b195f49868b5)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga856edda34709d32f3c4e2738005cb263"></a>

```c
#define ICM45686_DT_ACCEL_ODR_200 8
```

相关声明：[ICM45686_DT_ACCEL_ODR_200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga856edda34709d32f3c4e2738005cb263)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga54053977b70e2d369661f4de0614a512"></a>

```c
#define ICM45686_DT_ACCEL_ODR_100 9
```

相关声明：[ICM45686_DT_ACCEL_ODR_100](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga54053977b70e2d369661f4de0614a512)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga5d5dc91e2993a0ec533e4e332740ada2"></a>

```c
#define ICM45686_DT_ACCEL_ODR_50 10
```

相关声明：[ICM45686_DT_ACCEL_ODR_50](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5d5dc91e2993a0ec533e4e332740ada2)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gab319d91b31ac5b09248d30042391c3ff"></a>

```c
#define ICM45686_DT_ACCEL_ODR_25 11
```

相关声明：[ICM45686_DT_ACCEL_ODR_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab319d91b31ac5b09248d30042391c3ff)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga6c83ccbef5b5cb0dd6bf10eaa6ab5dc4"></a>

```c
#define ICM45686_DT_ACCEL_ODR_12_5 12
```

相关声明：[ICM45686_DT_ACCEL_ODR_12_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga6c83ccbef5b5cb0dd6bf10eaa6ab5dc4)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gafd818ea53188619aab8e8b53c82bed75"></a>

```c
#define ICM45686_DT_ACCEL_ODR_6_25 13
```

相关声明：[ICM45686_DT_ACCEL_ODR_6_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gafd818ea53188619aab8e8b53c82bed75)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_gaeded0acef70490aaa122a54456c39c80"></a>

```c
#define ICM45686_DT_ACCEL_ODR_3_125 14
```

相关声明：[ICM45686_DT_ACCEL_ODR_3_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaeded0acef70490aaa122a54456c39c80)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga7fc1f9759a6b6ab9c287491f33673f5a"></a>

```c
#define ICM45686_DT_ACCEL_ODR_1_5625 15
```

相关声明：[ICM45686_DT_ACCEL_ODR_1_5625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7fc1f9759a6b6ab9c287491f33673f5a)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="define-members-5"></a>

### 陀螺仪数据速率选项（Gyroscope Data Rate Options）

设备树属性（Devicetree Property）`gyro-odr` 的取值。

<a id="r_gab5eb26c981fbb104d368ef57371d8a7c"></a>

```c
#define ICM45686_DT_GYRO_ODR_6400 3
```

相关声明：[ICM45686_DT_GYRO_ODR_6400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab5eb26c981fbb104d368ef57371d8a7c)。

6400 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gab53b400f63aa733b790340a96b322885"></a>

```c
#define ICM45686_DT_GYRO_ODR_3200 4
```

相关声明：[ICM45686_DT_GYRO_ODR_3200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab53b400f63aa733b790340a96b322885)。

3200 Hz（仅适用于低噪声（LN）模式）。

<a id="r_gaa85269312c7a548aabe9f0da4ff2acac"></a>

```c
#define ICM45686_DT_GYRO_ODR_1600 5
```

相关声明：[ICM45686_DT_GYRO_ODR_1600](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa85269312c7a548aabe9f0da4ff2acac)。

1600 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga1ac6b40e0b5416a31d08e7433c9228bd"></a>

```c
#define ICM45686_DT_GYRO_ODR_800 6
```

相关声明：[ICM45686_DT_GYRO_ODR_800](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga1ac6b40e0b5416a31d08e7433c9228bd)。

800 Hz（仅适用于低噪声（LN）模式）。

<a id="r_ga4364e0123afc4afde78a4a04b690ab16"></a>

```c
#define ICM45686_DT_GYRO_ODR_400 7
```

相关声明：[ICM45686_DT_GYRO_ODR_400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga4364e0123afc4afde78a4a04b690ab16)。

400 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga79941259cc7ba89409b57a9d0f955881"></a>

```c
#define ICM45686_DT_GYRO_ODR_200 8
```

相关声明：[ICM45686_DT_GYRO_ODR_200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga79941259cc7ba89409b57a9d0f955881)。

200 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gac0ed04fd24cccd6145629d9f967c7e1c"></a>

```c
#define ICM45686_DT_GYRO_ODR_100 9
```

相关声明：[ICM45686_DT_GYRO_ODR_100](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gac0ed04fd24cccd6145629d9f967c7e1c)。

100 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gafd69abea1b6667ce91ad0aa0cfd35ea7"></a>

```c
#define ICM45686_DT_GYRO_ODR_50 10
```

相关声明：[ICM45686_DT_GYRO_ODR_50](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gafd69abea1b6667ce91ad0aa0cfd35ea7)。

50 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_gada0b64962561d0978a4d7eca1c953cf9"></a>

```c
#define ICM45686_DT_GYRO_ODR_25 11
```

相关声明：[ICM45686_DT_GYRO_ODR_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gada0b64962561d0978a4d7eca1c953cf9)。

25 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga73f72b58714ea8ee5f16da67c19acebe"></a>

```c
#define ICM45686_DT_GYRO_ODR_12_5 12
```

相关声明：[ICM45686_DT_GYRO_ODR_12_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga73f72b58714ea8ee5f16da67c19acebe)。

12.5 Hz（适用于低噪声（LN）或低功耗（LP）模式）。

<a id="r_ga80f01d68efff04a831d99f34cc7c4095"></a>

```c
#define ICM45686_DT_GYRO_ODR_6_25 13
```

相关声明：[ICM45686_DT_GYRO_ODR_6_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga80f01d68efff04a831d99f34cc7c4095)。

6.25 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga2e10d8ad52d7635f550d2ae99f522d58"></a>

```c
#define ICM45686_DT_GYRO_ODR_3_125 14
```

相关声明：[ICM45686_DT_GYRO_ODR_3_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga2e10d8ad52d7635f550d2ae99f522d58)。

3.125 Hz（仅适用于低功耗（LP）模式）。

<a id="r_ga416e6c246e18be3321d4070b10d704ff"></a>

```c
#define ICM45686_DT_GYRO_ODR_1_5625 15
```

相关声明：[ICM45686_DT_GYRO_ODR_1_5625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga416e6c246e18be3321d4070b10d704ff)。

1.5625 Hz（仅适用于低功耗（LP）模式）。

<a id="define-members-6"></a>

### 陀螺仪低通滤波器选项（Gyroscope Low-pass Filter Options）

设备树属性（Devicetree Property）`gyro-lpf` 的取值。

带宽（Bandwidth）表示为所选输出数据速率（Output Data Rate）的一部分。

<a id="r_ga3e7966cdb32e1bf4b45284bdaa019aff"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_OFF 0
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga3e7966cdb32e1bf4b45284bdaa019aff)。

禁用滤波器（Filter Disabled）。

<a id="r_ga824b5b245825766b8e3e55337b563e00"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_4 1
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga824b5b245825766b8e3e55337b563e00)。

输出数据速率（ODR）除以 4。

<a id="r_gaa6ab971581b350d6e39aafaeb2eb9224"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_8 2
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa6ab971581b350d6e39aafaeb2eb9224)。

输出数据速率（ODR）除以 8。

<a id="r_ga768aee240c0e30484ee2c51cd906bb32"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_16 3
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga768aee240c0e30484ee2c51cd906bb32)。

输出数据速率（ODR）除以 16。

<a id="r_ga214dbae4eba8b982d3a64cffeaab5e74"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_32 4
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga214dbae4eba8b982d3a64cffeaab5e74)。

输出数据速率（ODR）除以 32。

<a id="r_gaea4539a5b53911d62defcfda36321802"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_64 5
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_64](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaea4539a5b53911d62defcfda36321802)。

输出数据速率（ODR）除以 64。

<a id="r_gabb75aef9c5b0f814b6437c245837958a"></a>

```c
#define ICM45686_DT_GYRO_LPF_BW_1_128 6
```

相关声明：[ICM45686_DT_GYRO_LPF_BW_1_128](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gabb75aef9c5b0f814b6437c245837958a)。

输出数据速率（ODR）除以 128。

<a id="define-members-7"></a>

### 加速度计低通滤波器选项（Accelerometer Low-pass Filter Options）

设备树属性（Devicetree Property）`accel-lpf` 的取值。

带宽（Bandwidth）表示为所选输出数据速率（Output Data Rate）的一部分。

<a id="r_ga5cd6f0bdb7bbe7c1bb2f9e894b503d32"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_OFF 0
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5cd6f0bdb7bbe7c1bb2f9e894b503d32)。

禁用滤波器（Filter Disabled）。

<a id="r_gae1b58c4126f0270b4a29d3411bca8933"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_4 1
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gae1b58c4126f0270b4a29d3411bca8933)。

输出数据速率（ODR）除以 4。

<a id="r_ga9fb18995a51d3d3367d4daf289e63c85"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_8 2
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9fb18995a51d3d3367d4daf289e63c85)。

输出数据速率（ODR）除以 8。

<a id="r_gae9411f41d66488dca5b7309c33b1413c"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_16 3
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gae9411f41d66488dca5b7309c33b1413c)。

输出数据速率（ODR）除以 16。

<a id="r_ga48b322615cc68ce56944aaac54def755"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_32 4
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga48b322615cc68ce56944aaac54def755)。

输出数据速率（ODR）除以 32。

<a id="r_ga5e82ec391e86aeb1296b4ffae9401fac"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_64 5
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_64](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5e82ec391e86aeb1296b4ffae9401fac)。

输出数据速率（ODR）除以 64。

<a id="r_ga9473e299e65b1fe23e4dd987aae3554e"></a>

```c
#define ICM45686_DT_ACCEL_LPF_BW_1_128 6
```

相关声明：[ICM45686_DT_ACCEL_LPF_BW_1_128](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9473e299e65b1fe23e4dd987aae3554e)。

输出数据速率（ODR）除以 128。


## 5.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P336_icm45686.h_源码浏览.md)
- [ICM45686_DT_ACCEL_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga8b33a42ca2ee186c644481a20681599d)
- [ICM45686_DT_ACCEL_LP](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab87a06cbd382b4d3b781cb3d00907fa9)
- [ICM45686_DT_ACCEL_LN](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaaef05bb2b940ce73d5afaf28ce14d9ce)
- [ICM45686_DT_GYRO_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gade7adbaae8ac2eba67a8fa3f97ef0415)
- [ICM45686_DT_GYRO_STANDBY](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gadae95f6a41154f1984da037fb83258d5)
- [ICM45686_DT_GYRO_LP](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaee3b6201bb6d391c52f62d7b81e12fbc)
- [ICM45686_DT_GYRO_LN](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa3cce06238e725b6aabe749cb9a9b0d4)
- [ICM45686_DT_ACCEL_FS_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaf790544808b65f948d0b53cb0de7cb54)
- [ICM45686_DT_ACCEL_FS_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7690e5863f8437e6e30e8dd26f5d3dc1)
- [ICM45686_DT_ACCEL_FS_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga1f2974e42fb6af6e2f94eeefaad8fdc2)
- [ICM45686_DT_ACCEL_FS_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5349fe55ec137b9eddb2e37454321486)
- [ICM45686_DT_ACCEL_FS_2](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gad37d83f116fde8bb5ba419e8db209ad1)
- [ICM45686_DT_GYRO_FS_4000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga02e33c717d16c4f6e8ad39f41098a368)
- [ICM45686_DT_GYRO_FS_2000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7eada42888012443169b722b68590e30)
- [ICM45686_DT_GYRO_FS_1000](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga573e9a7c2517f47690a2bb57fa02e9e4)
- [ICM45686_DT_GYRO_FS_500](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gacd9c8c364e136f66e0dac901f5a8d470)
- [ICM45686_DT_GYRO_FS_250](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gadc7a6ca2050179c0049f03797988d3e3)
- [ICM45686_DT_GYRO_FS_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9cc1fe4f1738e8695c7e7e6fa7df44e9)
- [ICM45686_DT_GYRO_FS_62_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga27956d51388dea37fd9f1d8e4ca286b6)
- [ICM45686_DT_GYRO_FS_31_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga2dfe38c6ebef4b45f95b9383450b6799)
- [ICM45686_DT_GYRO_FS_15_625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaef81e5104573864864de5781692df31d)
- [ICM45686_DT_ACCEL_ODR_6400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga60693a4e030bca38e742735cd082a46e)
- [ICM45686_DT_ACCEL_ODR_3200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaf91570280567f8b094c10d665b32cdf8)
- [ICM45686_DT_ACCEL_ODR_1600](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab22b9e6b25a80b5629536cb3014e1582)
- [ICM45686_DT_ACCEL_ODR_800](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga3ff3f2111a8ab2f4420aa31db8813da4)
- [ICM45686_DT_ACCEL_ODR_400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7cb0cad42bb0eda5a694b195f49868b5)
- [ICM45686_DT_ACCEL_ODR_200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga856edda34709d32f3c4e2738005cb263)
- [ICM45686_DT_ACCEL_ODR_100](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga54053977b70e2d369661f4de0614a512)
- [ICM45686_DT_ACCEL_ODR_50](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5d5dc91e2993a0ec533e4e332740ada2)
- [ICM45686_DT_ACCEL_ODR_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab319d91b31ac5b09248d30042391c3ff)
- [ICM45686_DT_ACCEL_ODR_12_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga6c83ccbef5b5cb0dd6bf10eaa6ab5dc4)
- [ICM45686_DT_ACCEL_ODR_6_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gafd818ea53188619aab8e8b53c82bed75)
- [ICM45686_DT_ACCEL_ODR_3_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaeded0acef70490aaa122a54456c39c80)
- [ICM45686_DT_ACCEL_ODR_1_5625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga7fc1f9759a6b6ab9c287491f33673f5a)
- [ICM45686_DT_GYRO_ODR_6400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab5eb26c981fbb104d368ef57371d8a7c)
- [ICM45686_DT_GYRO_ODR_3200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gab53b400f63aa733b790340a96b322885)
- [ICM45686_DT_GYRO_ODR_1600](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa85269312c7a548aabe9f0da4ff2acac)
- [ICM45686_DT_GYRO_ODR_800](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga1ac6b40e0b5416a31d08e7433c9228bd)
- [ICM45686_DT_GYRO_ODR_400](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga4364e0123afc4afde78a4a04b690ab16)
- [ICM45686_DT_GYRO_ODR_200](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga79941259cc7ba89409b57a9d0f955881)
- [ICM45686_DT_GYRO_ODR_100](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gac0ed04fd24cccd6145629d9f967c7e1c)
- [ICM45686_DT_GYRO_ODR_50](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gafd69abea1b6667ce91ad0aa0cfd35ea7)
- [ICM45686_DT_GYRO_ODR_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gada0b64962561d0978a4d7eca1c953cf9)
- [ICM45686_DT_GYRO_ODR_12_5](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga73f72b58714ea8ee5f16da67c19acebe)
- [ICM45686_DT_GYRO_ODR_6_25](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga80f01d68efff04a831d99f34cc7c4095)
- [ICM45686_DT_GYRO_ODR_3_125](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga2e10d8ad52d7635f550d2ae99f522d58)
- [ICM45686_DT_GYRO_ODR_1_5625](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga416e6c246e18be3321d4070b10d704ff)
- [ICM45686_DT_GYRO_LPF_BW_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga3e7966cdb32e1bf4b45284bdaa019aff)
- [ICM45686_DT_GYRO_LPF_BW_1_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga824b5b245825766b8e3e55337b563e00)
- [ICM45686_DT_GYRO_LPF_BW_1_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaa6ab971581b350d6e39aafaeb2eb9224)
- [ICM45686_DT_GYRO_LPF_BW_1_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga768aee240c0e30484ee2c51cd906bb32)
- [ICM45686_DT_GYRO_LPF_BW_1_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga214dbae4eba8b982d3a64cffeaab5e74)
- [ICM45686_DT_GYRO_LPF_BW_1_64](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gaea4539a5b53911d62defcfda36321802)
- [ICM45686_DT_GYRO_LPF_BW_1_128](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gabb75aef9c5b0f814b6437c245837958a)
- [ICM45686_DT_ACCEL_LPF_BW_OFF](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5cd6f0bdb7bbe7c1bb2f9e894b503d32)
- [ICM45686_DT_ACCEL_LPF_BW_1_4](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gae1b58c4126f0270b4a29d3411bca8933)
- [ICM45686_DT_ACCEL_LPF_BW_1_8](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9fb18995a51d3d3367d4daf289e63c85)
- [ICM45686_DT_ACCEL_LPF_BW_1_16](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#gae9411f41d66488dca5b7309c33b1413c)
- [ICM45686_DT_ACCEL_LPF_BW_1_32](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga48b322615cc68ce56944aaac54def755)
- [ICM45686_DT_ACCEL_LPF_BW_1_64](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga5e82ec391e86aeb1296b4ffae9401fac)
- [ICM45686_DT_ACCEL_LPF_BW_1_128](../api_input_runtime_topic_reference/P008_ICM45686 API主题.md#ga9473e299e65b1fe23e4dd987aae3554e)

<a id="header-details"></a>

---

[上一章](P004_zephyr__dt-bindings__sensor__afbr_s50.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__interrupt_controller__intc_nxp_siul2_eirq.h_文件参考.md)
