---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-11
title: LSM6DSO API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_LSM6DSO API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dso__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSO 六轴惯性测量单元（IMU）。

<a id="details"></a>

STMicroelectronics LSM6DSO 六轴惯性测量单元（IMU）。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_lsm6dso_2Eh"></a>

```c
file lsm6dso.h
```

相关声明：[lsm6dso.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso_8h.html)。

the ST LSM6DSO IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.2\_加速度计电源模式（Accelerometer Power Modes）

设备树属性（Devicetree Property）`accel-pm` 的取值。

<a id="r_gaa62e5d2a5529d005f4d622ecdf97f8f0"></a>

```c
#define LSM6DSO_DT_XL_HP_MODE 0
```

相关声明：[LSM6DSO_DT_XL_HP_MODE](#gaa62e5d2a5529d005f4d622ecdf97f8f0)。

高性能模式（High-performance Mode）。

<a id="r_ga031783c6119db7de6138f368c65c0e49"></a>

```c
#define LSM6DSO_DT_XL_LP_NORMAL_MODE 1
```

相关声明：[LSM6DSO_DT_XL_LP_NORMAL_MODE](#ga031783c6119db7de6138f368c65c0e49)。

低功耗／正常模式（Low-power/Normal Mode）。

<a id="r_gae1fc1b3317d8dac484cc8f094ff453c6"></a>

```c
#define LSM6DSO_DT_XL_ULP_MODE 2
```

相关声明：[LSM6DSO_DT_XL_ULP_MODE](#gae1fc1b3317d8dac484cc8f094ff453c6)。

超低功耗模式（Ultra-low-power Mode）。

## 11.3\_陀螺仪电源模式（Gyroscope Power Modes）

设备树属性（Devicetree Property）`gyro-pm` 的取值。

<a id="r_gac6810407924f44016f0f27c44aca22de"></a>

```c
#define LSM6DSO_DT_GY_HP_MODE 0
```

相关声明：[LSM6DSO_DT_GY_HP_MODE](#gac6810407924f44016f0f27c44aca22de)。

高性能模式（High-performance Mode）。

<a id="r_gaae6bf6b52db6321cba323a06af6afe4c"></a>

```c
#define LSM6DSO_DT_GY_NORMAL_MODE 1
```

相关声明：[LSM6DSO_DT_GY_NORMAL_MODE](#gaae6bf6b52db6321cba323a06af6afe4c)。

正常模式（Normal Mode）。

## 11.4\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga4b6fd691c9843fdce021c027a6c1d38f"></a>

```c
#define LSM6DSO_DT_FS_2G 0
```

相关声明：[LSM6DSO_DT_FS_2G](#ga4b6fd691c9843fdce021c027a6c1d38f)。

量程（range）：±2 g。

<a id="r_gaab163b8d605a6433aff9af2c4fb31764"></a>

```c
#define LSM6DSO_DT_FS_16G 1
```

相关声明：[LSM6DSO_DT_FS_16G](#gaab163b8d605a6433aff9af2c4fb31764)。

量程（range）：±16 g。

<a id="r_gac6b3e663efb2aa9340480a0a955b97d7"></a>

```c
#define LSM6DSO_DT_FS_4G 2
```

相关声明：[LSM6DSO_DT_FS_4G](#gac6b3e663efb2aa9340480a0a955b97d7)。

量程（range）：±4 g。

<a id="r_gad2f86d00fa1665c011296fa27b4a235c"></a>

```c
#define LSM6DSO_DT_FS_8G 3
```

相关声明：[LSM6DSO_DT_FS_8G](#gad2f86d00fa1665c011296fa27b4a235c)。

量程（range）：±8 g。

## 11.5\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga3754f6339351a7d1be2b98fab8b88102"></a>

```c
#define LSM6DSO_DT_FS_250DPS 0
```

相关声明：[LSM6DSO_DT_FS_250DPS](#ga3754f6339351a7d1be2b98fab8b88102)。

角速度量程：±250 度／秒（dps）。

<a id="r_gae427e045d161c9f90eff4c6e5dee4efe"></a>

```c
#define LSM6DSO_DT_FS_125DPS 1
```

相关声明：[LSM6DSO_DT_FS_125DPS](#gae427e045d161c9f90eff4c6e5dee4efe)。

角速度量程：±125 度／秒（dps）。

<a id="r_ga0edc66177f1cb810257fe8e3460586a4"></a>

```c
#define LSM6DSO_DT_FS_500DPS 2
```

相关声明：[LSM6DSO_DT_FS_500DPS](#ga0edc66177f1cb810257fe8e3460586a4)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga862e3383ea2a6db7fea154fe7b5e5f58"></a>

```c
#define LSM6DSO_DT_FS_1000DPS 4
```

相关声明：[LSM6DSO_DT_FS_1000DPS](#ga862e3383ea2a6db7fea154fe7b5e5f58)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga5f007e2d998b5eda7c5fd08145665e4e"></a>

```c
#define LSM6DSO_DT_FS_2000DPS 6
```

相关声明：[LSM6DSO_DT_FS_2000DPS](#ga5f007e2d998b5eda7c5fd08145665e4e)。

角速度量程：±2000 度／秒（dps）。

## 11.6\_加速度计与陀螺仪输出数据率（Accelerometer and Gyroscope Output Data Rate）

设备树（Devicetree）属性 `accel-odr` 和 `gyro-odr` 的取值。

<a id="r_ga8969b4f07c618f652bf4b15de9d0b5f7"></a>

```c
#define LSM6DSO_DT_ODR_OFF 0x0
```

相关声明：[LSM6DSO_DT_ODR_OFF](#ga8969b4f07c618f652bf4b15de9d0b5f7)。

掉电（Power-down）。

<a id="r_ga9f0952fa1854848632b30b59e8145f08"></a>

```c
#define LSM6DSO_DT_ODR_12Hz5 0x1
```

相关声明：[LSM6DSO_DT_ODR_12Hz5](#ga9f0952fa1854848632b30b59e8145f08)。

频率：12.5 Hz。

<a id="r_gab8cc4ee8854e45071720c6e97cb9a133"></a>

```c
#define LSM6DSO_DT_ODR_26H 0x2
```

相关声明：[LSM6DSO_DT_ODR_26H](#gab8cc4ee8854e45071720c6e97cb9a133)。

频率：26 Hz。

<a id="r_gab172e908c0810d7a57cad2ccd70626b1"></a>

```c
#define LSM6DSO_DT_ODR_52Hz 0x3
```

相关声明：[LSM6DSO_DT_ODR_52Hz](#gab172e908c0810d7a57cad2ccd70626b1)。

频率：52 Hz。

<a id="r_ga59b98b9f338fd9cf2d568b14ac5a5410"></a>

```c
#define LSM6DSO_DT_ODR_104Hz 0x4
```

相关声明：[LSM6DSO_DT_ODR_104Hz](#ga59b98b9f338fd9cf2d568b14ac5a5410)。

频率：104 Hz。

<a id="r_gaf57d5e0ecb4fba8230d4a69390a4857c"></a>

```c
#define LSM6DSO_DT_ODR_208Hz 0x5
```

相关声明：[LSM6DSO_DT_ODR_208Hz](#gaf57d5e0ecb4fba8230d4a69390a4857c)。

频率：208 Hz。

<a id="r_gaeb374d527698dc50af30a2469957da6f"></a>

```c
#define LSM6DSO_DT_ODR_417Hz 0x6
```

相关声明：[LSM6DSO_DT_ODR_417Hz](#gaeb374d527698dc50af30a2469957da6f)。

频率（Frequency）：417 Hz。

<a id="r_ga2cb2a2d726eee22c6e5457700a966c9a"></a>

```c
#define LSM6DSO_DT_ODR_833Hz 0x7
```

相关声明：[LSM6DSO_DT_ODR_833Hz](#ga2cb2a2d726eee22c6e5457700a966c9a)。

频率：833 Hz。

<a id="r_ga41f7e1ee6c74cd37b707382ccda3474b"></a>

```c
#define LSM6DSO_DT_ODR_1667Hz 0x8
```

相关声明：[LSM6DSO_DT_ODR_1667Hz](#ga41f7e1ee6c74cd37b707382ccda3474b)。

频率（Frequency）：1667 Hz。

<a id="r_gab66ab364d747f4b95f68c596effeb143"></a>

```c
#define LSM6DSO_DT_ODR_3333Hz 0x9
```

相关声明：[LSM6DSO_DT_ODR_3333Hz](#gab66ab364d747f4b95f68c596effeb143)。

频率（Frequency）：3333 Hz。

<a id="r_ga73b782f5504622e185d60d635397620a"></a>

```c
#define LSM6DSO_DT_ODR_6667Hz 0xa
```

相关声明：[LSM6DSO_DT_ODR_6667Hz](#ga73b782f5504622e185d60d635397620a)。

6667 Hz（赫兹）。

<a id="r_ga14963a4bd7e78ba44eb33da3eaa950af"></a>

```c
#define LSM6DSO_DT_ODR_1Hz6 0xb
```

相关声明：[LSM6DSO_DT_ODR_1Hz6](#ga14963a4bd7e78ba44eb33da3eaa950af)。

1.6 Hz，低功耗（Low-power）模式。

## 11.7\_低通滤波器分频选项（Low-pass Filter Divider Options）

设备树属性（Devicetree Property）`accel-lp-filter` 的取值。

<a id="r_ga4981c36e44bf1aa45bf05ab9b356117e"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_2 0
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_2](#ga4981c36e44bf1aa45bf05ab9b356117e)。

输出数据速率（ODR）除以 2。

<a id="r_gab17d663d64d484ce04ac5c934e6d269a"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_10 1
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_10](#gab17d663d64d484ce04ac5c934e6d269a)。

输出数据速率（ODR）除以 10。

<a id="r_gab57ddcf22ff9ae72a92b245c0fecc025"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_20 2
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_20](#gab57ddcf22ff9ae72a92b245c0fecc025)。

输出数据速率（ODR）除以 20。

<a id="r_gaecd1f9c4b8e9ef0f98169f275b8ee98c"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_45 3
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_45](#gaecd1f9c4b8e9ef0f98169f275b8ee98c)。

输出数据速率（ODR）除以 45。

<a id="r_ga8cffd21429574fa53f5817affb3620a6"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_100 4
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_100](#ga8cffd21429574fa53f5817affb3620a6)。

输出数据速率（ODR）除以 100。

<a id="r_gaa200437c6db2aba3f4385bca36d2107c"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_200 5
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_200](#gaa200437c6db2aba3f4385bca36d2107c)。

输出数据速率（ODR）除以 200。

<a id="r_ga33f69cb9156a657b46a88d5b34dfbd52"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_400 6
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_400](#ga33f69cb9156a657b46a88d5b34dfbd52)。

输出数据速率（ODR）除以 400。

<a id="r_ga6799d36f05d459ebdb2fc51fa368bdb2"></a>

```c
#define LSM6DSO_DT_LP_ODR_DIV_800 7
```

相关声明：[LSM6DSO_DT_LP_ODR_DIV_800](#ga6799d36f05d459ebdb2fc51fa368bdb2)。

输出数据速率（ODR）除以 800。

## 11.8\_敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_gade7b8d0e5cf3f46ccee6133919af35df"></a>

```c
#define LSM6DSO_DT_SINGLE_TAP 0
```

相关声明：[LSM6DSO_DT_SINGLE_TAP](#gade7b8d0e5cf3f46ccee6133919af35df)。

仅单击（Single-tap Only）。

<a id="r_ga7ad4099bd82ffa09ce63eeaa79490941"></a>

```c
#define LSM6DSO_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[LSM6DSO_DT_SINGLE_DOUBLE_TAP](#ga7ad4099bd82ffa09ce63eeaa79490941)。

单击与双击（Single and Double Tap）。

## 11.9\_详细说明（Detailed Documentation）

<a id="ga862e3383ea2a6db7fea154fe7b5e5f58"></a>

### `LSM6DSO_DT_FS_1000DPS`

```c
#define LSM6DSO_DT_FS_1000DPS 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="gae427e045d161c9f90eff4c6e5dee4efe"></a>

### `LSM6DSO_DT_FS_125DPS`

```c
#define LSM6DSO_DT_FS_125DPS 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

角速度量程：±125 度／秒（dps）。

<a id="gaab163b8d605a6433aff9af2c4fb31764"></a>

### `LSM6DSO_DT_FS_16G`

```c
#define LSM6DSO_DT_FS_16G 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

量程（range）：±16 g。

<a id="ga5f007e2d998b5eda7c5fd08145665e4e"></a>

### `LSM6DSO_DT_FS_2000DPS`

```c
#define LSM6DSO_DT_FS_2000DPS 6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga3754f6339351a7d1be2b98fab8b88102"></a>

### `LSM6DSO_DT_FS_250DPS`

```c
#define LSM6DSO_DT_FS_250DPS 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

角速度量程：±250 度／秒（dps）。

<a id="ga4b6fd691c9843fdce021c027a6c1d38f"></a>

### `LSM6DSO_DT_FS_2G`

```c
#define LSM6DSO_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

量程（range）：±2 g。

<a id="gac6b3e663efb2aa9340480a0a955b97d7"></a>

### `LSM6DSO_DT_FS_4G`

```c
#define LSM6DSO_DT_FS_4G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

量程（range）：±4 g。

<a id="ga0edc66177f1cb810257fe8e3460586a4"></a>

### `LSM6DSO_DT_FS_500DPS`

```c
#define LSM6DSO_DT_FS_500DPS 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

角速度量程：±500 度／秒（dps）。

<a id="gad2f86d00fa1665c011296fa27b4a235c"></a>

### `LSM6DSO_DT_FS_8G`

```c
#define LSM6DSO_DT_FS_8G 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

量程（range）：±8 g。

<a id="gac6810407924f44016f0f27c44aca22de"></a>

### `LSM6DSO_DT_GY_HP_MODE`

```c
#define LSM6DSO_DT_GY_HP_MODE 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

高性能模式（High-performance Mode）。

<a id="gaae6bf6b52db6321cba323a06af6afe4c"></a>

### `LSM6DSO_DT_GY_NORMAL_MODE`

```c
#define LSM6DSO_DT_GY_NORMAL_MODE 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

正常模式（Normal Mode）。

<a id="gab17d663d64d484ce04ac5c934e6d269a"></a>

### `LSM6DSO_DT_LP_ODR_DIV_10`

```c
#define LSM6DSO_DT_LP_ODR_DIV_10 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 10。

<a id="ga8cffd21429574fa53f5817affb3620a6"></a>

### `LSM6DSO_DT_LP_ODR_DIV_100`

```c
#define LSM6DSO_DT_LP_ODR_DIV_100 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 100。

<a id="ga4981c36e44bf1aa45bf05ab9b356117e"></a>

### `LSM6DSO_DT_LP_ODR_DIV_2`

```c
#define LSM6DSO_DT_LP_ODR_DIV_2 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 2。

<a id="gab57ddcf22ff9ae72a92b245c0fecc025"></a>

### `LSM6DSO_DT_LP_ODR_DIV_20`

```c
#define LSM6DSO_DT_LP_ODR_DIV_20 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 20。

<a id="gaa200437c6db2aba3f4385bca36d2107c"></a>

### `LSM6DSO_DT_LP_ODR_DIV_200`

```c
#define LSM6DSO_DT_LP_ODR_DIV_200 5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 200。

<a id="ga33f69cb9156a657b46a88d5b34dfbd52"></a>

### `LSM6DSO_DT_LP_ODR_DIV_400`

```c
#define LSM6DSO_DT_LP_ODR_DIV_400 6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 400。

<a id="gaecd1f9c4b8e9ef0f98169f275b8ee98c"></a>

### `LSM6DSO_DT_LP_ODR_DIV_45`

```c
#define LSM6DSO_DT_LP_ODR_DIV_45 3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 45。

<a id="ga6799d36f05d459ebdb2fc51fa368bdb2"></a>

### `LSM6DSO_DT_LP_ODR_DIV_800`

```c
#define LSM6DSO_DT_LP_ODR_DIV_800 7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

输出数据速率（ODR）除以 800。

<a id="ga59b98b9f338fd9cf2d568b14ac5a5410"></a>

### `LSM6DSO_DT_ODR_104Hz`

```c
#define LSM6DSO_DT_ODR_104Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：104 Hz。

<a id="ga9f0952fa1854848632b30b59e8145f08"></a>

### `LSM6DSO_DT_ODR_12Hz5`

```c
#define LSM6DSO_DT_ODR_12Hz5 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：12.5 Hz。

<a id="ga41f7e1ee6c74cd37b707382ccda3474b"></a>

### `LSM6DSO_DT_ODR_1667Hz`

```c
#define LSM6DSO_DT_ODR_1667Hz 0x8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率（Frequency）：1667 Hz。

<a id="ga14963a4bd7e78ba44eb33da3eaa950af"></a>

### `LSM6DSO_DT_ODR_1Hz6`

```c
#define LSM6DSO_DT_ODR_1Hz6 0xb
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

1.6 Hz，低功耗（Low-power）模式。

<a id="gaf57d5e0ecb4fba8230d4a69390a4857c"></a>

### `LSM6DSO_DT_ODR_208Hz`

```c
#define LSM6DSO_DT_ODR_208Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：208 Hz。

<a id="gab8cc4ee8854e45071720c6e97cb9a133"></a>

### `LSM6DSO_DT_ODR_26H`

```c
#define LSM6DSO_DT_ODR_26H 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：26 Hz。

<a id="gab66ab364d747f4b95f68c596effeb143"></a>

### `LSM6DSO_DT_ODR_3333Hz`

```c
#define LSM6DSO_DT_ODR_3333Hz 0x9
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率（Frequency）：3333 Hz。

<a id="gaeb374d527698dc50af30a2469957da6f"></a>

### `LSM6DSO_DT_ODR_417Hz`

```c
#define LSM6DSO_DT_ODR_417Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率（Frequency）：417 Hz。

<a id="gab172e908c0810d7a57cad2ccd70626b1"></a>

### `LSM6DSO_DT_ODR_52Hz`

```c
#define LSM6DSO_DT_ODR_52Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：52 Hz。

<a id="ga73b782f5504622e185d60d635397620a"></a>

### `LSM6DSO_DT_ODR_6667Hz`

```c
#define LSM6DSO_DT_ODR_6667Hz 0xa
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

6667 Hz（赫兹）。

<a id="ga2cb2a2d726eee22c6e5457700a966c9a"></a>

### `LSM6DSO_DT_ODR_833Hz`

```c
#define LSM6DSO_DT_ODR_833Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

频率：833 Hz。

<a id="ga8969b4f07c618f652bf4b15de9d0b5f7"></a>

### `LSM6DSO_DT_ODR_OFF`

```c
#define LSM6DSO_DT_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

掉电（Power-down）。

<a id="ga7ad4099bd82ffa09ce63eeaa79490941"></a>

### `LSM6DSO_DT_SINGLE_DOUBLE_TAP`

```c
#define LSM6DSO_DT_SINGLE_DOUBLE_TAP 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

单击与双击（Single and Double Tap）。

<a id="gade7b8d0e5cf3f46ccee6133919af35df"></a>

### `LSM6DSO_DT_SINGLE_TAP`

```c
#define LSM6DSO_DT_SINGLE_TAP 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

仅单击（Single-tap Only）。

<a id="gaa62e5d2a5529d005f4d622ecdf97f8f0"></a>

### `LSM6DSO_DT_XL_HP_MODE`

```c
#define LSM6DSO_DT_XL_HP_MODE 0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

高性能模式（High-performance Mode）。

<a id="ga031783c6119db7de6138f368c65c0e49"></a>

### `LSM6DSO_DT_XL_LP_NORMAL_MODE`

```c
#define LSM6DSO_DT_XL_LP_NORMAL_MODE 1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

低功耗／正常模式（Low-power/Normal Mode）。

<a id="gae1fc1b3317d8dac484cc8f094ff453c6"></a>

### `LSM6DSO_DT_XL_ULP_MODE`

```c
#define LSM6DSO_DT_XL_ULP_MODE 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dso.h>
```

超低功耗模式（Ultra-low-power Mode）。


## 11.10\_原页交叉引用（Cross References）

- [lsm6dso.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dso_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010__input_（输入）。.md) · [返回大纲](大纲.md) · [下一章](P012_BBC micro_bit显示（Display）的API。.md)
