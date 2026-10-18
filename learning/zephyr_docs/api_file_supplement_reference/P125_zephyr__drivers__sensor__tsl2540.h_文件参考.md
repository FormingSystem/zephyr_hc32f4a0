---
id: learning.zephyr-docs.api-file-supplement-reference.page-125
title: zephyr__drivers__sensor__tsl2540.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tsl2540_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_zephyr\_\_drivers\_\_sensor\_\_tsl2540.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tsl2540_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

AMS TSL2540环境光传感器（Ambient Light Sensor）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

AMS TSL2540 环境光传感器（Ambient Light Sensor）的扩展公共应用程序编程接口（Extended Public API）。它公开 TSL2540 的属性（Attributes），可用于设置片上增益（On-Chip Gain）和积分时间（Integration Time）参数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 125.1\_枚举（Enumerations）

<a id="r_a9883d80dadfb4ea2b3362579f16ff2a7"></a>

```c
enum sensor_attribute_tsl2540 { SENSOR_ATTR_INTEGRATION_TIME = SENSOR_ATTR_PRIV_START + 1 , SENSOR_ATTR_INT_APERS , SENSOR_ATTR_TSL2540_SHUTDOWN_MODE , SENSOR_ATTR_TSL2540_CONTINUOUS_MODE , SENSOR_ATTR_TSL2540_CONTINUOUS_NO_WAIT_MODE }
```

相关声明：[sensor_attribute_tsl2540](#a9883d80dadfb4ea2b3362579f16ff2a7)、[SENSOR_ATTR_INTEGRATION_TIME](#a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59)、[SENSOR_ATTR_INT_APERS](#a9883d80dadfb4ea2b3362579f16ff2a7aa54ec0288bcccb2b2e6421f4b72f79f3)、[SENSOR_ATTR_TSL2540_SHUTDOWN_MODE](#a9883d80dadfb4ea2b3362579f16ff2a7af93ed8b682d02741d4a0c3a30c43c54b)、[SENSOR_ATTR_TSL2540_CONTINUOUS_MODE](#a9883d80dadfb4ea2b3362579f16ff2a7acd384fa1b346065f061d48ac5acfa5c5)、[SENSOR_ATTR_TSL2540_CONTINUOUS_NO_WAIT_MODE](#a9883d80dadfb4ea2b3362579f16ff2a7af1d695bedc5680aa3ed3194442419cac)。

<a id="r_af3d41ccc17abc24a7d10d950f19f45e9"></a>

```c
enum sensor_gain_tsl2540 { TSL2540_SENSOR_GAIN_1_2 , TSL2540_SENSOR_GAIN_1 , TSL2540_SENSOR_GAIN_4 , TSL2540_SENSOR_GAIN_16 , TSL2540_SENSOR_GAIN_64 , TSL2540_SENSOR_GAIN_128 }
```

相关声明：[sensor_gain_tsl2540](#af3d41ccc17abc24a7d10d950f19f45e9)、[TSL2540_SENSOR_GAIN_1_2](#af3d41ccc17abc24a7d10d950f19f45e9a2f573c66b903ebce339e0fb55bbc7ce1)、[TSL2540_SENSOR_GAIN_1](#af3d41ccc17abc24a7d10d950f19f45e9a2885634c5618ccb0c90389951cf394cb)、[TSL2540_SENSOR_GAIN_4](#af3d41ccc17abc24a7d10d950f19f45e9a4bda1e9f1384f0ef751ee8f9a0061d42)、[TSL2540_SENSOR_GAIN_16](#af3d41ccc17abc24a7d10d950f19f45e9ab874914e285c574ac4cfe9c358d9c66e)、[TSL2540_SENSOR_GAIN_64](#af3d41ccc17abc24a7d10d950f19f45e9a459c02cbca3e4109695fe646d128fc7f)、[TSL2540_SENSOR_GAIN_128](#af3d41ccc17abc24a7d10d950f19f45e9aee855aff34d1544549bc554faccfa948)。

## 125.2\_详细说明（Detailed Documentation）

<a id="a9883d80dadfb4ea2b3362579f16ff2a7"></a>

### `sensor_attribute_tsl2540`

```c
enum sensor_attribute_tsl2540
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_INTEGRATION_TIME` |  |
| `SENSOR_ATTR_INT_APERS` |  |
| `SENSOR_ATTR_TSL2540_SHUTDOWN_MODE` |  |
| `SENSOR_ATTR_TSL2540_CONTINUOUS_MODE` |  |
| `SENSOR_ATTR_TSL2540_CONTINUOUS_NO_WAIT_MODE` |  |

<a id="af3d41ccc17abc24a7d10d950f19f45e9"></a>

### `sensor_gain_tsl2540`

```c
enum sensor_gain_tsl2540
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TSL2540_SENSOR_GAIN_1_2` |  |
| `TSL2540_SENSOR_GAIN_1` |  |
| `TSL2540_SENSOR_GAIN_4` |  |
| `TSL2540_SENSOR_GAIN_16` |  |
| `TSL2540_SENSOR_GAIN_64` |  |
| `TSL2540_SENSOR_GAIN_128` |  |


## 125.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/tsl2540_8h_source.html)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a9883d80dadfb4ea2b3362579f16ff2a7aeba46c663afa61df6d07ce3f90f2ec59"></a>
<a id="a9883d80dadfb4ea2b3362579f16ff2a7aa54ec0288bcccb2b2e6421f4b72f79f3"></a>
<a id="a9883d80dadfb4ea2b3362579f16ff2a7af93ed8b682d02741d4a0c3a30c43c54b"></a>
<a id="a9883d80dadfb4ea2b3362579f16ff2a7acd384fa1b346065f061d48ac5acfa5c5"></a>
<a id="a9883d80dadfb4ea2b3362579f16ff2a7af1d695bedc5680aa3ed3194442419cac"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9a2f573c66b903ebce339e0fb55bbc7ce1"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9a2885634c5618ccb0c90389951cf394cb"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9a4bda1e9f1384f0ef751ee8f9a0061d42"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9ab874914e285c574ac4cfe9c358d9c66e"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9a459c02cbca3e4109695fe646d128fc7f"></a>
<a id="af3d41ccc17abc24a7d10d950f19f45e9aee855aff34d1544549bc554faccfa948"></a>

---

[上一章](P124_zephyr__arch__tricore__exception.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P126_zephyr__drivers__sensor__tsl2591.h_文件参考.md)
