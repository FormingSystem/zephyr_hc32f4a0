---
id: learning.zephyr-docs.api-source-configuration-reference.page-41
title: intel_socfpga_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/intel__socfpga__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_intel\_socfpga\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/intel__socfpga__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/intel__socfpga__reset_8h.html)。

## 41.1\_原始可见代码（Source Code）

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
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
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
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>

```c
/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (C) 2023, Intel Corporation
 *
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_INTEL_SOCFPGA_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_INTEL_SOCFPGA_RESET_H_

/* The Reset line value will be used by the reset controller driver to
 * derive the register offset and the associated device bit to perform
 * device assert and de-assert.
 *
 * The reset lines should be passed as a parameter to the resets property
 * of the driver node in dtsi which will call reset-controller driver to
 * assert/de-assert itself.
 *
 * Example: Deriving Reset Line value
 * per0modrst register offset = 0x24;
 * NAND RSTLINE pin = 5;
 * RSTMGR_NAND_RSTLINE = (0x24 * 8) + 5 = 293
 */

#define RSTMGR_SDMCOLDRST_RSTLINE           0
#define RSTMGR_SDMWARMRST_RSTLINE           1
#define RSTMGR_SDMLASTPORRST_RSTLINE        2
#define RSTMGR_L4WD0RST_RSTLINE             16
#define RSTMGR_L4WD1RST_RSTLINE             17
#define RSTMGR_L4WD2RST_RSTLINE             18
#define RSTMGR_L4WD3RST_RSTLINE             19
#define RSTMGR_L4WD4RST_RSTLINE             20
#define RSTMGR_DEBUGRST_RSTLINE             21
#define RSTMGR_CSDAPRST_RSTLINE             22
#define RSTMGR_EMIFTIMEOUT_RSTLINE          64
#define RSTMGR_FPGAHSTIMEOUT_RSTLINE        66
#define RSTMGR_ETRSTALLTIMEOUT_RSTLINE      67
#define RSTMGR_LWSOC2FPGATIMEOUT_RSTLINE    72
#define RSTMGR_SOC2FPGATIMEOUT_RSTLINE      73
#define RSTMGR_F2SDRAMTIMEOUT_RSTLINE       74
#define RSTMGR_F2STIMEOUT_RSTLINE           75
#define RSTMGR_L3NOCDBGTIMEOUT_RSTLINE      79
#define RSTMGR_DEBUGL3NOCTIMEOUT_RSTLINE    80
#define RSTMGR_EMIF_FLUSH_RSTLINE           128
#define RSTMGR_FPGAHSEN_RSTLINE             130
#define RSTMGR_ETRSTALLEN_RSTLINE           131
#define RSTMGR_LWSOC2FPGA_FLUSH_RSTLINE     137
#define RSTMGR_SOC2FPGA_FLUSH_RSTLINE       138
#define RSTMGR_F2SDRAM_FLUSH_RSTLINE        139
#define RSTMGR_F2SOC_FLUSH_RSTLINE          140
#define RSTMGR_L3NOC_DBG_RSTLINE            144
#define RSTMGR_DEBUG_L3NOC_RSTLINE          145
#define RSTMGR_EMIF_FLUSH_REQ_RSTLINE       160
#define RSTMGR_FPGAHSREQ_RSTLINE            162
#define RSTMGR_ETRSTALLREQ_RSTLINE          163
#define RSTMGR_LWSOC2FPGA_FLUSH_REQ_RSTLINE 169
#define RSTMGR_SOC2FPGA_FLUSH_REQ_RSTLINE   170
#define RSTMGR_F2SDRAM_FLUSH_REQ_RSTLINE    171
#define RSTMGR_F2S_FLUSH_REQ_RSTLINE        172
#define RSTMGR_L3NOC_DBG_REQ_RSTLINE        176
#define RSTMGR_DEBUG_L3NOC_REQ_RSTLINE      177
#define RSTMGR_EMIF_FLUSH_ACK_RSTLINE       192
#define RSTMGR_FPGAHSACK_RSTLINE            194
#define RSTMGR_ETRSTALLACK_RSTLINE          195
#define RSTMGR_LWSOC2FPGA_FLUSH_ACK_RSTLINE 201
#define RSTMGR_SOC2FPGA_FLUSH_ACK_RSTLINE   202
#define RSTMGR_F2SDRAM_FLUSH_ACK_RSTLINE    203
#define RSTMGR_F2S_FLUSH_ACK_RSTLINE        204
#define RSTMGR_L3NOC_DBG_ACK_RSTLINE        208
#define RSTMGR_DEBUG_L3NOC_ACK_RSTLINE      209
#define RSTMGR_ETRSTALLWARMRST_RSTLINE      224
#define RSTMGR_TSN0_RSTLINE                 288
#define RSTMGR_TSN1_RSTLINE                 289
#define RSTMGR_TSN2_RSTLINE                 290
#define RSTMGR_USB0_RSTLINE                 291
#define RSTMGR_USB1_RSTLINE                 292
#define RSTMGR_NAND_RSTLINE                 293
#define RSTMGR_SOFTPHY_RSTLINE              294
#define RSTMGR_SDMMC_RSTLINE                295
#define RSTMGR_TSN0ECC_RSTLINE              296
#define RSTMGR_TSN1ECC_RSTLINE              297
#define RSTMGR_TSN2ECC_RSTLINE              298
#define RSTMGR_USB0ECC_RSTLINE              299
#define RSTMGR_USB1ECC_RSTLINE              300
#define RSTMGR_NANDECC_RSTLINE              301
#define RSTMGR_SDMMCECC_RSTLINE             303
#define RSTMGR_DMA_RSTLINE                  304
#define RSTMGR_SPIM0_RSTLINE                305
#define RSTMGR_SPIM1_RSTLINE                306
#define RSTMGR_SPIS0_RSTLINE                307
#define RSTMGR_SPIS1_RSTLINE                308
#define RSTMGR_DMAECC_RSTLINE               309
#define RSTMGR_EMACPTP_RSTLINE              310
#define RSTMGR_DMAIF0_RSTLINE               312
#define RSTMGR_DMAIF1_RSTLINE               313
#define RSTMGR_DMAIF2_RSTLINE               314
#define RSTMGR_DMAIF3_RSTLINE               315
#define RSTMGR_DMAIF4_RSTLINE               316
#define RSTMGR_DMAIF5_RSTLINE               317
#define RSTMGR_DMAIF6_RSTLINE               318
#define RSTMGR_DMAIF7_RSTLINE               319
#define RSTMGR_WATCHDOG0_RSTLINE            320
#define RSTMGR_WATCHDOG1_RSTLINE            321
#define RSTMGR_WATCHDOG2_RSTLINE            322
#define RSTMGR_WATCHDOG3_RSTLINE            323
#define RSTMGR_L4SYSTIMER0_RSTLINE          324
#define RSTMGR_L4SYSTIMER1_RSTLINE          325
#define RSTMGR_SPTIMER0_RSTLINE             326
#define RSTMGR_SPTIMER1_RSTLINE             327
#define RSTMGR_I2C0_RSTLINE                 328
#define RSTMGR_I2C1_RSTLINE                 329
#define RSTMGR_I2C2_RSTLINE                 330
#define RSTMGR_I2C3_RSTLINE                 331
#define RSTMGR_I2C4_RSTLINE                 332
#define RSTMGR_I3C0_RSTLINE                 333
#define RSTMGR_I3C1_RSTLINE                 334
#define RSTMGR_UART0_RSTLINE                336
#define RSTMGR_UART1_RSTLINE                337
#define RSTMGR_GPIO0_RSTLINE                344
#define RSTMGR_GPIO1_RSTLINE                345
#define RSTMGR_WATCHDOG4_RSTLINE            346
#define RSTMGR_SOC2FPGA_RSTLINE             352
#define RSTMGR_LWSOC2FPGA_RSTLINE           353
#define RSTMGR_FPGA2SOC_RSTLINE             354
#define RSTMGR_FPGA2SDRAM_RSTLINE           355
#define RSTMGR_MPFE_RSTLINE                 358
#define RSTMGR_DBG_RST_RSTLINE              480
#define RSTMGR_SOC2FPGA_WARM_RSTLINE        608
#define RSTMGR_LWSOC2FPGA_WARM_RSTLINE      609
#define RSTMGR_FPGA2SOC_WARM_RSTLINE        610
#define RSTMGR_FPGA2SDRAM_WARM_RSTLINE      611
#define RSTMGR_MPFE_WARM_RSTLINE            614

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_INTEL_SOCFPGA_RESET_H_ */
```

## 41.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

版权（Copyright）：© 2023, Intel Corporation。

### 注释 2：原第 11 行

复位控制器驱动使用复位线（Reset line）值推导寄存器偏移量及关联的设备位，以对设备执行复位置位和解除（Assert / de-assert）。

复位线应作为参数传给 DTSI 中驱动节点的 `resets` 属性；该驱动将调用复位控制器驱动，对自身执行复位置位/解除。

复位线值的推导示例：

- `per0modrst` 寄存器偏移量为 `0x24`。
- NAND 的 `RSTLINE` 引脚为 5。
- `RSTMGR_NAND_RSTLINE = (0x24 * 8) + 5 = 293`。

### 注释 3：原第 134 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_INTEL_SOCFPGA_RESET_H_`。

## 41.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/intel__socfpga__reset_8h.html)

---

[上一章](P040_intel-ioapic.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P042_ioapic.h_源码浏览.md)
