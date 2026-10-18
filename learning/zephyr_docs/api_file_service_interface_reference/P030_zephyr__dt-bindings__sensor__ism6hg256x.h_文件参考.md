---
id: learning.zephyr-docs.api-file-service-interface-reference.page-30
title: zephyr__dt-bindings__sensor__ism6hg256x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ism6hg256x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_dt-bindings\_\_sensor\_\_ism6hg256x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ism6hg256x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST ISM6HG256X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="details"></a>

```c
#include "lsm6dsvxxx.h"
```

查看此文件的源码。

the ST ISM6HG256X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 30.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_ga7477d162ef5fb35973706f955bc10338"></a>

```c
#define ISM6HG256X_HG_XL_ODR_OFF 0x0
```

相关声明：[ISM6HG256X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga7477d162ef5fb35973706f955bc10338)。

掉电（Power-down）。

<a id="r_ga0c2e476c326bf1219c61f6a463c87a40"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga0c2e476c326bf1219c61f6a463c87a40)。

480 Hz（赫兹）。

<a id="r_ga74ae0c8c7de345a4e502bcbe325327c0"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga74ae0c8c7de345a4e502bcbe325327c0)。

960 Hz（赫兹）。

<a id="r_ga83edc7b75919e0d8b6c0c2801cae8352"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga83edc7b75919e0d8b6c0c2801cae8352)。

1920 Hz（赫兹）。

<a id="r_gaa2d8fc5c0e0cce7a974c7ce453e892f9"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gaa2d8fc5c0e0cce7a974c7ce453e892f9)。

3840 Hz（赫兹）。

<a id="r_ga332f8593d5209221abf0f8be149805f7"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga332f8593d5209221abf0f8be149805f7)。

7680 Hz（赫兹）。

<a id="define-members-1"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gae0be7879b6b860307022ecf37cc0b11c"></a>

```c
#define ISM6HG256X_DT_FS_2G 2
```

相关声明：[ISM6HG256X_DT_FS_2G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gae0be7879b6b860307022ecf37cc0b11c)。

量程（range）：±2 g。

<a id="r_ga284e359f07327f96f2a8da6ff93f2c6d"></a>

```c
#define ISM6HG256X_DT_FS_4G 4
```

相关声明：[ISM6HG256X_DT_FS_4G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga284e359f07327f96f2a8da6ff93f2c6d)。

量程（range）：±4 g。

<a id="r_ga36ddf57dcd3cfcfd333884003045f3d8"></a>

```c
#define ISM6HG256X_DT_FS_8G 8
```

相关声明：[ISM6HG256X_DT_FS_8G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga36ddf57dcd3cfcfd333884003045f3d8)。

量程（range）：±8 g。

<a id="r_ga2539b8008b7389fbfcdc965c4684e666"></a>

```c
#define ISM6HG256X_DT_FS_16G 16
```

相关声明：[ISM6HG256X_DT_FS_16G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga2539b8008b7389fbfcdc965c4684e666)。

量程（range）：±16 g。

<a id="r_ga5c525dbe57a12689850b28e61b8bce53"></a>

```c
#define ISM6HG256X_DT_FS_32G 32
```

相关声明：[ISM6HG256X_DT_FS_32G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga5c525dbe57a12689850b28e61b8bce53)。

量程（range）：±32 g。

<a id="r_gabc47fde1072f6d2f618d86b279fea466"></a>

```c
#define ISM6HG256X_DT_FS_64G 64
```

相关声明：[ISM6HG256X_DT_FS_64G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gabc47fde1072f6d2f618d86b279fea466)。

±64 g（重力加速度单位）。

<a id="r_ga6030b7ec79aaf52102fe5b9cbac6d57e"></a>

```c
#define ISM6HG256X_DT_FS_128G 128
```

相关声明：[ISM6HG256X_DT_FS_128G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga6030b7ec79aaf52102fe5b9cbac6d57e)。

±128 g（重力加速度单位）。

<a id="r_ga5bb04edd3b13ae44768ddbd508154209"></a>

```c
#define ISM6HG256X_DT_FS_256G 256
```

