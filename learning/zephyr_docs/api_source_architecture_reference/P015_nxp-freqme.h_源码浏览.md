---
id: learning.zephyr-docs.api-source-architecture-reference.page-15
title: nxp-freqme.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_nxp-freqme.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h.html)。

## 15.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00025"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
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
<a id="l00156"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00161"></a>
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

```c
/*
 * SPDX-FileCopyrightText: 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FREQME_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FREQME_H_


#define NXP_FREQME_PMUX_SHIFT 20

#define NXP_FREQME_SOURCE_UNCHANGED 0U

/*
 * MCX families with separate FREQMEAS_REF (0x180) / FREQMEAS_TAR (0x184) mux
 * registers. MCXA, MCXC, MCXN, MCXL and MCXW all share this register layout;
 * only the per-source selector numbers differ, so each family has its own
 * cookie set below.
 */

#define NXP_FREQME_REF_REG 0x180
#define NXP_FREQME_TAR_REG 0x184

#define NXP_FREQME_REF(sel) ((sel) + (NXP_FREQME_REF_REG << NXP_FREQME_PMUX_SHIFT))
#define NXP_FREQME_TAR(sel) ((sel) + (NXP_FREQME_TAR_REG << NXP_FREQME_PMUX_SHIFT))

/*
 * MCXA selectors.
 * Devices: MCXA153, MCXA156, MCXA174, MCXA266, MCXA344, MCXA346, MCXA577 and
 *          MCXC162 (identical selector numbering).
 */
#define NXP_FREQME_REF_CLK_IN      NXP_FREQME_REF(1)
#define NXP_FREQME_REF_FRO_12M     NXP_FREQME_REF(2)
#define NXP_FREQME_REF_FRO_HF_DIV  NXP_FREQME_REF(3)
#define NXP_FREQME_REF_CLK_16K1    NXP_FREQME_REF(5)
#define NXP_FREQME_REF_SLOW_CLK    NXP_FREQME_REF(6)
#define NXP_FREQME_REF_CLK_IN0     NXP_FREQME_REF(7)
#define NXP_FREQME_REF_CLK_IN1     NXP_FREQME_REF(8)

#define NXP_FREQME_TAR_CLK_IN      NXP_FREQME_TAR(1)
#define NXP_FREQME_TAR_FRO_12M     NXP_FREQME_TAR(2)
#define NXP_FREQME_TAR_FRO_HF_DIV  NXP_FREQME_TAR(3)
#define NXP_FREQME_TAR_CLK_16K1    NXP_FREQME_TAR(5)
#define NXP_FREQME_TAR_SLOW_CLK    NXP_FREQME_TAR(6)
#define NXP_FREQME_TAR_CLK_IN0     NXP_FREQME_TAR(7)
#define NXP_FREQME_TAR_CLK_IN1     NXP_FREQME_TAR(8)

/*
 * MCXN selectors.
 * Devices: MCXN236, MCXN947.
 */
#define NXP_FREQME_MCXN_REF_CLK_IN       NXP_FREQME_REF(0)
#define NXP_FREQME_MCXN_REF_FRO_12M      NXP_FREQME_REF(1)
#define NXP_FREQME_MCXN_REF_FRO_HF       NXP_FREQME_REF(2)
#define NXP_FREQME_MCXN_REF_OSC32K       NXP_FREQME_REF(4)
#define NXP_FREQME_MCXN_REF_CPU_AHB_CLK  NXP_FREQME_REF(5)
#define NXP_FREQME_MCXN_REF_CLK_IN0      NXP_FREQME_REF(6)
#define NXP_FREQME_MCXN_REF_CLK_IN1      NXP_FREQME_REF(7)

#define NXP_FREQME_MCXN_TAR_CLK_IN       NXP_FREQME_TAR(0)
#define NXP_FREQME_MCXN_TAR_FRO_12M      NXP_FREQME_TAR(1)
#define NXP_FREQME_MCXN_TAR_FRO_HF       NXP_FREQME_TAR(2)
#define NXP_FREQME_MCXN_TAR_OSC32K       NXP_FREQME_TAR(4)
#define NXP_FREQME_MCXN_TAR_CPU_AHB_CLK  NXP_FREQME_TAR(5)
#define NXP_FREQME_MCXN_TAR_CLK_IN0      NXP_FREQME_TAR(6)
#define NXP_FREQME_MCXN_TAR_CLK_IN1      NXP_FREQME_TAR(7)

/*
 * MCXL selectors.
 * Devices: MCXL255.
 */
#define NXP_FREQME_MCXL_REF_FRO_12M     NXP_FREQME_REF(2)
#define NXP_FREQME_MCXL_REF_FRO_HF_DIV  NXP_FREQME_REF(3)
#define NXP_FREQME_MCXL_REF_XTAL32K     NXP_FREQME_REF(4)
#define NXP_FREQME_MCXL_REF_CLK_16K0    NXP_FREQME_REF(5)
#define NXP_FREQME_MCXL_REF_SLOW_CLK    NXP_FREQME_REF(6)
#define NXP_FREQME_MCXL_REF_CLK_IN0     NXP_FREQME_REF(7)
#define NXP_FREQME_MCXL_REF_CLK_IN1     NXP_FREQME_REF(8)

#define NXP_FREQME_MCXL_TAR_FRO_12M     NXP_FREQME_TAR(2)
#define NXP_FREQME_MCXL_TAR_FRO_HF_DIV  NXP_FREQME_TAR(3)
#define NXP_FREQME_MCXL_TAR_XTAL32K     NXP_FREQME_TAR(4)
#define NXP_FREQME_MCXL_TAR_CLK_16K0    NXP_FREQME_TAR(5)
#define NXP_FREQME_MCXL_TAR_SLOW_CLK    NXP_FREQME_TAR(6)
#define NXP_FREQME_MCXL_TAR_CLK_IN0     NXP_FREQME_TAR(7)
#define NXP_FREQME_MCXL_TAR_CLK_IN1     NXP_FREQME_TAR(8)

/*
 * MCXW selectors.
 * Devices: MCXW236. A completely distinct selector set.
 */
#define NXP_FREQME_MCXW_REF_EXTERN_OSC   NXP_FREQME_REF(0)
#define NXP_FREQME_MCXW_REF_FRO_12M      NXP_FREQME_REF(1)
#define NXP_FREQME_MCXW_REF_FRO_32M      NXP_FREQME_REF(2)
#define NXP_FREQME_MCXW_REF_FRO_1M       NXP_FREQME_REF(3)
#define NXP_FREQME_MCXW_REF_OSC32K       NXP_FREQME_REF(4)
#define NXP_FREQME_MCXW_REF_MAIN_CLK     NXP_FREQME_REF(5)
#define NXP_FREQME_MCXW_REF_SPIFI_CLK    NXP_FREQME_REF(6)
#define NXP_FREQME_MCXW_REF_PORT0_PIN3   NXP_FREQME_REF(7)
#define NXP_FREQME_MCXW_REF_PORT0_PIN11  NXP_FREQME_REF(8)
#define NXP_FREQME_MCXW_REF_PORT0_PIN12  NXP_FREQME_REF(9)
#define NXP_FREQME_MCXW_REF_PORT0_PIN14  NXP_FREQME_REF(10)

#define NXP_FREQME_MCXW_TAR_EXTERN_OSC   NXP_FREQME_TAR(0)
#define NXP_FREQME_MCXW_TAR_FRO_12M      NXP_FREQME_TAR(1)
#define NXP_FREQME_MCXW_TAR_FRO_32M      NXP_FREQME_TAR(2)
#define NXP_FREQME_MCXW_TAR_FRO_1M       NXP_FREQME_TAR(3)
#define NXP_FREQME_MCXW_TAR_OSC32K       NXP_FREQME_TAR(4)
#define NXP_FREQME_MCXW_TAR_MAIN_CLK     NXP_FREQME_TAR(5)
#define NXP_FREQME_MCXW_TAR_SPIFI_CLK    NXP_FREQME_TAR(6)
#define NXP_FREQME_MCXW_TAR_PORT0_PIN3   NXP_FREQME_TAR(7)
#define NXP_FREQME_MCXW_TAR_PORT0_PIN11  NXP_FREQME_TAR(8)
#define NXP_FREQME_MCXW_TAR_PORT0_PIN12  NXP_FREQME_TAR(9)
#define NXP_FREQME_MCXW_TAR_PORT0_PIN14  NXP_FREQME_TAR(10)

/*
 * i.MX RT700 selectors.
 * Devices: MIMXRT798S (and RT7xx family).
 *
 * RT700 places the FREQMEAS reference / target mux registers at 0x700 / 0x704
 * (not 0x180 / 0x184 like the MCX families), so it needs its own register
 * constants and helpers.
 */

#define NXP_FREQME_RT7XX_REF_REG 0x700
#define NXP_FREQME_RT7XX_TAR_REG 0x704

#define NXP_FREQME_RT7XX_REF(sel) ((sel) + (NXP_FREQME_RT7XX_REF_REG << NXP_FREQME_PMUX_SHIFT))
#define NXP_FREQME_RT7XX_TAR(sel) ((sel) + (NXP_FREQME_RT7XX_TAR_REG << NXP_FREQME_PMUX_SHIFT))

#define NXP_FREQME_RT7XX_REF_OSC_CLK     NXP_FREQME_RT7XX_REF(0)
#define NXP_FREQME_RT7XX_REF_FRO1_DIV8   NXP_FREQME_RT7XX_REF(1)
#define NXP_FREQME_RT7XX_REF_FRO1        NXP_FREQME_RT7XX_REF(2)
#define NXP_FREQME_RT7XX_REF_LPOSC       NXP_FREQME_RT7XX_REF(3)
#define NXP_FREQME_RT7XX_REF_OSC32K      NXP_FREQME_RT7XX_REF(4)
#define NXP_FREQME_RT7XX_REF_FRO0        NXP_FREQME_RT7XX_REF(6)
#define NXP_FREQME_RT7XX_REF_FRO2        NXP_FREQME_RT7XX_REF(7)
#define NXP_FREQME_RT7XX_REF_GPIO_A_CLK  NXP_FREQME_RT7XX_REF(8)
#define NXP_FREQME_RT7XX_REF_GPIO_B_CLK  NXP_FREQME_RT7XX_REF(9)

#define NXP_FREQME_RT7XX_TAR_OSC_CLK     NXP_FREQME_RT7XX_TAR(0)
#define NXP_FREQME_RT7XX_TAR_FRO1_DIV8   NXP_FREQME_RT7XX_TAR(1)
#define NXP_FREQME_RT7XX_TAR_FRO1        NXP_FREQME_RT7XX_TAR(2)
#define NXP_FREQME_RT7XX_TAR_LPOSC       NXP_FREQME_RT7XX_TAR(3)
#define NXP_FREQME_RT7XX_TAR_OSC32K      NXP_FREQME_RT7XX_TAR(4)
#define NXP_FREQME_RT7XX_TAR_FRO0        NXP_FREQME_RT7XX_TAR(6)
#define NXP_FREQME_RT7XX_TAR_FRO2        NXP_FREQME_RT7XX_TAR(7)
#define NXP_FREQME_RT7XX_TAR_GPIO_A_CLK  NXP_FREQME_RT7XX_TAR(8)
#define NXP_FREQME_RT7XX_TAR_GPIO_B_CLK  NXP_FREQME_RT7XX_TAR(9)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FREQME_H_ */
```

