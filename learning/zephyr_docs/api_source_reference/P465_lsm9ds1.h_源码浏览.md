---
id: learning.zephyr-docs.api-source-reference.page-465
title: lsm9ds1.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第465章\_lsm9ds1.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h.html)。

## 465.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
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
<a id="l00081"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00093"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>

```c
/*
 * Copyright (c) 2024 Bootlin
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM9DS1_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM9DS1_H_


#define LSM9DS1_DT_FS_2G  0
#define LSM9DS1_DT_FS_16G 1
#define LSM9DS1_DT_FS_4G  2
#define LSM9DS1_DT_FS_8G  3

#define LSM9DS1_DT_FS_245DPS  0
#define LSM9DS1_DT_FS_500DPS  1
#define LSM9DS1_DT_FS_2000DPS 3

#define LSM9DS1_IMU_OFF            0x00
#define LSM9DS1_GY_OFF_XL_10Hz     0x10
#define LSM9DS1_GY_OFF_XL_50Hz     0x20
#define LSM9DS1_GY_OFF_XL_119Hz    0x30
#define LSM9DS1_GY_OFF_XL_238Hz    0x40
#define LSM9DS1_GY_OFF_XL_476Hz    0x50
#define LSM9DS1_GY_OFF_XL_952Hz    0x60
#define LSM9DS1_XL_OFF_GY_14Hz9    0x01
#define LSM9DS1_XL_OFF_GY_59Hz5    0x02
#define LSM9DS1_XL_OFF_GY_119Hz    0x03
#define LSM9DS1_XL_OFF_GY_238Hz    0x04
#define LSM9DS1_XL_OFF_GY_476Hz    0x05
#define LSM9DS1_XL_OFF_GY_952Hz    0x06
#define LSM9DS1_IMU_14Hz9          0x11
#define LSM9DS1_IMU_59Hz5          0x22
#define LSM9DS1_IMU_119Hz          0x33
#define LSM9DS1_IMU_238Hz          0x44
#define LSM9DS1_IMU_476Hz          0x55
#define LSM9DS1_IMU_952Hz          0x66
#define LSM9DS1_XL_OFF_GY_14Hz9_LP 0x81
#define LSM9DS1_XL_OFF_GY_59Hz5_LP 0x82
#define LSM9DS1_XL_OFF_GY_119Hz_LP 0x83
#define LSM9DS1_IMU_14Hz9_LP       0x91
#define LSM9DS1_IMU_59Hz5_LP       0xA2
#define LSM9DS1_IMU_119Hz_LP       0xB3

#define LSM9DS1_DT_FS_4Ga  0
#define LSM9DS1_DT_FS_8Ga  1
#define LSM9DS1_DT_FS_12Ga 2
#define LSM9DS1_DT_FS_16Ga 3

#define LSM9DS1_MAG_POWER_DOWN 0xC0
#define LSM9DS1_MAG_LP_0Hz625  0x00
#define LSM9DS1_MAG_LP_1Hz25   0x01
#define LSM9DS1_MAG_LP_2Hz5    0x02
#define LSM9DS1_MAG_LP_5Hz     0x03
#define LSM9DS1_MAG_LP_10Hz    0x04
#define LSM9DS1_MAG_LP_20Hz    0x05
#define LSM9DS1_MAG_LP_40Hz    0x06
#define LSM9DS1_MAG_LP_80Hz    0x07
#define LSM9DS1_MAG_MP_0Hz625  0x10
#define LSM9DS1_MAG_MP_1Hz25   0x11
#define LSM9DS1_MAG_MP_2Hz5    0x12
#define LSM9DS1_MAG_MP_5Hz     0x13
#define LSM9DS1_MAG_MP_10Hz    0x14
#define LSM9DS1_MAG_MP_20Hz    0x15
#define LSM9DS1_MAG_MP_40Hz    0x16
#define LSM9DS1_MAG_MP_80Hz    0x17
#define LSM9DS1_MAG_HP_0Hz625  0x20
#define LSM9DS1_MAG_HP_1Hz25   0x21
#define LSM9DS1_MAG_HP_2Hz5    0x22
#define LSM9DS1_MAG_HP_5Hz     0x23
#define LSM9DS1_MAG_HP_10Hz    0x24
#define LSM9DS1_MAG_HP_20Hz    0x25
#define LSM9DS1_MAG_HP_40Hz    0x26
#define LSM9DS1_MAG_HP_80Hz    0x27
#define LSM9DS1_MAG_UHP_0Hz625 0x30
#define LSM9DS1_MAG_UHP_1Hz25  0x31
#define LSM9DS1_MAG_UHP_2Hz5   0x32
#define LSM9DS1_MAG_UHP_5Hz    0x33
#define LSM9DS1_MAG_UHP_10Hz   0x34
#define LSM9DS1_MAG_UHP_20Hz   0x35
#define LSM9DS1_MAG_UHP_40Hz   0x36
#define LSM9DS1_MAG_UHP_80Hz   0x37
#define LSM9DS1_MAG_UHP_155Hz  0x38
#define LSM9DS1_MAG_HP_300Hz   0x28
#define LSM9DS1_MAG_MP_560Hz   0x18
#define LSM9DS1_MAG_LP_1000Hz  0x08
#define LSM9DS1_MAG_ONE_SHOT   0x70


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM9DS1_H_ */
```

## 465.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Bootlin。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 145 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_SENSOR_LSM9DS1_H_`。

## 465.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/lsm9ds1_8h.html)

---

[上一章](P464_lsm6dsv80x.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P466_ltc4286.h_源码浏览.md)
