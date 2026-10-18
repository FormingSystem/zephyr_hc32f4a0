---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-46
title: sensor_q31_data__sensor_q31_sample_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__q31__data_1_1sensor__q31__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_sensor\_q31\_data\_\_sensor\_q31\_sample\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__q31__data_1_1sensor__q31__sample__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_afdf41c27c4f3f55c3ed18c73ab8b6183"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#afdf41c27c4f3f55c3ed18c73ab8b6183)。

```c
union {
```

<a id="r_a105d82bdaf50a6c1803a36128a06135b"></a>

```c
q31_t value
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[value](#afd73a2b1b6e4e262e89e242853f4ef23)。

<a id="r_a62fb1fb44a159d138fa19f54c7feb711"></a>

```c
q31_t light
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[light](#a7ae2d145a778a72322a78ed433781a0d)。

单位：勒克斯（lux）。

<a id="r_aec16bcc88b170003fd125322bbdf8fb6"></a>

```c
q31_t pressure
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[pressure](#ae07081204f6c01334ea9f2e970879b72)。

单位：千帕（kilopascal）。

<a id="r_a161769c8d87894c1fa6cb2d1391b9527"></a>

```c
q31_t temperature
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[temperature](#a8101423f27270dcee7a356cabcc4d9dd)。

单位：摄氏度（degrees Celsius）。

<a id="r_a7aea2062ca3f6959e5d8545486b049cb"></a>

```c
q31_t percent
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[percent](#a39f4f4bf64dd49ff2fe027f6e8f8a04d)。

单位：百分比（percent）。

<a id="r_ad58d1ac37759a9f60808b2b3f22dda29"></a>

```c
q31_t distance
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[distance](#ad5d6a48016d474635c0f8a829915a8d2)。

单位：米（meters）。

<a id="r_af7b555af89b6006090be05818be6d057"></a>

```c
q31_t density
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[density](#a2ed468c4be6417f0ea2bb324560e622d)。

单位：微克/立方米（ug/m^3）。

<a id="r_a4cfd968d06e0efcc51f80bea4627ad2d"></a>

```c
q31_t density_ppm
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[density_ppm](#a1493dc66c9d6e4782aed2ddadd74e178)。

单位：百万分率（parts per million，ppm）。

<a id="r_a22449da4c630b5692e4cb07aeaae5543"></a>

```c
q31_t density_ppb
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[density_ppb](#a215aab449c2b5ee8cf32d971aa5e7708)。

单位：十亿分率（parts per billion，ppb）。

<a id="r_a1b990aad2628979372723e9638c0f8d6"></a>

```c
q31_t resistance
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[resistance](#aeb66bf289c9e17ac6473eb69c22d4eb3)。

单位：欧姆（ohms）。

<a id="r_a2918f8880a1f1a6fdda17c8fad89be6f"></a>

```c
q31_t voltage
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[voltage](#af63a2f7a618c8ff17be31a0543920525)。

单位：伏特（volts）。

<a id="r_a3db59079e854001f9a5e027359e08461"></a>

```c
q31_t current
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[current](#a60f0af8beb207f90ed916fe445525fed)。

单位：安培（amps）。

<a id="r_a2cd0935ae2a082fc32524deb9abb4b4b"></a>

```c
q31_t power
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[power](#a428adc52033ba50b871c8986e55b06af)。

单位：瓦特（watts）。

<a id="r_ae29115dc6197695b37d49dac9abaad4a"></a>

```c
q31_t angle
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[angle](#a9e58a7ea902e27b02b34cc8f619aca96)。

单位：度（degrees）。

<a id="r_a5817159e40cbb291b1820c47b0d05b1c"></a>

```c
q31_t electric_charge
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[electric_charge](#aafb3c0aa55c129b310525f7181b59d51)。

单位：毫安时（mAh）。

<a id="r_a5b616f030588f48a6ddce2a1dbef40cf"></a>

```c
q31_t humidity
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[humidity](#ac0d247952ae488af354fa1462a014d1d)。

单位：相对湿度（RH）。

<a id="r_ad573c7c15520712fce7d6789fd68df04"></a>

```c
};
```

## 46.2\_详细说明（Detailed Documentation）

<a id="ad573c7c15520712fce7d6789fd68df04"></a>

### `[union]`

```c
union { ... } sensor_q31_data::sensor_q31_sample_data
```

<a id="a9e58a7ea902e27b02b34cc8f619aca96"></a>

### `angle`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::angle
```

单位：度（degrees）。

<a id="a60f0af8beb207f90ed916fe445525fed"></a>

### `current`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::current
```

单位：安培（amps）。

<a id="a2ed468c4be6417f0ea2bb324560e622d"></a>

### `density`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::density
```

单位：微克/立方米（ug/m^3）。

<a id="a215aab449c2b5ee8cf32d971aa5e7708"></a>

### `density_ppb`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::density_ppb
```

单位：十亿分率（parts per billion，ppb）。

<a id="a1493dc66c9d6e4782aed2ddadd74e178"></a>

### `density_ppm`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::density_ppm
```

单位：百万分率（parts per million，ppm）。

<a id="ad5d6a48016d474635c0f8a829915a8d2"></a>

### `distance`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::distance
```

单位：米（meters）。

<a id="aafb3c0aa55c129b310525f7181b59d51"></a>

### `electric_charge`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::electric_charge
```

单位：毫安时（mAh）。

<a id="ac0d247952ae488af354fa1462a014d1d"></a>

### `humidity`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::humidity
```

单位：相对湿度（RH）。

<a id="a7ae2d145a778a72322a78ed433781a0d"></a>

### `light`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::light
```

单位：勒克斯（lux）。

<a id="a39f4f4bf64dd49ff2fe027f6e8f8a04d"></a>

### `percent`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::percent
```

单位：百分比（percent）。

<a id="a428adc52033ba50b871c8986e55b06af"></a>

### `power`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::power
```

单位：瓦特（watts）。

<a id="ae07081204f6c01334ea9f2e970879b72"></a>

### `pressure`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::pressure
```

单位：千帕（kilopascal）。

<a id="aeb66bf289c9e17ac6473eb69c22d4eb3"></a>

### `resistance`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::resistance
```

单位：欧姆（ohms）。

<a id="a8101423f27270dcee7a356cabcc4d9dd"></a>

### `temperature`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::temperature
```

单位：摄氏度（degrees Celsius）。

<a id="afdf41c27c4f3f55c3ed18c73ab8b6183"></a>

### `timestamp_delta`

```c
uint32_t sensor_q31_data::sensor_q31_sample_data::timestamp_delta
```

<a id="afd73a2b1b6e4e262e89e242853f4ef23"></a>

### `value`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::value
```

<a id="af63a2f7a618c8ff17be31a0543920525"></a>

### `voltage`

```c
q31_t sensor_q31_data::sensor_q31_sample_data::voltage
```

单位：伏特（volts）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [sensor_q31_data::sensor_q31_sample_data](P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_sensor_q31_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_sensor_read_config_结构体.md)
