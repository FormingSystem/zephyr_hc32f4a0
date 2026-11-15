---
id: learning.zephyr-docs.api-file-service-interface-reference.page-36
title: zephyr__dt-bindings__sensor__lsm6dsv320x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_dt-bindings\_\_sensor\_\_lsm6dsv320x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lsm6dsv320x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST LSM6DSV320X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "lsm6dsvxxx.h"
```

查看此文件的源码。

the ST LSM6DSV320X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 36.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_ga4a630613d01e476125b1a1fa9e894cb8"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_OFF 0x0
```

相关声明：[LSM6DSV320X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga4a630613d01e476125b1a1fa9e894cb8)。

掉电（Power-down）。

<a id="r_gaa3000f771aa3ef89e3b786fdd9055742"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaa3000f771aa3ef89e3b786fdd9055742)。

480 Hz（赫兹）。

<a id="r_gaf09aa8484b2ab208933a5a0e25c6de10"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf09aa8484b2ab208933a5a0e25c6de10)。

960 Hz（赫兹）。

<a id="r_ga2d718e3e593c7cc8a4ac31584d410be8"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga2d718e3e593c7cc8a4ac31584d410be8)。

1920 Hz（赫兹）。

<a id="r_ga001b8a3d4c95c156ea89ad0187f92468"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga001b8a3d4c95c156ea89ad0187f92468)。

3840 Hz（赫兹）。

<a id="r_gaf536c506da4d13aa17e8388134180ce4"></a>

