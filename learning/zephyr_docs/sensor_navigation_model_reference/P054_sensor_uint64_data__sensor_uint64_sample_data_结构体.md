---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-54
title: sensor_uint64_data__sensor_uint64_sample_data_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__uint64__data_1_1sensor__uint64__sample__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_sensor\_uint64\_data\_\_sensor\_uint64\_sample\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__uint64__data_1_1sensor__uint64__sample__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/drivers/sensor_data_types.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_af0274c154cbc342161b46cb6c3ca0984"></a>

```c
uint32_t timestamp_delta
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timestamp_delta](#af0274c154cbc342161b46cb6c3ca0984)。

<a id="r_a37b7eb52969798316f23102dfc66f343"></a>

```c
uint64_t value
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[value](#a37b7eb52969798316f23102dfc66f343)。

## 54.2\_详细说明（Detailed Documentation）

<a id="af0274c154cbc342161b46cb6c3ca0984"></a>

### `timestamp_delta`

```c
uint32_t sensor_uint64_data::sensor_uint64_sample_data::timestamp_delta
```

<a id="a37b7eb52969798316f23102dfc66f343"></a>

### `value`

```c
uint64_t sensor_uint64_data::sensor_uint64_sample_data::value
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor_data_types.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor_data_types.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_sensor_uint64_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_sensor_value_结构体.md)
