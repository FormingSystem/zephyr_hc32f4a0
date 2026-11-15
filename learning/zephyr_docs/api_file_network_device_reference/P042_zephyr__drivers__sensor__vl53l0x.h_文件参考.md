---
id: learning.zephyr-docs.api-file-network-device-reference.page-42
title: zephyr__drivers__sensor__vl53l0x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/vl53l0x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_drivers\_\_sensor\_\_vl53l0x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/vl53l0x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

VL53L0X飞行时间（ToF）传感器的自定义通道和值。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

VL53L0X飞行时间（ToF）传感器的自定义通道和值。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.1\_宏定义（Macros）

<a id="define-members-0"></a>

### VL53L0X 测量状态值（Measurement Status Values）

由 `SENSOR_CHAN_VL53L0X_RANGE_STATUS` 在 `sensor_value.val1` 中报告。

<a id="r_gac0ba15e7b164d53a46f88eb3807d015d"></a>

```c
#define VL53L0X_RANGE_STATUS_RANGE_VALID (0)
```

相关声明：[VL53L0X_RANGE_STATUS_RANGE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gac0ba15e7b164d53a46f88eb3807d015d)。

距离测量（Range Measurement）有效。

<a id="r_ga4b96413c5d9569b0f8037a4613b220a7"></a>

```c
#define VL53L0X_RANGE_STATUS_SIGMA_FAIL (1)
```

相关声明：[VL53L0X_RANGE_STATUS_SIGMA_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga4b96413c5d9569b0f8037a4613b220a7)。

Sigma 噪声检查（Noise Check）失败。

<a id="r_gaf7317fa7071929096d3413b60f620ea1"></a>

```c
#define VL53L0X_RANGE_STATUS_SIGNAL_FAIL (2)
```

相关声明：[VL53L0X_RANGE_STATUS_SIGNAL_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gaf7317fa7071929096d3413b60f620ea1)。

信号电平检查（Signal Level Check）失败。

<a id="r_ga96dd67966d2d8b4d2eb16a5ac8b9724e"></a>

```c
#define VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL (3)
```

相关声明：[VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga96dd67966d2d8b4d2eb16a5ac8b9724e)。

目标低于最小可测距离（Minimum Measurable Range）。

<a id="r_ga4d4565e46665ca56a5143b1868aabbda"></a>

```c
#define VL53L0X_RANGE_STATUS_PHASE_FAIL (4)
```

相关声明：[VL53L0X_RANGE_STATUS_PHASE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga4d4565e46665ca56a5143b1868aabbda)。

相位检查（Phase Check）失败，目标超出量程。

<a id="r_ga6c7cbe25fbf1603f37d53fb81bc606df"></a>

```c
#define VL53L0X_RANGE_STATUS_HARDWARE_FAIL (5)
```

相关声明：[VL53L0X_RANGE_STATUS_HARDWARE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga6c7cbe25fbf1603f37d53fb81bc606df)。

硬件故障（Hardware Failure）。

<a id="r_ga78056dcc0a8aa02321a4acf8c23bd5d1"></a>

```c
#define VL53L0X_RANGE_STATUS_NO_UPDATE (255)
```

相关声明：[VL53L0X_RANGE_STATUS_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga78056dcc0a8aa02321a4acf8c23bd5d1)。

没有新的测量结果（Measurement）可用。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 42.2\_枚举（Enumerations）

<a id="r_gaca3102e6b764e2a96732648325a93690"></a>

```c
enum sensor_channel_vl53l0x { SENSOR_CHAN_VL53L0X_RANGE_DMAX = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS , SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS , SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT , SENSOR_CHAN_VL53L0X_RANGE_STATUS }
```

相关声明：[sensor_channel_vl53l0x](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gaca3102e6b764e2a96732648325a93690)、[SENSOR_CHAN_VL53L0X_RANGE_DMAX](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161)、[SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172)、[SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e)、[SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19)、[SENSOR_CHAN_VL53L0X_RANGE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)。

VL53L0X 的自定义传感器通道（Custom Sensor Channels）。


## 42.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P913_vl53l0x.h_源码浏览.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [SENSOR_CHAN_VL53L0X_RANGE_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)
- [VL53L0X_RANGE_STATUS_RANGE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gac0ba15e7b164d53a46f88eb3807d015d)
- [VL53L0X_RANGE_STATUS_SIGMA_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga4b96413c5d9569b0f8037a4613b220a7)
- [VL53L0X_RANGE_STATUS_SIGNAL_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gaf7317fa7071929096d3413b60f620ea1)
- [VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga96dd67966d2d8b4d2eb16a5ac8b9724e)
- [VL53L0X_RANGE_STATUS_PHASE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga4d4565e46665ca56a5143b1868aabbda)
- [VL53L0X_RANGE_STATUS_HARDWARE_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga6c7cbe25fbf1603f37d53fb81bc606df)
- [VL53L0X_RANGE_STATUS_NO_UPDATE](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ga78056dcc0a8aa02321a4acf8c23bd5d1)
- [sensor_channel_vl53l0x](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#gaca3102e6b764e2a96732648325a93690)
- [SENSOR_CHAN_VL53L0X_RANGE_DMAX](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161)
- [SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172)
- [SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e)
- [SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html#ggaca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19)

<a id="vl53l0x_range_status_values"></a>
<a id="header-details"></a>

---

[上一章](P041_zephyr__drivers__sensor__tcs34725.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__net__wifi_certs.h_文件参考.md)
