---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-10
title: LIS2DW12 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_LIS2DW12 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2dw12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LIS2DW12 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics LIS2DW12 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 10.1\_文件（Files）

<a id="r_lis2dw12_2Eh"></a>

```c
file lis2dw12.h
```

相关声明：[lis2dw12.h](../api_file_mesh_interrupt_reference/P014_zephyr__dt-bindings__sensor__lis2dw12.h_文件参考.md)。

the ST LIS2DW12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 10.2\_电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_ga0c03f55d1b6ebbf1d48e0c34d9122a74"></a>

```c
#define LIS2DW12_DT_LP_M1 0
```

相关声明：[LIS2DW12_DT_LP_M1](#ga0c03f55d1b6ebbf1d48e0c34d9122a74)。

低功耗模式（Low-power Mode）1，12 位。

<a id="r_gaeb6d34d3c11a1f3e7dc2cfe5f7405aae"></a>

```c
#define LIS2DW12_DT_LP_M2 1
```

相关声明：[LIS2DW12_DT_LP_M2](#gaeb6d34d3c11a1f3e7dc2cfe5f7405aae)。

低功耗模式（Low-power Mode）2，14 位。

<a id="r_gab9ab746af6c8dfa384671ee313c7eea4"></a>

```c
#define LIS2DW12_DT_LP_M3 2
```

相关声明：[LIS2DW12_DT_LP_M3](#gab9ab746af6c8dfa384671ee313c7eea4)。

低功耗模式（Low-power Mode）3，14 位。

<a id="r_gada20bc2633adb3ae955c2f709d727154"></a>

```c
#define LIS2DW12_DT_LP_M4 3
```

相关声明：[LIS2DW12_DT_LP_M4](#gada20bc2633adb3ae955c2f709d727154)。

低功耗模式（Low-power Mode）4，14 位。

<a id="r_ga0307502b4dee186f1945636c713eee4d"></a>

```c
#define LIS2DW12_DT_HP_MODE 4
```

相关声明：[LIS2DW12_DT_HP_MODE](#ga0307502b4dee186f1945636c713eee4d)。

高性能模式（High-performance Mode），14 位。

## 10.3\_滤波器带宽选项（Filter Bandwidth Options）

设备树属性（Devicetree Property）`bw-filt` 的取值。

<a id="r_ga88efe563d0f4d704773886d7670bea31"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_2 0
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_2](#ga88efe563d0f4d704773886d7670bea31)。

输出数据速率（ODR）除以 2。

<a id="r_ga4433ccc00389f58d30b9998b11915848"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_4 1
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_4](#ga4433ccc00389f58d30b9998b11915848)。

输出数据速率（ODR）除以 4。

<a id="r_gaad4197948abbd4587f6c9810f34e0c49"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_10 2
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_10](#gaad4197948abbd4587f6c9810f34e0c49)。

输出数据速率（ODR）除以 10。

<a id="r_ga9972d8b7618f39c9ddff273ecd80616a"></a>

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_20 3
```

相关声明：[LIS2DW12_DT_FILTER_BW_ODR_DIV_20](#ga9972d8b7618f39c9ddff273ecd80616a)。

输出数据速率（ODR）除以 20。

## 10.4\_敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_ga71fc2ff7108bd85a86fd82c0ff002c18"></a>

```c
#define LIS2DW12_DT_SINGLE_TAP 0
```

相关声明：[LIS2DW12_DT_SINGLE_TAP](#ga71fc2ff7108bd85a86fd82c0ff002c18)。

仅单击（Single-tap Only）。

<a id="r_ga4011203a9d243f9650cecab3d9ecf34d"></a>

```c
#define LIS2DW12_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[LIS2DW12_DT_SINGLE_DOUBLE_TAP](#ga4011203a9d243f9650cecab3d9ecf34d)。

单击与双击（Single and Double Tap）。

## 10.5\_自由落体阈值选项（Free-fall Threshold Options）

设备树属性（Devicetree Property）`ff-threshold` 的取值。

<a id="r_gac0420687b2a5ef0b886534b183d9b2f7"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_156_mg 0
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_156_mg](#gac0420687b2a5ef0b886534b183d9b2f7)。

156 mg（千分之一标准重力加速度）。

<a id="r_ga6afc0cf0328630c3bcdaf4cc579d8988"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_219_mg 1
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_219_mg](#ga6afc0cf0328630c3bcdaf4cc579d8988)。

219 mg（千分之一标准重力加速度）。

<a id="r_ga25b0e004ef448952083e417b0c77f97d"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_250_mg 2
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_250_mg](#ga25b0e004ef448952083e417b0c77f97d)。

250 mg（千分之一标准重力加速度）。

<a id="r_ga5ab3d56ad2ab84179316f3706780d716"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_312_mg 3
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_312_mg](#ga5ab3d56ad2ab84179316f3706780d716)。

312 mg（千分之一标准重力加速度）。

<a id="r_ga429524e40340eb36610b7c0b4a449298"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_344_mg 4
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_344_mg](#ga429524e40340eb36610b7c0b4a449298)。

344 mg（千分之一标准重力加速度）。

<a id="r_ga9a7a1520051a5b6107e6e0adbfb1d837"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_406_mg 5
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_406_mg](#ga9a7a1520051a5b6107e6e0adbfb1d837)。

406 mg（千分之一标准重力加速度）。

<a id="r_gac336d6955333fc41ce21b9d68dfde4e5"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_469_mg 6
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_469_mg](#gac336d6955333fc41ce21b9d68dfde4e5)。

469 mg（千分之一标准重力加速度）。

<a id="r_ga7de449940954836ff3c48ef192662760"></a>

```c
#define LIS2DW12_DT_FF_THRESHOLD_500_mg 7
```

相关声明：[LIS2DW12_DT_FF_THRESHOLD_500_mg](#ga7de449940954836ff3c48ef192662760)。

500 mg（千分之一标准重力加速度）。

## 10.6\_唤醒持续时间选项（Wake-up Duration Options）

设备树属性（Devicetree Property）`wakeup-duration` 的取值。

<a id="r_ga1bcffaa1b8439f626164b736be17f9db"></a>

```c
#define LIS2DW12_DT_WAKEUP_1_ODR 0
```

相关声明：[LIS2DW12_DT_WAKEUP_1_ODR](#ga1bcffaa1b8439f626164b736be17f9db)。

1 个输出数据速率周期（ODR Period）。

<a id="r_ga53457e3a0d24bf3599ff779f3a559fb4"></a>

```c
#define LIS2DW12_DT_WAKEUP_2_ODR 1
```

相关声明：[LIS2DW12_DT_WAKEUP_2_ODR](#ga53457e3a0d24bf3599ff779f3a559fb4)。

2 个输出数据速率周期（ODR Period）。

<a id="r_ga580dd3e03a377fce36db7916c254b52a"></a>

```c
#define LIS2DW12_DT_WAKEUP_3_ODR 2
```

相关声明：[LIS2DW12_DT_WAKEUP_3_ODR](#ga580dd3e03a377fce36db7916c254b52a)。

3 个输出数据速率周期（ODR Period）。

<a id="r_gaae58921652443e8f7757b38ade589c49"></a>

```c
#define LIS2DW12_DT_WAKEUP_4_ODR 3
```

相关声明：[LIS2DW12_DT_WAKEUP_4_ODR](#gaae58921652443e8f7757b38ade589c49)。

4 个输出数据速率周期（ODR Period）。

## 10.7\_休眠持续时间选项（Sleep Duration Options）

设备树属性（Devicetree Property）`sleep-duration` 的取值。

<a id="r_gaa9df8cef65e33e117a8de9eb2df745c3"></a>

```c
#define LIS2DW12_DT_SLEEP_0_ODR 0
```

相关声明：[LIS2DW12_DT_SLEEP_0_ODR](#gaa9df8cef65e33e117a8de9eb2df745c3)。

0 个输出数据速率周期（ODR Period）。

<a id="r_gaf43f42617789c1482e1ddf1d9abd7c3d"></a>

```c
#define LIS2DW12_DT_SLEEP_1_ODR 1
```

相关声明：[LIS2DW12_DT_SLEEP_1_ODR](#gaf43f42617789c1482e1ddf1d9abd7c3d)。

1 个输出数据速率周期（ODR Period）。

<a id="r_ga6c76600bf9baff0483d5865ba98aa75e"></a>

```c
#define LIS2DW12_DT_SLEEP_2_ODR 2
```

相关声明：[LIS2DW12_DT_SLEEP_2_ODR](#ga6c76600bf9baff0483d5865ba98aa75e)。

2 个输出数据速率周期（ODR Period）。

<a id="r_gaf294baab225caba1e4931abfee9660b8"></a>

```c
#define LIS2DW12_DT_SLEEP_3_ODR 3
```

相关声明：[LIS2DW12_DT_SLEEP_3_ODR](#gaf294baab225caba1e4931abfee9660b8)。

3 个输出数据速率周期（ODR Period）。

<a id="r_gac45de707e5c1ee485b5cdd95ce3332af"></a>

```c
#define LIS2DW12_DT_SLEEP_4_ODR 4
```

相关声明：[LIS2DW12_DT_SLEEP_4_ODR](#gac45de707e5c1ee485b5cdd95ce3332af)。

4 个输出数据速率周期（ODR Period）。

<a id="r_ga904ec47239d01ac05218bee5fa2f4235"></a>

```c
#define LIS2DW12_DT_SLEEP_5_ODR 5
```

相关声明：[LIS2DW12_DT_SLEEP_5_ODR](#ga904ec47239d01ac05218bee5fa2f4235)。

5 个输出数据速率周期（ODR Period）。

<a id="r_ga552a71243df2cfe6dcc6f9ca5a4208c9"></a>

```c
#define LIS2DW12_DT_SLEEP_6_ODR 6
```

相关声明：[LIS2DW12_DT_SLEEP_6_ODR](#ga552a71243df2cfe6dcc6f9ca5a4208c9)。

6 个输出数据速率周期（ODR Period）。

<a id="r_ga72ced204873bfce192b6bcfc9d823ffc"></a>

```c
#define LIS2DW12_DT_SLEEP_7_ODR 7
```

相关声明：[LIS2DW12_DT_SLEEP_7_ODR](#ga72ced204873bfce192b6bcfc9d823ffc)。

7 个输出数据速率周期（ODR Period）。

<a id="r_ga9078b4d1fa77dd53871ddbc7715b3f0c"></a>

```c
#define LIS2DW12_DT_SLEEP_8_ODR 8
```

相关声明：[LIS2DW12_DT_SLEEP_8_ODR](#ga9078b4d1fa77dd53871ddbc7715b3f0c)。

8 个输出数据速率周期（ODR Period）。

<a id="r_ga979e47f3dda9c72b92d87bb3fc5b3e4f"></a>

```c
#define LIS2DW12_DT_SLEEP_9_ODR 9
```

相关声明：[LIS2DW12_DT_SLEEP_9_ODR](#ga979e47f3dda9c72b92d87bb3fc5b3e4f)。

9 个输出数据速率周期（ODR Period）。

<a id="r_ga15982beb9fce8268a056fb2f088f6724"></a>

```c
#define LIS2DW12_DT_SLEEP_10_ODR 10
```

相关声明：[LIS2DW12_DT_SLEEP_10_ODR](#ga15982beb9fce8268a056fb2f088f6724)。

10 个输出数据速率周期（ODR Period）。

<a id="r_gad3546f54d5eee5d7d9cb9318a6104a9c"></a>

```c
#define LIS2DW12_DT_SLEEP_11_ODR 11
```

相关声明：[LIS2DW12_DT_SLEEP_11_ODR](#gad3546f54d5eee5d7d9cb9318a6104a9c)。

11 个输出数据速率周期（ODR Period）。

<a id="r_ga97614b907ca69fd13f0e8a9b61e15904"></a>

```c
#define LIS2DW12_DT_SLEEP_12_ODR 12
```

相关声明：[LIS2DW12_DT_SLEEP_12_ODR](#ga97614b907ca69fd13f0e8a9b61e15904)。

12 个输出数据速率周期（ODR Period）。

<a id="r_gabff45bcd009134ee4da471e9e915584a"></a>

```c
#define LIS2DW12_DT_SLEEP_13_ODR 13
```

相关声明：[LIS2DW12_DT_SLEEP_13_ODR](#gabff45bcd009134ee4da471e9e915584a)。

13 个输出数据速率周期（ODR Period）。

<a id="r_ga8ba46d92426bf168d6b9da5acee6668f"></a>

```c
#define LIS2DW12_DT_SLEEP_14_ODR 14
```

相关声明：[LIS2DW12_DT_SLEEP_14_ODR](#ga8ba46d92426bf168d6b9da5acee6668f)。

14 个输出数据速率周期（ODR Period）。

<a id="r_ga39ddac85ed26346de4272157ce2533a8"></a>

```c
#define LIS2DW12_DT_SLEEP_15_ODR 15
```

相关声明：[LIS2DW12_DT_SLEEP_15_ODR](#ga39ddac85ed26346de4272157ce2533a8)。

15 个输出数据速率周期（ODR Period）。

## 10.8\_详细说明（Detailed Documentation）

<a id="gac0420687b2a5ef0b886534b183d9b2f7"></a>

### `LIS2DW12_DT_FF_THRESHOLD_156_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_156_mg 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

156 mg（千分之一标准重力加速度）。

<a id="ga6afc0cf0328630c3bcdaf4cc579d8988"></a>

### `LIS2DW12_DT_FF_THRESHOLD_219_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_219_mg 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

219 mg（千分之一标准重力加速度）。

<a id="ga25b0e004ef448952083e417b0c77f97d"></a>

### `LIS2DW12_DT_FF_THRESHOLD_250_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_250_mg 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

250 mg（千分之一标准重力加速度）。

<a id="ga5ab3d56ad2ab84179316f3706780d716"></a>

### `LIS2DW12_DT_FF_THRESHOLD_312_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_312_mg 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

312 mg（千分之一标准重力加速度）。

<a id="ga429524e40340eb36610b7c0b4a449298"></a>

### `LIS2DW12_DT_FF_THRESHOLD_344_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_344_mg 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

344 mg（千分之一标准重力加速度）。

<a id="ga9a7a1520051a5b6107e6e0adbfb1d837"></a>

### `LIS2DW12_DT_FF_THRESHOLD_406_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_406_mg 5
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

406 mg（千分之一标准重力加速度）。

<a id="gac336d6955333fc41ce21b9d68dfde4e5"></a>

### `LIS2DW12_DT_FF_THRESHOLD_469_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_469_mg 6
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

469 mg（千分之一标准重力加速度）。

<a id="ga7de449940954836ff3c48ef192662760"></a>

### `LIS2DW12_DT_FF_THRESHOLD_500_mg`

```c
#define LIS2DW12_DT_FF_THRESHOLD_500_mg 7
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

500 mg（千分之一标准重力加速度）。

<a id="gaad4197948abbd4587f6c9810f34e0c49"></a>

### `LIS2DW12_DT_FILTER_BW_ODR_DIV_10`

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_10 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

输出数据速率（ODR）除以 10。

<a id="ga88efe563d0f4d704773886d7670bea31"></a>

### `LIS2DW12_DT_FILTER_BW_ODR_DIV_2`

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_2 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

输出数据速率（ODR）除以 2。

<a id="ga9972d8b7618f39c9ddff273ecd80616a"></a>

### `LIS2DW12_DT_FILTER_BW_ODR_DIV_20`

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_20 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

输出数据速率（ODR）除以 20。

<a id="ga4433ccc00389f58d30b9998b11915848"></a>

### `LIS2DW12_DT_FILTER_BW_ODR_DIV_4`

```c
#define LIS2DW12_DT_FILTER_BW_ODR_DIV_4 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

输出数据速率（ODR）除以 4。

<a id="ga0307502b4dee186f1945636c713eee4d"></a>

### `LIS2DW12_DT_HP_MODE`

```c
#define LIS2DW12_DT_HP_MODE 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

高性能模式（High-performance Mode），14 位。

<a id="ga0c03f55d1b6ebbf1d48e0c34d9122a74"></a>

### `LIS2DW12_DT_LP_M1`

```c
#define LIS2DW12_DT_LP_M1 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

低功耗模式（Low-power Mode）1，12 位。

<a id="gaeb6d34d3c11a1f3e7dc2cfe5f7405aae"></a>

### `LIS2DW12_DT_LP_M2`

```c
#define LIS2DW12_DT_LP_M2 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

低功耗模式（Low-power Mode）2，14 位。

<a id="gab9ab746af6c8dfa384671ee313c7eea4"></a>

### `LIS2DW12_DT_LP_M3`

```c
#define LIS2DW12_DT_LP_M3 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

低功耗模式（Low-power Mode）3，14 位。

<a id="gada20bc2633adb3ae955c2f709d727154"></a>

### `LIS2DW12_DT_LP_M4`

```c
#define LIS2DW12_DT_LP_M4 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

低功耗模式（Low-power Mode）4，14 位。

<a id="ga4011203a9d243f9650cecab3d9ecf34d"></a>

### `LIS2DW12_DT_SINGLE_DOUBLE_TAP`

```c
#define LIS2DW12_DT_SINGLE_DOUBLE_TAP 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

单击与双击（Single and Double Tap）。

<a id="ga71fc2ff7108bd85a86fd82c0ff002c18"></a>

### `LIS2DW12_DT_SINGLE_TAP`

```c
#define LIS2DW12_DT_SINGLE_TAP 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

仅单击（Single-tap Only）。

<a id="gaa9df8cef65e33e117a8de9eb2df745c3"></a>

### `LIS2DW12_DT_SLEEP_0_ODR`

```c
#define LIS2DW12_DT_SLEEP_0_ODR 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

0 个输出数据速率周期（ODR Period）。

<a id="ga15982beb9fce8268a056fb2f088f6724"></a>

### `LIS2DW12_DT_SLEEP_10_ODR`

```c
#define LIS2DW12_DT_SLEEP_10_ODR 10
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

10 个输出数据速率周期（ODR Period）。

<a id="gad3546f54d5eee5d7d9cb9318a6104a9c"></a>

### `LIS2DW12_DT_SLEEP_11_ODR`

```c
#define LIS2DW12_DT_SLEEP_11_ODR 11
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

11 个输出数据速率周期（ODR Period）。

<a id="ga97614b907ca69fd13f0e8a9b61e15904"></a>

### `LIS2DW12_DT_SLEEP_12_ODR`

```c
#define LIS2DW12_DT_SLEEP_12_ODR 12
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

12 个输出数据速率周期（ODR Period）。

<a id="gabff45bcd009134ee4da471e9e915584a"></a>

### `LIS2DW12_DT_SLEEP_13_ODR`

```c
#define LIS2DW12_DT_SLEEP_13_ODR 13
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

13 个输出数据速率周期（ODR Period）。

<a id="ga8ba46d92426bf168d6b9da5acee6668f"></a>

### `LIS2DW12_DT_SLEEP_14_ODR`

```c
#define LIS2DW12_DT_SLEEP_14_ODR 14
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

14 个输出数据速率周期（ODR Period）。

<a id="ga39ddac85ed26346de4272157ce2533a8"></a>

### `LIS2DW12_DT_SLEEP_15_ODR`

```c
#define LIS2DW12_DT_SLEEP_15_ODR 15
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

15 个输出数据速率周期（ODR Period）。

<a id="gaf43f42617789c1482e1ddf1d9abd7c3d"></a>

### `LIS2DW12_DT_SLEEP_1_ODR`

```c
#define LIS2DW12_DT_SLEEP_1_ODR 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

1 个输出数据速率周期（ODR Period）。

<a id="ga6c76600bf9baff0483d5865ba98aa75e"></a>

### `LIS2DW12_DT_SLEEP_2_ODR`

```c
#define LIS2DW12_DT_SLEEP_2_ODR 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

2 个输出数据速率周期（ODR Period）。

<a id="gaf294baab225caba1e4931abfee9660b8"></a>

### `LIS2DW12_DT_SLEEP_3_ODR`

```c
#define LIS2DW12_DT_SLEEP_3_ODR 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

3 个输出数据速率周期（ODR Period）。

<a id="gac45de707e5c1ee485b5cdd95ce3332af"></a>

### `LIS2DW12_DT_SLEEP_4_ODR`

```c
#define LIS2DW12_DT_SLEEP_4_ODR 4
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

4 个输出数据速率周期（ODR Period）。

<a id="ga904ec47239d01ac05218bee5fa2f4235"></a>

### `LIS2DW12_DT_SLEEP_5_ODR`

```c
#define LIS2DW12_DT_SLEEP_5_ODR 5
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

5 个输出数据速率周期（ODR Period）。

<a id="ga552a71243df2cfe6dcc6f9ca5a4208c9"></a>

### `LIS2DW12_DT_SLEEP_6_ODR`

```c
#define LIS2DW12_DT_SLEEP_6_ODR 6
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

6 个输出数据速率周期（ODR Period）。

<a id="ga72ced204873bfce192b6bcfc9d823ffc"></a>

### `LIS2DW12_DT_SLEEP_7_ODR`

```c
#define LIS2DW12_DT_SLEEP_7_ODR 7
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

7 个输出数据速率周期（ODR Period）。

<a id="ga9078b4d1fa77dd53871ddbc7715b3f0c"></a>

### `LIS2DW12_DT_SLEEP_8_ODR`

```c
#define LIS2DW12_DT_SLEEP_8_ODR 8
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

8 个输出数据速率周期（ODR Period）。

<a id="ga979e47f3dda9c72b92d87bb3fc5b3e4f"></a>

### `LIS2DW12_DT_SLEEP_9_ODR`

```c
#define LIS2DW12_DT_SLEEP_9_ODR 9
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

9 个输出数据速率周期（ODR Period）。

<a id="ga1bcffaa1b8439f626164b736be17f9db"></a>

### `LIS2DW12_DT_WAKEUP_1_ODR`

```c
#define LIS2DW12_DT_WAKEUP_1_ODR 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

1 个输出数据速率周期（ODR Period）。

<a id="ga53457e3a0d24bf3599ff779f3a559fb4"></a>

### `LIS2DW12_DT_WAKEUP_2_ODR`

```c
#define LIS2DW12_DT_WAKEUP_2_ODR 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

2 个输出数据速率周期（ODR Period）。

<a id="ga580dd3e03a377fce36db7916c254b52a"></a>

### `LIS2DW12_DT_WAKEUP_3_ODR`

```c
#define LIS2DW12_DT_WAKEUP_3_ODR 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

3 个输出数据速率周期（ODR Period）。

<a id="gaae58921652443e8f7757b38ade589c49"></a>

### `LIS2DW12_DT_WAKEUP_4_ODR`

```c
#define LIS2DW12_DT_WAKEUP_4_ODR 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2dw12.h>
```

4 个输出数据速率周期（ODR Period）。


## 10.9\_原页交叉引用（Cross References）

- [lis2dw12.h](../api_file_mesh_interrupt_reference/P014_zephyr__dt-bindings__sensor__lis2dw12.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P009_INA230 API主题.md) · [返回大纲](大纲.md) · [下一章](P011_MCP9600 API主题.md)
