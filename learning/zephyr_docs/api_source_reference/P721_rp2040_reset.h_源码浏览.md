---
id: learning.zephyr-docs.api-source-reference.page-721
title: rp2040_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rp2040__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第721章\_rp2040\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rp2040__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rp2040__reset_8h.html)。

## 721.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00040"></a>
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
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>

```c
/*
 * Copyright (c) 2021 Yonatan Schachter
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RP2040_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RP2040_RESET_H_



#define RPI_PICO_RESETS_RESET_ADC        0
#define RPI_PICO_RESETS_RESET_BUSCTRL    1
#define RPI_PICO_RESETS_RESET_DMA        2
#define RPI_PICO_RESETS_RESET_I2C0       3
#define RPI_PICO_RESETS_RESET_I2C1       4
#define RPI_PICO_RESETS_RESET_IO_BANK0   5
#define RPI_PICO_RESETS_RESET_IO_QSPI    6
#define RPI_PICO_RESETS_RESET_JTAG       7
#define RPI_PICO_RESETS_RESET_PADS_BANK0 8
#define RPI_PICO_RESETS_RESET_PADS_QSPI  9
#define RPI_PICO_RESETS_RESET_PIO0       10
#define RPI_PICO_RESETS_RESET_PIO1       11
#define RPI_PICO_RESETS_RESET_PLL_SYS    12
#define RPI_PICO_RESETS_RESET_PLL_USB    13
#define RPI_PICO_RESETS_RESET_PWM        14
#define RPI_PICO_RESETS_RESET_RTC        15
#define RPI_PICO_RESETS_RESET_SPI0       16
#define RPI_PICO_RESETS_RESET_SPI1       17
#define RPI_PICO_RESETS_RESET_SYSCFG     18
#define RPI_PICO_RESETS_RESET_SYSINFO    19
#define RPI_PICO_RESETS_RESET_TBMAN      20
#define RPI_PICO_RESETS_RESET_TIMER      21
#define RPI_PICO_RESETS_RESET_UART0      22
#define RPI_PICO_RESETS_RESET_UART1      23
#define RPI_PICO_RESETS_RESET_USBCTRL    24



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RP2040_RESET_H_ */
```

## 721.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021 Yonatan Schachter。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 73 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_RP2040_RESET_H_`。

## 721.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rp2040__reset_8h.html)

---

[上一章](P720_rm3100.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P722_rp2350_reset.h_源码浏览.md)
