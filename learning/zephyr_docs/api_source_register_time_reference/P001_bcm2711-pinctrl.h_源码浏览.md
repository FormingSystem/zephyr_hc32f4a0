---
id: learning.zephyr-docs.api-source-register-time-reference.page-1
title: bcm2711-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bcm2711-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_bcm2711-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/bcm2711-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P025_zephyr__dt-bindings__pinctrl__bcm2711-pinctrl.h_文件参考.md)。

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
<a id="foldopen00026"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00030"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00034"></a>
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

```c
/*
 * Copyright (c) 2025 Muhammad Waleed Badar
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_BCM2711_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_BCM2711_PINCTRL_H_

/* BCM2711 Pin Functions */
#define BCM2711_FSEL_GPIO_IN  0
#define BCM2711_FSEL_GPIO_OUT 1
#define BCM2711_FSEL_ALT0     4
#define BCM2711_FSEL_ALT1     5
#define BCM2711_FSEL_ALT2     6
#define BCM2711_FSEL_ALT3     7
#define BCM2711_FSEL_ALT4     3
#define BCM2711_FSEL_ALT5     2

/* BCM2711 Pull Configuration */
#define BCM2711_PULL_NONE       0
#define BCM2711_PULL_UP         1
#define BCM2711_PULL_DOWN       2

/* BCM2711 pinmux configuration macro */
#define BCM2711_PINMUX(pin, func) \
        (((pin) & 0xFF) | (((func) & 0x7) << 8))

/* Extract pin number from BCM2711 pinmux value */
#define BCM2711_GET_PIN(pinmux) \
        ((pinmux) & 0xFF)

/* Extract function from BCM2711 pinmux value */
#define BCM2711_GET_FUNC(pinmux) \
        (((pinmux) >> 8) & 0x7)

/* UART0 pinmux definitions */
#define UART0_TX_GPIO14 BCM2711_PINMUX(14, BCM2711_FSEL_ALT0)
#define UART0_RX_GPIO15 BCM2711_PINMUX(15, BCM2711_FSEL_ALT0)

#define UART0_TX_GPIO32 BCM2711_PINMUX(32, BCM2711_FSEL_ALT3)
#define UART0_RX_GPIO33 BCM2711_PINMUX(33, BCM2711_FSEL_ALT3)

#define UART0_TX_GPIO36 BCM2711_PINMUX(36, BCM2711_FSEL_ALT2)
#define UART0_RX_GPIO37 BCM2711_PINMUX(37, BCM2711_FSEL_ALT2)

#define UART0_CTS_GPIO16 BCM2711_PINMUX(16, BCM2711_FSEL_ALT3)
#define UART0_RTS_GPIO17 BCM2711_PINMUX(17, BCM2711_FSEL_ALT3)

#define UART0_CTS_GPIO30 BCM2711_PINMUX(30, BCM2711_FSEL_ALT3)
#define UART0_RTS_GPIO31 BCM2711_PINMUX(31, BCM2711_FSEL_ALT3)

#define UART0_CTS_GPIO38 BCM2711_PINMUX(38, BCM2711_FSEL_ALT2)
#define UART0_RTS_GPIO39 BCM2711_PINMUX(39, BCM2711_FSEL_ALT2)

/* UART1 pinmux definitions */
#define UART1_TX_GPIO14 BCM2711_PINMUX(14, BCM2711_FSEL_ALT5)
#define UART1_RX_GPIO15 BCM2711_PINMUX(15, BCM2711_FSEL_ALT5)

#define UART1_TX_GPIO32 BCM2711_PINMUX(32, BCM2711_FSEL_ALT5)
#define UART1_RX_GPIO33 BCM2711_PINMUX(33, BCM2711_FSEL_ALT5)

#define UART1_TX_GPIO40 BCM2711_PINMUX(40, BCM2711_FSEL_ALT5)
#define UART1_RX_GPIO41 BCM2711_PINMUX(41, BCM2711_FSEL_ALT5)

#define UART1_CTS_GPIO16 BCM2711_PINMUX(16, BCM2711_FSEL_ALT5)
#define UART1_RTS_GPIO17 BCM2711_PINMUX(17, BCM2711_FSEL_ALT5)

#define UART1_CTS_GPIO30 BCM2711_PINMUX(30, BCM2711_FSEL_ALT5)
#define UART1_RTS_GPIO31 BCM2711_PINMUX(31, BCM2711_FSEL_ALT5)

#define UART1_CTS_GPIO42 BCM2711_PINMUX(42, BCM2711_FSEL_ALT5)
#define UART1_RTS_GPIO43 BCM2711_PINMUX(43, BCM2711_FSEL_ALT5)

/* UART2 pinmux definitions */
#define UART2_TX_GPIO0 BCM2711_PINMUX(0, BCM2711_FSEL_ALT4)
#define UART2_RX_GPIO1 BCM2711_PINMUX(1, BCM2711_FSEL_ALT4)

#define UART2_CTS_GPIO2 BCM2711_PINMUX(2, BCM2711_FSEL_ALT4)
#define UART2_RTS_GPIO3 BCM2711_PINMUX(3, BCM2711_FSEL_ALT4)

/* UART3 pinmux definitions */
#define UART3_TX_GPIO4 BCM2711_PINMUX(4, BCM2711_FSEL_ALT4)
#define UART3_RX_GPIO5 BCM2711_PINMUX(5, BCM2711_FSEL_ALT4)

#define UART3_CTS_GPIO6 BCM2711_PINMUX(6, BCM2711_FSEL_ALT4)
#define UART3_RTS_GPIO7 BCM2711_PINMUX(7, BCM2711_FSEL_ALT4)

/* UART4 pinmux definitions */
#define UART4_TX_GPIO8 BCM2711_PINMUX(8, BCM2711_FSEL_ALT4)
#define UART4_RX_GPIO9 BCM2711_PINMUX(9, BCM2711_FSEL_ALT4)

#define UART4_CTS_GPIO10 BCM2711_PINMUX(10, BCM2711_FSEL_ALT4)
#define UART4_RTS_GPIO11 BCM2711_PINMUX(11, BCM2711_FSEL_ALT4)

/* UART5 pinmux definitions */
#define UART5_TX_GPIO12 BCM2711_PINMUX(12, BCM2711_FSEL_ALT4)
#define UART5_RX_GPIO13 BCM2711_PINMUX(13, BCM2711_FSEL_ALT4)

#define UART5_CTS_GPIO14 BCM2711_PINMUX(14, BCM2711_FSEL_ALT4)
#define UART5_RTS_GPIO15 BCM2711_PINMUX(15, BCM2711_FSEL_ALT4)

/* I2C0 pinmux definitions */
#define I2C0_SDA_GPIO0    BCM2711_PINMUX(0,  BCM2711_FSEL_ALT0)
#define I2C0_SCL_GPIO1    BCM2711_PINMUX(1,  BCM2711_FSEL_ALT0)

#define I2C0_SDA_GPIO28   BCM2711_PINMUX(28, BCM2711_FSEL_ALT0)
#define I2C0_SCL_GPIO29   BCM2711_PINMUX(29, BCM2711_FSEL_ALT0)

#define I2C0_SDA_GPIO44   BCM2711_PINMUX(44, BCM2711_FSEL_ALT1)
#define I2C0_SCL_GPIO45   BCM2711_PINMUX(45, BCM2711_FSEL_ALT1)

/* I2C1 pinmux definitions */
#define I2C1_SDA_GPIO2    BCM2711_PINMUX(2,  BCM2711_FSEL_ALT0)
#define I2C1_SCL_GPIO3    BCM2711_PINMUX(3,  BCM2711_FSEL_ALT0)

#define I2C1_SDA_GPIO44   BCM2711_PINMUX(44, BCM2711_FSEL_ALT2)
#define I2C1_SCL_GPIO45   BCM2711_PINMUX(45, BCM2711_FSEL_ALT2)

/* I2C3 pinmux definitions */
#define I2C3_SDA_GPIO2    BCM2711_PINMUX(2,  BCM2711_FSEL_ALT5)
#define I2C3_SCL_GPIO3    BCM2711_PINMUX(3,  BCM2711_FSEL_ALT5)

#define I2C3_SDA_GPIO4    BCM2711_PINMUX(4,  BCM2711_FSEL_ALT5)
#define I2C3_SCL_GPIO5    BCM2711_PINMUX(5,  BCM2711_FSEL_ALT5)

/* I2C4 pinmux definitions */
#define I2C4_SDA_GPIO6    BCM2711_PINMUX(6,  BCM2711_FSEL_ALT5)
#define I2C4_SCL_GPIO7    BCM2711_PINMUX(7,  BCM2711_FSEL_ALT5)

#define I2C4_SDA_GPIO8    BCM2711_PINMUX(8,  BCM2711_FSEL_ALT5)
#define I2C4_SCL_GPIO9    BCM2711_PINMUX(9,  BCM2711_FSEL_ALT5)

/* I2C5 pinmux definitions */
#define I2C5_SDA_GPIO10   BCM2711_PINMUX(10, BCM2711_FSEL_ALT5)
#define I2C5_SCL_GPIO11   BCM2711_PINMUX(11, BCM2711_FSEL_ALT5)

#define I2C5_SDA_GPIO12   BCM2711_PINMUX(12, BCM2711_FSEL_ALT5)
#define I2C5_SCL_GPIO13   BCM2711_PINMUX(13, BCM2711_FSEL_ALT5)

/* I2C6 pinmux definitions */
#define I2C6_SDA_GPIO0    BCM2711_PINMUX(0,  BCM2711_FSEL_ALT5)
#define I2C6_SCL_GPIO1    BCM2711_PINMUX(1,  BCM2711_FSEL_ALT5)

#define I2C6_SDA_GPIO22   BCM2711_PINMUX(22, BCM2711_FSEL_ALT5)
#define I2C6_SCL_GPIO23   BCM2711_PINMUX(23, BCM2711_FSEL_ALT5)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_BCM2711_PINCTRL_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Muhammad Waleed Badar。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

BCM2711 引脚功能（Pin Functions）。

### 注释 3：原第 20 行

BCM2711 上下拉配置（Pull Configuration）。

### 注释 4：原第 25 行

BCM2711 引脚复用（pinmux）配置宏。

### 注释 5：原第 29 行

从 BCM2711 引脚复用值中提取引脚编号。

### 注释 6：原第 33 行

从 BCM2711 引脚复用值中提取功能。

### 注释 7：原第 37 行

UART0 引脚复用（pinmux）定义。

### 注释 8：原第 56 行

UART1 引脚复用（pinmux）定义。

### 注释 9：原第 75 行

UART2 引脚复用（pinmux）定义。

### 注释 10：原第 82 行

UART3 引脚复用（pinmux）定义。

### 注释 11：原第 89 行

UART4 引脚复用（pinmux）定义。

### 注释 12：原第 96 行

UART5 引脚复用（pinmux）定义。

### 注释 13：原第 103 行

I2C0 引脚复用（pinmux）定义。

### 注释 14：原第 113 行

I2C1 引脚复用（pinmux）定义。

### 注释 15：原第 120 行

I2C3 引脚复用（pinmux）定义。

### 注释 16：原第 127 行

I2C4 引脚复用（pinmux）定义。

### 注释 17：原第 134 行

I2C5 引脚复用（pinmux）定义。

### 注释 18：原第 141 行

I2C6 引脚复用（pinmux）定义。

### 注释 19：原第 148 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_BCM2711_PINCTRL_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P025_zephyr__dt-bindings__pinctrl__bcm2711-pinctrl.h_文件参考.md)

---

[返回大纲](大纲.md) · [下一章](P002_conn.h_源码浏览.md)