```c
#define LSM6DSV320X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[LSM6DSV320X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf536c506da4d13aa17e8388134180ce4)。

7680 Hz（赫兹）。

<a id="define-members-1"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga2e586abbca79ddaf5f697396d8102a3a"></a>

```c
#define LSM6DSV320X_DT_FS_2G 2
```

相关声明：[LSM6DSV320X_DT_FS_2G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga2e586abbca79ddaf5f697396d8102a3a)。

量程（range）：±2 g。

<a id="r_gaba78d3c3569c44528a970ac6e5c99413"></a>

```c
#define LSM6DSV320X_DT_FS_4G 4
```

相关声明：[LSM6DSV320X_DT_FS_4G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaba78d3c3569c44528a970ac6e5c99413)。

量程（range）：±4 g。

<a id="r_ga91952d45d6a3020b79ae6a79027d5728"></a>

```c
#define LSM6DSV320X_DT_FS_8G 8
```

相关声明：[LSM6DSV320X_DT_FS_8G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga91952d45d6a3020b79ae6a79027d5728)。

量程（range）：±8 g。

<a id="r_gabb2c1de34e3a5a2e9ee777420d1c1744"></a>

```c
#define LSM6DSV320X_DT_FS_16G 16
```

相关声明：[LSM6DSV320X_DT_FS_16G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gabb2c1de34e3a5a2e9ee777420d1c1744)。

量程（range）：±16 g。

<a id="r_gaf3f87288e27f4e99f9820790fc47887d"></a>

```c
#define LSM6DSV320X_DT_FS_32G 32
```

相关声明：[LSM6DSV320X_DT_FS_32G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf3f87288e27f4e99f9820790fc47887d)。

量程（range）：±32 g。

<a id="r_ga408b46a045596c3e7e719f9c80db6f25"></a>

```c
#define LSM6DSV320X_DT_FS_64G 64
```

相关声明：[LSM6DSV320X_DT_FS_64G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga408b46a045596c3e7e719f9c80db6f25)。

±64 g（重力加速度单位）。

<a id="r_gaf72dfff525d0fde356181a7e20913304"></a>

```c
#define LSM6DSV320X_DT_FS_128G 128
```

相关声明：[LSM6DSV320X_DT_FS_128G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf72dfff525d0fde356181a7e20913304)。

±128 g（重力加速度单位）。

<a id="r_ga9c114238f7edd06c6be2a875fffac9f3"></a>

```c
#define LSM6DSV320X_DT_FS_256G 256
```

相关声明：[LSM6DSV320X_DT_FS_256G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga9c114238f7edd06c6be2a875fffac9f3)。

±256 g（重力加速度单位）。

<a id="r_ga094ece1d53c2364657a06b3e3e2f91db"></a>

```c
#define LSM6DSV320X_DT_FS_320G 320
```

相关声明：[LSM6DSV320X_DT_FS_320G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga094ece1d53c2364657a06b3e3e2f91db)。

±320 g（重力加速度单位）。

<a id="define-members-2"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_gaa1db4dee887556c23b3c28e94798e286"></a>

```c
#define LSM6DSV320X_DT_FS_250DPS 0x1
```

相关声明：[LSM6DSV320X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaa1db4dee887556c23b3c28e94798e286)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga3c29c7980aacb096930a840db29dbace"></a>

```c
#define LSM6DSV320X_DT_FS_500DPS 0x2
```

相关声明：[LSM6DSV320X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga3c29c7980aacb096930a840db29dbace)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga0f3b2fa9b2415d18ec59ca1801b6d0bd"></a>

```c
#define LSM6DSV320X_DT_FS_1000DPS 0x3
```

相关声明：[LSM6DSV320X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga0f3b2fa9b2415d18ec59ca1801b6d0bd)。

角速度量程：±1000 度／秒（dps）。

<a id="r_ga70128ea873aac26fb036a968b5f81a47"></a>

```c
#define LSM6DSV320X_DT_FS_2000DPS 0x4
```

相关声明：[LSM6DSV320X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga70128ea873aac26fb036a968b5f81a47)。

角速度量程：±2000 度／秒（dps）。

<a id="r_ga08e5eb5bf99390efbe67b7b9f94aa578"></a>

```c
#define LSM6DSV320X_DT_FS_4000DPS 0x5
```

相关声明：[LSM6DSV320X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga08e5eb5bf99390efbe67b7b9f94aa578)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。


## 36.2\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P462_lsm6dsv320x.h_源码浏览.md)
- [LSM6DSV320X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga4a630613d01e476125b1a1fa9e894cb8)
- [LSM6DSV320X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaa3000f771aa3ef89e3b786fdd9055742)
- [LSM6DSV320X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf09aa8484b2ab208933a5a0e25c6de10)
- [LSM6DSV320X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga2d718e3e593c7cc8a4ac31584d410be8)
- [LSM6DSV320X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga001b8a3d4c95c156ea89ad0187f92468)
- [LSM6DSV320X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf536c506da4d13aa17e8388134180ce4)
- [LSM6DSV320X_DT_FS_2G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga2e586abbca79ddaf5f697396d8102a3a)
- [LSM6DSV320X_DT_FS_4G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaba78d3c3569c44528a970ac6e5c99413)
- [LSM6DSV320X_DT_FS_8G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga91952d45d6a3020b79ae6a79027d5728)
- [LSM6DSV320X_DT_FS_16G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gabb2c1de34e3a5a2e9ee777420d1c1744)
- [LSM6DSV320X_DT_FS_32G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf3f87288e27f4e99f9820790fc47887d)
- [LSM6DSV320X_DT_FS_64G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga408b46a045596c3e7e719f9c80db6f25)
- [LSM6DSV320X_DT_FS_128G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaf72dfff525d0fde356181a7e20913304)
- [LSM6DSV320X_DT_FS_256G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga9c114238f7edd06c6be2a875fffac9f3)
- [LSM6DSV320X_DT_FS_320G](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga094ece1d53c2364657a06b3e3e2f91db)
- [LSM6DSV320X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#gaa1db4dee887556c23b3c28e94798e286)
- [LSM6DSV320X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga3c29c7980aacb096930a840db29dbace)
- [LSM6DSV320X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga0f3b2fa9b2415d18ec59ca1801b6d0bd)
- [LSM6DSV320X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga70128ea873aac26fb036a968b5f81a47)
- [LSM6DSV320X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P013_LSM6DSV320X API主题.md#ga08e5eb5bf99390efbe67b7b9f94aa578)

<a id="header-details"></a>

---

[上一章](P035_zephyr__dt-bindings__sensor__lsm6dsv16x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__dt-bindings__sensor__lsm6dsv32x.h_文件参考.md)
