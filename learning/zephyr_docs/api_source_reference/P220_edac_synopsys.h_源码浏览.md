---
id: learning.zephyr-docs.api-source-reference.page-220
title: edac_synopsys.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/edac__synopsys_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第220章\_edac\_synopsys.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/edac__synopsys_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/edac__synopsys_8h.html)。

## 220.1\_原始可见代码（Source Code）

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
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructedac__synopsys__callback__data_html"></a>
<a id="astructedac__synopsys__callback__data_html_a07c6bd60a094e5b807df0bf823959a3e"></a>
<a id="astructedac__synopsys__callback__data_html_a10387f0ff6db7c6a116a8ccb2ba3e7c0"></a>
<a id="astructedac__synopsys__callback__data_html_a17fee6074688540133b07fb0d567857a"></a>
<a id="astructedac__synopsys__callback__data_html_a36d022f0de8a63581a4a2a95d923e041"></a>
<a id="astructedac__synopsys__callback__data_html_a3c05b263247c78ac195760f6a73a30b8"></a>
<a id="astructedac__synopsys__callback__data_html_a659a7a12f24337cc57ea121e06cbd20c"></a>
<a id="astructedac__synopsys__callback__data_html_a71c5e4b31f16927b483e7bd3bf8b6f32"></a>
<a id="astructedac__synopsys__callback__data_html_a73567e401a706bbf392db489afd72012"></a>
<a id="astructedac__synopsys__callback__data_html_a749fb5929f89a63cb62fd76f4c143dba"></a>
<a id="astructedac__synopsys__callback__data_html_a8df3545fd3f7dfa8a99dcac90e708ec2"></a>
<a id="astructedac__synopsys__callback__data_html_a99670584c0c09eaf2e14e6e797ec834d"></a>
<a id="astructedac__synopsys__callback__data_html_aa34f78372e80c57772ea864827a5abe1"></a>
<a id="astructedac__synopsys__callback__data_html_aa549050b7305f4e8bb15f5b849bec165"></a>
<a id="astructedac__synopsys__callback__data_html_aca79f779ac263e5344dad5e12ee6d3da"></a>
<a id="astructedac__synopsys__callback__data_html_ae6a6c090671e5bfda93b904ee9e95a2b"></a>
<a id="astructedac__synopsys__callback__data_html_aece294a29dbd98a3e75f4cfb6c9c79c3"></a>
<a id="astructedac__synopsys__callback__data_html_af148757e829b0e0bfbf575521131f54b"></a>
<a id="astructedac__synopsys__callback__data_html_af23d5d538b8ebe722838a186c6b30909"></a>

```c
/*
 * Copyright (c) 2025 Calian Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_EDAC_EDAC_SYNOPSYS_H_
#define ZEPHYR_DRIVERS_EDAC_EDAC_SYNOPSYS_H_


#include <stdint.h>

struct edac_synopsys_callback_data {
        uint16_t corr_err_count;
        uint8_t corr_err_rank;
        uint8_t corr_err_bg;
        uint8_t corr_err_bank;
        uint32_t corr_err_row;
        uint8_t corr_err_col;
        uint64_t corr_err_syndrome;
        uint8_t corr_err_syndrome_ecc;
        uint64_t corr_err_bitmask;
        uint8_t corr_err_bitmask_ecc;

        uint16_t uncorr_err_count;
        uint8_t uncorr_err_rank;
        uint8_t uncorr_err_bg;
        uint8_t uncorr_err_bank;
        uint32_t uncorr_err_row;
        uint8_t uncorr_err_col;
        uint64_t uncorr_err_syndrome;
        uint8_t uncorr_err_syndrome_ecc;
};


#endif /* ZEPHYR_DRIVERS_EDAC_EDAC_SYNOPSYS_H_ */
```

## 220.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Calian Ltd。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 68 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_EDAC_EDAC_SYNOPSYS_H_`。

