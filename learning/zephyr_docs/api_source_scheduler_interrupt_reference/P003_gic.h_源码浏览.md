---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-3
title: gic.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gic_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_gic.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html)。

## 3.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
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
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
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
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
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
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
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
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
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
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
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
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="adevice_8h_html"></a>
<a id="agic_8h_html_a08291705f002f01687cf507abbb410dc"></a>
<a id="agic_8h_html_a2980cdb020c9d8a886bf9d4fd485121b"></a>
<a id="agic_8h_html_a3c2d3adf07e2d48bdf863d8142a685aa"></a>
<a id="agic_8h_html_a3f5ec5c6b16fbac66cd02459d6045742"></a>
<a id="agic_8h_html_a4bfb597ef68cc7f83d86ba52e099e3b4"></a>
<a id="agic_8h_html_a585b5b22a16dab6999ab94dae30f4e71"></a>
<a id="agic_8h_html_a967a15ed8b1eeacde827b5a396867671"></a>
<a id="agic_8h_html_aa9e67bf28cee4b9382ebdc641874d2f8"></a>
<a id="agic_8h_html_acfa77cdcf46cad1181476bc3b974b58e"></a>
<a id="agic_8h_html_ad0cc0929cc6e0336448d45ebd27a45bd"></a>
<a id="agic_8h_html_ad5eb3fc988f7077dc9600e62d768b076"></a>
<a id="agic_8h_html_ae545623722c1b45fda2b58155f3fd0ed"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>

