---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-1
title: AFBR-S50 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_AFBR-S50 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__afbr__s50__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Broadcom AFBR-S50 三维飞行时间（3D ToF）传感器。

<a id="details"></a>

Broadcom AFBR-S50 三维飞行时间（3D ToF）传感器，即 Broadcom AFBR-S50 飞行时间测距传感器（Time-of-flight Distance Sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_afbr_5Fs50_2Eh"></a>

```c
file afbr_s50.h
```

相关声明：[afbr_s50.h](../api_file_configuration_reference/P017_zephyr__drivers__sensor__afbr_s50.h_文件参考.md)。

AFBR-S50传感器的扩展API头文件（Extended Sensor API Header）。

```c
file afbr_s50.h
```

相关声明：[afbr_s50.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html)。

the Broadcom AFBR-S50 ToF sensor的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_ga026e02d538d6e283b7b1136470e6e478"></a>

```c
#define AFBR_PIXEL_INVALID_VALUE 0x80000000
```

相关声明：[AFBR_PIXEL_INVALID_VALUE](#ga026e02d538d6e283b7b1136470e6e478)。

若像素读数（Pixel Reading）包含此值，则忽略该读数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga2be1db0094a49e8e59310b8c8137e54f"></a>

```c
enum sensor_channel_afbr_s50 { SENSOR_CHAN_AFBR_S50_PIXELS = SENSOR_CHAN_PRIV_START + 1 }
```

相关声明：[sensor_channel_afbr_s50](#ga2be1db0094a49e8e59310b8c8137e54f)、[SENSOR_CHAN_AFBR_S50_PIXELS](#gga2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7)。

AFBR-S50 的自定义传感器通道（Custom Sensor Channels）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.4\_双频模式选项（Dual-frequency Mode Options）

设备树属性（Devicetree Property）`dual-freq-mode` 的取值。

双频模式（Dual-frequency Mode）结合两个调制频率下的测量结果，扩展无模糊量程（Unambiguous Range）。

<a id="r_ga8876f0466109e96bdfea3fc533180539"></a>

```c
#define AFBR_S50_DT_DFM_MODE_OFF 0
```

相关声明：[AFBR_S50_DT_DFM_MODE_OFF](#ga8876f0466109e96bdfea3fc533180539)。

禁用（Disabled）。

<a id="r_gad3b8e0c86fe0ef50ff8b134bb952b6ee"></a>

```c
#define AFBR_S50_DT_DFM_MODE_4X 1
```

相关声明：[AFBR_S50_DT_DFM_MODE_4X](#gad3b8e0c86fe0ef50ff8b134bb952b6ee)。

4 倍量程扩展（4x Range Extension）。

<a id="r_ga142b78ba68727d9c85dbe243503dff65"></a>

```c
#define AFBR_S50_DT_DFM_MODE_8X 2
```

相关声明：[AFBR_S50_DT_DFM_MODE_8X](#ga142b78ba68727d9c85dbe243503dff65)。

8 倍量程扩展（8x Range Extension）。

## 1.5\_测量模式（Measurement Modes）

设备树属性（Devicetree Property）`measurement-mode` 的取值。

带 `laser-class-2` 后缀的模式会提高光学输出功率（Optical Output Power）。

<a id="r_gadfe6cccf720230f57a84d366733fab31"></a>

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE 1
```

相关声明：[AFBR_S50_DT_MODE_SHORT_RANGE](#gadfe6cccf720230f57a84d366733fab31)。

短量程（Short Range）。

<a id="r_ga44f255c5f786d435a06a134ef6f1f767"></a>

```c
#define AFBR_S50_DT_MODE_LONG_RANGE 2
```

相关声明：[AFBR_S50_DT_MODE_LONG_RANGE](#ga44f255c5f786d435a06a134ef6f1f767)。

长量程（Long Range）。

<a id="r_gaee1514551ef77c017071231509c51f16"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE 5
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE](#gaee1514551ef77c017071231509c51f16)。

高速短量程（High-speed Short Range）。

<a id="r_gad28361ea69a29cc5c4e6a856a3fa59e4"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE 6
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE](#gad28361ea69a29cc5c4e6a856a3fa59e4)。

高速长量程（High-speed Long Range）。

<a id="r_ga7859e170d43d8b0741601abf10ce23bd"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE 9
```

相关声明：[AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE](#ga7859e170d43d8b0741601abf10ce23bd)。

高精度短量程（High-precision Short Range）。

<a id="r_ga0c7b3995f3df932279d03771f41f1fe1"></a>

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2 129
```

相关声明：[AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2](#ga0c7b3995f3df932279d03771f41f1fe1)。

短量程（Short Range），2 类激光（Laser Class 2）。

<a id="r_gaa4f9e151e35ae38abf0e9488029a1258"></a>

```c
#define AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2 130
```

相关声明：[AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2](#gaa4f9e151e35ae38abf0e9488029a1258)。

长量程（Long Range），2 类激光（Laser Class 2）。

<a id="r_ga673e118c7fc92d0cb83f30f599f45209"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2 133
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2](#ga673e118c7fc92d0cb83f30f599f45209)。

高速短量程（High-speed Short Range），2 类激光（Laser Class 2）。

<a id="r_gad4b8aa14142578155e83adb7ee0e83b5"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2 134
```

相关声明：[AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2](#gad4b8aa14142578155e83adb7ee0e83b5)。

高速长量程（High-speed Long Range），2 类激光（Laser Class 2）。

<a id="r_ga2d7544987a12b451812e3fc259a851ef"></a>

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2 137
```

相关声明：[AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2](#ga2d7544987a12b451812e3fc259a851ef)。

高精度短量程（High-precision Short Range），2 类激光（Laser Class 2）。

## 1.6\_详细说明（Detailed Documentation）

<a id="ga026e02d538d6e283b7b1136470e6e478"></a>

### `AFBR_PIXEL_INVALID_VALUE`

```c
#define AFBR_PIXEL_INVALID_VALUE 0x80000000
```

```c
#include <zephyr/drivers/sensor/afbr_s50.h>
```

若像素读数（Pixel Reading）包含此值，则忽略该读数。

<a id="gad3b8e0c86fe0ef50ff8b134bb952b6ee"></a>

### `AFBR_S50_DT_DFM_MODE_4X`

```c
#define AFBR_S50_DT_DFM_MODE_4X 1
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

4 倍量程扩展（4x Range Extension）。

<a id="ga142b78ba68727d9c85dbe243503dff65"></a>

### `AFBR_S50_DT_DFM_MODE_8X`

```c
#define AFBR_S50_DT_DFM_MODE_8X 2
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

8 倍量程扩展（8x Range Extension）。

<a id="ga8876f0466109e96bdfea3fc533180539"></a>

### `AFBR_S50_DT_DFM_MODE_OFF`

```c
#define AFBR_S50_DT_DFM_MODE_OFF 0
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

禁用（Disabled）。

<a id="ga7859e170d43d8b0741601abf10ce23bd"></a>

### `AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE`

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE 9
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高精度短量程（High-precision Short Range）。

<a id="ga2d7544987a12b451812e3fc259a851ef"></a>

### `AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2`

```c
#define AFBR_S50_DT_MODE_HIGH_PRECISION_SHORT_RANGE_LASER_CLASS_2 137
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高精度短量程（High-precision Short Range），2 类激光（Laser Class 2）。

<a id="gad28361ea69a29cc5c4e6a856a3fa59e4"></a>

### `AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE`

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE 6
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高速长量程（High-speed Long Range）。

<a id="gad4b8aa14142578155e83adb7ee0e83b5"></a>

### `AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2`

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_LONG_RANGE_LASER_CLASS_2 134
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高速长量程（High-speed Long Range），2 类激光（Laser Class 2）。

<a id="gaee1514551ef77c017071231509c51f16"></a>

### `AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE`

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE 5
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高速短量程（High-speed Short Range）。

<a id="ga673e118c7fc92d0cb83f30f599f45209"></a>

### `AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2`

```c
#define AFBR_S50_DT_MODE_HIGH_SPEED_SHORT_RANGE_LASER_CLASS_2 133
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

高速短量程（High-speed Short Range），2 类激光（Laser Class 2）。

<a id="ga44f255c5f786d435a06a134ef6f1f767"></a>

### `AFBR_S50_DT_MODE_LONG_RANGE`

```c
#define AFBR_S50_DT_MODE_LONG_RANGE 2
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

长量程（Long Range）。

<a id="gaa4f9e151e35ae38abf0e9488029a1258"></a>

### `AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2`

```c
#define AFBR_S50_DT_MODE_LONG_RANGE_LASER_CLASS_2 130
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

长量程（Long Range），2 类激光（Laser Class 2）。

<a id="gadfe6cccf720230f57a84d366733fab31"></a>

### `AFBR_S50_DT_MODE_SHORT_RANGE`

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE 1
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

短量程（Short Range）。

<a id="ga0c7b3995f3df932279d03771f41f1fe1"></a>

### `AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2`

```c
#define AFBR_S50_DT_MODE_SHORT_RANGE_LASER_CLASS_2 129
```

```c
#include <zephyr/dt-bindings/sensor/afbr_s50.h>
```

短量程（Short Range），2 类激光（Laser Class 2）。

<a id="ga2be1db0094a49e8e59310b8c8137e54f"></a>

### `sensor_channel_afbr_s50`

```c
enum sensor_channel_afbr_s50
```

```c
#include <zephyr/drivers/sensor/afbr_s50.h>
```

AFBR-S50 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_AFBR_S50_PIXELS` | 获取像素矩阵（Matrix of Pixels），读数单位为米。传感器一次读取最多支持 32 个像素，组成 `4 × 8` 矩阵。 |


## 1.7\_原页交叉引用（Cross References）

- [afbr_s50.h](../api_file_configuration_reference/P017_zephyr__drivers__sensor__afbr_s50.h_文件参考.md)
- [afbr_s50.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2afbr__s50_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7"></a>

---

[返回大纲](大纲.md) · [下一章](P002_当前时间服务（Current Time Service，CTS）.md)
