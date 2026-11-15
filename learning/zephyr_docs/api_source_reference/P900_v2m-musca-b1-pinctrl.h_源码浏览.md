---
id: learning.zephyr-docs.api-source-reference.page-900
title: v2m-musca-b1-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第900章\_v2m-musca-b1-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h.html)。

## 900.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00014"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00031"></a>
<a id="l00032"></a>
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

```c
/*
 * Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#define MUSCA_B1_ALT_FUNC_MASK 0x1

#define MUSCA_B1_ALT_FUNC_POS 0

#define MUSCA_B1_EXP_NUM_MASK 0xF

#define MUSCA_B1_EXP_NUM_POS  4

#define MUSCA_B1_PINMUX(exp_num) (exp_num << MUSCA_B1_EXP_NUM_POS | 1 << MUSCA_B1_ALT_FUNC_POS)


#define UART0_RXD     MUSCA_B1_PINMUX(0)
#define UART0_TXD     MUSCA_B1_PINMUX(1)
#define MR_I2S_SD     MUSCA_B1_PINMUX(2)
#define MR_I2S_WS     MUSCA_B1_PINMUX(3)
#define MR_I2S_SCK    MUSCA_B1_PINMUX(4)
#define MT_I2S_SD0    MUSCA_B1_PINMUX(6)
#define MT_I2S_WS0    MUSCA_B1_PINMUX(5)
#define MT_I2S_SD1    MUSCA_B1_PINMUX(7)
#define MT_I2S_WS1    MUSCA_B1_PINMUX(8)
#define MT_I2S_SCK    MUSCA_B1_PINMUX(9)
#define SPIO_NSS0     MUSCA_B1_PINMUX(10)
#define SPIO_MOSI     MUSCA_B1_PINMUX(11)
#define SPIO_MISO     MUSCA_B1_PINMUX(12)
#define SPIO_SCK      MUSCA_B1_PINMUX(13)
#define I2C0_DATA     MUSCA_B1_PINMUX(14)
#define I2C0_CLOCK    MUSCA_B1_PINMUX(15)

```

## 900.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2026 Arm Limited and/or its affiliates <open-source-office@arm.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 900.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/v2m-musca-b1-pinctrl_8h.html)

---

[上一章](P899_user_pipe.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P901_vc.h_源码浏览.md)
