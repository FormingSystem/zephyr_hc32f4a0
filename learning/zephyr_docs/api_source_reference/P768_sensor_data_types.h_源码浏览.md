---
id: learning.zephyr-docs.api-source-reference.page-768
title: sensor_data_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第768章\_sensor\_data\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h.html)。

## 768.1\_原始可见代码（Source Code）

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
<a id="l00018"></a>
<a id="foldopen00019"></a>
<a id="l00019"></a>
<a id="l00024"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00045"></a>
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
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00061"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="foldopen00089"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00102"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00117"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="foldopen00120"></a>
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
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00145"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00153"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="foldopen00155"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="foldopen00169"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="foldopen00177"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00187"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="ainttypes_8h_html"></a>
<a id="aprint__format_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructsensor__byte__data_1_1sensor__byte__sample__data_html"></a>
<a id="astructsensor__byte__data_1_1sensor__byte__sample__data_html_a3ad640ff448fe87d2eda7c5118404b7a"></a>
<a id="astructsensor__byte__data_1_1sensor__byte__sample__data_html_ab07c2a7ce6e47c61249606a88aeda2bd"></a>
<a id="astructsensor__byte__data_1_1sensor__byte__sample__data_html_ab29a911990794b35bde3114e813d2c9a"></a>
<a id="astructsensor__byte__data_1_1sensor__byte__sample__data_html_acd42cfa0dc446378cebf998c1b795963"></a>
<a id="astructsensor__byte__data_html"></a>
<a id="astructsensor__byte__data_html_ab18ad72251bae040fc4752bc125be3ba"></a>
<a id="astructsensor__byte__data_html_ad4ac07ed10938265e89a43133c41af24"></a>
<a id="astructsensor__data__header_html"></a>
<a id="astructsensor__data__header_html_a1db93386466e8e4778f448ae0d8ca556"></a>
<a id="astructsensor__data__header_html_ad31873d402a02842eb3098431591c151"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_a3ff5782e8544602eb858e034a67667b6"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_a44471cf8b4de7faa0f4abf94e9fbb36e"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_a7e34b93a4d3393b0c7c5918e6f6acb93"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_a8631568f550497620734f27f2a96553d"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_acb44311f2b7bc97dae7b26a8256905cf"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_ad5fcab0aaca689606cbfacb7f6b13887"></a>
<a id="astructsensor__game__rotation__vector__data_1_1sensor__game__rotation__vector__sample__data_html_af453e301f5d1fdacf86daddc0c683498"></a>
<a id="astructsensor__game__rotation__vector__data_html"></a>
<a id="astructsensor__game__rotation__vector__data_html_a22817d2c2b6b9e04ab574eb816df5442"></a>
<a id="astructsensor__game__rotation__vector__data_html_abb709edf89ac7dc720a5f307cd1a48bb"></a>
<a id="astructsensor__game__rotation__vector__data_html_acc17463dbd99f1ce4fc6a0c42a6bf0c2"></a>
<a id="astructsensor__occurrence__data_1_1sensor__occurrence__sample__data_html"></a>
<a id="astructsensor__occurrence__data_1_1sensor__occurrence__sample__data_html_a19fb2f7d23a2d58e0bf7f2009f8aba59"></a>
<a id="astructsensor__occurrence__data_html"></a>
<a id="astructsensor__occurrence__data_html_a06e7c6b24166e1c85d05286d44f60768"></a>
<a id="astructsensor__occurrence__data_html_a181279d03759db87e3855d46d30c5aaf"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a1493dc66c9d6e4782aed2ddadd74e178"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a215aab449c2b5ee8cf32d971aa5e7708"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a2ed468c4be6417f0ea2bb324560e622d"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a39f4f4bf64dd49ff2fe027f6e8f8a04d"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a428adc52033ba50b871c8986e55b06af"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a60f0af8beb207f90ed916fe445525fed"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a7ae2d145a778a72322a78ed433781a0d"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a8101423f27270dcee7a356cabcc4d9dd"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_a9e58a7ea902e27b02b34cc8f619aca96"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_aafb3c0aa55c129b310525f7181b59d51"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_ac0d247952ae488af354fa1462a014d1d"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_ad5d6a48016d474635c0f8a829915a8d2"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_ae07081204f6c01334ea9f2e970879b72"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_aeb66bf289c9e17ac6473eb69c22d4eb3"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_af63a2f7a618c8ff17be31a0543920525"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_afd73a2b1b6e4e262e89e242853f4ef23"></a>
<a id="astructsensor__q31__data_1_1sensor__q31__sample__data_html_afdf41c27c4f3f55c3ed18c73ab8b6183"></a>
<a id="astructsensor__q31__data_html"></a>
<a id="astructsensor__q31__data_html_a23fc75fd1dafe2789a7d0bff116cb681"></a>
<a id="astructsensor__q31__data_html_a41f8315cbe740bdc7aec6bd30ce0e096"></a>
<a id="astructsensor__q31__data_html_a9dcc5ffe1d31c37eef75b4132c5f94fd"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_a5ef91a336b07c2c3e79ed34afbbf8850"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_a60a8b323508fb4ececd4c3bdad770525"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_a62dd4febada1d6b0b0fad600747089a2"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_aa0de6e1354c259857b2b5a89717a5f9a"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_aa8a07324f3139a6a34f695927a1d6486"></a>
<a id="astructsensor__three__axis__data_1_1sensor__three__axis__sample__data_html_ac78d9fa7e085025f1ccc9f53bf30f3bb"></a>
<a id="astructsensor__three__axis__data_html"></a>
<a id="astructsensor__three__axis__data_html_a6017fc7964204235e2222c4950f3650a"></a>
<a id="astructsensor__three__axis__data_html_ad1a498b1cc31b18b17e69300749bbbc0"></a>
<a id="astructsensor__three__axis__data_html_ade10fa0bd60d4b31eebed92e564539c5"></a>
<a id="astructsensor__uint64__data_1_1sensor__uint64__sample__data_html"></a>
<a id="astructsensor__uint64__data_1_1sensor__uint64__sample__data_html_a37b7eb52969798316f23102dfc66f343"></a>
<a id="astructsensor__uint64__data_1_1sensor__uint64__sample__data_html_af0274c154cbc342161b46cb6c3ca0984"></a>
<a id="astructsensor__uint64__data_html"></a>
<a id="astructsensor__uint64__data_html_a61e2d0796ba3c0e95a0455e03ce01d76"></a>
<a id="astructsensor__uint64__data_html_a86a1b96bd7a3aeb6b615e6ab0c3a96a6"></a>

