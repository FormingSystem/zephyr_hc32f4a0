---
id: learning.zephyr-docs.api-source-reference.page-222
title: emsdp-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emsdp-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第222章\_emsdp-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emsdp-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emsdp-pinctrl_8h.html)。

## 222.1\_原始可见代码（Source Code）

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

```c
/*
 * Copyright (c) 2023 Synopsys
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EMSDP_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EMSDP_PINCTRL_H_

#define PMOD_A              0
#define PMOD_B              1
#define PMOD_C              2
#define ARDUINO_PIN_0       3
#define ARDUINO_PIN_1       4
#define ARDUINO_PIN_2       5
#define ARDUINO_PIN_3       6
#define ARDUINO_PIN_4       7
#define ARDUINO_PIN_5       8
#define ARDUINO_PIN_6       9
#define ARDUINO_PIN_7       10
#define ARDUINO_PIN_8       11
#define ARDUINO_PIN_9       12
#define ARDUINO_PIN_10      13
#define ARDUINO_PIN_11      14
#define ARDUINO_PIN_12      15
#define ARDUINO_PIN_13      16
#define ARDUINO_PIN_AD0     17
#define ARDUINO_PIN_AD1     18
#define ARDUINO_PIN_AD2     19
#define ARDUINO_PIN_AD3     20
#define ARDUINO_PIN_AD4     21
#define ARDUINO_PIN_AD5     22
#define UNMUXED_PIN       23

#define PMOD_GPIO           0
#define PMOD_UARTA          1
#define PMOD_UARTB          2
#define PMOD_SPI            3
#define PMOD_I2C            4
#define PMOD_PWM_MODE1      5
#define PMOD_PWM_MODE2      6
#define PMOD_PWM_MODE3      7
#define ARDUINO_GPIO        8
#define ARDUINO_UART        9
#define ARDUINO_SPI         10
#define ARDUINO_I2C         11
#define ARDUINO_PWM         12
#define ARDUINO_ADC         13
#define NOT_PINMUX          14


#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EMSDP_PINCTRL_H_ */
```

## 222.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Synopsys。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_EMSDP_PINCTRL_H_`。

## 222.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emsdp-pinctrl_8h.html)

---

[上一章](P221_elf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P223_emul_bbram.h_源码浏览.md)
