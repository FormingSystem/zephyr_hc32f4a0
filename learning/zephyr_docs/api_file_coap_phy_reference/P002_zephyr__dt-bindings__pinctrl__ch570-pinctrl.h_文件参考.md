---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-2
title: zephyr__dt-bindings__pinctrl__ch570-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ch570-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ch570-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WCH CH570/CH572片上系统（SoC；仅限这些型号）的引脚控制定义（Pinctrl Definitions）。

查看此文件的源码。

<a id="details"></a>

仅适用于 WCH CH570／CH572 片上系统（SoCs）的引脚控制（Pinctrl）定义。此头文件为 WCH CH570／CH572 提供引脚复用（Pin Multiplexing）定义。每个外设可使用多个复用功能（Alternate Functions，AFs）进行配置。引脚复用编码为 14 位值：位 `[0:3]` 为目标引脚号（0–11）；位 `[4:8]` 为引脚复用寄存器中外设重映射字段的偏移（0–16）；位 `[9:10]` 为该寄存器中复用功能字段的宽度（0–3 位）；位 `[11:13]` 为复用功能值（0–7）。引脚命名约定为 `{PERIPHERAL}_{FUNCTION}_{PIN}_{REMAP_NUMBER}`。例如，`UART_TXD_PA10_7` 表示 PA10 引脚上的 UART TXD 功能，使用重映射配置 7。注：某些功能没有重映射配置。为保持一致，仍定义一个宏，使其可在设备树中使用，例如配置内部上拉。当且仅当字段宽度为 0 且字段偏移为 16 时属于这种情况。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_a1d7fb03de4edbd52a4f3e404e410c473"></a>

```c
#define CH570_PINMUX_DEFINE(pin, peripheral, remapping)
```

