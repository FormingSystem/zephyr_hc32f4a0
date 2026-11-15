---
id: learning.zephyr-docs.api-file-runtime-reference.page-73
title: zephyr__drivers__sensor__veml6046.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veml6046_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_zephyr\_\_drivers\_\_sensor\_\_veml6046.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/veml6046_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

VEML6046传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor/veml60xx-common.h>
```

查看此文件的源码。

VEML6046传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 73.1\_宏定义（Macros）

<a id="r_a8b1aa2eefaeeaf17b6e4b5f1dcf72429"></a>

```c
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6046_H_
```

相关声明：[ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6046_H_](#a8b1aa2eefaeeaf17b6e4b5f1dcf72429)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 73.2\_枚举（Enumerations）

<a id="r_ga3747fce9eeb66d848ac53793be999607"></a>

```c
enum veml6046_pdd { VEML6046_SIZE_2_2 = 0x00 , VEML6046_SIZE_1_2 = 0x01 }
```

相关声明：[veml6046_pdd](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ga3747fce9eeb66d848ac53793be999607)、[VEML6046_SIZE_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gga3747fce9eeb66d848ac53793be999607aeff5e18fb4b2b411752418c768a112c0)、[VEML6046_SIZE_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gga3747fce9eeb66d848ac53793be999607a9a640844b083600613ffc2b159d56adc)。

VEML6046 光测量（Light Measurements）的尺寸选项（Size Options）。

<a id="r_gaa2daffcfea5560747a19e84e42c6c335"></a>

```c
enum sensor_attribute_veml6046 { SENSOR_ATTR_VEML6046_IT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEML6046_PDD , SENSOR_ATTR_VEML6046_GAIN , SENSOR_ATTR_VEML6046_PERS }
```

相关声明：[sensor_attribute_veml6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gaa2daffcfea5560747a19e84e42c6c335)、[SENSOR_ATTR_VEML6046_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335a6b7ba7f1343d8310b836b21eaeea7c25)、[SENSOR_ATTR_VEML6046_PDD](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335a3d4b03ea2659b6f4b1c6a69c86c09d92)、[SENSOR_ATTR_VEML6046_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335ab21a315393242e6d2f0279c8f1d0cfc2)、[SENSOR_ATTR_VEML6046_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335ad63cec22680ee6e843c6c9d0fec824cf)。

VEML6046 专用传感器属性（Specific Sensor Attributes）。

<a id="r_gacb4b1e3922372b95053c0afb488fb75d"></a>

```c
enum sensor_channel_veml6046 { SENSOR_CHAN_VEML6046_RED_RAW_COUNTS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS , SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS , SENSOR_CHAN_VEML6046_IR_RAW_COUNTS }
```

相关声明：[sensor_channel_veml6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gacb4b1e3922372b95053c0afb488fb75d)、[SENSOR_CHAN_VEML6046_RED_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75dad0972db632d1df667df84992751cd116)、[SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75da3f7b10a1bc199743c61edccda562058e)、[SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75daed4b5e65cfb012627111984d78b849ea)、[SENSOR_CHAN_VEML6046_IR_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75da96c69d6bb4682e7cc073d7cad2d065f4)。

VEML6046 专用传感器通道（Specific Sensor Channels）。

## 73.3\_详细说明（Detailed Documentation）

<a id="a8b1aa2eefaeeaf17b6e4b5f1dcf72429"></a>

### `ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6046_H_`

```c
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEML6046_H_
```


## 73.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/veml60xx-common.h](https://docs.zephyrproject.org/latest/doxygen/html/veml60xx-common_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P905_veml6046.h_源码浏览.md)
- [veml6046_pdd](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ga3747fce9eeb66d848ac53793be999607)
- [VEML6046_SIZE_2_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gga3747fce9eeb66d848ac53793be999607aeff5e18fb4b2b411752418c768a112c0)
- [VEML6046_SIZE_1_2](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gga3747fce9eeb66d848ac53793be999607a9a640844b083600613ffc2b159d56adc)
- [sensor_attribute_veml6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gaa2daffcfea5560747a19e84e42c6c335)
- [SENSOR_ATTR_VEML6046_IT](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335a6b7ba7f1343d8310b836b21eaeea7c25)
- [SENSOR_ATTR_VEML6046_PDD](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335a3d4b03ea2659b6f4b1c6a69c86c09d92)
- [SENSOR_ATTR_VEML6046_GAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335ab21a315393242e6d2f0279c8f1d0cfc2)
- [SENSOR_ATTR_VEML6046_PERS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggaa2daffcfea5560747a19e84e42c6c335ad63cec22680ee6e843c6c9d0fec824cf)
- [sensor_channel_veml6046](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#gacb4b1e3922372b95053c0afb488fb75d)
- [SENSOR_CHAN_VEML6046_RED_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75dad0972db632d1df667df84992751cd116)
- [SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75da3f7b10a1bc199743c61edccda562058e)
- [SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75daed4b5e65cfb012627111984d78b849ea)
- [SENSOR_CHAN_VEML6046_IR_RAW_COUNTS](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html#ggacb4b1e3922372b95053c0afb488fb75da96c69d6bb4682e7cc073d7cad2d065f4)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P072_zephyr__drivers__sensor__veml6031.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P074_zephyr__drivers__sensor__veml60xx-common.h_文件参考.md)
