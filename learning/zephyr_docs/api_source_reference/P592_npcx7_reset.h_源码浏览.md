---
id: learning.zephyr-docs.api-source-reference.page-592
title: npcx7_reset.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx7__reset_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第592章\_npcx7\_reset.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/npcx7__reset_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/npcx7__reset_8h.html)。

## 592.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2024 Nuvoton Technology Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NPCX7_RESET_H
#define ZEPHYR_INCLUDE_DT_BINDINGS_RESET_NPCX7_RESET_H

#define NPCX_RESET_SWRST_CTL1_OFFSET 0
#define NPCX_RESET_SWRST_CTL2_OFFSET 32
#define NPCX_RESET_SWRST_CTL3_OFFSET 64

#define NPCX_RESET_GPIO0    (NPCX_RESET_SWRST_CTL1_OFFSET + 0)
#define NPCX_RESET_GPIO1    (NPCX_RESET_SWRST_CTL1_OFFSET + 1)
#define NPCX_RESET_GPIO2    (NPCX_RESET_SWRST_CTL1_OFFSET + 2)
#define NPCX_RESET_GPIO3    (NPCX_RESET_SWRST_CTL1_OFFSET + 3)
#define NPCX_RESET_GPIO4    (NPCX_RESET_SWRST_CTL1_OFFSET + 4)
#define NPCX_RESET_GPIO5    (NPCX_RESET_SWRST_CTL1_OFFSET + 5)
#define NPCX_RESET_GPIO6    (NPCX_RESET_SWRST_CTL1_OFFSET + 6)
#define NPCX_RESET_GPIO7    (NPCX_RESET_SWRST_CTL1_OFFSET + 7)
#define NPCX_RESET_GPIO8    (NPCX_RESET_SWRST_CTL1_OFFSET + 8)
#define NPCX_RESET_GPIO9    (NPCX_RESET_SWRST_CTL1_OFFSET + 9)
#define NPCX_RESET_GPIOA    (NPCX_RESET_SWRST_CTL1_OFFSET + 10)
#define NPCX_RESET_GPIOB    (NPCX_RESET_SWRST_CTL1_OFFSET + 11)
#define NPCX_RESET_GPIOC    (NPCX_RESET_SWRST_CTL1_OFFSET + 12)
#define NPCX_RESET_GPIOD    (NPCX_RESET_SWRST_CTL1_OFFSET + 13)
#define NPCX_RESET_GPIOE    (NPCX_RESET_SWRST_CTL1_OFFSET + 14)
#define NPCX_RESET_GPIOF    (NPCX_RESET_SWRST_CTL1_OFFSET + 15)
#define NPCX_RESET_ITIM64   (NPCX_RESET_SWRST_CTL1_OFFSET + 16)
#define NPCX_RESET_ITIM16_1 (NPCX_RESET_SWRST_CTL1_OFFSET + 18)
#define NPCX_RESET_ITIM16_2 (NPCX_RESET_SWRST_CTL1_OFFSET + 19)
#define NPCX_RESET_ITIM16_3 (NPCX_RESET_SWRST_CTL1_OFFSET + 20)
#define NPCX_RESET_ITIM16_4 (NPCX_RESET_SWRST_CTL1_OFFSET + 21)
#define NPCX_RESET_ITIM16_5 (NPCX_RESET_SWRST_CTL1_OFFSET + 22)
#define NPCX_RESET_ITIM16_6 (NPCX_RESET_SWRST_CTL1_OFFSET + 23)
#define NPCX_RESET_ITIM32   (NPCX_RESET_SWRST_CTL1_OFFSET + 24)
#define NPCX_RESET_MTC      (NPCX_RESET_SWRST_CTL1_OFFSET + 25)
#define NPCX_RESET_MIWU0    (NPCX_RESET_SWRST_CTL1_OFFSET + 26)
#define NPCX_RESET_MIWU1    (NPCX_RESET_SWRST_CTL1_OFFSET + 27)
#define NPCX_RESET_MIWU2    (NPCX_RESET_SWRST_CTL1_OFFSET + 28)
#define NPCX_RESET_GDMA     (NPCX_RESET_SWRST_CTL1_OFFSET + 29)
#define NPCX_RESET_FIU      (NPCX_RESET_SWRST_CTL1_OFFSET + 30)

