---
id: learning.zephyr-docs.api-source-reference.page-256
title: fcx_mldx5.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第256章\_fcx\_mldx5.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h.html)。

## 256.1\_原始可见代码（Source Code）

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
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00053"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00068"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="agroup__fcx__mldx5__interface_html_ga413367eb7215e5c3e509e3cd039d37b1"></a>
<a id="agroup__fcx__mldx5__interface_html_ga61852fad03f2a92a59a20cdc7bbbdd49"></a>
<a id="agroup__fcx__mldx5__interface_html_gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179"></a>
<a id="agroup__fcx__mldx5__interface_html_gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540"></a>
<a id="agroup__fcx__mldx5__interface_html_gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4"></a>
<a id="agroup__fcx__mldx5__interface_html_gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7"></a>
<a id="agroup__fcx__mldx5__interface_html_gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00"></a>
<a id="agroup__fcx__mldx5__interface_html_gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585"></a>
<a id="agroup__fcx__mldx5__interface_html_gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7"></a>
<a id="agroup__sensor__interface_html_gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2025 Prevas A/S
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_FCX_MLDX5_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_FCX_MLDX5_H_


#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/drivers/sensor.h>

enum sensor_attribute_fcx_mldx5 {
        SENSOR_ATTR_FCX_MLDX5_STATUS = SENSOR_ATTR_PRIV_START,
        SENSOR_ATTR_FCX_MLDX5_RESET,
};

enum fcx_mldx5_status {
        FCX_MLDX5_STATUS_STANDBY = 2,
        FCX_MLDX5_STATUS_RAMP_UP = 3,
        FCX_MLDX5_STATUS_RUN = 4,
        FCX_MLDX5_STATUS_ERROR = 5,
        FCX_MLDX5_STATUS_UNKNOWN,
};

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_FCX_MLDX5_H_ */
```

## 256.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Prevas A/S。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 84 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_FCX_MLDX5_H_`。

## 256.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/fcx__mldx5_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [sensor_attribute_fcx_mldx5](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga61852fad03f2a92a59a20cdc7bbbdd49)
- [SENSOR_ATTR_FCX_MLDX5_STATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49aac5a09e1192a54d29275ba7f3c9d52b7)
- [SENSOR_ATTR_PRIV_START](https://docs.zephyrproject.org/latest/doxygen/html/group__sensor__interface.html#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)
- [SENSOR_ATTR_FCX_MLDX5_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga61852fad03f2a92a59a20cdc7bbbdd49a59ad17024844d8904168256f8f153585)
- [fcx_mldx5_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#ga413367eb7215e5c3e509e3cd039d37b1)
- [FCX_MLDX5_STATUS_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1adb1e1c971bfaaeecc7d376291f021a00)
- [FCX_MLDX5_STATUS_RAMP_UP](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a9e08ae3cedf51bbeaccbd390990a6ad4)
- [FCX_MLDX5_STATUS_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a002a770d06574829304afba178f8a179)
- [FCX_MLDX5_STATUS_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1a94945852b893160875764c9d34915540)
- [FCX_MLDX5_STATUS_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__fcx__mldx5__interface.html#gga413367eb7215e5c3e509e3cd039d37b1aa9ec19b887f79f85bf7d61d824698ca7)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P255_fcntl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P257_fdt.h_源码浏览.md)
