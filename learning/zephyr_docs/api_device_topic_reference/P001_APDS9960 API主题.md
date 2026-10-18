---
id: learning.zephyr-docs.api-device-topic-reference.page-1
title: APDS9960 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_APDS9960 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Avago APDS9960 环境光、RGB、接近和手势传感器。

<a id="details"></a>

Avago APDS9960 环境光、RGB、接近和手势传感器。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_apds9960_2Eh"></a>

```c
file apds9960.h
```

相关声明：[apds9960.h](../api_file_configuration_reference/P007_zephyr__drivers__sensor__apds9960.h_文件参考.md)。

APDS9960传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_ga6648e8c202d0befcf33fa43aea247176"></a>

```c
enum sensor_channel_apds9960 { SENSOR_CHAN_APDS9960_GESTURE = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_apds9960](#ga6648e8c202d0befcf33fa43aea247176)、[SENSOR_CHAN_APDS9960_GESTURE](#gga6648e8c202d0befcf33fa43aea247176a13ebf95e7c54e981a9a3876cfac9d8da)。

APDS9960 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga29b5111c1ab189c9a5607c14eaf511bf"></a>

```c
enum apds9960_gesture { APDS9960_GESTURE_NONE , APDS9960_GESTURE_UP , APDS9960_GESTURE_DOWN , APDS9960_GESTURE_LEFT , APDS9960_GESTURE_RIGHT }
```

相关声明：[apds9960_gesture](#ga29b5111c1ab189c9a5607c14eaf511bf)、[APDS9960_GESTURE_NONE](#gga29b5111c1ab189c9a5607c14eaf511bfa84aafd48b4d599473c2f8018f1f7096a)、[APDS9960_GESTURE_UP](#gga29b5111c1ab189c9a5607c14eaf511bfa20a51800d88988f6ed9f3ec6424e02f8)、[APDS9960_GESTURE_DOWN](#gga29b5111c1ab189c9a5607c14eaf511bfa5677bc9f2e794729b1901ba8eecca0ee)、[APDS9960_GESTURE_LEFT](#gga29b5111c1ab189c9a5607c14eaf511bfa5c2efff7945556ade307674ada20f378)、[APDS9960_GESTURE_RIGHT](#gga29b5111c1ab189c9a5607c14eaf511bfa9ec783d15ddfa9c7251d57bd92db52d4)。

`SENSOR_CHAN_APDS9960_GESTURE` 通道通过 `sensor_value.val1` 报告的手势值（Gesture Values）。

## 1.3\_详细说明（Detailed Documentation）

<a id="ga29b5111c1ab189c9a5607c14eaf511bf"></a>

### `apds9960_gesture`

```c
enum apds9960_gesture
```

```c
#include <zephyr/drivers/sensor/apds9960.h>
```

`SENSOR_CHAN_APDS9960_GESTURE` 通道通过 `sensor_value.val1` 报告的手势值（Gesture Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `APDS9960_GESTURE_NONE` | 未检测到手势（gesture）。 |
| `APDS9960_GESTURE_UP` | 向上手势（upward gesture），即手在传感器上方由下向上移动。 |
| `APDS9960_GESTURE_DOWN` | 向下手势（downward gesture），即手在传感器上方由上向下移动。 |
| `APDS9960_GESTURE_LEFT` | 向左手势（leftward gesture），即手在传感器上方由右向左移动。 |
| `APDS9960_GESTURE_RIGHT` | 向右手势（rightward gesture），即手在传感器上方由左向右移动。 |

<a id="ga6648e8c202d0befcf33fa43aea247176"></a>

### `sensor_channel_apds9960`

```c
enum sensor_channel_apds9960
```

```c
#include <zephyr/drivers/sensor/apds9960.h>
```

APDS9960 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_APDS9960_GESTURE` | 最近检测到的手势。`sensor_value.val1` 为手势值，取 `apds9960_gesture` 中的一个值；`sensor_value.val2` 未使用，始终为 0。 |


## 1.4\_原页交叉引用（Cross References）

- [apds9960.h](../api_file_configuration_reference/P007_zephyr__drivers__sensor__apds9960.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga29b5111c1ab189c9a5607c14eaf511bfa84aafd48b4d599473c2f8018f1f7096a"></a>
<a id="gga29b5111c1ab189c9a5607c14eaf511bfa20a51800d88988f6ed9f3ec6424e02f8"></a>
<a id="gga29b5111c1ab189c9a5607c14eaf511bfa5677bc9f2e794729b1901ba8eecca0ee"></a>
<a id="gga29b5111c1ab189c9a5607c14eaf511bfa5c2efff7945556ade307674ada20f378"></a>
<a id="gga29b5111c1ab189c9a5607c14eaf511bfa9ec783d15ddfa9c7251d57bd92db52d4"></a>
<a id="gga6648e8c202d0befcf33fa43aea247176a13ebf95e7c54e981a9a3876cfac9d8da"></a>

---

[返回大纲](大纲.md) · [下一章](P002_数字麦克风驱动后端 API（Digital Microphone Driver Backend API）.md)
