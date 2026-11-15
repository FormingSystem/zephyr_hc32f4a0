---
id: learning.zephyr-docs.api-connection-topic-reference.page-1
title: ADXL345 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl345__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ADXL345 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl345__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL345 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL345 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_adxl345_2Eh"></a>

```c
file adxl345.h
```

相关声明：[adxl345.h](https://docs.zephyrproject.org/latest/doxygen/html/adxl345_8h.html)。

the Analog Devices ADXL345 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.2\_输出数据率选项（Output data rate options）

设备树 `odr` 属性的取值。

<a id="r_ga8a5bbcf4613102e5c3f0e94bcc3c60ae"></a>

```c
#define ADXL345_DT_ODR_12_5 7
```

相关声明：[ADXL345_DT_ODR_12_5](#ga8a5bbcf4613102e5c3f0e94bcc3c60ae)。

频率：12.5 Hz。

<a id="r_ga09764c27782131ee1860f5f81300862d"></a>

```c
#define ADXL345_DT_ODR_25 8
```

相关声明：[ADXL345_DT_ODR_25](#ga09764c27782131ee1860f5f81300862d)。

频率：25 Hz。

<a id="r_gacf11af5464cce21e110e5b1af20c88cc"></a>

```c
#define ADXL345_DT_ODR_50 9
```

相关声明：[ADXL345_DT_ODR_50](#gacf11af5464cce21e110e5b1af20c88cc)。

频率：50 Hz。

<a id="r_ga237e85997341d8c1ecfecbcd4b3dd845"></a>

```c
#define ADXL345_DT_ODR_100 10
```

相关声明：[ADXL345_DT_ODR_100](#ga237e85997341d8c1ecfecbcd4b3dd845)。

频率：100 Hz。

<a id="r_gacbf8615cb511204588debb1134b306fd"></a>

```c
#define ADXL345_DT_ODR_200 11
```

相关声明：[ADXL345_DT_ODR_200](#gacbf8615cb511204588debb1134b306fd)。

频率：200 Hz。

<a id="r_ga529e2926d1101ba4f0a3dd5aaa5486ac"></a>

```c
#define ADXL345_DT_ODR_400 12
```

相关声明：[ADXL345_DT_ODR_400](#ga529e2926d1101ba4f0a3dd5aaa5486ac)。

频率：400 Hz。

## 1.3\_测量量程选项（Measurement range options）

设备树 `range` 属性的取值。

<a id="r_gac1cd31fd104a49f38110c8be392f2dcf"></a>

```c
#define ADXL345_DT_RANGE_2G 0
```

相关声明：[ADXL345_DT_RANGE_2G](#gac1cd31fd104a49f38110c8be392f2dcf)。

量程（range）：±2 g。

<a id="r_gacb4c325c001ea2a17d8bdc89d9353531"></a>

```c
#define ADXL345_DT_RANGE_4G 1
```

相关声明：[ADXL345_DT_RANGE_4G](#gacb4c325c001ea2a17d8bdc89d9353531)。

量程（range）：±4 g。

<a id="r_ga04fe23a42782d0efe267596bf10d56c0"></a>

```c
#define ADXL345_DT_RANGE_8G 2
```

相关声明：[ADXL345_DT_RANGE_8G](#ga04fe23a42782d0efe267596bf10d56c0)。

量程（range）：±8 g。

<a id="r_gab7548617062a51ea2d11464cfb9653ae"></a>

```c
#define ADXL345_DT_RANGE_16G 3
```

相关声明：[ADXL345_DT_RANGE_16G](#gab7548617062a51ea2d11464cfb9653ae)。

量程（range）：±16 g。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga237e85997341d8c1ecfecbcd4b3dd845"></a>

### `ADXL345_DT_ODR_100`

```c
#define ADXL345_DT_ODR_100 10
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：100 Hz。

<a id="ga8a5bbcf4613102e5c3f0e94bcc3c60ae"></a>

### `ADXL345_DT_ODR_12_5`

```c
#define ADXL345_DT_ODR_12_5 7
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：12.5 Hz。

<a id="gacbf8615cb511204588debb1134b306fd"></a>

### `ADXL345_DT_ODR_200`

```c
#define ADXL345_DT_ODR_200 11
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：200 Hz。

<a id="ga09764c27782131ee1860f5f81300862d"></a>

### `ADXL345_DT_ODR_25`

```c
#define ADXL345_DT_ODR_25 8
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：25 Hz。

<a id="ga529e2926d1101ba4f0a3dd5aaa5486ac"></a>

### `ADXL345_DT_ODR_400`

```c
#define ADXL345_DT_ODR_400 12
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：400 Hz。

<a id="gacf11af5464cce21e110e5b1af20c88cc"></a>

### `ADXL345_DT_ODR_50`

```c
#define ADXL345_DT_ODR_50 9
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

频率：50 Hz。

<a id="gab7548617062a51ea2d11464cfb9653ae"></a>

### `ADXL345_DT_RANGE_16G`

```c
#define ADXL345_DT_RANGE_16G 3
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

量程（range）：±16 g。

<a id="gac1cd31fd104a49f38110c8be392f2dcf"></a>

### `ADXL345_DT_RANGE_2G`

```c
#define ADXL345_DT_RANGE_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

量程（range）：±2 g。

<a id="gacb4c325c001ea2a17d8bdc89d9353531"></a>

### `ADXL345_DT_RANGE_4G`

```c
#define ADXL345_DT_RANGE_4G 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

量程（range）：±4 g。

<a id="ga04fe23a42782d0efe267596bf10d56c0"></a>

### `ADXL345_DT_RANGE_8G`

```c
#define ADXL345_DT_RANGE_8G 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl345.h>
```

量程（range）：±8 g。


## 1.5\_原页交叉引用（Cross References）

- [adxl345.h](https://docs.zephyrproject.org/latest/doxygen/html/adxl345_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_蓝牙内容控制标识符（Bluetooth Content Control Identifier）.md)
