---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-14
title: LSM6DSV80X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv80x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_LSM6DSV80X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv80x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSV80X 双加速度计与陀螺仪惯性测量单元（Dual accelerometer and gyroscope IMU）。

<a id="details"></a>

意法半导体（STMicroelectronics）的 LSM6DSV80X 双加速度计与陀螺仪惯性测量单元（IMU）。本系列共用输出数据率（Output Data Rate）和先进先出（FIFO）设置；参见 LSM6DSVXXX。

<a id="header-files"></a>
<a id="files"></a>

## 14.1\_文件（Files）

<a id="r_lsm6dsv80x_2Eh"></a>

```c
file lsm6dsv80x.h
```

相关声明：[lsm6dsv80x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv80x_8h.html)。

the ST LSM6DSV80X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 14.2\_高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_gae5107fc0abbb4d3644bdc08f265e2dfb"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_OFF 0x0
```

相关声明：[LSM6DSV80X_HG_XL_ODR_OFF](#gae5107fc0abbb4d3644bdc08f265e2dfb)。

掉电（Power-down）。

<a id="r_gae2b7bb3e0a118742cf43d1a861b5c0e2"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_480Hz](#gae2b7bb3e0a118742cf43d1a861b5c0e2)。

480 Hz（赫兹）。

<a id="r_ga275f58c9c06a555d083f39dc27d59b97"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_960Hz](#ga275f58c9c06a555d083f39dc27d59b97)。

960 Hz（赫兹）。

<a id="r_ga835ced437617127ae14b7c66c78b3c29"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_1920Hz](#ga835ced437617127ae14b7c66c78b3c29)。

1920 Hz（赫兹）。

<a id="r_ga27c15d3e87430c3c5ec4c41faace32d4"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_3840Hz](#ga27c15d3e87430c3c5ec4c41faace32d4)。

3840 Hz（赫兹）。

<a id="r_ga9a996de027e4a6ba62913014ec58e146"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_7680Hz](#ga9a996de027e4a6ba62913014ec58e146)。

7680 Hz（赫兹）。

## 14.3\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gaf39b6edd5b404e3fab2fa3d9ddd9a676"></a>

```c
#define LSM6DSV80X_DT_FS_2G 2
```

相关声明：[LSM6DSV80X_DT_FS_2G](#gaf39b6edd5b404e3fab2fa3d9ddd9a676)。

量程（range）：±2 g。

<a id="r_ga36db2fc1b95af74e9c37b73f817c62fa"></a>

```c
#define LSM6DSV80X_DT_FS_4G 4
```

相关声明：[LSM6DSV80X_DT_FS_4G](#ga36db2fc1b95af74e9c37b73f817c62fa)。

量程（range）：±4 g。

<a id="r_ga75fd8443f9c9ee7858a7aef2dd76ad1a"></a>

```c
#define LSM6DSV80X_DT_FS_8G 8
```

相关声明：[LSM6DSV80X_DT_FS_8G](#ga75fd8443f9c9ee7858a7aef2dd76ad1a)。

量程（range）：±8 g。

<a id="r_ga37b357c8db6e24871dfad8927d940b90"></a>

```c
#define LSM6DSV80X_DT_FS_16G 16
```

相关声明：[LSM6DSV80X_DT_FS_16G](#ga37b357c8db6e24871dfad8927d940b90)。

量程（range）：±16 g。

<a id="r_ga15f009fd0c94ca2e0981a113c5937da6"></a>

```c
#define LSM6DSV80X_DT_FS_32G 32
```

相关声明：[LSM6DSV80X_DT_FS_32G](#ga15f009fd0c94ca2e0981a113c5937da6)。

量程（range）：±32 g。

<a id="r_gac786fcbc53064b5fb0b82d506dded6d0"></a>

```c
#define LSM6DSV80X_DT_FS_64G 64
```

相关声明：[LSM6DSV80X_DT_FS_64G](#gac786fcbc53064b5fb0b82d506dded6d0)。

±64 g（重力加速度单位）。

<a id="r_gad7af9a9dd7d2482ebebb1ea883873d6d"></a>

```c
#define LSM6DSV80X_DT_FS_80G 80
```

相关声明：[LSM6DSV80X_DT_FS_80G](#gad7af9a9dd7d2482ebebb1ea883873d6d)。

±80 g（重力加速度单位）。

## 14.4\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaf12fda3698938071f33e2eb8935b260d"></a>

```c
#define LSM6DSV80X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV80X_DT_FS_250DPS](#gaf12fda3698938071f33e2eb8935b260d)。

角速度量程：±250 度／秒（dps）。

<a id="r_gaccabb277c647d6dadd1e11a23d24dd80"></a>

```c
#define LSM6DSV80X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV80X_DT_FS_500DPS](#gaccabb277c647d6dadd1e11a23d24dd80)。

角速度量程：±500 度／秒（dps）。

<a id="r_gaa665aee5c06bd5edb49b5b0e2b3d577a"></a>

```c
#define LSM6DSV80X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV80X_DT_FS_1000DPS](#gaa665aee5c06bd5edb49b5b0e2b3d577a)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga05179e45cd95551113792e6d0da881a6"></a>

