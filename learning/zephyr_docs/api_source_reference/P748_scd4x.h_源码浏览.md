---
id: learning.zephyr-docs.api-source-reference.page-748
title: scd4x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第748章\_scd4x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h.html)。

## 748.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00038"></a>
<a id="l00044"></a>
<a id="l00050"></a>
<a id="l00056"></a>
<a id="l00063"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="agroup__scd4x__interface_html_ga076766c7322d9b050acf5963ceba718a"></a>
<a id="agroup__scd4x__interface_html_ga8cbb7f3f4cad13f36cd454073e9d344d"></a>
<a id="agroup__scd4x__interface_html_ga91f055d3b7a4c8c70c30982cf0ceff9c"></a>
<a id="agroup__scd4x__interface_html_ga9c7260e275f85836ea717186ff8aa796"></a>
<a id="agroup__scd4x__interface_html_gaa501b89af4dbed0dc9be5d1bc1742c99"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a"></a>
<a id="agroup__scd4x__interface_html_gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2024 Jan Fäh
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_SCD4X_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_SCD4X_H_


#include <zephyr/drivers/sensor.h>

enum sensor_attribute_scd4x {
        SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE,
        SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE,
        SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE,
        SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD,
        SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD,
};

int scd4x_forced_recalibration(const struct device *dev, uint16_t target_concentration,
                               uint16_t *frc_correction);

int scd4x_self_test(const struct device *dev);

int scd4x_persist_settings(const struct device *dev);

int scd4x_factory_reset(const struct device *dev);


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_SCD4X_H_ */
```

## 748.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Jan Fäh。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_SCD4X_H_`。

## 748.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/scd4x_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_scd4x](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga8cbb7f3f4cad13f36cd454073e9d344d)
- [SENSOR_ATTR_SCD4X_TEMPERATURE_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa8c54289d95f79519831458018ccb4ba)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_SCD4X_SENSOR_ALTITUDE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac2697f0466ec1822fbfe82e7b5d6287e)
- [SENSOR_ATTR_SCD4X_AMBIENT_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344daa6a806666dcb476b83c1affb15c2964c)
- [SENSOR_ATTR_SCD4X_AUTOMATIC_CALIB_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dae61b7281c3d3135bc1557e970d6b2b14)
- [SENSOR_ATTR_SCD4X_SELF_CALIB_INITIAL_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344da8dccaa05552bbc5b9c474cbaa65ed7b0)
- [SENSOR_ATTR_SCD4X_SELF_CALIB_STANDARD_PERIOD](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gga8cbb7f3f4cad13f36cd454073e9d344dac54720c5cb0dce105986b8b6c7b0ea8a)
- [scd4x_forced_recalibration](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga9c7260e275f85836ea717186ff8aa796)
- [device](../device_reference/P002_设备对象结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [scd4x_self_test](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga076766c7322d9b050acf5963ceba718a)
- [scd4x_persist_settings](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#ga91f055d3b7a4c8c70c30982cf0ceff9c)
- [scd4x_factory_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__scd4x__interface.html#gaa501b89af4dbed0dc9be5d1bc1742c99)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P747_sbc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P749_scg_k4.h_源码浏览.md)
