---
id: learning.zephyr-docs.api-source-configuration-reference.page-61
title: npm2100_vbat.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_npm2100\_vbat.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html)。

## 61.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="anpm2100__vbat_8h_html_a0c9921cfee8de69b35666e1ab276196e"></a>
<a id="anpm2100__vbat_8h_html_a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49"></a>
<a id="anpm2100__vbat_8h_html_ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM2100_VBAT_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_NPM2100_VBAT_H_

#include <zephyr/drivers/sensor.h>

/* NPM2100 vbat specific channels */
enum sensor_channel_npm2100_vbat {
        SENSOR_CHAN_NPM2100_VBAT_STATUS = SENSOR_CHAN_PRIV_START,
        SENSOR_CHAN_NPM2100_VOLT_DROOP,
        SENSOR_CHAN_NPM2100_DPS_COUNT,
        SENSOR_CHAN_NPM2100_DPS_TIMER,
        SENSOR_CHAN_NPM2100_DPS_DURATION,
};

/* NPM2100 vbat specific attributes */
enum sensor_attr_npm2100_vbat {
        SENSOR_ATTR_NPM2100_ADC_DELAY = SENSOR_ATTR_PRIV_START,
};

#endif
```

## 61.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

NPM2100 电池电压（vbat）专用通道。

### 注释 3：原第 20 行

NPM2100 电池电压（vbat）专用属性。

## 61.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_npm2100_vbat](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7)
- [SENSOR_CHAN_NPM2100_VBAT_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7ab2556cfe11bce37125a1b2c734acc368)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_NPM2100_VOLT_DROOP](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7a5b291484fb7cf4978bd7607081ccbd4a)
- [SENSOR_CHAN_NPM2100_DPS_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7afa85e0dbca574d95493578cac8bff834)
- [SENSOR_CHAN_NPM2100_DPS_TIMER](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7a95abddd9aabcf283728d0fbd32834623)
- [SENSOR_CHAN_NPM2100_DPS_DURATION](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#ad07cbdadaca3c654f3a27a54f74b30e7ae722a338b422b8310d0c999ef510cb49)
- [sensor_attr_npm2100_vbat](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#a0c9921cfee8de69b35666e1ab276196e)
- [SENSOR_ATTR_NPM2100_ADC_DELAY](https://docs.zephyrproject.org/latest/doxygen/html/npm2100__vbat_8h.html#a0c9921cfee8de69b35666e1ab276196ea6523499d40a42c85a2d316b74859ba1d)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P060_npm13xx_charger.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P062_obex.h_源码浏览.md)
