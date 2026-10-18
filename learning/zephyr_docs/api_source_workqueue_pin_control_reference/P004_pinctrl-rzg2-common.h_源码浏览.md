---
id: learning.zephyr-docs.api-source-workqueue-pin-control-reference.page-4
title: pinctrl-rzg2-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg2-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_pinctrl-rzg2-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rzg2-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P297_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg2-common.h_文件参考.md)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00147"></a>
<a id="l00148"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG2_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG2_COMMON_H_


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

/*
 * Create the value contain port/pin/function information
 *
 * port: port number BSP_IO_PORT_00..BSP_IO_PORT_48
 * pin: pin number
 * func: pin function
 */
#define RZG_PINMUX(port, pin, func) (port | pin | (func << 4))

/* Special purpose port */
#define BSP_IO_NMI 0xFFFF0100 /* NMI */

#define BSP_IO_TMS_SWDIO 0xFFFF0200 /* TMS_SWDIO */
#define BSP_IO_TDO       0xFFFF0300 /* TDO */

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

/* FILNUM */
#define RZG_FILNUM_4_STAGE  0
#define RZG_FILNUM_8_STAGE  1
#define RZG_FILNUM_12_STAGE 2
#define RZG_FILNUM_16_STAGE 3

/* FILCLKSEL */
#define RZG_FILCLKSEL_NOT_DIV   0
#define RZG_FILCLKSEL_DIV_9000  1
#define RZG_FILCLKSEL_DIV_18000 2
#define RZG_FILCLKSEL_DIV_36000 3