```c
/*
 * Copyright (c) 2019 Stephanos Ioannidis <root@stephanos.io>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GIC_H_
#define ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GIC_H_

/*
 * GIC Register Interface Base Addresses
 */

#define GIC_DIST_BASE DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 0)
#define GIC_CPU_BASE  DT_REG_ADDR_BY_IDX(DT_INST(0, arm_gic), 1)

/*
 * GIC Distributor Interface
 */

/*
 * 0x000  Distributor Control Register
 * v1           ICDDCR
 * v2/v3        GICD_CTLR
 */
#define GICD_CTLR (GIC_DIST_BASE + 0x0)

/*
 * 0x004  Interrupt Controller Type Register
 * v1           ICDICTR
 * v2/v3        GICD_TYPER
 */
#define GICD_TYPER (GIC_DIST_BASE + 0x4)

/*
 * 0x008  Distributor Implementer Identification Register
 * v1           ICDIIDR
 * v2/v3        GICD_IIDR
 */
#define GICD_IIDR (GIC_DIST_BASE + 0x8)

/*
 * 0x080  Interrupt Group Registers
 * v1           ICDISRn
 * v2/v3        GICD_IGROUPRn
 */
#define GICD_IGROUPRn (GIC_DIST_BASE + 0x80)

/*
 * 0x1000  Interrupt Group Registers for Extended SPI Range
 * v3.1         GICD_IGROUPRnE
 */
#define GICD_IGROUPRnE (GIC_DIST_BASE + 0x1000)

/*
 * 0x100  Interrupt Set-Enable Registers
 * v1           ICDISERn
 * v2/v3        GICD_ISENABLERn
 */
#define GICD_ISENABLERn (GIC_DIST_BASE + 0x100)

/*
 * 0x1200  Interrupt Set-Enable Registers for Extended SPI Range
 * v3.1         GICD_ISENABLERnE
 */
#define GICD_ISENABLERnE (GIC_DIST_BASE + 0x1200)

/*
 * 0x180  Interrupt Clear-Enable Registers
 * v1           ICDICERn
 * v2/v3        GICD_ICENABLERn
 */
#define GICD_ICENABLERn (GIC_DIST_BASE + 0x180)

/*
 * 0x1400  Interrupt Clear-Enable Registers for Extended SPI Range
 * v3.1         GICD_ICENABLERnE
 */
#define GICD_ICENABLERnE (GIC_DIST_BASE + 0x1400)

/*
 * 0x200  Interrupt Set-Pending Registers
 * v1           ICDISPRn
 * v2/v3        GICD_ISPENDRn
 */
#define GICD_ISPENDRn (GIC_DIST_BASE + 0x200)

/*
 * 1600  Interrupt Set-Pending Registers for Extended SPI Range
 * v3.1         GICD_ISPENDRnE
 */
#define GICD_ISPENDRnE (GIC_DIST_BASE + 0x1600)

/*
 * 0x280  Interrupt Clear-Pending Registers
 * v1           ICDICPRn
 * v2/v3        GICD_ICPENDRn
 */
#define GICD_ICPENDRn (GIC_DIST_BASE + 0x280)

/*
 * 0x1800  Interrupt Clear-Pending Registers for Extended SPI Range
 * v3.1         GICD_ICPENDRnE
 */
#define GICD_ICPENDRnE (GIC_DIST_BASE + 0x1800)

/*
 * 0x300  Interrupt Set-Active Registers
 * v1           ICDABRn
 * v2/v3        GICD_ISACTIVERn
 */
#define GICD_ISACTIVERn (GIC_DIST_BASE + 0x300)

/*
 * 0x1A00  Interrupt Set-Active Registers for Extended SPI Range
 * v3.1         GICD_ISACTIVERnE
 */
#define GICD_ISACTIVERnE (GIC_DIST_BASE + 0x1A00)

#if CONFIG_GIC_VER >= 2
/*
 * 0x380  Interrupt Clear-Active Registers
 * v2/v3        GICD_ICACTIVERn
 */
#define GICD_ICACTIVERn (GIC_DIST_BASE + 0x380)

/*
 * 0x1C00  Interrupt Clear-Active Registers for Extended SPI Range
 * v3.1         GICD_ICACTIVERnE
 */
#define GICD_ICACTIVERnE (GIC_DIST_BASE + 0x1C00)
#endif

/*
 * 0x400  Interrupt Priority Registers
 * v1           ICDIPRn
 * v2/v3        GICD_IPRIORITYRn
 */
#define GICD_IPRIORITYRn (GIC_DIST_BASE + 0x400)

/*
 * 0x2000  Interrupt Priority Registers for Extended SPI Range
 * v3.1         GICD_IPRIORITYRnE
 */
#define GICD_IPRIORITYRnE (GIC_DIST_BASE + 0x2000)

/*
 * 0x800  Interrupt Processor Targets Registers
 * v1           ICDIPTRn
 * v2/v3        GICD_ITARGETSRn
 */
#define GICD_ITARGETSRn (GIC_DIST_BASE + 0x800)

/*
 * 0xC00  Interrupt Configuration Registers
 * v1           ICDICRn
 * v2/v3        GICD_ICFGRn
 */
#define GICD_ICFGRn (GIC_DIST_BASE + 0xc00)

/*
 * 0x3000  Interrupt Configuration Registers for Extended SPI Range
 * v3.1         GICD_ICFGRnE
 */
#define GICD_ICFGRnE (GIC_DIST_BASE + 0x3000)

/*
 * 0xF00  Software Generated Interrupt Register
 * v1           ICDSGIR
 * v2/v3        GICD_SGIR
 */
#define GICD_SGIR (GIC_DIST_BASE + 0xf00)

/*
 * GIC CPU Interface
 */

#if CONFIG_GIC_VER <= 2

/*
 * 0x0000  CPU Interface Control Register
 * v1           ICCICR
 * v2/v3        GICC_CTLR
 */
#define GICC_CTLR (GIC_CPU_BASE + 0x0)

/*
 * 0x0004  Interrupt Priority Mask Register
 * v1           ICCPMR
 * v2/v3        GICC_PMR
 */
#define GICC_PMR (GIC_CPU_BASE + 0x4)

/*
 * 0x0008  Binary Point Register
 * v1           ICCBPR
 * v2/v3        GICC_BPR
 */
#define GICC_BPR (GIC_CPU_BASE + 0x8)

/*
 * 0x000C  Interrupt Acknowledge Register
 * v1           ICCIAR
 * v2/v3        GICC_IAR
 */
#define GICC_IAR (GIC_CPU_BASE + 0xc)

/*
 * 0x0010  End of Interrupt Register
 * v1           ICCEOIR
 * v2/v3        GICC_EOIR
 */
#define GICC_EOIR (GIC_CPU_BASE + 0x10)

/*
 * Helper Constants
 */

/* GICC_CTLR */
#define GICC_CTLR_ENABLEGRP0 BIT(0)
#define GICC_CTLR_ENABLEGRP1 BIT(1)

#define GICC_CTLR_ENABLE_MASK (GICC_CTLR_ENABLEGRP0 | GICC_CTLR_ENABLEGRP1)

#if defined(CONFIG_GIC_V2)

#define GICC_CTLR_FIQBYPDISGRP0 BIT(5)
#define GICC_CTLR_IRQBYPDISGRP0 BIT(6)
#define GICC_CTLR_FIQBYPDISGRP1 BIT(7)
#define GICC_CTLR_IRQBYPDISGRP1 BIT(8)

#define GICC_CTLR_BYPASS_MASK                                                                      \
        (GICC_CTLR_FIQBYPDISGRP0 | GICC_CTLR_IRQBYPDISGRP1 | GICC_CTLR_FIQBYPDISGRP1 |             \
         GICC_CTLR_IRQBYPDISGRP1)

#endif /* CONFIG_GIC_V2 */

/* GICD_SGIR */
#define GICD_SGIR_TGTFILT(x)        ((x) << 24)
#define GICD_SGIR_TGTFILT_CPULIST   GICD_SGIR_TGTFILT(0b00)
#define GICD_SGIR_TGTFILT_ALLBUTREQ GICD_SGIR_TGTFILT(0b01)
#define GICD_SGIR_TGTFILT_REQONLY   GICD_SGIR_TGTFILT(0b10)

#define GICD_SGIR_CPULIST(x)     ((x) << 16)
#define GICD_SGIR_CPULIST_CPU(n) GICD_SGIR_CPULIST(BIT(n))
#define GICD_SGIR_CPULIST_MASK   0xff

#define GICD_SGIR_NSATT BIT(15)

#define GICD_SGIR_SGIINTID(x) (x)

#endif /* CONFIG_GIC_VER <= 2 */

#define GICD_CTLR_DS BIT(6)

/* GICD_ICFGR */
#define GICD_ICFGR_MASK BIT_MASK(2)
#define GICD_ICFGR_TYPE BIT(1)

/* GICD_TYPER.ITLinesNumber 0:4 */
#define GICD_TYPER_ITLINESNUM_MASK 0x1f

/* GICD_TYPER.ESPI [8] */
#define GICD_TYPER_ESPI_MASK BIT(8)

/* GICD_TYPER.IDbits */
#define GICD_TYPER_IDBITS(typer) ((((typer) >> 19) & 0x1f) + 1)

/*
 * Common Helper Constants
 */
#define GIC_SGI_INT_BASE 0
#define GIC_PPI_INT_BASE 16

#define GIC_IS_SGI(intid) (((intid) >= GIC_SGI_INT_BASE) && ((intid) < GIC_PPI_INT_BASE))

#define GIC_SPI_INT_BASE 32

#define GIC_SPI_MAX_INTID 1019

#define GIC_IS_SPI(intid) (((intid) >= GIC_SPI_INT_BASE) && ((intid) <= GIC_SPI_MAX_INTID))

#define GIC_NUM_INTR_PER_REG 32

#define GIC_NUM_CFG_PER_REG 16

#define GIC_NUM_PRI_PER_REG 4

/* GIC idle priority : value '0xff' will allow all interrupts */
#define GIC_IDLE_PRIO 0xff

/* Priority levels 0:255 */
#define GIC_PRI_MASK 0xff

/*
 * '0xa0'is used to initialize each interrupt default priority.
 * This is an arbitrary value in current context.
 * Any value '0x80' to '0xff' will work for both NS and S state.
 * The values of individual interrupt and default has to be chosen
 * carefully if PMR and BPR based nesting and preemption has to be done.
 */
#define GIC_INT_DEF_PRI_X4 0xa0a0a0a0

/* GIC special interrupt id */
#define GIC_INTID_SPURIOUS 1023

#define GIC_NUM_CPU_IF CONFIG_MP_MAX_NUM_CPUS

#ifndef _ASMLANGUAGE

#include <zephyr/types.h>
#include <zephyr/device.h>

/*
 * GIC Driver Interface Functions
 */

void arm_gic_irq_enable(unsigned int irq);

void arm_gic_irq_disable(unsigned int irq);

bool arm_gic_irq_is_enabled(unsigned int irq);

bool arm_gic_irq_is_pending(unsigned int irq);

void arm_gic_irq_set_pending(unsigned int irq);

void arm_gic_irq_clear_pending(unsigned int irq);

void arm_gic_irq_set_priority(unsigned int irq, unsigned int prio, unsigned int flags);

void arm_gic_irq_set_affinity(unsigned int irq, uint64_t mpidr);

unsigned int arm_gic_get_active(void);

void arm_gic_eoi(unsigned int irq);

#ifdef CONFIG_SMP
void arm_gic_secondary_init(void);
#endif

void gic_raise_sgi(unsigned int sgi_id, uint64_t target_aff, uint16_t target_list);

#endif /* !_ASMLANGUAGE */

#endif /* ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GIC_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Stephanos Ioannidis <root@stephanos.io>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

通用中断控制器（GIC）寄存器接口基地址（Register Interface Base Addresses）。

### 注释 3：原第 26 行

通用中断控制器分发器接口（GIC Distributor Interface）。

### 注释 4：原第 30 行

偏移 `0x000`：分发器控制寄存器（Distributor Control Register）。

版本对应的寄存器名称如下：

```text
v1           ICDDCR
v2/v3        GICD_CTLR
```

### 注释 5：原第 37 行

偏移 `0x004`：中断控制器类型寄存器（Interrupt Controller Type Register）。

版本对应的寄存器名称如下：

```text
v1           ICDICTR
v2/v3        GICD_TYPER
```

### 注释 6：原第 44 行

偏移 `0x008`：分发器实现者标识寄存器（Distributor Implementer Identification Register）。

版本对应的寄存器名称如下：

```text
v1           ICDIIDR
v2/v3        GICD_IIDR
```

### 注释 7：原第 51 行

偏移 `0x080`：中断分组寄存器（Interrupt Group Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDISRn
v2/v3        GICD_IGROUPRn
```

