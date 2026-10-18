---
id: learning.zephyr-docs.api-source-system-reference.page-8
title: digilent-pmod.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_digilent-pmod.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h.html)。

## 8.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>

```c
/*
 * Copyright (c) 2023 Elektronikutvecklingsbyrån EUB AB
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_DIGILENT_PMOD_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_DIGILENT_PMOD_H_


/* GPIO */

#define PMOD_IO(n) ((n) - 1)

/* SPI */

#define PMOD_SPI_CS     PMOD_IO(1)

#define PMOD_SPI_MOSI   PMOD_IO(2)

#define PMOD_SPI_MISO   PMOD_IO(3)

#define PMOD_SPI_SCK    PMOD_IO(4)

/* Expanded SPI */

#define PMOD_EXP_SPI_CS         PMOD_IO(1)

#define PMOD_EXP_SPI_MOSI       PMOD_IO(2)

#define PMOD_EXP_SPI_MISO       PMOD_IO(3)

#define PMOD_EXP_SPI_SCK        PMOD_IO(4)

#define PMOD_EXP_SPI_INT        PMOD_IO(5)

#define PMOD_EXP_SPI_RESET      PMOD_IO(6)

#define PMOD_EXP_SPI_CS2        PMOD_IO(7)

#define PMOD_EXP_SPI_CS3        PMOD_IO(8)

/* Expanded UART */

#define PMOD_EXP_UART_INT       PMOD_IO(5)

#define PMOD_EXP_UART_RESET     PMOD_IO(6)

/* H-bridge */

#define PMOD_HBRIDGE_DIR        PMOD_IO(1)

#define PMOD_HBRIDGE_EN         PMOD_IO(2)

/* Dual H-bridge */

#define PMOD_DUAL_HBRIDGE_DIR1  PMOD_IO(1)

#define PMOD_DUAL_HBRIDGE_EN1   PMOD_IO(2)

#define PMOD_DUAL_HBRIDGE_DIR2  PMOD_IO(3)

#define PMOD_DUAL_HBRIDGE_EN2   PMOD_IO(4)

/* Expanded dual H-bridge */

#define PMOD_EXP_DUAL_HBRIDGE_DIR1      PMOD_IO(1)

#define PMOD_EXP_DUAL_HBRIDGE_EN1       PMOD_IO(2)

#define PMOD_EXP_DUAL_HBRIDGE_DIR2      PMOD_IO(5)

#define PMOD_EXP_DUAL_HBRIDGE_EN2       PMOD_IO(6)

/* I2C */

#define PMOD_I2C_INT    PMOD_IO(1)

#define PMOD_I2C_RESET  PMOD_IO(2)

#define PMOD_I2C_SCL    PMOD_IO(3)

#define PMOD_I2C_SDA    PMOD_IO(4)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_DIGILENT_PMOD_H_ */
```

## 8.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Elektronikutvecklingsbyrån EUB AB。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 35 行

通用输入输出（GPIO）

### 注释 3：原第 45 行

串行外设接口（SPI）

### 注释 4：原第 71 行

扩展 SPI（Expanded SPI）。

### 注释 5：原第 121 行

扩展 UART（Expanded UART）。

### 注释 6：原第 135 行

H 桥（H-Bridge）。

### 注释 7：原第 149 行

双 H 桥（Dual H-Bridge）。

### 注释 8：原第 175 行

扩展双 H 桥（Expanded Dual H-Bridge）。

### 注释 9：原第 201 行

集成电路间总线（I2C）

### 注释 10：原第 227 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_GPIO_DIGILENT_PMOD_H_`。

## 8.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/digilent-pmod_8h.html)

---

[上一章](P007_cts.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P009_util.h_源码浏览.md)
