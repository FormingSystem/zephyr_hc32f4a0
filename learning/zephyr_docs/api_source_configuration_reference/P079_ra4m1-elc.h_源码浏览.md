---
id: learning.zephyr-docs.api-source-configuration-reference.page-79
title: ra4m1-elc.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ra4m1-elc_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_ra4m1-elc.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ra4m1-elc_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ra4m1-elc_8h.html)。

## 79.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00053"></a>
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
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA4M1_ELC_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA4M1_ELC_H_




/* Event codes for Renesas RA4M1 Event Link Controller (ELC). */
#define RA_ELC_EVENT_NONE                   0x0
#define RA_ELC_EVENT_ICU_IRQ0               0x001
#define RA_ELC_EVENT_ICU_IRQ1               0x002
#define RA_ELC_EVENT_ICU_IRQ2               0x003
#define RA_ELC_EVENT_ICU_IRQ3               0x004
#define RA_ELC_EVENT_ICU_IRQ4               0x005
#define RA_ELC_EVENT_ICU_IRQ5               0x006
#define RA_ELC_EVENT_ICU_IRQ6               0x007
#define RA_ELC_EVENT_ICU_IRQ7               0x008
#define RA_ELC_EVENT_ICU_IRQ8               0x009
#define RA_ELC_EVENT_ICU_IRQ9               0x00A
#define RA_ELC_EVENT_ICU_IRQ10              0x00B
#define RA_ELC_EVENT_ICU_IRQ11              0x00C
#define RA_ELC_EVENT_ICU_IRQ12              0x00D
#define RA_ELC_EVENT_ICU_IRQ14              0x00F
#define RA_ELC_EVENT_ICU_IRQ15              0x010
#define RA_ELC_EVENT_DMAC0_INT              0x011
#define RA_ELC_EVENT_DMAC1_INT              0x012
#define RA_ELC_EVENT_DMAC2_INT              0x013
#define RA_ELC_EVENT_DMAC3_INT              0x014
#define RA_ELC_EVENT_DTC_COMPLETE           0x015
#define RA_ELC_EVENT_DTC_END                0x016
#define RA_ELC_EVENT_ICU_SNOOZE_CANCEL      0x017
#define RA_ELC_EVENT_FCU_FRDYI              0x018
#define RA_ELC_EVENT_LVD_LVD1               0x019
#define RA_ELC_EVENT_LVD_LVD2               0x01A
#define RA_ELC_EVENT_LVD_VBATT              0x01B
#define RA_ELC_EVENT_CGC_MOSC_STOP          0x01C
#define RA_ELC_EVENT_LPM_SNOOZE_REQUEST     0x01D
#define RA_ELC_EVENT_AGT0_INT               0x01E
#define RA_ELC_EVENT_AGT0_COMPARE_A         0x01F
#define RA_ELC_EVENT_AGT0_COMPARE_B         0x020
#define RA_ELC_EVENT_AGT1_INT               0x021
#define RA_ELC_EVENT_AGT1_COMPARE_A         0x022
#define RA_ELC_EVENT_AGT1_COMPARE_B         0x023
#define RA_ELC_EVENT_IWDT_UNDERFLOW         0x024
#define RA_ELC_EVENT_WDT_UNDERFLOW          0x025
#define RA_ELC_EVENT_RTC_ALARM              0x026
#define RA_ELC_EVENT_RTC_PERIOD             0x027
#define RA_ELC_EVENT_RTC_CARRY              0x028
#define RA_ELC_EVENT_ADC0_SCAN_END          0x029
#define RA_ELC_EVENT_ADC0_SCAN_END_B        0x02A
#define RA_ELC_EVENT_ADC0_WINDOW_A          0x02B
#define RA_ELC_EVENT_ADC0_WINDOW_B          0x02C
#define RA_ELC_EVENT_ADC0_COMPARE_MATCH     0x02D
#define RA_ELC_EVENT_ADC0_COMPARE_MISMATCH  0x02E
#define RA_ELC_EVENT_ACMPLP0_INT            0x02F
#define RA_ELC_EVENT_ACMPLP1_INT            0x030
#define RA_ELC_EVENT_USBFS_FIFO_0           0x031
#define RA_ELC_EVENT_USBFS_FIFO_1           0x032
#define RA_ELC_EVENT_USBFS_INT              0x033
#define RA_ELC_EVENT_USBFS_RESUME           0x034
#define RA_ELC_EVENT_IIC0_RXI               0x035
#define RA_ELC_EVENT_IIC0_TXI               0x036
#define RA_ELC_EVENT_IIC0_TEI               0x037
#define RA_ELC_EVENT_IIC0_ERI               0x038
#define RA_ELC_EVENT_IIC0_WUI               0x039
#define RA_ELC_EVENT_IIC1_RXI               0x03A
#define RA_ELC_EVENT_IIC1_TXI               0x03B
#define RA_ELC_EVENT_IIC1_TEI               0x03C
#define RA_ELC_EVENT_IIC1_ERI               0x03D
#define RA_ELC_EVENT_SSI0_TXI               0x03E
#define RA_ELC_EVENT_SSI0_RXI               0x03F
#define RA_ELC_EVENT_SSI0_INT               0x041
#define RA_ELC_EVENT_CTSU_WRITE             0x042
#define RA_ELC_EVENT_CTSU_READ              0x043
#define RA_ELC_EVENT_CTSU_END               0x044
#define RA_ELC_EVENT_KEY_INT                0x045
#define RA_ELC_EVENT_DOC_INT                0x046
#define RA_ELC_EVENT_CAC_FREQUENCY_ERROR    0x047
#define RA_ELC_EVENT_CAC_MEASUREMENT_END    0x048
#define RA_ELC_EVENT_CAC_OVERFLOW           0x049
#define RA_ELC_EVENT_CAN0_ERROR             0x04A
#define RA_ELC_EVENT_CAN0_FIFO_RX           0x04B
#define RA_ELC_EVENT_CAN0_FIFO_TX           0x04C
#define RA_ELC_EVENT_CAN0_MAILBOX_RX        0x04D
#define RA_ELC_EVENT_CAN0_MAILBOX_TX        0x04E
#define RA_ELC_EVENT_IOPORT_EVENT_1         0x04F
#define RA_ELC_EVENT_IOPORT_EVENT_2         0x050
#define RA_ELC_EVENT_IOPORT_EVENT_3         0x051
#define RA_ELC_EVENT_IOPORT_EVENT_4         0x052
#define RA_ELC_EVENT_ELC_SOFTWARE_EVENT_0   0x053
#define RA_ELC_EVENT_ELC_SOFTWARE_EVENT_1   0x054
#define RA_ELC_EVENT_POEG0_EVENT            0x055
#define RA_ELC_EVENT_POEG1_EVENT            0x056
#define RA_ELC_EVENT_GPT0_CAPTURE_COMPARE_A 0x057
#define RA_ELC_EVENT_GPT0_CAPTURE_COMPARE_B 0x058
#define RA_ELC_EVENT_GPT0_COMPARE_C         0x059
#define RA_ELC_EVENT_GPT0_COMPARE_D         0x05A
#define RA_ELC_EVENT_GPT0_COMPARE_E         0x05B
#define RA_ELC_EVENT_GPT0_COMPARE_F         0x05C
#define RA_ELC_EVENT_GPT0_COUNTER_OVERFLOW  0x05D
#define RA_ELC_EVENT_GPT0_COUNTER_UNDERFLOW 0x05E
#define RA_ELC_EVENT_GPT1_CAPTURE_COMPARE_A 0x05F
#define RA_ELC_EVENT_GPT1_CAPTURE_COMPARE_B 0x060
#define RA_ELC_EVENT_GPT1_COMPARE_C         0x061
#define RA_ELC_EVENT_GPT1_COMPARE_D         0x062
#define RA_ELC_EVENT_GPT1_COMPARE_E         0x063
#define RA_ELC_EVENT_GPT1_COMPARE_F         0x064
#define RA_ELC_EVENT_GPT1_COUNTER_OVERFLOW  0x065
#define RA_ELC_EVENT_GPT1_COUNTER_UNDERFLOW 0x066
#define RA_ELC_EVENT_GPT2_CAPTURE_COMPARE_A 0x067
#define RA_ELC_EVENT_GPT2_CAPTURE_COMPARE_B 0x068
#define RA_ELC_EVENT_GPT2_COMPARE_C         0x069
#define RA_ELC_EVENT_GPT2_COMPARE_D         0x06A
#define RA_ELC_EVENT_GPT2_COMPARE_E         0x06B
#define RA_ELC_EVENT_GPT2_COMPARE_F         0x06C
#define RA_ELC_EVENT_GPT2_COUNTER_OVERFLOW  0x06D
#define RA_ELC_EVENT_GPT2_COUNTER_UNDERFLOW 0x06E
#define RA_ELC_EVENT_GPT3_CAPTURE_COMPARE_A 0x06F
#define RA_ELC_EVENT_GPT3_CAPTURE_COMPARE_B 0x070
#define RA_ELC_EVENT_GPT3_COMPARE_C         0x071
#define RA_ELC_EVENT_GPT3_COMPARE_D         0x072
#define RA_ELC_EVENT_GPT3_COMPARE_E         0x073
#define RA_ELC_EVENT_GPT3_COMPARE_F         0x074
#define RA_ELC_EVENT_GPT3_COUNTER_OVERFLOW  0x075
#define RA_ELC_EVENT_GPT3_COUNTER_UNDERFLOW 0x076
#define RA_ELC_EVENT_GPT4_CAPTURE_COMPARE_A 0x077
#define RA_ELC_EVENT_GPT4_CAPTURE_COMPARE_B 0x078
#define RA_ELC_EVENT_GPT4_COMPARE_C         0x079
#define RA_ELC_EVENT_GPT4_COMPARE_D         0x07A
#define RA_ELC_EVENT_GPT4_COMPARE_E         0x07B
#define RA_ELC_EVENT_GPT4_COMPARE_F         0x07C
#define RA_ELC_EVENT_GPT4_COUNTER_OVERFLOW  0x07D
#define RA_ELC_EVENT_GPT4_COUNTER_UNDERFLOW 0x07E
#define RA_ELC_EVENT_GPT5_CAPTURE_COMPARE_A 0x07F
#define RA_ELC_EVENT_GPT5_CAPTURE_COMPARE_B 0x080
#define RA_ELC_EVENT_GPT5_COMPARE_C         0x081
#define RA_ELC_EVENT_GPT5_COMPARE_D         0x082
#define RA_ELC_EVENT_GPT5_COMPARE_E         0x083
#define RA_ELC_EVENT_GPT5_COMPARE_F         0x084
#define RA_ELC_EVENT_GPT5_COUNTER_OVERFLOW  0x085
#define RA_ELC_EVENT_GPT5_COUNTER_UNDERFLOW 0x086
#define RA_ELC_EVENT_GPT6_CAPTURE_COMPARE_A 0x087
#define RA_ELC_EVENT_GPT6_CAPTURE_COMPARE_B 0x088
#define RA_ELC_EVENT_GPT6_COMPARE_C         0x089
#define RA_ELC_EVENT_GPT6_COMPARE_D         0x08A
#define RA_ELC_EVENT_GPT6_COMPARE_E         0x08B
#define RA_ELC_EVENT_GPT6_COMPARE_F         0x08C
#define RA_ELC_EVENT_GPT6_COUNTER_OVERFLOW  0x08D
#define RA_ELC_EVENT_GPT6_COUNTER_UNDERFLOW 0x08E
#define RA_ELC_EVENT_GPT7_CAPTURE_COMPARE_A 0x08F
#define RA_ELC_EVENT_GPT7_CAPTURE_COMPARE_B 0x090
#define RA_ELC_EVENT_GPT7_COMPARE_C         0x091
#define RA_ELC_EVENT_GPT7_COMPARE_D         0x092
#define RA_ELC_EVENT_GPT7_COMPARE_E         0x093
#define RA_ELC_EVENT_GPT7_COMPARE_F         0x094
#define RA_ELC_EVENT_GPT7_COUNTER_OVERFLOW  0x095
#define RA_ELC_EVENT_GPT7_COUNTER_UNDERFLOW 0x096
#define RA_ELC_EVENT_OPS_UVW_EDGE           0x097
#define RA_ELC_EVENT_SCI0_RXI               0x098
#define RA_ELC_EVENT_SCI0_TXI               0x099
#define RA_ELC_EVENT_SCI0_TEI               0x09A
#define RA_ELC_EVENT_SCI0_ERI               0x09B
#define RA_ELC_EVENT_SCI0_AM                0x09C
#define RA_ELC_EVENT_SCI0_RXI_OR_ERI        0x09D
#define RA_ELC_EVENT_SCI1_RXI               0x09E
#define RA_ELC_EVENT_SCI1_TXI               0x09F
#define RA_ELC_EVENT_SCI1_TEI               0x0A0
#define RA_ELC_EVENT_SCI1_ERI               0x0A1
#define RA_ELC_EVENT_SCI1_AM                0x0A2
#define RA_ELC_EVENT_SCI2_RXI               0x0A3
#define RA_ELC_EVENT_SCI2_TXI               0x0A4
#define RA_ELC_EVENT_SCI2_TEI               0x0A5
#define RA_ELC_EVENT_SCI2_ERI               0x0A6
#define RA_ELC_EVENT_SCI2_AM                0x0A7
#define RA_ELC_EVENT_SCI9_RXI               0x0A8
#define RA_ELC_EVENT_SCI9_TXI               0x0A9
#define RA_ELC_EVENT_SCI9_TEI               0x0AA
#define RA_ELC_EVENT_SCI9_ERI               0x0AB
#define RA_ELC_EVENT_SCI9_AM                0x0AC
#define RA_ELC_EVENT_SPI0_RXI               0x0AD
#define RA_ELC_EVENT_SPI0_TXI               0x0AE
#define RA_ELC_EVENT_SPI0_IDLE              0x0AF
#define RA_ELC_EVENT_SPI0_ERI               0x0B0
#define RA_ELC_EVENT_SPI0_TEI               0x0B1
#define RA_ELC_EVENT_SPI1_RXI               0x0B2
#define RA_ELC_EVENT_SPI1_TXI               0x0B3
#define RA_ELC_EVENT_SPI1_IDLE              0x0B4
#define RA_ELC_EVENT_SPI1_ERI               0x0B5
#define RA_ELC_EVENT_SPI1_TEI               0x0B6

