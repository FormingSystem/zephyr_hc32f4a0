---
id: learning.zephyr-docs.api-file-system-device-reference.page-37
title: zephyr__drivers__sensor__pcnt_esp32.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_drivers\_\_sensor\_\_pcnt\_esp32.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pcnt__esp32_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ESP32脉冲计数器（PCNT）驱动的公共扩展。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

ESP32 脉冲计数器（PCNT）驱动公共扩展。通过传统 `sensor_attr_set()`／`sensor_attr_get()`／`sensor_trigger_set()` API 寻址特定 PCNT 单元的辅助定义，因为这些 API 本身不携带通道索引。通过读取与解码 API（Read-and-Decode API）访问多个单元时，直接使用 `sensor_chan_spec.chan_idx`，无须这些辅助定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="r_a19a6a63bf5efb926d34d080f81d908e8"></a>

```c
#define SENSOR_CHAN_PCNT_ESP32_UNIT(n)
```

相关声明：[SENSOR_CHAN_PCNT_ESP32_UNIT](#a19a6a63bf5efb926d34d080f81d908e8)。

生成选择 PCNT 单元 n 的 `sensor_channel` 值。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 37.2\_枚举（Enumerations）

<a id="r_a72fbc07d3bc92e1bfbba0c4aa47edbc8"></a>

```c
enum sensor_attribute_pcnt_esp32 { SENSOR_ATTR_PCNT_ESP32_RESET = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_pcnt_esp32](#a72fbc07d3bc92e1bfbba0c4aa47edbc8)、[SENSOR_ATTR_PCNT_ESP32_RESET](#a72fbc07d3bc92e1bfbba0c4aa47edbc8a29611b47f17dbee835dc48e8aedfc9d4)。

PCNT 专用传感器属性（sensor attributes）。

## 37.3\_详细说明（Detailed Documentation）

<a id="a19a6a63bf5efb926d34d080f81d908e8"></a>

### `SENSOR_CHAN_PCNT_ESP32_UNIT`

```c
#define SENSOR_CHAN_PCNT_ESP32_UNIT ( n)
```

展开值（Value）：

```c
((enum sensor_channel)(SENSOR_CHAN_PRIV_START + (n)))
```

生成选择 PCNT 单元 n 的 `sensor_channel` 值。

将此值作为 `sensor_attr_set`／`sensor_attr_get` 的 `chan` 参数，或 `struct sensor_trigger` 的 `chan` 字段，以选中单元 n。单元 0 也可通过 `SENSOR_CHAN_ROTATION` 或 `SENSOR_CHAN_ENCODER_COUNT` 寻址。

<a id="a72fbc07d3bc92e1bfbba0c4aa47edbc8"></a>

### `sensor_attribute_pcnt_esp32`

```c
enum sensor_attribute_pcnt_esp32
```

PCNT 专用传感器属性（sensor attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_PCNT_ESP32_RESET` | 清除所寻址单元的硬件计数器，并将缓存值重置为零。忽略 `val` 参数。 |


## 37.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](../api_source_transport_clock_reference/P024_sensor.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P649_pcnt_esp32.h_源码浏览.md)
- [sensor_channel](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gaaa1b502bc029b10d7b23b0a25ef4e934)
- [sensor_attr_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gafbf65226a227e9f8824908bc38e336f5)
- [sensor_chan_spec.chan_idx](../sensor_navigation_model_reference/P035_sensor_chan_spec_结构体.md#a00d4a927cfeae33b2beea8cdc415dda1)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [sensor_trigger](../sensor_navigation_model_reference/P052_sensor_trigger_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sensor__interface_html_gaaa1b502bc029b10d7b23b0a25ef4e934"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a72fbc07d3bc92e1bfbba0c4aa47edbc8a29611b47f17dbee835dc48e8aedfc9d4"></a>

---

[上一章](P036_zephyr__drivers__mfd__pca9422.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__drivers__pinctrl__pinctrl_rcar_common.h_文件参考.md)
