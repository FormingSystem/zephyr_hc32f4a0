---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-21
title: VEML6046 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_VEML6046 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__veml6046__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Vishay VEML6046 红、绿、蓝与红外（RGBIR）传感器。

<a id="details"></a>

Vishay VEML6046 红、绿、蓝与红外（RGBIR）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 21.1\_文件（Files）

<a id="r_veml6046_2Eh"></a>

```c
file veml6046.h
```

相关声明：[veml6046.h](../api_file_runtime_reference/P073_zephyr__drivers__sensor__veml6046.h_文件参考.md)。

VEML6046传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.2\_枚举（Enumerations）

<a id="r_ga3747fce9eeb66d848ac53793be999607"></a>

```c
enum veml6046_pdd { VEML6046_SIZE_2_2 = 0x00 , VEML6046_SIZE_1_2 = 0x01 }
```

相关声明：[veml6046_pdd](#ga3747fce9eeb66d848ac53793be999607)、[VEML6046_SIZE_2_2](#gga3747fce9eeb66d848ac53793be999607aeff5e18fb4b2b411752418c768a112c0)、[VEML6046_SIZE_1_2](#gga3747fce9eeb66d848ac53793be999607a9a640844b083600613ffc2b159d56adc)。

VEML6046 光测量（Light Measurements）的尺寸选项（Size Options）。

<a id="r_gaa2daffcfea5560747a19e84e42c6c335"></a>

```c
enum sensor_attribute_veml6046 { SENSOR_ATTR_VEML6046_IT = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_VEML6046_PDD , SENSOR_ATTR_VEML6046_GAIN , SENSOR_ATTR_VEML6046_PERS }
```

相关声明：[sensor_attribute_veml6046](#gaa2daffcfea5560747a19e84e42c6c335)、[SENSOR_ATTR_VEML6046_IT](#ggaa2daffcfea5560747a19e84e42c6c335a6b7ba7f1343d8310b836b21eaeea7c25)、[SENSOR_ATTR_VEML6046_PDD](#ggaa2daffcfea5560747a19e84e42c6c335a3d4b03ea2659b6f4b1c6a69c86c09d92)、[SENSOR_ATTR_VEML6046_GAIN](#ggaa2daffcfea5560747a19e84e42c6c335ab21a315393242e6d2f0279c8f1d0cfc2)、[SENSOR_ATTR_VEML6046_PERS](#ggaa2daffcfea5560747a19e84e42c6c335ad63cec22680ee6e843c6c9d0fec824cf)。

VEML6046 专用传感器属性（Specific Sensor Attributes）。

<a id="r_gacb4b1e3922372b95053c0afb488fb75d"></a>

```c
enum sensor_channel_veml6046 { SENSOR_CHAN_VEML6046_RED_RAW_COUNTS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS , SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS , SENSOR_CHAN_VEML6046_IR_RAW_COUNTS }
```

相关声明：[sensor_channel_veml6046](#gacb4b1e3922372b95053c0afb488fb75d)、[SENSOR_CHAN_VEML6046_RED_RAW_COUNTS](#ggacb4b1e3922372b95053c0afb488fb75dad0972db632d1df667df84992751cd116)、[SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS](#ggacb4b1e3922372b95053c0afb488fb75da3f7b10a1bc199743c61edccda562058e)、[SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS](#ggacb4b1e3922372b95053c0afb488fb75daed4b5e65cfb012627111984d78b849ea)、[SENSOR_CHAN_VEML6046_IR_RAW_COUNTS](#ggacb4b1e3922372b95053c0afb488fb75da96c69d6bb4682e7cc073d7cad2d065f4)。

VEML6046 专用传感器通道（Specific Sensor Channels）。

## 21.3\_详细说明（Detailed Documentation）

<a id="gaa2daffcfea5560747a19e84e42c6c335"></a>

### `sensor_attribute_veml6046`

```c
enum sensor_attribute_veml6046
```

```c
#include <zephyr/drivers/sensor/veml6046.h>
```

VEML6046 专用传感器属性（Specific Sensor Attributes）。

配置阈值窗口的上下限（Threshold Window，G_THDH_L、G_THDH_H、G_THDL_L 和 G_THDL_H）时，使用通用属性 SENSOR_ATTR_UPPER_THRESH 和 SENSOR_ATTR_LOWER_THRESH，并提供 16 位无符号整数值。两个阈值均以勒克斯（Lux）为单位，由驱动转换为传感器兼容的值。转换依赖当前增益（Gain）、积分时间（Integration Time）和有效光电二极管尺寸（Effective Photodiode Size）设置。因此，改变这些设置通常需要更新阈值窗口。为向传感器写入正确阈值，应在改变增益或积分时间之后再更新阈值。

传感器进入饱和（Saturation）状态时返回 -E2BIG；即原始环境光（ALS）值达到最大值 0xFFFF。此时由用户降低以下一个或多个属性，使传感器回到最佳测量范围：SENSOR_ATTR_VEML6046_GAIN（增益，Gain）、SENSOR_ATTR_VEML6046_IT（积分时间，Integration Time）、SENSOR_ATTR_VEML6046_PDD（有效光电二极管尺寸，Effective Photodiode Size）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_VEML6046_IT` | 测量的积分时间（Integration Time，IT）设置。属性值使用 enum veml6046_it。 |
| `SENSOR_ATTR_VEML6046_PDD` | 有效光电二极管尺寸（Effective Photodiode Size，PDD）。属性值使用 enum veml6046_pdd。 |
| `SENSOR_ATTR_VEML6046_GAIN` | 测量的增益（Gain，GAIN）设置。属性值使用 enum veml6046_gain。 |
| `SENSOR_ATTR_VEML6046_PERS` | 持续性保护计数（Persistence Protect Number，PERS）设置。属性值使用 enum veml6046_pers。 |

<a id="gacb4b1e3922372b95053c0afb488fb75d"></a>

### `sensor_channel_veml6046`

```c
enum sensor_channel_veml6046
```

```c
#include <zephyr/drivers/sensor/veml6046.h>
```

VEML6046 专用传感器通道（Specific Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_VEML6046_RED_RAW_COUNTS` | 原始红光传感器值通道（Raw Red Sensor Values）。此通道表示传感器寄存器提供的原始测量计数。在获取与读取模式（Fetch and Get Mode）下，可用于估算合适的积分时间（Integration Time）、有效光电二极管尺寸（Effective Photodiode Size）和增益（Gain）属性值。对于未来使用触发器（Triggers）的实现，也可用于估算处理传感器中断所需的阈值窗口属性（Threshold Window Attributes）。不能直接采集此通道。其值通过 SENSOR_CHAN_RED 隐式采集。尝试将此枚举值作为参数调用 sensor_channel_fetch_chan 会返回 -ENOTSUP。 |
| `SENSOR_CHAN_VEML6046_GREEN_RAW_COUNTS` | 绿光传感器值通道（Green Sensor Values）。此通道为传感器的原始绿光通道计数（Raw Green Channel Count）输出。采集方式与 SENSOR_CHAN_VEML6046_RED_RAW_COUNTS 相同。 |
| `SENSOR_CHAN_VEML6046_BLUE_RAW_COUNTS` | 蓝光传感器值通道（Blue Sensor Values）。此通道为传感器的原始蓝光通道计数（Raw Blue Channel Count）输出。采集方式与 SENSOR_CHAN_VEML6046_RED_RAW_COUNTS 相同。 |
| `SENSOR_CHAN_VEML6046_IR_RAW_COUNTS` | 红外传感器值通道（IR Sensor Values）。此通道为传感器的原始红外通道计数（Raw IR Channel Count）输出。采集方式与 SENSOR_CHAN_VEML6046_RED_RAW_COUNTS 相同。 |

<a id="ga3747fce9eeb66d848ac53793be999607"></a>

### `veml6046_pdd`

```c
enum veml6046_pdd
```

```c
#include <zephyr/drivers/sensor/veml6046.h>
```

VEML6046 光测量（Light Measurements）的尺寸选项（Size Options）。

自定义属性 SENSOR_ATTR_VEML6046_PDD 的可选值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `VEML6046_SIZE_2_2` | 光电二极管尺寸（Photodiode Size）：2/2。 |
| `VEML6046_SIZE_1_2` | 光电二极管尺寸（Photodiode Size）：1/2。 |


## 21.4\_原页交叉引用（Cross References）

- [veml6046.h](../api_file_runtime_reference/P073_zephyr__drivers__sensor__veml6046.h_文件参考.md)
- [SENSOR_ATTR_UPPER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)
- [SENSOR_ATTR_LOWER_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)
- [SENSOR_CHAN_RED](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaa2daffcfea5560747a19e84e42c6c335a6b7ba7f1343d8310b836b21eaeea7c25"></a>
<a id="ggaa2daffcfea5560747a19e84e42c6c335a3d4b03ea2659b6f4b1c6a69c86c09d92"></a>
<a id="ggaa2daffcfea5560747a19e84e42c6c335ab21a315393242e6d2f0279c8f1d0cfc2"></a>
<a id="ggaa2daffcfea5560747a19e84e42c6c335ad63cec22680ee6e843c6c9d0fec824cf"></a>
<a id="ggacb4b1e3922372b95053c0afb488fb75dad0972db632d1df667df84992751cd116"></a>
<a id="ggacb4b1e3922372b95053c0afb488fb75da3f7b10a1bc199743c61edccda562058e"></a>
<a id="ggacb4b1e3922372b95053c0afb488fb75daed4b5e65cfb012627111984d78b849ea"></a>
<a id="ggacb4b1e3922372b95053c0afb488fb75da96c69d6bb4682e7cc073d7cad2d065f4"></a>
<a id="gga3747fce9eeb66d848ac53793be999607aeff5e18fb4b2b411752418c768a112c0"></a>
<a id="gga3747fce9eeb66d848ac53793be999607a9a640844b083600613ffc2b159d56adc"></a>

---

[上一章](P020_VEML6031 API主题.md) · [返回大纲](大纲.md)