```c
/*
 * Copyright (c) 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_SENSOR_DATA_TYPES_H
#define ZEPHYR_INCLUDE_DRIVERS_SENSOR_DATA_TYPES_H

#include <zephyr/dsp/types.h>
#include <zephyr/dsp/print_format.h>

#include <inttypes.h>

#ifdef __cplusplus
extern "C" {
#endif

struct sensor_data_header {
        uint64_t base_timestamp_ns;
        uint16_t reading_count;
};

struct sensor_three_axis_data {
        struct sensor_data_header header;
        int8_t shift;
        struct sensor_three_axis_sample_data {
                uint32_t timestamp_delta;
                union {
                        q31_t values[3];
                        q31_t v[3];
                        struct {
                                q31_t x;
                                q31_t y;
                                q31_t z;
                        };
                };
        } readings[1];
};

#define PRIsensor_three_axis_data PRIu64 "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6) ")"

#define PRIsensor_three_axis_data_arg(data_, readings_offset_)                                     \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
                PRIq_arg((data_).readings[(readings_offset_)].x, 6, (data_).shift),                \
                PRIq_arg((data_).readings[(readings_offset_)].y, 6, (data_).shift),                \
                PRIq_arg((data_).readings[(readings_offset_)].z, 6, (data_).shift)

struct sensor_game_rotation_vector_data {
        struct sensor_data_header header;
        int8_t shift;
        struct sensor_game_rotation_vector_sample_data {
                uint32_t timestamp_delta;
                union {
                        q31_t values[4];
                        q31_t v[4];
                        struct {
                                q31_t x;
                                q31_t y;
                                q31_t z;
                                q31_t w;
                        };
                };
        } readings[1];
};

#define PRIsensor_game_rotation_vector_data PRIu64                                                 \
        "ns, (%" PRIq(6) ", %" PRIq(6) ", %" PRIq(6)  ", %" PRIq(6) ")"

#define PRIsensor_game_rotation_vector_data_arg(data_, readings_offset_)                           \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
                PRIq_arg((data_).readings[(readings_offset_)].x, 6, (data_).shift),                \
                PRIq_arg((data_).readings[(readings_offset_)].y, 6, (data_).shift),                \
                PRIq_arg((data_).readings[(readings_offset_)].z, 6, (data_).shift),                \
                PRIq_arg((data_).readings[(readings_offset_)].w, 6, (data_).shift)

struct sensor_occurrence_data {
        struct sensor_data_header header;
        struct sensor_occurrence_sample_data {
                uint32_t timestamp_delta;
        } readings[1];
};

#define PRIsensor_occurrence_data PRIu64 "ns"

#define PRIsensor_occurrence_data_arg(data_, readings_offset_)                                     \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta

struct sensor_q31_data {
        struct sensor_data_header header;
        int8_t shift;
        struct sensor_q31_sample_data {
                uint32_t timestamp_delta;
                union {
                        q31_t value;
                        q31_t light;
                        q31_t pressure;
                        q31_t temperature;
                        q31_t percent;
                        q31_t distance;
                        q31_t density;
                        q31_t density_ppm;
                        q31_t density_ppb;
                        q31_t resistance;
                        q31_t voltage;
                        q31_t current;
                        q31_t power;
                        q31_t angle;
                        q31_t electric_charge;
                        q31_t humidity;
                };
        } readings[1];
};

#define PRIsensor_q31_data PRIu64 "ns (%" PRIq(6) ")"

#define PRIsensor_q31_data_arg(data_, readings_offset_)                                            \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
                PRIq_arg((data_).readings[(readings_offset_)].value, 6, (data_).shift)

struct sensor_byte_data {
        struct sensor_data_header header;
        struct sensor_byte_sample_data {
                uint32_t timestamp_delta;
                union {
                        uint8_t value;
                        struct {
                                uint8_t is_near: 1;
                                uint8_t padding: 7;
                        };
                };
        } readings[1];
};

#define PRIsensor_byte_data(field_name_) PRIu64 "ns (" STRINGIFY(field_name_) " = %" PRIu8 ")"

#define PRIsensor_byte_data_arg(data_, readings_offset_, field_name_)                              \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
                (data_).readings[(readings_offset_)].field_name_

struct sensor_uint64_data {
        struct sensor_data_header header;
        struct sensor_uint64_sample_data {
                uint32_t timestamp_delta;
                uint64_t value;
        } readings[1];
};

#define PRIsensor_uint64_data PRIu64 "ns (%" PRIu64 ")"

#define PRIsensor_uint64_data_arg(data_, readings_offset_)                                         \
        (data_).header.base_timestamp_ns + (data_).readings[(readings_offset_)].timestamp_delta,   \
                (data_).readings[(readings_offset_)].value

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_SENSOR_DATA_TYPES_H */
```

