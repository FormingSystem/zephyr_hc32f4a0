---
id: learning.zephyr-docs.api-source-supplement-reference.page-128
title: npcm_clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_npcm\_clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h.html)。

## 128.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NPCM_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NPCM_CLOCK_H_

/* clock bus references */
#define NPCM_CLOCK_GROUP_OFFSET(N) ((N) << 3)

#define NPCM_CLOCK_PWM_I   (NPCM_CLOCK_GROUP_OFFSET(0) + 0)
#define NPCM_CLOCK_PWM_J   (NPCM_CLOCK_GROUP_OFFSET(0) + 1)
#define NPCM_CLOCK_I3CI    (NPCM_CLOCK_GROUP_OFFSET(0) + 2)
#define NPCM_CLOCK_UART3   (NPCM_CLOCK_GROUP_OFFSET(0) + 5)
#define NPCM_CLOCK_UART2   (NPCM_CLOCK_GROUP_OFFSET(0) + 6)
#define NPCM_CLOCK_SPIM    (NPCM_CLOCK_GROUP_OFFSET(1) + 0)
#define NPCM_CLOCK_FIU     (NPCM_CLOCK_GROUP_OFFSET(1) + 2)
#define NPCM_CLOCK_USB20   (NPCM_CLOCK_GROUP_OFFSET(1) + 3)
#define NPCM_CLOCK_UART    (NPCM_CLOCK_GROUP_OFFSET(1) + 4)
#define NPCM_CLOCK_MFT1    (NPCM_CLOCK_GROUP_OFFSET(1) + 5)
#define NPCM_CLOCK_MFT2    (NPCM_CLOCK_GROUP_OFFSET(1) + 6)
#define NPCM_CLOCK_MFT3    (NPCM_CLOCK_GROUP_OFFSET(1) + 7)
#define NPCM_CLOCK_PWM_A   (NPCM_CLOCK_GROUP_OFFSET(2) + 0)
#define NPCM_CLOCK_PWM_B   (NPCM_CLOCK_GROUP_OFFSET(2) + 1)
#define NPCM_CLOCK_PWM_C   (NPCM_CLOCK_GROUP_OFFSET(2) + 2)
#define NPCM_CLOCK_PWM_D   (NPCM_CLOCK_GROUP_OFFSET(2) + 3)
#define NPCM_CLOCK_PWM_E   (NPCM_CLOCK_GROUP_OFFSET(2) + 4)
#define NPCM_CLOCK_PWM_F   (NPCM_CLOCK_GROUP_OFFSET(2) + 5)
#define NPCM_CLOCK_PWM_G   (NPCM_CLOCK_GROUP_OFFSET(2) + 6)
#define NPCM_CLOCK_PWM_H   (NPCM_CLOCK_GROUP_OFFSET(2) + 7)
#define NPCM_CLOCK_SMB1    (NPCM_CLOCK_GROUP_OFFSET(3) + 0)
#define NPCM_CLOCK_SMB2    (NPCM_CLOCK_GROUP_OFFSET(3) + 1)
#define NPCM_CLOCK_SMB3    (NPCM_CLOCK_GROUP_OFFSET(3) + 2)
#define NPCM_CLOCK_SMB4    (NPCM_CLOCK_GROUP_OFFSET(3) + 3)
#define NPCM_CLOCK_SMB5    (NPCM_CLOCK_GROUP_OFFSET(3) + 4)
#define NPCM_CLOCK_SMB6    (NPCM_CLOCK_GROUP_OFFSET(3) + 5)
#define NPCM_CLOCK_GDMA    (NPCM_CLOCK_GROUP_OFFSET(3) + 7)
#define NPCM_CLOCK_ITIM1   (NPCM_CLOCK_GROUP_OFFSET(4) + 0)
#define NPCM_CLOCK_ITIM2   (NPCM_CLOCK_GROUP_OFFSET(4) + 1)
#define NPCM_CLOCK_ITIM3   (NPCM_CLOCK_GROUP_OFFSET(4) + 2)
#define NPCM_CLOCK_SMB_DMA (NPCM_CLOCK_GROUP_OFFSET(4) + 3)
#define NPCM_CLOCK_ADC     (NPCM_CLOCK_GROUP_OFFSET(4) + 4)
#define NPCM_CLOCK_PECI    (NPCM_CLOCK_GROUP_OFFSET(4) + 5)
#define NPCM_CLOCK_SPIP1   (NPCM_CLOCK_GROUP_OFFSET(4) + 7)
#define NPCM_CLOCK_UART4   (NPCM_CLOCK_GROUP_OFFSET(5) + 0)
#define NPCM_CLOCK_C2HACC  (NPCM_CLOCK_GROUP_OFFSET(5) + 3)
#define NPCM_CLOCK_SHM_REG (NPCM_CLOCK_GROUP_OFFSET(5) + 4)
#define NPCM_CLOCK_SHM     (NPCM_CLOCK_GROUP_OFFSET(5) + 5)
#define NPCM_CLOCK_DP80    (NPCM_CLOCK_GROUP_OFFSET(5) + 6)
#define NPCM_CLOCK_MSWC    (NPCM_CLOCK_GROUP_OFFSET(5) + 7)
#define NPCM_CLOCK_ITIM4   (NPCM_CLOCK_GROUP_OFFSET(6) + 0)
#define NPCM_CLOCK_ITIM5   (NPCM_CLOCK_GROUP_OFFSET(6) + 1)
#define NPCM_CLOCK_ITIM6   (NPCM_CLOCK_GROUP_OFFSET(6) + 2)
#define NPCM_CLOCK_RNG     (NPCM_CLOCK_GROUP_OFFSET(6) + 3)
#define NPCM_CLOCK_SHA     (NPCM_CLOCK_GROUP_OFFSET(6) + 5)
#define NPCM_CLOCK_ESPI    (NPCM_CLOCK_GROUP_OFFSET(6) + 7)
#define NPCM_CLOCK_SMB7    (NPCM_CLOCK_GROUP_OFFSET(7) + 0)
#define NPCM_CLOCK_SMB8    (NPCM_CLOCK_GROUP_OFFSET(7) + 1)
#define NPCM_CLOCK_SMB9    (NPCM_CLOCK_GROUP_OFFSET(7) + 2)
#define NPCM_CLOCK_SMB10   (NPCM_CLOCK_GROUP_OFFSET(7) + 3)
#define NPCM_CLOCK_SMB11   (NPCM_CLOCK_GROUP_OFFSET(7) + 4)
#define NPCM_CLOCK_SMB12   (NPCM_CLOCK_GROUP_OFFSET(7) + 5)
#define NPCM_CLOCK_SIOX2   (NPCM_CLOCK_GROUP_OFFSET(7) + 6)
#define NPCM_CLOCK_SIOX1   (NPCM_CLOCK_GROUP_OFFSET(7) + 7)
#define NPCM_CLOCK_I3CI2   (NPCM_CLOCK_GROUP_OFFSET(8) + 0)
#define NPCM_CLOCK_I3CI3   (NPCM_CLOCK_GROUP_OFFSET(8) + 1)
#define NPCM_CLOCK_I3CI4   (NPCM_CLOCK_GROUP_OFFSET(8) + 2)
#define NPCM_CLOCK_I3CI5   (NPCM_CLOCK_GROUP_OFFSET(8) + 3)
#define NPCM_CLOCK_I3CI6   (NPCM_CLOCK_GROUP_OFFSET(8) + 4)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NPCM_CLOCK_H_ */
```

## 128.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 9 行

时钟总线引用（Clock bus references）。

### 注释 3：原第 72 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_NPCM_CLOCK_H_`。

## 128.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/npcm__clock_8h.html)

---

[上一章](P127_nordic-nrf-ficr-nrf9230-engb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P129_npcx_clock.h_源码浏览.md)
