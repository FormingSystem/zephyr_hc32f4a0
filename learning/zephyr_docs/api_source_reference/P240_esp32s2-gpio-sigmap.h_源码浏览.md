---
id: learning.zephyr-docs.api-source-reference.page-240
title: esp32s2-gpio-sigmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-gpio-sigmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第240章\_esp32s2-gpio-sigmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-gpio-sigmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-gpio-sigmap_8h.html)。

## 240.1\_原始可见代码（Source Code）

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
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
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
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00325"></a>
<a id="l00326"></a>

```c
/*
 * Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32S2_GPIO_SIGMAP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32S2_GPIO_SIGMAP_H_


#define ESP_NOSIG                       ESP_SIG_INVAL

#define ESP_SPICLK_OUT                  ESP_SPICLK_OUT_MUX
#define ESP_CLK_I2S                     ESP_CLK_I2S_MUX
#define ESP_FSPICLK_OUT                 ESP_FSPICLK_OUT_MUX

#define ESP_SPIQ_IN                     0
#define ESP_SPIQ_OUT                    0
#define ESP_SPID_IN                     1
#define ESP_SPID_OUT                    1
#define ESP_SPIHD_IN                    2
#define ESP_SPIHD_OUT                   2
#define ESP_SPIWP_IN                    3
#define ESP_SPIWP_OUT                   3
#define ESP_SPICLK_OUT_MUX              4
#define ESP_SPICS0_OUT                  5
#define ESP_SPICS1_OUT                  6
#define ESP_SPID4_IN                    7
#define ESP_SPID4_OUT                   7
#define ESP_SPID5_IN                    8
#define ESP_SPID5_OUT                   8
#define ESP_SPID6_IN                    9
#define ESP_SPID6_OUT                   9
#define ESP_SPID7_IN                    10
#define ESP_SPID7_OUT                   10
#define ESP_SPIDQS_IN                   11
#define ESP_SPIDQS_OUT                  11
#define ESP_U0RXD_IN                    14
#define ESP_U0TXD_OUT                   14
#define ESP_U0CTS_IN                    15
#define ESP_U0RTS_OUT                   15
#define ESP_U0DSR_IN                    16
#define ESP_U0DTR_OUT                   16
#define ESP_U1RXD_IN                    17
#define ESP_U1TXD_OUT                   17
#define ESP_U1CTS_IN                    18
#define ESP_U1RTS_OUT                   18
#define ESP_U1DSR_IN                    21
#define ESP_U1DTR_OUT                   21
#define ESP_I2S0O_BCK_IN                23
#define ESP_I2S0O_BCK_OUT               23
#define ESP_I2S0O_WS_IN                 25
#define ESP_I2S0O_WS_OUT                25
#define ESP_I2S0I_BCK_IN                27
#define ESP_I2S0I_BCK_OUT               27
#define ESP_I2S0I_WS_IN                 28
#define ESP_I2S0I_WS_OUT                28
#define ESP_I2CEXT0_SCL_IN              29
#define ESP_I2CEXT0_SCL_OUT             29
#define ESP_I2CEXT0_SDA_IN              30
#define ESP_I2CEXT0_SDA_OUT             30
#define ESP_SDIO_TOHOST_INT_OUT         31
#define ESP_GPIO_BT_ACTIVE              37
#define ESP_GPIO_BT_PRIORITY            38
#define ESP_PCNT_SIG_CH0_IN0            39
#define ESP_GPIO_WLAN_PRIO              39
#define ESP_PCNT_SIG_CH1_IN0            40
#define ESP_GPIO_WLAN_ACTIVE            40
#define ESP_PCNT_CTRL_CH0_IN0           41
#define ESP_BB_DIAG0                    41
#define ESP_PCNT_CTRL_CH1_IN0           42
#define ESP_BB_DIAG1                    42
#define ESP_PCNT_SIG_CH0_IN1            43
#define ESP_BB_DIAG2                    43
#define ESP_PCNT_SIG_CH1_IN1            44
#define ESP_BB_DIAG3                    44
#define ESP_PCNT_CTRL_CH0_IN1           45
#define ESP_BB_DIAG4                    45
#define ESP_PCNT_CTRL_CH1_IN1           46
#define ESP_BB_DIAG5                    46
#define ESP_PCNT_SIG_CH0_IN2            47
#define ESP_BB_DIAG6                    47
#define ESP_PCNT_SIG_CH1_IN2            48
#define ESP_BB_DIAG7                    48
#define ESP_PCNT_CTRL_CH0_IN2           49
#define ESP_BB_DIAG8                    49
#define ESP_PCNT_CTRL_CH1_IN2           50
#define ESP_BB_DIAG9                    50
#define ESP_PCNT_SIG_CH0_IN3            51
#define ESP_BB_DIAG10                   51
#define ESP_PCNT_SIG_CH1_IN3            52
#define ESP_BB_DIAG11                   52
#define ESP_PCNT_CTRL_CH0_IN3           53
#define ESP_BB_DIAG12                   53
#define ESP_PCNT_CTRL_CH1_IN3           54
#define ESP_BB_DIAG13                   54
#define ESP_BB_DIAG14                   55
#define ESP_BB_DIAG15                   56
#define ESP_BB_DIAG16                   57
#define ESP_BB_DIAG17                   58
#define ESP_BB_DIAG18                   59
#define ESP_BB_DIAG19                   60
#define ESP_USB_EXTPHY_VP               61
#define ESP_USB_EXTPHY_OEN              61
#define ESP_USB_EXTPHY_VM               62
#define ESP_USB_EXTPHY_SPEED            62
#define ESP_USB_EXTPHY_RCV              63
#define ESP_USB_EXTPHY_VPO              63
#define ESP_USB_OTG_IDDIG_IN            64
#define ESP_USB_EXTPHY_VMO              64
#define ESP_USB_OTG_AVALID_IN           65
#define ESP_USB_EXTPHY_SUSPND           65
#define ESP_USB_SRP_BVALID_IN           66
#define ESP_USB_OTG_IDPULLUP            66
#define ESP_USB_OTG_VBUSVALID_IN        67
#define ESP_USB_OTG_DPPULLDOWN          67
#define ESP_USB_SRP_SESSEND_IN          68
#define ESP_USB_OTG_DMPULLDOWN          68
#define ESP_USB_OTG_DRVVBUS             69
#define ESP_USB_SRP_CHRGVBUS            70
#define ESP_USB_SRP_DISCHRGVBUS         71
#define ESP_SPI3_CLK_IN                 72
#define ESP_SPI3_CLK_OUT_MUX            72
#define ESP_SPI3_Q_IN                   73
#define ESP_SPI3_Q_OUT                  73
#define ESP_SPI3_D_IN                   74
#define ESP_SPI3_D_OUT                  74
#define ESP_SPI3_HD_IN                  75
#define ESP_SPI3_HD_OUT                 75
#define ESP_SPI3_CS0_IN                 76
#define ESP_SPI3_CS0_OUT                76
#define ESP_SPI3_CS1_OUT                77
#define ESP_SPI3_CS2_OUT                78
#define ESP_LEDC_LS_SIG_OUT0            79
#define ESP_LEDC_LS_SIG_OUT1            80
#define ESP_LEDC_LS_SIG_OUT2            81
#define ESP_LEDC_LS_SIG_OUT3            82
#define ESP_RMT_SIG_IN0                 83
#define ESP_LEDC_LS_SIG_OUT4            83
#define ESP_RMT_SIG_IN1                 84
#define ESP_LEDC_LS_SIG_OUT5            84
#define ESP_RMT_SIG_IN2                 85
#define ESP_LEDC_LS_SIG_OUT6            85
#define ESP_RMT_SIG_IN3                 86
#define ESP_LEDC_LS_SIG_OUT7            86
#define ESP_RMT_SIG_OUT0                87
#define ESP_RMT_SIG_OUT1                88
#define ESP_RMT_SIG_OUT2                89
#define ESP_RMT_SIG_OUT3                90
#define ESP_EXT_ADC_START               93
#define ESP_I2CEXT1_SCL_IN              95
#define ESP_I2CEXT1_SCL_OUT             95
#define ESP_I2CEXT1_SDA_IN              96
#define ESP_I2CEXT1_SDA_OUT             96
#define ESP_GPIO_SD0_OUT                100
#define ESP_GPIO_SD1_OUT                101
#define ESP_GPIO_SD2_OUT                102
#define ESP_GPIO_SD3_OUT                103
#define ESP_GPIO_SD4_OUT                104
#define ESP_GPIO_SD5_OUT                105
#define ESP_GPIO_SD6_OUT                106
#define ESP_GPIO_SD7_OUT                107
#define ESP_FSPICLK_IN                  108
#define ESP_FSPICLK_OUT_MUX             108
#define ESP_FSPIQ_IN                    109
#define ESP_FSPIQ_OUT                   109
#define ESP_FSPID_IN                    110
#define ESP_FSPID_OUT                   110
#define ESP_FSPIHD_IN                   111
#define ESP_FSPIHD_OUT                  111
#define ESP_FSPIWP_IN                   112
#define ESP_FSPIWP_OUT                  112
#define ESP_FSPIIO4_IN                  113
#define ESP_FSPIIO4_OUT                 113
#define ESP_FSPIIO5_IN                  114
#define ESP_FSPIIO5_OUT                 114
#define ESP_FSPIIO6_IN                  115
#define ESP_FSPIIO6_OUT                 115
#define ESP_FSPIIO7_IN                  116
#define ESP_FSPIIO7_OUT                 116
#define ESP_FSPICS0_IN                  117
#define ESP_FSPICS0_OUT                 117
#define ESP_FSPICS1_OUT                 118
#define ESP_FSPICS2_OUT                 119
#define ESP_FSPICS3_OUT                 120
#define ESP_FSPICS4_OUT                 121
#define ESP_FSPICS5_OUT                 122
#define ESP_TWAI_RX                     123
#define ESP_TWAI_TX                     123
#define ESP_TWAI_BUS_OFF_ON             124
#define ESP_TWAI_CLKOUT                 125
#define ESP_SUBSPICLK_OUT_MUX           126
#define ESP_SUBSPIQ_IN                  127
#define ESP_SUBSPIQ_OUT                 127
#define ESP_SUBSPID_IN                  128
#define ESP_SUBSPID_OUT                 128
#define ESP_SUBSPIHD_IN                 129
#define ESP_SUBSPIHD_OUT                129
#define ESP_SUBSPIWP_IN                 130
#define ESP_SUBSPIWP_OUT                130
#define ESP_SUBSPICS0_OUT               131
#define ESP_SUBSPICS1_OUT               132
#define ESP_FSPIDQS_OUT                 133
#define ESP_FSPI_HSYNC_OUT              134
#define ESP_FSPI_VSYNC_OUT              135
#define ESP_FSPI_DE_OUT                 136
#define ESP_FSPICD_OUT                  137
#define ESP_SPI3_CD_OUT                 139
#define ESP_SPI3_DQS_OUT                140
#define ESP_I2S0I_DATA_IN0              143
#define ESP_I2S0O_DATA_OUT0             143
#define ESP_I2S0I_DATA_IN1              144
#define ESP_I2S0O_DATA_OUT1             144
#define ESP_I2S0I_DATA_IN2              145
#define ESP_I2S0O_DATA_OUT2             145
#define ESP_I2S0I_DATA_IN3              146
#define ESP_I2S0O_DATA_OUT3             146
#define ESP_I2S0I_DATA_IN4              147
#define ESP_I2S0O_DATA_OUT4             147
#define ESP_I2S0I_DATA_IN5              148
#define ESP_I2S0O_DATA_OUT5             148
#define ESP_I2S0I_DATA_IN6              149
#define ESP_I2S0O_DATA_OUT6             149
#define ESP_I2S0I_DATA_IN7              150
#define ESP_I2S0O_DATA_OUT7             150
#define ESP_I2S0I_DATA_IN8              151
#define ESP_I2S0O_DATA_OUT8             151
#define ESP_I2S0I_DATA_IN9              152
#define ESP_I2S0O_DATA_OUT9             152
#define ESP_I2S0I_DATA_IN10             153
#define ESP_I2S0O_DATA_OUT10            153
#define ESP_I2S0I_DATA_IN11             154
#define ESP_I2S0O_DATA_OUT11            154
#define ESP_I2S0I_DATA_IN12             155
#define ESP_I2S0O_DATA_OUT12            155
#define ESP_I2S0I_DATA_IN13             156
#define ESP_I2S0O_DATA_OUT13            156
#define ESP_I2S0I_DATA_IN14             157
#define ESP_I2S0O_DATA_OUT14            157
#define ESP_I2S0I_DATA_IN15             158
#define ESP_I2S0O_DATA_OUT15            158
#define ESP_I2S0O_DATA_OUT16            159
#define ESP_I2S0O_DATA_OUT17            160
#define ESP_I2S0O_DATA_OUT18            161
#define ESP_I2S0O_DATA_OUT19            162
#define ESP_I2S0O_DATA_OUT20            163
#define ESP_I2S0O_DATA_OUT21            164
#define ESP_I2S0O_DATA_OUT22            165
#define ESP_I2S0O_DATA_OUT23            166
#define ESP_SUBSPID4_IN                 167
#define ESP_SUBSPID4_OUT                167
#define ESP_SUBSPID5_IN                 168
#define ESP_SUBSPID5_OUT                168
#define ESP_SUBSPID6_IN                 169
#define ESP_SUBSPID6_OUT                169
#define ESP_SUBSPID7_IN                 170
#define ESP_SUBSPID7_OUT                170
#define ESP_SUBSPIDQS_IN                171
#define ESP_SUBSPIDQS_OUT               171
#define ESP_I2S0I_H_SYNC                193
#define ESP_I2S0I_V_SYNC                194
#define ESP_I2S0I_H_ENABLE              195
#define ESP_PCMFSYNC_IN                 203
#define ESP_BT_AUDIO0_IRQ               203
#define ESP_PCMCLK_IN                   204
#define ESP_BT_AUDIO1_IRQ               204
#define ESP_PCMDIN                      205
#define ESP_BT_AUDIO2_IRQ               205
#define ESP_RW_WAKEUP_REQ               206
#define ESP_BLE_AUDIO0_IRQ              206
#define ESP_BLE_AUDIO1_IRQ              207
#define ESP_BLE_AUDIO2_IRQ              208
#define ESP_PCMFSYNC_OUT                209
#define ESP_PCMCLK_OUT                  210
#define ESP_PCMDOUT                     211
#define ESP_BLE_AUDIO_SYNC0_P           212
#define ESP_BLE_AUDIO_SYNC1_P           213
#define ESP_BLE_AUDIO_SYNC2_P           214
#define ESP_ANT_SEL0                    215
#define ESP_ANT_SEL1                    216
#define ESP_ANT_SEL2                    217
#define ESP_ANT_SEL3                    218
#define ESP_ANT_SEL4                    219
#define ESP_ANT_SEL5                    220
#define ESP_ANT_SEL6                    221
#define ESP_ANT_SEL7                    222
#define ESP_SIG_IN_FUNC_223             223
#define ESP_SIG_IN_FUNC223              223
#define ESP_SIG_IN_FUNC_224             224
#define ESP_SIG_IN_FUNC224              224
#define ESP_SIG_IN_FUNC_225             225
#define ESP_SIG_IN_FUNC225              225
#define ESP_SIG_IN_FUNC_226             226
#define ESP_SIG_IN_FUNC226              226
#define ESP_SIG_IN_FUNC_227             227
#define ESP_SIG_IN_FUNC227              227
#define ESP_PRO_ALONEGPIO_IN0           235
#define ESP_PRO_ALONEGPIO_OUT0          235
#define ESP_PRO_ALONEGPIO_IN1           236
#define ESP_PRO_ALONEGPIO_OUT1          236
#define ESP_PRO_ALONEGPIO_IN2           237
#define ESP_PRO_ALONEGPIO_OUT2          237
#define ESP_PRO_ALONEGPIO_IN3           238
#define ESP_PRO_ALONEGPIO_OUT3          238
#define ESP_PRO_ALONEGPIO_IN4           239
#define ESP_PRO_ALONEGPIO_OUT4          239
#define ESP_PRO_ALONEGPIO_IN5           240
#define ESP_PRO_ALONEGPIO_OUT5          240
#define ESP_PRO_ALONEGPIO_IN6           241
#define ESP_PRO_ALONEGPIO_OUT6          241
#define ESP_PRO_ALONEGPIO_IN7           242
#define ESP_PRO_ALONEGPIO_OUT7          242
#define ESP_CLK_I2S_MUX                 251
#define ESP_SIG_GPIO_OUT                256
#define ESP_GPIO_MAP_DATE               0x1904100


#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32S2_GPIO_SIGMAP_H_ */
```

## 240.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 326 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32S2_GPIO_SIGMAP_H_`。

## 240.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32s2-gpio-sigmap_8h.html)

---

[上一章](P239_esp32h2-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P241_esp32s3-gpio-sigmap.h_源码浏览.md)
