---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-7
title: FDC2X1X API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_FDC2X1X API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fdc2x1x__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Texas Instruments FDC2X1X 电容传感器（Capacitive sensor）。

<a id="details"></a>

Texas Instruments FDC2X1X 电容传感器（Capacitive sensor）。

<a id="header-files"></a>
<a id="files"></a>

## 7.1\_文件（Files）

<a id="r_fdc2x1x_2Eh"></a>

```c
file fdc2x1x.h
```

相关声明：[fdc2x1x.h](../api_file_supplement_reference/P031_zephyr__drivers__sensor__fdc2x1x.h_文件参考.md)。

FDC2X1X传感器的扩展API头文件（Extended Sensor API Header）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 7.2\_枚举（Enumerations）

<a id="r_ga54b192a2943c38935321de727e803424"></a>

```c
enum sensor_channel_fdc2x1x { SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0 = SENSOR_CHAN_PRIV_START , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1 , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2 , SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3 , SENSOR_CHAN_FDC2X1X_FREQ_CH0 , SENSOR_CHAN_FDC2X1X_FREQ_CH1 , SENSOR_CHAN_FDC2X1X_FREQ_CH2 , SENSOR_CHAN_FDC2X1X_FREQ_CH3 }
```

相关声明：[sensor_channel_fdc2x1x](#ga54b192a2943c38935321de727e803424)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0](#gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1](#gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2](#gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332)、[SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3](#gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837)、[SENSOR_CHAN_FDC2X1X_FREQ_CH0](#gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491)、[SENSOR_CHAN_FDC2X1X_FREQ_CH1](#gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed)、[SENSOR_CHAN_FDC2X1X_FREQ_CH2](#gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3)、[SENSOR_CHAN_FDC2X1X_FREQ_CH3](#gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d)。

FDC2X1X 的自定义传感器通道（Custom Sensor Channels）。

## 7.3\_详细说明（Detailed Documentation）

<a id="ga54b192a2943c38935321de727e803424"></a>

### `sensor_channel_fdc2x1x`

```c
enum sensor_channel_fdc2x1x
```

```c
#include <zephyr/drivers/sensor/fdc2x1x.h>
```

FDC2X1X 的自定义传感器通道（Custom Sensor Channels）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH0` | CH0 电容（capacitance），单位为皮法（pF）。 |
| `SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH1` | CH1 电容，单位为皮法（pF）。 |
| `SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH2` | CH2 电容，单位为皮法（pF）。 |
| `SENSOR_CHAN_FDC2X1X_CAPACITANCE_CH3` | CH3 电容，单位为皮法（pF）。 |
| `SENSOR_CHAN_FDC2X1X_FREQ_CH0` | CH0 频率（frequency），单位为 MHz。 |
| `SENSOR_CHAN_FDC2X1X_FREQ_CH1` | CH1 频率，单位为 MHz。 |
| `SENSOR_CHAN_FDC2X1X_FREQ_CH2` | CH2 频率，单位为 MHz。 |
| `SENSOR_CHAN_FDC2X1X_FREQ_CH3` | CH3 频率，单位为 MHz。 |


## 7.4\_原页交叉引用（Cross References）

- [fdc2x1x.h](../api_file_supplement_reference/P031_zephyr__drivers__sensor__fdc2x1x.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga54b192a2943c38935321de727e803424ae67ca7e5bf190118499123b0c53eef50"></a>
<a id="gga54b192a2943c38935321de727e803424abada5248fa138e6e86261c556b178720"></a>
<a id="gga54b192a2943c38935321de727e803424aac37d2db97bf0e615d8d32ee7c163332"></a>
<a id="gga54b192a2943c38935321de727e803424a7d093e4262cfd7c89d492e9fea7cc837"></a>
<a id="gga54b192a2943c38935321de727e803424a4edf2c46f77dba6ff63b731c7c723491"></a>
<a id="gga54b192a2943c38935321de727e803424a3533658442ff4abf624d1efe6be2c9ed"></a>
<a id="gga54b192a2943c38935321de727e803424adb42fc6433868dbbaaba669ffc84c1c3"></a>
<a id="gga54b192a2943c38935321de727e803424a62f569565ebb4f613ab4d12992b4630d"></a>

---

[上一章](P006_FCX-MLDX5 API主题.md) · [返回大纲](大纲.md) · [下一章](P008_AHB3RSTCR 复位控制（Reset Control）.md)
