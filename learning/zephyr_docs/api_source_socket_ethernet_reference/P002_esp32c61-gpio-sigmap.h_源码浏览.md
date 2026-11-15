---
id: learning.zephyr-docs.api-source-socket-ethernet-reference.page-2
title: esp32c61-gpio-sigmap.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32c61-gpio-sigmap_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_esp32c61-gpio-sigmap.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/esp32c61-gpio-sigmap_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P097_zephyr__dt-bindings__pinctrl__esp32c61-gpio-sigmap.h_文件参考.md)。

## 2.1\_原始可见代码（Source Code）

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
<a id="l00227"></a>
<a id="l00228"></a>

```c
/*
 * Copyright (c) 2026 Espressif Systems (Shanghai) Co., Ltd.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C61_GPIO_SIGMAP_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C61_GPIO_SIGMAP_H_


#define ESP_NOSIG ESP_SIG_INVAL

/* LEDC signals */
#define ESP_EXT_ADC_START    0
#define ESP_LEDC_LS_SIG_OUT0 0
#define ESP_LEDC_LS_SIG_OUT1 1
#define ESP_LEDC_LS_SIG_OUT2 2
#define ESP_LEDC_LS_SIG_OUT3 3
#define ESP_LEDC_LS_SIG_OUT4 4
#define ESP_LEDC_LS_SIG_OUT5 5

/* UART0 signals */
#define ESP_U0RXD_IN  6
#define ESP_U0TXD_OUT 6
#define ESP_U0CTS_IN  7
#define ESP_U0RTS_OUT 7
#define ESP_U0DSR_IN  8
#define ESP_U0DTR_OUT 8

/* UART1 signals */
#define ESP_U1RXD_IN  9
#define ESP_U1TXD_OUT 9
#define ESP_U1CTS_IN  10
#define ESP_U1RTS_OUT 10
#define ESP_U1DSR_IN  11
#define ESP_U1DTR_OUT 11

/* I2S signals */
#define ESP_I2S_MCLK_IN  12
#define ESP_I2S_MCLK_OUT 12
#define ESP_I2SO_BCK_IN  13
#define ESP_I2SO_BCK_OUT 13
#define ESP_I2SO_WS_IN   14
#define ESP_I2SO_WS_OUT  14
#define ESP_I2SI_SD_IN   15
#define ESP_I2SO_SD_OUT  15
#define ESP_I2SI_BCK_IN  16
#define ESP_I2SI_BCK_OUT 16
#define ESP_I2SI_WS_IN   17
#define ESP_I2SI_WS_OUT  17
#define ESP_I2SO_SD1_OUT 18

/* CPU test bus signals */
#define ESP_CPU_TESTBUS0 19
#define ESP_CPU_TESTBUS1 20
#define ESP_CPU_TESTBUS2 21
#define ESP_CPU_TESTBUS3 22
#define ESP_CPU_TESTBUS4 23
#define ESP_CPU_TESTBUS5 24
#define ESP_CPU_TESTBUS6 25
#define ESP_CPU_TESTBUS7 26

/* CPU GPIO signals */
#define ESP_CPU_GPIO_IN0  27
#define ESP_CPU_GPIO_OUT0 27
#define ESP_CPU_GPIO_IN1  28
#define ESP_CPU_GPIO_OUT1 28
#define ESP_CPU_GPIO_IN2  29
#define ESP_CPU_GPIO_OUT2 29
#define ESP_CPU_GPIO_IN3  30
#define ESP_CPU_GPIO_OUT3 30
#define ESP_CPU_GPIO_IN4  31
#define ESP_CPU_GPIO_OUT4 31
#define ESP_CPU_GPIO_IN5  32
#define ESP_CPU_GPIO_OUT5 32
#define ESP_CPU_GPIO_IN6  33
#define ESP_CPU_GPIO_OUT6 33
#define ESP_CPU_GPIO_IN7  34
#define ESP_CPU_GPIO_OUT7 34

/* USB JTAG signals */
#define ESP_USB_JTAG_TDO     35
#define ESP_USB_JTAG_TRST    35
#define ESP_USB_JTAG_SRST    36
#define ESP_USB_JTAG_TCK     37
#define ESP_USB_JTAG_TMS     38
#define ESP_USB_JTAG_TDI     39
#define ESP_CPU_USB_JTAG_TDO 40

/* USB external PHY signals */
#define ESP_USB_EXTPHY_VP     41
#define ESP_USB_EXTPHY_OEN    41
#define ESP_USB_EXTPHY_VM     42
#define ESP_USB_EXTPHY_SPEED  42
#define ESP_USB_EXTPHY_RCV    43
#define ESP_USB_EXTPHY_VPO    43
#define ESP_USB_EXTPHY_VMO    44
#define ESP_USB_EXTPHY_SUSPND 45

/* I2C signals */
#define ESP_I2CEXT0_SCL_IN  46
#define ESP_I2CEXT0_SCL_OUT 46
#define ESP_I2CEXT0_SDA_IN  47
#define ESP_I2CEXT0_SDA_OUT 47

/* Antenna select signals */
#define ESP_ANT_SEL0  48
#define ESP_ANT_SEL1  49
#define ESP_ANT_SEL2  50
#define ESP_ANT_SEL3  51
#define ESP_ANT_SEL4  52
#define ESP_ANT_SEL5  53
#define ESP_ANT_SEL6  54
#define ESP_ANT_SEL7  55
#define ESP_ANT_SEL8  56
#define ESP_ANT_SEL9  57
#define ESP_ANT_SEL10 58
#define ESP_ANT_SEL11 59
#define ESP_ANT_SEL12 60
#define ESP_ANT_SEL13 61
#define ESP_ANT_SEL14 62
#define ESP_ANT_SEL15 63

/* FSPI signals */
#define ESP_FSPICLK_IN  64
#define ESP_FSPICLK_OUT 64
#define ESP_FSPIQ_IN    65
#define ESP_FSPIQ_OUT   65
#define ESP_FSPID_IN    66
#define ESP_FSPID_OUT   66
#define ESP_FSPIHD_IN   67
#define ESP_FSPIHD_OUT  67
#define ESP_FSPIWP_IN   68
#define ESP_FSPIWP_OUT  68
#define ESP_FSPICS0_IN  69
#define ESP_FSPICS0_OUT 69

/* UART2 signals */
#define ESP_U2RXD_IN  72
#define ESP_U2TXD_OUT 72
#define ESP_U2CTS_IN  73
#define ESP_U2RTS_OUT 73
#define ESP_U2DSR_IN  74
#define ESP_U2DTR_OUT 74

/* External priority signals */
#define ESP_EXTERN_PRIORITY_I 82
#define ESP_EXTERN_PRIORITY_O 82
#define ESP_EXTERN_ACTIVE_I   83
#define ESP_EXTERN_ACTIVE_O   83

/* Generic input function signals */
#define ESP_SIG_IN_FUNC97  97
#define ESP_SIG_IN_FUNC98  98
#define ESP_SIG_IN_FUNC99  99
#define ESP_SIG_IN_FUNC100 100

/* FSPI CS signals */
#define ESP_FSPICS1_OUT 102
#define ESP_FSPICS2_OUT 103
#define ESP_FSPICS3_OUT 104
#define ESP_FSPICS4_OUT 105
#define ESP_FSPICS5_OUT 106

/* GPIO ETM signals */
#define ESP_GPIO_EVENT_MATRIX_IN0 118
#define ESP_GPIO_TASK_MATRIX_OUT0 118
#define ESP_GPIO_EVENT_MATRIX_IN1 119
#define ESP_GPIO_TASK_MATRIX_OUT1 119
#define ESP_GPIO_EVENT_MATRIX_IN2 120
#define ESP_GPIO_TASK_MATRIX_OUT2 120
#define ESP_GPIO_EVENT_MATRIX_IN3 121
#define ESP_GPIO_TASK_MATRIX_OUT3 121

/* SDIO signal */
#define ESP_SDIO_TOHOST_INT_OUT 124

/* Clock output signals */
#define ESP_CLK_OUT_OUT1 126
#define ESP_CLK_OUT_OUT2 127
#define ESP_CLK_OUT_OUT3 128

/* Modem diagnostic signals */
#define ESP_MODEM_DIAG0  129
#define ESP_MODEM_DIAG1  130
#define ESP_MODEM_DIAG2  131
#define ESP_MODEM_DIAG3  132
#define ESP_MODEM_DIAG4  133
#define ESP_MODEM_DIAG5  134
#define ESP_MODEM_DIAG6  135
#define ESP_MODEM_DIAG7  136
#define ESP_MODEM_DIAG8  137
#define ESP_MODEM_DIAG9  138
#define ESP_MODEM_DIAG10 139
#define ESP_MODEM_DIAG11 140
#define ESP_MODEM_DIAG12 141
#define ESP_MODEM_DIAG13 142
#define ESP_MODEM_DIAG14 143
#define ESP_MODEM_DIAG15 144
#define ESP_MODEM_DIAG16 145
#define ESP_MODEM_DIAG17 146
#define ESP_MODEM_DIAG18 147
#define ESP_MODEM_DIAG19 148
#define ESP_MODEM_DIAG20 149
#define ESP_MODEM_DIAG21 150
#define ESP_MODEM_DIAG22 151
#define ESP_MODEM_DIAG23 152
#define ESP_MODEM_DIAG24 153
#define ESP_MODEM_DIAG25 154
#define ESP_MODEM_DIAG26 155
#define ESP_MODEM_DIAG27 156
#define ESP_MODEM_DIAG28 157
#define ESP_MODEM_DIAG29 158
#define ESP_MODEM_DIAG30 159
#define ESP_MODEM_DIAG31 160

#define ESP_SIG_GPIO_OUT 256


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C61_GPIO_SIGMAP_H_ */
```

