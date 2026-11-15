---
id: learning.zephyr-docs.api-file-supplement-reference.page-122
title: zephyr__drivers__sensor__ti_hdc302x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti__hdc302x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_zephyr\_\_drivers\_\_sensor\_\_ti\_hdc302x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti__hdc302x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HDC302X温度传感器（Temperature Sensors）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/i2c.h>
```

查看此文件的源码。

HDC302X 温度传感器（Temperature Sensors）的扩展公共应用程序编程接口（Extended Public API）。它公开 HDC302X 的属性（Attributes），可用于设置低功耗参数（Low Power Parameters）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 122.1\_枚举（Enumerations）

<a id="r_af9b817b9c11d3b73f563f0bf08cedf8f"></a>

```c
enum sensor_attribute_hdc302x { SENSOR_ATTR_POWER_MODE = SENSOR_ATTR_PRIV_START + 1 , SENSOR_ATTR_INTEGRATION_TIME , SENSOR_ATTR_STATUS_REGISTER , SENSOR_ATTR_HEATER_LEVEL }
```

相关声明：[sensor_attribute_hdc302x](#af9b817b9c11d3b73f563f0bf08cedf8f)、[SENSOR_ATTR_POWER_MODE](#af9b817b9c11d3b73f563f0bf08cedf8fad6ac196a42cad27354914526ed101986)、[SENSOR_ATTR_INTEGRATION_TIME](#af9b817b9c11d3b73f563f0bf08cedf8faeba46c663afa61df6d07ce3f90f2ec59)、[SENSOR_ATTR_STATUS_REGISTER](#af9b817b9c11d3b73f563f0bf08cedf8fade393ab7f8ba4ff6f85cd3d6c0a9cbc2)、[SENSOR_ATTR_HEATER_LEVEL](#af9b817b9c11d3b73f563f0bf08cedf8fa4772c29035f16339008525cc3e639947)。

<a id="r_a2e5c141fdfe76febfc08878c209d804e"></a>

```c
enum sensor_power_mode_hdc302x { HDC302X_SENSOR_POWER_MODE_0 , HDC302X_SENSOR_POWER_MODE_1 , HDC302X_SENSOR_POWER_MODE_2 , HDC302X_SENSOR_POWER_MODE_3 , HDC302X_SENSOR_POWER_MODE_MAX }
```

相关声明：[sensor_power_mode_hdc302x](#a2e5c141fdfe76febfc08878c209d804e)、[HDC302X_SENSOR_POWER_MODE_0](#a2e5c141fdfe76febfc08878c209d804ea377ec0e73db27706ea11a634b7c316ed)、[HDC302X_SENSOR_POWER_MODE_1](#a2e5c141fdfe76febfc08878c209d804ead94d8ceb5df3fbd98b8f9f913e0080c7)、[HDC302X_SENSOR_POWER_MODE_2](#a2e5c141fdfe76febfc08878c209d804ea3f824959a8bf61afb6e595b4aa8c876e)、[HDC302X_SENSOR_POWER_MODE_3](#a2e5c141fdfe76febfc08878c209d804eaab97abcb143c4366a8e3074b4d5d2a93)、[HDC302X_SENSOR_POWER_MODE_MAX](#a2e5c141fdfe76febfc08878c209d804eaf760bfd6fa7c71bc01cbc058299d0102)。

<a id="r_a556419bccd5c76de43c27fcdf93c0896"></a>

```c
enum sensor_measurement_interval_hdc302x { HDC302X_SENSOR_MEAS_INTERVAL_MANUAL , HDC302X_SENSOR_MEAS_INTERVAL_0_5 , HDC302X_SENSOR_MEAS_INTERVAL_1 , HDC302X_SENSOR_MEAS_INTERVAL_2 , HDC302X_SENSOR_MEAS_INTERVAL_4 , HDC302X_SENSOR_MEAS_INTERVAL_10 , HDC302X_SENSOR_MEAS_INTERVAL_MAX }
```

相关声明：[sensor_measurement_interval_hdc302x](#a556419bccd5c76de43c27fcdf93c0896)、[HDC302X_SENSOR_MEAS_INTERVAL_MANUAL](#a556419bccd5c76de43c27fcdf93c0896a97369b309fa9314e17ed037156a09285)、[HDC302X_SENSOR_MEAS_INTERVAL_0_5](#a556419bccd5c76de43c27fcdf93c0896a12d80d9a5105ea987d4c2a0a71cbe8d8)、[HDC302X_SENSOR_MEAS_INTERVAL_1](#a556419bccd5c76de43c27fcdf93c0896a01f370f86e630ca4892fa76ff8c08cfd)、[HDC302X_SENSOR_MEAS_INTERVAL_2](#a556419bccd5c76de43c27fcdf93c0896ac63b8ec4d957ec2691a1ca7906d0ebfd)、[HDC302X_SENSOR_MEAS_INTERVAL_4](#a556419bccd5c76de43c27fcdf93c0896ac861f09a400d473067a8f3ba7a989acb)、[HDC302X_SENSOR_MEAS_INTERVAL_10](#a556419bccd5c76de43c27fcdf93c0896a5f26dd9cf416c1c49c553517bb3d430d)、[HDC302X_SENSOR_MEAS_INTERVAL_MAX](#a556419bccd5c76de43c27fcdf93c0896a0634192bddd4b40e9fd362aa0d7340bf)。

## 122.2\_详细说明（Detailed Documentation）

<a id="af9b817b9c11d3b73f563f0bf08cedf8f"></a>

### `sensor_attribute_hdc302x`

```c
enum sensor_attribute_hdc302x
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_POWER_MODE` |  |
| `SENSOR_ATTR_INTEGRATION_TIME` |  |
| `SENSOR_ATTR_STATUS_REGISTER` |  |
| `SENSOR_ATTR_HEATER_LEVEL` |  |

<a id="a556419bccd5c76de43c27fcdf93c0896"></a>

### `sensor_measurement_interval_hdc302x`

```c
enum sensor_measurement_interval_hdc302x
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HDC302X_SENSOR_MEAS_INTERVAL_MANUAL` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_0_5` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_1` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_2` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_4` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_10` |  |
| `HDC302X_SENSOR_MEAS_INTERVAL_MAX` |  |

