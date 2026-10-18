---
id: learning.zephyr-docs.api-source-system-reference.page-32
title: numicro_m48x_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/numicro__m48x__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_numicro\_m48x\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/numicro__m48x__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P274_zephyr__dt-bindings__reset__numicro_m48x_reset.h_文件参考.md)。

## 32.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00027"></a>
<a id="l00029"></a>
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
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
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
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00196"></a>

```c


/*
 * Copyright (c) 2026 Fiona Behrens
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMICRO_M48X_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMICRO_M48X_RESET_H_




/* Beginning of M480 BSP sys_reg.h reset module copy */

#define NUMICRO_SYS_IPRST0_CHIPRST_Pos   0
#define NUMICRO_SYS_IPRST0_CPURST_Pos    1
#define NUMICRO_SYS_IPRST0_PDMARST_Pos   2
#define NUMICRO_SYS_IPRST0_EBIRST_Pos    3
#define NUMICRO_SYS_IPRST0_EMACRST_Pos   5
#define NUMICRO_SYS_IPRST0_SDH0RST_Pos   6
#define NUMICRO_SYS_IPRST0_CRCRST_Pos    7
#define NUMICRO_SYS_IPRST0_CCAPRST_Pos   8
#define NUMICRO_SYS_IPRST0_HSUSBDRST_Pos 10
#define NUMICRO_SYS_IPRST0_CRPTRST_Pos   12
#define NUMICRO_SYS_IPRST0_SPIMRST_Pos   14
#define NUMICRO_SYS_IPRST0_USBHRST_Pos   16
#define NUMICRO_SYS_IPRST0_SDH1RST_Pos   17

#define NUMICRO_SYS_IPRST1_GPIORST_Pos   1
#define NUMICRO_SYS_IPRST1_TMR0RST_Pos   2
#define NUMICRO_SYS_IPRST1_TMR1RST_Pos   3
#define NUMICRO_SYS_IPRST1_TMR2RST_Pos   4
#define NUMICRO_SYS_IPRST1_TMR3RST_Pos   5
#define NUMICRO_SYS_IPRST1_ACMP01RST_Pos 7
#define NUMICRO_SYS_IPRST1_I2C0RST_Pos   8
#define NUMICRO_SYS_IPRST1_I2C1RST_Pos   9
#define NUMICRO_SYS_IPRST1_I2C2RST_Pos   10
#define NUMICRO_SYS_IPRST1_QSPI0RST_Pos  12
#define NUMICRO_SYS_IPRST1_SPI0RST_Pos   13
#define NUMICRO_SYS_IPRST1_SPI1RST_Pos   14
#define NUMICRO_SYS_IPRST1_SPI2RST_Pos   15
#define NUMICRO_SYS_IPRST1_UART0RST_Pos  16
#define NUMICRO_SYS_IPRST1_UART1RST_Pos  17
#define NUMICRO_SYS_IPRST1_UART2RST_Pos  18
#define NUMICRO_SYS_IPRST1_UART3RST_Pos  19
#define NUMICRO_SYS_IPRST1_UART4RST_Pos  20
#define NUMICRO_SYS_IPRST1_UART5RST_Pos  21
#define NUMICRO_SYS_IPRST1_UART6RST_Pos  22
#define NUMICRO_SYS_IPRST1_UART7RST_Pos  23
#define NUMICRO_SYS_IPRST1_CAN0RST_Pos   24
#define NUMICRO_SYS_IPRST1_CAN1RST_Pos   25
#define NUMICRO_SYS_IPRST1_OTGRST_Pos    26
#define NUMICRO_SYS_IPRST1_USBDRST_Pos   27
#define NUMICRO_SYS_IPRST1_EADCRST_Pos   28
#define NUMICRO_SYS_IPRST1_I2S0RST_Pos   29
#define NUMICRO_SYS_IPRST1_HSOTGRST_Pos  30
#define NUMICRO_SYS_IPRST1_TRNGRST_Pos   31

#define NUMICRO_SYS_IPRST2_SC0RST_Pos   0
#define NUMICRO_SYS_IPRST2_SC1RST_Pos   1
#define NUMICRO_SYS_IPRST2_SC2RST_Pos   2
#define NUMICRO_SYS_IPRST2_QSPI1RST_Pos 4
#define NUMICRO_SYS_IPRST2_SPI3RST_Pos  6
#define NUMICRO_SYS_IPRST2_USCI0RST_Pos 8
#define NUMICRO_SYS_IPRST2_USCI1RST_Pos 9
#define NUMICRO_SYS_IPRST2_DACRST_Pos   12
#define NUMICRO_SYS_IPRST2_EPWM0RST_Pos 16
#define NUMICRO_SYS_IPRST2_EPWM1RST_Pos 17
#define NUMICRO_SYS_IPRST2_BPWM0RST_Pos 18
#define NUMICRO_SYS_IPRST2_BPWM1RST_Pos 19
#define NUMICRO_SYS_IPRST2_QEI0RST_Pos  22
#define NUMICRO_SYS_IPRST2_QEI1RST_Pos  23
#define NUMICRO_SYS_IPRST2_ECAP0RST_Pos 26
#define NUMICRO_SYS_IPRST2_ECAP1RST_Pos 27
#define NUMICRO_SYS_IPRST2_CAN2RST_Pos  28
#define NUMICRO_SYS_IPRST2_OPARST_Pos   30
#define NUMICRO_SYS_IPRST2_EADC1RST_Pos 31

/* End of M480 BSP sys_reg.h reset module copy */



#define NUMICRO_RST_ID_IPRST0 (0UL << 24)
#define NUMICRO_RST_ID_IPRST1 (4UL << 24)
#define NUMICRO_RST_ID_IPRST2 (8UL << 24)




/* Beginning of M480 BSP sys.h reset module copy */

/* Module Reset Control Resister constant definitions. */

#define NUMICRO_PDMA_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_PDMARST_Pos)
#define NUMICRO_EBI_RST    (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_EBIRST_Pos)
#define NUMICRO_EMAC_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_EMACRST_Pos)
#define NUMICRO_SDH0_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_SDH0RST_Pos)
#define NUMICRO_CRC_RST    (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_CRCRST_Pos)
#define NUMICRO_CCAP_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_CCAPRST_Pos)
#define NUMICRO_HSUSBD_RST (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_HSUSBDRST_Pos)
#define NUMICRO_CRPT_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_CRPTRST_Pos)
#define NUMICRO_SPIM_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_SPIMRST_Pos)
#define NUMICRO_USBH_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_USBHRST_Pos)
#define NUMICRO_SDH1_RST   (NUMICRO_RST_ID_IPRST0 | NUMICRO_SYS_IPRST0_SDH1RST_Pos)

#define NUMICRO_GPIO_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_GPIORST_Pos)
#define NUMICRO_TMR0_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_TMR0RST_Pos)
#define NUMICRO_TMR1_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_TMR1RST_Pos)
#define NUMICRO_TMR2_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_TMR2RST_Pos)
#define NUMICRO_TMR3_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_TMR3RST_Pos)
#define NUMICRO_ACMP01_RST (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_ACMP01RST_Pos)
#define NUMICRO_I2C0_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_I2C0RST_Pos)
#define NUMICRO_I2C1_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_I2C1RST_Pos)
#define NUMICRO_I2C2_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_I2C2RST_Pos)
#define NUMICRO_QSPI0_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_QSPI0RST_Pos)
#define NUMICRO_SPI0_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_SPI0RST_Pos)
#define NUMICRO_SPI1_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_SPI1RST_Pos)
#define NUMICRO_SPI2_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_SPI2RST_Pos)
#define NUMICRO_UART0_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART0RST_Pos)
#define NUMICRO_UART1_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART1RST_Pos)
#define NUMICRO_UART2_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART2RST_Pos)
#define NUMICRO_UART3_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART3RST_Pos)
#define NUMICRO_UART4_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART4RST_Pos)
#define NUMICRO_UART5_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART5RST_Pos)
#define NUMICRO_UART6_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART6RST_Pos)
#define NUMICRO_UART7_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_UART7RST_Pos)
#define NUMICRO_CAN0_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_CAN0RST_Pos)
#define NUMICRO_CAN1_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_CAN1RST_Pos)
#define NUMICRO_OTG_RST    (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_OTGRST_Pos)
#define NUMICRO_USBD_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_USBDRST_Pos)
#define NUMICRO_EADC_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_EADCRST_Pos)
#define NUMICRO_I2S0_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_I2S0RST_Pos)
#define NUMICRO_HSOTG_RST  (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_HSOTGRST_Pos)
#define NUMICRO_TRNG_RST   (NUMICRO_RST_ID_IPRST1 | NUMICRO_SYS_IPRST1_TRNGRST_Pos)

#define NUMICRO_SC0_RST   (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_SC0RST_Pos)
#define NUMICRO_SC1_RST   (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_SC1RST_Pos)
#define NUMICRO_SC2_RST   (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_SC2RST_Pos)
#define NUMICRO_QSPI1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_QSPI1RST_Pos)
#define NUMICRO_SPI3_RST  (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_SPI3RST_Pos)
#define NUMICRO_USCI0_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_USCI0RST_Pos)
#define NUMICRO_USCI1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_USCI1RST_Pos)
#define NUMICRO_DAC_RST   (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_DACRST_Pos)
#define NUMICRO_EPWM0_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_EPWM0RST_Pos)
#define NUMICRO_EPWM1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_EPWM1RST_Pos)
#define NUMICRO_BPWM0_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_BPWM0RST_Pos)
#define NUMICRO_BPWM1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_BPWM1RST_Pos)
#define NUMICRO_QEI0_RST  (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_QEI0RST_Pos)
#define NUMICRO_QEI1_RST  (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_QEI1RST_Pos)
#define NUMICRO_ECAP0_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_ECAP0RST_Pos)
#define NUMICRO_ECAP1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_ECAP1RST_Pos)
#define NUMICRO_CAN2_RST  (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_CAN2RST_Pos)
#define NUMICRO_OPA_RST   (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_OPARST_Pos)
#define NUMICRO_EADC1_RST (NUMICRO_RST_ID_IPRST2 | NUMICRO_SYS_IPRST2_EADC1RST_Pos)

/* End of M480 BSP sys.h reset module copy */




#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMICRO_M48X_RESET_H_ */
```

## 32.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2026 Fiona Behrens。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

复制自 M480 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 3：原第 101 行

复制自 M480 板级支持包（BSP）`sys_reg.h` 的复位模块（Reset Module）结束（End）。

### 注释 4：原第 122 行

复制自 M480 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）开始（Beginning）。

### 注释 5：原第 124 行

模块复位控制寄存器常量定义（Module Reset Control Register Constant Definitions）。

### 注释 6：原第 188 行

复制自 M480 板级支持包（BSP）`sys.h` 的复位模块（Reset Module）结束（End）。

### 注释 7：原第 196 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NUMICRO_M48X_RESET_H_`。

## 32.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P274_zephyr__dt-bindings__reset__numicro_m48x_reset.h_文件参考.md)

---

[上一章](P031_numaker_m55m1x_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P033_nxp_flexram.h_源码浏览.md)
