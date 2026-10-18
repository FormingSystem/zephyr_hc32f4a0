---
id: learning.zephyr-docs.api-source-reference.page-219
title: edac_mcux_erm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/edac__mcux__erm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第219章\_edac\_mcux\_erm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/edac__mcux__erm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/edac__mcux__erm_8h.html)。

## 219.1\_原始可见代码（Source Code）

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
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructedac__nxp__callback__data_html"></a>
<a id="astructedac__nxp__callback__data_html_a505938240dd1ade2aa7d7a62176c6ab2"></a>
<a id="astructedac__nxp__callback__data_html_a50766299a1d828d69c185ebe713b7167"></a>
<a id="astructedac__nxp__callback__data_html_a86b3ffc195ea995856b9ab1369696084"></a>
<a id="astructedac__nxp__callback__data_html_ac6c51cd937e68365c03bf9adc0d812d9"></a>

```c
/*
 * Copyright 2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_EDAC_NXP_ERM_H_
#define ZEPHYR_DRIVERS_EDAC_NXP_ERM_H_


struct edac_nxp_callback_data {
        uint8_t corr_err_count;
        uint8_t err_syndrome;
        uint32_t err_addr;
        uint32_t err_status;
};


#endif /* ZEPHYR_DRIVERS_EDAC_NXP_ERM_H_ */
```

## 219.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 37 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_EDAC_NXP_ERM_H_`。

## 219.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/edac__mcux__erm_8h.html)
- [edac_nxp_callback_data](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [corr_err_count](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#ac6c51cd937e68365c03bf9adc0d812d9)
- [err_syndrome](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a50766299a1d828d69c185ebe713b7167)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [err_addr](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a505938240dd1ade2aa7d7a62176c6ab2)
- [err_status](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a86b3ffc195ea995856b9ab1369696084)
- [edac_nxp_callback_data::err_addr](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a505938240dd1ade2aa7d7a62176c6ab2)
- [edac_nxp_callback_data::err_syndrome](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a50766299a1d828d69c185ebe713b7167)
- [edac_nxp_callback_data::err_status](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#a86b3ffc195ea995856b9ab1369696084)
- [edac_nxp_callback_data::corr_err_count](../platform_security_model_reference/P003_edac_nxp_callback_data_结构体.md#ac6c51cd937e68365c03bf9adc0d812d9)

---

[上一章](P218_ed2208-gca.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P220_edac_synopsys.h_源码浏览.md)