## 15.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 40 行

具有独立 `FREQMEAS_REF`（0x180）／`FREQMEAS_TAR`（0x184）复用器寄存器（Mux Registers）的 MCX 系列。MCXA、MCXC、MCXN、MCXL 和 MCXW 共享此寄存器布局（Register Layout），只有各时钟源的选择器编号（Selector Numbers）不同，因此下文为每个系列分别定义一组标识值（Cookie Set）。

### 注释 3：原第 57 行

MCXA 选择器（Selectors）。
设备：MCXA153、MCXA156、MCXA174、MCXA266、MCXA344、MCXA346、MCXA577，以及选择器编号相同的 MCXC162。

### 注释 4：原第 78 行

MCXN 选择器（Selectors）。
设备：MCXN236、MCXN947。

### 注释 5：原第 98 行

MCXL 选择器（Selectors）。
设备：MCXL255。

### 注释 6：原第 118 行

MCXW 选择器（Selectors）。
设备：MCXW236。其选择器集合完全不同。

### 注释 7：原第 146 行

i.MX RT700 选择器（Selectors）。
设备：MIMXRT798S，以及 RT7xx 系列。

RT700 将频率测量参考／目标复用器寄存器（FREQMEAS Reference / Target Mux Registers）放在 0x700／0x704，而非 MCX 系列的 0x180／0x184，因此需要独立的寄存器常量（Register Constants）和辅助工具（Helpers）。

### 注释 8：原第 185 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_MONITOR_NXP_FREQME_H_`。

## 15.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/nxp-freqme_8h.html)

---

[上一章](P014_microchip-xec-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P016_nxp_mc_cgm.h_源码浏览.md)
