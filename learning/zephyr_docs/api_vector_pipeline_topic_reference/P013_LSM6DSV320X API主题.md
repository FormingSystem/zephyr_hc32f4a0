---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-13
title: LSM6DSV320X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv320x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_LSM6DSV320X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsv320x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LSM6DSV320X 双加速度计与陀螺仪惯性测量单元（Dual accelerometer and gyroscope IMU）。

<a id="details"></a>

意法半导体（STMicroelectronics）的 LSM6DSV320X 双加速度计与陀螺仪惯性测量单元（IMU）。本系列共用输出数据率（Output Data Rate）和先进先出（FIFO）设置；参见 LSM6DSVXXX。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_lsm6dsv320x_2Eh"></a>

```c
file lsm6dsv320x.h
```

相关声明：[lsm6dsv320x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html)。

the ST LSM6DSV320X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 13.2\_高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_ga4a630613d01e476125b1a1fa9e894cb8"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_OFF 0x0
```

相关声明：[LSM6DSV320X_HG_XL_ODR_OFF](#ga4a630613d01e476125b1a1fa9e894cb8)。

掉电（Power-down）。

<a id="r_gaa3000f771aa3ef89e3b786fdd9055742"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_480Hz](#gaa3000f771aa3ef89e3b786fdd9055742)。

480 Hz（赫兹）。

<a id="r_gaf09aa8484b2ab208933a5a0e25c6de10"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_960Hz](#gaf09aa8484b2ab208933a5a0e25c6de10)。

960 Hz（赫兹）。

<a id="r_ga2d718e3e593c7cc8a4ac31584d410be8"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_1920Hz](#ga2d718e3e593c7cc8a4ac31584d410be8)。

1920 Hz（赫兹）。

<a id="r_ga001b8a3d4c95c156ea89ad0187f92468"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_3840Hz](#ga001b8a3d4c95c156ea89ad0187f92468)。

3840 Hz（赫兹）。

<a id="r_gaf536c506da4d13aa17e8388134180ce4"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_7680Hz](#gaf536c506da4d13aa17e8388134180ce4)。

7680 Hz（赫兹）。

## 13.3\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga2e586abbca79ddaf5f697396d8102a3a"></a>

```c
#define LSM6DSV320X_DT_FS_2G 2
```

相关声明：[LSM6DSV320X_DT_FS_2G](#ga2e586abbca79ddaf5f697396d8102a3a)。

量程（range）：±2 g。

<a id="r_gaba78d3c3569c44528a970ac6e5c99413"></a>

```c
#define LSM6DSV320X_DT_FS_4G 4
```

相关声明：[LSM6DSV320X_DT_FS_4G](#gaba78d3c3569c44528a970ac6e5c99413)。

量程（range）：±4 g。

<a id="r_ga91952d45d6a3020b79ae6a79027d5728"></a>

```c
#define LSM6DSV320X_DT_FS_8G 8
```

相关声明：[LSM6DSV320X_DT_FS_8G](#ga91952d45d6a3020b79ae6a79027d5728)。

量程（range）：±8 g。

<a id="r_gabb2c1de34e3a5a2e9ee777420d1c1744"></a>

```c
#define LSM6DSV320X_DT_FS_16G 16
```

相关声明：[LSM6DSV320X_DT_FS_16G](#gabb2c1de34e3a5a2e9ee777420d1c1744)。

量程（range）：±16 g。

<a id="r_gaf3f87288e27f4e99f9820790fc47887d"></a>

```c
#define LSM6DSV320X_DT_FS_32G 32
```

相关声明：[LSM6DSV320X_DT_FS_32G](#gaf3f87288e27f4e99f9820790fc47887d)。

量程（range）：±32 g。

<a id="r_ga408b46a045596c3e7e719f9c80db6f25"></a>

```c
#define LSM6DSV320X_DT_FS_64G 64
```

相关声明：[LSM6DSV320X_DT_FS_64G](#ga408b46a045596c3e7e719f9c80db6f25)。

±64 g（重力加速度单位）。

<a id="r_gaf72dfff525d0fde356181a7e20913304"></a>

```c
#define LSM6DSV320X_DT_FS_128G 128
```

相关声明：[LSM6DSV320X_DT_FS_128G](#gaf72dfff525d0fde356181a7e20913304)。

±128 g（重力加速度单位）。

<a id="r_ga9c114238f7edd06c6be2a875fffac9f3"></a>

```c
#define LSM6DSV320X_DT_FS_256G 256
```

相关声明：[LSM6DSV320X_DT_FS_256G](#ga9c114238f7edd06c6be2a875fffac9f3)。

±256 g（重力加速度单位）。

<a id="r_ga094ece1d53c2364657a06b3e3e2f91db"></a>

```c
#define LSM6DSV320X_DT_FS_320G 320
```

相关声明：[LSM6DSV320X_DT_FS_320G](#ga094ece1d53c2364657a06b3e3e2f91db)。

±320 g（重力加速度单位）。

## 13.4\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaa1db4dee887556c23b3c28e94798e286"></a>

```c
#define LSM6DSV320X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV320X_DT_FS_250DPS](#gaa1db4dee887556c23b3c28e94798e286)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga3c29c7980aacb096930a840db29dbace"></a>

```c
#define LSM6DSV320X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV320X_DT_FS_500DPS](#ga3c29c7980aacb096930a840db29dbace)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga0f3b2fa9b2415d18ec59ca1801b6d0bd"></a>

```c
#define LSM6DSV320X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV320X_DT_FS_1000DPS](#ga0f3b2fa9b2415d18ec59ca1801b6d0bd)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga70128ea873aac26fb036a968b5f81a47"></a>

