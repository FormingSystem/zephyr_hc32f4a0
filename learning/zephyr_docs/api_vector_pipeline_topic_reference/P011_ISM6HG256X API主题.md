---
id: learning.zephyr-docs.api-vector-pipeline-topic-reference.page-11
title: ISM6HG256X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ism6hg256x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_ISM6HG256X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ism6hg256x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics ISM6HG256X 高 g 值六轴惯性测量单元（High-g 6-axis IMU）。

<a id="details"></a>

意法半导体（STMicroelectronics）的 ISM6HG256X 高 g 值六轴惯性测量单元（6-axis IMU）。本系列共用输出数据率（Output Data Rate）和先进先出（FIFO）设置；参见 LSM6DSVXXX。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_ism6hg256x_2Eh"></a>

```c
file ism6hg256x.h
```

相关声明：[ism6hg256x.h](https://docs.zephyrproject.org/latest/doxygen/html/ism6hg256x_8h.html)。

the ST ISM6HG256X IMU的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.2\_高 g 值加速度计输出数据率（High-g Accelerometer Output Data Rate）

设备树（Devicetree）属性 `accel-hg-odr` 的取值。

<a id="r_ga7477d162ef5fb35973706f955bc10338"></a>

```c
#define ISM6HG256X_HG_XL_ODR_OFF 0x0
```

相关声明：[ISM6HG256X_HG_XL_ODR_OFF](#ga7477d162ef5fb35973706f955bc10338)。

掉电（Power-down）。

<a id="r_ga0c2e476c326bf1219c61f6a463c87a40"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_480Hz 0x3
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_480Hz](#ga0c2e476c326bf1219c61f6a463c87a40)。

480 Hz（赫兹）。

<a id="r_ga74ae0c8c7de345a4e502bcbe325327c0"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_960Hz 0x4
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_960Hz](#ga74ae0c8c7de345a4e502bcbe325327c0)。

960 Hz（赫兹）。

<a id="r_ga83edc7b75919e0d8b6c0c2801cae8352"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_1920Hz 0x5
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_1920Hz](#ga83edc7b75919e0d8b6c0c2801cae8352)。

1920 Hz（赫兹）。

<a id="r_gaa2d8fc5c0e0cce7a974c7ce453e892f9"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_3840Hz 0x6
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_3840Hz](#gaa2d8fc5c0e0cce7a974c7ce453e892f9)。

3840 Hz（赫兹）。

<a id="r_ga332f8593d5209221abf0f8be149805f7"></a>

```c
#define ISM6HG256X_HG_XL_ODR_AT_7680Hz 0x7
```

相关声明：[ISM6HG256X_HG_XL_ODR_AT_7680Hz](#ga332f8593d5209221abf0f8be149805f7)。

7680 Hz（赫兹）。

## 11.3\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_gae0be7879b6b860307022ecf37cc0b11c"></a>

```c
#define ISM6HG256X_DT_FS_2G 2
```

相关声明：[ISM6HG256X_DT_FS_2G](#gae0be7879b6b860307022ecf37cc0b11c)。

量程（range）：±2 g。

<a id="r_ga284e359f07327f96f2a8da6ff93f2c6d"></a>

```c
#define ISM6HG256X_DT_FS_4G 4
```

相关声明：[ISM6HG256X_DT_FS_4G](#ga284e359f07327f96f2a8da6ff93f2c6d)。

量程（range）：±4 g。

<a id="r_ga36ddf57dcd3cfcfd333884003045f3d8"></a>

```c
#define ISM6HG256X_DT_FS_8G 8
```

相关声明：[ISM6HG256X_DT_FS_8G](#ga36ddf57dcd3cfcfd333884003045f3d8)。

量程（range）：±8 g。

<a id="r_ga2539b8008b7389fbfcdc965c4684e666"></a>

```c
#define ISM6HG256X_DT_FS_16G 16
```

相关声明：[ISM6HG256X_DT_FS_16G](#ga2539b8008b7389fbfcdc965c4684e666)。

量程（range）：±16 g。

<a id="r_ga5c525dbe57a12689850b28e61b8bce53"></a>

```c
#define ISM6HG256X_DT_FS_32G 32
```

相关声明：[ISM6HG256X_DT_FS_32G](#ga5c525dbe57a12689850b28e61b8bce53)。

量程（range）：±32 g。

<a id="r_gabc47fde1072f6d2f618d86b279fea466"></a>

```c
#define ISM6HG256X_DT_FS_64G 64
```

相关声明：[ISM6HG256X_DT_FS_64G](#gabc47fde1072f6d2f618d86b279fea466)。

±64 g（重力加速度单位）。

<a id="r_ga6030b7ec79aaf52102fe5b9cbac6d57e"></a>

```c
#define ISM6HG256X_DT_FS_128G 128
```

相关声明：[ISM6HG256X_DT_FS_128G](#ga6030b7ec79aaf52102fe5b9cbac6d57e)。

±128 g（重力加速度单位）。

<a id="r_ga5bb04edd3b13ae44768ddbd508154209"></a>

```c
#define ISM6HG256X_DT_FS_256G 256
```

相关声明：[ISM6HG256X_DT_FS_256G](#ga5bb04edd3b13ae44768ddbd508154209)。

±256 g（重力加速度单位）。

## 11.4\_陀螺仪满量程范围（Gyroscope full-scale range）

设备树 `gyro-range` 属性的取值。

<a id="r_ga91d9f04ed8ecae9226549154515cfbb5"></a>

```c
#define ISM6HG256X_DT_FS_250DPS 0x1
```

相关声明：[ISM6HG256X_DT_FS_250DPS](#ga91d9f04ed8ecae9226549154515cfbb5)。

角速度量程：±250 度／秒（dps）。

<a id="r_ga39297d327d364df169e98bb81872939a"></a>

```c
#define ISM6HG256X_DT_FS_500DPS 0x2
```

相关声明：[ISM6HG256X_DT_FS_500DPS](#ga39297d327d364df169e98bb81872939a)。

角速度量程：±500 度／秒（dps）。

<a id="r_ga8e04d042315c5cd8f970074c00eb5879"></a>

```c
#define ISM6HG256X_DT_FS_1000DPS 0x3
```

相关声明：[ISM6HG256X_DT_FS_1000DPS](#ga8e04d042315c5cd8f970074c00eb5879)。

角速度量程：±1000 度／秒（dps）。

<a id="r_gab51ff37bc8285016a1083768956577e3"></a>

```c
#define ISM6HG256X_DT_FS_2000DPS 0x4
```

相关声明：[ISM6HG256X_DT_FS_2000DPS](#gab51ff37bc8285016a1083768956577e3)。

角速度量程：±2000 度／秒（dps）。

<a id="r_gaff832e3bccec11724cf51aa4db6cdb5d"></a>

```c
#define ISM6HG256X_DT_FS_4000DPS 0x5
```

相关声明：[ISM6HG256X_DT_FS_4000DPS](#gaff832e3bccec11724cf51aa4db6cdb5d)。

角速度量程（angular-rate range）：±4000 度／秒（dps）。

## 11.5\_详细说明（Detailed Documentation）

<a id="ga8e04d042315c5cd8f970074c00eb5879"></a>

### `ISM6HG256X_DT_FS_1000DPS`

```c
#define ISM6HG256X_DT_FS_1000DPS 0x3
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

角速度量程：±1000 度／秒（dps）。

<a id="ga6030b7ec79aaf52102fe5b9cbac6d57e"></a>

### `ISM6HG256X_DT_FS_128G`

```c
#define ISM6HG256X_DT_FS_128G 128
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

±128 g（重力加速度单位）。

<a id="ga2539b8008b7389fbfcdc965c4684e666"></a>

### `ISM6HG256X_DT_FS_16G`

```c
#define ISM6HG256X_DT_FS_16G 16
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

量程（range）：±16 g。

<a id="gab51ff37bc8285016a1083768956577e3"></a>

### `ISM6HG256X_DT_FS_2000DPS`

```c
#define ISM6HG256X_DT_FS_2000DPS 0x4
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

角速度量程：±2000 度／秒（dps）。

<a id="ga91d9f04ed8ecae9226549154515cfbb5"></a>

### `ISM6HG256X_DT_FS_250DPS`

```c
#define ISM6HG256X_DT_FS_250DPS 0x1
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

角速度量程：±250 度／秒（dps）。

<a id="ga5bb04edd3b13ae44768ddbd508154209"></a>

### `ISM6HG256X_DT_FS_256G`

```c
#define ISM6HG256X_DT_FS_256G 256
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

±256 g（重力加速度单位）。

<a id="gae0be7879b6b860307022ecf37cc0b11c"></a>

### `ISM6HG256X_DT_FS_2G`

```c
#define ISM6HG256X_DT_FS_2G 2
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

量程（range）：±2 g。

<a id="ga5c525dbe57a12689850b28e61b8bce53"></a>

### `ISM6HG256X_DT_FS_32G`

```c
#define ISM6HG256X_DT_FS_32G 32
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

量程（range）：±32 g。

<a id="gaff832e3bccec11724cf51aa4db6cdb5d"></a>

### `ISM6HG256X_DT_FS_4000DPS`

```c
#define ISM6HG256X_DT_FS_4000DPS 0x5
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

角速度量程（angular-rate range）：±4000 度／秒（dps）。

<a id="ga284e359f07327f96f2a8da6ff93f2c6d"></a>

### `ISM6HG256X_DT_FS_4G`

```c
#define ISM6HG256X_DT_FS_4G 4
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

量程（range）：±4 g。

<a id="ga39297d327d364df169e98bb81872939a"></a>

### `ISM6HG256X_DT_FS_500DPS`

```c
#define ISM6HG256X_DT_FS_500DPS 0x2
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

角速度量程：±500 度／秒（dps）。

<a id="gabc47fde1072f6d2f618d86b279fea466"></a>

### `ISM6HG256X_DT_FS_64G`

```c
#define ISM6HG256X_DT_FS_64G 64
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

±64 g（重力加速度单位）。

<a id="ga36ddf57dcd3cfcfd333884003045f3d8"></a>

### `ISM6HG256X_DT_FS_8G`

```c
#define ISM6HG256X_DT_FS_8G 8
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

量程（range）：±8 g。

<a id="ga83edc7b75919e0d8b6c0c2801cae8352"></a>

### `ISM6HG256X_HG_XL_ODR_AT_1920Hz`

```c
#define ISM6HG256X_HG_XL_ODR_AT_1920Hz 0x5
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

1920 Hz（赫兹）。

<a id="gaa2d8fc5c0e0cce7a974c7ce453e892f9"></a>

### `ISM6HG256X_HG_XL_ODR_AT_3840Hz`

```c
#define ISM6HG256X_HG_XL_ODR_AT_3840Hz 0x6
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

3840 Hz（赫兹）。

<a id="ga0c2e476c326bf1219c61f6a463c87a40"></a>

### `ISM6HG256X_HG_XL_ODR_AT_480Hz`

```c
#define ISM6HG256X_HG_XL_ODR_AT_480Hz 0x3
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

480 Hz（赫兹）。

<a id="ga332f8593d5209221abf0f8be149805f7"></a>

### `ISM6HG256X_HG_XL_ODR_AT_7680Hz`

```c
#define ISM6HG256X_HG_XL_ODR_AT_7680Hz 0x7
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

7680 Hz（赫兹）。

<a id="ga74ae0c8c7de345a4e502bcbe325327c0"></a>

### `ISM6HG256X_HG_XL_ODR_AT_960Hz`

```c
#define ISM6HG256X_HG_XL_ODR_AT_960Hz 0x4
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

960 Hz（赫兹）。

<a id="ga7477d162ef5fb35973706f955bc10338"></a>

### `ISM6HG256X_HG_XL_ODR_OFF`

```c
#define ISM6HG256X_HG_XL_ODR_OFF 0x0
```

```c
#include <zephyr/dt-bindings/sensor/ism6hg256x.h>
```

掉电（Power-down）。


## 11.6\_原页交叉引用（Cross References）

- [ism6hg256x.h](https://docs.zephyrproject.org/latest/doxygen/html/ism6hg256x_8h.html)
- [LSM6DSVXXX](https://docs.zephyrproject.org/latest/doxygen/html/group__lsm6dsvxxx__interface.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_ISM330DHCX API主题.md) · [返回大纲](大纲.md) · [下一章](P012_LIS2DE12 API主题.md)
