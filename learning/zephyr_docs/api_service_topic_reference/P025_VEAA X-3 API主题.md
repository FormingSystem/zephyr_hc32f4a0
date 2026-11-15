---
id: learning.zephyr-docs.api-service-topic-reference.page-25
title: VEAA X-3 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_VEAA X-3 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Festo VEAA X-3 压力调节器（Pressure regulator）。

<a id="details"></a>

Festo VEAA X-3 压力调节器（Pressure regulator）。

<a id="header-files"></a>
<a id="files"></a>

## 25.1\_文件（Files）

<a id="r_veaa_5Fx_5F3_2Eh"></a>

```c
file veaa_x_3.h
```

相关声明：[veaa_x_3.h](../api_file_supplement_reference/P127_zephyr__drivers__sensor__veaa_x_3.h_文件参考.md)。

VEAA X-3传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.2\_枚举（Enumerations）

<a id="r_ga0766ed6ec5cca998f67ae8061ee9e862"></a>

```c
enum sensor_attribute_veaa_x_3 { SENSOR_ATTR_VEAA_X_3_SETPOINT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEAA_X_3_RANGE }
```

相关声明：[sensor_attribute_veaa_x_3](#ga0766ed6ec5cca998f67ae8061ee9e862)、[SENSOR_ATTR_VEAA_X_3_SETPOINT](#gga0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3)、[SENSOR_ATTR_VEAA_X_3_RANGE](#gga0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc)。

VEAA X-3 的自定义传感器属性（Custom Sensor Attributes）。

## 25.3\_详细说明（Detailed Documentation）

<a id="ga0766ed6ec5cca998f67ae8061ee9e862"></a>

### `sensor_attribute_veaa_x_3`

```c
enum sensor_attribute_veaa_x_3
```

```c
#include <zephyr/drivers/sensor/veaa_x_3.h>
```

VEAA X-3 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_VEAA_X_3_SETPOINT` | 设置压力设定点（Pressure Setpoint），单位为千帕（kPa）。 |
| `SENSOR_ATTR_VEAA_X_3_RANGE` | 支持的压力范围（Pressure Range），单位为千帕（kPa）。`sensor_value.val1` 和 `sensor_value.val2` 分别为支持的最低和最高压力。 |


## 25.4\_原页交叉引用（Cross References）

- [veaa_x_3.h](../api_file_supplement_reference/P127_zephyr__drivers__sensor__veaa_x_3.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3"></a>
<a id="gga0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc"></a>

---

[上一章](P024_串行线调试端口（SWDP）.md) · [返回大纲](大纲.md) · [下一章](P026_WSEN-PADS-2511020213301 API主题.md)
