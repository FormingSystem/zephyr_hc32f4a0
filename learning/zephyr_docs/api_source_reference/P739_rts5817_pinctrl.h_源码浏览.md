---
id: learning.zephyr-docs.api-source-reference.page-739
title: rts5817_pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第739章\_rts5817\_pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h.html)。

## 739.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="foldopen00021"></a>
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

```c
/*
 * Copyright (c) 2025 Realtek Semiconductor, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTS5817_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTS5817_PINCTRL_H_

#define RTS_FP_PIN_SHIFT  0U
#define RTS_FP_PIN_MASK   0xFFU
#define RTS_FP_FUNC_SHIFT 8U
#define RTS_FP_FUNC_MASK  0x1FU

#define RTS_FP_PINMUX(pin, func)                                                                   \
        ((((RTS_FP_PIN_##pin) & RTS_FP_PIN_MASK) << RTS_FP_PIN_SHIFT) |                            \
         (((RTS_FP_PIN_##func) & RTS_FP_FUNC_MASK) << RTS_FP_FUNC_SHIFT))

#define RTS_FP_PINMUX_PIN(__pin)  (((__pin) >> RTS_FP_PIN_SHIFT) & RTS_FP_PIN_MASK)
#define RTS_FP_PINMUX_FUNC(__pin) (((__pin) >> RTS_FP_FUNC_SHIFT) & RTS_FP_FUNC_MASK)

#define IO_POWER_1V8 0
#define IO_POWER_3V3 1

#define RTS_FP_PIN_FUNC0 0
#define RTS_FP_PIN_FUNC1 1
#define RTS_FP_PIN_FUNC2 2
#define RTS_FP_PIN_FUNC3 3
#define RTS_FP_PIN_FUNC4 4
#define RTS_FP_PIN_FUNC5 5
#define RTS_FP_PIN_FUNC6 6
#define RTS_FP_PIN_FUNC7 7

#define RTS_FP_PIN_CACHE_CS1  0
#define RTS_FP_PIN_CACHE_MISO 1
#define RTS_FP_PIN_CACHE_MOSI 2
#define RTS_FP_PIN_CACHE_SCK  3
#define RTS_FP_PIN_CACHE_WP   4
#define RTS_FP_PIN_CACHE_HOLD 5
#define RTS_FP_PIN_CACHE_CS2  6
#define RTS_FP_PIN_SNR_MISO   7
#define RTS_FP_PIN_SNR_MOSI   8
#define RTS_FP_PIN_SNR_CLK    9
#define RTS_FP_PIN_SSI_M_MISO 10
#define RTS_FP_PIN_SSI_M_MOSI 11
#define RTS_FP_PIN_SSI_M_CS   12
#define RTS_FP_PIN_SSI_M_SCK  13
#define RTS_FP_PIN_SCL0       14
#define RTS_FP_PIN_SDA0       15
#define RTS_FP_PIN_SCL2       16
#define RTS_FP_PIN_SDA2       17
#define RTS_FP_PIN_SCL1       18
#define RTS_FP_PIN_SDA1       19
#define RTS_FP_PIN_SSI_S_MISO 20
#define RTS_FP_PIN_SSI_S_MOSI 21
#define RTS_FP_PIN_SSI_S_CS   22
#define RTS_FP_PIN_SSI_S_SCK  23
#define RTS_FP_PIN_GPIO14     24
#define RTS_FP_PIN_GPIO15     25
#define RTS_FP_PIN_AL0        26
#define RTS_FP_PIN_AL1        27
#define RTS_FP_PIN_AL2        28
#define RTS_FP_PIN_SNR_RST    29
#define RTS_FP_PIN_SNR_CS     30
#define RTS_FP_PIN_SNR_GPIO   31

#define P_CACHE_CS2_F_CACHE_CS2 RTS_FP_PINMUX(CACHE_CS2, FUNC0)
#define P_CACHE_CS2_F_GPIO      RTS_FP_PINMUX(CACHE_CS2, FUNC1)

#define P_SNR_MISO_F_SNR_MISO RTS_FP_PINMUX(SNR_MISO, FUNC0)
#define P_SNR_MOSI_F_SNR_MOSI RTS_FP_PINMUX(SNR_MOSI, FUNC0)
#define P_SNR_CLK_F_SNR_CLK   RTS_FP_PINMUX(SNR_CLK, FUNC0)

#define P_SSI_M_MISO_F_GPIO       RTS_FP_PINMUX(SSI_M_MISO, FUNC0)
#define P_SSI_M_MISO_F_PWM        RTS_FP_PINMUX(SSI_M_MISO, FUNC1)
#define P_SSI_M_MISO_F_SSI_M_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC2)
#define P_SSI_M_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_M_MISO, FUNC3)
#define P_SSI_M_MISO_F_UART1_RX   RTS_FP_PINMUX(SSI_M_MISO, FUNC4)
#define P_SSI_M_MISO_F_ASIC_DBG   RTS_FP_PINMUX(SSI_M_MISO, FUNC5)

#define P_SSI_M_MOSI_F_GPIO       RTS_FP_PINMUX(SSI_M_MOSI, FUNC0)
#define P_SSI_M_MOSI_F_PWM        RTS_FP_PINMUX(SSI_M_MOSI, FUNC1)
#define P_SSI_M_MOSI_F_SSI_M_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC2)
#define P_SSI_M_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_M_MOSI, FUNC3)
#define P_SSI_M_MOSI_F_UART1_TX   RTS_FP_PINMUX(SSI_M_MOSI, FUNC4)
#define P_SSI_M_MOSI_F_ASIC_DBG   RTS_FP_PINMUX(SSI_M_MOSI, FUNC5)

#define P_SSI_M_CS_F_GPIO      RTS_FP_PINMUX(SSI_M_CS, FUNC0)
#define P_SSI_M_CS_F_PWM       RTS_FP_PINMUX(SSI_M_CS, FUNC1)
#define P_SSI_M_CS_F_SSI_M_CS  RTS_FP_PINMUX(SSI_M_CS, FUNC2)
#define P_SSI_M_CS_F_SSI_S_CS  RTS_FP_PINMUX(SSI_M_CS, FUNC3)
#define P_SSI_M_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_M_CS, FUNC4)
#define P_SSI_M_CS_F_ASIC_DBG  RTS_FP_PINMUX(SSI_M_CS, FUNC5)

#define P_SSI_M_SCK_F_GPIO      RTS_FP_PINMUX(SSI_M_SCK, FUNC0)
#define P_SSI_M_SCK_F_PWM       RTS_FP_PINMUX(SSI_M_SCK, FUNC1)
#define P_SSI_M_SCK_F_SSI_M_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC2)
#define P_SSI_M_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_M_SCK, FUNC3)
#define P_SSI_M_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_M_SCK, FUNC4)
#define P_SSI_M_SCK_F_ASIC_DBG  RTS_FP_PINMUX(SSI_M_SCK, FUNC5)

#define P_SCL0_F_GPIO     RTS_FP_PINMUX(SCL0, FUNC0)
#define P_SCL0_F_PWM      RTS_FP_PINMUX(SCL0, FUNC1)
#define P_SCL0_F_I2C0_SCL RTS_FP_PINMUX(SCL0, FUNC2)
#define P_SCL0_F_UART0_RX RTS_FP_PINMUX(SCL0, FUNC3)
#define P_SCL0_F_SWD_CLK  RTS_FP_PINMUX(SCL0, FUNC4)
#define P_SCL0_F_ASIC_DBG RTS_FP_PINMUX(SCL0, FUNC5)

#define P_SDA0_F_GPIO     RTS_FP_PINMUX(SDA0, FUNC0)
#define P_SDA0_F_PWM      RTS_FP_PINMUX(SDA0, FUNC1)
#define P_SDA0_F_I2C0_SDA RTS_FP_PINMUX(SDA0, FUNC2)
#define P_SDA0_F_UART0_TX RTS_FP_PINMUX(SDA0, FUNC3)
#define P_SDA0_F_SWD_DAT  RTS_FP_PINMUX(SDA0, FUNC4)
#define P_SDA0_F_ASIC_DBG RTS_FP_PINMUX(SDA0, FUNC5)

#define P_SCL2_F_GPIO     RTS_FP_PINMUX(SCL2, FUNC0)
#define P_SCL2_F_PWM      RTS_FP_PINMUX(SCL2, FUNC1)
#define P_SCL2_F_I2C2_SCL RTS_FP_PINMUX(SCL2, FUNC2)
#define P_SCL2_F_UART0_RX RTS_FP_PINMUX(SCL2, FUNC3)
#define P_SCL2_F_SWD_CLK  RTS_FP_PINMUX(SCL2, FUNC4)
#define P_SCL2_F_ASIC_DBG RTS_FP_PINMUX(SCL2, FUNC5)

#define P_SDA2_F_GPIO     RTS_FP_PINMUX(SDA2, FUNC0)
#define P_SDA2_F_PWM      RTS_FP_PINMUX(SDA2, FUNC1)
#define P_SDA2_F_I2C2_SDA RTS_FP_PINMUX(SDA2, FUNC2)
#define P_SDA2_F_UART0_TX RTS_FP_PINMUX(SDA2, FUNC3)
#define P_SDA2_F_SWD_DAT  RTS_FP_PINMUX(SDA2, FUNC4)
#define P_SDA2_F_ASIC_DBG RTS_FP_PINMUX(SDA2, FUNC5)

#define P_SCL1_F_GPIO     RTS_FP_PINMUX(SCL1, FUNC0)
#define P_SCL1_F_PWM      RTS_FP_PINMUX(SCL1, FUNC1)
#define P_SCL1_F_I2C1_SCL RTS_FP_PINMUX(SCL1, FUNC2)
#define P_SCL1_F_JTAG_TCK RTS_FP_PINMUX(SCL1, FUNC4)

#define P_SDA1_F_GPIO     RTS_FP_PINMUX(SDA1, FUNC0)
#define P_SDA1_F_PWM      RTS_FP_PINMUX(SDA1, FUNC1)
#define P_SDA1_F_I2C1_SDA RTS_FP_PINMUX(SDA1, FUNC2)
#define P_SDA1_F_JTAG_TMS RTS_FP_PINMUX(SDA1, FUNC4)

#define P_SSI_S_MISO_F_GPIO       RTS_FP_PINMUX(SSI_S_MISO, FUNC0)
#define P_SSI_S_MISO_F_PWM        RTS_FP_PINMUX(SSI_S_MISO, FUNC1)
#define P_SSI_S_MISO_F_SSI_S_MISO RTS_FP_PINMUX(SSI_S_MISO, FUNC2)
#define P_SSI_S_MISO_F_UART1_RX   RTS_FP_PINMUX(SSI_S_MISO, FUNC3)
#define P_SSI_S_MISO_F_JTAG_TDI   RTS_FP_PINMUX(SSI_S_MISO, FUNC4)

#define P_SSI_S_MOSI_F_GPIO       RTS_FP_PINMUX(SSI_S_MOSI, FUNC0)
#define P_SSI_S_MOSI_F_PWM        RTS_FP_PINMUX(SSI_S_MOSI, FUNC1)
#define P_SSI_S_MOSI_F_SSI_S_MOSI RTS_FP_PINMUX(SSI_S_MOSI, FUNC2)
#define P_SSI_S_MOSI_F_UART1_TX   RTS_FP_PINMUX(SSI_S_MOSI, FUNC3)
#define P_SSI_S_MOSI_F_JTAG_TRST  RTS_FP_PINMUX(SSI_S_MOSI, FUNC4)

#define P_SSI_S_CS_F_GPIO      RTS_FP_PINMUX(SSI_S_CS, FUNC0)
#define P_SSI_S_CS_F_PWM       RTS_FP_PINMUX(SSI_S_CS, FUNC1)
#define P_SSI_S_CS_F_SSI_S_CS  RTS_FP_PINMUX(SSI_S_CS, FUNC2)
#define P_SSI_S_CS_F_UART1_RTS RTS_FP_PINMUX(SSI_S_CS, FUNC3)
#define P_SSI_S_CS_F_JTAG_TDO  RTS_FP_PINMUX(SSI_S_CS, FUNC4)

#define P_SSI_S_SCK_F_GPIO      RTS_FP_PINMUX(SSI_S_SCK, FUNC0)
#define P_SSI_S_SCK_F_PWM       RTS_FP_PINMUX(SSI_S_SCK, FUNC1)
#define P_SSI_S_SCK_F_SSI_S_CLK RTS_FP_PINMUX(SSI_S_SCK, FUNC2)
#define P_SSI_S_SCK_F_UART1_CTS RTS_FP_PINMUX(SSI_S_SCK, FUNC3)

#define P_GPIO14_F_GPIO     RTS_FP_PINMUX(GPIO14, FUNC0)
#define P_GPIO14_F_PWM      RTS_FP_PINMUX(GPIO14, FUNC1)
#define P_GPIO14_F_UART0_RX RTS_FP_PINMUX(GPIO14, FUNC2)

#define P_GPIO15_F_GPIO     RTS_FP_PINMUX(GPIO15, FUNC0)
#define P_GPIO15_F_PWM      RTS_FP_PINMUX(GPIO15, FUNC1)
#define P_GPIO15_F_UART0_TX RTS_FP_PINMUX(GPIO15, FUNC2)

#define P_AL0_F_GPIO      RTS_FP_PINMUX(AL0, FUNC0)
#define P_AL0_F_PWM       RTS_FP_PINMUX(AL0, FUNC1)
#define P_AL0_F_CS_BRIDGE RTS_FP_PINMUX(AL0, FUNC2)

#define P_AL1_F_GPIO RTS_FP_PINMUX(AL1, FUNC0)
#define P_AL1_F_PWM  RTS_FP_PINMUX(AL1, FUNC1)

#define P_AL2_F_GPIO RTS_FP_PINMUX(AL2, FUNC0)
#define P_AL2_F_PWM  RTS_FP_PINMUX(AL2, FUNC1)

#define P_SNR_RST_F_SNR_RST RTS_FP_PINMUX(SNR_RST, FUNC0)

#define P_SNR_CS_F_SNR_CS RTS_FP_PINMUX(SNR_CS, FUNC0)
#define P_SNR_CS_F_GPIO   RTS_FP_PINMUX(SNR_CS, FUNC1)

#define P_SNR_GPIO_F_GPIO RTS_FP_PINMUX(SNR_GPIO, FUNC0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTS5817_PINCTRL_H_ */
```

## 739.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Realtek Semiconductor, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 194 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RTS5817_PINCTRL_H_`。

## 739.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rts5817__pinctrl_8h.html)

---

[上一章](P738_rts5817_intc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P740_rts5817_reset.h_源码浏览.md)
