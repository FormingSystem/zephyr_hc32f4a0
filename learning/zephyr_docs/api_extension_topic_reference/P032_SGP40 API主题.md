---
id: learning.zephyr-docs.api-extension-topic-reference.page-32
title: SGP40 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_SGP40 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sgp40__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Sensirion SGP40 气体传感器。

<a id="details"></a>

Sensirion SGP40 气体传感器。

<a id="header-files"></a>
<a id="files"></a>

## 32.1\_文件（Files）

<a id="r_sgp40_2Eh"></a>

```c
file sgp40.h
```

相关声明：[sgp40.h](../api_file_configuration_reference/P068_zephyr__drivers__sensor__sgp40.h_文件参考.md)。

SGP40传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 32.2\_枚举（Enumerations）

<a id="r_gae5259bb652233f89852c45961f58faa9"></a>

```c
enum sensor_attribute_sgp40 { SENSOR_ATTR_SGP40_TEMPERATURE = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SGP40_HUMIDITY }
```

相关声明：[sensor_attribute_sgp40](#gae5259bb652233f89852c45961f58faa9)、[SENSOR_ATTR_SGP40_TEMPERATURE](#ggae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419)、[SENSOR_ATTR_SGP40_HUMIDITY](#ggae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3)。

SGP40 的自定义传感器属性（Custom Sensor Attributes）。

## 32.3\_详细说明（Detailed Documentation）

<a id="gae5259bb652233f89852c45961f58faa9"></a>

### `sensor_attribute_sgp40`

```c
enum sensor_attribute_sgp40
```

```c
#include <zephyr/drivers/sensor/sgp40.h>
```

SGP40 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_SGP40_TEMPERATURE` | 温度（Temperature），单位为摄氏度（degC），仅使用整数部分。 |
| `SENSOR_ATTR_SGP40_HUMIDITY` | 相对湿度（Relative Humidity），单位为百分比（%），仅使用整数部分。 |


## 32.4\_原页交叉引用（Cross References）

- [sgp40.h](../api_file_configuration_reference/P068_zephyr__drivers__sensor__sgp40.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae5259bb652233f89852c45961f58faa9a30ea4c26f16600bc6ee22857fdc8c419"></a>
<a id="ggae5259bb652233f89852c45961f58faa9ab49e709137d8eee2d36c7f4588e3b8e3"></a>

---

[上一章](P031_MCUX 增强型正交解码器（EQDC MCUX）.md) · [返回大纲](大纲.md) · [下一章](P033_TCS3400 API主题.md)
