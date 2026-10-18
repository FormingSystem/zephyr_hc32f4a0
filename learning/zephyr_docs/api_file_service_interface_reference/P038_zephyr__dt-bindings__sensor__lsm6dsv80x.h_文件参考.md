---
id: learning.zephyr-docs.api-file-service-interface-reference.page-38
title: zephyr__dt-bindings__sensor__lsm6dsv80x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv80x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dsv80x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv80x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM6DSV80X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "lsm6dsvxxx.h"
```

查看此文件的源码。

the ST LSM6DSV80X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_gae5107fc0abbb4d3644bdc08f265e2dfb"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_OFF 0x0
```

相关声明：[LSM6DSV80X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gae5107fc0abbb4d3644bdc08f265e2dfb)。

掉电（Power-down）。

<a id="r_gae2b7bb3e0a118742cf43d1a861b5c0e2"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gae2b7bb3e0a118742cf43d1a861b5c0e2)。

480 Hz（赫兹）。

<a id="r_ga275f58c9c06a555d083f39dc27d59b97"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga275f58c9c06a555d083f39dc27d59b97)。

960 Hz（赫兹）。

<a id="r_ga835ced437617127ae14b7c66c78b3c29"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga835ced437617127ae14b7c66c78b3c29)。

1920 Hz（赫兹）。

<a id="r_ga27c15d3e87430c3c5ec4c41faace32d4"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga27c15d3e87430c3c5ec4c41faace32d4)。

3840 Hz（赫兹）。

<a id="r_ga9a996de027e4a6ba62913014ec58e146"></a>

```c
#define LSM6DSV80X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[LSM6DSV80X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga9a996de027e4a6ba62913014ec58e146)。

7680 Hz（赫兹）。

<a id="define-members-1"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gaf39b6edd5b404e3fab2fa3d9ddd9a676"></a>

```c
#define LSM6DSV80X_DT_FS_2G 2
```

相关声明：[LSM6DSV80X_DT_FS_2G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaf39b6edd5b404e3fab2fa3d9ddd9a676)。

量程（range）：±2 g。

<a id="r_ga36db2fc1b95af74e9c37b73f817c62fa"></a>

```c
#define LSM6DSV80X_DT_FS_4G 4
```

相关声明：[LSM6DSV80X_DT_FS_4G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga36db2fc1b95af74e9c37b73f817c62fa)。

量程（range）：±4 g。

<a id="r_ga75fd8443f9c9ee7858a7aef2dd76ad1a"></a>

```c
#define LSM6DSV80X_DT_FS_8G 8
```

相关声明：[LSM6DSV80X_DT_FS_8G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga75fd8443f9c9ee7858a7aef2dd76ad1a)。

量程（range）：±8 g。

<a id="r_ga37b357c8db6e24871dfad8927d940b90"></a>

```c
#define LSM6DSV80X_DT_FS_16G 16
```

相关声明：[LSM6DSV80X_DT_FS_16G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga37b357c8db6e24871dfad8927d940b90)。

量程（range）：±16 g。

<a id="r_ga15f009fd0c94ca2e0981a113c5937da6"></a>

```c
#define LSM6DSV80X_DT_FS_32G 32
```

相关声明：[LSM6DSV80X_DT_FS_32G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga15f009fd0c94ca2e0981a113c5937da6)。

量程（range）：±32 g。

<a id="r_gac786fcbc53064b5fb0b82d506dded6d0"></a>

```c
#define LSM6DSV80X_DT_FS_64G 64
```

相关声明：[LSM6DSV80X_DT_FS_64G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gac786fcbc53064b5fb0b82d506dded6d0)。

±64 g（重力加速度单位）。

<a id="r_gad7af9a9dd7d2482ebebb1ea883873d6d"></a>

```c
#define LSM6DSV80X_DT_FS_80G 80
```

相关声明：[LSM6DSV80X_DT_FS_80G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gad7af9a9dd7d2482ebebb1ea883873d6d)。

±80 g（重力加速度单位）。

<a id="define-members-2"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaf12fda3698938071f33e2eb8935b260d"></a>

```c
#define LSM6DSV80X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV80X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaf12fda3698938071f33e2eb8935b260d)。

角速度量程：±250 度／秒（dps）。

<a id="r_gaccabb277c647d6dadd1e11a23d24dd80"></a>

```c
#define LSM6DSV80X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV80X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaccabb277c647d6dadd1e11a23d24dd80)。

角速度量程：±500 度／秒（dps）。

<a id="r_gaa665aee5c06bd5edb49b5b0e2b3d577a"></a>

```c
#define LSM6DSV80X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV80X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaa665aee5c06bd5edb49b5b0e2b3d577a)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga05179e45cd95551113792e6d0da881a6"></a>

```c
#define LSM6DSV80X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV80X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga05179e45cd95551113792e6d0da881a6)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaaf7e240788e89a68d497799fce6cf4f1"></a>

```c
#define LSM6DSV80X_DT_FS_4000DPS 0x5
```

相关声明：[LSM6DSV80X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaaf7e240788e89a68d497799fce6cf4f1)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。


## 38.2\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P464_lsm6dsv80x.h_源码浏览.md)
- [LSM6DSV80X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gae5107fc0abbb4d3644bdc08f265e2dfb)
- [LSM6DSV80X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gae2b7bb3e0a118742cf43d1a861b5c0e2)
- [LSM6DSV80X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga275f58c9c06a555d083f39dc27d59b97)
- [LSM6DSV80X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga835ced437617127ae14b7c66c78b3c29)
- [LSM6DSV80X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga27c15d3e87430c3c5ec4c41faace32d4)
- [LSM6DSV80X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga9a996de027e4a6ba62913014ec58e146)
- [LSM6DSV80X_DT_FS_2G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaf39b6edd5b404e3fab2fa3d9ddd9a676)
- [LSM6DSV80X_DT_FS_4G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga36db2fc1b95af74e9c37b73f817c62fa)
- [LSM6DSV80X_DT_FS_8G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga75fd8443f9c9ee7858a7aef2dd76ad1a)
- [LSM6DSV80X_DT_FS_16G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga37b357c8db6e24871dfad8927d940b90)
- [LSM6DSV80X_DT_FS_32G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga15f009fd0c94ca2e0981a113c5937da6)
- [LSM6DSV80X_DT_FS_64G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gac786fcbc53064b5fb0b82d506dded6d0)
- [LSM6DSV80X_DT_FS_80G](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gad7af9a9dd7d2482ebebb1ea883873d6d)
- [LSM6DSV80X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaf12fda3698938071f33e2eb8935b260d)
- [LSM6DSV80X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaccabb277c647d6dadd1e11a23d24dd80)
- [LSM6DSV80X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaa665aee5c06bd5edb49b5b0e2b3d577a)
- [LSM6DSV80X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#ga05179e45cd95551113792e6d0da881a6)
- [LSM6DSV80X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P014_LSM6DSV80X API主题.md#gaaf7e240788e89a68d497799fce6cf4f1)

<a id="header-details"></a>

---

[上一章](P037_zephyr__dt-bindings__sensor__lsm6dsv32x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__net__midi2.h_文件参考.md)
