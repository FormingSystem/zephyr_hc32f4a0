---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-27
title: sensing_sensor_register_info_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__register__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_sensing\_sensor\_register\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__register__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器注册信息（Sensor Registration Information）。

```c
#include <zephyr/sensing/sensing_sensor.h>
```

<a id="details"></a>

传感器注册信息（Sensor Registration Information）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 27.1\_数据成员（Data Fields）

<a id="r_a6300055172c8692b8313adcef5507d41"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#a6300055172c8692b8313adcef5507d41)。

传感器标志。

<a id="r_a133621dcf1da9c9ffd111eeec007f220"></a>

```c
uint16_t sample_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[sample_size](#a133621dcf1da9c9ffd111eeec007f220)。

已注册传感器的单个样本大小，单位为字节。

<a id="r_aab10e29faf4e3a6bcc33d99119bb8bc9"></a>

```c
uint8_t sensitivity_count
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sensitivity_count](#aab10e29faf4e3a6bcc33d99119bb8bc9)。

传感器灵敏度的数量。

<a id="r_af87ee2748229a7f43049d058da930ce1"></a>

```c
struct sensing_sensor_version version
```

相关声明：[sensing_sensor_version](P032_sensing_sensor_version_结构体.md)、[version](#af87ee2748229a7f43049d058da930ce1)。

传感器版本。

## 27.2\_详细说明（Detailed Documentation）

<a id="a6300055172c8692b8313adcef5507d41"></a>

### `flags`

```c
uint16_t sensing_sensor_register_info::flags
```

传感器标志。

<a id="a133621dcf1da9c9ffd111eeec007f220"></a>

### `sample_size`

```c
uint16_t sensing_sensor_register_info::sample_size
```

已注册传感器的单个样本大小，单位为字节。

感知子系统运行时（sensing runtime）需要此信息来分配内部缓冲区。

<a id="aab10e29faf4e3a6bcc33d99119bb8bc9"></a>

### `sensitivity_count`

```c
uint8_t sensing_sensor_register_info::sensitivity_count
```

传感器灵敏度的数量。

<a id="af87ee2748229a7f43049d058da930ce1"></a>

### `version`

```c
struct sensing_sensor_version sensing_sensor_register_info::version
```

传感器版本。

版本可用于区分传感器实现的不同版本。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing_sensor.h`

## 27.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__sensor_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [sensing_sensor_version](P032_sensing_sensor_version_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P026_sensing_sensor_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P028_sensing_sensor_value_3d_q31_结构体.md)
