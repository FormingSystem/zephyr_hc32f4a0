---
id: learning.zephyr-docs.api-source-device-reference.page-59
title: ztress.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第59章\_ztress.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html)。

## 59.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00035"></a>
<a id="foldopen00055"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="foldopen00100"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00176"></a>
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
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="agroup__ztest__ztress_html_ga4406b828d170bc19065aaf65aeb4613e"></a>
<a id="agroup__ztest__ztress_html_ga57f171e230fba462b3dea6b2d3cf71f6"></a>
<a id="agroup__ztest__ztress_html_ga5b3069bb2aa35ddc64c46c18d2e30091"></a>
<a id="agroup__ztest__ztress_html_ga633439263754bf08baee06c37dddab40"></a>
<a id="agroup__ztest__ztress_html_ga99eeabcc672fc5ec0b83ce5b8fb4ec5b"></a>
<a id="agroup__ztest__ztress_html_gacbbdb8e7bad532d6dd20c486b3256e21"></a>
<a id="agroup__ztest__ztress_html_gaf4db2092eee17d863c9810333ba4c870"></a>
<a id="agroup__ztest__ztress_html_gaf706f1af4c42f5925d7545dadf5548fd"></a>
<a id="akernel_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructztress__context__data_html"></a>
<a id="astructztress__context__data_html_a1208baa35d4adc19126d85f45ed78c63"></a>
<a id="astructztress__context__data_html_a17b5f520522cd6fc7024f097f18261ba"></a>
<a id="astructztress__context__data_html_a871f79e1717137500d9ee4c1a2ad07ef"></a>
<a id="astructztress__context__data_html_abc27db12d2734fa35bee654b30497108"></a>
<a id="astructztress__context__data_html_ae96b7b02d0c315bb126193a4f0ad2bdf"></a>
<a id="asys_2util_8h_html"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef TESTSUITE_ZTEST_INCLUDE_ZTRESS_H__
#define TESTSUITE_ZTEST_INCLUDE_ZTRESS_H__

#include <zephyr/sys/util.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

#define ZTRESS_ID_THREAD 0
#define ZTRESS_ID_K_TIMER 1


#define ZTRESS_TIMER(handler, user_data, exec_cnt, init_timeout) \
        (ZTRESS_ID_K_TIMER, handler, user_data, exec_cnt, 0, init_timeout)

#define ZTRESS_THREAD(handler, user_data, exec_cnt, preempt_cnt, init_timeout) \
        (ZTRESS_ID_THREAD, handler, user_data, exec_cnt, preempt_cnt, init_timeout)

typedef bool (*ztress_handler)(void *user_data, uint32_t cnt, bool last, int prio);

struct ztress_context_data {
        /* Handler. */
        ztress_handler handler;

        /* User data */
        void *user_data;

        /* Minimum number of executions to complete the test. */
        uint32_t exec_cnt;

        /* Minimum number of preemptions to complete the test. Valid only for
         * thread context.
         */
        uint32_t preempt_cnt;

        /* Initial timeout. */
        k_timeout_t t;
};

#define ZTRESS_CONTEXT_INITIALIZER(_handler, _user_data, _exec_cnt, _preempt_cnt, _t) \
        { \
                .handler = (_handler), \
                .user_data = (_user_data), \
                .exec_cnt = (_exec_cnt), \
                .preempt_cnt = (_preempt_cnt), \
                .t = (_t) \
        }

#define Z_ZTRESS_GET_HANDLER_DATA2(_, ...) \
        ZTRESS_CONTEXT_INITIALIZER(__VA_ARGS__)

#define Z_ZTRESS_GET_HANDLER_DATA(data) \
        Z_ZTRESS_GET_HANDLER_DATA2 data

#define Z_ZTRESS_HAS_TIMER(data, ...) \
        GET_ARG_N(1, __DEBRACKET data)

#define Z_ZTRESS_TIMER_IDX(idx, data) \
        ((GET_ARG_N(1, __DEBRACKET data)) == ZTRESS_ID_K_TIMER ? idx : 0)

#define Z_ZTRESS_TIMER_CONTEXT_VALIDATE(...) \
        BUILD_ASSERT((FOR_EACH_IDX(Z_ZTRESS_TIMER_IDX, (+), __VA_ARGS__)) == 0, \
                        "There can only be up to one ZTRESS_TIMER context and it must " \
                        "be the first in the list")

