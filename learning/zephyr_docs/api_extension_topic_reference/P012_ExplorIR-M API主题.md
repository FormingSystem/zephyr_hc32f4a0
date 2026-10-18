---
id: learning.zephyr-docs.api-extension-topic-reference.page-12
title: ExplorIR-M API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__explorir__m__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ExplorIR-M API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__explorir__m__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Gas Sensing Solutions ExplorIR-M 二氧化碳（CO2）传感器。

<a id="details"></a>

Gas Sensing Solutions ExplorIR-M 二氧化碳（CO2）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_explorir_5Fm_2Eh"></a>

```c
file explorir_m.h
```

相关声明：[explorir_m.h](../api_file_supplement_reference/P029_zephyr__drivers__sensor__explorir_m.h_文件参考.md)。

ExplorIR-M传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.2\_枚举（Enumerations）

<a id="r_gae381791648801463bad62c98b551a7c4"></a>

```c
enum sensor_attribute_explorir_m { SENSOR_ATTR_EXPLORIR_M_FILTER = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_explorir_m](#gae381791648801463bad62c98b551a7c4)、[SENSOR_ATTR_EXPLORIR_M_FILTER](#ggae381791648801463bad62c98b551a7c4a5ecbe0b20ab67018a78efa779d216c24)。

ExplorIR-M 二氧化碳传感器（CO2 Sensor）的自定义传感器属性（Custom Sensor Attributes）。

## 12.3\_详细说明（Detailed Documentation）

<a id="gae381791648801463bad62c98b551a7c4"></a>

### `sensor_attribute_explorir_m`

```c
enum sensor_attribute_explorir_m
```

```c
#include <zephyr/drivers/sensor/explorir_m.h>
```

ExplorIR-M 二氧化碳传感器（CO2 Sensor）的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_EXPLORIR_M_FILTER` | 传感器集成的低通滤波器（Integrated Low-Pass Filter）。允许值为 0～65535，默认值为 16。 |


## 12.4\_原页交叉引用（Cross References）

- [explorir_m.h](../api_file_supplement_reference/P029_zephyr__drivers__sensor__explorir_m.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae381791648801463bad62c98b551a7c4a5ecbe0b20ab67018a78efa779d216c24"></a>

---

[上一章](P011_Xilinx ADMA 专用功能（Specifics）.md) · [返回大纲](大纲.md) · [下一章](P013_F75303 API主题.md)
