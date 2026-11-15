---
id: learning.zephyr-docs.api-source-reference.page-237
title: esp32c3-gpio-sigmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c3-gpio-sigmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第237章\_esp32c3-gpio-sigmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32c3-gpio-sigmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32c3-gpio-sigmap_8h.html)。

## 237.1\_原始可见代码（Source Code）

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
<a id="l00189"></a>
<a id="l00190"></a>

```c
/*
 * Copyright (c) 2022 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C3_GPIO_SIGMAP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C3_GPIO_SIGMAP_H_


#define ESP_NOSIG                       ESP_SIG_INVAL

#define ESP_SPICLK_OUT_MUX              ESP_SPICLK_OUT
#define ESP_SPIQ_IN                     0
#define ESP_SPIQ_OUT                    0
#define ESP_SPID_IN                     1
#define ESP_SPID_OUT                    1
#define ESP_SPIHD_IN                    2
#define ESP_SPIHD_OUT                   2
#define ESP_SPIWP_IN                    3
#define ESP_SPIWP_OUT                   3
#define ESP_SPICLK_OUT                  4
#define ESP_SPICS0_OUT                  5
#define ESP_U0RXD_IN                    6
#define ESP_U0TXD_OUT                   6
#define ESP_U0CTS_IN                    7
#define ESP_U0RTS_OUT                   7
#define ESP_U0DSR_IN                    8
#define ESP_U0DTR_OUT                   8
#define ESP_U1RXD_IN                    9
#define ESP_U1TXD_OUT                   9
#define ESP_U1CTS_IN                    10
#define ESP_U1RTS_OUT                   10
#define ESP_U1DSR_IN                    11
#define ESP_U1DTR_OUT                   11
#define ESP_I2S_MCLK_IN                 12
#define ESP_I2S_MCLK_OUT                12
#define ESP_I2SO_BCK_IN                 13
#define ESP_I2SO_BCK_OUT                13
#define ESP_I2SO_WS_IN                  14
#define ESP_I2SO_WS_OUT                 14
#define ESP_I2SI_SD_IN                  15
#define ESP_I2SO_SD_OUT                 15
#define ESP_I2SI_BCK_IN                 16
#define ESP_I2SI_BCK_OUT                16
#define ESP_I2SI_WS_IN                  17
#define ESP_I2SI_WS_OUT                 17
#define ESP_GPIO_BT_PRIORITY            18
#define ESP_GPIO_WLAN_PRIO              18
#define ESP_GPIO_BT_ACTIVE              19
#define ESP_GPIO_WLAN_ACTIVE            19
#define ESP_BB_DIAG0                    20
#define ESP_BB_DIAG1                    21
#define ESP_BB_DIAG2                    22
#define ESP_BB_DIAG3                    23
#define ESP_BB_DIAG4                    24
#define ESP_BB_DIAG5                    25
#define ESP_BB_DIAG6                    26
#define ESP_BB_DIAG7                    27
#define ESP_BB_DIAG8                    28
#define ESP_BB_DIAG9                    29
#define ESP_BB_DIAG10                   30
#define ESP_BB_DIAG11                   31
#define ESP_BB_DIAG12                   32
#define ESP_BB_DIAG13                   33
#define ESP_BB_DIAG14                   34
#define ESP_BB_DIAG15                   35
#define ESP_BB_DIAG16                   36
#define ESP_BB_DIAG17                   37
#define ESP_BB_DIAG18                   38
#define ESP_BB_DIAG19                   39
#define ESP_USB_EXTPHY_VP               40
#define ESP_USB_EXTPHY_OEN              40
#define ESP_USB_EXTPHY_VM               41
#define ESP_USB_EXTPHY_SPEED            41
#define ESP_USB_EXTPHY_RCV              42
#define ESP_USB_EXTPHY_VPO              42
#define ESP_USB_EXTPHY_VMO              43
#define ESP_USB_EXTPHY_SUSPND           44
#define ESP_EXT_ADC_START               45
#define ESP_LEDC_LS_SIG_OUT0            45
#define ESP_LEDC_LS_SIG_OUT1            46
#define ESP_LEDC_LS_SIG_OUT2            47
#define ESP_LEDC_LS_SIG_OUT3            48
#define ESP_LEDC_LS_SIG_OUT4            49
#define ESP_LEDC_LS_SIG_OUT5            50
#define ESP_RMT_SIG_IN0                 51
#define ESP_RMT_SIG_OUT0                51
#define ESP_RMT_SIG_IN1                 52
#define ESP_RMT_SIG_OUT1                52
#define ESP_I2CEXT0_SCL_IN              53
#define ESP_I2CEXT0_SCL_OUT             53
#define ESP_I2CEXT0_SDA_IN              54
#define ESP_I2CEXT0_SDA_OUT             54
#define ESP_GPIO_SD0_OUT                55
#define ESP_GPIO_SD1_OUT                56
#define ESP_GPIO_SD2_OUT                57
#define ESP_GPIO_SD3_OUT                58
#define ESP_FSPICLK_IN                  63
#define ESP_FSPICLK_OUT                 63
#define ESP_FSPIQ_IN                    64
#define ESP_FSPIQ_OUT                   64
#define ESP_FSPID_IN                    65
#define ESP_FSPID_OUT                   65
#define ESP_FSPIHD_IN                   66
#define ESP_FSPIHD_OUT                  66
#define ESP_FSPIWP_IN                   67
#define ESP_FSPIWP_OUT                  67
#define ESP_FSPICS0_IN                  68
#define ESP_FSPICS0_OUT                 68
#define ESP_FSPICS1_OUT                 69
#define ESP_FSPICS2_OUT                 70
#define ESP_FSPICS3_OUT                 71
#define ESP_FSPICS4_OUT                 72
#define ESP_FSPICS5_OUT                 73
#define ESP_TWAI_RX                     74
#define ESP_TWAI_TX                     74
#define ESP_TWAI_BUS_OFF_ON             75
#define ESP_TWAI_CLKOUT                 76
#define ESP_PCMFSYNC_IN                 77
#define ESP_BT_AUDIO0_IRQ               77
#define ESP_PCMCLK_IN                   78
#define ESP_BT_AUDIO1_IRQ               78
#define ESP_PCMDIN                      79
#define ESP_BT_AUDIO2_IRQ               79
#define ESP_RW_WAKEUP_REQ               80
#define ESP_BLE_AUDIO0_IRQ              80
#define ESP_BLE_AUDIO1_IRQ              81
#define ESP_BLE_AUDIO2_IRQ              82
#define ESP_PCMFSYNC_OUT                83
#define ESP_PCMCLK_OUT                  84
#define ESP_PCMDOUT                     85
#define ESP_BLE_AUDIO_SYNC0_P           86
#define ESP_BLE_AUDIO_SYNC1_P           87
#define ESP_BLE_AUDIO_SYNC2_P           88
#define ESP_ANT_SEL0                    89
#define ESP_ANT_SEL1                    90
#define ESP_ANT_SEL2                    91
#define ESP_ANT_SEL3                    92
#define ESP_ANT_SEL4                    93
#define ESP_ANT_SEL5                    94
#define ESP_ANT_SEL6                    95
#define ESP_ANT_SEL7                    96
#define ESP_SIG_IN_FUNC_97              97
#define ESP_SIG_IN_FUNC97               97
#define ESP_SIG_IN_FUNC_98              98
#define ESP_SIG_IN_FUNC98               98
#define ESP_SIG_IN_FUNC_99              99
#define ESP_SIG_IN_FUNC99               99
#define ESP_SIG_IN_FUNC_100             100
#define ESP_SIG_IN_FUNC100              100
#define ESP_SYNCERR                     101
#define ESP_SYNCFOUND_FLAG              102
#define ESP_EVT_CNTL_IMMEDIATE_ABORT    103
#define ESP_LINKLBL                     104
#define ESP_DATA_EN                     105
#define ESP_DATA                        106
#define ESP_PKT_TX_ON                   107
#define ESP_PKT_RX_ON                   108
#define ESP_RW_TX_ON                    109
#define ESP_RW_RX_ON                    110
#define ESP_EVT_REQ_P                   111
#define ESP_EVT_STOP_P                  112
#define ESP_BT_MODE_ON                  113
#define ESP_GPIO_LC_DIAG0               114
#define ESP_GPIO_LC_DIAG1               115
#define ESP_GPIO_LC_DIAG2               116
#define ESP_CH                          117
#define ESP_RX_WINDOW                   118
#define ESP_UPDATE_RX                   119
#define ESP_RX_STATUS                   120
#define ESP_CLK_GPIO                    121
#define ESP_NBT_BLE                     122
#define ESP_CLK_OUT_OUT1                123
#define ESP_CLK_OUT_OUT2                124
#define ESP_CLK_OUT_OUT3                125
#define ESP_SPICS1_OUT                  126
#define ESP_SIG_GPIO_OUT                128
#define ESP_GPIO_MAP_DATE               0x2006130


#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C3_GPIO_SIGMAP_H_ */
```

## 237.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 190 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C3_GPIO_SIGMAP_H_`。

## 237.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32c3-gpio-sigmap_8h.html)

---

[上一章](P236_esp32c2-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P238_esp32c6-gpio-sigmap.h_源码浏览.md)