### 注释 8：原第 58 行

偏移 `0x1000`：扩展共享外设中断（Extended SPI）范围的中断分组寄存器（Interrupt Group Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_IGROUPRnE
```

### 注释 9：原第 64 行

偏移 `0x100`：中断置位使能寄存器（Interrupt Set-Enable Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDISERn
v2/v3        GICD_ISENABLERn
```

### 注释 10：原第 71 行

偏移 `0x1200`：扩展共享外设中断（Extended SPI）范围的中断置位使能寄存器（Interrupt Set-Enable Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ISENABLERnE
```

### 注释 11：原第 77 行

偏移 `0x180`：中断清除使能寄存器（Interrupt Clear-Enable Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDICERn
v2/v3        GICD_ICENABLERn
```

### 注释 12：原第 84 行

偏移 `0x1400`：扩展共享外设中断（Extended SPI）范围的中断清除使能寄存器（Interrupt Clear-Enable Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ICENABLERnE
```

### 注释 13：原第 90 行

偏移 `0x200`：中断挂起置位寄存器（Interrupt Set-Pending Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDISPRn
v2/v3        GICD_ISPENDRn
```

### 注释 14：原第 97 行

偏移 `1600`：扩展共享外设中断（Extended SPI）范围的中断挂起置位寄存器（Interrupt Set-Pending Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ISPENDRnE
```

### 注释 15：原第 103 行

偏移 `0x280`：中断挂起清除寄存器（Interrupt Clear-Pending Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDICPRn
v2/v3        GICD_ICPENDRn
```

