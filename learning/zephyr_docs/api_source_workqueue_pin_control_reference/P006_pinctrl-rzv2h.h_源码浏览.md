---
id: learning.zephyr-docs.api-source-workqueue-pin-control-reference.page-6
title: pinctrl-rzv2h.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv2h_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_pinctrl-rzv2h.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzv2h_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P298_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2h.h_文件参考.md)。

## 6.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
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
<a id="l00152"></a>
<a id="l00153"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV2H_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV2H_H_


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

/*
 * Create the value contain port/pin/function information
 *
 * port: port number BSP_IO_PORT_00..BSP_IO_PORT_11
 * pin: pin number
 * func: pin function
 */
#define RZV_PINMUX(port, pin, func) (port | pin | (func << 4))

/* Special purpose port */
#define BSP_IO_NMI 0xFFFF0100 /* NMI */

#define BSP_IO_TMS_SWDIO 0xFFFF0300 /* TMS_SWDIO */

#define BSP_IO_TDO 0xFFFF0302 /* TDO */

#define BSP_IO_WDTUDFCA 0xFFFF0500 /* WDTUDFCA */
#define BSP_IO_WDTUDFCM 0xFFFF0501 /* WDTUDFCM */

#define BSP_IO_SCIF_RXD 0xFFFF0600 /* SCIF_RXD */
#define BSP_IO_SCIF_TXD 0xFFFF0601 /* SCIF_TXD */

#define BSP_IO_XSPI0_CKP     0xFFFF0700 /* XSPI0_CKP */
#define BSP_IO_XSPI0_CKN     0xFFFF0701 /* XSPI0_CKN */
#define BSP_IO_XSPI0_CS0N    0xFFFF0702 /* XSPI0_CS0N */
#define BSP_IO_XSPI0_DS      0xFFFF0703 /* XSPI0_DS */
#define BSP_IO_XSPI0_RESET0N 0xFFFF0704 /* XSPI0_RESET0N */
#define BSP_IO_XSPI0_RSTO0N  0xFFFF0705 /* XSPI0_RSTO0N */
#define BSP_IO_XSPI0_INT0N   0xFFFF0706 /* XSPI0_INT0N */
#define BSP_IO_XSPI0_ECS0N   0xFFFF0707 /* XSPI0_ECS0N */

#define BSP_IO_XSPI0_IO0 0xFFFF0800 /* XSPI0_IO0 */
#define BSP_IO_XSPI0_IO1 0xFFFF0801 /* XSPI0_IO1 */
#define BSP_IO_XSPI0_IO2 0xFFFF0802 /* XSPI0_IO2 */
#define BSP_IO_XSPI0_IO3 0xFFFF0803 /* XSPI0_IO3 */
#define BSP_IO_XSPI0_IO4 0xFFFF0804 /* XSPI0_IO4 */
#define BSP_IO_XSPI0_IO5 0xFFFF0805 /* XSPI0_IO5 */
#define BSP_IO_XSPI0_IO6 0xFFFF0806 /* XSPI0_IO6 */
#define BSP_IO_XSPI0_IO7 0xFFFF0807 /* XSPI0_IO7 */

#define BSP_IO_SD0CLK  0xFFFF0900 /* SD0CLK */
#define BSP_IO_SD0CMD  0xFFFF0901 /* SD0CMD */
#define BSP_IO_SD0RSTN 0xFFFF0902 /* SD0RSTN */

#define BSP_IO_SD0DAT0 0xFFFF0A00 /* SD0DAT0 */
#define BSP_IO_SD0DAT1 0xFFFF0A01 /* SD0DAT1 */
#define BSP_IO_SD0DAT2 0xFFFF0A02 /* SD0DAT2 */
#define BSP_IO_SD0DAT3 0xFFFF0A03 /* SD0DAT3 */
#define BSP_IO_SD0DAT4 0xFFFF0A04 /* SD0DAT4 */
#define BSP_IO_SD0DAT5 0xFFFF0A05 /* SD0DAT5 */
#define BSP_IO_SD0DAT6 0xFFFF0A06 /* SD0DAT6 */
#define BSP_IO_SD0DAT7 0xFFFF0A07 /* SD0DAT7 */

#define BSP_IO_SD1CLK 0xFFFF0B00 /* SD1CLK */
#define BSP_IO_SD1CMD 0xFFFF0B01 /* SD1CMD */

#define BSP_IO_SD1DAT0 0xFFFF0C00 /* SD1DAT0 */
#define BSP_IO_SD1DAT1 0xFFFF0C01 /* SD1DAT1 */
#define BSP_IO_SD1DAT2 0xFFFF0C02 /* SD1DAT2 */
#define BSP_IO_SD1DAT3 0xFFFF0C03 /* SD1DAT3 */

