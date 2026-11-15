---
id: learning.zephyr-docs.api-source-supplement-reference.page-223
title: ti-cc32xx-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第223章\_ti-cc32xx-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h.html)。

## 223.1\_原始可见代码（Source Code）

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
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
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
<a id="l00219"></a>
<a id="l00220"></a>

```c
/*
 * Copyright (c) 2021 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TI_CC32XX_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TI_CC32XX_PINCTRL_H_

/*
 * The whole TI CC32XX pin configuration information is encoded in a 32-bit
 * bitfield organized as follows:
 *
 * - 31..22: Reserved
 * - 21..16: Pin.
 * - 15..10: Reserved.
 * - 9:      Pull-down flag.
 * - 8:      Pull-up flag.
 * - 7..5:   Drive strength.
 * - 4:      Enable open-drain flag.
 * - 3..0:   Configuration mode
 *
 * Note that the lower bits (11..0) map directly to the MEM_GPIO_PAD_CONFIG
 * register.
 */


#define TI_CC32XX_PIN_MSK 0x3FU
#define TI_CC32XX_PIN_POS 16U
#define TI_CC32XX_MUX_MSK 0xFU
#define TI_CC32XX_MUX_POS 0U


#define TI_CC32XX_PINMUX(pin, mux)                                                                 \
        ((((pin)&TI_CC32XX_PIN_MSK) << TI_CC32XX_PIN_POS) |                                        \
         (((mux)&TI_CC32XX_MUX_MSK) << TI_CC32XX_MUX_POS))


#define GPIO10_P1     TI_CC32XX_PINMUX(1U, 0U)
#define I2C_SCL_P1    TI_CC32XX_PINMUX(1U, 1U)
#define GT_PWM06_P1   TI_CC32XX_PINMUX(1U, 3U)
#define UART1_TX_P1   TI_CC32XX_PINMUX(1U, 7U)
#define SDCARD_CLK_P1 TI_CC32XX_PINMUX(1U, 6U)
#define GT_CCP01_P1   TI_CC32XX_PINMUX(1U, 12U)

#define GPIO11_P2     TI_CC32XX_PINMUX(2U, 0U)
#define I2C_SDA_P2    TI_CC32XX_PINMUX(2U, 1U)
#define GT_PWM07_P2   TI_CC32XX_PINMUX(2U, 3U)
#define PXCLK_P2      TI_CC32XX_PINMUX(2U, 4U)
#define SDCARD_CMD_P2 TI_CC32XX_PINMUX(2U, 6U)
#define UART1_RX_P2   TI_CC32XX_PINMUX(2U, 7U)
#define GT_CCP02_P2   TI_CC32XX_PINMUX(2U, 12U)
#define MCAFSX_P2     TI_CC32XX_PINMUX(2U, 13U)

#define GPIO12_P3   TI_CC32XX_PINMUX(3U, 0U)
#define MCACLK_P3   TI_CC32XX_PINMUX(3U, 3U)
#define PVS_P3      TI_CC32XX_PINMUX(3U, 4U)
#define I2C_SCL_P3  TI_CC32XX_PINMUX(3U, 5U)
#define UART0_TX_P3 TI_CC32XX_PINMUX(3U, 7U)
#define GT_CCP03_P3 TI_CC32XX_PINMUX(3U, 12U)

#define GPIO13_P4   TI_CC32XX_PINMUX(4U, 0U)
#define I2C_SDA_P4  TI_CC32XX_PINMUX(4U, 5U)
#define PHS_P4      TI_CC32XX_PINMUX(4U, 4U)
#define UART0_RX_P4 TI_CC32XX_PINMUX(4U, 7U)
#define GT_CCP04_P4 TI_CC32XX_PINMUX(4U, 12U)

#define GPIO14_P5   TI_CC32XX_PINMUX(5U, 0U)
#define I2C_SCL_P5  TI_CC32XX_PINMUX(5U, 5U)
#define GSPI_CLK_P5 TI_CC32XX_PINMUX(5U, 7U)
#define PDATA8_P5   TI_CC32XX_PINMUX(5U, 4U)
#define GT_CCP05_P5 TI_CC32XX_PINMUX(5U, 12U)

#define GPIO15_P6       TI_CC32XX_PINMUX(6U, 0U)
#define I2C_SDA_P6      TI_CC32XX_PINMUX(6U, 5U)
#define GSPI_MISO_P6    TI_CC32XX_PINMUX(6U, 7U)
#define PDATA9_P6       TI_CC32XX_PINMUX(6U, 4U)
#define SDCARD_DATA3_P6 TI_CC32XX_PINMUX(6U, 8U)
#define GT_CCP06_P6     TI_CC32XX_PINMUX(6U, 13U)

#define GPIO16_P7     TI_CC32XX_PINMUX(7U, 0U)
#define GSPI_MOSI_P7  TI_CC32XX_PINMUX(7U, 7U)
#define PDATA10_P7    TI_CC32XX_PINMUX(7U, 4U)
#define UART1_TX_P7   TI_CC32XX_PINMUX(7U, 5U)
#define SDCARD_CLK_P7 TI_CC32XX_PINMUX(7U, 8U)
#define GT_CCP07_P7   TI_CC32XX_PINMUX(7U, 13U)

#define GPIO17_P8     TI_CC32XX_PINMUX(8U, 0U)
#define UART1_RX_P8   TI_CC32XX_PINMUX(8U, 5U)
#define GSPI_CS_P8    TI_CC32XX_PINMUX(8U, 7U)
#define SDCARD_CMD_P8 TI_CC32XX_PINMUX(8U, 8U)
#define PDATA11_P8    TI_CC32XX_PINMUX(8U, 4U)

#define GPIO22_P15   TI_CC32XX_PINMUX(15U, 0U)
#define MCAFSX_P15   TI_CC32XX_PINMUX(15U, 7U)
#define GT_CCP04_P15 TI_CC32XX_PINMUX(15U, 5U)

#define GPIO23_P16   TI_CC32XX_PINMUX(16U, 0U)
#define TDI_P16      TI_CC32XX_PINMUX(16U, 1U)
#define UART1_TX_P16 TI_CC32XX_PINMUX(16U, 2U)
#define I2C_SCL_P16  TI_CC32XX_PINMUX(16U, 9U)

#define GPIO24_P17   TI_CC32XX_PINMUX(17U, 0U)
#define TDO_P17      TI_CC32XX_PINMUX(17U, 1U)
#define PWM0_P17     TI_CC32XX_PINMUX(17U, 5U)
#define UART1_RX_P17 TI_CC32XX_PINMUX(17U, 2U)
#define I2C_SDA_P17  TI_CC32XX_PINMUX(17U, 9U)
#define GT_CCP06_P17 TI_CC32XX_PINMUX(17U, 4U)
#define MCAFSX_P17   TI_CC32XX_PINMUX(17U, 6U)

#define GPIO28_P18 TI_CC32XX_PINMUX(18U, 0U)

#define TCK_P19      TI_CC32XX_PINMUX(19U, 1U)
#define GT_PWM03_P19 TI_CC32XX_PINMUX(19U, 8U)

#define GPIO29_P20 TI_CC32XX_PINMUX(20U, 0U)
#define TMS_P20    TI_CC32XX_PINMUX(20U, 1U)

#define GPIO25_P21   TI_CC32XX_PINMUX(21U, 0U)
#define GT_PWM02_P21 TI_CC32XX_PINMUX(21U, 9U)
#define MCASFX_P21   TI_CC32XX_PINMUX(21U, 2U)

#define ANTSEL1_P29 TI_CC32XX_PINMUX(29U, 0U)

#define ANTSEL2_P30 TI_CC32XX_PINMUX(30U, 0U)

#define GPIO31_P45   TI_CC32XX_PINMUX(45U, 0U)
#define UART0_RX_P45 TI_CC32XX_PINMUX(45U, 9U)
#define MCAFSX_P45   TI_CC32XX_PINMUX(45U, 12U)
#define UART1_RX_P45 TI_CC32XX_PINMUX(45U, 2U)
#define MCAXR0_P45   TI_CC32XX_PINMUX(45U, 6U)
#define GSPI_CLK_P45 TI_CC32XX_PINMUX(45U, 7U)

#define GPIO0_P50      TI_CC32XX_PINMUX(50U, 0U)
#define UART0_CTSN_P50 TI_CC32XX_PINMUX(50U, 12U)
#define MCAXR1_P50     TI_CC32XX_PINMUX(50U, 6U)
#define GT_CCP00_P50   TI_CC32XX_PINMUX(50U, 7U)
#define GSPI_CS_P50    TI_CC32XX_PINMUX(50U, 9U)
#define UART1_RTS_P50  TI_CC32XX_PINMUX(50U, 10U)
#define UART0_RTS_P50  TI_CC32XX_PINMUX(50U, 3U)
#define MCAXR0_P50     TI_CC32XX_PINMUX(50U, 4U)

#define GPIO32_P52    TI_CC32XX_PINMUX(52U, 0U)
#define MCACLK_P52    TI_CC32XX_PINMUX(52U, 2U)
#define MCAXR0_P52    TI_CC32XX_PINMUX(52U, 4U)
#define UART0_RTS_P52 TI_CC32XX_PINMUX(52U, 6U)
#define GSPI_MOSI_P52 TI_CC32XX_PINMUX(52U, 8U)

#define GPIO30_P53    TI_CC32XX_PINMUX(53U, 0U)
#define UART0_TX_P53  TI_CC32XX_PINMUX(53U, 9U)
#define MCACLK_P53    TI_CC32XX_PINMUX(53U, 2U)
#define MCAFSX_P53    TI_CC32XX_PINMUX(53U, 3U)
#define GT_CCP05_P53  TI_CC32XX_PINMUX(53U, 4U)
#define GSPI_MISO_P53 TI_CC32XX_PINMUX(53U, 7U)

#define GPIO1_P55    TI_CC32XX_PINMUX(55U, 0U)
#define UART0_TX_P55 TI_CC32XX_PINMUX(55U, 3U)
#define PCLK_P55     TI_CC32XX_PINMUX(55U, 4U)
#define UART1_TX_P55 TI_CC32XX_PINMUX(55U, 6U)
#define GT_CCP01_P55 TI_CC32XX_PINMUX(55U, 7U)

#define GPIO2_P57    TI_CC32XX_PINMUX(57U, 0U)
#define UART0_RX_P57 TI_CC32XX_PINMUX(57U, 3U)
#define UART1_RX_P57 TI_CC32XX_PINMUX(57U, 6U)
#define GT_CCP02_P57 TI_CC32XX_PINMUX(57U, 7U)

#define GPIO3_P58    TI_CC32XX_PINMUX(58U, 0U)
#define UART1_TX_P58 TI_CC32XX_PINMUX(58U, 6U)
#define PDATA7_P58   TI_CC32XX_PINMUX(58U, 7U)

#define GPIO5_P59    TI_CC32XX_PINMUX(59U, 0U)
#define UART1_RX_P59 TI_CC32XX_PINMUX(59U, 6U)
#define PDATA6_P59   TI_CC32XX_PINMUX(59U, 4U)

#define GPIO5_P60    TI_CC32XX_PINMUX(60U, 0U)
#define PDATA5_P60   TI_CC32XX_PINMUX(60U, 4U)
#define MCAXR1_P60   TI_CC32XX_PINMUX(60U, 6U)
#define GT_CCP05_P60 TI_CC32XX_PINMUX(60U, 7U)

#define GPIO6_P61     TI_CC32XX_PINMUX(61U, 0U)
#define UART0_RTS_P61 TI_CC32XX_PINMUX(61U, 5U)
#define PDATA4_P61    TI_CC32XX_PINMUX(61U, 4U)
#define UART1_CTS_P61 TI_CC32XX_PINMUX(61U, 3U)
#define UART0_CTS_P61 TI_CC32XX_PINMUX(61U, 6U)
#define GT_CCP06_P61  TI_CC32XX_PINMUX(61U, 7U)

#define GPIO7_P62     TI_CC32XX_PINMUX(62U, 0U)
#define MCACLKX_P62   TI_CC32XX_PINMUX(62U, 13U)
#define UART1_RTS_P62 TI_CC32XX_PINMUX(62U, 3U)
#define UART0_RTS_P62 TI_CC32XX_PINMUX(62U, 10U)
#define UART0_TX_P62  TI_CC32XX_PINMUX(62U, 11U)

#define GPIO8_P63      TI_CC32XX_PINMUX(63U, 0U)
#define SDCARD_IRQ_P63 TI_CC32XX_PINMUX(63U, 6U)
#define MCAFSX_P63     TI_CC32XX_PINMUX(63U, 7U)
#define GT_CCP06_P63   TI_CC32XX_PINMUX(63U, 12U)

#define GPIO9_P64       TI_CC32XX_PINMUX(64U, 0U)
#define GT_PWM05_P64    TI_CC32XX_PINMUX(64U, 3U)
#define SDCARD_DATA_P64 TI_CC32XX_PINMUX(64U, 6U)
#define MCAXR0_P64      TI_CC32XX_PINMUX(64U, 7U)
#define GT_CCP00_P64    TI_CC32XX_PINMUX(64U, 12U)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TI_CC32XX_PINCTRL_H_ */
```

## 223.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

全部 TI CC32XX 引脚配置信息编码在一个 32 位位域（Bitfield）中，组织如下：

- `31..22`：保留。
- `21..16`：引脚。
- `15..10`：保留。
- `9`：下拉标志。
- `8`：上拉标志。
- `7..5`：驱动强度。
- `4`：开漏使能标志（Enable open-drain flag）。
- `3..0`：配置模式。

注意，低位 `11..0` 直接映射到 `MEM_GPIO_PAD_CONFIG` 寄存器。

### 注释 3：原第 220 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_TI_CC32XX_PINCTRL_H_`。

## 223.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h.html)

---

[上一章](P222_test_asm_inline_other.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P224_ti-k3-pinctrl.h_源码浏览.md)
