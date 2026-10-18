---
id: learning.zephyr-docs.api-source-supplement-reference.page-122
title: mtk_mt8188_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mtk__mt8188__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第122章\_mtk\_mt8188\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mtk__mt8188__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mtk__mt8188__clock_8h.html)。

## 122.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
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
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
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
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>

```c
/*
 * Copyright (c) 2026 MediaTek Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MTK_MT8188_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MTK_MT8188_CLOCK_H_

/* INFRACFG_AO */
#define CLK_INFRA_AO_PMIC_TMR             0
#define CLK_INFRA_AO_PMIC_AP              1
#define CLK_INFRA_AO_PMIC_MD              2
#define CLK_INFRA_AO_PMIC_CONN            3
#define CLK_INFRA_AO_SEJ                  4
#define CLK_INFRA_AO_APXGPT               5
#define CLK_INFRA_AO_GCE                  6
#define CLK_INFRA_AO_GCE2                 7
#define CLK_INFRA_AO_THERM                8
#define CLK_INFRA_AO_PWM_HCLK             9
#define CLK_INFRA_AO_PWM1                 10
#define CLK_INFRA_AO_PWM2                 11
#define CLK_INFRA_AO_PWM3                 12
#define CLK_INFRA_AO_PWM4                 13
#define CLK_INFRA_AO_PWM                  14
#define CLK_INFRA_AO_UART0                15
#define CLK_INFRA_AO_UART1                16
#define CLK_INFRA_AO_UART2                17
#define CLK_INFRA_AO_UART3                18
#define CLK_INFRA_AO_UART4                19
#define CLK_INFRA_AO_GCE_26M              20
#define CLK_INFRA_AO_CQ_DMA_FPC           21
#define CLK_INFRA_AO_UART5                22
#define CLK_INFRA_AO_HDMI_26M             23
#define CLK_INFRA_AO_SPI0                 24
#define CLK_INFRA_AO_MSDC0                25
#define CLK_INFRA_AO_MSDC1                26
#define CLK_INFRA_AO_MSDC2                27
#define CLK_INFRA_AO_MSDC0_SRC            28
#define CLK_INFRA_AO_DVFSRC               29
#define CLK_INFRA_AO_TRNG                 30
#define CLK_INFRA_AO_AUXADC               31
#define CLK_INFRA_AO_CPUM                 32
#define CLK_INFRA_AO_HDMI_32K             33
#define CLK_INFRA_AO_CEC_66M_HCLK         34
#define CLK_INFRA_AO_PCIE_TL_26M          35
#define CLK_INFRA_AO_MSDC1_SRC            36
#define CLK_INFRA_AO_CEC_66M_BCLK         37
#define CLK_INFRA_AO_PCIE_TL_96M          38
#define CLK_INFRA_AO_DEVICE_APC           39
#define CLK_INFRA_AO_ECC_66M_HCLK         40
#define CLK_INFRA_AO_DEBUGSYS             41
#define CLK_INFRA_AO_AUDIO                42
#define CLK_INFRA_AO_PCIE_TL_32K          43
#define CLK_INFRA_AO_DBG_TRACE            44
#define CLK_INFRA_AO_DRAMC_F26M           45
#define CLK_INFRA_AO_IRTX                 46
#define CLK_INFRA_AO_DISP_PWM             47
#define CLK_INFRA_AO_CLDMA_BCLK           48
#define CLK_INFRA_AO_AUDIO_26M_BCLK       49
#define CLK_INFRA_AO_SPI1                 50
#define CLK_INFRA_AO_SPI2                 51
#define CLK_INFRA_AO_SPI3                 52
#define CLK_INFRA_AO_FSSPM                53
#define CLK_INFRA_AO_SSPM_BUS_HCLK        54
#define CLK_INFRA_AO_APDMA_BCLK           55
#define CLK_INFRA_AO_SPI4                 56
#define CLK_INFRA_AO_SPI5                 57
#define CLK_INFRA_AO_CQ_DMA               58
#define CLK_INFRA_AO_MSDC0_SELF           59
#define CLK_INFRA_AO_MSDC1_SELF           60
#define CLK_INFRA_AO_MSDC2_SELF           61
#define CLK_INFRA_AO_I2S_DMA              62
#define CLK_INFRA_AO_AP_MSDC0             63
#define CLK_INFRA_AO_MD_MSDC0             64
#define CLK_INFRA_AO_MSDC30_2             65
#define CLK_INFRA_AO_GCPU                 66
#define CLK_INFRA_AO_PCIE_PERI_26M        67
#define CLK_INFRA_AO_GCPU_66M_BCLK        68
#define CLK_INFRA_AO_GCPU_133M_BCLK       69
#define CLK_INFRA_AO_DISP_PWM1            70
#define CLK_INFRA_AO_FBIST2FPC            71
#define CLK_INFRA_AO_DEVICE_APC_SYNC      72
#define CLK_INFRA_AO_PCIE_P1_PERI_26M     73
#define CLK_INFRA_AO_133M_MCLK_CK         74
#define CLK_INFRA_AO_66M_MCLK_CK          75
#define CLK_INFRA_AO_PCIE_PL_P_250M_P0    76
#define CLK_INFRA_AO_RG_AES_MSDCFDE_CK_0P 77
#define CLK_INFRA_AO_NR_CLK               78

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MTK_MT8188_CLOCK_H_ */
```

## 122.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 MediaTek Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

`INFRACFG_AO` 标记。

### 注释 3：原第 91 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MTK_MT8188_CLOCK_H_`。

## 122.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mtk__mt8188__clock_8h.html)

---

[上一章](P121_mtk-common-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P123_net_config.h_源码浏览.md)
