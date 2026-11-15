---
id: learning.zephyr-docs.api-device-topic-reference.page-11
title: INA2XX API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_INA2XX API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI INA2xx 电流/功率监测器系列。

<a id="details"></a>

TI INA2xx 电流/功率监测器系列。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_ina2xx_2Eh"></a>

```c
file ina2xx.h
```

相关声明：[ina2xx.h](../api_file_configuration_reference/P041_zephyr__drivers__sensor__ina2xx.h_文件参考.md)。

INA2xx系列电流/功率监测器（Current / Power Monitors）的扩展公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.2\_枚举（Enumerations）

<a id="r_gadc510f74d492767788d1b607b1aaf546"></a>

```c
enum sensor_channel_ina2xx { SENSOR_CHAN_INA2XX_ENERGY = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_INA2XX_CHARGE }
```

相关声明：[sensor_channel_ina2xx](#gadc510f74d492767788d1b607b1aaf546)、[SENSOR_CHAN_INA2XX_ENERGY](#ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3)、[SENSOR_CHAN_INA2XX_CHARGE](#ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff)。

INA2xx 系列的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga37021fdf250e53ed4c9967f7ca047f4c"></a>

```c
enum sensor_attribute_ina2xx { SENSOR_ATTR_ADC_CONFIGURATION = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_ina2xx](#ga37021fdf250e53ed4c9967f7ca047f4c)、[SENSOR_ATTR_ADC_CONFIGURATION](#gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4)。

INA2xx 系列的扩展传感器属性（Extended Sensor Attributes）。

## 11.3\_详细说明（Detailed Documentation）

<a id="ga37021fdf250e53ed4c9967f7ca047f4c"></a>

### `sensor_attribute_ina2xx`

```c
enum sensor_attribute_ina2xx
```

```c
#include <zephyr/drivers/sensor/ina2xx.h>
```

INA2xx 系列的扩展传感器属性（Extended Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_ADC_CONFIGURATION` | 模数转换器（ADC）配置寄存器值。`sensor_value.val1` 是原始 16 位 ADC 配置寄存器值；`sensor_value.val2` 未使用，始终为 0。 |

<a id="gadc510f74d492767788d1b607b1aaf546"></a>

### `sensor_channel_ina2xx`

```c
enum sensor_channel_ina2xx
```

```c
#include <zephyr/drivers/sensor/ina2xx.h>
```

INA2xx 系列的自定义传感器通道（Custom Sensor Channels）。

仅在提供相应寄存器的设备变体（device variants）上可用，例如 INA228。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_INA2XX_ENERGY` | 累计电能，单位为焦耳。`sensor_value.val1` 为电能的整数部分，单位为 J；`sensor_value.val2` 为小数部分，以百万分之一焦耳为单位。 |
| `SENSOR_CHAN_INA2XX_CHARGE` | 累计电荷量，单位为库仑。`sensor_value.val1` 为电荷量的整数部分，单位为 C；`sensor_value.val2` 为小数部分，以百万分之一库仑为单位。 |


## 11.4\_原页交叉引用（Cross References）

- [ina2xx.h](../api_file_configuration_reference/P041_zephyr__drivers__sensor__ina2xx.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4"></a>
<a id="ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3"></a>
<a id="ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff"></a>

---

[上一章](P010_FT8xx 通用函数.md) · [返回大纲](大纲.md) · [下一章](P012_键位映射实用工具（Keymap utilities）.md)
