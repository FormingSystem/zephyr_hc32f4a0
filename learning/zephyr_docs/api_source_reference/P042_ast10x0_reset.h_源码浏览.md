---
id: learning.zephyr-docs.api-source-reference.page-42
title: ast10x0_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_ast10x0\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h.html)。

## 42.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2022 Aspeed Technology Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_AST10X0_RESET_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_AST10X0_RESET_H_

#define ASPEED_RESET_GRP_0_OFFSET       (0)
#define ASPEED_RESET_GRP_1_OFFSET       (32)

#define ASPEED_RESET_HACE               (ASPEED_RESET_GRP_0_OFFSET + 4)
#define ASPEED_RESET_USB                (ASPEED_RESET_GRP_0_OFFSET + 3)
#define ASPEED_RESET_SRAM               (ASPEED_RESET_GRP_0_OFFSET + 0)

#define ASPEED_RESET_UART4              (ASPEED_RESET_GRP_1_OFFSET + 31)
#define ASPEED_RESET_UART3              (ASPEED_RESET_GRP_1_OFFSET + 30)
#define ASPEED_RESET_UART2              (ASPEED_RESET_GRP_1_OFFSET + 29)
#define ASPEED_RESET_UART1              (ASPEED_RESET_GRP_1_OFFSET + 28)

#define ASPEED_RESET_JTAG_M0            (ASPEED_RESET_GRP_1_OFFSET + 26)
#define ASPEED_RESET_ESPI               (ASPEED_RESET_GRP_1_OFFSET + 25)

#define ASPEED_RESET_ADC                (ASPEED_RESET_GRP_1_OFFSET + 23)
#define ASPEED_RESET_JTAG_M1            (ASPEED_RESET_GRP_1_OFFSET + 22)

#define ASPEED_RESET_MAC                (ASPEED_RESET_GRP_1_OFFSET + 20)

#define ASPEED_RESET_I3C3               (ASPEED_RESET_GRP_1_OFFSET + 11)
#define ASPEED_RESET_I3C2               (ASPEED_RESET_GRP_1_OFFSET + 10)
#define ASPEED_RESET_I3C1               (ASPEED_RESET_GRP_1_OFFSET + 9)
#define ASPEED_RESET_I3C0               (ASPEED_RESET_GRP_1_OFFSET + 8)
#define ASPEED_RESET_I3C                (ASPEED_RESET_GRP_1_OFFSET + 7)
#define ASPEED_RESET_PWM_TACH           (ASPEED_RESET_GRP_1_OFFSET + 5)
#define ASPEED_RESET_PECI               (ASPEED_RESET_GRP_1_OFFSET + 4)
#define ASPEED_RESET_MII                (ASPEED_RESET_GRP_1_OFFSET + 3)
#define ASPEED_RESET_I2C                (ASPEED_RESET_GRP_1_OFFSET + 2)

#define ASPEED_RESET_LPC                (ASPEED_RESET_GRP_1_OFFSET + 0)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_RESET_AST10X0_RESET_H_ */
```

## 42.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Aspeed Technology Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_RESET_AST10X0_RESET_H_`。

## 42.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ast10x0__reset_8h.html)

---

[上一章](P041_ast10x0_clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P043_atmel-sam-gpio.h_源码浏览.md)
