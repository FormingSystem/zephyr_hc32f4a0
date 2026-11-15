---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-4
title: zephyr__drivers__sensor__mcp9600.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2mcp9600_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_sensor\_\_mcp9600.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2mcp9600_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCP9600传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

MCP9600传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 热电偶类型选择（Thermocouple Type Selection）

`SENSOR_ATTR_MCP9600_THERMOCOUPLE_TYPE` 属性的 `sensor_value.val1` 可用取值（Possible Values）。

<a id="r_ga37487f01aef0b0d66bf46da6ffae7f96"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_K 0x0
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_K](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga37487f01aef0b0d66bf46da6ffae7f96)。

K 型热电偶（Thermocouple）。

<a id="r_ga459f229b98700430a50df00f396fd3f5"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_J 0x1
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_J](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga459f229b98700430a50df00f396fd3f5)。

J 型热电偶（Thermocouple）。

<a id="r_gad6e65d95cecb7ad7b37e3d2862d1d349"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_T 0x2
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_T](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gad6e65d95cecb7ad7b37e3d2862d1d349)。

T 型热电偶（Thermocouple）。

<a id="r_gafb686f23f9d68ba01ba0d2ae1c47aec6"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_N 0x3
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_N](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gafb686f23f9d68ba01ba0d2ae1c47aec6)。

N 型热电偶（Thermocouple）。

<a id="r_ga5bacd640fdd43f29c15f014b1210af07"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_S 0x4
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_S](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga5bacd640fdd43f29c15f014b1210af07)。

S 型热电偶（Thermocouple）。

<a id="r_gae3c3e463ec8ce5d5f7dd7fb910133250"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_E 0x5
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_E](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gae3c3e463ec8ce5d5f7dd7fb910133250)。

E 型热电偶（Thermocouple）。

<a id="r_ga10ddddec5263a71e4f3753969a1fa3e5"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_B 0x6
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_B](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga10ddddec5263a71e4f3753969a1fa3e5)。

B 型热电偶（Thermocouple）。

<a id="r_ga8d735d10b5e9cc6e9f49dfde86de7f1d"></a>

```c
#define MCP9600_ATTR_VALUE_TYPE_R 0x7
```

相关声明：[MCP9600_ATTR_VALUE_TYPE_R](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga8d735d10b5e9cc6e9f49dfde86de7f1d)。

R 型热电偶（Thermocouple）。

<a id="define-members-1"></a>

### 模数转换器分辨率（ADC Resolution）

`SENSOR_ATTR_MCP9600_ADC_RES` 属性的 `sensor_value.val1` 可用取值（Possible Values）。

<a id="r_ga11c287f0770ffa4e3106652a81842441"></a>

```c
#define MCP9600_ATTR_VALUE_ADC_RES_18BIT 0x0
```

相关声明：[MCP9600_ATTR_VALUE_ADC_RES_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga11c287f0770ffa4e3106652a81842441)。

18 位分辨率（Resolution）。

<a id="r_ga1e86680bee48434c1949884abb5d426f"></a>

```c
#define MCP9600_ATTR_VALUE_ADC_RES_16BIT 0x1
```

相关声明：[MCP9600_ATTR_VALUE_ADC_RES_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga1e86680bee48434c1949884abb5d426f)。

16 位分辨率（Resolution）。

<a id="r_ga7f332819cd8714bb32c5e2014c3e4e69"></a>

```c
#define MCP9600_ATTR_VALUE_ADC_RES_14BIT 0x2
```

相关声明：[MCP9600_ATTR_VALUE_ADC_RES_14BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga7f332819cd8714bb32c5e2014c3e4e69)。

14 位分辨率（Resolution）。

<a id="r_ga3a7cbe687c924aca0f32f70f0d196506"></a>

```c
#define MCP9600_ATTR_VALUE_ADC_RES_12BIT 0x3
```

相关声明：[MCP9600_ATTR_VALUE_ADC_RES_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga3a7cbe687c924aca0f32f70f0d196506)。

12 位分辨率（Resolution）。

<a id="define-members-2"></a>

### 冷端温度分辨率（Cold Junction Temperature Resolution）

`SENSOR_ATTR_MCP9600_COLD_JUNCTION_RESOLUTION` 属性的 `sensor_value.val1` 可用取值（Possible Values）。

<a id="r_ga206aef29d1adc2d1882682194432b8e4"></a>

```c
#define MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_0625C 0x0
```

相关声明：[MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_0625C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga206aef29d1adc2d1882682194432b8e4)。

0.0625 °C 分辨率（Resolution）。

<a id="r_ga5192c78deeaf66e872526bcbf2fcc31e"></a>

```c
#define MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_25C 0x1
```

相关声明：[MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_25C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga5192c78deeaf66e872526bcbf2fcc31e)。

0.25 °C 分辨率（Resolution）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.2\_枚举（Enumerations）

<a id="r_gacdedea96abe329cfee16affa1552578c"></a>

```c
enum sensor_channel_mcp9600 { SENSOR_CHAN_MCP9600_COLD_JUNCTION_TEMP = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_MCP9600_HOT_JUNCTION_TEMP , SENSOR_CHAN_MCP9600_DELTA_TEMP , SENSOR_CHAN_MCP9600_RAW_ADC }
```