#define NPCX_RESET_PMC     (NPCX_RESET_SWRST_CTL2_OFFSET + 0)
#define NPCX_RESET_SHI     (NPCX_RESET_SWRST_CTL2_OFFSET + 2)
#define NPCX_RESET_SPIP    (NPCX_RESET_SWRST_CTL2_OFFSET + 3)
#define NPCX_RESET_PECI    (NPCX_RESET_SWRST_CTL2_OFFSET + 5)
#define NPCX_RESET_CRUART2 (NPCX_RESET_SWRST_CTL2_OFFSET + 6)
#define NPCX_RESET_ADC     (NPCX_RESET_SWRST_CTL2_OFFSET + 7)
#define NPCX_RESET_SMB0    (NPCX_RESET_SWRST_CTL2_OFFSET + 8)
#define NPCX_RESET_SMB1    (NPCX_RESET_SWRST_CTL2_OFFSET + 9)
#define NPCX_RESET_SMB2    (NPCX_RESET_SWRST_CTL2_OFFSET + 10)
#define NPCX_RESET_SMB3    (NPCX_RESET_SWRST_CTL2_OFFSET + 11)
#define NPCX_RESET_SMB4    (NPCX_RESET_SWRST_CTL2_OFFSET + 12)
#define NPCX_RESET_SMB5    (NPCX_RESET_SWRST_CTL2_OFFSET + 13)
#define NPCX_RESET_SMB6    (NPCX_RESET_SWRST_CTL2_OFFSET + 14)
#define NPCX_RESET_TWD     (NPCX_RESET_SWRST_CTL2_OFFSET + 15)
#define NPCX_RESET_PWM0    (NPCX_RESET_SWRST_CTL2_OFFSET + 16)
#define NPCX_RESET_PWM1    (NPCX_RESET_SWRST_CTL2_OFFSET + 17)
#define NPCX_RESET_PWM2    (NPCX_RESET_SWRST_CTL2_OFFSET + 18)
#define NPCX_RESET_PWM3    (NPCX_RESET_SWRST_CTL2_OFFSET + 19)
#define NPCX_RESET_PWM4    (NPCX_RESET_SWRST_CTL2_OFFSET + 20)
#define NPCX_RESET_PWM5    (NPCX_RESET_SWRST_CTL2_OFFSET + 21)
#define NPCX_RESET_PWM6    (NPCX_RESET_SWRST_CTL2_OFFSET + 22)
#define NPCX_RESET_PWM7    (NPCX_RESET_SWRST_CTL2_OFFSET + 23)
#define NPCX_RESET_MFT16_1 (NPCX_RESET_SWRST_CTL2_OFFSET + 24)
#define NPCX_RESET_MFT16_2 (NPCX_RESET_SWRST_CTL2_OFFSET + 25)
#define NPCX_RESET_MFT16_3 (NPCX_RESET_SWRST_CTL2_OFFSET + 26)
#define NPCX_RESET_SMB7    (NPCX_RESET_SWRST_CTL2_OFFSET + 27)
#define NPCX_RESET_CRUART1 (NPCX_RESET_SWRST_CTL2_OFFSET + 28)
#define NPCX_RESET_PS2     (NPCX_RESET_SWRST_CTL2_OFFSET + 29)
#define NPCX_RESET_SDP     (NPCX_RESET_SWRST_CTL2_OFFSET + 30)
#define NPCX_RESET_KBS     (NPCX_RESET_SWRST_CTL2_OFFSET + 31)

#define NPCX_RESET_SIOCFG  (NPCX_RESET_SWRST_CTL3_OFFSET + 0)
#define NPCX_RESET_SERPORT (NPCX_RESET_SWRST_CTL3_OFFSET + 1)
#define NPCX_RESET_MSWC    (NPCX_RESET_SWRST_CTL3_OFFSET + 8)
#define NPCX_RESET_SHM     (NPCX_RESET_SWRST_CTL3_OFFSET + 9)
#define NPCX_RESET_PMCH1   (NPCX_RESET_SWRST_CTL3_OFFSET + 10)
#define NPCX_RESET_PMCH2   (NPCX_RESET_SWRST_CTL3_OFFSET + 11)
#define NPCX_RESET_PMCH3   (NPCX_RESET_SWRST_CTL3_OFFSET + 12)
#define NPCX_RESET_PMCH4   (NPCX_RESET_SWRST_CTL3_OFFSET + 13)
#define NPCX_RESET_KBC     (NPCX_RESET_SWRST_CTL3_OFFSET + 15)
#define NPCX_RESET_C2HOST  (NPCX_RESET_SWRST_CTL3_OFFSET + 16)
#define NPCX_RESET_LFCG    (NPCX_RESET_SWRST_CTL3_OFFSET + 20)
#define NPCX_RESET_DEV     (NPCX_RESET_SWRST_CTL3_OFFSET + 22)
#define NPCX_RESET_SYSCFG  (NPCX_RESET_SWRST_CTL3_OFFSET + 23)
#define NPCX_RESET_SBY     (NPCX_RESET_SWRST_CTL3_OFFSET + 24)
#define NPCX_RESET_BBRAM   (NPCX_RESET_SWRST_CTL3_OFFSET + 25)

#define NPCX_RESET_ID_START NPCX_RESET_GPIO0
#define NPCX_RESET_ID_END   NPCX_RESET_BBRAM
#endif
```

## 592.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nuvoton Technology Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 592.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/npcx7__reset_8h.html)

---

[上一章](P591_npcx4_reset.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P593_npcx9_reset.h_源码浏览.md)
