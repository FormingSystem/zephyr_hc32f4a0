---
id: learning.zephyr-docs.api-service-topic-reference.page-22
title: nPM10xx 传感器接口（Sensor interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_nPM10xx 传感器接口（Sensor interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 22.1\_枚举（Enumerations）

<a id="r_ga5d1bad2f8fe96e651b5637ff59009cab"></a>

```c
enum npm10xx_sensor_chan { NPM10XX_SENSOR_CHAN_VSYS = SENSOR_CHAN_PRIV_START , NPM10XX_SENSOR_CHAN_VBUS , NPM10XX_SENSOR_CHAN_OFFSET }
```

相关声明：[npm10xx_sensor_chan](#ga5d1bad2f8fe96e651b5637ff59009cab)、[NPM10XX_SENSOR_CHAN_VSYS](#gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a)、[NPM10XX_SENSOR_CHAN_VBUS](#gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa)、[NPM10XX_SENSOR_CHAN_OFFSET](#gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18)。

nPM10xx 电源管理芯片传感器（PMIC Sensor）的自定义通道（Custom Channels）。

## 22.2\_详细说明（Detailed Documentation）

<a id="ga5d1bad2f8fe96e651b5637ff59009cab"></a>

### `npm10xx_sensor_chan`

```c
enum npm10xx_sensor_chan
```

```c
#include <zephyr/drivers/sensor/npm10xx.h>
```

nPM10xx 电源管理芯片传感器（PMIC Sensor）的自定义通道（Custom Channels）。

扩展 `enum sensor_channel`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `NPM10XX_SENSOR_CHAN_VSYS` | VSYS 电压（Voltage），单位为伏特（Volts）。 |
| `NPM10XX_SENSOR_CHAN_VBUS` | VBUS 电压（Voltage），单位为伏特（Volts）。 |
| `NPM10XX_SENSOR_CHAN_OFFSET` | 模数转换器偏移值（ADC Offset Value）。 |


## 22.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/npm10xx.h](../api_file_supplement_reference/P023_zephyr__drivers__sensor__npm10xx.h_文件参考.md)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a"></a>
<a id="gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa"></a>
<a id="gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18"></a>

---

[上一章](P021_Realtek Bee 正交解码器（QDEC）.md) · [返回大纲](大纲.md) · [下一章](P023_套接字 NET_MGMT 库.md)
