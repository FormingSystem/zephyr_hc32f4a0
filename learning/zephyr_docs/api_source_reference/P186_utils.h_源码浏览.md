---
id: learning.zephyr-docs.api-source-reference.page-186
title: utils.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第186章\_utils.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html)。

## 186.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00033"></a>
<a id="l00043"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00075"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00087"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00119"></a>
<a id="l00129"></a>
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00149"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="foldopen00161"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="foldopen00173"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="foldopen00185"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="foldopen00197"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00205"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_ga0f8cf55569dddb741d7e21bda192c618"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_ga6e06a7f19486f15447cccfc7dcd932e7"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_ga8970f2c9068f2efc3afb04998d0b0d9c"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_ga9c8d709286fe9be34bd5d156bb7ff54b"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_gab2152a9a007d7bd7106567bef08bfee0"></a>
<a id="agroup__math__dsp__basic__conv__to__fixed_html_gaf683e782aab7cd7beea33d5322f6f4d7"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_ga1f3f2c495cc243c66d23431b97c0acdb"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_ga27cf1582b219e1d5522d32081b1faedd"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_ga5b48f9416c2f5305fb5bc17db6e51e37"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_ga7ecfaad745f108899d21d4e508e05cfd"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_gabdca080c25364e463c5ded433b27f9be"></a>
<a id="agroup__math__dsp__basic__conv__to__float_html_gad764039dcc24a76dfc859df54620dd65"></a>
<a id="agroup__math__dsp_html_ga4611b605e45ab401f02cab15c5e38715"></a>
<a id="agroup__math__dsp_html_gab5a8fb21a5b3b983d5f54f31614052ea"></a>
<a id="agroup__math__dsp_html_gac55f3ae81b5bc9053760baacf57e47f4"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="agroup__math__dsp_html_gae541b6f232c305361e9b416fc9eed263"></a>
<a id="ainclude_2zephyr_2dsp_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="aminmax_8h_html"></a>
<a id="aminmax_8h_html_a04e8e3eede9e473bd18f298fddd67b46"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a181807730d4a375f848ba139813ce04f"></a>
<a id="astdint_8h_html_a688eb21a22db27c2b2bd5836943cdcbe"></a>
<a id="astdint_8h_html_aadcf2a81af243df333b31efa6461ab8e"></a>
<a id="astdint_8h_html_aaf7f29f45f1a513b4748a4e5014ddf6a"></a>
<a id="astdint_8h_html_ac58f2c111cc9989c86db2a7dc4fd84ca"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_ad4e9955955b27624963643eac448118a"></a>

```c
/*
 * Copyright (C) 2024 OWL Services LLC. All rights reserved.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DSP_UTILS_H_
#define ZEPHYR_INCLUDE_DSP_UTILS_H_

#include <stdint.h>
#include <zephyr/sys/minmax.h>
#include <zephyr/kernel.h>
#include <zephyr/dsp/types.h>

#ifdef __cplusplus
extern "C" {
#endif



static inline float32_t zdsp_q7_to_f32_shift(q7_t src, uint32_t m)
{
        return (float32_t)((src << m) / (float32_t)(1U << 7));
}

static inline float32_t zdsp_q15_to_f32_shift(q15_t src, uint32_t m)
{
        return (float32_t)((src << m) / (float32_t)(1U << 15));
}

static inline float32_t zdsp_q31_to_f32_shift(q31_t src, uint32_t m)
{
        return (float32_t)(((int64_t)src) << m) / (float32_t)(1U << 31);
}

static inline float64_t zdsp_q7_to_f64_shift(q7_t src, uint32_t m)
{
        return ((float64_t)(src << m)) / (1U << 7);
}

static inline float64_t zdsp_q15_to_f64_shift(q15_t src, uint32_t m)
{
        return ((float64_t)(src << m)) / (1UL << 15);
}

static inline float64_t zdsp_q31_to_f64_shift(q31_t src, uint32_t m)
{
        return (float64_t)(((int64_t)src) << m) / (1ULL << 31);
}



static inline q7_t zdsp_f32_to_q7_shift(float32_t src, uint32_t m)
{
        return (q7_t)clamp((int32_t)(src * (1U << 7)) >> m, INT8_MIN, INT8_MAX);
}

static inline q15_t zdsp_f32_to_q15_shift(float32_t src, uint32_t m)
{
        return (q15_t)clamp((int32_t)(src * (1U << 15)) >> m, INT16_MIN, INT16_MAX);
}

static inline q31_t zdsp_f32_to_q31_shift(float32_t src, uint32_t m)
{
        return (q31_t)clamp((int64_t)(src * (1U << 31)) >> m, INT32_MIN, INT32_MAX);
}

static inline q7_t zdsp_f64_to_q7_shift(float64_t src, uint32_t m)
{
        return (q7_t)clamp((int32_t)(src * (1U << 7)) >> m, INT8_MIN, INT8_MAX);
}

static inline q15_t zdsp_f64_to_q15_shift(float64_t src, uint32_t m)
{
        return (q15_t)clamp((int32_t)(src * (1U << 15)) >> m, INT16_MIN, INT16_MAX);
}

static inline q31_t zdsp_f64_to_q31_shift(float64_t src, uint32_t m)
{
        return (q31_t)clamp((int64_t)(src * (1U << 31)) >> m, INT32_MIN, INT32_MAX);
}



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DSP_UTILS_H_ */
```

