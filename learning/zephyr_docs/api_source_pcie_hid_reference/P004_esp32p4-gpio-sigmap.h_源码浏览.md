---
id: learning.zephyr-docs.api-source-pcie-hid-reference.page-4
title: esp32p4-gpio-sigmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_esp32p4-gpio-sigmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h.html)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
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

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * Derived from components/soc/esp32p4/include/soc/gpio_sig_map.h
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32P4_GPIO_SIGMAP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32P4_GPIO_SIGMAP_H_

#define ESP_NOSIG ESP_SIG_INVAL

/* UART0 */
#define ESP_U0RXD_IN  10
#define ESP_U0TXD_OUT 10
#define ESP_U0CTS_IN  11
#define ESP_U0RTS_OUT 11
#define ESP_U0DSR_IN  12
#define ESP_U0DTR_OUT 12

/* UART1 */
#define ESP_U1RXD_IN  13
#define ESP_U1TXD_OUT 13
#define ESP_U1CTS_IN  14
#define ESP_U1RTS_OUT 14
#define ESP_U1DSR_IN  15
#define ESP_U1DTR_OUT 15

/* UART2 */
#define ESP_U2RXD_IN  16
#define ESP_U2TXD_OUT 16
#define ESP_U2CTS_IN  17
#define ESP_U2RTS_OUT 17
#define ESP_U2DSR_IN  18
#define ESP_U2DTR_OUT 18

/* UART3 */
#define ESP_U3RXD_IN  19
#define ESP_U3TXD_OUT 19
#define ESP_U3CTS_IN  20
#define ESP_U3RTS_OUT 20
#define ESP_U3DSR_IN  21
#define ESP_U3DTR_OUT 21

/* UART4 */
#define ESP_U4RXD_IN  22
#define ESP_U4TXD_OUT 22
#define ESP_U4CTS_IN  23
#define ESP_U4RTS_OUT 23
#define ESP_U4DSR_IN  24
#define ESP_U4DTR_OUT 24

/* I2S1 */
#define ESP_I2S1_O_BCK_IN  31
#define ESP_I2S1_O_BCK_OUT 31
#define ESP_I2S1_MCLK_IN   32
#define ESP_I2S1_MCLK_OUT  32
#define ESP_I2S1_O_WS_IN   33
#define ESP_I2S1_O_WS_OUT  33
#define ESP_I2S1_I_SD_IN   34
#define ESP_I2S1_O_SD_OUT  34
#define ESP_I2S1_I_BCK_IN  35
#define ESP_I2S1_I_BCK_OUT 35
#define ESP_I2S1_I_WS_IN   36
#define ESP_I2S1_I_WS_OUT  36

/* I2S2 */
#define ESP_I2S2_O_BCK_IN  37
#define ESP_I2S2_O_BCK_OUT 37
#define ESP_I2S2_MCLK_IN   38
#define ESP_I2S2_MCLK_OUT  38
#define ESP_I2S2_O_WS_IN   39
#define ESP_I2S2_O_WS_OUT  39
#define ESP_I2S2_I_SD_IN   40
#define ESP_I2S2_O_SD_OUT  40
#define ESP_I2S2_I_BCK_IN  41
#define ESP_I2S2_I_BCK_OUT 41
#define ESP_I2S2_I_WS_IN   42
#define ESP_I2S2_I_WS_OUT  42

/* SPI3 */
#define ESP_SPI3_CS2_OUT  45
#define ESP_SPI3_CS1_OUT  46
#define ESP_SPI3_CK_IN    47
#define ESP_SPI3_CK_OUT   47
#define ESP_SPI3_Q_IN     48
#define ESP_SPI3_QO_OUT   48
#define ESP_SPI3_D_IN     49
#define ESP_SPI3_D_OUT    49
#define ESP_SPI3_HOLD_IN  50
#define ESP_SPI3_HOLD_OUT 50
#define ESP_SPI3_WP_IN    51
#define ESP_SPI3_WP_OUT   51
#define ESP_SPI3_CS_IN    52
#define ESP_SPI3_CS_OUT   52

/* SPI2 (FSPI) */
#define ESP_FSPICLK_IN  53
#define ESP_FSPICLK_OUT 53
#define ESP_FSPIQ_IN    54
#define ESP_FSPIQ_OUT   54
#define ESP_FSPID_IN    55
#define ESP_FSPID_OUT   55
#define ESP_FSPIHD_IN   56
#define ESP_FSPIHD_OUT  56
#define ESP_FSPIWP_IN   57
#define ESP_FSPIWP_OUT  57
#define ESP_FSPICS0_IN  62
#define ESP_FSPICS0_OUT 62

