---
id: learning.zephyr-docs.api-source-reference.page-53
title: basicmath.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_basicmath.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)。

## 53.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00038"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00109"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00168"></a>
<a id="l00180"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00239"></a>
<a id="l00265"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00330"></a>
<a id="l00344"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00399"></a>
<a id="l00412"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00479"></a>
<a id="l00496"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00548"></a>
<a id="l00563"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00588"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="l00603"></a>
<a id="l00616"></a>
<a id="l00617"></a>
<a id="l00618"></a>
<a id="l00622"></a>
<a id="l00637"></a>
<a id="l00644"></a>
<a id="l00645"></a>
<a id="l00646"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="l00660"></a>
<a id="l00672"></a>
<a id="l00673"></a>
<a id="l00674"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00692"></a>
<a id="l00702"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="l00712"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00736"></a>
<a id="l00746"></a>
<a id="l00754"></a>
<a id="l00755"></a>
<a id="l00756"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00774"></a>
<a id="l00775"></a>
<a id="l00776"></a>
<a id="l00780"></a>
<a id="l00790"></a>
<a id="l00797"></a>
<a id="l00798"></a>
<a id="l00799"></a>
<a id="l00806"></a>
<a id="l00807"></a>
<a id="l00808"></a>
<a id="l00815"></a>
<a id="l00816"></a>
<a id="l00817"></a>
<a id="l00821"></a>
<a id="l00831"></a>
<a id="l00839"></a>
<a id="l00840"></a>
<a id="l00841"></a>
<a id="l00849"></a>
<a id="l00850"></a>
<a id="l00851"></a>
<a id="l00859"></a>
<a id="l00860"></a>
<a id="l00861"></a>
<a id="l00865"></a>
<a id="l00877"></a>
<a id="l00886"></a>
<a id="l00887"></a>
<a id="l00888"></a>
<a id="l00897"></a>
<a id="l00898"></a>
<a id="l00899"></a>
<a id="l00908"></a>
<a id="l00909"></a>
<a id="l00910"></a>
<a id="l00919"></a>
<a id="l00920"></a>
<a id="l00921"></a>
<a id="l00925"></a>
<a id="l00929"></a>
<a id="l00930"></a>
<a id="l00931"></a>
<a id="l00932"></a>
<a id="l00933"></a>
<a id="l00934"></a>
<a id="l00935"></a>
<a id="l00936"></a>
<a id="l00937"></a>
<a id="l00938"></a>
<a id="abasicmath__f16_8h_html"></a>
<a id="adsp_8h_html"></a>
<a id="adsp_8h_html_a2ba5cab25d6c097e55bbe14094a06c7c"></a>
<a id="adsp_8h_html_a88feaebec50a9dcd42836439a9849bc7"></a>
<a id="agroup__math__dsp__basic__abs_html_ga53ee6bbc05423703f6299fd60c8e1d44"></a>
<a id="agroup__math__dsp__basic__abs_html_ga5a5358fb90f726256f064757fbab1bcd"></a>
<a id="agroup__math__dsp__basic__abs_html_ga69c38809979de090a3458ec9b31f4cb4"></a>
<a id="agroup__math__dsp__basic__abs_html_ga74ccbbaf60257ca482fc96e1d40edeca"></a>
<a id="agroup__math__dsp__basic__add_html_ga978af9251a9c8b8d62b47a921dcf9d38"></a>
<a id="agroup__math__dsp__basic__add_html_gad2bbabc990f868b3ecfe270458e22657"></a>
<a id="agroup__math__dsp__basic__add_html_gae5d919e8595e80216302953797fcf987"></a>
<a id="agroup__math__dsp__basic__add_html_gae890add140205717dcb4b1c39650b797"></a>
<a id="agroup__math__dsp__basic__and_html_ga22c8c022d4f8cd9e34f1e1e47433d121"></a>
<a id="agroup__math__dsp__basic__and_html_ga988879dc54666692130793f6ce26fd23"></a>
<a id="agroup__math__dsp__basic__and_html_ga99019932e69574ca8aef86b4ace9c3b6"></a>
<a id="agroup__math__dsp__basic__clip_html_ga2a7483cb8150e3caee8fade382dc3ceb"></a>
<a id="agroup__math__dsp__basic__clip_html_ga4e368fccf4ec5f46e82127816ecfc22e"></a>
<a id="agroup__math__dsp__basic__clip_html_ga7c83f52241784bfdf81baf14581435b9"></a>
<a id="agroup__math__dsp__basic__clip_html_gaa81f891d1946313161d1a2989aafe0e1"></a>
<a id="agroup__math__dsp__basic__dot_html_ga5a76ac790b7d981b97143f7473587ccf"></a>
<a id="agroup__math__dsp__basic__dot_html_ga66932c50dc7e2b7207ad5c8218c110a6"></a>
<a id="agroup__math__dsp__basic__dot_html_gaa6bdeed693734e5d1c7b93b58eaf9eeb"></a>
<a id="agroup__math__dsp__basic__dot_html_gaae752f1d9645d8c80fcdabc0f0b249f8"></a>
<a id="agroup__math__dsp__basic__mult_html_ga0e4e4ff5e33e792feecf811cb8e96d18"></a>
<a id="agroup__math__dsp__basic__mult_html_gac9513150fc602b6bab481faf36f81ca4"></a>
<a id="agroup__math__dsp__basic__mult_html_gae0792b036a40a19af1c25b3a6a23e988"></a>
<a id="agroup__math__dsp__basic__mult_html_gaf8aa8d6e976c9ee5f4ac836506da3bc7"></a>
<a id="agroup__math__dsp__basic__negate_html_ga08591323e804b4d7932c7bade4331705"></a>
<a id="agroup__math__dsp__basic__negate_html_ga41dc3e0d8a0bd3654f74cbbd9038153d"></a>
<a id="agroup__math__dsp__basic__negate_html_ga578a3cee7cff2d818e41ec974066d55a"></a>
<a id="agroup__math__dsp__basic__negate_html_gad8760ce77fcf2198f73813278fa15343"></a>
<a id="agroup__math__dsp__basic__not_html_ga3bca20f3c626e1a64dd79d0e22a43bed"></a>
<a id="agroup__math__dsp__basic__not_html_gaafd38edd648a03d328d51b5ca9097b5d"></a>
<a id="agroup__math__dsp__basic__not_html_gafd6993acd6abeaa529dea84f3fd4d3a9"></a>
<a id="agroup__math__dsp__basic__offset_html_ga1740996532090e41ce20913bb201023c"></a>
<a id="agroup__math__dsp__basic__offset_html_ga1f14e702ad5dc6482fcdb4758ad862c3"></a>
<a id="agroup__math__dsp__basic__offset_html_ga2b5958ec0fc8bb26662c41136ec46b3e"></a>
<a id="agroup__math__dsp__basic__offset_html_ga701b8bbd1437e0f19807c38fd4d0e7e9"></a>
<a id="agroup__math__dsp__basic__or_html_ga979e50ef34a5e5c8dc28f1cfc5ef708a"></a>
<a id="agroup__math__dsp__basic__or_html_gaa218930efe8ab83663eb00b4f6f170bc"></a>
<a id="agroup__math__dsp__basic__or_html_gabf9687bce70f19c4192b2ddba7b0d2da"></a>
<a id="agroup__math__dsp__basic__scale_html_ga2158a3f20bd5af0516f5b3af824c32e1"></a>
<a id="agroup__math__dsp__basic__scale_html_ga3a07935285b763bb9e9106db42292466"></a>
<a id="agroup__math__dsp__basic__scale_html_ga63eaab2b1ef431e4bceb90b0a701c879"></a>
<a id="agroup__math__dsp__basic__scale_html_ga95e03e993542ff1710c771a9dc0eb01b"></a>
<a id="agroup__math__dsp__basic__shift_html_ga738fc0fe86b9c910a30fceff7dc4a789"></a>
<a id="agroup__math__dsp__basic__shift_html_ga8eb72ff139c173d3e1794a1d1c1c8fde"></a>
<a id="agroup__math__dsp__basic__shift_html_gaf9af89a3c76ad385eec0225185b522c9"></a>
<a id="agroup__math__dsp__basic__sub_html_ga4eb67772a48933a9f24a68f73228adbf"></a>
<a id="agroup__math__dsp__basic__sub_html_ga693b9677fdf54694e49e03a9b629b35d"></a>
<a id="agroup__math__dsp__basic__sub_html_gab9698353b69654eefbd76ff6f723a4f3"></a>
<a id="agroup__math__dsp__basic__sub_html_gafc66edd5888b19174cb24c2ea858d24d"></a>
<a id="agroup__math__dsp__basic__xor_html_ga4f5a442ce2ce79a6d09fde4648ceb100"></a>
<a id="agroup__math__dsp__basic__xor_html_gaa4d486a9a9022120e86e6e5d62940444"></a>
<a id="agroup__math__dsp__basic__xor_html_gac4dd8fed6e7485a0e989fb37b3fe0c77"></a>
<a id="agroup__math__dsp_html_ga4611b605e45ab401f02cab15c5e38715"></a>
<a id="agroup__math__dsp_html_ga5aea1cb12fc02d9d44c8abf217eaa5c6"></a>
<a id="agroup__math__dsp_html_gab5a8fb21a5b3b983d5f54f31614052ea"></a>
<a id="agroup__math__dsp_html_gadc89a3547f5324b7b3b95adec3806bc0"></a>
<a id="agroup__math__dsp_html_gae541b6f232c305361e9b416fc9eed263"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>

