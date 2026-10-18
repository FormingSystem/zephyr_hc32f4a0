---
id: learning.zephyr-docs.api-source-pin-register-fields-reference.page-3
title: pinctrl-rzg-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_pinctrl-rzg-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00068"></a>
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
<a id="l00093"></a>
<a id="l00103"></a>
<a id="l00104"></a>
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
<a id="l00159"></a>
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
<a id="l00179"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00196"></a>

```c
/*
 * Copyright (c) 2024 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG_COMMON_H_




/* Superset list of all possible IO ports. */
#define PORT_00 0x0000 /* IO port 0 */
#define PORT_01 0x1000 /* IO port 1 */
#define PORT_02 0x1100 /* IO port 2 */
#define PORT_03 0x1200 /* IO port 3 */
#define PORT_04 0x1300 /* IO port 4 */
#define PORT_05 0x0100 /* IO port 5 */
#define PORT_06 0x0200 /* IO port 6 */
#define PORT_07 0x1400 /* IO port 7 */
#define PORT_08 0x1500 /* IO port 8 */
#define PORT_09 0x1600 /* IO port 9 */
#define PORT_10 0x1700 /* IO port 10 */
#define PORT_11 0x0300 /* IO port 11 */
#define PORT_12 0x0400 /* IO port 12 */
#define PORT_13 0x0500 /* IO port 13 */
#define PORT_14 0x0600 /* IO port 14 */
#define PORT_15 0x0700 /* IO port 15 */
#define PORT_16 0x0800 /* IO port 16 */
#define PORT_17 0x0900 /* IO port 17 */
#define PORT_18 0x0A00 /* IO port 18 */


#define RZG_PINMUX(port, pin, func) (port | pin | (func << 4))


/* Special purpose port */
#define BSP_IO_NMI 0xFFFF0000 /* NMI */

#define BSP_IO_TMS_SWDIO 0xFFFF0100 /* TMS_SWDIO */
#define BSP_IO_TDO       0xFFFF0101 /* TDO */

#define BSP_IO_AUDIO_CLK1 0xFFFF0200 /* AUDIO_CLK1 */
#define BSP_IO_AUDIO_CLK2 0xFFFF0201 /* AUDIO_CLK2 */

#define BSP_IO_XSPI_SPCLK   0xFFFF0400 /* XSPI_SPCLK */
#define BSP_IO_XSPI_RESET_N 0xFFFF0401 /* XSPI_RESET_N */
#define BSP_IO_XSPI_WP_N    0xFFFF0402 /* XSPI_WP_N */
#define BSP_IO_XSPI_DS      0xFFFF0403 /* XSPI_DS */
#define BSP_IO_XSPI_CS0_N   0xFFFF0404 /* XSPI_CS0_N */
#define BSP_IO_XSPI_CS1_N   0xFFFF0405 /* XSPI_CS1_N */

#define BSP_IO_XSPI_IO0 0xFFFF0500 /* XSPI_IO0 */
#define BSP_IO_XSPI_IO1 0xFFFF0501 /* XSPI_IO1 */
#define BSP_IO_XSPI_IO2 0xFFFF0502 /* XSPI_IO2 */
#define BSP_IO_XSPI_IO3 0xFFFF0503 /* XSPI_IO3 */
#define BSP_IO_XSPI_IO4 0xFFFF0504 /* XSPI_IO4 */
#define BSP_IO_XSPI_IO5 0xFFFF0505 /* XSPI_IO5 */
#define BSP_IO_XSPI_IO6 0xFFFF0506 /* XSPI_IO6 */
#define BSP_IO_XSPI_IO7 0xFFFF0507 /* XSPI_IO7 */

#define BSP_IO_WDTOVF_PERROUT 0xFFFF0600 /* WDTOVF_PERROUT */

#define BSP_IO_I3C_SDA 0xFFFF0900 /* I3C_SDA */
#define BSP_IO_I3C_SCL 0xFFFF0901 /* I3C_SCL */

#define BSP_IO_SD0_CLK   0xFFFF1000 /* CD0_CLK */
#define BSP_IO_SD0_CMD   0xFFFF1001 /* CD0_CMD */
#define BSP_IO_SD0_RST_N 0xFFFF1002 /* CD0_RST_N */

#define BSP_IO_SD0_DATA0 0xFFFF1100 /* SD0_DATA0 */
#define BSP_IO_SD0_DATA1 0xFFFF1101 /* SD0_DATA1 */
#define BSP_IO_SD0_DATA2 0xFFFF1102 /* SD0_DATA2 */
#define BSP_IO_SD0_DATA3 0xFFFF1103 /* SD0_DATA3 */
#define BSP_IO_SD0_DATA4 0xFFFF1104 /* SD0_DATA4 */
#define BSP_IO_SD0_DATA5 0xFFFF1105 /* SD0_DATA5 */
#define BSP_IO_SD0_DATA6 0xFFFF1106 /* SD0_DATA6 */
#define BSP_IO_SD0_DATA7 0xFFFF1107 /* SD0_DATA7 */

#define BSP_IO_SD1_CLK 0xFFFF1200 /* SD1_CLK */
#define BSP_IO_SD1_CMD 0xFFFF1201 /* SD1_CMD */

#define BSP_IO_SD1_DATA0 0xFFFF1300 /* SD1_DATA0 */
#define BSP_IO_SD1_DATA1 0xFFFF1301 /* SD1_DATA1 */
#define BSP_IO_SD1_DATA2 0xFFFF1302 /* SD1_DATA2 */
#define BSP_IO_SD1_DATA3 0xFFFF1303 /* SD1_DATA3 */



#define RZG_FILNUM_4_STAGE  0
#define RZG_FILNUM_8_STAGE  1
#define RZG_FILNUM_12_STAGE 2
#define RZG_FILNUM_16_STAGE 3

#define RZG_FILCLKSEL_NOT_DIV   0
#define RZG_FILCLKSEL_DIV_9000  1
#define RZG_FILCLKSEL_DIV_18000 2
#define RZG_FILCLKSEL_DIV_36000 3


#define RZG_FILTER_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG_COMMON_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

包含所有可能 I/O 端口的超集列表（Superset list）。

### 注释 3：原第 72 行

输入输出端口（I/O Port）0。

### 注释 4：原第 73 行

输入输出端口（I/O Port）1。

### 注释 5：原第 74 行

输入输出端口（I/O Port）2。

### 注释 6：原第 75 行

输入输出端口（I/O Port）3。

### 注释 7：原第 76 行

输入输出端口（I/O Port）4。

### 注释 8：原第 77 行

输入输出端口（I/O Port）5。

### 注释 9：原第 78 行

输入输出端口（I/O Port）6。

### 注释 10：原第 79 行

输入输出端口（I/O Port）7。

### 注释 11：原第 80 行

输入输出端口（I/O Port）8。

### 注释 12：原第 81 行

输入输出端口（I/O Port）9。

### 注释 13：原第 82 行

输入输出端口（I/O Port）10。

### 注释 14：原第 83 行

输入输出端口（I/O Port）11。

### 注释 15：原第 84 行

输入输出端口（I/O Port）12。

### 注释 16：原第 85 行

输入输出端口（I/O Port）13。

### 注释 17：原第 86 行

输入输出端口（I/O Port）14。

### 注释 18：原第 87 行

输入输出端口（I/O Port）15。

### 注释 19：原第 88 行

输入输出端口（I/O Port）16。

### 注释 20：原第 89 行

输入输出端口（I/O Port）17。

### 注释 21：原第 90 行

输入输出端口（I/O Port）18。

### 注释 22：原第 107 行

专用端口（Special Purpose Port）。

### 注释 23：原第 108 行

不可屏蔽中断（NMI）。

### 注释 24：原第 110 行

引脚功能（Pin Function）：`TMS_SWDIO`。

### 注释 25：原第 111 行

引脚功能（Pin Function）：`TDO`。

### 注释 26：原第 113 行

引脚功能（Pin Function）：`AUDIO_CLK1`。

### 注释 27：原第 114 行

引脚功能（Pin Function）：`AUDIO_CLK2`。

### 注释 28：原第 116 行

引脚功能（Pin Function）：`XSPI_SPCLK`。

### 注释 29：原第 117 行

引脚功能（Pin Function）：`XSPI_RESET_N`。

### 注释 30：原第 118 行

引脚功能（Pin Function）：`XSPI_WP_N`。

### 注释 31：原第 119 行

引脚功能（Pin Function）：`XSPI_DS`。

### 注释 32：原第 120 行

引脚功能（Pin Function）：`XSPI_CS0_N`。

### 注释 33：原第 121 行

引脚功能（Pin Function）：`XSPI_CS1_N`。

### 注释 34：原第 123 行

引脚功能（Pin Function）：`XSPI_IO0`。

### 注释 35：原第 124 行

引脚功能（Pin Function）：`XSPI_IO1`。

### 注释 36：原第 125 行

引脚功能（Pin Function）：`XSPI_IO2`。

### 注释 37：原第 126 行

引脚功能（Pin Function）：`XSPI_IO3`。

### 注释 38：原第 127 行

引脚功能（Pin Function）：`XSPI_IO4`。

### 注释 39：原第 128 行

引脚功能（Pin Function）：`XSPI_IO5`。

### 注释 40：原第 129 行

引脚功能（Pin Function）：`XSPI_IO6`。

### 注释 41：原第 130 行

引脚功能（Pin Function）：`XSPI_IO7`。

### 注释 42：原第 132 行

引脚功能（Pin Function）：`WDTOVF_PERROUT`。

### 注释 43：原第 134 行

引脚功能（Pin Function）：`I3C_SDA`。

### 注释 44：原第 135 行

引脚功能（Pin Function）：`I3C_SCL`。

### 注释 45：原第 137 行

引脚功能（Pin Function）：`CD0_CLK`。

### 注释 46：原第 138 行

引脚功能（Pin Function）：`CD0_CMD`。

### 注释 47：原第 139 行

引脚功能（Pin Function）：`CD0_RST_N`。

### 注释 48：原第 141 行

引脚功能（Pin Function）：`SD0_DATA0`。

### 注释 49：原第 142 行

引脚功能（Pin Function）：`SD0_DATA1`。

### 注释 50：原第 143 行

引脚功能（Pin Function）：`SD0_DATA2`。

### 注释 51：原第 144 行

引脚功能（Pin Function）：`SD0_DATA3`。

### 注释 52：原第 145 行

引脚功能（Pin Function）：`SD0_DATA4`。

### 注释 53：原第 146 行

引脚功能（Pin Function）：`SD0_DATA5`。

### 注释 54：原第 147 行

引脚功能（Pin Function）：`SD0_DATA6`。

### 注释 55：原第 148 行

引脚功能（Pin Function）：`SD0_DATA7`。

### 注释 56：原第 150 行

引脚功能（Pin Function）：`SD1_CLK`。

### 注释 57：原第 151 行

引脚功能（Pin Function）：`SD1_CMD`。

### 注释 58：原第 153 行

引脚功能（Pin Function）：`SD1_DATA0`。

### 注释 59：原第 154 行

引脚功能（Pin Function）：`SD1_DATA1`。

### 注释 60：原第 155 行

引脚功能（Pin Function）：`SD1_DATA2`。

### 注释 61：原第 156 行

引脚功能（Pin Function）：`SD1_DATA3`。

### 注释 62：原第 196 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG_COMMON_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg-common_8h.html)

---

[上一章](P002_pinctrl-rza-common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_sf32lb52x-pinctrl.h_源码浏览.md)
