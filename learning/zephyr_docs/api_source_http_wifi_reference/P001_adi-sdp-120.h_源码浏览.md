---
id: learning.zephyr-docs.api-source-http-wifi-reference.page-1
title: adi-sdp-120.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adi-sdp-120_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_adi-sdp-120.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/adi-sdp-120_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P001_zephyr__dt-bindings__gpio__adi-sdp-120.h_文件参考.md)。

## 1.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
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

```c


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_SDP_120_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_SDP_120_H_

/* GPIO */


#define SDP_120_IO(n) (n-1)

/* SPI */
#define SDP_120_SPI_D2                          SDP_120_IO(33)  /* SPI_D2 */
#define SDP_120_SPI_D3                          SDP_120_IO(34)  /* SPI_D3 */
#define SDP_120_SERIAL_INT                      SDP_120_IO(35)  /* SERIAL_INT */
#define SDP_120_SPI_SEL_B_N                     SDP_120_IO(37)  /* SPI_SEL_B_N */
#define SDP_120_SPI_SEL_C_N                     SDP_120_IO(38)  /* SPI_SEL_C_N */
#define SDP_120_SPI_SS_N                        SDP_120_IO(39)  /* SPI_SS_N */

/* GPIO */
#define SDP_120_GPIO0                           SDP_120_IO(43) /* GPIO0 */
#define SDP_120_GPIO2                           SDP_120_IO(44) /* GPIO2 */
#define SDP_120_GPIO4                           SDP_120_IO(45) /* GPIO4 */
#define SDP_120_GPIO6                           SDP_120_IO(47) /* GPIO6 */

/* TMR */
#define SDP_120_TMR_A                           SDP_120_IO(48) /* TMR_A */

/* USART */
#define SDP_120_UART_RX                         SDP_120_IO(59) /* UART2_RX */
#define SDP_120_UART_TX                         SDP_120_IO(62) /* UART2_TX */

/* TMR */
#define SDP_120_TMR_D                           SDP_120_IO(72) /* TMR_D */
#define SDP_120_TMR_B                           SDP_120_IO(73) /* TMR_B */

/* GPIO */
#define SDP_120_GPIO7                           SDP_120_IO(74) /* GPIO7 */
#define SDP_120_GPIO5                           SDP_120_IO(76) /* GPIO5 */
#define SDP_120_GPIO3                           SDP_120_IO(77) /* GPIO3 */
#define SDP_120_GPIO1                           SDP_120_IO(78) /* GPIO1  */

/* I2C */
#define SDP_120_SCL_0                           SDP_120_IO(79) /* SCL_0 */
#define SDP_120_SDA_0                           SDP_120_IO(80) /* SDA_0 */

/* SPI */
#define SDP_120_SPI_CLK                         SDP_120_IO(82) /* SPI_CLK */
#define SDP_120_SPI_MISO                        SDP_120_IO(83) /* SPI_MISO */
#define SDP_120_SPI_MOSI                        SDP_120_IO(84) /* SPI_MOSI */
#define SDP_120_SPI_SEL_A_N                     SDP_120_IO(85) /* SPI_SEL_A_N */

/* SPORT - no driver yet */
#define SDP_120_SPI_SPORT_TSCLK                 SDP_120_IO(87) /* SPORT_TSCLK */
#define SDP_120_SPI_SPORT_DT0                   SDP_120_IO(88) /* SPORT_DT0 */
#define SDP_120_SPI_SPORT_TFS                   SDP_120_IO(89) /* SPORT_TFS */
#define SDP_120_SPI_SPORT_RFS                   SDP_120_IO(90) /* SPORT_RFS */
#define SDP_120_SPI_SPORT_DR0                   SDP_120_IO(91) /* SPORT_DR0 */
#define SDP_120_SPI_SPORT_RSCLK                 SDP_120_IO(92) /* SPORT_RSCLK */

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_SDP_120_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 30 行

通用输入输出（GPIO）

### 注释 2：原第 38 行

串行外设接口（SPI）

### 注释 3：原第 39 行

引脚功能（Pin Function）：`SPI_D2`。

### 注释 4：原第 40 行

引脚功能（Pin Function）：`SPI_D3`。

### 注释 5：原第 41 行

引脚功能（Pin Function）：`SERIAL_INT`。

### 注释 6：原第 42 行

引脚功能（Pin Function）：`SPI_SEL_B_N`。

### 注释 7：原第 43 行

引脚功能（Pin Function）：`SPI_SEL_C_N`。

### 注释 8：原第 44 行

引脚功能（Pin Function）：`SPI_SS_N`。

### 注释 9：原第 46 行

通用输入输出（GPIO）

### 注释 10：原第 47 行

通用输入输出 0（GPIO0）。

### 注释 11：原第 48 行

引脚功能（Pin Function）：`GPIO2`。

### 注释 12：原第 49 行

引脚功能（Pin Function）：`GPIO4`。

### 注释 13：原第 50 行

引脚功能（Pin Function）：`GPIO6`。

### 注释 14：原第 52 行

引脚功能（Pin Function）：`TMR`。

### 注释 15：原第 53 行

引脚功能（Pin Function）：`TMR_A`。

### 注释 16：原第 55 行

引脚功能（Pin Function）：`USART`。

### 注释 17：原第 56 行

引脚功能（Pin Function）：`UART2_RX`。

### 注释 18：原第 57 行

引脚功能（Pin Function）：`UART2_TX`。

### 注释 19：原第 59 行

引脚功能（Pin Function）：`TMR`。

### 注释 20：原第 60 行

引脚功能（Pin Function）：`TMR_D`。

### 注释 21：原第 61 行

引脚功能（Pin Function）：`TMR_B`。

### 注释 22：原第 63 行

通用输入输出（GPIO）

### 注释 23：原第 64 行

引脚功能（Pin Function）：`GPIO7`。

### 注释 24：原第 65 行

引脚功能（Pin Function）：`GPIO5`。

### 注释 25：原第 66 行

引脚功能（Pin Function）：`GPIO3`。

### 注释 26：原第 67 行

通用输入输出 1（GPIO1）。

### 注释 27：原第 69 行

集成电路间总线（I2C）

### 注释 28：原第 70 行

引脚功能（Pin Function）：`SCL_0`。

### 注释 29：原第 71 行

引脚功能（Pin Function）：`SDA_0`。

### 注释 30：原第 73 行

串行外设接口（SPI）

### 注释 31：原第 74 行

引脚功能（Pin Function）：`SPI_CLK`。

### 注释 32：原第 75 行

引脚功能（Pin Function）：`SPI_MISO`。

### 注释 33：原第 76 行

引脚功能（Pin Function）：`SPI_MOSI`。

### 注释 34：原第 77 行

引脚功能（Pin Function）：`SPI_SEL_A_N`。

### 注释 35：原第 79 行

串行端口（SPORT），尚无驱动。

### 注释 36：原第 80 行

引脚功能（Pin Function）：`SPORT_TSCLK`。

### 注释 37：原第 81 行

引脚功能（Pin Function）：`SPORT_DT0`。

### 注释 38：原第 82 行

引脚功能（Pin Function）：`SPORT_TFS`。

### 注释 39：原第 83 行

引脚功能（Pin Function）：`SPORT_RFS`。

### 注释 40：原第 84 行

引脚功能（Pin Function）：`SPORT_DR0`。

### 注释 41：原第 85 行

引脚功能（Pin Function）：`SPORT_RSCLK`。

### 注释 42：原第 87 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_ADI_SDP_120_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P001_zephyr__dt-bindings__gpio__adi-sdp-120.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_amebadplus_clock.h_源码浏览.md)
