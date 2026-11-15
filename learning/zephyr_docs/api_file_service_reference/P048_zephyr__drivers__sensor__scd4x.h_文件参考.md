---
id: learning.zephyr-docs.api-file-service-reference.page-48
title: zephyr__drivers__sensor__scd4x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第48章\_zephyr\_\_drivers\_\_sensor\_\_scd4x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SCD4X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

SCD4X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 48.1\_枚举（Enumerations）

<a id="r_ga8cbb7f3f4cad13f36cd454073e9d344d"></a>

```c
enum sensor_attribute_scd4x { SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET = SENSOR_ATTR_PRIV_START , SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE , SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE , SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE , SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD , SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD }
```

相关声明：[sensor_attribute_scd4x](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga8cbb7f3f4cad13f36cd454073e9d344d)、[SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba)、[SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e)、[SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c)、[SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14)、[SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0)、[SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)。

SCD4X 的自定义传感器属性（Custom Sensor Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 48.2\_函数（Functions）

<a id="r_ga9c7260e275f85836ea717186ff8aa796"></a>

```c
int scd4x_forced_recalibration (const struct device *dev, uint16_t target_concentration, uint16_t *frc_correction)
```

相关声明：[scd4x_forced_recalibration](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga9c7260e275f85836ea717186ff8aa796)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行强制重新校准（Forced Recalibration）。

<a id="r_ga076766c7322d9b050acf5963ceba718a"></a>

```c
int scd4x_self_test (const struct device *dev)
```

相关声明：[scd4x_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga076766c7322d9b050acf5963ceba718a)、[device](../device_reference/P002_设备对象结构.md)。

执行自检（Self Test）。

<a id="r_ga91f055d3b7a4c8c70c30982cf0ceff9c"></a>

```c
int scd4x_persist_settings (const struct device *dev)
```

相关声明：[scd4x_persist_settings](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga91f055d3b7a4c8c70c30982cf0ceff9c)、[device](../device_reference/P002_设备对象结构.md)。

执行自检（Self Test）。

<a id="r_gaa501b89af4dbed0dc9be5d1bc1742c99"></a>

```c
int scd4x_factory_reset (const struct device *dev)
```

相关声明：[scd4x_factory_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gaa501b89af4dbed0dc9be5d1bc1742c99)、[device](../device_reference/P002_设备对象结构.md)。

执行出厂复位（Factory Reset）。


## 48.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P748_scd4x.h_源码浏览.md)
- [sensor_attribute_scd4x](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga8cbb7f3f4cad13f36cd454073e9d344d)
- [SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba)
- [SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e)
- [SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c)
- [SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14)
- [SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0)
- [SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)
- [scd4x_forced_recalibration](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga9c7260e275f85836ea717186ff8aa796)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [scd4x_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga076766c7322d9b050acf5963ceba718a)
- [scd4x_persist_settings](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga91f055d3b7a4c8c70c30982cf0ceff9c)
- [scd4x_factory_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gaa501b89af4dbed0dc9be5d1bc1742c99)

<a id="header-details"></a>

---

[上一章](P047_zephyr__dt-bindings__pinctrl__rv32m1-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P049_zephyr__drivers__sensor__sht4x.h_文件参考.md)
