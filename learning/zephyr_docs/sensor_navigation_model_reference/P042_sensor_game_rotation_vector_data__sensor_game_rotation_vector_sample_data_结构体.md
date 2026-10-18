---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-42
title: sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_sensor\_game\_rotation\_vector\_data\_\_sensor\_game\_rotation\_vector\_sample\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 42.1\_数据成员（Data Fields）

<a id="r_af453e301f5d1fdacf86daddc0c683498"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#af453e301f5d1fdacf86daddc0c683498)。

```c
union {
```

<a id="r_a0518d9e337c12ea411f5c1439ee91217"></a>

```c
q31_t values [4]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[values](#a7e34b93a4d3393b0c7c5918e6f6acb93)。

<a id="r_a632cfbe32084e61805bf0c23a3f641ae"></a>

```c
q31_t v [4]
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[v](#a44471cf8b4de7faa0f4abf94e9fbb36e)。

```c
struct {
```

<a id="r_a535095701ec3c6644df5be4eafafda13"></a>

```c
q31_t x
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[x](#a3ff5782e8544602eb858e034a67667b6)。

<a id="r_aca32f529ace2ee3c0343dbd53f202d61"></a>

```c
q31_t y
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[y](#a8631568f550497620734f27f2a96553d)。

<a id="r_a521cc103058028299acf5ba3b7aee9e5"></a>

```c
q31_t z
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[z](#acb44311f2b7bc97dae7b26a8256905cf)。

<a id="r_af74ccdc9872199275abec3418cefe24e"></a>

```c
q31_t w
```

相关声明：[q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)、[w](#ad5fcab0aaca689606cbfacb7f6b13887)。

<a id="r_a903a764578296c9bb435fcece1cd36ae"></a>

```c
}
```

<a id="r_a236fbdcaffa5456494b301a9e33a4271"></a>

```c
};
```

## 42.2\_详细说明（Detailed Documentation）

<a id="a236fbdcaffa5456494b301a9e33a4271"></a>

### `[union]`

```c
union { ... } sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data
```

<a id="af453e301f5d1fdacf86daddc0c683498"></a>

### `timestamp_delta`

```c
uint32_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::timestamp_delta
```

<a id="a44471cf8b4de7faa0f4abf94e9fbb36e"></a>

### `v`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::v[4]
```

<a id="a7e34b93a4d3393b0c7c5918e6f6acb93"></a>

### `values`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::values[4]
```

<a id="ad5fcab0aaca689606cbfacb7f6b13887"></a>

### `w`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::w
```

<a id="a3ff5782e8544602eb858e034a67667b6"></a>

### `x`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::x
```

<a id="a8631568f550497620734f27f2a96553d"></a>

### `y`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::y
```

<a id="acb44311f2b7bc97dae7b26a8256905cf"></a>

### `z`

```c
q31_t sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::z
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 42.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data](P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P041_sensor_game_rotation_vector_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P043_sensor_occurrence_data_结构体.md)
