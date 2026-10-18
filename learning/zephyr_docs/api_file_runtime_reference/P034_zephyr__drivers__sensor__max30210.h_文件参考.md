---
id: learning.zephyr-docs.api-file-runtime-reference.page-34
title: zephyr__drivers__sensor__max30210.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max30210_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_drivers\_\_sensor\_\_max30210.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max30210_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MAX30210传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

MAX30210传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 34.1\_枚举（Enumerations）

<a id="r_gaa488348f55e1d329ef0b671cdc3b6596"></a>

```c
enum sensor_attribute_max30210 { SENSOR_ATTR_MAX30210_INTERRUPT_POLARITY = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_MAX30210_CONTINUOUS_CONVERSION_MODE , SENSOR_ATTR_MAX30210_TEMP_INC_FAST_THRESH , SENSOR_ATTR_MAX30210_TEMP_DEC_FAST_THRESH , SENSOR_ATTR_MAX30210_RATE_CHG_FILTER , SENSOR_ATTR_MAX30210_HI_TRIP_COUNT , SENSOR_ATTR_MAX30210_LO_TRIP_COUNT , SENSOR_ATTR_MAX30210_HI_TRIP_COUNT_RESET , SENSOR_ATTR_MAX30210_LO_TRIP_COUNT_RESET , SENSOR_ATTR_MAX30210_HI_NON_CONSECUTIVE_MODE , SENSOR_ATTR_MAX30210_LO_NON_CONSECUTIVE_MODE , SENSOR_ATTR_MAX30210_ALERT_MODE , SENSOR_ATTR_MAX30210_SOFTWARE_RESET , SENSOR_ATTR_MAX30210_TEMP_CONVERT , SENSOR_ATTR_MAX30210_AUTO_MODE }
```

相关声明：[sensor_attribute_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gaa488348f55e1d329ef0b671cdc3b6596)、[SENSOR_ATTR_MAX30210_INTERRUPT_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a24f467601f1d4c3b0f4f30187ad18383)、[SENSOR_ATTR_MAX30210_CONTINUOUS_CONVERSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596af2832c156b33eb492a6b4ccfbfe04962)、[SENSOR_ATTR_MAX30210_TEMP_INC_FAST_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ad8006179be6db28b7b7c94d29cfacaaf)、[SENSOR_ATTR_MAX30210_TEMP_DEC_FAST_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ad0891ab0e7d3b4e5471076ef110a1484)、[SENSOR_ATTR_MAX30210_RATE_CHG_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ab8bf3efd154661c296343d895c2ee0c1)、[SENSOR_ATTR_MAX30210_HI_TRIP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a5b82942e05aa324d8a376a3308e33154)、[SENSOR_ATTR_MAX30210_LO_TRIP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a1421ffa5dc618242b9476bf9b9d2477c)、[SENSOR_ATTR_MAX30210_HI_TRIP_COUNT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a49a1d9f8c7cfd048f5d6f6e8e557f80f)、[SENSOR_ATTR_MAX30210_LO_TRIP_COUNT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ac17544d14818e04c202b2b7b7c48a4a6)、[SENSOR_ATTR_MAX30210_HI_NON_CONSECUTIVE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a8afa486799cc1a610c99ad827a2fa187)、[SENSOR_ATTR_MAX30210_LO_NON_CONSECUTIVE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a1eed2a6782fbe96e212952f57aa813e0)、[SENSOR_ATTR_MAX30210_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ac2a5d18baf0f9fa9de10c290b40850be)、[SENSOR_ATTR_MAX30210_SOFTWARE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a382ff1041d62421a8d909e9ca1206b9a)、[SENSOR_ATTR_MAX30210_TEMP_CONVERT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a10ed080d8db49b8cf3af80ad07ed3f43)、[SENSOR_ATTR_MAX30210_AUTO_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a7e44327b23d6c6e9c0fcf30728f4043e)。

MAX30210 的自定义传感器属性（Custom Sensor Attributes）。

