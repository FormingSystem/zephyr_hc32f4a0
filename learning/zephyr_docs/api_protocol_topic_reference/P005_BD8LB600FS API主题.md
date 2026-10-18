---
id: learning.zephyr-docs.api-protocol-topic-reference.page-5
title: BD8LB600FS API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bd8lb600fs__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_BD8LB600FS API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bd8lb600fs__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ROHM Semiconductor BD8LB600FS 开路负载与过流检测（Open load and over-current detection）。

<a id="details"></a>

ROHM Semiconductor BD8LB600FS 开路负载与过流检测（Open load and over-current detection）。

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_bd8lb600fs_2Eh"></a>

```c
file bd8lb600fs.h
```

相关声明：[bd8lb600fs.h](../api_file_supplement_reference/P108_zephyr__drivers__sensor__bd8lb600fs.h_文件参考.md)。

BD8LB600FS传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.2\_枚举（Enumerations）

<a id="r_gaaeae18fce2525ea91a9e02566ab455ea"></a>

```c
enum sensor_channel_bd8lb600fs { SENSOR_CHAN_BD8LB600FS_OPEN_LOAD = SENSOR_ATTR_PRIV_START , SENSOR_CHAN_BD8LB600FS_OVER_CURRENT_OR_THERMAL_SHUTDOWN }
```

相关声明：[sensor_channel_bd8lb600fs](#gaaeae18fce2525ea91a9e02566ab455ea)、[SENSOR_CHAN_BD8LB600FS_OPEN_LOAD](#ggaaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587)、[SENSOR_CHAN_BD8LB600FS_OVER_CURRENT_OR_THERMAL_SHUTDOWN](#ggaaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de)。

BD8LB600FS 的自定义传感器通道（Custom Sensor Channels）。

## 5.3\_详细说明（Detailed Documentation）

<a id="gaaeae18fce2525ea91a9e02566ab455ea"></a>

### `sensor_channel_bd8lb600fs`

```c
enum sensor_channel_bd8lb600fs
```

```c
#include <zephyr/drivers/sensor/bd8lb600fs.h>
```

BD8LB600FS 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_BD8LB600FS_OPEN_LOAD` | 检测到负载开路（open load）。布尔值，每个输出对应一位。 |
| `SENSOR_CHAN_BD8LB600FS_OVER_CURRENT_OR_THERMAL_SHUTDOWN` | 过流保护（over current protection）或过热关断（thermal shutdown）。布尔值，每个输出对应一位。 |


## 5.4\_原页交叉引用（Cross References）

- [bd8lb600fs.h](../api_file_supplement_reference/P108_zephyr__drivers__sensor__bd8lb600fs.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587"></a>
<a id="ggaaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de"></a>

---

[上一章](P004_ADXL372 API主题.md) · [返回大纲](大纲.md) · [下一章](P006_蓝牙 Mesh 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）.md)
