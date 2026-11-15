---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-13
title: ti_hdc302x.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti__hdc302x_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ti\_hdc302x.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ti__hdc302x_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md)。

## 13.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00025"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="foldopen00064"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="adrivers_2i2c_8h_html"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804e"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804ea377ec0e73db27706ea11a634b7c316ed"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804ea3f824959a8bf61afb6e595b4aa8c876e"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804eaab97abcb143c4366a8e3074b4d5d2a93"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804ead94d8ceb5df3fbd98b8f9f913e0080c7"></a>
<a id="ati__hdc302x_8h_html_a2e5c141fdfe76febfc08878c209d804eaf760bfd6fa7c71bc01cbc058299d0102"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896a01f370f86e630ca4892fa76ff8c08cfd"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896a0634192bddd4b40e9fd362aa0d7340bf"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896a12d80d9a5105ea987d4c2a0a71cbe8d8"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896a5f26dd9cf416c1c49c553517bb3d430d"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896a97369b309fa9314e17ed037156a09285"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896ac63b8ec4d957ec2691a1ca7906d0ebfd"></a>
<a id="ati__hdc302x_8h_html_a556419bccd5c76de43c27fcdf93c0896ac861f09a400d473067a8f3ba7a989acb"></a>
<a id="ati__hdc302x_8h_html_af9b817b9c11d3b73f563f0bf08cedf8f"></a>
<a id="ati__hdc302x_8h_html_af9b817b9c11d3b73f563f0bf08cedf8fa4772c29035f16339008525cc3e639947"></a>
<a id="ati__hdc302x_8h_html_af9b817b9c11d3b73f563f0bf08cedf8fad6ac196a42cad27354914526ed101986"></a>
<a id="ati__hdc302x_8h_html_af9b817b9c11d3b73f563f0bf08cedf8fade393ab7f8ba4ff6f85cd3d6c0a9cbc2"></a>
<a id="ati__hdc302x_8h_html_af9b817b9c11d3b73f563f0bf08cedf8faeba46c663afa61df6d07ce3f90f2ec59"></a>

