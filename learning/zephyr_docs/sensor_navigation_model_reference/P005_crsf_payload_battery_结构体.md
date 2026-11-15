---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-5
title: crsf_payload_battery_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__battery.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_crsf\_payload\_battery\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__battery.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电池遥测（Battery Telemetry）载荷，类型为0x08。

```c
#include <zephyr/input/input_crsf.h>
```

<a id="details"></a>

电池遥测（Battery Telemetry）载荷，类型为0x08。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_a245c82fbe1a42795d54589869909ad31"></a>

```c
uint16_t voltage_dV
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[voltage_dV](#a245c82fbe1a42795d54589869909ad31)。

电池电压，编码值为伏特值乘以 10。

<a id="r_a09e735b8d23408c8280a7804dbb606ff"></a>

```c
uint16_t current_dA
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[current_dA](#a09e735b8d23408c8280a7804dbb606ff)。

电池电流，编码值为安培值乘以 10。

<a id="r_a612773b4ce7a0e46213a5a1e2f1b72a0"></a>

```c
uint8_t capacity_mah [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[capacity_mah](#a612773b4ce7a0e46213a5a1e2f1b72a0)。

已消耗容量，单位为毫安时，采用 24 位大端序（big-endian）表示。

<a id="r_a23c069f3185633447dc60b3bacd82f5f"></a>

```c
uint8_t remaining_pct
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[remaining_pct](#a23c069f3185633447dc60b3bacd82f5f)。

剩余电量百分比，范围为 0 至 100。

## 5.2\_详细说明（Detailed Documentation）

<a id="a612773b4ce7a0e46213a5a1e2f1b72a0"></a>

### `capacity_mah`

```c
uint8_t crsf_payload_battery::capacity_mah[3]
```

已消耗容量，单位为毫安时，采用 24 位大端序（big-endian）表示。

<a id="a09e735b8d23408c8280a7804dbb606ff"></a>

### `current_dA`

```c
uint16_t crsf_payload_battery::current_dA
```

电池电流，编码值为安培值乘以 10。

<a id="a23c069f3185633447dc60b3bacd82f5f"></a>

### `remaining_pct`

```c
uint8_t crsf_payload_battery::remaining_pct
```

剩余电量百分比，范围为 0 至 100。

<a id="a245c82fbe1a42795d54589869909ad31"></a>

### `voltage_dV`

```c
uint16_t crsf_payload_battery::voltage_dV
```

电池电压，编码值为伏特值乘以 10。

本数据类型文档由以下文件生成：

- `zephyr/input/input_crsf.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/input/input_crsf.h](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_crsf_payload_attitude_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_crsf_payload_gps_结构体.md)
