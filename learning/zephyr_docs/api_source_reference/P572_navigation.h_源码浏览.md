---
id: learning.zephyr-docs.api-source-reference.page-572
title: navigation.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第572章\_navigation.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html)。

## 572.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="agroup__navigation_html_ga36655c6a733ba4e96cc6bfd055a0bf8b"></a>
<a id="agroup__navigation_html_ga99b3460548c6e88cb16391ba77303829"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astructnavigation__data_html"></a>
<a id="astructnavigation__data_html_a02d9f8cea5fe68810123bb2bf554d59c"></a>
<a id="astructnavigation__data_html_a530eb9c4e3750bbb03b26256794d0914"></a>
<a id="astructnavigation__data_html_a5fd501c07c21e66217a7634d7d607d1d"></a>
<a id="astructnavigation__data_html_addd80254be4619c4ea7707f9c9bc434e"></a>
<a id="astructnavigation__data_html_af9887a29823fc3e083dbd14d1f6cfce1"></a>

```c
/*
 * Copyright (c) 2023 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DATA_NAVIGATION_H_
#define ZEPHYR_INCLUDE_DATA_NAVIGATION_H_


#include <zephyr/types.h>


struct navigation_data {
        int64_t latitude;
        int64_t longitude;
        uint32_t bearing;
        uint32_t speed;
        int32_t altitude;
};

int navigation_distance(uint64_t *distance, const struct navigation_data *p1,
                        const struct navigation_data *p2);

int navigation_bearing(uint32_t *bearing, const struct navigation_data *from,
                       const struct navigation_data *to);


#endif /* ZEPHYR_INCLUDE_DATA_NAVIGATION_H_ */
```

## 572.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DATA_NAVIGATION_H_`。

## 572.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/navigation_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [navigation_data](../sensor_navigation_model_reference/P018_navigation_data_结构体.md)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [latitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a02d9f8cea5fe68810123bb2bf554d59c)
- [longitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a530eb9c4e3750bbb03b26256794d0914)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bearing](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#af9887a29823fc3e083dbd14d1f6cfce1)
- [speed](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a5fd501c07c21e66217a7634d7d607d1d)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [altitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#addd80254be4619c4ea7707f9c9bc434e)
- [navigation_distance](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga99b3460548c6e88cb16391ba77303829)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [navigation_bearing](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html#ga36655c6a733ba4e96cc6bfd055a0bf8b)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [navigation_data::latitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a02d9f8cea5fe68810123bb2bf554d59c)
- [navigation_data::longitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a530eb9c4e3750bbb03b26256794d0914)
- [navigation_data::speed](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#a5fd501c07c21e66217a7634d7d607d1d)
- [navigation_data::altitude](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#addd80254be4619c4ea7707f9c9bc434e)
- [navigation_data::bearing](../sensor_navigation_model_reference/P018_navigation_data_结构体.md#af9887a29823fc3e083dbd14d1f6cfce1)

---

[上一章](P571_mt8188-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P573_nct38xx.h_源码浏览.md)