### 注释 16：原第 110 行

偏移 `0x1800`：扩展共享外设中断（Extended SPI）范围的中断挂起清除寄存器（Interrupt Clear-Pending Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ICPENDRnE
```

### 注释 17：原第 116 行

偏移 `0x300`：中断活动置位寄存器（Interrupt Set-Active Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDABRn
v2/v3        GICD_ISACTIVERn
```

### 注释 18：原第 123 行

偏移 `0x1A00`：扩展共享外设中断（Extended SPI）范围的中断活动置位寄存器（Interrupt Set-Active Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ISACTIVERnE
```

### 注释 19：原第 130 行

偏移 `0x380`：中断活动清除寄存器（Interrupt Clear-Active Registers）。

版本对应的寄存器名称如下：

```text
v2/v3        GICD_ICACTIVERn
```

### 注释 20：原第 136 行

偏移 `0x1C00`：扩展共享外设中断（Extended SPI）范围的中断活动清除寄存器（Interrupt Clear-Active Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ICACTIVERnE
```

### 注释 21：原第 143 行

偏移 `0x400`：中断优先级寄存器（Interrupt Priority Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDIPRn
v2/v3        GICD_IPRIORITYRn
```

### 注释 22：原第 150 行

偏移 `0x2000`：扩展共享外设中断（Extended SPI）范围的中断优先级寄存器（Interrupt Priority Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_IPRIORITYRnE
```

### 注释 23：原第 156 行

