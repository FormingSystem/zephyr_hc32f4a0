---
id: learning.zephyr-docs.api-source-configuration-reference.page-4
title: amebadplus-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_amebadplus-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h.html)。

## 4.1\_原始可见代码（Source Code）

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
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>

```c
/*
 * Copyright (c) 2024 Realtek Semiconductor Corp.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBADPLUS_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBADPLUS_PINCTRL_H_

/* PINMUX Function definitions */
#define AMEBA_GPIO        0
#define AMEBA_LOG_UART    1
#define AMEBA_UART        1
#define AMEBA_SPIC0_FLASH 2
#define AMEBA_SPIC1_FLASH 3
#define AMEBA_SPIC1_PSRAM 4
#define AMEBA_OSPI        5
#define AMEBA_QSPI        5
#define AMEBA_ADC         6
#define AMEBA_CAP_TOUCH   6
#define AMEBA_SIC         7
#define AMEBA_SPI         8
#define AMEBA_SWD         9
#define AMEBA_SDIO        10
#define AMEBA_ANT_DIV     11
#define AMEBA_EXT_BT      12
#define AMEBA_BT_IO       13
#define AMEBA_BT          14
#define AMEBA_EXT_ZIGBEE  15
#define AMEBA_TIMER       16
#define AMEBA_USB         17
#define AMEBA_DEBUG       18
#define AMEBA_UART0_TXD   19
#define AMEBA_UART0_RXD   20
#define AMEBA_UART0_CTS   21
#define AMEBA_UART0_RTS   22
#define AMEBA_UART1_TXD   23
#define AMEBA_UART1_RXD   24
#define AMEBA_UART2_TXD   25
#define AMEBA_UART2_RXD   26
#define AMEBA_UART2_CTS   27
#define AMEBA_UART2_RTS   28
#define AMEBA_SPI1_CLK    29
#define AMEBA_SPI1_MISO   30
#define AMEBA_SPI1_MOSI   31
#define AMEBA_SPI1_CS     32
#define AMEBA_LEDC        33
#define AMEBA_I2S0_MCLK   34
#define AMEBA_I2S0_BCLK   35
#define AMEBA_I2S0_WS     36
#define AMEBA_I2S0_DIO0   37
#define AMEBA_I2S0_DIO1   38
#define AMEBA_I2S0_DIO2   39
#define AMEBA_I2S0_DIO3   40
#define AMEBA_I2S1_MCLK   41
#define AMEBA_I2S1_BCLK   42
#define AMEBA_I2S1_WS     43
#define AMEBA_I2S1_DIO0   44
#define AMEBA_I2S1_DIO1   45
#define AMEBA_I2S1_DIO2   46
#define AMEBA_I2S1_DIO3   47
#define AMEBA_I2C0_SCL    48
#define AMEBA_I2C0_SDA    49
#define AMEBA_I2C1_SCL    50
#define AMEBA_I2C1_SDA    51
#define AMEBA_PWM0        52
#define AMEBA_PWM1        53
#define AMEBA_PWM2        54
#define AMEBA_PWM3        55
#define AMEBA_PWM4        56
#define AMEBA_PWM5        57
#define AMEBA_PWM6        58
#define AMEBA_PWM7        59
#define AMEBA_BT_UART_TXD 60
#define AMEBA_BT_UART_RTS 61
#define AMEBA_DMIC_CLK    62
#define AMEBA_DMIC_DATA   63
#define AMEBA_IR_TX       64
#define AMEBA_IR_RX       65
#define AMEBA_KEY_ROW0    66
#define AMEBA_KEY_ROW1    67
#define AMEBA_KEY_ROW2    68
#define AMEBA_KEY_ROW3    69
#define AMEBA_KEY_ROW4    70
#define AMEBA_KEY_ROW5    71
#define AMEBA_KEY_ROW6    72
#define AMEBA_KEY_ROW7    73
#define AMEBA_KEY_COL0    74
#define AMEBA_KEY_COL1    75
#define AMEBA_KEY_COL2    76
#define AMEBA_KEY_COL3    77
#define AMEBA_KEY_COL4    78
#define AMEBA_KEY_COL5    79
#define AMEBA_KEY_COL6    80
#define AMEBA_KEY_COL7    81

/* Define pins number: bit[14:13] port, bit[12:8] pin, bit[7:0] function ID */
#define AMEBA_PORT_PIN(port, line)       ((((port) - 'A') << 5) + (line))
#define AMEBA_PINMUX(port, line, funcid) (((AMEBA_PORT_PIN(port, line)) << 8) | (funcid))

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBADPLUS_PINCTRL_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Realtek Semiconductor Corp.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 10 行

引脚复用功能定义（PINMUX Function definitions）。

### 注释 3：原第 97 行

引脚编号定义：`bit[14:13]` 为端口，`bit[12:8]` 为引脚，`bit[7:0]` 为功能标识符（Function ID）。

### 注释 4：原第 101 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_AMEBADPLUS_PINCTRL_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/amebadplus-pinctrl_8h.html)

---

[上一章](P003_amebad-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_arm-mps3-pinctrl.h_源码浏览.md)
