---
id: learning.zephyr-docs.api-file-service-reference.page-60
title: zephyr__drivers__sensor__w1_sensor.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_zephyr\_\_drivers\_\_sensor\_\_w1\_sensor.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/w1__sensor_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

单总线（1-Wire）传感器的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/w1.h>
```

查看此文件的源码。

单总线传感器（1-Wire Sensors）的扩展公共 API（Extended Public API）。本头文件公开一个传感器属性（Sensor Attribute）和若干辅助函数（Helper Functions），允许在运行时配置 1-Wire 传感器的 ROM 标识（ROM IDs）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 60.1\_枚举（Enumerations）

<a id="r_gae6c6848f94bde562a95f5f987a8c76fc"></a>

```c
enum sensor_attribute_w1 { SENSOR_ATTR_W1_ROM = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_w1](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#gae6c6848f94bde562a95f5f987a8c76fc)、[SENSOR_ATTR_W1_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36)。

单总线传感器（1-Wire Sensors）的扩展传感器属性（Extended Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 60.2\_函数（Functions）

<a id="r_ga947aea2687107b1b3471c3e9eded7504"></a>

```c
static void w1_rom_to_sensor_value (const struct w1_rom *rom, struct sensor_value *val)
```

相关声明：[w1_rom_to_sensor_value](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga947aea2687107b1b3471c3e9eded7504)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)。

将 `w1_rom` 编码为 `sensor_value`。

<a id="r_ga3c0b20580be768bcc45f93a4c01ee9db"></a>

```c
static void w1_sensor_value_to_rom (const struct sensor_value *val, struct w1_rom *rom)
```

相关声明：[w1_sensor_value_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga3c0b20580be768bcc45f93a4c01ee9db)、[sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)、[w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)。

将 `sensor_value` 解码为 `w1_rom`。


## 60.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/drivers/w1.h](../peripheral_bus_storage_source_reference/P029_zephyr__drivers__w1.h_头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P915_w1_sensor.h_源码浏览.md)
- [sensor_attribute_w1](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#gae6c6848f94bde562a95f5f987a8c76fc)
- [SENSOR_ATTR_W1_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36)
- [w1_rom_to_sensor_value](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga947aea2687107b1b3471c3e9eded7504)
- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [sensor_value](../sensor_navigation_model_reference/P055_sensor_value_结构体.md)
- [w1_sensor_value_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__sensor.html#ga3c0b20580be768bcc45f93a4c01ee9db)

<a id="header-details"></a>

---

[上一章](P059_zephyr__usb__class__usbd_uac2.h_文件参考.md) · [返回大纲](大纲.md)
