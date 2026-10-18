---
id: learning.zephyr-docs.api-source-packet-gnss-reference.page-1
title: cc13xx_cc26xx-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cc13xx__cc26xx-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_cc13xx\_cc26xx-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cc13xx__cc26xx-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P031_zephyr__dt-bindings__pinctrl__cc13xx_cc26xx-pinctrl.h_文件参考.md)。

## 1.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2015 - 2017, Texas Instruments Incorporated
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC13XX_CC26XX_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC13XX_CC26XX_PINCTRL_H_

/* Adapted from hal/ti/simplelink/source/ti/devices/cc13x2_cc26x2/driverlib/ioc.h */

/* IOC Peripheral Port Mapping */
#define IOC_PORT_GPIO             0x00000000  /* Default general purpose IO usage */
#define IOC_PORT_AON_CLK32K       0x00000007  /* AON External 32kHz clock */
#define IOC_PORT_AUX_IO           0x00000008  /* AUX IO Pin */
#define IOC_PORT_MCU_SSI0_RX      0x00000009  /* MCU SSI0 Receive Pin */
#define IOC_PORT_MCU_SSI0_TX      0x0000000A  /* MCU SSI0 Transmit Pin */
#define IOC_PORT_MCU_SSI0_FSS     0x0000000B  /* MCU SSI0 FSS Pin */
#define IOC_PORT_MCU_SSI0_CLK     0x0000000C  /* MCU SSI0 Clock Pin */
#define IOC_PORT_MCU_I2C_MSSDA    0x0000000D  /* MCU I2C Data Pin */
#define IOC_PORT_MCU_I2C_MSSCL    0x0000000E  /* MCU I2C Clock Pin */
#define IOC_PORT_MCU_UART0_RX     0x0000000F  /* MCU UART0 Receive Pin */
#define IOC_PORT_MCU_UART0_TX     0x00000010  /* MCU UART0 Transmit Pin */
#define IOC_PORT_MCU_UART0_CTS    0x00000011  /* MCU UART0 Clear To Send Pin */
#define IOC_PORT_MCU_UART0_RTS    0x00000012  /* MCU UART0 Request To Send Pin */
#define IOC_PORT_MCU_UART1_RX     0x00000013  /* MCU UART1 Receive Pin */
#define IOC_PORT_MCU_UART1_TX     0x00000014  /* MCU UART1 Transmit Pin */
#define IOC_PORT_MCU_UART1_CTS    0x00000015  /* MCU UART1 Clear To Send Pin */
#define IOC_PORT_MCU_UART1_RTS    0x00000016  /* MCU UART1 Request To Send Pin */
#define IOC_PORT_MCU_PORT_EVENT0  0x00000017  /* MCU PORT EVENT 0 */
#define IOC_PORT_MCU_PORT_EVENT1  0x00000018  /* MCU PORT EVENT 1 */
#define IOC_PORT_MCU_PORT_EVENT2  0x00000019  /* MCU PORT EVENT 2 */
#define IOC_PORT_MCU_PORT_EVENT3  0x0000001A  /* MCU PORT EVENT 3 */
#define IOC_PORT_MCU_PORT_EVENT4  0x0000001B  /* MCU PORT EVENT 4 */
#define IOC_PORT_MCU_PORT_EVENT5  0x0000001C  /* MCU PORT EVENT 5 */
#define IOC_PORT_MCU_PORT_EVENT6  0x0000001D  /* MCU PORT EVENT 6 */
#define IOC_PORT_MCU_PORT_EVENT7  0x0000001E  /* MCU PORT EVENT 7 */
#define IOC_PORT_MCU_SWV          0x00000020  /* Serial Wire Viewer */
#define IOC_PORT_MCU_SSI1_RX      0x00000021  /* MCU SSI1 Receive Pin */
#define IOC_PORT_MCU_SSI1_TX      0x00000022  /* MCU SSI1 Transmit Pin */
#define IOC_PORT_MCU_SSI1_FSS     0x00000023  /* MCU SSI1 FSS Pin */
#define IOC_PORT_MCU_SSI1_CLK     0x00000024  /* MCU SSI1 Clock Pin */
#define IOC_PORT_MCU_I2S_AD0      0x00000025  /* MCU I2S Data Pin 0 */
#define IOC_PORT_MCU_I2S_AD1      0x00000026  /* MCU I2S Data Pin 1 */
#define IOC_PORT_MCU_I2S_WCLK     0x00000027  /* MCU I2S Frame/Word Clock */
#define IOC_PORT_MCU_I2S_BCLK     0x00000028  /* MCU I2S Bit Clock */
#define IOC_PORT_MCU_I2S_MCLK     0x00000029  /* MCU I2S Master clock 2 */
#define IOC_PORT_RFC_TRC          0x0000002E  /* RF Core Tracer */
#define IOC_PORT_RFC_GPO0         0x0000002F  /* RC Core Data Out Pin 0 */
#define IOC_PORT_RFC_GPO1         0x00000030  /* RC Core Data Out Pin 1 */
#define IOC_PORT_RFC_GPO2         0x00000031  /* RC Core Data Out Pin 2 */
#define IOC_PORT_RFC_GPO3         0x00000032  /* RC Core Data Out Pin 3 */
#define IOC_PORT_RFC_GPI0         0x00000033  /* RC Core Data In Pin 0 */
#define IOC_PORT_RFC_GPI1         0x00000034  /* RC Core Data In Pin 1 */
#define IOC_PORT_RFC_SMI_DL_OUT   0x00000035  /* RF Core SMI Data Link Out */
#define IOC_PORT_RFC_SMI_DL_IN    0x00000036  /* RF Core SMI Data Link in */
#define IOC_PORT_RFC_SMI_CL_OUT   0x00000037  /* RF Core SMI Command Link Out */
#define IOC_PORT_RFC_SMI_CL_IN    0x00000038  /* RF Core SMI Command Link In */