```c
/* Copyright (C) 2010-2021 ARM Limited or its affiliates. All rights reserved.
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DSP_BASICMATH_H_
#define ZEPHYR_INCLUDE_DSP_BASICMATH_H_

#include <zephyr/dsp/dsp.h>

#ifdef __cplusplus
extern "C" {
#endif



DSP_FUNC_SCOPE void zdsp_mult_q7(const DSP_DATA q7_t *src_a, const DSP_DATA q7_t *src_b,
                                DSP_DATA q7_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_mult_q15(const DSP_DATA q15_t *src_a, const DSP_DATA q15_t *src_b,
                                DSP_DATA q15_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_mult_q31(const DSP_DATA q31_t *src_a, const DSP_DATA q31_t *src_b,
                                DSP_DATA q31_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_mult_f32(const DSP_DATA float32_t *src_a, const DSP_DATA float32_t *src_b,
                                DSP_DATA float32_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_add_f32(const DSP_DATA float32_t *src_a, const DSP_DATA float32_t *src_b,
                                DSP_DATA float32_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_add_q7(const DSP_DATA q7_t *src_a, const DSP_DATA q7_t *src_b,
                                DSP_DATA q7_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_add_q15(const DSP_DATA q15_t *src_a, const DSP_DATA q15_t *src_b,
                                DSP_DATA q15_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_add_q31(const DSP_DATA q31_t *src_a, const DSP_DATA q31_t *src_b,
                                DSP_DATA q31_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_sub_f32(const DSP_DATA float32_t *src_a, const DSP_DATA float32_t *src_b,
                                DSP_DATA float32_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_sub_q7(const DSP_DATA q7_t *src_a, const DSP_DATA q7_t *src_b,
                                DSP_DATA q7_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_sub_q15(const DSP_DATA q15_t *src_a, const DSP_DATA q15_t *src_b,
                                DSP_DATA q15_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_sub_q31(const DSP_DATA q31_t *src_a, const DSP_DATA q31_t *src_b,
                                DSP_DATA q31_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_scale_f32(const DSP_DATA float32_t *src, float32_t scale,
                                DSP_DATA float32_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_scale_q7(const DSP_DATA q7_t *src, q7_t scale_fract, int8_t shift,
                                DSP_DATA q7_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_scale_q15(const DSP_DATA q15_t *src, q15_t scale_fract, int8_t shift,
                                DSP_DATA q15_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_scale_q31(const DSP_DATA q31_t *src, q31_t scale_fract, int8_t shift,
                                DSP_DATA q31_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_abs_f32(const DSP_DATA float32_t *src, DSP_DATA float32_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_abs_q7(const DSP_DATA q7_t *src, DSP_DATA q7_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_abs_q15(const DSP_DATA q15_t *src, DSP_DATA q15_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_abs_q31(const DSP_DATA q31_t *src, DSP_DATA q31_t *dst,
                                uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_dot_prod_f32(const DSP_DATA float32_t *src_a,
                                const DSP_DATA float32_t *src_b, uint32_t block_size,
                                DSP_DATA float32_t *result);

DSP_FUNC_SCOPE void zdsp_dot_prod_q7(const DSP_DATA q7_t *src_a, const DSP_DATA q7_t *src_b,
                                uint32_t block_size, DSP_DATA q31_t *result);

DSP_FUNC_SCOPE void zdsp_dot_prod_q15(const DSP_DATA q15_t *src_a, const DSP_DATA q15_t *src_b,
                                uint32_t block_size, DSP_DATA q63_t *result);

DSP_FUNC_SCOPE void zdsp_dot_prod_q31(const DSP_DATA q31_t *src_a, const DSP_DATA q31_t *src_b,
                                uint32_t block_size, DSP_DATA q63_t *result);



DSP_FUNC_SCOPE void zdsp_shift_q7(const DSP_DATA q7_t *src, int8_t shift_bits, DSP_DATA q7_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_shift_q15(const DSP_DATA q15_t *src, int8_t shift_bits,
                                DSP_DATA q15_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_shift_q31(const DSP_DATA q31_t *src, int8_t shift_bits,
                                DSP_DATA q31_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_offset_f32(const DSP_DATA float32_t *src, float32_t offset,
                                DSP_DATA float32_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_offset_q7(const DSP_DATA q7_t *src, q7_t offset, DSP_DATA q7_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_offset_q15(const DSP_DATA q15_t *src, q15_t offset, DSP_DATA q15_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_offset_q31(const DSP_DATA q31_t *src, q31_t offset, DSP_DATA q31_t *dst,
                                uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_negate_f32(const DSP_DATA float32_t *src, DSP_DATA float32_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_negate_q7(const DSP_DATA q7_t *src, DSP_DATA q7_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_negate_q15(const DSP_DATA q15_t *src, DSP_DATA q15_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_negate_q31(const DSP_DATA q31_t *src, DSP_DATA q31_t *dst,
                                uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_and_u8(const DSP_DATA uint8_t *src_a, const DSP_DATA uint8_t *src_b,
                                DSP_DATA uint8_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_and_u16(const DSP_DATA uint16_t *src_a, const DSP_DATA uint16_t *src_b,
                                DSP_DATA uint16_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_and_u32(const DSP_DATA uint32_t *src_a, const DSP_DATA uint32_t *src_b,
                                DSP_DATA uint32_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_or_u8(const DSP_DATA uint8_t *src_a, const DSP_DATA uint8_t *src_b,
                                DSP_DATA uint8_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_or_u16(const DSP_DATA uint16_t *src_a, const DSP_DATA uint16_t *src_b,
                                DSP_DATA uint16_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_or_u32(const DSP_DATA uint32_t *src_a, const DSP_DATA uint32_t *src_b,
                                DSP_DATA uint32_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_not_u8(const DSP_DATA uint8_t *src, DSP_DATA uint8_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_not_u16(const DSP_DATA uint16_t *src, DSP_DATA uint16_t *dst,
                                uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_not_u32(const DSP_DATA uint32_t *src, DSP_DATA uint32_t *dst,
                                uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_xor_u8(const DSP_DATA uint8_t *src_a, const DSP_DATA uint8_t *src_b,
                                DSP_DATA uint8_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_xor_u16(const DSP_DATA uint16_t *src_a, const DSP_DATA uint16_t *src_b,
                                DSP_DATA uint16_t *dst, uint32_t block_size);

DSP_FUNC_SCOPE void zdsp_xor_u32(const DSP_DATA uint32_t *src_a, const DSP_DATA uint32_t *src_b,
                                DSP_DATA uint32_t *dst, uint32_t block_size);



DSP_FUNC_SCOPE void zdsp_clip_f32(const DSP_DATA float32_t *src, DSP_DATA float32_t *dst,
                                float32_t low, float32_t high, uint32_t num_samples);

DSP_FUNC_SCOPE void zdsp_clip_q31(const DSP_DATA q31_t *src, DSP_DATA q31_t *dst, q31_t low,
                                q31_t high, uint32_t num_samples);

DSP_FUNC_SCOPE void zdsp_clip_q15(const DSP_DATA q15_t *src, DSP_DATA q15_t *dst, q15_t low,
                                q15_t high, uint32_t num_samples);

DSP_FUNC_SCOPE void zdsp_clip_q7(const DSP_DATA q7_t *src, DSP_DATA q7_t *dst, q7_t low, q7_t high,
                                uint32_t num_samples);



#ifdef __cplusplus
}
#endif

#ifdef CONFIG_FP16
#include <zephyr/dsp/basicmath_f16.h>
#endif /* CONFIG_FP16 */

#endif /* ZEPHYR_INCLUDE_DSP_BASICMATH_H_ */
```

