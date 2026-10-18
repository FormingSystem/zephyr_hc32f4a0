---
id: learning.zephyr-docs.api-protocol-topic-reference.page-1
title: ADLTC2990 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_ADLTC2990 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__adltc2990__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Analog Devices ADLTC2990 四通道 I2C 电压、电流和温度监测器。

<a id="details"></a>

Analog Devices ADLTC2990 四通道 I2C 电压、电流和温度监测器。

<a id="header-files"></a>
<a id="files"></a>

## 1.1\_文件（Files）

<a id="r_adltc2990_2Eh"></a>

```c
file adltc2990.h
```

相关声明：[adltc2990.h](../api_file_runtime_reference/P001_zephyr__drivers__sensor__adltc2990.h_文件参考.md)。

ADLTC2990传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_ga2bb0bc14920f8645b371c194148e8d21"></a>

```c
enum adltc2990_acquisition_format { ADLTC2990_REPEATED_ACQUISITION , ADLTC2990_SINGLE_SHOT_ACQUISITION }
```

相关声明：[adltc2990_acquisition_format](#ga2bb0bc14920f8645b371c194148e8d21)、[ADLTC2990_REPEATED_ACQUISITION](#gga2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415)、[ADLTC2990_SINGLE_SHOT_ACQUISITION](#gga2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870)。

采集格式（Acquisition Format）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_gae6b634f7ff028d3c4a954c111bcbc4d2"></a>

```c
int adltc2990_is_busy (const struct device *dev, bool *is_busy)
```

相关声明：[adltc2990_is_busy](#gae6b634f7ff028d3c4a954c111bcbc4d2)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

检查 adtlc2990 是否正在执行转换（Conversion）。

<a id="r_ga1952f17894be82e3b09065f79168edde"></a>

```c
int adltc2990_trigger_measurement (const struct device *dev, enum adltc2990_acquisition_format format)
```

相关声明：[adltc2990_trigger_measurement](#ga1952f17894be82e3b09065f79168edde)、[device](../device_reference/P002_设备对象结构.md)、[adltc2990_acquisition_format](#ga2bb0bc14920f8645b371c194148e8d21)。

触发 adltc2990 开始测量（Measurement）。

## 1.4\_详细说明（Detailed Documentation）

<a id="ga2bb0bc14920f8645b371c194148e8d21"></a>

### `adltc2990_acquisition_format`

```c
enum adltc2990_acquisition_format
```

```c
#include <zephyr/drivers/sensor/adltc2990.h>
```

采集格式（Acquisition Format）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ADLTC2990_REPEATED_ACQUISITION` | 重复采集（repeated acquisition）。 |
| `ADLTC2990_SINGLE_SHOT_ACQUISITION` | 单次采集（single shot acquisition）。 |

<a id="gae6b634f7ff028d3c4a954c111bcbc4d2"></a>

### `adltc2990_is_busy()`

```c
int adltc2990_is_busy ( const struct device * dev, bool * is_busy )
```

```c
#include <zephyr/drivers/sensor/adltc2990.h>
```

检查 adtlc2990 是否正在执行转换（Conversion）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 adltc2990 设备的指针。 |
| `is_busy` | 指向用于存储忙状态（busy status）的变量的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga1952f17894be82e3b09065f79168edde"></a>

### `adltc2990_trigger_measurement()`

```c
int adltc2990_trigger_measurement ( const struct device * dev, enum adltc2990_acquisition_format format )
```

```c
#include <zephyr/drivers/sensor/adltc2990.h>
```

触发 adltc2990 开始测量（Measurement）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 adltc2990 设备的指针。 |
| `format` | 要使用的采集格式（acquisition format）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |


## 1.5\_原页交叉引用（Cross References）

- [adltc2990.h](../api_file_runtime_reference/P001_zephyr__drivers__sensor__adltc2990.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2bb0bc14920f8645b371c194148e8d21a1dd5299deae992e0aa45231873180415"></a>
<a id="gga2bb0bc14920f8645b371c194148e8d21a24e4c7d8197707dbae839f08ff1fc870"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_ADXL362 API主题.md)