/* Edge Detection */
#define IOC_NO_EDGE      0x00000000 /* No edge detection */
#define IOC_FALLING_EDGE 0x00010000 /* Edge detection on falling edge */
#define IOC_RISING_EDGE  0x00020000 /* Edge detection on rising edge */
#define IOC_BOTH_EDGES   0x00030000 /* Edge detection on both edges */

#endif  /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC13XX_CC26XX_PINCTRL_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2015 - 2017, Texas Instruments Incorporated。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

改编自 `hal/ti/simplelink/source/ti/devices/cc13x2_cc26x2/driverlib/ioc.h`。

### 注释 3：原第 12 行

输入输出控制器（IOC）外设端口映射（Peripheral Port Mapping）。

### 注释 4：原第 13 行

默认通用输入输出（General-purpose I/O）用途。

### 注释 5：原第 14 行

常开域（AON）外部 32 kHz 时钟。

### 注释 6：原第 15 行

辅助（AUX）输入输出引脚。

### 注释 7：原第 16 行

微控制器（MCU）的 SSI0 接收引脚（Receive Pin）。

### 注释 8：原第 17 行

微控制器（MCU）的 SSI0 发送引脚（Transmit Pin）。

### 注释 9：原第 18 行

微控制器（MCU）的 SSI0 帧选择引脚（FSS Pin）。

### 注释 10：原第 19 行

微控制器（MCU）的 SSI0 时钟引脚（Clock Pin）。

### 注释 11：原第 20 行

微控制器（MCU）的 I2C 数据引脚（Data Pin）。

### 注释 12：原第 21 行

微控制器（MCU）的 I2C 时钟引脚（Clock Pin）。

### 注释 13：原第 22 行

微控制器（MCU）的 UART0 接收引脚（Receive Pin）。

### 注释 14：原第 23 行

微控制器（MCU）的 UART0 发送引脚（Transmit Pin）。

### 注释 15：原第 24 行

微控制器（MCU）的 UART0 允许发送引脚（Clear To Send Pin）。

### 注释 16：原第 25 行

微控制器（MCU）的 UART0 请求发送引脚（Request To Send Pin）。

### 注释 17：原第 26 行

微控制器（MCU）的 UART1 接收引脚（Receive Pin）。

