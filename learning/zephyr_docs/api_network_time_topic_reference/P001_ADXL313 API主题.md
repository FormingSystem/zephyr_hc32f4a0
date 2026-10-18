---
id: learning.zephyr-docs.api-network-time-topic-reference.page-1
title: ADXL313 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl313__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ADXL313 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl313__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL313 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL313 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_adxl313_2Eh"></a>

```c
file adxl313.h
```

相关声明：[adxl313.h](https://docs.zephyrproject.org/latest/doxygen/html/adxl313_8h.html)。

the Analog Devices ADXL313 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值，对应 `BW_RATE` 寄存器。

<a id="r_ga02a7095f521f5e696800cfc5fce72217"></a>

```c
#define ADXL313_DT_ODR_6_25 6
```

相关声明：[ADXL313_DT_ODR_6_25](#ga02a7095f521f5e696800cfc5fce72217)。

频率：6.25 Hz。

<a id="r_ga4807d03edd4da963773d99a24b805f12"></a>

```c
#define ADXL313_DT_ODR_12_5 7
```

相关声明：[ADXL313_DT_ODR_12_5](#ga4807d03edd4da963773d99a24b805f12)。

频率：12.5 Hz。

<a id="r_gae74ffdddc1787b97e561785f6b8ad202"></a>

```c
#define ADXL313_DT_ODR_25 8
```

相关声明：[ADXL313_DT_ODR_25](#gae74ffdddc1787b97e561785f6b8ad202)。

频率：25 Hz。

<a id="r_ga1d20b1876f2c6ca49d974f374bdef464"></a>

```c
#define ADXL313_DT_ODR_50 9
```

相关声明：[ADXL313_DT_ODR_50](#ga1d20b1876f2c6ca49d974f374bdef464)。

频率：50 Hz。

<a id="r_gaece105aeb621ef3f73ce67f434d76771"></a>

```c
#define ADXL313_DT_ODR_100 10
```

相关声明：[ADXL313_DT_ODR_100](#gaece105aeb621ef3f73ce67f434d76771)。

频率：100 Hz。

<a id="r_gab4fa8769a7c3d8b97513da312be8c188"></a>

```c
#define ADXL313_DT_ODR_200 11
```

相关声明：[ADXL313_DT_ODR_200](#gab4fa8769a7c3d8b97513da312be8c188)。

频率：200 Hz。

<a id="r_ga087d90450b45bb0bb75e895610ce4665"></a>

```c
#define ADXL313_DT_ODR_400 12
```

相关声明：[ADXL313_DT_ODR_400](#ga087d90450b45bb0bb75e895610ce4665)。

频率：400 Hz。

<a id="r_ga3e44a470a8849b99688352afefa7e1de"></a>

```c
#define ADXL313_DT_ODR_800 13
```

相关声明：[ADXL313_DT_ODR_800](#ga3e44a470a8849b99688352afefa7e1de)。

频率：800 Hz。

<a id="r_ga730220c782b951050dd16a248bf978ad"></a>

```c
#define ADXL313_DT_ODR_1600 14
```

相关声明：[ADXL313_DT_ODR_1600](#ga730220c782b951050dd16a248bf978ad)。

频率：1600 Hz。

<a id="r_gaec20668bace20c1d9342b0d79468ed5c"></a>

```c
#define ADXL313_DT_ODR_3200 15
```

相关声明：[ADXL313_DT_ODR_3200](#gaec20668bace20c1d9342b0d79468ed5c)。

频率：3200 Hz。

## 1.3\_测量量程选项（Measurement range options）

设备树 `range` 属性的取值，对应 `DATA_FORMAT` 寄存器。

<a id="r_ga01d6676b81a52cafc326940abe8c3dcd"></a>

```c
#define ADXL313_DT_RANGE_0_5G 0
```

相关声明：[ADXL313_DT_RANGE_0_5G](#ga01d6676b81a52cafc326940abe8c3dcd)。

量程（range）：±0.5 g。

<a id="r_ga876a5a51a12688ed335d78a75d362dce"></a>

```c
#define ADXL313_DT_RANGE_1G 1
```

相关声明：[ADXL313_DT_RANGE_1G](#ga876a5a51a12688ed335d78a75d362dce)。

量程（range）：±1 g。

<a id="r_ga576838117e35f1f086da223d1ca29639"></a>

```c
#define ADXL313_DT_RANGE_2G 2
```

相关声明：[ADXL313_DT_RANGE_2G](#ga576838117e35f1f086da223d1ca29639)。

量程（range）：±2 g。

<a id="r_ga49806e46c1570f30498e2d672738e6f6"></a>

```c
#define ADXL313_DT_RANGE_4G 3
```

相关声明：[ADXL313_DT_RANGE_4G](#ga49806e46c1570f30498e2d672738e6f6)。

量程（range）：±4 g。

## 1.4\_详细说明（Detailed Documentation）

<a id="gaece105aeb621ef3f73ce67f434d76771"></a>

### `ADXL313_DT_ODR_100`

```c
#define ADXL313_DT_ODR_100 10
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：100 Hz。

<a id="ga4807d03edd4da963773d99a24b805f12"></a>

### `ADXL313_DT_ODR_12_5`

```c
#define ADXL313_DT_ODR_12_5 7
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：12.5 Hz。

<a id="ga730220c782b951050dd16a248bf978ad"></a>

### `ADXL313_DT_ODR_1600`

```c
#define ADXL313_DT_ODR_1600 14
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：1600 Hz。

<a id="gab4fa8769a7c3d8b97513da312be8c188"></a>

### `ADXL313_DT_ODR_200`

```c
#define ADXL313_DT_ODR_200 11
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：200 Hz。

<a id="gae74ffdddc1787b97e561785f6b8ad202"></a>

### `ADXL313_DT_ODR_25`

```c
#define ADXL313_DT_ODR_25 8
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：25 Hz。

<a id="gaec20668bace20c1d9342b0d79468ed5c"></a>

### `ADXL313_DT_ODR_3200`

```c
#define ADXL313_DT_ODR_3200 15
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：3200 Hz。

<a id="ga087d90450b45bb0bb75e895610ce4665"></a>

### `ADXL313_DT_ODR_400`

```c
#define ADXL313_DT_ODR_400 12
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：400 Hz。

<a id="ga1d20b1876f2c6ca49d974f374bdef464"></a>

### `ADXL313_DT_ODR_50`

```c
#define ADXL313_DT_ODR_50 9
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：50 Hz。

<a id="ga02a7095f521f5e696800cfc5fce72217"></a>

### `ADXL313_DT_ODR_6_25`

```c
#define ADXL313_DT_ODR_6_25 6
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：6.25 Hz。

<a id="ga3e44a470a8849b99688352afefa7e1de"></a>

### `ADXL313_DT_ODR_800`

```c
#define ADXL313_DT_ODR_800 13
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

频率：800 Hz。

<a id="ga01d6676b81a52cafc326940abe8c3dcd"></a>

### `ADXL313_DT_RANGE_0_5G`

```c
#define ADXL313_DT_RANGE_0_5G 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

量程（range）：±0.5 g。

<a id="ga876a5a51a12688ed335d78a75d362dce"></a>

### `ADXL313_DT_RANGE_1G`

```c
#define ADXL313_DT_RANGE_1G 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

量程（range）：±1 g。

<a id="ga576838117e35f1f086da223d1ca29639"></a>

### `ADXL313_DT_RANGE_2G`

```c
#define ADXL313_DT_RANGE_2G 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

量程（range）：±2 g。

<a id="ga49806e46c1570f30498e2d672738e6f6"></a>

### `ADXL313_DT_RANGE_4G`

```c
#define ADXL313_DT_RANGE_4G 3
```

```c
#include <zephyr/dt-bindings/sensor/adxl313.h>
```

量程（range）：±4 g。


## 1.5\_原页交叉引用（Cross References）

- [adxl313.h](https://docs.zephyrproject.org/latest/doxygen/html/adxl313_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_BMM350 API主题.md)
