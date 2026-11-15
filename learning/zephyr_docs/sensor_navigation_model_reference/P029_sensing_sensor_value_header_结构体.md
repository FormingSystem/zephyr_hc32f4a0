---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-29
title: sensing_sensor_value_header_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_sensing\_sensor\_value\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__value__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部传感器值载荷（Sensor Value Payloads）的通用头部。

```c
#include <zephyr/sensing/sensing_datatypes.h>
```

<a id="details"></a>

所有传感器值载荷的通用头部（common header），每种传感器值数据结构都应包含它。这里使用 `base_timestamp`（`uint64_t`）和 `timestamp_delta`（`uint32_t`）来减少批处理模式的内存占用。`base_timestamp` 用于 `readings[0]`，`timestamp_delta` 相对于前一个读数。因此，`readings[0]` 的时间戳为 `header.base_timestamp + readings[0].timestamp_delta`；`readings[1]` 的时间戳为 `readings[0]` 的时间戳加上 `readings[1].timestamp_delta`。时间戳单位为微秒，所以 `timestamp_delta`（`uint32_t`）可表示的最长间隔按原文约为 4295 秒。如果传感器批量数据中两个相邻读数相差超过 4295 秒，传感器子系统核心会将它们拆分到多个读数结构实例，并发送多个事件。此设计借鉴 Android 上下文中心运行时环境（CHRE）；原文所指源码为 `system/chre/chre_api/include/chre_api/chre/sensor_types.h`，位于 `cs.android.com/android/platform/superproject` 的 `master` 分支。原页源码链接保留在交叉引用中。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 29.1\_数据成员（Data Fields）

<a id="r_aa8efbfd682535deca1172cb192c1a86c"></a>

```c
uint64_t base_timestamp
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[base_timestamp](#aa8efbfd682535deca1172cb192c1a86c)。

本组读数的基础时间戳（base timestamp），单位为微秒。

<a id="r_a147989d4c36de1cbd83093a2c5d90950"></a>

```c
uint16_t reading_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reading_count](#a147989d4c36de1cbd83093a2c5d90950)。

本组数据中的读数数量。

## 29.2\_详细说明（Detailed Documentation）

<a id="aa8efbfd682535deca1172cb192c1a86c"></a>

### `base_timestamp`

```c
uint64_t sensing_sensor_value_header::base_timestamp
```

本组读数的基础时间戳（base timestamp），单位为微秒。

<a id="a147989d4c36de1cbd83093a2c5d90950"></a>

### `reading_count`

```c
uint16_t sensing_sensor_value_header::reading_count
```

本组数据中的读数数量。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing_datatypes.h`

## 29.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing_datatypes.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [https://cs.android.com/android/platform/superproject/+/master:](https://cs.android.com/android/platform/superproject/+/master:)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P028_sensing_sensor_value_3d_q31_结构体.md) · [返回大纲](大纲.md) · [下一章](P030_sensing_sensor_value_q31_结构体.md)