<a id="a2e5c141fdfe76febfc08878c209d804e"></a>

### `sensor_power_mode_hdc302x`

```c
enum sensor_power_mode_hdc302x
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HDC302X_SENSOR_POWER_MODE_0` |  |
| `HDC302X_SENSOR_POWER_MODE_1` |  |
| `HDC302X_SENSOR_POWER_MODE_2` |  |
| `HDC302X_SENSOR_POWER_MODE_3` |  |
| `HDC302X_SENSOR_POWER_MODE_MAX` |  |


## 122.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/ti__hdc302x_8h_source.html)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="af9b817b9c11d3b73f563f0bf08cedf8fad6ac196a42cad27354914526ed101986"></a>
<a id="af9b817b9c11d3b73f563f0bf08cedf8faeba46c663afa61df6d07ce3f90f2ec59"></a>
<a id="af9b817b9c11d3b73f563f0bf08cedf8fade393ab7f8ba4ff6f85cd3d6c0a9cbc2"></a>
<a id="af9b817b9c11d3b73f563f0bf08cedf8fa4772c29035f16339008525cc3e639947"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896a97369b309fa9314e17ed037156a09285"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896a12d80d9a5105ea987d4c2a0a71cbe8d8"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896a01f370f86e630ca4892fa76ff8c08cfd"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896ac63b8ec4d957ec2691a1ca7906d0ebfd"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896ac861f09a400d473067a8f3ba7a989acb"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896a5f26dd9cf416c1c49c553517bb3d430d"></a>
<a id="a556419bccd5c76de43c27fcdf93c0896a0634192bddd4b40e9fd362aa0d7340bf"></a>
<a id="a2e5c141fdfe76febfc08878c209d804ea377ec0e73db27706ea11a634b7c316ed"></a>
<a id="a2e5c141fdfe76febfc08878c209d804ead94d8ceb5df3fbd98b8f9f913e0080c7"></a>
<a id="a2e5c141fdfe76febfc08878c209d804ea3f824959a8bf61afb6e595b4aa8c876e"></a>
<a id="a2e5c141fdfe76febfc08878c209d804eaab97abcb143c4366a8e3074b4d5d2a93"></a>
<a id="a2e5c141fdfe76febfc08878c209d804eaf760bfd6fa7c71bc01cbc058299d0102"></a>

---

[上一章](P121_zephyr__drivers__sensor__tcs3400.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P123_zephyr__drivers__firmware__scmi__transport.h_文件参考.md)
