---
id: learning.zephyr-docs.api-source-supplement-reference.page-143
title: pinctrl-rcar-common.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第143章\_pinctrl-rcar-common.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)。

## 143.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00021"></a>
<a id="l00056"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>

```c
/*
 * Copyright (c) 2021-2023 IoT.bzh
 * Copyright (c) 2025 Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RCAR_COMMON_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RCAR_COMMON_H_



#define IPSR(bank, shift, func) (((bank) << 10U) | ((shift) << 4U) | (func))

/* Arbitrary number to encode non capable gpio pin */
#define PIN_NOGPSR_START 1024U

#define RCAR_GP_PIN(bank, pin)     (((bank) * 32U) + (pin))

#define RCAR_NOGP_PIN(pin)         (PIN_NOGPSR_START + pin)

#define IPnSR(bank, reg, shift, func) \
        IPSR(((reg) << 5U) | (bank), shift, func)

#define IP0SR0(shift, func) IPnSR(0, 0, shift, func)
#define IP1SR0(shift, func) IPnSR(1, 0, shift, func)
#define IP2SR0(shift, func) IPnSR(2, 0, shift, func)
#define IP3SR0(shift, func) IPnSR(3, 0, shift, func)
#define IP0SR1(shift, func) IPnSR(0, 1, shift, func)
#define IP1SR1(shift, func) IPnSR(1, 1, shift, func)
#define IP2SR1(shift, func) IPnSR(2, 1, shift, func)
#define IP3SR1(shift, func) IPnSR(3, 1, shift, func)
#define IP0SR2(shift, func) IPnSR(0, 2, shift, func)
#define IP1SR2(shift, func) IPnSR(1, 2, shift, func)
#define IP2SR2(shift, func) IPnSR(2, 2, shift, func)
#define IP3SR2(shift, func) IPnSR(3, 2, shift, func)
#define IP0SR3(shift, func) IPnSR(0, 3, shift, func)
#define IP1SR3(shift, func) IPnSR(1, 3, shift, func)
#define IP2SR3(shift, func) IPnSR(2, 3, shift, func)
#define IP3SR3(shift, func) IPnSR(3, 3, shift, func)
#define IP0SR4(shift, func) IPnSR(0, 4, shift, func)
#define IP1SR4(shift, func) IPnSR(1, 4, shift, func)
#define IP2SR4(shift, func) IPnSR(2, 4, shift, func)
#define IP3SR4(shift, func) IPnSR(3, 4, shift, func)
#define IP0SR5(shift, func) IPnSR(0, 5, shift, func)
#define IP1SR5(shift, func) IPnSR(1, 5, shift, func)
#define IP2SR5(shift, func) IPnSR(2, 5, shift, func)
#define IP3SR5(shift, func) IPnSR(3, 5, shift, func)
#define IP0SR6(shift, func) IPnSR(0, 6, shift, func)
#define IP1SR6(shift, func) IPnSR(1, 6, shift, func)
#define IP2SR6(shift, func) IPnSR(2, 6, shift, func)
#define IP3SR6(shift, func) IPnSR(3, 6, shift, func)
#define IP0SR7(shift, func) IPnSR(0, 7, shift, func)
#define IP1SR7(shift, func) IPnSR(1, 7, shift, func)
#define IP2SR7(shift, func) IPnSR(2, 7, shift, func)
#define IP3SR7(shift, func) IPnSR(3, 7, shift, func)
#define IP0SR8(shift, func) IPnSR(0, 8, shift, func)
#define IP1SR8(shift, func) IPnSR(1, 8, shift, func)
#define IP2SR8(shift, func) IPnSR(2, 8, shift, func)
#define IP3SR8(shift, func) IPnSR(3, 8, shift, func)

#define IPSR_DUMMY IPnSR(0x1f, 7, 0x1f, 0xf)

#define RCAR_ALTSEL_FUNC(group, pin, func) (((pin) << 14U) | ((group) << 10U) | (func))

#define PIN_VOLTAGE_NONE 0
#define PIN_VOLTAGE_1P8V 1
#define PIN_VOLTAGE_3P3V 2


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RCAR_COMMON_H_ */
```

## 143.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2021-2023 IoT.bzh。

版权（Copyright）：© 2025 Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 75 行

用于编码不具备相应能力的 GPIO 引脚的任意数值。

### 注释 3：原第 186 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_RENESAS_PINCTRL_RCAR_COMMON_H_`。

## 143.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl-rcar-common_8h.html)

---

[上一章](P142_phy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P144_pinctrl-rzt-common.h_源码浏览.md)
