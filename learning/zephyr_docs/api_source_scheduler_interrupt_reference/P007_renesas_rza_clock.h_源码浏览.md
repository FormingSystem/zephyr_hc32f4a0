---
id: learning.zephyr-docs.api-source-scheduler-interrupt-reference.page-7
title: renesas_rza_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_renesas\_rza\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md)。

## 7.1\_原始可见代码（Source Code）

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
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
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

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA_CLOCK_H_

/* RZ/A clock configuration values */
#define RZ_IP_MASK         0xFF000000UL
#define RZ_IP_SHIFT        24UL
#define RZ_IP_CH_MASK      0xFF0000UL
#define RZ_IP_CH_SHIFT     16UL
#define RZ_CLOCK_MASK      0xFF00UL
#define RZ_CLOCK_SHIFT     8UL
#define RZ_CLOCK_DIV_MASK  0xFFUL
#define RZ_CLOCK_DIV_SHIFT 0UL

#define RZ_IP_GTM   0UL /* General Timer */
#define RZ_IP_SCI   1UL /* Serial Communications Interface */
#define RZ_IP_SCIF  2UL /* Serial Communications Interface with FIFO */
#define RZ_IP_RIIC  3UL /* I2C Bus Interface */
#define RZ_IP_RSPI  4UL /* Renesas Serial Peripheral Interface */
#define RZ_IP_DMAC  5UL /* Direct Memory Access Controller */
#define RZ_IP_CANFD 6UL /* CANFD Interface (RS-CANFD) */
#define RZ_IP_ADC   7UL /* A/D Converter */
#define RZ_IP_WDT   8UL /* Watchdog Timer */

#define RZ_CLOCK_ICLK    0UL  /* Cortex-A55 Clock */
#define RZ_CLOCK_I2CLK   1UL  /* Cortex-M33 Clock */
#define RZ_CLOCK_S0CLK   2UL  /* DDR-PHY Clock */
#define RZ_CLOCK_SPI0CLK 3UL  /* SPI0 Clock */
#define RZ_CLOCK_SPI1CLK 4UL  /* SPI1 Clock */
#define RZ_CLOCK_OC0CLK  5UL  /* Octa0 Clock */
#define RZ_CLOCK_OC1CLK  6UL  /* Octa1 Clock */
#define RZ_CLOCK_SD0CLK  7UL  /* SDH0 Clock */
#define RZ_CLOCK_SD1CLK  8UL  /* SDH1 Clock */
#define RZ_CLOCK_M0CLK   9UL  /* VCP, LCDC Clock */
#define RZ_CLOCK_M2CLK   10UL /* CRU, MIPI-DSI Clock */
#define RZ_CLOCK_M3CLK   11UL /* MIPI-DSI, LCDC Clock */
#define RZ_CLOCK_HPCLK   12UL /* Ethernet Clock */
#define RZ_CLOCK_TSUCLK  13UL /* TSU Clock */
#define RZ_CLOCK_ZTCLK   14UL /* JAUTH Clock */
#define RZ_CLOCK_P0CLK   15UL /* APB-BUS Clock */
#define RZ_CLOCK_P1CLK   16UL /* AXI-BUS Clock */
#define RZ_CLOCK_P2CLK   17UL /* P2CLK */
#define RZ_CLOCK_ATCLK   18UL /* ATCLK */
#define RZ_CLOCK_OSCCLK  19UL /* OSC Clock */

