---
id: learning.zephyr-docs.api-source-reference.page-686
title: qdec_bee.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/qdec__bee_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第686章\_qdec\_bee.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/qdec__bee_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/qdec__bee_8h.html)。

## 686.1\_原始可见代码（Source Code）

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
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="agroup__qdec__bee__interface_html_gacbac5e46dc517ffe889f7e7352cac18c"></a>
<a id="agroup__qdec__bee__interface_html_ggacbac5e46dc517ffe889f7e7352cac18ca6e0b15769b472ca1579cd9360b2a31c6"></a>
<a id="agroup__qdec__bee__interface_html_ggacbac5e46dc517ffe889f7e7352cac18ca906cf6ffe58d3f7a57455f666cddbbae"></a>
<a id="agroup__qdec__bee__interface_html_ggacbac5e46dc517ffe889f7e7352cac18cabe71e0cfa084e4f2c1d3f09a79857845"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2026, Realtek Semiconductor Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_BEE_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_BEE_H_

#include <zephyr/drivers/sensor.h>


enum sensor_channel_qdec_bee {
        SENSOR_CHAN_QDEC_X_COUNT = SENSOR_CHAN_PRIV_START,
        SENSOR_CHAN_QDEC_Y_COUNT,
        SENSOR_CHAN_QDEC_Z_COUNT,
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_BEE_H_ */
```

## 686.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026, Realtek Semiconductor Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 43 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_QDEC_BEE_H_`。

## 686.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/qdec__bee_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_qdec_bee](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html#gacbac5e46dc517ffe889f7e7352cac18c)
- [SENSOR_CHAN_QDEC_X_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html#ggacbac5e46dc517ffe889f7e7352cac18cabe71e0cfa084e4f2c1d3f09a79857845)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_QDEC_Y_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html#ggacbac5e46dc517ffe889f7e7352cac18ca6e0b15769b472ca1579cd9360b2a31c6)
- [SENSOR_CHAN_QDEC_Z_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__qdec__bee__interface.html#ggacbac5e46dc517ffe889f7e7352cac18ca906cf6ffe58d3f7a57455f666cddbbae)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P685_pwm_utils.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P687_qdec_mcux.h_源码浏览.md)
