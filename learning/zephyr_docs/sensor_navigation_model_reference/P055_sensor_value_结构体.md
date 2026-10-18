---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-55
title: sensor_value_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensor__value.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_sensor\_value\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensor__value.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器读出值（Sensor Readout Value）的表示。

```c
#include <zephyr/drivers/sensor.h>
```

<a id="details"></a>

传感器读数值的表示方式。值由整数部分和小数部分构成，可通过公式 `val1 + val2 * 10^(-6)` 得到。负值也遵循此公式，但可能需要特别注意。以下是原文给出的数值表示示例：

```c
 0.5: val1 =  0, val2 =  500000
-0.5: val1 =  0, val2 = -500000
-1.0: val1 = -1, val2 =  0
-1.5: val1 = -1, val2 = -500000
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_af21dddb084da4c42a7e77b48edf26fbe"></a>

```c
int32_t val1
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[val1](#af21dddb084da4c42a7e77b48edf26fbe)。

数值的整数部分（integer part）。

<a id="r_a91f81bd0f5da69084cf3c629fde68a1b"></a>

```c
int32_t val2
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[val2](#a91f81bd0f5da69084cf3c629fde68a1b)。

数值的小数部分（fractional part），以百万分之一为单位。

## 55.2\_详细说明（Detailed Documentation）

<a id="af21dddb084da4c42a7e77b48edf26fbe"></a>

### `val1`

```c
int32_t sensor_value::val1
```

数值的整数部分（integer part）。

<a id="a91f81bd0f5da69084cf3c629fde68a1b"></a>

### `val2`

```c
int32_t sensor_value::val2
```

数值的小数部分（fractional part），以百万分之一为单位。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_ubx_ack_结构体.md)
