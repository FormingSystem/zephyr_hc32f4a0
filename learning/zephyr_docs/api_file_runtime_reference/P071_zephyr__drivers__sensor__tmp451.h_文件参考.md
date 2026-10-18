---
id: learning.zephyr-docs.api-file-runtime-reference.page-71
title: zephyr__drivers__sensor__tmp451.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tmp451_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_zephyr\_\_drivers\_\_sensor\_\_tmp451.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tmp451_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI TMP451温度传感器（Temperature Sensor）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

TI TMP451 温度传感器（Temperature Sensor）的扩展公共 API（Extended Public API）。它公开 TMP451 的属性（Attributes），可用于在运行时（Runtime）设置转换模式（Conversion Mode），并提供附加的便利类型（Convenience Types）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 71.1\_枚举（Enumerations）

<a id="r_ga7f503a1223c0a96d5e6216aba55ee50a"></a>

```c
enum sensor_attribute_tmp451 { SENSOR_ATTR_TMP451_ONE_SHOT_MODE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_TMP451_CONTINUOUS_MODE , SENSOR_ATTR_TMP451_SHUTDOWN_MODE }
```

相关声明：[sensor_attribute_tmp451](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ga7f503a1223c0a96d5e6216aba55ee50a)、[SENSOR_ATTR_TMP451_ONE_SHOT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa5b1bf883cc3b81b82a50b6a12738ccf9)、[SENSOR_ATTR_TMP451_CONTINUOUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa77e910c168f0ff2b9ad7e02ab3af6637)、[SENSOR_ATTR_TMP451_SHUTDOWN_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa0f3107c25c647996978a5f20c008de3c)。

TMP451 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_gabed252b77f157824aa982e32516204a5"></a>

```c
enum tmp451_conversion_rate { TMP451_RATE_0_0625_HZ = 62500 , TMP451_RATE_0_125_HZ = 125000 , TMP451_RATE_0_25_HZ = 250000 , TMP451_RATE_0_5_HZ = 500000 , TMP451_RATE_1_HZ = 1000000 , TMP451_RATE_2_HZ = 2000000 , TMP451_RATE_4_HZ = 4000000 , TMP451_RATE_8_HZ = 8000000 , TMP451_RATE_16_HZ = 16000000 , TMP451_RATE_32_HZ = 32000000 }
```

相关声明：[tmp451_conversion_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gabed252b77f157824aa982e32516204a5)、[TMP451_RATE_0_0625_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ae9173643fb08904d6cc112c2c7e7f3b8)、[TMP451_RATE_0_125_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a08a7dcec000020e4389f36f3482da6c6)、[TMP451_RATE_0_25_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a4665dce49367010641c2f4e0d2b201c4)、[TMP451_RATE_0_5_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ab4414bf14ff963efca380fe0cd49b3ed)、[TMP451_RATE_1_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a24a24c873a20af6ab86445dafd9afe19)、[TMP451_RATE_2_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a76313da12ad7d0232ecbf936dd0e22b8)、[TMP451_RATE_4_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ac511fe1434bf851c676c49953af47a6d)、[TMP451_RATE_8_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a049dabe3978580379deff14aaac1abf8)、[TMP451_RATE_16_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5aeb67ebab98eadf80440f4ffbb68691df)、[TMP451_RATE_32_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ab2dd7ab2c84f4a2f973c5486571b4093)。

与 `SENSOR_ATTR_SAMPLING_FREQUENCY` 配合使用的转换速率（Conversion Rates），单位为微赫兹（Micro-Hz）。


## 71.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P874_tmp451.h_源码浏览.md)
- [sensor_attribute_tmp451](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ga7f503a1223c0a96d5e6216aba55ee50a)
- [SENSOR_ATTR_TMP451_ONE_SHOT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa5b1bf883cc3b81b82a50b6a12738ccf9)
- [SENSOR_ATTR_TMP451_CONTINUOUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa77e910c168f0ff2b9ad7e02ab3af6637)
- [SENSOR_ATTR_TMP451_SHUTDOWN_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gga7f503a1223c0a96d5e6216aba55ee50aa0f3107c25c647996978a5f20c008de3c)
- [tmp451_conversion_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#gabed252b77f157824aa982e32516204a5)
- [TMP451_RATE_0_0625_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ae9173643fb08904d6cc112c2c7e7f3b8)
- [TMP451_RATE_0_125_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a08a7dcec000020e4389f36f3482da6c6)
- [TMP451_RATE_0_25_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a4665dce49367010641c2f4e0d2b201c4)
- [TMP451_RATE_0_5_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ab4414bf14ff963efca380fe0cd49b3ed)
- [TMP451_RATE_1_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a24a24c873a20af6ab86445dafd9afe19)
- [TMP451_RATE_2_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a76313da12ad7d0232ecbf936dd0e22b8)
- [TMP451_RATE_4_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ac511fe1434bf851c676c49953af47a6d)
- [TMP451_RATE_8_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5a049dabe3978580379deff14aaac1abf8)
- [TMP451_RATE_16_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5aeb67ebab98eadf80440f4ffbb68691df)
- [TMP451_RATE_32_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__tmp451__interface.html#ggabed252b77f157824aa982e32516204a5ab2dd7ab2c84f4a2f973c5486571b4093)

<a id="header-details"></a>

---

[上一章](P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P072_zephyr__drivers__sensor__veml6031.h_文件参考.md)
