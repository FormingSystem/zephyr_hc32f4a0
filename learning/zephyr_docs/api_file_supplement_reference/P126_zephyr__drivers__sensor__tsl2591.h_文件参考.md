---
id: learning.zephyr-docs.api-file-supplement-reference.page-126
title: zephyr__drivers__sensor__tsl2591.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tsl2591_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第126章\_zephyr\_\_drivers\_\_sensor\_\_tsl2591.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tsl2591_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AMS TSL2591环境光传感器（Ambient Light Sensor）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

AMS TSL2591 环境光传感器（Ambient Light Sensor）的扩展公共应用程序编程接口（Extended Public API）。它公开 TSL2591 的属性（Attributes），可用于设置片上增益（On-Chip Gain）、积分时间（Integration Time）和持续性滤波器（Persist Filter）参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 126.1\_枚举（Enumerations）

<a id="r_a683bdf5ef1219acd06189f46f9a5840b"></a>

```c
enum sensor_attribute_tsl2591 { SENSOR_ATTR_GAIN_MODE = SENSOR_ATTR_PRIV_START + 1 , SENSOR_ATTR_INTEGRATION_TIME , SENSOR_ATTR_INT_PERSIST }
```

相关声明：[sensor_attribute_tsl2591](#a683bdf5ef1219acd06189f46f9a5840b)、[SENSOR_ATTR_GAIN_MODE](#a683bdf5ef1219acd06189f46f9a5840ba3016fceb8359cc1e6ef20a6e3dbf56b5)、[SENSOR_ATTR_INTEGRATION_TIME](#a683bdf5ef1219acd06189f46f9a5840baeba46c663afa61df6d07ce3f90f2ec59)、[SENSOR_ATTR_INT_PERSIST](#a683bdf5ef1219acd06189f46f9a5840ba1d689501ee9f6619454ecc17201d4022)。

<a id="r_a1ee7e6e68817a10b7667bec7b52e01d8"></a>

```c
enum sensor_gain_tsl2591 { TSL2591_SENSOR_GAIN_LOW , TSL2591_SENSOR_GAIN_MED , TSL2591_SENSOR_GAIN_HIGH , TSL2591_SENSOR_GAIN_MAX }
```

相关声明：[sensor_gain_tsl2591](#a1ee7e6e68817a10b7667bec7b52e01d8)、[TSL2591_SENSOR_GAIN_LOW](#a1ee7e6e68817a10b7667bec7b52e01d8a544da22b5e70425dc5d2c3f21683fd44)、[TSL2591_SENSOR_GAIN_MED](#a1ee7e6e68817a10b7667bec7b52e01d8a14ed033d086566893a305e67a3e63be1)、[TSL2591_SENSOR_GAIN_HIGH](#a1ee7e6e68817a10b7667bec7b52e01d8a439580991f302eb9f065d4d4cc093ea4)、[TSL2591_SENSOR_GAIN_MAX](#a1ee7e6e68817a10b7667bec7b52e01d8aed9cac2266a0e7172b1ac5c48a2d9f98)。

## 126.2\_详细说明（Detailed Documentation）

<a id="a683bdf5ef1219acd06189f46f9a5840b"></a>

### `sensor_attribute_tsl2591`

```c
enum sensor_attribute_tsl2591
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_GAIN_MODE` |  |
| `SENSOR_ATTR_INTEGRATION_TIME` |  |
| `SENSOR_ATTR_INT_PERSIST` |  |

<a id="a1ee7e6e68817a10b7667bec7b52e01d8"></a>

### `sensor_gain_tsl2591`

```c
enum sensor_gain_tsl2591
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TSL2591_SENSOR_GAIN_LOW` |  |
| `TSL2591_SENSOR_GAIN_MED` |  |
| `TSL2591_SENSOR_GAIN_HIGH` |  |
| `TSL2591_SENSOR_GAIN_MAX` |  |


## 126.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_runtime_reference/P064_tsl2591.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a683bdf5ef1219acd06189f46f9a5840ba3016fceb8359cc1e6ef20a6e3dbf56b5"></a>
<a id="a683bdf5ef1219acd06189f46f9a5840baeba46c663afa61df6d07ce3f90f2ec59"></a>
<a id="a683bdf5ef1219acd06189f46f9a5840ba1d689501ee9f6619454ecc17201d4022"></a>
<a id="a1ee7e6e68817a10b7667bec7b52e01d8a544da22b5e70425dc5d2c3f21683fd44"></a>
<a id="a1ee7e6e68817a10b7667bec7b52e01d8a14ed033d086566893a305e67a3e63be1"></a>
<a id="a1ee7e6e68817a10b7667bec7b52e01d8a439580991f302eb9f065d4d4cc093ea4"></a>
<a id="a1ee7e6e68817a10b7667bec7b52e01d8aed9cac2266a0e7172b1ac5c48a2d9f98"></a>

---

[上一章](P125_zephyr__drivers__sensor__tsl2540.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P127_zephyr__drivers__sensor__veaa_x_3.h_文件参考.md)