```c
/*
 * Copyright (c) 2025 Psicontrol N.V.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_TI_HDC302X_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_TI_HDC302X_H_

#include <zephyr/drivers/sensor.h>
#include <zephyr/drivers/i2c.h>

#ifdef __cplusplus
extern "C" {
#endif

enum sensor_attribute_hdc302x {
        /* Sensor low power Mode
         * Rather than set this value directly, can only be set to operate in one of four modes:
         *
         * HDC302X_SENSOR_POWER_MODE_0
         * HDC302X_SENSOR_POWER_MODE_1
         * HDC302X_SENSOR_POWER_MODE_2
         * HDC302X_SENSOR_POWER_MODE_3
         *
         * See datasheet for more info on different modes.
         */
        SENSOR_ATTR_POWER_MODE = SENSOR_ATTR_PRIV_START + 1,

        /* Sensor Automatic Measurement Mode
         * Can only be set to one of the following values:
         *
         * HDC302X_SENSOR_MEAS_INTERVAL_MANUAL,
         * HDC302X_SENSOR_MEAS_INTERVAL_0_5,
         * HDC302X_SENSOR_MEAS_INTERVAL_1,
         * HDC302X_SENSOR_MEAS_INTERVAL_2,
         * HDC302X_SENSOR_MEAS_INTERVAL_4,
         * HDC302X_SENSOR_MEAS_INTERVAL_10,
         */
        SENSOR_ATTR_INTEGRATION_TIME,
        /* Sensor status register */
        SENSOR_ATTR_STATUS_REGISTER,
        /* Sensor heater level */
        SENSOR_ATTR_HEATER_LEVEL, /* Heater level (0-14) */
};

enum sensor_power_mode_hdc302x {
        HDC302X_SENSOR_POWER_MODE_0, /* (lowest noise) */
        HDC302X_SENSOR_POWER_MODE_1,
        HDC302X_SENSOR_POWER_MODE_2,
        HDC302X_SENSOR_POWER_MODE_3, /* (lowest power) */

        HDC302X_SENSOR_POWER_MODE_MAX
};

enum sensor_measurement_interval_hdc302x {
        HDC302X_SENSOR_MEAS_INTERVAL_MANUAL, /*  Manual Mode                 */
        HDC302X_SENSOR_MEAS_INTERVAL_0_5,    /*  1 Measurement per 2 Seconds */
        HDC302X_SENSOR_MEAS_INTERVAL_1,      /*  1 Measurement per Second    */
        HDC302X_SENSOR_MEAS_INTERVAL_2,      /*  2 Measurements per Second   */
        HDC302X_SENSOR_MEAS_INTERVAL_4,      /*  4 Measurements per Second   */
        HDC302X_SENSOR_MEAS_INTERVAL_10,     /* 10 Measurements per Second   */

        HDC302X_SENSOR_MEAS_INTERVAL_MAX
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_TI_HDC302X_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Psicontrol N.V.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

传感器低功耗模式（Sensor low power Mode）。不得直接设置任意值，只能设置为以下四种工作模式之一：

- `HDC302X_SENSOR_POWER_MODE_0`
- `HDC302X_SENSOR_POWER_MODE_1`
- `HDC302X_SENSOR_POWER_MODE_2`
- `HDC302X_SENSOR_POWER_MODE_3`

有关各模式的详细信息，请参阅数据手册（datasheet）。

### 注释 3：原第 38 行

传感器自动测量模式（Sensor Automatic Measurement Mode）。只能设置为下列值之一：

- `HDC302X_SENSOR_MEAS_INTERVAL_MANUAL`
- `HDC302X_SENSOR_MEAS_INTERVAL_0_5`
- `HDC302X_SENSOR_MEAS_INTERVAL_1`
- `HDC302X_SENSOR_MEAS_INTERVAL_2`
- `HDC302X_SENSOR_MEAS_INTERVAL_4`
- `HDC302X_SENSOR_MEAS_INTERVAL_10`

### 注释 4：原第 49 行

传感器状态寄存器（status register）。

### 注释 5：原第 51 行

传感器加热器档位（heater level）。

### 注释 6：原第 52 行

加热器档位（heater level），取值为 0–14。

### 注释 7：原第 56 行

最低噪声（lowest noise）。

### 注释 8：原第 59 行

最低功耗（lowest power）。

### 注释 9：原第 65 行

手动模式（Manual Mode）。

### 注释 10：原第 66 行

每 2 秒测量 1 次。

### 注释 11：原第 67 行

每秒测量 1 次。

### 注释 12：原第 68 行

每秒测量 2 次。

### 注释 13：原第 69 行

每秒测量 4 次。

### 注释 14：原第 70 行

每秒测量 10 次。

### 注释 15：原第 79 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_TI_HDC302X_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [sensor_attribute_hdc302x](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#af9b817b9c11d3b73f563f0bf08cedf8f)
- [SENSOR_ATTR_POWER_MODE](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#af9b817b9c11d3b73f563f0bf08cedf8fad6ac196a42cad27354914526ed101986)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_INTEGRATION_TIME](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#af9b817b9c11d3b73f563f0bf08cedf8faeba46c663afa61df6d07ce3f90f2ec59)
- [SENSOR_ATTR_STATUS_REGISTER](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#af9b817b9c11d3b73f563f0bf08cedf8fade393ab7f8ba4ff6f85cd3d6c0a9cbc2)
- [SENSOR_ATTR_HEATER_LEVEL](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#af9b817b9c11d3b73f563f0bf08cedf8fa4772c29035f16339008525cc3e639947)
- [sensor_power_mode_hdc302x](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804e)
- [HDC302X_SENSOR_POWER_MODE_0](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804ea377ec0e73db27706ea11a634b7c316ed)
- [HDC302X_SENSOR_POWER_MODE_1](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804ead94d8ceb5df3fbd98b8f9f913e0080c7)
- [HDC302X_SENSOR_POWER_MODE_2](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804ea3f824959a8bf61afb6e595b4aa8c876e)
- [HDC302X_SENSOR_POWER_MODE_3](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804eaab97abcb143c4366a8e3074b4d5d2a93)
- [HDC302X_SENSOR_POWER_MODE_MAX](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a2e5c141fdfe76febfc08878c209d804eaf760bfd6fa7c71bc01cbc058299d0102)
- [sensor_measurement_interval_hdc302x](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896)
- [HDC302X_SENSOR_MEAS_INTERVAL_MANUAL](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896a97369b309fa9314e17ed037156a09285)
- [HDC302X_SENSOR_MEAS_INTERVAL_0_5](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896a12d80d9a5105ea987d4c2a0a71cbe8d8)
- [HDC302X_SENSOR_MEAS_INTERVAL_1](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896a01f370f86e630ca4892fa76ff8c08cfd)
- [HDC302X_SENSOR_MEAS_INTERVAL_2](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896ac63b8ec4d957ec2691a1ca7906d0ebfd)
- [HDC302X_SENSOR_MEAS_INTERVAL_4](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896ac861f09a400d473067a8f3ba7a989acb)
- [HDC302X_SENSOR_MEAS_INTERVAL_10](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896a5f26dd9cf416c1c49c553517bb3d430d)
- [HDC302X_SENSOR_MEAS_INTERVAL_MAX](../api_file_supplement_reference/P122_zephyr__drivers__sensor__ti_hdc302x.h_文件参考.md#a556419bccd5c76de43c27fcdf93c0896a0634192bddd4b40e9fd362aa0d7340bf)
- [i2c.h](../i2c_driver_reference/P001_I2C驱动头文件参考.md)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P012_sys_getopt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_timestamp.h_源码浏览.md)