相关声明：[ISM6HG256X_DT_FS_256G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga5bb04edd3b13ae44768ddbd508154209)。

±256 g（重力加速度单位）。

<a id="define-members-2"></a>

### 陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga91d9f04ed8ecae9226549154515cfbb5"></a>

```c
#define ISM6HG256X_DT_FS_250DPS 0x1
```

相关声明：[ISM6HG256X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga91d9f04ed8ecae9226549154515cfbb5)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga39297d327d364df169e98bb81872939a"></a>

```c
#define ISM6HG256X_DT_FS_500DPS 0x2
```

相关声明：[ISM6HG256X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga39297d327d364df169e98bb81872939a)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga8e04d042315c5cd8f970074c00eb5879"></a>

```c
#define ISM6HG256X_DT_FS_1000DPS 0x3
```

相关声明：[ISM6HG256X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga8e04d042315c5cd8f970074c00eb5879)。

角速度量程：±1000 度／秒（dps）。

<a id="r_gab51ff37bc8285016a1083768956577e3"></a>

```c
#define ISM6HG256X_DT_FS_2000DPS 0x4
```

相关声明：[ISM6HG256X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gab51ff37bc8285016a1083768956577e3)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaff832e3bccec11724cf51aa4db6cdb5d"></a>

```c
#define ISM6HG256X_DT_FS_4000DPS 0x5
```

相关声明：[ISM6HG256X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gaff832e3bccec11724cf51aa4db6cdb5d)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。


## 30.2\_原页交叉引用（Cross References）

- [lsm6dsvxxx.h](../api_source_reference/P207_lsm6dsvxxx.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P414_ism6hg256x.h_源码浏览.md)
- [ISM6HG256X_HG_XL_ODR_OFF](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga7477d162ef5fb35973706f955bc10338)
- [ISM6HG256X_HG_XL_ODR_AT_480Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga0c2e476c326bf1219c61f6a463c87a40)
- [ISM6HG256X_HG_XL_ODR_AT_960Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga74ae0c8c7de345a4e502bcbe325327c0)
- [ISM6HG256X_HG_XL_ODR_AT_1920Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga83edc7b75919e0d8b6c0c2801cae8352)
- [ISM6HG256X_HG_XL_ODR_AT_3840Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gaa2d8fc5c0e0cce7a974c7ce453e892f9)
- [ISM6HG256X_HG_XL_ODR_AT_7680Hz](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga332f8593d5209221abf0f8be149805f7)
- [ISM6HG256X_DT_FS_2G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gae0be7879b6b860307022ecf37cc0b11c)
- [ISM6HG256X_DT_FS_4G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga284e359f07327f96f2a8da6ff93f2c6d)
- [ISM6HG256X_DT_FS_8G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga36ddf57dcd3cfcfd333884003045f3d8)
- [ISM6HG256X_DT_FS_16G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga2539b8008b7389fbfcdc965c4684e666)
- [ISM6HG256X_DT_FS_32G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga5c525dbe57a12689850b28e61b8bce53)
- [ISM6HG256X_DT_FS_64G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gabc47fde1072f6d2f618d86b279fea466)
- [ISM6HG256X_DT_FS_128G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga6030b7ec79aaf52102fe5b9cbac6d57e)
- [ISM6HG256X_DT_FS_256G](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga5bb04edd3b13ae44768ddbd508154209)
- [ISM6HG256X_DT_FS_250DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga91d9f04ed8ecae9226549154515cfbb5)
- [ISM6HG256X_DT_FS_500DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga39297d327d364df169e98bb81872939a)
- [ISM6HG256X_DT_FS_1000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#ga8e04d042315c5cd8f970074c00eb5879)
- [ISM6HG256X_DT_FS_2000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gab51ff37bc8285016a1083768956577e3)
- [ISM6HG256X_DT_FS_4000DPS](../api_vector_pipeline_topic_reference/P011_ISM6HG256X API主题.md#gaff832e3bccec11724cf51aa4db6cdb5d)

<a id="header-details"></a>

---

[上一章](P029_zephyr__dt-bindings__sensor__ism330dhcx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_____w__zephyr__zephyr__kernel__include__kernel_arch_interface.h_文件参考.md)
