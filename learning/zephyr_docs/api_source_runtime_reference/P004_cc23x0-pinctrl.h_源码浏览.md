---
id: learning.zephyr-docs.api-source-runtime-reference.page-4
title: cc23x0-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cc23x0-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_cc23x0-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cc23x0-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cc23x0-pinctrl_8h.html)。

## 4.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024 Texas Instruments Incorporated
 * Copyright (c) 2024 BayLibre, SAS
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC23X0_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC23X0_PINCTRL_H_

/*
 * The whole TI CC23X0 pin configuration information is encoded in a 32-bit
 * bitfield organized as follow:
 *
 * - 31:     Reserved
 * - 30:     Input hysteresis
 * - 29:     Input capability of IO
 * - 28..27: Reserved
 * - 26..24: IO mode
 * - 23..22: Reserved
 * - 21..20: Wakeup configuration from shutdown
 * - 19:     Reserved
 * - 18:     Wakeup capability from standby
 * - 17..16: Edge detection configuration
 * - 15:     Reserved
 * - 14..13: Pull control
 * - 12..3:  Reserved
 * - 2..0:   Function configuration
 */

/* TI CC23X0 function configuration */

#define IOC_PORTCFG_BASE   0U
#define IOC_PORTCFG_PFUNC1 1U
#define IOC_PORTCFG_PFUNC2 2U
#define IOC_PORTCFG_PFUNC3 3U
#define IOC_PORTCFG_PFUNC4 4U
#define IOC_PORTCFG_PFUNC5 5U
#define IOC_PORTCFG_ANA    6U
#define IOC_PORTCFG_DTB    7U

/* TI CC23X0 peripheral pin mapping */

#define DIO0_GPIO0    IOC_PORTCFG_BASE
#define DIO0_SPI0_CSN IOC_PORTCFG_PFUNC1
#define DIO0_I2C0_SDA IOC_PORTCFG_PFUNC2
#define DIO0_T3_C2    IOC_PORTCFG_PFUNC3
#define DIO0_ADC5     IOC_PORTCFG_ANA

#define DIO1_GPIO1     IOC_PORTCFG_BASE
#define DIO1_T3_C1     IOC_PORTCFG_PFUNC1
#define DIO1_LRFD7     IOC_PORTCFG_PFUNC2
#define DIO1_T1_F      IOC_PORTCFG_PFUNC3
#define DIO1_UART0_RTS IOC_PORTCFG_PFUNC4
#define DIO1_ADC4      IOC_PORTCFG_ANA
#define DIO1_DTB2      IOC_PORTCFG_DTB

#define DIO2_GPIO2     IOC_PORTCFG_BASE
#define DIO2_T0_PE     IOC_PORTCFG_PFUNC1
#define DIO2_T2_C1N    IOC_PORTCFG_PFUNC2
#define DIO2_UART0_CTS IOC_PORTCFG_PFUNC3
#define DIO2_ADC3      IOC_PORTCFG_ANA

#define DIO3_GPIO3  IOC_PORTCFG_BASE
#define DIO3_LFCI   IOC_PORTCFG_PFUNC1
#define DIO3_T0_C1N IOC_PORTCFG_PFUNC2
#define DIO3_LRFD0  IOC_PORTCFG_PFUNC3
#define DIO3_T3_C1  IOC_PORTCFG_PFUNC4
#define DIO3_T1_C2  IOC_PORTCFG_PFUNC5
#define DIO3_LFXT_P IOC_PORTCFG_ANA
#define DIO3_DTB7   IOC_PORTCFG_DTB

#define DIO4_GPIO4     IOC_PORTCFG_BASE
#define DIO4_T0_C2N    IOC_PORTCFG_PFUNC1
#define DIO4_UART0_TXD IOC_PORTCFG_PFUNC2
#define DIO4_LRFD1     IOC_PORTCFG_PFUNC3
#define DIO4_SPI0_MOSI IOC_PORTCFG_PFUNC4
#define DIO4_T0_C2     IOC_PORTCFG_PFUNC5
#define DIO4_LFXT_N    IOC_PORTCFG_ANA
#define DIO4_DTB8      IOC_PORTCFG_DTB

#define DIO5_GPIO5 IOC_PORTCFG_BASE
#define DIO5_T2_C2 IOC_PORTCFG_PFUNC1
#define DIO5_LRFD6 IOC_PORTCFG_PFUNC3
#define DIO5_ADC2  IOC_PORTCFG_ANA

#define DIO6_GPIO6      IOC_PORTCFG_BASE
#define DIO6_SPI0_CSN   IOC_PORTCFG_PFUNC1
#define DIO6_I2C0_SCL   IOC_PORTCFG_PFUNC2
#define DIO6_T1_C2      IOC_PORTCFG_PFUNC3
#define DIO6_LRFD2      IOC_PORTCFG_PFUNC4
#define DIO6_UART0_TXD  IOC_PORTCFG_PFUNC5
#define DIO6_ADC1_AREFP IOC_PORTCFG_ANA
#define DIO6_DTB6       IOC_PORTCFG_DTB

