---
id: learning.zephyr-docs.api-source-reference.page-664
title: pmu.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第664章\_pmu.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html)。

## 664.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00025"></a>
<a id="l00026"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00045"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="foldopen00054"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="agroup__pmu_html_ga12a5201eb9df8c7f83496847526e63ad"></a>
<a id="agroup__pmu_html_ga1b740b0f45c4435cdf3219a5bb3058f7"></a>
<a id="agroup__pmu_html_ga29dc5718b7d83eaaf1c52645394394ef"></a>
<a id="agroup__pmu_html_ga3093c22c8e423cddd786c8555fcb7c80"></a>
<a id="agroup__pmu_html_ga35a447da13644c22f4e7148547cbdc9d"></a>
<a id="agroup__pmu_html_ga3fa69d6fabe2389dc23ab3b54b72bc6d"></a>
<a id="agroup__pmu_html_ga4b1050bae21c638c9b2dad291461cfdf"></a>
<a id="agroup__pmu_html_ga6cc9827c689699f6a33ad2c782a6b22a"></a>
<a id="agroup__pmu_html_ga6df789669765f445f865c8f6435bb679"></a>
<a id="agroup__pmu_html_ga788901c9f07cadaf4768b48536af7eac"></a>
<a id="agroup__pmu_html_ga928fc146e105f2250fe6f971e2f67a00"></a>
<a id="agroup__pmu_html_gaa6301bd3af19d347ae4210be8dfe20e6"></a>
<a id="agroup__pmu_html_gaaa6b497c1d6e3b0af8ef6f04cbdf0d98"></a>
<a id="agroup__pmu_html_gaad18df75ad3e5928f6a15e92acb4899c"></a>
<a id="agroup__pmu_html_gab4d1ae5b2c4351a0d0c69d9477357c0e"></a>
<a id="agroup__pmu_html_gac3299a44c61e0d28d974ea6aa2e9ffbc"></a>
<a id="agroup__pmu_html_gafe7fb7ed9a8646ecfc40d2c7c443b35f"></a>
<a id="apmu_8h_html_a1e81090eaba4c1aa7009fe85f5bf2f6a"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructpmu__counter__config_html"></a>
<a id="astructpmu__counter__config_html_a482305d6da6760f7a177a8737f720f88"></a>
<a id="astructpmu__counter__config_html_ab8f9346eec1110d9b45dba5570aef2cd"></a>
<a id="astructpmu__info__t_html"></a>
<a id="astructpmu__info__t_html_a20ad7ea312a6f3199078d9cdb7c224f1"></a>
<a id="astructpmu__info__t_html_a5b11627370ddcc76202fd7c59f6e7e3d"></a>

```c
/*
 * Copyright (c) 2026 Advanced Micro Devices, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_ZEPHYR_PMU_H_
#define ZEPHYR_INCLUDE_ZEPHYR_PMU_H_

#include <zephyr/autoconf.h>
#include <stdint.h>
#include <stdbool.h>

#if defined(CONFIG_ARM64)
#include <zephyr/arch/arm64/pmuv3.h>
#else
typedef uint32_t pmu_evt_t;

typedef struct {
        uint32_t implementer;
        uint32_t idcode;
} pmu_info_t;
#endif

#ifdef __cplusplus
extern "C" {
#endif


#define PMU_MAX_COUNTERS 8

struct pmu_counter_config {
        pmu_evt_t event;
        bool enabled;
};

int pmu_init(void);

uint32_t pmu_num_counters(void);

void pmu_get_info(pmu_info_t *info);

int pmu_counter_config(uint32_t counter, pmu_evt_t event);

void pmu_counter_enable(uint32_t counter);

void pmu_counter_disable(uint32_t counter);

void pmu_counter_enable_all(void);

void pmu_counter_disable_all(void);

uint64_t pmu_counter_read(uint32_t counter);

void pmu_counter_reset(uint32_t counter);

void pmu_counter_reset_all(void);

uint64_t pmu_cycle_count(void);

void pmu_cycle_reset(void);

void pmu_start(void);

void pmu_stop(void);

bool pmu_counter_overflow(uint32_t counter);

void pmu_counter_clear_overflow(uint32_t counter);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_ZEPHYR_PMU_H_ */
```

## 664.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Advanced Micro Devices, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 208 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_PMU_H_`。

## 664.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [pmu_evt_t](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h.html#a1e81090eaba4c1aa7009fe85f5bf2f6a)
- [implementer](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md#a20ad7ea312a6f3199078d9cdb7c224f1)
- [idcode](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md#a5b11627370ddcc76202fd7c59f6e7e3d)
- [pmu_info_t](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md)
- [pmu_counter_config](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md)
- [event](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md#a482305d6da6760f7a177a8737f720f88)
- [enabled](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md#ab8f9346eec1110d9b45dba5570aef2cd)
- [pmu_init](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaad18df75ad3e5928f6a15e92acb4899c)
- [pmu_num_counters](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaa6301bd3af19d347ae4210be8dfe20e6)
- [pmu_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6cc9827c689699f6a33ad2c782a6b22a)
- [pmu_counter_config](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3093c22c8e423cddd786c8555fcb7c80)
- [pmu_counter_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga1b740b0f45c4435cdf3219a5bb3058f7)
- [pmu_counter_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga788901c9f07cadaf4768b48536af7eac)
- [pmu_counter_enable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga928fc146e105f2250fe6f971e2f67a00)
- [pmu_counter_disable_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga6df789669765f445f865c8f6435bb679)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pmu_counter_read](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gab4d1ae5b2c4351a0d0c69d9477357c0e)
- [pmu_counter_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga4b1050bae21c638c9b2dad291461cfdf)
- [pmu_counter_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gafe7fb7ed9a8646ecfc40d2c7c443b35f)
- [pmu_cycle_count](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gaaa6b497c1d6e3b0af8ef6f04cbdf0d98)
- [pmu_cycle_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#gac3299a44c61e0d28d974ea6aa2e9ffbc)
- [pmu_start](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga12a5201eb9df8c7f83496847526e63ad)
- [pmu_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga3fa69d6fabe2389dc23ab3b54b72bc6d)
- [pmu_counter_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga35a447da13644c22f4e7148547cbdc9d)
- [pmu_counter_clear_overflow](https://docs.zephyrproject.org/latest/doxygen/html/group__pmu.html#ga29dc5718b7d83eaaf1c52645394394ef)
- [pmu_counter_config::event](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md#a482305d6da6760f7a177a8737f720f88)
- [pmu_counter_config::enabled](../kernel_runtime_model_reference/P013_pmu_counter_config_结构体.md#ab8f9346eec1110d9b45dba5570aef2cd)
- [pmu_info_t::implementer](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md#a20ad7ea312a6f3199078d9cdb7c224f1)
- [pmu_info_t::idcode](../kernel_runtime_model_reference/P014_pmu_info_t_结构体.md#a5b11627370ddcc76202fd7c59f6e7e3d)

---

[上一章](P663_pm_cpu_ops.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P665_poll.h_源码浏览.md)