## 186.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2024 OWL Services LLC. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 214 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_UTILS_H_`。

## 186.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/dsp_2utils_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/minmax.h](../numeric_reference/P001_最小最大值与限幅宏参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/dsp/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [float32_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#ga4611b605e45ab401f02cab15c5e38715)
- [zdsp_q7_to_f32_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#ga1f3f2c495cc243c66d23431b97c0acdb)
- [q7_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_q15_to_f32_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#ga5b48f9416c2f5305fb5bc17db6e51e37)
- [q15_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gab5a8fb21a5b3b983d5f54f31614052ea)
- [zdsp_q31_to_f32_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#ga7ecfaad745f108899d21d4e508e05cfd)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [float64_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gac55f3ae81b5bc9053760baacf57e47f4)
- [zdsp_q7_to_f64_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#ga27cf1582b219e1d5522d32081b1faedd)
- [zdsp_q15_to_f64_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#gabdca080c25364e463c5ded433b27f9be)
- [zdsp_q31_to_f64_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__float.html#gad764039dcc24a76dfc859df54620dd65)
- [zdsp_f32_to_q7_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#ga9c8d709286fe9be34bd5d156bb7ff54b)
- [clamp](../numeric_reference/P001_最小最大值与限幅宏参考.md#a04e8e3eede9e473bd18f298fddd67b46)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [INT8_MIN](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#aadcf2a81af243df333b31efa6461ab8e)
- [INT8_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#aaf7f29f45f1a513b4748a4e5014ddf6a)
- [zdsp_f32_to_q15_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#ga0f8cf55569dddb741d7e21bda192c618)
- [INT16_MIN](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ad4e9955955b27624963643eac448118a)
- [INT16_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac58f2c111cc9989c86db2a7dc4fd84ca)
- [zdsp_f32_to_q31_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#ga8970f2c9068f2efc3afb04998d0b0d9c)
- [INT32_MIN](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a688eb21a22db27c2b2bd5836943cdcbe)
- [INT32_MAX](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a181807730d4a375f848ba139813ce04f)
- [zdsp_f64_to_q7_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#gaf683e782aab7cd7beea33d5322f6f4d7)
- [zdsp_f64_to_q15_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#gab2152a9a007d7bd7106567bef08bfee0)
- [zdsp_f64_to_q31_shift](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__conv__to__fixed.html#ga6e06a7f19486f15447cccfc7dcd932e7)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [minmax.h](../numeric_reference/P001_最小最大值与限幅宏参考.md)

---

[上一章](P185_ds3231.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P187_dsp.h_源码浏览.md)
