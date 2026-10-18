---
id: learning.zephyr-docs.api-source-runtime-reference.page-3
title: bmp581_user.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_bmp581\_user.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
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
<a id="l00046"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="abmp581_8h_html"></a>
<a id="agroup__bmp581__interface_html_gaca06546e057d7295ca4f6ed4298247dc"></a>
<a id="agroup__bmp581__interface_html_ggaca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57"></a>
<a id="agroup__bmp581__interface_html_ggaca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1"></a>
<a id="agroup__bmp581__interface_html_ggaca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f"></a>
<a id="agroup__bmp581__interface_html_ggaca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c"></a>
<a id="agroup__bmp581__interface_html_ggaca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96"></a>
<a id="asensor_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Badgerd Technologies B.V.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Driver is developed to be used with Zephyr. And it only supports i2c interface.
 *
 * Author: Talha Can Havadar <havadartalha@gmail.com>
 *
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_BMP581_USER_H_
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_BMP581_USER_H_


#include <zephyr/drivers/sensor.h>
#include <zephyr/dt-bindings/sensor/bmp581.h>

/* Custom ATTR values */

/* This is used to enable IIR config,
 * keep in mind that disabling IIR back in runtime is not
 * supported yet
 */

#define BMP5_ATTR_IIR_CONFIG (SENSOR_ATTR_PRIV_START + 1u)
#define BMP5_ATTR_POWER_MODE (SENSOR_ATTR_PRIV_START + 2u)

enum bmp5_powermode {
        BMP5_POWERMODE_STANDBY,
        BMP5_POWERMODE_NORMAL,
        BMP5_POWERMODE_FORCED,
        BMP5_POWERMODE_CONTINUOUS,
        BMP5_POWERMODE_DEEP_STANDBY
};


#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_BMP581_USER_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Badgerd Technologies B.V.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

此驱动为 Zephyr 开发，仅支持 I2C 接口。

作者（Author）：Talha Can Havadar <havadartalha@gmail.com>。

### 注释 2：原第 31 行

自定义属性（ATTR）值。

### 注释 3：原第 33 行

用于启用无限脉冲响应（IIR）滤波配置。请注意，目前还不支持在运行时重新禁用 IIR。

### 注释 4：原第 74 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_BMP581_USER_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/bmp581__user_8h.html)
- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)
- [zephyr/dt-bindings/sensor/bmp581.h](https://docs.zephyrproject.org/latest/doxygen/html/bmp581_8h.html)
- [bmp5_powermode](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#gaca06546e057d7295ca4f6ed4298247dc)
- [BMP5_POWERMODE_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca8f50ab92ba9607eaeed772ddbe92a15f)
- [BMP5_POWERMODE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcabb75d9c71965843c27724d956ffd1f8c)
- [BMP5_POWERMODE_FORCED](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dcaf57d41b2953f1986618de43ac1315b96)
- [BMP5_POWERMODE_CONTINUOUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca14a304e989e6c079c9b6d668b4fd3e57)
- [BMP5_POWERMODE_DEEP_STANDBY](https://docs.zephyrproject.org/latest/doxygen/html/group__bmp581__interface.html#ggaca06546e057d7295ca4f6ed4298247dca3904b0e3e14b2cad554436ba96fe4bf1)
- [bmp581.h](https://docs.zephyrproject.org/latest/doxygen/html/bmp581_8h.html)
- [sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h.html)

---

[上一章](P002_blob_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_cc23x0-pinctrl.h_源码浏览.md)
