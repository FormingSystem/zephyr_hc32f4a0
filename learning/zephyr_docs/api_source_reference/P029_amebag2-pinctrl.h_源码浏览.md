---
id: learning.zephyr-docs.api-source-reference.page-29
title: amebag2-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_amebag2-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h.html)。

## 29.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00014"></a>
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
<a id="l00175"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAG2_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAG2_PINCTRL_H_


#define AMEBA_GPIO           0
#define AMEBA_LOG_UART       1
#define AMEBA_SPIC0_FLASH    2
#define AMEBA_SPIC1_FLASH    3
#define AMEBA_SPIC1_PSRAM    4
#define AMEBA_ADC            5
#define AMEBA_CAP_TOUCH      5
#define AMEBA_TSSI           6
#define AMEBA_USB            7
#define AMEBA_RMII           8
#define AMEBA_SPI0           9
#define AMEBA_SPI1           10
#define AMEBA_SWD            11
#define AMEBA_SDIO_MST       12
#define AMEBA_SDIO_SLV       13
#define AMEBA_SIC            14
#define AMEBA_BT_IO          15
#define AMEBA_BT             16
#define AMEBA_DEBUG          17
#define AMEBA_I2S0_BCLK      32
#define AMEBA_I2S0_MCLK      33
#define AMEBA_I2S0_WS        34
#define AMEBA_I2S0_DIO0      35
#define AMEBA_I2S0_DIO1      36
#define AMEBA_I2S0_DIO2      37
#define AMEBA_I2S0_DIO3      38
#define AMEBA_LCD_RGB_DCLK   39
#define AMEBA_LCD_MCU_WR     39
#define AMEBA_LCD_RGB_DE     40
#define AMEBA_LCD_MCU_CSX    40
#define AMEBA_LCD_RGB_HSYNC  41
#define AMEBA_LCD_MCU_RD     41
#define AMEBA_LCD_RGB_TE     42
#define AMEBA_LCD_MCU_TE     42
#define AMEBA_LCD_RGB_VSYNC  43
#define AMEBA_LCD_MCU_VSYNC  43
#define AMEBA_LCD_MCU_DCX    44
#define AMEBA_LCD_D0         45
#define AMEBA_LCD_D1         46
#define AMEBA_LCD_D2         47
#define AMEBA_LCD_D3         48
#define AMEBA_LCD_D4         49
#define AMEBA_LCD_D5         50
#define AMEBA_LCD_D6         51
#define AMEBA_LCD_D7         52
#define AMEBA_LCD_D8         53
#define AMEBA_LCD_D9         54
#define AMEBA_LCD_D10        55
#define AMEBA_LCD_D11        56
#define AMEBA_LCD_D12        57
#define AMEBA_LCD_D13        58
#define AMEBA_LCD_D14        59
#define AMEBA_LCD_D15        60
#define AMEBA_LCD_D16        61
#define AMEBA_LCD_D17        62
#define AMEBA_LCD_D18        63
#define AMEBA_LCD_D19        64
#define AMEBA_LCD_D20        65
#define AMEBA_LCD_D21        66
#define AMEBA_LCD_D22        67
#define AMEBA_LCD_D23        68
#define AMEBA_SD_M_CLK       69
#define AMEBA_SD_M_CMD       70
#define AMEBA_SD_M_D0        71
#define AMEBA_SD_M_D1        72
#define AMEBA_SD_M_D2        73
#define AMEBA_SD_M_D3        74
#define AMEBA_SPI0_CLK       75
#define AMEBA_SPI0_MISO      76
#define AMEBA_SPI0_MOSI      77
#define AMEBA_SPI0_CS        78
#define AMEBA_SPI1_CLK       79
#define AMEBA_SPI1_MISO      80
#define AMEBA_SPI1_MOSI      81
#define AMEBA_SPI1_CS        82
#define AMEBA_SWD_CLK        83
#define AMEBA_SWD_DAT        84
#define AMEBA_DMIC_CLK       85
#define AMEBA_DMIC_DATA      86
#define AMEBA_LED_SCL        87
#define AMEBA_LED_SDA        88
#define AMEBA_I2C0_SCL       89
#define AMEBA_I2C0_SDA       90
#define AMEBA_I2C1_SCL       91
#define AMEBA_I2C1_SDA       92
#define AMEBA_RMII_MDIO      93
#define AMEBA_RMII_MDC       94
#define AMEBA_UART0_TXD      95
#define AMEBA_UART0_RXD      96
#define AMEBA_UART0_CTS      97
#define AMEBA_UART0_RTS      98
#define AMEBA_UART1_TXD      99
#define AMEBA_UART1_RXD      100
#define AMEBA_UART2_TXD      101
#define AMEBA_UART2_RXD      102
#define AMEBA_UART3_TXD      103
#define AMEBA_UART3_RXD      104
#define AMEBA_UART3_CTS      105
#define AMEBA_UART3_RTS      106
#define AMEBA_A2C0_TX        107
#define AMEBA_A2C0_RX        108
#define AMEBA_A2C1_TX        109
#define AMEBA_A2C1_RX        110
#define AMEBA_TIM4_PWM0      111
#define AMEBA_TIM4_PWM1      112
#define AMEBA_TIM4_PWM2      113
#define AMEBA_TIM4_PWM3      114
#define AMEBA_TIM5_PWM0      115
#define AMEBA_TIM5_PWM1      116
#define AMEBA_TIM5_PWM2      117
#define AMEBA_TIM5_PWM3      118
#define AMEBA_TIM6_PWM0      119
#define AMEBA_TIM6_PWM1      120
#define AMEBA_TIM6_PWM2      121
#define AMEBA_TIM6_PWM3      122
#define AMEBA_TIM7_PWM0      123
#define AMEBA_TIM7_PWM1      124
#define AMEBA_TIM7_PWM2      125
#define AMEBA_TIM7_PWM3      126
#define AMEBA_PWM_TIM4_TRIG  127
#define AMEBA_PWM_TIM5_TRIG  128
#define AMEBA_PWM_TIM6_TRIG  129
#define AMEBA_PWM_TIM7_TRIG  130
#define AMEBA_CAPT_TIM8_TRIG 131
#define AMEBA_IR_TX          132
#define AMEBA_IR_RX          133
#define AMEBA_ANT_SEL_P      134
#define AMEBA_ANT_SEL_N      135
#define AMEBA_TRSW_P         136
#define AMEBA_TRSW_N         137
#define AMEBA_PA_EN0         138
#define AMEBA_LNA_EN0        139
#define AMEBA_PA_EN1         140
#define AMEBA_LNA_EN1        141
#define AMEBA_BT_CLK_REQ     142
#define AMEBA_WLAN_ACT       143
#define AMEBA_BT_ACT         144
#define AMEBA_BT_STE         145
#define AMEBA_BT_CK          146
#define AMEBA_ZB_REQ         147
#define AMEBA_ZB_GRANT       148
#define AMEBA_ZB_PRI         149
#define AMEBA_BT_ANT_SW0     150
#define AMEBA_BT_ANT_SW1     151
#define AMEBA_BT_ANT_SW2     152
#define AMEBA_BT_ANT_SW3     153
#define AMEBA_EXT_CLK50M_IN  154
#define AMEBA_EXT_CLK_OUT    155
#define AMEBA_UART_LOG_RXD   156
#define AMEBA_UART_LOG_TXD   157
#define AMEBA_SIC_CLK        158
#define AMEBA_SIC_DAT        159
#define AMEBA_BT_FWLOG       160
#define AMEBA_BT_I2C_SDA     161
#define AMEBA_BT_I2C_SCL     162

#define AMEBA_PORT_PIN(port, line) ((((port) - 'A') << 5) + (line))

#define AMEBA_PINMUX(port, line, funcid) (((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAG2_PINCTRL_H_ */
```

## 29.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 188 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBAG2_PINCTRL_H_`。

## 29.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebag2-pinctrl_8h.html)

---

[上一章](P028_ameba_dma.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P030_andes_flash_xip_api_ex.h_源码浏览.md)
