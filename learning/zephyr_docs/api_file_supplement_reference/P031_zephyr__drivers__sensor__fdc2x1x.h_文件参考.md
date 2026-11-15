---
id: learning.zephyr-docs.api-file-supplement-reference.page-31
title: zephyr__drivers__sensor__fdc2x1x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_drivers\_\_sensor\_\_fdc2x1x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fdc2x1x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FDC2X1X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

FDC2X1X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.1\_枚举（Enumerations）

<a id="r_ga54b192a2943c38935321de727e803424"></a>

```c
enum sensor_channel_fdc2x1x { SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0 = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1 , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2 , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3 , SENSOR_CHAN_FDC2X1X_FREQ_CH0 , SENSOR_CHAN_FDC2X1X_FREQ_CH1 , SENSOR_CHAN_FDC2X1X_FREQ_CH2 , SENSOR_CHAN_FDC2X1X_FREQ_CH3 }
```

相关声明：[sensor_channel_fdc2x1x](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#ga54b192a2943c38935321de727e803424)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837)、[SENSOR_CHAN_FDC2X1X_FREQ_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491)、[SENSOR_CHAN_FDC2X1X_FREQ_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed)、[SENSOR_CHAN_FDC2X1X_FREQ_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3)、[SENSOR_CHAN_FDC2X1X_FREQ_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d)。

FDC2X1X 的自定义传感器通道（Custom Sensor Channels）。


## 31.2\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_supplement_reference/P070_fdc2x1x.h_源码浏览.md)
- [sensor_channel_fdc2x1x](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#ga54b192a2943c38935321de727e803424)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332)
- [SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH0](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH1](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH2](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3)
- [SENSOR_CHAN_FDC2X1X_FREQ_CH3](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html#gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d)

<a id="header-details"></a>

---

[上一章](P030_zephyr__drivers__sensor__f75303.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__fff_extensions.h_文件参考.md)
