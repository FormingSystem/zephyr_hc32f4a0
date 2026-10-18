---
id: learning.zephyr-docs.api-source-interrupt-modem-reference.page-10
title: renesas_rztn_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rztn__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_renesas\_rztn\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rztn__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P353_zephyr__dt-bindings__clock__renesas_rztn_clock.h_文件参考.md)。

## 10.1\_原始可见代码（Source Code）

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
<a id="foldopen00074"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZTN_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZTN_CLOCK_H_

/* RZ clock configuration values */
#define RZ_IP_MASK     0xFF0000UL
#define RZ_IP_SHIFT    16UL
#define RZ_IP_CH_MASK  0xFF00UL
#define RZ_IP_CH_SHIFT 8UL
#define RZ_CLOCK_MASK  0xFFUL
#define RZ_CLOCK_SHIFT 0UL

#define RZ_IP_BSC   0UL  /* Bus State Controller */
#define RZ_IP_XSPI  1UL  /* Expanded Serial Peripheral Interface */
#define RZ_IP_SCI   2UL  /* Serial Communications Interface */
#define RZ_IP_IIC   3UL  /* I2C Bus Interface */
#define RZ_IP_SPI   4UL  /* Serial Peripheral Interface */
#define RZ_IP_GPT   5UL  /* General PWM Timer */
#define RZ_IP_ADC12 6UL  /* 12-Bit A/D Converter */
#define RZ_IP_CMT   7UL  /* Compare Match Timer */
#define RZ_IP_CMTW  8UL  /* Compare Match Timer W */
#define RZ_IP_CANFD 9UL  /* Controller Area Network with Flexible Data Rate */
#define RZ_IP_GMAC  10UL /* Ethernet MAC */
#define RZ_IP_ETHSW 11UL /* Ethernet Switch */
#define RZ_IP_USBHS 12UL /* USB High Speed */
#define RZ_IP_RTC   13UL /* Real Time Clock */

#define RZ_CLOCK_CPU0       0UL
#define RZ_CLOCK_CPU1       1UL
#define RZ_CLOCK_CA55C0     2UL
#define RZ_CLOCK_CA55C1     3UL
#define RZ_CLOCK_CA55C2     4UL
#define RZ_CLOCK_CA55C3     5UL
#define RZ_CLOCK_CA55SCLK   6UL
#define RZ_CLOCK_ICLK       7UL
#define RZ_CLOCK_PCLKH      8UL
#define RZ_CLOCK_PCLKM      9UL
#define RZ_CLOCK_PCLKL      10UL
#define RZ_CLOCK_PCLKADC    11UL
#define RZ_CLOCK_PCLKGPTL   12UL
#define RZ_CLOCK_PCLKENCO   13UL
#define RZ_CLOCK_PCLKSPI0   14UL
#define RZ_CLOCK_PCLKSPI1   15UL
#define RZ_CLOCK_PCLKSPI2   16UL
#define RZ_CLOCK_PCLKSPI3   17UL
#define RZ_CLOCK_PCLKSCI0   18UL
#define RZ_CLOCK_PCLKSCI1   19UL
#define RZ_CLOCK_PCLKSCI2   20UL
#define RZ_CLOCK_PCLKSCI3   21UL
#define RZ_CLOCK_PCLKSCI4   22UL
#define RZ_CLOCK_PCLKSCI5   23UL
#define RZ_CLOCK_PCLKSCIE0  24UL
#define RZ_CLOCK_PCLKSCIE1  25UL
#define RZ_CLOCK_PCLKSCIE2  26UL
#define RZ_CLOCK_PCLKSCIE3  27UL
#define RZ_CLOCK_PCLKSCIE4  28UL
#define RZ_CLOCK_PCLKSCIE5  29UL
#define RZ_CLOCK_PCLKSCIE6  30UL
#define RZ_CLOCK_PCLKSCIE7  31UL
#define RZ_CLOCK_PCLKSCIE8  32UL
#define RZ_CLOCK_PCLKSCIE9  33UL
#define RZ_CLOCK_PCLKSCIE10 34UL
#define RZ_CLOCK_PCLKSCIE11 35UL
#define RZ_CLOCK_PCLKCAN    36UL
#define RZ_CLOCK_CKIO       37UL
#define RZ_CLOCK_XSPI0_CLK  38UL
#define RZ_CLOCK_XSPI1_CLK  39UL

#define RZ_CLOCK(IP, ch, clk)                                                                      \
        ((IP << RZ_IP_SHIFT) | ((ch) << RZ_IP_CH_SHIFT) | ((clk) << RZ_CLOCK_SHIFT))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZTN_CLOCK_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

RZ 时钟配置值（Clock Configuration Values）。

### 注释 3：原第 18 行

总线状态控制器（Bus State Controller）。

### 注释 4：原第 19 行

扩展串行外设接口（Expanded Serial Peripheral Interface）。

### 注释 5：原第 20 行

串行通信接口（Serial Communications Interface）。

### 注释 6：原第 21 行

I2C 总线接口（I2C Bus Interface）。

### 注释 7：原第 22 行

串行外设接口（Serial Peripheral Interface）。

### 注释 8：原第 23 行

通用脉宽调制定时器（General PWM Timer）。

### 注释 9：原第 24 行

12 位模数转换器（12-Bit A/D Converter）。

### 注释 10：原第 25 行

比较匹配定时器（Compare Match Timer）。

### 注释 11：原第 26 行

比较匹配定时器 W（Compare Match Timer W）。

### 注释 12：原第 27 行

支持灵活数据速率的控制器局域网（Controller Area Network with Flexible Data Rate，CAN FD）。

### 注释 13：原第 28 行

以太网媒体访问控制器（Ethernet MAC）。

### 注释 14：原第 29 行

以太网交换机（Ethernet Switch）。

### 注释 15：原第 30 行

高速 USB（USB High Speed）。

### 注释 16：原第 31 行

实时时钟（Real Time Clock）。

### 注释 17：原第 77 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZTN_CLOCK_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P353_zephyr__dt-bindings__clock__renesas_rztn_clock.h_文件参考.md)

---

[上一章](P009_pthread.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_sw_isr_table.h_源码浏览.md)
