---
id: learning.zephyr-docs.api-source-reference.page-791
title: siwx91x-clock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第791章\_siwx91x-clock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html)。

## 791.1\_原始可见代码（Source Code）

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
<a id="l00025"></a>
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
<a id="l00056"></a>
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
<a id="l00072"></a>
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
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>

```c
/*
 * Copyright (c) 2024-2026 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_SIWX91X_CLOCK_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_SIWX91X_CLOCK_H_


#define SIWX91X_CLK_UART0          0
#define SIWX91X_CLK_UART1          1
#define SIWX91X_CLK_I2C0           2
#define SIWX91X_CLK_I2C1           3
#define SIWX91X_CLK_UDMA           4
#define SIWX91X_CLK_PWM            5
#define SIWX91X_CLK_GSPI           6
#define SIWX91X_CLK_QSPI           7
#define SIWX91X_CLK_QSPI2          8
#define SIWX91X_CLK_I2S            9
#define SIWX91X_CLK_STATIC_I2S     10
#define SIWX91X_CLK_GPDMA          11
#define SIWX91X_CLK_RNG            12
#define SIWX91X_CLK_GPIO           13
#define SIWX91X_CLK_SSI            14
#define SIWX91X_CLK_PIN_OUT        15
#define SIWX91X_CLK_ICACHE         16

#define SIWX91X_CLK_CPU            17
#define SIWX91X_CLK_CPU_LP         18

#define SIWX91X_CLK_HP_REF_ULP     19
#define SIWX91X_CLK_HP_REF_PLL     20

#define SIWX91X_CLK_PLL_SOC        21
#define SIWX91X_CLK_PLL_INTF       22
#define SIWX91X_CLK_PLL_I2S        23

#define SIWX91X_CLK_ULP_UART       24
#define SIWX91X_CLK_ULP_I2C        25
#define SIWX91X_CLK_ULP_UDMA       26
#define SIWX91X_CLK_ULP_I2S        27
#define SIWX91X_CLK_ULP_STATIC_I2S 28
#define SIWX91X_CLK_ULP_ADC        29
#define SIWX91X_CLK_ULP_SSI        30
#define SIWX91X_CLK_ULP_TIMER      31
#define SIWX91X_CLK_ULP_GPIO       32

#define SIWX91X_CLK_ULP_REF_AON    33
#define SIWX91X_CLK_ULP_REF_CPU    34

#define SIWX91X_CLK_XTAL_MHZ       35
#define SIWX91X_CLK_XTAL_KHZ       36
#define SIWX91X_CLK_RC_MHZ         37
#define SIWX91X_CLK_RC_KHZ         38

#define SIWX91X_CLK_WATCHDOG       39
#define SIWX91X_CLK_RTC            40
#define SIWX91X_CLK_SYSRTC         41
#define SIWX91X_CLK_UULP_GPIO      42

#define SIWX91X_CLK_REF_HP         43
#define SIWX91X_CLK_REF_ULP        44
#define SIWX91X_CLK_AON_REF_HF     45
#define SIWX91X_CLK_AON_REF_LF     46

#define SIWX91X_CLK_GATED          47


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_SIWX91X_CLOCK_H_ */
```

## 791.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024-2026 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 96 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_CLOCK_SILABS_SIWX91X_CLOCK_H_`。

## 791.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/siwx91x-clock_8h.html)

---

[上一章](P790_sip_svc_proto.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P792_smartbond-pinctrl.h_源码浏览.md)