### 注释 18：原第 27 行

微控制器（MCU）的 UART1 发送引脚（Transmit Pin）。

### 注释 19：原第 28 行

微控制器（MCU）的 UART1 允许发送引脚（Clear To Send Pin）。

### 注释 20：原第 29 行

微控制器（MCU）的 UART1 请求发送引脚（Request To Send Pin）。

### 注释 21：原第 30 行

微控制器（MCU）端口事件（Port Event）0。

### 注释 22：原第 31 行

微控制器（MCU）端口事件（Port Event）1。

### 注释 23：原第 32 行

微控制器（MCU）端口事件（Port Event）2。

### 注释 24：原第 33 行

微控制器（MCU）端口事件（Port Event）3。

### 注释 25：原第 34 行

微控制器（MCU）端口事件（Port Event）4。

### 注释 26：原第 35 行

微控制器（MCU）端口事件（Port Event）5。

### 注释 27：原第 36 行

微控制器（MCU）端口事件（Port Event）6。

### 注释 28：原第 37 行

微控制器（MCU）端口事件（Port Event）7。

### 注释 29：原第 38 行

串行线观察器（Serial Wire Viewer）。

### 注释 30：原第 39 行

微控制器（MCU）的 SSI1 接收引脚（Receive Pin）。

### 注释 31：原第 40 行

微控制器（MCU）的 SSI1 发送引脚（Transmit Pin）。

### 注释 32：原第 41 行

微控制器（MCU）的 SSI1 帧选择引脚（FSS Pin）。

### 注释 33：原第 42 行

微控制器（MCU）的 SSI1 时钟引脚（Clock Pin）。

### 注释 34：原第 43 行

微控制器（MCU）的 I2S 数据引脚（Data Pin） 0。

### 注释 35：原第 44 行

微控制器（MCU）的 I2S 数据引脚（Data Pin） 1。

### 注释 36：原第 45 行

微控制器（MCU）的 I2S 帧／字时钟（Frame/Word Clock）。

### 注释 37：原第 46 行

微控制器（MCU）的 I2S 位时钟（Bit Clock）。

### 注释 38：原第 47 行

微控制器（MCU）的 I2S 主时钟 2（Master Clock 2）。

### 注释 39：原第 48 行

射频内核跟踪器（RF Core Tracer）。

### 注释 40：原第 49 行

RC 内核数据输出引脚 0（RC Core Data Out Pin 0）。

### 注释 41：原第 50 行

RC 内核数据输出引脚 1（RC Core Data Out Pin 1）。

### 注释 42：原第 51 行

RC 内核数据输出引脚 2（RC Core Data Out Pin 2）。

### 注释 43：原第 52 行

RC 内核数据输出引脚 3（RC Core Data Out Pin 3）。

### 注释 44：原第 53 行

RC 内核数据输入引脚 0（RC Core Data In Pin 0）。

### 注释 45：原第 54 行

RC 内核数据输入引脚 1（RC Core Data In Pin 1）。

### 注释 46：原第 55 行

射频内核 SMI 数据链路输出（RF Core SMI Data Link Out）。

### 注释 47：原第 56 行

射频内核 SMI 数据链路输入（RF Core SMI Data Link In）。

### 注释 48：原第 57 行

射频内核 SMI 命令链路输出（RF Core SMI Command Link Out）。

### 注释 49：原第 58 行

射频内核 SMI 命令链路输入（RF Core SMI Command Link In）。

### 注释 50：原第 60 行

边沿检测（Edge Detection）。

### 注释 51：原第 61 行

不检测边沿（No Edge Detection）。

### 注释 52：原第 62 行

检测下降沿（Falling Edge）。

### 注释 53：原第 63 行

检测上升沿（Rising Edge）。

### 注释 54：原第 64 行

检测双边沿（Both Edges）。

### 注释 55：原第 66 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CC13XX_CC26XX_PINCTRL_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P031_zephyr__dt-bindings__pinctrl__cc13xx_cc26xx-pinctrl.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_esp32s3-xtensa-intmux.h_源码浏览.md)
