---
id: learning.zephyr-docs.api-source-configuration-reference.page-34
title: imx_ccm.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_imx\_ccm.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm_8h.html)。

## 34.1\_原始可见代码（Source Code）

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
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>

```c
/*
 * Copyright 2017-2022,2024-2025 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_H_

/*
 * Define 16 bits clock ID: 0xXXXX
 * The highest 8 bits is Peripheral ID
 * The lowest 8 bits is Instance ID
 */
#define IMX_CCM_PERIPHERAL_MASK         0xFF00UL
#define IMX_CCM_INSTANCE_MASK           0x00FFUL

#define IMX_CCM_CORESYS_CLK             0x0000UL
#define IMX_CCM_PLATFORM_CLK            0x0100UL
#define IMX_CCM_BUS_CLK                 0x0200UL

#define IMX_CCM_LPUART_CLK              0x0300UL
#define IMX_CCM_LPUART1_CLK             0x0300UL
#define IMX_CCM_LPUART2_CLK             0x0301UL
#define IMX_CCM_LPUART3_CLK             0x0302UL
#define IMX_CCM_LPUART4_CLK             0x0303UL
#define IMX_CCM_LPUART5_CLK             0x0304UL
#define IMX_CCM_LPUART6_CLK             0x0305UL
#define IMX_CCM_LPUART7_CLK             0x0306UL
#define IMX_CCM_LPUART8_CLK             0x0307UL

#define IMX_CCM_LPI2C_CLK               0x0400UL

#define IMX_CCM_LPSPI_CLK               0x0500UL

#define IMX_CCM_USDHC1_CLK              0x0600UL
#define IMX_CCM_USDHC2_CLK              0x0601UL

#define IMX_CCM_EDMA_CLK                0x0700UL

#define IMX_CCM_UART1_CLK               0x0800UL
#define IMX_CCM_UART2_CLK               0x0801UL
#define IMX_CCM_UART3_CLK               0x0802UL
#define IMX_CCM_UART4_CLK               0x0803UL

#define IMX_CCM_CAN_CLK                 0x0900UL
#define IMX_CCM_CAN1_CLK                0x0900UL
#define IMX_CCM_CAN2_CLK                0x0901UL

#define IMX_CCM_GPT_CLK                 0x0A00UL

#define IMX_CCM_SAI1_CLK                0x0B00UL
#define IMX_CCM_SAI2_CLK                0x0B01UL
#define IMX_CCM_SAI3_CLK                0x0B02UL

#define IMX_CCM_PWM_CLK                 0x0C00UL

#define IMX_CCM_QTMR_CLK                0x0D00UL

#define IMX_CCM_ENET_CLK                0x0E00UL
#define IMX_CCM_ENET_PLL                0x0E01UL

#define IMX_CCM_FLEXSPI_CLK             0x0F00UL
#define IMX_CCM_FLEXSPI2_CLK            0x0F01UL

#define IMX_CCM_PIT_CLK                 0x1000UL

#define IMX_CCM_FLEXIO1_CLK             0x1100UL
#define IMX_CCM_FLEXIO2_3_CLK           0x1101UL

#define IMX_CCM_ECSPI1_CLK              0x1200UL
#define IMX_CCM_ECSPI2_CLK              0x1201UL
#define IMX_CCM_ECSPI3_CLK              0x1202UL

#define IMX_CCM_GPT_IPG_CLK             0x1300UL

#define IMX_CCM_I2C1_CLK                0x1400UL
#define IMX_CCM_I2C2_CLK                0x1401UL
#define IMX_CCM_I2C3_CLK                0x1402UL
#define IMX_CCM_I2C4_CLK                0x1403UL
#define IMX_CCM_I2C5_CLK                0x1404UL
#define IMX_CCM_I2C6_CLK                0x1405UL

#define IMX_CCM_ESAI0_CLK               0x1500UL
#define IMX_CCM_ESAI1_CLK               0x1501UL

#define IMX_CCM_AUD_PLL_DIV_CLK0                0x1600UL

#define IMX_CCM_OCOTP_CLK               0x1700UL

#define IMX_CCM_XBAR1_CLK               0x1800UL
#define IMX_CCM_XBAR2_CLK               0x1801UL
#define IMX_CCM_XBAR3_CLK               0x1802UL

/*
 * i.MX PWM ("ipwm") instances, as found on the i.MX8M family
 */
#define IMX_CCM_PWM1_CLK                0x1900UL
#define IMX_CCM_PWM2_CLK                0x1901UL
#define IMX_CCM_PWM3_CLK                0x1902UL
#define IMX_CCM_PWM4_CLK                0x1903UL

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_H_ */
```

## 34.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2017-2022,2024-2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

定义 16 位时钟标识符（Clock ID）：`0xXXXX`。高 8 位是外设标识符（Peripheral ID），低 8 位是实例标识符（Instance ID）。

### 注释 3：原第 98 行

i.MX PWM（`ipwm`）实例，例如 i.MX8M 系列中的实例。

### 注释 4：原第 110 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_IMX_CCM_H_`。

## 34.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/imx__ccm_8h.html)

---

[上一章](P033_imx8ulp_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P035_settings.h_源码浏览.md)