#define ZTRESS_EXECUTE(...) do {                                                        \
        Z_ZTRESS_TIMER_CONTEXT_VALIDATE(__VA_ARGS__);                                   \
        int has_timer = Z_ZTRESS_HAS_TIMER(__VA_ARGS__);                                \
        struct ztress_context_data _ctx_data1[] = {                                     \
                FOR_EACH(Z_ZTRESS_GET_HANDLER_DATA, (,), __VA_ARGS__)                   \
        };                                                                              \
        size_t cnt = ARRAY_SIZE(_ctx_data1) - has_timer;                                \
        static struct ztress_context_data _ctx_data[ARRAY_SIZE(_ctx_data1)];            \
        for (size_t i = 0; i < ARRAY_SIZE(_ctx_data1); i++) {                           \
                _ctx_data[i] = _ctx_data1[i];                                           \
        }                                                                               \
        int exec_err = ztress_execute(has_timer ? &_ctx_data[0] : NULL,                 \
                                 &_ctx_data[has_timer], cnt);                           \
                                                                                        \
        zassert_equal(exec_err, 0, "ztress_execute failed (err: %d)", exec_err);        \
} while (0)

int ztress_execute(struct ztress_context_data *timer_data,
                     struct ztress_context_data *thread_data,
                     size_t cnt);

void ztress_abort(void);

void ztress_set_timeout(k_timeout_t t);

void ztress_report(void);

int ztress_exec_count(uint32_t id);

int ztress_preempt_count(uint32_t id);

uint32_t ztress_optimized_ticks(uint32_t id);


#ifdef __cplusplus
}
#endif

#endif /* TESTSUITE_ZTEST_INCLUDE_ZTRESS_H__ */
```

## 59.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 101 行

处理器（Handler）。

### 注释 3：原第 104 行

用户数据（User Data）。

### 注释 4：原第 107 行

完成测试所需的最少执行次数（Minimum Number of Executions）。

### 注释 5：原第 110 行

完成测试所需的最少抢占次数（Minimum Number of Preemptions），仅在线程上下文（Thread Context）中有效。

### 注释 6：原第 115 行

初始超时（Initial Timeout）。

### 注释 7：原第 266 行

头文件保护宏（Header guard）标记：`TESTSUITE_ZTEST_INCLUDE_ZTRESS_H__`。

## 59.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztress_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ztress_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga633439263754bf08baee06c37dddab40)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [ztress_context_data](../hardware/P517_压力测试上下文结构.md)
- [handler](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#abc27db12d2734fa35bee654b30497108)
- [user_data](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a871f79e1717137500d9ee4c1a2ad07ef)
- [exec_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#ae96b7b02d0c315bb126193a4f0ad2bdf)
- [preempt_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a17b5f520522cd6fc7024f097f18261ba)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [t](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a1208baa35d4adc19126d85f45ed78c63)
- [ztress_execute](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf706f1af4c42f5925d7545dadf5548fd)
- [ztress_abort](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga57f171e230fba462b3dea6b2d3cf71f6)
- [ztress_set_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga5b3069bb2aa35ddc64c46c18d2e30091)
- [ztress_report](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gaf4db2092eee17d863c9810333ba4c870)
- [ztress_exec_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga99eeabcc672fc5ec0b83ce5b8fb4ec5b)
- [ztress_preempt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#ga4406b828d170bc19065aaf65aeb4613e)
- [ztress_optimized_ticks](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__ztress.html#gacbbdb8e7bad532d6dd20c486b3256e21)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [ztress_context_data::t](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a1208baa35d4adc19126d85f45ed78c63)
- [ztress_context_data::preempt_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a17b5f520522cd6fc7024f097f18261ba)
- [ztress_context_data::user_data](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#a871f79e1717137500d9ee4c1a2ad07ef)
- [ztress_context_data::handler](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#abc27db12d2734fa35bee654b30497108)
- [ztress_context_data::exec_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structztress__context__data.html#ae96b7b02d0c315bb126193a4f0ad2bdf)
- [util.h](../util_reference/P002_通用工具头文件参考.md)

---

[上一章](P058_ztest_test.h_源码浏览.md) · [返回大纲](大纲.md)
