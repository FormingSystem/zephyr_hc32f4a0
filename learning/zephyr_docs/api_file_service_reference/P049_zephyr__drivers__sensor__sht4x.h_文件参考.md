---
id: learning.zephyr-docs.api-file-service-reference.page-49
title: zephyr__drivers__sensor__sht4x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_zephyr\_\_drivers\_\_sensor\_\_sht4x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SHT4X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

SHT4X 传感器扩展 API（Extended Sensor API）的头文件。它公开片上加热器（On-Chip Heater）的 API；加热器的使用因应用／环境而异，无法通过通用传感器驱动抽象（Sensor Driver Abstraction）表达。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 49.1\_宏定义（Macros）

<a id="r_gaf10d0155ec46d5b5152251d02f7578ee"></a>

```c
#define SHT4X_HEATER_MAX_TEMP 65
```

相关声明：[SHT4X_HEATER_MAX_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gaf10d0155ec46d5b5152251d02f7578ee)。

最高温度（Maximum Temperature）；超过该温度时不应使用加热器（Heater）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 49.2\_枚举（Enumerations）

<a id="r_ga4191e02c97b8130a1c96d47c0939d535"></a>

```c
enum sensor_attribute_sht4x { SENSOR_ATTR_SHT4X_HEATER_POWER = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SHT4X_HEATER_DURATION }
```

相关声明：[sensor_attribute_sht4x](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#ga4191e02c97b8130a1c96d47c0939d535)、[SENSOR_ATTR_SHT4X_HEATER_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052)、[SENSOR_ATTR_SHT4X_HEATER_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)。

SHT4X 的自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 49.3\_函数（Functions）

<a id="r_gaf2539064f44eb3981cb40a3c2f7a0eb8"></a>

```c
int sht4x_fetch_with_heater (const struct device *dev)
```

相关声明：[sht4x_fetch_with_heater](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gaf2539064f44eb3981cb40a3c2f7a0eb8)、[device](../device_reference/P002_设备对象结构.md)。

使用片上加热器（On-Chip Heater）获取数据（Fetch Data）。


## 49.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P781_sht4x.h_源码浏览.md)
- [SHT4X_HEATER_MAX_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gaf10d0155ec46d5b5152251d02f7578ee)
- [sensor_attribute_sht4x](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#ga4191e02c97b8130a1c96d47c0939d535)
- [SENSOR_ATTR_SHT4X_HEATER_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052)
- [SENSOR_ATTR_SHT4X_HEATER_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)
- [sht4x_fetch_with_heater](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gaf2539064f44eb3981cb40a3c2f7a0eb8)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>

---

[上一章](P048_zephyr__drivers__sensor__scd4x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P050_zephyr__dt-bindings__pinctrl__si32-pinctrl.h_文件参考.md)