#define RZG_FILTER_SET(filnum, filclksel) (((filnum) & 0x3) << 0x2) | (filclksel & 0x3)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG2_COMMON_H_ */
```

## 4.2\_可见注释译文（Comments）

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

### 注释 15：原第 30 行

输入输出端口（I/O Port）12。

### 注释 16：原第 31 行

输入输出端口（I/O Port）13。

### 注释 17：原第 32 行

输入输出端口（I/O Port）14。

### 注释 18：原第 33 行

输入输出端口（I/O Port）15。

### 注释 19：原第 34 行

输入输出端口（I/O Port）16。

### 注释 20：原第 35 行

输入输出端口（I/O Port）17。

### 注释 21：原第 36 行

输入输出端口（I/O Port）18。

### 注释 22：原第 37 行

输入输出端口（I/O Port）19。

### 注释 23：原第 38 行

输入输出端口（I/O Port）20。

### 注释 24：原第 39 行

输入输出端口（I/O Port）21。

### 注释 25：原第 40 行

输入输出端口（I/O Port）22。

### 注释 26：原第 41 行

输入输出端口（I/O Port）23。

### 注释 27：原第 42 行

输入输出端口（I/O Port）24。

### 注释 28：原第 43 行

输入输出端口（I/O Port）25。

### 注释 29：原第 44 行

输入输出端口（I/O Port）26。

### 注释 30：原第 45 行

输入输出端口（I/O Port）27。

### 注释 31：原第 46 行

输入输出端口（I/O Port）28。

### 注释 32：原第 47 行

输入输出端口（I/O Port）29。

### 注释 33：原第 48 行

输入输出端口（I/O Port）30。

### 注释 34：原第 49 行

输入输出端口（I/O Port）31。

### 注释 35：原第 50 行

输入输出端口（I/O Port）32。

### 注释 36：原第 51 行

输入输出端口（I/O Port）33。

### 注释 37：原第 52 行

输入输出端口（I/O Port）34。

### 注释 38：原第 53 行

输入输出端口（I/O Port）35。

### 注释 39：原第 54 行

输入输出端口（I/O Port）36。

### 注释 40：原第 55 行

输入输出端口（I/O Port）37。

### 注释 41：原第 56 行

输入输出端口（I/O Port）38。

### 注释 42：原第 57 行

输入输出端口（I/O Port）39。

### 注释 43：原第 58 行

输入输出端口（I/O Port）40。

### 注释 44：原第 59 行

输入输出端口（I/O Port）41。

### 注释 45：原第 60 行

输入输出端口（I/O Port）42。

### 注释 46：原第 61 行

输入输出端口（I/O Port）43。

### 注释 47：原第 62 行

输入输出端口（I/O Port）44。

### 注释 48：原第 63 行

输入输出端口（I/O Port）45。

### 注释 49：原第 64 行

输入输出端口（I/O Port）46。

### 注释 50：原第 65 行

输入输出端口（I/O Port）47。

### 注释 51：原第 66 行

输入输出端口（I/O Port）48。

### 注释 52：原第 68 行

创建包含端口／引脚／功能信息的值。

- `port`：端口编号，范围为 `BSP_IO_PORT_00..BSP_IO_PORT_48`。
- `pin`：引脚编号（Pin Number）。
- `func`：引脚功能（Pin Function）。

### 注释 53：原第 77 行

专用端口（Special Purpose Port）。

### 注释 54：原第 78 行

不可屏蔽中断（NMI）。

### 注释 55：原第 80 行

引脚功能（Pin Function）：`TMS_SWDIO`。

### 注释 56：原第 81 行

引脚功能（Pin Function）：`TDO`。

### 注释 57：原第 83 行

引脚功能（Pin Function）：`AUDIO_CLK1`。

### 注释 58：原第 84 行

引脚功能（Pin Function）：`AUDIO_CLK2`。

### 注释 59：原第 86 行

引脚功能（Pin Function）：`SD0_CLK`。

### 注释 60：原第 87 行

引脚功能（Pin Function）：`SD0_CMD`。

### 注释 61：原第 88 行

引脚功能（Pin Function）：`SD0_RST_N`。

### 注释 62：原第 90 行

引脚功能（Pin Function）：`SD0_DATA0`。

### 注释 63：原第 91 行

引脚功能（Pin Function）：`SD0_DATA1`。

### 注释 64：原第 92 行

引脚功能（Pin Function）：`SD0_DATA2`。

### 注释 65：原第 93 行

引脚功能（Pin Function）：`SD0_DATA3`。

### 注释 66：原第 94 行

引脚功能（Pin Function）：`SD0_DATA4`。

### 注释 67：原第 95 行

引脚功能（Pin Function）：`SD0_DATA5`。

### 注释 68：原第 96 行

引脚功能（Pin Function）：`SD0_DATA6`。

### 注释 69：原第 97 行

引脚功能（Pin Function）：`SD0_DATA7`。

### 注释 70：原第 99 行

引脚功能（Pin Function）：`SD1_CLK`。

### 注释 71：原第 100 行

引脚功能（Pin Function）：`SD1_CMD`。

### 注释 72：原第 102 行

引脚功能（Pin Function）：`SD1_DATA0`。

### 注释 73：原第 103 行

引脚功能（Pin Function）：`SD1_DATA1`。

### 注释 74：原第 104 行

引脚功能（Pin Function）：`SD1_DATA2`。

### 注释 75：原第 105 行

引脚功能（Pin Function）：`SD1_DATA3`。

### 注释 76：原第 107 行

引脚功能（Pin Function）：`QSPI0_SPCLK`。

### 注释 77：原第 108 行

引脚功能（Pin Function）：`QSPI0_IO0`。

### 注释 78：原第 109 行

引脚功能（Pin Function）：`QSPI0_IO1`。

### 注释 79：原第 110 行

引脚功能（Pin Function）：`QSPI0_IO2`。

### 注释 80：原第 111 行

引脚功能（Pin Function）：`QSPI0_IO3`。

### 注释 81：原第 112 行

引脚功能（Pin Function）：`QSPI0_SSL`。

### 注释 82：原第 114 行

引脚功能（Pin Function）：`QSPI1_SPCLK`。

### 注释 83：原第 115 行

引脚功能（Pin Function）：`QSPI1_IO0`。

### 注释 84：原第 116 行

引脚功能（Pin Function）：`QSPI1_IO1`。

### 注释 85：原第 117 行

引脚功能（Pin Function）：`QSPI1_IO2`。

### 注释 86：原第 118 行

引脚功能（Pin Function）：`QSPI1_IO3`。

### 注释 87：原第 119 行

引脚功能（Pin Function）：`QSPI1_SSL`。

### 注释 88：原第 121 行

引脚功能（Pin Function）：`QSPI_RESET_N`。

### 注释 89：原第 122 行

引脚功能（Pin Function）：`QSPI_WP_N`。

### 注释 90：原第 123 行

引脚功能（Pin Function）：`QSPI_INT_N`。

### 注释 91：原第 125 行

引脚功能（Pin Function）：`WDTOVF_PERROUT_N`。

### 注释 92：原第 127 行

引脚功能（Pin Function）：`RIIC0_SDA`。

### 注释 93：原第 128 行

引脚功能（Pin Function）：`RIIC0_SCL`。

### 注释 94：原第 129 行

引脚功能（Pin Function）：`RIIC1_SDA`。

### 注释 95：原第 130 行

引脚功能（Pin Function）：`RIIC1_SCL`。

### 注释 96：原第 132 行

引脚功能（Pin Function）：`FILNUM`。

### 注释 97：原第 138 行

引脚功能（Pin Function）：`FILCLKSEL`。

### 注释 98：原第 148 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZG2_COMMON_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P297_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rzg2-common.h_文件参考.md)

---

[上一章](P003_lpc11u6x-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_pinctrl-rzv-common.h_源码浏览.md)
