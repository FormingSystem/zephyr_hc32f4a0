---
id: learning.zephyr-docs.api-source-reference.page-362
title: ina2xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第362章\_ina2xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h.html)。

## 362.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="agroup__ina2xx__interface_html_ga37021fdf250e53ed4c9967f7ca047f4c"></a>
<a id="agroup__ina2xx__interface_html_gadc510f74d492767788d1b607b1aaf546"></a>
<a id="agroup__ina2xx__interface_html_gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4"></a>
<a id="agroup__ina2xx__interface_html_ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3"></a>
<a id="agroup__ina2xx__interface_html_ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright 2025 Nova Dynamics LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_INA2XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_INA2XX_H_


#include <zephyr/drivers/sensor.h>

#ifdef __cplusplus
extern "C" {
#endif

enum sensor_channel_ina2xx {
        SENSOR_CHAN_INA2XX_ENERGY = SENSOR_CHAN_PRIV_START,

        SENSOR_CHAN_INA2XX_CHARGE,
};

enum sensor_attribute_ina2xx {
        SENSOR_ATTR_ADC_CONFIGURATION = SENSOR_ATTR_PRIV_START,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_INA2XX_H_ */
```

## 362.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Nova Dynamics LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_INA2XX_H_`。

## 362.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ina2xx_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gadc510f74d492767788d1b607b1aaf546)
- [SENSOR_CHAN_INA2XX_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546a8553896697b4b815cc6847b9eff062a3)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_INA2XX_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ggadc510f74d492767788d1b607b1aaf546af3aa56f79a8b02d04cfb8c1ab8d4bfff)
- [sensor_attribute_ina2xx](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#ga37021fdf250e53ed4c9967f7ca047f4c)
- [SENSOR_ATTR_ADC_CONFIGURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__ina2xx__interface.html#gga37021fdf250e53ed4c9967f7ca047f4caa97b247e30f7f8fd981f4e372720e6c4)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P361_ina237.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P363_error.h_源码浏览.md)
