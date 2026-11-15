---
id: learning.zephyr-docs.api-service-topic-reference.page-21
title: Realtek Bee 正交解码器（QDEC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_Realtek Bee 正交解码器（QDEC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek Bee 正交解码器（QDEC）

<a id="details"></a>

Realtek Bee 正交解码器（QDEC）。它为 X／Y／Z 轴原始计数（Raw Counts）提供自定义传感器通道（Custom Sensor Channels）。

<a id="header-files"></a>
<a id="files"></a>

## 21.1\_文件（Files）

<a id="r_qdec_5Fbee_2Eh"></a>

```c
file qdec_bee.h
```

相关声明：[qdec_bee.h](../api_file_supplement_reference/P095_zephyr__drivers__sensor__qdec_bee.h_文件参考.md)。

Realtek Bee正交解码器（QDEC）自定义传感器通道的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.2\_枚举（Enumerations）

<a id="r_gacbac5e46dc517ffe889f7e7352cac18c"></a>

```c
enum sensor_channel_qdec_bee { SENSOR_CHAN_QDEC_X_COUNT = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_QDEC_Y_COUNT , SENSOR_CHAN_QDEC_Z_COUNT }
```

相关声明：[sensor_channel_qdec_bee](#gacbac5e46dc517ffe889f7e7352cac18c)、[SENSOR_CHAN_QDEC_X_COUNT](#ggacbac5e46dc517ffe889f7e7352cac18cabe71e0cfa084e4f2c1d3f09a79857845)、[SENSOR_CHAN_QDEC_Y_COUNT](#ggacbac5e46dc517ffe889f7e7352cac18ca6e0b15769b472ca1579cd9360b2a31c6)、[SENSOR_CHAN_QDEC_Z_COUNT](#ggacbac5e46dc517ffe889f7e7352cac18ca906cf6ffe58d3f7a57455f666cddbbae)。

Realtek Bee 正交解码器（QDEC）的自定义传感器通道（Custom Sensor Channels）。

## 21.3\_详细说明（Detailed Documentation）

<a id="gacbac5e46dc517ffe889f7e7352cac18c"></a>

### `sensor_channel_qdec_bee`

```c
enum sensor_channel_qdec_bee
```

```c
#include <zephyr/drivers/sensor/qdec_bee.h>
```

Realtek Bee 正交解码器（QDEC）的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_QDEC_X_COUNT` | X 轴原始计数（Raw Count）。 |
| `SENSOR_CHAN_QDEC_Y_COUNT` | Y 轴原始计数（Raw Count）。 |
| `SENSOR_CHAN_QDEC_Z_COUNT` | Z 轴原始计数（Raw Count）。 |


## 21.4\_原页交叉引用（Cross References）

- [qdec_bee.h](../api_file_supplement_reference/P095_zephyr__drivers__sensor__qdec_bee.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacbac5e46dc517ffe889f7e7352cac18cabe71e0cfa084e4f2c1d3f09a79857845"></a>
<a id="ggacbac5e46dc517ffe889f7e7352cac18ca6e0b15769b472ca1579cd9360b2a31c6"></a>
<a id="ggacbac5e46dc517ffe889f7e7352cac18ca906cf6ffe58d3f7a57455f666cddbbae"></a>

---

[上一章](P020_PTP 支持.md) · [返回大纲](大纲.md) · [下一章](P022_nPM10xx 传感器接口（Sensor interface）.md)