相关声明：[sensor_channel_mcp9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gacdedea96abe329cfee16affa1552578c)、[SENSOR_CHAN_MCP9600_COLD_JUNCTION_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578ca47b64269a4af22fd863f3747aa5db98d)、[SENSOR_CHAN_MCP9600_HOT_JUNCTION_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578cae12b14e6cb9fa10d7b5e0c7ae3c02cb0)、[SENSOR_CHAN_MCP9600_DELTA_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578caf6e4fdc4e7bd9d15e93bed9193559e8a)、[SENSOR_CHAN_MCP9600_RAW_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578ca50b37a085486804fb64594d4b16938c3)。

MCP9600 的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga44de6e154d7859fbeec11361e38cc4b5"></a>

```c
enum sensor_attribute_mcp9600 { SENSOR_ATTR_MCP9600_ADC_RES = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_MCP9600_FILTER_COEFFICIENT , SENSOR_ATTR_MCP9600_THERMOCOUPLE_TYPE , SENSOR_ATTR_MCP9600_COLD_JUNCTION_RESOLUTION , SENSOR_ATTR_MCP9600_DEV_ID }
```

相关声明：[sensor_attribute_mcp9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga44de6e154d7859fbeec11361e38cc4b5)、[SENSOR_ATTR_MCP9600_ADC_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ab043f3fbe0f5b6608553da956a0ba776)、[SENSOR_ATTR_MCP9600_FILTER_COEFFICIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5a79c46a0c20969c13bd1163bd8cdf3f2a)、[SENSOR_ATTR_MCP9600_THERMOCOUPLE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ab9ca6d796183e3665995411c8f02e7d9)、[SENSOR_ATTR_MCP9600_COLD_JUNCTION_RESOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ad8b22654ddc9eca630e8e5db50d2fb81)、[SENSOR_ATTR_MCP9600_DEV_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5a3929d9dc3234f8c8f8199a7f94f11e85)。

MCP9600 的自定义传感器属性（Custom Sensor Attributes）。


## 4.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P044_mcp9600.h_源码浏览.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [SENSOR_ATTR_MCP9600_THERMOCOUPLE_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ab9ca6d796183e3665995411c8f02e7d9)
- [MCP9600_ATTR_VALUE_TYPE_K](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga37487f01aef0b0d66bf46da6ffae7f96)
- [MCP9600_ATTR_VALUE_TYPE_J](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga459f229b98700430a50df00f396fd3f5)
- [MCP9600_ATTR_VALUE_TYPE_T](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gad6e65d95cecb7ad7b37e3d2862d1d349)
- [MCP9600_ATTR_VALUE_TYPE_N](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gafb686f23f9d68ba01ba0d2ae1c47aec6)
- [MCP9600_ATTR_VALUE_TYPE_S](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga5bacd640fdd43f29c15f014b1210af07)
- [MCP9600_ATTR_VALUE_TYPE_E](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gae3c3e463ec8ce5d5f7dd7fb910133250)
- [MCP9600_ATTR_VALUE_TYPE_B](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga10ddddec5263a71e4f3753969a1fa3e5)
- [MCP9600_ATTR_VALUE_TYPE_R](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga8d735d10b5e9cc6e9f49dfde86de7f1d)
- [SENSOR_ATTR_MCP9600_ADC_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ab043f3fbe0f5b6608553da956a0ba776)
- [MCP9600_ATTR_VALUE_ADC_RES_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga11c287f0770ffa4e3106652a81842441)
- [MCP9600_ATTR_VALUE_ADC_RES_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga1e86680bee48434c1949884abb5d426f)
- [MCP9600_ATTR_VALUE_ADC_RES_14BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga7f332819cd8714bb32c5e2014c3e4e69)
- [MCP9600_ATTR_VALUE_ADC_RES_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga3a7cbe687c924aca0f32f70f0d196506)
- [SENSOR_ATTR_MCP9600_COLD_JUNCTION_RESOLUTION](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5ad8b22654ddc9eca630e8e5db50d2fb81)
- [MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_0625C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga206aef29d1adc2d1882682194432b8e4)
- [MCP9600_ATTR_VALUE_COLD_JUNC_TMP_RES_0_25C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga5192c78deeaf66e872526bcbf2fcc31e)
- [sensor_channel_mcp9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gacdedea96abe329cfee16affa1552578c)
- [SENSOR_CHAN_MCP9600_COLD_JUNCTION_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578ca47b64269a4af22fd863f3747aa5db98d)
- [SENSOR_CHAN_MCP9600_HOT_JUNCTION_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578cae12b14e6cb9fa10d7b5e0c7ae3c02cb0)
- [SENSOR_CHAN_MCP9600_DELTA_TEMP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578caf6e4fdc4e7bd9d15e93bed9193559e8a)
- [SENSOR_CHAN_MCP9600_RAW_ADC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ggacdedea96abe329cfee16affa1552578ca50b37a085486804fb64594d4b16938c3)
- [sensor_attribute_mcp9600](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga44de6e154d7859fbeec11361e38cc4b5)
- [SENSOR_ATTR_MCP9600_FILTER_COEFFICIENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5a79c46a0c20969c13bd1163bd8cdf3f2a)
- [SENSOR_ATTR_MCP9600_DEV_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gga44de6e154d7859fbeec11361e38cc4b5a3929d9dc3234f8c8f8199a7f94f11e85)

<a id="mcp9600_thermocouple_type"></a>
<a id="mcp9600_adc_resolution"></a>
<a id="mcp9600_cold_junction_resolution"></a>
<a id="header-details"></a>

---

[上一章](P003_zephyr__net__conn_mgr_connectivity.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__sensor__icm566xx.h_文件参考.md)
