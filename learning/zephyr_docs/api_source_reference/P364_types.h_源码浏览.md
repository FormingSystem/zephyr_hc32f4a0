---
id: learning.zephyr-docs.api-source-reference.page-364
title: types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第364章\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)。

## 364.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="agroup__math__dsp_html_ga4611b605e45ab401f02cab15c5e38715"></a>
<a id="agroup__math__dsp_html_ga5aea1cb12fc02d9d44c8abf217eaa5c6"></a>
<a id="agroup__math__dsp_html_gaa94dc44bddb5718a22bb612890a7fe9f"></a>
<a id="agroup__math__dsp_html_gab5a8fb21a5b3b983d5f54f31614052ea"></a>
<a id="agroup__math__dsp_html_gac55f3ae81b5bc9053760baacf57e47f4"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="agroup__math__dsp_html_gae541b6f232c305361e9b416fc9eed263"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>

```c
/* Copyright (c) 2022 Google LLC
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DSP_TYPES_H_
#define ZEPHYR_INCLUDE_DSP_TYPES_H_

#include <stdint.h>


#ifdef __cplusplus
extern "C" {
#endif

typedef int8_t q7_t;

typedef int16_t q15_t;

typedef int32_t q31_t;

typedef int64_t q63_t;

#if defined(CONFIG_FP16)
typedef __fp16 float16_t;
#endif /* CONFIG_FP16 */

typedef float float32_t;

typedef double float64_t;

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DSP_TYPES_H_ */
```

## 364.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 49 行

条件编译配置（Configuration）标记：`CONFIG_FP16`。

### 注释 3：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_TYPES_H_`。

## 364.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2dsp_2types_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [q7_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gae541b6f232c305361e9b416fc9eed263)
- [int16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#afe270aee8d96ad7f279a4020b9d58bdf)
- [q15_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gab5a8fb21a5b3b983d5f54f31614052ea)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [int64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#ac714c0d2c1a4adb10e73cab29623314b)
- [q63_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#ga5aea1cb12fc02d9d44c8abf217eaa5c6)
- [float16_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gaa94dc44bddb5718a22bb612890a7fe9f)
- [float32_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#ga4611b605e45ab401f02cab15c5e38715)
- [float64_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gac55f3ae81b5bc9053760baacf57e47f4)

---

[上一章](P363_error.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P365_openthread.h_源码浏览.md)