相关声明：[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

编码引脚复用配置（Pinmux Configuration）。

<a id="define-members-0"></a>

### 引脚控制功能位域位置与掩码（Pinctrl pin functions bit field positions and masks.）

<a id="r_aa80767532c2208f691f38778e205ebad"></a>

```c
#define CH570_PINCTRL_PIN_NOT_DEFINED 0xF
```

相关声明：[CH570_PINCTRL_PIN_NOT_DEFINED](#aa80767532c2208f691f38778e205ebad)。

未定义的引脚（Not Defined Pin），表示无需进行任何配置。

<a id="r_a29afa7ec723d5e49c6039a151d3f1e82"></a>

```c
#define CH570_PINCTRL_UART_RXD 0
```

相关声明：[CH570_PINCTRL_UART_RXD](#a29afa7ec723d5e49c6039a151d3f1e82)。

`UART_RXD` 功能字段偏移（Function Field Offset）。

<a id="r_a252845c61515de6cbff25a10ab905621"></a>

```c
#define CH570_PINCTRL_UART_TXD 3
```

相关声明：[CH570_PINCTRL_UART_TXD](#a252845c61515de6cbff25a10ab905621)。

`UART_TXD` 功能字段偏移（Function Field Offset）。

<a id="r_af428cee20a80f02512e51ebba0477cb5"></a>

```c
#define CH570_PINCTRL_TMR 6
```

相关声明：[CH570_PINCTRL_TMR](#af428cee20a80f02512e51ebba0477cb5)。

`TMR` 功能字段偏移（Function Field Offset）。

<a id="r_a485e5a13d188f9d73d39a8183f258c05"></a>

```c
#define CH570_PINCTRL_SPI_CS 8
```

相关声明：[CH570_PINCTRL_SPI_CS](#a485e5a13d188f9d73d39a8183f258c05)。

`SPI_CS` 功能字段偏移（Function Field Offset）。

<a id="r_a141a359338bc2435b93bd1887aea8aa6"></a>

```c
#define CH570_PINCTRL_I2C_PIN 9
```

相关声明：[CH570_PINCTRL_I2C_PIN](#a141a359338bc2435b93bd1887aea8aa6)。

`I2C_PIN` 功能字段偏移（Function Field Offset）。

<a id="r_a206add68a2bdcfa5c828a4c798257ff0"></a>

```c
#define CH570_PINCTRL_SPI_CLK 11
```

相关声明：[CH570_PINCTRL_SPI_CLK](#a206add68a2bdcfa5c828a4c798257ff0)。

`SPI_CLK` 功能字段偏移（Function Field Offset）。

<a id="r_a5eda153a82edd2fb056ce5a3f016ea55"></a>

```c
#define CH570_PINCTRL_OSC_25M_ENABLE 12
```

相关声明：[CH570_PINCTRL_OSC_25M_ENABLE](#a5eda153a82edd2fb056ce5a3f016ea55)。

`OSC_25M_ENABLE` 功能字段偏移（Function Field Offset）。

<a id="r_a2c1e4ca59b24972132809acc6bf9b32f"></a>

```c
#define CH570_PINCTRL_NO_ALTERNATE 16
```

相关声明：[CH570_PINCTRL_NO_ALTERNATE](#a2c1e4ca59b24972132809acc6bf9b32f)。

无复用功能配置字段（No-Alternate Function Configuration Field）的偏移，必须为 16。

<a id="r_ad9335fe65b9c8e44ce3406010be1413d"></a>

```c
#define CH570_PINCTRL_UART_RXD_ALT_WIDTH 3
```

相关声明：[CH570_PINCTRL_UART_RXD_ALT_WIDTH](#ad9335fe65b9c8e44ce3406010be1413d)。

`UART_RXD` 复用功能字段宽度（Alternate Function Field Width），有 8 个重映射选项（Remap Options）。

<a id="r_a303d03d7710c28f7c3146bd7926cd904"></a>

```c
#define CH570_PINCTRL_UART_TXD_ALT_WIDTH 3
```

相关声明：[CH570_PINCTRL_UART_TXD_ALT_WIDTH](#a303d03d7710c28f7c3146bd7926cd904)。

`UART_TXD` 复用功能字段宽度（Alternate Function Field Width），有 8 个重映射选项（Remap Options）。

<a id="r_a54083faef197e4f4348b49ff79066f6b"></a>

```c
#define CH570_PINCTRL_TMR_ALT_WIDTH 2
```

相关声明：[CH570_PINCTRL_TMR_ALT_WIDTH](#a54083faef197e4f4348b49ff79066f6b)。

`TMR` 复用功能字段宽度（Alternate Function Field Width），有 4 个重映射选项（Remap Options）。

<a id="r_abc196d307f13f413528fb1f7a034e1d0"></a>

```c
#define CH570_PINCTRL_SPI_CS_ALT_WIDTH 1
```

相关声明：[CH570_PINCTRL_SPI_CS_ALT_WIDTH](#abc196d307f13f413528fb1f7a034e1d0)。

`SPI_CS` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="r_a63bf07387548b3044299e1183e7a6763"></a>

```c
#define CH570_PINCTRL_I2C_PIN_ALT_WIDTH 2
```

相关声明：[CH570_PINCTRL_I2C_PIN_ALT_WIDTH](#a63bf07387548b3044299e1183e7a6763)。

`I2C_PIN` 复用功能字段宽度（Alternate Function Field Width），有 4 个重映射选项（Remap Options）。

<a id="r_a5e25077724a7f450973d557a2129d90a"></a>

```c
#define CH570_PINCTRL_SPI_CLK_ALT_WIDTH 1
```

相关声明：[CH570_PINCTRL_SPI_CLK_ALT_WIDTH](#a5e25077724a7f450973d557a2129d90a)。

`SPI_CLK` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="r_a73b7fcb0cf0d61e3a03bc0e9202172d3"></a>

```c
#define CH570_PINCTRL_OSC_25M_ENABLE_ALT_WIDTH 1
```

相关声明：[CH570_PINCTRL_OSC_25M_ENABLE_ALT_WIDTH](#a73b7fcb0cf0d61e3a03bc0e9202172d3)。

`OSC_25M_ENABLE` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="r_aae31f07b5c28393a9cb1ae4fe557a6c5"></a>

```c
#define CH570_PINCTRL_NO_ALTERNATE_ALT_WIDTH 0
```

相关声明：[CH570_PINCTRL_NO_ALTERNATE_ALT_WIDTH](#aae31f07b5c28393a9cb1ae4fe557a6c5)。

无复用配置（No-Alternate Configuration）的宽度，必须严格为 0。

<a id="define-members-1"></a>

### 引脚复用编码位域定义（Pinmux encoding bit field definitions）

<a id="r_a04139b43b62feb1accffd36a3de52a18"></a>

```c
#define CH570_PINCTRL_PIN_SHIFT 0
```

相关声明：[CH570_PINCTRL_PIN_SHIFT](#a04139b43b62feb1accffd36a3de52a18)。

引脚复用编码值（Pinmux Encoded Value）中引脚号字段的位置。

<a id="r_af54f8ce5e139c0e30682a62743a91388"></a>

```c
#define CH570_PINCTRL_PIN_MASK GENMASK(3, 0)
```

相关声明：[CH570_PINCTRL_PIN_MASK](#af54f8ce5e139c0e30682a62743a91388)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

引脚复用编码值（Pinmux Encoded Value）中引脚号字段的掩码。

<a id="r_a8d35dc38eb90c9bc86bb7e24bc1518b7"></a>

```c
#define CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT 4
```

相关声明：[CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT](#a8d35dc38eb90c9bc86bb7e24bc1518b7)。

引脚复用编码值（Pinmux Encoded Value）中重映射偏移字段的位置。

<a id="r_a4d1d891a119b900bf3a5ef112a394968"></a>

```c
#define CH570_PINCTRL_ALT_FIELD_OFFSET_MASK GENMASK(8, 4)
```

相关声明：[CH570_PINCTRL_ALT_FIELD_OFFSET_MASK](#a4d1d891a119b900bf3a5ef112a394968)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

引脚复用编码值（Pinmux Encoded Value）中重映射偏移字段的掩码。

<a id="r_a0f0971917074fc391a3d0cd324cbc8a3"></a>

```c
#define CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT 9
```

相关声明：[CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT](#a0f0971917074fc391a3d0cd324cbc8a3)。

引脚复用编码值（Pinmux Encoded Value）中复用功能字段宽度的位置。

<a id="r_a6e7f463e26c7d84dc4b29b871ab0bb16"></a>

```c
#define CH570_PINCTRL_ALT_FIELD_WIDTH_MASK GENMASK(10, 9)
```

相关声明：[CH570_PINCTRL_ALT_FIELD_WIDTH_MASK](#a6e7f463e26c7d84dc4b29b871ab0bb16)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

引脚复用编码值（Pinmux Encoded Value）中复用功能字段宽度的掩码。

<a id="r_ab34e63823ea4d3af569b1048ba856c3d"></a>

```c
#define CH570_PINCTRL_ALT_FUNC_SHIFT 11
```

相关声明：[CH570_PINCTRL_ALT_FUNC_SHIFT](#ab34e63823ea4d3af569b1048ba856c3d)。

引脚复用编码值（Pinmux Encoded Value）中复用功能值的位置。

<a id="r_a63750c606883aaa8f0ff405abfdc6220"></a>

```c
#define CH570_PINCTRL_ALT_FUNC_MASK GENMASK(13, 11)
```

相关声明：[CH570_PINCTRL_ALT_FUNC_MASK](#a63750c606883aaa8f0ff405abfdc6220)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

引脚复用编码值（Pinmux Encoded Value）中复用功能值的掩码。

<a id="define-members-2"></a>

### 通用异步收发器（UART）

<a id="r_a6ab973f92bfaaa5030a09915470a3c12"></a>

```c
#define UART_TXD_PA3_0 CH570_PINMUX_DEFINE(3, UART_TXD, 0)
```

相关声明：[UART_TXD_PA3_0](#a6ab973f92bfaaa5030a09915470a3c12)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，无重映射（No Remap）。

<a id="r_a6602a9ab79d337744d6b48e281d20967"></a>

```c
#define UART_TXD_PA2_1 CH570_PINMUX_DEFINE(2, UART_TXD, 1)
```

相关声明：[UART_TXD_PA2_1](#a6602a9ab79d337744d6b48e281d20967)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 1）。

<a id="r_a7c836dadf9f4487a5aef4f3ed8e62bee"></a>

```c
#define UART_TXD_PA1_2 CH570_PINMUX_DEFINE(1, UART_TXD, 2)
```

相关声明：[UART_TXD_PA1_2](#a7c836dadf9f4487a5aef4f3ed8e62bee)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 2）。

<a id="r_a01513352b7e94e55ddaa9ce4f1abfc18"></a>

```c
#define UART_TXD_PA0_3 CH570_PINMUX_DEFINE(0, UART_TXD, 3)
```

相关声明：[UART_TXD_PA0_3](#a01513352b7e94e55ddaa9ce4f1abfc18)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 3）。

<a id="r_a3052a31fbcd7596c3e9d452141a4cf40"></a>

```c
#define UART_TXD_PA7_4 CH570_PINMUX_DEFINE(7, UART_TXD, 4)
```

相关声明：[UART_TXD_PA7_4](#a3052a31fbcd7596c3e9d452141a4cf40)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 4）。

<a id="r_a1f8f584e28dfcafacdc88aa586ed8ca8"></a>

```c
#define UART_TXD_PA8_5 CH570_PINMUX_DEFINE(8, UART_TXD, 5)
```

相关声明：[UART_TXD_PA8_5](#a1f8f584e28dfcafacdc88aa586ed8ca8)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 5）。

<a id="r_aee97aabbc54c073b4eea7b0417fc1567"></a>

```c
#define UART_TXD_PA11_6 CH570_PINMUX_DEFINE(11, UART_TXD, 6)
```

相关声明：[UART_TXD_PA11_6](#aee97aabbc54c073b4eea7b0417fc1567)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 6）。

<a id="r_a7b77cd376abe633deb3428dd3fd5c534"></a>

```c
#define UART_TXD_PA10_7 CH570_PINMUX_DEFINE(10, UART_TXD, 7)
```

相关声明：[UART_TXD_PA10_7](#a7b77cd376abe633deb3428dd3fd5c534)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART TXD，重映射（remap 7）。

<a id="r_a657a150a9970713d4c63a97c9afd00a1"></a>

```c
#define UART_RXD_PA2_0 CH570_PINMUX_DEFINE(2, UART_RXD, 0)
```

相关声明：[UART_RXD_PA2_0](#a657a150a9970713d4c63a97c9afd00a1)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，无重映射（No Remap）。

<a id="r_ac3084d96c355992a2c1fcdb05a8b6ad0"></a>

```c
#define UART_RXD_PA3_1 CH570_PINMUX_DEFINE(3, UART_RXD, 1)
```

相关声明：[UART_RXD_PA3_1](#ac3084d96c355992a2c1fcdb05a8b6ad0)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 1）。

<a id="r_a78c10a6630b3a61c1b37c10750178413"></a>

```c
#define UART_RXD_PA0_2 CH570_PINMUX_DEFINE(0, UART_RXD, 2)
```

相关声明：[UART_RXD_PA0_2](#a78c10a6630b3a61c1b37c10750178413)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 2）。

<a id="r_a93f41a7af7c53b62cef9f92ed49d681b"></a>

```c
#define UART_RXD_PA1_3 CH570_PINMUX_DEFINE(1, UART_RXD, 3)
```

相关声明：[UART_RXD_PA1_3](#a93f41a7af7c53b62cef9f92ed49d681b)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 3）。

<a id="r_a16036295764abf7558810a77459b3fd7"></a>

```c
#define UART_RXD_PA6_4 CH570_PINMUX_DEFINE(6, UART_RXD, 4)
```

相关声明：[UART_RXD_PA6_4](#a16036295764abf7558810a77459b3fd7)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 4）。

<a id="r_a406fb38af0e92d691e1a8309bcbd3d79"></a>

```c
#define UART_RXD_PA9_5 CH570_PINMUX_DEFINE(9, UART_RXD, 5)
```

相关声明：[UART_RXD_PA9_5](#a406fb38af0e92d691e1a8309bcbd3d79)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 5）。

<a id="r_a4e7149f9bdc2a1a3e04295106387d10e"></a>

```c
#define UART_RXD_PA10_6 CH570_PINMUX_DEFINE(10, UART_RXD, 6)
```

相关声明：[UART_RXD_PA10_6](#a4e7149f9bdc2a1a3e04295106387d10e)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 6）。

<a id="r_a5b6f75a2f41807832e6bb2f7a881f49b"></a>

```c
#define UART_RXD_PA11_7 CH570_PINMUX_DEFINE(11, UART_RXD, 7)
```

相关声明：[UART_RXD_PA11_7](#a5b6f75a2f41807832e6bb2f7a881f49b)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

UART RXD，重映射（remap 7）。

<a id="define-members-3"></a>

### 定时器：PWM0或双通道CAPIN（TIMER (PWM0 or CAPIN (2-channels))）

<a id="r_aca2cbf5aaa38936ddf7d320736b292be"></a>

```c
#define TMR_PWM0_CAPIN1_PA7_0 CH570_PINMUX_DEFINE(7, TMR, 0)
```

相关声明：[TMR_PWM0_CAPIN1_PA7_0](#aca2cbf5aaa38936ddf7d320736b292be)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第一路输入（第一捕获输入通道，First Capture Input Channel）或输出（PWM），无重映射（No Remap）。

<a id="r_a523df477b163f4a9397cf23de8dafe44"></a>

```c
#define TMR_PWM0_CAPIN1_PA2_1 CH570_PINMUX_DEFINE(2, TMR, 1)
```

相关声明：[TMR_PWM0_CAPIN1_PA2_1](#a523df477b163f4a9397cf23de8dafe44)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）1。

<a id="r_adc850da40d9647d26606517611b50623"></a>

```c
#define TMR_PWM0_CAPIN1_PA4_2 CH570_PINMUX_DEFINE(4, TMR, 2)
```

相关声明：[TMR_PWM0_CAPIN1_PA4_2](#adc850da40d9647d26606517611b50623)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）2。

<a id="r_ae81cc93cc761fb188563ee60063f45ad"></a>

```c
#define TMR_PWM0_CAPIN1_PA9_3 CH570_PINMUX_DEFINE(9, TMR, 3)
```

相关声明：[TMR_PWM0_CAPIN1_PA9_3](#ae81cc93cc761fb188563ee60063f45ad)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）3。

<a id="r_a019655e3262fcd1e86f8140c07aae74a"></a>

```c
#define TMR_CAPIN2_PA2_0 CH570_PINMUX_DEFINE(2, TMR, 0)
```

相关声明：[TMR_CAPIN2_PA2_0](#a019655e3262fcd1e86f8140c07aae74a)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第二捕获输入通道（Second Capture Input Channel），无重映射（No Remap）。

<a id="r_a1b96cea53357c1bec51921000d44154b"></a>

```c
#define TMR_CAPIN2_PA7_1 CH570_PINMUX_DEFINE(7, TMR, 1)
```

相关声明：[TMR_CAPIN2_PA7_1](#a1b96cea53357c1bec51921000d44154b)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）1。

<a id="r_a526a8697f94b93eb3a3d8b6250a45134"></a>

```c
#define TMR_CAPIN2_PA9_2 CH570_PINMUX_DEFINE(9, TMR, 2)
```

相关声明：[TMR_CAPIN2_PA9_2](#a526a8697f94b93eb3a3d8b6250a45134)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）2。

<a id="r_adf5d6376f1f7320526a8bd78afdb3035"></a>

```c
#define TMR_CAPIN2_PA4_3 CH570_PINMUX_DEFINE(4, TMR, 3)
```

相关声明：[TMR_CAPIN2_PA4_3](#adf5d6376f1f7320526a8bd78afdb3035)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）3。

<a id="define-members-4"></a>

### 串行外设接口（SPI）

<a id="r_add776992de806e7f35bbecdfbd9c6811"></a>

```c
#define SPI_CS_PA4_0 CH570_PINMUX_DEFINE(4, SPI_CS, 0)
```

相关声明：[SPI_CS_PA4_0](#add776992de806e7f35bbecdfbd9c6811)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_CS，无重映射（No Remap）。

<a id="r_aa5563c43bf1c2cd4b8ebaf6abeae080f"></a>

```c
#define SPI_CS_PA2_1 CH570_PINMUX_DEFINE(2, SPI_CS, 1)
```

相关声明：[SPI_CS_PA2_1](#aa5563c43bf1c2cd4b8ebaf6abeae080f)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_CS，重映射（remap）。

<a id="r_a7a36f1b26b6d9b96dbc915b2d3ef68d5"></a>

```c
#define SPI_CLK_PA5_0 CH570_PINMUX_DEFINE(5, SPI_CLK, 0)
```

相关声明：[SPI_CLK_PA5_0](#a7a36f1b26b6d9b96dbc915b2d3ef68d5)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_CLK，无重映射（No Remap）。

<a id="r_a88464db5d3b7f0d6c0a1426df10fb792"></a>

```c
#define SPI_CLK_PA3_1 CH570_PINMUX_DEFINE(3, SPI_CLK, 1)
```

相关声明：[SPI_CLK_PA3_1](#a88464db5d3b7f0d6c0a1426df10fb792)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_CLK，重映射（remap）。

<a id="r_a7e6b1697c20577d2bc56c6738c8427bc"></a>

```c
#define SPI_MOSI_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
```

相关声明：[SPI_MOSI_PA7_0](#a7e6b1697c20577d2bc56c6738c8427bc)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_MOSI，无重映射（No Remap）。

<a id="r_a4ab9e297ac4b68c5d04c832ebf29c0b4"></a>

```c
#define SPI_MISO_PA6_0 CH570_PINMUX_DEFINE(6, NO_ALTERNATE, 0)
```

相关声明：[SPI_MISO_PA6_0](#a4ab9e297ac4b68c5d04c832ebf29c0b4)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

SPI_MISO，无重映射（No Remap）。

<a id="define-members-5"></a>

### 集成电路间总线（I2C）

<a id="r_a353c690a2fd0c6e553b89349fd2f76c8"></a>

```c
#define I2C_SCL_PA8_0 CH570_PINMUX_DEFINE(8, I2C_PIN, 0)
```

相关声明：[I2C_SCL_PA8_0](#a353c690a2fd0c6e553b89349fd2f76c8)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SCL，无重映射（No Remap）。

<a id="r_a46cdf01500821e48723793f8e6068173"></a>

```c
#define I2C_SCL_PA0_1 CH570_PINMUX_DEFINE(0, I2C_PIN, 1)
```

相关声明：[I2C_SCL_PA0_1](#a46cdf01500821e48723793f8e6068173)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SCL，重映射（remap 1）。

<a id="r_aef03348c13c39818f61442552881de41"></a>

```c
#define I2C_SCL_PA3_2 CH570_PINMUX_DEFINE(3, I2C_PIN, 2)
```

相关声明：[I2C_SCL_PA3_2](#aef03348c13c39818f61442552881de41)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SCL，重映射（remap 2）。

<a id="r_abec182ccfa72601ff5a966d170ea4eb0"></a>

```c
#define I2C_SCL_PA5_3 CH570_PINMUX_DEFINE(5, I2C_PIN, 3)
```

相关声明：[I2C_SCL_PA5_3](#abec182ccfa72601ff5a966d170ea4eb0)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SCL，重映射（remap 3）。

<a id="r_a23111e0a90372a7a05f74432e59d2315"></a>

```c
#define I2C_SDA_PA9_0 CH570_PINMUX_DEFINE(9, I2C_PIN, 0)
```

相关声明：[I2C_SDA_PA9_0](#a23111e0a90372a7a05f74432e59d2315)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SDA，无重映射（No Remap）。

<a id="r_ad6d59409fb4d4c9104130949add95be0"></a>

```c
#define I2C_SDA_PA1_1 CH570_PINMUX_DEFINE(1, I2C_PIN, 1)
```

相关声明：[I2C_SDA_PA1_1](#ad6d59409fb4d4c9104130949add95be0)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SDA，重映射（remap 1）。

<a id="r_aef2c9347262574c84465a2c0ed916067"></a>

```c
#define I2C_SDA_PA2_2 CH570_PINMUX_DEFINE(2, I2C_PIN, 2)
```

相关声明：[I2C_SDA_PA2_2](#aef2c9347262574c84465a2c0ed916067)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SDA，重映射（remap 2）。

<a id="r_ab6178e93143f6c2700280b463337da0e"></a>

```c
#define I2C_SDA_PA6_3 CH570_PINMUX_DEFINE(6, I2C_PIN, 3)
```

相关声明：[I2C_SDA_PA6_3](#ab6178e93143f6c2700280b463337da0e)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

I2C_SDA，重映射（remap 3）。

<a id="define-members-6"></a>

### 按键扫描（Keyscan）

<a id="r_a8a6b729e4d7ef5cf90a94cf1979975c6"></a>

```c
#define KEYSCAN_0_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

相关声明：[KEYSCAN_0_PA2_0](#a8a6b729e4d7ef5cf90a94cf1979975c6)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

按键扫描输入（Keyscan Input）0，无复用功能（No Alternate Function）。

<a id="r_af7810e1a6d8b4ec428e57673abd1e7d4"></a>

```c
#define KEYSCAN_1_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

相关声明：[KEYSCAN_1_PA3_0](#af7810e1a6d8b4ec428e57673abd1e7d4)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

按键扫描输入（Keyscan Input）1，无复用功能（No Alternate Function）。

<a id="r_afdb48308cbd5599f319e531a747aa5ee"></a>

```c
#define KEYSCAN_2_PA8_0 CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)
```

相关声明：[KEYSCAN_2_PA8_0](#afdb48308cbd5599f319e531a747aa5ee)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

按键扫描输入（Keyscan Input）2，无复用功能（No Alternate Function）。

<a id="r_a2c4fe7f7d4087182380d9ae78dc3c7f8"></a>

```c
#define KEYSCAN_3_PA10_0 CH570_PINMUX_DEFINE(10, NO_ALTERNATE, 0)
```

相关声明：[KEYSCAN_3_PA10_0](#a2c4fe7f7d4087182380d9ae78dc3c7f8)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

按键扫描输入（Keyscan Input）3，无复用功能（No Alternate Function）。

<a id="r_a37a58eccca38edd8e1e9ad1474d33f78"></a>

```c
#define KEYSCAN_4_PA11_0 CH570_PINMUX_DEFINE(11, NO_ALTERNATE, 0)
```

相关声明：[KEYSCAN_4_PA11_0](#a37a58eccca38edd8e1e9ad1474d33f78)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

按键扫描输入（Keyscan Input）4，无复用功能（No Alternate Function）。

<a id="define-members-7"></a>

### 比较器（CMP）

<a id="r_abba3b251f2f8618fe3a5f95e4bfc19ef"></a>

```c
#define CMP_P_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

相关声明：[CMP_P_PA3_0](#abba3b251f2f8618fe3a5f95e4bfc19ef)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

比较器正输入（CMP Positive Input），无复用功能（No Alternate Function）。

<a id="r_a6e2f3b910df98ae7811ce0fa7d69cccd"></a>

```c
#define CMP_P_PA7_1 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 1)
```

相关声明：[CMP_P_PA7_1](#a6e2f3b910df98ae7811ce0fa7d69cccd)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

比较器正输入（CMP Positive Input），通过 CMP CTRL 寄存器选择 PA7。

<a id="r_a210060212b4046c428614e20ad790c86"></a>

```c
#define CMP_N_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

相关声明：[CMP_N_PA2_0](#a210060212b4046c428614e20ad790c86)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

比较器负输入（CMP Negative Input），无复用功能（No Alternate Function）。

<a id="r_a1f73e8d61725373a404b067dc8c7e9bd"></a>

```c
#define CMP_N_CMP_VREF_1 CH570_PINMUX_DEFINE(CH570_PINCTRL_PIN_NOT_DEFINED, NO_ALTERNATE, 1)
```

相关声明：[CMP_N_CMP_VREF_1](#a1f73e8d61725373a404b067dc8c7e9bd)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)、[CH570_PINCTRL_PIN_NOT_DEFINED](#aa80767532c2208f691f38778e205ebad)。

比较器负输入（CMP Negative Input），通过 CMP CTRL 寄存器选择内部参考电压（Internal Reference Voltage）。

<a id="define-members-8"></a>

### 脉宽调制（PWM）

<a id="r_a8ada56b37c41605b1d18563adb4cb9fa"></a>

```c
#define PWM1_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
```

相关声明：[PWM1_PA7_0](#a8ada56b37c41605b1d18563adb4cb9fa)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

PWM 输出（Output）1，无复用功能（No Alternate Function）。

<a id="r_afff97bcd53f2d34d4b9aa976242f4ccc"></a>

```c
#define PWM2_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

相关声明：[PWM2_PA2_0](#afff97bcd53f2d34d4b9aa976242f4ccc)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

PWM 输出（Output）2，无复用功能（No Alternate Function）。

<a id="r_a0d56f144184debd3aa2811190b5e7802"></a>

```c
#define PWM3_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

相关声明：[PWM3_PA3_0](#a0d56f144184debd3aa2811190b5e7802)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

PWM 输出（Output）3，无复用功能（No Alternate Function）。

<a id="r_aa0d627820e39744d3d1474e4a14cf76c"></a>

```c
#define PWM4_PA4_0 CH570_PINMUX_DEFINE(4, NO_ALTERNATE, 0)
```

相关声明：[PWM4_PA4_0](#aa0d627820e39744d3d1474e4a14cf76c)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

PWM 输出（Output）4，无复用功能（No Alternate Function）。

<a id="r_af06a1c9be9c915cc977b8be45428150b"></a>

```c
#define PWM5_PA8_0 CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)
```

相关声明：[PWM5_PA8_0](#af06a1c9be9c915cc977b8be45428150b)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

PWM 输出（Output）5，无复用功能（No Alternate Function）。

<a id="define-members-9"></a>

### 振荡器（OSC）

<a id="r_a6b11b51942d06618f8554d50127a2577"></a>

```c
#define OSC25M_ENABLE_PA4_0 CH570_PINMUX_DEFINE(4, OSC_25M_ENABLE, 1)
```

相关声明：[OSC25M_ENABLE_PA4_0](#a6b11b51942d06618f8554d50127a2577)、[CH570_PINMUX_DEFINE](#a1d7fb03de4edbd52a4f3e404e410c473)。

25 MHz 振荡器输出（Oscillator Output）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a4d1d891a119b900bf3a5ef112a394968"></a>

### `CH570_PINCTRL_ALT_FIELD_OFFSET_MASK`

```c
#define CH570_PINCTRL_ALT_FIELD_OFFSET_MASK GENMASK(8, 4)
```

引脚复用编码值（Pinmux Encoded Value）中重映射偏移字段的掩码。

<a id="a8d35dc38eb90c9bc86bb7e24bc1518b7"></a>

### `CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT`

```c
#define CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT 4
```

引脚复用编码值（Pinmux Encoded Value）中重映射偏移字段的位置。

<a id="a6e7f463e26c7d84dc4b29b871ab0bb16"></a>

### `CH570_PINCTRL_ALT_FIELD_WIDTH_MASK`

```c
#define CH570_PINCTRL_ALT_FIELD_WIDTH_MASK GENMASK(10, 9)
```

引脚复用编码值（Pinmux Encoded Value）中复用功能字段宽度的掩码。

<a id="a0f0971917074fc391a3d0cd324cbc8a3"></a>

### `CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT`

```c
#define CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT 9
```

引脚复用编码值（Pinmux Encoded Value）中复用功能字段宽度的位置。

<a id="a63750c606883aaa8f0ff405abfdc6220"></a>

### `CH570_PINCTRL_ALT_FUNC_MASK`

```c
#define CH570_PINCTRL_ALT_FUNC_MASK GENMASK(13, 11)
```

引脚复用编码值（Pinmux Encoded Value）中复用功能值的掩码。

<a id="ab34e63823ea4d3af569b1048ba856c3d"></a>

### `CH570_PINCTRL_ALT_FUNC_SHIFT`

```c
#define CH570_PINCTRL_ALT_FUNC_SHIFT 11
```

引脚复用编码值（Pinmux Encoded Value）中复用功能值的位置。

<a id="a141a359338bc2435b93bd1887aea8aa6"></a>

### `CH570_PINCTRL_I2C_PIN`

```c
#define CH570_PINCTRL_I2C_PIN 9
```

`I2C_PIN` 功能字段偏移（Function Field Offset）。

<a id="a63bf07387548b3044299e1183e7a6763"></a>

### `CH570_PINCTRL_I2C_PIN_ALT_WIDTH`

```c
#define CH570_PINCTRL_I2C_PIN_ALT_WIDTH 2
```

`I2C_PIN` 复用功能字段宽度（Alternate Function Field Width），有 4 个重映射选项（Remap Options）。

<a id="a2c1e4ca59b24972132809acc6bf9b32f"></a>

### `CH570_PINCTRL_NO_ALTERNATE`

```c
#define CH570_PINCTRL_NO_ALTERNATE 16
```

无复用功能配置字段（No-Alternate Function Configuration Field）的偏移，必须为 16。

<a id="aae31f07b5c28393a9cb1ae4fe557a6c5"></a>

### `CH570_PINCTRL_NO_ALTERNATE_ALT_WIDTH`

```c
#define CH570_PINCTRL_NO_ALTERNATE_ALT_WIDTH 0
```

无复用配置（No-Alternate Configuration）的宽度，必须严格为 0。

<a id="a5eda153a82edd2fb056ce5a3f016ea55"></a>

### `CH570_PINCTRL_OSC_25M_ENABLE`

```c
#define CH570_PINCTRL_OSC_25M_ENABLE 12
```

`OSC_25M_ENABLE` 功能字段偏移（Function Field Offset）。

<a id="a73b7fcb0cf0d61e3a03bc0e9202172d3"></a>

### `CH570_PINCTRL_OSC_25M_ENABLE_ALT_WIDTH`

```c
#define CH570_PINCTRL_OSC_25M_ENABLE_ALT_WIDTH 1
```

`OSC_25M_ENABLE` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="af54f8ce5e139c0e30682a62743a91388"></a>

### `CH570_PINCTRL_PIN_MASK`

```c
#define CH570_PINCTRL_PIN_MASK GENMASK(3, 0)
```

引脚复用编码值（Pinmux Encoded Value）中引脚号字段的掩码。

<a id="aa80767532c2208f691f38778e205ebad"></a>

### `CH570_PINCTRL_PIN_NOT_DEFINED`

```c
#define CH570_PINCTRL_PIN_NOT_DEFINED 0xF
```

未定义的引脚（Not Defined Pin），表示无需进行任何配置。

<a id="a04139b43b62feb1accffd36a3de52a18"></a>

### `CH570_PINCTRL_PIN_SHIFT`

```c
#define CH570_PINCTRL_PIN_SHIFT 0
```

引脚复用编码值（Pinmux Encoded Value）中引脚号字段的位置。

<a id="a206add68a2bdcfa5c828a4c798257ff0"></a>

### `CH570_PINCTRL_SPI_CLK`

```c
#define CH570_PINCTRL_SPI_CLK 11
```

`SPI_CLK` 功能字段偏移（Function Field Offset）。

<a id="a5e25077724a7f450973d557a2129d90a"></a>

### `CH570_PINCTRL_SPI_CLK_ALT_WIDTH`

```c
#define CH570_PINCTRL_SPI_CLK_ALT_WIDTH 1
```

`SPI_CLK` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="a485e5a13d188f9d73d39a8183f258c05"></a>

### `CH570_PINCTRL_SPI_CS`

```c
#define CH570_PINCTRL_SPI_CS 8
```

`SPI_CS` 功能字段偏移（Function Field Offset）。

<a id="abc196d307f13f413528fb1f7a034e1d0"></a>

### `CH570_PINCTRL_SPI_CS_ALT_WIDTH`

```c
#define CH570_PINCTRL_SPI_CS_ALT_WIDTH 1
```

`SPI_CS` 复用功能字段宽度（Alternate Function Field Width），有 2 个重映射选项（Remap Options）。

<a id="af428cee20a80f02512e51ebba0477cb5"></a>

### `CH570_PINCTRL_TMR`

```c
#define CH570_PINCTRL_TMR 6
```

`TMR` 功能字段偏移（Function Field Offset）。

<a id="a54083faef197e4f4348b49ff79066f6b"></a>

### `CH570_PINCTRL_TMR_ALT_WIDTH`

```c
#define CH570_PINCTRL_TMR_ALT_WIDTH 2
```

`TMR` 复用功能字段宽度（Alternate Function Field Width），有 4 个重映射选项（Remap Options）。

<a id="a29afa7ec723d5e49c6039a151d3f1e82"></a>

### `CH570_PINCTRL_UART_RXD`

```c
#define CH570_PINCTRL_UART_RXD 0
```

`UART_RXD` 功能字段偏移（Function Field Offset）。

<a id="ad9335fe65b9c8e44ce3406010be1413d"></a>

### `CH570_PINCTRL_UART_RXD_ALT_WIDTH`

```c
#define CH570_PINCTRL_UART_RXD_ALT_WIDTH 3
```

`UART_RXD` 复用功能字段宽度（Alternate Function Field Width），有 8 个重映射选项（Remap Options）。

<a id="a252845c61515de6cbff25a10ab905621"></a>

### `CH570_PINCTRL_UART_TXD`

```c
#define CH570_PINCTRL_UART_TXD 3
```

`UART_TXD` 功能字段偏移（Function Field Offset）。

<a id="a303d03d7710c28f7c3146bd7926cd904"></a>

### `CH570_PINCTRL_UART_TXD_ALT_WIDTH`

```c
#define CH570_PINCTRL_UART_TXD_ALT_WIDTH 3
```

`UART_TXD` 复用功能字段宽度（Alternate Function Field Width），有 8 个重映射选项（Remap Options）。

<a id="a1d7fb03de4edbd52a4f3e404e410c473"></a>

### `CH570_PINMUX_DEFINE`

```c
#define CH570_PINMUX_DEFINE ( pin, peripheral, remapping )
```

展开值（Value）：

```c
((pin << CH570_PINCTRL_PIN_SHIFT) |                                                        \
 (CH570_PINCTRL_##peripheral << CH570_PINCTRL_ALT_FIELD_OFFSET_SHIFT) |                    \
 (CH570_PINCTRL_##peripheral##_ALT_WIDTH << CH570_PINCTRL_ALT_FIELD_WIDTH_SHIFT) |         \
 (remapping << CH570_PINCTRL_ALT_FUNC_SHIFT))
```

编码引脚复用配置（Pinmux Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 引脚号（Pin Number），范围为 0–11。 |
| `peripheral` | 外设名称（Peripheral Name），例如 UART、TMR。必须与已定义的引脚复用宏（Pinmux Macros）匹配。 |
| `remapping` | 重映射配置编号（Remap Configuration Number），最大范围为 0–7。 |

**返回（Returns）**：返回值（Returns）：用于设备树（Devicetree）的已编码引脚复用值（Pinmux Value）。

<a id="a1f73e8d61725373a404b067dc8c7e9bd"></a>

### `CMP_N_CMP_VREF_1`

```c
#define CMP_N_CMP_VREF_1 CH570_PINMUX_DEFINE(CH570_PINCTRL_PIN_NOT_DEFINED, NO_ALTERNATE, 1)
```

比较器负输入（CMP Negative Input），通过 CMP CTRL 寄存器选择内部参考电压（Internal Reference Voltage）。

<a id="a210060212b4046c428614e20ad790c86"></a>

### `CMP_N_PA2_0`

```c
#define CMP_N_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

比较器负输入（CMP Negative Input），无复用功能（No Alternate Function）。

<a id="abba3b251f2f8618fe3a5f95e4bfc19ef"></a>

### `CMP_P_PA3_0`

```c
#define CMP_P_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

比较器正输入（CMP Positive Input），无复用功能（No Alternate Function）。

<a id="a6e2f3b910df98ae7811ce0fa7d69cccd"></a>

### `CMP_P_PA7_1`

```c
#define CMP_P_PA7_1 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 1)
```

比较器正输入（CMP Positive Input），通过 CMP CTRL 寄存器选择 PA7。

<a id="a46cdf01500821e48723793f8e6068173"></a>

### `I2C_SCL_PA0_1`

```c
#define I2C_SCL_PA0_1 CH570_PINMUX_DEFINE(0, I2C_PIN, 1)
```

I2C_SCL，重映射（remap 1）。

<a id="aef03348c13c39818f61442552881de41"></a>

### `I2C_SCL_PA3_2`

```c
#define I2C_SCL_PA3_2 CH570_PINMUX_DEFINE(3, I2C_PIN, 2)
```

I2C_SCL，重映射（remap 2）。

<a id="abec182ccfa72601ff5a966d170ea4eb0"></a>

### `I2C_SCL_PA5_3`

```c
#define I2C_SCL_PA5_3 CH570_PINMUX_DEFINE(5, I2C_PIN, 3)
```

I2C_SCL，重映射（remap 3）。

<a id="a353c690a2fd0c6e553b89349fd2f76c8"></a>

### `I2C_SCL_PA8_0`

```c
#define I2C_SCL_PA8_0 CH570_PINMUX_DEFINE(8, I2C_PIN, 0)
```

I2C_SCL，无重映射（No Remap）。

<a id="ad6d59409fb4d4c9104130949add95be0"></a>

### `I2C_SDA_PA1_1`

```c
#define I2C_SDA_PA1_1 CH570_PINMUX_DEFINE(1, I2C_PIN, 1)
```

I2C_SDA，重映射（remap 1）。

<a id="aef2c9347262574c84465a2c0ed916067"></a>

### `I2C_SDA_PA2_2`

```c
#define I2C_SDA_PA2_2 CH570_PINMUX_DEFINE(2, I2C_PIN, 2)
```

I2C_SDA，重映射（remap 2）。

<a id="ab6178e93143f6c2700280b463337da0e"></a>

### `I2C_SDA_PA6_3`

```c
#define I2C_SDA_PA6_3 CH570_PINMUX_DEFINE(6, I2C_PIN, 3)
```

I2C_SDA，重映射（remap 3）。

<a id="a23111e0a90372a7a05f74432e59d2315"></a>

### `I2C_SDA_PA9_0`

```c
#define I2C_SDA_PA9_0 CH570_PINMUX_DEFINE(9, I2C_PIN, 0)
```

I2C_SDA，无重映射（No Remap）。

<a id="a8a6b729e4d7ef5cf90a94cf1979975c6"></a>

### `KEYSCAN_0_PA2_0`

```c
#define KEYSCAN_0_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

按键扫描输入（Keyscan Input）0，无复用功能（No Alternate Function）。

<a id="af7810e1a6d8b4ec428e57673abd1e7d4"></a>

### `KEYSCAN_1_PA3_0`

```c
#define KEYSCAN_1_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

按键扫描输入（Keyscan Input）1，无复用功能（No Alternate Function）。

<a id="afdb48308cbd5599f319e531a747aa5ee"></a>

### `KEYSCAN_2_PA8_0`

```c
#define KEYSCAN_2_PA8_0 CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)
```

按键扫描输入（Keyscan Input）2，无复用功能（No Alternate Function）。

<a id="a2c4fe7f7d4087182380d9ae78dc3c7f8"></a>

### `KEYSCAN_3_PA10_0`

```c
#define KEYSCAN_3_PA10_0 CH570_PINMUX_DEFINE(10, NO_ALTERNATE, 0)
```

按键扫描输入（Keyscan Input）3，无复用功能（No Alternate Function）。

<a id="a37a58eccca38edd8e1e9ad1474d33f78"></a>

### `KEYSCAN_4_PA11_0`

```c
#define KEYSCAN_4_PA11_0 CH570_PINMUX_DEFINE(11, NO_ALTERNATE, 0)
```

按键扫描输入（Keyscan Input）4，无复用功能（No Alternate Function）。

<a id="a6b11b51942d06618f8554d50127a2577"></a>

### `OSC25M_ENABLE_PA4_0`

```c
#define OSC25M_ENABLE_PA4_0 CH570_PINMUX_DEFINE(4, OSC_25M_ENABLE, 1)
```

25 MHz 振荡器输出（Oscillator Output）。

<a id="a8ada56b37c41605b1d18563adb4cb9fa"></a>

### `PWM1_PA7_0`

```c
#define PWM1_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
```

PWM 输出（Output）1，无复用功能（No Alternate Function）。

<a id="afff97bcd53f2d34d4b9aa976242f4ccc"></a>

### `PWM2_PA2_0`

```c
#define PWM2_PA2_0 CH570_PINMUX_DEFINE(2, NO_ALTERNATE, 0)
```

PWM 输出（Output）2，无复用功能（No Alternate Function）。

<a id="a0d56f144184debd3aa2811190b5e7802"></a>

### `PWM3_PA3_0`

```c
#define PWM3_PA3_0 CH570_PINMUX_DEFINE(3, NO_ALTERNATE, 0)
```

PWM 输出（Output）3，无复用功能（No Alternate Function）。

<a id="aa0d627820e39744d3d1474e4a14cf76c"></a>

### `PWM4_PA4_0`

```c
#define PWM4_PA4_0 CH570_PINMUX_DEFINE(4, NO_ALTERNATE, 0)
```

PWM 输出（Output）4，无复用功能（No Alternate Function）。

<a id="af06a1c9be9c915cc977b8be45428150b"></a>

### `PWM5_PA8_0`

```c
#define PWM5_PA8_0 CH570_PINMUX_DEFINE(8, NO_ALTERNATE, 0)
```

PWM 输出（Output）5，无复用功能（No Alternate Function）。

<a id="a88464db5d3b7f0d6c0a1426df10fb792"></a>

### `SPI_CLK_PA3_1`

```c
#define SPI_CLK_PA3_1 CH570_PINMUX_DEFINE(3, SPI_CLK, 1)
```

SPI_CLK，重映射（remap）。

<a id="a7a36f1b26b6d9b96dbc915b2d3ef68d5"></a>

### `SPI_CLK_PA5_0`

```c
#define SPI_CLK_PA5_0 CH570_PINMUX_DEFINE(5, SPI_CLK, 0)
```

SPI_CLK，无重映射（No Remap）。

<a id="aa5563c43bf1c2cd4b8ebaf6abeae080f"></a>

### `SPI_CS_PA2_1`

```c
#define SPI_CS_PA2_1 CH570_PINMUX_DEFINE(2, SPI_CS, 1)
```

SPI_CS，重映射（remap）。

<a id="add776992de806e7f35bbecdfbd9c6811"></a>

### `SPI_CS_PA4_0`

```c
#define SPI_CS_PA4_0 CH570_PINMUX_DEFINE(4, SPI_CS, 0)
```

SPI_CS，无重映射（No Remap）。

<a id="a4ab9e297ac4b68c5d04c832ebf29c0b4"></a>

### `SPI_MISO_PA6_0`

```c
#define SPI_MISO_PA6_0 CH570_PINMUX_DEFINE(6, NO_ALTERNATE, 0)
```

SPI_MISO，无重映射（No Remap）。

<a id="a7e6b1697c20577d2bc56c6738c8427bc"></a>

### `SPI_MOSI_PA7_0`

```c
#define SPI_MOSI_PA7_0 CH570_PINMUX_DEFINE(7, NO_ALTERNATE, 0)
```

SPI_MOSI，无重映射（No Remap）。

<a id="a019655e3262fcd1e86f8140c07aae74a"></a>

### `TMR_CAPIN2_PA2_0`

```c
#define TMR_CAPIN2_PA2_0 CH570_PINMUX_DEFINE(2, TMR, 0)
```

TMR 第二捕获输入通道（Second Capture Input Channel），无重映射（No Remap）。

<a id="adf5d6376f1f7320526a8bd78afdb3035"></a>

### `TMR_CAPIN2_PA4_3`

```c
#define TMR_CAPIN2_PA4_3 CH570_PINMUX_DEFINE(4, TMR, 3)
```

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）3。

<a id="a1b96cea53357c1bec51921000d44154b"></a>

### `TMR_CAPIN2_PA7_1`

```c
#define TMR_CAPIN2_PA7_1 CH570_PINMUX_DEFINE(7, TMR, 1)
```

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）1。

<a id="a526a8697f94b93eb3a3d8b6250a45134"></a>

### `TMR_CAPIN2_PA9_2`

```c
#define TMR_CAPIN2_PA9_2 CH570_PINMUX_DEFINE(9, TMR, 2)
```

TMR 第二捕获输入通道（Second Capture Input Channel），重映射（Remap）2。

<a id="a523df477b163f4a9397cf23de8dafe44"></a>

### `TMR_PWM0_CAPIN1_PA2_1`

```c
#define TMR_PWM0_CAPIN1_PA2_1 CH570_PINMUX_DEFINE(2, TMR, 1)
```

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）1。

<a id="adc850da40d9647d26606517611b50623"></a>

### `TMR_PWM0_CAPIN1_PA4_2`

```c
#define TMR_PWM0_CAPIN1_PA4_2 CH570_PINMUX_DEFINE(4, TMR, 2)
```

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）2。

<a id="aca2cbf5aaa38936ddf7d320736b292be"></a>

### `TMR_PWM0_CAPIN1_PA7_0`

```c
#define TMR_PWM0_CAPIN1_PA7_0 CH570_PINMUX_DEFINE(7, TMR, 0)
```

TMR 第一路输入（第一捕获输入通道，First Capture Input Channel）或输出（PWM），无重映射（No Remap）。

<a id="ae81cc93cc761fb188563ee60063f45ad"></a>

### `TMR_PWM0_CAPIN1_PA9_3`

```c
#define TMR_PWM0_CAPIN1_PA9_3 CH570_PINMUX_DEFINE(9, TMR, 3)
```

TMR 第一路输入（捕获，Capture）或输出（TMR），重映射（Remap）3。

<a id="a78c10a6630b3a61c1b37c10750178413"></a>

### `UART_RXD_PA0_2`

```c
#define UART_RXD_PA0_2 CH570_PINMUX_DEFINE(0, UART_RXD, 2)
```

UART RXD，重映射（remap 2）。

<a id="a4e7149f9bdc2a1a3e04295106387d10e"></a>

### `UART_RXD_PA10_6`

```c
#define UART_RXD_PA10_6 CH570_PINMUX_DEFINE(10, UART_RXD, 6)
```

UART RXD，重映射（remap 6）。

<a id="a5b6f75a2f41807832e6bb2f7a881f49b"></a>

### `UART_RXD_PA11_7`

```c
#define UART_RXD_PA11_7 CH570_PINMUX_DEFINE(11, UART_RXD, 7)
```

UART RXD，重映射（remap 7）。

<a id="a93f41a7af7c53b62cef9f92ed49d681b"></a>

### `UART_RXD_PA1_3`

```c
#define UART_RXD_PA1_3 CH570_PINMUX_DEFINE(1, UART_RXD, 3)
```

UART RXD，重映射（remap 3）。

<a id="a657a150a9970713d4c63a97c9afd00a1"></a>

### `UART_RXD_PA2_0`

```c
#define UART_RXD_PA2_0 CH570_PINMUX_DEFINE(2, UART_RXD, 0)
```

UART RXD，无重映射（No Remap）。

<a id="ac3084d96c355992a2c1fcdb05a8b6ad0"></a>

### `UART_RXD_PA3_1`

```c
#define UART_RXD_PA3_1 CH570_PINMUX_DEFINE(3, UART_RXD, 1)
```

UART RXD，重映射（remap 1）。

<a id="a16036295764abf7558810a77459b3fd7"></a>

### `UART_RXD_PA6_4`

```c
#define UART_RXD_PA6_4 CH570_PINMUX_DEFINE(6, UART_RXD, 4)
```

UART RXD，重映射（remap 4）。

<a id="a406fb38af0e92d691e1a8309bcbd3d79"></a>

### `UART_RXD_PA9_5`

```c
#define UART_RXD_PA9_5 CH570_PINMUX_DEFINE(9, UART_RXD, 5)
```

UART RXD，重映射（remap 5）。

<a id="a01513352b7e94e55ddaa9ce4f1abfc18"></a>

### `UART_TXD_PA0_3`

```c
#define UART_TXD_PA0_3 CH570_PINMUX_DEFINE(0, UART_TXD, 3)
```

UART TXD，重映射（remap 3）。

<a id="a7b77cd376abe633deb3428dd3fd5c534"></a>

### `UART_TXD_PA10_7`

```c
#define UART_TXD_PA10_7 CH570_PINMUX_DEFINE(10, UART_TXD, 7)
```

UART TXD，重映射（remap 7）。

<a id="aee97aabbc54c073b4eea7b0417fc1567"></a>

### `UART_TXD_PA11_6`

```c
#define UART_TXD_PA11_6 CH570_PINMUX_DEFINE(11, UART_TXD, 6)
```

UART TXD，重映射（remap 6）。

<a id="a7c836dadf9f4487a5aef4f3ed8e62bee"></a>

### `UART_TXD_PA1_2`

```c
#define UART_TXD_PA1_2 CH570_PINMUX_DEFINE(1, UART_TXD, 2)
```

UART TXD，重映射（remap 2）。

<a id="a6602a9ab79d337744d6b48e281d20967"></a>

### `UART_TXD_PA2_1`

```c
#define UART_TXD_PA2_1 CH570_PINMUX_DEFINE(2, UART_TXD, 1)
```

UART TXD，重映射（remap 1）。

<a id="a6ab973f92bfaaa5030a09915470a3c12"></a>

### `UART_TXD_PA3_0`

```c
#define UART_TXD_PA3_0 CH570_PINMUX_DEFINE(3, UART_TXD, 0)
```

UART TXD，无重映射（No Remap）。

<a id="a3052a31fbcd7596c3e9d452141a4cf40"></a>

### `UART_TXD_PA7_4`

```c
#define UART_TXD_PA7_4 CH570_PINMUX_DEFINE(7, UART_TXD, 4)
```

UART TXD，重映射（remap 4）。

<a id="a1f8f584e28dfcafacdc88aa586ed8ca8"></a>

### `UART_TXD_PA8_5`

```c
#define UART_TXD_PA8_5 CH570_PINMUX_DEFINE(8, UART_TXD, 5)
```

UART TXD，重映射（remap 5）。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P013_ch570-pinctrl.h_源码浏览.md)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ach570-pinctrl_8h_html_a04139b43b62feb1accffd36a3de52a18"></a>
<a id="ach570-pinctrl_8h_html_a0f0971917074fc391a3d0cd324cbc8a3"></a>
<a id="ach570-pinctrl_8h_html_a8d35dc38eb90c9bc86bb7e24bc1518b7"></a>
<a id="ach570-pinctrl_8h_html_ab34e63823ea4d3af569b1048ba856c3d"></a>

---

[上一章](P001_zephyr__bluetooth__classic__avrcp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__net__coap.h_文件参考.md)