## 220.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/edac__synopsys_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [edac_synopsys_callback_data](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [corr_err_count](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a71c5e4b31f16927b483e7bd3bf8b6f32)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [corr_err_rank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aece294a29dbd98a3e75f4cfb6c9c79c3)
- [corr_err_bg](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#ae6a6c090671e5bfda93b904ee9e95a2b)
- [corr_err_bank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a749fb5929f89a63cb62fd76f4c143dba)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [corr_err_row](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aa549050b7305f4e8bb15f5b849bec165)
- [corr_err_col](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#af23d5d538b8ebe722838a186c6b30909)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [corr_err_syndrome](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aca79f779ac263e5344dad5e12ee6d3da)
- [corr_err_syndrome_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a73567e401a706bbf392db489afd72012)
- [corr_err_bitmask](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a10387f0ff6db7c6a116a8ccb2ba3e7c0)
- [corr_err_bitmask_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a659a7a12f24337cc57ea121e06cbd20c)
- [uncorr_err_count](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aa34f78372e80c57772ea864827a5abe1)
- [uncorr_err_rank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a07c6bd60a094e5b807df0bf823959a3e)
- [uncorr_err_bg](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#af148757e829b0e0bfbf575521131f54b)
- [uncorr_err_bank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a8df3545fd3f7dfa8a99dcac90e708ec2)
- [uncorr_err_row](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a99670584c0c09eaf2e14e6e797ec834d)
- [uncorr_err_col](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a17fee6074688540133b07fb0d567857a)
- [uncorr_err_syndrome](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a3c05b263247c78ac195760f6a73a30b8)
- [uncorr_err_syndrome_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a36d022f0de8a63581a4a2a95d923e041)
- [edac_synopsys_callback_data::uncorr_err_rank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a07c6bd60a094e5b807df0bf823959a3e)
- [edac_synopsys_callback_data::corr_err_bitmask](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a10387f0ff6db7c6a116a8ccb2ba3e7c0)
- [edac_synopsys_callback_data::uncorr_err_col](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a17fee6074688540133b07fb0d567857a)
- [edac_synopsys_callback_data::uncorr_err_syndrome_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a36d022f0de8a63581a4a2a95d923e041)
- [edac_synopsys_callback_data::uncorr_err_syndrome](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a3c05b263247c78ac195760f6a73a30b8)
- [edac_synopsys_callback_data::corr_err_bitmask_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a659a7a12f24337cc57ea121e06cbd20c)
- [edac_synopsys_callback_data::corr_err_count](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a71c5e4b31f16927b483e7bd3bf8b6f32)
- [edac_synopsys_callback_data::corr_err_syndrome_ecc](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a73567e401a706bbf392db489afd72012)
- [edac_synopsys_callback_data::corr_err_bank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a749fb5929f89a63cb62fd76f4c143dba)
- [edac_synopsys_callback_data::uncorr_err_bank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a8df3545fd3f7dfa8a99dcac90e708ec2)
- [edac_synopsys_callback_data::uncorr_err_row](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#a99670584c0c09eaf2e14e6e797ec834d)
- [edac_synopsys_callback_data::uncorr_err_count](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aa34f78372e80c57772ea864827a5abe1)
- [edac_synopsys_callback_data::corr_err_row](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aa549050b7305f4e8bb15f5b849bec165)
- [edac_synopsys_callback_data::corr_err_syndrome](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aca79f779ac263e5344dad5e12ee6d3da)
- [edac_synopsys_callback_data::corr_err_bg](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#ae6a6c090671e5bfda93b904ee9e95a2b)
- [edac_synopsys_callback_data::corr_err_rank](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#aece294a29dbd98a3e75f4cfb6c9c79c3)
- [edac_synopsys_callback_data::uncorr_err_bg](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#af148757e829b0e0bfbf575521131f54b)
- [edac_synopsys_callback_data::corr_err_col](../platform_security_model_reference/P004_edac_synopsys_callback_data_结构体.md#af23d5d538b8ebe722838a186c6b30909)

---

[上一章](P219_edac_mcux_erm.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P221_elf.h_源码浏览.md)
