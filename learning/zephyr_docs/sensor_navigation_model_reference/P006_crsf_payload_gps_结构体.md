---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-6
title: crsf_payload_gps_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__gps.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_crsf\_payload\_gps\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcrsf__payload__gps.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

GPS遥测（GPS Telemetry）载荷，类型为0x02。

```c
#include <zephyr/input/input_crsf.h>
```

<a id="details"></a>

全球定位系统（GPS）遥测载荷，类型为 `0x02`。多字节值以大端序（big-endian）传输。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 6.1\_数据成员（Data Fields）

<a id="r_a5f150bbfb8bba875bb93bf53be3e46ac"></a>

```c
int32_t lat
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[lat](#a5f150bbfb8bba875bb93bf53be3e46ac)。

纬度（Latitude），编码值为角度值乘以 10,000,000。

<a id="r_ab716fc23f202bdda1c710640937f6439"></a>

```c
int32_t lon
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[lon](#ab716fc23f202bdda1c710640937f6439)。

经度（Longitude），编码值为角度值乘以 10,000,000。

<a id="r_abd1ed4c7d07b652f9d051a14e8ffbb0e"></a>

```c
uint16_t speed
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[speed](#abd1ed4c7d07b652f9d051a14e8ffbb0e)。

地速（Ground speed），编码值为 km/h 数值乘以 10。

<a id="r_a649b54ebbde44a496a2ce5354d7905e9"></a>

```c
uint16_t heading
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[heading](#a649b54ebbde44a496a2ce5354d7905e9)。

航向（Heading），编码值为角度值乘以 100。

<a id="r_a55c48a2ba2206b2031743823dee8f26b"></a>

```c
uint16_t altitude
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[altitude](#a55c48a2ba2206b2031743823dee8f26b)。

高度，单位为米，带有 +1000 m 的偏移量。

<a id="r_a8c71400a0707f52a36edec98437a7ff8"></a>

```c
uint8_t satellites
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[satellites](#a8c71400a0707f52a36edec98437a7ff8)。

可见卫星数量。

## 6.2\_详细说明（Detailed Documentation）

<a id="a55c48a2ba2206b2031743823dee8f26b"></a>

### `altitude`

```c
uint16_t crsf_payload_gps::altitude
```

高度，单位为米，带有 +1000 m 的偏移量。

<a id="a649b54ebbde44a496a2ce5354d7905e9"></a>

### `heading`

```c
uint16_t crsf_payload_gps::heading
```

航向（Heading），编码值为角度值乘以 100。

<a id="a5f150bbfb8bba875bb93bf53be3e46ac"></a>

### `lat`

```c
int32_t crsf_payload_gps::lat
```

纬度（Latitude），编码值为角度值乘以 10,000,000。

<a id="ab716fc23f202bdda1c710640937f6439"></a>

### `lon`

```c
int32_t crsf_payload_gps::lon
```

经度（Longitude），编码值为角度值乘以 10,000,000。

<a id="a8c71400a0707f52a36edec98437a7ff8"></a>

### `satellites`

```c
uint8_t crsf_payload_gps::satellites
```

可见卫星数量。

<a id="abd1ed4c7d07b652f9d051a14e8ffbb0e"></a>

### `speed`

```c
uint16_t crsf_payload_gps::speed
```

地速（Ground speed），编码值为 km/h 数值乘以 10。

本数据类型文档由以下文件生成：

- `zephyr/input/input_crsf.h`

## 6.3\_原页交叉引用（Cross References）

- [zephyr/input/input_crsf.h](https://docs.zephyrproject.org/latest/doxygen/html/input__crsf_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P005_crsf_payload_battery_结构体.md) · [返回大纲](大纲.md) · [下一章](P007_cy8cmbr3xxx_config_data_结构体.md)
