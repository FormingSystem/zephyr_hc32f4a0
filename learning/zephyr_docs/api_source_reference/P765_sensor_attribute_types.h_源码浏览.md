---
id: learning.zephyr-docs.api-source-reference.page-765
title: sensor_attribute_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第765章\_sensor\_attribute\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h.html)。

## 765.1\_原始可见代码（Source Code）

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
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00027"></a>
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
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="ainttypes_8h_html"></a>
<a id="aprint__format_8h_html"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructsensor__three__axis__attribute_html"></a>
<a id="astructsensor__three__axis__attribute_html_a230f8021356406c3225868d43e39be18"></a>
<a id="astructsensor__three__axis__attribute_html_a5c1bd40fb615aa6515c10ff249bae0c2"></a>
<a id="astructsensor__three__axis__attribute_html_a82ee018216949a3132fcdf165e63d2be"></a>
<a id="astructsensor__three__axis__attribute_html_a88cb3f5259b9dde34c5b26daae4ed270"></a>
<a id="astructsensor__three__axis__attribute_html_afee1c9c4fc2b18fb5ae7f6a69af6e2e9"></a>

```c
/*
 * Copyright (c) 2023 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_ATTRIBUTE_TYPES_H
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_ATTRIBUTE_TYPES_H

#include <zephyr/dsp/types.h>
#include <zephyr/dsp/print_format.h>

#include <inttypes.h>

#ifdef __cplusplus
extern "C" {
#endif

struct sensor_three_axis_attribute {
        int8_t shift;
        union {
                struct {
                        q31_t x;
                        q31_t y;
                        q31_t z;
                };
                q31_t values[3];
        };
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_ATTRIBUTE_TYPES_H */
```

## 765.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 43 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_ATTRIBUTE_TYPES_H`。

## 765.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor__attribute__types_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [zephyr/dsp/print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [sensor_three_axis_attribute](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [shift](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a230f8021356406c3225868d43e39be18)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [x](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a82ee018216949a3132fcdf165e63d2be)
- [y](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a5c1bd40fb615aa6515c10ff249bae0c2)
- [z](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#afee1c9c4fc2b18fb5ae7f6a69af6e2e9)
- [values](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a88cb3f5259b9dde34c5b26daae4ed270)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [sensor_three_axis_attribute::shift](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a230f8021356406c3225868d43e39be18)
- [sensor_three_axis_attribute::y](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a5c1bd40fb615aa6515c10ff249bae0c2)
- [sensor_three_axis_attribute::x](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a82ee018216949a3132fcdf165e63d2be)
- [sensor_three_axis_attribute::values](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#a88cb3f5259b9dde34c5b26daae4ed270)
- [sensor_three_axis_attribute::z](../sensor_navigation_model_reference/P049_sensor_three_axis_attribute_结构体.md#afee1c9c4fc2b18fb5ae7f6a69af6e2e9)

---

[上一章](P764_tle9104.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P766_sensor_axis_align.h_源码浏览.md)