#define BSP_IO_PCIE0_RSTOUTB 0xFFFF0E00 /* PCIE0_RSTOUTB */
#define BSP_IO_PCIE1_RSTOUTB 0xFFFF0E01 /* PCIE1_RSTOUTB */

#define BSP_IO_ET0_MDIO 0xFFFF0F00 /* ET0_MDIO */
#define BSP_IO_ET0_MDC  0xFFFF0F01 /* ET0_MDC */

#define BSP_IO_ET0_RXCTL_RXDV 0xFFFF1000 /* ET0_RXCTL_RXDV */
#define BSP_IO_ET0_TXCTL_TXEN 0xFFFF1001 /* ET0_TXCTL_TXEN */
#define BSP_IO_ET0_TXER       0xFFFF1002 /* ET0_TXER */
#define BSP_IO_ET0_RXER       0xFFFF1003 /* ET0_RXER */
#define BSP_IO_ET0_RXC_RXCLK  0xFFFF1004 /* ET0_RXC_RXCLK */
#define BSP_IO_ET0_TXC_TXCLK  0xFFFF1005 /* ET0_TXC_TXCLK */
#define BSP_IO_ET0_CRS        0xFFFF1006 /* ET0_CRS */
#define BSP_IO_ET0_COL        0xFFFF1007 /* ET0_COL */

#define BSP_IO_ET0_TXD0 0xFFFF1100 /* ET0_TXD0 */
#define BSP_IO_ET0_TXD1 0xFFFF1101 /* ET0_TXD1 */
#define BSP_IO_ET0_TXD2 0xFFFF1102 /* ET0_TXD2 */
#define BSP_IO_ET0_TXD3 0xFFFF1103 /* ET0_TXD3 */
#define BSP_IO_ET0_RXD0 0xFFFF1104 /* ET0_RXD0 */
#define BSP_IO_ET0_RXD1 0xFFFF1105 /* ET0_RXD1 */
#define BSP_IO_ET0_RXD2 0xFFFF1106 /* ET0_RXD2 */
#define BSP_IO_ET0_RXD3 0xFFFF1107 /* ET0_RXD3 */

#define BSP_IO_ET1_MDIO 0xFFFF1200 /* ET1_MDIO */
#define BSP_IO_ET1_MDC  0xFFFF1201 /* ET1_MDC */

#define BSP_IO_ET1_RXCTL_RXDV 0xFFFF1300 /* ET1_RXCTL_RXDV */
#define BSP_IO_ET1_TXCTL_TXEN 0xFFFF1301 /* ET1_TXCTL_TXEN */
#define BSP_IO_ET1_TXER       0xFFFF1302 /* ET1_TXER */
#define BSP_IO_ET1_RXER       0xFFFF1303 /* ET1_RXER */
#define BSP_IO_ET1_RXC_RXCLK  0xFFFF1304 /* ET1_RXC_RXCLK */
#define BSP_IO_ET1_TXC_TXCLK  0xFFFF1305 /* ET1_TXC_TXCLK */
#define BSP_IO_ET1_CRS        0xFFFF1306 /* ET1_CRS */
#define BSP_IO_ET1_COL        0xFFFF1307 /* ET1_COL */

#define BSP_IO_ET1_TXD0 0xFFFF1400 /* ET1_TXD0 */
#define BSP_IO_ET1_TXD1 0xFFFF1401 /* ET1_TXD1 */
#define BSP_IO_ET1_TXD2 0xFFFF1402 /* ET1_TXD2 */
#define BSP_IO_ET1_TXD3 0xFFFF1403 /* ET1_TXD3 */
#define BSP_IO_ET1_RXD0 0xFFFF1404 /* ET1_RXD0 */
#define BSP_IO_ET1_RXD1 0xFFFF1405 /* ET1_RXD1 */
#define BSP_IO_ET1_RXD2 0xFFFF1406 /* ET1_RXD2 */
#define BSP_IO_ET1_RXD3 0xFFFF1407 /* ET1_RXD3 */

/* FILNUM */
#define RZV_FILNUM_4_STAGE  0
#define RZV_FILNUM_8_STAGE  1
#define RZV_FILNUM_12_STAGE 2
#define RZV_FILNUM_16_STAGE 3

/* FILCLKSEL */
#define RZV_FILCLKSEL_NOT_DIV   0
#define RZV_FILCLKSEL_DIV_9000  1
#define RZV_FILCLKSEL_DIV_18000 2
#define RZV_FILCLKSEL_DIV_36000 3

#define RZV_FILTER_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV2H_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 17 行

包含所有可能 I/O 端口的超集列表（Superset list）。

