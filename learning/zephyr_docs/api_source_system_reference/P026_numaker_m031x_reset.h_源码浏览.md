---
id: learning.zephyr-docs.api-source-system-reference.page-26
title: numaker_m031x_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numaker__m031x__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_numaker\_m031x\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numaker__m031x__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P262_zephyr__dt-bindings__reset__numaker_m031x_reset.h_文件参考.md)。

## 26.1\_原始可见代码（Source Code）

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
<a id="l00040"></a>
<a id="l00052"></a>
<a id="l00054"></a>
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
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>

```c
/*
 * Copyright (c) 2026 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M031X_RESET_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMAKER_M031X_RESET_H





/* Beginning of M031 BSP sys_reg.h reset module copy */

#define SYS_IPRST0_CHIPRST_Pos           0
#define SYS_IPRST0_CPURST_Pos            1
#define SYS_IPRST0_PDMARST_Pos           2
#define SYS_IPRST0_EBIRST_Pos            3
#define SYS_IPRST0_HDIVRST_Pos           4
#define SYS_IPRST0_CRCRST_Pos            7
#define SYS_IPRST1_GPIORST_Pos           1
#define SYS_IPRST1_TMR0RST_Pos           2
#define SYS_IPRST1_TMR1RST_Pos           3
#define SYS_IPRST1_TMR2RST_Pos           4
#define SYS_IPRST1_TMR3RST_Pos           5
#define SYS_IPRST1_ACMP01RST_Pos         7
#define SYS_IPRST1_I2C0RST_Pos           8
#define SYS_IPRST1_I2C1RST_Pos           9
#define SYS_IPRST1_QSPI0RST_Pos          12
#define SYS_IPRST1_SPI0RST_Pos           13
#define SYS_IPRST1_UART0RST_Pos          16
#define SYS_IPRST1_UART1RST_Pos          17
#define SYS_IPRST1_UART2RST_Pos          18
#define SYS_IPRST1_UART3RST_Pos          19
#define SYS_IPRST1_UART4RST_Pos          20
#define SYS_IPRST1_UART5RST_Pos          21
#define SYS_IPRST1_UART6RST_Pos          22
#define SYS_IPRST1_UART7RST_Pos          23
#define SYS_IPRST1_USBDRST_Pos           27
#define SYS_IPRST1_ADCRST_Pos            28
#define SYS_IPRST2_USCI0RST_Pos          8
#define SYS_IPRST2_USCI1RST_Pos          9
#define SYS_IPRST2_PWM0RST_Pos           16
#define SYS_IPRST2_PWM1RST_Pos           17
#define SYS_IPRST2_BPWM0RST_Pos          18
#define SYS_IPRST2_BPWM1RST_Pos          19

/* End of M031 BSP sys_reg.h reset module copy */

/* Beginning of M031 BSP sys.h reset module copy */

/*---------------------------------------------------------------------
 *  Module Reset Control Resister constant definitions.
 *---------------------------------------------------------------------
 */

#define NUMAKER_PDMA_RST    ((0x0 << 24) | SYS_IPRST0_PDMARST_Pos)
#define NUMAKER_EBI_RST     ((0x0 << 24) | SYS_IPRST0_EBIRST_Pos)
#define NUMAKER_HDIV_RST    ((0x0 << 24) | SYS_IPRST0_HDIVRST_Pos)
#define NUMAKER_CRC_RST     ((0x0 << 24) | SYS_IPRST0_CRCRST_Pos)
#define NUMAKER_GPIO_RST    ((0x4 << 24) | SYS_IPRST1_GPIORST_Pos)
#define NUMAKER_TMR0_RST    ((0x4 << 24) | SYS_IPRST1_TMR0RST_Pos)
#define NUMAKER_TMR1_RST    ((0x4 << 24) | SYS_IPRST1_TMR1RST_Pos)
#define NUMAKER_TMR2_RST    ((0x4 << 24) | SYS_IPRST1_TMR2RST_Pos)
#define NUMAKER_TMR3_RST    ((0x4 << 24) | SYS_IPRST1_TMR3RST_Pos)
#define NUMAKER_ACMP01_RST  ((0x4 << 24) | SYS_IPRST1_ACMP01RST_Pos)
#define NUMAKER_I2C0_RST    ((0x4 << 24) | SYS_IPRST1_I2C0RST_Pos)
#define NUMAKER_I2C1_RST    ((0x4 << 24) | SYS_IPRST1_I2C1RST_Pos)
#define NUMAKER_QSPI0_RST   ((0x4 << 24) | SYS_IPRST1_QSPI0RST_Pos)
#define NUMAKER_SPI0_RST    ((0x4 << 24) | SYS_IPRST1_SPI0RST_Pos)
#define NUMAKER_UART0_RST   ((0x4 << 24) | SYS_IPRST1_UART0RST_Pos)
#define NUMAKER_UART1_RST   ((0x4 << 24) | SYS_IPRST1_UART1RST_Pos)
#define NUMAKER_UART2_RST   ((0x4 << 24) | SYS_IPRST1_UART2RST_Pos)
#define NUMAKER_UART3_RST   ((0x4 << 24) | SYS_IPRST1_UART3RST_Pos)
#define NUMAKER_UART4_RST   ((0x4 << 24) | SYS_IPRST1_UART4RST_Pos)
#define NUMAKER_UART5_RST   ((0x4 << 24) | SYS_IPRST1_UART5RST_Pos)
#define NUMAKER_UART6_RST   ((0x4 << 24) | SYS_IPRST1_UART6RST_Pos)
#define NUMAKER_UART7_RST   ((0x4 << 24) | SYS_IPRST1_UART7RST_Pos)
#define NUMAKER_USBD_RST    ((0x4 << 24) | SYS_IPRST1_USBDRST_Pos)
#define NUMAKER_ADC_RST     ((0x4 << 24) | SYS_IPRST1_ADCRST_Pos)
#define NUMAKER_USCI0_RST   ((0x8 << 24) | SYS_IPRST2_USCI0RST_Pos)
#define NUMAKER_USCI1_RST   ((0x8 << 24) | SYS_IPRST2_USCI1RST_Pos)
#define NUMAKER_PWM0_RST    ((0x8 << 24) | SYS_IPRST2_PWM0RST_Pos)
#define NUMAKER_PWM1_RST    ((0x8 << 24) | SYS_IPRST2_PWM1RST_Pos)
#define NUMAKER_BPWM0_RST   ((0x8 << 24) | SYS_IPRST2_BPWM0RST_Pos)
#define NUMAKER_BPWM1_RST   ((0x8 << 24) | SYS_IPRST2_BPWM1RST_Pos)

/* End of M031 BSP sys.h reset module copy */





#endif
```

## 26.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 61 行

复制自 M031 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 3：原第 96 行

复制自 M031 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）结束（End）。

### 注释 4：原第 98 行

复制自 M031 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 5：原第 100 行

模块复位控制寄存器常量定义（Module Reset Control Register Constant Definitions）。原注释以分隔线标示此段。

### 注释 6：原第 136 行

复制自 M031 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）结束（End）。

## 26.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P262_zephyr__dt-bindings__reset__numaker_m031x_reset.h_文件参考.md)

---

[上一章](P025_npcx_espi.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P027_numaker_m2l31x_reset.h_源码浏览.md)
