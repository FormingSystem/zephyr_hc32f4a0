---
id: learning.zephyr-docs.api-source-reference.page-903
title: veaa_x_3.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/veaa__x__3_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第903章\_veaa\_x\_3.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/veaa__x__3_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/veaa__x__3_8h.html)。

## 903.1\_原始可见代码（Source Code）

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
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__veaa__x__3__interface_html_ga0766ed6ec5cca998f67ae8061ee9e862"></a>
<a id="agroup__veaa__x__3__interface_html_gga0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3"></a>
<a id="agroup__veaa__x__3__interface_html_gga0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Prevas A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEAA_X_3_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEAA_X_3_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

enum sensor_attribute_veaa_x_3 {
        SENSOR_ATTR_VEAA_X_3_SETPOINT = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_VEAA_X_3_RANGE,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEAA_X_3_H_ */
```

## 903.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Prevas A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_VEAA_X_3_H_`。

## 903.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/veaa__x__3_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_veaa_x_3](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html#ga0766ed6ec5cca998f67ae8061ee9e862)
- [SENSOR_ATTR_VEAA_X_3_SETPOINT](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html#gga0766ed6ec5cca998f67ae8061ee9e862a9c7fbc183c05b73e5345677b8cd69bd3)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_VEAA_X_3_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__veaa__x__3__interface.html#gga0766ed6ec5cca998f67ae8061ee9e862ae783f1639cec9875927dcc7157b292bc)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P902_vcp.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P904_veml6031.h_源码浏览.md)
