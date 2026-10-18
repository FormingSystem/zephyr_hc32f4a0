---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-25
title: sensing_sensor_config_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_sensing\_sensor\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

感知子系统（Sensing Subsystem）的传感器配置，包括间隔、灵敏度和延迟。

```c
#include <zephyr/sensing/sensing.h>
```

<a id="details"></a>

感知子系统（Sensing Subsystem）的传感器配置，包括间隔、灵敏度和延迟。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 25.1\_数据成员（Data Fields）

<a id="r_a9bdf50a1018d6d9426efd991d05bf72b"></a>

```c
enum sensing_sensor_attribute attri
```

相关声明：[sensing_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga69d2ae9f45215742654bfc7e4676e6f2)、[attri](#a9bdf50a1018d6d9426efd991d05bf72b)。

传感器配置的属性（attribute）。

<a id="r_ac4389c439db16cb25a2e622baf0aeb9b"></a>

```c
int8_t data_field
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[data_field](#ac4389c439db16cb25a2e622baf0aeb9b)。

所有灵敏度索引：`SENSING_SENSITIVITY_INDEX_ALL`。

```c
union {
```

<a id="r_a38aff1fadd495d2d2e1ea7a0301f018d"></a>

```c
uint32_t interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[interval](#a7512f7254f6960ed398150db23868965)。

两次传感器采样之间的间隔，单位为微秒（us）。

<a id="r_a0ca28d6c176d87faf523bab33cd09e25"></a>

```c
uint32_t sensitivity
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[sensitivity](#acc1270dbe02ff6324e0f66acbde8ce33)。

报告新数据的灵敏度阈值（sensitivity threshold）。

<a id="r_aa3ccb3cdd0a0daeea7bbee7576ca1756"></a>

```c
uint64_t latency
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[latency](#af9d2ee27b3a04fd65baa1d1d0cb2badc)。

传感器样本在报告前进行批量缓存的最长时间，单位为微秒（us）。

<a id="r_ac6e3e46290fc929d6126f5582a8a4795"></a>

```c
};
```

配置值；所使用的成员由属性选择。

## 25.2\_详细说明（Detailed Documentation）

<a id="ac6e3e46290fc929d6126f5582a8a4795"></a>

### `[union]`

```c
union { ... } sensing_sensor_config
```

配置值；所使用的成员由属性选择。

<a id="a9bdf50a1018d6d9426efd991d05bf72b"></a>

### `attri`

```c
enum sensing_sensor_attribute sensing_sensor_config::attri
```

传感器配置的属性（attribute）。

<a id="ac4389c439db16cb25a2e622baf0aeb9b"></a>

### `data_field`

```c
int8_t sensing_sensor_config::data_field
```

所有灵敏度索引：`SENSING_SENSITIVITY_INDEX_ALL`。

传感器配置的数据字段。

<a id="a7512f7254f6960ed398150db23868965"></a>

### `interval`

```c
uint32_t sensing_sensor_config::interval
```

两次传感器采样之间的间隔，单位为微秒（us）。

<a id="af9d2ee27b3a04fd65baa1d1d0cb2badc"></a>

### `latency`

```c
uint64_t sensing_sensor_config::latency
```

传感器样本在报告前进行批量缓存的最长时间，单位为微秒（us）。

定义传感器样本最多可以累积多久，超过该时间就必须报告。

<a id="acc1270dbe02ff6324e0f66acbde8ce33"></a>

### `sensitivity`

```c
uint32_t sensing_sensor_config::sensitivity
```

报告新数据的灵敏度阈值（sensitivity threshold）。

只有新样本与前一样本之间的差异超过此灵敏度值时，才报告该新样本。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing.h`

## 25.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html)
- [sensing_sensor_attribute](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga69d2ae9f45215742654bfc7e4676e6f2)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [SENSING_SENSITIVITY_INDEX_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__sensing__api.html#ga16ac7bd397836280f7e8b4aa82f8eb4c)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [sensing_sensor_config](P025_sensing_sensor_config_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P024_sensing_callback_list_结构体.md) · [返回大纲](大纲.md) · [下一章](P026_sensing_sensor_info_结构体.md)