```c
#define LSM6DSV320X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV320X_DT_FS_2000DPS](#ga70128ea873aac26fb036a968b5f81a47)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga08e5eb5bf99390efbe67b7b9f94aa578"></a>

```c
#define LSM6DSV320X_DT_FS_4000DPS 0x5
```

相关声明：[LSM6DSV320X_DT_FS_4000DPS](#ga08e5eb5bf99390efbe67b7b9f94aa578)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

## 13.5\_详细说明（Detailed Documentation）

<a id="ga0f3b2fa9b2415d18ec59ca1801b6d0bd"></a>

### `LSM6DSV320X_DT_FS_1000DPS`

```c
#define LSM6DSV320X_DT_FS_1000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="gaf72dfff525d0fde356181a7e20913304"></a>

### `LSM6DSV320X_DT_FS_128G`

```c
#define LSM6DSV320X_DT_FS_128G 128
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

±128 g（重力加速度单位）。

<a id="gabb2c1de34e3a5a2e9ee777420d1c1744"></a>

### `LSM6DSV320X_DT_FS_16G`

```c
#define LSM6DSV320X_DT_FS_16G 16
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

量程（range）：±16 g。

<a id="ga70128ea873aac26fb036a968b5f81a47"></a>

### `LSM6DSV320X_DT_FS_2000DPS`

```c
#define LSM6DSV320X_DT_FS_2000DPS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="gaa1db4dee887556c23b3c28e94798e286"></a>

### `LSM6DSV320X_DT_FS_250DPS`

```c
#define LSM6DSV320X_DT_FS_250DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

角速度量程：±250 度／秒（dps）。

<a id="ga9c114238f7edd06c6be2a875fffac9f3"></a>

### `LSM6DSV320X_DT_FS_256G`

```c
#define LSM6DSV320X_DT_FS_256G 256
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

±256 g（重力加速度单位）。

<a id="ga2e586abbca79ddaf5f697396d8102a3a"></a>

### `LSM6DSV320X_DT_FS_2G`

```c
#define LSM6DSV320X_DT_FS_2G 2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

量程（range）：±2 g。

<a id="ga094ece1d53c2364657a06b3e3e2f91db"></a>

### `LSM6DSV320X_DT_FS_320G`

```c
#define LSM6DSV320X_DT_FS_320G 320
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

±320 g（重力加速度单位）。

<a id="gaf3f87288e27f4e99f9820790fc47887d"></a>

### `LSM6DSV320X_DT_FS_32G`

```c
#define LSM6DSV320X_DT_FS_32G 32
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

量程（range）：±32 g。

<a id="ga08e5eb5bf99390efbe67b7b9f94aa578"></a>

### `LSM6DSV320X_DT_FS_4000DPS`

```c
#define LSM6DSV320X_DT_FS_4000DPS 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="gaba78d3c3569c44528a970ac6e5c99413"></a>

### `LSM6DSV320X_DT_FS_4G`

```c
#define LSM6DSV320X_DT_FS_4G 4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

量程（range）：±4 g。

<a id="ga3c29c7980aacb096930a840db29dbace"></a>

### `LSM6DSV320X_DT_FS_500DPS`

```c
#define LSM6DSV320X_DT_FS_500DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

角速度量程：±500 度／秒（dps）。

<a id="ga408b46a045596c3e7e719f9c80db6f25"></a>

### `LSM6DSV320X_DT_FS_64G`

```c
#define LSM6DSV320X_DT_FS_64G 64
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

±64 g（重力加速度单位）。

<a id="ga91952d45d6a3020b79ae6a79027d5728"></a>

### `LSM6DSV320X_DT_FS_8G`

```c
#define LSM6DSV320X_DT_FS_8G 8
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

量程（range）：±8 g。

<a id="ga2d718e3e593c7cc8a4ac31584d410be8"></a>

### `LSM6DSV320X_HG_XL_ODR_AT_1920Hz`

```c
#define LSM6DSV320X_HG_XL_ODR_AT_1920Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

1920 Hz（赫兹）。

<a id="ga001b8a3d4c95c156ea89ad0187f92468"></a>

### `LSM6DSV320X_HG_XL_ODR_AT_3840Hz`

```c
#define LSM6DSV320X_HG_XL_ODR_AT_3840Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

3840 Hz（赫兹）。

<a id="gaa3000f771aa3ef89e3b786fdd9055742"></a>

### `LSM6DSV320X_HG_XL_ODR_AT_480Hz`

```c
#define LSM6DSV320X_HG_XL_ODR_AT_480Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

480 Hz（赫兹）。

<a id="gaf536c506da4d13aa17e8388134180ce4"></a>

### `LSM6DSV320X_HG_XL_ODR_AT_7680Hz`

```c
#define LSM6DSV320X_HG_XL_ODR_AT_7680Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

7680 Hz（赫兹）。

<a id="gaf09aa8484b2ab208933a5a0e25c6de10"></a>

### `LSM6DSV320X_HG_XL_ODR_AT_960Hz`

```c
#define LSM6DSV320X_HG_XL_ODR_AT_960Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

960 Hz（赫兹）。

<a id="ga4a630613d01e476125b1a1fa9e894cb8"></a>

### `LSM6DSV320X_HG_XL_ODR_OFF`

```c
#define LSM6DSV320X_HG_XL_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/lsm6dsv320x.h>
```

掉电（Power-down）。


## 13.6\_原页交叉引用（Cross References）

- [lsm6dsv320x.h](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html)
- [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P012_LIS2DE12 API主题.md) · [返回大纲](大纲.md) · [下一章](P014_LSM6DSV80X API主题.md)