#define RZ_CLOCK(IP, ch, clk, div)                                                                 \
        ((RZ_IP_##IP << RZ_IP_SHIFT) | ((ch) << RZ_IP_CH_SHIFT) | ((clk) << RZ_CLOCK_SHIFT) |      \
         ((div) << RZ_CLOCK_DIV_SHIFT))


/* GTM */
#define RZ_CLOCK_GTM(ch) RZ_CLOCK(GTM, ch, RZ_CLOCK_P0CLK, 1)

/* SCI */
#define RZ_CLOCK_SCI(ch) RZ_CLOCK(SCI, ch, RZ_CLOCK_P0CLK, 1)

/* SCIF */
#define RZ_CLOCK_SCIF(ch) RZ_CLOCK(SCIF, ch, RZ_CLOCK_P0CLK, 1)

/* RIIC */
#define RZ_CLOCK_RIIC(ch) RZ_CLOCK(RIIC, ch, RZ_CLOCK_P0CLK, 1)

/* RSPI */
#define RZ_CLOCK_RSPI(ch) RZ_CLOCK(RSPI, ch, RZ_CLOCK_P0CLK, 1)

/* DMAC */
#define RZ_CLOCK_DMAC_NS(ch) RZ_CLOCK(DMAC, ch, RZ_CLOCK_P1CLK, 1)

/* CAN */
#define RZ_CLOCK_CANFD(ch) RZ_CLOCK(CANFD, ch, RZ_CLOCK_P0CLK, 1)

/* ADC */
#define RZ_CLOCK_ADC(ch) RZ_CLOCK(ADC, ch, RZ_CLOCK_P0CLK, 1)

/* WDT */
#define RZ_CLOCK_WDT(ch) RZ_CLOCK(WDT, ch, RZ_CLOCK_P0CLK, 1)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA_CLOCK_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

RZ/A 时钟配置值（Clock Configuration Values）。

### 注释 3：原第 20 行

通用定时器（General Timer）。

### 注释 4：原第 21 行

串行通信接口（Serial Communications Interface）。

### 注释 5：原第 22 行

带先进先出缓冲区（FIFO）的串行通信接口（Serial Communications Interface）。

### 注释 6：原第 23 行

I2C 总线接口（I2C Bus Interface）。

### 注释 7：原第 24 行

瑞萨串行外设接口（Renesas Serial Peripheral Interface）。

### 注释 8：原第 25 行

直接内存访问控制器（Direct Memory Access Controller）。

### 注释 9：原第 26 行

灵活数据速率 CAN 接口（CAN FD Interface），即 RS-CANFD。

### 注释 10：原第 27 行

模数转换器（A/D Converter）。

### 注释 11：原第 28 行

看门狗定时器（Watchdog Timer）。

### 注释 12：原第 30 行

Cortex-A55 时钟（Clock）。

### 注释 13：原第 31 行

Cortex-M33 时钟（Clock）。

### 注释 14：原第 32 行

DDR-PHY 时钟（Clock）。

### 注释 15：原第 33 行

SPI0 时钟（Clock）。

### 注释 16：原第 34 行

SPI1 时钟（Clock）。

### 注释 17：原第 35 行

Octa0 时钟（Clock）。

### 注释 18：原第 36 行

Octa1 时钟（Clock）。

### 注释 19：原第 37 行

SDH0 时钟（Clock）。

### 注释 20：原第 38 行

SDH1 时钟（Clock）。

### 注释 21：原第 39 行

VCP, LCDC 时钟（Clock）。

### 注释 22：原第 40 行

CRU, MIPI-DSI 时钟（Clock）。

### 注释 23：原第 41 行

MIPI-DSI, LCDC 时钟（Clock）。

### 注释 24：原第 42 行

Ethernet 时钟（Clock）。

### 注释 25：原第 43 行

TSU 时钟（Clock）。

### 注释 26：原第 44 行

JAUTH 时钟（Clock）。

### 注释 27：原第 45 行

APB-BUS 时钟（Clock）。

### 注释 28：原第 46 行

AXI-BUS 时钟（Clock）。

### 注释 29：原第 47 行

时钟标识（Clock Identifier）：`P2CLK`。

### 注释 30：原第 48 行

时钟标识（Clock Identifier）：`ATCLK`。

### 注释 31：原第 49 行

OSC 时钟（Clock）。

### 注释 32：原第 62 行

通用定时器模块（GTM）。

### 注释 33：原第 65 行

串行通信接口（SCI）。

### 注释 34：原第 68 行

带 FIFO 的串行通信接口（SCIF）。

### 注释 35：原第 71 行

瑞萨 I2C 接口（RIIC）。

### 注释 36：原第 74 行

瑞萨串行外设接口（RSPI）。

### 注释 37：原第 77 行

直接内存访问控制器（DMAC）。

### 注释 38：原第 80 行

控制器局域网（CAN）

### 注释 39：原第 83 行

模数转换器（ADC）

### 注释 40：原第 86 行

看门狗定时器（WDT）。

### 注释 41：原第 89 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_RENESAS_RZA_CLOCK_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P063_zephyr__dt-bindings__clock__renesas_rza_clock.h_文件参考.md)

---

[上一章](P006_pinctrl-r8a78000.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_renesas_rzg_clock.h_源码浏览.md)
