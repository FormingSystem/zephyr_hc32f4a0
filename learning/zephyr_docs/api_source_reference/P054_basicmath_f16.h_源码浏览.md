---
id: learning.zephyr-docs.api-source-reference.page-54
title: basicmath_f16.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_basicmath\_f16.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)。

## 54.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00010"></a>
<a id="l00011"></a>
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
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="adsp_8h_html"></a>
<a id="adsp_8h_html_a88feaebec50a9dcd42836439a9849bc7"></a>
<a id="agroup__math__dsp__basic__abs_html_gae1a01c6ab370ebdb6beaf12c02ca5b8d"></a>
<a id="agroup__math__dsp__basic__add_html_gaebb4b61e2e77ace0f9cc0a5765d6661a"></a>
<a id="agroup__math__dsp__basic__clip_html_ga3d3bed1aab5379a67c86b2ffc2ac0c9c"></a>
<a id="agroup__math__dsp__basic__dot_html_ga0ad6b24c20716781e2beb4164059160c"></a>
<a id="agroup__math__dsp__basic__mult_html_ga35c098db40d7973507bb17db7436c538"></a>
<a id="agroup__math__dsp__basic__negate_html_ga662d3680b3a44d00c6b402e9072128dc"></a>
<a id="agroup__math__dsp__basic__offset_html_ga0bcfb3671a9257cabb525fe95794b286"></a>
<a id="agroup__math__dsp__basic__scale_html_gaf25f08e866acb513c69797e4097dd1f5"></a>
<a id="agroup__math__dsp__basic__sub_html_gadfc2150ce943fe13853dedc5a6cb75bd"></a>
<a id="agroup__math__dsp_html_gaa94dc44bddb5718a22bb612890a7fe9f"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>

```c
/* Copyright (C) 2010-2021 ARM Limited or its affiliates. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DSP_BASICMATH_F16_H_
#define ZEPHYR_INCLUDE_DSP_BASICMATH_F16_H_

#ifndef CONFIG_FP16
#error "Cannot use float16 DSP functionality without CONFIG_FP16 enabled"
#endif /* CONFIG_FP16 */

#include <zephyr/dsp/dsp.h>

#ifdef __cplusplus
extern "C" {
#endif

DSP_FUNC_SCOPE void zdsp_mult_f16(const float16_t *src_a, const float16_t *src_b, float16_t *dst,
                                  uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_add_f16(const float16_t *src_a, const float16_t *src_b, float16_t *dst,
                                 uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_sub_f16(const float16_t *src_a, const float16_t *src_b, float16_t *dst,
                                 uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_scale_f16(const float16_t *src, float16_t scale, float16_t *dst,
                                   uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_abs_f16(const float16_t *src, float16_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_dot_prod_f16(const float16_t *src_a, const float16_t *src_b,
                                      uint32_t block_size, float16_t *result);

DSP_FUNC_SCOPE void zdsp_offset_f16(const float16_t *src, float16_t offset, float16_t *dst,
                                    uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_negate_f16(const float16_t *src, float16_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_clip_f16(const float16_t *src, float16_t *dst, float16_t low,
                                  float16_t high, uint32_t num_samples);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DSP_BASICMATH_F16_H_ */
```

## 54.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2010-2021 ARM Limited or its affiliates. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

条件编译配置（Configuration）标记：`CONFIG_FP16`。

### 注释 3：原第 124 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_BASICMATH_F16_H_`。

## 54.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [zephyr/dsp/dsp.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)
- [DSP_FUNC_SCOPE](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html#a88feaebec50a9dcd42836439a9849bc7)
- [zdsp_mult_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html#ga35c098db40d7973507bb17db7436c538)
- [float16_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gaa94dc44bddb5718a22bb612890a7fe9f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_add_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html#gaebb4b61e2e77ace0f9cc0a5765d6661a)
- [zdsp_sub_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html#gadfc2150ce943fe13853dedc5a6cb75bd)
- [zdsp_scale_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#gaf25f08e866acb513c69797e4097dd1f5)
- [zdsp_abs_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html#gae1a01c6ab370ebdb6beaf12c02ca5b8d)
- [zdsp_dot_prod_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html#ga0ad6b24c20716781e2beb4164059160c)
- [zdsp_offset_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga0bcfb3671a9257cabb525fe95794b286)
- [zdsp_negate_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html#ga662d3680b3a44d00c6b402e9072128dc)
- [zdsp_clip_f16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html#ga3d3bed1aab5379a67c86b2ffc2ac0c9c)
- [dsp.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)

---

[上一章](P053_basicmath.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P055_bbram.h_源码浏览.md)
