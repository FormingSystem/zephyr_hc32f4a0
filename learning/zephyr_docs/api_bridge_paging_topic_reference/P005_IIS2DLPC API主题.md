---
id: learning.zephyr-docs.api-bridge-paging-topic-reference.page-5
title: IIS2DLPC API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__iis2dlpc__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_IIS2DLPC API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__iis2dlpc__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics IIS2DLPC 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics IIS2DLPC 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_iis2dlpc_2Eh"></a>

```c
file iis2dlpc.h
```

相关声明：[iis2dlpc.h](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html)。

the ST IIS2DLPC accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.2\_电源模式（Power Modes）

设备树属性（Devicetree Property）`power-mode` 的取值。

<a id="r_ga1e1c2a12612d55d0d1a60e6df5cc3050"></a>

```c
#define IIS2DLPC_DT_LP_M1 0
```

相关声明：[IIS2DLPC_DT_LP_M1](#ga1e1c2a12612d55d0d1a60e6df5cc3050)。

低功耗模式（Low-power Mode）1，12 位。

<a id="r_ga52571a5d3d8e7a042a442f8d8b55029e"></a>

```c
#define IIS2DLPC_DT_LP_M2 1
```

相关声明：[IIS2DLPC_DT_LP_M2](#ga52571a5d3d8e7a042a442f8d8b55029e)。

低功耗模式（Low-power Mode）2，14 位。

<a id="r_gada77b7def23ffce8089c4773204a5ed0"></a>

```c
#define IIS2DLPC_DT_LP_M3 2
```

相关声明：[IIS2DLPC_DT_LP_M3](#gada77b7def23ffce8089c4773204a5ed0)。

低功耗模式（Low-power Mode）3，14 位。

<a id="r_gaa39b8641e427747eb81ab276b30447f9"></a>

```c
#define IIS2DLPC_DT_LP_M4 3
```

相关声明：[IIS2DLPC_DT_LP_M4](#gaa39b8641e427747eb81ab276b30447f9)。

低功耗模式（Low-power Mode）4，14 位。

<a id="r_ga623fd5c18feaac196c33265ea84aa0e8"></a>

```c
#define IIS2DLPC_DT_HP_MODE 4
```

相关声明：[IIS2DLPC_DT_HP_MODE](#ga623fd5c18feaac196c33265ea84aa0e8)。

高性能模式（High-performance Mode），14 位。

## 5.3\_滤波器带宽选项（Filter Bandwidth Options）

抗混叠滤波器（Anti-aliasing Filter）的带宽，用输出数据速率（ODR）的比例表示。

<a id="r_gabf53338af02c9036850d61f4942123fe"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_2 0
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_2](#gabf53338af02c9036850d61f4942123fe)。

输出数据速率（ODR）除以 2。

<a id="r_ga24ba2864f9a1c76f73636ab40ce977cc"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_4 1
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_4](#ga24ba2864f9a1c76f73636ab40ce977cc)。

输出数据速率（ODR）除以 4。

<a id="r_gae701e403e5b068c4188bf6ecebc5e088"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_10 2
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_10](#gae701e403e5b068c4188bf6ecebc5e088)。

输出数据速率（ODR）除以 10。

<a id="r_gab453a45f6561c03f6c2657b025fb8280"></a>

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_20 3
```

相关声明：[IIS2DLPC_DT_FILTER_BW_ODR_DIV_20](#gab453a45f6561c03f6c2657b025fb8280)。

输出数据速率（ODR）除以 20。

## 5.4\_敲击检测模式（Tap Detection Mode）

设备树属性（Devicetree Property）`tap-mode` 的取值。

<a id="r_ga52c4b179f307100adfbe341dcc8756b1"></a>

```c
#define IIS2DLPC_DT_SINGLE_TAP 0
```

相关声明：[IIS2DLPC_DT_SINGLE_TAP](#ga52c4b179f307100adfbe341dcc8756b1)。

仅单击（Single-tap Only）。

<a id="r_gae49fca709c40c78ae3001454d2277761"></a>

```c
#define IIS2DLPC_DT_SINGLE_DOUBLE_TAP 1
```

相关声明：[IIS2DLPC_DT_SINGLE_DOUBLE_TAP](#gae49fca709c40c78ae3001454d2277761)。

单击与双击（Single and Double Tap）。

## 5.5\_自由落体阈值选项（Free-fall Threshold Options）

自由落体检测阈值（Free-fall Detection Threshold）。

<a id="r_ga31b120d2c9f9271f6d6c0e6270d6869c"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_156_mg 0
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_156_mg](#ga31b120d2c9f9271f6d6c0e6270d6869c)。

156 mg（千分之一标准重力加速度）。

<a id="r_gaa03f24ea0546d41d75b7b27980ec4a03"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_219_mg 1
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_219_mg](#gaa03f24ea0546d41d75b7b27980ec4a03)。

219 mg（千分之一标准重力加速度）。

<a id="r_gaa97f60a94b60643bf8fd53ba93a213b5"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_250_mg 2
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_250_mg](#gaa97f60a94b60643bf8fd53ba93a213b5)。

250 mg（千分之一标准重力加速度）。

<a id="r_ga6958c72e3b6a4202c2e393802f44c045"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_312_mg 3
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_312_mg](#ga6958c72e3b6a4202c2e393802f44c045)。

312 mg（千分之一标准重力加速度）。

<a id="r_ga368134487e769d5b6a9a8c43caf75fb4"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_344_mg 4
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_344_mg](#ga368134487e769d5b6a9a8c43caf75fb4)。

344 mg（千分之一标准重力加速度）。

<a id="r_ga189b31dc699c5c7698289502d1d4a2c2"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_406_mg 5
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_406_mg](#ga189b31dc699c5c7698289502d1d4a2c2)。

406 mg（千分之一标准重力加速度）。

<a id="r_gabb23c1eaaa0b82d566e3c6fb24b4bf75"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_469_mg 6
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_469_mg](#gabb23c1eaaa0b82d566e3c6fb24b4bf75)。

469 mg（千分之一标准重力加速度）。

<a id="r_ga84b6e0ed1a646f349e7e166e18ef3b5d"></a>

```c
#define IIS2DLPC_DT_FF_THRESHOLD_500_mg 7
```

相关声明：[IIS2DLPC_DT_FF_THRESHOLD_500_mg](#ga84b6e0ed1a646f349e7e166e18ef3b5d)。

500 mg（千分之一标准重力加速度）。

## 5.6\_唤醒持续时间选项（Wake-up Duration Options）

唤醒事件持续时间（Wake-up Event Duration），以输出数据速率周期（ODR Periods）为单位。

<a id="r_gad369d4265e7542856d5ccd052fcb3025"></a>

```c
#define IIS2DLPC_DT_WAKEUP_1_ODR 0
```

相关声明：[IIS2DLPC_DT_WAKEUP_1_ODR](#gad369d4265e7542856d5ccd052fcb3025)。

1 个输出数据速率周期（ODR Period）。

<a id="r_gad7f6fb74463c30e726dc34ef9462993c"></a>

```c
#define IIS2DLPC_DT_WAKEUP_2_ODR 1
```

相关声明：[IIS2DLPC_DT_WAKEUP_2_ODR](#gad7f6fb74463c30e726dc34ef9462993c)。

2 个输出数据速率周期（ODR Period）。

<a id="r_gad3f89e84420074c53fc9e13a30f116a8"></a>

```c
#define IIS2DLPC_DT_WAKEUP_3_ODR 2
```

相关声明：[IIS2DLPC_DT_WAKEUP_3_ODR](#gad3f89e84420074c53fc9e13a30f116a8)。

3 个输出数据速率周期（ODR Period）。

<a id="r_ga651cadb8f638381169876dbd5291714a"></a>

```c
#define IIS2DLPC_DT_WAKEUP_4_ODR 3
```

相关声明：[IIS2DLPC_DT_WAKEUP_4_ODR](#ga651cadb8f638381169876dbd5291714a)。

4 个输出数据速率周期（ODR Period）。

## 5.7\_详细说明（Detailed Documentation）

<a id="ga31b120d2c9f9271f6d6c0e6270d6869c"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_156_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_156_mg 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

156 mg（千分之一标准重力加速度）。

<a id="gaa03f24ea0546d41d75b7b27980ec4a03"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_219_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_219_mg 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

219 mg（千分之一标准重力加速度）。

<a id="gaa97f60a94b60643bf8fd53ba93a213b5"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_250_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_250_mg 2
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

250 mg（千分之一标准重力加速度）。

<a id="ga6958c72e3b6a4202c2e393802f44c045"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_312_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_312_mg 3
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

312 mg（千分之一标准重力加速度）。

<a id="ga368134487e769d5b6a9a8c43caf75fb4"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_344_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_344_mg 4
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

344 mg（千分之一标准重力加速度）。

<a id="ga189b31dc699c5c7698289502d1d4a2c2"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_406_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_406_mg 5
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

406 mg（千分之一标准重力加速度）。

<a id="gabb23c1eaaa0b82d566e3c6fb24b4bf75"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_469_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_469_mg 6
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

469 mg（千分之一标准重力加速度）。

<a id="ga84b6e0ed1a646f349e7e166e18ef3b5d"></a>

### `IIS2DLPC_DT_FF_THRESHOLD_500_mg`

```c
#define IIS2DLPC_DT_FF_THRESHOLD_500_mg 7
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

500 mg（千分之一标准重力加速度）。

<a id="gae701e403e5b068c4188bf6ecebc5e088"></a>

### `IIS2DLPC_DT_FILTER_BW_ODR_DIV_10`

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_10 2
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

输出数据速率（ODR）除以 10。

<a id="gabf53338af02c9036850d61f4942123fe"></a>

### `IIS2DLPC_DT_FILTER_BW_ODR_DIV_2`

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_2 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

输出数据速率（ODR）除以 2。

<a id="gab453a45f6561c03f6c2657b025fb8280"></a>

### `IIS2DLPC_DT_FILTER_BW_ODR_DIV_20`

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_20 3
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

输出数据速率（ODR）除以 20。

<a id="ga24ba2864f9a1c76f73636ab40ce977cc"></a>

### `IIS2DLPC_DT_FILTER_BW_ODR_DIV_4`

```c
#define IIS2DLPC_DT_FILTER_BW_ODR_DIV_4 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

输出数据速率（ODR）除以 4。

<a id="ga623fd5c18feaac196c33265ea84aa0e8"></a>

### `IIS2DLPC_DT_HP_MODE`

```c
#define IIS2DLPC_DT_HP_MODE 4
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

高性能模式（High-performance Mode），14 位。

<a id="ga1e1c2a12612d55d0d1a60e6df5cc3050"></a>

### `IIS2DLPC_DT_LP_M1`

```c
#define IIS2DLPC_DT_LP_M1 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

低功耗模式（Low-power Mode）1，12 位。

<a id="ga52571a5d3d8e7a042a442f8d8b55029e"></a>

### `IIS2DLPC_DT_LP_M2`

```c
#define IIS2DLPC_DT_LP_M2 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

低功耗模式（Low-power Mode）2，14 位。

<a id="gada77b7def23ffce8089c4773204a5ed0"></a>

### `IIS2DLPC_DT_LP_M3`

```c
#define IIS2DLPC_DT_LP_M3 2
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

低功耗模式（Low-power Mode）3，14 位。

<a id="gaa39b8641e427747eb81ab276b30447f9"></a>

### `IIS2DLPC_DT_LP_M4`

```c
#define IIS2DLPC_DT_LP_M4 3
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

低功耗模式（Low-power Mode）4，14 位。

<a id="gae49fca709c40c78ae3001454d2277761"></a>

### `IIS2DLPC_DT_SINGLE_DOUBLE_TAP`

```c
#define IIS2DLPC_DT_SINGLE_DOUBLE_TAP 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

单击与双击（Single and Double Tap）。

<a id="ga52c4b179f307100adfbe341dcc8756b1"></a>

### `IIS2DLPC_DT_SINGLE_TAP`

```c
#define IIS2DLPC_DT_SINGLE_TAP 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

仅单击（Single-tap Only）。

<a id="gad369d4265e7542856d5ccd052fcb3025"></a>

### `IIS2DLPC_DT_WAKEUP_1_ODR`

```c
#define IIS2DLPC_DT_WAKEUP_1_ODR 0
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

1 个输出数据速率周期（ODR Period）。

<a id="gad7f6fb74463c30e726dc34ef9462993c"></a>

### `IIS2DLPC_DT_WAKEUP_2_ODR`

```c
#define IIS2DLPC_DT_WAKEUP_2_ODR 1
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

2 个输出数据速率周期（ODR Period）。

<a id="gad3f89e84420074c53fc9e13a30f116a8"></a>

### `IIS2DLPC_DT_WAKEUP_3_ODR`

```c
#define IIS2DLPC_DT_WAKEUP_3_ODR 2
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

3 个输出数据速率周期（ODR Period）。

<a id="ga651cadb8f638381169876dbd5291714a"></a>

### `IIS2DLPC_DT_WAKEUP_4_ODR`

```c
#define IIS2DLPC_DT_WAKEUP_4_ODR 3
```

```c
#include <zephyr/dt-bindings/sensor/iis2dlpc.h>
```

4 个输出数据速率周期（ODR Period）。


## 5.8\_原页交叉引用（Cross References）

- [iis2dlpc.h](https://docs.zephyrproject.org/latest/doxygen/html/iis2dlpc_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_ICM566xx API主题.md) · [返回大纲](大纲.md) · [下一章](P006_NXP i.MX952电源域（Power Domains）.md)
