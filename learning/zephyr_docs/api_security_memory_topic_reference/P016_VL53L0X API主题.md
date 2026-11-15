---
id: learning.zephyr-docs.api-security-memory-topic-reference.page-16
title: VL53L0X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_VL53L0X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__vl53l0x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ST VL53L0X 飞行时间测距传感器（Time-of-flight ranging sensor）。

<a id="details"></a>

ST VL53L0X 飞行时间测距传感器（Time-of-flight ranging sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 16.1\_文件（Files）

<a id="r_vl53l0x_2Eh"></a>

```c
file vl53l0x.h
```

相关声明：[vl53l0x.h](../api_file_network_device_reference/P042_zephyr__drivers__sensor__vl53l0x.h_文件参考.md)。

VL53L0X飞行时间（ToF）传感器的自定义通道和值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.2\_枚举（Enumerations）

<a id="r_gaca3102e6b764e2a96732648325a93690"></a>

```c
enum sensor_channel_vl53l0x { SENSOR_CHAN_VL53L0X_RANGE_DMAX = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS , SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS , SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT , SENSOR_CHAN_VL53L0X_RANGE_STATUS }
```

相关声明：[sensor_channel_vl53l0x](#gaca3102e6b764e2a96732648325a93690)、[SENSOR_CHAN_VL53L0X_RANGE_DMAX](#ggaca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161)、[SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS](#ggaca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172)、[SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS](#ggaca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e)、[SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT](#ggaca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19)、[SENSOR_CHAN_VL53L0X_RANGE_STATUS](#ggaca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)。

VL53L0X 的自定义传感器通道（Custom Sensor Channels）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 16.3\_VL53L0X 测量状态值（Measurement Status Values）

由 `SENSOR_CHAN_VL53L0X_RANGE_STATUS` 在 `sensor_value.val1` 中报告。

<a id="r_gac0ba15e7b164d53a46f88eb3807d015d"></a>

```c
#define VL53L0X_RANGE_STATUS_RANGE_VALID (0)
```

相关声明：[VL53L0X_RANGE_STATUS_RANGE_VALID](#gac0ba15e7b164d53a46f88eb3807d015d)。

距离测量（Range Measurement）有效。

<a id="r_ga4b96413c5d9569b0f8037a4613b220a7"></a>

```c
#define VL53L0X_RANGE_STATUS_SIGMA_FAIL (1)
```

相关声明：[VL53L0X_RANGE_STATUS_SIGMA_FAIL](#ga4b96413c5d9569b0f8037a4613b220a7)。

Sigma 噪声检查（Noise Check）失败。

<a id="r_gaf7317fa7071929096d3413b60f620ea1"></a>

```c
#define VL53L0X_RANGE_STATUS_SIGNAL_FAIL (2)
```

相关声明：[VL53L0X_RANGE_STATUS_SIGNAL_FAIL](#gaf7317fa7071929096d3413b60f620ea1)。

信号电平检查（Signal Level Check）失败。

<a id="r_ga96dd67966d2d8b4d2eb16a5ac8b9724e"></a>

```c
#define VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL (3)
```

相关声明：[VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL](#ga96dd67966d2d8b4d2eb16a5ac8b9724e)。

目标低于最小可测距离（Minimum Measurable Range）。

<a id="r_ga4d4565e46665ca56a5143b1868aabbda"></a>

```c
#define VL53L0X_RANGE_STATUS_PHASE_FAIL (4)
```

相关声明：[VL53L0X_RANGE_STATUS_PHASE_FAIL](#ga4d4565e46665ca56a5143b1868aabbda)。

相位检查（Phase Check）失败，目标超出量程。

<a id="r_ga6c7cbe25fbf1603f37d53fb81bc606df"></a>

```c
#define VL53L0X_RANGE_STATUS_HARDWARE_FAIL (5)
```

相关声明：[VL53L0X_RANGE_STATUS_HARDWARE_FAIL](#ga6c7cbe25fbf1603f37d53fb81bc606df)。

硬件故障（Hardware Failure）。

<a id="r_ga78056dcc0a8aa02321a4acf8c23bd5d1"></a>

```c
#define VL53L0X_RANGE_STATUS_NO_UPDATE (255)
```

相关声明：[VL53L0X_RANGE_STATUS_NO_UPDATE](#ga78056dcc0a8aa02321a4acf8c23bd5d1)。

没有新的测量结果（Measurement）可用。

## 16.4\_详细说明（Detailed Documentation）

<a id="ga6c7cbe25fbf1603f37d53fb81bc606df"></a>

### `VL53L0X_RANGE_STATUS_HARDWARE_FAIL`

```c
#define VL53L0X_RANGE_STATUS_HARDWARE_FAIL (5)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

硬件故障（Hardware Failure）。

<a id="ga96dd67966d2d8b4d2eb16a5ac8b9724e"></a>

### `VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL`

```c
#define VL53L0X_RANGE_STATUS_MIN_RANGE_FAIL (3)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

目标低于最小可测距离（Minimum Measurable Range）。

<a id="ga78056dcc0a8aa02321a4acf8c23bd5d1"></a>

### `VL53L0X_RANGE_STATUS_NO_UPDATE`

```c
#define VL53L0X_RANGE_STATUS_NO_UPDATE (255)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

没有新的测量结果（Measurement）可用。

<a id="ga4d4565e46665ca56a5143b1868aabbda"></a>

### `VL53L0X_RANGE_STATUS_PHASE_FAIL`

```c
#define VL53L0X_RANGE_STATUS_PHASE_FAIL (4)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

相位检查（Phase Check）失败，目标超出量程。

<a id="gac0ba15e7b164d53a46f88eb3807d015d"></a>

### `VL53L0X_RANGE_STATUS_RANGE_VALID`

```c
#define VL53L0X_RANGE_STATUS_RANGE_VALID (0)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

距离测量（Range Measurement）有效。

<a id="ga4b96413c5d9569b0f8037a4613b220a7"></a>

### `VL53L0X_RANGE_STATUS_SIGMA_FAIL`

```c
#define VL53L0X_RANGE_STATUS_SIGMA_FAIL (1)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

Sigma 噪声检查（Noise Check）失败。

<a id="gaf7317fa7071929096d3413b60f620ea1"></a>

### `VL53L0X_RANGE_STATUS_SIGNAL_FAIL`

```c
#define VL53L0X_RANGE_STATUS_SIGNAL_FAIL (2)
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

信号电平检查（Signal Level Check）失败。

<a id="gaca3102e6b764e2a96732648325a93690"></a>

### `sensor_channel_vl53l0x`

```c
enum sensor_channel_vl53l0x
```

```c
#include <zephyr/drivers/sensor/vl53l0x.h>
```

VL53L0X 的自定义传感器通道（Custom Sensor Channels）。

这些通道提供标准 Zephyr 传感器通道（Sensor Channels）未涵盖的额外传感器数据。

使用示例：

原始示例（Example）：

```c
#include <zephyr/drivers/sensor/vl53l0x.h>

if (sensor_channel_get(dev, SENSOR_CHAN_VL53L0X_RANGE_STATUS, &value)) {
     printk("Status: %d\n", value.val1);
}
```

每个通道通过 `sensor_value` 结构体返回值。除非另有说明，`sensor_value.val2` 不使用，始终为 0。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_VL53L0X_RANGE_DMAX` | 设备可测量的最大距离（Maximum Range），单位为米。`sensor_value.val1` 是距离的整数部分，`sensor_value.val2` 是小数部分，以百万分之一米为单位。 |
| `SENSOR_CHAN_VL53L0X_SIGNAL_RATE_RTN_CPS` | 回波信号率（Return Signal Rate），单位为每秒计数（CPS）。`sensor_value.val1` 为该信号率。 |
| `SENSOR_CHAN_VL53L0X_AMBIENT_RATE_RTN_CPS` | 环境信号率（Ambient Signal Rate），单位为每秒计数（CPS）。`sensor_value.val1` 为该环境信号率。 |
| `SENSOR_CHAN_VL53L0X_EFFECTIVE_SPAD_RTN_COUNT` | 用于回波测量的有效单光子雪崩二极管（SPAD）数量。`sensor_value.val1` 为整数 SPAD 数量。 |
| `SENSOR_CHAN_VL53L0X_RANGE_STATUS` | 最近一次测量的距离状态（Range Status）。`sensor_value.val1` 为某个距离状态值。 |


## 16.5\_原页交叉引用（Cross References）

- [vl53l0x.h](../api_file_network_device_reference/P042_zephyr__drivers__sensor__vl53l0x.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_channel_get](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ga9e0e6c1408d32c52267984bae7cb268d)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="vl53l0x_range_status_values"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="agroup__sensor__interface_html_ga9e0e6c1408d32c52267984bae7cb268d"></a>
<a id="agroup__vl53l0x__interface_html_ggaca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="avl53l0x_8h_html"></a>
<a id="ggaca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161"></a>
<a id="ggaca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172"></a>
<a id="ggaca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e"></a>
<a id="ggaca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19"></a>
<a id="ggaca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b"></a>

---

[上一章](P015_SocketCAN 库.md) · [返回大纲](大纲.md) · [下一章](P017_虚拟局域网（Virtual LAN）定义与辅助工具。.md)
