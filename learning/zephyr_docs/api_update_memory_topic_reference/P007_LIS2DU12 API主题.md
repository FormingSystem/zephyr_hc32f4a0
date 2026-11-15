---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-7
title: LIS2DU12 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lis2du12__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_LIS2DU12 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lis2du12__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STMicroelectronics LIS2DU12 三轴加速度计（3-axis accelerometer）。

<a id="details"></a>

STMicroelectronics LIS2DU12 三轴加速度计（3-axis accelerometer）。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_lis2du12_2Eh"></a>

```c
file lis2du12.h
```

相关声明：[lis2du12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2du12_8h.html)。

the ST LIS2DU12 accelerometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 7.2\_加速度计满量程范围（Accelerometer full-scale range）

设备树 `accel-range` 属性的取值。

<a id="r_ga2b42fd439750df2fb03d62a9c657fca1"></a>

```c
#define LIS2DU12_DT_FS_2G 0
```

相关声明：[LIS2DU12_DT_FS_2G](#ga2b42fd439750df2fb03d62a9c657fca1)。

量程（range）：±2 g。

<a id="r_ga3465e147dab6ce4b85fbdf2709e39613"></a>

```c
#define LIS2DU12_DT_FS_4G 1
```

相关声明：[LIS2DU12_DT_FS_4G](#ga3465e147dab6ce4b85fbdf2709e39613)。

量程（range）：±4 g。

<a id="r_gaf1b1956d5a808fca2dbaab01845bcf5e"></a>

```c
#define LIS2DU12_DT_FS_8G 2
```

相关声明：[LIS2DU12_DT_FS_8G](#gaf1b1956d5a808fca2dbaab01845bcf5e)。

量程（range）：±8 g。

<a id="r_ga07253b36548b1ae59171576a8e7e2115"></a>

```c
#define LIS2DU12_DT_FS_16G 3
```

相关声明：[LIS2DU12_DT_FS_16G](#ga07253b36548b1ae59171576a8e7e2115)。

量程（range）：±16 g。

## 7.3\_加速度计输出数据率（Accelerometer output data rate）

设备树（Devicetree）属性 `accel-odr` 的取值。

超低功耗模式（Ultra-low-power Mode，ULP）。

<a id="r_ga3a76a7b040855274d5e8b00ea522654d"></a>

```c
#define LIS2DU12_DT_ODR_OFF 0x00
```

相关声明：[LIS2DU12_DT_ODR_OFF](#ga3a76a7b040855274d5e8b00ea522654d)。

掉电（Power-down）。

<a id="r_gac1c54a059fbfb427f975fc0961343e28"></a>

```c
#define LIS2DU12_DT_ODR_AT_1Hz6_ULP 0x01
```

相关声明：[LIS2DU12_DT_ODR_AT_1Hz6_ULP](#gac1c54a059fbfb427f975fc0961343e28)。

1.6 Hz，超低功耗（ULP）模式。

<a id="r_ga64606f40cd014eae9d89c929168c5e0f"></a>

```c
#define LIS2DU12_DT_ODR_AT_3Hz_ULP 0x02
```

相关声明：[LIS2DU12_DT_ODR_AT_3Hz_ULP](#ga64606f40cd014eae9d89c929168c5e0f)。

3 Hz，超低功耗（ULP）模式。

<a id="r_gab54ebbbe8991aa268c0dbaae4427fcd8"></a>

```c
#define LIS2DU12_DT_ODR_AT_6Hz_ULP 0x03
```

相关声明：[LIS2DU12_DT_ODR_AT_6Hz_ULP](#gab54ebbbe8991aa268c0dbaae4427fcd8)。

6 Hz，超低功耗（ULP）模式。

<a id="r_gaf135c2f1fd176eef32ee45ec09010213"></a>

```c
#define LIS2DU12_DT_ODR_AT_6Hz 0x04
```

相关声明：[LIS2DU12_DT_ODR_AT_6Hz](#gaf135c2f1fd176eef32ee45ec09010213)。

6 Hz，正常（Normal）模式。

<a id="r_ga421b54616308f44cd796b4553ccbd93d"></a>

```c
#define LIS2DU12_DT_ODR_AT_12Hz 0x05
```

相关声明：[LIS2DU12_DT_ODR_AT_12Hz](#ga421b54616308f44cd796b4553ccbd93d)。

12.5 Hz，正常（Normal）模式。

<a id="r_gad3aaa0a89d8e90cac5e67a52b63e2c7e"></a>

```c
#define LIS2DU12_DT_ODR_AT_25Hz 0x06
```

相关声明：[LIS2DU12_DT_ODR_AT_25Hz](#gad3aaa0a89d8e90cac5e67a52b63e2c7e)。

25 Hz，正常（Normal）模式。

<a id="r_gac444fac795f58756c3d5dd469412bba1"></a>

```c
#define LIS2DU12_DT_ODR_AT_50Hz 0x07
```

相关声明：[LIS2DU12_DT_ODR_AT_50Hz](#gac444fac795f58756c3d5dd469412bba1)。

50 Hz，正常（Normal）模式。

<a id="r_ga2f43a631e26e62246d9b198b48b3c10e"></a>

```c
#define LIS2DU12_DT_ODR_AT_100Hz 0x08
```

相关声明：[LIS2DU12_DT_ODR_AT_100Hz](#ga2f43a631e26e62246d9b198b48b3c10e)。

100 Hz，正常（Normal）模式。

<a id="r_ga11789548c0055a69e0899dcd8590df07"></a>

```c
#define LIS2DU12_DT_ODR_AT_200Hz 0x09
```

相关声明：[LIS2DU12_DT_ODR_AT_200Hz](#ga11789548c0055a69e0899dcd8590df07)。

200 Hz，正常（Normal）模式。

<a id="r_gaa728d2f438efffdcd6eb607efa5db714"></a>

```c
#define LIS2DU12_DT_ODR_AT_400Hz 0x0a
```

相关声明：[LIS2DU12_DT_ODR_AT_400Hz](#gaa728d2f438efffdcd6eb607efa5db714)。

400 Hz，正常（Normal）模式。

<a id="r_ga1ab1a8891428768cbdfedf3f281ff9fb"></a>

```c
#define LIS2DU12_DT_ODR_AT_800Hz 0x0b
```

相关声明：[LIS2DU12_DT_ODR_AT_800Hz](#ga1ab1a8891428768cbdfedf3f281ff9fb)。

800 Hz，正常（Normal）模式。

<a id="r_ga5b1ec0132ce400ce9207b100a1926687"></a>

```c
#define LIS2DU12_DT_ODR_TRIG_PIN 0x0e
```

相关声明：[LIS2DU12_DT_ODR_TRIG_PIN](#ga5b1ec0132ce400ce9207b100a1926687)。

通过 INT2 执行单次采样（Single-shot），高延迟（High Latency）。

<a id="r_gaf3389a81e1bc4ce6a9965ad6ba828963"></a>

```c
#define LIS2DU12_DT_ODR_TRIG_SW 0x0f
```

相关声明：[LIS2DU12_DT_ODR_TRIG_SW](#gaf3389a81e1bc4ce6a9965ad6ba828963)。

通过总线执行单次采样（Single-shot），高延迟（High Latency）。

## 7.4\_详细说明（Detailed Documentation）

<a id="ga07253b36548b1ae59171576a8e7e2115"></a>

### `LIS2DU12_DT_FS_16G`

```c
#define LIS2DU12_DT_FS_16G 3
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

量程（range）：±16 g。

<a id="ga2b42fd439750df2fb03d62a9c657fca1"></a>

### `LIS2DU12_DT_FS_2G`

```c
#define LIS2DU12_DT_FS_2G 0
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

量程（range）：±2 g。

<a id="ga3465e147dab6ce4b85fbdf2709e39613"></a>

### `LIS2DU12_DT_FS_4G`

```c
#define LIS2DU12_DT_FS_4G 1
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

量程（range）：±4 g。

<a id="gaf1b1956d5a808fca2dbaab01845bcf5e"></a>

### `LIS2DU12_DT_FS_8G`

```c
#define LIS2DU12_DT_FS_8G 2
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

量程（range）：±8 g。

<a id="ga2f43a631e26e62246d9b198b48b3c10e"></a>

### `LIS2DU12_DT_ODR_AT_100Hz`

```c
#define LIS2DU12_DT_ODR_AT_100Hz 0x08
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

100 Hz，正常（Normal）模式。

<a id="ga421b54616308f44cd796b4553ccbd93d"></a>

### `LIS2DU12_DT_ODR_AT_12Hz`

```c
#define LIS2DU12_DT_ODR_AT_12Hz 0x05
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

12.5 Hz，正常（Normal）模式。

<a id="gac1c54a059fbfb427f975fc0961343e28"></a>

### `LIS2DU12_DT_ODR_AT_1Hz6_ULP`

```c
#define LIS2DU12_DT_ODR_AT_1Hz6_ULP 0x01
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

1.6 Hz，超低功耗（ULP）模式。

<a id="ga11789548c0055a69e0899dcd8590df07"></a>

### `LIS2DU12_DT_ODR_AT_200Hz`

```c
#define LIS2DU12_DT_ODR_AT_200Hz 0x09
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

200 Hz，正常（Normal）模式。

<a id="gad3aaa0a89d8e90cac5e67a52b63e2c7e"></a>

### `LIS2DU12_DT_ODR_AT_25Hz`

```c
#define LIS2DU12_DT_ODR_AT_25Hz 0x06
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

25 Hz，正常（Normal）模式。

<a id="ga64606f40cd014eae9d89c929168c5e0f"></a>

### `LIS2DU12_DT_ODR_AT_3Hz_ULP`

```c
#define LIS2DU12_DT_ODR_AT_3Hz_ULP 0x02
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

3 Hz，超低功耗（ULP）模式。

<a id="gaa728d2f438efffdcd6eb607efa5db714"></a>

### `LIS2DU12_DT_ODR_AT_400Hz`

```c
#define LIS2DU12_DT_ODR_AT_400Hz 0x0a
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

400 Hz，正常（Normal）模式。

<a id="gac444fac795f58756c3d5dd469412bba1"></a>

### `LIS2DU12_DT_ODR_AT_50Hz`

```c
#define LIS2DU12_DT_ODR_AT_50Hz 0x07
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

50 Hz，正常（Normal）模式。

<a id="gaf135c2f1fd176eef32ee45ec09010213"></a>

### `LIS2DU12_DT_ODR_AT_6Hz`

```c
#define LIS2DU12_DT_ODR_AT_6Hz 0x04
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

6 Hz，正常（Normal）模式。

<a id="gab54ebbbe8991aa268c0dbaae4427fcd8"></a>

### `LIS2DU12_DT_ODR_AT_6Hz_ULP`

```c
#define LIS2DU12_DT_ODR_AT_6Hz_ULP 0x03
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

6 Hz，超低功耗（ULP）模式。

<a id="ga1ab1a8891428768cbdfedf3f281ff9fb"></a>

### `LIS2DU12_DT_ODR_AT_800Hz`

```c
#define LIS2DU12_DT_ODR_AT_800Hz 0x0b
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

800 Hz，正常（Normal）模式。

<a id="ga3a76a7b040855274d5e8b00ea522654d"></a>

### `LIS2DU12_DT_ODR_OFF`

```c
#define LIS2DU12_DT_ODR_OFF 0x00
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

掉电（Power-down）。

<a id="ga5b1ec0132ce400ce9207b100a1926687"></a>

### `LIS2DU12_DT_ODR_TRIG_PIN`

```c
#define LIS2DU12_DT_ODR_TRIG_PIN 0x0e
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

通过 INT2 执行单次采样（Single-shot），高延迟（High Latency）。

<a id="gaf3389a81e1bc4ce6a9965ad6ba828963"></a>

### `LIS2DU12_DT_ODR_TRIG_SW`

```c
#define LIS2DU12_DT_ODR_TRIG_SW 0x0f
```

```c
#include <zephyr/dt-bindings/sensor/lis2du12.h>
```

通过总线执行单次采样（Single-shot），高延迟（High Latency）。


## 7.5\_原页交叉引用（Cross References）

- [lis2du12.h](https://docs.zephyrproject.org/latest/doxygen/html/lis2du12_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P006_LIN 收发器（LIN Transceiver）.md) · [返回大纲](大纲.md) · [下一章](P008_向量偏移（Vector Offset）.md)