/* I2C0 */
#define ESP_I2CEXT0_SCL_IN  68
#define ESP_I2CEXT0_SCL_OUT 68
#define ESP_I2CEXT0_SDA_IN  69
#define ESP_I2CEXT0_SDA_OUT 69

/* I2C1 */
#define ESP_I2CEXT1_SCL_IN  70
#define ESP_I2CEXT1_SCL_OUT 70
#define ESP_I2CEXT1_SDA_IN  71
#define ESP_I2CEXT1_SDA_OUT 71

/* I2S0 */
#define ESP_I2S0_O_BCK_IN  25
#define ESP_I2S0_O_BCK_OUT 25
#define ESP_I2S0_MCLK_IN   26
#define ESP_I2S0_MCLK_OUT  26
#define ESP_I2S0_O_WS_IN   27
#define ESP_I2S0_O_WS_OUT  27
#define ESP_I2S0_I_SD_IN   28
#define ESP_I2S0_O_SD_OUT  28
#define ESP_I2S0_O_SD1_OUT 43
#define ESP_I2S0_I_BCK_IN  29
#define ESP_I2S0_I_BCK_OUT 29
#define ESP_I2S0_I_WS_IN   30
#define ESP_I2S0_I_WS_OUT  30

/* TWAI1 */
#define ESP_TWAI1_RX 83
#define ESP_TWAI1_TX 83

/* TWAI2 */
#define ESP_TWAI2_RX 86
#define ESP_TWAI2_TX 86

/* MCPWM0 */
#define ESP_PWM0_SYNC0_IN  89
#define ESP_PWM0_OUT0A     89
#define ESP_PWM0_CH0_A_OUT 89
#define ESP_PWM0_SYNC1_IN  90
#define ESP_PWM0_OUT0B     90
#define ESP_PWM0_CH0_B_OUT 90
#define ESP_PWM0_SYNC2_IN  91
#define ESP_PWM0_OUT1A     91
#define ESP_PWM0_CH1_A_OUT 91
#define ESP_PWM0_F0_IN     92
#define ESP_PWM0_OUT1B     92
#define ESP_PWM0_CH1_B_OUT 92
#define ESP_PWM0_F1_IN     93
#define ESP_PWM0_OUT2A     93
#define ESP_PWM0_CH2_A_OUT 93
#define ESP_PWM0_F2_IN     94
#define ESP_PWM0_OUT2B     94
#define ESP_PWM0_CH2_B_OUT 94
#define ESP_PWM0_CAP0_IN   95
#define ESP_PWM0_CAP1_IN   96
#define ESP_PWM0_CAP2_IN   97

/* MCPWM1 */
#define ESP_PWM1_CH0_A_OUT 95
#define ESP_PWM1_CH0_B_OUT 96
#define ESP_PWM1_CH1_A_OUT 97
#define ESP_PWM1_SYNC0_IN  98
#define ESP_PWM1_CH1_B_OUT 98
#define ESP_PWM1_SYNC1_IN  99
#define ESP_PWM1_CH2_A_OUT 99
#define ESP_PWM1_SYNC2_IN  100
#define ESP_PWM1_CH2_B_OUT 100
#define ESP_PWM1_F0_IN     101
#define ESP_PWM1_F1_IN     102
#define ESP_PWM1_F2_IN     103
#define ESP_PWM1_CAP0_IN   104
#define ESP_PWM1_CAP1_IN   105
#define ESP_PWM1_CAP2_IN   106

/* TWAI0 */
#define ESP_TWAI0_RX 80
#define ESP_TWAI0_TX 80

/* LEDC */
#define ESP_LEDC_LS_SIG_OUT0 126
#define ESP_LEDC_LS_SIG_OUT1 127
#define ESP_LEDC_LS_SIG_OUT2 128
#define ESP_LEDC_LS_SIG_OUT3 129
#define ESP_LEDC_LS_SIG_OUT4 130
#define ESP_LEDC_LS_SIG_OUT5 131
#define ESP_LEDC_LS_SIG_OUT6 132
#define ESP_LEDC_LS_SIG_OUT7 133

