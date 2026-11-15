---
id: learning.zephyr-docs.api-device-topic-reference.page-8
title: ENS160 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ENS160 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ens160__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ScioSense ENS160 数字金属氧化物多气体传感器（Digital metal-oxide multi-gas sensor）。

<a id="details"></a>

ScioSense ENS160 数字金属氧化物多气体传感器（Digital metal-oxide multi-gas sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_ens160_2Eh"></a>

```c
file ens160.h
```

相关声明：[ens160.h](../api_file_configuration_reference/P025_zephyr__drivers__sensor__ens160.h_文件参考.md)。

ENS160传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.2\_枚举（Enumerations）

<a id="r_ga8d2ba05aa65d222313abb94ea4fbc0a5"></a>

```c
enum sensor_channel_ens160 { SENSOR_CHAN_ENS160_AQI = SENSOR_CHAN_PRIV_START }
```

相关声明：[sensor_channel_ens160](#ga8d2ba05aa65d222313abb94ea4fbc0a5)、[SENSOR_CHAN_ENS160_AQI](#gga8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56)。

ENS160 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga8005c12c1132ce8b76bd571035a37836"></a>

```c
enum sensor_attribute_ens160 { SENSOR_ATTR_ENS160_TEMP = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_ENS160_RH }
```

相关声明：[sensor_attribute_ens160](#ga8005c12c1132ce8b76bd571035a37836)、[SENSOR_ATTR_ENS160_TEMP](#gga8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be)、[SENSOR_ATTR_ENS160_RH](#gga8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608)。

ENS160 的自定义传感器属性（Custom Sensor Attributes）。

## 8.3\_详细说明（Detailed Documentation）

<a id="ga8005c12c1132ce8b76bd571035a37836"></a>

### `sensor_attribute_ens160`

```c
enum sensor_attribute_ens160
```

```c
#include <zephyr/drivers/sensor/ens160.h>
```

ENS160 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_ENS160_TEMP` | 温度补偿（temperature compensation），用于设置传感器的环境温度补偿。 |
| `SENSOR_ATTR_ENS160_RH` | 相对湿度补偿（relative humidity compensation），用于设置传感器的环境相对湿度补偿。 |

<a id="ga8d2ba05aa65d222313abb94ea4fbc0a5"></a>

### `sensor_channel_ens160`

```c
enum sensor_channel_ens160
```

```c
#include <zephyr/drivers/sensor/ens160.h>
```

ENS160 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_ENS160_AQI` | 空气质量指数（Air Quality Index，AQI）。 |


## 8.4\_原页交叉引用（Cross References）

- [ens160.h](../api_file_configuration_reference/P025_zephyr__drivers__sensor__ens160.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8005c12c1132ce8b76bd571035a37836a09b24e7aae253d6e4ee71fd57e0347be"></a>
<a id="gga8005c12c1132ce8b76bd571035a37836a23a397dcaad8efe37bc66aa54bfd3608"></a>
<a id="gga8d2ba05aa65d222313abb94ea4fbc0a5ac57da55fa36fe09123bba287ea6fef56"></a>

---

[上一章](P007_充电器驱动后端 API（Charger Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P009_FPGA 驱动后端 API（Driver Backend API）.md)
