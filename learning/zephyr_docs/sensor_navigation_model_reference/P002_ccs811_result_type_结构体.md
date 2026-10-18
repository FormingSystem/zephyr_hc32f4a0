---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-2
title: ccs811_result_type_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structccs811__result__type.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_ccs811\_result\_type\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structccs811__result__type.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

每次获取（Fetch）操作从传感器收集的信息。

```c
#include <zephyr/drivers/sensor/ccs811.h>
```

<a id="details"></a>

每次获取（Fetch）操作从传感器收集的信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a07b71c653136f3afb9d8e0d594cf7c24"></a>

```c
uint16_t co2
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[co2](#a07b71c653136f3afb9d8e0d594cf7c24)。

等效二氧化碳（equivalent carbon dioxide）浓度，以体积百万分率（ppmv）表示。

<a id="r_ad3fef69b83fa1f67f0a3cf7ab1f36f12"></a>

```c
uint16_t voc
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[voc](#ad3fef69b83fa1f67f0a3cf7ab1f36f12)。

等效总挥发性有机物（equivalent total volatile organic compounds）浓度，以体积十亿分率（ppbv）表示。

<a id="r_a5ddde08ed2992dcd24a283f781775da2"></a>

```c
uint16_t raw
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[raw](#a5ddde08ed2992dcd24a283f781775da2)。

传感器测得的原始电压和电流。

<a id="r_adf50f8b7e4eb0b45b61a00fb4e2ae8f5"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#adf50f8b7e4eb0b45b61a00fb4e2ae8f5)。

最近一次取样（fetch）完成时的传感器状态。

<a id="r_a00426f8ba17dcbf696b70a5adb6ff5a4"></a>

```c
uint8_t error
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[error](#a00426f8ba17dcbf696b70a5adb6ff5a4)。

最近一次取样完成时的传感器错误标志。

## 2.2\_详细说明（Detailed Documentation）

<a id="a07b71c653136f3afb9d8e0d594cf7c24"></a>

### `co2`

```c
uint16_t ccs811_result_type::co2
```

等效二氧化碳（equivalent carbon dioxide）浓度，以体积百万分率（ppmv）表示。

<a id="a00426f8ba17dcbf696b70a5adb6ff5a4"></a>

### `error`

```c
uint8_t ccs811_result_type::error
```

最近一次取样完成时的传感器错误标志。

注意：错误在读取时会被清除。

<a id="a5ddde08ed2992dcd24a283f781775da2"></a>

### `raw`

```c
uint16_t ccs811_result_type::raw
```

传感器测得的原始电压和电流。

<a id="adf50f8b7e4eb0b45b61a00fb4e2ae8f5"></a>

### `status`

```c
uint8_t ccs811_result_type::status
```

最近一次取样（fetch）完成时的传感器状态。

<a id="ad3fef69b83fa1f67f0a3cf7ab1f36f12"></a>

### `voc`

```c
uint16_t ccs811_result_type::voc
```

等效总挥发性有机物（equivalent total volatile organic compounds）浓度，以体积十亿分率（ppbv）表示。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sensor/ccs811.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor/ccs811.h](https://docs.zephyrproject.org/latest/doxygen/html/ccs811_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_ccs811_configver_type_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_crsf_link_stats_结构体.md)