<a id="r_gac35ad53eddd397885548aebcc6190287"></a>

```c
enum sensor_trigger_type_max30210 { SENSOR_TRIG_TEMP_INC_FAST = SENSOR_TRIG_PRIV_START , SENSOR_TRIG_TEMP_DEC_FAST }
```

相关声明：[sensor_trigger_type_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gac35ad53eddd397885548aebcc6190287)、[SENSOR_TRIG_TEMP_INC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggac35ad53eddd397885548aebcc6190287a97e05340d2e54cdd49480c63f5eacb30)、[SENSOR_TRIG_TEMP_DEC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggac35ad53eddd397885548aebcc6190287aa9367e6c0f2def7de255e5eac3be9777)。

MAX30210 的自定义传感器触发类型（Custom Sensor Trigger Types）。

<a id="enum-members-0"></a>

<a id="r_gafe0c00a2212f7684350f868dfa0f10ba"></a>

```c
enum sensor_sampling_rate_max30210 { SENSOR_SAMPLING_RATE_MAX30210_0_015625 = 0 , SENSOR_SAMPLING_RATE_MAX30210_0_03125 , SENSOR_SAMPLING_RATE_MAX30210_0_0625 , SENSOR_SAMPLING_RATE_MAX30210_0_125 , SENSOR_SAMPLING_RATE_MAX30210_0_25 , SENSOR_SAMPLING_RATE_MAX30210_0_5 , SENSOR_SAMPLING_RATE_MAX30210_1 , SENSOR_SAMPLING_RATE_MAX30210_2 , SENSOR_SAMPLING_RATE_MAX30210_4 , SENSOR_SAMPLING_RATE_MAX30210_8 }
```

相关声明：[sensor_sampling_rate_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gafe0c00a2212f7684350f868dfa0f10ba)、[SENSOR_SAMPLING_RATE_MAX30210_0_015625](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa932a2336e86bcdee54934d0ee5f59e04)、[SENSOR_SAMPLING_RATE_MAX30210_0_03125](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baaf0f5b0c7eac8e0b719b5bf81f8c4dbb6)、[SENSOR_SAMPLING_RATE_MAX30210_0_0625](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa3c606c343fb0256ca4bce14a30897e35)、[SENSOR_SAMPLING_RATE_MAX30210_0_125](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baaaddbb1de87abb83e0c8264b278e2238f)、[SENSOR_SAMPLING_RATE_MAX30210_0_25](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa5337b300e4bc8fbe5c6133805ccd6072)、[SENSOR_SAMPLING_RATE_MAX30210_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baae41176f7c449017562fe5945fa7bdb47)、[SENSOR_SAMPLING_RATE_MAX30210_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baab5b1a47df9b59c9daa622e00327b9df3)、[SENSOR_SAMPLING_RATE_MAX30210_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa269c10a5d06c78dfb8e35f6349d020ca)、[SENSOR_SAMPLING_RATE_MAX30210_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baac3315a842c88dc3fa7c2ffed3ffcab4e)、[SENSOR_SAMPLING_RATE_MAX30210_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa7ee110f3510120739cd7077c76f245d6)。

`SENSOR_ATTR_SAMPLING_FREQUENCY` 的取值，单位为赫兹（Hz）。