## 53.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2010-2021 ARM Limited or its affiliates. All rights reserved.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 936 行

条件编译配置（Configuration）标记：`CONFIG_FP16`。

### 注释 3：原第 938 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DSP_BASICMATH_H_`。

## 53.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/basicmath_8h.html)
- [zephyr/dsp/dsp.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)
- [DSP_FUNC_SCOPE](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html#a88feaebec50a9dcd42836439a9849bc7)
- [zdsp_mult_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html#gae0792b036a40a19af1c25b3a6a23e988)
- [DSP_DATA](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html#a2ba5cab25d6c097e55bbe14094a06c7c)
- [q7_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gae541b6f232c305361e9b416fc9eed263)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [zdsp_mult_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html#gaf8aa8d6e976c9ee5f4ac836506da3bc7)
- [q15_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gab5a8fb21a5b3b983d5f54f31614052ea)
- [zdsp_mult_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html#ga0e4e4ff5e33e792feecf811cb8e96d18)
- [q31_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#gadc89a3547f5324b7b3b95adec3806bc0)
- [zdsp_mult_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__mult.html#gac9513150fc602b6bab481faf36f81ca4)
- [float32_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#ga4611b605e45ab401f02cab15c5e38715)
- [zdsp_add_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html#gae890add140205717dcb4b1c39650b797)
- [zdsp_add_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html#gae5d919e8595e80216302953797fcf987)
- [zdsp_add_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html#ga978af9251a9c8b8d62b47a921dcf9d38)
- [zdsp_add_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__add.html#gad2bbabc990f868b3ecfe270458e22657)
- [zdsp_sub_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html#gafc66edd5888b19174cb24c2ea858d24d)
- [zdsp_sub_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html#ga4eb67772a48933a9f24a68f73228adbf)
- [zdsp_sub_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html#gab9698353b69654eefbd76ff6f723a4f3)
- [zdsp_sub_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__sub.html#ga693b9677fdf54694e49e03a9b629b35d)
- [zdsp_scale_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga3a07935285b763bb9e9106db42292466)
- [zdsp_scale_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga2158a3f20bd5af0516f5b3af824c32e1)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [zdsp_scale_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga95e03e993542ff1710c771a9dc0eb01b)
- [zdsp_scale_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__scale.html#ga63eaab2b1ef431e4bceb90b0a701c879)
- [zdsp_abs_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html#ga5a5358fb90f726256f064757fbab1bcd)
- [zdsp_abs_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html#ga69c38809979de090a3458ec9b31f4cb4)
- [zdsp_abs_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html#ga53ee6bbc05423703f6299fd60c8e1d44)
- [zdsp_abs_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__abs.html#ga74ccbbaf60257ca482fc96e1d40edeca)
- [zdsp_dot_prod_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html#ga66932c50dc7e2b7207ad5c8218c110a6)
- [zdsp_dot_prod_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html#gaa6bdeed693734e5d1c7b93b58eaf9eeb)
- [zdsp_dot_prod_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html#ga5a76ac790b7d981b97143f7473587ccf)
- [q63_t](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html#ga5aea1cb12fc02d9d44c8abf217eaa5c6)
- [zdsp_dot_prod_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__dot.html#gaae752f1d9645d8c80fcdabc0f0b249f8)
- [zdsp_shift_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html#ga8eb72ff139c173d3e1794a1d1c1c8fde)
- [zdsp_shift_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html#ga738fc0fe86b9c910a30fceff7dc4a789)
- [zdsp_shift_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__shift.html#gaf9af89a3c76ad385eec0225185b522c9)
- [zdsp_offset_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1f14e702ad5dc6482fcdb4758ad862c3)
- [zdsp_offset_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga701b8bbd1437e0f19807c38fd4d0e7e9)
- [zdsp_offset_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga1740996532090e41ce20913bb201023c)
- [zdsp_offset_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__offset.html#ga2b5958ec0fc8bb26662c41136ec46b3e)
- [zdsp_negate_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html#gad8760ce77fcf2198f73813278fa15343)
- [zdsp_negate_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html#ga578a3cee7cff2d818e41ec974066d55a)
- [zdsp_negate_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html#ga41dc3e0d8a0bd3654f74cbbd9038153d)
- [zdsp_negate_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__negate.html#ga08591323e804b4d7932c7bade4331705)
- [zdsp_and_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html#ga22c8c022d4f8cd9e34f1e1e47433d121)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zdsp_and_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html#ga988879dc54666692130793f6ce26fd23)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [zdsp_and_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__and.html#ga99019932e69574ca8aef86b4ace9c3b6)
- [zdsp_or_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__or.html#gabf9687bce70f19c4192b2ddba7b0d2da)
- [zdsp_or_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__or.html#ga979e50ef34a5e5c8dc28f1cfc5ef708a)
- [zdsp_or_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__or.html#gaa218930efe8ab83663eb00b4f6f170bc)
- [zdsp_not_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html#gaafd38edd648a03d328d51b5ca9097b5d)
- [zdsp_not_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html#ga3bca20f3c626e1a64dd79d0e22a43bed)
- [zdsp_not_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__not.html#gafd6993acd6abeaa529dea84f3fd4d3a9)
- [zdsp_xor_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html#ga4f5a442ce2ce79a6d09fde4648ceb100)
- [zdsp_xor_u16](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html#gaa4d486a9a9022120e86e6e5d62940444)
- [zdsp_xor_u32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__xor.html#gac4dd8fed6e7485a0e989fb37b3fe0c77)
- [zdsp_clip_f32](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html#gaa81f891d1946313161d1a2989aafe0e1)
- [zdsp_clip_q31](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html#ga2a7483cb8150e3caee8fade382dc3ceb)
- [zdsp_clip_q15](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html#ga7c83f52241784bfdf81baf14581435b9)
- [zdsp_clip_q7](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp__basic__clip.html#ga4e368fccf4ec5f46e82127816ecfc22e)
- [zephyr/dsp/basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [basicmath_f16.h](https://docs.zephyrproject.org/latest/doxygen/html/basicmath__f16_8h.html)
- [dsp.h](https://docs.zephyrproject.org/latest/doxygen/html/dsp_8h.html)

---

[上一章](P052_base.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P054_basicmath_f16.h_源码浏览.md)