/* PCNT */
#define ESP_PCNT_SIG_CH0_IN0  141
#define ESP_PCNT_SIG_CH0_IN1  142
#define ESP_PCNT_SIG_CH0_IN2  143
#define ESP_PCNT_SIG_CH0_IN3  144
#define ESP_PCNT_SIG_CH1_IN0  145
#define ESP_PCNT_SIG_CH1_IN1  146
#define ESP_PCNT_SIG_CH1_IN2  147
#define ESP_PCNT_SIG_CH1_IN3  148
#define ESP_PCNT_CTRL_CH0_IN0 149
#define ESP_PCNT_CTRL_CH0_IN1 150
#define ESP_PCNT_CTRL_CH0_IN2 151
#define ESP_PCNT_CTRL_CH0_IN3 152
#define ESP_PCNT_CTRL_CH1_IN0 153
#define ESP_PCNT_CTRL_CH1_IN1 154
#define ESP_PCNT_CTRL_CH1_IN2 155
#define ESP_PCNT_CTRL_CH1_IN3 156

/* EMAC */
#define ESP_EMAC_MDI_I 107
#define ESP_EMAC_MDC_O 108
#define ESP_EMAC_MDO_O 109

/* PCNT */
#define ESP_PCNT_SIG_CH0_IN0  141
#define ESP_PCNT_SIG_CH0_IN1  142
#define ESP_PCNT_SIG_CH0_IN2  143
#define ESP_PCNT_SIG_CH0_IN3  144
#define ESP_PCNT_SIG_CH1_IN0  145
#define ESP_PCNT_SIG_CH1_IN1  146
#define ESP_PCNT_SIG_CH1_IN2  147
#define ESP_PCNT_SIG_CH1_IN3  148
#define ESP_PCNT_CTRL_CH0_IN0 149
#define ESP_PCNT_CTRL_CH0_IN1 150
#define ESP_PCNT_CTRL_CH0_IN2 151
#define ESP_PCNT_CTRL_CH0_IN3 152
#define ESP_PCNT_CTRL_CH1_IN0 153
#define ESP_PCNT_CTRL_CH1_IN1 154
#define ESP_PCNT_CTRL_CH1_IN2 155
#define ESP_PCNT_CTRL_CH1_IN3 156

/* RMT */
#define ESP_RMT_SIG_IN0  246
#define ESP_RMT_SIG_OUT0 246
#define ESP_RMT_SIG_IN1  247
#define ESP_RMT_SIG_OUT1 247
#define ESP_RMT_SIG_IN2  248
#define ESP_RMT_SIG_OUT2 248
#define ESP_RMT_SIG_IN3  249
#define ESP_RMT_SIG_OUT3 249

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32P4_GPIO_SIGMAP_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

派生自 `components/soc/esp32p4/include/soc/gpio_sig_map.h`。

### 注释 2：原第 21 行

通用异步收发器 UART0。

### 注释 3：原第 29 行

通用异步收发器 UART1。

### 注释 4：原第 37 行

通用异步收发器 UART2。

### 注释 5：原第 45 行

通用异步收发器 UART3。

### 注释 6：原第 53 行

通用异步收发器 UART4。

### 注释 7：原第 61 行

音频总线 I2S1。

### 注释 8：原第 75 行

音频总线 I2S2。

### 注释 9：原第 89 行

串行外设接口 SPI3。

### 注释 10：原第 105 行

串行外设接口 SPI2（FSPI）。

### 注释 11：原第 119 行

集成电路间总线 I2C0。

### 注释 12：原第 125 行

集成电路间总线 I2C1。

### 注释 13：原第 131 行

音频总线 I2S0。

### 注释 14：原第 146 行

双线汽车接口 TWAI1。

### 注释 15：原第 150 行

双线汽车接口 TWAI2。

### 注释 16：原第 154 行

电机控制脉宽调制 MCPWM0。

### 注释 17：原第 177 行

电机控制脉宽调制 MCPWM1。

### 注释 18：原第 194 行

双线汽车接口 TWAI0。

### 注释 19：原第 198 行

LED 控制器（LEDC）。

### 注释 20：原第 208 行

脉冲计数器（PCNT）。

### 注释 21：原第 226 行

以太网媒体访问控制器（EMAC）。

### 注释 22：原第 231 行

脉冲计数器（PCNT）。

### 注释 23：原第 249 行

远程控制模块（RMT）。

### 注释 24：原第 259 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32P4_GPIO_SIGMAP_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h.html)

---

[上一章](P003_esp32c5-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_hfp_ag.h_源码浏览.md)