```c
#define LSM6DSV80X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV80X_DT_FS_2000DPS](#ga05179e45cd95551113792e6d0da881a6)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaaf7e240788e89a68d497799fce6cf4f1"></a>

```c
#define LSM6DSV80X_DT_FS_4000DPS 0x5
```

相关声明：[LSM6DSV80X_DT_FS_4000DPS](#gaaf7e240788e89a68d497799fce6cf4f1)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

## 14.5\_详细说明（Detailed Documentation）

<a id="gaa665aee5c06bd5edb49b5b0e2b3d577a"></a>

### `LSM6DSV80X_DT_FS_1000DPS`

```c
#define LSM6DSV80X_DT_FS_1000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="ga37b357c8db6e24871dfad8927d940b90"></a>

### `LSM6DSV80X_DT_FS_16G`

```c
#define LSM6DSV80X_DT_FS_16G 16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

量程（range）：±16 g。

<a id="ga05179e45cd95551113792e6d0da881a6"></a>

### `LSM6DSV80X_DT_FS_2000DPS`

```c
#define LSM6DSV80X_DT_FS_2000DPS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="gaf12fda3698938071f33e2eb8935b260d"></a>

### `LSM6DSV80X_DT_FS_250DPS`

```c
#define LSM6DSV80X_DT_FS_250DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

角速度量程：±250 度／秒（dps）。

<a id="gaf39b6edd5b404e3fab2fa3d9ddd9a676"></a>

### `LSM6DSV80X_DT_FS_2G`

```c
#define LSM6DSV80X_DT_FS_2G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

量程（range）：±2 g。

<a id="ga15f009fd0c94ca2e0981a113c5937da6"></a>

### `LSM6DSV80X_DT_FS_32G`

```c
#define LSM6DSV80X_DT_FS_32G 32
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

量程（range）：±32 g。

<a id="gaaf7e240788e89a68d497799fce6cf4f1"></a>

### `LSM6DSV80X_DT_FS_4000DPS`

```c
#define LSM6DSV80X_DT_FS_4000DPS 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="ga36db2fc1b95af74e9c37b73f817c62fa"></a>

### `LSM6DSV80X_DT_FS_4G`

```c
#define LSM6DSV80X_DT_FS_4G 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

量程（range）：±4 g。

<a id="gaccabb277c647d6dadd1e11a23d24dd80"></a>

### `LSM6DSV80X_DT_FS_500DPS`

```c
#define LSM6DSV80X_DT_FS_500DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

角速度量程：±500 度／秒（dps）。

<a id="gac786fcbc53064b5fb0b82d506dded6d0"></a>

### `LSM6DSV80X_DT_FS_64G`

```c
#define LSM6DSV80X_DT_FS_64G 64
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

±64 g（重力加速度单位）。

<a id="gad7af9a9dd7d2482ebebb1ea883873d6d"></a>

### `LSM6DSV80X_DT_FS_80G`

```c
#define LSM6DSV80X_DT_FS_80G 80
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

±80 g（重力加速度单位）。

<a id="ga75fd8443f9c9ee7858a7aef2dd76ad1a"></a>

### `LSM6DSV80X_DT_FS_8G`

```c
#define LSM6DSV80X_DT_FS_8G 8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

量程（range）：±8 g。

<a id="ga835ced437617127ae14b7c66c78b3c29"></a>

### `LSM6DSV80X_HG_XL_ODR_AT_1920Hz`

```c
#define LSM6DSV80X_HG_XL_ODR_AT_1920Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

1920 Hz（赫兹）。

<a id="ga27c15d3e87430c3c5ec4c41faace32d4"></a>

### `LSM6DSV80X_HG_XL_ODR_AT_3840Hz`

```c
#define LSM6DSV80X_HG_XL_ODR_AT_3840Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

3840 Hz（赫兹）。

<a id="gae2b7bb3e0a118742cf43d1a861b5c0e2"></a>

### `LSM6DSV80X_HG_XL_ODR_AT_480Hz`

```c
#define LSM6DSV80X_HG_XL_ODR_AT_480Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

480 Hz（赫兹）。

<a id="ga9a996de027e4a6ba62913014ec58e146"></a>

### `LSM6DSV80X_HG_XL_ODR_AT_7680Hz`

```c
#define LSM6DSV80X_HG_XL_ODR_AT_7680Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

7680 Hz（赫兹）。

<a id="ga275f58c9c06a555d083f39dc27d59b97"></a>

### `LSM6DSV80X_HG_XL_ODR_AT_960Hz`

```c
#define LSM6DSV80X_HG_XL_ODR_AT_960Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

960 Hz（赫兹）。

<a id="gae5107fc0abbb4d3644bdc08f265e2dfb"></a>

### `LSM6DSV80X_HG_XL_ODR_OFF`

```c
#define LSM6DSV80X_HG_XL_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv80x.h>
```

掉电（Power-down）。


## 14.6\_原页交叉引用（Cross References）

- [lsm6dsv80x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv80x_8h.html)
- [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P013_LSM6DSV320X API主题.md) · [返回大纲](大纲.md) · [下一章](P015_向量加法（Vector Addition）.md)
