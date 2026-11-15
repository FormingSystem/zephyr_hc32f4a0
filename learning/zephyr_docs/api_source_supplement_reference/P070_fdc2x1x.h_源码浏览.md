---
id: learning.zephyr-docs.api-source-supplement-reference.page-70
title: fdc2x1x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_fdc2x1x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h.html)。

## 70.1\_原始可见代码（Source Code）

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
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="agroup__fdc2x1x__interface_html_ga54b192a2943c38935321de727e803424"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3"></a>
<a id="agroup__fdc2x1x__interface_html_gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50"></a>
<a id="agroup__sensor__interface_html_ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2020 arithmetics.io
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_FDC2X1X_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_FDC2X1X_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

enum sensor_channel_fdc2x1x {
        SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0 = SENSOR_CHAN_PRIV_START,
        SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1,
        SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2,
        SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3,

        SENSOR_CHAN_FDC2X1X_FREQ_CH0,
        SENSOR_CHAN_FDC2X1X_FREQ_CH1,
        SENSOR_CHAN_FDC2X1X_FREQ_CH2,
        SENSOR_CHAN_FDC2X1X_FREQ_CH3,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_FDC2X1X_ */
```

## 70.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 arithmetics.io。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 60 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_FDC2X1X_`。

## 70.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_channel_fdc2x1x](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#ga54b192a2943c38935321de727e803424)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50)
- [SENSOR_CHAN_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P069_exception.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P071_fff_extensions.h_源码浏览.md)
