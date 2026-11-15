---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-17
title: 1-Wire 传感器 API（Sensor API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_1-Wire 传感器 API（Sensor API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

1-Wire 传感器 API（Sensor API）

<a id="details"></a>

1-Wire 传感器 API（Sensor API）

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_w1_5Fsensor_2Eh"></a>

```c
file w1_sensor.h
```

相关声明：[w1_sensor.h](../api_file_service_reference/P060_zephyr__drivers__sensor__w1_sensor.h_文件参考.md)。

单总线（1-Wire）传感器的扩展公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.2\_枚举（Enumerations）

<a id="r_gae6c6848f94bde562a95f5f987a8c76fc"></a>

```c
enum sensor_attribute_w1 { SENSOR_ATTR_W1_ROM = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_w1](#gae6c6848f94bde562a95f5f987a8c76fc)、[SENSOR_ATTR_W1_ROM](#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36)。

单总线传感器（1-Wire Sensors）的扩展传感器属性（Extended Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_ga947aea2687107b1b3471c3e9eded7504"></a>

```c
static void w1_rom_to_sensor_value (const struct w1_rom *rom, struct sensor_value *val)
```

相关声明：[w1_rom_to_sensor_value](#ga947aea2687107b1b3471c3e9eded7504)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `w1_rom` 编码为 `sensor_value`。

<a id="r_ga3c0b20580be768bcc45f93a4c01ee9db"></a>

```c
static void w1_sensor_value_to_rom (const struct sensor_value *val, struct w1_rom *rom)
```

相关声明：[w1_sensor_value_to_rom](#ga3c0b20580be768bcc45f93a4c01ee9db)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `sensor_value` 解码为 `w1_rom`。

## 17.4\_详细说明（Detailed Documentation）

<a id="gae6c6848f94bde562a95f5f987a8c76fc"></a>

### `sensor_attribute_w1`

```c
enum sensor_attribute_w1
```

```c
#include <zephyr/drivers/sensor/w1_sensor.h>
```

单总线传感器（1-Wire Sensors）的扩展传感器属性（Extended Sensor Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_W1_ROM` | 设备唯一的单总线 ROM 标识符（1-Wire ROM identifier）。64 位 ROM 值包含家族代码（family code）、序列号（serial number）及 CRC，并编码为大端整数（big-endian integer）：`sensor_value.val1` 为低 32 位，`sensor_value.val2` 为高 32 位。使用 `w1_rom_to_sensor_value()` 和 `w1_sensor_value_to_rom()` 在 `w1_rom` 与 `sensor_value` 之间转换。 |

<a id="ga947aea2687107b1b3471c3e9eded7504"></a>

### `w1_rom_to_sensor_value()`

```c
void w1_rom_to_sensor_value ( const struct w1_rom * rom, struct sensor_value * val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/w1_sensor.h>
```

将 `w1_rom` 编码为 `sensor_value`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] rom` | 指向 ROM 结构体的指针。 |
| `[out] val` | 指向待填充传感器值（sensor value）的指针。 |

<a id="ga3c0b20580be768bcc45f93a4c01ee9db"></a>

### `w1_sensor_value_to_rom()`

```c
void w1_sensor_value_to_rom ( const struct sensor_value * val, struct w1_rom * rom )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/sensor/w1_sensor.h>
```

将 `sensor_value` 解码为 `w1_rom`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] val` | 指向包含已编码 ROM 的传感器值的指针。 |
| `[out] rom` | 指向待填充 ROM 结构体的指针。 |


## 17.5\_原页交叉引用（Cross References）

- [w1_sensor.h](../api_file_service_reference/P060_zephyr__drivers__sensor__w1_sensor.h_文件参考.md)
- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [sensor_value.val1](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#af21dddb084da4c42a7e77b48edf26fbe)
- [sensor_value.val2](../sensor_navigation_model_reference/P055_sensor_value_结构体.md#a91f81bd0f5da69084cf3c629fde68a1b)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_STTS22H API主题.md) · [返回大纲](大纲.md)
