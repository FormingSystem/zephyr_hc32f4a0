---
id: learning.zephyr-docs.api-source-workqueue-pin-control-reference.page-5
title: pinctrl-rzv-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_pinctrl-rzv-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h.html)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00019"></a>
<a id="l00069"></a>
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
<a id="l00124"></a>
<a id="l00134"></a>
<a id="l00135"></a>
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
<a id="l00195"></a>
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
<a id="l00215"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV_COMMON_H_




/* Superset list of all possible IO ports. */
#define PORT_00 0x0000 /* IO port 0 */
#define PORT_01 0x0100 /* IO port 1 */
#define PORT_02 0x0200 /* IO port 2 */
#define PORT_03 0x0300 /* IO port 3 */
#define PORT_04 0x0400 /* IO port 4 */
#define PORT_05 0x0500 /* IO port 5 */
#define PORT_06 0x0600 /* IO port 6 */
#define PORT_07 0x0700 /* IO port 7 */
#define PORT_08 0x0800 /* IO port 8 */
#define PORT_09 0x0900 /* IO port 9 */
#define PORT_10 0x0A00 /* IO port 10 */
#define PORT_11 0x0B00 /* IO port 11 */
#define PORT_12 0x0C00 /* IO port 12 */
#define PORT_13 0x0D00 /* IO port 13 */
#define PORT_14 0x0E00 /* IO port 14 */
#define PORT_15 0x0F00 /* IO port 15 */
#define PORT_16 0x1000 /* IO port 16 */
#define PORT_17 0x1100 /* IO port 17 */
#define PORT_18 0x1200 /* IO port 18 */
#define PORT_19 0x1300 /* IO port 19 */
#define PORT_20 0x1400 /* IO port 20 */
#define PORT_21 0x1500 /* IO port 21 */
#define PORT_22 0x1600 /* IO port 22 */
#define PORT_23 0x1700 /* IO port 23 */
#define PORT_24 0x1800 /* IO port 24 */
#define PORT_25 0x1900 /* IO port 25 */
#define PORT_26 0x1A00 /* IO port 26 */
#define PORT_27 0x1B00 /* IO port 27 */
#define PORT_28 0x1C00 /* IO port 28 */
#define PORT_29 0x1D00 /* IO port 29 */
#define PORT_30 0x1E00 /* IO port 30 */
#define PORT_31 0x1F00 /* IO port 31 */
#define PORT_32 0x2000 /* IO port 32 */
#define PORT_33 0x2100 /* IO port 33 */
#define PORT_34 0x2200 /* IO port 34 */
#define PORT_35 0x2300 /* IO port 35 */
#define PORT_36 0x2400 /* IO port 36 */
#define PORT_37 0x2500 /* IO port 37 */
#define PORT_38 0x2600 /* IO port 38 */
#define PORT_39 0x2700 /* IO port 39 */
#define PORT_40 0x2800 /* IO port 40 */
#define PORT_41 0x2900 /* IO port 41 */
#define PORT_42 0x2A00 /* IO port 42 */
#define PORT_43 0x2B00 /* IO port 43 */
#define PORT_44 0x2C00 /* IO port 44 */
#define PORT_45 0x2D00 /* IO port 45 */
#define PORT_46 0x2E00 /* IO port 46 */
#define PORT_47 0x2F00 /* IO port 47 */
#define PORT_48 0x3000 /* IO port 48 */


#define RZV_PINMUX(port, pin, func) (port | pin | (func << 4))


/* Special purpose port */
#define BSP_IO_NMI 0xFFFF0100 /* NMI */

#define BSP_IO_TMS_SWDIO 0xFFFF0200 /* TMS_SWDIO */

#define BSP_IO_TDO 0xFFFF0300 /* TDO */

#define BSP_IO_AUDIO_CLK1 0xFFFF0400 /* AUDIO_CLK1 */
#define BSP_IO_AUDIO_CLK2 0xFFFF0401 /* AUDIO_CLK2 */

#define BSP_IO_SD0_CLK   0xFFFF0600 /* SD0_CLK */
#define BSP_IO_SD0_CMD   0xFFFF0601 /* SD0_CMD */
#define BSP_IO_SD0_RST_N 0xFFFF0602 /* SD0_RST_N */

