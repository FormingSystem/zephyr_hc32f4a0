---
id: learning.zephyr-docs.api-source-architecture-reference.page-8
title: ft8xx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_ft8xx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h.html)。

## 8.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00029"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__ft8xx__interface_html_ga1c9ade4374b9619c68efa11dd1a56eae"></a>
<a id="agroup__ft8xx__interface_html_ga1d74a13782c6ab9f8b07a28503058356"></a>
<a id="agroup__ft8xx__interface_html_ga586f6ff1eddd5b596d2e35fb5fdd8148"></a>
<a id="agroup__ft8xx__interface_html_ga846a90d72b56f388d5b4f60cf6d658b0"></a>
<a id="agroup__ft8xx__interface_html_gaea3589b5a0aa34a09a81ea15c1595219"></a>
<a id="agroup__ft8xx__interface_html_gaf392199312ddb82451a4f31e2955079d"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructft8xx__touch__transform_html"></a>
<a id="astructft8xx__touch__transform_html_a307e6438e32a36ac78c76979925e5e1c"></a>
<a id="astructft8xx__touch__transform_html_a8c31db728937a0b69f01b9c3e265287a"></a>
<a id="astructft8xx__touch__transform_html_aa72829a35d054aa88fc8fd494e5eecbe"></a>
<a id="astructft8xx__touch__transform_html_ab86ed8962e01945c63751912c622b623"></a>
<a id="astructft8xx__touch__transform_html_aebc5352e00847e41b2d239a9265b5e45"></a>
<a id="astructft8xx__touch__transform_html_aeee5e2153eca64f1c5a6196d910c3d3e"></a>

```c
/*
 * Copyright (c) 2020 Hubert Miś
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_H_
#define ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_H_

#include <stdint.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif


struct ft8xx_touch_transform {
        uint32_t a; /*< Coefficient A of the bitmap transform matrix */
        uint32_t b; /*< Coefficient B of the bitmap transform matrix */
        uint32_t c; /*< Coefficient C of the bitmap transform matrix */
        uint32_t d; /*< Coefficient D of the bitmap transform matrix */
        uint32_t e; /*< Coefficient E of the bitmap transform matrix */
        uint32_t f; /*< Coefficient F of the bitmap transform matrix */
};

typedef void (*ft8xx_int_callback)(const struct device *dev, void *user_data);

void ft8xx_calibrate(const struct device *dev,
                     struct ft8xx_touch_transform *data);

void ft8xx_touch_transform_set(const struct device *dev,
                               const struct ft8xx_touch_transform *data);

int ft8xx_get_touch_tag(const struct device *dev);

uint32_t ft8xx_get_tracker_value(const struct device *dev);

void ft8xx_register_int(const struct device *dev,
                        ft8xx_int_callback callback,
                        void *user_data);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Hubert Miś。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

位图变换矩阵（Bitmap Transform Matrix）的系数 A（Coefficient A）。

### 注释 3：原第 38 行

位图变换矩阵（Bitmap Transform Matrix）的系数 B（Coefficient B）。

### 注释 4：原第 39 行

位图变换矩阵（Bitmap Transform Matrix）的系数 C（Coefficient C）。

### 注释 5：原第 40 行

位图变换矩阵（Bitmap Transform Matrix）的系数 D（Coefficient D）。

### 注释 6：原第 41 行

位图变换矩阵（Bitmap Transform Matrix）的系数 E（Coefficient E）。

### 注释 7：原第 42 行

位图变换矩阵（Bitmap Transform Matrix）的系数 F（Coefficient F）。

### 注释 8：原第 133 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_MISC_FT8XX_FT8XX_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [ft8xx_touch_transform](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [a](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aebc5352e00847e41b2d239a9265b5e45)
- [b](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#a307e6438e32a36ac78c76979925e5e1c)
- [c](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#ab86ed8962e01945c63751912c622b623)
- [d](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aeee5e2153eca64f1c5a6196d910c3d3e)
- [e](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#a8c31db728937a0b69f01b9c3e265287a)
- [f](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aa72829a35d054aa88fc8fd494e5eecbe)
- [ft8xx_int_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga846a90d72b56f388d5b4f60cf6d658b0)
- [device](../device_reference/P002_设备对象结构.md)
- [ft8xx_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga586f6ff1eddd5b596d2e35fb5fdd8148)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ft8xx_touch_transform_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1d74a13782c6ab9f8b07a28503058356)
- [ft8xx_get_touch_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaea3589b5a0aa34a09a81ea15c1595219)
- [ft8xx_get_tracker_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#ga1c9ade4374b9619c68efa11dd1a56eae)
- [ft8xx_register_int](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__interface.html#gaf392199312ddb82451a4f31e2955079d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ft8xx_touch_transform::b](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#a307e6438e32a36ac78c76979925e5e1c)
- [ft8xx_touch_transform::e](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#a8c31db728937a0b69f01b9c3e265287a)
- [ft8xx_touch_transform::f](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aa72829a35d054aa88fc8fd494e5eecbe)
- [ft8xx_touch_transform::c](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#ab86ed8962e01945c63751912c622b623)
- [ft8xx_touch_transform::a](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aebc5352e00847e41b2d239a9265b5e45)
- [ft8xx_touch_transform::d](../sensor_navigation_model_reference/P008_ft8xx_touch_transform_结构体.md#aeee5e2153eca64f1c5a6196d910c3d3e)

---

[上一章](P007_fdtable.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_grove_lcd.h_源码浏览.md)
