---
id: learning.zephyr-docs.api-file-configuration-reference.page-41
title: zephyr__drivers__sensor__ina2xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_drivers\_\_sensor\_\_ina2xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

INA2xx系列电流/功率监测器（Current / Power Monitors）的扩展公共API。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

INA2xx系列电流/功率监测器（Current / Power Monitors）的扩展公共API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 41.1\_枚举（Enumerations）

<a id="r_gadc510f74d492767788d1b607b1aaf546"></a>

```c
enum sensor_channel_ina2xx { SENSOR_CHAN_INA2XX_ENERGY = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_INA2XX_CHARGE }
```

相关声明：[sensor_channel_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gadc510f74d492767788d1b607b1aaf546)、[SENSOR_CHAN_INA2XX_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3)、[SENSOR_CHAN_INA2XX_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff)。

INA2xx 系列的自定义传感器通道（Custom Sensor Channels）。

<a id="r_ga37021fdf250e53ed4c9967f7ca047f4c"></a>

```c
enum sensor_attribute_ina2xx { SENSOR_ATTR_ADC_CONFIGURATION = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ga37021fdf250e53ed4c9967f7ca047f4c)、[SENSOR_ATTR_ADC_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4)。

INA2xx 系列的扩展传感器属性（Extended Sensor Attributes）。


## 41.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P362_ina2xx.h_源码浏览.md)
- [sensor_channel_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gadc510f74d492767788d1b607b1aaf546)
- [SENSOR_CHAN_INA2XX_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3)
- [SENSOR_CHAN_INA2XX_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff)
- [sensor_attribute_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ga37021fdf250e53ed4c9967f7ca047f4c)
- [SENSOR_ATTR_ADC_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4)

<a id="header-details"></a>

---

[上一章](P040_zephyr__net__igmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__input__input_hid.h_文件参考.md)