#define DIO7_GPIO7      IOC_PORTCFG_BASE
#define DIO7_T3_C1      IOC_PORTCFG_PFUNC1
#define DIO7_LRFD4      IOC_PORTCFG_PFUNC3
#define DIO7_ADC0_AREFM IOC_PORTCFG_ANA

#define DIO8_GPIO8     IOC_PORTCFG_BASE
#define DIO8_SPI0_SCLK IOC_PORTCFG_PFUNC1
#define DIO8_UART0_RTS IOC_PORTCFG_PFUNC2
#define DIO8_T1_C0N    IOC_PORTCFG_PFUNC3
#define DIO8_I2C0_SDA  IOC_PORTCFG_PFUNC4
#define DIO8_T0_C0N    IOC_PORTCFG_PFUNC5
#define DIO8_DTB3      IOC_PORTCFG_DTB

#define DIO9_GPIO9 IOC_PORTCFG_BASE
#define DIO9_T3_C0 IOC_PORTCFG_PFUNC1
#define DIO9_LRFD3 IOC_PORTCFG_PFUNC3

#define DIO10_GPIO10 IOC_PORTCFG_BASE
#define DIO10_LPC0   IOC_PORTCFG_PFUNC1
#define DIO10_T2_PE  IOC_PORTCFG_PFUNC2
#define DIO10_T3_C0N IOC_PORTCFG_PFUNC3

#define DIO11_GPIO11    IOC_PORTCFG_BASE
#define DIO11_SPI0_CSN  IOC_PORTCFG_PFUNC1
#define DIO11_T1_C2N    IOC_PORTCFG_PFUNC2
#define DIO11_T0_C0     IOC_PORTCFG_PFUNC3
#define DIO11_LRFD0     IOC_PORTCFG_PFUNC4
#define DIO11_SPI0_MISO IOC_PORTCFG_PFUNC5
#define DIO11_DTB9      IOC_PORTCFG_DTB

#define DIO12_GPIO12    IOC_PORTCFG_BASE
#define DIO12_SPI0_MISO IOC_PORTCFG_PFUNC1
#define DIO12_SPI0_MOSI IOC_PORTCFG_PFUNC2
#define DIO12_UART0_RXD IOC_PORTCFG_PFUNC3
#define DIO12_T1_C1     IOC_PORTCFG_PFUNC4
#define DIO12_I2C0_SDA  IOC_PORTCFG_PFUNC5
#define DIO12_DTB13     IOC_PORTCFG_DTB

#define DIO13_GPIO13    IOC_PORTCFG_BASE
#define DIO13_SPI0_MISO IOC_PORTCFG_PFUNC1
#define DIO13_SPI0_MOSI IOC_PORTCFG_PFUNC2
#define DIO13_UART0_TXD IOC_PORTCFG_PFUNC3
#define DIO13_T0_C0N    IOC_PORTCFG_PFUNC4
#define DIO13_T1_F      IOC_PORTCFG_PFUNC5
#define DIO13_DTB4      IOC_PORTCFG_DTB

#define DIO14_GPIO14 IOC_PORTCFG_BASE
#define DIO14_T3_C2  IOC_PORTCFG_PFUNC1
#define DIO14_T1_C2N IOC_PORTCFG_PFUNC2
#define DIO14_LRFD5  IOC_PORTCFG_PFUNC3
#define DIO14_T1_F   IOC_PORTCFG_PFUNC4

#define DIO15_GPIO15    IOC_PORTCFG_BASE
#define DIO15_UART0_RXD IOC_PORTCFG_PFUNC1
#define DIO15_T2_C0N    IOC_PORTCFG_PFUNC2
#define DIO15_CKMIN     IOC_PORTCFG_PFUNC3

#define DIO16_GPIO16    IOC_PORTCFG_BASE
#define DIO16_SPI0_MOSI IOC_PORTCFG_PFUNC1
#define DIO16_UART0_RXD IOC_PORTCFG_PFUNC2
#define DIO16_I2C0_SDA  IOC_PORTCFG_PFUNC3
#define DIO16_T1_C2     IOC_PORTCFG_PFUNC4
#define DIO16_T1_C0N    IOC_PORTCFG_PFUNC5
#define DIO16_DTB10     IOC_PORTCFG_DTB

#define DIO17_GPIO17    IOC_PORTCFG_BASE
#define DIO17_SPI0_SCLK IOC_PORTCFG_PFUNC1
#define DIO17_UART0_TXD IOC_PORTCFG_PFUNC2
#define DIO17_I2C0_SCL  IOC_PORTCFG_PFUNC3
#define DIO17_T1_C1N    IOC_PORTCFG_PFUNC4
#define DIO17_T0_C2     IOC_PORTCFG_PFUNC5
#define DIO17_DTB11     IOC_PORTCFG_DTB

