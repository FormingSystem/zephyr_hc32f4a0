---
id: learning.zephyr-docs.api-source-reference.page-758
title: sensing_datatypes.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第758章\_sensing\_datatypes.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html)。

## 758.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00123"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructsensing__sensor__value__3d__q31_html"></a>
<a id="astructsensing__sensor__value__3d__q31_html_a163e62d50de3b5f61688ff9b00db0dcd"></a>
<a id="astructsensing__sensor__value__3d__q31_html_a1bf323a7bb69af0801acebfe03e35b7a"></a>
<a id="astructsensing__sensor__value__3d__q31_html_a68eefb9ba2e8d954e8ea3c4f30893f3f"></a>
<a id="astructsensing__sensor__value__3d__q31_html_a721b9cd33e360691b9fb07a90c3f4df2"></a>
<a id="astructsensing__sensor__value__3d__q31_html_abbf0f5aaae8978eba1e5f3e2ffad20d0"></a>
<a id="astructsensing__sensor__value__3d__q31_html_ad1d2f43d1a9a4b5333ac1b8531d6c94c"></a>
<a id="astructsensing__sensor__value__3d__q31_html_aea782e09d486595b5fbd7a94f3bde253"></a>
<a id="astructsensing__sensor__value__3d__q31_html_af0db9faee6eaabff7f9c2f955873378b"></a>
<a id="astructsensing__sensor__value__header_html"></a>
<a id="astructsensing__sensor__value__header_html_a147989d4c36de1cbd83093a2c5d90950"></a>
<a id="astructsensing__sensor__value__header_html_aa8efbfd682535deca1172cb192c1a86c"></a>
<a id="astructsensing__sensor__value__q31_html"></a>
<a id="astructsensing__sensor__value__q31_html_a555e1bec3fe6f781fd12c13a097d4f16"></a>
<a id="astructsensing__sensor__value__q31_html_a94e301bf8a27dfdb0e5e6c2d6540b83b"></a>
<a id="astructsensing__sensor__value__q31_html_ad3ed83faec34ebce96e57e23aab36101"></a>
<a id="astructsensing__sensor__value__q31_html_af3dbde41e764de34d1b2b38800909da9"></a>
<a id="astructsensing__sensor__value__q31_html_aff3865d5645e7cb53718b4f09b20b162"></a>
<a id="astructsensing__sensor__value__uint32_html"></a>
<a id="astructsensing__sensor__value__uint32_html_a10d8f7d8f36c4969552b297ed34bf592"></a>
<a id="astructsensing__sensor__value__uint32_html_a1fd1c1d018a3793e56e4d0bfded03812"></a>
<a id="astructsensing__sensor__value__uint32_html_adfb3431b5b5e90d29931b9861c9dcd21"></a>
<a id="astructsensing__sensor__value__uint32_html_af30e831ebd860b0dec15733220bdb9df"></a>

```c
/*
 * Copyright (c) 2022-2023 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SENSING_SENSING_DATATYPES_H_
#define ZEPHYR_INCLUDE_SENSING_SENSING_DATATYPES_H_

#include <stdint.h>
#include <zephyr/dsp/types.h>


struct sensing_sensor_value_header {
        uint64_t base_timestamp;
        uint16_t reading_count;
};


struct sensing_sensor_value_3d_q31 {
        struct sensing_sensor_value_header header;
        int8_t shift;
        struct {
                uint32_t timestamp_delta;
                union {
                        q31_t v[3];
                        struct {
                                q31_t x;
                                q31_t y;
                                q31_t z;
                        };
                };
        } readings[1];
};

struct sensing_sensor_value_uint32 {
        struct sensing_sensor_value_header header;
        struct {
                uint32_t timestamp_delta;
                uint32_t v;
        } readings[1];
};

struct sensing_sensor_value_q31 {
        struct sensing_sensor_value_header header;
        int8_t shift;
        struct {
                uint32_t timestamp_delta;
                q31_t v;
        } readings[1];
};


#endif /* ZEPHYR_INCLUDE_SENSING_SENSING_DATATYPES_H_ */
```

## 758.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022-2023 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 142 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SENSING_SENSING_DATATYPES_H_`。

