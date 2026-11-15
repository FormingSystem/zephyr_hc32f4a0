---
id: learning.zephyr-docs.api-source-reference.page-180
title: npm10xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第180章\_npm10xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h.html)。

## 180.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00022"></a>
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="agroup__sensor__interface__npm10xx_html_ga5d1bad2f8fe96e651b5637ff59009cab"></a>
<a id="agroup__sensor__interface__npm10xx_html_gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a"></a>
<a id="agroup__sensor__interface__npm10xx_html_gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa"></a>
<a id="agroup__sensor__interface__npm10xx_html_gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM10XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM10XX_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>


enum npm10xx_sensor_chan {
        NPM10XX_SENSOR_CHAN_VSYS = SENSOR_CHAN_PRIV_START,
        NPM10XX_SENSOR_CHAN_VBUS,
        NPM10XX_SENSOR_CHAN_OFFSET,
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM10XX_H_ */
```

## 180.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 39 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM10XX_H_`。

## 180.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2npm10xx_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [npm10xx_sensor_chan](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#ga5d1bad2f8fe96e651b5637ff59009cab)
- [NPM10XX_SENSOR_CHAN_VSYS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba17daa3620ccc82aa2a512cb6e9b8ad0a)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [NPM10XX_SENSOR_CHAN_VBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009caba43be67d949b7d3d59ab091ed773e01fa)
- [NPM10XX_SENSOR_CHAN_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface__npm10xx.html#gga5d1bad2f8fe96e651b5637ff59009cabae9b04b8540ecef1d994be29d261fdb18)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P179_max30009.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P181_pac194x.h_源码浏览.md)
