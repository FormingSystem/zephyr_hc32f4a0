---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-19
title: Iclegend S3KM1110 API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_Iclegend S3KM1110 API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__s3km1110__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Iclegend S3KM1110 24 GHz 毫米波雷达（mmWave radar）。

<a id="details"></a>

Iclegend S3KM1110 24 GHz 毫米波雷达（mmWave radar）。

<a id="header-files"></a>
<a id="files"></a>

## 19.1\_文件（Files）

<a id="r_s3km1110_2Eh"></a>

```c
file s3km1110.h
```

相关声明：[s3km1110.h](../api_file_configuration_reference/P065_zephyr__drivers__sensor__s3km1110.h_文件参考.md)。

Iclegend S3KM1110传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 19.2\_枚举（Enumerations）

<a id="r_ga490cac4394a0d2dce5c095eaf1b9a207"></a>

```c
enum s3km1110_target_status { S3KM1110_TARGET_NO_TARGET = 0x00 , S3KM1110_TARGET_MOVING = 0x01 , S3KM1110_TARGET_STATIC = 0x02 , S3KM1110_TARGET_BOTH = 0x03 , S3KM1110_TARGET_ERROR = 0x04 }
```

相关声明：[s3km1110_target_status](#ga490cac4394a0d2dce5c095eaf1b9a207)、[S3KM1110_TARGET_NO_TARGET](#gga490cac4394a0d2dce5c095eaf1b9a207a8c6ca499099aeda4fc310b90f1355869)、[S3KM1110_TARGET_MOVING](#gga490cac4394a0d2dce5c095eaf1b9a207aef0844ec3aeefb0049ed40bc78bc640e)、[S3KM1110_TARGET_STATIC](#gga490cac4394a0d2dce5c095eaf1b9a207aeb01dab2ad8f7d2f54fca829b610a36d)、[S3KM1110_TARGET_BOTH](#gga490cac4394a0d2dce5c095eaf1b9a207a22fda04d1d3d1c204f724a9f15c32465)、[S3KM1110_TARGET_ERROR](#gga490cac4394a0d2dce5c095eaf1b9a207aad1c636614b9b5a03af1ae924d5cd062)。

S3KM1110 报告的雷达目标状态值（Radar Target Status Values）。

<a id="r_ga246184cf5aba644fdefa52d7eea07ee5"></a>

```c
enum sensor_channel_s3km1110 { SENSOR_CHAN_S3KM1110_TARGET_STATUS = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_S3KM1110_MOVING_DISTANCE , SENSOR_CHAN_S3KM1110_STATIC_DISTANCE , SENSOR_CHAN_S3KM1110_MOVING_ENERGY , SENSOR_CHAN_S3KM1110_STATIC_ENERGY }
```

相关声明：[sensor_channel_s3km1110](#ga246184cf5aba644fdefa52d7eea07ee5)、[SENSOR_CHAN_S3KM1110_TARGET_STATUS](#gga246184cf5aba644fdefa52d7eea07ee5a62d06b042d9e07e302ce21b6b48e80c1)、[SENSOR_CHAN_S3KM1110_MOVING_DISTANCE](#gga246184cf5aba644fdefa52d7eea07ee5a49aeaaf493be20cd2ac70666344259a1)、[SENSOR_CHAN_S3KM1110_STATIC_DISTANCE](#gga246184cf5aba644fdefa52d7eea07ee5a5e9c481a82e32ffdc28f80558d2e9ee5)、[SENSOR_CHAN_S3KM1110_MOVING_ENERGY](#gga246184cf5aba644fdefa52d7eea07ee5a2318a4db392087b678b04ce63f829ae9)、[SENSOR_CHAN_S3KM1110_STATIC_ENERGY](#gga246184cf5aba644fdefa52d7eea07ee5a16ee99536316fc8d26186fe4e6634f3d)。

S3KM1110 的自定义传感器通道（Custom Sensor Channels）。

## 19.3\_详细说明（Detailed Documentation）

<a id="ga490cac4394a0d2dce5c095eaf1b9a207"></a>

### `s3km1110_target_status`

```c
enum s3km1110_target_status
```

```c
#include <zephyr/drivers/sensor/s3km1110.h>
```

S3KM1110 报告的雷达目标状态值（Radar Target Status Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `S3KM1110_TARGET_NO_TARGET` | 未检测到目标（Target）。 |
| `S3KM1110_TARGET_MOVING` | 检测到移动目标（Moving Target）。 |
| `S3KM1110_TARGET_STATIC` | 检测到静止目标（Static Target）。 |
| `S3KM1110_TARGET_BOTH` | 同时检测到移动目标与静止目标（Moving and Static Targets）。 |
| `S3KM1110_TARGET_ERROR` | 目标检测（Target Detection）出错。 |

<a id="ga246184cf5aba644fdefa52d7eea07ee5"></a>

### `sensor_channel_s3km1110`

```c
enum sensor_channel_s3km1110
```

```c
#include <zephyr/drivers/sensor/s3km1110.h>
```

S3KM1110 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_S3KM1110_TARGET_STATUS` | 目标状态（Target Status）。`sensor_value.val1` 为 `s3km1110_target_status` 值；`sensor_value.val2` 未使用，始终为 `0`。 |
| `SENSOR_CHAN_S3KM1110_MOVING_DISTANCE` | 到移动目标的距离（Distance to Moving Target），单位为米。`sensor_value.val1` 为距离的整数部分，单位为米；`sensor_value.val2` 为小数部分，单位为百万分之一米。 |
| `SENSOR_CHAN_S3KM1110_STATIC_DISTANCE` | 到静止目标的距离（Distance to Static Target），单位为米。`sensor_value.val1` 为距离的整数部分，单位为米；`sensor_value.val2` 为小数部分，单位为百万分之一米。 |
| `SENSOR_CHAN_S3KM1110_MOVING_ENERGY` | 移动目标能量水平（Moving Target Energy Level），以百分比表示。`sensor_value.val1` 为能量值，范围 `0–100`；`sensor_value.val2` 未使用，始终为 `0`。 |
| `SENSOR_CHAN_S3KM1110_STATIC_ENERGY` | 静止目标能量水平（Static Target Energy Level），以百分比表示。`sensor_value.val1` 为能量值，范围 `0–100`；`sensor_value.val2` 未使用，始终为 `0`。 |


## 19.4\_原页交叉引用（Cross References）

- [s3km1110.h](../api_file_configuration_reference/P065_zephyr__drivers__sensor__s3km1110.h_文件参考.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga490cac4394a0d2dce5c095eaf1b9a207a8c6ca499099aeda4fc310b90f1355869"></a>
<a id="gga490cac4394a0d2dce5c095eaf1b9a207aef0844ec3aeefb0049ed40bc78bc640e"></a>
<a id="gga490cac4394a0d2dce5c095eaf1b9a207aeb01dab2ad8f7d2f54fca829b610a36d"></a>
<a id="gga490cac4394a0d2dce5c095eaf1b9a207a22fda04d1d3d1c204f724a9f15c32465"></a>
<a id="gga490cac4394a0d2dce5c095eaf1b9a207aad1c636614b9b5a03af1ae924d5cd062"></a>
<a id="gga246184cf5aba644fdefa52d7eea07ee5a62d06b042d9e07e302ce21b6b48e80c1"></a>
<a id="gga246184cf5aba644fdefa52d7eea07ee5a49aeaaf493be20cd2ac70666344259a1"></a>
<a id="gga246184cf5aba644fdefa52d7eea07ee5a5e9c481a82e32ffdc28f80558d2e9ee5"></a>
<a id="gga246184cf5aba644fdefa52d7eea07ee5a2318a4db392087b678b04ce63f829ae9"></a>
<a id="gga246184cf5aba644fdefa52d7eea07ee5a16ee99536316fc8d26186fe4e6634f3d"></a>

---

[上一章](P018_STM32 正交解码器（QDEC STM32）.md) · [返回大纲](大纲.md) · [下一章](P020_传感器驱动后端 API.md)
