---
id: learning.zephyr-docs.api-connection-topic-reference.page-20
title: SHT4X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_SHT4X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sensirion SHT4X 温湿度传感器。

<a id="details"></a>

Sensirion SHT4X 温湿度传感器。

<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_sht4x_2Eh"></a>

```c
file sht4x.h
```

相关声明：[sht4x.h](../api_file_service_reference/P049_zephyr__drivers__sensor__sht4x.h_文件参考.md)。

SHT4X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.2\_宏定义（Macros）

<a id="r_gaf10d0155ec46d5b5152251d02f7578ee"></a>

```c
#define SHT4X_HEATER_MAX_TEMP 65
```

相关声明：[SHT4X_HEATER_MAX_TEMP](#gaf10d0155ec46d5b5152251d02f7578ee)。

最高温度（Maximum Temperature）；超过该温度时不应使用加热器（Heater）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 20.3\_枚举（Enumerations）

<a id="r_ga4191e02c97b8130a1c96d47c0939d535"></a>

```c
enum sensor_attribute_sht4x { SENSOR_ATTR_SHT4X_HEATER_POWER = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SHT4X_HEATER_DURATION }
```

相关声明：[sensor_attribute_sht4x](#ga4191e02c97b8130a1c96d47c0939d535)、[SENSOR_ATTR_SHT4X_HEATER_POWER](#gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052)、[SENSOR_ATTR_SHT4X_HEATER_DURATION](#gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)。

SHT4X 的自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.4\_函数（Functions）

<a id="r_gaf2539064f44eb3981cb40a3c2f7a0eb8"></a>

```c
int sht4x_fetch_with_heater (const struct device *dev)
```

相关声明：[sht4x_fetch_with_heater](#gaf2539064f44eb3981cb40a3c2f7a0eb8)、[device](../device_reference/P002_设备对象结构.md)。

使用片上加热器（On-Chip Heater）获取数据（Fetch Data）。

## 20.5\_详细说明（Detailed Documentation）

<a id="gaf10d0155ec46d5b5152251d02f7578ee"></a>

### `SHT4X_HEATER_MAX_TEMP`

```c
#define SHT4X_HEATER_MAX_TEMP 65
```

```c
#include <zephyr/drivers/sensor/sht4x.h>
```

最高温度（Maximum Temperature）；超过该温度时不应使用加热器（Heater）。

<a id="ga4191e02c97b8130a1c96d47c0939d535"></a>

### `sensor_attribute_sht4x`

```c
enum sensor_attribute_sht4x
```

```c
#include <zephyr/drivers/sensor/sht4x.h>
```

SHT4X 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_SHT4X_HEATER_POWER` | 加热器功率（Heater Power）：0、1、2 分别对应高、中、低。 |
| `SENSOR_ATTR_SHT4X_HEATER_DURATION` | 加热器持续时间（Heater Duration）：0、1 分别对应长、短。 |

<a id="gaf2539064f44eb3981cb40a3c2f7a0eb8"></a>

### `sht4x_fetch_with_heater()`

```c
int sht4x_fetch_with_heater ( const struct device * dev)
```

```c
#include <zephyr/drivers/sensor/sht4x.h>
```

使用片上加热器（On-Chip Heater）获取数据（Fetch Data）。

测量始终采用“高”重复性（high repeatability）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向传感器设备的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。


## 20.6\_原页交叉引用（Cross References）

- [sht4x.h](../api_file_service_reference/P049_zephyr__drivers__sensor__sht4x.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052"></a>
<a id="gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_NXP 系统电源协议（NXP System Power Protocol）.md) · [返回大纲](大纲.md) · [下一章](P021_TMP114 API主题.md)