#define DIO18_GPIO18    IOC_PORTCFG_BASE
#define DIO18_T3_C0     IOC_PORTCFG_PFUNC1
#define DIO18_LPC0      IOC_PORTCFG_PFUNC2
#define DIO18_UART0_TXD IOC_PORTCFG_PFUNC3
#define DIO18_SPI0_SCLK IOC_PORTCFG_PFUNC4
#define DIO18_DTB12     IOC_PORTCFG_DTB

#define DIO19_GPIO19    IOC_PORTCFG_BASE
#define DIO19_T3_C1     IOC_PORTCFG_PFUNC1
#define DIO19_T2_PE     IOC_PORTCFG_PFUNC2
#define DIO19_SPI0_MOSI IOC_PORTCFG_PFUNC4
#define DIO19_DTB0      IOC_PORTCFG_DTB

#define DIO20_GPIO20    IOC_PORTCFG_BASE
#define DIO20_LPC0      IOC_PORTCFG_PFUNC1
#define DIO20_UART0_TXD IOC_PORTCFG_PFUNC2
#define DIO20_UART0_RXD IOC_PORTCFG_PFUNC3
#define DIO20_T1_C0     IOC_PORTCFG_PFUNC4
#define DIO20_SPI0_MISO IOC_PORTCFG_PFUNC5
#define DIO20_ADC11     IOC_PORTCFG_ANA
#define DIO20_DTB14     IOC_PORTCFG_DTB

#define DIO21_GPIO21     IOC_PORTCFG_BASE
#define DIO21_UART0_CTS  IOC_PORTCFG_PFUNC1
#define DIO21_T1_C1N     IOC_PORTCFG_PFUNC2
#define DIO21_T0_C1      IOC_PORTCFG_PFUNC3
#define DIO21_SPI0_MISO  IOC_PORTCFG_PFUNC4
#define DIO21_LRFD1      IOC_PORTCFG_PFUNC5
#define DIO21_ADC10_LPCP IOC_PORTCFG_ANA
#define DIO21_DTB15      IOC_PORTCFG_DTB

#define DIO22_GPIO22    IOC_PORTCFG_BASE
#define DIO22_T2_C0     IOC_PORTCFG_PFUNC1
#define DIO22_UART0_RXD IOC_PORTCFG_PFUNC2
#define DIO22_T3_C1N    IOC_PORTCFG_PFUNC3
#define DIO22_ADC9      IOC_PORTCFG_ANA
#define DIO22_DTB1      IOC_PORTCFG_DTB

#define DIO23_GPIO23         IOC_PORTCFG_BASE
#define DIO23_T2_C1          IOC_PORTCFG_PFUNC1
#define DIO23_T3_C2N         IOC_PORTCFG_PFUNC3
#define DIO23_ADC8_LPCP_LPCM IOC_PORTCFG_ANA

#define DIO24_GPIO24         IOC_PORTCFG_BASE
#define DIO24_SPI0_SCLK      IOC_PORTCFG_PFUNC1
#define DIO24_T1_C0          IOC_PORTCFG_PFUNC2
#define DIO24_T3_C0          IOC_PORTCFG_PFUNC3
#define DIO24_T0_PE          IOC_PORTCFG_PFUNC4
#define DIO24_I2C0_SCL       IOC_PORTCFG_PFUNC5
#define DIO24_ADC7_LPCP_LPCM IOC_PORTCFG_ANA
#define DIO24_DTB5           IOC_PORTCFG_DTB

#define DIO25_GPIO25    IOC_PORTCFG_BASE
#define DIO25_SPI0_MISO IOC_PORTCFG_PFUNC1
#define DIO25_I2C0_SCL  IOC_PORTCFG_PFUNC2
#define DIO25_T2_C2N    IOC_PORTCFG_PFUNC3
#define DIO25_ADC6      IOC_PORTCFG_ANA

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC23X0_PINCTRL_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Texas Instruments Incorporated。

版权（Copyright）：© 2024 BayLibre, SAS。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 11 行

全部 TI CC23X0 引脚配置信息编码在一个 32 位位域（Bitfield）中，组织如下：

- `31`：保留。
- `30`：输入迟滞（Input hysteresis）。
- `29`：I/O 的输入能力。
- `28..27`：保留。
- `26..24`：I/O 模式。
- `23..22`：保留。
- `21..20`：从关闭状态（Shutdown）唤醒的配置。
- `19`：保留。
- `18`：从待机状态（Standby）唤醒的能力。
- `17..16`：边沿检测配置。
- `15`：保留。
- `14..13`：上拉/下拉控制（Pull control）。
- `12..3`：保留。
- `2..0`：功能配置。

### 注释 3：原第 31 行

TI CC23X0 功能配置。

### 注释 4：原第 42 行

TI CC23X0 外设引脚映射（Peripheral pin mapping）。

### 注释 5：原第 227 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC23X0_PINCTRL_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cc23x0-pinctrl_8h.html)

---

[上一章](P003_bmp581_user.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_ccs811.h_源码浏览.md)
