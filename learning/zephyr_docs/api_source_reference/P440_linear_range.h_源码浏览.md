---
id: learning.zephyr-docs.api-source-reference.page-440
title: linear_range.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第440章\_linear\_range.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h.html)。

## 440.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00024"></a>
<a id="l00067"></a>
<a id="foldopen00069"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00116"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="foldopen00150"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="foldopen00173"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00239"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="foldopen00273"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00326"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__linear__range_html_ga11dc5408be53887e9ddf992b574aa16c"></a>
<a id="agroup__linear__range_html_ga67b24d9d6e7088daf39020c8c02f8d96"></a>
<a id="agroup__linear__range_html_ga6c06a26d629f4d7a195188e7c5df5db1"></a>
<a id="agroup__linear__range_html_ga72b800d1c6af44cb247130139176a59e"></a>
<a id="agroup__linear__range_html_ga90610e42e63eb4290e5ae6187a53143f"></a>
<a id="agroup__linear__range_html_gab8b661f6ed1caba2ab4796a02c1b24a8"></a>
<a id="agroup__linear__range_html_gac054f5cc2aad11de223fa968ebeaa55c"></a>
<a id="agroup__linear__range_html_gae02547c7922e5a36c815dc89bc1df128"></a>
<a id="agroup__linear__range_html_gae6315858afa73945bc44d8c5c997645c"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="agroup__system__errno_html_gaa1591a4f3a86360108de5b9ba34980ca"></a>
<a id="aminmax_8h_html_ac6afabdc09a49a433ee19d8a9486056d"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdlib_8h_html"></a>
<a id="astructlinear__range_html"></a>
<a id="astructlinear__range_html_a4523369fa49fa1d6aa58f0d2634eb41d"></a>
<a id="astructlinear__range_html_a705275f156fc4bcf5bb111be01aff6ef"></a>
<a id="astructlinear__range_html_a84af63957a1b3e829cf1d53fa6342982"></a>
<a id="astructlinear__range_html_a963889c27dd8541f7cd6528ac82401b3"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (C) 2022, Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_SYS_LINEAR_RANGE_H_
#define ZEPHYR_INCLUDE_SYS_LINEAR_RANGE_H_

#include <errno.h>
#include <stdint.h>
#include <stdlib.h>

#include <zephyr/sys/util.h>

