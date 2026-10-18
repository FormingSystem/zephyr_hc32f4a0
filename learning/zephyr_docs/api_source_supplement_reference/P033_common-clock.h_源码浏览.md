---
id: learning.zephyr-docs.api-source-supplement-reference.page-33
title: common-clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/common-clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第33章\_common-clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/common-clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/common-clock_8h.html)。

## 33.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00027"></a>
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
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00089"></a>

```c


 /*
 * Copyright (c) 2024 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_COMMON_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_COMMON_CLOCK_H_



/*
 * DT macros for clock branches.
 * Must stay in sync with the enum sl_clock_branch_t in the Silicon Labs HAL to be
 * interpreted correctly by the clock control driver.
 */
#define CLOCK_BRANCH_SYSCLK       0
#define CLOCK_BRANCH_HCLK         1
#define CLOCK_BRANCH_HCLKRADIO    2
#define CLOCK_BRANCH_PCLK         3
#define CLOCK_BRANCH_LSPCLK       4
#define CLOCK_BRANCH_TRACECLK     5
#define CLOCK_BRANCH_ADCCLK       6
#define CLOCK_BRANCH_EXPORTCLK    7
#define CLOCK_BRANCH_EM01GRPACLK  8
#define CLOCK_BRANCH_EM01GRPBCLK  9
#define CLOCK_BRANCH_EM01GRPCCLK  10
#define CLOCK_BRANCH_EM01GRPDCLK  11
#define CLOCK_BRANCH_EM23GRPACLK  12
#define CLOCK_BRANCH_EM4GRPACLK   13
#define CLOCK_BRANCH_QSPISYSCLK   14
#define CLOCK_BRANCH_IADCCLK      15
#define CLOCK_BRANCH_WDOG0CLK     16
#define CLOCK_BRANCH_WDOG1CLK     17
#define CLOCK_BRANCH_RTCCCLK      18
#define CLOCK_BRANCH_SYSRTCCLK    19
#define CLOCK_BRANCH_EUART0CLK    20
#define CLOCK_BRANCH_EUSART0CLK   21
#define CLOCK_BRANCH_EUSART1CLK   22
#define CLOCK_BRANCH_DPLLREFCLK   23
#define CLOCK_BRANCH_I2C0CLK      24
#define CLOCK_BRANCH_LCDCLK       25
#define CLOCK_BRANCH_PIXELRZCLK   26
#define CLOCK_BRANCH_PCNT0CLK     27
#define CLOCK_BRANCH_PRORTCCLK    28
#define CLOCK_BRANCH_SYSTICKCLK   29
#define CLOCK_BRANCH_LESENSEHFCLK 30
#define CLOCK_BRANCH_VDAC0CLK     31
#define CLOCK_BRANCH_VDAC1CLK     32
#define CLOCK_BRANCH_USB0CLK      33
#define CLOCK_BRANCH_FLPLLREFCLK  34
#define CLOCK_BRANCH_PDM0CLK      35
#define CLOCK_BRANCH_CAN0CLK      36
#define CLOCK_BRANCH_CAN1CLK      37
#define CLOCK_BRANCH_HCLKDIVN     38
#define CLOCK_BRANCH_CPUCLK       39
#define CLOCK_BRANCH_ADC0CLK      40
#define CLOCK_BRANCH_ADC1CLK      41
#define CLOCK_BRANCH_LEDSINK0CLK  42
#define CLOCK_BRANCH_INVALID      43

#define CLOCK_BIT_MASK 0x03FUL
#define CLOCK_REG_MASK 0x1C0UL



#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_COMMON_CLOCK_H_ */
```

## 33.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2024 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 30 行

时钟分支（Clock branches）的设备树（DT）宏。必须与 Silicon Labs HAL 中的 `sl_clock_branch_t` 枚举保持同步，才能被时钟控制驱动正确解释。

### 注释 3：原第 89 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_COMMON_CLOCK_H_`。

## 33.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/common-clock_8h.html)

---

[上一章](P032_codec.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P034_policy.h_源码浏览.md)
