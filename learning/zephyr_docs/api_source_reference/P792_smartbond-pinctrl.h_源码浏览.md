---
id: learning.zephyr-docs.api-source-reference.page-792
title: smartbond-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第792章\_smartbond-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h.html)。

## 792.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00076"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>

```c
/*
 * Copyright (c) 2022, Renesas Electronics Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SMARTBOND_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SMARTBOND_PINCTRL_H_

#define SMARTBOND_FUNC_GPIO             0
#define SMARTBOND_FUNC_UART_RX          1
#define SMARTBOND_FUNC_UART_TX          2
#define SMARTBOND_FUNC_UART2_RX         3
#define SMARTBOND_FUNC_UART2_TX         4
#define SMARTBOND_FUNC_UART2_CTSN       5
#define SMARTBOND_FUNC_UART2_RTSN       6
#define SMARTBOND_FUNC_UART3_RX         7
#define SMARTBOND_FUNC_UART3_TX         8
#define SMARTBOND_FUNC_UART3_CTSN       9
#define SMARTBOND_FUNC_UART3_RTSN       10
#define SMARTBOND_FUNC_ISO_CLK          11
#define SMARTBOND_FUNC_ISO_DATA         12
#define SMARTBOND_FUNC_SPI_DI           13
#define SMARTBOND_FUNC_SPI_DO           14
#define SMARTBOND_FUNC_SPI_CLK          15
#define SMARTBOND_FUNC_SPI_EN           16
#define SMARTBOND_FUNC_SPI2_DI          17
#define SMARTBOND_FUNC_SPI2_DO          18
#define SMARTBOND_FUNC_SPI2_CLK         19
#define SMARTBOND_FUNC_SPI2_EN          20
#define SMARTBOND_FUNC_I2C_SCL          21
#define SMARTBOND_FUNC_I2C_SDA          22
#define SMARTBOND_FUNC_I2C2_SCL         23
#define SMARTBOND_FUNC_I2C2_SDA         24
#define SMARTBOND_FUNC_USB_SOF          25
#define SMARTBOND_FUNC_ADC              26
#define SMARTBOND_FUNC_USB              27
#define SMARTBOND_FUNC_PCM_DI           28
#define SMARTBOND_FUNC_PCM_DO           29
#define SMARTBOND_FUNC_PCM_FSC          30
#define SMARTBOND_FUNC_PCM_CLK          31
#define SMARTBOND_FUNC_PDM_DATA         32
#define SMARTBOND_FUNC_PDM_CLK          33
#define SMARTBOND_FUNC_COEX_EXT_ACT     34
#define SMARTBOND_FUNC_COEX_SMART_ACT   35
#define SMARTBOND_FUNC_COEX_SMART_PRI   36
#define SMARTBOND_FUNC_PORT0_DCF        37
#define SMARTBOND_FUNC_PORT1_DCF        38
#define SMARTBOND_FUNC_PORT2_DCF        39
#define SMARTBOND_FUNC_PORT3_DCF        40
#define SMARTBOND_FUNC_PORT4_DCF        41
#define SMARTBOND_FUNC_CLOCK            42
#define SMARTBOND_FUNC_PG               43
#define SMARTBOND_FUNC_LCD              44
#define SMARTBOND_FUNC_LCD_SPI_DC       45
#define SMARTBOND_FUNC_LCD_SPI_DO       46
#define SMARTBOND_FUNC_LCD_SPI_CLK      47
#define SMARTBOND_FUNC_LCD_SPI_EN       48
#define SMARTBOND_FUNC_TIM_PWM          49
#define SMARTBOND_FUNC_TIM2_PWM         50
#define SMARTBOND_FUNC_TIM_1SHOT        51
#define SMARTBOND_FUNC_TIM2_1SHOT       52
#define SMARTBOND_FUNC_TIM3_PWM         53
#define SMARTBOND_FUNC_TIM4_PWM         54

#define SMARTBOND_PINMUX_PIN_POS        0
#define SMARTBOND_PINMUX_PIN_MASK       0x1f
#define SMARTBOND_PINMUX_PORT_POS       5
#define SMARTBOND_PINMUX_PORT_MASK      0x01
#define SMARTBOND_PINMUX_FUNC_POS       6
#define SMARTBOND_PINMUX_FUNC_MASK      0xff

#define SMARTBOND_PINMUX(func, port, pin)                               \
        (((SMARTBOND_FUNC_ ## func) << SMARTBOND_PINMUX_FUNC_POS) |     \
         ((port) << SMARTBOND_PINMUX_PORT_POS) |                        \
         (pin) << SMARTBOND_PINMUX_PIN_POS)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SMARTBOND_PINCTRL_H_ */
```

## 792.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022, Renesas Electronics Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 81 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_SMARTBOND_PINCTRL_H_`。

## 792.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smartbond-pinctrl_8h.html)

---

[上一章](P791_siwx91x-clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P793_smartbond_clock_control.h_源码浏览.md)