偏移 `0x800`：中断目标处理器寄存器（Interrupt Processor Targets Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDIPTRn
v2/v3        GICD_ITARGETSRn
```

### 注释 24：原第 163 行

偏移 `0xC00`：中断配置寄存器（Interrupt Configuration Registers）。

版本对应的寄存器名称如下：

```text
v1           ICDICRn
v2/v3        GICD_ICFGRn
```

### 注释 25：原第 170 行

偏移 `0x3000`：扩展共享外设中断（Extended SPI）范围的中断配置寄存器（Interrupt Configuration Registers for Extended SPI Range）。

版本对应的寄存器名称如下：

```text
v3.1         GICD_ICFGRnE
```

### 注释 26：原第 176 行

偏移 `0xF00`：软件生成中断寄存器（Software Generated Interrupt Register）。

版本对应的寄存器名称如下：

```text
v1           ICDSGIR
v2/v3        GICD_SGIR
```

### 注释 27：原第 183 行

通用中断控制器 CPU 接口（GIC CPU Interface）。

### 注释 28：原第 189 行

偏移 `0x0000`：CPU 接口控制寄存器（CPU Interface Control Register）。

版本对应的寄存器名称如下：

```text
v1           ICCICR
v2/v3        GICC_CTLR
```

### 注释 29：原第 196 行

偏移 `0x0004`：中断优先级屏蔽寄存器（Interrupt Priority Mask Register）。

版本对应的寄存器名称如下：

```text
v1           ICCPMR
v2/v3        GICC_PMR
```

### 注释 30：原第 203 行

偏移 `0x0008`：二进制分点寄存器（Binary Point Register）。

版本对应的寄存器名称如下：

```text
v1           ICCBPR
v2/v3        GICC_BPR
```

### 注释 31：原第 210 行

偏移 `0x000C`：中断确认寄存器（Interrupt Acknowledge Register）。

版本对应的寄存器名称如下：

```text
v1           ICCIAR
v2/v3        GICC_IAR
```

### 注释 32：原第 217 行

偏移 `0x0010`：中断结束寄存器（End of Interrupt Register）。

版本对应的寄存器名称如下：

```text
v1           ICCEOIR
v2/v3        GICC_EOIR
```

### 注释 33：原第 224 行

辅助常量（Helper Constants）。

### 注释 34：原第 228 行

`GICC_CTLR` 寄存器。

### 注释 35：原第 245 行

条件编译配置（Configuration）标记：`CONFIG_GIC_V2`。

### 注释 36：原第 247 行

`GICD_SGIR` 寄存器。

### 注释 37：原第 261 行

条件编译标记：`CONFIG_GIC_VER <= 2`。

### 注释 38：原第 269 行

`GICD_ICFGR` 寄存器。

### 注释 39：原第 273 行

`GICD_TYPER.ITLinesNumber` 字段，位范围为 `0:4`。

### 注释 40：原第 276 行

`GICD_TYPER.ESPI` 字段，位位置为 `[8]`。

### 注释 41：原第 279 行

`GICD_TYPER.IDbits` 字段。

### 注释 42：原第 282 行

通用辅助常量（Common Helper Constants）。

### 注释 43：原第 302 行

GIC 空闲优先级（Idle Priority）：值 `0xff` 将允许所有中断。

### 注释 44：原第 305 行

优先级范围（Priority Levels）：`0:255`。

### 注释 45：原第 308 行

使用 `0xa0` 初始化各中断的默认优先级，这只是当前上下文中任意选定的值。`0x80` 到 `0xff` 中任意值均适用于非安全（NS）和安全（S）状态。若要基于优先级屏蔽寄存器（PMR）和二进制分点寄存器（BPR）实现嵌套与抢占（Nesting and Preemption），必须谨慎选择各中断优先级及默认优先级。

### 注释 46：原第 317 行

GIC 特殊中断标识（Special Interrupt ID）。

### 注释 47：原第 333 行

GIC 驱动接口函数（Driver Interface Functions）。

### 注释 48：原第 446 行

条件编译表达式：`!_ASMLANGUAGE`。

### 注释 49：原第 448 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_INTERRUPT_CONTROLLER_GIC_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html)
- [zephyr/types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [arm_gic_irq_enable](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a585b5b22a16dab6999ab94dae30f4e71)
- [arm_gic_irq_disable](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a3f5ec5c6b16fbac66cd02459d6045742)
- [arm_gic_irq_is_enabled](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#acfa77cdcf46cad1181476bc3b974b58e)
- [arm_gic_irq_is_pending](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#ad0cc0929cc6e0336448d45ebd27a45bd)
- [arm_gic_irq_set_pending](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#aa9e67bf28cee4b9382ebdc641874d2f8)
- [arm_gic_irq_clear_pending](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a2980cdb020c9d8a886bf9d4fd485121b)
- [arm_gic_irq_set_priority](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#ad5eb3fc988f7077dc9600e62d768b076)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [arm_gic_irq_set_affinity](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a967a15ed8b1eeacde827b5a396867671)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [arm_gic_get_active](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#ae545623722c1b45fda2b58155f3fd0ed)
- [arm_gic_eoi](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a4bfb597ef68cc7f83d86ba52e099e3b4)
- [arm_gic_secondary_init](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a3c2d3adf07e2d48bdf863d8142a685aa)
- [gic_raise_sgi](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a08291705f002f01687cf507abbb410dc)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](../api_file_reference/P160_zephyr__types.h_文件参考.md)

---

[上一章](P002_esp-esp32c6-intmux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_kernel_structs.h_源码浏览.md)