#ifdef __cplusplus
extern "C" {
#endif


struct linear_range {
        int32_t min;
        uint32_t step;
        uint16_t min_idx;
        uint16_t max_idx;
};

#define LINEAR_RANGE_INIT(_min, _step, _min_idx, _max_idx)                     \
        {                                                                      \
                .min = (_min),                                                 \
                .step = (_step),                                               \
                .min_idx = (_min_idx),                                         \
                .max_idx = (_max_idx),                                         \
        }

static inline uint32_t linear_range_values_count(const struct linear_range *r)
{
        return r->max_idx - r->min_idx + 1U;
}

static inline uint32_t linear_range_group_values_count(
        const struct linear_range *r, size_t r_cnt)
{
        uint32_t values = 0U;

        for (size_t i = 0U; i < r_cnt; i++) {
                values += linear_range_values_count(&r[i]);
        }

        return values;
}

static inline int32_t linear_range_get_max_value(const struct linear_range *r)
{
        return r->min + (int32_t)(r->step * (r->max_idx - r->min_idx));
}

static inline int linear_range_get_value(const struct linear_range *r,
                                         uint16_t idx, int32_t *val)
{
        if ((idx < r->min_idx) || (idx > r->max_idx)) {
                return -EINVAL;
        }

        *val = r->min + (int32_t)(r->step * (idx - r->min_idx));

        return 0;
}

static inline int linear_range_group_get_value(const struct linear_range *r,
                                               size_t r_cnt, uint16_t idx,
                                               int32_t *val)
{
        int ret = -EINVAL;

        for (size_t i = 0U; (ret != 0) && (i < r_cnt); i++) {
                ret = linear_range_get_value(&r[i], idx, val);
        }

        return ret;
}

static inline int linear_range_get_index(const struct linear_range *r,
                                         int32_t val, uint16_t *idx)
{
        if (val < r->min) {
                *idx = r->min_idx;
                return -ERANGE;
        }

        if (val > linear_range_get_max_value(r)) {
                *idx = r->max_idx;
                return -ERANGE;
        }

        if (r->step == 0U) {
                *idx = r->min_idx;
        } else {
                *idx = r->min_idx + DIV_ROUND_UP((uint32_t)(val - r->min),
                                                 r->step);
        }

        return 0;
}

static inline int linear_range_group_get_index(const struct linear_range *r,
                                               size_t r_cnt, int32_t val,
                                               uint16_t *idx)
{
        for (size_t i = 0U; i < r_cnt; i++) {
                if ((val > linear_range_get_max_value(&r[i])) &&
                    (i < (r_cnt - 1U))) {
                        continue;
                }

                return linear_range_get_index(&r[i], val, idx);
        }

        return -EINVAL;
}

static inline int linear_range_get_win_index(const struct linear_range *r,
                                             int32_t val_min, int32_t val_max,
                                             uint16_t *idx)
{
        int32_t r_max = linear_range_get_max_value(r);

        if ((val_max < r->min) || (val_min > r_max)) {
                return -EINVAL;
        }

        if (val_min < r->min) {
                *idx = r->min_idx;
                return -ERANGE;
        }

        if (val_max > r_max) {
                *idx = r->max_idx;
                return -ERANGE;
        }

        if (r->step == 0U) {
                *idx = r->min_idx;
                return 0;
        }

        *idx = r->min_idx + DIV_ROUND_UP((uint32_t)(val_min - r->min), r->step);
        if ((r->min + r->step * (*idx - r->min_idx)) > val_max) {
                return -EINVAL;
        }

        return 0;
}

static inline int linear_range_group_get_win_index(const struct linear_range *r,
                                                   size_t r_cnt,
                                                   int32_t val_min,
                                                   int32_t val_max,
                                                   uint16_t *idx)
{
        for (size_t i = 0U; i < r_cnt; i++) {
                if (val_min > linear_range_get_max_value(&r[i])) {
                        continue;
                }

                return linear_range_get_win_index(&r[i], val_min, val_max, idx);
        }

        return -EINVAL;
}


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_LINEAR_RANGE_H_ */
```

## 440.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：(C) 2022, Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 349 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SYS_LINEAR_RANGE_H_`。

## 440.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/linear__range_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdlib.h](https://docs.zephyrproject.org/latest/doxygen/html/stdlib_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [linear_range](../system_service_model_reference/P060_linear_range_结构体.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [min](../system_service_model_reference/P060_linear_range_结构体.md#a4523369fa49fa1d6aa58f0d2634eb41d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [step](../system_service_model_reference/P060_linear_range_结构体.md#a963889c27dd8541f7cd6528ac82401b3)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [min_idx](../system_service_model_reference/P060_linear_range_结构体.md#a705275f156fc4bcf5bb111be01aff6ef)
- [max_idx](../system_service_model_reference/P060_linear_range_结构体.md#a84af63957a1b3e829cf1d53fa6342982)
- [linear_range_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae02547c7922e5a36c815dc89bc1df128)
- [linear_range_group_values_count](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga67b24d9d6e7088daf39020c8c02f8d96)
- [linear_range_get_max_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gae6315858afa73945bc44d8c5c997645c)
- [linear_range_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga72b800d1c6af44cb247130139176a59e)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [linear_range_group_get_value](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gac054f5cc2aad11de223fa968ebeaa55c)
- [linear_range_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga90610e42e63eb4290e5ae6187a53143f)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [ERANGE](../error_reference/P003_系统错误号公共接口.md#gaa1591a4f3a86360108de5b9ba34980ca)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [linear_range_group_get_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#gab8b661f6ed1caba2ab4796a02c1b24a8)
- [linear_range_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga6c06a26d629f4d7a195188e7c5df5db1)
- [linear_range_group_get_win_index](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html#ga11dc5408be53887e9ddf992b574aa16c)
- [linear_range::min](../system_service_model_reference/P060_linear_range_结构体.md#a4523369fa49fa1d6aa58f0d2634eb41d)
- [linear_range::min_idx](../system_service_model_reference/P060_linear_range_结构体.md#a705275f156fc4bcf5bb111be01aff6ef)
- [linear_range::max_idx](../system_service_model_reference/P060_linear_range_结构体.md#a84af63957a1b3e829cf1d53fa6342982)
- [linear_range::step](../system_service_model_reference/P060_linear_range_结构体.md#a963889c27dd8541f7cd6528ac82401b3)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P439_transceiver.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P441_lis2de12.h_源码浏览.md)
