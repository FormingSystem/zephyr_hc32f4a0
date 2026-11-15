---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-19
title: TMP451 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_TMP451 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI TMP451 温度传感器（Temperature sensor）。

<a id="details"></a>

TI TMP451 温度传感器（Temperature sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_tmp451_2Eh"></a>

```c
file tmp451.h
```

相关声明：[tmp451.h](../api_file_runtime_reference/P071_zephyr__drivers__sensor__tmp451.h_文件参考.md)。

TI TMP451温度传感器（Temperature Sensor）的扩展公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.2\_枚举（Enumerations）

<a id="r_ga7f503a1223c0a96d5e6216aba55ee50a"></a>

```c
enum sensor_attribute_tmp451 { SENSOR_ATTR_TMP451_ONE_SHOT_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_TMP451_CONTINUOUS_MODE , SENSOR_ATTR_TMP451_SHUTDOWN_MODE }
```

相关声明：[sensor_attribute_tmp451](#ga7f503a1223c0a96d5e6216aba55ee50a)、[SENSOR_ATTR_TMP451_ONE_SHOT_MODE](#gga7f503a1223c0a96d5e6216aba55ee50aa5b1bf883cc3b81b82a50b6a12738ccf9)、[SENSOR_ATTR_TMP451_CONTINUOUS_MODE](#gga7f503a1223c0a96d5e6216aba55ee50aa77e910c168f0ff2b9ad7e02ab3af6637)、[SENSOR_ATTR_TMP451_SHUTDOWN_MODE](#gga7f503a1223c0a96d5e6216aba55ee50aa0f3107c25c647996978a5f20c008de3c)。

TMP451 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_gabed252b77f157824aa982e32516204a5"></a>

```c
enum tmp451_conversion_rate { TMP451_RATE_0_0625_HZ = 62500 , TMP451_RATE_0_125_HZ = 125000 , TMP451_RATE_0_25_HZ = 250000 , TMP451_RATE_0_5_HZ = 500000 , TMP451_RATE_1_HZ = 1000000 , TMP451_RATE_2_HZ = 2000000 , TMP451_RATE_4_HZ = 4000000 , TMP451_RATE_8_HZ = 8000000 , TMP451_RATE_16_HZ = 16000000 , TMP451_RATE_32_HZ = 32000000 }
```

相关声明：[tmp451_conversion_rate](#gabed252b77f157824aa982e32516204a5)、[TMP451_RATE_0_0625_HZ](#ggabed252b77f157824aa982e32516204a5ae9173643fb08904d6cc112c2c7e7f3b8)、[TMP451_RATE_0_125_HZ](#ggabed252b77f157824aa982e32516204a5a08a7dcec000020e4389f36f3482da6c6)、[TMP451_RATE_0_25_HZ](#ggabed252b77f157824aa982e32516204a5a4665dce49367010641c2f4e0d2b201c4)、[TMP451_RATE_0_5_HZ](#ggabed252b77f157824aa982e32516204a5ab4414bf14ff963efca380fe0cd49b3ed)、[TMP451_RATE_1_HZ](#ggabed252b77f157824aa982e32516204a5a24a24c873a20af6ab86445dafd9afe19)、[TMP451_RATE_2_HZ](#ggabed252b77f157824aa982e32516204a5a76313da12ad7d0232ecbf936dd0e22b8)、[TMP451_RATE_4_HZ](#ggabed252b77f157824aa982e32516204a5ac511fe1434bf851c676c49953af47a6d)、[TMP451_RATE_8_HZ](#ggabed252b77f157824aa982e32516204a5a049dabe3978580379deff14aaac1abf8)、[TMP451_RATE_16_HZ](#ggabed252b77f157824aa982e32516204a5aeb67ebab98eadf80440f4ffbb68691df)、[TMP451_RATE_32_HZ](#ggabed252b77f157824aa982e32516204a5ab2dd7ab2c84f4a2f973c5486571b4093)。

与 `SENSOR_ATTR_SAMPLING_FREQUENCY` 配合使用的转换速率（Conversion Rates），单位为微赫兹（Micro-Hz）。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga7f503a1223c0a96d5e6216aba55ee50a"></a>

### `sensor_attribute_tmp451`

```c
enum sensor_attribute_tmp451
```

```c
#include <zephyr/drivers/sensor/tmp451.h>
```

TMP451 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_TMP451_ONE_SHOT_MODE` | 将传感器设为单次模式（One-shot Mode），即关断后按需转换（Shutdown + Convert on Demand）。 |
| `SENSOR_ATTR_TMP451_CONTINUOUS_MODE` | 将传感器设为连续转换模式（Continuous Conversion Mode），转换频率由用户设置。 |
| `SENSOR_ATTR_TMP451_SHUTDOWN_MODE` | 将传感器设为关断模式（Shutdown Mode），不进行转换。 |

<a id="gabed252b77f157824aa982e32516204a5"></a>

### `tmp451_conversion_rate`

```c
enum tmp451_conversion_rate
```

```c
#include <zephyr/drivers/sensor/tmp451.h>
```

与 `SENSOR_ATTR_SAMPLING_FREQUENCY` 配合使用的转换速率（Conversion Rates），单位为微赫兹（Micro-Hz）。

以下为 TMP451 支持的离散转换速率（Discrete Conversion Rates）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TMP451_RATE_0_0625_HZ` | 0.0625 赫兹（Hz），周期（Period）为 16 s。 |
| `TMP451_RATE_0_125_HZ` | 0.125 赫兹（Hz），周期（Period）为 8 s。 |
| `TMP451_RATE_0_25_HZ` | 0.25 赫兹（Hz），周期（Period）为 4 s。 |
| `TMP451_RATE_0_5_HZ` | 0.5 赫兹（Hz），周期（Period）为 2 s。 |
| `TMP451_RATE_1_HZ` | 1 赫兹（Hz），周期（Period）为 1 s。 |
| `TMP451_RATE_2_HZ` | 2 赫兹（Hz），周期（Period）为 500 ms。 |
| `TMP451_RATE_4_HZ` | 4 赫兹（Hz），周期（Period）为 250 ms。 |
| `TMP451_RATE_8_HZ` | 8 赫兹（Hz），周期（Period）为 125 ms。 |
| `TMP451_RATE_16_HZ` | 16 赫兹（Hz），周期（Period）为 63 ms。 |
| `TMP451_RATE_32_HZ` | 32 赫兹（Hz），周期（Period）为 32 ms。 |


## 19.4\_原页交叉引用（Cross References）

- [tmp451.h](../api_file_runtime_reference/P071_zephyr__drivers__sensor__tmp451.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga7f503a1223c0a96d5e6216aba55ee50aa5b1bf883cc3b81b82a50b6a12738ccf9"></a>
<a id="gga7f503a1223c0a96d5e6216aba55ee50aa77e910c168f0ff2b9ad7e02ab3af6637"></a>
<a id="gga7f503a1223c0a96d5e6216aba55ee50aa0f3107c25c647996978a5f20c008de3c"></a>
<a id="ggabed252b77f157824aa982e32516204a5ae9173643fb08904d6cc112c2c7e7f3b8"></a>
<a id="ggabed252b77f157824aa982e32516204a5a08a7dcec000020e4389f36f3482da6c6"></a>
<a id="ggabed252b77f157824aa982e32516204a5a4665dce49367010641c2f4e0d2b201c4"></a>
<a id="ggabed252b77f157824aa982e32516204a5ab4414bf14ff963efca380fe0cd49b3ed"></a>
<a id="ggabed252b77f157824aa982e32516204a5a24a24c873a20af6ab86445dafd9afe19"></a>
<a id="ggabed252b77f157824aa982e32516204a5a76313da12ad7d0232ecbf936dd0e22b8"></a>
<a id="ggabed252b77f157824aa982e32516204a5ac511fe1434bf851c676c49953af47a6d"></a>
<a id="ggabed252b77f157824aa982e32516204a5a049dabe3978580379deff14aaac1abf8"></a>
<a id="ggabed252b77f157824aa982e32516204a5aeb67ebab98eadf80440f4ffbb68691df"></a>
<a id="ggabed252b77f157824aa982e32516204a5ab2dd7ab2c84f4a2f973c5486571b4093"></a>

---

[上一章](P018_全球导航卫星系统（GNSS）配置.md) · [返回大纲](大纲.md) · [下一章](P020_视频控制项（Video Controls）.md)
