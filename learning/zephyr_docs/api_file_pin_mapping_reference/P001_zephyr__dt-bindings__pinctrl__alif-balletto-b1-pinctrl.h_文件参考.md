---
id: learning.zephyr-docs.api-file-pin-mapping-reference.page-1
title: zephyr__dt-bindings__pinctrl__alif-balletto-b1-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-b1-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_alif-balletto-b1-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/alif-balletto-b1-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Alif Balletto B1系列的引脚控制定义（Pinctrl Definitions）。

查看此文件的源码。

<a id="details"></a>

Alif Balletto B1 系列的引脚控制（Pinctrl）定义。本头文件提供该系列的引脚复用（Pin Multiplexing）定义。每个引脚最多可以配置为 8 种不同功能，即 GPIO 加 7 种复用功能（Alternate Functions）。引脚复用编码（Pinmux Encoding）采用 11 位值：位 [0:2] 为复用功能，`0` 表示 GPIO，`1–7` 表示 AF1–AF7；位 [3:5] 为端口内的引脚编号，范围为 `0–7`；位 [6:10] 为端口编号，普通 GPIO 使用 `0–8`，LPGPIO 使用 `15`。引脚命名约定为 `PIN_P{port}_{pin}__{function}`。例如，`PIN_P0_0__UART0_RX_A` 表示端口 0、引脚 0、UART0 RX 功能（A 组）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ab0a2e9966868f5dcb365d5d533318a21"></a>

```c
#define ALIF_PINMUX(port, pin, func)
```

相关声明：[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

编码引脚复用配置（Pinmux Configuration）。

<a id="define-members-0"></a>

### 引脚复用编码位域定义（Pinmux encoding bit field definitions）

<a id="r_ab8529e7ad1002e2e112bf1286d4d6c62"></a>

```c
#define ALIF_PINMUX_FUNC_POS 0U
```

相关声明：[ALIF_PINMUX_FUNC_POS](#ab8529e7ad1002e2e112bf1286d4d6c62)。

复用功能（Alternate Function）字段的位位置。

<a id="r_a195b3893d9913e77419e111178923a3d"></a>

```c
#define ALIF_PINMUX_FUNC_MASK 0x7U
```

相关声明：[ALIF_PINMUX_FUNC_MASK](#a195b3893d9913e77419e111178923a3d)。

复用功能（Alternate Function）字段的位掩码，共 3 位。

<a id="r_a8c94e09e787a9fb1079e5fbe0aa875d2"></a>

```c
#define ALIF_PINMUX_PIN_POS 3U
```

相关声明：[ALIF_PINMUX_PIN_POS](#a8c94e09e787a9fb1079e5fbe0aa875d2)。

引脚编号（Pin Number）字段的位位置。

<a id="r_a723a8df1e91c947c25af42db8b9f73dd"></a>

```c
#define ALIF_PINMUX_PIN_MASK 0x7U
```

相关声明：[ALIF_PINMUX_PIN_MASK](#a723a8df1e91c947c25af42db8b9f73dd)。

引脚编号（Pin Number）字段的位掩码，共 3 位。

<a id="r_a5d3f4f922452dc948bcc7727d9875107"></a>

```c
#define ALIF_PINMUX_PORT_POS 6U
```

相关声明：[ALIF_PINMUX_PORT_POS](#a5d3f4f922452dc948bcc7727d9875107)。

端口编号（Port Number）字段的位位置。

<a id="r_a280dd67858770ceb0a88153aa29e09da"></a>

```c
#define ALIF_PINMUX_PORT_MASK 0x1FU
```

相关声明：[ALIF_PINMUX_PORT_MASK](#a280dd67858770ceb0a88153aa29e09da)。

端口编号（Port Number）字段的位掩码，共 5 位。

<a id="define-members-1"></a>

### 端口 0 的引脚定义（Port 0 Pin Definitions）

GPIO 端口（Port）0 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_a21c0982e31739a0e14d1d5bbe8d28e26"></a>

```c
#define PIN_P0_0__GPIO ALIF_PINMUX(0, 0, 0)
```

相关声明：[PIN_P0_0__GPIO](#a21c0982e31739a0e14d1d5bbe8d28e26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.0` 的复用功能（Alternate Functions）。

<a id="r_af61f7092241bffd1e1c72f4875753646"></a>

```c
#define PIN_P0_0__SEUART_RX_A ALIF_PINMUX(0, 0, 1)
```

相关声明：[PIN_P0_0__SEUART_RX_A](#af61f7092241bffd1e1c72f4875753646)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`SEUART_RX_A`。

<a id="r_a90cebb445be4e8ec705a6fec4f446849"></a>

```c
#define PIN_P0_0__UART0_RX_A ALIF_PINMUX(0, 0, 2)
```

相关声明：[PIN_P0_0__UART0_RX_A](#a90cebb445be4e8ec705a6fec4f446849)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`UART0_RX_A`。

<a id="r_aaec802e33197d50afe17f58f3614294b"></a>

```c
#define PIN_P0_0__LPI2S_SDI_A ALIF_PINMUX(0, 0, 3)
```

相关声明：[PIN_P0_0__LPI2S_SDI_A](#aaec802e33197d50afe17f58f3614294b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`LPI2S_SDI_A`。

<a id="r_aacbc860014b31389d2e1d19059020462"></a>

```c
#define PIN_P0_0__SPI0_SS0_A ALIF_PINMUX(0, 0, 4)
```

相关声明：[PIN_P0_0__SPI0_SS0_A](#aacbc860014b31389d2e1d19059020462)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`SPI0_SS0_A`。

<a id="r_ad83a764cf6e61171dcc56e6ad213e59e"></a>

```c
#define PIN_P0_0__LPI2C0_SCL_A ALIF_PINMUX(0, 0, 5)
```

相关声明：[PIN_P0_0__LPI2C0_SCL_A](#ad83a764cf6e61171dcc56e6ad213e59e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`LPI2C0_SCL_A`。

<a id="r_aa23df37079d3cb2dfc04e0712ea4b98d"></a>

```c
#define PIN_P0_0__ANA_S0 ALIF_PINMUX(0, 0, 6)
```

相关声明：[PIN_P0_0__ANA_S0](#aa23df37079d3cb2dfc04e0712ea4b98d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）0：`ANA_S0`。

<a id="r_a32eb0096f118eeaafa9f397de1d80611"></a>

```c
#define PIN_P0_1__GPIO ALIF_PINMUX(0, 1, 0)
```

相关声明：[PIN_P0_1__GPIO](#a32eb0096f118eeaafa9f397de1d80611)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.1` 的复用功能（Alternate Functions）。

<a id="r_ad2e9b4bc2f8fb875bbbaad78362bf3b2"></a>

```c
#define PIN_P0_1__SEUART_TX_A ALIF_PINMUX(0, 1, 1)
```

相关声明：[PIN_P0_1__SEUART_TX_A](#ad2e9b4bc2f8fb875bbbaad78362bf3b2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`SEUART_TX_A`。

<a id="r_ad3c6925fe9f38326a5750bfa5bfca6f1"></a>

```c
#define PIN_P0_1__UART0_TX_A ALIF_PINMUX(0, 1, 2)
```

相关声明：[PIN_P0_1__UART0_TX_A](#ad3c6925fe9f38326a5750bfa5bfca6f1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`UART0_TX_A`。

<a id="r_a4c5291503299cbd81d4337796735fd24"></a>

```c
#define PIN_P0_1__LPI2S_SDO_A ALIF_PINMUX(0, 1, 3)
```

相关声明：[PIN_P0_1__LPI2S_SDO_A](#a4c5291503299cbd81d4337796735fd24)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`LPI2S_SDO_A`。

<a id="r_a0db281f253dd9e245269cc4901347844"></a>

```c
#define PIN_P0_1__SPI0_SS1_A ALIF_PINMUX(0, 1, 4)
```

相关声明：[PIN_P0_1__SPI0_SS1_A](#a0db281f253dd9e245269cc4901347844)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`SPI0_SS1_A`。

<a id="r_a8a765220ea90dbdb4cf985be31b0a1a0"></a>

```c
#define PIN_P0_1__LPI2C0_SDA_A ALIF_PINMUX(0, 1, 5)
```

相关声明：[PIN_P0_1__LPI2C0_SDA_A](#a8a765220ea90dbdb4cf985be31b0a1a0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`LPI2C0_SDA_A`。

<a id="r_a9a7460d69ed218e8bfe8e5038ad27f92"></a>

```c
#define PIN_P0_1__ANA_S1 ALIF_PINMUX(0, 1, 6)
```

相关声明：[PIN_P0_1__ANA_S1](#a9a7460d69ed218e8bfe8e5038ad27f92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）1：`ANA_S1`。

<a id="r_a4fb3d6992e5eedb80cd18620d13aa3f4"></a>

```c
#define PIN_P0_2__GPIO ALIF_PINMUX(0, 2, 0)
```

相关声明：[PIN_P0_2__GPIO](#a4fb3d6992e5eedb80cd18620d13aa3f4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.2` 的复用功能（Alternate Functions）。

<a id="r_aea911d4031ea9ef5c6bfcb387ddfe716"></a>

```c
#define PIN_P0_2__JTAG1_TDI ALIF_PINMUX(0, 2, 1)
```

相关声明：[PIN_P0_2__JTAG1_TDI](#aea911d4031ea9ef5c6bfcb387ddfe716)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`JTAG1_TDI`。

<a id="r_a85030d71c6aedee18cb7f701432ecd9b"></a>

```c
#define PIN_P0_2__OSPI0_SS0_A ALIF_PINMUX(0, 2, 2)
```

相关声明：[PIN_P0_2__OSPI0_SS0_A](#a85030d71c6aedee18cb7f701432ecd9b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`OSPI0_SS0_A`。

<a id="r_a81dafa48db9962a46d804fe26b4d9aef"></a>

```c
#define PIN_P0_2__UART0_CTS_A ALIF_PINMUX(0, 2, 3)
```

相关声明：[PIN_P0_2__UART0_CTS_A](#a81dafa48db9962a46d804fe26b4d9aef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`UART0_CTS_A`。

<a id="r_a18c4cf23b00afd5dcd176295c5ff6ed9"></a>

```c
#define PIN_P0_2__LPI2S_SCLK_A ALIF_PINMUX(0, 2, 4)
```

相关声明：[PIN_P0_2__LPI2S_SCLK_A](#a18c4cf23b00afd5dcd176295c5ff6ed9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`LPI2S_SCLK_A`。

<a id="r_a631b7e7921b71f9b823bab70e3d4ab1d"></a>

```c
#define PIN_P0_2__SPI0_SS2_A ALIF_PINMUX(0, 2, 5)
```

相关声明：[PIN_P0_2__SPI0_SS2_A](#a631b7e7921b71f9b823bab70e3d4ab1d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`SPI0_SS2_A`。

<a id="r_a49b9fef54a6baea750aadaa5d80f8b59"></a>

```c
#define PIN_P0_2__ANA_S2 ALIF_PINMUX(0, 2, 6)
```

相关声明：[PIN_P0_2__ANA_S2](#a49b9fef54a6baea750aadaa5d80f8b59)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）2：`ANA_S2`。

<a id="r_af6db067634b65894a37a5edbe29654a5"></a>

```c
#define PIN_P0_3__GPIO ALIF_PINMUX(0, 3, 0)
```

相关声明：[PIN_P0_3__GPIO](#af6db067634b65894a37a5edbe29654a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.3` 的复用功能（Alternate Functions）。

<a id="r_aab83fe2126443e905a451effda41c154"></a>

```c
#define PIN_P0_3__JTAG1_TDO ALIF_PINMUX(0, 3, 1)
```

相关声明：[PIN_P0_3__JTAG1_TDO](#aab83fe2126443e905a451effda41c154)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`JTAG1_TDO`。

<a id="r_a2551a16bfe9f91ce64188d4bd78d5a92"></a>

```c
#define PIN_P0_3__OSPI0_SS1_A ALIF_PINMUX(0, 3, 2)
```

相关声明：[PIN_P0_3__OSPI0_SS1_A](#a2551a16bfe9f91ce64188d4bd78d5a92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`OSPI0_SS1_A`。

<a id="r_a37d3d9cde76c648ab549818678cdd02c"></a>

```c
#define PIN_P0_3__UART0_RTS_A ALIF_PINMUX(0, 3, 3)
```

相关声明：[PIN_P0_3__UART0_RTS_A](#a37d3d9cde76c648ab549818678cdd02c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`UART0_RTS_A`。

<a id="r_a9b8e5ae3f49eb1cf23c9b2ec0770636b"></a>

```c
#define PIN_P0_3__LPI2S_WS_A ALIF_PINMUX(0, 3, 4)
```

相关声明：[PIN_P0_3__LPI2S_WS_A](#a9b8e5ae3f49eb1cf23c9b2ec0770636b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`LPI2S_WS_A`。

<a id="r_a9fb13233a0bebf28a29ad65cb4975a70"></a>

```c
#define PIN_P0_3__SPI1_SS0_A ALIF_PINMUX(0, 3, 5)
```

相关声明：[PIN_P0_3__SPI1_SS0_A](#a9fb13233a0bebf28a29ad65cb4975a70)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`SPI1_SS0_A`。

<a id="r_acde8c916348493ac12ab8d892f4c4f5d"></a>

```c
#define PIN_P0_3__ANA_S3 ALIF_PINMUX(0, 3, 6)
```

相关声明：[PIN_P0_3__ANA_S3](#acde8c916348493ac12ab8d892f4c4f5d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）3：`ANA_S3`。

<a id="r_a068d5bd9723f62cb6aaa42fba90a9034"></a>

```c
#define PIN_P0_4__GPIO ALIF_PINMUX(0, 4, 0)
```

相关声明：[PIN_P0_4__GPIO](#a068d5bd9723f62cb6aaa42fba90a9034)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.4` 的复用功能（Alternate Functions）。

<a id="r_adacd1c63dc4eba3bd0c5d3795b9dbd4d"></a>

```c
#define PIN_P0_4__JTAG1_TRST ALIF_PINMUX(0, 4, 1)
```

相关声明：[PIN_P0_4__JTAG1_TRST](#adacd1c63dc4eba3bd0c5d3795b9dbd4d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`JTAG1_TRST`。

<a id="r_a86dde3f58b034c8276602748a76ca207"></a>

```c
#define PIN_P0_4__UART1_RX_A ALIF_PINMUX(0, 4, 2)
```

相关声明：[PIN_P0_4__UART1_RX_A](#a86dde3f58b034c8276602748a76ca207)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`UART1_RX_A`。

<a id="r_aa849bd3926156c6ac30b90b32eabfaad"></a>

```c
#define PIN_P0_4__SPI1_SS1_A ALIF_PINMUX(0, 4, 3)
```

相关声明：[PIN_P0_4__SPI1_SS1_A](#aa849bd3926156c6ac30b90b32eabfaad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`SPI1_SS1_A`。

<a id="r_a6cf94fa138887b35b52354bbbcfe26a2"></a>

```c
#define PIN_P0_4__I2C0_SDA_A ALIF_PINMUX(0, 4, 4)
```

相关声明：[PIN_P0_4__I2C0_SDA_A](#a6cf94fa138887b35b52354bbbcfe26a2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`I2C0_SDA_A`。

<a id="r_afb6485483deeafda4a21ed55c68491e3"></a>

```c
#define PIN_P0_4__FAULT0_A ALIF_PINMUX(0, 4, 5)
```

相关声明：[PIN_P0_4__FAULT0_A](#afb6485483deeafda4a21ed55c68491e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`FAULT0_A`。

<a id="r_aa132663d37ec856ce1cad081dbe0193e"></a>

```c
#define PIN_P0_4__ANA_S4 ALIF_PINMUX(0, 4, 6)
```

相关声明：[PIN_P0_4__ANA_S4](#aa132663d37ec856ce1cad081dbe0193e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）4：`ANA_S4`。

<a id="r_abd7d8c1f0be68ab38e7e4c7d62e8c88d"></a>

```c
#define PIN_P0_5__GPIO ALIF_PINMUX(0, 5, 0)
```

相关声明：[PIN_P0_5__GPIO](#abd7d8c1f0be68ab38e7e4c7d62e8c88d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.5` 的复用功能（Alternate Functions）。

<a id="r_a5294b8ee6a61abecc2b8e1a1cfb80668"></a>

```c
#define PIN_P0_5__JTAG1_TCK ALIF_PINMUX(0, 5, 1)
```

相关声明：[PIN_P0_5__JTAG1_TCK](#a5294b8ee6a61abecc2b8e1a1cfb80668)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`JTAG1_TCK`。

<a id="r_a4c0f43be2ca7617733c39d6956d0898c"></a>

```c
#define PIN_P0_5__UART1_TX_A ALIF_PINMUX(0, 5, 2)
```

相关声明：[PIN_P0_5__UART1_TX_A](#a4c0f43be2ca7617733c39d6956d0898c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`UART1_TX_A`。

<a id="r_a21264e6bc27ee7f361a46ac06658c721"></a>

```c
#define PIN_P0_5__SPI1_SS2_A ALIF_PINMUX(0, 5, 3)
```

相关声明：[PIN_P0_5__SPI1_SS2_A](#a21264e6bc27ee7f361a46ac06658c721)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`SPI1_SS2_A`。

<a id="r_a2c4aa8781e1a50243b5c0581bf0c0e0f"></a>

```c
#define PIN_P0_5__I2C0_SCL_A ALIF_PINMUX(0, 5, 4)
```

相关声明：[PIN_P0_5__I2C0_SCL_A](#a2c4aa8781e1a50243b5c0581bf0c0e0f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`I2C0_SCL_A`。

<a id="r_a3d0e9c04f7c008ae658cf87bdd691341"></a>

```c
#define PIN_P0_5__I3C_SCL_A ALIF_PINMUX(0, 5, 5)
```

相关声明：[PIN_P0_5__I3C_SCL_A](#a3d0e9c04f7c008ae658cf87bdd691341)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`I3C_SCL_A`。

<a id="r_adab066f4e9f8d2741b138fc08b513cf6"></a>

```c
#define PIN_P0_5__ANA_S5 ALIF_PINMUX(0, 5, 6)
```

相关声明：[PIN_P0_5__ANA_S5](#adab066f4e9f8d2741b138fc08b513cf6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）5：`ANA_S5`。

<a id="r_ad494beaa1230d6528f706e36a8f007cd"></a>

```c
#define PIN_P0_6__GPIO ALIF_PINMUX(0, 6, 0)
```

相关声明：[PIN_P0_6__GPIO](#ad494beaa1230d6528f706e36a8f007cd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.6` 的复用功能（Alternate Functions）。

<a id="r_aa24d097a966de41f5200b015d812cea3"></a>

```c
#define PIN_P0_6__JTAG1_TMS ALIF_PINMUX(0, 6, 1)
```

相关声明：[PIN_P0_6__JTAG1_TMS](#aa24d097a966de41f5200b015d812cea3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`JTAG1_TMS`。

<a id="r_a8d2cc812b823a3e6dfc06cb34e57a0aa"></a>

```c
#define PIN_P0_6__UART1_CTS_A ALIF_PINMUX(0, 6, 2)
```

相关声明：[PIN_P0_6__UART1_CTS_A](#a8d2cc812b823a3e6dfc06cb34e57a0aa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`UART1_CTS_A`。

<a id="r_a535db12aabf7cff50c012f39bb021101"></a>

```c
#define PIN_P0_6__I2C1_SDA_A ALIF_PINMUX(0, 6, 3)
```

相关声明：[PIN_P0_6__I2C1_SDA_A](#a535db12aabf7cff50c012f39bb021101)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`I2C1_SDA_A`。

<a id="r_a35d7d996009ded8b1f05a345b819e8ad"></a>

```c
#define PIN_P0_6__FAULT2_A ALIF_PINMUX(0, 6, 4)
```

相关声明：[PIN_P0_6__FAULT2_A](#a35d7d996009ded8b1f05a345b819e8ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`FAULT2_A`。

<a id="r_a790bf4cd500681d76b13722103f241ff"></a>

```c
#define PIN_P0_6__I3C_SDA_A ALIF_PINMUX(0, 6, 5)
```

相关声明：[PIN_P0_6__I3C_SDA_A](#a790bf4cd500681d76b13722103f241ff)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`I3C_SDA_A`。

<a id="r_aa5907af749639d7948c06be6af51c75e"></a>

```c
#define PIN_P0_6__ANA_S6 ALIF_PINMUX(0, 6, 6)
```

相关声明：[PIN_P0_6__ANA_S6](#aa5907af749639d7948c06be6af51c75e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）6：`ANA_S6`。

<a id="r_a3461a7c5af5e46d8e668e1e633c5d721"></a>

```c
#define PIN_P0_7__GPIO ALIF_PINMUX(0, 7, 0)
```

相关声明：[PIN_P0_7__GPIO](#a3461a7c5af5e46d8e668e1e633c5d721)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P0.7` 的复用功能（Alternate Functions）。

<a id="r_a8c262122844a7c5ff415d909d982a9b3"></a>

```c
#define PIN_P0_7__UART1_RTS_A ALIF_PINMUX(0, 7, 1)
```

相关声明：[PIN_P0_7__UART1_RTS_A](#a8c262122844a7c5ff415d909d982a9b3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`UART1_RTS_A`。

<a id="r_ad1dbe52190aa500b3ea50aa3bf4f5a36"></a>

```c
#define PIN_P0_7__I2C1_SCL_A ALIF_PINMUX(0, 7, 2)
```

相关声明：[PIN_P0_7__I2C1_SCL_A](#ad1dbe52190aa500b3ea50aa3bf4f5a36)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`I2C1_SCL_A`。

<a id="r_a37f70eb27978363bfa5ce7a1a06ff745"></a>

```c
#define PIN_P0_7__FAULT3_A ALIF_PINMUX(0, 7, 3)
```

相关声明：[PIN_P0_7__FAULT3_A](#a37f70eb27978363bfa5ce7a1a06ff745)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`FAULT3_A`。

<a id="r_acfeb79a95b8fe2cf9d04b0c28fa8f3c5"></a>

```c
#define PIN_P0_7__LPCAM_VSYNC_B ALIF_PINMUX(0, 7, 4)
```

相关声明：[PIN_P0_7__LPCAM_VSYNC_B](#acfeb79a95b8fe2cf9d04b0c28fa8f3c5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`LPCAM_VSYNC_B`。

<a id="r_a996b9421d83cdf9fc98ee86a07037882"></a>

```c
#define PIN_P0_7__ANA_S7 ALIF_PINMUX(0, 7, 6)
```

相关声明：[PIN_P0_7__ANA_S7](#a996b9421d83cdf9fc98ee86a07037882)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）0 的引脚（Pin）7：`ANA_S7`。

<a id="define-members-2"></a>

### 端口 1 的引脚定义（Port 1 Pin Definitions）

GPIO 端口（Port）1 的引脚复用定义（Pin Multiplexing Definitions）。

<a id="r_af59cc6b851070a403399aa14ec9522d5"></a>

```c
#define PIN_P1_0__GPIO ALIF_PINMUX(1, 0, 0)
```

相关声明：[PIN_P1_0__GPIO](#af59cc6b851070a403399aa14ec9522d5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.0` 的复用功能（Alternate Functions）。

<a id="r_a2c4a2a155ef84a5b8fd5bb2b4ada0429"></a>

```c
#define PIN_P1_0__OSPI0_D0_A ALIF_PINMUX(1, 0, 1)
```

相关声明：[PIN_P1_0__OSPI0_D0_A](#a2c4a2a155ef84a5b8fd5bb2b4ada0429)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="r_a86fd70e32e1fe8ef3ddb28394c1181b9"></a>

```c
#define PIN_P1_0__UART2_RX_A ALIF_PINMUX(1, 0, 2)
```

相关声明：[PIN_P1_0__UART2_RX_A](#a86fd70e32e1fe8ef3ddb28394c1181b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`UART2_RX_A`。

<a id="r_ace793548d3589296b9eda950d89a5329"></a>

```c
#define PIN_P1_0__LPPDM_D0_A ALIF_PINMUX(1, 0, 3)
```

相关声明：[PIN_P1_0__LPPDM_D0_A](#ace793548d3589296b9eda950d89a5329)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`LPPDM_D0_A`。

<a id="r_ad36a394ace52050ea666e8a4e49628b3"></a>

```c
#define PIN_P1_0__LPI2S_SDI_B ALIF_PINMUX(1, 0, 4)
```

相关声明：[PIN_P1_0__LPI2S_SDI_B](#ad36a394ace52050ea666e8a4e49628b3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`LPI2S_SDI_B`。

<a id="r_a1b162fa1d3aa4c3dd720b47331a07a43"></a>

```c
#define PIN_P1_0__SPI0_MISO_A ALIF_PINMUX(1, 0, 5)
```

相关声明：[PIN_P1_0__SPI0_MISO_A](#a1b162fa1d3aa4c3dd720b47331a07a43)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`SPI0_MISO_A`。

<a id="r_a9dbd3e87d6822b951f4f479014a0152e"></a>

```c
#define PIN_P1_0__LPCAM_D0_A ALIF_PINMUX(1, 0, 6)
```

相关声明：[PIN_P1_0__LPCAM_D0_A](#a9dbd3e87d6822b951f4f479014a0152e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="r_aa2f15500734f01ae94c048c566b2f3cf"></a>

```c
#define PIN_P1_0__SD_D0_A ALIF_PINMUX(1, 0, 7)
```

相关声明：[PIN_P1_0__SD_D0_A](#aa2f15500734f01ae94c048c566b2f3cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）0：`SD_D0_A`。

<a id="r_a5bde8570f8ee36a7dfa0e5d486dcb4d1"></a>

```c
#define PIN_P1_1__GPIO ALIF_PINMUX(1, 1, 0)
```

相关声明：[PIN_P1_1__GPIO](#a5bde8570f8ee36a7dfa0e5d486dcb4d1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.1` 的复用功能（Alternate Functions）。

<a id="r_a65def1cda3c68f532896b4fc9a47454c"></a>

```c
#define PIN_P1_1__OSPI0_D1_A ALIF_PINMUX(1, 1, 1)
```

相关声明：[PIN_P1_1__OSPI0_D1_A](#a65def1cda3c68f532896b4fc9a47454c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="r_ae31470618a41e1fa01512589fd7d454d"></a>

```c
#define PIN_P1_1__UART2_TX_A ALIF_PINMUX(1, 1, 2)
```

相关声明：[PIN_P1_1__UART2_TX_A](#ae31470618a41e1fa01512589fd7d454d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`UART2_TX_A`。

<a id="r_ae157fe998af3a929a8e9f572b0a842fd"></a>

```c
#define PIN_P1_1__LPPDM_C0_A ALIF_PINMUX(1, 1, 3)
```

相关声明：[PIN_P1_1__LPPDM_C0_A](#ae157fe998af3a929a8e9f572b0a842fd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`LPPDM_C0_A`。

<a id="r_ae9a5cdf32577a784e1ea21958a706c63"></a>

```c
#define PIN_P1_1__LPI2S_SDO_B ALIF_PINMUX(1, 1, 4)
```

相关声明：[PIN_P1_1__LPI2S_SDO_B](#ae9a5cdf32577a784e1ea21958a706c63)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`LPI2S_SDO_B`。

<a id="r_a37f579415afac4b490325552b9a90197"></a>

```c
#define PIN_P1_1__SPI0_MOSI_A ALIF_PINMUX(1, 1, 5)
```

相关声明：[PIN_P1_1__SPI0_MOSI_A](#a37f579415afac4b490325552b9a90197)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`SPI0_MOSI_A`。

<a id="r_abc5440c97b76369acb8c294e874d045f"></a>

```c
#define PIN_P1_1__LPCAM_D1_A ALIF_PINMUX(1, 1, 6)
```

相关声明：[PIN_P1_1__LPCAM_D1_A](#abc5440c97b76369acb8c294e874d045f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="r_a79fbe4374cc4d9ec5a943a874cd2ffdd"></a>

```c
#define PIN_P1_1__SD_D1_A ALIF_PINMUX(1, 1, 7)
```

相关声明：[PIN_P1_1__SD_D1_A](#a79fbe4374cc4d9ec5a943a874cd2ffdd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）1：`SD_D1_A`。

<a id="r_a6b0ea73c6cb252fda5ad10a28ceae4cf"></a>

```c
#define PIN_P1_2__GPIO ALIF_PINMUX(1, 2, 0)
```

相关声明：[PIN_P1_2__GPIO](#a6b0ea73c6cb252fda5ad10a28ceae4cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.2` 的复用功能（Alternate Functions）。

<a id="r_ad5ac88afcac7dfc33106a727e4337899"></a>

```c
#define PIN_P1_2__OSPI0_D2_A ALIF_PINMUX(1, 2, 1)
```

相关声明：[PIN_P1_2__OSPI0_D2_A](#ad5ac88afcac7dfc33106a727e4337899)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="r_acfa94e12c954bfef4f2f7a64a31e8157"></a>

```c
#define PIN_P1_2__LPPDM_D1_A ALIF_PINMUX(1, 2, 2)
```

相关声明：[PIN_P1_2__LPPDM_D1_A](#acfa94e12c954bfef4f2f7a64a31e8157)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`LPPDM_D1_A`。

<a id="r_a21780e98a55451b24b78cee13316750a"></a>

```c
#define PIN_P1_2__LPI2S_SCLK_B ALIF_PINMUX(1, 2, 3)
```

相关声明：[PIN_P1_2__LPI2S_SCLK_B](#a21780e98a55451b24b78cee13316750a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`LPI2S_SCLK_B`。

<a id="r_a80e2fc726f8004102da0cc8cf2acbaa3"></a>

```c
#define PIN_P1_2__SPI0_SCLK_A ALIF_PINMUX(1, 2, 4)
```

相关声明：[PIN_P1_2__SPI0_SCLK_A](#a80e2fc726f8004102da0cc8cf2acbaa3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`SPI0_SCLK_A`。

<a id="r_a64bd88e750072adce1beef23bc18d9c7"></a>

```c
#define PIN_P1_2__LPCAM_D2_A ALIF_PINMUX(1, 2, 5)
```

相关声明：[PIN_P1_2__LPCAM_D2_A](#a64bd88e750072adce1beef23bc18d9c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="r_a985eb14aa143e61b4f082b7fd01f45fa"></a>

```c
#define PIN_P1_2__SD_D2_A ALIF_PINMUX(1, 2, 6)
```

相关声明：[PIN_P1_2__SD_D2_A](#a985eb14aa143e61b4f082b7fd01f45fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`SD_D2_A`。

<a id="r_adba91c460bdb9baff03835112cae3258"></a>

```c
#define PIN_P1_2__CX_MWS_SF0 ALIF_PINMUX(1, 2, 7)
```

相关声明：[PIN_P1_2__CX_MWS_SF0](#adba91c460bdb9baff03835112cae3258)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）2：`CX_MWS_SF0`。

<a id="r_a7ff354be10a7bcfd9418e346c2f860e5"></a>

```c
#define PIN_P1_3__GPIO ALIF_PINMUX(1, 3, 0)
```

相关声明：[PIN_P1_3__GPIO](#a7ff354be10a7bcfd9418e346c2f860e5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.3` 的复用功能（Alternate Functions）。

<a id="r_a4986acb3712740cf61dfb50ababa692a"></a>

```c
#define PIN_P1_3__LPUART_RTS_A ALIF_PINMUX(1, 3, 1)
```

相关声明：[PIN_P1_3__LPUART_RTS_A](#a4986acb3712740cf61dfb50ababa692a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`LPUART_RTS_A`。

<a id="r_a5c5aedeee2a3e96123d9a07c43d1b2ee"></a>

```c
#define PIN_P1_3__LPPDM_C1_A ALIF_PINMUX(1, 3, 2)
```

相关声明：[PIN_P1_3__LPPDM_C1_A](#a5c5aedeee2a3e96123d9a07c43d1b2ee)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`LPPDM_C1_A`。

<a id="r_a7353a8c4b1709432b75cfb14da19094c"></a>

```c
#define PIN_P1_3__I2S1_SCLK_SLV_A ALIF_PINMUX(1, 3, 3)
```

相关声明：[PIN_P1_3__I2S1_SCLK_SLV_A](#a7353a8c4b1709432b75cfb14da19094c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`I2S1_SCLK_SLV_A`。

<a id="r_a0c0491e471c23646ec105c560b9d1bfd"></a>

```c
#define PIN_P1_3__LPSPI_MISO_A ALIF_PINMUX(1, 3, 4)
```

相关声明：[PIN_P1_3__LPSPI_MISO_A](#a0c0491e471c23646ec105c560b9d1bfd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`LPSPI_MISO_A`。

<a id="r_ade023cdbfea4810fa301e30db0e0f2c9"></a>

```c
#define PIN_P1_3__CAN1_RXD_A ALIF_PINMUX(1, 3, 5)
```

相关声明：[PIN_P1_3__CAN1_RXD_A](#ade023cdbfea4810fa301e30db0e0f2c9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`CAN1_RXD_A`。

<a id="r_a8d9249f611752c27fd8dde2e0c85ce97"></a>

```c
#define PIN_P1_3__CX_MWS_SF0 ALIF_PINMUX(1, 3, 6)
```

相关声明：[PIN_P1_3__CX_MWS_SF0](#a8d9249f611752c27fd8dde2e0c85ce97)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）3：`CX_MWS_SF0`。

<a id="r_ad1e50e7a0add033402abf705b503b80a"></a>

```c
#define PIN_P1_4__GPIO ALIF_PINMUX(1, 4, 0)
```

相关声明：[PIN_P1_4__GPIO](#ad1e50e7a0add033402abf705b503b80a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.4` 的复用功能（Alternate Functions）。

<a id="r_a852d85e129922cc715c7a856c2d363d3"></a>

```c
#define PIN_P1_4__LPPDM_C2_A ALIF_PINMUX(1, 4, 1)
```

相关声明：[PIN_P1_4__LPPDM_C2_A](#a852d85e129922cc715c7a856c2d363d3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`LPPDM_C2_A`。

<a id="r_a81cb8240e507cda646f00ff6d4dd613d"></a>

```c
#define PIN_P1_4__I2S0_SDI_A ALIF_PINMUX(1, 4, 2)
```

相关声明：[PIN_P1_4__I2S0_SDI_A](#a81cb8240e507cda646f00ff6d4dd613d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`I2S0_SDI_A`。

<a id="r_a5f628e7f376cba53188fcf6dc8e4baf8"></a>

```c
#define PIN_P1_4__LPSPI_MOSI_A ALIF_PINMUX(1, 4, 3)
```

相关声明：[PIN_P1_4__LPSPI_MOSI_A](#a5f628e7f376cba53188fcf6dc8e4baf8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`LPSPI_MOSI_A`。

<a id="r_af52e204fca8c22a5d8c4b5cac40d5d89"></a>

```c
#define PIN_P1_4__I2C1_SDA_A ALIF_PINMUX(1, 4, 4)
```

相关声明：[PIN_P1_4__I2C1_SDA_A](#af52e204fca8c22a5d8c4b5cac40d5d89)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`I2C1_SDA_A`。

<a id="r_a438b06a1a987884be2e8bbc6571c2259"></a>

```c
#define PIN_P1_4__CDC_PCLK_A ALIF_PINMUX(1, 4, 5)
```

相关声明：[PIN_P1_4__CDC_PCLK_A](#a438b06a1a987884be2e8bbc6571c2259)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`CDC_PCLK_A`。

<a id="r_aa4e2b2142b81fad286ff1a3ff1b5703c"></a>

```c
#define PIN_P1_4__CAN1_TXD_A ALIF_PINMUX(1, 4, 6)
```

相关声明：[PIN_P1_4__CAN1_TXD_A](#aa4e2b2142b81fad286ff1a3ff1b5703c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`CAN1_TXD_A`。

<a id="r_ac4da87f989323600b4a7be42e67d49bc"></a>

```c
#define PIN_P1_4__CX_MWS_SF1 ALIF_PINMUX(1, 4, 7)
```

相关声明：[PIN_P1_4__CX_MWS_SF1](#ac4da87f989323600b4a7be42e67d49bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）4：`CX_MWS_SF1`。

<a id="r_a0fb34153badcd47f16246988312d0275"></a>

```c
#define PIN_P1_5__GPIO ALIF_PINMUX(1, 5, 0)
```

相关声明：[PIN_P1_5__GPIO](#a0fb34153badcd47f16246988312d0275)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.5` 的复用功能（Alternate Functions）。

<a id="r_a09b45ab0a6289d6e7e69abbcb02aac2b"></a>

```c
#define PIN_P1_5__LPPDM_D2_A ALIF_PINMUX(1, 5, 1)
```

相关声明：[PIN_P1_5__LPPDM_D2_A](#a09b45ab0a6289d6e7e69abbcb02aac2b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`LPPDM_D2_A`。

<a id="r_a1d1d1469fccacc9a4d5fcc0580165aaf"></a>

```c
#define PIN_P1_5__I2S0_SDO_A ALIF_PINMUX(1, 5, 2)
```

相关声明：[PIN_P1_5__I2S0_SDO_A](#a1d1d1469fccacc9a4d5fcc0580165aaf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`I2S0_SDO_A`。

<a id="r_a0835421b3b50e0416131d4c063591950"></a>

```c
#define PIN_P1_5__LPSPI_SCLK_A ALIF_PINMUX(1, 5, 3)
```

相关声明：[PIN_P1_5__LPSPI_SCLK_A](#a0835421b3b50e0416131d4c063591950)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`LPSPI_SCLK_A`。

<a id="r_ad3a04ad686eb3f97794c20352361c85d"></a>

```c
#define PIN_P1_5__I2C1_SCLA_A ALIF_PINMUX(1, 5, 4)
```

相关声明：[PIN_P1_5__I2C1_SCLA_A](#ad3a04ad686eb3f97794c20352361c85d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`I2C1_SCLA_A`。

<a id="r_a09266ca5f3f0de6444564cb1c786fcd3"></a>

```c
#define PIN_P1_5__SD_RST_A ALIF_PINMUX(1, 5, 5)
```

相关声明：[PIN_P1_5__SD_RST_A](#a09266ca5f3f0de6444564cb1c786fcd3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`SD_RST_A`。

<a id="r_a32ed27284aad83f3b86e8fee897b06e9"></a>

```c
#define PIN_P1_5__CDC_DE_A ALIF_PINMUX(1, 5, 6)
```

相关声明：[PIN_P1_5__CDC_DE_A](#a32ed27284aad83f3b86e8fee897b06e9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`CDC_DE_A`。

<a id="r_ac4e9cd584cc68fed78dad46e1ea5c3b9"></a>

```c
#define PIN_P1_5__CAN1_STBY_A ALIF_PINMUX(1, 5, 7)
```

相关声明：[PIN_P1_5__CAN1_STBY_A](#ac4e9cd584cc68fed78dad46e1ea5c3b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）5：`CAN1_STBY_A`。

<a id="r_ab6f0917e71cae608320a3c16b8edf1bf"></a>

```c
#define PIN_P1_6__GPIO ALIF_PINMUX(1, 6, 0)
```

相关声明：[PIN_P1_6__GPIO](#ab6f0917e71cae608320a3c16b8edf1bf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.6` 的复用功能（Alternate Functions）。

<a id="r_ada7bb910d102350d9dcec48198720b93"></a>

```c
#define PIN_P1_6__UART2_RX_A ALIF_PINMUX(1, 6, 1)
```

相关声明：[PIN_P1_6__UART2_RX_A](#ada7bb910d102350d9dcec48198720b93)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`UART2_RX_A`。

<a id="r_a5b6b8967ed87f89d7d7b3c7b247d6089"></a>

```c
#define PIN_P1_6__LPPDM_C3_A ALIF_PINMUX(1, 6, 2)
```

相关声明：[PIN_P1_6__LPPDM_C3_A](#a5b6b8967ed87f89d7d7b3c7b247d6089)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`LPPDM_C3_A`。

<a id="r_a74039131f9d4e2d1940cfd8f743ce824"></a>

```c
#define PIN_P1_6__I2S0_SCLK_A ALIF_PINMUX(1, 6, 3)
```

相关声明：[PIN_P1_6__I2S0_SCLK_A](#a74039131f9d4e2d1940cfd8f743ce824)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`I2S0_SCLK_A`。

<a id="r_a54bfd633600c6cc06c628a18595ecb10"></a>

```c
#define PIN_P1_6__LPCAM_D6_A ALIF_PINMUX(1, 6, 4)
```

相关声明：[PIN_P1_6__LPCAM_D6_A](#a54bfd633600c6cc06c628a18595ecb10)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`LPCAM_D6_A`。

<a id="r_a4d1002ffd98e0b5c04bd77e809e92c64"></a>

```c
#define PIN_P1_6__CDC_HSYNC_A ALIF_PINMUX(1, 6, 5)
```

相关声明：[PIN_P1_6__CDC_HSYNC_A](#a4d1002ffd98e0b5c04bd77e809e92c64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`CDC_HSYNC_A`。

<a id="r_a77ea0ac3485787b2f624dc49ebe07df5"></a>

```c
#define PIN_P1_6__I3C_SDA_B ALIF_PINMUX(1, 6, 6)
```

相关声明：[PIN_P1_6__I3C_SDA_B](#a77ea0ac3485787b2f624dc49ebe07df5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`I3C_SDA_B`。

<a id="r_a1d24eb6e033eca4d0a11d005ece3355b"></a>

```c
#define PIN_P1_6__CX_MWS_SF2 ALIF_PINMUX(1, 6, 7)
```

相关声明：[PIN_P1_6__CX_MWS_SF2](#a1d24eb6e033eca4d0a11d005ece3355b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）6：`CX_MWS_SF2`。

<a id="r_a259e17b2ef415b6aed714af92b5f2ac5"></a>

```c
#define PIN_P1_7__GPIO ALIF_PINMUX(1, 7, 0)
```

相关声明：[PIN_P1_7__GPIO](#a259e17b2ef415b6aed714af92b5f2ac5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P1.7` 的复用功能（Alternate Functions）。

<a id="r_a6cd4b29c5faba814bac2a5e272c1b719"></a>

```c
#define PIN_P1_7__UART2_TX_A ALIF_PINMUX(1, 7, 1)
```

相关声明：[PIN_P1_7__UART2_TX_A](#a6cd4b29c5faba814bac2a5e272c1b719)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`UART2_TX_A`。

<a id="r_ae2a93374aabed0d707900021104cf17d"></a>

```c
#define PIN_P1_7__LPPDM_D3_A ALIF_PINMUX(1, 7, 2)
```

相关声明：[PIN_P1_7__LPPDM_D3_A](#ae2a93374aabed0d707900021104cf17d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`LPPDM_D3_A`。

<a id="r_ada7e1cdd706c29aaef13c58b96c7ac7f"></a>

```c
#define PIN_P1_7__I2S0_WS_A ALIF_PINMUX(1, 7, 3)
```

相关声明：[PIN_P1_7__I2S0_WS_A](#ada7e1cdd706c29aaef13c58b96c7ac7f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`I2S0_WS_A`。

<a id="r_aeff3a8f52d2d2f6ddad2722f39cde727"></a>

```c
#define PIN_P1_7__LPCAM_D7_A ALIF_PINMUX(1, 7, 4)
```

相关声明：[PIN_P1_7__LPCAM_D7_A](#aeff3a8f52d2d2f6ddad2722f39cde727)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`LPCAM_D7_A`。

<a id="r_a3b09ec5dce35b51c8246a5cf4093f30b"></a>

```c
#define PIN_P1_7__CDC_VSYNC_A ALIF_PINMUX(1, 7, 5)
```

相关声明：[PIN_P1_7__CDC_VSYNC_A](#a3b09ec5dce35b51c8246a5cf4093f30b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`CDC_VSYNC_A`。

<a id="r_a50b07141b78f1c3aacb82b36900d94ec"></a>

```c
#define PIN_P1_7__I3C_SCL_B ALIF_PINMUX(1, 7, 6)
```

相关声明：[PIN_P1_7__I3C_SCL_B](#a50b07141b78f1c3aacb82b36900d94ec)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`I3C_SCL_B`。

<a id="r_ae182eb7af40754e77554f22083efc6d0"></a>

```c
#define PIN_P1_7__CX_MWS_SF3 ALIF_PINMUX(1, 7, 7)
```

相关声明：[PIN_P1_7__CX_MWS_SF3](#ae182eb7af40754e77554f22083efc6d0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）1 的引脚（Pin）7：`CX_MWS_SF3`。

<a id="r_a2ed50f7f44d929b517287eaae4560f33"></a>

```c
#define PIN_P2_0__GPIO ALIF_PINMUX(2, 0, 0)
```

相关声明：[PIN_P2_0__GPIO](#a2ed50f7f44d929b517287eaae4560f33)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.0` 的复用功能（Alternate Functions）。

<a id="r_a72dae293916d95004e3ad6e2e085cb1a"></a>

```c
#define PIN_P2_0__OSPI0_SS0_B ALIF_PINMUX(2, 0, 1)
```

相关声明：[PIN_P2_0__OSPI0_SS0_B](#a72dae293916d95004e3ad6e2e085cb1a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`OSPI0_SS0_B`。

<a id="r_a88da704295f0daa28b21c529a1074282"></a>

```c
#define PIN_P2_0__LPUART_RX_A ALIF_PINMUX(2, 0, 2)
```

相关声明：[PIN_P2_0__LPUART_RX_A](#a88da704295f0daa28b21c529a1074282)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`LPUART_RX_A`。

<a id="r_a9f5ca61e4e7b13447adf7d83ebed0589"></a>

```c
#define PIN_P2_0__I2S1_SDI_A ALIF_PINMUX(2, 0, 3)
```

相关声明：[PIN_P2_0__I2S1_SDI_A](#a9f5ca61e4e7b13447adf7d83ebed0589)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`I2S1_SDI_A`。

<a id="r_aa161fedd1fad49b89f86f82349225e2e"></a>

```c
#define PIN_P2_0__LPSPI_SS_A ALIF_PINMUX(2, 0, 4)
```

相关声明：[PIN_P2_0__LPSPI_SS_A](#aa161fedd1fad49b89f86f82349225e2e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`LPSPI_SS_A`。

<a id="r_a9767a4cdb16cd471bff2d8f1df559606"></a>

```c
#define PIN_P2_0__LPCAM_HSYNC_B ALIF_PINMUX(2, 0, 5)
```

相关声明：[PIN_P2_0__LPCAM_HSYNC_B](#a9767a4cdb16cd471bff2d8f1df559606)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`LPCAM_HSYNC_B`。

<a id="r_a5a7560198d64f30347607f3b7417af66"></a>

```c
#define PIN_P2_0__ANA_S8 ALIF_PINMUX(2, 0, 6)
```

相关声明：[PIN_P2_0__ANA_S8](#a5a7560198d64f30347607f3b7417af66)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`ANA_S8`。

<a id="r_acb1cacef0c6d322a88b1e8da5dce8f14"></a>

```c
#define PIN_P2_0__CX_MWS_SF4 ALIF_PINMUX(2, 0, 7)
```

相关声明：[PIN_P2_0__CX_MWS_SF4](#acb1cacef0c6d322a88b1e8da5dce8f14)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）0：`CX_MWS_SF4`。

<a id="r_ac05af956aca2528e61e358c597c5b637"></a>

```c
#define PIN_P2_1__GPIO ALIF_PINMUX(2, 1, 0)
```

相关声明：[PIN_P2_1__GPIO](#ac05af956aca2528e61e358c597c5b637)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.1` 的复用功能（Alternate Functions）。

<a id="r_a18ca55a1ac5dbc69b5e53d51286c9e7c"></a>

```c
#define PIN_P2_1__OSPI0_SS1_B ALIF_PINMUX(2, 1, 1)
```

相关声明：[PIN_P2_1__OSPI0_SS1_B](#a18ca55a1ac5dbc69b5e53d51286c9e7c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`OSPI0_SS1_B`。

<a id="r_a68efa41efddb6154f6e67238caa96f55"></a>

```c
#define PIN_P2_1__LPUART_TX_A ALIF_PINMUX(2, 1, 2)
```

相关声明：[PIN_P2_1__LPUART_TX_A](#a68efa41efddb6154f6e67238caa96f55)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`LPUART_TX_A`。

<a id="r_a2fa94b5eaef2282dcb59990fadb88903"></a>

```c
#define PIN_P2_1__I2S1_SDO_A ALIF_PINMUX(2, 1, 3)
```

相关声明：[PIN_P2_1__I2S1_SDO_A](#a2fa94b5eaef2282dcb59990fadb88903)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`I2S1_SDO_A`。

<a id="r_abb84790ef7fdd51429b869c60b9cc84d"></a>

```c
#define PIN_P2_1__LPI2C0_SCL_B ALIF_PINMUX(2, 1, 4)
```

相关声明：[PIN_P2_1__LPI2C0_SCL_B](#abb84790ef7fdd51429b869c60b9cc84d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`LPI2C0_SCL_B`。

<a id="r_aab1b851c0104dc9889b0eb66fb6c155b"></a>

```c
#define PIN_P2_1__UT0_T1_A ALIF_PINMUX(2, 1, 5)
```

相关声明：[PIN_P2_1__UT0_T1_A](#aab1b851c0104dc9889b0eb66fb6c155b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`UT0_T1_A`。

<a id="r_a261a9f14d4c08b38619a1e92b9437b64"></a>

```c
#define PIN_P2_1__ANA_S9 ALIF_PINMUX(2, 1, 6)
```

相关声明：[PIN_P2_1__ANA_S9](#a261a9f14d4c08b38619a1e92b9437b64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`ANA_S9`。

<a id="r_a54e4d2487b39e439e14bf00259f9bfe0"></a>

```c
#define PIN_P2_1__CX_MWS_PAT0 ALIF_PINMUX(2, 1, 7)
```

相关声明：[PIN_P2_1__CX_MWS_PAT0](#a54e4d2487b39e439e14bf00259f9bfe0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）1：`CX_MWS_PAT0`。

<a id="r_a3fc212b07d980d4ae21a1743da443ac8"></a>

```c
#define PIN_P2_2__GPIO ALIF_PINMUX(2, 2, 0)
```

相关声明：[PIN_P2_2__GPIO](#a3fc212b07d980d4ae21a1743da443ac8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.2` 的复用功能（Alternate Functions）。

<a id="r_a70ba485bfc0e12dd07aa04ac6055df8f"></a>

```c
#define PIN_P2_2__LPUART_RTS_A ALIF_PINMUX(2, 2, 1)
```

相关声明：[PIN_P2_2__LPUART_RTS_A](#a70ba485bfc0e12dd07aa04ac6055df8f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`LPUART_RTS_A`。

<a id="r_a15ff3015d007e89490a604afe45ec84d"></a>

```c
#define PIN_P2_2__I2S1_SCLK_SLV_A ALIF_PINMUX(2, 2, 2)
```

相关声明：[PIN_P2_2__I2S1_SCLK_SLV_A](#a15ff3015d007e89490a604afe45ec84d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`I2S1_SCLK_SLV_A`。

<a id="r_afb814e15c86aa147acff7e4b06313bdc"></a>

```c
#define PIN_P2_2__LPI2C0_SDA_B ALIF_PINMUX(2, 2, 3)
```

相关声明：[PIN_P2_2__LPI2C0_SDA_B](#afb814e15c86aa147acff7e4b06313bdc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`LPI2C0_SDA_B`。

<a id="r_a55c235d4c2f152461414381ca914187e"></a>

```c
#define PIN_P2_2__UT1_T0_A ALIF_PINMUX(2, 2, 4)
```

相关声明：[PIN_P2_2__UT1_T0_A](#a55c235d4c2f152461414381ca914187e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`UT1_T0_A`。

<a id="r_abc41608c0c3830bca1c4d1b13bdf5691"></a>

```c
#define PIN_P2_2__ANA_S10 ALIF_PINMUX(2, 2, 5)
```

相关声明：[PIN_P2_2__ANA_S10](#abc41608c0c3830bca1c4d1b13bdf5691)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`ANA_S10`。

<a id="r_ac9e833de34324c123cb33ae8e57cad21"></a>

```c
#define PIN_P2_2__CX_MWS_PAT1 ALIF_PINMUX(2, 2, 6)
```

相关声明：[PIN_P2_2__CX_MWS_PAT1](#ac9e833de34324c123cb33ae8e57cad21)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）2：`CX_MWS_PAT1`。

<a id="r_a8408f18132258a0ef9fb8c3fe4f33977"></a>

```c
#define PIN_P2_3__GPIO ALIF_PINMUX(2, 3, 0)
```

相关声明：[PIN_P2_3__GPIO](#a8408f18132258a0ef9fb8c3fe4f33977)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.3` 的复用功能（Alternate Functions）。

<a id="r_ab0a7d39ed08e3175c520c240de446a01"></a>

```c
#define PIN_P2_3__LPUART_CTS_A ALIF_PINMUX(2, 3, 1)
```

相关声明：[PIN_P2_3__LPUART_CTS_A](#ab0a7d39ed08e3175c520c240de446a01)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`LPUART_CTS_A`。

<a id="r_a78aa0182ca489e9b3f11b1c247552228"></a>

```c
#define PIN_P2_3__I2S1_WS_SLV_A ALIF_PINMUX(2, 3, 2)
```

相关声明：[PIN_P2_3__I2S1_WS_SLV_A](#a78aa0182ca489e9b3f11b1c247552228)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`I2S1_WS_SLV_A`。

<a id="r_a16fe807eaee34126a00a11ba747e113e"></a>

```c
#define PIN_P2_3__UT1_T1_A ALIF_PINMUX(2, 3, 3)
```

相关声明：[PIN_P2_3__UT1_T1_A](#a16fe807eaee34126a00a11ba747e113e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`UT1_T1_A`。

<a id="r_a410ee38ad792684ccd0f00e8a0c0f62f"></a>

```c
#define PIN_P2_3__SD_RST_A ALIF_PINMUX(2, 3, 4)
```

相关声明：[PIN_P2_3__SD_RST_A](#a410ee38ad792684ccd0f00e8a0c0f62f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`SD_RST_A`。

<a id="r_a2819bc2ec4b910739f12065b99efe98d"></a>

```c
#define PIN_P2_3__CAN0_RXD_A ALIF_PINMUX(2, 3, 5)
```

相关声明：[PIN_P2_3__CAN0_RXD_A](#a2819bc2ec4b910739f12065b99efe98d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`CAN0_RXD_A`。

<a id="r_a72c628f0e6dc25e0816a40e3ca252f30"></a>

```c
#define PIN_P2_3__ANA_S11 ALIF_PINMUX(2, 3, 6)
```

相关声明：[PIN_P2_3__ANA_S11](#a72c628f0e6dc25e0816a40e3ca252f30)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`ANA_S11`。

<a id="r_af99be1d667e2c817c3007c11c5ca2d49"></a>

```c
#define PIN_P2_3__CX_MWS_SYNC ALIF_PINMUX(2, 3, 7)
```

相关声明：[PIN_P2_3__CX_MWS_SYNC](#af99be1d667e2c817c3007c11c5ca2d49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）3：`CX_MWS_SYNC`。

<a id="r_a649d4dc937e3cb6269408b128ed3aae3"></a>

```c
#define PIN_P2_4__GPIO ALIF_PINMUX(2, 4, 0)
```

相关声明：[PIN_P2_4__GPIO](#a649d4dc937e3cb6269408b128ed3aae3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.4` 的复用功能（Alternate Functions）。

<a id="r_ad87b8ed21814361c00b172b73afd49d1"></a>

```c
#define PIN_P2_4__UART3_RX_A ALIF_PINMUX(2, 4, 1)
```

相关声明：[PIN_P2_4__UART3_RX_A](#ad87b8ed21814361c00b172b73afd49d1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`UART3_RX_A`。

<a id="r_a021d984d183324f18d2b63cffae1f918"></a>

```c
#define PIN_P2_4__I2S0_SDI_B ALIF_PINMUX(2, 4, 2)
```

相关声明：[PIN_P2_4__I2S0_SDI_B](#a021d984d183324f18d2b63cffae1f918)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`I2S0_SDI_B`。

<a id="r_aea227c4b940cdfdbbb491fef80270cab"></a>

```c
#define PIN_P2_4__I2C0_SCL_B ALIF_PINMUX(2, 4, 3)
```

相关声明：[PIN_P2_4__I2C0_SCL_B](#aea227c4b940cdfdbbb491fef80270cab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`I2C0_SCL_B`。

<a id="r_a595a81d1d4a9e4f93d13049d0a966915"></a>

```c
#define PIN_P2_4__UT2_T0_A ALIF_PINMUX(2, 4, 4)
```

相关声明：[PIN_P2_4__UT2_T0_A](#a595a81d1d4a9e4f93d13049d0a966915)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`UT2_T0_A`。

<a id="r_acbcc2a9351cb7eac4c28833e9f725677"></a>

```c
#define PIN_P2_4__CAN0_TXD_A ALIF_PINMUX(2, 4, 5)
```

相关声明：[PIN_P2_4__CAN0_TXD_A](#acbcc2a9351cb7eac4c28833e9f725677)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`CAN0_TXD_A`。

<a id="r_a5ad9a9c92200896609d122bb0e81e8a0"></a>

```c
#define PIN_P2_4__ANA_S12 ALIF_PINMUX(2, 4, 6)
```

相关声明：[PIN_P2_4__ANA_S12](#a5ad9a9c92200896609d122bb0e81e8a0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`ANA_S12`。

<a id="r_ae365e707419062f080c974aecfe0e9e0"></a>

```c
#define PIN_P2_4__CX_MWS_TX ALIF_PINMUX(2, 4, 7)
```

相关声明：[PIN_P2_4__CX_MWS_TX](#ae365e707419062f080c974aecfe0e9e0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）4：`CX_MWS_TX`。

<a id="r_ac399d584c2f7dbdf0a2ceeb91a9a9ea0"></a>

```c
#define PIN_P2_5__GPIO ALIF_PINMUX(2, 5, 0)
```

相关声明：[PIN_P2_5__GPIO](#ac399d584c2f7dbdf0a2ceeb91a9a9ea0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.5` 的复用功能（Alternate Functions）。

<a id="r_a32cdfdf070321c2dc45b600554935d1c"></a>

```c
#define PIN_P2_5__UART3_TX_A ALIF_PINMUX(2, 5, 1)
```

相关声明：[PIN_P2_5__UART3_TX_A](#a32cdfdf070321c2dc45b600554935d1c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`UART3_TX_A`。

<a id="r_a960479f610500a14c90ad06af4046d4b"></a>

```c
#define PIN_P2_5__I2S0_SDO_B ALIF_PINMUX(2, 5, 2)
```

相关声明：[PIN_P2_5__I2S0_SDO_B](#a960479f610500a14c90ad06af4046d4b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`I2S0_SDO_B`。

<a id="r_a163ef064afe3540c8f61091a69781b4b"></a>

```c
#define PIN_P2_5__I2C0_SDA_B ALIF_PINMUX(2, 5, 3)
```

相关声明：[PIN_P2_5__I2C0_SDA_B](#a163ef064afe3540c8f61091a69781b4b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`I2C0_SDA_B`。

<a id="r_a6f783a7eeaae764b087000d898124f45"></a>

```c
#define PIN_P2_5__UT2_T1_A ALIF_PINMUX(2, 5, 4)
```

相关声明：[PIN_P2_5__UT2_T1_A](#a6f783a7eeaae764b087000d898124f45)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`UT2_T1_A`。

<a id="r_af21c79f39e818aba2dd8185b31d61987"></a>

```c
#define PIN_P2_5__CAN0_STBY_A ALIF_PINMUX(2, 5, 5)
```

相关声明：[PIN_P2_5__CAN0_STBY_A](#af21c79f39e818aba2dd8185b31d61987)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`CAN0_STBY_A`。

<a id="r_a9e1eb637336aa83aa460dd7e14ecd6bf"></a>

```c
#define PIN_P2_5__ANA_S13 ALIF_PINMUX(2, 5, 6)
```

相关声明：[PIN_P2_5__ANA_S13](#a9e1eb637336aa83aa460dd7e14ecd6bf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`ANA_S13`。

<a id="r_a53a063c6f4fe109d49a011f4f2e50d19"></a>

```c
#define PIN_P2_5__CX_MWS_RX ALIF_PINMUX(2, 5, 7)
```

相关声明：[PIN_P2_5__CX_MWS_RX](#a53a063c6f4fe109d49a011f4f2e50d19)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）5：`CX_MWS_RX`。

<a id="r_acf70da7d084f17a152af48ea6ef34527"></a>

```c
#define PIN_P2_6__GPIO ALIF_PINMUX(2, 6, 0)
```

相关声明：[PIN_P2_6__GPIO](#acf70da7d084f17a152af48ea6ef34527)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.6` 的复用功能（Alternate Functions）。

<a id="r_ad89370bf62edbef192a85783afd63b3e"></a>

```c
#define PIN_P2_6__UART4_RX_A ALIF_PINMUX(2, 6, 1)
```

相关声明：[PIN_P2_6__UART4_RX_A](#ad89370bf62edbef192a85783afd63b3e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`UART4_RX_A`。

<a id="r_ab7b482cc545e06022c8549c62a5796d7"></a>

```c
#define PIN_P2_6__I2S0_SCLK_B ALIF_PINMUX(2, 6, 2)
```

相关声明：[PIN_P2_6__I2S0_SCLK_B](#ab7b482cc545e06022c8549c62a5796d7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`I2S0_SCLK_B`。

<a id="r_ae2cc326e40642086ffefa929c5c01ac5"></a>

```c
#define PIN_P2_6__I2C1_SDA_B ALIF_PINMUX(2, 6, 3)
```

相关声明：[PIN_P2_6__I2C1_SDA_B](#ae2cc326e40642086ffefa929c5c01ac5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`I2C1_SDA_B`。

<a id="r_afe56bb2aa798518976190a959d88fdb6"></a>

```c
#define PIN_P2_6__UT3_T0_A ALIF_PINMUX(2, 6, 4)
```

相关声明：[PIN_P2_6__UT3_T0_A](#afe56bb2aa798518976190a959d88fdb6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`UT3_T0_A`。

<a id="r_aecc3c9c2a85fd42569f9c4559101bd7c"></a>

```c
#define PIN_P2_6__ANA_S14 ALIF_PINMUX(2, 6, 6)
```

相关声明：[PIN_P2_6__ANA_S14](#aecc3c9c2a85fd42569f9c4559101bd7c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）6：`ANA_S14`。

<a id="r_ab3f711dc40129f35a38cec46e12f23dd"></a>

```c
#define PIN_P2_7__GPIO ALIF_PINMUX(2, 7, 0)
```

相关声明：[PIN_P2_7__GPIO](#ab3f711dc40129f35a38cec46e12f23dd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P2.7` 的复用功能（Alternate Functions）。

<a id="r_a24548c32d58d93a273c702862ac1f101"></a>

```c
#define PIN_P2_7__UART4_TX_A ALIF_PINMUX(2, 7, 1)
```

相关声明：[PIN_P2_7__UART4_TX_A](#a24548c32d58d93a273c702862ac1f101)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`UART4_TX_A`。

<a id="r_a5c52059835751817fa789428c272b4b2"></a>

```c
#define PIN_P2_7__I2S0_WS_B ALIF_PINMUX(2, 7, 2)
```

相关声明：[PIN_P2_7__I2S0_WS_B](#a5c52059835751817fa789428c272b4b2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`I2S0_WS_B`。

<a id="r_a77dba1bd3536b87c3b804b4b5c8844c5"></a>

```c
#define PIN_P2_7__I2C1_SCL_B ALIF_PINMUX(2, 7, 3)
```

相关声明：[PIN_P2_7__I2C1_SCL_B](#a77dba1bd3536b87c3b804b4b5c8844c5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`I2C1_SCL_B`。

<a id="r_af33c77692ea55157dde2a366df179946"></a>

```c
#define PIN_P2_7__UT3_T1_A ALIF_PINMUX(2, 7, 4)
```

相关声明：[PIN_P2_7__UT3_T1_A](#af33c77692ea55157dde2a366df179946)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`UT3_T1_A`。

<a id="r_a1a690217c990dac7671bcad9e6855e4c"></a>

```c
#define PIN_P2_7__ANA_S15 ALIF_PINMUX(2, 7, 6)
```

相关声明：[PIN_P2_7__ANA_S15](#a1a690217c990dac7671bcad9e6855e4c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）2 的引脚（Pin）7：`ANA_S15`。

<a id="r_aeb39304438c089405b315935caa1d90b"></a>

```c
#define PIN_P3_0__GPIO ALIF_PINMUX(3, 0, 0)
```

相关声明：[PIN_P3_0__GPIO](#aeb39304438c089405b315935caa1d90b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.0` 的复用功能（Alternate Functions）。

<a id="r_a08e6a0f6bde4e7bb7585c23d89d26e34"></a>

```c
#define PIN_P3_0__OSPI0_D0_A ALIF_PINMUX(3, 0, 1)
```

相关声明：[PIN_P3_0__OSPI0_D0_A](#a08e6a0f6bde4e7bb7585c23d89d26e34)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="r_aca5323c8961628d66981805dc76e426d"></a>

```c
#define PIN_P3_0__UART5_RX_A ALIF_PINMUX(3, 0, 2)
```

相关声明：[PIN_P3_0__UART5_RX_A](#aca5323c8961628d66981805dc76e426d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`UART5_RX_A`。

<a id="r_a657f73711ba0d8cc715200c6d00f12a0"></a>

```c
#define PIN_P3_0__LPPDM_C0_B ALIF_PINMUX(3, 0, 3)
```

相关声明：[PIN_P3_0__LPPDM_C0_B](#a657f73711ba0d8cc715200c6d00f12a0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`LPPDM_C0_B`。

<a id="r_ab272993eba936e78b7b49628656270c0"></a>

```c
#define PIN_P3_0__I2S1_SDI_B ALIF_PINMUX(3, 0, 4)
```

相关声明：[PIN_P3_0__I2S1_SDI_B](#ab272993eba936e78b7b49628656270c0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`I2S1_SDI_B`。

<a id="r_a180a5337fefee4470d0207159a3a6b89"></a>

```c
#define PIN_P3_0__SPI2_MISO_A ALIF_PINMUX(3, 0, 5)
```

相关声明：[PIN_P3_0__SPI2_MISO_A](#a180a5337fefee4470d0207159a3a6b89)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`SPI2_MISO_A`。

<a id="r_acbf62e57bca8f709a7c999b310d49fd8"></a>

```c
#define PIN_P3_0__CDC_HSYNC_B ALIF_PINMUX(3, 0, 6)
```

相关声明：[PIN_P3_0__CDC_HSYNC_B](#acbf62e57bca8f709a7c999b310d49fd8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）0：`CDC_HSYNC_B`。

<a id="r_a6cd05b1a797d571a1d1d1981ba849f8f"></a>

```c
#define PIN_P3_1__GPIO ALIF_PINMUX(3, 1, 0)
```

相关声明：[PIN_P3_1__GPIO](#a6cd05b1a797d571a1d1d1981ba849f8f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.1` 的复用功能（Alternate Functions）。

<a id="r_a6b9214690f4a38d21962692dd8d8a48f"></a>

```c
#define PIN_P3_1__OSPI0_D1_A ALIF_PINMUX(3, 1, 1)
```

相关声明：[PIN_P3_1__OSPI0_D1_A](#a6b9214690f4a38d21962692dd8d8a48f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="r_abb45e90dbe3e11cdb30a79ee1ad737da"></a>

```c
#define PIN_P3_1__UART5_TX_A ALIF_PINMUX(3, 1, 2)
```

相关声明：[PIN_P3_1__UART5_TX_A](#abb45e90dbe3e11cdb30a79ee1ad737da)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`UART5_TX_A`。

<a id="r_af2b49d47624cdb616d2c7726cb63cc25"></a>

```c
#define PIN_P3_1__LPPDM_D0_B ALIF_PINMUX(3, 1, 3)
```

相关声明：[PIN_P3_1__LPPDM_D0_B](#af2b49d47624cdb616d2c7726cb63cc25)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`LPPDM_D0_B`。

<a id="r_a4b5b4b545552f71a7119ae29b2b4b4ec"></a>

```c
#define PIN_P3_1__I2S1_SDO_B ALIF_PINMUX(3, 1, 4)
```

相关声明：[PIN_P3_1__I2S1_SDO_B](#a4b5b4b545552f71a7119ae29b2b4b4ec)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`I2S1_SDO_B`。

<a id="r_a65ecac46cfcbed6eb9c9703176a73159"></a>

```c
#define PIN_P3_1__SPI2_MOSI_A ALIF_PINMUX(3, 1, 5)
```

相关声明：[PIN_P3_1__SPI2_MOSI_A](#a65ecac46cfcbed6eb9c9703176a73159)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`SPI2_MOSI_A`。

<a id="r_a125d130d6c1407193272677f26989444"></a>

```c
#define PIN_P3_1__CDC_VSYNC_B ALIF_PINMUX(3, 1, 6)
```

相关声明：[PIN_P3_1__CDC_VSYNC_B](#a125d130d6c1407193272677f26989444)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）1：`CDC_VSYNC_B`。

<a id="r_a4bfd126d24cab1669b9880c163e9b73a"></a>

```c
#define PIN_P3_2__GPIO ALIF_PINMUX(3, 2, 0)
```

相关声明：[PIN_P3_2__GPIO](#a4bfd126d24cab1669b9880c163e9b73a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.2` 的复用功能（Alternate Functions）。

<a id="r_acac0bc02b88cfffac293e54860f915b6"></a>

```c
#define PIN_P3_2__OSPI0_D2_A ALIF_PINMUX(3, 2, 1)
```

相关声明：[PIN_P3_2__OSPI0_D2_A](#acac0bc02b88cfffac293e54860f915b6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="r_a7119fa1cbc0ca291d2aba6fb742bf6f8"></a>

```c
#define PIN_P3_2__UART3_RX_B ALIF_PINMUX(3, 2, 2)
```

相关声明：[PIN_P3_2__UART3_RX_B](#a7119fa1cbc0ca291d2aba6fb742bf6f8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`UART3_RX_B`。

<a id="r_a5c1597499610b3867a91dcbd15fccf39"></a>

```c
#define PIN_P3_2__LPPDM_C1_B ALIF_PINMUX(3, 2, 3)
```

相关声明：[PIN_P3_2__LPPDM_C1_B](#a5c1597499610b3867a91dcbd15fccf39)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`LPPDM_C1_B`。

<a id="r_a0ae2607bb670c7e115a600cb35462e49"></a>

```c
#define PIN_P3_2__I2S1_SCLK_SLV_B ALIF_PINMUX(3, 2, 4)
```

相关声明：[PIN_P3_2__I2S1_SCLK_SLV_B](#a0ae2607bb670c7e115a600cb35462e49)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`I2S1_SCLK_SLV_B`。

<a id="r_a02f965e1da21a78ada64cfb1f31d7753"></a>

```c
#define PIN_P3_2__SPI2_SCLK_A ALIF_PINMUX(3, 2, 5)
```

相关声明：[PIN_P3_2__SPI2_SCLK_A](#a02f965e1da21a78ada64cfb1f31d7753)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`SPI2_SCLK_A`。

<a id="r_a8204e79617e38dcd9183dce74f30caaf"></a>

```c
#define PIN_P3_2__CDC_PCLK_B ALIF_PINMUX(3, 2, 6)
```

相关声明：[PIN_P3_2__CDC_PCLK_B](#a8204e79617e38dcd9183dce74f30caaf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）2：`CDC_PCLK_B`。

<a id="r_ac22b3e259b7eac30c576114860368ae4"></a>

```c
#define PIN_P3_3__GPIO ALIF_PINMUX(3, 3, 0)
```

相关声明：[PIN_P3_3__GPIO](#ac22b3e259b7eac30c576114860368ae4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.3` 的复用功能（Alternate Functions）。

<a id="r_ad01b9c7e9987a9f24df78666736d7c64"></a>

```c
#define PIN_P3_3__OSPI0_D3_A ALIF_PINMUX(3, 3, 1)
```

相关声明：[PIN_P3_3__OSPI0_D3_A](#ad01b9c7e9987a9f24df78666736d7c64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`OSPI0_D3_A`。

<a id="r_acd31e37bd65d6ee81bf629388730b2de"></a>

```c
#define PIN_P3_3__UART3_TX_B ALIF_PINMUX(3, 3, 2)
```

相关声明：[PIN_P3_3__UART3_TX_B](#acd31e37bd65d6ee81bf629388730b2de)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`UART3_TX_B`。

<a id="r_a22392f2d0211f8d72d4c3e55bb09d579"></a>

```c
#define PIN_P3_3__LPPDM_D1_B ALIF_PINMUX(3, 3, 3)
```

相关声明：[PIN_P3_3__LPPDM_D1_B](#a22392f2d0211f8d72d4c3e55bb09d579)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`LPPDM_D1_B`。

<a id="r_a19299a3b792e33a1632d329de35aa6cb"></a>

```c
#define PIN_P3_3__I2S1_WS_SLV_B ALIF_PINMUX(3, 3, 4)
```

相关声明：[PIN_P3_3__I2S1_WS_SLV_B](#a19299a3b792e33a1632d329de35aa6cb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`I2S1_WS_SLV_B`。

<a id="r_ae50bd1782360494a12bada142b5a5fbe"></a>

```c
#define PIN_P3_3__SPI2_SS0_A ALIF_PINMUX(3, 3, 5)
```

相关声明：[PIN_P3_3__SPI2_SS0_A](#ae50bd1782360494a12bada142b5a5fbe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`SPI2_SS0_A`。

<a id="r_a8a657205eda7450f90f32a1e7b85d5bc"></a>

```c
#define PIN_P3_3__CDC_DE_B ALIF_PINMUX(3, 3, 6)
```

相关声明：[PIN_P3_3__CDC_DE_B](#a8a657205eda7450f90f32a1e7b85d5bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）3：`CDC_DE_B`。

<a id="r_af826ee88e3ed085269f16bee4a1a5bd7"></a>

```c
#define PIN_P3_4__GPIO ALIF_PINMUX(3, 4, 0)
```

相关声明：[PIN_P3_4__GPIO](#af826ee88e3ed085269f16bee4a1a5bd7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.4` 的复用功能（Alternate Functions）。

<a id="r_a6b6cb80eb2ec08d5a72dad514fbe6717"></a>

```c
#define PIN_P3_4__OSPI0_D4_A ALIF_PINMUX(3, 4, 1)
```

相关声明：[PIN_P3_4__OSPI0_D4_A](#a6b6cb80eb2ec08d5a72dad514fbe6717)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`OSPI0_D4_A`。

<a id="r_a4ac9aba64d45c9ac940c369519715fcc"></a>

```c
#define PIN_P3_4__LPPDM_C2_B ALIF_PINMUX(3, 4, 2)
```

相关声明：[PIN_P3_4__LPPDM_C2_B](#a4ac9aba64d45c9ac940c369519715fcc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`LPPDM_C2_B`。

<a id="r_ac11d291faff2b72ae43b542cdfa79b43"></a>

```c
#define PIN_P3_4__SPI1_MISO_A ALIF_PINMUX(3, 4, 3)
```

相关声明：[PIN_P3_4__SPI1_MISO_A](#ac11d291faff2b72ae43b542cdfa79b43)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`SPI1_MISO_A`。

<a id="r_ac81d90635b271e413d3a8216c98f6a64"></a>

```c
#define PIN_P3_4__LPCAM_VSYNC_A ALIF_PINMUX(3, 4, 4)
```

相关声明：[PIN_P3_4__LPCAM_VSYNC_A](#ac81d90635b271e413d3a8216c98f6a64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`LPCAM_VSYNC_A`。

<a id="r_a0d63779879e818e7185ac29a5251be7a"></a>

```c
#define PIN_P3_4__SD_CMD_A ALIF_PINMUX(3, 4, 5)
```

相关声明：[PIN_P3_4__SD_CMD_A](#a0d63779879e818e7185ac29a5251be7a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`SD_CMD_A`。

<a id="r_a334331e4bebc81e43c8007e45dbe41ca"></a>

```c
#define PIN_P3_4__CMP0_OUT_A ALIF_PINMUX(3, 4, 6)
```

相关声明：[PIN_P3_4__CMP0_OUT_A](#a334331e4bebc81e43c8007e45dbe41ca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）4：`CMP0_OUT_A`。

<a id="r_a3f53dddbffc228108e7c1eb17ee058a4"></a>

```c
#define PIN_P3_5__GPIO ALIF_PINMUX(3, 5, 0)
```

相关声明：[PIN_P3_5__GPIO](#a3f53dddbffc228108e7c1eb17ee058a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.5` 的复用功能（Alternate Functions）。

<a id="r_a07dc35c610e8c3cc067ce280102894da"></a>

```c
#define PIN_P3_5__OSPI0_D5_A ALIF_PINMUX(3, 5, 1)
```

相关声明：[PIN_P3_5__OSPI0_D5_A](#a07dc35c610e8c3cc067ce280102894da)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`OSPI0_D5_A`。

<a id="r_a693d2fc47da86e789e016b3367a6a945"></a>

```c
#define PIN_P3_5__LPPDM_D2_B ALIF_PINMUX(3, 5, 2)
```

相关声明：[PIN_P3_5__LPPDM_D2_B](#a693d2fc47da86e789e016b3367a6a945)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`LPPDM_D2_B`。

<a id="r_a408a4a0e8b2cc3ba0ed810c2c4d797ba"></a>

```c
#define PIN_P3_5__SPI1_MOSI_A ALIF_PINMUX(3, 5, 3)
```

相关声明：[PIN_P3_5__SPI1_MOSI_A](#a408a4a0e8b2cc3ba0ed810c2c4d797ba)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`SPI1_MOSI_A`。

<a id="r_ab4bd78c83bf8c6916c350b0582a127b4"></a>

```c
#define PIN_P3_5__LPCAM_HSYNC_A ALIF_PINMUX(3, 5, 4)
```

相关声明：[PIN_P3_5__LPCAM_HSYNC_A](#ab4bd78c83bf8c6916c350b0582a127b4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`LPCAM_HSYNC_A`。

<a id="r_a2e462b52b0754c84210ee53bccdf7cf3"></a>

```c
#define PIN_P3_5__SD_CLK_A ALIF_PINMUX(3, 5, 5)
```

相关声明：[PIN_P3_5__SD_CLK_A](#a2e462b52b0754c84210ee53bccdf7cf3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`SD_CLK_A`。

<a id="r_a1ccd8435bb96e65d67b09d351dc95bd4"></a>

```c
#define PIN_P3_5__CMP1_OUT_A ALIF_PINMUX(3, 5, 6)
```

相关声明：[PIN_P3_5__CMP1_OUT_A](#a1ccd8435bb96e65d67b09d351dc95bd4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）5：`CMP1_OUT_A`。

<a id="r_a6de92753c75d2827828767a9ed529829"></a>

```c
#define PIN_P3_6__GPIO ALIF_PINMUX(3, 6, 0)
```

相关声明：[PIN_P3_6__GPIO](#a6de92753c75d2827828767a9ed529829)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.6` 的复用功能（Alternate Functions）。

<a id="r_aea873d99be810ba6e9a710720e2d2f76"></a>

```c
#define PIN_P3_6__OSPI0_D6_A ALIF_PINMUX(3, 6, 1)
```

相关声明：[PIN_P3_6__OSPI0_D6_A](#aea873d99be810ba6e9a710720e2d2f76)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`OSPI0_D6_A`。

<a id="r_a6995bac7197a680fc2d5835934758ccc"></a>

```c
#define PIN_P3_6__UART4_RX_B ALIF_PINMUX(3, 6, 2)
```

相关声明：[PIN_P3_6__UART4_RX_B](#a6995bac7197a680fc2d5835934758ccc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`UART4_RX_B`。

<a id="r_a266153536a0c5ae308ec86013f04eef2"></a>

```c
#define PIN_P3_6__LPPDM_C3_B ALIF_PINMUX(3, 6, 3)
```

相关声明：[PIN_P3_6__LPPDM_C3_B](#a266153536a0c5ae308ec86013f04eef2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`LPPDM_C3_B`。

<a id="r_a46572ca90cf7364a9664816bb5a7cc30"></a>

```c
#define PIN_P3_6__SPI1_SCLK_A ALIF_PINMUX(3, 6, 4)
```

相关声明：[PIN_P3_6__SPI1_SCLK_A](#a46572ca90cf7364a9664816bb5a7cc30)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`SPI1_SCLK_A`。

<a id="r_adda246545320f5be35347ad5756f96f3"></a>

```c
#define PIN_P3_6__LPCAM_PCLK_A ALIF_PINMUX(3, 6, 5)
```

相关声明：[PIN_P3_6__LPCAM_PCLK_A](#adda246545320f5be35347ad5756f96f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`LPCAM_PCLK_A`。

<a id="r_acfdc172b1746aa6cb05a46782d84b8e3"></a>

```c
#define PIN_P3_6__EXT_RTS_A ALIF_PINMUX(3, 6, 6)
```

相关声明：[PIN_P3_6__EXT_RTS_A](#acfdc172b1746aa6cb05a46782d84b8e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`EXT_RTS_A`。

<a id="r_aedf1d5746a7b7f7fbf815a3518a4be67"></a>

```c
#define PIN_P3_6__CX_WLAN_TX ALIF_PINMUX(3, 6, 7)
```

相关声明：[PIN_P3_6__CX_WLAN_TX](#aedf1d5746a7b7f7fbf815a3518a4be67)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）6：`CX_WLAN_TX`。

<a id="r_a60d3cb4a00a06169c18eedd0593c0e3b"></a>

```c
#define PIN_P3_7__GPIO ALIF_PINMUX(3, 7, 0)
```

相关声明：[PIN_P3_7__GPIO](#a60d3cb4a00a06169c18eedd0593c0e3b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P3.7` 的复用功能（Alternate Functions）。

<a id="r_a03367dff465d39650944aed091c5529f"></a>

```c
#define PIN_P3_7__OSPI0_D7_A ALIF_PINMUX(3, 7, 1)
```

相关声明：[PIN_P3_7__OSPI0_D7_A](#a03367dff465d39650944aed091c5529f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`OSPI0_D7_A`。

<a id="r_a6a8d56588c6366fd712451566aaad6b0"></a>

```c
#define PIN_P3_7__UART4_TX_B ALIF_PINMUX(3, 7, 2)
```

相关声明：[PIN_P3_7__UART4_TX_B](#a6a8d56588c6366fd712451566aaad6b0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`UART4_TX_B`。

<a id="r_a50b7bcbbbfe2e4b6eb7a4a8dba31e4a9"></a>

```c
#define PIN_P3_7__LPPDM_D3_B ALIF_PINMUX(3, 7, 3)
```

相关声明：[PIN_P3_7__LPPDM_D3_B](#a50b7bcbbbfe2e4b6eb7a4a8dba31e4a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`LPPDM_D3_B`。

<a id="r_ab41862028c94474a27360852a45b492a"></a>

```c
#define PIN_P3_7__LPCAM_XVCLK_A ALIF_PINMUX(3, 7, 4)
```

相关声明：[PIN_P3_7__LPCAM_XVCLK_A](#ab41862028c94474a27360852a45b492a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`LPCAM_XVCLK_A`。

<a id="r_ac471eaf7fde1a025f146c40a4a1cb74b"></a>

```c
#define PIN_P3_7__SD_RST_B ALIF_PINMUX(3, 7, 5)
```

相关声明：[PIN_P3_7__SD_RST_B](#ac471eaf7fde1a025f146c40a4a1cb74b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`SD_RST_B`。

<a id="r_a97ddd001f0aaa2f9077d304d66036f61"></a>

```c
#define PIN_P3_7__EXT_CTS_A ALIF_PINMUX(3, 7, 6)
```

相关声明：[PIN_P3_7__EXT_CTS_A](#a97ddd001f0aaa2f9077d304d66036f61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`EXT_CTS_A`。

<a id="r_a08ce04f3e23b3249a99007cdc01b486a"></a>

```c
#define PIN_P3_7__CX_WLAN_RX ALIF_PINMUX(3, 7, 7)
```

相关声明：[PIN_P3_7__CX_WLAN_RX](#a08ce04f3e23b3249a99007cdc01b486a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）3 的引脚（Pin）7：`CX_WLAN_RX`。

<a id="r_a1ab2ef5cf337828d3e4be24bba3391e6"></a>

```c
#define PIN_P4_0__GPIO ALIF_PINMUX(4, 0, 0)
```

相关声明：[PIN_P4_0__GPIO](#a1ab2ef5cf337828d3e4be24bba3391e6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.0` 的复用功能（Alternate Functions）。

<a id="r_aa4a65ef0d12969c5f86e959537887b2d"></a>

```c
#define PIN_P4_0__OSPI0_SCLKN_A ALIF_PINMUX(4, 0, 1)
```

相关声明：[PIN_P4_0__OSPI0_SCLKN_A](#aa4a65ef0d12969c5f86e959537887b2d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`OSPI0_SCLKN_A`。

<a id="r_a746064cb94df8b7298905f74a9c8ecdc"></a>

```c
#define PIN_P4_0__UART0_RX_B ALIF_PINMUX(4, 0, 2)
```

相关声明：[PIN_P4_0__UART0_RX_B](#a746064cb94df8b7298905f74a9c8ecdc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`UART0_RX_B`。

<a id="r_a0ce696d8a98527b7aef206be42f9cc64"></a>

```c
#define PIN_P4_0__SPI2_SS1_A ALIF_PINMUX(4, 0, 3)
```

相关声明：[PIN_P4_0__SPI2_SS1_A](#a0ce696d8a98527b7aef206be42f9cc64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`SPI2_SS1_A`。

<a id="r_a5e7e485258c9cefe47c4a4787624d3ca"></a>

```c
#define PIN_P4_0__UT0_T0_A ALIF_PINMUX(4, 0, 4)
```

相关声明：[PIN_P4_0__UT0_T0_A](#a5e7e485258c9cefe47c4a4787624d3ca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`UT0_T0_A`。

<a id="r_ae25864e7506f7b27e332543d2470fddf"></a>

```c
#define PIN_P4_0__LPCAM_D0_A ALIF_PINMUX(4, 0, 5)
```

相关声明：[PIN_P4_0__LPCAM_D0_A](#ae25864e7506f7b27e332543d2470fddf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="r_a1a292ebb91985973ab40aeee4e5d89cf"></a>

```c
#define PIN_P4_0__SD_D0_A ALIF_PINMUX(4, 0, 6)
```

相关声明：[PIN_P4_0__SD_D0_A](#a1a292ebb91985973ab40aeee4e5d89cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`SD_D0_A`。

<a id="r_a18718ec4f3d76dc2c004254ce07fb79b"></a>

```c
#define PIN_P4_0__EXT_RX_A ALIF_PINMUX(4, 0, 7)
```

相关声明：[PIN_P4_0__EXT_RX_A](#a18718ec4f3d76dc2c004254ce07fb79b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）0：`EXT_RX_A`。

<a id="r_a5fb4375020986c6656759f3223558f10"></a>

```c
#define PIN_P4_1__GPIO ALIF_PINMUX(4, 1, 0)
```

相关声明：[PIN_P4_1__GPIO](#a5fb4375020986c6656759f3223558f10)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.1` 的复用功能（Alternate Functions）。

<a id="r_a0df28f60edf04802895e2e65c8c62700"></a>

```c
#define PIN_P4_1__OSPI0_RXDS_A ALIF_PINMUX(4, 1, 1)
```

相关声明：[PIN_P4_1__OSPI0_RXDS_A](#a0df28f60edf04802895e2e65c8c62700)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`OSPI0_RXDS_A`。

<a id="r_a7c22e0d1553016df93e54d3d383178ff"></a>

```c
#define PIN_P4_1__UART0_TX_B ALIF_PINMUX(4, 1, 2)
```

相关声明：[PIN_P4_1__UART0_TX_B](#a7c22e0d1553016df93e54d3d383178ff)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`UART0_TX_B`。

<a id="r_ad22e1e1495cfbde6d14323b9c3e32bd0"></a>

```c
#define PIN_P4_1__SPI2_SS2_A ALIF_PINMUX(4, 1, 3)
```

相关声明：[PIN_P4_1__SPI2_SS2_A](#ad22e1e1495cfbde6d14323b9c3e32bd0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`SPI2_SS2_A`。

<a id="r_ab8905fd2eb3785e6fee1f3bc479d9ca2"></a>

```c
#define PIN_P4_1__UT0_T1_A ALIF_PINMUX(4, 1, 4)
```

相关声明：[PIN_P4_1__UT0_T1_A](#ab8905fd2eb3785e6fee1f3bc479d9ca2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`UT0_T1_A`。

<a id="r_ac2829e522c09bde1f8dcc9ec0e1e8b9c"></a>

```c
#define PIN_P4_1__LPCAM_D1_A ALIF_PINMUX(4, 1, 5)
```

相关声明：[PIN_P4_1__LPCAM_D1_A](#ac2829e522c09bde1f8dcc9ec0e1e8b9c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="r_aa8d357f6692b4eaca657b934834350a9"></a>

```c
#define PIN_P4_1__SD_D1_A ALIF_PINMUX(4, 1, 6)
```

相关声明：[PIN_P4_1__SD_D1_A](#aa8d357f6692b4eaca657b934834350a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`SD_D1_A`。

<a id="r_af1b2095550709b1e14c30ad6ae474771"></a>

```c
#define PIN_P4_1__EXT_TX_A ALIF_PINMUX(4, 1, 7)
```

相关声明：[PIN_P4_1__EXT_TX_A](#af1b2095550709b1e14c30ad6ae474771)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）1：`EXT_TX_A`。

<a id="r_a2a9f0b7627d1f0149fa1cddc428e76f9"></a>

```c
#define PIN_P4_2__GPIO ALIF_PINMUX(4, 2, 0)
```

相关声明：[PIN_P4_2__GPIO](#a2a9f0b7627d1f0149fa1cddc428e76f9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.2` 的复用功能（Alternate Functions）。

<a id="r_a98c0f9bd017151740c3ccfea7284a20b"></a>

```c
#define PIN_P4_2__HFXO_OUT_A ALIF_PINMUX(4, 2, 1)
```

相关声明：[PIN_P4_2__HFXO_OUT_A](#a98c0f9bd017151740c3ccfea7284a20b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`HFXO_OUT_A`。

<a id="r_a5da13c644ad45ce5ff82c01d05fe5d8b"></a>

```c
#define PIN_P4_2__OSPI0_SCLK_A ALIF_PINMUX(4, 2, 2)
```

相关声明：[PIN_P4_2__OSPI0_SCLK_A](#a5da13c644ad45ce5ff82c01d05fe5d8b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`OSPI0_SCLK_A`。

<a id="r_ae629174d9c48b1cd4eb7c1cf7d1ffa7e"></a>

```c
#define PIN_P4_2__UART4_DE_A ALIF_PINMUX(4, 2, 3)
```

相关声明：[PIN_P4_2__UART4_DE_A](#ae629174d9c48b1cd4eb7c1cf7d1ffa7e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`UART4_DE_A`。

<a id="r_a20e581f0adef0fcfe47bc16323f24ed3"></a>

```c
#define PIN_P4_2__UT1_T0_A ALIF_PINMUX(4, 2, 4)
```

相关声明：[PIN_P4_2__UT1_T0_A](#a20e581f0adef0fcfe47bc16323f24ed3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`UT1_T0_A`。

<a id="r_af81bdc4d2f7ec97fe76ec92ca24ddaac"></a>

```c
#define PIN_P4_2__LPCAM_D2_A ALIF_PINMUX(4, 2, 5)
```

相关声明：[PIN_P4_2__LPCAM_D2_A](#af81bdc4d2f7ec97fe76ec92ca24ddaac)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="r_aecf120640ee69bbbf5a1ed7cb80deb96"></a>

```c
#define PIN_P4_2__SD_D2_A ALIF_PINMUX(4, 2, 6)
```

相关声明：[PIN_P4_2__SD_D2_A](#aecf120640ee69bbbf5a1ed7cb80deb96)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`SD_D2_A`。

<a id="r_a7691073005a4ead27b8f64beb2548f2a"></a>

```c
#define PIN_P4_2__EXT_TRACE_A ALIF_PINMUX(4, 2, 7)
```

相关声明：[PIN_P4_2__EXT_TRACE_A](#a7691073005a4ead27b8f64beb2548f2a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）2：`EXT_TRACE_A`。

<a id="r_a97b4675f5259e06d48cdd30755a46f3e"></a>

```c
#define PIN_P4_3__GPIO ALIF_PINMUX(4, 3, 0)
```

相关声明：[PIN_P4_3__GPIO](#a97b4675f5259e06d48cdd30755a46f3e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.3` 的复用功能（Alternate Functions）。

<a id="r_a19f6e008e0abb13d14c7fe8ad6fbe6f7"></a>

```c
#define PIN_P4_3__JTAG0_NSRST ALIF_PINMUX(4, 3, 1)
```

相关声明：[PIN_P4_3__JTAG0_NSRST](#a19f6e008e0abb13d14c7fe8ad6fbe6f7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`JTAG0_NSRST`。

<a id="r_ad3a967ff2a55e33d61a036a466f8e438"></a>

```c
#define PIN_P4_3__CS_MWS_ID0 ALIF_PINMUX(4, 3, 2)
```

相关声明：[PIN_P4_3__CS_MWS_ID0](#ad3a967ff2a55e33d61a036a466f8e438)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`CS_MWS_ID0`。

<a id="r_a5aa98d3c3d4b2341b39f13be3af830a5"></a>

```c
#define PIN_P4_3__UT1_T1_A ALIF_PINMUX(4, 3, 3)
```

相关声明：[PIN_P4_3__UT1_T1_A](#a5aa98d3c3d4b2341b39f13be3af830a5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`UT1_T1_A`。

<a id="r_a0d58327743edb52505ead51efddd7eb4"></a>

```c
#define PIN_P4_3__CMP0_OUT_B ALIF_PINMUX(4, 3, 6)
```

相关声明：[PIN_P4_3__CMP0_OUT_B](#a0d58327743edb52505ead51efddd7eb4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）3：`CMP0_OUT_B`。

<a id="r_a71f56da2cfc34a4fa6dbbba7e9936d28"></a>

```c
#define PIN_P4_4__GPIO ALIF_PINMUX(4, 4, 0)
```

相关声明：[PIN_P4_4__GPIO](#a71f56da2cfc34a4fa6dbbba7e9936d28)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.4` 的复用功能（Alternate Functions）。

<a id="r_a026da00206cb806cf7e868c00dfa15de"></a>

```c
#define PIN_P4_4__JTAG0_TCK ALIF_PINMUX(4, 4, 1)
```

相关声明：[PIN_P4_4__JTAG0_TCK](#a026da00206cb806cf7e868c00dfa15de)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`JTAG0_TCK`。

<a id="r_a8f8a4b37bca8ab9c9021626f9e15adb4"></a>

```c
#define PIN_P4_4__FAULT0_B ALIF_PINMUX(4, 4, 2)
```

相关声明：[PIN_P4_4__FAULT0_B](#a8f8a4b37bca8ab9c9021626f9e15adb4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`FAULT0_B`。

<a id="r_a8318b5bd441072af1b0d4dfeb97d55e0"></a>

```c
#define PIN_P4_4__CS_MWS_ID1 ALIF_PINMUX(4, 4, 3)
```

相关声明：[PIN_P4_4__CS_MWS_ID1](#a8318b5bd441072af1b0d4dfeb97d55e0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`CS_MWS_ID1`。

<a id="r_a25e0c2ba6146de455410dab64097aa33"></a>

```c
#define PIN_P4_4__UT2_T0_A ALIF_PINMUX(4, 4, 4)
```

相关声明：[PIN_P4_4__UT2_T0_A](#a25e0c2ba6146de455410dab64097aa33)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）4：`UT2_T0_A`。

<a id="r_a44781940091d6eadb753aa098a1c8a3a"></a>

```c
#define PIN_P4_5__GPIO ALIF_PINMUX(4, 5, 0)
```

相关声明：[PIN_P4_5__GPIO](#a44781940091d6eadb753aa098a1c8a3a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.5` 的复用功能（Alternate Functions）。

<a id="r_ac8c66019ed9ef1f3e1761b9676666d7c"></a>

```c
#define PIN_P4_5__JTAG0_TMS ALIF_PINMUX(4, 5, 1)
```

相关声明：[PIN_P4_5__JTAG0_TMS](#ac8c66019ed9ef1f3e1761b9676666d7c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`JTAG0_TMS`。

<a id="r_ad1dc12f3fb93facb6b056284db1dd865"></a>

```c
#define PIN_P4_5__FAULT1_B ALIF_PINMUX(4, 5, 2)
```

相关声明：[PIN_P4_5__FAULT1_B](#ad1dc12f3fb93facb6b056284db1dd865)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`FAULT1_B`。

<a id="r_a000faa2a435ba773512656c672ba6151"></a>

```c
#define PIN_P4_5__CS_MWS_ID2 ALIF_PINMUX(4, 5, 3)
```

相关声明：[PIN_P4_5__CS_MWS_ID2](#a000faa2a435ba773512656c672ba6151)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`CS_MWS_ID2`。

<a id="r_a6a406851e165d3138915a0e9af6ac44f"></a>

```c
#define PIN_P4_5__UT2_T1_A ALIF_PINMUX(4, 5, 4)
```

相关声明：[PIN_P4_5__UT2_T1_A](#a6a406851e165d3138915a0e9af6ac44f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）5：`UT2_T1_A`。

<a id="r_aae4c2f3f2743c6281127d761c2d3c952"></a>

```c
#define PIN_P4_6__GPIO ALIF_PINMUX(4, 6, 0)
```

相关声明：[PIN_P4_6__GPIO](#aae4c2f3f2743c6281127d761c2d3c952)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.6` 的复用功能（Alternate Functions）。

<a id="r_a64e905aad463ddb010ef5e31aa4bb355"></a>

```c
#define PIN_P4_6__JTAG0_TDI ALIF_PINMUX(4, 6, 1)
```

相关声明：[PIN_P4_6__JTAG0_TDI](#a64e905aad463ddb010ef5e31aa4bb355)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`JTAG0_TDI`。

<a id="r_ae86da62dbb31a6c4b1a4d0b23fcbaaab"></a>

```c
#define PIN_P4_6__FAULT2_B ALIF_PINMUX(4, 6, 2)
```

相关声明：[PIN_P4_6__FAULT2_B](#ae86da62dbb31a6c4b1a4d0b23fcbaaab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`FAULT2_B`。

<a id="r_aeac835d737d34448f0a28bc7101a087b"></a>

```c
#define PIN_P4_6__LPI2S_WS_B ALIF_PINMUX(4, 6, 3)
```

相关声明：[PIN_P4_6__LPI2S_WS_B](#aeac835d737d34448f0a28bc7101a087b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`LPI2S_WS_B`。

<a id="r_ad9aa455c48e18f8651b6c46265912bfa"></a>

```c
#define PIN_P4_6__UT3_T0_A ALIF_PINMUX(4, 6, 4)
```

相关声明：[PIN_P4_6__UT3_T0_A](#ad9aa455c48e18f8651b6c46265912bfa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）6：`UT3_T0_A`。

<a id="r_a414ee602068915040eb8dab92a92bb61"></a>

```c
#define PIN_P4_7__GPIO ALIF_PINMUX(4, 7, 0)
```

相关声明：[PIN_P4_7__GPIO](#a414ee602068915040eb8dab92a92bb61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P4.7` 的复用功能（Alternate Functions）。

<a id="r_a1882c539a53276d676235207bd87494a"></a>

```c
#define PIN_P4_7__JTAG0_TDO ALIF_PINMUX(4, 7, 1)
```

相关声明：[PIN_P4_7__JTAG0_TDO](#a1882c539a53276d676235207bd87494a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`JTAG0_TDO`。

<a id="r_a4781e1c7651d920f43fb0b2472372436"></a>

```c
#define PIN_P4_7__FAULT3_B ALIF_PINMUX(4, 7, 2)
```

相关声明：[PIN_P4_7__FAULT3_B](#a4781e1c7651d920f43fb0b2472372436)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`FAULT3_B`。

<a id="r_a85dc41a85f81bf5aa6b21adea41f6cc7"></a>

```c
#define PIN_P4_7__UT3_T1_A ALIF_PINMUX(4, 7, 3)
```

相关声明：[PIN_P4_7__UT3_T1_A](#a85dc41a85f81bf5aa6b21adea41f6cc7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`UT3_T1_A`。

<a id="r_ae195873e36cdb06497fa9c821e422350"></a>

```c
#define PIN_P4_7__CS_MWS_ID4 ALIF_PINMUX(4, 7, 4)
```

相关声明：[PIN_P4_7__CS_MWS_ID4](#ae195873e36cdb06497fa9c821e422350)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`CS_MWS_ID4`。

<a id="r_a921f7c932359c5bc8f188c7ab9ce53d3"></a>

```c
#define PIN_P4_7__CMP1_OUT_B ALIF_PINMUX(4, 7, 6)
```

相关声明：[PIN_P4_7__CMP1_OUT_B](#a921f7c932359c5bc8f188c7ab9ce53d3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）4 的引脚（Pin）7：`CMP1_OUT_B`。

<a id="r_a456e61913b22b9d8a56be8b0377ac81e"></a>

```c
#define PIN_P5_0__GPIO ALIF_PINMUX(5, 0, 0)
```

相关声明：[PIN_P5_0__GPIO](#a456e61913b22b9d8a56be8b0377ac81e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.0` 的复用功能（Alternate Functions）。

<a id="r_a7515446e7f6b91cb8e9ad6059684ed5e"></a>

```c
#define PIN_P5_0__OSPI0_D0_B ALIF_PINMUX(5, 0, 1)
```

相关声明：[PIN_P5_0__OSPI0_D0_B](#a7515446e7f6b91cb8e9ad6059684ed5e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`OSPI0_D0_B`。

<a id="r_a70e357d53457779d10d0b21e4b58a306"></a>

```c
#define PIN_P5_0__UART1_RX_B ALIF_PINMUX(5, 0, 2)
```

相关声明：[PIN_P5_0__UART1_RX_B](#a70e357d53457779d10d0b21e4b58a306)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`UART1_RX_B`。

<a id="r_a8d7a46642529764190d788a4e6fd45ad"></a>

```c
#define PIN_P5_0__SPI0_MISO_B ALIF_PINMUX(5, 0, 3)
```

相关声明：[PIN_P5_0__SPI0_MISO_B](#a8d7a46642529764190d788a4e6fd45ad)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`SPI0_MISO_B`。

<a id="r_a19da3e4d236b8aead55eced77dbede8a"></a>

```c
#define PIN_P5_0__CDC_D0_A ALIF_PINMUX(5, 0, 4)
```

相关声明：[PIN_P5_0__CDC_D0_A](#a19da3e4d236b8aead55eced77dbede8a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`CDC_D0_A`。

<a id="r_a09144d6ba2498f87a362d6ed24d3b806"></a>

```c
#define PIN_P5_0__CAN0_RXD_B ALIF_PINMUX(5, 0, 5)
```

相关声明：[PIN_P5_0__CAN0_RXD_B](#a09144d6ba2498f87a362d6ed24d3b806)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`CAN0_RXD_B`。

<a id="r_a33aeb846f89757467e96fc37655d4560"></a>

```c
#define PIN_P5_0__DEBUG_PORT0 ALIF_PINMUX(5, 0, 6)
```

相关声明：[PIN_P5_0__DEBUG_PORT0](#a33aeb846f89757467e96fc37655d4560)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）0：`DEBUG_PORT0`。

<a id="r_a98fa74bbdae6f1f210c490cdc73d7cb8"></a>

```c
#define PIN_P5_1__GPIO ALIF_PINMUX(5, 1, 0)
```

相关声明：[PIN_P5_1__GPIO](#a98fa74bbdae6f1f210c490cdc73d7cb8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.1` 的复用功能（Alternate Functions）。

<a id="r_abd2a49b69427e6dd3d36041739e26e64"></a>

```c
#define PIN_P5_1__OSPI0_D1_B ALIF_PINMUX(5, 1, 1)
```

相关声明：[PIN_P5_1__OSPI0_D1_B](#abd2a49b69427e6dd3d36041739e26e64)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`OSPI0_D1_B`。

<a id="r_accef3fca5f47ce8a465ff8c16f485963"></a>

```c
#define PIN_P5_1__UART1_TX_B ALIF_PINMUX(5, 1, 2)
```

相关声明：[PIN_P5_1__UART1_TX_B](#accef3fca5f47ce8a465ff8c16f485963)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`UART1_TX_B`。

<a id="r_a02c0d84f1ce09a7db4f16344ce7d6e0f"></a>

```c
#define PIN_P5_1__SPI0_MOSI_B ALIF_PINMUX(5, 1, 3)
```

相关声明：[PIN_P5_1__SPI0_MOSI_B](#a02c0d84f1ce09a7db4f16344ce7d6e0f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`SPI0_MOSI_B`。

<a id="r_af760abc039a42c556a870cd724bc8cfd"></a>

```c
#define PIN_P5_1__CDC_D1_A ALIF_PINMUX(5, 1, 4)
```

相关声明：[PIN_P5_1__CDC_D1_A](#af760abc039a42c556a870cd724bc8cfd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`CDC_D1_A`。

<a id="r_a75e6ca2a4fbdf460b505179d29c4c340"></a>

```c
#define PIN_P5_1__CAN0_TXD_B ALIF_PINMUX(5, 1, 5)
```

相关声明：[PIN_P5_1__CAN0_TXD_B](#a75e6ca2a4fbdf460b505179d29c4c340)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`CAN0_TXD_B`。

<a id="r_a9300ca0c13f79f5fbe0cee6a407bb6a1"></a>

```c
#define PIN_P5_1__DEBUG_PORT1 ALIF_PINMUX(5, 1, 6)
```

相关声明：[PIN_P5_1__DEBUG_PORT1](#a9300ca0c13f79f5fbe0cee6a407bb6a1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）1：`DEBUG_PORT1`。

<a id="r_a97a74c55bf53c437a39b3f10cfa778bc"></a>

```c
#define PIN_P5_2__GPIO ALIF_PINMUX(5, 2, 0)
```

相关声明：[PIN_P5_2__GPIO](#a97a74c55bf53c437a39b3f10cfa778bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.2` 的复用功能（Alternate Functions）。

<a id="r_a9412174bfeabbc0ef5bac744684200e6"></a>

```c
#define PIN_P5_2__HFXO_OUT_B ALIF_PINMUX(5, 2, 1)
```

相关声明：[PIN_P5_2__HFXO_OUT_B](#a9412174bfeabbc0ef5bac744684200e6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`HFXO_OUT_B`。

<a id="r_a9d38ab0662de65a0c523e9def2eea72c"></a>

```c
#define PIN_P5_2__OSPI0_D2_B ALIF_PINMUX(5, 2, 2)
```

相关声明：[PIN_P5_2__OSPI0_D2_B](#a9d38ab0662de65a0c523e9def2eea72c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`OSPI0_D2_B`。

<a id="r_aef66774050c916f8a431df007e4a4721"></a>

```c
#define PIN_P5_2__UART2_RX_B ALIF_PINMUX(5, 2, 3)
```

相关声明：[PIN_P5_2__UART2_RX_B](#aef66774050c916f8a431df007e4a4721)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`UART2_RX_B`。

<a id="r_aa4e51a07e335aceeb1d4c7a0ba483945"></a>

```c
#define PIN_P5_2__SPI0_SCLK_B ALIF_PINMUX(5, 2, 4)
```

相关声明：[PIN_P5_2__SPI0_SCLK_B](#aa4e51a07e335aceeb1d4c7a0ba483945)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`SPI0_SCLK_B`。

<a id="r_aa54f58186118a8cc7b816e3c8e08670d"></a>

```c
#define PIN_P5_2__CDC_D2_A ALIF_PINMUX(5, 2, 5)
```

相关声明：[PIN_P5_2__CDC_D2_A](#aa54f58186118a8cc7b816e3c8e08670d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`CDC_D2_A`。

<a id="r_aeb0c6ac8de20eb3b7da621944e98970b"></a>

```c
#define PIN_P5_2__DEBUG_PORT2 ALIF_PINMUX(5, 2, 6)
```

相关声明：[PIN_P5_2__DEBUG_PORT2](#aeb0c6ac8de20eb3b7da621944e98970b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）2：`DEBUG_PORT2`。

<a id="r_af2c171dfdada8390ed0c80e115f024eb"></a>

```c
#define PIN_P5_3__GPIO ALIF_PINMUX(5, 3, 0)
```

相关声明：[PIN_P5_3__GPIO](#af2c171dfdada8390ed0c80e115f024eb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.3` 的复用功能（Alternate Functions）。

<a id="r_a26d1e825401e3265e1f84b6fe668bb4b"></a>

```c
#define PIN_P5_3__OSPI0_D3_B ALIF_PINMUX(5, 3, 1)
```

相关声明：[PIN_P5_3__OSPI0_D3_B](#a26d1e825401e3265e1f84b6fe668bb4b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`OSPI0_D3_B`。

<a id="r_ac655344000cbc93d5d59943a9a357f35"></a>

```c
#define PIN_P5_3__UART2_TX_B ALIF_PINMUX(5, 3, 2)
```

相关声明：[PIN_P5_3__UART2_TX_B](#ac655344000cbc93d5d59943a9a357f35)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`UART2_TX_B`。

<a id="r_a9bef667960418991b8dcd10c622659bc"></a>

```c
#define PIN_P5_3__SPI0_SS0_B ALIF_PINMUX(5, 3, 3)
```

相关声明：[PIN_P5_3__SPI0_SS0_B](#a9bef667960418991b8dcd10c622659bc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`SPI0_SS0_B`。

<a id="r_a9e39c3bab0ba922acc2ccfa570e8f768"></a>

```c
#define PIN_P5_3__CDC_D3_A ALIF_PINMUX(5, 3, 4)
```

相关声明：[PIN_P5_3__CDC_D3_A](#a9e39c3bab0ba922acc2ccfa570e8f768)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`CDC_D3_A`。

<a id="r_afcc5c2f160ddea37e8d27066e1f56f0b"></a>

```c
#define PIN_P5_3__DEBUG_PORT3 ALIF_PINMUX(5, 3, 5)
```

相关声明：[PIN_P5_3__DEBUG_PORT3](#afcc5c2f160ddea37e8d27066e1f56f0b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）3：`DEBUG_PORT3`。

<a id="r_a6846e3f2b170cb7a3216f81e5ec3b30e"></a>

```c
#define PIN_P5_4__GPIO ALIF_PINMUX(5, 4, 0)
```

相关声明：[PIN_P5_4__GPIO](#a6846e3f2b170cb7a3216f81e5ec3b30e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.4` 的复用功能（Alternate Functions）。

<a id="r_acfae802a9c0d84dd7fe2fa7ae137da32"></a>

```c
#define PIN_P5_4__OSPI0_D4_B ALIF_PINMUX(5, 4, 1)
```

相关声明：[PIN_P5_4__OSPI0_D4_B](#acfae802a9c0d84dd7fe2fa7ae137da32)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`OSPI0_D4_B`。

<a id="r_ae8575f29fe033284403815de52e2b0b1"></a>

```c
#define PIN_P5_4__UART3_CTS_A ALIF_PINMUX(5, 4, 2)
```

相关声明：[PIN_P5_4__UART3_CTS_A](#ae8575f29fe033284403815de52e2b0b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`UART3_CTS_A`。

<a id="r_aba535b3b3becd72a6155033116e157cf"></a>

```c
#define PIN_P5_4__LPPDM_C0_C ALIF_PINMUX(5, 4, 3)
```

相关声明：[PIN_P5_4__LPPDM_C0_C](#aba535b3b3becd72a6155033116e157cf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`LPPDM_C0_C`。

<a id="r_ad8ff5c1bc4ae11a8417d37c08725ca1e"></a>

```c
#define PIN_P5_4__SPI0_SS1_B ALIF_PINMUX(5, 4, 4)
```

相关声明：[PIN_P5_4__SPI0_SS1_B](#ad8ff5c1bc4ae11a8417d37c08725ca1e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`SPI0_SS1_B`。

<a id="r_a3492ede5bc47cdcbc93ffa2c618d9de5"></a>

```c
#define PIN_P5_4__CDC_D4_A ALIF_PINMUX(5, 4, 5)
```

相关声明：[PIN_P5_4__CDC_D4_A](#a3492ede5bc47cdcbc93ffa2c618d9de5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`CDC_D4_A`。

<a id="r_ab51b446a130c3e4d5ad5bcd224435ec8"></a>

```c
#define PIN_P5_4__DEBUG_PORT4 ALIF_PINMUX(5, 4, 6)
```

相关声明：[PIN_P5_4__DEBUG_PORT4](#ab51b446a130c3e4d5ad5bcd224435ec8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）4：`DEBUG_PORT4`。

<a id="r_a466c951ce8310bac71e4a36b062e3b48"></a>

```c
#define PIN_P5_5__GPIO ALIF_PINMUX(5, 5, 0)
```

相关声明：[PIN_P5_5__GPIO](#a466c951ce8310bac71e4a36b062e3b48)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.5` 的复用功能（Alternate Functions）。

<a id="r_aee3d8c711f4960174ef78aaa66f546a4"></a>

```c
#define PIN_P5_5__OSPI0_D5_B ALIF_PINMUX(5, 5, 1)
```

相关声明：[PIN_P5_5__OSPI0_D5_B](#aee3d8c711f4960174ef78aaa66f546a4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`OSPI0_D5_B`。

<a id="r_aefd41d2a46a675a37216980f16e2fd58"></a>

```c
#define PIN_P5_5__UART3_RTS_A ALIF_PINMUX(5, 5, 2)
```

相关声明：[PIN_P5_5__UART3_RTS_A](#aefd41d2a46a675a37216980f16e2fd58)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`UART3_RTS_A`。

<a id="r_affea3cc1741e8f1d8b481d382231e8b2"></a>

```c
#define PIN_P5_5__LPPDM_C1_C ALIF_PINMUX(5, 5, 3)
```

相关声明：[PIN_P5_5__LPPDM_C1_C](#affea3cc1741e8f1d8b481d382231e8b2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`LPPDM_C1_C`。

<a id="r_ac6c32c362dd4a8136e7afba82bd2ed26"></a>

```c
#define PIN_P5_5__SPI0_SS2_B ALIF_PINMUX(5, 5, 4)
```

相关声明：[PIN_P5_5__SPI0_SS2_B](#ac6c32c362dd4a8136e7afba82bd2ed26)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`SPI0_SS2_B`。

<a id="r_ab8b92f2241fd09c81a4e881e4c12e0a3"></a>

```c
#define PIN_P5_5__CDC_D5_A ALIF_PINMUX(5, 5, 5)
```

相关声明：[PIN_P5_5__CDC_D5_A](#ab8b92f2241fd09c81a4e881e4c12e0a3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`CDC_D5_A`。

<a id="r_aa6991f74e9a8bc6f4559e5463862e142"></a>

```c
#define PIN_P5_5__DEBUG_PORT5 ALIF_PINMUX(5, 5, 6)
```

相关声明：[PIN_P5_5__DEBUG_PORT5](#aa6991f74e9a8bc6f4559e5463862e142)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）5：`DEBUG_PORT5`。

<a id="r_acd3416c5b74cd24d02c29e3144d63436"></a>

```c
#define PIN_P5_6__GPIO ALIF_PINMUX(5, 6, 0)
```

相关声明：[PIN_P5_6__GPIO](#acd3416c5b74cd24d02c29e3144d63436)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.6` 的复用功能（Alternate Functions）。

<a id="r_a992d43f89e37b80a8da4608e67529c1b"></a>

```c
#define PIN_P5_6__OSPI0_D6_B ALIF_PINMUX(5, 6, 1)
```

相关声明：[PIN_P5_6__OSPI0_D6_B](#a992d43f89e37b80a8da4608e67529c1b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`OSPI0_D6_B`。

<a id="r_a3bd03266c3d91de23071a3d0241e97e3"></a>

```c
#define PIN_P5_6__UART1_CTS_B ALIF_PINMUX(5, 6, 2)
```

相关声明：[PIN_P5_6__UART1_CTS_B](#a3bd03266c3d91de23071a3d0241e97e3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`UART1_CTS_B`。

<a id="r_abdd1f1a77582773e32e38f4f3d7b7f9f"></a>

```c
#define PIN_P5_6__LPPDM_D0_C ALIF_PINMUX(5, 6, 3)
```

相关声明：[PIN_P5_6__LPPDM_D0_C](#abdd1f1a77582773e32e38f4f3d7b7f9f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`LPPDM_D0_C`。

<a id="r_a1fef293fbc151e83a6059a043296696a"></a>

```c
#define PIN_P5_6__LPSPI_MISO_B ALIF_PINMUX(5, 6, 4)
```

相关声明：[PIN_P5_6__LPSPI_MISO_B](#a1fef293fbc151e83a6059a043296696a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`LPSPI_MISO_B`。

<a id="r_a75155e55cff32f1b264994b3f795d7cd"></a>

```c
#define PIN_P5_6__CDC_D6_A ALIF_PINMUX(5, 6, 5)
```

相关声明：[PIN_P5_6__CDC_D6_A](#a75155e55cff32f1b264994b3f795d7cd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`CDC_D6_A`。

<a id="r_a6a08b389c3a815867e60c3120b0ea33c"></a>

```c
#define PIN_P5_6__DEBUG_PORT6 ALIF_PINMUX(5, 6, 6)
```

相关声明：[PIN_P5_6__DEBUG_PORT6](#a6a08b389c3a815867e60c3120b0ea33c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）6：`DEBUG_PORT6`。

<a id="r_abc168fa2810d9a33b66d8899581c97ed"></a>

```c
#define PIN_P5_7__GPIO ALIF_PINMUX(5, 7, 0)
```

相关声明：[PIN_P5_7__GPIO](#abc168fa2810d9a33b66d8899581c97ed)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P5.7` 的复用功能（Alternate Functions）。

<a id="r_af2d4965c3a398c12ae01ddce15a3f1e6"></a>

```c
#define PIN_P5_7__OSPI0_D7_B ALIF_PINMUX(5, 7, 1)
```

相关声明：[PIN_P5_7__OSPI0_D7_B](#af2d4965c3a398c12ae01ddce15a3f1e6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`OSPI0_D7_B`。

<a id="r_a16337846b4c79f3bf2b8601bd2b97f91"></a>

```c
#define PIN_P5_7__UART1_RTS_B ALIF_PINMUX(5, 7, 2)
```

相关声明：[PIN_P5_7__UART1_RTS_B](#a16337846b4c79f3bf2b8601bd2b97f91)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`UART1_RTS_B`。

<a id="r_ac1a9c0edd0801e204c2c73e804bc2b88"></a>

```c
#define PIN_P5_7__LPPDM_D1_C ALIF_PINMUX(5, 7, 3)
```

相关声明：[PIN_P5_7__LPPDM_D1_C](#ac1a9c0edd0801e204c2c73e804bc2b88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`LPPDM_D1_C`。

<a id="r_a101d18b757575a6b4d774eb367e47f1d"></a>

```c
#define PIN_P5_7__LPSPI_MOSI_B ALIF_PINMUX(5, 7, 4)
```

相关声明：[PIN_P5_7__LPSPI_MOSI_B](#a101d18b757575a6b4d774eb367e47f1d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`LPSPI_MOSI_B`。

<a id="r_a9a269398cead600a0730cf59ee346efe"></a>

```c
#define PIN_P5_7__CDC_D7_A ALIF_PINMUX(5, 7, 5)
```

相关声明：[PIN_P5_7__CDC_D7_A](#a9a269398cead600a0730cf59ee346efe)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`CDC_D7_A`。

<a id="r_a7a7892f2e7caa1291c8a75505f2cd4ef"></a>

```c
#define PIN_P5_7__DEBUG_PORT7 ALIF_PINMUX(5, 7, 6)
```

相关声明：[PIN_P5_7__DEBUG_PORT7](#a7a7892f2e7caa1291c8a75505f2cd4ef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）5 的引脚（Pin）7：`DEBUG_PORT7`。

<a id="r_ae7ade9dfd32e609fb86f13f6525953fc"></a>

```c
#define PIN_P6_0__GPIO ALIF_PINMUX(6, 0, 0)
```

相关声明：[PIN_P6_0__GPIO](#ae7ade9dfd32e609fb86f13f6525953fc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.0` 的复用功能（Alternate Functions）。

<a id="r_af006833ac80c14da05e6a4599a24ac61"></a>

```c
#define PIN_P6_0__OSPI0_D0_C ALIF_PINMUX(6, 0, 1)
```

相关声明：[PIN_P6_0__OSPI0_D0_C](#af006833ac80c14da05e6a4599a24ac61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`OSPI0_D0_C`。

<a id="r_a79570f9e4a4d6cf2551a9610c48ef2b9"></a>

```c
#define PIN_P6_0__UART4_DE_B ALIF_PINMUX(6, 0, 2)
```

相关声明：[PIN_P6_0__UART4_DE_B](#a79570f9e4a4d6cf2551a9610c48ef2b9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`UART4_DE_B`。

<a id="r_a5bb14125f4edce700f4ec3003446446c"></a>

```c
#define PIN_P6_0__LPSPI_SS_B ALIF_PINMUX(6, 0, 3)
```

相关声明：[PIN_P6_0__LPSPI_SS_B](#a5bb14125f4edce700f4ec3003446446c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`LPSPI_SS_B`。

<a id="r_a7278e3b97a506751e694bedd1ed07f72"></a>

```c
#define PIN_P6_0__UT0_T0_B ALIF_PINMUX(6, 0, 4)
```

相关声明：[PIN_P6_0__UT0_T0_B](#a7278e3b97a506751e694bedd1ed07f72)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`UT0_T0_B`。

<a id="r_a8cdbf1027a1529384f1a861b04036391"></a>

```c
#define PIN_P6_0__SD_D0_B ALIF_PINMUX(6, 0, 5)
```

相关声明：[PIN_P6_0__SD_D0_B](#a8cdbf1027a1529384f1a861b04036391)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`SD_D0_B`。

<a id="r_a34729c1d8880ed50f395c50a2fe51e28"></a>

```c
#define PIN_P6_0__CDC_D8_A ALIF_PINMUX(6, 0, 6)
```

相关声明：[PIN_P6_0__CDC_D8_A](#a34729c1d8880ed50f395c50a2fe51e28)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）0：`CDC_D8_A`。

<a id="r_ad55f5467ffabdbffd5b51ddfeaed9c4f"></a>

```c
#define PIN_P6_1__GPIO ALIF_PINMUX(6, 1, 0)
```

相关声明：[PIN_P6_1__GPIO](#ad55f5467ffabdbffd5b51ddfeaed9c4f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.1` 的复用功能（Alternate Functions）。

<a id="r_aa0c327b4b44ee5068c84f65827555817"></a>

```c
#define PIN_P6_1__OSPI0_D1_C ALIF_PINMUX(6, 1, 1)
```

相关声明：[PIN_P6_1__OSPI0_D1_C](#aa0c327b4b44ee5068c84f65827555817)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`OSPI0_D1_C`。

<a id="r_aeb4ee42999e56e3a6c98cf66e476be59"></a>

```c
#define PIN_P6_1__UART5_DE_A ALIF_PINMUX(6, 1, 2)
```

相关声明：[PIN_P6_1__UART5_DE_A](#aeb4ee42999e56e3a6c98cf66e476be59)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`UART5_DE_A`。

<a id="r_acc7a686a7268479f6f114f354a022bf5"></a>

```c
#define PIN_P6_1__SPI1_MISO_B ALIF_PINMUX(6, 1, 3)
```

相关声明：[PIN_P6_1__SPI1_MISO_B](#acc7a686a7268479f6f114f354a022bf5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`SPI1_MISO_B`。

<a id="r_ace62f048486756791fdfdc9dd67b1057"></a>

```c
#define PIN_P6_1__UT0_T1_B ALIF_PINMUX(6, 1, 4)
```

相关声明：[PIN_P6_1__UT0_T1_B](#ace62f048486756791fdfdc9dd67b1057)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`UT0_T1_B`。

<a id="r_a9830bcd6296f620190099a1d42afeb94"></a>

```c
#define PIN_P6_1__SD_D1_B ALIF_PINMUX(6, 1, 5)
```

相关声明：[PIN_P6_1__SD_D1_B](#a9830bcd6296f620190099a1d42afeb94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`SD_D1_B`。

<a id="r_a6efed7a051659015ba52b794a8307682"></a>

```c
#define PIN_P6_1__CDC_D9_A ALIF_PINMUX(6, 1, 6)
```

相关声明：[PIN_P6_1__CDC_D9_A](#a6efed7a051659015ba52b794a8307682)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）1：`CDC_D9_A`。

<a id="r_adae4d80fc2a0fb040a8eed5c89e72cdd"></a>

```c
#define PIN_P6_2__GPIO ALIF_PINMUX(6, 2, 0)
```

相关声明：[PIN_P6_2__GPIO](#adae4d80fc2a0fb040a8eed5c89e72cdd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.2` 的复用功能（Alternate Functions）。

<a id="r_a1a29ae10d58edee6e97fd88d3057f1d6"></a>

```c
#define PIN_P6_2__OSPI0_D2_C ALIF_PINMUX(6, 2, 1)
```

相关声明：[PIN_P6_2__OSPI0_D2_C](#a1a29ae10d58edee6e97fd88d3057f1d6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`OSPI0_D2_C`。

<a id="r_a9bae739436d46b7844632df7afa34d94"></a>

```c
#define PIN_P6_2__UART2_CTS_A ALIF_PINMUX(6, 2, 2)
```

相关声明：[PIN_P6_2__UART2_CTS_A](#a9bae739436d46b7844632df7afa34d94)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`UART2_CTS_A`。

<a id="r_a011a62ceebd9b9ce35e4123833649fb0"></a>

```c
#define PIN_P6_2__SPI1_MOSI_B ALIF_PINMUX(6, 2, 3)
```

相关声明：[PIN_P6_2__SPI1_MOSI_B](#a011a62ceebd9b9ce35e4123833649fb0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`SPI1_MOSI_B`。

<a id="r_a99d44c64afab8fdd36300b15cd2994ab"></a>

```c
#define PIN_P6_2__UT1_T0_B ALIF_PINMUX(6, 2, 4)
```

相关声明：[PIN_P6_2__UT1_T0_B](#a99d44c64afab8fdd36300b15cd2994ab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`UT1_T0_B`。

<a id="r_accdb6fb802aa3b5cf02c6a71e85289a9"></a>

```c
#define PIN_P6_2__SD_D2_B ALIF_PINMUX(6, 2, 5)
```

相关声明：[PIN_P6_2__SD_D2_B](#accdb6fb802aa3b5cf02c6a71e85289a9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`SD_D2_B`。

<a id="r_ad0983e6b2d0c0cf85a14897416d037f0"></a>

```c
#define PIN_P6_2__CDC_D10_A ALIF_PINMUX(6, 2, 6)
```

相关声明：[PIN_P6_2__CDC_D10_A](#ad0983e6b2d0c0cf85a14897416d037f0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）2：`CDC_D10_A`。

<a id="r_a9c055a8795fbd5a4145bf758a72d1d23"></a>

```c
#define PIN_P6_3__GPIO ALIF_PINMUX(6, 3, 0)
```

相关声明：[PIN_P6_3__GPIO](#a9c055a8795fbd5a4145bf758a72d1d23)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.3` 的复用功能（Alternate Functions）。

<a id="r_ab9ef591fd0935f7082f8a08d31f3393f"></a>

```c
#define PIN_P6_3__OSPI0_D3_C ALIF_PINMUX(6, 3, 1)
```

相关声明：[PIN_P6_3__OSPI0_D3_C](#ab9ef591fd0935f7082f8a08d31f3393f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`OSPI0_D3_C`。

<a id="r_a6407df773a1b7922599c36f9d5ba134f"></a>

```c
#define PIN_P6_3__UART2_RTS_A ALIF_PINMUX(6, 3, 2)
```

相关声明：[PIN_P6_3__UART2_RTS_A](#a6407df773a1b7922599c36f9d5ba134f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`UART2_RTS_A`。

<a id="r_ade2d09480c128ca2346db206a5c31dc2"></a>

```c
#define PIN_P6_3__SPI1_SCLK_B ALIF_PINMUX(6, 3, 3)
```

相关声明：[PIN_P6_3__SPI1_SCLK_B](#ade2d09480c128ca2346db206a5c31dc2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`SPI1_SCLK_B`。

<a id="r_a81929813f463bf3e98dcec0012cadd6c"></a>

```c
#define PIN_P6_3__UT1_T1_B ALIF_PINMUX(6, 3, 4)
```

相关声明：[PIN_P6_3__UT1_T1_B](#a81929813f463bf3e98dcec0012cadd6c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`UT1_T1_B`。

<a id="r_a0a0be736abe9bfd71290393a24faca36"></a>

```c
#define PIN_P6_3__SD_D3_B ALIF_PINMUX(6, 3, 5)
```

相关声明：[PIN_P6_3__SD_D3_B](#a0a0be736abe9bfd71290393a24faca36)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`SD_D3_B`。

<a id="r_af667c27ea23d08184baaa71fda64b915"></a>

```c
#define PIN_P6_3__CDC_D11_A ALIF_PINMUX(6, 3, 6)
```

相关声明：[PIN_P6_3__CDC_D11_A](#af667c27ea23d08184baaa71fda64b915)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）3：`CDC_D11_A`。

<a id="r_a80712cd6a9a977af7a2f879634daf24d"></a>

```c
#define PIN_P6_4__GPIO ALIF_PINMUX(6, 4, 0)
```

相关声明：[PIN_P6_4__GPIO](#a80712cd6a9a977af7a2f879634daf24d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.4` 的复用功能（Alternate Functions）。

<a id="r_a587f62993920d1f067ce5b5119b05aab"></a>

```c
#define PIN_P6_4__OSPI0_D4_C ALIF_PINMUX(6, 4, 1)
```

相关声明：[PIN_P6_4__OSPI0_D4_C](#a587f62993920d1f067ce5b5119b05aab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`OSPI0_D4_C`。

<a id="r_a3ce358cbdd477ef4755e0a59e5d62b22"></a>

```c
#define PIN_P6_4__UART2_CTS_B ALIF_PINMUX(6, 4, 2)
```

相关声明：[PIN_P6_4__UART2_CTS_B](#a3ce358cbdd477ef4755e0a59e5d62b22)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`UART2_CTS_B`。

<a id="r_a4097acd4e3c33280170dbea58ab20604"></a>

```c
#define PIN_P6_4__SPI1_SS0_B ALIF_PINMUX(6, 4, 3)
```

相关声明：[PIN_P6_4__SPI1_SS0_B](#a4097acd4e3c33280170dbea58ab20604)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`SPI1_SS0_B`。

<a id="r_a74d24395ae08b32dacd5c3160dd492c1"></a>

```c
#define PIN_P6_4__UT2_T0_B ALIF_PINMUX(6, 4, 4)
```

相关声明：[PIN_P6_4__UT2_T0_B](#a74d24395ae08b32dacd5c3160dd492c1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`UT2_T0_B`。

<a id="r_a2cf67978227d7711caa02bd1e6106be6"></a>

```c
#define PIN_P6_4__SD_D4_B ALIF_PINMUX(6, 4, 5)
```

相关声明：[PIN_P6_4__SD_D4_B](#a2cf67978227d7711caa02bd1e6106be6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`SD_D4_B`。

<a id="r_a19f9eb6a8bf2182bf472932289fcd81a"></a>

```c
#define PIN_P6_4__CDC_D12_A ALIF_PINMUX(6, 4, 6)
```

相关声明：[PIN_P6_4__CDC_D12_A](#a19f9eb6a8bf2182bf472932289fcd81a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）4：`CDC_D12_A`。

<a id="r_a4f8cb1991ad80690327a9272f790c7fa"></a>

```c
#define PIN_P6_5__GPIO ALIF_PINMUX(6, 5, 0)
```

相关声明：[PIN_P6_5__GPIO](#a4f8cb1991ad80690327a9272f790c7fa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.5` 的复用功能（Alternate Functions）。

<a id="r_ae178273fd0d60e578038153dfa3d44d2"></a>

```c
#define PIN_P6_5__OSPI0_D5_C ALIF_PINMUX(6, 5, 1)
```

相关声明：[PIN_P6_5__OSPI0_D5_C](#ae178273fd0d60e578038153dfa3d44d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`OSPI0_D5_C`。

<a id="r_ac1b09ec40a2a0d186be393ce2a22bb6e"></a>

```c
#define PIN_P6_5__UART2_RTS_B ALIF_PINMUX(6, 5, 2)
```

相关声明：[PIN_P6_5__UART2_RTS_B](#ac1b09ec40a2a0d186be393ce2a22bb6e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`UART2_RTS_B`。

<a id="r_af896508d8b1829141300d9c174c6a4dc"></a>

```c
#define PIN_P6_5__SPI1_SS1_B ALIF_PINMUX(6, 5, 3)
```

相关声明：[PIN_P6_5__SPI1_SS1_B](#af896508d8b1829141300d9c174c6a4dc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`SPI1_SS1_B`。

<a id="r_a38159c76a1cb17b4dbd18d339585dfcc"></a>

```c
#define PIN_P6_5__UT2_T1_B ALIF_PINMUX(6, 5, 4)
```

相关声明：[PIN_P6_5__UT2_T1_B](#a38159c76a1cb17b4dbd18d339585dfcc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`UT2_T1_B`。

<a id="r_a351d27e39ee616cec1ea000692dbaa00"></a>

```c
#define PIN_P6_5__SD_D5_B ALIF_PINMUX(6, 5, 5)
```

相关声明：[PIN_P6_5__SD_D5_B](#a351d27e39ee616cec1ea000692dbaa00)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`SD_D5_B`。

<a id="r_a5009293a09cb76741e2ee7d496de4a01"></a>

```c
#define PIN_P6_5__CDC_D13_A ALIF_PINMUX(6, 5, 6)
```

相关声明：[PIN_P6_5__CDC_D13_A](#a5009293a09cb76741e2ee7d496de4a01)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）5：`CDC_D13_A`。

<a id="r_ae379d12c8cb8b76c585b3745eef14bfc"></a>

```c
#define PIN_P6_6__GPIO ALIF_PINMUX(6, 6, 0)
```

相关声明：[PIN_P6_6__GPIO](#ae379d12c8cb8b76c585b3745eef14bfc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.6` 的复用功能（Alternate Functions）。

<a id="r_a8adab274d4857b76f38a42a19c7af021"></a>

```c
#define PIN_P6_6__OSPI0_D6_C ALIF_PINMUX(6, 6, 1)
```

相关声明：[PIN_P6_6__OSPI0_D6_C](#a8adab274d4857b76f38a42a19c7af021)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`OSPI0_D6_C`。

<a id="r_a149c5ebf20984a0032f56170946e1b76"></a>

```c
#define PIN_P6_6__UART0_CTS_B ALIF_PINMUX(6, 6, 2)
```

相关声明：[PIN_P6_6__UART0_CTS_B](#a149c5ebf20984a0032f56170946e1b76)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`UART0_CTS_B`。

<a id="r_a88f58696cc0671871bbf7e67d96411ba"></a>

```c
#define PIN_P6_6__SPI1_SS2_B ALIF_PINMUX(6, 6, 3)
```

相关声明：[PIN_P6_6__SPI1_SS2_B](#a88f58696cc0671871bbf7e67d96411ba)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`SPI1_SS2_B`。

<a id="r_aa9ff5aa10ea39c234104f716b17487d8"></a>

```c
#define PIN_P6_6__UT3_T0_B ALIF_PINMUX(6, 6, 4)
```

相关声明：[PIN_P6_6__UT3_T0_B](#aa9ff5aa10ea39c234104f716b17487d8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`UT3_T0_B`。

<a id="r_a6f6b543054d09e34217fd25d761fa1d5"></a>

```c
#define PIN_P6_6__SD_D6_B ALIF_PINMUX(6, 6, 5)
```

相关声明：[PIN_P6_6__SD_D6_B](#a6f6b543054d09e34217fd25d761fa1d5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`SD_D6_B`。

<a id="r_aac2a8a26747c7d6bbd4a7c74602f3867"></a>

```c
#define PIN_P6_6__CDC_D14_A ALIF_PINMUX(6, 6, 6)
```

相关声明：[PIN_P6_6__CDC_D14_A](#aac2a8a26747c7d6bbd4a7c74602f3867)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）6：`CDC_D14_A`。

<a id="r_a1e66098ffe67eddd23463192fcd1fbcd"></a>

```c
#define PIN_P6_7__GPIO ALIF_PINMUX(6, 7, 0)
```

相关声明：[PIN_P6_7__GPIO](#a1e66098ffe67eddd23463192fcd1fbcd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P6.7` 的复用功能（Alternate Functions）。

<a id="r_aef69daa6cb1613f9c4e417eaa709d9df"></a>

```c
#define PIN_P6_7__OSPI0_D7_C ALIF_PINMUX(6, 7, 1)
```

相关声明：[PIN_P6_7__OSPI0_D7_C](#aef69daa6cb1613f9c4e417eaa709d9df)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`OSPI0_D7_C`。

<a id="r_ae4dd7c19afbead2d7459b0e317238ae4"></a>

```c
#define PIN_P6_7__UART0_RTS_B ALIF_PINMUX(6, 7, 2)
```

相关声明：[PIN_P6_7__UART0_RTS_B](#ae4dd7c19afbead2d7459b0e317238ae4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`UART0_RTS_B`。

<a id="r_a225e78df9676b56259829bd042385839"></a>

```c
#define PIN_P6_7__SPI2_SS2_C ALIF_PINMUX(6, 7, 3)
```

相关声明：[PIN_P6_7__SPI2_SS2_C](#a225e78df9676b56259829bd042385839)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`SPI2_SS2_C`。

<a id="r_a5b82e1c93054b79ad2496d3929c81682"></a>

```c
#define PIN_P6_7__UT3_T1_B ALIF_PINMUX(6, 7, 4)
```

相关声明：[PIN_P6_7__UT3_T1_B](#a5b82e1c93054b79ad2496d3929c81682)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`UT3_T1_B`。

<a id="r_a81371fe588865cec958fa73ef38bcc8b"></a>

```c
#define PIN_P6_7__SD_D7_B ALIF_PINMUX(6, 7, 5)
```

相关声明：[PIN_P6_7__SD_D7_B](#a81371fe588865cec958fa73ef38bcc8b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`SD_D7_B`。

<a id="r_a77ba808a6080decf1043e8e2a469ba19"></a>

```c
#define PIN_P6_7__CDC_D15_A ALIF_PINMUX(6, 7, 6)
```

相关声明：[PIN_P6_7__CDC_D15_A](#a77ba808a6080decf1043e8e2a469ba19)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）6 的引脚（Pin）7：`CDC_D15_A`。

<a id="r_ac5e4bcb47b0ccd35d7458401dbe81233"></a>

```c
#define PIN_P7_0__GPIO ALIF_PINMUX(7, 0, 0)
```

相关声明：[PIN_P7_0__GPIO](#ac5e4bcb47b0ccd35d7458401dbe81233)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.0` 的复用功能（Alternate Functions）。

<a id="r_a81333f2343eb5b4490a59236c211dce9"></a>

```c
#define PIN_P7_0__OSPI0_SCLK_C ALIF_PINMUX(7, 0, 1)
```

相关声明：[PIN_P7_0__OSPI0_SCLK_C](#a81333f2343eb5b4490a59236c211dce9)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`OSPI0_SCLK_C`。

<a id="r_ac02486e63bf2d9a793552ab7e8c57fab"></a>

```c
#define PIN_P7_0__LPUART_RX_B ALIF_PINMUX(7, 0, 2)
```

相关声明：[PIN_P7_0__LPUART_RX_B](#ac02486e63bf2d9a793552ab7e8c57fab)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`LPUART_RX_B`。

<a id="r_ad7e701bd246ba906f0ccd67dfae4ff96"></a>

```c
#define PIN_P7_0__SPI2_MISO_B ALIF_PINMUX(7, 0, 3)
```

相关声明：[PIN_P7_0__SPI2_MISO_B](#ad7e701bd246ba906f0ccd67dfae4ff96)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`SPI2_MISO_B`。

<a id="r_a1fde60e018d010f91f259fe2684f2bef"></a>

```c
#define PIN_P7_0__I2C0_SDA_C ALIF_PINMUX(7, 0, 4)
```

相关声明：[PIN_P7_0__I2C0_SDA_C](#a1fde60e018d010f91f259fe2684f2bef)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`I2C0_SDA_C`。

<a id="r_ac61deb751bad112fb5744f0b14556b75"></a>

```c
#define PIN_P7_0__LPCAM_D0_B ALIF_PINMUX(7, 0, 5)
```

相关声明：[PIN_P7_0__LPCAM_D0_B](#ac61deb751bad112fb5744f0b14556b75)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`LPCAM_D0_B`。

<a id="r_a434fbeabd67039cc7fbb8bf0f3827519"></a>

```c
#define PIN_P7_0__CDC_D16_A ALIF_PINMUX(7, 0, 6)
```

相关声明：[PIN_P7_0__CDC_D16_A](#a434fbeabd67039cc7fbb8bf0f3827519)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）0：`CDC_D16_A`。

<a id="r_afd333ffdddac335d52e506deb72eacaf"></a>

```c
#define PIN_P7_1__GPIO ALIF_PINMUX(7, 1, 0)
```

相关声明：[PIN_P7_1__GPIO](#afd333ffdddac335d52e506deb72eacaf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.1` 的复用功能（Alternate Functions）。

<a id="r_a40442bb3dc5803462792e7f422a6cea8"></a>

```c
#define PIN_P7_1__OSPI0_SCLKN_C ALIF_PINMUX(7, 1, 1)
```

相关声明：[PIN_P7_1__OSPI0_SCLKN_C](#a40442bb3dc5803462792e7f422a6cea8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`OSPI0_SCLKN_C`。

<a id="r_ae0167e359b7e8636c8ac16a70e1e8268"></a>

```c
#define PIN_P7_1__LPUART_TX_B ALIF_PINMUX(7, 1, 2)
```

相关声明：[PIN_P7_1__LPUART_TX_B](#ae0167e359b7e8636c8ac16a70e1e8268)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`LPUART_TX_B`。

<a id="r_aabd05e34bb204e9b9a11a27a91a8f4d2"></a>

```c
#define PIN_P7_1__SPI2_MOSI_B ALIF_PINMUX(7, 1, 3)
```

相关声明：[PIN_P7_1__SPI2_MOSI_B](#aabd05e34bb204e9b9a11a27a91a8f4d2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`SPI2_MOSI_B`。

<a id="r_af1c7a7f1fc1d87b7036a5ac346c435a7"></a>

```c
#define PIN_P7_1__I2C0_SCL_C ALIF_PINMUX(7, 1, 4)
```

相关声明：[PIN_P7_1__I2C0_SCL_C](#af1c7a7f1fc1d87b7036a5ac346c435a7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`I2C0_SCL_C`。

<a id="r_a4a5713a8962c62a0a8bcd0766da483fc"></a>

```c
#define PIN_P7_1__LPCAM_D1_B ALIF_PINMUX(7, 1, 5)
```

相关声明：[PIN_P7_1__LPCAM_D1_B](#a4a5713a8962c62a0a8bcd0766da483fc)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`LPCAM_D1_B`。

<a id="r_a41a1d3b230284cc4de145da552bc072f"></a>

```c
#define PIN_P7_1__CDC_D17_A ALIF_PINMUX(7, 1, 6)
```

相关声明：[PIN_P7_1__CDC_D17_A](#a41a1d3b230284cc4de145da552bc072f)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）1：`CDC_D17_A`。

<a id="r_adc16259fec5582a1e6ebc9cb8a825c03"></a>

```c
#define PIN_P7_2__GPIO ALIF_PINMUX(7, 2, 0)
```

相关声明：[PIN_P7_2__GPIO](#adc16259fec5582a1e6ebc9cb8a825c03)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.2` 的复用功能（Alternate Functions）。

<a id="r_a7123e2e8362601d8f25102c6c9ea14c3"></a>

```c
#define PIN_P7_2__OSPI0_SS0_C ALIF_PINMUX(7, 2, 1)
```

相关声明：[PIN_P7_2__OSPI0_SS0_C](#a7123e2e8362601d8f25102c6c9ea14c3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`OSPI0_SS0_C`。

<a id="r_a2ac043357aa1f8f702f196f070023af4"></a>

```c
#define PIN_P7_2__LPUART_CTS_B ALIF_PINMUX(7, 2, 2)
```

相关声明：[PIN_P7_2__LPUART_CTS_B](#a2ac043357aa1f8f702f196f070023af4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`LPUART_CTS_B`。

<a id="r_a176b3c4d6fc1f304ff10fe307a175ac7"></a>

```c
#define PIN_P7_2__SPI2_SCLK_B ALIF_PINMUX(7, 2, 3)
```

相关声明：[PIN_P7_2__SPI2_SCLK_B](#a176b3c4d6fc1f304ff10fe307a175ac7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`SPI2_SCLK_B`。

<a id="r_a803ef3f2d107d05670bba596998fca2a"></a>

```c
#define PIN_P7_2__I2C1_SDA_C ALIF_PINMUX(7, 2, 4)
```

相关声明：[PIN_P7_2__I2C1_SDA_C](#a803ef3f2d107d05670bba596998fca2a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`I2C1_SDA_C`。

<a id="r_a406797f78dd005ce0485b9d2807fc8f3"></a>

```c
#define PIN_P7_2__LPCAM_D2_B ALIF_PINMUX(7, 2, 5)
```

相关声明：[PIN_P7_2__LPCAM_D2_B](#a406797f78dd005ce0485b9d2807fc8f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`LPCAM_D2_B`。

<a id="r_afc62dda2e707d7d994e3d31b72911caa"></a>

```c
#define PIN_P7_2__CDC_D18_A ALIF_PINMUX(7, 2, 6)
```

相关声明：[PIN_P7_2__CDC_D18_A](#afc62dda2e707d7d994e3d31b72911caa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）2：`CDC_D18_A`。

<a id="r_a75dbeec7072793acd5eaa20f0d0d1055"></a>

```c
#define PIN_P7_3__GPIO ALIF_PINMUX(7, 3, 0)
```

相关声明：[PIN_P7_3__GPIO](#a75dbeec7072793acd5eaa20f0d0d1055)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.3` 的复用功能（Alternate Functions）。

<a id="r_a1c916c92dca31a5ebf293130254c4a90"></a>

```c
#define PIN_P7_3__OSPI0_SS1_C ALIF_PINMUX(7, 3, 1)
```

相关声明：[PIN_P7_3__OSPI0_SS1_C](#a1c916c92dca31a5ebf293130254c4a90)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`OSPI0_SS1_C`。

<a id="r_a4ed1e54224d8b1cd53fb993e739ee817"></a>

```c
#define PIN_P7_3__LPUART_RTS_B ALIF_PINMUX(7, 3, 2)
```

相关声明：[PIN_P7_3__LPUART_RTS_B](#a4ed1e54224d8b1cd53fb993e739ee817)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`LPUART_RTS_B`。

<a id="r_a6e47c806b3893950d5c0100c93cd4b62"></a>

```c
#define PIN_P7_3__SPI2_SS0_B ALIF_PINMUX(7, 3, 3)
```

相关声明：[PIN_P7_3__SPI2_SS0_B](#a6e47c806b3893950d5c0100c93cd4b62)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`SPI2_SS0_B`。

<a id="r_a62c7010c5c2ec0aa887cdc198dc4ab61"></a>

```c
#define PIN_P7_3__I2C1_SCL_C ALIF_PINMUX(7, 3, 4)
```

相关声明：[PIN_P7_3__I2C1_SCL_C](#a62c7010c5c2ec0aa887cdc198dc4ab61)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`I2C1_SCL_C`。

<a id="r_a654db72e8024434dee055f3a3a1c2308"></a>

```c
#define PIN_P7_3__LPCAM_D3_B ALIF_PINMUX(7, 3, 5)
```

相关声明：[PIN_P7_3__LPCAM_D3_B](#a654db72e8024434dee055f3a3a1c2308)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`LPCAM_D3_B`。

<a id="r_acc8d18e6404550464314fa765a8fc821"></a>

```c
#define PIN_P7_3__CDC_D19_A ALIF_PINMUX(7, 3, 6)
```

相关声明：[PIN_P7_3__CDC_D19_A](#acc8d18e6404550464314fa765a8fc821)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）3：`CDC_D19_A`。

<a id="r_ae4761d31982dad9a275346a237d734c7"></a>

```c
#define PIN_P7_4__GPIO ALIF_PINMUX(7, 4, 0)
```

相关声明：[PIN_P7_4__GPIO](#ae4761d31982dad9a275346a237d734c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.4` 的复用功能（Alternate Functions）。

<a id="r_a166f0d58b8578261369787277e3a70d1"></a>

```c
#define PIN_P7_4__UART3_CTS_B ALIF_PINMUX(7, 4, 1)
```

相关声明：[PIN_P7_4__UART3_CTS_B](#a166f0d58b8578261369787277e3a70d1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`UART3_CTS_B`。

<a id="r_ae67ab14af06fffcc4e02c1247e3184f3"></a>

```c
#define PIN_P7_4__LPPDM_C2_C ALIF_PINMUX(7, 4, 2)
```

相关声明：[PIN_P7_4__LPPDM_C2_C](#ae67ab14af06fffcc4e02c1247e3184f3)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPPDM_C2_C`。

<a id="r_aa3fe8586c90b46938d06b25f468596de"></a>

```c
#define PIN_P7_4__SPI2_SS1_B ALIF_PINMUX(7, 4, 3)
```

相关声明：[PIN_P7_4__SPI2_SS1_B](#aa3fe8586c90b46938d06b25f468596de)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`SPI2_SS1_B`。

<a id="r_a43db86bba44a27ce84e2f1f11a62cece"></a>

```c
#define PIN_P7_4__LPI2C0_SCL_C ALIF_PINMUX(7, 4, 4)
```

相关声明：[PIN_P7_4__LPI2C0_SCL_C](#a43db86bba44a27ce84e2f1f11a62cece)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPI2C0_SCL_C`。

<a id="r_a4d2e0b66dae7d0082d4898b4392cb289"></a>

```c
#define PIN_P7_4__LPCAM_D4_B ALIF_PINMUX(7, 4, 5)
```

相关声明：[PIN_P7_4__LPCAM_D4_B](#a4d2e0b66dae7d0082d4898b4392cb289)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`LPCAM_D4_B`。

<a id="r_a10eb04884400107ff7db9327d92feb07"></a>

```c
#define PIN_P7_4__CDC_D20_A ALIF_PINMUX(7, 4, 6)
```

相关声明：[PIN_P7_4__CDC_D20_A](#a10eb04884400107ff7db9327d92feb07)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）4：`CDC_D20_A`。

<a id="r_ac47d162d1d4eb774e733fe27673c7c6b"></a>

```c
#define PIN_P7_5__GPIO ALIF_PINMUX(7, 5, 0)
```

相关声明：[PIN_P7_5__GPIO](#ac47d162d1d4eb774e733fe27673c7c6b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.5` 的复用功能（Alternate Functions）。

<a id="r_a34f0e74e10b4bdcedf5490f07bc94510"></a>

```c
#define PIN_P7_5__UART3_RTS_B ALIF_PINMUX(7, 5, 1)
```

相关声明：[PIN_P7_5__UART3_RTS_B](#a34f0e74e10b4bdcedf5490f07bc94510)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`UART3_RTS_B`。

<a id="r_a43b9e2e891e5c79f8f2fd049c2255fc7"></a>

```c
#define PIN_P7_5__LPPDM_D2_C ALIF_PINMUX(7, 5, 2)
```

相关声明：[PIN_P7_5__LPPDM_D2_C](#a43b9e2e891e5c79f8f2fd049c2255fc7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPPDM_D2_C`。

<a id="r_a6ec983760b4afbd138517dd7fae4333a"></a>

```c
#define PIN_P7_5__SPI2_SS2_B ALIF_PINMUX(7, 5, 3)
```

相关声明：[PIN_P7_5__SPI2_SS2_B](#a6ec983760b4afbd138517dd7fae4333a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`SPI2_SS2_B`。

<a id="r_a3fb7404ea8166f4ddd1ca38982d0da08"></a>

```c
#define PIN_P7_5__LPI2C0_SDA_C ALIF_PINMUX(7, 5, 4)
```

相关声明：[PIN_P7_5__LPI2C0_SDA_C](#a3fb7404ea8166f4ddd1ca38982d0da08)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPI2C0_SDA_C`。

<a id="r_a21c2ed1feba0129e42f54bd9a45f5064"></a>

```c
#define PIN_P7_5__LPCAM_D5_B ALIF_PINMUX(7, 5, 5)
```

相关声明：[PIN_P7_5__LPCAM_D5_B](#a21c2ed1feba0129e42f54bd9a45f5064)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`LPCAM_D5_B`。

<a id="r_aed833e3e5644c082d2aff8d460aa7ab4"></a>

```c
#define PIN_P7_5__CDC_D21_A ALIF_PINMUX(7, 5, 6)
```

相关声明：[PIN_P7_5__CDC_D21_A](#aed833e3e5644c082d2aff8d460aa7ab4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）5：`CDC_D21_A`。

<a id="r_ab95fc52f53c6a1703df290ac307871e4"></a>

```c
#define PIN_P7_6__GPIO ALIF_PINMUX(7, 6, 0)
```

相关声明：[PIN_P7_6__GPIO](#ab95fc52f53c6a1703df290ac307871e4)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.6` 的复用功能（Alternate Functions）。

<a id="r_ac86c6e2a402bc36f8b371b3b3c52c031"></a>

```c
#define PIN_P7_6__SEUART_RX_C ALIF_PINMUX(7, 6, 1)
```

相关声明：[PIN_P7_6__SEUART_RX_C](#ac86c6e2a402bc36f8b371b3b3c52c031)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`SEUART_RX_C`。

<a id="r_ae176791eedf1350b98257d2500273beb"></a>

```c
#define PIN_P7_6__UART5_RX_B ALIF_PINMUX(7, 6, 2)
```

相关声明：[PIN_P7_6__UART5_RX_B](#ae176791eedf1350b98257d2500273beb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`UART5_RX_B`。

<a id="r_ab4b3792dd2d61cee03eae788dbe32c88"></a>

```c
#define PIN_P7_6__LPPDM_C3_C ALIF_PINMUX(7, 6, 3)
```

相关声明：[PIN_P7_6__LPPDM_C3_C](#ab4b3792dd2d61cee03eae788dbe32c88)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPPDM_C3_C`。

<a id="r_ab78d246a64325058b5f1b7cb6cc11e15"></a>

```c
#define PIN_P7_6__SPI0_MISO_C ALIF_PINMUX(7, 6, 4)
```

相关声明：[PIN_P7_6__SPI0_MISO_C](#ab78d246a64325058b5f1b7cb6cc11e15)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`SPI0_MISO_C`。

<a id="r_abc5d28133fc1f9173df80aa2abe39955"></a>

```c
#define PIN_P7_6__LPCAM_D6_B ALIF_PINMUX(7, 6, 5)
```

相关声明：[PIN_P7_6__LPCAM_D6_B](#abc5d28133fc1f9173df80aa2abe39955)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`LPCAM_D6_B`。

<a id="r_abdbf76721d7bfbbb08a27266913b8ebf"></a>

```c
#define PIN_P7_6__CDC_D22_A ALIF_PINMUX(7, 6, 6)
```

相关声明：[PIN_P7_6__CDC_D22_A](#abdbf76721d7bfbbb08a27266913b8ebf)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）6：`CDC_D22_A`。

<a id="r_ae3abc19efe0b06fc7f3dc73c1eb040c7"></a>

```c
#define PIN_P7_7__GPIO ALIF_PINMUX(7, 7, 0)
```

相关声明：[PIN_P7_7__GPIO](#ae3abc19efe0b06fc7f3dc73c1eb040c7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P7.7` 的复用功能（Alternate Functions）。

<a id="r_a5c82a65c9a340d4ed121a7a03d295739"></a>

```c
#define PIN_P7_7__SEUART_TX_C ALIF_PINMUX(7, 7, 1)
```

相关声明：[PIN_P7_7__SEUART_TX_C](#a5c82a65c9a340d4ed121a7a03d295739)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`SEUART_TX_C`。

<a id="r_aa791fcf124397d4852a8319404c7f7b1"></a>

```c
#define PIN_P7_7__UART5_TX_B ALIF_PINMUX(7, 7, 2)
```

相关声明：[PIN_P7_7__UART5_TX_B](#aa791fcf124397d4852a8319404c7f7b1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`UART5_TX_B`。

<a id="r_a6719936ee12e645dccf126f627c96bdb"></a>

```c
#define PIN_P7_7__LPPDM_D3_C ALIF_PINMUX(7, 7, 3)
```

相关声明：[PIN_P7_7__LPPDM_D3_C](#a6719936ee12e645dccf126f627c96bdb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPPDM_D3_C`。

<a id="r_a6cada0c7c7ac09e8ec99fb99b0e64cc5"></a>

```c
#define PIN_P7_7__SPI0_MOSI_C ALIF_PINMUX(7, 7, 4)
```

相关声明：[PIN_P7_7__SPI0_MOSI_C](#a6cada0c7c7ac09e8ec99fb99b0e64cc5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`SPI0_MOSI_C`。

<a id="r_ada14fb90a5399c5e4b0a8a880ea70ef8"></a>

```c
#define PIN_P7_7__LPCAM_D7_B ALIF_PINMUX(7, 7, 5)
```

相关声明：[PIN_P7_7__LPCAM_D7_B](#ada14fb90a5399c5e4b0a8a880ea70ef8)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`LPCAM_D7_B`。

<a id="r_a5baa436ab02db34ffd62978c8428e1c5"></a>

```c
#define PIN_P7_7__CDC_D23_A ALIF_PINMUX(7, 7, 6)
```

相关声明：[PIN_P7_7__CDC_D23_A](#a5baa436ab02db34ffd62978c8428e1c5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）7 的引脚（Pin）7：`CDC_D23_A`。

<a id="r_afae07d2c2c36cf28b58d3025bd312bcd"></a>

```c
#define PIN_P8_0__GPIO ALIF_PINMUX(8, 0, 0)
```

相关声明：[PIN_P8_0__GPIO](#afae07d2c2c36cf28b58d3025bd312bcd)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.0` 的复用功能（Alternate Functions）。

<a id="r_a58bbba227cb5e1f12ac075c9a5e42e75"></a>

```c
#define PIN_P8_0__UART0_RX_C ALIF_PINMUX(8, 0, 1)
```

相关声明：[PIN_P8_0__UART0_RX_C](#a58bbba227cb5e1f12ac075c9a5e42e75)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`UART0_RX_C`。

<a id="r_add5139fb39426db9eecc9077b6cb460a"></a>

```c
#define PIN_P8_0__I2S0_SDI_C ALIF_PINMUX(8, 0, 2)
```

相关声明：[PIN_P8_0__I2S0_SDI_C](#add5139fb39426db9eecc9077b6cb460a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`I2S0_SDI_C`。

<a id="r_aa16141bb8f8655b759d2c1d89f811654"></a>

```c
#define PIN_P8_0__SPI0_SCLK_C ALIF_PINMUX(8, 0, 3)
```

相关声明：[PIN_P8_0__SPI0_SCLK_C](#aa16141bb8f8655b759d2c1d89f811654)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`SPI0_SCLK_C`。

<a id="r_ab79c19d10789928fc5221dde4ffc7631"></a>

```c
#define PIN_P8_0__UT0_T0_C ALIF_PINMUX(8, 0, 4)
```

相关声明：[PIN_P8_0__UT0_T0_C](#ab79c19d10789928fc5221dde4ffc7631)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`UT0_T0_C`。

<a id="r_a80efe03682baa66d7367d29c3226e7c5"></a>

```c
#define PIN_P8_0__SD_CMD_C ALIF_PINMUX(8, 0, 5)
```

相关声明：[PIN_P8_0__SD_CMD_C](#a80efe03682baa66d7367d29c3226e7c5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`SD_CMD_C`。

<a id="r_ad71cd9d2d19e676624b7d597620d456a"></a>

```c
#define PIN_P8_0__I3C_SCL_C ALIF_PINMUX(8, 0, 6)
```

相关声明：[PIN_P8_0__I3C_SCL_C](#ad71cd9d2d19e676624b7d597620d456a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）0：`I3C_SCL_C`。

<a id="r_ab7545d1438381ff91c47907abe36bde2"></a>

```c
#define PIN_P8_1__GPIO ALIF_PINMUX(8, 1, 0)
```

相关声明：[PIN_P8_1__GPIO](#ab7545d1438381ff91c47907abe36bde2)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.1` 的复用功能（Alternate Functions）。

<a id="r_a3708ad7f65ca0bd5a0d05c390aa3bc36"></a>

```c
#define PIN_P8_1__UART0_TX_C ALIF_PINMUX(8, 1, 1)
```

相关声明：[PIN_P8_1__UART0_TX_C](#a3708ad7f65ca0bd5a0d05c390aa3bc36)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`UART0_TX_C`。

<a id="r_aecdf8538d1daba974407d66a6826d18d"></a>

```c
#define PIN_P8_1__I2S0_SDO_C ALIF_PINMUX(8, 1, 2)
```

相关声明：[PIN_P8_1__I2S0_SDO_C](#aecdf8538d1daba974407d66a6826d18d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`I2S0_SDO_C`。

<a id="r_a8551b940fa9293173f90da6886079ac7"></a>

```c
#define PIN_P8_1__SPI0_SS0_C ALIF_PINMUX(8, 1, 3)
```

相关声明：[PIN_P8_1__SPI0_SS0_C](#a8551b940fa9293173f90da6886079ac7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`SPI0_SS0_C`。

<a id="r_a6e0b62693de52080c892062924740675"></a>

```c
#define PIN_P8_1__UT0_T1_C ALIF_PINMUX(8, 1, 4)
```

相关声明：[PIN_P8_1__UT0_T1_C](#a6e0b62693de52080c892062924740675)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`UT0_T1_C`。

<a id="r_a7ddacd2a5789fe8587a24daed92619f7"></a>

```c
#define PIN_P8_1__SD_CLK_C ALIF_PINMUX(8, 1, 5)
```

相关声明：[PIN_P8_1__SD_CLK_C](#a7ddacd2a5789fe8587a24daed92619f7)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`SD_CLK_C`。

<a id="r_a206e662c71dd50a55059bc9454a19379"></a>

```c
#define PIN_P8_1__I3C_SDA_C ALIF_PINMUX(8, 1, 6)
```

相关声明：[PIN_P8_1__I3C_SDA_C](#a206e662c71dd50a55059bc9454a19379)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）1：`I3C_SDA_C`。

<a id="r_a60cd1313b5dbd2f3e804024add367802"></a>

```c
#define PIN_P8_2__GPIO ALIF_PINMUX(8, 2, 0)
```

相关声明：[PIN_P8_2__GPIO](#a60cd1313b5dbd2f3e804024add367802)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.2` 的复用功能（Alternate Functions）。

<a id="r_a86921d6a2960aabd4d0386fda119c312"></a>

```c
#define PIN_P8_2__SEUART_RX_B ALIF_PINMUX(8, 2, 1)
```

相关声明：[PIN_P8_2__SEUART_RX_B](#a86921d6a2960aabd4d0386fda119c312)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`SEUART_RX_B`。

<a id="r_ab5340acc8bb2b67e47ab6cafaf1e3f73"></a>

```c
#define PIN_P8_2__UART1_RX_C ALIF_PINMUX(8, 2, 2)
```

相关声明：[PIN_P8_2__UART1_RX_C](#ab5340acc8bb2b67e47ab6cafaf1e3f73)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`UART1_RX_C`。

<a id="r_a32c45381d99f79eaee7a76484eecb64e"></a>

```c
#define PIN_P8_2__I2S0_SCLK_C ALIF_PINMUX(8, 2, 3)
```

相关声明：[PIN_P8_2__I2S0_SCLK_C](#a32c45381d99f79eaee7a76484eecb64e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`I2S0_SCLK_C`。

<a id="r_aa86eff0d25a32c3ae0ec1186800140f5"></a>

```c
#define PIN_P8_2__SPI0_SS1_C ALIF_PINMUX(8, 2, 4)
```

相关声明：[PIN_P8_2__SPI0_SS1_C](#aa86eff0d25a32c3ae0ec1186800140f5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`SPI0_SS1_C`。

<a id="r_a46fb8739c6ae846bf36cafad253ebe20"></a>

```c
#define PIN_P8_2__UT1_T0_C ALIF_PINMUX(8, 2, 5)
```

相关声明：[PIN_P8_2__UT1_T0_C](#a46fb8739c6ae846bf36cafad253ebe20)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`UT1_T0_C`。

<a id="r_a4a76b56c903dba7a0aa59fed719b4667"></a>

```c
#define PIN_P8_2__SD_RST_C ALIF_PINMUX(8, 2, 6)
```

相关声明：[PIN_P8_2__SD_RST_C](#a4a76b56c903dba7a0aa59fed719b4667)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`SD_RST_C`。

<a id="r_a66e4eadceca2ff968dfa3195a4250122"></a>

```c
#define PIN_P8_2__CAN0_RXD_C ALIF_PINMUX(8, 2, 7)
```

相关声明：[PIN_P8_2__CAN0_RXD_C](#a66e4eadceca2ff968dfa3195a4250122)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）2：`CAN0_RXD_C`。

<a id="r_ada60da6343aec9d7f341d29d6c0f7d6e"></a>

```c
#define PIN_P8_3__GPIO ALIF_PINMUX(8, 3, 0)
```

相关声明：[PIN_P8_3__GPIO](#ada60da6343aec9d7f341d29d6c0f7d6e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.3` 的复用功能（Alternate Functions）。

<a id="r_a6648fb7145169a8b26d9f7be77927683"></a>

```c
#define PIN_P8_3__SEUART_TX_B ALIF_PINMUX(8, 3, 1)
```

相关声明：[PIN_P8_3__SEUART_TX_B](#a6648fb7145169a8b26d9f7be77927683)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`SEUART_TX_B`。

<a id="r_a61fa9fcc8852a233ea722ac92481d152"></a>

```c
#define PIN_P8_3__UART1_TX_C ALIF_PINMUX(8, 3, 2)
```

相关声明：[PIN_P8_3__UART1_TX_C](#a61fa9fcc8852a233ea722ac92481d152)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`UART1_TX_C`。

<a id="r_afb096c4d807b834a4a8aa1bd0c899e50"></a>

```c
#define PIN_P8_3__I2S0_WS_C ALIF_PINMUX(8, 3, 3)
```

相关声明：[PIN_P8_3__I2S0_WS_C](#afb096c4d807b834a4a8aa1bd0c899e50)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`I2S0_WS_C`。

<a id="r_a7f20e17c17ec01ee643a192119f9fbe5"></a>

```c
#define PIN_P8_3__SPI0_SS2_C ALIF_PINMUX(8, 3, 4)
```

相关声明：[PIN_P8_3__SPI0_SS2_C](#a7f20e17c17ec01ee643a192119f9fbe5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`SPI0_SS2_C`。

<a id="r_a51e2fecfda5f8e671340b40116b241be"></a>

```c
#define PIN_P8_3__UT1_T1_C ALIF_PINMUX(8, 3, 5)
```

相关声明：[PIN_P8_3__UT1_T1_C](#a51e2fecfda5f8e671340b40116b241be)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`UT1_T1_C`。

<a id="r_af7a4aec639e5e6c29d29dd9f1511e5fb"></a>

```c
#define PIN_P8_3__CAN0_TXD_C ALIF_PINMUX(8, 3, 6)
```

相关声明：[PIN_P8_3__CAN0_TXD_C](#af7a4aec639e5e6c29d29dd9f1511e5fb)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`CAN0_TXD_C`。

<a id="r_a34640dc5781b53cbf9113e1def9fc2ff"></a>

```c
#define PIN_P8_3__EXT_RTS_B ALIF_PINMUX(8, 3, 7)
```

相关声明：[PIN_P8_3__EXT_RTS_B](#a34640dc5781b53cbf9113e1def9fc2ff)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）3：`EXT_RTS_B`。

<a id="r_a077f91c6d32af478832d2f868a03ce92"></a>

```c
#define PIN_P8_4__GPIO ALIF_PINMUX(8, 4, 0)
```

相关声明：[PIN_P8_4__GPIO](#a077f91c6d32af478832d2f868a03ce92)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.4` 的复用功能（Alternate Functions）。

<a id="r_a63f07834cb140489a435742cb4bb8929"></a>

```c
#define PIN_P8_4__UART2_RX_C ALIF_PINMUX(8, 4, 1)
```

相关声明：[PIN_P8_4__UART2_RX_C](#a63f07834cb140489a435742cb4bb8929)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`UART2_RX_C`。

<a id="r_a120e7ac88d5656af5ae1050b1ade43aa"></a>

```c
#define PIN_P8_4__I2S1_SDI_C ALIF_PINMUX(8, 4, 2)
```

相关声明：[PIN_P8_4__I2S1_SDI_C](#a120e7ac88d5656af5ae1050b1ade43aa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`I2S1_SDI_C`。

<a id="r_aa22e557329e1a5bb4cbcf3b614ba066c"></a>

```c
#define PIN_P8_4__SPI1_MISO_C ALIF_PINMUX(8, 4, 3)
```

相关声明：[PIN_P8_4__SPI1_MISO_C](#aa22e557329e1a5bb4cbcf3b614ba066c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`SPI1_MISO_C`。

<a id="r_a24aee8e934f4b64d7e7db9c69ba84010"></a>

```c
#define PIN_P8_4__UT2_T0_C ALIF_PINMUX(8, 4, 4)
```

相关声明：[PIN_P8_4__UT2_T0_C](#a24aee8e934f4b64d7e7db9c69ba84010)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`UT2_T0_C`。

<a id="r_acf34db33a03da94b1b557826ca9c6fca"></a>

```c
#define PIN_P8_4__LPCAM_VSYNC_C ALIF_PINMUX(8, 4, 5)
```

相关声明：[PIN_P8_4__LPCAM_VSYNC_C](#acf34db33a03da94b1b557826ca9c6fca)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`LPCAM_VSYNC_C`。

<a id="r_ac485ddd7241a84dccdd1c1a2bf011fc1"></a>

```c
#define PIN_P8_4__CAN0_STBY_C ALIF_PINMUX(8, 4, 6)
```

相关声明：[PIN_P8_4__CAN0_STBY_C](#ac485ddd7241a84dccdd1c1a2bf011fc1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`CAN0_STBY_C`。

<a id="r_a6dcf47f3f8095e7bb8e33bd49eb65bfa"></a>

```c
#define PIN_P8_4__EXT_CTS_B ALIF_PINMUX(8, 4, 7)
```

相关声明：[PIN_P8_4__EXT_CTS_B](#a6dcf47f3f8095e7bb8e33bd49eb65bfa)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）4：`EXT_CTS_B`。

<a id="r_a3d1dbbf65ec7141c08cbdf70186faa0a"></a>

```c
#define PIN_P8_5__GPIO ALIF_PINMUX(8, 5, 0)
```

相关声明：[PIN_P8_5__GPIO](#a3d1dbbf65ec7141c08cbdf70186faa0a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.5` 的复用功能（Alternate Functions）。

<a id="r_ad31f2a501dd199a749a1c95d6d82273d"></a>

```c
#define PIN_P8_5__UART2_TX_C ALIF_PINMUX(8, 5, 1)
```

相关声明：[PIN_P8_5__UART2_TX_C](#ad31f2a501dd199a749a1c95d6d82273d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`UART2_TX_C`。

<a id="r_ae7050df3aa65dfea482ae99ae9993c75"></a>

```c
#define PIN_P8_5__I2S1_SDO_C ALIF_PINMUX(8, 5, 2)
```

相关声明：[PIN_P8_5__I2S1_SDO_C](#ae7050df3aa65dfea482ae99ae9993c75)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`I2S1_SDO_C`。

<a id="r_a55e6064e7f03d2c5b7d2f085384b06af"></a>

```c
#define PIN_P8_5__SPI1_MOSI_C ALIF_PINMUX(8, 5, 3)
```

相关声明：[PIN_P8_5__SPI1_MOSI_C](#a55e6064e7f03d2c5b7d2f085384b06af)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`SPI1_MOSI_C`。

<a id="r_a014098250157c9b8db9f0f5eb3c05254"></a>

```c
#define PIN_P8_5__UT2_T1_C ALIF_PINMUX(8, 5, 4)
```

相关声明：[PIN_P8_5__UT2_T1_C](#a014098250157c9b8db9f0f5eb3c05254)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`UT2_T1_C`。

<a id="r_afa53accd52402116b20cc56ddbf81144"></a>

```c
#define PIN_P8_5__LPCAM_HSYNC_C ALIF_PINMUX(8, 5, 5)
```

相关声明：[PIN_P8_5__LPCAM_HSYNC_C](#afa53accd52402116b20cc56ddbf81144)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`LPCAM_HSYNC_C`。

<a id="r_aa9c0b4c975f719fed6151f781e2ff914"></a>

```c
#define PIN_P8_5__CAN1_RXD_B ALIF_PINMUX(8, 5, 6)
```

相关声明：[PIN_P8_5__CAN1_RXD_B](#aa9c0b4c975f719fed6151f781e2ff914)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`CAN1_RXD_B`。

<a id="r_a5cb04e2264ad4c65af758f8962647f15"></a>

```c
#define PIN_P8_5__EXT_TRACE_B ALIF_PINMUX(8, 5, 7)
```

相关声明：[PIN_P8_5__EXT_TRACE_B](#a5cb04e2264ad4c65af758f8962647f15)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）5：`EXT_TRACE_B`。

<a id="r_aac04079cc075adb9c60dc629fb9e544e"></a>

```c
#define PIN_P8_6__GPIO ALIF_PINMUX(8, 6, 0)
```

相关声明：[PIN_P8_6__GPIO](#aac04079cc075adb9c60dc629fb9e544e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.6` 的复用功能（Alternate Functions）。

<a id="r_a314b2b687c40bf633cbb380a8fef9be0"></a>

```c
#define PIN_P8_6__UART3_RX_C ALIF_PINMUX(8, 6, 1)
```

相关声明：[PIN_P8_6__UART3_RX_C](#a314b2b687c40bf633cbb380a8fef9be0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`UART3_RX_C`。

<a id="r_a0385729cf0232abca6c12d677915cc56"></a>

```c
#define PIN_P8_6__I2S1_SCLK_SLV_C ALIF_PINMUX(8, 6, 2)
```

相关声明：[PIN_P8_6__I2S1_SCLK_SLV_C](#a0385729cf0232abca6c12d677915cc56)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`I2S1_SCLK_SLV_C`。

<a id="r_ab61338d7cfa1b124b4aefd3232973fa5"></a>

```c
#define PIN_P8_6__SPI1_SCLK_C ALIF_PINMUX(8, 6, 3)
```

相关声明：[PIN_P8_6__SPI1_SCLK_C](#ab61338d7cfa1b124b4aefd3232973fa5)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`SPI1_SCLK_C`。

<a id="r_a0659b1c3adb2e94c605a2cb2d47f6478"></a>

```c
#define PIN_P8_6__UT3_T0_C ALIF_PINMUX(8, 6, 4)
```

相关声明：[PIN_P8_6__UT3_T0_C](#a0659b1c3adb2e94c605a2cb2d47f6478)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`UT3_T0_C`。

<a id="r_ad8746ccd7ebe5b1f96b31ec2ffefe862"></a>

```c
#define PIN_P8_6__LPCAM_PCLK_C ALIF_PINMUX(8, 6, 5)
```

相关声明：[PIN_P8_6__LPCAM_PCLK_C](#ad8746ccd7ebe5b1f96b31ec2ffefe862)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`LPCAM_PCLK_C`。

<a id="r_a7db044cf6eed8db9319ab0a56b23ff4a"></a>

```c
#define PIN_P8_6__CAN1_TXD_B ALIF_PINMUX(8, 6, 6)
```

相关声明：[PIN_P8_6__CAN1_TXD_B](#a7db044cf6eed8db9319ab0a56b23ff4a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`CAN1_TXD_B`。

<a id="r_af2fe383f96275201cdad073aa15ee7c6"></a>

```c
#define PIN_P8_6__EXT_RX_B ALIF_PINMUX(8, 6, 7)
```

相关声明：[PIN_P8_6__EXT_RX_B](#af2fe383f96275201cdad073aa15ee7c6)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）6：`EXT_RX_B`。

<a id="r_adeed03c5ceab2806bff7df654f45982d"></a>

```c
#define PIN_P8_7__GPIO ALIF_PINMUX(8, 7, 0)
```

相关声明：[PIN_P8_7__GPIO](#adeed03c5ceab2806bff7df654f45982d)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `P8.7` 的复用功能（Alternate Functions）。

<a id="r_ae47d9b593d7d7508eccf313133767a82"></a>

```c
#define PIN_P8_7__UART3_TX_C ALIF_PINMUX(8, 7, 1)
```

相关声明：[PIN_P8_7__UART3_TX_C](#ae47d9b593d7d7508eccf313133767a82)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`UART3_TX_C`。

<a id="r_af8422945c480799c91c5194eb5ef3674"></a>

```c
#define PIN_P8_7__I2S1_WS_SLV_C ALIF_PINMUX(8, 7, 2)
```

相关声明：[PIN_P8_7__I2S1_WS_SLV_C](#af8422945c480799c91c5194eb5ef3674)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`I2S1_WS_SLV_C`。

<a id="r_a3fe74929914837237c6ce113ea00535b"></a>

```c
#define PIN_P8_7__SPI1_SS0_C ALIF_PINMUX(8, 7, 3)
```

相关声明：[PIN_P8_7__SPI1_SS0_C](#a3fe74929914837237c6ce113ea00535b)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`SPI1_SS0_C`。

<a id="r_a1204f92355e74076ef32abe8ddf62cb1"></a>

```c
#define PIN_P8_7__UT3_T1_C ALIF_PINMUX(8, 7, 4)
```

相关声明：[PIN_P8_7__UT3_T1_C](#a1204f92355e74076ef32abe8ddf62cb1)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`UT3_T1_C`。

<a id="r_aaefded103cf34db389da0e730b66f41c"></a>

```c
#define PIN_P8_7__LPCAM_XVCLK_C ALIF_PINMUX(8, 7, 5)
```

相关声明：[PIN_P8_7__LPCAM_XVCLK_C](#aaefded103cf34db389da0e730b66f41c)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`LPCAM_XVCLK_C`。

<a id="r_ac5141e80198c35db5cc964ae99d02c0a"></a>

```c
#define PIN_P8_7__CAN1_STBY_B ALIF_PINMUX(8, 7, 6)
```

相关声明：[PIN_P8_7__CAN1_STBY_B](#ac5141e80198c35db5cc964ae99d02c0a)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`CAN1_STBY_B`。

<a id="r_a71a58c7d97e8a9d0f6e8c66274a32b5e"></a>

```c
#define PIN_P8_7__EXT_TX_B ALIF_PINMUX(8, 7, 7)
```

相关声明：[PIN_P8_7__EXT_TX_B](#a71a58c7d97e8a9d0f6e8c66274a32b5e)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

端口（Port）8 的引脚（Pin）7：`EXT_TX_B`。

<a id="define-members-3"></a>

### LPGPIO 引脚定义（Pin Definitions）

LPGPIO 的引脚复用定义（Pin Multiplexing Definitions）。

注意（Note）：为兼容驱动程序（Driver Compatibility），编码中使用 `15`。

<a id="r_a482ff296b3458b8da397d102f23bba34"></a>

```c
#define PIN_P15_0__LPGPIO ALIF_PINMUX(15, 0, 0)
```

相关声明：[PIN_P15_0__LPGPIO](#a482ff296b3458b8da397d102f23bba34)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `LPGPIO.0` 的复用功能（Alternate Functions）。

<a id="r_a87b1f1b590da3e225affcf5e22e0fde0"></a>

```c
#define PIN_P15_1__LPGPIO ALIF_PINMUX(15, 1, 0)
```

相关声明：[PIN_P15_1__LPGPIO](#a87b1f1b590da3e225affcf5e22e0fde0)、[ALIF_PINMUX](#ab0a2e9966868f5dcb365d5d533318a21)。

引脚 `LPGPIO.1` 的复用功能（Alternate Functions）。

## 1.2\_详细说明（Detailed Documentation）

<a id="ab0a2e9966868f5dcb365d5d533318a21"></a>

### `ALIF_PINMUX`

```c
#define ALIF_PINMUX ( port, pin, func )
```

展开值（Value）：

```c
((((port) & ALIF_PINMUX_PORT_MASK) << ALIF_PINMUX_PORT_POS) |   \
(((pin) & ALIF_PINMUX_PIN_MASK) << ALIF_PINMUX_PIN_POS) |       \
(((func) & ALIF_PINMUX_FUNC_MASK) << ALIF_PINMUX_FUNC_POS))
```

编码引脚复用配置（Pinmux Configuration）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口编号（Port Number）：普通 GPIO 使用 `0–8`，LPGPIO 使用 `15`。 |
| `pin` | 端口内的引脚编号（Pin Number Within Port），范围为 `0–7`。 |
| `func` | 复用功能（Alternate Function）：`0` 表示 GPIO，`1–7` 表示 AF1–AF7。 |

**返回（Returns）**：返回值（Returns）：用于设备树（Devicetree）的已编码引脚复用值（Pinmux Value）。

<a id="a195b3893d9913e77419e111178923a3d"></a>

### `ALIF_PINMUX_FUNC_MASK`

```c
#define ALIF_PINMUX_FUNC_MASK 0x7U
```

复用功能（Alternate Function）字段的位掩码，共 3 位。

<a id="ab8529e7ad1002e2e112bf1286d4d6c62"></a>

### `ALIF_PINMUX_FUNC_POS`

```c
#define ALIF_PINMUX_FUNC_POS 0U
```

复用功能（Alternate Function）字段的位位置。

<a id="a723a8df1e91c947c25af42db8b9f73dd"></a>

### `ALIF_PINMUX_PIN_MASK`

```c
#define ALIF_PINMUX_PIN_MASK 0x7U
```

引脚编号（Pin Number）字段的位掩码，共 3 位。

<a id="a8c94e09e787a9fb1079e5fbe0aa875d2"></a>

### `ALIF_PINMUX_PIN_POS`

```c
#define ALIF_PINMUX_PIN_POS 3U
```

引脚编号（Pin Number）字段的位位置。

<a id="a280dd67858770ceb0a88153aa29e09da"></a>

### `ALIF_PINMUX_PORT_MASK`

```c
#define ALIF_PINMUX_PORT_MASK 0x1FU
```

端口编号（Port Number）字段的位掩码，共 5 位。

<a id="a5d3f4f922452dc948bcc7727d9875107"></a>

### `ALIF_PINMUX_PORT_POS`

```c
#define ALIF_PINMUX_PORT_POS 6U
```

端口编号（Port Number）字段的位位置。

<a id="aa23df37079d3cb2dfc04e0712ea4b98d"></a>

### `PIN_P0_0__ANA_S0`

```c
#define PIN_P0_0__ANA_S0 ALIF_PINMUX(0, 0, 6)
```

端口（Port）0 的引脚（Pin）0：`ANA_S0`。

<a id="a21c0982e31739a0e14d1d5bbe8d28e26"></a>

### `PIN_P0_0__GPIO`

```c
#define PIN_P0_0__GPIO ALIF_PINMUX(0, 0, 0)
```

引脚 `P0.0` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）0：`GPIO`。

<a id="ad83a764cf6e61171dcc56e6ad213e59e"></a>

### `PIN_P0_0__LPI2C0_SCL_A`

```c
#define PIN_P0_0__LPI2C0_SCL_A ALIF_PINMUX(0, 0, 5)
```

端口（Port）0 的引脚（Pin）0：`LPI2C0_SCL_A`。

<a id="aaec802e33197d50afe17f58f3614294b"></a>

### `PIN_P0_0__LPI2S_SDI_A`

```c
#define PIN_P0_0__LPI2S_SDI_A ALIF_PINMUX(0, 0, 3)
```

端口（Port）0 的引脚（Pin）0：`LPI2S_SDI_A`。

<a id="af61f7092241bffd1e1c72f4875753646"></a>

### `PIN_P0_0__SEUART_RX_A`

```c
#define PIN_P0_0__SEUART_RX_A ALIF_PINMUX(0, 0, 1)
```

端口（Port）0 的引脚（Pin）0：`SEUART_RX_A`。

<a id="aacbc860014b31389d2e1d19059020462"></a>

### `PIN_P0_0__SPI0_SS0_A`

```c
#define PIN_P0_0__SPI0_SS0_A ALIF_PINMUX(0, 0, 4)
```

端口（Port）0 的引脚（Pin）0：`SPI0_SS0_A`。

<a id="a90cebb445be4e8ec705a6fec4f446849"></a>

### `PIN_P0_0__UART0_RX_A`

```c
#define PIN_P0_0__UART0_RX_A ALIF_PINMUX(0, 0, 2)
```

端口（Port）0 的引脚（Pin）0：`UART0_RX_A`。

<a id="a9a7460d69ed218e8bfe8e5038ad27f92"></a>

### `PIN_P0_1__ANA_S1`

```c
#define PIN_P0_1__ANA_S1 ALIF_PINMUX(0, 1, 6)
```

端口（Port）0 的引脚（Pin）1：`ANA_S1`。

<a id="a32eb0096f118eeaafa9f397de1d80611"></a>

### `PIN_P0_1__GPIO`

```c
#define PIN_P0_1__GPIO ALIF_PINMUX(0, 1, 0)
```

引脚 `P0.1` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）1：`GPIO`。

<a id="a8a765220ea90dbdb4cf985be31b0a1a0"></a>

### `PIN_P0_1__LPI2C0_SDA_A`

```c
#define PIN_P0_1__LPI2C0_SDA_A ALIF_PINMUX(0, 1, 5)
```

端口（Port）0 的引脚（Pin）1：`LPI2C0_SDA_A`。

<a id="a4c5291503299cbd81d4337796735fd24"></a>

### `PIN_P0_1__LPI2S_SDO_A`

```c
#define PIN_P0_1__LPI2S_SDO_A ALIF_PINMUX(0, 1, 3)
```

端口（Port）0 的引脚（Pin）1：`LPI2S_SDO_A`。

<a id="ad2e9b4bc2f8fb875bbbaad78362bf3b2"></a>

### `PIN_P0_1__SEUART_TX_A`

```c
#define PIN_P0_1__SEUART_TX_A ALIF_PINMUX(0, 1, 1)
```

端口（Port）0 的引脚（Pin）1：`SEUART_TX_A`。

<a id="a0db281f253dd9e245269cc4901347844"></a>

### `PIN_P0_1__SPI0_SS1_A`

```c
#define PIN_P0_1__SPI0_SS1_A ALIF_PINMUX(0, 1, 4)
```

端口（Port）0 的引脚（Pin）1：`SPI0_SS1_A`。

<a id="ad3c6925fe9f38326a5750bfa5bfca6f1"></a>

### `PIN_P0_1__UART0_TX_A`

```c
#define PIN_P0_1__UART0_TX_A ALIF_PINMUX(0, 1, 2)
```

端口（Port）0 的引脚（Pin）1：`UART0_TX_A`。

<a id="a49b9fef54a6baea750aadaa5d80f8b59"></a>

### `PIN_P0_2__ANA_S2`

```c
#define PIN_P0_2__ANA_S2 ALIF_PINMUX(0, 2, 6)
```

端口（Port）0 的引脚（Pin）2：`ANA_S2`。

<a id="a4fb3d6992e5eedb80cd18620d13aa3f4"></a>

### `PIN_P0_2__GPIO`

```c
#define PIN_P0_2__GPIO ALIF_PINMUX(0, 2, 0)
```

引脚 `P0.2` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）2：`GPIO`。

<a id="aea911d4031ea9ef5c6bfcb387ddfe716"></a>

### `PIN_P0_2__JTAG1_TDI`

```c
#define PIN_P0_2__JTAG1_TDI ALIF_PINMUX(0, 2, 1)
```

端口（Port）0 的引脚（Pin）2：`JTAG1_TDI`。

<a id="a18c4cf23b00afd5dcd176295c5ff6ed9"></a>

### `PIN_P0_2__LPI2S_SCLK_A`

```c
#define PIN_P0_2__LPI2S_SCLK_A ALIF_PINMUX(0, 2, 4)
```

端口（Port）0 的引脚（Pin）2：`LPI2S_SCLK_A`。

<a id="a85030d71c6aedee18cb7f701432ecd9b"></a>

### `PIN_P0_2__OSPI0_SS0_A`

```c
#define PIN_P0_2__OSPI0_SS0_A ALIF_PINMUX(0, 2, 2)
```

端口（Port）0 的引脚（Pin）2：`OSPI0_SS0_A`。

<a id="a631b7e7921b71f9b823bab70e3d4ab1d"></a>

### `PIN_P0_2__SPI0_SS2_A`

```c
#define PIN_P0_2__SPI0_SS2_A ALIF_PINMUX(0, 2, 5)
```

端口（Port）0 的引脚（Pin）2：`SPI0_SS2_A`。

<a id="a81dafa48db9962a46d804fe26b4d9aef"></a>

### `PIN_P0_2__UART0_CTS_A`

```c
#define PIN_P0_2__UART0_CTS_A ALIF_PINMUX(0, 2, 3)
```

端口（Port）0 的引脚（Pin）2：`UART0_CTS_A`。

<a id="acde8c916348493ac12ab8d892f4c4f5d"></a>

### `PIN_P0_3__ANA_S3`

```c
#define PIN_P0_3__ANA_S3 ALIF_PINMUX(0, 3, 6)
```

端口（Port）0 的引脚（Pin）3：`ANA_S3`。

<a id="af6db067634b65894a37a5edbe29654a5"></a>

### `PIN_P0_3__GPIO`

```c
#define PIN_P0_3__GPIO ALIF_PINMUX(0, 3, 0)
```

引脚 `P0.3` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）3：`GPIO`。

<a id="aab83fe2126443e905a451effda41c154"></a>

### `PIN_P0_3__JTAG1_TDO`

```c
#define PIN_P0_3__JTAG1_TDO ALIF_PINMUX(0, 3, 1)
```

端口（Port）0 的引脚（Pin）3：`JTAG1_TDO`。

<a id="a9b8e5ae3f49eb1cf23c9b2ec0770636b"></a>

### `PIN_P0_3__LPI2S_WS_A`

```c
#define PIN_P0_3__LPI2S_WS_A ALIF_PINMUX(0, 3, 4)
```

端口（Port）0 的引脚（Pin）3：`LPI2S_WS_A`。

<a id="a2551a16bfe9f91ce64188d4bd78d5a92"></a>

### `PIN_P0_3__OSPI0_SS1_A`

```c
#define PIN_P0_3__OSPI0_SS1_A ALIF_PINMUX(0, 3, 2)
```

端口（Port）0 的引脚（Pin）3：`OSPI0_SS1_A`。

<a id="a9fb13233a0bebf28a29ad65cb4975a70"></a>

### `PIN_P0_3__SPI1_SS0_A`

```c
#define PIN_P0_3__SPI1_SS0_A ALIF_PINMUX(0, 3, 5)
```

端口（Port）0 的引脚（Pin）3：`SPI1_SS0_A`。

<a id="a37d3d9cde76c648ab549818678cdd02c"></a>

### `PIN_P0_3__UART0_RTS_A`

```c
#define PIN_P0_3__UART0_RTS_A ALIF_PINMUX(0, 3, 3)
```

端口（Port）0 的引脚（Pin）3：`UART0_RTS_A`。

<a id="aa132663d37ec856ce1cad081dbe0193e"></a>

### `PIN_P0_4__ANA_S4`

```c
#define PIN_P0_4__ANA_S4 ALIF_PINMUX(0, 4, 6)
```

端口（Port）0 的引脚（Pin）4：`ANA_S4`。

<a id="afb6485483deeafda4a21ed55c68491e3"></a>

### `PIN_P0_4__FAULT0_A`

```c
#define PIN_P0_4__FAULT0_A ALIF_PINMUX(0, 4, 5)
```

端口（Port）0 的引脚（Pin）4：`FAULT0_A`。

<a id="a068d5bd9723f62cb6aaa42fba90a9034"></a>

### `PIN_P0_4__GPIO`

```c
#define PIN_P0_4__GPIO ALIF_PINMUX(0, 4, 0)
```

引脚 `P0.4` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）4：`GPIO`。

<a id="a6cf94fa138887b35b52354bbbcfe26a2"></a>

### `PIN_P0_4__I2C0_SDA_A`

```c
#define PIN_P0_4__I2C0_SDA_A ALIF_PINMUX(0, 4, 4)
```

端口（Port）0 的引脚（Pin）4：`I2C0_SDA_A`。

<a id="adacd1c63dc4eba3bd0c5d3795b9dbd4d"></a>

### `PIN_P0_4__JTAG1_TRST`

```c
#define PIN_P0_4__JTAG1_TRST ALIF_PINMUX(0, 4, 1)
```

端口（Port）0 的引脚（Pin）4：`JTAG1_TRST`。

<a id="aa849bd3926156c6ac30b90b32eabfaad"></a>

### `PIN_P0_4__SPI1_SS1_A`

```c
#define PIN_P0_4__SPI1_SS1_A ALIF_PINMUX(0, 4, 3)
```

端口（Port）0 的引脚（Pin）4：`SPI1_SS1_A`。

<a id="a86dde3f58b034c8276602748a76ca207"></a>

### `PIN_P0_4__UART1_RX_A`

```c
#define PIN_P0_4__UART1_RX_A ALIF_PINMUX(0, 4, 2)
```

端口（Port）0 的引脚（Pin）4：`UART1_RX_A`。

<a id="adab066f4e9f8d2741b138fc08b513cf6"></a>

### `PIN_P0_5__ANA_S5`

```c
#define PIN_P0_5__ANA_S5 ALIF_PINMUX(0, 5, 6)
```

端口（Port）0 的引脚（Pin）5：`ANA_S5`。

<a id="abd7d8c1f0be68ab38e7e4c7d62e8c88d"></a>

### `PIN_P0_5__GPIO`

```c
#define PIN_P0_5__GPIO ALIF_PINMUX(0, 5, 0)
```

引脚 `P0.5` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）5：`GPIO`。

<a id="a2c4aa8781e1a50243b5c0581bf0c0e0f"></a>

### `PIN_P0_5__I2C0_SCL_A`

```c
#define PIN_P0_5__I2C0_SCL_A ALIF_PINMUX(0, 5, 4)
```

端口（Port）0 的引脚（Pin）5：`I2C0_SCL_A`。

<a id="a3d0e9c04f7c008ae658cf87bdd691341"></a>

### `PIN_P0_5__I3C_SCL_A`

```c
#define PIN_P0_5__I3C_SCL_A ALIF_PINMUX(0, 5, 5)
```

端口（Port）0 的引脚（Pin）5：`I3C_SCL_A`。

<a id="a5294b8ee6a61abecc2b8e1a1cfb80668"></a>

### `PIN_P0_5__JTAG1_TCK`

```c
#define PIN_P0_5__JTAG1_TCK ALIF_PINMUX(0, 5, 1)
```

端口（Port）0 的引脚（Pin）5：`JTAG1_TCK`。

<a id="a21264e6bc27ee7f361a46ac06658c721"></a>

### `PIN_P0_5__SPI1_SS2_A`

```c
#define PIN_P0_5__SPI1_SS2_A ALIF_PINMUX(0, 5, 3)
```

端口（Port）0 的引脚（Pin）5：`SPI1_SS2_A`。

<a id="a4c0f43be2ca7617733c39d6956d0898c"></a>

### `PIN_P0_5__UART1_TX_A`

```c
#define PIN_P0_5__UART1_TX_A ALIF_PINMUX(0, 5, 2)
```

端口（Port）0 的引脚（Pin）5：`UART1_TX_A`。

<a id="aa5907af749639d7948c06be6af51c75e"></a>

### `PIN_P0_6__ANA_S6`

```c
#define PIN_P0_6__ANA_S6 ALIF_PINMUX(0, 6, 6)
```

端口（Port）0 的引脚（Pin）6：`ANA_S6`。

<a id="a35d7d996009ded8b1f05a345b819e8ad"></a>

### `PIN_P0_6__FAULT2_A`

```c
#define PIN_P0_6__FAULT2_A ALIF_PINMUX(0, 6, 4)
```

端口（Port）0 的引脚（Pin）6：`FAULT2_A`。

<a id="ad494beaa1230d6528f706e36a8f007cd"></a>

### `PIN_P0_6__GPIO`

```c
#define PIN_P0_6__GPIO ALIF_PINMUX(0, 6, 0)
```

引脚 `P0.6` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）6：`GPIO`。

<a id="a535db12aabf7cff50c012f39bb021101"></a>

### `PIN_P0_6__I2C1_SDA_A`

```c
#define PIN_P0_6__I2C1_SDA_A ALIF_PINMUX(0, 6, 3)
```

端口（Port）0 的引脚（Pin）6：`I2C1_SDA_A`。

<a id="a790bf4cd500681d76b13722103f241ff"></a>

### `PIN_P0_6__I3C_SDA_A`

```c
#define PIN_P0_6__I3C_SDA_A ALIF_PINMUX(0, 6, 5)
```

端口（Port）0 的引脚（Pin）6：`I3C_SDA_A`。

<a id="aa24d097a966de41f5200b015d812cea3"></a>

### `PIN_P0_6__JTAG1_TMS`

```c
#define PIN_P0_6__JTAG1_TMS ALIF_PINMUX(0, 6, 1)
```

端口（Port）0 的引脚（Pin）6：`JTAG1_TMS`。

<a id="a8d2cc812b823a3e6dfc06cb34e57a0aa"></a>

### `PIN_P0_6__UART1_CTS_A`

```c
#define PIN_P0_6__UART1_CTS_A ALIF_PINMUX(0, 6, 2)
```

端口（Port）0 的引脚（Pin）6：`UART1_CTS_A`。

<a id="a996b9421d83cdf9fc98ee86a07037882"></a>

### `PIN_P0_7__ANA_S7`

```c
#define PIN_P0_7__ANA_S7 ALIF_PINMUX(0, 7, 6)
```

端口（Port）0 的引脚（Pin）7：`ANA_S7`。

<a id="a37f70eb27978363bfa5ce7a1a06ff745"></a>

### `PIN_P0_7__FAULT3_A`

```c
#define PIN_P0_7__FAULT3_A ALIF_PINMUX(0, 7, 3)
```

端口（Port）0 的引脚（Pin）7：`FAULT3_A`。

<a id="a3461a7c5af5e46d8e668e1e633c5d721"></a>

### `PIN_P0_7__GPIO`

```c
#define PIN_P0_7__GPIO ALIF_PINMUX(0, 7, 0)
```

引脚 `P0.7` 的复用功能（Alternate Functions）。

端口（Port）0 的引脚（Pin）7：`GPIO`。

<a id="ad1dbe52190aa500b3ea50aa3bf4f5a36"></a>

### `PIN_P0_7__I2C1_SCL_A`

```c
#define PIN_P0_7__I2C1_SCL_A ALIF_PINMUX(0, 7, 2)
```

端口（Port）0 的引脚（Pin）7：`I2C1_SCL_A`。

<a id="acfeb79a95b8fe2cf9d04b0c28fa8f3c5"></a>

### `PIN_P0_7__LPCAM_VSYNC_B`

```c
#define PIN_P0_7__LPCAM_VSYNC_B ALIF_PINMUX(0, 7, 4)
```

端口（Port）0 的引脚（Pin）7：`LPCAM_VSYNC_B`。

<a id="a8c262122844a7c5ff415d909d982a9b3"></a>

### `PIN_P0_7__UART1_RTS_A`

```c
#define PIN_P0_7__UART1_RTS_A ALIF_PINMUX(0, 7, 1)
```

端口（Port）0 的引脚（Pin）7：`UART1_RTS_A`。

<a id="a482ff296b3458b8da397d102f23bba34"></a>

### `PIN_P15_0__LPGPIO`

```c
#define PIN_P15_0__LPGPIO ALIF_PINMUX(15, 0, 0)
```

引脚 `LPGPIO.0` 的复用功能（Alternate Functions）。

LPGPIO 引脚（Pin）0：GPIO。

<a id="a87b1f1b590da3e225affcf5e22e0fde0"></a>

### `PIN_P15_1__LPGPIO`

```c
#define PIN_P15_1__LPGPIO ALIF_PINMUX(15, 1, 0)
```

引脚 `LPGPIO.1` 的复用功能（Alternate Functions）。

LPGPIO 引脚（Pin）1：GPIO。

<a id="af59cc6b851070a403399aa14ec9522d5"></a>

### `PIN_P1_0__GPIO`

```c
#define PIN_P1_0__GPIO ALIF_PINMUX(1, 0, 0)
```

引脚 `P1.0` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）0：`GPIO`。

<a id="a9dbd3e87d6822b951f4f479014a0152e"></a>

### `PIN_P1_0__LPCAM_D0_A`

```c
#define PIN_P1_0__LPCAM_D0_A ALIF_PINMUX(1, 0, 6)
```

端口（Port）1 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="ad36a394ace52050ea666e8a4e49628b3"></a>

### `PIN_P1_0__LPI2S_SDI_B`

```c
#define PIN_P1_0__LPI2S_SDI_B ALIF_PINMUX(1, 0, 4)
```

端口（Port）1 的引脚（Pin）0：`LPI2S_SDI_B`。

<a id="ace793548d3589296b9eda950d89a5329"></a>

### `PIN_P1_0__LPPDM_D0_A`

```c
#define PIN_P1_0__LPPDM_D0_A ALIF_PINMUX(1, 0, 3)
```

端口（Port）1 的引脚（Pin）0：`LPPDM_D0_A`。

<a id="a2c4a2a155ef84a5b8fd5bb2b4ada0429"></a>

### `PIN_P1_0__OSPI0_D0_A`

```c
#define PIN_P1_0__OSPI0_D0_A ALIF_PINMUX(1, 0, 1)
```

端口（Port）1 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="aa2f15500734f01ae94c048c566b2f3cf"></a>

### `PIN_P1_0__SD_D0_A`

```c
#define PIN_P1_0__SD_D0_A ALIF_PINMUX(1, 0, 7)
```

端口（Port）1 的引脚（Pin）0：`SD_D0_A`。

<a id="a1b162fa1d3aa4c3dd720b47331a07a43"></a>

### `PIN_P1_0__SPI0_MISO_A`

```c
#define PIN_P1_0__SPI0_MISO_A ALIF_PINMUX(1, 0, 5)
```

端口（Port）1 的引脚（Pin）0：`SPI0_MISO_A`。

<a id="a86fd70e32e1fe8ef3ddb28394c1181b9"></a>

### `PIN_P1_0__UART2_RX_A`

```c
#define PIN_P1_0__UART2_RX_A ALIF_PINMUX(1, 0, 2)
```

端口（Port）1 的引脚（Pin）0：`UART2_RX_A`。

<a id="a5bde8570f8ee36a7dfa0e5d486dcb4d1"></a>

### `PIN_P1_1__GPIO`

```c
#define PIN_P1_1__GPIO ALIF_PINMUX(1, 1, 0)
```

引脚 `P1.1` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）1：`GPIO`。

<a id="abc5440c97b76369acb8c294e874d045f"></a>

### `PIN_P1_1__LPCAM_D1_A`

```c
#define PIN_P1_1__LPCAM_D1_A ALIF_PINMUX(1, 1, 6)
```

端口（Port）1 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="ae9a5cdf32577a784e1ea21958a706c63"></a>

### `PIN_P1_1__LPI2S_SDO_B`

```c
#define PIN_P1_1__LPI2S_SDO_B ALIF_PINMUX(1, 1, 4)
```

端口（Port）1 的引脚（Pin）1：`LPI2S_SDO_B`。

<a id="ae157fe998af3a929a8e9f572b0a842fd"></a>

### `PIN_P1_1__LPPDM_C0_A`

```c
#define PIN_P1_1__LPPDM_C0_A ALIF_PINMUX(1, 1, 3)
```

端口（Port）1 的引脚（Pin）1：`LPPDM_C0_A`。

<a id="a65def1cda3c68f532896b4fc9a47454c"></a>

### `PIN_P1_1__OSPI0_D1_A`

```c
#define PIN_P1_1__OSPI0_D1_A ALIF_PINMUX(1, 1, 1)
```

端口（Port）1 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="a79fbe4374cc4d9ec5a943a874cd2ffdd"></a>

### `PIN_P1_1__SD_D1_A`

```c
#define PIN_P1_1__SD_D1_A ALIF_PINMUX(1, 1, 7)
```

端口（Port）1 的引脚（Pin）1：`SD_D1_A`。

<a id="a37f579415afac4b490325552b9a90197"></a>

### `PIN_P1_1__SPI0_MOSI_A`

```c
#define PIN_P1_1__SPI0_MOSI_A ALIF_PINMUX(1, 1, 5)
```

端口（Port）1 的引脚（Pin）1：`SPI0_MOSI_A`。

<a id="ae31470618a41e1fa01512589fd7d454d"></a>

### `PIN_P1_1__UART2_TX_A`

```c
#define PIN_P1_1__UART2_TX_A ALIF_PINMUX(1, 1, 2)
```

端口（Port）1 的引脚（Pin）1：`UART2_TX_A`。

<a id="adba91c460bdb9baff03835112cae3258"></a>

### `PIN_P1_2__CX_MWS_SF0`

```c
#define PIN_P1_2__CX_MWS_SF0 ALIF_PINMUX(1, 2, 7)
```

端口（Port）1 的引脚（Pin）2：`CX_MWS_SF0`。

<a id="a6b0ea73c6cb252fda5ad10a28ceae4cf"></a>

### `PIN_P1_2__GPIO`

```c
#define PIN_P1_2__GPIO ALIF_PINMUX(1, 2, 0)
```

引脚 `P1.2` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）2：`GPIO`。

<a id="a64bd88e750072adce1beef23bc18d9c7"></a>

### `PIN_P1_2__LPCAM_D2_A`

```c
#define PIN_P1_2__LPCAM_D2_A ALIF_PINMUX(1, 2, 5)
```

端口（Port）1 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="a21780e98a55451b24b78cee13316750a"></a>

### `PIN_P1_2__LPI2S_SCLK_B`

```c
#define PIN_P1_2__LPI2S_SCLK_B ALIF_PINMUX(1, 2, 3)
```

端口（Port）1 的引脚（Pin）2：`LPI2S_SCLK_B`。

<a id="acfa94e12c954bfef4f2f7a64a31e8157"></a>

### `PIN_P1_2__LPPDM_D1_A`

```c
#define PIN_P1_2__LPPDM_D1_A ALIF_PINMUX(1, 2, 2)
```

端口（Port）1 的引脚（Pin）2：`LPPDM_D1_A`。

<a id="ad5ac88afcac7dfc33106a727e4337899"></a>

### `PIN_P1_2__OSPI0_D2_A`

```c
#define PIN_P1_2__OSPI0_D2_A ALIF_PINMUX(1, 2, 1)
```

端口（Port）1 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="a985eb14aa143e61b4f082b7fd01f45fa"></a>

### `PIN_P1_2__SD_D2_A`

```c
#define PIN_P1_2__SD_D2_A ALIF_PINMUX(1, 2, 6)
```

端口（Port）1 的引脚（Pin）2：`SD_D2_A`。

<a id="a80e2fc726f8004102da0cc8cf2acbaa3"></a>

### `PIN_P1_2__SPI0_SCLK_A`

```c
#define PIN_P1_2__SPI0_SCLK_A ALIF_PINMUX(1, 2, 4)
```

端口（Port）1 的引脚（Pin）2：`SPI0_SCLK_A`。

<a id="ade023cdbfea4810fa301e30db0e0f2c9"></a>

### `PIN_P1_3__CAN1_RXD_A`

```c
#define PIN_P1_3__CAN1_RXD_A ALIF_PINMUX(1, 3, 5)
```

端口（Port）1 的引脚（Pin）3：`CAN1_RXD_A`。

<a id="a8d9249f611752c27fd8dde2e0c85ce97"></a>

### `PIN_P1_3__CX_MWS_SF0`

```c
#define PIN_P1_3__CX_MWS_SF0 ALIF_PINMUX(1, 3, 6)
```

端口（Port）1 的引脚（Pin）3：`CX_MWS_SF0`。

<a id="a7ff354be10a7bcfd9418e346c2f860e5"></a>

### `PIN_P1_3__GPIO`

```c
#define PIN_P1_3__GPIO ALIF_PINMUX(1, 3, 0)
```

引脚 `P1.3` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）3：`GPIO`。

<a id="a7353a8c4b1709432b75cfb14da19094c"></a>

### `PIN_P1_3__I2S1_SCLK_SLV_A`

```c
#define PIN_P1_3__I2S1_SCLK_SLV_A ALIF_PINMUX(1, 3, 3)
```

端口（Port）1 的引脚（Pin）3：`I2S1_SCLK_SLV_A`。

<a id="a5c5aedeee2a3e96123d9a07c43d1b2ee"></a>

### `PIN_P1_3__LPPDM_C1_A`

```c
#define PIN_P1_3__LPPDM_C1_A ALIF_PINMUX(1, 3, 2)
```

端口（Port）1 的引脚（Pin）3：`LPPDM_C1_A`。

<a id="a0c0491e471c23646ec105c560b9d1bfd"></a>

### `PIN_P1_3__LPSPI_MISO_A`

```c
#define PIN_P1_3__LPSPI_MISO_A ALIF_PINMUX(1, 3, 4)
```

端口（Port）1 的引脚（Pin）3：`LPSPI_MISO_A`。

<a id="a4986acb3712740cf61dfb50ababa692a"></a>

### `PIN_P1_3__LPUART_RTS_A`

```c
#define PIN_P1_3__LPUART_RTS_A ALIF_PINMUX(1, 3, 1)
```

端口（Port）1 的引脚（Pin）3：`LPUART_RTS_A`。

<a id="aa4e2b2142b81fad286ff1a3ff1b5703c"></a>

### `PIN_P1_4__CAN1_TXD_A`

```c
#define PIN_P1_4__CAN1_TXD_A ALIF_PINMUX(1, 4, 6)
```

端口（Port）1 的引脚（Pin）4：`CAN1_TXD_A`。

<a id="a438b06a1a987884be2e8bbc6571c2259"></a>

### `PIN_P1_4__CDC_PCLK_A`

```c
#define PIN_P1_4__CDC_PCLK_A ALIF_PINMUX(1, 4, 5)
```

端口（Port）1 的引脚（Pin）4：`CDC_PCLK_A`。

<a id="ac4da87f989323600b4a7be42e67d49bc"></a>

### `PIN_P1_4__CX_MWS_SF1`

```c
#define PIN_P1_4__CX_MWS_SF1 ALIF_PINMUX(1, 4, 7)
```

端口（Port）1 的引脚（Pin）4：`CX_MWS_SF1`。

<a id="ad1e50e7a0add033402abf705b503b80a"></a>

### `PIN_P1_4__GPIO`

```c
#define PIN_P1_4__GPIO ALIF_PINMUX(1, 4, 0)
```

引脚 `P1.4` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）4：`GPIO`。

<a id="af52e204fca8c22a5d8c4b5cac40d5d89"></a>

### `PIN_P1_4__I2C1_SDA_A`

```c
#define PIN_P1_4__I2C1_SDA_A ALIF_PINMUX(1, 4, 4)
```

端口（Port）1 的引脚（Pin）4：`I2C1_SDA_A`。

<a id="a81cb8240e507cda646f00ff6d4dd613d"></a>

### `PIN_P1_4__I2S0_SDI_A`

```c
#define PIN_P1_4__I2S0_SDI_A ALIF_PINMUX(1, 4, 2)
```

端口（Port）1 的引脚（Pin）4：`I2S0_SDI_A`。

<a id="a852d85e129922cc715c7a856c2d363d3"></a>

### `PIN_P1_4__LPPDM_C2_A`

```c
#define PIN_P1_4__LPPDM_C2_A ALIF_PINMUX(1, 4, 1)
```

端口（Port）1 的引脚（Pin）4：`LPPDM_C2_A`。

<a id="a5f628e7f376cba53188fcf6dc8e4baf8"></a>

### `PIN_P1_4__LPSPI_MOSI_A`

```c
#define PIN_P1_4__LPSPI_MOSI_A ALIF_PINMUX(1, 4, 3)
```

端口（Port）1 的引脚（Pin）4：`LPSPI_MOSI_A`。

<a id="ac4e9cd584cc68fed78dad46e1ea5c3b9"></a>

### `PIN_P1_5__CAN1_STBY_A`

```c
#define PIN_P1_5__CAN1_STBY_A ALIF_PINMUX(1, 5, 7)
```

端口（Port）1 的引脚（Pin）5：`CAN1_STBY_A`。

<a id="a32ed27284aad83f3b86e8fee897b06e9"></a>

### `PIN_P1_5__CDC_DE_A`

```c
#define PIN_P1_5__CDC_DE_A ALIF_PINMUX(1, 5, 6)
```

端口（Port）1 的引脚（Pin）5：`CDC_DE_A`。

<a id="a0fb34153badcd47f16246988312d0275"></a>

### `PIN_P1_5__GPIO`

```c
#define PIN_P1_5__GPIO ALIF_PINMUX(1, 5, 0)
```

引脚 `P1.5` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）5：`GPIO`。

<a id="ad3a04ad686eb3f97794c20352361c85d"></a>

### `PIN_P1_5__I2C1_SCLA_A`

```c
#define PIN_P1_5__I2C1_SCLA_A ALIF_PINMUX(1, 5, 4)
```

端口（Port）1 的引脚（Pin）5：`I2C1_SCLA_A`。

<a id="a1d1d1469fccacc9a4d5fcc0580165aaf"></a>

### `PIN_P1_5__I2S0_SDO_A`

```c
#define PIN_P1_5__I2S0_SDO_A ALIF_PINMUX(1, 5, 2)
```

端口（Port）1 的引脚（Pin）5：`I2S0_SDO_A`。

<a id="a09b45ab0a6289d6e7e69abbcb02aac2b"></a>

### `PIN_P1_5__LPPDM_D2_A`

```c
#define PIN_P1_5__LPPDM_D2_A ALIF_PINMUX(1, 5, 1)
```

端口（Port）1 的引脚（Pin）5：`LPPDM_D2_A`。

<a id="a0835421b3b50e0416131d4c063591950"></a>

### `PIN_P1_5__LPSPI_SCLK_A`

```c
#define PIN_P1_5__LPSPI_SCLK_A ALIF_PINMUX(1, 5, 3)
```

端口（Port）1 的引脚（Pin）5：`LPSPI_SCLK_A`。

<a id="a09266ca5f3f0de6444564cb1c786fcd3"></a>

### `PIN_P1_5__SD_RST_A`

```c
#define PIN_P1_5__SD_RST_A ALIF_PINMUX(1, 5, 5)
```

端口（Port）1 的引脚（Pin）5：`SD_RST_A`。

<a id="a4d1002ffd98e0b5c04bd77e809e92c64"></a>

### `PIN_P1_6__CDC_HSYNC_A`

```c
#define PIN_P1_6__CDC_HSYNC_A ALIF_PINMUX(1, 6, 5)
```

端口（Port）1 的引脚（Pin）6：`CDC_HSYNC_A`。

<a id="a1d24eb6e033eca4d0a11d005ece3355b"></a>

### `PIN_P1_6__CX_MWS_SF2`

```c
#define PIN_P1_6__CX_MWS_SF2 ALIF_PINMUX(1, 6, 7)
```

端口（Port）1 的引脚（Pin）6：`CX_MWS_SF2`。

<a id="ab6f0917e71cae608320a3c16b8edf1bf"></a>

### `PIN_P1_6__GPIO`

```c
#define PIN_P1_6__GPIO ALIF_PINMUX(1, 6, 0)
```

引脚 `P1.6` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）6：`GPIO`。

<a id="a74039131f9d4e2d1940cfd8f743ce824"></a>

### `PIN_P1_6__I2S0_SCLK_A`

```c
#define PIN_P1_6__I2S0_SCLK_A ALIF_PINMUX(1, 6, 3)
```

端口（Port）1 的引脚（Pin）6：`I2S0_SCLK_A`。

<a id="a77ea0ac3485787b2f624dc49ebe07df5"></a>

### `PIN_P1_6__I3C_SDA_B`

```c
#define PIN_P1_6__I3C_SDA_B ALIF_PINMUX(1, 6, 6)
```

端口（Port）1 的引脚（Pin）6：`I3C_SDA_B`。

<a id="a54bfd633600c6cc06c628a18595ecb10"></a>

### `PIN_P1_6__LPCAM_D6_A`

```c
#define PIN_P1_6__LPCAM_D6_A ALIF_PINMUX(1, 6, 4)
```

端口（Port）1 的引脚（Pin）6：`LPCAM_D6_A`。

<a id="a5b6b8967ed87f89d7d7b3c7b247d6089"></a>

### `PIN_P1_6__LPPDM_C3_A`

```c
#define PIN_P1_6__LPPDM_C3_A ALIF_PINMUX(1, 6, 2)
```

端口（Port）1 的引脚（Pin）6：`LPPDM_C3_A`。

<a id="ada7bb910d102350d9dcec48198720b93"></a>

### `PIN_P1_6__UART2_RX_A`

```c
#define PIN_P1_6__UART2_RX_A ALIF_PINMUX(1, 6, 1)
```

端口（Port）1 的引脚（Pin）6：`UART2_RX_A`。

<a id="a3b09ec5dce35b51c8246a5cf4093f30b"></a>

### `PIN_P1_7__CDC_VSYNC_A`

```c
#define PIN_P1_7__CDC_VSYNC_A ALIF_PINMUX(1, 7, 5)
```

端口（Port）1 的引脚（Pin）7：`CDC_VSYNC_A`。

<a id="ae182eb7af40754e77554f22083efc6d0"></a>

### `PIN_P1_7__CX_MWS_SF3`

```c
#define PIN_P1_7__CX_MWS_SF3 ALIF_PINMUX(1, 7, 7)
```

端口（Port）1 的引脚（Pin）7：`CX_MWS_SF3`。

<a id="a259e17b2ef415b6aed714af92b5f2ac5"></a>

### `PIN_P1_7__GPIO`

```c
#define PIN_P1_7__GPIO ALIF_PINMUX(1, 7, 0)
```

引脚 `P1.7` 的复用功能（Alternate Functions）。

端口（Port）1 的引脚（Pin）7：`GPIO`。

<a id="ada7e1cdd706c29aaef13c58b96c7ac7f"></a>

### `PIN_P1_7__I2S0_WS_A`

```c
#define PIN_P1_7__I2S0_WS_A ALIF_PINMUX(1, 7, 3)
```

端口（Port）1 的引脚（Pin）7：`I2S0_WS_A`。

<a id="a50b07141b78f1c3aacb82b36900d94ec"></a>

### `PIN_P1_7__I3C_SCL_B`

```c
#define PIN_P1_7__I3C_SCL_B ALIF_PINMUX(1, 7, 6)
```

端口（Port）1 的引脚（Pin）7：`I3C_SCL_B`。

<a id="aeff3a8f52d2d2f6ddad2722f39cde727"></a>

### `PIN_P1_7__LPCAM_D7_A`

```c
#define PIN_P1_7__LPCAM_D7_A ALIF_PINMUX(1, 7, 4)
```

端口（Port）1 的引脚（Pin）7：`LPCAM_D7_A`。

<a id="ae2a93374aabed0d707900021104cf17d"></a>

### `PIN_P1_7__LPPDM_D3_A`

```c
#define PIN_P1_7__LPPDM_D3_A ALIF_PINMUX(1, 7, 2)
```

端口（Port）1 的引脚（Pin）7：`LPPDM_D3_A`。

<a id="a6cd4b29c5faba814bac2a5e272c1b719"></a>

### `PIN_P1_7__UART2_TX_A`

```c
#define PIN_P1_7__UART2_TX_A ALIF_PINMUX(1, 7, 1)
```

端口（Port）1 的引脚（Pin）7：`UART2_TX_A`。

<a id="a5a7560198d64f30347607f3b7417af66"></a>

### `PIN_P2_0__ANA_S8`

```c
#define PIN_P2_0__ANA_S8 ALIF_PINMUX(2, 0, 6)
```

端口（Port）2 的引脚（Pin）0：`ANA_S8`。

<a id="acb1cacef0c6d322a88b1e8da5dce8f14"></a>

### `PIN_P2_0__CX_MWS_SF4`

```c
#define PIN_P2_0__CX_MWS_SF4 ALIF_PINMUX(2, 0, 7)
```

端口（Port）2 的引脚（Pin）0：`CX_MWS_SF4`。

<a id="a2ed50f7f44d929b517287eaae4560f33"></a>

### `PIN_P2_0__GPIO`

```c
#define PIN_P2_0__GPIO ALIF_PINMUX(2, 0, 0)
```

引脚 `P2.0` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）0：`GPIO`。

<a id="a9f5ca61e4e7b13447adf7d83ebed0589"></a>

### `PIN_P2_0__I2S1_SDI_A`

```c
#define PIN_P2_0__I2S1_SDI_A ALIF_PINMUX(2, 0, 3)
```

端口（Port）2 的引脚（Pin）0：`I2S1_SDI_A`。

<a id="a9767a4cdb16cd471bff2d8f1df559606"></a>

### `PIN_P2_0__LPCAM_HSYNC_B`

```c
#define PIN_P2_0__LPCAM_HSYNC_B ALIF_PINMUX(2, 0, 5)
```

端口（Port）2 的引脚（Pin）0：`LPCAM_HSYNC_B`。

<a id="aa161fedd1fad49b89f86f82349225e2e"></a>

### `PIN_P2_0__LPSPI_SS_A`

```c
#define PIN_P2_0__LPSPI_SS_A ALIF_PINMUX(2, 0, 4)
```

端口（Port）2 的引脚（Pin）0：`LPSPI_SS_A`。

<a id="a88da704295f0daa28b21c529a1074282"></a>

### `PIN_P2_0__LPUART_RX_A`

```c
#define PIN_P2_0__LPUART_RX_A ALIF_PINMUX(2, 0, 2)
```

端口（Port）2 的引脚（Pin）0：`LPUART_RX_A`。

<a id="a72dae293916d95004e3ad6e2e085cb1a"></a>

### `PIN_P2_0__OSPI0_SS0_B`

```c
#define PIN_P2_0__OSPI0_SS0_B ALIF_PINMUX(2, 0, 1)
```

端口（Port）2 的引脚（Pin）0：`OSPI0_SS0_B`。

<a id="a261a9f14d4c08b38619a1e92b9437b64"></a>

### `PIN_P2_1__ANA_S9`

```c
#define PIN_P2_1__ANA_S9 ALIF_PINMUX(2, 1, 6)
```

端口（Port）2 的引脚（Pin）1：`ANA_S9`。

<a id="a54e4d2487b39e439e14bf00259f9bfe0"></a>

### `PIN_P2_1__CX_MWS_PAT0`

```c
#define PIN_P2_1__CX_MWS_PAT0 ALIF_PINMUX(2, 1, 7)
```

端口（Port）2 的引脚（Pin）1：`CX_MWS_PAT0`。

<a id="ac05af956aca2528e61e358c597c5b637"></a>

### `PIN_P2_1__GPIO`

```c
#define PIN_P2_1__GPIO ALIF_PINMUX(2, 1, 0)
```

引脚 `P2.1` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）1：`GPIO`。

<a id="a2fa94b5eaef2282dcb59990fadb88903"></a>

### `PIN_P2_1__I2S1_SDO_A`

```c
#define PIN_P2_1__I2S1_SDO_A ALIF_PINMUX(2, 1, 3)
```

端口（Port）2 的引脚（Pin）1：`I2S1_SDO_A`。

<a id="abb84790ef7fdd51429b869c60b9cc84d"></a>

### `PIN_P2_1__LPI2C0_SCL_B`

```c
#define PIN_P2_1__LPI2C0_SCL_B ALIF_PINMUX(2, 1, 4)
```

端口（Port）2 的引脚（Pin）1：`LPI2C0_SCL_B`。

<a id="a68efa41efddb6154f6e67238caa96f55"></a>

### `PIN_P2_1__LPUART_TX_A`

```c
#define PIN_P2_1__LPUART_TX_A ALIF_PINMUX(2, 1, 2)
```

端口（Port）2 的引脚（Pin）1：`LPUART_TX_A`。

<a id="a18ca55a1ac5dbc69b5e53d51286c9e7c"></a>

### `PIN_P2_1__OSPI0_SS1_B`

```c
#define PIN_P2_1__OSPI0_SS1_B ALIF_PINMUX(2, 1, 1)
```

端口（Port）2 的引脚（Pin）1：`OSPI0_SS1_B`。

<a id="aab1b851c0104dc9889b0eb66fb6c155b"></a>

### `PIN_P2_1__UT0_T1_A`

```c
#define PIN_P2_1__UT0_T1_A ALIF_PINMUX(2, 1, 5)
```

端口（Port）2 的引脚（Pin）1：`UT0_T1_A`。

<a id="abc41608c0c3830bca1c4d1b13bdf5691"></a>

### `PIN_P2_2__ANA_S10`

```c
#define PIN_P2_2__ANA_S10 ALIF_PINMUX(2, 2, 5)
```

端口（Port）2 的引脚（Pin）2：`ANA_S10`。

<a id="ac9e833de34324c123cb33ae8e57cad21"></a>

### `PIN_P2_2__CX_MWS_PAT1`

```c
#define PIN_P2_2__CX_MWS_PAT1 ALIF_PINMUX(2, 2, 6)
```

端口（Port）2 的引脚（Pin）2：`CX_MWS_PAT1`。

<a id="a3fc212b07d980d4ae21a1743da443ac8"></a>

### `PIN_P2_2__GPIO`

```c
#define PIN_P2_2__GPIO ALIF_PINMUX(2, 2, 0)
```

引脚 `P2.2` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）2：`GPIO`。

<a id="a15ff3015d007e89490a604afe45ec84d"></a>

### `PIN_P2_2__I2S1_SCLK_SLV_A`

```c
#define PIN_P2_2__I2S1_SCLK_SLV_A ALIF_PINMUX(2, 2, 2)
```

端口（Port）2 的引脚（Pin）2：`I2S1_SCLK_SLV_A`。

<a id="afb814e15c86aa147acff7e4b06313bdc"></a>

### `PIN_P2_2__LPI2C0_SDA_B`

```c
#define PIN_P2_2__LPI2C0_SDA_B ALIF_PINMUX(2, 2, 3)
```

端口（Port）2 的引脚（Pin）2：`LPI2C0_SDA_B`。

<a id="a70ba485bfc0e12dd07aa04ac6055df8f"></a>

### `PIN_P2_2__LPUART_RTS_A`

```c
#define PIN_P2_2__LPUART_RTS_A ALIF_PINMUX(2, 2, 1)
```

端口（Port）2 的引脚（Pin）2：`LPUART_RTS_A`。

<a id="a55c235d4c2f152461414381ca914187e"></a>

### `PIN_P2_2__UT1_T0_A`

```c
#define PIN_P2_2__UT1_T0_A ALIF_PINMUX(2, 2, 4)
```

端口（Port）2 的引脚（Pin）2：`UT1_T0_A`。

<a id="a72c628f0e6dc25e0816a40e3ca252f30"></a>

### `PIN_P2_3__ANA_S11`

```c
#define PIN_P2_3__ANA_S11 ALIF_PINMUX(2, 3, 6)
```

端口（Port）2 的引脚（Pin）3：`ANA_S11`。

<a id="a2819bc2ec4b910739f12065b99efe98d"></a>

### `PIN_P2_3__CAN0_RXD_A`

```c
#define PIN_P2_3__CAN0_RXD_A ALIF_PINMUX(2, 3, 5)
```

端口（Port）2 的引脚（Pin）3：`CAN0_RXD_A`。

<a id="af99be1d667e2c817c3007c11c5ca2d49"></a>

### `PIN_P2_3__CX_MWS_SYNC`

```c
#define PIN_P2_3__CX_MWS_SYNC ALIF_PINMUX(2, 3, 7)
```

端口（Port）2 的引脚（Pin）3：`CX_MWS_SYNC`。

<a id="a8408f18132258a0ef9fb8c3fe4f33977"></a>

### `PIN_P2_3__GPIO`

```c
#define PIN_P2_3__GPIO ALIF_PINMUX(2, 3, 0)
```

引脚 `P2.3` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）3：`GPIO`。

<a id="a78aa0182ca489e9b3f11b1c247552228"></a>

### `PIN_P2_3__I2S1_WS_SLV_A`

```c
#define PIN_P2_3__I2S1_WS_SLV_A ALIF_PINMUX(2, 3, 2)
```

端口（Port）2 的引脚（Pin）3：`I2S1_WS_SLV_A`。

<a id="ab0a7d39ed08e3175c520c240de446a01"></a>

### `PIN_P2_3__LPUART_CTS_A`

```c
#define PIN_P2_3__LPUART_CTS_A ALIF_PINMUX(2, 3, 1)
```

端口（Port）2 的引脚（Pin）3：`LPUART_CTS_A`。

<a id="a410ee38ad792684ccd0f00e8a0c0f62f"></a>

### `PIN_P2_3__SD_RST_A`

```c
#define PIN_P2_3__SD_RST_A ALIF_PINMUX(2, 3, 4)
```

端口（Port）2 的引脚（Pin）3：`SD_RST_A`。

<a id="a16fe807eaee34126a00a11ba747e113e"></a>

### `PIN_P2_3__UT1_T1_A`

```c
#define PIN_P2_3__UT1_T1_A ALIF_PINMUX(2, 3, 3)
```

端口（Port）2 的引脚（Pin）3：`UT1_T1_A`。

<a id="a5ad9a9c92200896609d122bb0e81e8a0"></a>

### `PIN_P2_4__ANA_S12`

```c
#define PIN_P2_4__ANA_S12 ALIF_PINMUX(2, 4, 6)
```

端口（Port）2 的引脚（Pin）4：`ANA_S12`。

<a id="acbcc2a9351cb7eac4c28833e9f725677"></a>

### `PIN_P2_4__CAN0_TXD_A`

```c
#define PIN_P2_4__CAN0_TXD_A ALIF_PINMUX(2, 4, 5)
```

端口（Port）2 的引脚（Pin）4：`CAN0_TXD_A`。

<a id="ae365e707419062f080c974aecfe0e9e0"></a>

### `PIN_P2_4__CX_MWS_TX`

```c
#define PIN_P2_4__CX_MWS_TX ALIF_PINMUX(2, 4, 7)
```

端口（Port）2 的引脚（Pin）4：`CX_MWS_TX`。

<a id="a649d4dc937e3cb6269408b128ed3aae3"></a>

### `PIN_P2_4__GPIO`

```c
#define PIN_P2_4__GPIO ALIF_PINMUX(2, 4, 0)
```

引脚 `P2.4` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）4：`GPIO`。

<a id="aea227c4b940cdfdbbb491fef80270cab"></a>

### `PIN_P2_4__I2C0_SCL_B`

```c
#define PIN_P2_4__I2C0_SCL_B ALIF_PINMUX(2, 4, 3)
```

端口（Port）2 的引脚（Pin）4：`I2C0_SCL_B`。

<a id="a021d984d183324f18d2b63cffae1f918"></a>

### `PIN_P2_4__I2S0_SDI_B`

```c
#define PIN_P2_4__I2S0_SDI_B ALIF_PINMUX(2, 4, 2)
```

端口（Port）2 的引脚（Pin）4：`I2S0_SDI_B`。

<a id="ad87b8ed21814361c00b172b73afd49d1"></a>

### `PIN_P2_4__UART3_RX_A`

```c
#define PIN_P2_4__UART3_RX_A ALIF_PINMUX(2, 4, 1)
```

端口（Port）2 的引脚（Pin）4：`UART3_RX_A`。

<a id="a595a81d1d4a9e4f93d13049d0a966915"></a>

### `PIN_P2_4__UT2_T0_A`

```c
#define PIN_P2_4__UT2_T0_A ALIF_PINMUX(2, 4, 4)
```

端口（Port）2 的引脚（Pin）4：`UT2_T0_A`。

<a id="a9e1eb637336aa83aa460dd7e14ecd6bf"></a>

### `PIN_P2_5__ANA_S13`

```c
#define PIN_P2_5__ANA_S13 ALIF_PINMUX(2, 5, 6)
```

端口（Port）2 的引脚（Pin）5：`ANA_S13`。

<a id="af21c79f39e818aba2dd8185b31d61987"></a>

### `PIN_P2_5__CAN0_STBY_A`

```c
#define PIN_P2_5__CAN0_STBY_A ALIF_PINMUX(2, 5, 5)
```

端口（Port）2 的引脚（Pin）5：`CAN0_STBY_A`。

<a id="a53a063c6f4fe109d49a011f4f2e50d19"></a>

### `PIN_P2_5__CX_MWS_RX`

```c
#define PIN_P2_5__CX_MWS_RX ALIF_PINMUX(2, 5, 7)
```

端口（Port）2 的引脚（Pin）5：`CX_MWS_RX`。

<a id="ac399d584c2f7dbdf0a2ceeb91a9a9ea0"></a>

### `PIN_P2_5__GPIO`

```c
#define PIN_P2_5__GPIO ALIF_PINMUX(2, 5, 0)
```

引脚 `P2.5` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）5：`GPIO`。

<a id="a163ef064afe3540c8f61091a69781b4b"></a>

### `PIN_P2_5__I2C0_SDA_B`

```c
#define PIN_P2_5__I2C0_SDA_B ALIF_PINMUX(2, 5, 3)
```

端口（Port）2 的引脚（Pin）5：`I2C0_SDA_B`。

<a id="a960479f610500a14c90ad06af4046d4b"></a>

### `PIN_P2_5__I2S0_SDO_B`

```c
#define PIN_P2_5__I2S0_SDO_B ALIF_PINMUX(2, 5, 2)
```

端口（Port）2 的引脚（Pin）5：`I2S0_SDO_B`。

<a id="a32cdfdf070321c2dc45b600554935d1c"></a>

### `PIN_P2_5__UART3_TX_A`

```c
#define PIN_P2_5__UART3_TX_A ALIF_PINMUX(2, 5, 1)
```

端口（Port）2 的引脚（Pin）5：`UART3_TX_A`。

<a id="a6f783a7eeaae764b087000d898124f45"></a>

### `PIN_P2_5__UT2_T1_A`

```c
#define PIN_P2_5__UT2_T1_A ALIF_PINMUX(2, 5, 4)
```

端口（Port）2 的引脚（Pin）5：`UT2_T1_A`。

<a id="aecc3c9c2a85fd42569f9c4559101bd7c"></a>

### `PIN_P2_6__ANA_S14`

```c
#define PIN_P2_6__ANA_S14 ALIF_PINMUX(2, 6, 6)
```

端口（Port）2 的引脚（Pin）6：`ANA_S14`。

<a id="acf70da7d084f17a152af48ea6ef34527"></a>

### `PIN_P2_6__GPIO`

```c
#define PIN_P2_6__GPIO ALIF_PINMUX(2, 6, 0)
```

引脚 `P2.6` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）6：`GPIO`。

<a id="ae2cc326e40642086ffefa929c5c01ac5"></a>

### `PIN_P2_6__I2C1_SDA_B`

```c
#define PIN_P2_6__I2C1_SDA_B ALIF_PINMUX(2, 6, 3)
```

端口（Port）2 的引脚（Pin）6：`I2C1_SDA_B`。

<a id="ab7b482cc545e06022c8549c62a5796d7"></a>

### `PIN_P2_6__I2S0_SCLK_B`

```c
#define PIN_P2_6__I2S0_SCLK_B ALIF_PINMUX(2, 6, 2)
```

端口（Port）2 的引脚（Pin）6：`I2S0_SCLK_B`。

<a id="ad89370bf62edbef192a85783afd63b3e"></a>

### `PIN_P2_6__UART4_RX_A`

```c
#define PIN_P2_6__UART4_RX_A ALIF_PINMUX(2, 6, 1)
```

端口（Port）2 的引脚（Pin）6：`UART4_RX_A`。

<a id="afe56bb2aa798518976190a959d88fdb6"></a>

### `PIN_P2_6__UT3_T0_A`

```c
#define PIN_P2_6__UT3_T0_A ALIF_PINMUX(2, 6, 4)
```

端口（Port）2 的引脚（Pin）6：`UT3_T0_A`。

<a id="a1a690217c990dac7671bcad9e6855e4c"></a>

### `PIN_P2_7__ANA_S15`

```c
#define PIN_P2_7__ANA_S15 ALIF_PINMUX(2, 7, 6)
```

端口（Port）2 的引脚（Pin）7：`ANA_S15`。

<a id="ab3f711dc40129f35a38cec46e12f23dd"></a>

### `PIN_P2_7__GPIO`

```c
#define PIN_P2_7__GPIO ALIF_PINMUX(2, 7, 0)
```

引脚 `P2.7` 的复用功能（Alternate Functions）。

端口（Port）2 的引脚（Pin）7：`GPIO`。

<a id="a77dba1bd3536b87c3b804b4b5c8844c5"></a>

### `PIN_P2_7__I2C1_SCL_B`

```c
#define PIN_P2_7__I2C1_SCL_B ALIF_PINMUX(2, 7, 3)
```

端口（Port）2 的引脚（Pin）7：`I2C1_SCL_B`。

<a id="a5c52059835751817fa789428c272b4b2"></a>

### `PIN_P2_7__I2S0_WS_B`

```c
#define PIN_P2_7__I2S0_WS_B ALIF_PINMUX(2, 7, 2)
```

端口（Port）2 的引脚（Pin）7：`I2S0_WS_B`。

<a id="a24548c32d58d93a273c702862ac1f101"></a>

### `PIN_P2_7__UART4_TX_A`

```c
#define PIN_P2_7__UART4_TX_A ALIF_PINMUX(2, 7, 1)
```

端口（Port）2 的引脚（Pin）7：`UART4_TX_A`。

<a id="af33c77692ea55157dde2a366df179946"></a>

### `PIN_P2_7__UT3_T1_A`

```c
#define PIN_P2_7__UT3_T1_A ALIF_PINMUX(2, 7, 4)
```

端口（Port）2 的引脚（Pin）7：`UT3_T1_A`。

<a id="acbf62e57bca8f709a7c999b310d49fd8"></a>

### `PIN_P3_0__CDC_HSYNC_B`

```c
#define PIN_P3_0__CDC_HSYNC_B ALIF_PINMUX(3, 0, 6)
```

端口（Port）3 的引脚（Pin）0：`CDC_HSYNC_B`。

<a id="aeb39304438c089405b315935caa1d90b"></a>

### `PIN_P3_0__GPIO`

```c
#define PIN_P3_0__GPIO ALIF_PINMUX(3, 0, 0)
```

引脚 `P3.0` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）0：`GPIO`。

<a id="ab272993eba936e78b7b49628656270c0"></a>

### `PIN_P3_0__I2S1_SDI_B`

```c
#define PIN_P3_0__I2S1_SDI_B ALIF_PINMUX(3, 0, 4)
```

端口（Port）3 的引脚（Pin）0：`I2S1_SDI_B`。

<a id="a657f73711ba0d8cc715200c6d00f12a0"></a>

### `PIN_P3_0__LPPDM_C0_B`

```c
#define PIN_P3_0__LPPDM_C0_B ALIF_PINMUX(3, 0, 3)
```

端口（Port）3 的引脚（Pin）0：`LPPDM_C0_B`。

<a id="a08e6a0f6bde4e7bb7585c23d89d26e34"></a>

### `PIN_P3_0__OSPI0_D0_A`

```c
#define PIN_P3_0__OSPI0_D0_A ALIF_PINMUX(3, 0, 1)
```

端口（Port）3 的引脚（Pin）0：`OSPI0_D0_A`。

<a id="a180a5337fefee4470d0207159a3a6b89"></a>

### `PIN_P3_0__SPI2_MISO_A`

```c
#define PIN_P3_0__SPI2_MISO_A ALIF_PINMUX(3, 0, 5)
```

端口（Port）3 的引脚（Pin）0：`SPI2_MISO_A`。

<a id="aca5323c8961628d66981805dc76e426d"></a>

### `PIN_P3_0__UART5_RX_A`

```c
#define PIN_P3_0__UART5_RX_A ALIF_PINMUX(3, 0, 2)
```

端口（Port）3 的引脚（Pin）0：`UART5_RX_A`。

<a id="a125d130d6c1407193272677f26989444"></a>

### `PIN_P3_1__CDC_VSYNC_B`

```c
#define PIN_P3_1__CDC_VSYNC_B ALIF_PINMUX(3, 1, 6)
```

端口（Port）3 的引脚（Pin）1：`CDC_VSYNC_B`。

<a id="a6cd05b1a797d571a1d1d1981ba849f8f"></a>

### `PIN_P3_1__GPIO`

```c
#define PIN_P3_1__GPIO ALIF_PINMUX(3, 1, 0)
```

引脚 `P3.1` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）1：`GPIO`。

<a id="a4b5b4b545552f71a7119ae29b2b4b4ec"></a>

### `PIN_P3_1__I2S1_SDO_B`

```c
#define PIN_P3_1__I2S1_SDO_B ALIF_PINMUX(3, 1, 4)
```

端口（Port）3 的引脚（Pin）1：`I2S1_SDO_B`。

<a id="af2b49d47624cdb616d2c7726cb63cc25"></a>

### `PIN_P3_1__LPPDM_D0_B`

```c
#define PIN_P3_1__LPPDM_D0_B ALIF_PINMUX(3, 1, 3)
```

端口（Port）3 的引脚（Pin）1：`LPPDM_D0_B`。

<a id="a6b9214690f4a38d21962692dd8d8a48f"></a>

### `PIN_P3_1__OSPI0_D1_A`

```c
#define PIN_P3_1__OSPI0_D1_A ALIF_PINMUX(3, 1, 1)
```

端口（Port）3 的引脚（Pin）1：`OSPI0_D1_A`。

<a id="a65ecac46cfcbed6eb9c9703176a73159"></a>

### `PIN_P3_1__SPI2_MOSI_A`

```c
#define PIN_P3_1__SPI2_MOSI_A ALIF_PINMUX(3, 1, 5)
```

端口（Port）3 的引脚（Pin）1：`SPI2_MOSI_A`。

<a id="abb45e90dbe3e11cdb30a79ee1ad737da"></a>

### `PIN_P3_1__UART5_TX_A`

```c
#define PIN_P3_1__UART5_TX_A ALIF_PINMUX(3, 1, 2)
```

端口（Port）3 的引脚（Pin）1：`UART5_TX_A`。

<a id="a8204e79617e38dcd9183dce74f30caaf"></a>

### `PIN_P3_2__CDC_PCLK_B`

```c
#define PIN_P3_2__CDC_PCLK_B ALIF_PINMUX(3, 2, 6)
```

端口（Port）3 的引脚（Pin）2：`CDC_PCLK_B`。

<a id="a4bfd126d24cab1669b9880c163e9b73a"></a>

### `PIN_P3_2__GPIO`

```c
#define PIN_P3_2__GPIO ALIF_PINMUX(3, 2, 0)
```

引脚 `P3.2` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）2：`GPIO`。

<a id="a0ae2607bb670c7e115a600cb35462e49"></a>

### `PIN_P3_2__I2S1_SCLK_SLV_B`

```c
#define PIN_P3_2__I2S1_SCLK_SLV_B ALIF_PINMUX(3, 2, 4)
```

端口（Port）3 的引脚（Pin）2：`I2S1_SCLK_SLV_B`。

<a id="a5c1597499610b3867a91dcbd15fccf39"></a>

### `PIN_P3_2__LPPDM_C1_B`

```c
#define PIN_P3_2__LPPDM_C1_B ALIF_PINMUX(3, 2, 3)
```

端口（Port）3 的引脚（Pin）2：`LPPDM_C1_B`。

<a id="acac0bc02b88cfffac293e54860f915b6"></a>

### `PIN_P3_2__OSPI0_D2_A`

```c
#define PIN_P3_2__OSPI0_D2_A ALIF_PINMUX(3, 2, 1)
```

端口（Port）3 的引脚（Pin）2：`OSPI0_D2_A`。

<a id="a02f965e1da21a78ada64cfb1f31d7753"></a>

### `PIN_P3_2__SPI2_SCLK_A`

```c
#define PIN_P3_2__SPI2_SCLK_A ALIF_PINMUX(3, 2, 5)
```

端口（Port）3 的引脚（Pin）2：`SPI2_SCLK_A`。

<a id="a7119fa1cbc0ca291d2aba6fb742bf6f8"></a>

### `PIN_P3_2__UART3_RX_B`

```c
#define PIN_P3_2__UART3_RX_B ALIF_PINMUX(3, 2, 2)
```

端口（Port）3 的引脚（Pin）2：`UART3_RX_B`。

<a id="a8a657205eda7450f90f32a1e7b85d5bc"></a>

### `PIN_P3_3__CDC_DE_B`

```c
#define PIN_P3_3__CDC_DE_B ALIF_PINMUX(3, 3, 6)
```

端口（Port）3 的引脚（Pin）3：`CDC_DE_B`。

<a id="ac22b3e259b7eac30c576114860368ae4"></a>

### `PIN_P3_3__GPIO`

```c
#define PIN_P3_3__GPIO ALIF_PINMUX(3, 3, 0)
```

引脚 `P3.3` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）3：`GPIO`。

<a id="a19299a3b792e33a1632d329de35aa6cb"></a>

### `PIN_P3_3__I2S1_WS_SLV_B`

```c
#define PIN_P3_3__I2S1_WS_SLV_B ALIF_PINMUX(3, 3, 4)
```

端口（Port）3 的引脚（Pin）3：`I2S1_WS_SLV_B`。

<a id="a22392f2d0211f8d72d4c3e55bb09d579"></a>

### `PIN_P3_3__LPPDM_D1_B`

```c
#define PIN_P3_3__LPPDM_D1_B ALIF_PINMUX(3, 3, 3)
```

端口（Port）3 的引脚（Pin）3：`LPPDM_D1_B`。

<a id="ad01b9c7e9987a9f24df78666736d7c64"></a>

### `PIN_P3_3__OSPI0_D3_A`

```c
#define PIN_P3_3__OSPI0_D3_A ALIF_PINMUX(3, 3, 1)
```

端口（Port）3 的引脚（Pin）3：`OSPI0_D3_A`。

<a id="ae50bd1782360494a12bada142b5a5fbe"></a>

### `PIN_P3_3__SPI2_SS0_A`

```c
#define PIN_P3_3__SPI2_SS0_A ALIF_PINMUX(3, 3, 5)
```

端口（Port）3 的引脚（Pin）3：`SPI2_SS0_A`。

<a id="acd31e37bd65d6ee81bf629388730b2de"></a>

### `PIN_P3_3__UART3_TX_B`

```c
#define PIN_P3_3__UART3_TX_B ALIF_PINMUX(3, 3, 2)
```

端口（Port）3 的引脚（Pin）3：`UART3_TX_B`。

<a id="a334331e4bebc81e43c8007e45dbe41ca"></a>

### `PIN_P3_4__CMP0_OUT_A`

```c
#define PIN_P3_4__CMP0_OUT_A ALIF_PINMUX(3, 4, 6)
```

端口（Port）3 的引脚（Pin）4：`CMP0_OUT_A`。

<a id="af826ee88e3ed085269f16bee4a1a5bd7"></a>

### `PIN_P3_4__GPIO`

```c
#define PIN_P3_4__GPIO ALIF_PINMUX(3, 4, 0)
```

引脚 `P3.4` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）4：`GPIO`。

<a id="ac81d90635b271e413d3a8216c98f6a64"></a>

### `PIN_P3_4__LPCAM_VSYNC_A`

```c
#define PIN_P3_4__LPCAM_VSYNC_A ALIF_PINMUX(3, 4, 4)
```

端口（Port）3 的引脚（Pin）4：`LPCAM_VSYNC_A`。

<a id="a4ac9aba64d45c9ac940c369519715fcc"></a>

### `PIN_P3_4__LPPDM_C2_B`

```c
#define PIN_P3_4__LPPDM_C2_B ALIF_PINMUX(3, 4, 2)
```

端口（Port）3 的引脚（Pin）4：`LPPDM_C2_B`。

<a id="a6b6cb80eb2ec08d5a72dad514fbe6717"></a>

### `PIN_P3_4__OSPI0_D4_A`

```c
#define PIN_P3_4__OSPI0_D4_A ALIF_PINMUX(3, 4, 1)
```

端口（Port）3 的引脚（Pin）4：`OSPI0_D4_A`。

<a id="a0d63779879e818e7185ac29a5251be7a"></a>

### `PIN_P3_4__SD_CMD_A`

```c
#define PIN_P3_4__SD_CMD_A ALIF_PINMUX(3, 4, 5)
```

端口（Port）3 的引脚（Pin）4：`SD_CMD_A`。

<a id="ac11d291faff2b72ae43b542cdfa79b43"></a>

### `PIN_P3_4__SPI1_MISO_A`

```c
#define PIN_P3_4__SPI1_MISO_A ALIF_PINMUX(3, 4, 3)
```

端口（Port）3 的引脚（Pin）4：`SPI1_MISO_A`。

<a id="a1ccd8435bb96e65d67b09d351dc95bd4"></a>

### `PIN_P3_5__CMP1_OUT_A`

```c
#define PIN_P3_5__CMP1_OUT_A ALIF_PINMUX(3, 5, 6)
```

端口（Port）3 的引脚（Pin）5：`CMP1_OUT_A`。

<a id="a3f53dddbffc228108e7c1eb17ee058a4"></a>

### `PIN_P3_5__GPIO`

```c
#define PIN_P3_5__GPIO ALIF_PINMUX(3, 5, 0)
```

引脚 `P3.5` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）5：`GPIO`。

<a id="ab4bd78c83bf8c6916c350b0582a127b4"></a>

### `PIN_P3_5__LPCAM_HSYNC_A`

```c
#define PIN_P3_5__LPCAM_HSYNC_A ALIF_PINMUX(3, 5, 4)
```

端口（Port）3 的引脚（Pin）5：`LPCAM_HSYNC_A`。

<a id="a693d2fc47da86e789e016b3367a6a945"></a>

### `PIN_P3_5__LPPDM_D2_B`

```c
#define PIN_P3_5__LPPDM_D2_B ALIF_PINMUX(3, 5, 2)
```

端口（Port）3 的引脚（Pin）5：`LPPDM_D2_B`。

<a id="a07dc35c610e8c3cc067ce280102894da"></a>

### `PIN_P3_5__OSPI0_D5_A`

```c
#define PIN_P3_5__OSPI0_D5_A ALIF_PINMUX(3, 5, 1)
```

端口（Port）3 的引脚（Pin）5：`OSPI0_D5_A`。

<a id="a2e462b52b0754c84210ee53bccdf7cf3"></a>

### `PIN_P3_5__SD_CLK_A`

```c
#define PIN_P3_5__SD_CLK_A ALIF_PINMUX(3, 5, 5)
```

端口（Port）3 的引脚（Pin）5：`SD_CLK_A`。

<a id="a408a4a0e8b2cc3ba0ed810c2c4d797ba"></a>

### `PIN_P3_5__SPI1_MOSI_A`

```c
#define PIN_P3_5__SPI1_MOSI_A ALIF_PINMUX(3, 5, 3)
```

端口（Port）3 的引脚（Pin）5：`SPI1_MOSI_A`。

<a id="aedf1d5746a7b7f7fbf815a3518a4be67"></a>

### `PIN_P3_6__CX_WLAN_TX`

```c
#define PIN_P3_6__CX_WLAN_TX ALIF_PINMUX(3, 6, 7)
```

端口（Port）3 的引脚（Pin）6：`CX_WLAN_TX`。

<a id="acfdc172b1746aa6cb05a46782d84b8e3"></a>

### `PIN_P3_6__EXT_RTS_A`

```c
#define PIN_P3_6__EXT_RTS_A ALIF_PINMUX(3, 6, 6)
```

端口（Port）3 的引脚（Pin）6：`EXT_RTS_A`。

<a id="a6de92753c75d2827828767a9ed529829"></a>

### `PIN_P3_6__GPIO`

```c
#define PIN_P3_6__GPIO ALIF_PINMUX(3, 6, 0)
```

引脚 `P3.6` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）6：`GPIO`。

<a id="adda246545320f5be35347ad5756f96f3"></a>

### `PIN_P3_6__LPCAM_PCLK_A`

```c
#define PIN_P3_6__LPCAM_PCLK_A ALIF_PINMUX(3, 6, 5)
```

端口（Port）3 的引脚（Pin）6：`LPCAM_PCLK_A`。

<a id="a266153536a0c5ae308ec86013f04eef2"></a>

### `PIN_P3_6__LPPDM_C3_B`

```c
#define PIN_P3_6__LPPDM_C3_B ALIF_PINMUX(3, 6, 3)
```

端口（Port）3 的引脚（Pin）6：`LPPDM_C3_B`。

<a id="aea873d99be810ba6e9a710720e2d2f76"></a>

### `PIN_P3_6__OSPI0_D6_A`

```c
#define PIN_P3_6__OSPI0_D6_A ALIF_PINMUX(3, 6, 1)
```

端口（Port）3 的引脚（Pin）6：`OSPI0_D6_A`。

<a id="a46572ca90cf7364a9664816bb5a7cc30"></a>

### `PIN_P3_6__SPI1_SCLK_A`

```c
#define PIN_P3_6__SPI1_SCLK_A ALIF_PINMUX(3, 6, 4)
```

端口（Port）3 的引脚（Pin）6：`SPI1_SCLK_A`。

<a id="a6995bac7197a680fc2d5835934758ccc"></a>

### `PIN_P3_6__UART4_RX_B`

```c
#define PIN_P3_6__UART4_RX_B ALIF_PINMUX(3, 6, 2)
```

端口（Port）3 的引脚（Pin）6：`UART4_RX_B`。

<a id="a08ce04f3e23b3249a99007cdc01b486a"></a>

### `PIN_P3_7__CX_WLAN_RX`

```c
#define PIN_P3_7__CX_WLAN_RX ALIF_PINMUX(3, 7, 7)
```

端口（Port）3 的引脚（Pin）7：`CX_WLAN_RX`。

<a id="a97ddd001f0aaa2f9077d304d66036f61"></a>

### `PIN_P3_7__EXT_CTS_A`

```c
#define PIN_P3_7__EXT_CTS_A ALIF_PINMUX(3, 7, 6)
```

端口（Port）3 的引脚（Pin）7：`EXT_CTS_A`。

<a id="a60d3cb4a00a06169c18eedd0593c0e3b"></a>

### `PIN_P3_7__GPIO`

```c
#define PIN_P3_7__GPIO ALIF_PINMUX(3, 7, 0)
```

引脚 `P3.7` 的复用功能（Alternate Functions）。

端口（Port）3 的引脚（Pin）7：`GPIO`。

<a id="ab41862028c94474a27360852a45b492a"></a>

### `PIN_P3_7__LPCAM_XVCLK_A`

```c
#define PIN_P3_7__LPCAM_XVCLK_A ALIF_PINMUX(3, 7, 4)
```

端口（Port）3 的引脚（Pin）7：`LPCAM_XVCLK_A`。

<a id="a50b7bcbbbfe2e4b6eb7a4a8dba31e4a9"></a>

### `PIN_P3_7__LPPDM_D3_B`

```c
#define PIN_P3_7__LPPDM_D3_B ALIF_PINMUX(3, 7, 3)
```

端口（Port）3 的引脚（Pin）7：`LPPDM_D3_B`。

<a id="a03367dff465d39650944aed091c5529f"></a>

### `PIN_P3_7__OSPI0_D7_A`

```c
#define PIN_P3_7__OSPI0_D7_A ALIF_PINMUX(3, 7, 1)
```

端口（Port）3 的引脚（Pin）7：`OSPI0_D7_A`。

<a id="ac471eaf7fde1a025f146c40a4a1cb74b"></a>

### `PIN_P3_7__SD_RST_B`

```c
#define PIN_P3_7__SD_RST_B ALIF_PINMUX(3, 7, 5)
```

端口（Port）3 的引脚（Pin）7：`SD_RST_B`。

<a id="a6a8d56588c6366fd712451566aaad6b0"></a>

### `PIN_P3_7__UART4_TX_B`

```c
#define PIN_P3_7__UART4_TX_B ALIF_PINMUX(3, 7, 2)
```

端口（Port）3 的引脚（Pin）7：`UART4_TX_B`。

<a id="a18718ec4f3d76dc2c004254ce07fb79b"></a>

### `PIN_P4_0__EXT_RX_A`

```c
#define PIN_P4_0__EXT_RX_A ALIF_PINMUX(4, 0, 7)
```

端口（Port）4 的引脚（Pin）0：`EXT_RX_A`。

<a id="a1ab2ef5cf337828d3e4be24bba3391e6"></a>

### `PIN_P4_0__GPIO`

```c
#define PIN_P4_0__GPIO ALIF_PINMUX(4, 0, 0)
```

引脚 `P4.0` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）0：`GPIO`。

<a id="ae25864e7506f7b27e332543d2470fddf"></a>

### `PIN_P4_0__LPCAM_D0_A`

```c
#define PIN_P4_0__LPCAM_D0_A ALIF_PINMUX(4, 0, 5)
```

端口（Port）4 的引脚（Pin）0：`LPCAM_D0_A`。

<a id="aa4a65ef0d12969c5f86e959537887b2d"></a>

### `PIN_P4_0__OSPI0_SCLKN_A`

```c
#define PIN_P4_0__OSPI0_SCLKN_A ALIF_PINMUX(4, 0, 1)
```

端口（Port）4 的引脚（Pin）0：`OSPI0_SCLKN_A`。

<a id="a1a292ebb91985973ab40aeee4e5d89cf"></a>

### `PIN_P4_0__SD_D0_A`

```c
#define PIN_P4_0__SD_D0_A ALIF_PINMUX(4, 0, 6)
```

端口（Port）4 的引脚（Pin）0：`SD_D0_A`。

<a id="a0ce696d8a98527b7aef206be42f9cc64"></a>

### `PIN_P4_0__SPI2_SS1_A`

```c
#define PIN_P4_0__SPI2_SS1_A ALIF_PINMUX(4, 0, 3)
```

端口（Port）4 的引脚（Pin）0：`SPI2_SS1_A`。

<a id="a746064cb94df8b7298905f74a9c8ecdc"></a>

### `PIN_P4_0__UART0_RX_B`

```c
#define PIN_P4_0__UART0_RX_B ALIF_PINMUX(4, 0, 2)
```

端口（Port）4 的引脚（Pin）0：`UART0_RX_B`。

<a id="a5e7e485258c9cefe47c4a4787624d3ca"></a>

### `PIN_P4_0__UT0_T0_A`

```c
#define PIN_P4_0__UT0_T0_A ALIF_PINMUX(4, 0, 4)
```

端口（Port）4 的引脚（Pin）0：`UT0_T0_A`。

<a id="af1b2095550709b1e14c30ad6ae474771"></a>

### `PIN_P4_1__EXT_TX_A`

```c
#define PIN_P4_1__EXT_TX_A ALIF_PINMUX(4, 1, 7)
```

端口（Port）4 的引脚（Pin）1：`EXT_TX_A`。

<a id="a5fb4375020986c6656759f3223558f10"></a>

### `PIN_P4_1__GPIO`

```c
#define PIN_P4_1__GPIO ALIF_PINMUX(4, 1, 0)
```

引脚 `P4.1` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）1：`GPIO`。

<a id="ac2829e522c09bde1f8dcc9ec0e1e8b9c"></a>

### `PIN_P4_1__LPCAM_D1_A`

```c
#define PIN_P4_1__LPCAM_D1_A ALIF_PINMUX(4, 1, 5)
```

端口（Port）4 的引脚（Pin）1：`LPCAM_D1_A`。

<a id="a0df28f60edf04802895e2e65c8c62700"></a>

### `PIN_P4_1__OSPI0_RXDS_A`

```c
#define PIN_P4_1__OSPI0_RXDS_A ALIF_PINMUX(4, 1, 1)
```

端口（Port）4 的引脚（Pin）1：`OSPI0_RXDS_A`。

<a id="aa8d357f6692b4eaca657b934834350a9"></a>

### `PIN_P4_1__SD_D1_A`

```c
#define PIN_P4_1__SD_D1_A ALIF_PINMUX(4, 1, 6)
```

端口（Port）4 的引脚（Pin）1：`SD_D1_A`。

<a id="ad22e1e1495cfbde6d14323b9c3e32bd0"></a>

### `PIN_P4_1__SPI2_SS2_A`

```c
#define PIN_P4_1__SPI2_SS2_A ALIF_PINMUX(4, 1, 3)
```

端口（Port）4 的引脚（Pin）1：`SPI2_SS2_A`。

<a id="a7c22e0d1553016df93e54d3d383178ff"></a>

### `PIN_P4_1__UART0_TX_B`

```c
#define PIN_P4_1__UART0_TX_B ALIF_PINMUX(4, 1, 2)
```

端口（Port）4 的引脚（Pin）1：`UART0_TX_B`。

<a id="ab8905fd2eb3785e6fee1f3bc479d9ca2"></a>

### `PIN_P4_1__UT0_T1_A`

```c
#define PIN_P4_1__UT0_T1_A ALIF_PINMUX(4, 1, 4)
```

端口（Port）4 的引脚（Pin）1：`UT0_T1_A`。

<a id="a7691073005a4ead27b8f64beb2548f2a"></a>

### `PIN_P4_2__EXT_TRACE_A`

```c
#define PIN_P4_2__EXT_TRACE_A ALIF_PINMUX(4, 2, 7)
```

端口（Port）4 的引脚（Pin）2：`EXT_TRACE_A`。

<a id="a2a9f0b7627d1f0149fa1cddc428e76f9"></a>

### `PIN_P4_2__GPIO`

```c
#define PIN_P4_2__GPIO ALIF_PINMUX(4, 2, 0)
```

引脚 `P4.2` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）2：`GPIO`。

<a id="a98c0f9bd017151740c3ccfea7284a20b"></a>

### `PIN_P4_2__HFXO_OUT_A`

```c
#define PIN_P4_2__HFXO_OUT_A ALIF_PINMUX(4, 2, 1)
```

端口（Port）4 的引脚（Pin）2：`HFXO_OUT_A`。

<a id="af81bdc4d2f7ec97fe76ec92ca24ddaac"></a>

### `PIN_P4_2__LPCAM_D2_A`

```c
#define PIN_P4_2__LPCAM_D2_A ALIF_PINMUX(4, 2, 5)
```

端口（Port）4 的引脚（Pin）2：`LPCAM_D2_A`。

<a id="a5da13c644ad45ce5ff82c01d05fe5d8b"></a>

### `PIN_P4_2__OSPI0_SCLK_A`

```c
#define PIN_P4_2__OSPI0_SCLK_A ALIF_PINMUX(4, 2, 2)
```

端口（Port）4 的引脚（Pin）2：`OSPI0_SCLK_A`。

<a id="aecf120640ee69bbbf5a1ed7cb80deb96"></a>

### `PIN_P4_2__SD_D2_A`

```c
#define PIN_P4_2__SD_D2_A ALIF_PINMUX(4, 2, 6)
```

端口（Port）4 的引脚（Pin）2：`SD_D2_A`。

<a id="ae629174d9c48b1cd4eb7c1cf7d1ffa7e"></a>

### `PIN_P4_2__UART4_DE_A`

```c
#define PIN_P4_2__UART4_DE_A ALIF_PINMUX(4, 2, 3)
```

端口（Port）4 的引脚（Pin）2：`UART4_DE_A`。

<a id="a20e581f0adef0fcfe47bc16323f24ed3"></a>

### `PIN_P4_2__UT1_T0_A`

```c
#define PIN_P4_2__UT1_T0_A ALIF_PINMUX(4, 2, 4)
```

端口（Port）4 的引脚（Pin）2：`UT1_T0_A`。

<a id="a0d58327743edb52505ead51efddd7eb4"></a>

### `PIN_P4_3__CMP0_OUT_B`

```c
#define PIN_P4_3__CMP0_OUT_B ALIF_PINMUX(4, 3, 6)
```

端口（Port）4 的引脚（Pin）3：`CMP0_OUT_B`。

<a id="ad3a967ff2a55e33d61a036a466f8e438"></a>

### `PIN_P4_3__CS_MWS_ID0`

```c
#define PIN_P4_3__CS_MWS_ID0 ALIF_PINMUX(4, 3, 2)
```

端口（Port）4 的引脚（Pin）3：`CS_MWS_ID0`。

<a id="a97b4675f5259e06d48cdd30755a46f3e"></a>

### `PIN_P4_3__GPIO`

```c
#define PIN_P4_3__GPIO ALIF_PINMUX(4, 3, 0)
```

引脚 `P4.3` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）3：`GPIO`。

<a id="a19f6e008e0abb13d14c7fe8ad6fbe6f7"></a>

### `PIN_P4_3__JTAG0_NSRST`

```c
#define PIN_P4_3__JTAG0_NSRST ALIF_PINMUX(4, 3, 1)
```

端口（Port）4 的引脚（Pin）3：`JTAG0_NSRST`。

<a id="a5aa98d3c3d4b2341b39f13be3af830a5"></a>

### `PIN_P4_3__UT1_T1_A`

```c
#define PIN_P4_3__UT1_T1_A ALIF_PINMUX(4, 3, 3)
```

端口（Port）4 的引脚（Pin）3：`UT1_T1_A`。

<a id="a8318b5bd441072af1b0d4dfeb97d55e0"></a>

### `PIN_P4_4__CS_MWS_ID1`

```c
#define PIN_P4_4__CS_MWS_ID1 ALIF_PINMUX(4, 4, 3)
```

端口（Port）4 的引脚（Pin）4：`CS_MWS_ID1`。

<a id="a8f8a4b37bca8ab9c9021626f9e15adb4"></a>

### `PIN_P4_4__FAULT0_B`

```c
#define PIN_P4_4__FAULT0_B ALIF_PINMUX(4, 4, 2)
```

端口（Port）4 的引脚（Pin）4：`FAULT0_B`。

<a id="a71f56da2cfc34a4fa6dbbba7e9936d28"></a>

### `PIN_P4_4__GPIO`

```c
#define PIN_P4_4__GPIO ALIF_PINMUX(4, 4, 0)
```

引脚 `P4.4` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）4：`GPIO`。

<a id="a026da00206cb806cf7e868c00dfa15de"></a>

### `PIN_P4_4__JTAG0_TCK`

```c
#define PIN_P4_4__JTAG0_TCK ALIF_PINMUX(4, 4, 1)
```

端口（Port）4 的引脚（Pin）4：`JTAG0_TCK`。

<a id="a25e0c2ba6146de455410dab64097aa33"></a>

### `PIN_P4_4__UT2_T0_A`

```c
#define PIN_P4_4__UT2_T0_A ALIF_PINMUX(4, 4, 4)
```

端口（Port）4 的引脚（Pin）4：`UT2_T0_A`。

<a id="a000faa2a435ba773512656c672ba6151"></a>

### `PIN_P4_5__CS_MWS_ID2`

```c
#define PIN_P4_5__CS_MWS_ID2 ALIF_PINMUX(4, 5, 3)
```

端口（Port）4 的引脚（Pin）5：`CS_MWS_ID2`。

<a id="ad1dc12f3fb93facb6b056284db1dd865"></a>

### `PIN_P4_5__FAULT1_B`

```c
#define PIN_P4_5__FAULT1_B ALIF_PINMUX(4, 5, 2)
```

端口（Port）4 的引脚（Pin）5：`FAULT1_B`。

<a id="a44781940091d6eadb753aa098a1c8a3a"></a>

### `PIN_P4_5__GPIO`

```c
#define PIN_P4_5__GPIO ALIF_PINMUX(4, 5, 0)
```

引脚 `P4.5` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）5：`GPIO`。

<a id="ac8c66019ed9ef1f3e1761b9676666d7c"></a>

### `PIN_P4_5__JTAG0_TMS`

```c
#define PIN_P4_5__JTAG0_TMS ALIF_PINMUX(4, 5, 1)
```

端口（Port）4 的引脚（Pin）5：`JTAG0_TMS`。

<a id="a6a406851e165d3138915a0e9af6ac44f"></a>

### `PIN_P4_5__UT2_T1_A`

```c
#define PIN_P4_5__UT2_T1_A ALIF_PINMUX(4, 5, 4)
```

端口（Port）4 的引脚（Pin）5：`UT2_T1_A`。

<a id="ae86da62dbb31a6c4b1a4d0b23fcbaaab"></a>

### `PIN_P4_6__FAULT2_B`

```c
#define PIN_P4_6__FAULT2_B ALIF_PINMUX(4, 6, 2)
```

端口（Port）4 的引脚（Pin）6：`FAULT2_B`。

<a id="aae4c2f3f2743c6281127d761c2d3c952"></a>

### `PIN_P4_6__GPIO`

```c
#define PIN_P4_6__GPIO ALIF_PINMUX(4, 6, 0)
```

引脚 `P4.6` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）6：`GPIO`。

<a id="a64e905aad463ddb010ef5e31aa4bb355"></a>

### `PIN_P4_6__JTAG0_TDI`

```c
#define PIN_P4_6__JTAG0_TDI ALIF_PINMUX(4, 6, 1)
```

端口（Port）4 的引脚（Pin）6：`JTAG0_TDI`。

<a id="aeac835d737d34448f0a28bc7101a087b"></a>

### `PIN_P4_6__LPI2S_WS_B`

```c
#define PIN_P4_6__LPI2S_WS_B ALIF_PINMUX(4, 6, 3)
```

端口（Port）4 的引脚（Pin）6：`LPI2S_WS_B`。

<a id="ad9aa455c48e18f8651b6c46265912bfa"></a>

### `PIN_P4_6__UT3_T0_A`

```c
#define PIN_P4_6__UT3_T0_A ALIF_PINMUX(4, 6, 4)
```

端口（Port）4 的引脚（Pin）6：`UT3_T0_A`。

<a id="a921f7c932359c5bc8f188c7ab9ce53d3"></a>

### `PIN_P4_7__CMP1_OUT_B`

```c
#define PIN_P4_7__CMP1_OUT_B ALIF_PINMUX(4, 7, 6)
```

端口（Port）4 的引脚（Pin）7：`CMP1_OUT_B`。

<a id="ae195873e36cdb06497fa9c821e422350"></a>

### `PIN_P4_7__CS_MWS_ID4`

```c
#define PIN_P4_7__CS_MWS_ID4 ALIF_PINMUX(4, 7, 4)
```

端口（Port）4 的引脚（Pin）7：`CS_MWS_ID4`。

<a id="a4781e1c7651d920f43fb0b2472372436"></a>

### `PIN_P4_7__FAULT3_B`

```c
#define PIN_P4_7__FAULT3_B ALIF_PINMUX(4, 7, 2)
```

端口（Port）4 的引脚（Pin）7：`FAULT3_B`。

<a id="a414ee602068915040eb8dab92a92bb61"></a>

### `PIN_P4_7__GPIO`

```c
#define PIN_P4_7__GPIO ALIF_PINMUX(4, 7, 0)
```

引脚 `P4.7` 的复用功能（Alternate Functions）。

端口（Port）4 的引脚（Pin）7：`GPIO`。

<a id="a1882c539a53276d676235207bd87494a"></a>

### `PIN_P4_7__JTAG0_TDO`

```c
#define PIN_P4_7__JTAG0_TDO ALIF_PINMUX(4, 7, 1)
```

端口（Port）4 的引脚（Pin）7：`JTAG0_TDO`。

<a id="a85dc41a85f81bf5aa6b21adea41f6cc7"></a>

### `PIN_P4_7__UT3_T1_A`

```c
#define PIN_P4_7__UT3_T1_A ALIF_PINMUX(4, 7, 3)
```

端口（Port）4 的引脚（Pin）7：`UT3_T1_A`。

<a id="a09144d6ba2498f87a362d6ed24d3b806"></a>

### `PIN_P5_0__CAN0_RXD_B`

```c
#define PIN_P5_0__CAN0_RXD_B ALIF_PINMUX(5, 0, 5)
```

端口（Port）5 的引脚（Pin）0：`CAN0_RXD_B`。

<a id="a19da3e4d236b8aead55eced77dbede8a"></a>

### `PIN_P5_0__CDC_D0_A`

```c
#define PIN_P5_0__CDC_D0_A ALIF_PINMUX(5, 0, 4)
```

端口（Port）5 的引脚（Pin）0：`CDC_D0_A`。

<a id="a33aeb846f89757467e96fc37655d4560"></a>

### `PIN_P5_0__DEBUG_PORT0`

```c
#define PIN_P5_0__DEBUG_PORT0 ALIF_PINMUX(5, 0, 6)
```

端口（Port）5 的引脚（Pin）0：`DEBUG_PORT0`。

<a id="a456e61913b22b9d8a56be8b0377ac81e"></a>

### `PIN_P5_0__GPIO`

```c
#define PIN_P5_0__GPIO ALIF_PINMUX(5, 0, 0)
```

引脚 `P5.0` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）0：`GPIO`。

<a id="a7515446e7f6b91cb8e9ad6059684ed5e"></a>

### `PIN_P5_0__OSPI0_D0_B`

```c
#define PIN_P5_0__OSPI0_D0_B ALIF_PINMUX(5, 0, 1)
```

端口（Port）5 的引脚（Pin）0：`OSPI0_D0_B`。

<a id="a8d7a46642529764190d788a4e6fd45ad"></a>

### `PIN_P5_0__SPI0_MISO_B`

```c
#define PIN_P5_0__SPI0_MISO_B ALIF_PINMUX(5, 0, 3)
```

端口（Port）5 的引脚（Pin）0：`SPI0_MISO_B`。

<a id="a70e357d53457779d10d0b21e4b58a306"></a>

### `PIN_P5_0__UART1_RX_B`

```c
#define PIN_P5_0__UART1_RX_B ALIF_PINMUX(5, 0, 2)
```

端口（Port）5 的引脚（Pin）0：`UART1_RX_B`。

<a id="a75e6ca2a4fbdf460b505179d29c4c340"></a>

### `PIN_P5_1__CAN0_TXD_B`

```c
#define PIN_P5_1__CAN0_TXD_B ALIF_PINMUX(5, 1, 5)
```

端口（Port）5 的引脚（Pin）1：`CAN0_TXD_B`。

<a id="af760abc039a42c556a870cd724bc8cfd"></a>

### `PIN_P5_1__CDC_D1_A`

```c
#define PIN_P5_1__CDC_D1_A ALIF_PINMUX(5, 1, 4)
```

端口（Port）5 的引脚（Pin）1：`CDC_D1_A`。

<a id="a9300ca0c13f79f5fbe0cee6a407bb6a1"></a>

### `PIN_P5_1__DEBUG_PORT1`

```c
#define PIN_P5_1__DEBUG_PORT1 ALIF_PINMUX(5, 1, 6)
```

端口（Port）5 的引脚（Pin）1：`DEBUG_PORT1`。

<a id="a98fa74bbdae6f1f210c490cdc73d7cb8"></a>

### `PIN_P5_1__GPIO`

```c
#define PIN_P5_1__GPIO ALIF_PINMUX(5, 1, 0)
```

引脚 `P5.1` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）1：`GPIO`。

<a id="abd2a49b69427e6dd3d36041739e26e64"></a>

### `PIN_P5_1__OSPI0_D1_B`

```c
#define PIN_P5_1__OSPI0_D1_B ALIF_PINMUX(5, 1, 1)
```

端口（Port）5 的引脚（Pin）1：`OSPI0_D1_B`。

<a id="a02c0d84f1ce09a7db4f16344ce7d6e0f"></a>

### `PIN_P5_1__SPI0_MOSI_B`

```c
#define PIN_P5_1__SPI0_MOSI_B ALIF_PINMUX(5, 1, 3)
```

端口（Port）5 的引脚（Pin）1：`SPI0_MOSI_B`。

<a id="accef3fca5f47ce8a465ff8c16f485963"></a>

### `PIN_P5_1__UART1_TX_B`

```c
#define PIN_P5_1__UART1_TX_B ALIF_PINMUX(5, 1, 2)
```

端口（Port）5 的引脚（Pin）1：`UART1_TX_B`。

<a id="aa54f58186118a8cc7b816e3c8e08670d"></a>

### `PIN_P5_2__CDC_D2_A`

```c
#define PIN_P5_2__CDC_D2_A ALIF_PINMUX(5, 2, 5)
```

端口（Port）5 的引脚（Pin）2：`CDC_D2_A`。

<a id="aeb0c6ac8de20eb3b7da621944e98970b"></a>

### `PIN_P5_2__DEBUG_PORT2`

```c
#define PIN_P5_2__DEBUG_PORT2 ALIF_PINMUX(5, 2, 6)
```

端口（Port）5 的引脚（Pin）2：`DEBUG_PORT2`。

<a id="a97a74c55bf53c437a39b3f10cfa778bc"></a>

### `PIN_P5_2__GPIO`

```c
#define PIN_P5_2__GPIO ALIF_PINMUX(5, 2, 0)
```

引脚 `P5.2` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）2：`GPIO`。

<a id="a9412174bfeabbc0ef5bac744684200e6"></a>

### `PIN_P5_2__HFXO_OUT_B`

```c
#define PIN_P5_2__HFXO_OUT_B ALIF_PINMUX(5, 2, 1)
```

端口（Port）5 的引脚（Pin）2：`HFXO_OUT_B`。

<a id="a9d38ab0662de65a0c523e9def2eea72c"></a>

### `PIN_P5_2__OSPI0_D2_B`

```c
#define PIN_P5_2__OSPI0_D2_B ALIF_PINMUX(5, 2, 2)
```

端口（Port）5 的引脚（Pin）2：`OSPI0_D2_B`。

<a id="aa4e51a07e335aceeb1d4c7a0ba483945"></a>

### `PIN_P5_2__SPI0_SCLK_B`

```c
#define PIN_P5_2__SPI0_SCLK_B ALIF_PINMUX(5, 2, 4)
```

端口（Port）5 的引脚（Pin）2：`SPI0_SCLK_B`。

<a id="aef66774050c916f8a431df007e4a4721"></a>

### `PIN_P5_2__UART2_RX_B`

```c
#define PIN_P5_2__UART2_RX_B ALIF_PINMUX(5, 2, 3)
```

端口（Port）5 的引脚（Pin）2：`UART2_RX_B`。

<a id="a9e39c3bab0ba922acc2ccfa570e8f768"></a>

### `PIN_P5_3__CDC_D3_A`

```c
#define PIN_P5_3__CDC_D3_A ALIF_PINMUX(5, 3, 4)
```

端口（Port）5 的引脚（Pin）3：`CDC_D3_A`。

<a id="afcc5c2f160ddea37e8d27066e1f56f0b"></a>

### `PIN_P5_3__DEBUG_PORT3`

```c
#define PIN_P5_3__DEBUG_PORT3 ALIF_PINMUX(5, 3, 5)
```

端口（Port）5 的引脚（Pin）3：`DEBUG_PORT3`。

<a id="af2c171dfdada8390ed0c80e115f024eb"></a>

### `PIN_P5_3__GPIO`

```c
#define PIN_P5_3__GPIO ALIF_PINMUX(5, 3, 0)
```

引脚 `P5.3` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）3：`GPIO`。

<a id="a26d1e825401e3265e1f84b6fe668bb4b"></a>

### `PIN_P5_3__OSPI0_D3_B`

```c
#define PIN_P5_3__OSPI0_D3_B ALIF_PINMUX(5, 3, 1)
```

端口（Port）5 的引脚（Pin）3：`OSPI0_D3_B`。

<a id="a9bef667960418991b8dcd10c622659bc"></a>

### `PIN_P5_3__SPI0_SS0_B`

```c
#define PIN_P5_3__SPI0_SS0_B ALIF_PINMUX(5, 3, 3)
```

端口（Port）5 的引脚（Pin）3：`SPI0_SS0_B`。

<a id="ac655344000cbc93d5d59943a9a357f35"></a>

### `PIN_P5_3__UART2_TX_B`

```c
#define PIN_P5_3__UART2_TX_B ALIF_PINMUX(5, 3, 2)
```

端口（Port）5 的引脚（Pin）3：`UART2_TX_B`。

<a id="a3492ede5bc47cdcbc93ffa2c618d9de5"></a>

### `PIN_P5_4__CDC_D4_A`

```c
#define PIN_P5_4__CDC_D4_A ALIF_PINMUX(5, 4, 5)
```

端口（Port）5 的引脚（Pin）4：`CDC_D4_A`。

<a id="ab51b446a130c3e4d5ad5bcd224435ec8"></a>

### `PIN_P5_4__DEBUG_PORT4`

```c
#define PIN_P5_4__DEBUG_PORT4 ALIF_PINMUX(5, 4, 6)
```

端口（Port）5 的引脚（Pin）4：`DEBUG_PORT4`。

<a id="a6846e3f2b170cb7a3216f81e5ec3b30e"></a>

### `PIN_P5_4__GPIO`

```c
#define PIN_P5_4__GPIO ALIF_PINMUX(5, 4, 0)
```

引脚 `P5.4` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）4：`GPIO`。

<a id="aba535b3b3becd72a6155033116e157cf"></a>

### `PIN_P5_4__LPPDM_C0_C`

```c
#define PIN_P5_4__LPPDM_C0_C ALIF_PINMUX(5, 4, 3)
```

端口（Port）5 的引脚（Pin）4：`LPPDM_C0_C`。

<a id="acfae802a9c0d84dd7fe2fa7ae137da32"></a>

### `PIN_P5_4__OSPI0_D4_B`

```c
#define PIN_P5_4__OSPI0_D4_B ALIF_PINMUX(5, 4, 1)
```

端口（Port）5 的引脚（Pin）4：`OSPI0_D4_B`。

<a id="ad8ff5c1bc4ae11a8417d37c08725ca1e"></a>

### `PIN_P5_4__SPI0_SS1_B`

```c
#define PIN_P5_4__SPI0_SS1_B ALIF_PINMUX(5, 4, 4)
```

端口（Port）5 的引脚（Pin）4：`SPI0_SS1_B`。

<a id="ae8575f29fe033284403815de52e2b0b1"></a>

### `PIN_P5_4__UART3_CTS_A`

```c
#define PIN_P5_4__UART3_CTS_A ALIF_PINMUX(5, 4, 2)
```

端口（Port）5 的引脚（Pin）4：`UART3_CTS_A`。

<a id="ab8b92f2241fd09c81a4e881e4c12e0a3"></a>

### `PIN_P5_5__CDC_D5_A`

```c
#define PIN_P5_5__CDC_D5_A ALIF_PINMUX(5, 5, 5)
```

端口（Port）5 的引脚（Pin）5：`CDC_D5_A`。

<a id="aa6991f74e9a8bc6f4559e5463862e142"></a>

### `PIN_P5_5__DEBUG_PORT5`

```c
#define PIN_P5_5__DEBUG_PORT5 ALIF_PINMUX(5, 5, 6)
```

端口（Port）5 的引脚（Pin）5：`DEBUG_PORT5`。

<a id="a466c951ce8310bac71e4a36b062e3b48"></a>

### `PIN_P5_5__GPIO`

```c
#define PIN_P5_5__GPIO ALIF_PINMUX(5, 5, 0)
```

引脚 `P5.5` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）5：`GPIO`。

<a id="affea3cc1741e8f1d8b481d382231e8b2"></a>

### `PIN_P5_5__LPPDM_C1_C`

```c
#define PIN_P5_5__LPPDM_C1_C ALIF_PINMUX(5, 5, 3)
```

端口（Port）5 的引脚（Pin）5：`LPPDM_C1_C`。

<a id="aee3d8c711f4960174ef78aaa66f546a4"></a>

### `PIN_P5_5__OSPI0_D5_B`

```c
#define PIN_P5_5__OSPI0_D5_B ALIF_PINMUX(5, 5, 1)
```

端口（Port）5 的引脚（Pin）5：`OSPI0_D5_B`。

<a id="ac6c32c362dd4a8136e7afba82bd2ed26"></a>

### `PIN_P5_5__SPI0_SS2_B`

```c
#define PIN_P5_5__SPI0_SS2_B ALIF_PINMUX(5, 5, 4)
```

端口（Port）5 的引脚（Pin）5：`SPI0_SS2_B`。

<a id="aefd41d2a46a675a37216980f16e2fd58"></a>

### `PIN_P5_5__UART3_RTS_A`

```c
#define PIN_P5_5__UART3_RTS_A ALIF_PINMUX(5, 5, 2)
```

端口（Port）5 的引脚（Pin）5：`UART3_RTS_A`。

<a id="a75155e55cff32f1b264994b3f795d7cd"></a>

### `PIN_P5_6__CDC_D6_A`

```c
#define PIN_P5_6__CDC_D6_A ALIF_PINMUX(5, 6, 5)
```

端口（Port）5 的引脚（Pin）6：`CDC_D6_A`。

<a id="a6a08b389c3a815867e60c3120b0ea33c"></a>

### `PIN_P5_6__DEBUG_PORT6`

```c
#define PIN_P5_6__DEBUG_PORT6 ALIF_PINMUX(5, 6, 6)
```

端口（Port）5 的引脚（Pin）6：`DEBUG_PORT6`。

<a id="acd3416c5b74cd24d02c29e3144d63436"></a>

### `PIN_P5_6__GPIO`

```c
#define PIN_P5_6__GPIO ALIF_PINMUX(5, 6, 0)
```

引脚 `P5.6` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）6：`GPIO`。

<a id="abdd1f1a77582773e32e38f4f3d7b7f9f"></a>

### `PIN_P5_6__LPPDM_D0_C`

```c
#define PIN_P5_6__LPPDM_D0_C ALIF_PINMUX(5, 6, 3)
```

端口（Port）5 的引脚（Pin）6：`LPPDM_D0_C`。

<a id="a1fef293fbc151e83a6059a043296696a"></a>

### `PIN_P5_6__LPSPI_MISO_B`

```c
#define PIN_P5_6__LPSPI_MISO_B ALIF_PINMUX(5, 6, 4)
```

端口（Port）5 的引脚（Pin）6：`LPSPI_MISO_B`。

<a id="a992d43f89e37b80a8da4608e67529c1b"></a>

### `PIN_P5_6__OSPI0_D6_B`

```c
#define PIN_P5_6__OSPI0_D6_B ALIF_PINMUX(5, 6, 1)
```

端口（Port）5 的引脚（Pin）6：`OSPI0_D6_B`。

<a id="a3bd03266c3d91de23071a3d0241e97e3"></a>

### `PIN_P5_6__UART1_CTS_B`

```c
#define PIN_P5_6__UART1_CTS_B ALIF_PINMUX(5, 6, 2)
```

端口（Port）5 的引脚（Pin）6：`UART1_CTS_B`。

<a id="a9a269398cead600a0730cf59ee346efe"></a>

### `PIN_P5_7__CDC_D7_A`

```c
#define PIN_P5_7__CDC_D7_A ALIF_PINMUX(5, 7, 5)
```

端口（Port）5 的引脚（Pin）7：`CDC_D7_A`。

<a id="a7a7892f2e7caa1291c8a75505f2cd4ef"></a>

### `PIN_P5_7__DEBUG_PORT7`

```c
#define PIN_P5_7__DEBUG_PORT7 ALIF_PINMUX(5, 7, 6)
```

端口（Port）5 的引脚（Pin）7：`DEBUG_PORT7`。

<a id="abc168fa2810d9a33b66d8899581c97ed"></a>

### `PIN_P5_7__GPIO`

```c
#define PIN_P5_7__GPIO ALIF_PINMUX(5, 7, 0)
```

引脚 `P5.7` 的复用功能（Alternate Functions）。

端口（Port）5 的引脚（Pin）7：`GPIO`。

<a id="ac1a9c0edd0801e204c2c73e804bc2b88"></a>

### `PIN_P5_7__LPPDM_D1_C`

```c
#define PIN_P5_7__LPPDM_D1_C ALIF_PINMUX(5, 7, 3)
```

端口（Port）5 的引脚（Pin）7：`LPPDM_D1_C`。

<a id="a101d18b757575a6b4d774eb367e47f1d"></a>

### `PIN_P5_7__LPSPI_MOSI_B`

```c
#define PIN_P5_7__LPSPI_MOSI_B ALIF_PINMUX(5, 7, 4)
```

端口（Port）5 的引脚（Pin）7：`LPSPI_MOSI_B`。

<a id="af2d4965c3a398c12ae01ddce15a3f1e6"></a>

### `PIN_P5_7__OSPI0_D7_B`

```c
#define PIN_P5_7__OSPI0_D7_B ALIF_PINMUX(5, 7, 1)
```

端口（Port）5 的引脚（Pin）7：`OSPI0_D7_B`。

<a id="a16337846b4c79f3bf2b8601bd2b97f91"></a>

### `PIN_P5_7__UART1_RTS_B`

```c
#define PIN_P5_7__UART1_RTS_B ALIF_PINMUX(5, 7, 2)
```

端口（Port）5 的引脚（Pin）7：`UART1_RTS_B`。

<a id="a34729c1d8880ed50f395c50a2fe51e28"></a>

### `PIN_P6_0__CDC_D8_A`

```c
#define PIN_P6_0__CDC_D8_A ALIF_PINMUX(6, 0, 6)
```

端口（Port）6 的引脚（Pin）0：`CDC_D8_A`。

<a id="ae7ade9dfd32e609fb86f13f6525953fc"></a>

### `PIN_P6_0__GPIO`

```c
#define PIN_P6_0__GPIO ALIF_PINMUX(6, 0, 0)
```

引脚 `P6.0` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）0：`GPIO`。

<a id="a5bb14125f4edce700f4ec3003446446c"></a>

### `PIN_P6_0__LPSPI_SS_B`

```c
#define PIN_P6_0__LPSPI_SS_B ALIF_PINMUX(6, 0, 3)
```

端口（Port）6 的引脚（Pin）0：`LPSPI_SS_B`。

<a id="af006833ac80c14da05e6a4599a24ac61"></a>

### `PIN_P6_0__OSPI0_D0_C`

```c
#define PIN_P6_0__OSPI0_D0_C ALIF_PINMUX(6, 0, 1)
```

端口（Port）6 的引脚（Pin）0：`OSPI0_D0_C`。

<a id="a8cdbf1027a1529384f1a861b04036391"></a>

### `PIN_P6_0__SD_D0_B`

```c
#define PIN_P6_0__SD_D0_B ALIF_PINMUX(6, 0, 5)
```

端口（Port）6 的引脚（Pin）0：`SD_D0_B`。

<a id="a79570f9e4a4d6cf2551a9610c48ef2b9"></a>

### `PIN_P6_0__UART4_DE_B`

```c
#define PIN_P6_0__UART4_DE_B ALIF_PINMUX(6, 0, 2)
```

端口（Port）6 的引脚（Pin）0：`UART4_DE_B`。

<a id="a7278e3b97a506751e694bedd1ed07f72"></a>

### `PIN_P6_0__UT0_T0_B`

```c
#define PIN_P6_0__UT0_T0_B ALIF_PINMUX(6, 0, 4)
```

端口（Port）6 的引脚（Pin）0：`UT0_T0_B`。

<a id="a6efed7a051659015ba52b794a8307682"></a>

### `PIN_P6_1__CDC_D9_A`

```c
#define PIN_P6_1__CDC_D9_A ALIF_PINMUX(6, 1, 6)
```

端口（Port）6 的引脚（Pin）1：`CDC_D9_A`。

<a id="ad55f5467ffabdbffd5b51ddfeaed9c4f"></a>

### `PIN_P6_1__GPIO`

```c
#define PIN_P6_1__GPIO ALIF_PINMUX(6, 1, 0)
```

引脚 `P6.1` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）1：`GPIO`。

<a id="aa0c327b4b44ee5068c84f65827555817"></a>

### `PIN_P6_1__OSPI0_D1_C`

```c
#define PIN_P6_1__OSPI0_D1_C ALIF_PINMUX(6, 1, 1)
```

端口（Port）6 的引脚（Pin）1：`OSPI0_D1_C`。

<a id="a9830bcd6296f620190099a1d42afeb94"></a>

### `PIN_P6_1__SD_D1_B`

```c
#define PIN_P6_1__SD_D1_B ALIF_PINMUX(6, 1, 5)
```

端口（Port）6 的引脚（Pin）1：`SD_D1_B`。

<a id="acc7a686a7268479f6f114f354a022bf5"></a>

### `PIN_P6_1__SPI1_MISO_B`

```c
#define PIN_P6_1__SPI1_MISO_B ALIF_PINMUX(6, 1, 3)
```

端口（Port）6 的引脚（Pin）1：`SPI1_MISO_B`。

<a id="aeb4ee42999e56e3a6c98cf66e476be59"></a>

### `PIN_P6_1__UART5_DE_A`

```c
#define PIN_P6_1__UART5_DE_A ALIF_PINMUX(6, 1, 2)
```

端口（Port）6 的引脚（Pin）1：`UART5_DE_A`。

<a id="ace62f048486756791fdfdc9dd67b1057"></a>

### `PIN_P6_1__UT0_T1_B`

```c
#define PIN_P6_1__UT0_T1_B ALIF_PINMUX(6, 1, 4)
```

端口（Port）6 的引脚（Pin）1：`UT0_T1_B`。

<a id="ad0983e6b2d0c0cf85a14897416d037f0"></a>

### `PIN_P6_2__CDC_D10_A`

```c
#define PIN_P6_2__CDC_D10_A ALIF_PINMUX(6, 2, 6)
```

端口（Port）6 的引脚（Pin）2：`CDC_D10_A`。

<a id="adae4d80fc2a0fb040a8eed5c89e72cdd"></a>

### `PIN_P6_2__GPIO`

```c
#define PIN_P6_2__GPIO ALIF_PINMUX(6, 2, 0)
```

引脚 `P6.2` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）2：`GPIO`。

<a id="a1a29ae10d58edee6e97fd88d3057f1d6"></a>

### `PIN_P6_2__OSPI0_D2_C`

```c
#define PIN_P6_2__OSPI0_D2_C ALIF_PINMUX(6, 2, 1)
```

端口（Port）6 的引脚（Pin）2：`OSPI0_D2_C`。

<a id="accdb6fb802aa3b5cf02c6a71e85289a9"></a>

### `PIN_P6_2__SD_D2_B`

```c
#define PIN_P6_2__SD_D2_B ALIF_PINMUX(6, 2, 5)
```

端口（Port）6 的引脚（Pin）2：`SD_D2_B`。

<a id="a011a62ceebd9b9ce35e4123833649fb0"></a>

### `PIN_P6_2__SPI1_MOSI_B`

```c
#define PIN_P6_2__SPI1_MOSI_B ALIF_PINMUX(6, 2, 3)
```

端口（Port）6 的引脚（Pin）2：`SPI1_MOSI_B`。

<a id="a9bae739436d46b7844632df7afa34d94"></a>

### `PIN_P6_2__UART2_CTS_A`

```c
#define PIN_P6_2__UART2_CTS_A ALIF_PINMUX(6, 2, 2)
```

端口（Port）6 的引脚（Pin）2：`UART2_CTS_A`。

<a id="a99d44c64afab8fdd36300b15cd2994ab"></a>

### `PIN_P6_2__UT1_T0_B`

```c
#define PIN_P6_2__UT1_T0_B ALIF_PINMUX(6, 2, 4)
```

端口（Port）6 的引脚（Pin）2：`UT1_T0_B`。

<a id="af667c27ea23d08184baaa71fda64b915"></a>

### `PIN_P6_3__CDC_D11_A`

```c
#define PIN_P6_3__CDC_D11_A ALIF_PINMUX(6, 3, 6)
```

端口（Port）6 的引脚（Pin）3：`CDC_D11_A`。

<a id="a9c055a8795fbd5a4145bf758a72d1d23"></a>

### `PIN_P6_3__GPIO`

```c
#define PIN_P6_3__GPIO ALIF_PINMUX(6, 3, 0)
```

引脚 `P6.3` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）3：`GPIO`。

<a id="ab9ef591fd0935f7082f8a08d31f3393f"></a>

### `PIN_P6_3__OSPI0_D3_C`

```c
#define PIN_P6_3__OSPI0_D3_C ALIF_PINMUX(6, 3, 1)
```

端口（Port）6 的引脚（Pin）3：`OSPI0_D3_C`。

<a id="a0a0be736abe9bfd71290393a24faca36"></a>

### `PIN_P6_3__SD_D3_B`

```c
#define PIN_P6_3__SD_D3_B ALIF_PINMUX(6, 3, 5)
```

端口（Port）6 的引脚（Pin）3：`SD_D3_B`。

<a id="ade2d09480c128ca2346db206a5c31dc2"></a>

### `PIN_P6_3__SPI1_SCLK_B`

```c
#define PIN_P6_3__SPI1_SCLK_B ALIF_PINMUX(6, 3, 3)
```

端口（Port）6 的引脚（Pin）3：`SPI1_SCLK_B`。

<a id="a6407df773a1b7922599c36f9d5ba134f"></a>

### `PIN_P6_3__UART2_RTS_A`

```c
#define PIN_P6_3__UART2_RTS_A ALIF_PINMUX(6, 3, 2)
```

端口（Port）6 的引脚（Pin）3：`UART2_RTS_A`。

<a id="a81929813f463bf3e98dcec0012cadd6c"></a>

### `PIN_P6_3__UT1_T1_B`

```c
#define PIN_P6_3__UT1_T1_B ALIF_PINMUX(6, 3, 4)
```

端口（Port）6 的引脚（Pin）3：`UT1_T1_B`。

<a id="a19f9eb6a8bf2182bf472932289fcd81a"></a>

### `PIN_P6_4__CDC_D12_A`

```c
#define PIN_P6_4__CDC_D12_A ALIF_PINMUX(6, 4, 6)
```

端口（Port）6 的引脚（Pin）4：`CDC_D12_A`。

<a id="a80712cd6a9a977af7a2f879634daf24d"></a>

### `PIN_P6_4__GPIO`

```c
#define PIN_P6_4__GPIO ALIF_PINMUX(6, 4, 0)
```

引脚 `P6.4` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）4：`GPIO`。

<a id="a587f62993920d1f067ce5b5119b05aab"></a>

### `PIN_P6_4__OSPI0_D4_C`

```c
#define PIN_P6_4__OSPI0_D4_C ALIF_PINMUX(6, 4, 1)
```

端口（Port）6 的引脚（Pin）4：`OSPI0_D4_C`。

<a id="a2cf67978227d7711caa02bd1e6106be6"></a>

### `PIN_P6_4__SD_D4_B`

```c
#define PIN_P6_4__SD_D4_B ALIF_PINMUX(6, 4, 5)
```

端口（Port）6 的引脚（Pin）4：`SD_D4_B`。

<a id="a4097acd4e3c33280170dbea58ab20604"></a>

### `PIN_P6_4__SPI1_SS0_B`

```c
#define PIN_P6_4__SPI1_SS0_B ALIF_PINMUX(6, 4, 3)
```

端口（Port）6 的引脚（Pin）4：`SPI1_SS0_B`。

<a id="a3ce358cbdd477ef4755e0a59e5d62b22"></a>

### `PIN_P6_4__UART2_CTS_B`

```c
#define PIN_P6_4__UART2_CTS_B ALIF_PINMUX(6, 4, 2)
```

端口（Port）6 的引脚（Pin）4：`UART2_CTS_B`。

<a id="a74d24395ae08b32dacd5c3160dd492c1"></a>

### `PIN_P6_4__UT2_T0_B`

```c
#define PIN_P6_4__UT2_T0_B ALIF_PINMUX(6, 4, 4)
```

端口（Port）6 的引脚（Pin）4：`UT2_T0_B`。

<a id="a5009293a09cb76741e2ee7d496de4a01"></a>

### `PIN_P6_5__CDC_D13_A`

```c
#define PIN_P6_5__CDC_D13_A ALIF_PINMUX(6, 5, 6)
```

端口（Port）6 的引脚（Pin）5：`CDC_D13_A`。

<a id="a4f8cb1991ad80690327a9272f790c7fa"></a>

### `PIN_P6_5__GPIO`

```c
#define PIN_P6_5__GPIO ALIF_PINMUX(6, 5, 0)
```

引脚 `P6.5` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）5：`GPIO`。

<a id="ae178273fd0d60e578038153dfa3d44d2"></a>

### `PIN_P6_5__OSPI0_D5_C`

```c
#define PIN_P6_5__OSPI0_D5_C ALIF_PINMUX(6, 5, 1)
```

端口（Port）6 的引脚（Pin）5：`OSPI0_D5_C`。

<a id="a351d27e39ee616cec1ea000692dbaa00"></a>

### `PIN_P6_5__SD_D5_B`

```c
#define PIN_P6_5__SD_D5_B ALIF_PINMUX(6, 5, 5)
```

端口（Port）6 的引脚（Pin）5：`SD_D5_B`。

<a id="af896508d8b1829141300d9c174c6a4dc"></a>

### `PIN_P6_5__SPI1_SS1_B`

```c
#define PIN_P6_5__SPI1_SS1_B ALIF_PINMUX(6, 5, 3)
```

端口（Port）6 的引脚（Pin）5：`SPI1_SS1_B`。

<a id="ac1b09ec40a2a0d186be393ce2a22bb6e"></a>

### `PIN_P6_5__UART2_RTS_B`

```c
#define PIN_P6_5__UART2_RTS_B ALIF_PINMUX(6, 5, 2)
```

端口（Port）6 的引脚（Pin）5：`UART2_RTS_B`。

<a id="a38159c76a1cb17b4dbd18d339585dfcc"></a>

### `PIN_P6_5__UT2_T1_B`

```c
#define PIN_P6_5__UT2_T1_B ALIF_PINMUX(6, 5, 4)
```

端口（Port）6 的引脚（Pin）5：`UT2_T1_B`。

<a id="aac2a8a26747c7d6bbd4a7c74602f3867"></a>

### `PIN_P6_6__CDC_D14_A`

```c
#define PIN_P6_6__CDC_D14_A ALIF_PINMUX(6, 6, 6)
```

端口（Port）6 的引脚（Pin）6：`CDC_D14_A`。

<a id="ae379d12c8cb8b76c585b3745eef14bfc"></a>

### `PIN_P6_6__GPIO`

```c
#define PIN_P6_6__GPIO ALIF_PINMUX(6, 6, 0)
```

引脚 `P6.6` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）6：`GPIO`。

<a id="a8adab274d4857b76f38a42a19c7af021"></a>

### `PIN_P6_6__OSPI0_D6_C`

```c
#define PIN_P6_6__OSPI0_D6_C ALIF_PINMUX(6, 6, 1)
```

端口（Port）6 的引脚（Pin）6：`OSPI0_D6_C`。

<a id="a6f6b543054d09e34217fd25d761fa1d5"></a>

### `PIN_P6_6__SD_D6_B`

```c
#define PIN_P6_6__SD_D6_B ALIF_PINMUX(6, 6, 5)
```

端口（Port）6 的引脚（Pin）6：`SD_D6_B`。

<a id="a88f58696cc0671871bbf7e67d96411ba"></a>

### `PIN_P6_6__SPI1_SS2_B`

```c
#define PIN_P6_6__SPI1_SS2_B ALIF_PINMUX(6, 6, 3)
```

端口（Port）6 的引脚（Pin）6：`SPI1_SS2_B`。

<a id="a149c5ebf20984a0032f56170946e1b76"></a>

### `PIN_P6_6__UART0_CTS_B`

```c
#define PIN_P6_6__UART0_CTS_B ALIF_PINMUX(6, 6, 2)
```

端口（Port）6 的引脚（Pin）6：`UART0_CTS_B`。

<a id="aa9ff5aa10ea39c234104f716b17487d8"></a>

### `PIN_P6_6__UT3_T0_B`

```c
#define PIN_P6_6__UT3_T0_B ALIF_PINMUX(6, 6, 4)
```

端口（Port）6 的引脚（Pin）6：`UT3_T0_B`。

<a id="a77ba808a6080decf1043e8e2a469ba19"></a>

### `PIN_P6_7__CDC_D15_A`

```c
#define PIN_P6_7__CDC_D15_A ALIF_PINMUX(6, 7, 6)
```

端口（Port）6 的引脚（Pin）7：`CDC_D15_A`。

<a id="a1e66098ffe67eddd23463192fcd1fbcd"></a>

### `PIN_P6_7__GPIO`

```c
#define PIN_P6_7__GPIO ALIF_PINMUX(6, 7, 0)
```

引脚 `P6.7` 的复用功能（Alternate Functions）。

端口（Port）6 的引脚（Pin）7：`GPIO`。

<a id="aef69daa6cb1613f9c4e417eaa709d9df"></a>

### `PIN_P6_7__OSPI0_D7_C`

```c
#define PIN_P6_7__OSPI0_D7_C ALIF_PINMUX(6, 7, 1)
```

端口（Port）6 的引脚（Pin）7：`OSPI0_D7_C`。

<a id="a81371fe588865cec958fa73ef38bcc8b"></a>

### `PIN_P6_7__SD_D7_B`

```c
#define PIN_P6_7__SD_D7_B ALIF_PINMUX(6, 7, 5)
```

端口（Port）6 的引脚（Pin）7：`SD_D7_B`。

<a id="a225e78df9676b56259829bd042385839"></a>

### `PIN_P6_7__SPI2_SS2_C`

```c
#define PIN_P6_7__SPI2_SS2_C ALIF_PINMUX(6, 7, 3)
```

端口（Port）6 的引脚（Pin）7：`SPI2_SS2_C`。

<a id="ae4dd7c19afbead2d7459b0e317238ae4"></a>

### `PIN_P6_7__UART0_RTS_B`

```c
#define PIN_P6_7__UART0_RTS_B ALIF_PINMUX(6, 7, 2)
```

端口（Port）6 的引脚（Pin）7：`UART0_RTS_B`。

<a id="a5b82e1c93054b79ad2496d3929c81682"></a>

### `PIN_P6_7__UT3_T1_B`

```c
#define PIN_P6_7__UT3_T1_B ALIF_PINMUX(6, 7, 4)
```

端口（Port）6 的引脚（Pin）7：`UT3_T1_B`。

<a id="a434fbeabd67039cc7fbb8bf0f3827519"></a>

### `PIN_P7_0__CDC_D16_A`

```c
#define PIN_P7_0__CDC_D16_A ALIF_PINMUX(7, 0, 6)
```

端口（Port）7 的引脚（Pin）0：`CDC_D16_A`。

<a id="ac5e4bcb47b0ccd35d7458401dbe81233"></a>

### `PIN_P7_0__GPIO`

```c
#define PIN_P7_0__GPIO ALIF_PINMUX(7, 0, 0)
```

引脚 `P7.0` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）0：`GPIO`。

<a id="a1fde60e018d010f91f259fe2684f2bef"></a>

### `PIN_P7_0__I2C0_SDA_C`

```c
#define PIN_P7_0__I2C0_SDA_C ALIF_PINMUX(7, 0, 4)
```

端口（Port）7 的引脚（Pin）0：`I2C0_SDA_C`。

<a id="ac61deb751bad112fb5744f0b14556b75"></a>

### `PIN_P7_0__LPCAM_D0_B`

```c
#define PIN_P7_0__LPCAM_D0_B ALIF_PINMUX(7, 0, 5)
```

端口（Port）7 的引脚（Pin）0：`LPCAM_D0_B`。

<a id="ac02486e63bf2d9a793552ab7e8c57fab"></a>

### `PIN_P7_0__LPUART_RX_B`

```c
#define PIN_P7_0__LPUART_RX_B ALIF_PINMUX(7, 0, 2)
```

端口（Port）7 的引脚（Pin）0：`LPUART_RX_B`。

<a id="a81333f2343eb5b4490a59236c211dce9"></a>

### `PIN_P7_0__OSPI0_SCLK_C`

```c
#define PIN_P7_0__OSPI0_SCLK_C ALIF_PINMUX(7, 0, 1)
```

端口（Port）7 的引脚（Pin）0：`OSPI0_SCLK_C`。

<a id="ad7e701bd246ba906f0ccd67dfae4ff96"></a>

### `PIN_P7_0__SPI2_MISO_B`

```c
#define PIN_P7_0__SPI2_MISO_B ALIF_PINMUX(7, 0, 3)
```

端口（Port）7 的引脚（Pin）0：`SPI2_MISO_B`。

<a id="a41a1d3b230284cc4de145da552bc072f"></a>

### `PIN_P7_1__CDC_D17_A`

```c
#define PIN_P7_1__CDC_D17_A ALIF_PINMUX(7, 1, 6)
```

端口（Port）7 的引脚（Pin）1：`CDC_D17_A`。

<a id="afd333ffdddac335d52e506deb72eacaf"></a>

### `PIN_P7_1__GPIO`

```c
#define PIN_P7_1__GPIO ALIF_PINMUX(7, 1, 0)
```

引脚 `P7.1` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）1：`GPIO`。

<a id="af1c7a7f1fc1d87b7036a5ac346c435a7"></a>

### `PIN_P7_1__I2C0_SCL_C`

```c
#define PIN_P7_1__I2C0_SCL_C ALIF_PINMUX(7, 1, 4)
```

端口（Port）7 的引脚（Pin）1：`I2C0_SCL_C`。

<a id="a4a5713a8962c62a0a8bcd0766da483fc"></a>

### `PIN_P7_1__LPCAM_D1_B`

```c
#define PIN_P7_1__LPCAM_D1_B ALIF_PINMUX(7, 1, 5)
```

端口（Port）7 的引脚（Pin）1：`LPCAM_D1_B`。

<a id="ae0167e359b7e8636c8ac16a70e1e8268"></a>

### `PIN_P7_1__LPUART_TX_B`

```c
#define PIN_P7_1__LPUART_TX_B ALIF_PINMUX(7, 1, 2)
```

端口（Port）7 的引脚（Pin）1：`LPUART_TX_B`。

<a id="a40442bb3dc5803462792e7f422a6cea8"></a>

### `PIN_P7_1__OSPI0_SCLKN_C`

```c
#define PIN_P7_1__OSPI0_SCLKN_C ALIF_PINMUX(7, 1, 1)
```

端口（Port）7 的引脚（Pin）1：`OSPI0_SCLKN_C`。

<a id="aabd05e34bb204e9b9a11a27a91a8f4d2"></a>

### `PIN_P7_1__SPI2_MOSI_B`

```c
#define PIN_P7_1__SPI2_MOSI_B ALIF_PINMUX(7, 1, 3)
```

端口（Port）7 的引脚（Pin）1：`SPI2_MOSI_B`。

<a id="afc62dda2e707d7d994e3d31b72911caa"></a>

### `PIN_P7_2__CDC_D18_A`

```c
#define PIN_P7_2__CDC_D18_A ALIF_PINMUX(7, 2, 6)
```

端口（Port）7 的引脚（Pin）2：`CDC_D18_A`。

<a id="adc16259fec5582a1e6ebc9cb8a825c03"></a>

### `PIN_P7_2__GPIO`

```c
#define PIN_P7_2__GPIO ALIF_PINMUX(7, 2, 0)
```

引脚 `P7.2` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）2：`GPIO`。

<a id="a803ef3f2d107d05670bba596998fca2a"></a>

### `PIN_P7_2__I2C1_SDA_C`

```c
#define PIN_P7_2__I2C1_SDA_C ALIF_PINMUX(7, 2, 4)
```

端口（Port）7 的引脚（Pin）2：`I2C1_SDA_C`。

<a id="a406797f78dd005ce0485b9d2807fc8f3"></a>

### `PIN_P7_2__LPCAM_D2_B`

```c
#define PIN_P7_2__LPCAM_D2_B ALIF_PINMUX(7, 2, 5)
```

端口（Port）7 的引脚（Pin）2：`LPCAM_D2_B`。

<a id="a2ac043357aa1f8f702f196f070023af4"></a>

### `PIN_P7_2__LPUART_CTS_B`

```c
#define PIN_P7_2__LPUART_CTS_B ALIF_PINMUX(7, 2, 2)
```

端口（Port）7 的引脚（Pin）2：`LPUART_CTS_B`。

<a id="a7123e2e8362601d8f25102c6c9ea14c3"></a>

### `PIN_P7_2__OSPI0_SS0_C`

```c
#define PIN_P7_2__OSPI0_SS0_C ALIF_PINMUX(7, 2, 1)
```

端口（Port）7 的引脚（Pin）2：`OSPI0_SS0_C`。

<a id="a176b3c4d6fc1f304ff10fe307a175ac7"></a>

### `PIN_P7_2__SPI2_SCLK_B`

```c
#define PIN_P7_2__SPI2_SCLK_B ALIF_PINMUX(7, 2, 3)
```

端口（Port）7 的引脚（Pin）2：`SPI2_SCLK_B`。

<a id="acc8d18e6404550464314fa765a8fc821"></a>

### `PIN_P7_3__CDC_D19_A`

```c
#define PIN_P7_3__CDC_D19_A ALIF_PINMUX(7, 3, 6)
```

端口（Port）7 的引脚（Pin）3：`CDC_D19_A`。

<a id="a75dbeec7072793acd5eaa20f0d0d1055"></a>

### `PIN_P7_3__GPIO`

```c
#define PIN_P7_3__GPIO ALIF_PINMUX(7, 3, 0)
```

引脚 `P7.3` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）3：`GPIO`。

<a id="a62c7010c5c2ec0aa887cdc198dc4ab61"></a>

### `PIN_P7_3__I2C1_SCL_C`

```c
#define PIN_P7_3__I2C1_SCL_C ALIF_PINMUX(7, 3, 4)
```

端口（Port）7 的引脚（Pin）3：`I2C1_SCL_C`。

<a id="a654db72e8024434dee055f3a3a1c2308"></a>

### `PIN_P7_3__LPCAM_D3_B`

```c
#define PIN_P7_3__LPCAM_D3_B ALIF_PINMUX(7, 3, 5)
```

端口（Port）7 的引脚（Pin）3：`LPCAM_D3_B`。

<a id="a4ed1e54224d8b1cd53fb993e739ee817"></a>

### `PIN_P7_3__LPUART_RTS_B`

```c
#define PIN_P7_3__LPUART_RTS_B ALIF_PINMUX(7, 3, 2)
```

端口（Port）7 的引脚（Pin）3：`LPUART_RTS_B`。

<a id="a1c916c92dca31a5ebf293130254c4a90"></a>

### `PIN_P7_3__OSPI0_SS1_C`

```c
#define PIN_P7_3__OSPI0_SS1_C ALIF_PINMUX(7, 3, 1)
```

端口（Port）7 的引脚（Pin）3：`OSPI0_SS1_C`。

<a id="a6e47c806b3893950d5c0100c93cd4b62"></a>

### `PIN_P7_3__SPI2_SS0_B`

```c
#define PIN_P7_3__SPI2_SS0_B ALIF_PINMUX(7, 3, 3)
```

端口（Port）7 的引脚（Pin）3：`SPI2_SS0_B`。

<a id="a10eb04884400107ff7db9327d92feb07"></a>

### `PIN_P7_4__CDC_D20_A`

```c
#define PIN_P7_4__CDC_D20_A ALIF_PINMUX(7, 4, 6)
```

端口（Port）7 的引脚（Pin）4：`CDC_D20_A`。

<a id="ae4761d31982dad9a275346a237d734c7"></a>

### `PIN_P7_4__GPIO`

```c
#define PIN_P7_4__GPIO ALIF_PINMUX(7, 4, 0)
```

引脚 `P7.4` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）4：`GPIO`。

<a id="a4d2e0b66dae7d0082d4898b4392cb289"></a>

### `PIN_P7_4__LPCAM_D4_B`

```c
#define PIN_P7_4__LPCAM_D4_B ALIF_PINMUX(7, 4, 5)
```

端口（Port）7 的引脚（Pin）4：`LPCAM_D4_B`。

<a id="a43db86bba44a27ce84e2f1f11a62cece"></a>

### `PIN_P7_4__LPI2C0_SCL_C`

```c
#define PIN_P7_4__LPI2C0_SCL_C ALIF_PINMUX(7, 4, 4)
```

端口（Port）7 的引脚（Pin）4：`LPI2C0_SCL_C`。

<a id="ae67ab14af06fffcc4e02c1247e3184f3"></a>

### `PIN_P7_4__LPPDM_C2_C`

```c
#define PIN_P7_4__LPPDM_C2_C ALIF_PINMUX(7, 4, 2)
```

端口（Port）7 的引脚（Pin）4：`LPPDM_C2_C`。

<a id="aa3fe8586c90b46938d06b25f468596de"></a>

### `PIN_P7_4__SPI2_SS1_B`

```c
#define PIN_P7_4__SPI2_SS1_B ALIF_PINMUX(7, 4, 3)
```

端口（Port）7 的引脚（Pin）4：`SPI2_SS1_B`。

<a id="a166f0d58b8578261369787277e3a70d1"></a>

### `PIN_P7_4__UART3_CTS_B`

```c
#define PIN_P7_4__UART3_CTS_B ALIF_PINMUX(7, 4, 1)
```

端口（Port）7 的引脚（Pin）4：`UART3_CTS_B`。

<a id="aed833e3e5644c082d2aff8d460aa7ab4"></a>

### `PIN_P7_5__CDC_D21_A`

```c
#define PIN_P7_5__CDC_D21_A ALIF_PINMUX(7, 5, 6)
```

端口（Port）7 的引脚（Pin）5：`CDC_D21_A`。

<a id="ac47d162d1d4eb774e733fe27673c7c6b"></a>

### `PIN_P7_5__GPIO`

```c
#define PIN_P7_5__GPIO ALIF_PINMUX(7, 5, 0)
```

引脚 `P7.5` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）5：`GPIO`。

<a id="a21c2ed1feba0129e42f54bd9a45f5064"></a>

### `PIN_P7_5__LPCAM_D5_B`

```c
#define PIN_P7_5__LPCAM_D5_B ALIF_PINMUX(7, 5, 5)
```

端口（Port）7 的引脚（Pin）5：`LPCAM_D5_B`。

<a id="a3fb7404ea8166f4ddd1ca38982d0da08"></a>

### `PIN_P7_5__LPI2C0_SDA_C`

```c
#define PIN_P7_5__LPI2C0_SDA_C ALIF_PINMUX(7, 5, 4)
```

端口（Port）7 的引脚（Pin）5：`LPI2C0_SDA_C`。

<a id="a43b9e2e891e5c79f8f2fd049c2255fc7"></a>

### `PIN_P7_5__LPPDM_D2_C`

```c
#define PIN_P7_5__LPPDM_D2_C ALIF_PINMUX(7, 5, 2)
```

端口（Port）7 的引脚（Pin）5：`LPPDM_D2_C`。

<a id="a6ec983760b4afbd138517dd7fae4333a"></a>

### `PIN_P7_5__SPI2_SS2_B`

```c
#define PIN_P7_5__SPI2_SS2_B ALIF_PINMUX(7, 5, 3)
```

端口（Port）7 的引脚（Pin）5：`SPI2_SS2_B`。

<a id="a34f0e74e10b4bdcedf5490f07bc94510"></a>

### `PIN_P7_5__UART3_RTS_B`

```c
#define PIN_P7_5__UART3_RTS_B ALIF_PINMUX(7, 5, 1)
```

端口（Port）7 的引脚（Pin）5：`UART3_RTS_B`。

<a id="abdbf76721d7bfbbb08a27266913b8ebf"></a>

### `PIN_P7_6__CDC_D22_A`

```c
#define PIN_P7_6__CDC_D22_A ALIF_PINMUX(7, 6, 6)
```

端口（Port）7 的引脚（Pin）6：`CDC_D22_A`。

<a id="ab95fc52f53c6a1703df290ac307871e4"></a>

### `PIN_P7_6__GPIO`

```c
#define PIN_P7_6__GPIO ALIF_PINMUX(7, 6, 0)
```

引脚 `P7.6` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）6：`GPIO`。

<a id="abc5d28133fc1f9173df80aa2abe39955"></a>

### `PIN_P7_6__LPCAM_D6_B`

```c
#define PIN_P7_6__LPCAM_D6_B ALIF_PINMUX(7, 6, 5)
```

端口（Port）7 的引脚（Pin）6：`LPCAM_D6_B`。

<a id="ab4b3792dd2d61cee03eae788dbe32c88"></a>

### `PIN_P7_6__LPPDM_C3_C`

```c
#define PIN_P7_6__LPPDM_C3_C ALIF_PINMUX(7, 6, 3)
```

端口（Port）7 的引脚（Pin）6：`LPPDM_C3_C`。

<a id="ac86c6e2a402bc36f8b371b3b3c52c031"></a>

### `PIN_P7_6__SEUART_RX_C`

```c
#define PIN_P7_6__SEUART_RX_C ALIF_PINMUX(7, 6, 1)
```

端口（Port）7 的引脚（Pin）6：`SEUART_RX_C`。

<a id="ab78d246a64325058b5f1b7cb6cc11e15"></a>

### `PIN_P7_6__SPI0_MISO_C`

```c
#define PIN_P7_6__SPI0_MISO_C ALIF_PINMUX(7, 6, 4)
```

端口（Port）7 的引脚（Pin）6：`SPI0_MISO_C`。

<a id="ae176791eedf1350b98257d2500273beb"></a>

### `PIN_P7_6__UART5_RX_B`

```c
#define PIN_P7_6__UART5_RX_B ALIF_PINMUX(7, 6, 2)
```

端口（Port）7 的引脚（Pin）6：`UART5_RX_B`。

<a id="a5baa436ab02db34ffd62978c8428e1c5"></a>

### `PIN_P7_7__CDC_D23_A`

```c
#define PIN_P7_7__CDC_D23_A ALIF_PINMUX(7, 7, 6)
```

端口（Port）7 的引脚（Pin）7：`CDC_D23_A`。

<a id="ae3abc19efe0b06fc7f3dc73c1eb040c7"></a>

### `PIN_P7_7__GPIO`

```c
#define PIN_P7_7__GPIO ALIF_PINMUX(7, 7, 0)
```

引脚 `P7.7` 的复用功能（Alternate Functions）。

端口（Port）7 的引脚（Pin）7：`GPIO`。

<a id="ada14fb90a5399c5e4b0a8a880ea70ef8"></a>

### `PIN_P7_7__LPCAM_D7_B`

```c
#define PIN_P7_7__LPCAM_D7_B ALIF_PINMUX(7, 7, 5)
```

端口（Port）7 的引脚（Pin）7：`LPCAM_D7_B`。

<a id="a6719936ee12e645dccf126f627c96bdb"></a>

### `PIN_P7_7__LPPDM_D3_C`

```c
#define PIN_P7_7__LPPDM_D3_C ALIF_PINMUX(7, 7, 3)
```

端口（Port）7 的引脚（Pin）7：`LPPDM_D3_C`。

<a id="a5c82a65c9a340d4ed121a7a03d295739"></a>

### `PIN_P7_7__SEUART_TX_C`

```c
#define PIN_P7_7__SEUART_TX_C ALIF_PINMUX(7, 7, 1)
```

端口（Port）7 的引脚（Pin）7：`SEUART_TX_C`。

<a id="a6cada0c7c7ac09e8ec99fb99b0e64cc5"></a>

### `PIN_P7_7__SPI0_MOSI_C`

```c
#define PIN_P7_7__SPI0_MOSI_C ALIF_PINMUX(7, 7, 4)
```

端口（Port）7 的引脚（Pin）7：`SPI0_MOSI_C`。

<a id="aa791fcf124397d4852a8319404c7f7b1"></a>

### `PIN_P7_7__UART5_TX_B`

```c
#define PIN_P7_7__UART5_TX_B ALIF_PINMUX(7, 7, 2)
```

端口（Port）7 的引脚（Pin）7：`UART5_TX_B`。

<a id="afae07d2c2c36cf28b58d3025bd312bcd"></a>

### `PIN_P8_0__GPIO`

```c
#define PIN_P8_0__GPIO ALIF_PINMUX(8, 0, 0)
```

引脚 `P8.0` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）0：`GPIO`。

<a id="add5139fb39426db9eecc9077b6cb460a"></a>

### `PIN_P8_0__I2S0_SDI_C`

```c
#define PIN_P8_0__I2S0_SDI_C ALIF_PINMUX(8, 0, 2)
```

端口（Port）8 的引脚（Pin）0：`I2S0_SDI_C`。

<a id="ad71cd9d2d19e676624b7d597620d456a"></a>

### `PIN_P8_0__I3C_SCL_C`

```c
#define PIN_P8_0__I3C_SCL_C ALIF_PINMUX(8, 0, 6)
```

端口（Port）8 的引脚（Pin）0：`I3C_SCL_C`。

<a id="a80efe03682baa66d7367d29c3226e7c5"></a>

### `PIN_P8_0__SD_CMD_C`

```c
#define PIN_P8_0__SD_CMD_C ALIF_PINMUX(8, 0, 5)
```

端口（Port）8 的引脚（Pin）0：`SD_CMD_C`。

<a id="aa16141bb8f8655b759d2c1d89f811654"></a>

### `PIN_P8_0__SPI0_SCLK_C`

```c
#define PIN_P8_0__SPI0_SCLK_C ALIF_PINMUX(8, 0, 3)
```

端口（Port）8 的引脚（Pin）0：`SPI0_SCLK_C`。

<a id="a58bbba227cb5e1f12ac075c9a5e42e75"></a>

### `PIN_P8_0__UART0_RX_C`

```c
#define PIN_P8_0__UART0_RX_C ALIF_PINMUX(8, 0, 1)
```

端口（Port）8 的引脚（Pin）0：`UART0_RX_C`。

<a id="ab79c19d10789928fc5221dde4ffc7631"></a>

### `PIN_P8_0__UT0_T0_C`

```c
#define PIN_P8_0__UT0_T0_C ALIF_PINMUX(8, 0, 4)
```

端口（Port）8 的引脚（Pin）0：`UT0_T0_C`。

<a id="ab7545d1438381ff91c47907abe36bde2"></a>

### `PIN_P8_1__GPIO`

```c
#define PIN_P8_1__GPIO ALIF_PINMUX(8, 1, 0)
```

引脚 `P8.1` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）1：`GPIO`。

<a id="aecdf8538d1daba974407d66a6826d18d"></a>

### `PIN_P8_1__I2S0_SDO_C`

```c
#define PIN_P8_1__I2S0_SDO_C ALIF_PINMUX(8, 1, 2)
```

端口（Port）8 的引脚（Pin）1：`I2S0_SDO_C`。

<a id="a206e662c71dd50a55059bc9454a19379"></a>

### `PIN_P8_1__I3C_SDA_C`

```c
#define PIN_P8_1__I3C_SDA_C ALIF_PINMUX(8, 1, 6)
```

端口（Port）8 的引脚（Pin）1：`I3C_SDA_C`。

<a id="a7ddacd2a5789fe8587a24daed92619f7"></a>

### `PIN_P8_1__SD_CLK_C`

```c
#define PIN_P8_1__SD_CLK_C ALIF_PINMUX(8, 1, 5)
```

端口（Port）8 的引脚（Pin）1：`SD_CLK_C`。

<a id="a8551b940fa9293173f90da6886079ac7"></a>

### `PIN_P8_1__SPI0_SS0_C`

```c
#define PIN_P8_1__SPI0_SS0_C ALIF_PINMUX(8, 1, 3)
```

端口（Port）8 的引脚（Pin）1：`SPI0_SS0_C`。

<a id="a3708ad7f65ca0bd5a0d05c390aa3bc36"></a>

### `PIN_P8_1__UART0_TX_C`

```c
#define PIN_P8_1__UART0_TX_C ALIF_PINMUX(8, 1, 1)
```

端口（Port）8 的引脚（Pin）1：`UART0_TX_C`。

<a id="a6e0b62693de52080c892062924740675"></a>

### `PIN_P8_1__UT0_T1_C`

```c
#define PIN_P8_1__UT0_T1_C ALIF_PINMUX(8, 1, 4)
```

端口（Port）8 的引脚（Pin）1：`UT0_T1_C`。

<a id="a66e4eadceca2ff968dfa3195a4250122"></a>

### `PIN_P8_2__CAN0_RXD_C`

```c
#define PIN_P8_2__CAN0_RXD_C ALIF_PINMUX(8, 2, 7)
```

端口（Port）8 的引脚（Pin）2：`CAN0_RXD_C`。

<a id="a60cd1313b5dbd2f3e804024add367802"></a>

### `PIN_P8_2__GPIO`

```c
#define PIN_P8_2__GPIO ALIF_PINMUX(8, 2, 0)
```

引脚 `P8.2` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）2：`GPIO`。

<a id="a32c45381d99f79eaee7a76484eecb64e"></a>

### `PIN_P8_2__I2S0_SCLK_C`

```c
#define PIN_P8_2__I2S0_SCLK_C ALIF_PINMUX(8, 2, 3)
```

端口（Port）8 的引脚（Pin）2：`I2S0_SCLK_C`。

<a id="a4a76b56c903dba7a0aa59fed719b4667"></a>

### `PIN_P8_2__SD_RST_C`

```c
#define PIN_P8_2__SD_RST_C ALIF_PINMUX(8, 2, 6)
```

端口（Port）8 的引脚（Pin）2：`SD_RST_C`。

<a id="a86921d6a2960aabd4d0386fda119c312"></a>

### `PIN_P8_2__SEUART_RX_B`

```c
#define PIN_P8_2__SEUART_RX_B ALIF_PINMUX(8, 2, 1)
```

端口（Port）8 的引脚（Pin）2：`SEUART_RX_B`。

<a id="aa86eff0d25a32c3ae0ec1186800140f5"></a>

### `PIN_P8_2__SPI0_SS1_C`

```c
#define PIN_P8_2__SPI0_SS1_C ALIF_PINMUX(8, 2, 4)
```

端口（Port）8 的引脚（Pin）2：`SPI0_SS1_C`。

<a id="ab5340acc8bb2b67e47ab6cafaf1e3f73"></a>

### `PIN_P8_2__UART1_RX_C`

```c
#define PIN_P8_2__UART1_RX_C ALIF_PINMUX(8, 2, 2)
```

端口（Port）8 的引脚（Pin）2：`UART1_RX_C`。

<a id="a46fb8739c6ae846bf36cafad253ebe20"></a>

### `PIN_P8_2__UT1_T0_C`

```c
#define PIN_P8_2__UT1_T0_C ALIF_PINMUX(8, 2, 5)
```

端口（Port）8 的引脚（Pin）2：`UT1_T0_C`。

<a id="af7a4aec639e5e6c29d29dd9f1511e5fb"></a>

### `PIN_P8_3__CAN0_TXD_C`

```c
#define PIN_P8_3__CAN0_TXD_C ALIF_PINMUX(8, 3, 6)
```

端口（Port）8 的引脚（Pin）3：`CAN0_TXD_C`。

<a id="a34640dc5781b53cbf9113e1def9fc2ff"></a>

### `PIN_P8_3__EXT_RTS_B`

```c
#define PIN_P8_3__EXT_RTS_B ALIF_PINMUX(8, 3, 7)
```

端口（Port）8 的引脚（Pin）3：`EXT_RTS_B`。

<a id="ada60da6343aec9d7f341d29d6c0f7d6e"></a>

### `PIN_P8_3__GPIO`

```c
#define PIN_P8_3__GPIO ALIF_PINMUX(8, 3, 0)
```

引脚 `P8.3` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）3：`GPIO`。

<a id="afb096c4d807b834a4a8aa1bd0c899e50"></a>

### `PIN_P8_3__I2S0_WS_C`

```c
#define PIN_P8_3__I2S0_WS_C ALIF_PINMUX(8, 3, 3)
```

端口（Port）8 的引脚（Pin）3：`I2S0_WS_C`。

<a id="a6648fb7145169a8b26d9f7be77927683"></a>

### `PIN_P8_3__SEUART_TX_B`

```c
#define PIN_P8_3__SEUART_TX_B ALIF_PINMUX(8, 3, 1)
```

端口（Port）8 的引脚（Pin）3：`SEUART_TX_B`。

<a id="a7f20e17c17ec01ee643a192119f9fbe5"></a>

### `PIN_P8_3__SPI0_SS2_C`

```c
#define PIN_P8_3__SPI0_SS2_C ALIF_PINMUX(8, 3, 4)
```

端口（Port）8 的引脚（Pin）3：`SPI0_SS2_C`。

<a id="a61fa9fcc8852a233ea722ac92481d152"></a>

### `PIN_P8_3__UART1_TX_C`

```c
#define PIN_P8_3__UART1_TX_C ALIF_PINMUX(8, 3, 2)
```

端口（Port）8 的引脚（Pin）3：`UART1_TX_C`。

<a id="a51e2fecfda5f8e671340b40116b241be"></a>

### `PIN_P8_3__UT1_T1_C`

```c
#define PIN_P8_3__UT1_T1_C ALIF_PINMUX(8, 3, 5)
```

端口（Port）8 的引脚（Pin）3：`UT1_T1_C`。

<a id="ac485ddd7241a84dccdd1c1a2bf011fc1"></a>

### `PIN_P8_4__CAN0_STBY_C`

```c
#define PIN_P8_4__CAN0_STBY_C ALIF_PINMUX(8, 4, 6)
```

端口（Port）8 的引脚（Pin）4：`CAN0_STBY_C`。

<a id="a6dcf47f3f8095e7bb8e33bd49eb65bfa"></a>

### `PIN_P8_4__EXT_CTS_B`

```c
#define PIN_P8_4__EXT_CTS_B ALIF_PINMUX(8, 4, 7)
```

端口（Port）8 的引脚（Pin）4：`EXT_CTS_B`。

<a id="a077f91c6d32af478832d2f868a03ce92"></a>

### `PIN_P8_4__GPIO`

```c
#define PIN_P8_4__GPIO ALIF_PINMUX(8, 4, 0)
```

引脚 `P8.4` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）4：`GPIO`。

<a id="a120e7ac88d5656af5ae1050b1ade43aa"></a>

### `PIN_P8_4__I2S1_SDI_C`

```c
#define PIN_P8_4__I2S1_SDI_C ALIF_PINMUX(8, 4, 2)
```

端口（Port）8 的引脚（Pin）4：`I2S1_SDI_C`。

<a id="acf34db33a03da94b1b557826ca9c6fca"></a>

### `PIN_P8_4__LPCAM_VSYNC_C`

```c
#define PIN_P8_4__LPCAM_VSYNC_C ALIF_PINMUX(8, 4, 5)
```

端口（Port）8 的引脚（Pin）4：`LPCAM_VSYNC_C`。

<a id="aa22e557329e1a5bb4cbcf3b614ba066c"></a>

### `PIN_P8_4__SPI1_MISO_C`

```c
#define PIN_P8_4__SPI1_MISO_C ALIF_PINMUX(8, 4, 3)
```

端口（Port）8 的引脚（Pin）4：`SPI1_MISO_C`。

<a id="a63f07834cb140489a435742cb4bb8929"></a>

### `PIN_P8_4__UART2_RX_C`

```c
#define PIN_P8_4__UART2_RX_C ALIF_PINMUX(8, 4, 1)
```

端口（Port）8 的引脚（Pin）4：`UART2_RX_C`。

<a id="a24aee8e934f4b64d7e7db9c69ba84010"></a>

### `PIN_P8_4__UT2_T0_C`

```c
#define PIN_P8_4__UT2_T0_C ALIF_PINMUX(8, 4, 4)
```

端口（Port）8 的引脚（Pin）4：`UT2_T0_C`。

<a id="aa9c0b4c975f719fed6151f781e2ff914"></a>

### `PIN_P8_5__CAN1_RXD_B`

```c
#define PIN_P8_5__CAN1_RXD_B ALIF_PINMUX(8, 5, 6)
```

端口（Port）8 的引脚（Pin）5：`CAN1_RXD_B`。

<a id="a5cb04e2264ad4c65af758f8962647f15"></a>

### `PIN_P8_5__EXT_TRACE_B`

```c
#define PIN_P8_5__EXT_TRACE_B ALIF_PINMUX(8, 5, 7)
```

端口（Port）8 的引脚（Pin）5：`EXT_TRACE_B`。

<a id="a3d1dbbf65ec7141c08cbdf70186faa0a"></a>

### `PIN_P8_5__GPIO`

```c
#define PIN_P8_5__GPIO ALIF_PINMUX(8, 5, 0)
```

引脚 `P8.5` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）5：`GPIO`。

<a id="ae7050df3aa65dfea482ae99ae9993c75"></a>

### `PIN_P8_5__I2S1_SDO_C`

```c
#define PIN_P8_5__I2S1_SDO_C ALIF_PINMUX(8, 5, 2)
```

端口（Port）8 的引脚（Pin）5：`I2S1_SDO_C`。

<a id="afa53accd52402116b20cc56ddbf81144"></a>

### `PIN_P8_5__LPCAM_HSYNC_C`

```c
#define PIN_P8_5__LPCAM_HSYNC_C ALIF_PINMUX(8, 5, 5)
```

端口（Port）8 的引脚（Pin）5：`LPCAM_HSYNC_C`。

<a id="a55e6064e7f03d2c5b7d2f085384b06af"></a>

### `PIN_P8_5__SPI1_MOSI_C`

```c
#define PIN_P8_5__SPI1_MOSI_C ALIF_PINMUX(8, 5, 3)
```

端口（Port）8 的引脚（Pin）5：`SPI1_MOSI_C`。

<a id="ad31f2a501dd199a749a1c95d6d82273d"></a>

### `PIN_P8_5__UART2_TX_C`

```c
#define PIN_P8_5__UART2_TX_C ALIF_PINMUX(8, 5, 1)
```

端口（Port）8 的引脚（Pin）5：`UART2_TX_C`。

<a id="a014098250157c9b8db9f0f5eb3c05254"></a>

### `PIN_P8_5__UT2_T1_C`

```c
#define PIN_P8_5__UT2_T1_C ALIF_PINMUX(8, 5, 4)
```

端口（Port）8 的引脚（Pin）5：`UT2_T1_C`。

<a id="a7db044cf6eed8db9319ab0a56b23ff4a"></a>

### `PIN_P8_6__CAN1_TXD_B`

```c
#define PIN_P8_6__CAN1_TXD_B ALIF_PINMUX(8, 6, 6)
```

端口（Port）8 的引脚（Pin）6：`CAN1_TXD_B`。

<a id="af2fe383f96275201cdad073aa15ee7c6"></a>

### `PIN_P8_6__EXT_RX_B`

```c
#define PIN_P8_6__EXT_RX_B ALIF_PINMUX(8, 6, 7)
```

端口（Port）8 的引脚（Pin）6：`EXT_RX_B`。

<a id="aac04079cc075adb9c60dc629fb9e544e"></a>

### `PIN_P8_6__GPIO`

```c
#define PIN_P8_6__GPIO ALIF_PINMUX(8, 6, 0)
```

引脚 `P8.6` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）6：`GPIO`。

<a id="a0385729cf0232abca6c12d677915cc56"></a>

### `PIN_P8_6__I2S1_SCLK_SLV_C`

```c
#define PIN_P8_6__I2S1_SCLK_SLV_C ALIF_PINMUX(8, 6, 2)
```

端口（Port）8 的引脚（Pin）6：`I2S1_SCLK_SLV_C`。

<a id="ad8746ccd7ebe5b1f96b31ec2ffefe862"></a>

### `PIN_P8_6__LPCAM_PCLK_C`

```c
#define PIN_P8_6__LPCAM_PCLK_C ALIF_PINMUX(8, 6, 5)
```

端口（Port）8 的引脚（Pin）6：`LPCAM_PCLK_C`。

<a id="ab61338d7cfa1b124b4aefd3232973fa5"></a>

### `PIN_P8_6__SPI1_SCLK_C`

```c
#define PIN_P8_6__SPI1_SCLK_C ALIF_PINMUX(8, 6, 3)
```

端口（Port）8 的引脚（Pin）6：`SPI1_SCLK_C`。

<a id="a314b2b687c40bf633cbb380a8fef9be0"></a>

### `PIN_P8_6__UART3_RX_C`

```c
#define PIN_P8_6__UART3_RX_C ALIF_PINMUX(8, 6, 1)
```

端口（Port）8 的引脚（Pin）6：`UART3_RX_C`。

<a id="a0659b1c3adb2e94c605a2cb2d47f6478"></a>

### `PIN_P8_6__UT3_T0_C`

```c
#define PIN_P8_6__UT3_T0_C ALIF_PINMUX(8, 6, 4)
```

端口（Port）8 的引脚（Pin）6：`UT3_T0_C`。

<a id="ac5141e80198c35db5cc964ae99d02c0a"></a>

### `PIN_P8_7__CAN1_STBY_B`

```c
#define PIN_P8_7__CAN1_STBY_B ALIF_PINMUX(8, 7, 6)
```

端口（Port）8 的引脚（Pin）7：`CAN1_STBY_B`。

<a id="a71a58c7d97e8a9d0f6e8c66274a32b5e"></a>

### `PIN_P8_7__EXT_TX_B`

```c
#define PIN_P8_7__EXT_TX_B ALIF_PINMUX(8, 7, 7)
```

端口（Port）8 的引脚（Pin）7：`EXT_TX_B`。

<a id="adeed03c5ceab2806bff7df654f45982d"></a>

### `PIN_P8_7__GPIO`

```c
#define PIN_P8_7__GPIO ALIF_PINMUX(8, 7, 0)
```

引脚 `P8.7` 的复用功能（Alternate Functions）。

端口（Port）8 的引脚（Pin）7：`GPIO`。

<a id="af8422945c480799c91c5194eb5ef3674"></a>

### `PIN_P8_7__I2S1_WS_SLV_C`

```c
#define PIN_P8_7__I2S1_WS_SLV_C ALIF_PINMUX(8, 7, 2)
```

端口（Port）8 的引脚（Pin）7：`I2S1_WS_SLV_C`。

<a id="aaefded103cf34db389da0e730b66f41c"></a>

### `PIN_P8_7__LPCAM_XVCLK_C`

```c
#define PIN_P8_7__LPCAM_XVCLK_C ALIF_PINMUX(8, 7, 5)
```

端口（Port）8 的引脚（Pin）7：`LPCAM_XVCLK_C`。

<a id="a3fe74929914837237c6ce113ea00535b"></a>

### `PIN_P8_7__SPI1_SS0_C`

```c
#define PIN_P8_7__SPI1_SS0_C ALIF_PINMUX(8, 7, 3)
```

端口（Port）8 的引脚（Pin）7：`SPI1_SS0_C`。

<a id="ae47d9b593d7d7508eccf313133767a82"></a>

### `PIN_P8_7__UART3_TX_C`

```c
#define PIN_P8_7__UART3_TX_C ALIF_PINMUX(8, 7, 1)
```

端口（Port）8 的引脚（Pin）7：`UART3_TX_C`。

<a id="a1204f92355e74076ef32abe8ddf62cb1"></a>

### `PIN_P8_7__UT3_T1_C`

```c
#define PIN_P8_7__UT3_T1_C ALIF_PINMUX(8, 7, 4)
```

端口（Port）8 的引脚（Pin）7：`UT3_T1_C`。


## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P019_alif-balletto-b1-pinctrl.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a195b3893d9913e77419e111178923a3d"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a280dd67858770ceb0a88153aa29e09da"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a5d3f4f922452dc948bcc7727d9875107"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a723a8df1e91c947c25af42db8b9f73dd"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_a8c94e09e787a9fb1079e5fbe0aa875d2"></a>
<a id="aalif-balletto-b1-pinctrl_8h_html_ab8529e7ad1002e2e112bf1286d4d6c62"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__pinctrl__alif-ensemble-e1c-pinctrl.h_文件参考.md)