#define BSP_IO_SD0_DATA0 0xFFFF0700 /* SD0_DATA0 */
#define BSP_IO_SD0_DATA1 0xFFFF0701 /* SD0_DATA1 */
#define BSP_IO_SD0_DATA2 0xFFFF0702 /* SD0_DATA2 */
#define BSP_IO_SD0_DATA3 0xFFFF0703 /* SD0_DATA3 */
#define BSP_IO_SD0_DATA4 0xFFFF0704 /* SD0_DATA4 */
#define BSP_IO_SD0_DATA5 0xFFFF0705 /* SD0_DATA5 */
#define BSP_IO_SD0_DATA6 0xFFFF0706 /* SD0_DATA6 */
#define BSP_IO_SD0_DATA7 0xFFFF0707 /* SD0_DATA7 */

#define BSP_IO_SD1_CLK 0xFFFF0800 /* SD1_CLK */
#define BSP_IO_SD1_CMD 0xFFFF0801 /* SD1_CMD */

#define BSP_IO_SD1_DATA0 0xFFFF0900 /* SD1_DATA0 */
#define BSP_IO_SD1_DATA1 0xFFFF0901 /* SD1_DATA1 */
#define BSP_IO_SD1_DATA2 0xFFFF0902 /* SD1_DATA2 */
#define BSP_IO_SD1_DATA3 0xFFFF0903 /* SD1_DATA3 */

#define BSP_IO_QSPI0_SPCLK 0xFFFF0A00 /* QSPI0_SPCLK */
#define BSP_IO_QSPI0_IO0   0xFFFF0A01 /* QSPI0_IO0 */
#define BSP_IO_QSPI0_IO1   0xFFFF0A02 /* QSPI0_IO1 */
#define BSP_IO_QSPI0_IO2   0xFFFF0A03 /* QSPI0_IO2 */
#define BSP_IO_QSPI0_IO3   0xFFFF0A04 /* QSPI0_IO3 */
#define BSP_IO_QSPI0_SSL   0xFFFF0A05 /* QSPI0_SSL */

#define BSP_IO_QSPI1_SPCLK 0xFFFF0B00 /* QSPI1_SPCLK */
#define BSP_IO_QSPI1_IO0   0xFFFF0B01 /* QSPI1_IO0 */
#define BSP_IO_QSPI1_IO1   0xFFFF0B02 /* QSPI1_IO1 */
#define BSP_IO_QSPI1_IO2   0xFFFF0B03 /* QSPI1_IO2 */
#define BSP_IO_QSPI1_IO3   0xFFFF0B04 /* QSPI1_IO3 */
#define BSP_IO_QSPI1_SSL   0xFFFF0B05 /* QSPI1_SSL */

#define BSP_IO_QSPI_RESET_N 0xFFFF0C00 /* QSPI_RESET_N */
#define BSP_IO_QSPI_WP_N    0xFFFF0C01 /* QSPI_WP_N */
#define BSP_IO_QSPI_INT_N   0xFFFF0C02 /* QSPI_INT_N */

#define BSP_IO_WDTOVF_PERROUT_N 0xFFFF0D00 /* WDTOVF_PERROUT_N */

#define BSP_IO_RIIC0_SDA 0xFFFF0E00 /* RIIC0_SDA */
#define BSP_IO_RIIC0_SCL 0xFFFF0E01 /* RIIC0_SCL */
#define BSP_IO_RIIC1_SDA 0xFFFF0E02 /* RIIC1_SDA */
#define BSP_IO_RIIC1_SCL 0xFFFF0E03 /* RIIC1_SCL */



#define RZV_FILNUM_4_STAGE  0
#define RZV_FILNUM_8_STAGE  1
#define RZV_FILNUM_12_STAGE 2
#define RZV_FILNUM_16_STAGE 3

#define RZV_FILCLKSEL_NOT_DIV   0
#define RZV_FILCLKSEL_DIV_9000  1
#define RZV_FILCLKSEL_DIV_18000 2
#define RZV_FILCLKSEL_DIV_36000 3