/* Renesas RA ELC peripherals that can be linked to event signals. */
#define RA_ELC_PERIPHERAL_GPT_A   0
#define RA_ELC_PERIPHERAL_GPT_B   1
#define RA_ELC_PERIPHERAL_GPT_C   2
#define RA_ELC_PERIPHERAL_GPT_D   3
#define RA_ELC_PERIPHERAL_GPT_E   4
#define RA_ELC_PERIPHERAL_GPT_F   5
#define RA_ELC_PERIPHERAL_GPT_G   6
#define RA_ELC_PERIPHERAL_GPT_H   7
#define RA_ELC_PERIPHERAL_ADC0    8
#define RA_ELC_PERIPHERAL_ADC0_B  9
#define RA_ELC_PERIPHERAL_DAC0    12
#define RA_ELC_PERIPHERAL_IOPORT1 14
#define RA_ELC_PERIPHERAL_IOPORT2 15
#define RA_ELC_PERIPHERAL_IOPORT3 16
#define RA_ELC_PERIPHERAL_IOPORT4 17
#define RA_ELC_PERIPHERAL_CTSU    18



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA4M1_ELC_H_ */
```

## 79.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

Renesas RA4M1 事件链接控制器（Event Link Controller，ELC）的事件代码。

### 注释 3：原第 239 行

可链接到事件信号的 Renesas RA ELC 外设。

### 注释 4：原第 261 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_MISC_RENESAS_RA_ELC_RA4M1_ELC_H_`。

## 79.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ra4m1-elc_8h.html)

---

[上一章](P078_ra4l1-elc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P080_ra4m2-elc.h_源码浏览.md)