## 2.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Espressif Systems (Shanghai) Co., Ltd.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 20 行

LED 控制器（LEDC）信号。

### 注释 3：原第 29 行

UART0 通用异步收发器信号（UART Signals）。

### 注释 4：原第 37 行

UART1 通用异步收发器信号（UART Signals）。

### 注释 5：原第 45 行

集成电路内置音频总线（I2S）信号。

### 注释 6：原第 60 行

CPU 测试总线信号（Test Bus Signals）。

### 注释 7：原第 70 行

CPU 通用输入输出（GPIO）信号。

### 注释 8：原第 88 行

USB JTAG 信号。

### 注释 9：原第 97 行

USB 外部物理层（External PHY）信号。

### 注释 10：原第 107 行

集成电路间总线（I2C）信号。

### 注释 11：原第 113 行

天线选择信号（Antenna Select Signals）。

### 注释 12：原第 131 行

FSPI 信号（Signals）。

### 注释 13：原第 145 行

UART2 通用异步收发器信号（UART Signals）。

### 注释 14：原第 153 行

外部优先级信号（External Priority Signals）。

### 注释 15：原第 159 行

通用输入功能信号（Generic Input Function Signals）。

### 注释 16：原第 165 行

FSPI 片选（CS）信号。

### 注释 17：原第 172 行

GPIO 事件任务矩阵（ETM）信号。

### 注释 18：原第 182 行

安全数字输入输出（SDIO）信号。

### 注释 19：原第 185 行

时钟输出信号（Clock Output Signals）。

### 注释 20：原第 190 行

调制解调器诊断信号（Modem Diagnostic Signals）。

### 注释 21：原第 228 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_ESP32C61_GPIO_SIGMAP_H_`。

## 2.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P097_zephyr__dt-bindings__pinctrl__esp32c61-gpio-sigmap.h_文件参考.md)

---

[上一章](P001_assigned_numbers.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P003_ethernet.h_源码浏览.md)
