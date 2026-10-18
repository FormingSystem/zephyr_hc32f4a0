---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-13
title: MMC56X3 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_MMC56X3 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mmc56x3__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Memsic MMC56X3 三轴磁场与温度传感器。

<a id="details"></a>

Memsic MMC56X3 三轴磁场与温度传感器。

<a id="header-files"></a>
<a id="files"></a>

## 13.1\_文件（Files）

<a id="r_mmc56x3_2Eh"></a>

```c
file mmc56x3.h
```

相关声明：[mmc56x3.h](../api_file_configuration_reference/P055_zephyr__drivers__sensor__mmc56x3.h_文件参考.md)。

MMC56X3传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.2\_枚举（Enumerations）

<a id="r_gaf722f9a8bf8bae84c57aaa1ece387ad8"></a>

```c
enum sensor_attribute_mmc56x3 { SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0 = SENSOR_ATTR_PRIV_START + 1 , SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1 , SENSOR_ATTR_AUTOMATIC_SELF_RESET }
```

相关声明：[sensor_attribute_mmc56x3](#gaf722f9a8bf8bae84c57aaa1ece387ad8)、[SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0](#ggaf722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b)、[SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1](#ggaf722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630)、[SENSOR_ATTR_AUTOMATIC_SELF_RESET](#ggaf722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f)。

MMC56X3 的自定义传感器属性（Custom Sensor Attributes）。

## 13.3\_详细说明（Detailed Documentation）

<a id="gaf722f9a8bf8bae84c57aaa1ece387ad8"></a>

### `sensor_attribute_mmc56x3`

```c
enum sensor_attribute_mmc56x3
```

```c
#include <zephyr/drivers/sensor/mmc56x3.h>
```

MMC56X3 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_0` | 带宽选择位 0。调整抽取滤波器（decimation filter）长度，控制每次测量的持续时间。这会影响输出数据率（ODR）；详情参见数据手册。 |
| `SENSOR_ATTR_BANDWIDTH_SELECTION_BITS_1` | 带宽选择位 1。调整抽取滤波器（decimation filter）长度，控制每次测量的持续时间。这会影响输出数据率（ODR）；详情参见数据手册。 |
| `SENSOR_ATTR_AUTOMATIC_SELF_RESET` | 自动自复位（automatic self reset）：启用自动自复位功能。这会影响输出数据率（ODR）；详情参见数据手册。 |


## 13.4\_原页交叉引用（Cross References）

- [mmc56x3.h](../api_file_configuration_reference/P055_zephyr__drivers__sensor__mmc56x3.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaf722f9a8bf8bae84c57aaa1ece387ad8a9cf5f5faa59252aa253a6ad708bf2e1b"></a>
<a id="ggaf722f9a8bf8bae84c57aaa1ece387ad8a4100c5eb1d3a101f409ba20100af6630"></a>
<a id="ggaf722f9a8bf8bae84c57aaa1ece387ad8a318620970dbe7fd406bcb27d4387253f"></a>

---

[上一章](P012_设置管理（Settings Management）.md) · [返回大纲](大纲.md) · [下一章](P014_多位串行外设接口（MSPI）.md)