## 758.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensing__datatypes_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [sensing_sensor_value_header](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [base_timestamp](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md#aa8efbfd682535deca1172cb192c1a86c)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [reading_count](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md#a147989d4c36de1cbd83093a2c5d90950)
- [sensing_sensor_value_3d_q31](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md)
- [header](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a163e62d50de3b5f61688ff9b00db0dcd)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [shift](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#af0db9faee6eaabff7f9c2f955873378b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [timestamp_delta](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a1bf323a7bb69af0801acebfe03e35b7a)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [v](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a68eefb9ba2e8d954e8ea3c4f30893f3f)
- [x](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#ad1d2f43d1a9a4b5333ac1b8531d6c94c)
- [y](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a721b9cd33e360691b9fb07a90c3f4df2)
- [z](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#abbf0f5aaae8978eba1e5f3e2ffad20d0)
- [readings](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#aea782e09d486595b5fbd7a94f3bde253)
- [sensing_sensor_value_uint32](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md)
- [header](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#adfb3431b5b5e90d29931b9861c9dcd21)
- [timestamp_delta](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#a1fd1c1d018a3793e56e4d0bfded03812)
- [v](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#a10d8f7d8f36c4969552b297ed34bf592)
- [readings](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#af30e831ebd860b0dec15733220bdb9df)
- [sensing_sensor_value_q31](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md)
- [header](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#af3dbde41e764de34d1b2b38800909da9)
- [shift](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#a555e1bec3fe6f781fd12c13a097d4f16)
- [timestamp_delta](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#aff3865d5645e7cb53718b4f09b20b162)
- [v](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#ad3ed83faec34ebce96e57e23aab36101)
- [readings](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#a94e301bf8a27dfdb0e5e6c2d6540b83b)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [sensing_sensor_value_3d_q31::header](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a163e62d50de3b5f61688ff9b00db0dcd)
- [sensing_sensor_value_3d_q31::timestamp_delta](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a1bf323a7bb69af0801acebfe03e35b7a)
- [sensing_sensor_value_3d_q31::v](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a68eefb9ba2e8d954e8ea3c4f30893f3f)
- [sensing_sensor_value_3d_q31::y](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#a721b9cd33e360691b9fb07a90c3f4df2)
- [sensing_sensor_value_3d_q31::z](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#abbf0f5aaae8978eba1e5f3e2ffad20d0)
- [sensing_sensor_value_3d_q31::x](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#ad1d2f43d1a9a4b5333ac1b8531d6c94c)
- [sensing_sensor_value_3d_q31::readings](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#aea782e09d486595b5fbd7a94f3bde253)
- [sensing_sensor_value_3d_q31::shift](../sensor_navigation_model_reference/P028_sensing_sensor_value_3d_q31_结构体.md#af0db9faee6eaabff7f9c2f955873378b)
- [sensing_sensor_value_header::reading_count](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md#a147989d4c36de1cbd83093a2c5d90950)
- [sensing_sensor_value_header::base_timestamp](../sensor_navigation_model_reference/P029_sensing_sensor_value_header_结构体.md#aa8efbfd682535deca1172cb192c1a86c)
- [sensing_sensor_value_q31::shift](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#a555e1bec3fe6f781fd12c13a097d4f16)
- [sensing_sensor_value_q31::readings](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#a94e301bf8a27dfdb0e5e6c2d6540b83b)
- [sensing_sensor_value_q31::v](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#ad3ed83faec34ebce96e57e23aab36101)
- [sensing_sensor_value_q31::header](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#af3dbde41e764de34d1b2b38800909da9)
- [sensing_sensor_value_q31::timestamp_delta](../sensor_navigation_model_reference/P030_sensing_sensor_value_q31_结构体.md#aff3865d5645e7cb53718b4f09b20b162)
- [sensing_sensor_value_uint32::v](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#a10d8f7d8f36c4969552b297ed34bf592)
- [sensing_sensor_value_uint32::timestamp_delta](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#a1fd1c1d018a3793e56e4d0bfded03812)
- [sensing_sensor_value_uint32::header](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#adfb3431b5b5e90d29931b9861c9dcd21)
- [sensing_sensor_value_uint32::readings](../sensor_navigation_model_reference/P031_sensing_sensor_value_uint32_结构体.md#af30e831ebd860b0dec15733220bdb9df)

---

[上一章](P757_sensing.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P759_sensing_sensor.h_源码浏览.md)
