---
id: learning.zephyr-docs.api-extension-topic-reference.page-19
title: MH-Z19B API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mhz19b__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_MH-Z19B API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mhz19b__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Winsen MH-Z19B 二氧化碳（CO2）传感器。

<a id="details"></a>

Winsen MH-Z19B 二氧化碳（CO2）传感器。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_mhz19b_2Eh"></a>

```c
file mhz19b.h
```

相关声明：[mhz19b.h](../api_file_supplement_reference/P069_zephyr__drivers__sensor__mhz19b.h_文件参考.md)。

MH-Z19B传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.2\_枚举（Enumerations）

<a id="r_ga8f990e8276817f44f1dc822fe9cb26f3"></a>

```c
enum sensor_attribute_mhz19b { SENSOR_ATTR_MHZ19B_ABC = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_mhz19b](#ga8f990e8276817f44f1dc822fe9cb26f3)、[SENSOR_ATTR_MHZ19B_ABC](#gga8f990e8276817f44f1dc822fe9cb26f3a31b1be7489dc1d15a526c6062dab81fa)。

MH-Z19B 的自定义传感器属性（Custom Sensor Attributes）。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga8f990e8276817f44f1dc822fe9cb26f3"></a>

### `sensor_attribute_mhz19b`

```c
enum sensor_attribute_mhz19b
```

```c
#include <zephyr/drivers/sensor/mhz19b.h>
```

MH-Z19B 的自定义传感器属性（Custom Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_MHZ19B_ABC` | 自动基线校正自校准功能（Automatic Baseline Correction Self Calibration Function）。`sensor_value.val1 == 0` 表示禁用（Disabled），`sensor_value.val1 == 1` 表示启用（Enabled）。 |


## 19.4\_原页交叉引用（Cross References）

- [mhz19b.h](../api_file_supplement_reference/P069_zephyr__drivers__sensor__mhz19b.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga8f990e8276817f44f1dc822fe9cb26f3a31b1be7489dc1d15a526c6062dab81fa"></a>

---

[上一章](P018_Zephyr 基础管理（Zephyr Basic Management）.md) · [返回大纲](大纲.md) · [下一章](P020_工作队列（Workqueues）.md)
