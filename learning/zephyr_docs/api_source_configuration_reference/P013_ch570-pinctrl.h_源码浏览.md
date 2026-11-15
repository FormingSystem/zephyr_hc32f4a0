---
id: learning.zephyr-docs.api-source-configuration-reference.page-13
title: ch570-pinctrl.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ch570-pinctrl.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h.html)。

## 13.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00183"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00199"></a>
<a id="l00201"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00223"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00239"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00249"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00259"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>

```c
/*
 * SPDX-FileCopyrightText: 2026 SMILE (smile.eu)
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * NOTE: This pin controller configuration header supports WCH CH570/CH572 SoCs only.
 */


#ifndef ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH570_PINCTRL_H_
#define ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH570_PINCTRL_H_


#define CH570_PINCTRL_PIN_NOT_DEFINED 0xF

#define CH570_PINCTRL_UART_RXD       0
#define CH570_PINCTRL_UART_TXD       3
#define CH570_PINCTRL_TMR            6
#define CH570_PINCTRL_SPI_CS         8
#define CH570_PINCTRL_I2C_PIN        9
#define CH570_PINCTRL_SPI_CLK        11
#define CH570_PINCTRL_OSC_25M_ENABLE 12
#define CH570_PINCTRL_NO_ALTERNATE   16

#define CH570_PINCTRL_UART_RXD_ALT_WIDTH       3
#define CH570_PINCTRL_UART_TXD_ALT_WIDTH       3
#define CH570_PINCTRL_TMR_ALT_WIDTH            2
#define CH570_PINCTRL_SPI_CS_ALT_WIDTH         1
#define CH570_PINCTRL_I2C_PIN_ALT_WIDTH        2
#define CH570_PINCTRL_SPI_CLK_ALT_WIDTH        1
#define CH570_PINCTRL_OSC_25M_ENABLE_ALT_WIDTH 1
#define CH570_PINCTRL_NO_ALTERNATE_ALT_WIDTH   0



#define CH570_PINCTRL_PIN_SHIFT 0
#define CH570_PINCTRL_PIN_MASK  GENMASK(3, 0)

#define CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT 4
#define CH570_PINCTRL_ALT_FIELD_OFFSET_MASK  GENMASK(8, 4)

#define CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT 9
#define CH570_PINCTRL_ALT_FIELD_WIDTH_MASK  GENMASK(10, 9)

#define CH570_PINCTRL_ALT_FUNC_SHIFT 11
#define CH570_PINCTRL_ALT_FUNC_MASK  GENMASK(13, 11)


#define CH570_PINMUX_DEFINE(pin, peripheral, remapping)                                            \
        ((pin << CH570_PINCTRL_PIN_SHIFT) |                                                        \
         (CH570_PINCTRL_##peripheral << CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT) |                    \
         (CH570_PINCTRL_##peripheral##_ALT_WIDTH << CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT) |         \
         (remapping << CH570_PINCTRL_ALT_FUNC_SHIFT))

#define UART_TXD_PA3_0  CH570_PINMUX_DEFINE(3, UART_TXD, 0)
#define UART_TXD_PA2_1  CH570_PINMUX_DEFINE(2, UART_TXD, 1)
#define UART_TXD_PA1_2  CH570_PINMUX_DEFINE(1, UART_TXD, 2)
#define UART_TXD_PA0_3  CH570_PINMUX_DEFINE(0, UART_TXD, 3)
#define UART_TXD_PA7_4  CH570_PINMUX_DEFINE(7, UART_TXD, 4)
#define UART_TXD_PA8_5  CH570_PINMUX_DEFINE(8, UART_TXD, 5)
#define UART_TXD_PA11_6 CH570_PINMUX_DEFINE(11, UART_TXD, 6)
#define UART_TXD_PA10_7 CH570_PINMUX_DEFINE(10, UART_TXD, 7)

/*
 * Documentation is inconsistent for UART RXD_4. AF table lists UART RXD on PA4 (config 4),
 * while the pinout section shows PA6. PA6 is used in practice.
 */
#define UART_RXD_PA2_0  CH570_PINMUX_DEFINE(2, UART_RXD, 0)
#define UART_RXD_PA3_1  CH570_PINMUX_DEFINE(3, UART_RXD, 1)
#define UART_RXD_PA0_2  CH570_PINMUX_DEFINE(0, UART_RXD, 2)
#define UART_RXD_PA1_3  CH570_PINMUX_DEFINE(1, UART_RXD, 3)
#define UART_RXD_PA6_4  CH570_PINMUX_DEFINE(6, UART_RXD, 4)
#define UART_RXD_PA9_5  CH570_PINMUX_DEFINE(9, UART_RXD, 5)
#define UART_RXD_PA10_6 CH570_PINMUX_DEFINE(10, UART_RXD, 6)
#define UART_RXD_PA11_7 CH570_PINMUX_DEFINE(11, UART_RXD, 7)

#define TMR_PWM0_CAPIN1_PA7_0 CH570_PINMUX_DEFINE(7, TMR, 0)
#define TMR_PWM0_CAPIN1_PA2_1 CH570_PINMUX_DEFINE(2, TMR, 1)
#define TMR_PWM0_CAPIN1_PA4_2 CH570_PINMUX_DEFINE(4, TMR, 2)
#define TMR_PWM0_CAPIN1_PA9_3 CH570_PINMUX_DEFINE(9, TMR, 3)
#define TMR_CAPIN2_PA2_0      CH570_PINMUX_DEFINE(2, TMR, 0)
#define TMR_CAPIN2_PA7_1      CH570_PINMUX_DEFINE(7, TMR, 1)
#define TMR_CAPIN2_PA9_2      CH570_PINMUX_DEFINE(9, TMR, 2)
#define TMR_CAPIN2_PA4_3      CH570_PINMUX_DEFINE(4, TMR, 3)

#define SPI_CS_PA4_0   CH570_PINMUX_DEFINE(4, SPI_CS, 0)
#define SPI_CS_PA2_1   CH570_PINMUX_DEFINE(2, SPI_CS, 1)
#define SPI_CLK_PA5_0  CH570_PINMUX_DEFINE(5, SPI_CLK, 0)
#define SPI_CLK_PA3_1  CH570_PINMUX_DEFINE(3, SPI_CLK, 1)
#define SPI_MOSI_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
#define SPI_MISO_PA6_0 CH570_PINMUX_DEFINE(6, NO_ALTERNATE, 0)

#define I2C_SCL_PA8_0 CH570_PINMUX_DEFINE(8, I2C_PIN, 0)
#define I2C_SCL_PA0_1 CH570_PINMUX_DEFINE(0, I2C_PIN, 1)
#define I2C_SCL_PA3_2 CH570_PINMUX_DEFINE(3, I2C_PIN, 2)
#define I2C_SCL_PA5_3 CH570_PINMUX_DEFINE(5, I2C_PIN, 3)
#define I2C_SDA_PA9_0 CH570_PINMUX_DEFINE(9, I2C_PIN, 0)
#define I2C_SDA_PA1_1 CH570_PINMUX_DEFINE(1, I2C_PIN, 1)
#define I2C_SDA_PA2_2 CH570_PINMUX_DEFINE(2, I2C_PIN, 2)
#define I2C_SDA_PA6_3 CH570_PINMUX_DEFINE(6, I2C_PIN, 3)

#define KEYSCAN_0_PA2_0  CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
#define KEYSCAN_1_PA3_0  CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
#define KEYSCAN_2_PA8_0  CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)
#define KEYSCAN_3_PA10_0 CH570_PINMUX_DEFINE(10, NO_ALTERNATE, 0)
#define KEYSCAN_4_PA11_0 CH570_PINMUX_DEFINE(11, NO_ALTERNATE, 0)

#define CMP_P_PA3_0      CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
#define CMP_P_PA7_1      CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 1)
#define CMP_N_PA2_0      CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
#define CMP_N_CMP_VREF_1 CH570_PINMUX_DEFINE(CH570_PINCTRL_PIN_NOT_DEFINED, NO_ALTERNATE, 1)

#define PWM1_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
#define PWM2_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
#define PWM3_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
#define PWM4_PA4_0 CH570_PINMUX_DEFINE(4, NO_ALTERNATE, 0)
#define PWM5_PA8_0 CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)

#define OSC25M_ENABLE_PA4_0 CH570_PINMUX_DEFINE(4, OSC_25M_ENABLE, 1)

#endif /* ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH570_PINCTRL_H_ */
```

## 13.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 SMILE (smile.eu)。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

注意（NOTE）：此引脚控制器配置头文件只支持 WCH CH570/CH572 片上系统（SoC）。

### 注释 2：原第 140 行

文档对 `UART RXD_4` 的描述不一致。复用功能（AF）表将 UART RXD 列在 PA4（配置 4），而引脚分布章节显示为 PA6。实际使用 PA6。

### 注释 3：原第 278 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DT_BINDINGS_PINCTRL_CH570_PINCTRL_H_`。

## 13.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h.html)

---

[上一章](P012_ch32h41x-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P014_csip.h_源码浏览.md)