#define RZV_FILTER_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV_COMMON_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 72 行

包含所有可能 I/O 端口的超集列表（Superset list）。

### 注释 3：原第 73 行

输入输出端口（I/O Port）0。

### 注释 4：原第 74 行

输入输出端口（I/O Port）1。

### 注释 5：原第 75 行

输入输出端口（I/O Port）2。

### 注释 6：原第 76 行

输入输出端口（I/O Port）3。

### 注释 7：原第 77 行

输入输出端口（I/O Port）4。

### 注释 8：原第 78 行

输入输出端口（I/O Port）5。

### 注释 9：原第 79 行

输入输出端口（I/O Port）6。

### 注释 10：原第 80 行

输入输出端口（I/O Port）7。

### 注释 11：原第 81 行

输入输出端口（I/O Port）8。

### 注释 12：原第 82 行

输入输出端口（I/O Port）9。

### 注释 13：原第 83 行

输入输出端口（I/O Port）10。

### 注释 14：原第 84 行

输入输出端口（I/O Port）11。

### 注释 15：原第 85 行

输入输出端口（I/O Port）12。

### 注释 16：原第 86 行

输入输出端口（I/O Port）13。

### 注释 17：原第 87 行

输入输出端口（I/O Port）14。

### 注释 18：原第 88 行

输入输出端口（I/O Port）15。

### 注释 19：原第 89 行

输入输出端口（I/O Port）16。

### 注释 20：原第 90 行

输入输出端口（I/O Port）17。

### 注释 21：原第 91 行

输入输出端口（I/O Port）18。

### 注释 22：原第 92 行

输入输出端口（I/O Port）19。

### 注释 23：原第 93 行

输入输出端口（I/O Port）20。

### 注释 24：原第 94 行

输入输出端口（I/O Port）21。

### 注释 25：原第 95 行

输入输出端口（I/O Port）22。

### 注释 26：原第 96 行

输入输出端口（I/O Port）23。

### 注释 27：原第 97 行

输入输出端口（I/O Port）24。

### 注释 28：原第 98 行

输入输出端口（I/O Port）25。

### 注释 29：原第 99 行

输入输出端口（I/O Port）26。

### 注释 30：原第 100 行

输入输出端口（I/O Port）27。

### 注释 31：原第 101 行

输入输出端口（I/O Port）28。

### 注释 32：原第 102 行

输入输出端口（I/O Port）29。

### 注释 33：原第 103 行

输入输出端口（I/O Port）30。

### 注释 34：原第 104 行

输入输出端口（I/O Port）31。

### 注释 35：原第 105 行

输入输出端口（I/O Port）32。

### 注释 36：原第 106 行

输入输出端口（I/O Port）33。

### 注释 37：原第 107 行

输入输出端口（I/O Port）34。

### 注释 38：原第 108 行

输入输出端口（I/O Port）35。

### 注释 39：原第 109 行

输入输出端口（I/O Port）36。

### 注释 40：原第 110 行

输入输出端口（I/O Port）37。

### 注释 41：原第 111 行

输入输出端口（I/O Port）38。

### 注释 42：原第 112 行

输入输出端口（I/O Port）39。

### 注释 43：原第 113 行

输入输出端口（I/O Port）40。

### 注释 44：原第 114 行

输入输出端口（I/O Port）41。

### 注释 45：原第 115 行

输入输出端口（I/O Port）42。

### 注释 46：原第 116 行

输入输出端口（I/O Port）43。

### 注释 47：原第 117 行

输入输出端口（I/O Port）44。

### 注释 48：原第 118 行

输入输出端口（I/O Port）45。

### 注释 49：原第 119 行

输入输出端口（I/O Port）46。

### 注释 50：原第 120 行

输入输出端口（I/O Port）47。

### 注释 51：原第 121 行

输入输出端口（I/O Port）48。

### 注释 52：原第 138 行

专用端口（Special Purpose Port）。

### 注释 53：原第 139 行

不可屏蔽中断（NMI）。

### 注释 54：原第 141 行

引脚功能（Pin Function）：`TMS_SWDIO`。

### 注释 55：原第 143 行