## 768.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 195 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_SENSOR_DATA_TYPES_H`。

## 768.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/sensor__data__types_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [zephyr/dsp/print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [sensor_data_header](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [base_timestamp_ns](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md#a1db93386466e8e4778f448ae0d8ca556)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [reading_count](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md#ad31873d402a02842eb3098431591c151)
- [sensor_three_axis_data](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md)
- [header](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#a6017fc7964204235e2222c4950f3650a)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [shift](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#ade10fa0bd60d4b31eebed92e564539c5)
- [sensor_three_axis_sample_data](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [timestamp_delta](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a62dd4febada1d6b0b0fad600747089a2)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [values](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#aa8a07324f3139a6a34f695927a1d6486)
- [v](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#aa0de6e1354c259857b2b5a89717a5f9a)
- [x](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a60a8b323508fb4ececd4c3bdad770525)
- [y](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#ac78d9fa7e085025f1ccc9f53bf30f3bb)
- [z](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a5ef91a336b07c2c3e79ed34afbbf8850)
- [readings](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#ad1a498b1cc31b18b17e69300749bbbc0)
- [sensor_game_rotation_vector_data](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md)
- [header](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#abb709edf89ac7dc720a5f307cd1a48bb)
- [shift](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#a22817d2c2b6b9e04ab574eb816df5442)
- [sensor_game_rotation_vector_sample_data](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)
- [timestamp_delta](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#af453e301f5d1fdacf86daddc0c683498)
- [values](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a7e34b93a4d3393b0c7c5918e6f6acb93)
- [v](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a44471cf8b4de7faa0f4abf94e9fbb36e)
- [x](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a3ff5782e8544602eb858e034a67667b6)
- [y](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a8631568f550497620734f27f2a96553d)
- [z](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#acb44311f2b7bc97dae7b26a8256905cf)
- [w](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#ad5fcab0aaca689606cbfacb7f6b13887)
- [readings](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#acc17463dbd99f1ce4fc6a0c42a6bf0c2)
- [sensor_occurrence_data](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md)
- [header](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md#a06e7c6b24166e1c85d05286d44f60768)
- [sensor_occurrence_sample_data](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)
- [timestamp_delta](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md#a19fb2f7d23a2d58e0bf7f2009f8aba59)
- [readings](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md#a181279d03759db87e3855d46d30c5aaf)
- [sensor_q31_data](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md)
- [header](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a9dcc5ffe1d31c37eef75b4132c5f94fd)
- [shift](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a41f8315cbe740bdc7aec6bd30ce0e096)
- [sensor_q31_sample_data](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)
- [timestamp_delta](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#afdf41c27c4f3f55c3ed18c73ab8b6183)
- [value](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#afd73a2b1b6e4e262e89e242853f4ef23)
- [light](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a7ae2d145a778a72322a78ed433781a0d)
- [pressure](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ae07081204f6c01334ea9f2e970879b72)
- [temperature](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a8101423f27270dcee7a356cabcc4d9dd)
- [percent](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d)
- [distance](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ad5d6a48016d474635c0f8a829915a8d2)
- [density](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a2ed468c4be6417f0ea2bb324560e622d)
- [density_ppm](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a1493dc66c9d6e4782aed2ddadd74e178)
- [density_ppb](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a215aab449c2b5ee8cf32d971aa5e7708)
- [resistance](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#aeb66bf289c9e17ac6473eb69c22d4eb3)
- [voltage](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#af63a2f7a618c8ff17be31a0543920525)
- [current](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a60f0af8beb207f90ed916fe445525fed)
- [power](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a428adc52033ba50b871c8986e55b06af)
- [angle](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a9e58a7ea902e27b02b34cc8f619aca96)
- [electric_charge](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#aafb3c0aa55c129b310525f7181b59d51)
- [humidity](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ac0d247952ae488af354fa1462a014d1d)
- [readings](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a23fc75fd1dafe2789a7d0bff116cb681)
- [sensor_byte_data](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md)
- [header](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md#ab18ad72251bae040fc4752bc125be3ba)
- [sensor_byte_sample_data](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)
- [timestamp_delta](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#ab29a911990794b35bde3114e813d2c9a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [value](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#a3ad640ff448fe87d2eda7c5118404b7a)
- [is_near](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#acd42cfa0dc446378cebf998c1b795963)
- [padding](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#ab07c2a7ce6e47c61249606a88aeda2bd)
- [readings](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md#ad4ac07ed10938265e89a43133c41af24)
- [sensor_uint64_data](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md)
- [header](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md#a61e2d0796ba3c0e95a0455e03ce01d76)
- [sensor_uint64_sample_data](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)
- [timestamp_delta](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md#af0274c154cbc342161b46cb6c3ca0984)
- [value](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md#a37b7eb52969798316f23102dfc66f343)
- [readings](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [print_format.h](https://docs.zephyrproject.org/latest/doxygen/html/print__format_8h.html)
- [sensor_byte_data::sensor_byte_sample_data](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md)
- [sensor_byte_data::sensor_byte_sample_data::value](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#a3ad640ff448fe87d2eda7c5118404b7a)
- [sensor_byte_data::sensor_byte_sample_data::padding](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#ab07c2a7ce6e47c61249606a88aeda2bd)
- [sensor_byte_data::sensor_byte_sample_data::timestamp_delta](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#ab29a911990794b35bde3114e813d2c9a)
- [sensor_byte_data::sensor_byte_sample_data::is_near](../sensor_navigation_model_reference/P034_sensor_byte_data__sensor_byte_sample_data_结构体.md#acd42cfa0dc446378cebf998c1b795963)
- [sensor_byte_data::header](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md#ab18ad72251bae040fc4752bc125be3ba)
- [sensor_byte_data::readings](../sensor_navigation_model_reference/P033_sensor_byte_data_结构体.md#ad4ac07ed10938265e89a43133c41af24)
- [sensor_data_header::base_timestamp_ns](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md#a1db93386466e8e4778f448ae0d8ca556)
- [sensor_data_header::reading_count](../sensor_navigation_model_reference/P037_sensor_data_header_结构体.md#ad31873d402a02842eb3098431591c151)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::x](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a3ff5782e8544602eb858e034a67667b6)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::v](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a44471cf8b4de7faa0f4abf94e9fbb36e)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::values](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a7e34b93a4d3393b0c7c5918e6f6acb93)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::y](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#a8631568f550497620734f27f2a96553d)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::z](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#acb44311f2b7bc97dae7b26a8256905cf)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::w](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#ad5fcab0aaca689606cbfacb7f6b13887)
- [sensor_game_rotation_vector_data::sensor_game_rotation_vector_sample_data::timestamp_delta](../sensor_navigation_model_reference/P042_sensor_game_rotation_vector_data__sensor_game_rotation_vector_sample_data_结构体.md#af453e301f5d1fdacf86daddc0c683498)
- [sensor_game_rotation_vector_data::shift](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#a22817d2c2b6b9e04ab574eb816df5442)
- [sensor_game_rotation_vector_data::header](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#abb709edf89ac7dc720a5f307cd1a48bb)
- [sensor_game_rotation_vector_data::readings](../sensor_navigation_model_reference/P041_sensor_game_rotation_vector_data_结构体.md#acc17463dbd99f1ce4fc6a0c42a6bf0c2)
- [sensor_occurrence_data::sensor_occurrence_sample_data](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md)
- [sensor_occurrence_data::sensor_occurrence_sample_data::timestamp_delta](../sensor_navigation_model_reference/P044_sensor_occurrence_data__sensor_occurrence_sample_data_结构体.md#a19fb2f7d23a2d58e0bf7f2009f8aba59)
- [sensor_occurrence_data::header](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md#a06e7c6b24166e1c85d05286d44f60768)
- [sensor_occurrence_data::readings](../sensor_navigation_model_reference/P043_sensor_occurrence_data_结构体.md#a181279d03759db87e3855d46d30c5aaf)
- [sensor_q31_data::sensor_q31_sample_data](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md)
- [sensor_q31_data::sensor_q31_sample_data::density_ppm](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a1493dc66c9d6e4782aed2ddadd74e178)
- [sensor_q31_data::sensor_q31_sample_data::density_ppb](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a215aab449c2b5ee8cf32d971aa5e7708)
- [sensor_q31_data::sensor_q31_sample_data::density](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a2ed468c4be6417f0ea2bb324560e622d)
- [sensor_q31_data::sensor_q31_sample_data::percent](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a39f4f4bf64dd49ff2fe027f6e8f8a04d)
- [sensor_q31_data::sensor_q31_sample_data::power](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a428adc52033ba50b871c8986e55b06af)
- [sensor_q31_data::sensor_q31_sample_data::current](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a60f0af8beb207f90ed916fe445525fed)
- [sensor_q31_data::sensor_q31_sample_data::light](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a7ae2d145a778a72322a78ed433781a0d)
- [sensor_q31_data::sensor_q31_sample_data::temperature](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a8101423f27270dcee7a356cabcc4d9dd)
- [sensor_q31_data::sensor_q31_sample_data::angle](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#a9e58a7ea902e27b02b34cc8f619aca96)
- [sensor_q31_data::sensor_q31_sample_data::electric_charge](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#aafb3c0aa55c129b310525f7181b59d51)
- [sensor_q31_data::sensor_q31_sample_data::humidity](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ac0d247952ae488af354fa1462a014d1d)
- [sensor_q31_data::sensor_q31_sample_data::distance](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ad5d6a48016d474635c0f8a829915a8d2)
- [sensor_q31_data::sensor_q31_sample_data::pressure](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#ae07081204f6c01334ea9f2e970879b72)
- [sensor_q31_data::sensor_q31_sample_data::resistance](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#aeb66bf289c9e17ac6473eb69c22d4eb3)
- [sensor_q31_data::sensor_q31_sample_data::voltage](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#af63a2f7a618c8ff17be31a0543920525)
- [sensor_q31_data::sensor_q31_sample_data::value](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#afd73a2b1b6e4e262e89e242853f4ef23)
- [sensor_q31_data::sensor_q31_sample_data::timestamp_delta](../sensor_navigation_model_reference/P046_sensor_q31_data__sensor_q31_sample_data_结构体.md#afdf41c27c4f3f55c3ed18c73ab8b6183)
- [sensor_q31_data::readings](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a23fc75fd1dafe2789a7d0bff116cb681)
- [sensor_q31_data::shift](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a41f8315cbe740bdc7aec6bd30ce0e096)
- [sensor_q31_data::header](../sensor_navigation_model_reference/P045_sensor_q31_data_结构体.md#a9dcc5ffe1d31c37eef75b4132c5f94fd)
- [sensor_three_axis_data::sensor_three_axis_sample_data](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md)
- [sensor_three_axis_data::sensor_three_axis_sample_data::z](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a5ef91a336b07c2c3e79ed34afbbf8850)
- [sensor_three_axis_data::sensor_three_axis_sample_data::x](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a60a8b323508fb4ececd4c3bdad770525)
- [sensor_three_axis_data::sensor_three_axis_sample_data::timestamp_delta](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#a62dd4febada1d6b0b0fad600747089a2)
- [sensor_three_axis_data::sensor_three_axis_sample_data::v](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#aa0de6e1354c259857b2b5a89717a5f9a)
- [sensor_three_axis_data::sensor_three_axis_sample_data::values](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#aa8a07324f3139a6a34f695927a1d6486)
- [sensor_three_axis_data::sensor_three_axis_sample_data::y](../sensor_navigation_model_reference/P051_sensor_three_axis_data__sensor_three_axis_sample_data_结构体.md#ac78d9fa7e085025f1ccc9f53bf30f3bb)
- [sensor_three_axis_data::header](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#a6017fc7964204235e2222c4950f3650a)
- [sensor_three_axis_data::readings](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#ad1a498b1cc31b18b17e69300749bbbc0)
- [sensor_three_axis_data::shift](../sensor_navigation_model_reference/P050_sensor_three_axis_data_结构体.md#ade10fa0bd60d4b31eebed92e564539c5)
- [sensor_uint64_data::sensor_uint64_sample_data](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md)
- [sensor_uint64_data::sensor_uint64_sample_data::value](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md#a37b7eb52969798316f23102dfc66f343)
- [sensor_uint64_data::sensor_uint64_sample_data::timestamp_delta](../sensor_navigation_model_reference/P054_sensor_uint64_data__sensor_uint64_sample_data_结构体.md#af0274c154cbc342161b46cb6c3ca0984)
- [sensor_uint64_data::header](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md#a61e2d0796ba3c0e95a0455e03ce01d76)
- [sensor_uint64_data::readings](../sensor_navigation_model_reference/P053_sensor_uint64_data_结构体.md#a86a1b96bd7a3aeb6b615e6ab0c3a96a6)

---

[上一章](P767_sensor_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P769_uart_emul.h_源码浏览.md)
