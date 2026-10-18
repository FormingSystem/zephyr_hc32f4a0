---
id: learning.zephyr-docs.api-source-network-reference.page-16
title: pinctrl-rza2m.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza2m_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_pinctrl-rza2m.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rza2m_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_configuration_reference/P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md)。

## 16.1\_原始可见代码（Source Code）

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
<a id="l00020"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00053"></a>
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
<a id="l00089"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>

```c
/*
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA2M_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA2M_H_



#define RZA2M_PIN_NUM_IN_PORT 8


/* Port names as labeled in the Hardware Manual */
#define PORT_00 0
#define PORT_01 1
#define PORT_02 2
#define PORT_03 3
#define PORT_04 4
#define PORT_05 5
#define PORT_06 6
#define PORT_07 7
#define PORT_08 8
#define PORT_09 9
#define PORT_A  10
#define PORT_B  11
#define PORT_C  12
#define PORT_D  13
#define PORT_E  14
#define PORT_F  15
#define PORT_G  16
#define PORT_H  17
/* No I */
#define PORT_J  18
#define PORT_K  19
#define PORT_L  20
#define PORT_M  21 /* Pins PM_0/1 are labeled JP_0/1 in HW manual */

#define PORT_CKIO 22
#define PORT_PPOC 23 /* Select between 1.8V and 3.3V for SPI and SD/MMC */

#define PIN_POSEL 0 /* Sets function for POSEL0 bits. 00, 01, 10 - 1.8v, 11 - 3.3v */
#define PIN_POC2  1 /* Sets function for SSD host 0, 0 - 1.8v 1 - 3.3v */
#define PIN_POC3  2 /* Sets function for SSD host 1, 0 - 1.8v 1 - 3.3v */


#define RZA2M_PINMUX(b, p, f) ((b) * RZA2M_PIN_NUM_IN_PORT + (p) | (f << 16))

#define CKIO_DRV RZA2M_PINMUX(PORT_CKIO, 0, 0)


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA2M_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 56 行

按硬件手册（Hardware Manual）标注的端口名称。

### 注释 3：原第 75 行

没有端口 I。

### 注释 4：原第 79 行

硬件手册中将引脚 `PM_0/1` 标为 `JP_0/1`。

### 注释 5：原第 82 行

为 SPI 和 SD/MMC 选择 1.8 V 或 3.3 V 电压。

### 注释 6：原第 84 行

设置 `POSEL0` 位的功能。`00`、`01`、`10` 表示 1.8 V，`11` 表示 3.3 V。

### 注释 7：原第 85 行

设置 SSD 主机（host）0 的功能：0 表示 1.8 V，1 表示 3.3 V。

### 注释 8：原第 86 行

设置 SSD 主机（host）1 的功能：0 表示 1.8 V，1 表示 3.3 V。

### 注释 9：原第 110 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RZA2M_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_configuration_reference/P060_zephyr__dt-bindings__pinctrl__renesas__pinctrl-rza2m.h_文件参考.md)

---

[上一章](P015_parser_url.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_rtl8752h-pinctrl.h_源码浏览.md)