## 34.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P473_max30210.h_源码浏览.md)
- [sensor_attribute_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gaa488348f55e1d329ef0b671cdc3b6596)
- [SENSOR_ATTR_MAX30210_INTERRUPT_POLARITY](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a24f467601f1d4c3b0f4f30187ad18383)
- [SENSOR_ATTR_MAX30210_CONTINUOUS_CONVERSION_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596af2832c156b33eb492a6b4ccfbfe04962)
- [SENSOR_ATTR_MAX30210_TEMP_INC_FAST_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ad8006179be6db28b7b7c94d29cfacaaf)
- [SENSOR_ATTR_MAX30210_TEMP_DEC_FAST_THRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ad0891ab0e7d3b4e5471076ef110a1484)
- [SENSOR_ATTR_MAX30210_RATE_CHG_FILTER](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ab8bf3efd154661c296343d895c2ee0c1)
- [SENSOR_ATTR_MAX30210_HI_TRIP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a5b82942e05aa324d8a376a3308e33154)
- [SENSOR_ATTR_MAX30210_LO_TRIP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a1421ffa5dc618242b9476bf9b9d2477c)
- [SENSOR_ATTR_MAX30210_HI_TRIP_COUNT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a49a1d9f8c7cfd048f5d6f6e8e557f80f)
- [SENSOR_ATTR_MAX30210_LO_TRIP_COUNT_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ac17544d14818e04c202b2b7b7c48a4a6)
- [SENSOR_ATTR_MAX30210_HI_NON_CONSECUTIVE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a8afa486799cc1a610c99ad827a2fa187)
- [SENSOR_ATTR_MAX30210_LO_NON_CONSECUTIVE_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a1eed2a6782fbe96e212952f57aa813e0)
- [SENSOR_ATTR_MAX30210_ALERT_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596ac2a5d18baf0f9fa9de10c290b40850be)
- [SENSOR_ATTR_MAX30210_SOFTWARE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a382ff1041d62421a8d909e9ca1206b9a)
- [SENSOR_ATTR_MAX30210_TEMP_CONVERT](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a10ed080d8db49b8cf3af80ad07ed3f43)
- [SENSOR_ATTR_MAX30210_AUTO_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggaa488348f55e1d329ef0b671cdc3b6596a7e44327b23d6c6e9c0fcf30728f4043e)
- [sensor_trigger_type_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gac35ad53eddd397885548aebcc6190287)
- [SENSOR_TRIG_TEMP_INC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggac35ad53eddd397885548aebcc6190287a97e05340d2e54cdd49480c63f5eacb30)
- [SENSOR_TRIG_TEMP_DEC_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggac35ad53eddd397885548aebcc6190287aa9367e6c0f2def7de255e5eac3be9777)
- [sensor_sampling_rate_max30210](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#gafe0c00a2212f7684350f868dfa0f10ba)
- [SENSOR_SAMPLING_RATE_MAX30210_0_015625](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa932a2336e86bcdee54934d0ee5f59e04)
- [SENSOR_SAMPLING_RATE_MAX30210_0_03125](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baaf0f5b0c7eac8e0b719b5bf81f8c4dbb6)
- [SENSOR_SAMPLING_RATE_MAX30210_0_0625](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa3c606c343fb0256ca4bce14a30897e35)
- [SENSOR_SAMPLING_RATE_MAX30210_0_125](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baaaddbb1de87abb83e0c8264b278e2238f)
- [SENSOR_SAMPLING_RATE_MAX30210_0_25](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa5337b300e4bc8fbe5c6133805ccd6072)
- [SENSOR_SAMPLING_RATE_MAX30210_0_5](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baae41176f7c449017562fe5945fa7bdb47)
- [SENSOR_SAMPLING_RATE_MAX30210_1](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baab5b1a47df9b59c9daa622e00327b9df3)
- [SENSOR_SAMPLING_RATE_MAX30210_2](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa269c10a5d06c78dfb8e35f6349d020ca)
- [SENSOR_SAMPLING_RATE_MAX30210_4](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baac3315a842c88dc3fa7c2ffed3ffcab4e)
- [SENSOR_SAMPLING_RATE_MAX30210_8](https://docs.zephyrproject.org/latest/doxygen/html/group__max30210__interface.html#ggafe0c00a2212f7684350f868dfa0f10baa7ee110f3510120739cd7077c76f245d6)
- [SENSOR_ATTR_SAMPLING_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)

<a id="header-details"></a>

---

[上一章](P033_zephyr__drivers__lin__transceiver.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__drivers__flash__mchp_nvmctrl_g3.h_文件参考.md)