引脚功能（Pin Function）：`TDO`。

### 注释 56：原第 145 行

引脚功能（Pin Function）：`AUDIO_CLK1`。

### 注释 57：原第 146 行

引脚功能（Pin Function）：`AUDIO_CLK2`。

### 注释 58：原第 148 行

引脚功能（Pin Function）：`SD0_CLK`。

### 注释 59：原第 149 行

引脚功能（Pin Function）：`SD0_CMD`。

### 注释 60：原第 150 行

引脚功能（Pin Function）：`SD0_RST_N`。

### 注释 61：原第 152 行

引脚功能（Pin Function）：`SD0_DATA0`。

### 注释 62：原第 153 行

引脚功能（Pin Function）：`SD0_DATA1`。

### 注释 63：原第 154 行

引脚功能（Pin Function）：`SD0_DATA2`。

### 注释 64：原第 155 行

引脚功能（Pin Function）：`SD0_DATA3`。

### 注释 65：原第 156 行

引脚功能（Pin Function）：`SD0_DATA4`。

### 注释 66：原第 157 行

引脚功能（Pin Function）：`SD0_DATA5`。

### 注释 67：原第 158 行

引脚功能（Pin Function）：`SD0_DATA6`。

### 注释 68：原第 159 行

引脚功能（Pin Function）：`SD0_DATA7`。

### 注释 69：原第 161 行

引脚功能（Pin Function）：`SD1_CLK`。

### 注释 70：原第 162 行

引脚功能（Pin Function）：`SD1_CMD`。

### 注释 71：原第 164 行

引脚功能（Pin Function）：`SD1_DATA0`。

### 注释 72：原第 165 行

引脚功能（Pin Function）：`SD1_DATA1`。

### 注释 73：原第 166 行

引脚功能（Pin Function）：`SD1_DATA2`。

### 注释 74：原第 167 行

引脚功能（Pin Function）：`SD1_DATA3`。

### 注释 75：原第 169 行

引脚功能（Pin Function）：`QSPI0_SPCLK`。

### 注释 76：原第 170 行

引脚功能（Pin Function）：`QSPI0_IO0`。

### 注释 77：原第 171 行

引脚功能（Pin Function）：`QSPI0_IO1`。

### 注释 78：原第 172 行

引脚功能（Pin Function）：`QSPI0_IO2`。

### 注释 79：原第 173 行

引脚功能（Pin Function）：`QSPI0_IO3`。

### 注释 80：原第 174 行

引脚功能（Pin Function）：`QSPI0_SSL`。

### 注释 81：原第 176 行

引脚功能（Pin Function）：`QSPI1_SPCLK`。

### 注释 82：原第 177 行

引脚功能（Pin Function）：`QSPI1_IO0`。

### 注释 83：原第 178 行

引脚功能（Pin Function）：`QSPI1_IO1`。

### 注释 84：原第 179 行

引脚功能（Pin Function）：`QSPI1_IO2`。

### 注释 85：原第 180 行

引脚功能（Pin Function）：`QSPI1_IO3`。

### 注释 86：原第 181 行

引脚功能（Pin Function）：`QSPI1_SSL`。

### 注释 87：原第 183 行

引脚功能（Pin Function）：`QSPI_RESET_N`。

### 注释 88：原第 184 行

引脚功能（Pin Function）：`QSPI_WP_N`。

### 注释 89：原第 185 行

引脚功能（Pin Function）：`QSPI_INT_N`。

### 注释 90：原第 187 行

引脚功能（Pin Function）：`WDTOVF_PERROUT_N`。

### 注释 91：原第 189 行

引脚功能（Pin Function）：`RIIC0_SDA`。

### 注释 92：原第 190 行

引脚功能（Pin Function）：`RIIC0_SCL`。

### 注释 93：原第 191 行

引脚功能（Pin Function）：`RIIC1_SDA`。

### 注释 94：原第 192 行

引脚功能（Pin Function）：`RIIC1_SCL`。

### 注释 95：原第 232 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV_COMMON_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv-common_8h.html)

---

[上一章](P004_pinctrl-rzg2-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_pinctrl-rzv2h.h_源码浏览.md)
