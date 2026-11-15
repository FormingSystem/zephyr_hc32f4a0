---
id: learning.zephyr-docs.api-file-configuration-reference.page-7
title: zephyr__drivers__sensor__apds9960.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/apds9960_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_drivers\_\_sensor\_\_apds9960.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/apds9960_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

APDS9960传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

APDS9960传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.1\_枚举（Enumerations）

<a id="r_ga6648e8c202d0befcf33fa43aea247176"></a>

```c
enum sensor_channel_apds9960 { SENSOR_CHAN_APDS9960_GESTURE = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_apds9960](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#ga6648e8c202d0befcf33fa43aea247176)、[SENSOR_CHAN_APDS9960_GESTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga6648e8c202d0befcf33fa43aea247176a13ebf95e7c54e981a9a3876cfac9d8da)。

APDS9960 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga29b5111c1ab189c9a5607c14eaf511bf"></a>

```c
enum apds9960_gesture { APDS9960_GESTURE_NONE , APDS9960_GESTURE_UP , APDS9960_GESTURE_DOWN , APDS9960_GESTURE_LEFT , APDS9960_GESTURE_RIGHT }
```

相关声明：[apds9960_gesture](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#ga29b5111c1ab189c9a5607c14eaf511bf)、[APDS9960_GESTURE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa84aafd48b4d599473c2f8018f1f7096a)、[APDS9960_GESTURE_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa20a51800d88988f6ed9f3ec6424e02f8)、[APDS9960_GESTURE_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa5677bc9f2e794729b1901ba8eecca0ee)、[APDS9960_GESTURE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa5c2efff7945556ade307674ada20f378)、[APDS9960_GESTURE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa9ec783d15ddfa9c7251d57bd92db52d4)。

`SENSOR_CHAN_APDS9960_GESTURE` 通道通过 `sensor_value.val1` 报告的手势值（Gesture Values）。


## 7.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P033_apds9960.h_源码浏览.md)
- [sensor_channel_apds9960](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#ga6648e8c202d0befcf33fa43aea247176)
- [SENSOR_CHAN_APDS9960_GESTURE](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga6648e8c202d0befcf33fa43aea247176a13ebf95e7c54e981a9a3876cfac9d8da)
- [apds9960_gesture](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#ga29b5111c1ab189c9a5607c14eaf511bf)
- [APDS9960_GESTURE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa84aafd48b4d599473c2f8018f1f7096a)
- [APDS9960_GESTURE_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa20a51800d88988f6ed9f3ec6424e02f8)
- [APDS9960_GESTURE_DOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa5677bc9f2e794729b1901ba8eecca0ee)
- [APDS9960_GESTURE_LEFT](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa5c2efff7945556ade307674ada20f378)
- [APDS9960_GESTURE_RIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__apds9960__interface.html#gga29b5111c1ab189c9a5607c14eaf511bfa9ec783d15ddfa9c7251d57bd92db52d4)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)

<a id="header-details"></a>

---

[上一章](P006_zephyr__dt-bindings__gpio__andestech-atcgpio100.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__clock_control__arm_clock_control.h_文件参考.md)
