---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-26
title: sensing_sensor_info_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_sensing\_sensor\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsensing__sensor__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

传感器实例（Sensor Instance）的只读描述。

```c
#include <zephyr/sensing/sensing.h>
```

<a id="details"></a>

传感器实例（Sensor Instance）的只读描述。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 26.1\_数据成员（Data Fields）

<a id="r_ac7b4f33115f7a7a24095ca90b1e7acfe"></a>

```c
const char * name
```

相关声明：[name](#ac7b4f33115f7a7a24095ca90b1e7acfe)。

传感器实例的名称。

<a id="r_aa3e056ad9c52c3388e049b08d0844b49"></a>

```c
const char * friendly_name
```

相关声明：[friendly_name](#aa3e056ad9c52c3388e049b08d0844b49)。

传感器实例的友好名称（friendly name）。

<a id="r_a085e8c00586c61245b822c7ea9db9c98"></a>

```c
const char * vendor
```

相关声明：[vendor](#a085e8c00586c61245b822c7ea9db9c98)。

传感器实例的供应商名称。

<a id="r_ace77ba2ab5d5eee7c4e385fc2ea74ee8"></a>

```c
const char * model
```

相关声明：[model](#ace77ba2ab5d5eee7c4e385fc2ea74ee8)。

传感器实例的型号名称。

<a id="r_a6b20ad8747a95cf1dc7346374de6b855"></a>

```c
const int32_t type
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[type](#a6b20ad8747a95cf1dc7346374de6b855)。

传感器类型（Sensor type）。

<a id="r_a5b2ddf0829031098301e244f60741f2b"></a>

```c
const uint32_t minimal_interval
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[minimal_interval](#a5b2ddf0829031098301e244f60741f2b)。

最小报告间隔，单位为微秒。

## 26.2\_详细说明（Detailed Documentation）

<a id="aa3e056ad9c52c3388e049b08d0844b49"></a>

### `friendly_name`

```c
const char* sensing_sensor_info::friendly_name
```

传感器实例的友好名称（friendly name）。

<a id="a5b2ddf0829031098301e244f60741f2b"></a>

### `minimal_interval`

```c
const uint32_t sensing_sensor_info::minimal_interval
```

最小报告间隔，单位为微秒。

<a id="ace77ba2ab5d5eee7c4e385fc2ea74ee8"></a>

### `model`

```c
const char* sensing_sensor_info::model
```

传感器实例的型号名称。

<a id="ac7b4f33115f7a7a24095ca90b1e7acfe"></a>

### `name`

```c
const char* sensing_sensor_info::name
```

传感器实例的名称。

<a id="a6b20ad8747a95cf1dc7346374de6b855"></a>

### `type`

```c
const int32_t sensing_sensor_info::type
```

传感器类型（Sensor type）。

<a id="a085e8c00586c61245b822c7ea9db9c98"></a>

### `vendor`

```c
const char* sensing_sensor_info::vendor
```

传感器实例的供应商名称。

本数据类型文档由以下文件生成：

- `zephyr/sensing/sensing.h`

## 26.3\_原页交叉引用（Cross References）

- [zephyr/sensing/sensing.h](https://docs.zephyrproject.org/latest/doxygen/html/sensing_8h_source.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P025_sensing_sensor_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P027_sensing_sensor_register_info_结构体.md)
