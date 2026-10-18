---
id: learning.zephyr-docs.api-source-reference.page-238
title: esp32c6-gpio-sigmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c6-gpio-sigmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第238章\_esp32c6-gpio-sigmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6-gpio-sigmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6-gpio-sigmap_8h.html)。

## 238.1\_原始可见代码（Source Code）

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
<a id="l00270"></a>
<a id="l00271"></a>

```c
/*
 * Copyright (c) 2023 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C6_GPIO_SIGMAP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C6_GPIO_SIGMAP_H_


#define ESP_NOSIG                       ESP_SIG_INVAL

#define ESP_EXT_ADC_START             0
#define ESP_LEDC_LS_SIG_OUT0          0
#define ESP_LEDC_LS_SIG_OUT1          1
#define ESP_LEDC_LS_SIG_OUT2          2
#define ESP_LEDC_LS_SIG_OUT3          3
#define ESP_LEDC_LS_SIG_OUT4          4
#define ESP_LEDC_LS_SIG_OUT5          5
#define ESP_U0RXD_IN                  6
#define ESP_U0TXD_OUT                 6
#define ESP_U0CTS_IN                  7
#define ESP_U0RTS_OUT                 7
#define ESP_U0DSR_IN                  8
#define ESP_U0DTR_OUT                 8
#define ESP_U1RXD_IN                  9
#define ESP_U1TXD_OUT                 9
#define ESP_U1CTS_IN                  10
#define ESP_U1RTS_OUT                 10
#define ESP_U1DSR_IN                  11
#define ESP_U1DTR_OUT                 11
#define ESP_I2S_MCLK_IN               12
#define ESP_I2S_MCLK_OUT              12
#define ESP_I2SO_BCK_IN               13
#define ESP_I2SO_BCK_OUT              13
#define ESP_I2SO_WS_IN                14
#define ESP_I2SO_WS_OUT               14
#define ESP_I2SI_SD_IN                15
#define ESP_I2SO_SD_OUT               15
#define ESP_I2SI_BCK_IN               16
#define ESP_I2SI_BCK_OUT              16
#define ESP_I2SI_WS_IN                17
#define ESP_I2SI_WS_OUT               17
#define ESP_I2SO_SD1_OUT              18
#define ESP_USB_JTAG_TDO_BRIDGE       19
#define ESP_USB_JTAG_TRST             19
#define ESP_CPU_TESTBUS0              20
#define ESP_CPU_TESTBUS1              21
#define ESP_CPU_TESTBUS2              22
#define ESP_CPU_TESTBUS3              23
#define ESP_CPU_TESTBUS4              24
#define ESP_CPU_TESTBUS5              25
#define ESP_CPU_TESTBUS6              26
#define ESP_CPU_TESTBUS7              27
#define ESP_CPU_GPIO_IN0              28
#define ESP_CPU_GPIO_OUT0             28
#define ESP_CPU_GPIO_IN1              29
#define ESP_CPU_GPIO_OUT1             29
#define ESP_CPU_GPIO_IN2              30
#define ESP_CPU_GPIO_OUT2             30
#define ESP_CPU_GPIO_IN3              31
#define ESP_CPU_GPIO_OUT3             31
#define ESP_CPU_GPIO_IN4              32
#define ESP_CPU_GPIO_OUT4             32
#define ESP_CPU_GPIO_IN5              33
#define ESP_CPU_GPIO_OUT5             33
#define ESP_CPU_GPIO_IN6              34
#define ESP_CPU_GPIO_OUT6             34
#define ESP_CPU_GPIO_IN7              35
#define ESP_CPU_GPIO_OUT7             35
#define ESP_USB_JTAG_TCK              36
#define ESP_USB_JTAG_TMS              37
#define ESP_USB_JTAG_TDI              38
#define ESP_USB_JTAG_TDO              39
#define ESP_USB_EXTPHY_VP             40
#define ESP_USB_EXTPHY_OEN            40
#define ESP_USB_EXTPHY_VM             41
#define ESP_USB_EXTPHY_SPEED          41
#define ESP_USB_EXTPHY_RCV            42
#define ESP_USB_EXTPHY_VPO            42
#define ESP_USB_EXTPHY_VMO            43
#define ESP_USB_EXTPHY_SUSPND         44
#define ESP_I2CEXT0_SCL_IN            45
#define ESP_I2CEXT0_SCL_OUT           45
#define ESP_I2CEXT0_SDA_IN            46
#define ESP_I2CEXT0_SDA_OUT           46
#define ESP_PARL_RX_DATA0             47
#define ESP_PARL_TX_DATA0             47
#define ESP_PARL_RX_DATA1             48
#define ESP_PARL_TX_DATA1             48
#define ESP_PARL_RX_DATA2             49
#define ESP_PARL_TX_DATA2             49
#define ESP_PARL_RX_DATA3             50
#define ESP_PARL_TX_DATA3             50
#define ESP_PARL_RX_DATA4             51
#define ESP_PARL_TX_DATA4             51
#define ESP_PARL_RX_DATA5             52
#define ESP_PARL_TX_DATA5             52
#define ESP_PARL_RX_DATA6             53
#define ESP_PARL_TX_DATA6             53
#define ESP_PARL_RX_DATA7             54
#define ESP_PARL_TX_DATA7             54
#define ESP_PARL_RX_DATA8             55
#define ESP_PARL_TX_DATA8             55
#define ESP_PARL_RX_DATA9             56
#define ESP_PARL_TX_DATA9             56
#define ESP_PARL_RX_DATA10            57
#define ESP_PARL_TX_DATA10            57
#define ESP_PARL_RX_DATA11            58
#define ESP_PARL_TX_DATA11            58
#define ESP_PARL_RX_DATA12            59
#define ESP_PARL_TX_DATA12            59
#define ESP_PARL_RX_DATA13            60
#define ESP_PARL_TX_DATA13            60
#define ESP_PARL_RX_DATA14            61
#define ESP_PARL_TX_DATA14            61
#define ESP_PARL_RX_DATA15            62
#define ESP_PARL_TX_DATA15            62
#define ESP_FSPICLK_IN                63
#define ESP_FSPICLK_OUT               63
#define ESP_FSPIQ_IN                  64
#define ESP_FSPIQ_OUT                 64
#define ESP_FSPID_IN                  65
#define ESP_FSPID_OUT                 65
#define ESP_FSPIHD_IN                 66
#define ESP_FSPIHD_OUT                66
#define ESP_FSPIWP_IN                 67
#define ESP_FSPIWP_OUT                67
#define ESP_FSPICS0_IN                68
#define ESP_FSPICS0_OUT               68
#define ESP_PARL_RX_CLK_IN            69
#define ESP_SDIO_TOHOST_INT_OUT       69
#define ESP_PARL_TX_CLK_IN            70
#define ESP_PARL_TX_CLK_OUT           70
#define ESP_RMT_SIG_IN0               71
#define ESP_RMT_SIG_OUT0              71
#define ESP_MODEM_DIAG0               71
#define ESP_RMT_SIG_IN1               72
#define ESP_RMT_SIG_OUT1              72
#define ESP_MODEM_DIAG1               72
#define ESP_TWAI0_RX                  73
#define ESP_TWAI0_TX                  73
#define ESP_MODEM_DIAG2               73
#define ESP_TWAI0_BUS_OFF_ON          74
#define ESP_MODEM_DIAG3               74
#define ESP_TWAI0_CLKOUT              75
#define ESP_MODEM_DIAG4               75
#define ESP_TWAI0_STANDBY             76
#define ESP_MODEM_DIAG5               76
#define ESP_TWAI1_RX                  77
#define ESP_TWAI1_TX                  77
#define ESP_MODEM_DIAG6               77
#define ESP_TWAI1_BUS_OFF_ON          78
#define ESP_MODEM_DIAG7               78
#define ESP_TWAI1_CLKOUT              79
#define ESP_MODEM_DIAG8               79
#define ESP_TWAI1_STANDBY             80
#define ESP_MODEM_DIAG9               80
#define ESP_EXTERN_PRIORITY_I         81
#define ESP_EXTERN_PRIORITY_O         81
#define ESP_EXTERN_ACTIVE_I           82
#define ESP_EXTERN_ACTIVE_O           82
#define ESP_GPIO_SD0_OUT              83
#define ESP_GPIO_SD1_OUT              84
#define ESP_GPIO_SD2_OUT              85
#define ESP_GPIO_SD3_OUT              86
#define ESP_PWM0_SYNC0_IN             87
#define ESP_PWM0_OUT0A                87
#define ESP_MODEM_DIAG10              87
#define ESP_PWM0_SYNC1_IN             88
#define ESP_PWM0_OUT0B                88
#define ESP_MODEM_DIAG11              88
#define ESP_PWM0_SYNC2_IN             89
#define ESP_PWM0_OUT1A                89
#define ESP_MODEM_DIAG12              89
#define ESP_PWM0_F0_IN                90
#define ESP_PWM0_OUT1B                90
#define ESP_MODEM_DIAG13              90
#define ESP_PWM0_F1_IN                91
#define ESP_PWM0_OUT2A                91
#define ESP_MODEM_DIAG14              91
#define ESP_PWM0_F2_IN                92
#define ESP_PWM0_OUT2B                92
#define ESP_MODEM_DIAG15              92
#define ESP_PWM0_CAP0_IN              93
#define ESP_ANT_SEL0                  93
#define ESP_PWM0_CAP1_IN              94
#define ESP_ANT_SEL1                  94
#define ESP_PWM0_CAP2_IN              95
#define ESP_ANT_SEL2                  95
#define ESP_ANT_SEL3                  96
#define ESP_SIG_IN_FUNC_97            97
#define ESP_SIG_IN_FUNC97             97
#define ESP_SIG_IN_FUNC_98            98
#define ESP_SIG_IN_FUNC98             98
#define ESP_SIG_IN_FUNC_99            99
#define ESP_SIG_IN_FUNC99             99
#define ESP_SIG_IN_FUNC_100           100
#define ESP_SIG_IN_FUNC100            100
#define ESP_PCNT_SIG_CH0_IN0          101
#define ESP_FSPICS1_OUT               101
#define ESP_MODEM_DIAG16              101
#define ESP_PCNT_SIG_CH1_IN0          102
#define ESP_FSPICS2_OUT               102
#define ESP_MODEM_DIAG17              102
#define ESP_PCNT_CTRL_CH0_IN0         103
#define ESP_FSPICS3_OUT               103
#define ESP_MODEM_DIAG18              103
#define ESP_PCNT_CTRL_CH1_IN0         104
#define ESP_FSPICS4_OUT               104
#define ESP_MODEM_DIAG19              104
#define ESP_PCNT_SIG_CH0_IN1          105
#define ESP_FSPICS5_OUT               105
#define ESP_MODEM_DIAG20              105
#define ESP_PCNT_SIG_CH1_IN1          106
#define ESP_MODEM_DIAG21              106
#define ESP_PCNT_CTRL_CH0_IN1         107
#define ESP_MODEM_DIAG22              107
#define ESP_PCNT_CTRL_CH1_IN1         108
#define ESP_MODEM_DIAG23              108
#define ESP_PCNT_SIG_CH0_IN2          109
#define ESP_MODEM_DIAG24              109
#define ESP_PCNT_SIG_CH1_IN2          110
#define ESP_MODEM_DIAG25              110
#define ESP_PCNT_CTRL_CH0_IN2         111
#define ESP_MODEM_DIAG26              111
#define ESP_PCNT_CTRL_CH1_IN2         112
#define ESP_MODEM_DIAG27              112
#define ESP_PCNT_SIG_CH0_IN3          113
#define ESP_MODEM_DIAG28              113
#define ESP_PCNT_SIG_CH1_IN3          114
#define ESP_SPICLK_OUT                114
#define ESP_MODEM_DIAG29              114
#define ESP_PCNT_CTRL_CH0_IN3         115
#define ESP_SPICS0_OUT                115
#define ESP_MODEM_DIAG30              115
#define ESP_PCNT_CTRL_CH1_IN3         116
#define ESP_SPICS1_OUT                116
#define ESP_MODEM_DIAG31              116
#define ESP_GPIO_EVENT_MATRIX_IN0     117
#define ESP_GPIO_TASK_MATRIX_OUT0     117
#define ESP_GPIO_EVENT_MATRIX_IN1     118
#define ESP_GPIO_TASK_MATRIX_OUT1     118
#define ESP_GPIO_EVENT_MATRIX_IN2     119
#define ESP_GPIO_TASK_MATRIX_OUT2     119
#define ESP_GPIO_EVENT_MATRIX_IN3     120
#define ESP_GPIO_TASK_MATRIX_OUT3     120
#define ESP_SPIQ_IN                   121
#define ESP_SPIQ_OUT                  121
#define ESP_SPID_IN                   122
#define ESP_SPID_OUT                  122
#define ESP_SPIHD_IN                  123
#define ESP_SPIHD_OUT                 123
#define ESP_SPIWP_IN                  124
#define ESP_SPIWP_OUT                 124
#define ESP_CLK_OUT_OUT1              125
#define ESP_CLK_OUT_OUT2              126
#define ESP_CLK_OUT_OUT3              127
#define ESP_SIG_GPIO_OUT              128
#define ESP_GPIO_MAP_DATE             0x2201120


#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C6_GPIO_SIGMAP_H_ */
```

## 238.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 271 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C6_GPIO_SIGMAP_H_`。

## 238.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/esp32c6-gpio-sigmap_8h.html)

---

[上一章](P237_esp32c3-gpio-sigmap.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P239_esp32h2-gpio-sigmap.h_源码浏览.md)
