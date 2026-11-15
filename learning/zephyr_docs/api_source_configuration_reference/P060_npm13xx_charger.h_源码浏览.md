---
id: learning.zephyr-docs.api-source-configuration-reference.page-60
title: npm13xx_charger.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_npm13xx\_charger.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html)。

## 60.1\_原始可见代码（Source Code）

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
<a id="foldopen00012"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="anpm13xx__charger_8h_html_a3b5c9edfeb25c77685d67babdc4c5299"></a>
<a id="anpm13xx__charger_8h_html_a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b"></a>
<a id="anpm13xx__charger_8h_html_a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2"></a>
<a id="anpm13xx__charger_8h_html_a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283"></a>
<a id="anpm13xx__charger_8h_html_add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM13XX_CHARGER_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM13XX_CHARGER_H_

#include <zephyr/drivers/sensor.h>

/* NPM13XX charger specific channels */
enum sensor_channel_npm13xx_charger {
        SENSOR_CHAN_NPM13XX_CHARGER_STATUS = SENSOR_CHAN_PRIV_START,
        SENSOR_CHAN_NPM13XX_CHARGER_ERROR,
        SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS,
};

/* NPM13XX charger specific attributes */
enum sensor_attribute_npm13xx_charger {
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_PRESENT = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_CUR_LIMIT,
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_OVERVLT_PROT,
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_UNDERVLT,
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_SUSPENDED,
        SENSOR_ATTR_NPM13XX_CHARGER_VBUS_BUSOUT,
};

#endif
```

## 60.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

NPM13XX 充电器专用通道。

### 注释 3：原第 18 行

NPM13XX 充电器专用属性。

## 60.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_npm13xx_charger](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#a3b5c9edfeb25c77685d67babdc4c5299)
- [SENSOR_CHAN_NPM13XX_CHARGER_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#a3b5c9edfeb25c77685d67babdc4c5299abb7d0a263602d5a4e7fddf5b7fa44946)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_NPM13XX_CHARGER_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#a3b5c9edfeb25c77685d67babdc4c5299a68daf03ea54b12dba3bd2cac5d5f142b)
- [SENSOR_CHAN_NPM13XX_CHARGER_VBUS_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#a3b5c9edfeb25c77685d67babdc4c5299aa070958a66af182e1db9c49a6a41c8c2)
- [sensor_attribute_npm13xx_charger](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_PRESENT](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058ac65dd6d01c5995c1f0514daaded1c283)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_CUR_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058a3faad43b78763a2520e9a87baf38265b)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_OVERVLT_PROT](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058a5674d4ecc2377640a42fc78fef60c0ab)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_UNDERVLT](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058addc2f6fbe32fd3bdadeb6c5d3aa00a08)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058a7e1153a7eeb8e02925d0ee57c79b8a31)
- [SENSOR_ATTR_NPM13XX_CHARGER_VBUS_BUSOUT](https://docs.zephyrproject.org/latest/doxygen/html/npm13xx__charger_8h.html#add553da0fb80ee2cfb6a5b009a1d6058abb429313846ec7adbf09d84b5385e2bc)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P059_mspm0_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P061_npm2100_vbat.h_源码浏览.md)
