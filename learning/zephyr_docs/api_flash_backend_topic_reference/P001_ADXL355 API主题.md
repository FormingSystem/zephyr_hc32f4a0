---
id: learning.zephyr-docs.api-flash-backend-topic-reference.page-1
title: ADXL355 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adxl355__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ADXL355 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adxl355__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADXL355 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

Analog Devices ADXL355 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_adxl355_2Eh"></a>

```c
file adxl355.h
```

相关声明：[adxl355.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2adxl355_8h.html)。

the Analog Devices ADXL355 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.2\_输出速率选项（Output Rate Options）

设备树 `odr` 属性的取值。

<a id="r_gab60be1cb5989008043c4c768c4bb67a5"></a>

```c
#define ADXL355_DT_ODR_4000 0
```

相关声明：[ADXL355_DT_ODR_4000](#gab60be1cb5989008043c4c768c4bb67a5)。

输出数据速率（Output Data Rate）：4000 Hz。

<a id="r_gaae25fe8c25742fb0358dff1c4aa95eef"></a>

```c
#define ADXL355_DT_ODR_2000 1
```

相关声明：[ADXL355_DT_ODR_2000](#gaae25fe8c25742fb0358dff1c4aa95eef)。

输出数据速率（Output Data Rate）：2000 Hz。

<a id="r_ga5aabb32d884ee322d8744408e507aee8"></a>

```c
#define ADXL355_DT_ODR_1000 2
```

相关声明：[ADXL355_DT_ODR_1000](#ga5aabb32d884ee322d8744408e507aee8)。

输出数据速率（Output Data Rate）：1000 Hz。

<a id="r_ga8c19b7c5d1a57c33a0ae3a5edc114768"></a>

```c
#define ADXL355_DT_ODR_500 3
```

相关声明：[ADXL355_DT_ODR_500](#ga8c19b7c5d1a57c33a0ae3a5edc114768)。

输出数据速率（Output Data Rate）：500 Hz。

<a id="r_ga71a30b4c271eabcf11ca501acfb05ff3"></a>

```c
#define ADXL355_DT_ODR_250 4
```

相关声明：[ADXL355_DT_ODR_250](#ga71a30b4c271eabcf11ca501acfb05ff3)。

输出数据速率（Output Data Rate）：250 Hz。

<a id="r_gab411f93d442413e4ca21061115c1399c"></a>

```c
#define ADXL355_DT_ODR_125 5
```

相关声明：[ADXL355_DT_ODR_125](#gab411f93d442413e4ca21061115c1399c)。

输出数据速率（Output Data Rate）：125 Hz。

<a id="r_gad0bf8e8272a0db9be1452c21a122cd98"></a>

```c
#define ADXL355_DT_ODR_62_5 6
```

相关声明：[ADXL355_DT_ODR_62_5](#gad0bf8e8272a0db9be1452c21a122cd98)。

输出数据速率（Output Data Rate）：62.5 Hz。

<a id="r_ga4f85d789f9b184ac8a96c75590a93719"></a>

```c
#define ADXL355_DT_ODR_31_25 7
```

相关声明：[ADXL355_DT_ODR_31_25](#ga4f85d789f9b184ac8a96c75590a93719)。

输出数据速率（Output Data Rate）：31.25 Hz。

<a id="r_ga61378797ab5e9e8d373908efce4df39e"></a>

```c
#define ADXL355_DT_ODR_15_625 8
```

相关声明：[ADXL355_DT_ODR_15_625](#ga61378797ab5e9e8d373908efce4df39e)。

输出数据速率（Output Data Rate）：15.625 Hz。

<a id="r_ga92cb10f98315e05768a90fd9397eccff"></a>

```c
#define ADXL355_DT_ODR_7_813 9
```

相关声明：[ADXL355_DT_ODR_7_813](#ga92cb10f98315e05768a90fd9397eccff)。

输出数据速率（Output Data Rate）：7.813 Hz。

<a id="r_ga0d6025b885cc0b21174b96f8fa2dced6"></a>

```c
#define ADXL355_DT_ODR_3_906 10
```

相关声明：[ADXL355_DT_ODR_3_906](#ga0d6025b885cc0b21174b96f8fa2dced6)。

输出数据速率（Output Data Rate）：3.906 Hz。

## 1.3\_测量范围选择选项（Select Range Options）

设备树 `range` 属性的取值。

<a id="r_gac0296485c3d583e12c9d4a73ee532f33"></a>

```c
#define ADXL355_DT_RANGE_2G 1
```

相关声明：[ADXL355_DT_RANGE_2G](#gac0296485c3d583e12c9d4a73ee532f33)。

选择 ±2 g 测量范围（Measurement Range）。

<a id="r_gaff43fe8c86158d46b826df053a6fa530"></a>

```c
#define ADXL355_DT_RANGE_4G 2
```

相关声明：[ADXL355_DT_RANGE_4G](#gaff43fe8c86158d46b826df053a6fa530)。

选择 ±4 g 测量范围（Measurement Range）。

<a id="r_ga083df135be18fe7bcdd1f6681d434197"></a>

```c
#define ADXL355_DT_RANGE_8G 3
```

相关声明：[ADXL355_DT_RANGE_8G](#ga083df135be18fe7bcdd1f6681d434197)。

选择 ±8 g 测量范围（Measurement Range）。

## 1.4\_高通滤波器截止频率选项（High Pass Filter Corner Options）

设备树属性（Devicetree Property）`hpf-corner` 的取值。

<a id="r_ga15cb598fda2032fea4f74df2dd586c43"></a>

```c
#define ADXL355_DT_HPF_OFF 0
```

相关声明：[ADXL355_DT_HPF_OFF](#ga15cb598fda2032fea4f74df2dd586c43)。

高通滤波器（High-pass Filter）禁用。

<a id="r_ga2bb6fc7a0f5db2d41d1b7ab41408e5cf"></a>

```c
#define ADXL355_DT_HPF_24_7e_4 1
```

相关声明：[ADXL355_DT_HPF_24_7e_4](#ga2bb6fc7a0f5db2d41d1b7ab41408e5cf)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 24.7e-4 倍。

<a id="r_gad88ed912cd272948bf6cc1d99786d190"></a>

```c
#define ADXL355_DT_HPF_6_208e_4 2
```

相关声明：[ADXL355_DT_HPF_6_208e_4](#gad88ed912cd272948bf6cc1d99786d190)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 6.208e-4 倍。

<a id="r_ga73f0b16ce376b02d42f0f93ff6ccc97c"></a>

```c
#define ADXL355_DT_HPF_1_5545e_4 3
```

相关声明：[ADXL355_DT_HPF_1_5545e_4](#ga73f0b16ce376b02d42f0f93ff6ccc97c)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 1.5545e-4 倍。

<a id="r_ga8eeaac80b071b9d0921e00d085cc0e0a"></a>

```c
#define ADXL355_DT_HPF_0_3862e_4 4
```

相关声明：[ADXL355_DT_HPF_0_3862e_4](#ga8eeaac80b071b9d0921e00d085cc0e0a)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.3862e-4 倍。

<a id="r_ga34c4fe4b7bbea96d3f6153746dc6228c"></a>

```c
#define ADXL355_DT_HPF_0_0954e_4 5
```

相关声明：[ADXL355_DT_HPF_0_0954e_4](#ga34c4fe4b7bbea96d3f6153746dc6228c)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0954e-4 倍。

<a id="r_ga665874864fa75fef549936a93ae61b52"></a>

```c
#define ADXL355_DT_HPF_0_0238e_4 6
```

相关声明：[ADXL355_DT_HPF_0_0238e_4](#ga665874864fa75fef549936a93ae61b52)。

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0238e-4 倍。

## 1.5\_外部时钟选项（External Clock Options）

设备树属性（Devicetree Property）`ext-clk` 的取值。

<a id="r_ga218ea74d36be97682a38b860b58b717f"></a>

```c
#define ADXL355_DT_EXTCLK_DISABLED 0
```

相关声明：[ADXL355_DT_EXTCLK_DISABLED](#ga218ea74d36be97682a38b860b58b717f)。

外部时钟（External Clock）禁用。

<a id="r_gaa9bed643f472c8c4f9056465be1fe1c6"></a>

```c
#define ADXL355_DT_EXTCLK_ENABLED 1
```

相关声明：[ADXL355_DT_EXTCLK_ENABLED](#gaa9bed643f472c8c4f9056465be1fe1c6)。

外部时钟（External Clock）启用。

## 1.6\_外部同步选项（External Sync Options）

设备树属性（Devicetree Property）`ext-sync` 的取值。

<a id="r_gafb59af517b95dcd49521605624ccd0f2"></a>

```c
#define ADXL355_DT_INTERNAL_SYNC 0
```

相关声明：[ADXL355_DT_INTERNAL_SYNC](#gafb59af517b95dcd49521605624ccd0f2)。

内部同步（Internal Synchronization）。

<a id="r_gab54040571fbb582ab22f60b878861db6"></a>

```c
#define ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION 1
```

相关声明：[ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION](#gab54040571fbb582ab22f60b878861db6)。

不带插值的外部同步（External Synchronization without Interpolation）。

<a id="r_ga0a8992af010d9c33e3874a3f88f8c5b9"></a>

```c
#define ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION 2
```

相关声明：[ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION](#ga0a8992af010d9c33e3874a3f88f8c5b9)。

带插值的外部同步（External Synchronization with Interpolation）。

## 1.7\_详细说明（Detailed Documentation）

<a id="ga218ea74d36be97682a38b860b58b717f"></a>

### `ADXL355_DT_EXTCLK_DISABLED`

```c
#define ADXL355_DT_EXTCLK_DISABLED 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

外部时钟（External Clock）禁用。

<a id="gaa9bed643f472c8c4f9056465be1fe1c6"></a>

### `ADXL355_DT_EXTCLK_ENABLED`

```c
#define ADXL355_DT_EXTCLK_ENABLED 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

外部时钟（External Clock）启用。

<a id="gab54040571fbb582ab22f60b878861db6"></a>

### `ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION`

```c
#define ADXL355_DT_EXTERNAL_SYNC_NO_INTERPOLATION 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

不带插值的外部同步（External Synchronization without Interpolation）。

<a id="ga0a8992af010d9c33e3874a3f88f8c5b9"></a>

### `ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION`

```c
#define ADXL355_DT_EXTERNAL_SYNC_WITH_INTERPOLATION 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

带插值的外部同步（External Synchronization with Interpolation）。

<a id="ga665874864fa75fef549936a93ae61b52"></a>

### `ADXL355_DT_HPF_0_0238e_4`

```c
#define ADXL355_DT_HPF_0_0238e_4 6
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0238e-4 倍。

<a id="ga34c4fe4b7bbea96d3f6153746dc6228c"></a>

### `ADXL355_DT_HPF_0_0954e_4`

```c
#define ADXL355_DT_HPF_0_0954e_4 5
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.0954e-4 倍。

<a id="ga8eeaac80b071b9d0921e00d085cc0e0a"></a>

### `ADXL355_DT_HPF_0_3862e_4`

```c
#define ADXL355_DT_HPF_0_3862e_4 4
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 0.3862e-4 倍。

<a id="ga73f0b16ce376b02d42f0f93ff6ccc97c"></a>

### `ADXL355_DT_HPF_1_5545e_4`

```c
#define ADXL355_DT_HPF_1_5545e_4 3
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 1.5545e-4 倍。

<a id="ga2bb6fc7a0f5db2d41d1b7ab41408e5cf"></a>

### `ADXL355_DT_HPF_24_7e_4`

```c
#define ADXL355_DT_HPF_24_7e_4 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 24.7e-4 倍。

<a id="gad88ed912cd272948bf6cc1d99786d190"></a>

### `ADXL355_DT_HPF_6_208e_4`

```c
#define ADXL355_DT_HPF_6_208e_4 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器截止频率（High-pass Filter Corner）为输出数据速率（ODR）的 6.208e-4 倍。

<a id="ga15cb598fda2032fea4f74df2dd586c43"></a>

### `ADXL355_DT_HPF_OFF`

```c
#define ADXL355_DT_HPF_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

高通滤波器（High-pass Filter）禁用。

<a id="gafb59af517b95dcd49521605624ccd0f2"></a>

### `ADXL355_DT_INTERNAL_SYNC`

```c
#define ADXL355_DT_INTERNAL_SYNC 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

内部同步（Internal Synchronization）。

<a id="ga5aabb32d884ee322d8744408e507aee8"></a>

### `ADXL355_DT_ODR_1000`

```c
#define ADXL355_DT_ODR_1000 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：1000 Hz。

<a id="gab411f93d442413e4ca21061115c1399c"></a>

### `ADXL355_DT_ODR_125`

```c
#define ADXL355_DT_ODR_125 5
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：125 Hz。

<a id="ga61378797ab5e9e8d373908efce4df39e"></a>

### `ADXL355_DT_ODR_15_625`

```c
#define ADXL355_DT_ODR_15_625 8
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：15.625 Hz。

<a id="gaae25fe8c25742fb0358dff1c4aa95eef"></a>

### `ADXL355_DT_ODR_2000`

```c
#define ADXL355_DT_ODR_2000 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：2000 Hz。

<a id="ga71a30b4c271eabcf11ca501acfb05ff3"></a>

### `ADXL355_DT_ODR_250`

```c
#define ADXL355_DT_ODR_250 4
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：250 Hz。

<a id="ga4f85d789f9b184ac8a96c75590a93719"></a>

### `ADXL355_DT_ODR_31_25`

```c
#define ADXL355_DT_ODR_31_25 7
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：31.25 Hz。

<a id="ga0d6025b885cc0b21174b96f8fa2dced6"></a>

### `ADXL355_DT_ODR_3_906`

```c
#define ADXL355_DT_ODR_3_906 10
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：3.906 Hz。

<a id="gab60be1cb5989008043c4c768c4bb67a5"></a>

### `ADXL355_DT_ODR_4000`

```c
#define ADXL355_DT_ODR_4000 0
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：4000 Hz。

<a id="ga8c19b7c5d1a57c33a0ae3a5edc114768"></a>

### `ADXL355_DT_ODR_500`

```c
#define ADXL355_DT_ODR_500 3
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：500 Hz。

<a id="gad0bf8e8272a0db9be1452c21a122cd98"></a>

### `ADXL355_DT_ODR_62_5`

```c
#define ADXL355_DT_ODR_62_5 6
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：62.5 Hz。

<a id="ga92cb10f98315e05768a90fd9397eccff"></a>

### `ADXL355_DT_ODR_7_813`

```c
#define ADXL355_DT_ODR_7_813 9
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

输出数据速率（Output Data Rate）：7.813 Hz。

<a id="gac0296485c3d583e12c9d4a73ee532f33"></a>

### `ADXL355_DT_RANGE_2G`

```c
#define ADXL355_DT_RANGE_2G 1
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

选择 ±2 g 测量范围（Measurement Range）。

<a id="gaff43fe8c86158d46b826df053a6fa530"></a>

### `ADXL355_DT_RANGE_4G`

```c
#define ADXL355_DT_RANGE_4G 2
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

选择 ±4 g 测量范围（Measurement Range）。

<a id="ga083df135be18fe7bcdd1f6681d434197"></a>

### `ADXL355_DT_RANGE_8G`

```c
#define ADXL355_DT_RANGE_8G 3
```

```c
#include <zephyr/dt-bindings/sensor/adxl355.h>
```

选择 ±8 g 测量范围（Measurement Range）。


## 1.8\_原页交叉引用（Cross References）

- [adxl355.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2adxl355_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_生物识别驱动后端 API（Biometrics Driver Backend API）.md)
