---
id: learning.zephyr-docs.api-source-reference.page-781
title: sht4x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第781章\_sht4x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h.html)。

## 781.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00044"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sht4x__interface_html_ga4191e02c97b8130a1c96d47c0939d535"></a>
<a id="agroup__sht4x__interface_html_gaf2539064f44eb3981cb40a3c2f7a0eb8"></a>
<a id="agroup__sht4x__interface_html_gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6"></a>
<a id="agroup__sht4x__interface_html_gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052"></a>
<a id="asensor_8h_html"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright (c) 2021, Leonard Pollak
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_SHT4X_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_SHT4X_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

#define SHT4X_HEATER_MAX_TEMP 65

enum sensor_attribute_sht4x {
        SENSOR_ATTR_SHT4X_HEATER_POWER = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_SHT4X_HEATER_DURATION
};

int sht4x_fetch_with_heater(const struct device *dev);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_SHT4X_H_ */
```

## 781.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021, Leonard Pollak。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_SHT4X_H_`。

## 781.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sht4x_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_sht4x](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#ga4191e02c97b8130a1c96d47c0939d535)
- [SENSOR_ATTR_SHT4X_HEATER_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535ad18746a0cddc2713d63b0b6ce70f5052)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_SHT4X_HEATER_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gga4191e02c97b8130a1c96d47c0939d535a1812fd253d281025c8d4155f58e9cbd6)
- [sht4x_fetch_with_heater](https://docs.zephyrproject.org/latest/doxygen/html/group__sht4x__interface.html#gaf2539064f44eb3981cb40a3c2f7a0eb8)
- [device](../device_reference/P002_设备对象结构.md)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P780_shmem.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P782_si32-pinctrl.h_源码浏览.md)