### 注释 3：原第 18 行

输入输出端口（I/O Port）0。

### 注释 4：原第 19 行

输入输出端口（I/O Port）1。

### 注释 5：原第 20 行

输入输出端口（I/O Port）2。

### 注释 6：原第 21 行

输入输出端口（I/O Port）3。

### 注释 7：原第 22 行

输入输出端口（I/O Port）4。

### 注释 8：原第 23 行

输入输出端口（I/O Port）5。

### 注释 9：原第 24 行

输入输出端口（I/O Port）6。

### 注释 10：原第 25 行

输入输出端口（I/O Port）7。

### 注释 11：原第 26 行

输入输出端口（I/O Port）8。

### 注释 12：原第 27 行

输入输出端口（I/O Port）9。

### 注释 13：原第 28 行

输入输出端口（I/O Port）10。

### 注释 14：原第 29 行

输入输出端口（I/O Port）11。

### 注释 15：原第 31 行

创建包含端口／引脚／功能信息的值。

- `port`：端口编号，范围为 `BSP_IO_PORT_00..BSP_IO_PORT_11`。
- `pin`：引脚编号（Pin Number）。
- `func`：引脚功能（Pin Function）。

### 注释 16：原第 40 行

专用端口（Special Purpose Port）。

### 注释 17：原第 41 行

不可屏蔽中断（NMI）。

### 注释 18：原第 43 行

引脚功能（Pin Function）：`TMS_SWDIO`。

### 注释 19：原第 45 行

引脚功能（Pin Function）：`TDO`。

### 注释 20：原第 47 行

引脚功能（Pin Function）：`WDTUDFCA`。

### 注释 21：原第 48 行

引脚功能（Pin Function）：`WDTUDFCM`。

### 注释 22：原第 50 行

引脚功能（Pin Function）：`SCIF_RXD`。

### 注释 23：原第 51 行

引脚功能（Pin Function）：`SCIF_TXD`。

### 注释 24：原第 53 行

引脚功能（Pin Function）：`XSPI0_CKP`。

### 注释 25：原第 54 行

引脚功能（Pin Function）：`XSPI0_CKN`。

### 注释 26：原第 55 行

引脚功能（Pin Function）：`XSPI0_CS0N`。

### 注释 27：原第 56 行

引脚功能（Pin Function）：`XSPI0_DS`。

### 注释 28：原第 57 行

引脚功能（Pin Function）：`XSPI0_RESET0N`。

### 注释 29：原第 58 行

引脚功能（Pin Function）：`XSPI0_RSTO0N`。

### 注释 30：原第 59 行

引脚功能（Pin Function）：`XSPI0_INT0N`。

### 注释 31：原第 60 行

引脚功能（Pin Function）：`XSPI0_ECS0N`。

### 注释 32：原第 62 行

引脚功能（Pin Function）：`XSPI0_IO0`。

### 注释 33：原第 63 行

引脚功能（Pin Function）：`XSPI0_IO1`。

### 注释 34：原第 64 行

引脚功能（Pin Function）：`XSPI0_IO2`。

### 注释 35：原第 65 行

引脚功能（Pin Function）：`XSPI0_IO3`。

### 注释 36：原第 66 行

引脚功能（Pin Function）：`XSPI0_IO4`。

### 注释 37：原第 67 行

引脚功能（Pin Function）：`XSPI0_IO5`。

### 注释 38：原第 68 行

引脚功能（Pin Function）：`XSPI0_IO6`。

### 注释 39：原第 69 行

引脚功能（Pin Function）：`XSPI0_IO7`。

### 注释 40：原第 71 行

引脚功能（Pin Function）：`SD0CLK`。

### 注释 41：原第 72 行

引脚功能（Pin Function）：`SD0CMD`。

### 注释 42：原第 73 行

引脚功能（Pin Function）：`SD0RSTN`。

### 注释 43：原第 75 行

引脚功能（Pin Function）：`SD0DAT0`。

### 注释 44：原第 76 行

引脚功能（Pin Function）：`SD0DAT1`。

### 注释 45：原第 77 行

引脚功能（Pin Function）：`SD0DAT2`。

### 注释 46：原第 78 行

引脚功能（Pin Function）：`SD0DAT3`。

### 注释 47：原第 79 行

引脚功能（Pin Function）：`SD0DAT4`。

### 注释 48：原第 80 行

引脚功能（Pin Function）：`SD0DAT5`。

### 注释 49：原第 81 行

引脚功能（Pin Function）：`SD0DAT6`。

### 注释 50：原第 82 行

引脚功能（Pin Function）：`SD0DAT7`。

### 注释 51：原第 84 行

引脚功能（Pin Function）：`SD1CLK`。

