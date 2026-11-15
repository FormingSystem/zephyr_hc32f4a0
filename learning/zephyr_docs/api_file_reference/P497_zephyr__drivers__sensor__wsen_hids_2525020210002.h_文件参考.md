---
id: learning.zephyr-docs.api-file-reference.page-497
title: zephyr__drivers__sensor__wsen_hids_2525020210002.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wsen__hids__2525020210002_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第497章\_zephyr\_\_drivers\_\_sensor\_\_wsen\_hids\_2525020210002.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wsen__hids__2525020210002_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WSEN-HIDS-2525020210002传感器（Sensor）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

WSEN-HIDS-2525020210002传感器（Sensor）的扩展公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 497.1\_枚举（Enumerations）

<a id="r_aac9a11a8c10c720779a31b56b59dda47"></a>

```c
enum sensor_attribute_wsen_hids_2525020210002 { SENSOR_ATTR_WSEN_HIDS_2525020210002_PRECISION = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_WSEN_HIDS_2525020210002_HEATER }
```

相关声明：[sensor_attribute_wsen_hids_2525020210002](#aac9a11a8c10c720779a31b56b59dda47)、[SENSOR_ATTR_WSEN_HIDS_2525020210002_PRECISION](#aac9a11a8c10c720779a31b56b59dda47ab3cc193216192e9c3bb349c8cdb6955a)、[SENSOR_ATTR_WSEN_HIDS_2525020210002_HEATER](#aac9a11a8c10c720779a31b56b59dda47a4a256cd71be3c93fa1efa5eb6c4e11dd)。

<a id="r_a5cbc99af974e11d6a0095139c9d53745"></a>

```c
enum hids_2525020210002_precision_t { hids_2525020210002_precision_Low = 0x0 , hids_2525020210002_precision_Medium = 0x1 , hids_2525020210002_precision_High = 0x2 }
```

相关声明：[hids_2525020210002_precision_t](#a5cbc99af974e11d6a0095139c9d53745)、[hids_2525020210002_precision_Low](#a5cbc99af974e11d6a0095139c9d53745a34a2ff586fb0eb69e5dca23672f8c214)、[hids_2525020210002_precision_Medium](#a5cbc99af974e11d6a0095139c9d53745aa5c2cf7ca07538112d21a9cb7872e524)、[hids_2525020210002_precision_High](#a5cbc99af974e11d6a0095139c9d53745ae3ba827aa8733b0e376f9e61967d5df7)。

<a id="r_a043e3bd14c15c3a9a2bacc1e78f7f317"></a>

```c
enum hids_2525020210002_heater_t { hids_2525020210002_heater_Off = 0x0 , hids_2525020210002_heater_On_200mW_1s = 0x1 , hids_2525020210002_heater_On_200mW_100ms = 0x2 , hids_2525020210002_heater_On_110mW_1s = 0x3 , hids_2525020210002_heater_On_110mW_100ms = 0x4 , hids_2525020210002_heater_On_20mW_1s = 0x5 , hids_2525020210002_heater_On_20mW_100ms = 0x6 }
```

相关声明：[hids_2525020210002_heater_t](#a043e3bd14c15c3a9a2bacc1e78f7f317)、[hids_2525020210002_heater_Off](#a043e3bd14c15c3a9a2bacc1e78f7f317aea95bf7ef0fa2430b6aad668b6b244d7)、[hids_2525020210002_heater_On_200mW_1s](#a043e3bd14c15c3a9a2bacc1e78f7f317a15b9a389d72e7d338d7e8cf8c171ff35)、[hids_2525020210002_heater_On_200mW_100ms](#a043e3bd14c15c3a9a2bacc1e78f7f317a030f5cad08959fdc084ba943ac392a48)、[hids_2525020210002_heater_On_110mW_1s](#a043e3bd14c15c3a9a2bacc1e78f7f317aa0e704349b9568e5fd4bbd60156c64be)、[hids_2525020210002_heater_On_110mW_100ms](#a043e3bd14c15c3a9a2bacc1e78f7f317a38b108fbe099aaaf48f7a11e81b119bc)、[hids_2525020210002_heater_On_20mW_1s](#a043e3bd14c15c3a9a2bacc1e78f7f317aa713ff24dde4522352ac7bf636b7d7c3)、[hids_2525020210002_heater_On_20mW_100ms](#a043e3bd14c15c3a9a2bacc1e78f7f317a2500b161f1b08b26f68b2f9e5ac6098d)。

## 497.2\_详细说明（Detailed Documentation）

<a id="a043e3bd14c15c3a9a2bacc1e78f7f317"></a>

### `hids_2525020210002_heater_t`

```c
enum hids_2525020210002_heater_t
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `hids_2525020210002_heater_Off` |  |
| `hids_2525020210002_heater_On_200mW_1s` |  |
| `hids_2525020210002_heater_On_200mW_100ms` |  |
| `hids_2525020210002_heater_On_110mW_1s` |  |
| `hids_2525020210002_heater_On_110mW_100ms` |  |
| `hids_2525020210002_heater_On_20mW_1s` |  |
| `hids_2525020210002_heater_On_20mW_100ms` |  |

<a id="a5cbc99af974e11d6a0095139c9d53745"></a>

### `hids_2525020210002_precision_t`

```c
enum hids_2525020210002_precision_t
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `hids_2525020210002_precision_Low` |  |
| `hids_2525020210002_precision_Medium` |  |
| `hids_2525020210002_precision_High` |  |

<a id="aac9a11a8c10c720779a31b56b59dda47"></a>

### `sensor_attribute_wsen_hids_2525020210002`

```c
enum sensor_attribute_wsen_hids_2525020210002
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_WSEN_HIDS_2525020210002_PRECISION` |  |
| `SENSOR_ATTR_WSEN_HIDS_2525020210002_HEATER` |  |


## 497.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P925_wsen_hids_2525020210002.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317aea95bf7ef0fa2430b6aad668b6b244d7"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317a15b9a389d72e7d338d7e8cf8c171ff35"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317a030f5cad08959fdc084ba943ac392a48"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317aa0e704349b9568e5fd4bbd60156c64be"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317a38b108fbe099aaaf48f7a11e81b119bc"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317aa713ff24dde4522352ac7bf636b7d7c3"></a>
<a id="a043e3bd14c15c3a9a2bacc1e78f7f317a2500b161f1b08b26f68b2f9e5ac6098d"></a>
<a id="a5cbc99af974e11d6a0095139c9d53745a34a2ff586fb0eb69e5dca23672f8c214"></a>
<a id="a5cbc99af974e11d6a0095139c9d53745aa5c2cf7ca07538112d21a9cb7872e524"></a>
<a id="a5cbc99af974e11d6a0095139c9d53745ae3ba827aa8733b0e376f9e61967d5df7"></a>
<a id="aac9a11a8c10c720779a31b56b59dda47ab3cc193216192e9c3bb349c8cdb6955a"></a>
<a id="aac9a11a8c10c720779a31b56b59dda47a4a256cd71be3c93fa1efa5eb6c4e11dd"></a>

---

[上一章](P496_zephyr__dt-bindings__led__worldsemi_ws2812c.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P498_zephyr__dt-bindings__clock__silabs__xg21-clock.h_文件参考.md)