### 注释 52：原第 85 行

引脚功能（Pin Function）：`SD1CMD`。

### 注释 53：原第 87 行

引脚功能（Pin Function）：`SD1DAT0`。

### 注释 54：原第 88 行

引脚功能（Pin Function）：`SD1DAT1`。

### 注释 55：原第 89 行

引脚功能（Pin Function）：`SD1DAT2`。

### 注释 56：原第 90 行

引脚功能（Pin Function）：`SD1DAT3`。

### 注释 57：原第 92 行

引脚功能（Pin Function）：`PCIE0_RSTOUTB`。

### 注释 58：原第 93 行

引脚功能（Pin Function）：`PCIE1_RSTOUTB`。

### 注释 59：原第 95 行

引脚功能（Pin Function）：`ET0_MDIO`。

### 注释 60：原第 96 行

引脚功能（Pin Function）：`ET0_MDC`。

### 注释 61：原第 98 行

引脚功能（Pin Function）：`ET0_RXCTL_RXDV`。

### 注释 62：原第 99 行

引脚功能（Pin Function）：`ET0_TXCTL_TXEN`。

### 注释 63：原第 100 行

引脚功能（Pin Function）：`ET0_TXER`。

### 注释 64：原第 101 行

引脚功能（Pin Function）：`ET0_RXER`。

### 注释 65：原第 102 行

引脚功能（Pin Function）：`ET0_RXC_RXCLK`。

### 注释 66：原第 103 行

引脚功能（Pin Function）：`ET0_TXC_TXCLK`。

### 注释 67：原第 104 行

引脚功能（Pin Function）：`ET0_CRS`。

### 注释 68：原第 105 行

引脚功能（Pin Function）：`ET0_COL`。

### 注释 69：原第 107 行

引脚功能（Pin Function）：`ET0_TXD0`。

### 注释 70：原第 108 行

引脚功能（Pin Function）：`ET0_TXD1`。

### 注释 71：原第 109 行

引脚功能（Pin Function）：`ET0_TXD2`。

### 注释 72：原第 110 行

引脚功能（Pin Function）：`ET0_TXD3`。

### 注释 73：原第 111 行

引脚功能（Pin Function）：`ET0_RXD0`。

### 注释 74：原第 112 行

引脚功能（Pin Function）：`ET0_RXD1`。

### 注释 75：原第 113 行

引脚功能（Pin Function）：`ET0_RXD2`。

### 注释 76：原第 114 行

引脚功能（Pin Function）：`ET0_RXD3`。

### 注释 77：原第 116 行

引脚功能（Pin Function）：`ET1_MDIO`。

### 注释 78：原第 117 行

引脚功能（Pin Function）：`ET1_MDC`。

### 注释 79：原第 119 行

引脚功能（Pin Function）：`ET1_RXCTL_RXDV`。

### 注释 80：原第 120 行

引脚功能（Pin Function）：`ET1_TXCTL_TXEN`。

### 注释 81：原第 121 行

引脚功能（Pin Function）：`ET1_TXER`。

### 注释 82：原第 122 行

引脚功能（Pin Function）：`ET1_RXER`。

### 注释 83：原第 123 行

引脚功能（Pin Function）：`ET1_RXC_RXCLK`。

### 注释 84：原第 124 行

引脚功能（Pin Function）：`ET1_TXC_TXCLK`。

### 注释 85：原第 125 行

引脚功能（Pin Function）：`ET1_CRS`。

### 注释 86：原第 126 行

引脚功能（Pin Function）：`ET1_COL`。

### 注释 87：原第 128 行

引脚功能（Pin Function）：`ET1_TXD0`。

### 注释 88：原第 129 行

引脚功能（Pin Function）：`ET1_TXD1`。

### 注释 89：原第 130 行

引脚功能（Pin Function）：`ET1_TXD2`。

### 注释 90：原第 131 行

引脚功能（Pin Function）：`ET1_TXD3`。

### 注释 91：原第 132 行

引脚功能（Pin Function）：`ET1_RXD0`。

### 注释 92：原第 133 行

引脚功能（Pin Function）：`ET1_RXD1`。

### 注释 93：原第 134 行

引脚功能（Pin Function）：`ET1_RXD2`。

### 注释 94：原第 135 行

引脚功能（Pin Function）：`ET1_RXD3`。

### 注释 95：原第 137 行

引脚功能（Pin Function）：`FILNUM`。

### 注释 96：原第 143 行

引脚功能（Pin Function）：`FILCLKSEL`。

### 注释 97：原第 153 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZV2H_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P298_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzv2h.h_文件参考.md)

---

[上一章](P005_pinctrl-rzv-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_pinctrl-rzv2n.h_源码浏览.md)
