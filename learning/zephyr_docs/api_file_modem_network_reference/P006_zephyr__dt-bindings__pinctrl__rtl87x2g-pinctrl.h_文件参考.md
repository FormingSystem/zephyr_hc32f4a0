---
id: learning.zephyr-docs.api-file-modem-network-reference.page-6
title: zephyr__dt-bindings__pinctrl__rtl87x2g-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_rtl87x2g-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl87x2g-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RTL87X2G引脚控制（Pin Control / Pinmux）的头文件。

<a id="details"></a>

```c
#include "bee-pinctrl.h"
```

查看此文件的源码。

RTL87X2G 引脚控制（Pin Control／Pinmux）头文件。本文件定义 Realtek RTL87X2G 片上系统（SoC）系列的引脚复用功能（Pinmux Functions）和引脚分配（Pin Assignments）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 引脚控制复用功能（Pinctrl Pinmux Functions）

<a id="r_aa96a1b1f865f33896d26cb0ebc67a654"></a>

```c
#define BEE_IDLE_MODE 0
```

相关声明：[BEE_IDLE_MODE](#aa96a1b1f865f33896d26cb0ebc67a654)。

`IDLE_MODE` 引脚复用功能（Pinmux Function）。

<a id="r_aba42501ee83715ca6ea53df22183c5f6"></a>

```c
#define BEE_UART0_TX 1
```

相关声明：[BEE_UART0_TX](#aba42501ee83715ca6ea53df22183c5f6)。

`UART0_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a1c7070aee57aedc7f8a131fe34444d60"></a>

```c
#define BEE_UART0_RX 2
```

相关声明：[BEE_UART0_RX](#a1c7070aee57aedc7f8a131fe34444d60)。

`UART0_RX` 引脚复用功能（Pinmux Function）。

<a id="r_af5094e3bfde1cf22e80c9144763940cc"></a>

```c
#define BEE_UART0_CTS 3
```

相关声明：[BEE_UART0_CTS](#af5094e3bfde1cf22e80c9144763940cc)。

`UART0_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a6ea0a2599d172ee66154a55c6dad1544"></a>

```c
#define BEE_UART0_RTS 4
```

相关声明：[BEE_UART0_RTS](#a6ea0a2599d172ee66154a55c6dad1544)。

`UART0_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_acf789455a751381f67bb5c0d00144cee"></a>

```c
#define BEE_UART1_TX 5
```

相关声明：[BEE_UART1_TX](#acf789455a751381f67bb5c0d00144cee)。

`UART1_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a360f04b358a9569940a03d0d19397df3"></a>

```c
#define BEE_UART1_RX 6
```

相关声明：[BEE_UART1_RX](#a360f04b358a9569940a03d0d19397df3)。

`UART1_RX` 引脚复用功能（Pinmux Function）。

<a id="r_ae1a337884566b230fb35533cb45f83ba"></a>

```c
#define BEE_UART1_CTS 7
```

相关声明：[BEE_UART1_CTS](#ae1a337884566b230fb35533cb45f83ba)。

`UART1_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_abe24c85e1d8f04d29607669efb795a85"></a>

```c
#define BEE_UART1_RTS 8
```

相关声明：[BEE_UART1_RTS](#abe24c85e1d8f04d29607669efb795a85)。

`UART1_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_a64c1b3bb3de7cbf46f5e15da73dd6af9"></a>

```c
#define BEE_UART2_TX 9
```

相关声明：[BEE_UART2_TX](#a64c1b3bb3de7cbf46f5e15da73dd6af9)。

`UART2_TX` 引脚复用功能（Pinmux Function）。

<a id="r_ac0e9e9aae4c3a7542a4283525446151a"></a>

```c
#define BEE_UART2_RX 10
```

相关声明：[BEE_UART2_RX](#ac0e9e9aae4c3a7542a4283525446151a)。

`UART2_RX` 引脚复用功能（Pinmux Function）。

<a id="r_a7efdd2cc3bd5b3e9686ec52348490a21"></a>

```c
#define BEE_UART2_CTS 11
```

相关声明：[BEE_UART2_CTS](#a7efdd2cc3bd5b3e9686ec52348490a21)。

`UART2_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a9c3102f61a4ea7d46a3b5bb363d8089d"></a>

```c
#define BEE_UART2_RTS 12
```

相关声明：[BEE_UART2_RTS](#a9c3102f61a4ea7d46a3b5bb363d8089d)。

`UART2_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_ac3f36cfbd9420ac239e8d339bc239ac9"></a>

```c
#define BEE_UART3_TX 13
```

相关声明：[BEE_UART3_TX](#ac3f36cfbd9420ac239e8d339bc239ac9)。

`UART3_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a8bb702c55c1a5de54a998647c92006b4"></a>

```c
#define BEE_UART3_RX 14
```

相关声明：[BEE_UART3_RX](#a8bb702c55c1a5de54a998647c92006b4)。

`UART3_RX` 引脚复用功能（Pinmux Function）。

<a id="r_a63c515f54930b48ffc8838ab6973220e"></a>

```c
#define BEE_UART3_CTS 15
```

相关声明：[BEE_UART3_CTS](#a63c515f54930b48ffc8838ab6973220e)。

`UART3_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a8bce684ba830b2ebff4ddd33139d1238"></a>

```c
#define BEE_UART3_RTS 16
```

相关声明：[BEE_UART3_RTS](#a8bce684ba830b2ebff4ddd33139d1238)。

`UART3_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_a26c87862eb77530af5058bb5710b434d"></a>

```c
#define BEE_UART4_TX 17
```

相关声明：[BEE_UART4_TX](#a26c87862eb77530af5058bb5710b434d)。

`UART4_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a2893d6c80e812e809b2d4c8852bbc85c"></a>

```c
#define BEE_UART4_RX 18
```

相关声明：[BEE_UART4_RX](#a2893d6c80e812e809b2d4c8852bbc85c)。

`UART4_RX` 引脚复用功能（Pinmux Function）。

<a id="r_a337d0bc0bfc8512081a1b2e59ac832bb"></a>

```c
#define BEE_UART4_CTS 19
```

相关声明：[BEE_UART4_CTS](#a337d0bc0bfc8512081a1b2e59ac832bb)。

`UART4_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a24ec0ff6ae46444b58d43817b320769c"></a>

```c
#define BEE_UART4_RTS 20
```

相关声明：[BEE_UART4_RTS](#a24ec0ff6ae46444b58d43817b320769c)。

`UART4_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_ab925e0d948107471ab1ba3908de5d105"></a>

```c
#define BEE_UART5_TX 21
```

相关声明：[BEE_UART5_TX](#ab925e0d948107471ab1ba3908de5d105)。

`UART5_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a0f6b987c94ad3bdd648e3996ef632eea"></a>

```c
#define BEE_UART5_RX 22
```

相关声明：[BEE_UART5_RX](#a0f6b987c94ad3bdd648e3996ef632eea)。

`UART5_RX` 引脚复用功能（Pinmux Function）。

<a id="r_aaf8ae6ec44aff2fdfc06835b904e2fb9"></a>

```c
#define BEE_UART5_CTS 23
```

相关声明：[BEE_UART5_CTS](#aaf8ae6ec44aff2fdfc06835b904e2fb9)。

`UART5_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a4ed28e6a66dfb4cf545d51081c163609"></a>

```c
#define BEE_UART5_RTS 24
```

相关声明：[BEE_UART5_RTS](#a4ed28e6a66dfb4cf545d51081c163609)。

`UART5_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_ae0341d05951da84bd30617c9dc341628"></a>

```c
#define BEE_I2C0_CLK 29
```

相关声明：[BEE_I2C0_CLK](#ae0341d05951da84bd30617c9dc341628)。

`I2C0_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_abf8d90380239e366fb63fd777fb25075"></a>

```c
#define BEE_I2C0_DAT 30
```

相关声明：[BEE_I2C0_DAT](#abf8d90380239e366fb63fd777fb25075)。

`I2C0_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_ad89dd6f55609883daef7915f779b193f"></a>

```c
#define BEE_I2C1_CLK 31
```

相关声明：[BEE_I2C1_CLK](#ad89dd6f55609883daef7915f779b193f)。

`I2C1_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_aa70f0eb0a8271e9e027a7307e9c2f203"></a>

```c
#define BEE_I2C1_DAT 32
```

相关声明：[BEE_I2C1_DAT](#aa70f0eb0a8271e9e027a7307e9c2f203)。

`I2C1_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_aa6ed0aa3c48770881ba917e57dc08df2"></a>

```c
#define BEE_I2C2_CLK 33
```

相关声明：[BEE_I2C2_CLK](#aa6ed0aa3c48770881ba917e57dc08df2)。

`I2C2_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a1252547d18e156d80d5250b328203c2f"></a>

```c
#define BEE_I2C2_DAT 34
```

相关声明：[BEE_I2C2_DAT](#a1252547d18e156d80d5250b328203c2f)。

`I2C2_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_a0f6888bef3c7f11e70e8c07267fa2e1f"></a>

```c
#define BEE_I2C3_CLK 35
```

相关声明：[BEE_I2C3_CLK](#a0f6888bef3c7f11e70e8c07267fa2e1f)。

`I2C3_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_af1c9332588450b35182481ec351e5455"></a>

```c
#define BEE_I2C3_DAT 36
```

相关声明：[BEE_I2C3_DAT](#af1c9332588450b35182481ec351e5455)。

`I2C3_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_ab0446a74b1486abd14de4fd0200ea74f"></a>

```c
#define BEE_SPI0_CLK_MASTER 37
```

相关声明：[BEE_SPI0_CLK_MASTER](#ab0446a74b1486abd14de4fd0200ea74f)。

`SPI0_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ae4d7727fa011b264c2262f8a93286b79"></a>

```c
#define BEE_SPI0_MO_MASTER 38
```

相关声明：[BEE_SPI0_MO_MASTER](#ae4d7727fa011b264c2262f8a93286b79)。

`SPI0_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ad0da29a2b105520d4b082c3995738a7c"></a>

```c
#define BEE_SPI0_MI_MASTER 39
```

相关声明：[BEE_SPI0_MI_MASTER](#ad0da29a2b105520d4b082c3995738a7c)。

`SPI0_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_adad5ada055c3c4d60d2600b1fe3fa1c5"></a>

```c
#define BEE_SPI0_CSN_0_MASTER 40
```

相关声明：[BEE_SPI0_CSN_0_MASTER](#adad5ada055c3c4d60d2600b1fe3fa1c5)。

`SPI0_CSN_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a4ba241d2467358de0b0ba6ab90486053"></a>

```c
#define BEE_SPI0_CSN_1_MASTER 41
```

相关声明：[BEE_SPI0_CSN_1_MASTER](#a4ba241d2467358de0b0ba6ab90486053)。

`SPI0_CSN_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ac2cb7c98322526828aac27e9f07b60f2"></a>

```c
#define BEE_SPI0_CSN_2_MASTER 42
```

相关声明：[BEE_SPI0_CSN_2_MASTER](#ac2cb7c98322526828aac27e9f07b60f2)。

`SPI0_CSN_2_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a3f0252d61a75a19686b709fc0f9626a1"></a>

```c
#define BEE_SPI0_CSN_0_SLAVE 43
```

相关声明：[BEE_SPI0_CSN_0_SLAVE](#a3f0252d61a75a19686b709fc0f9626a1)。

`SPI0_CSN_0_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_aa74d6d5790ee4b6c3804612d13ac2b5b"></a>

```c
#define BEE_SPI0_CLK_SLAVE 44
```

相关声明：[BEE_SPI0_CLK_SLAVE](#aa74d6d5790ee4b6c3804612d13ac2b5b)。

`SPI0_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ad8b8f9abd4e3a9f468621a1bcebc26c5"></a>

```c
#define BEE_SPI0_SO_SLAVE 45
```

相关声明：[BEE_SPI0_SO_SLAVE](#ad8b8f9abd4e3a9f468621a1bcebc26c5)。

`SPI0_SO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a42c6b4ef4945aa8dacaf653acffae16f"></a>

```c
#define BEE_SPI0_SI_SLAVE 46
```

相关声明：[BEE_SPI0_SI_SLAVE](#a42c6b4ef4945aa8dacaf653acffae16f)。

`SPI0_SI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a0452a4a0d75d2f3eba6dac55bd4d209c"></a>

```c
#define BEE_SPI1_CLK_MASTER 47
```

相关声明：[BEE_SPI1_CLK_MASTER](#a0452a4a0d75d2f3eba6dac55bd4d209c)。

`SPI1_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a113270bda7f1996417ae86e9d59f7c6e"></a>

```c
#define BEE_SPI1_MO_MASTER 48
```

相关声明：[BEE_SPI1_MO_MASTER](#a113270bda7f1996417ae86e9d59f7c6e)。

`SPI1_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a8064446640a0d1ff045af352b0da6670"></a>

```c
#define BEE_SPI1_MI_MASTER 49
```

相关声明：[BEE_SPI1_MI_MASTER](#a8064446640a0d1ff045af352b0da6670)。

`SPI1_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ad13d417d2d2a380af4b615291036785f"></a>

```c
#define BEE_SPI1_CSN_0_MASTER 50
```

相关声明：[BEE_SPI1_CSN_0_MASTER](#ad13d417d2d2a380af4b615291036785f)。

`SPI1_CSN_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_aec9bc8d94e3f80753439f36db561936f"></a>

```c
#define BEE_SPI1_CSN_1_MASTER 51
```

相关声明：[BEE_SPI1_CSN_1_MASTER](#aec9bc8d94e3f80753439f36db561936f)。

`SPI1_CSN_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ac5545ab44020d7ce32146251a5306f01"></a>

```c
#define BEE_SPI1_CSN_2_MASTER 52
```

相关声明：[BEE_SPI1_CSN_2_MASTER](#ac5545ab44020d7ce32146251a5306f01)。

`SPI1_CSN_2_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a7051bd1175f9fa98e28c31da2e3f82bf"></a>

```c
#define BEE_SPI2W_DATA 53
```

相关声明：[BEE_SPI2W_DATA](#a7051bd1175f9fa98e28c31da2e3f82bf)。

`SPI2W_DATA` 引脚复用功能（Pinmux Function）。

<a id="r_a3c97c43a62a7d802368350c585342a3d"></a>

```c
#define BEE_SPI2W_CLK 54
```

相关声明：[BEE_SPI2W_CLK](#a3c97c43a62a7d802368350c585342a3d)。

`SPI2W_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_abf0b517038a65b54ce1fe74e354c8242"></a>

```c
#define BEE_SPI2W_CS 55
```

相关声明：[BEE_SPI2W_CS](#abf0b517038a65b54ce1fe74e354c8242)。

`SPI2W_CS` 引脚复用功能（Pinmux Function）。

<a id="r_a317e02b0cb9050e461acf3c246be9af4"></a>

```c
#define BEE_ENPWM0_P 65
```

相关声明：[BEE_ENPWM0_P](#a317e02b0cb9050e461acf3c246be9af4)。

`ENPWM0_P` 引脚复用功能（Pinmux Function）。

<a id="r_a70f463ef325204a7874ade112c0993b3"></a>

```c
#define BEE_ENPWM0_N 66
```

相关声明：[BEE_ENPWM0_N](#a70f463ef325204a7874ade112c0993b3)。

`ENPWM0_N` 引脚复用功能（Pinmux Function）。

<a id="r_a5ba16fa5c3475f4714377bd100b10e7b"></a>

```c
#define BEE_ENPWM1_P 67
```

相关声明：[BEE_ENPWM1_P](#a5ba16fa5c3475f4714377bd100b10e7b)。

`ENPWM1_P` 引脚复用功能（Pinmux Function）。

<a id="r_a6aedfb25152fa14e489451f4678a453e"></a>

```c
#define BEE_ENPWM1_N 68
```

相关声明：[BEE_ENPWM1_N](#a6aedfb25152fa14e489451f4678a453e)。

`ENPWM1_N` 引脚复用功能（Pinmux Function）。

<a id="r_a8a5f812e1c4a764f6b549daba4057b43"></a>

```c
#define BEE_ENPWM2_P 69
```

相关声明：[BEE_ENPWM2_P](#a8a5f812e1c4a764f6b549daba4057b43)。

`ENPWM2_P` 引脚复用功能（Pinmux Function）。

<a id="r_ae781b89eaf360564a48f1f2bc203e088"></a>

```c
#define BEE_ENPWM2_N 70
```

相关声明：[BEE_ENPWM2_N](#ae781b89eaf360564a48f1f2bc203e088)。

`ENPWM2_N` 引脚复用功能（Pinmux Function）。

<a id="r_abc0d7be51b69c2b6feb7933824d6a7ba"></a>

```c
#define BEE_ENPWM3_P 71
```

相关声明：[BEE_ENPWM3_P](#abc0d7be51b69c2b6feb7933824d6a7ba)。

`ENPWM3_P` 引脚复用功能（Pinmux Function）。

<a id="r_ac344c7a2b0b5db363875d9439cd7bd22"></a>

```c
#define BEE_ENPWM3_N 72
```

相关声明：[BEE_ENPWM3_N](#ac344c7a2b0b5db363875d9439cd7bd22)。

`ENPWM3_N` 引脚复用功能（Pinmux Function）。

<a id="r_a8a0647f117f2ed3706b555900eb2dc72"></a>

```c
#define BEE_TIMER_PWM2 83
```

相关声明：[BEE_TIMER_PWM2](#a8a0647f117f2ed3706b555900eb2dc72)。

`TIMER_PWM2` 引脚复用功能（Pinmux Function）。

<a id="r_a57bdd180f5ca3fee9e5ca3c8fb9243b3"></a>

```c
#define BEE_TIMER_PWM3 84
```

相关声明：[BEE_TIMER_PWM3](#a57bdd180f5ca3fee9e5ca3c8fb9243b3)。

`TIMER_PWM3` 引脚复用功能（Pinmux Function）。

<a id="r_a33a86943fb382af407f1cc041b008fbe"></a>

```c
#define BEE_ISO7816_RST 85
```

相关声明：[BEE_ISO7816_RST](#a33a86943fb382af407f1cc041b008fbe)。

`ISO7816_RST` 引脚复用功能（Pinmux Function）。

<a id="r_ac011f9b7965756997354ea86afb50678"></a>

```c
#define BEE_ISO7816_CLK 86
```

相关声明：[BEE_ISO7816_CLK](#ac011f9b7965756997354ea86afb50678)。

`ISO7816_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a35492a7221ec181c25c3ac234b711509"></a>

```c
#define BEE_ISO7816_IO 87
```

相关声明：[BEE_ISO7816_IO](#a35492a7221ec181c25c3ac234b711509)。

`ISO7816_IO` 引脚复用功能（Pinmux Function）。

<a id="r_a438124ea813bc335d07ec29dae9f4215"></a>

```c
#define BEE_ISO7816_VCC_EN 88
```

相关声明：[BEE_ISO7816_VCC_EN](#a438124ea813bc335d07ec29dae9f4215)。

`ISO7816_VCC_EN` 引脚复用功能（Pinmux Function）。

<a id="r_a93f3d11e8a6c9fd056bc4e6a2f156989"></a>

```c
#define BEE_DWGPIO 89
```

相关声明：[BEE_DWGPIO](#a93f3d11e8a6c9fd056bc4e6a2f156989)。

`DWGPIO` 引脚复用功能（Pinmux Function）。

<a id="r_aa03d3f61b2ad1379c04e21e409797781"></a>

```c
#define BEE_IRDA_TX 90
```

相关声明：[BEE_IRDA_TX](#aa03d3f61b2ad1379c04e21e409797781)。

`IRDA_TX` 引脚复用功能（Pinmux Function）。

<a id="r_ad5404068fcc7bf2e2207f151d7baacc3"></a>

```c
#define BEE_IRDA_RX 91
```

相关声明：[BEE_IRDA_RX](#ad5404068fcc7bf2e2207f151d7baacc3)。

`IRDA_RX` 引脚复用功能（Pinmux Function）。

<a id="r_aafdc6f1211c064bf41d81e498019c11b"></a>

```c
#define BEE_TIMER_PWM4 92
```

相关声明：[BEE_TIMER_PWM4](#aafdc6f1211c064bf41d81e498019c11b)。

`TIMER_PWM4` 引脚复用功能（Pinmux Function）。

<a id="r_a357dc7d8566f63bed51117b6d13760b2"></a>

```c
#define BEE_TIMER_PWM5 93
```

相关声明：[BEE_TIMER_PWM5](#a357dc7d8566f63bed51117b6d13760b2)。

`TIMER_PWM5` 引脚复用功能（Pinmux Function）。

<a id="r_a432deff0be5af291d7ba5c6085a95395"></a>

```c
#define BEE_TIMER_PWM6 94
```

相关声明：[BEE_TIMER_PWM6](#a432deff0be5af291d7ba5c6085a95395)。

`TIMER_PWM6` 引脚复用功能（Pinmux Function）。

<a id="r_a0e72bc44c574f233b01b103a91224f77"></a>

```c
#define BEE_TIMER_PWM7 95
```

相关声明：[BEE_TIMER_PWM7](#a0e72bc44c574f233b01b103a91224f77)。

`TIMER_PWM7` 引脚复用功能（Pinmux Function）。

<a id="r_a53a225ad51952fe99a3b07fccd2eef16"></a>

```c
#define BEE_TIMER_PWM2_P 96
```

相关声明：[BEE_TIMER_PWM2_P](#a53a225ad51952fe99a3b07fccd2eef16)。

`TIMER_PWM2_P` 引脚复用功能（Pinmux Function）。

<a id="r_adf2187d6150b328d2b54e6d0cdf80e60"></a>

```c
#define BEE_TIMER_PWM2_N 97
```

相关声明：[BEE_TIMER_PWM2_N](#adf2187d6150b328d2b54e6d0cdf80e60)。

`TIMER_PWM2_N` 引脚复用功能（Pinmux Function）。

<a id="r_abf3272d4fda4b0b1653c22a4009fe232"></a>

```c
#define BEE_TIMER_PWM3_P 98
```

相关声明：[BEE_TIMER_PWM3_P](#abf3272d4fda4b0b1653c22a4009fe232)。

`TIMER_PWM3_P` 引脚复用功能（Pinmux Function）。

<a id="r_ae1d65057952dbbfb086c375d8d8b46d2"></a>

```c
#define BEE_TIMER_PWM3_N 99
```

相关声明：[BEE_TIMER_PWM3_N](#ae1d65057952dbbfb086c375d8d8b46d2)。

`TIMER_PWM3_N` 引脚复用功能（Pinmux Function）。

<a id="r_a5feafd3851cdad2ae95d13da759f846a"></a>

```c
#define BEE_KEY_COL_0 100
```

相关声明：[BEE_KEY_COL_0](#a5feafd3851cdad2ae95d13da759f846a)。

`KEY_COL_0` 引脚复用功能（Pinmux Function）。

<a id="r_a041f3ef212cd3b5632534b861cbc261a"></a>

```c
#define BEE_KEY_COL_1 101
```

相关声明：[BEE_KEY_COL_1](#a041f3ef212cd3b5632534b861cbc261a)。

`KEY_COL_1` 引脚复用功能（Pinmux Function）。

<a id="r_a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2"></a>

```c
#define BEE_KEY_COL_2 102
```

相关声明：[BEE_KEY_COL_2](#a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2)。

`KEY_COL_2` 引脚复用功能（Pinmux Function）。

<a id="r_a6faea0c7d7cfbc3557937914a8f3a3b5"></a>

```c
#define BEE_KEY_COL_3 103
```

相关声明：[BEE_KEY_COL_3](#a6faea0c7d7cfbc3557937914a8f3a3b5)。

`KEY_COL_3` 引脚复用功能（Pinmux Function）。

<a id="r_ad8b490ea83a896b7c702161613e8351d"></a>

```c
#define BEE_KEY_COL_4 104
```

相关声明：[BEE_KEY_COL_4](#ad8b490ea83a896b7c702161613e8351d)。

`KEY_COL_4` 引脚复用功能（Pinmux Function）。

<a id="r_afbb2d553138a1242007d6339631adb26"></a>

```c
#define BEE_KEY_COL_5 105
```

相关声明：[BEE_KEY_COL_5](#afbb2d553138a1242007d6339631adb26)。

`KEY_COL_5` 引脚复用功能（Pinmux Function）。

<a id="r_ac549db15241e4a3344a387b5b2188970"></a>

```c
#define BEE_KEY_COL_6 106
```

相关声明：[BEE_KEY_COL_6](#ac549db15241e4a3344a387b5b2188970)。

`KEY_COL_6` 引脚复用功能（Pinmux Function）。

<a id="r_aa61ab3cf42f2f48afe802d7cb12f222a"></a>

```c
#define BEE_KEY_COL_7 107
```

相关声明：[BEE_KEY_COL_7](#aa61ab3cf42f2f48afe802d7cb12f222a)。

`KEY_COL_7` 引脚复用功能（Pinmux Function）。

<a id="r_a5d28d0d40e6334592b08698a3f9e0da8"></a>

```c
#define BEE_KEY_COL_8 108
```

相关声明：[BEE_KEY_COL_8](#a5d28d0d40e6334592b08698a3f9e0da8)。

`KEY_COL_8` 引脚复用功能（Pinmux Function）。

<a id="r_ad2c88795b1b458608caa083d469ee86e"></a>

```c
#define BEE_KEY_COL_9 109
```

相关声明：[BEE_KEY_COL_9](#ad2c88795b1b458608caa083d469ee86e)。

`KEY_COL_9` 引脚复用功能（Pinmux Function）。

<a id="r_a431bd45fe23862cc55fa544d684b92d6"></a>

```c
#define BEE_KEY_COL_10 110
```

相关声明：[BEE_KEY_COL_10](#a431bd45fe23862cc55fa544d684b92d6)。

`KEY_COL_10` 引脚复用功能（Pinmux Function）。

<a id="r_a7164c3dc3423f443cd3e39875702f200"></a>

```c
#define BEE_KEY_COL_11 111
```

相关声明：[BEE_KEY_COL_11](#a7164c3dc3423f443cd3e39875702f200)。

`KEY_COL_11` 引脚复用功能（Pinmux Function）。

<a id="r_a02b8793d7bbde10e6d31f380f594758d"></a>

```c
#define BEE_KEY_COL_12 112
```

相关声明：[BEE_KEY_COL_12](#a02b8793d7bbde10e6d31f380f594758d)。

`KEY_COL_12` 引脚复用功能（Pinmux Function）。

<a id="r_a1493d93c12d93ca2e0f6dc267651106b"></a>

```c
#define BEE_KEY_COL_13 113
```

相关声明：[BEE_KEY_COL_13](#a1493d93c12d93ca2e0f6dc267651106b)。

`KEY_COL_13` 引脚复用功能（Pinmux Function）。

<a id="r_a60a32dd7c97e11c25cfec77882914300"></a>

```c
#define BEE_KEY_COL_14 114
```

相关声明：[BEE_KEY_COL_14](#a60a32dd7c97e11c25cfec77882914300)。

`KEY_COL_14` 引脚复用功能（Pinmux Function）。

<a id="r_a689da1d4cb37dbb30ceb751a0fa85b33"></a>

```c
#define BEE_KEY_COL_15 115
```

相关声明：[BEE_KEY_COL_15](#a689da1d4cb37dbb30ceb751a0fa85b33)。

`KEY_COL_15` 引脚复用功能（Pinmux Function）。

<a id="r_a369b59d63cc72309486ad36e29b8c6af"></a>

```c
#define BEE_KEY_COL_16 116
```

相关声明：[BEE_KEY_COL_16](#a369b59d63cc72309486ad36e29b8c6af)。

`KEY_COL_16` 引脚复用功能（Pinmux Function）。

<a id="r_a719bdfcc5efd46dcc6dd7c841c0447d4"></a>

```c
#define BEE_KEY_COL_17 117
```

相关声明：[BEE_KEY_COL_17](#a719bdfcc5efd46dcc6dd7c841c0447d4)。

`KEY_COL_17` 引脚复用功能（Pinmux Function）。

<a id="r_a53aebd67028abe2a744e11d781ca183f"></a>

```c
#define BEE_KEY_COL_18 118
```

相关声明：[BEE_KEY_COL_18](#a53aebd67028abe2a744e11d781ca183f)。

`KEY_COL_18` 引脚复用功能（Pinmux Function）。

<a id="r_af444884011ac39c3dcf213a22259c953"></a>

```c
#define BEE_KEY_COL_19 119
```

相关声明：[BEE_KEY_COL_19](#af444884011ac39c3dcf213a22259c953)。

`KEY_COL_19` 引脚复用功能（Pinmux Function）。

<a id="r_af82f5da17eada898f2dec8de92e603b0"></a>

```c
#define BEE_KEY_ROW_0 120
```

相关声明：[BEE_KEY_ROW_0](#af82f5da17eada898f2dec8de92e603b0)。

`KEY_ROW_0` 引脚复用功能（Pinmux Function）。

<a id="r_a24e82e85a07c80d7e390185f67726756"></a>

```c
#define BEE_KEY_ROW_1 121
```

相关声明：[BEE_KEY_ROW_1](#a24e82e85a07c80d7e390185f67726756)。

`KEY_ROW_1` 引脚复用功能（Pinmux Function）。

<a id="r_a695da19fd7bc007959fe2ce9f3882939"></a>

```c
#define BEE_KEY_ROW_2 122
```

相关声明：[BEE_KEY_ROW_2](#a695da19fd7bc007959fe2ce9f3882939)。

`KEY_ROW_2` 引脚复用功能（Pinmux Function）。

<a id="r_a3920941b7c17c1eb9df377230ae0e3d7"></a>

```c
#define BEE_KEY_ROW_3 123
```

相关声明：[BEE_KEY_ROW_3](#a3920941b7c17c1eb9df377230ae0e3d7)。

`KEY_ROW_3` 引脚复用功能（Pinmux Function）。

<a id="r_a94ce3c3c0775437059fe8d48ca1ae63d"></a>

```c
#define BEE_KEY_ROW_4 124
```

相关声明：[BEE_KEY_ROW_4](#a94ce3c3c0775437059fe8d48ca1ae63d)。

`KEY_ROW_4` 引脚复用功能（Pinmux Function）。

<a id="r_aebdb52372b88e9aa5d7173104f8088c7"></a>

```c
#define BEE_KEY_ROW_5 125
```

相关声明：[BEE_KEY_ROW_5](#aebdb52372b88e9aa5d7173104f8088c7)。

`KEY_ROW_5` 引脚复用功能（Pinmux Function）。

<a id="r_a6535c3d5752c54dd36ff7a138cb70b5c"></a>

```c
#define BEE_KEY_ROW_6 126
```

相关声明：[BEE_KEY_ROW_6](#a6535c3d5752c54dd36ff7a138cb70b5c)。

`KEY_ROW_6` 引脚复用功能（Pinmux Function）。

<a id="r_a4762128bf6b6e86a17b3c8c76ff2fc88"></a>

```c
#define BEE_KEY_ROW_7 127
```

相关声明：[BEE_KEY_ROW_7](#a4762128bf6b6e86a17b3c8c76ff2fc88)。

`KEY_ROW_7` 引脚复用功能（Pinmux Function）。

<a id="r_abbf110abd0ae22bb4767f28fe5901242"></a>

```c
#define BEE_KEY_ROW_8 128
```

相关声明：[BEE_KEY_ROW_8](#abbf110abd0ae22bb4767f28fe5901242)。

`KEY_ROW_8` 引脚复用功能（Pinmux Function）。

<a id="r_a681b30410bb04208c02a53f158dbedfb"></a>

```c
#define BEE_KEY_ROW_9 129
```

相关声明：[BEE_KEY_ROW_9](#a681b30410bb04208c02a53f158dbedfb)。

`KEY_ROW_9` 引脚复用功能（Pinmux Function）。

<a id="r_a8f0c299784cb107d46fdbcd5494ae2f0"></a>

```c
#define BEE_KEY_ROW_10 130
```

相关声明：[BEE_KEY_ROW_10](#a8f0c299784cb107d46fdbcd5494ae2f0)。

`KEY_ROW_10` 引脚复用功能（Pinmux Function）。

<a id="r_a2386911ec69b7416028fab5537243bee"></a>

```c
#define BEE_KEY_ROW_11 131
```

相关声明：[BEE_KEY_ROW_11](#a2386911ec69b7416028fab5537243bee)。

`KEY_ROW_11` 引脚复用功能（Pinmux Function）。

<a id="r_a5c05c2a5a36182329825a24c574d594e"></a>

```c
#define BEE_KM4_CLK_DIV_4 138
```

相关声明：[BEE_KM4_CLK_DIV_4](#a5c05c2a5a36182329825a24c574d594e)。

`KM4_CLK_DIV_4` 引脚复用功能（Pinmux Function）。

<a id="r_a08612d2752471ed4ed20aff687d20d18"></a>

```c
#define BEE_CARD_DETECT_N_0 147
```

相关声明：[BEE_CARD_DETECT_N_0](#a08612d2752471ed4ed20aff687d20d18)。

`CARD_DETECT_N_0` 引脚复用功能（Pinmux Function）。

<a id="r_ac08f855050ffa3b42fd846fec5db4fbd"></a>

```c
#define BEE_BIU_VOLT_REG_0 148
```

相关声明：[BEE_BIU_VOLT_REG_0](#ac08f855050ffa3b42fd846fec5db4fbd)。

`BIU_VOLT_REG_0` 引脚复用功能（Pinmux Function）。

<a id="r_aad1e43c193aa44b6f2301dbafe13ea92"></a>

```c
#define BEE_BACK_END_POWER_0 149
```

相关声明：[BEE_BACK_END_POWER_0](#aad1e43c193aa44b6f2301dbafe13ea92)。

`BACK_END_POWER_0` 引脚复用功能（Pinmux Function）。

<a id="r_af3cf294ea961f98b078c8ad034fae03d"></a>

```c
#define BEE_CARD_INT_N_SDHC_0 150
```

相关声明：[BEE_CARD_INT_N_SDHC_0](#af3cf294ea961f98b078c8ad034fae03d)。

`CARD_INT_N_SDHC_0` 引脚复用功能（Pinmux Function）。

<a id="r_ac5103fd9a770f992502e72e7076c46ce"></a>

```c
#define BEE_A2C_TX 155
```

相关声明：[BEE_A2C_TX](#ac5103fd9a770f992502e72e7076c46ce)。

`A2C_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a1383cae9e4cf0048180c741624c6909b"></a>

```c
#define BEE_A2C_RX 156
```

相关声明：[BEE_A2C_RX](#a1383cae9e4cf0048180c741624c6909b)。

`A2C_RX` 引脚复用功能（Pinmux Function）。

<a id="r_a4224637824110a64477a8d8890de4533"></a>

```c
#define BEE_LRC_SPORT1 157
```

相关声明：[BEE_LRC_SPORT1](#a4224637824110a64477a8d8890de4533)。

`LRC_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="r_a62e4dd6b6605747655b67407a1f08977"></a>

```c
#define BEE_BCLK_SPORT1 158
```

相关声明：[BEE_BCLK_SPORT1](#a62e4dd6b6605747655b67407a1f08977)。

`BCLK_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="r_a98522c73d9f29a0a43c37a94eea377e0"></a>

```c
#define BEE_ADCDAT_SPORT1 159
```

相关声明：[BEE_ADCDAT_SPORT1](#a98522c73d9f29a0a43c37a94eea377e0)。

`ADCDAT_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="r_a382b0d00ac01e3bff5aa95e1fe1d4b35"></a>

```c
#define BEE_DACDAT_SPORT1 160
```

相关声明：[BEE_DACDAT_SPORT1](#a382b0d00ac01e3bff5aa95e1fe1d4b35)。

`DACDAT_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="r_a49516c6243aed5817ba2ae4d6744687b"></a>

```c
#define BEE_DMIC1_CLK 162
```

相关声明：[BEE_DMIC1_CLK](#a49516c6243aed5817ba2ae4d6744687b)。

`DMIC1_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a8d6a69a1e3591004efb445bd9b3edfb3"></a>

```c
#define BEE_DMIC1_DAT 163
```

相关声明：[BEE_DMIC1_DAT](#a8d6a69a1e3591004efb445bd9b3edfb3)。

`DMIC1_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_a644fe132bc7a607b715744ae214635af"></a>

```c
#define BEE_LRC_I_CODEC_SLAVE 164
```

相关声明：[BEE_LRC_I_CODEC_SLAVE](#a644fe132bc7a607b715744ae214635af)。

`LRC_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a912613b40d5c8101fb80ef546259718c"></a>

```c
#define BEE_BCLK_I_CODEC_SLAVE 165
```

相关声明：[BEE_BCLK_I_CODEC_SLAVE](#a912613b40d5c8101fb80ef546259718c)。

`BCLK_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a4210b1402742ed6b988925e93b2fb875"></a>

```c
#define BEE_SDI_CODEC_SLAVE 166
```

相关声明：[BEE_SDI_CODEC_SLAVE](#a4210b1402742ed6b988925e93b2fb875)。

`SDI_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ad8fb809d69f74a7d77283fb004d2f323"></a>

```c
#define BEE_SDO_CODEC_SLAVE 167
```

相关声明：[BEE_SDO_CODEC_SLAVE](#ad8fb809d69f74a7d77283fb004d2f323)。

`SDO_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a44044eb50520f7a0dbf83abe70dc2bc5"></a>

```c
#define BEE_LRC_SPORT0 172
```

相关声明：[BEE_LRC_SPORT0](#a44044eb50520f7a0dbf83abe70dc2bc5)。

`LRC_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_ae8c197cf5a76f0e30b400e4190fa3d60"></a>

```c
#define BEE_BCLK_SPORT0 173
```

相关声明：[BEE_BCLK_SPORT0](#ae8c197cf5a76f0e30b400e4190fa3d60)。

`BCLK_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_a0a8dabb3051d18f3b0c63485417bfafd"></a>

```c
#define BEE_ADCDAT_SPORT0 174
```

相关声明：[BEE_ADCDAT_SPORT0](#a0a8dabb3051d18f3b0c63485417bfafd)。

`ADCDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_a60cdc36815f5a5057025a7a4e70e202f"></a>

```c
#define BEE_DACDAT_SPORT0 175
```

相关声明：[BEE_DACDAT_SPORT0](#a60cdc36815f5a5057025a7a4e70e202f)。

`DACDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_ab37d4968f633e5d24d97fe14e6d87178"></a>

```c
#define BEE_MCLK_OUT 176
```

相关声明：[BEE_MCLK_OUT](#ab37d4968f633e5d24d97fe14e6d87178)。

`MCLK_OUT` 引脚复用功能（Pinmux Function）。

<a id="r_aa4987bc9633f726511372e806855bb80"></a>

```c
#define BEE_MCLK_IN 189
```

相关声明：[BEE_MCLK_IN](#aa4987bc9633f726511372e806855bb80)。

`MCLK_IN` 引脚复用功能（Pinmux Function）。

<a id="r_a953c02232ba2b750df5eb0a75e299d82"></a>

```c
#define BEE_LRC_RX_CODEC_SLAVE 190
```

相关声明：[BEE_LRC_RX_CODEC_SLAVE](#a953c02232ba2b750df5eb0a75e299d82)。

`LRC_RX_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ae32bad8399c8049ede9df9631f3cb1db"></a>

```c
#define BEE_LRC_RX_SPORT0 191
```

相关声明：[BEE_LRC_RX_SPORT0](#ae32bad8399c8049ede9df9631f3cb1db)。

`LRC_RX_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_aa570f23c69d3e493587d96ea5ca43f79"></a>

```c
#define BEE_LRC_RX_SPORT1 192
```

相关声明：[BEE_LRC_RX_SPORT1](#aa570f23c69d3e493587d96ea5ca43f79)。

`LRC_RX_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="r_a3160663a5d36928382923eed0c5cf444"></a>

```c
#define BEE_PDM_DATA 196
```

相关声明：[BEE_PDM_DATA](#a3160663a5d36928382923eed0c5cf444)。

`PDM_DATA` 引脚复用功能（Pinmux Function）。

<a id="r_a586c8e8e4924b2f6f389e36ac3143d94"></a>

```c
#define BEE_PDM_CLK 197
```

相关声明：[BEE_PDM_CLK](#a586c8e8e4924b2f6f389e36ac3143d94)。

`PDM_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a9b22ae740c4fd42a120729b44271d1b3"></a>

```c
#define BEE_I2S1_LRC_TX_SLAVE 198
```

相关声明：[BEE_I2S1_LRC_TX_SLAVE](#a9b22ae740c4fd42a120729b44271d1b3)。

`I2S1_LRC_TX_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a73f47af907185a22e8dc672ffa784f47"></a>

```c
#define BEE_I2S1_BCLK_SLAVE 199
```

相关声明：[BEE_I2S1_BCLK_SLAVE](#a73f47af907185a22e8dc672ffa784f47)。

`I2S1_BCLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a01c614617ff43310d68aeb0e03cb6e13"></a>

```c
#define BEE_I2S1_SDI_SLAVE 200
```

相关声明：[BEE_I2S1_SDI_SLAVE](#a01c614617ff43310d68aeb0e03cb6e13)。

`I2S1_SDI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_acdd059e8af73a680e06e15951e5a5210"></a>

```c
#define BEE_I2S1_SDO_SLAVE 201
```

相关声明：[BEE_I2S1_SDO_SLAVE](#acdd059e8af73a680e06e15951e5a5210)。

`I2S1_SDO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ac82e2f9e94e04b1f4d362ffbdec5e2d1"></a>

```c
#define BEE_I2S1_LRC_RX_SLAVE 202
```

相关声明：[BEE_I2S1_LRC_RX_SLAVE](#ac82e2f9e94e04b1f4d362ffbdec5e2d1)。

`I2S1_LRC_RX_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ab122a176b695a923610b8d090ade6430"></a>

```c
#define BEE_BT_COEX_I_0 216
```

相关声明：[BEE_BT_COEX_I_0](#ab122a176b695a923610b8d090ade6430)。

`BT_COEX_I_0` 引脚复用功能（Pinmux Function）。

<a id="r_af55b98947776718e3b45e3e4c1636baa"></a>

```c
#define BEE_BT_COEX_I_1 217
```

相关声明：[BEE_BT_COEX_I_1](#af55b98947776718e3b45e3e4c1636baa)。

`BT_COEX_I_1` 引脚复用功能（Pinmux Function）。

<a id="r_abc580ad83269067b32fb42a476ff1e3d"></a>

```c
#define BEE_BT_COEX_I_2 218
```

相关声明：[BEE_BT_COEX_I_2](#abc580ad83269067b32fb42a476ff1e3d)。

`BT_COEX_I_2` 引脚复用功能（Pinmux Function）。

<a id="r_aae8555c6b679f48d0dcba40191e77166"></a>

```c
#define BEE_BT_COEX_I_3 219
```

相关声明：[BEE_BT_COEX_I_3](#aae8555c6b679f48d0dcba40191e77166)。

`BT_COEX_I_3` 引脚复用功能（Pinmux Function）。

<a id="r_adf8796c519f840189f367e7acd9e1738"></a>

```c
#define BEE_BT_COEX_O_0 220
```

相关声明：[BEE_BT_COEX_O_0](#adf8796c519f840189f367e7acd9e1738)。

`BT_COEX_O_0` 引脚复用功能（Pinmux Function）。

<a id="r_ab67e3e28eda567571d3d7586e94e03da"></a>

```c
#define BEE_BT_COEX_O_1 221
```

相关声明：[BEE_BT_COEX_O_1](#ab67e3e28eda567571d3d7586e94e03da)。

`BT_COEX_O_1` 引脚复用功能（Pinmux Function）。

<a id="r_a4b24f9dbcd7d24128db569fb93d84eef"></a>

```c
#define BEE_BT_COEX_O_2 222
```

相关声明：[BEE_BT_COEX_O_2](#a4b24f9dbcd7d24128db569fb93d84eef)。

`BT_COEX_O_2` 引脚复用功能（Pinmux Function）。

<a id="r_a786a847e166079b62cb5862573c5aeee"></a>

```c
#define BEE_BT_COEX_O_3 223
```

相关声明：[BEE_BT_COEX_O_3](#a786a847e166079b62cb5862573c5aeee)。

`BT_COEX_O_3` 引脚复用功能（Pinmux Function）。

<a id="r_abcf72b3e409c194ba2d2173aa7cb41ab"></a>

```c
#define BEE_PTA_I2C_CLK_SLAVE 224
```

相关声明：[BEE_PTA_I2C_CLK_SLAVE](#abcf72b3e409c194ba2d2173aa7cb41ab)。

`PTA_I2C_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a9254d4dd1aa797f1590ef84c1cd07ed1"></a>

```c
#define BEE_PTA_I2C_DAT_SLAVE 225
```

相关声明：[BEE_PTA_I2C_DAT_SLAVE](#a9254d4dd1aa797f1590ef84c1cd07ed1)。

`PTA_I2C_DAT_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a2e6661f9ef9bb93179130a186653468a"></a>

```c
#define BEE_PTA_I2C_INT_OUT 226
```

相关声明：[BEE_PTA_I2C_INT_OUT](#a2e6661f9ef9bb93179130a186653468a)。

`PTA_I2C_INT_OUT` 引脚复用功能（Pinmux Function）。

<a id="r_a37c7aeafe54f05e6a267f9f16af25c0c"></a>

```c
#define BEE_EN_EXPA 227
```

相关声明：[BEE_EN_EXPA](#a37c7aeafe54f05e6a267f9f16af25c0c)。

`EN_EXPA` 引脚复用功能（Pinmux Function）。

<a id="r_a510878941f7e323fe7eee5bb1b743c3e"></a>

```c
#define BEE_EN_EXLNA 228
```

相关声明：[BEE_EN_EXLNA](#a510878941f7e323fe7eee5bb1b743c3e)。

`EN_EXLNA` 引脚复用功能（Pinmux Function）。

<a id="r_a2cf4e89770aa792414e33cbda60c3e88"></a>

```c
#define BEE_SEL_TPM_SW 229
```

相关声明：[BEE_SEL_TPM_SW](#a2cf4e89770aa792414e33cbda60c3e88)。

`SEL_TPM_SW` 引脚复用功能（Pinmux Function）。

<a id="r_a7efece011140a52385c5aabdfc9b941d"></a>

```c
#define BEE_SEL_TPM_N_SW 230
```

相关声明：[BEE_SEL_TPM_N_SW](#a7efece011140a52385c5aabdfc9b941d)。

`SEL_TPM_N_SW` 引脚复用功能（Pinmux Function）。

<a id="r_a630537cb405d771f9ca478ad702c15ff"></a>

```c
#define BEE_ANT_SW0 231
```

相关声明：[BEE_ANT_SW0](#a630537cb405d771f9ca478ad702c15ff)。

`ANT_SW0` 引脚复用功能（Pinmux Function）。

<a id="r_a7d7a7ceac66b6d65e0dd466da57c7432"></a>

```c
#define BEE_ANT_SW1 232
```

相关声明：[BEE_ANT_SW1](#a7d7a7ceac66b6d65e0dd466da57c7432)。

`ANT_SW1` 引脚复用功能（Pinmux Function）。

<a id="r_a210a42a9f7bf5862bc5efbd27d6304de"></a>

```c
#define BEE_ANT_SW2 233
```

相关声明：[BEE_ANT_SW2](#a210a42a9f7bf5862bc5efbd27d6304de)。

`ANT_SW2` 引脚复用功能（Pinmux Function）。

<a id="r_ae25e5f43db415c0ef27adcf3cbd38e79"></a>

```c
#define BEE_ANT_SW3 234
```

相关声明：[BEE_ANT_SW3](#ae25e5f43db415c0ef27adcf3cbd38e79)。

`ANT_SW3` 引脚复用功能（Pinmux Function）。

<a id="r_a0b8ab8e7f60c24a1955356e5c718751e"></a>

```c
#define BEE_ANT_SW4 235
```

相关声明：[BEE_ANT_SW4](#a0b8ab8e7f60c24a1955356e5c718751e)。

`ANT_SW4` 引脚复用功能（Pinmux Function）。

<a id="r_a67af09727ac50bf3a71459d892315723"></a>

```c
#define BEE_ANT_SW5 236
```

相关声明：[BEE_ANT_SW5](#a67af09727ac50bf3a71459d892315723)。

`ANT_SW5` 引脚复用功能（Pinmux Function）。

<a id="r_a9abd2808f59a043725e9b441ba0a7114"></a>

```c
#define BEE_PHY_GPIO_1 237
```

相关声明：[BEE_PHY_GPIO_1](#a9abd2808f59a043725e9b441ba0a7114)。

`PHY_GPIO_1` 引脚复用功能（Pinmux Function）。

<a id="r_a69b08b31593daf0fa4f5ee5e6e98c730"></a>

```c
#define BEE_PHY_GPIO_2 238
```

相关声明：[BEE_PHY_GPIO_2](#a69b08b31593daf0fa4f5ee5e6e98c730)。

`PHY_GPIO_2` 引脚复用功能（Pinmux Function）。

<a id="r_a7ff4bfbdc644a16d4ba216bb011199fb"></a>

```c
#define BEE_SLOW_DEBUG_MUX_1 239
```

相关声明：[BEE_SLOW_DEBUG_MUX_1](#a7ff4bfbdc644a16d4ba216bb011199fb)。

`SLOW_DEBUG_MUX_1` 引脚复用功能（Pinmux Function）。

<a id="r_a4d6e8a3787f0f21724b0ded1e0708929"></a>

```c
#define BEE_SLOW_DEBUG_MUX_2 240
```

相关声明：[BEE_SLOW_DEBUG_MUX_2](#a4d6e8a3787f0f21724b0ded1e0708929)。

`SLOW_DEBUG_MUX_2` 引脚复用功能（Pinmux Function）。

<a id="r_a21637864c0e3b586c21dca96c2691405"></a>

```c
#define BEE_TEST_MODE 246
```

相关声明：[BEE_TEST_MODE](#a21637864c0e3b586c21dca96c2691405)。

`TEST_MODE` 引脚复用功能（Pinmux Function）。

<a id="r_a69b18937baf0d37c1302b897a29d0f0d"></a>

```c
#define BEE_SWD_CLK 253
```

相关声明：[BEE_SWD_CLK](#a69b18937baf0d37c1302b897a29d0f0d)。

`SWD_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a890a338c14aef5eb8e25844201b0289d"></a>

```c
#define BEE_SWD_DIO 254
```

相关声明：[BEE_SWD_DIO](#a890a338c14aef5eb8e25844201b0289d)。

`SWD_DIO` 引脚复用功能（Pinmux Function）。

<a id="r_aa23ca1adf7da20c2163b2fd78548cc9b"></a>

```c
#define BEE_DIG_DEBUG 255
```

相关声明：[BEE_DIG_DEBUG](#aa23ca1adf7da20c2163b2fd78548cc9b)。

`DIG_DEBUG` 引脚复用功能（Pinmux Function）。

<a id="r_a57b4629fefc1551701f145558e57f8fa"></a>

```c
#define BEE_PINMUX_MAX (BEE_DIG_DEBUG + 1)
```

相关声明：[BEE_PINMUX_MAX](#a57b4629fefc1551701f145558e57f8fa)、[BEE_DIG_DEBUG](#aa23ca1adf7da20c2163b2fd78548cc9b)。

`PINMUX_MAX` 引脚复用功能（Pinmux Function）。

<a id="r_a2207ba441c0defde698d2d1a49cb744d"></a>

```c
#define BEE_SW_MODE (BEE_PINMUX_MAX + 1)
```

相关声明：[BEE_SW_MODE](#a2207ba441c0defde698d2d1a49cb744d)、[BEE_PINMUX_MAX](#a57b4629fefc1551701f145558e57f8fa)。

`SW_MODE` 引脚复用功能（Pinmux Function）。

<a id="r_a95eb489d18499ff7ce936149d65ff03e"></a>

```c
#define BEE_PWR_OFF (BEE_PINMUX_MAX + 2)
```

相关声明：[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)、[BEE_PINMUX_MAX](#a57b4629fefc1551701f145558e57f8fa)。

`PWR_OFF` 引脚复用功能（Pinmux Function）。

<a id="r_a8b07e848c32157c2674c5956a434e877"></a>

```c
#define BEE_SDHC0_CLK_P9_4 (BEE_PWR_OFF + 1)
```

相关声明：[BEE_SDHC0_CLK_P9_4](#a8b07e848c32157c2674c5956a434e877)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_CLK_P9_4` 引脚复用功能（Pinmux Function）。

<a id="r_af0fcff204155abd2033c588ccfcfd43b"></a>

```c
#define BEE_SDHC0_CMD_P9_3 (BEE_PWR_OFF + 2)
```

相关声明：[BEE_SDHC0_CMD_P9_3](#af0fcff204155abd2033c588ccfcfd43b)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_CMD_P9_3` 引脚复用功能（Pinmux Function）。

<a id="r_a640fef966ab3c588d8b8fe444bf02285"></a>

```c
#define BEE_SDHC0_D0_P10_0 (BEE_PWR_OFF + 3)
```

相关声明：[BEE_SDHC0_D0_P10_0](#a640fef966ab3c588d8b8fe444bf02285)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D0_P10_0` 引脚复用功能（Pinmux Function）。

<a id="r_adc5ed31e3bd280c426350a907e127566"></a>

```c
#define BEE_SDHC0_D1_P9_7 (BEE_PWR_OFF + 4)
```

相关声明：[BEE_SDHC0_D1_P9_7](#adc5ed31e3bd280c426350a907e127566)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D1_P9_7` 引脚复用功能（Pinmux Function）。

<a id="r_aafa319b5c0ea2be2a7504b92b01f9a44"></a>

```c
#define BEE_SDHC0_D2_P9_6 (BEE_PWR_OFF + 5)
```

相关声明：[BEE_SDHC0_D2_P9_6](#aafa319b5c0ea2be2a7504b92b01f9a44)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D2_P9_6` 引脚复用功能（Pinmux Function）。

<a id="r_a5bcbca477a418781525d2045f9fd2cb2"></a>

```c
#define BEE_SDHC0_D3_P9_5 (BEE_PWR_OFF + 6)
```

相关声明：[BEE_SDHC0_D3_P9_5](#a5bcbca477a418781525d2045f9fd2cb2)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D3_P9_5` 引脚复用功能（Pinmux Function）。

<a id="r_a676fbe46df77c712016ebf08684d19cc"></a>

```c
#define BEE_SDHC0_D4_P4_4 (BEE_PWR_OFF + 7)
```

相关声明：[BEE_SDHC0_D4_P4_4](#a676fbe46df77c712016ebf08684d19cc)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D4_P4_4` 引脚复用功能（Pinmux Function）。

<a id="r_a0df0871c36c2e9ca877a46915e6bed5e"></a>

```c
#define BEE_SDHC0_D5_P4_5 (BEE_PWR_OFF + 8)
```

相关声明：[BEE_SDHC0_D5_P4_5](#a0df0871c36c2e9ca877a46915e6bed5e)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D5_P4_5` 引脚复用功能（Pinmux Function）。

<a id="r_af1900d620d09dc71b54d5c51687e9e64"></a>

```c
#define BEE_SDHC0_D6_P4_6 (BEE_PWR_OFF + 9)
```

相关声明：[BEE_SDHC0_D6_P4_6](#af1900d620d09dc71b54d5c51687e9e64)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D6_P4_6` 引脚复用功能（Pinmux Function）。

<a id="r_aa2af9a8cb37d9556d9bbfe42f59dc66d"></a>

```c
#define BEE_SDHC0_D7_P4_7 (BEE_PWR_OFF + 10)
```

相关声明：[BEE_SDHC0_D7_P4_7](#aa2af9a8cb37d9556d9bbfe42f59dc66d)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC0_D7_P4_7` 引脚复用功能（Pinmux Function）。

<a id="r_a6a5932281e193bbccf9c4df49cd2cc80"></a>

```c
#define BEE_SDHC1_CLK_P9_4 (BEE_PWR_OFF + 11)
```

相关声明：[BEE_SDHC1_CLK_P9_4](#a6a5932281e193bbccf9c4df49cd2cc80)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_CLK_P9_4` 引脚复用功能（Pinmux Function）。

<a id="r_ac5b3ba6fc43f19b40316d8d90f822ea3"></a>

```c
#define BEE_SDHC1_CMD_P9_3 (BEE_PWR_OFF + 12)
```

相关声明：[BEE_SDHC1_CMD_P9_3](#ac5b3ba6fc43f19b40316d8d90f822ea3)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_CMD_P9_3` 引脚复用功能（Pinmux Function）。

<a id="r_a472f94e2e5faf5a32ddb2cdba00fe375"></a>

```c
#define BEE_SDHC1_D0_P10_0 (BEE_PWR_OFF + 13)
```

相关声明：[BEE_SDHC1_D0_P10_0](#a472f94e2e5faf5a32ddb2cdba00fe375)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D0_P10_0` 引脚复用功能（Pinmux Function）。

<a id="r_a378f1cf157c1fd2e3422b0875319c2ae"></a>

```c
#define BEE_SDHC1_D1_P9_7 (BEE_PWR_OFF + 14)
```

相关声明：[BEE_SDHC1_D1_P9_7](#a378f1cf157c1fd2e3422b0875319c2ae)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D1_P9_7` 引脚复用功能（Pinmux Function）。

<a id="r_ac49769a013501d1530eb05993fd2b0de"></a>

```c
#define BEE_SDHC1_D2_P9_6 (BEE_PWR_OFF + 15)
```

相关声明：[BEE_SDHC1_D2_P9_6](#ac49769a013501d1530eb05993fd2b0de)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D2_P9_6` 引脚复用功能（Pinmux Function）。

<a id="r_af3447efd95a4854aab04e6f4292a2261"></a>

```c
#define BEE_SDHC1_D3_P9_5 (BEE_PWR_OFF + 16)
```

相关声明：[BEE_SDHC1_D3_P9_5](#af3447efd95a4854aab04e6f4292a2261)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D3_P9_5` 引脚复用功能（Pinmux Function）。

<a id="r_a83e1c3839af29370e73f2629bad3805b"></a>

```c
#define BEE_SDHC1_D4_P4_4 (BEE_PWR_OFF + 17)
```

相关声明：[BEE_SDHC1_D4_P4_4](#a83e1c3839af29370e73f2629bad3805b)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D4_P4_4` 引脚复用功能（Pinmux Function）。

<a id="r_a0d80adeb6f9d66dc4ddd860db2c91ce7"></a>

```c
#define BEE_SDHC1_D5_P4_5 (BEE_PWR_OFF + 18)
```

相关声明：[BEE_SDHC1_D5_P4_5](#a0d80adeb6f9d66dc4ddd860db2c91ce7)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D5_P4_5` 引脚复用功能（Pinmux Function）。

<a id="r_a99e608ea763a7336d7fe7972711bf6f9"></a>

```c
#define BEE_SDHC1_D6_P4_6 (BEE_PWR_OFF + 19)
```

相关声明：[BEE_SDHC1_D6_P4_6](#a99e608ea763a7336d7fe7972711bf6f9)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D6_P4_6` 引脚复用功能（Pinmux Function）。

<a id="r_af184420e457cbef61065fc6d7b507971"></a>

```c
#define BEE_SDHC1_D7_P4_7 (BEE_PWR_OFF + 20)
```

相关声明：[BEE_SDHC1_D7_P4_7](#af184420e457cbef61065fc6d7b507971)、[BEE_PWR_OFF](#a95eb489d18499ff7ce936149d65ff03e)。

`SDHC1_D7_P4_7` 引脚复用功能（Pinmux Function）。

<a id="r_a1b5b713e05457eff914beceab4922ca9"></a>

```c
#define BEE_QDPH0_IN_NONE 0x0F00
```

相关声明：[BEE_QDPH0_IN_NONE](#a1b5b713e05457eff914beceab4922ca9)。

`QDPH0_IN_NONE` 引脚复用功能（Pinmux Function）。

<a id="r_a6c2f5d25f68787afeab96c1a74093595"></a>

```c
#define BEE_QDPH0_IN_P1_3_P1_4 0x0F01
```

相关声明：[BEE_QDPH0_IN_P1_3_P1_4](#a6c2f5d25f68787afeab96c1a74093595)。

`QDPH0_IN_P1_3_P1_4` 引脚复用功能（Pinmux Function）。

<a id="r_a6b0e642ce4368bddcc46fa72a808379f"></a>

```c
#define BEE_QDPH0_IN_P5_6_P5_7 0x0F02
```

相关声明：[BEE_QDPH0_IN_P5_6_P5_7](#a6b0e642ce4368bddcc46fa72a808379f)。

`QDPH0_IN_P5_6_P5_7` 引脚复用功能（Pinmux Function）。

<a id="r_a0ee761c8fea15ab3f98d92ca8c286413"></a>

```c
#define BEE_QDPH0_IN_P9_0_P9_1 0x0F03
```

相关声明：[BEE_QDPH0_IN_P9_0_P9_1](#a0ee761c8fea15ab3f98d92ca8c286413)。

`QDPH0_IN_P9_0_P9_1` 引脚复用功能（Pinmux Function）。

<a id="r_a52116a87b4f4fd7ce6beeffbb44030da"></a>

```c
#define BEE_PIN_DISCONNECTED BEE_PIN_MSK
```

相关声明：[BEE_PIN_DISCONNECTED](#a52116a87b4f4fd7ce6beeffbb44030da)、[BEE_PIN_MSK](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a8514aca71581788b4e134f74d81bcd45)。

`PIN_DISCONNECTED` 引脚复用功能（Pinmux Function）。

<a id="define-members-1"></a>

### 引脚控制可用引脚（Pinctrl Available Pins）

<a id="r_a188735bd8812ee242324075c9cae4e0e"></a>

```c
#define P0_0 0
```

相关声明：[P0_0](#a188735bd8812ee242324075c9cae4e0e)。

通用输入／输出（GPIO）：`GPIOA_0`。

<a id="r_a6e605c856305ec72ac000d8cc45ab0b9"></a>

```c
#define P0_1 1
```

相关声明：[P0_1](#a6e605c856305ec72ac000d8cc45ab0b9)。

通用输入／输出（GPIO）：`GPIOA_1`。

<a id="r_a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

```c
#define P0_2 2
```

相关声明：[P0_2](#a876e3d0917cea9d0a75b2f6df2c3f1d4)。

通用输入／输出（GPIO）：`GPIOA_2`。

<a id="r_ab73f15237a6f8860438ba0359b283686"></a>

```c
#define P0_3 3
```

相关声明：[P0_3](#ab73f15237a6f8860438ba0359b283686)。

通用输入／输出（GPIO）：`GPIOA_3`。

<a id="r_a3218b7341a4f084375bade756f108940"></a>

```c
#define P0_4 4
```

相关声明：[P0_4](#a3218b7341a4f084375bade756f108940)。

通用输入／输出（GPIO）：`GPIOA_4`。

<a id="r_aa1681f3dab52db87cd32f77b20352770"></a>

```c
#define P0_5 5
```

相关声明：[P0_5](#aa1681f3dab52db87cd32f77b20352770)。

通用输入／输出（GPIO）：`GPIOA_5`。

<a id="r_a990dc4ba08ec342d0bfa50f99d9e1868"></a>

```c
#define P0_6 6
```

相关声明：[P0_6](#a990dc4ba08ec342d0bfa50f99d9e1868)。

通用输入／输出（GPIO）：`GPIOA_6`。

<a id="r_a34087bca5283adcf7cc7c810f30eab80"></a>

```c
#define P0_7 7
```

相关声明：[P0_7](#a34087bca5283adcf7cc7c810f30eab80)。

通用输入／输出（GPIO）：`GPIOA_7`。

<a id="r_a0a5c0ef038f9728173ca136eed5c9cd2"></a>

```c
#define P1_0 8
```

相关声明：[P1_0](#a0a5c0ef038f9728173ca136eed5c9cd2)。

通用输入／输出（GPIO）：`GPIOA_8`。

<a id="r_aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

```c
#define P1_1 9
```

相关声明：[P1_1](#aa7c3cebcd9dc4598bb69e51ecee85bd0)。

通用输入／输出（GPIO）：`GPIOA_9`。

<a id="r_a071e0091581eba3bdf70559d215cda5d"></a>

```c
#define P1_2 10
```

相关声明：[P1_2](#a071e0091581eba3bdf70559d215cda5d)。

通用输入／输出（GPIO）：`GPIOA_10`。

<a id="r_ad2a4d881a3a72ead238fcf2a4aea88bf"></a>

```c
#define P1_3 11
```

相关声明：[P1_3](#ad2a4d881a3a72ead238fcf2a4aea88bf)。

通用输入／输出（GPIO）：`GPIOA_11`。

<a id="r_ab65ddc9251137261c8c17b03a415e831"></a>

```c
#define P1_4 12
```

相关声明：[P1_4](#ab65ddc9251137261c8c17b03a415e831)。

通用输入／输出（GPIO）：`GPIOA_12`。

<a id="r_af610a6265a7bc9f5c44efa18219c5e96"></a>

```c
#define P1_5 13
```

相关声明：[P1_5](#af610a6265a7bc9f5c44efa18219c5e96)。

通用输入／输出（GPIO）：`GPIOA_13`。

<a id="r_a9e219f75c65aa5b19d59bd1596b3e548"></a>

```c
#define P1_6 14
```

相关声明：[P1_6](#a9e219f75c65aa5b19d59bd1596b3e548)。

通用输入／输出（GPIO）：`GPIOA_14`。

<a id="r_a59e6507c1874213b84ae809c24c3a76e"></a>

```c
#define P1_7 15
```

相关声明：[P1_7](#a59e6507c1874213b84ae809c24c3a76e)。

通用输入／输出（GPIO）：`GPIOA_15`。

<a id="r_a5b005e989c9ae92562196f830232dc1a"></a>

```c
#define P2_0 16
```

相关声明：[P2_0](#a5b005e989c9ae92562196f830232dc1a)。

通用输入／输出（GPIO）：`GPIOA_21`。

<a id="r_aaae6a77f4b93ec74cb11947217dd8fd1"></a>

```c
#define P2_1 17
```

相关声明：[P2_1](#aaae6a77f4b93ec74cb11947217dd8fd1)。

通用输入／输出（GPIO）：`GPIOA_22`。

<a id="r_a9216eb7ac06cf1906b8c3e6884943b5e"></a>

```c
#define P2_2 18
```

相关声明：[P2_2](#a9216eb7ac06cf1906b8c3e6884943b5e)。

通用输入／输出（GPIO）：`GPIOA_23`。

<a id="r_a98005d211f8692aa984d81e1b1cefd67"></a>

```c
#define P2_3 19
```

相关声明：[P2_3](#a98005d211f8692aa984d81e1b1cefd67)。

通用输入／输出（GPIO）：`GPIOA_24`。

<a id="r_a541f1278e79f6ce8b83f48b5f3e1c177"></a>

```c
#define P2_4 20
```

相关声明：[P2_4](#a541f1278e79f6ce8b83f48b5f3e1c177)。

通用输入／输出（GPIO）：`GPIOA_25`。

<a id="r_acf47cd715ad993d583a85ef8fcac6b3e"></a>

```c
#define P2_5 21
```

相关声明：[P2_5](#acf47cd715ad993d583a85ef8fcac6b3e)。

通用输入／输出（GPIO）：`GPIOA_26`。

<a id="r_aaf264201304e2d44dc57b61eaf041654"></a>

```c
#define P2_6 22
```

相关声明：[P2_6](#aaf264201304e2d44dc57b61eaf041654)。

通用输入／输出（GPIO）：`GPIOA_27`。

<a id="r_a4f3e81fec0b7d90e9ff61bae35882c8a"></a>

```c
#define P2_7 23
```

相关声明：[P2_7](#a4f3e81fec0b7d90e9ff61bae35882c8a)。

通用输入／输出（GPIO）：`GPIOA_28`。

<a id="r_a335073a6b45e1affb80cb03be0aebd28"></a>

```c
#define P3_0 24
```

相关声明：[P3_0](#a335073a6b45e1affb80cb03be0aebd28)。

通用输入／输出（GPIO）：`GPIOA_29`。

<a id="r_aa56aef7e8461bcefa151ed84ab438dd9"></a>

```c
#define P3_1 25
```

相关声明：[P3_1](#aa56aef7e8461bcefa151ed84ab438dd9)。

通用输入／输出（GPIO）：`GPIOA_30`。

<a id="r_a7060bd469f1a43b0d5c130d35f291687"></a>

```c
#define P3_2 26
```

相关声明：[P3_2](#a7060bd469f1a43b0d5c130d35f291687)。

通用输入／输出（GPIO）：`GPIOA_31`。

<a id="r_a3394fd21eaccbcd6bfb4cc9a20a93f63"></a>

```c
#define P3_3 27
```

相关声明：[P3_3](#a3394fd21eaccbcd6bfb4cc9a20a93f63)。

通用输入／输出（GPIO）：`GPIOB_0`。

<a id="r_a444f7e1de792cb878057f9fedf8c1e92"></a>

```c
#define P3_4 28
```

相关声明：[P3_4](#a444f7e1de792cb878057f9fedf8c1e92)。

通用输入／输出（GPIO）：`GPIOB_1`。

<a id="r_add5e9628720a9e18e34d148c5e4386ae"></a>

```c
#define P3_5 29
```

相关声明：[P3_5](#add5e9628720a9e18e34d148c5e4386ae)。

通用输入／输出（GPIO）：`GPIOB_2`。

<a id="r_a5f901ec132df36067c1aebb4f0f5e99e"></a>

```c
#define P3_6 30
```

相关声明：[P3_6](#a5f901ec132df36067c1aebb4f0f5e99e)。

通用输入／输出（GPIO）：`GPIOB_3`。

<a id="r_a1f282bc8f04faf3b85e6aee0891fd9ea"></a>

```c
#define P3_7 31
```

相关声明：[P3_7](#a1f282bc8f04faf3b85e6aee0891fd9ea)。

通用输入／输出（GPIO）：`GPIOB_4`。

<a id="r_a7d02796f1733eadcc315008ac83e939a"></a>

```c
#define P4_0 32
```

相关声明：[P4_0](#a7d02796f1733eadcc315008ac83e939a)。

通用输入／输出（GPIO）：`GPIOB_5`。

<a id="r_adbc665f56899cd3fa782adc76a77087f"></a>

```c
#define P4_1 33
```

相关声明：[P4_1](#adbc665f56899cd3fa782adc76a77087f)。

通用输入／输出（GPIO）：`GPIOB_6`。

<a id="r_aef67ce6b9c7f16a266927b0545631bc2"></a>

```c
#define P4_2 34
```

相关声明：[P4_2](#aef67ce6b9c7f16a266927b0545631bc2)。

通用输入／输出（GPIO）：`GPIOB_7`。

<a id="r_a57a1bc2364d61983bdf84d6e8a7cda5b"></a>

```c
#define P4_3 35
```

相关声明：[P4_3](#a57a1bc2364d61983bdf84d6e8a7cda5b)。

通用输入／输出（GPIO）：`GPIOB_8`。

<a id="r_acefb8edcc0cfd596683c3936d70045f3"></a>

```c
#define P4_4 36
```

相关声明：[P4_4](#acefb8edcc0cfd596683c3936d70045f3)。

通用输入／输出（GPIO）：`GPIOB_9`。

<a id="r_a5c377041cd591cac2023bfadfb870c02"></a>

```c
#define P4_5 37
```

相关声明：[P4_5](#a5c377041cd591cac2023bfadfb870c02)。

通用输入／输出（GPIO）：`GPIOB_10`。

<a id="r_af635e5f062246f82e14430fd5b7a37a1"></a>

```c
#define P4_6 38
```

相关声明：[P4_6](#af635e5f062246f82e14430fd5b7a37a1)。

通用输入／输出（GPIO）：`GPIOB_11`。

<a id="r_a32a4e75f5c818be26a6dc9e43942fc28"></a>

```c
#define P4_7 39
```

相关声明：[P4_7](#a32a4e75f5c818be26a6dc9e43942fc28)。

通用输入／输出（GPIO）：`GPIOB_12`。

<a id="r_ae2df503cdc1c77adb2d1580335feb8f5"></a>

```c
#define P5_0 40
```

相关声明：[P5_0](#ae2df503cdc1c77adb2d1580335feb8f5)。

通用输入／输出（GPIO）：`GPIOB_13`。

<a id="r_aaec8c9b05d0535f709f9e40ededd5ae8"></a>

```c
#define P5_1 41
```

相关声明：[P5_1](#aaec8c9b05d0535f709f9e40ededd5ae8)。

通用输入／输出（GPIO）：`GPIOB_14`。

<a id="r_ae908c3f54860d6e0d70a10bbc5b19aae"></a>

```c
#define P5_2 42
```

相关声明：[P5_2](#ae908c3f54860d6e0d70a10bbc5b19aae)。

通用输入／输出（GPIO）：`GPIOB_15`。

<a id="r_a7a4467dbbab48a7c9ad76582e617b0dd"></a>

```c
#define P5_3 43
```

相关声明：[P5_3](#a7a4467dbbab48a7c9ad76582e617b0dd)。

通用输入／输出（GPIO）：`GPIOB_16`。

<a id="r_aab394dcb2ec36fea0ce24796706fd674"></a>

```c
#define P5_4 44
```

相关声明：[P5_4](#aab394dcb2ec36fea0ce24796706fd674)。

通用输入／输出（GPIO）：`GPIOB_17`。

<a id="r_a72ec4d5f289f6ce9cc73197b8ff69847"></a>

```c
#define P5_5 45
```

相关声明：[P5_5](#a72ec4d5f289f6ce9cc73197b8ff69847)。

通用输入／输出（GPIO）：`GPIOB_18`。

<a id="r_ac5ae5e9f17ebefe7fd99c62410fb29f7"></a>

```c
#define P5_6 46
```

相关声明：[P5_6](#ac5ae5e9f17ebefe7fd99c62410fb29f7)。

通用输入／输出（GPIO）：`GPIOB_19`。

<a id="r_a0e7b711978feec1b1081f899e35e733c"></a>

```c
#define P5_7 47
```

相关声明：[P5_7](#a0e7b711978feec1b1081f899e35e733c)。

通用输入／输出（GPIO）：`GPIOB_20`。

<a id="r_ab138af2ef513e31f72e0eb3c15415c16"></a>

```c
#define P6_0 48
```

相关声明：[P6_0](#ab138af2ef513e31f72e0eb3c15415c16)。

通用输入／输出（GPIO）：`GPIOB_19`。

<a id="r_af718f3ffb7b29dda41400081d8c39fe5"></a>

```c
#define P6_1 49
```

相关声明：[P6_1](#af718f3ffb7b29dda41400081d8c39fe5)。

通用输入／输出（GPIO）：`GPIOB_20`。

<a id="r_a106310233e1c55e02634f43b461342b6"></a>

```c
#define P6_2 50
```

相关声明：[P6_2](#a106310233e1c55e02634f43b461342b6)。

通用输入／输出（GPIO）：`GPIOB_21`。

<a id="r_a2e9a52f7ca28ac87076e180001d328e1"></a>

```c
#define P6_3 51
```

相关声明：[P6_3](#a2e9a52f7ca28ac87076e180001d328e1)。

通用输入／输出（GPIO）：`GPIOB_22`。

<a id="r_a4f71151e2704238eca74acd651186997"></a>

```c
#define P6_4 52
```

相关声明：[P6_4](#a4f71151e2704238eca74acd651186997)。

通用输入／输出（GPIO）：`GPIOB_23`。

<a id="r_a130567ee98be683fe6f1f726f9446d6c"></a>

```c
#define P6_5 53
```

相关声明：[P6_5](#a130567ee98be683fe6f1f726f9446d6c)。

通用输入／输出（GPIO）：`GPIOB_24`。

<a id="r_a63c2878cb1bb26b97a50cbbf75f6c87e"></a>

```c
#define P6_6 54
```

相关声明：[P6_6](#a63c2878cb1bb26b97a50cbbf75f6c87e)。

通用输入／输出（GPIO）：`GPIOB_25`。

<a id="r_aa6d134e0c1a86dcc7af38fc81025ba79"></a>

```c
#define P6_7 55
```

相关声明：[P6_7](#aa6d134e0c1a86dcc7af38fc81025ba79)。

通用输入／输出（GPIO）：`GPIOB_26`。

<a id="r_a3e7831712fce0e5bed27b0f10d398138"></a>

```c
#define P7_0 56
```

相关声明：[P7_0](#a3e7831712fce0e5bed27b0f10d398138)。

通用输入／输出（GPIO）：`GPIOB_27`。

<a id="r_ac372dcfaf7c262b9c3a6a8098a449944"></a>

```c
#define P7_1 57
```

相关声明：[P7_1](#ac372dcfaf7c262b9c3a6a8098a449944)。

通用输入／输出（GPIO）：`GPIOB_28`。

<a id="r_a0878dac76551e9d725850af8fcd1a4a6"></a>

```c
#define P7_2 58
```

相关声明：[P7_2](#a0878dac76551e9d725850af8fcd1a4a6)。

通用输入／输出（GPIO）：`GPIOB_29`。

<a id="r_abff6873e818564215a355a4eb5d1196e"></a>

```c
#define P7_3 59
```

相关声明：[P7_3](#abff6873e818564215a355a4eb5d1196e)。

通用输入／输出（GPIO）：`GPIOB_30`。

<a id="r_a0050eb943971937ee46a80e7eeffa668"></a>

```c
#define P7_4 60
```

相关声明：[P7_4](#a0050eb943971937ee46a80e7eeffa668)。

通用输入／输出（GPIO）：`GPIOB_31`。

<a id="r_af61dadf194031aa5b73cd036fec71808"></a>

```c
#define MICBIAS 64
```

相关声明：[MICBIAS](#af61dadf194031aa5b73cd036fec71808)。

引脚（Pin）`P8_0`：通用输入／输出（GPIO）`GPIOA_16`。

<a id="r_abf8e89f1d9b5c134447644f741b57c41"></a>

```c
#define XI32K 65
```

相关声明：[XI32K](#abf8e89f1d9b5c134447644f741b57c41)。

引脚（Pin）`P8_1`：通用输入／输出（GPIO）`GPIOA_17`。

<a id="r_a805b514cc17d3f7de5f429d6ad10bc42"></a>

```c
#define XO32K 66
```

相关声明：[XO32K](#a805b514cc17d3f7de5f429d6ad10bc42)。

引脚（Pin）`P8_2`：通用输入／输出（GPIO）`GPIOA_18`。

<a id="r_a4d38fe7e6d50f0e97e124814499a029f"></a>

```c
#define DACP 67
```

相关声明：[DACP](#a4d38fe7e6d50f0e97e124814499a029f)。

引脚（Pin）`P8_3`：通用输入／输出（GPIO）`GPIOA_19`。

<a id="r_a200aa14859c9a06396c657b688b78fca"></a>

```c
#define DACN 68
```

相关声明：[DACN](#a200aa14859c9a06396c657b688b78fca)。

引脚（Pin）`P8_4`：通用输入／输出（GPIO）`GPIOA_20`。

<a id="r_acb0b166bac2f584c7d0d5426423d0903"></a>

```c
#define P9_0 72
```

相关声明：[P9_0](#acb0b166bac2f584c7d0d5426423d0903)。

通用输入／输出（GPIO）：`GPIOB_21`。

<a id="r_a16d9deedb2b362894e322dcf774e606e"></a>

```c
#define P9_1 73
```

相关声明：[P9_1](#a16d9deedb2b362894e322dcf774e606e)。

通用输入／输出（GPIO）：`GPIOB_22`。

<a id="r_a56f01131e1920415b52b4fed7ded208c"></a>

```c
#define P9_2 74
```

相关声明：[P9_2](#a56f01131e1920415b52b4fed7ded208c)。

通用输入／输出（GPIO）：`GPIOB_23`。

<a id="r_a0821ae65c3b727af99d77f5bb5300109"></a>

```c
#define P9_3 75
```

相关声明：[P9_3](#a0821ae65c3b727af99d77f5bb5300109)。

通用输入／输出（GPIO）：`GPIOB_24`。

<a id="r_ac5e71bd34f936ea1b3b052bef23230f7"></a>

```c
#define P9_4 76
```

相关声明：[P9_4](#ac5e71bd34f936ea1b3b052bef23230f7)。

通用输入／输出（GPIO）：`GPIOB_25`。

<a id="r_ab0e4f6e7ddd83730889485a12baf1d39"></a>

```c
#define P9_5 77
```

相关声明：[P9_5](#ab0e4f6e7ddd83730889485a12baf1d39)。

通用输入／输出（GPIO）：`GPIOB_26`。

<a id="r_a90dd0717671e40593b86be768a283d55"></a>

```c
#define P9_6 78
```

相关声明：[P9_6](#a90dd0717671e40593b86be768a283d55)。

通用输入／输出（GPIO）：`GPIOB_27`。

<a id="r_ad164655c022af1461aa791efe3b7081c"></a>

```c
#define P9_7 79
```

相关声明：[P9_7](#ad164655c022af1461aa791efe3b7081c)。

通用输入／输出（GPIO）：`GPIOB_28`。

<a id="r_ae04128858406c3ffea815d10aa4c249f"></a>

```c
#define P10_0 80
```

相关声明：[P10_0](#ae04128858406c3ffea815d10aa4c249f)。

通用输入／输出（GPIO）：`GPIOB_29`。

<a id="r_a1f329f65aec3379318a143b72688beaa"></a>

```c
#define P10_1 81
```

相关声明：[P10_1](#a1f329f65aec3379318a143b72688beaa)。

通用输入／输出（GPIO）：`GPIOB_30`。

<a id="r_a288626cc26c7738fad61aac371acffa1"></a>

```c
#define P10_2 82
```

相关声明：[P10_2](#a288626cc26c7738fad61aac371acffa1)。

通用输入／输出（GPIO）：`GPIOB_31`。

<a id="r_a5cbcaa568e20fcd4cc9325927d370860"></a>

```c
#define ADC_0 P2_0
```

相关声明：[ADC_0](#a5cbcaa568e20fcd4cc9325927d370860)、[P2_0](#a5b005e989c9ae92562196f830232dc1a)。

通用输入／输出（GPIO）：`GPIO16`。

<a id="r_a3d767e16f12a6ee542079f3c9677192c"></a>

```c
#define ADC_1 P2_1
```

相关声明：[ADC_1](#a3d767e16f12a6ee542079f3c9677192c)、[P2_1](#aaae6a77f4b93ec74cb11947217dd8fd1)。

通用输入／输出（GPIO）：`GPIO17`。

<a id="r_a01ac9d2f00660408bcc8c809020904f9"></a>

```c
#define ADC_2 P2_2
```

相关声明：[ADC_2](#a01ac9d2f00660408bcc8c809020904f9)、[P2_2](#a9216eb7ac06cf1906b8c3e6884943b5e)。

通用输入／输出（GPIO）：`GPIO18`。

<a id="r_a474279f28350114950d862951d72de66"></a>

```c
#define ADC_3 P2_3
```

相关声明：[ADC_3](#a474279f28350114950d862951d72de66)、[P2_3](#a98005d211f8692aa984d81e1b1cefd67)。

通用输入／输出（GPIO）：`GPIO19`。

<a id="r_a1d0bc863ec3717e7ed493491c0f82b24"></a>

```c
#define ADC_4 P2_4
```

相关声明：[ADC_4](#a1d0bc863ec3717e7ed493491c0f82b24)、[P2_4](#a541f1278e79f6ce8b83f48b5f3e1c177)。

通用输入／输出（GPIO）：`GPIO20`。

<a id="r_a482794539449d37c65de123d0d629acb"></a>

```c
#define ADC_5 P2_5
```

相关声明：[ADC_5](#a482794539449d37c65de123d0d629acb)、[P2_5](#acf47cd715ad993d583a85ef8fcac6b3e)。

通用输入／输出（GPIO）：`GPIO21`。

<a id="r_a11092789cb59e14976636d00760ed45f"></a>

```c
#define ADC_6 P2_6
```

相关声明：[ADC_6](#a11092789cb59e14976636d00760ed45f)、[P2_6](#aaf264201304e2d44dc57b61eaf041654)。

通用输入／输出（GPIO）：`GPIO22`。

<a id="r_aa8ade7e32d46ae622ee886a90b1ea9c8"></a>

```c
#define ADC_7 P2_7
```

相关声明：[ADC_7](#aa8ade7e32d46ae622ee886a90b1ea9c8)、[P2_7](#a4f3e81fec0b7d90e9ff61bae35882c8a)。

通用输入／输出（GPIO）：`GPIO23`。

<a id="define-members-2"></a>

### GPIO 引脚控制配置（GPIO Pinctrl Configuration）

<a id="r_aea3e0359b60d675d4fa8aca9d510810c"></a>

```c
#define BEE_PSEL_GPIOA_0_P0_0 BEE_PSEL(DWGPIO, P0_0)
```

相关声明：[BEE_PSEL_GPIOA_0_P0_0](#aea3e0359b60d675d4fa8aca9d510810c)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_0](#a188735bd8812ee242324075c9cae4e0e)。

引脚（Pin）`P0_0` 对应的通用输入／输出（GPIO）为 `GPIOA_0`。

<a id="r_a43339d36676fe5280317f760c1423ecd"></a>

```c
#define BEE_PSEL_GPIOA_1_P0_1 BEE_PSEL(DWGPIO, P0_1)
```

相关声明：[BEE_PSEL_GPIOA_1_P0_1](#a43339d36676fe5280317f760c1423ecd)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_1](#a6e605c856305ec72ac000d8cc45ab0b9)。

引脚（Pin）`P0_1` 对应的通用输入／输出（GPIO）为 `GPIOA_1`。

<a id="r_a26638afbd96b5b3b8355b0625fc24f19"></a>

```c
#define BEE_PSEL_GPIOA_2_P0_2 BEE_PSEL(DWGPIO, P0_2)
```

相关声明：[BEE_PSEL_GPIOA_2_P0_2](#a26638afbd96b5b3b8355b0625fc24f19)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_2](#a876e3d0917cea9d0a75b2f6df2c3f1d4)。

引脚（Pin）`P0_2` 对应的通用输入／输出（GPIO）为 `GPIOA_2`。

<a id="r_a1c8d22ab98b90553b8ab5e25464e345b"></a>

```c
#define BEE_PSEL_GPIOA_3_P0_3 BEE_PSEL(DWGPIO, P0_3)
```

相关声明：[BEE_PSEL_GPIOA_3_P0_3](#a1c8d22ab98b90553b8ab5e25464e345b)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_3](#ab73f15237a6f8860438ba0359b283686)。

引脚（Pin）`P0_3` 对应的通用输入／输出（GPIO）为 `GPIOA_3`。

<a id="r_a234c776bffcb0087f4d9d2cb412a1db9"></a>

```c
#define BEE_PSEL_GPIOA_4_P0_4 BEE_PSEL(DWGPIO, P0_4)
```

相关声明：[BEE_PSEL_GPIOA_4_P0_4](#a234c776bffcb0087f4d9d2cb412a1db9)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_4](#a3218b7341a4f084375bade756f108940)。

引脚（Pin）`P0_4` 对应的通用输入／输出（GPIO）为 `GPIOA_4`。

<a id="r_a9e3a999c21864d7a7b092b344730a4cd"></a>

```c
#define BEE_PSEL_GPIOA_5_P0_5 BEE_PSEL(DWGPIO, P0_5)
```

相关声明：[BEE_PSEL_GPIOA_5_P0_5](#a9e3a999c21864d7a7b092b344730a4cd)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_5](#aa1681f3dab52db87cd32f77b20352770)。

引脚（Pin）`P0_5` 对应的通用输入／输出（GPIO）为 `GPIOA_5`。

<a id="r_a7a3a3d65f7ebcd3cdfe49de66066a37a"></a>

```c
#define BEE_PSEL_GPIOA_6_P0_6 BEE_PSEL(DWGPIO, P0_6)
```

相关声明：[BEE_PSEL_GPIOA_6_P0_6](#a7a3a3d65f7ebcd3cdfe49de66066a37a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_6](#a990dc4ba08ec342d0bfa50f99d9e1868)。

引脚（Pin）`P0_6` 对应的通用输入／输出（GPIO）为 `GPIOA_6`。

<a id="r_ac4fe279a43adb807fa67538aa8118ee8"></a>

```c
#define BEE_PSEL_GPIOA_7_P0_7 BEE_PSEL(DWGPIO, P0_7)
```

相关声明：[BEE_PSEL_GPIOA_7_P0_7](#ac4fe279a43adb807fa67538aa8118ee8)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P0_7](#a34087bca5283adcf7cc7c810f30eab80)。

引脚（Pin）`P0_7` 对应的通用输入／输出（GPIO）为 `GPIOA_7`。

<a id="r_a454c9df6f1af0e26b69d0efce239cd08"></a>

```c
#define BEE_PSEL_GPIOA_8_P1_0 BEE_PSEL(DWGPIO, P1_0)
```

相关声明：[BEE_PSEL_GPIOA_8_P1_0](#a454c9df6f1af0e26b69d0efce239cd08)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_0](#a0a5c0ef038f9728173ca136eed5c9cd2)。

引脚（Pin）`P1_0` 对应的通用输入／输出（GPIO）为 `GPIOA_8`。

<a id="r_ad7f2432b06b8b9e304adbc333a6dd684"></a>

```c
#define BEE_PSEL_GPIOA_9_P1_1 BEE_PSEL(DWGPIO, P1_1)
```

相关声明：[BEE_PSEL_GPIOA_9_P1_1](#ad7f2432b06b8b9e304adbc333a6dd684)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_1](#aa7c3cebcd9dc4598bb69e51ecee85bd0)。

引脚（Pin）`P1_1` 对应的通用输入／输出（GPIO）为 `GPIOA_9`。

<a id="r_abe30025d83fff188f15688dc1e0e76c0"></a>

```c
#define BEE_PSEL_GPIOA_10_P1_2 BEE_PSEL(DWGPIO, P1_2)
```

相关声明：[BEE_PSEL_GPIOA_10_P1_2](#abe30025d83fff188f15688dc1e0e76c0)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_2](#a071e0091581eba3bdf70559d215cda5d)。

引脚（Pin）`P1_2` 对应的通用输入／输出（GPIO）为 `GPIOA_10`。

<a id="r_aa8347a5c9094390be062af3fc3fce746"></a>

```c
#define BEE_PSEL_GPIOA_11_P1_3 BEE_PSEL(DWGPIO, P1_3)
```

相关声明：[BEE_PSEL_GPIOA_11_P1_3](#aa8347a5c9094390be062af3fc3fce746)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_3](#ad2a4d881a3a72ead238fcf2a4aea88bf)。

引脚（Pin）`P1_3` 对应的通用输入／输出（GPIO）为 `GPIOA_11`。

<a id="r_af15b5bd2cdba62aac469dc0e7f34393f"></a>

```c
#define BEE_PSEL_GPIOA_12_P1_4 BEE_PSEL(DWGPIO, P1_4)
```

相关声明：[BEE_PSEL_GPIOA_12_P1_4](#af15b5bd2cdba62aac469dc0e7f34393f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_4](#ab65ddc9251137261c8c17b03a415e831)。

引脚（Pin）`P1_4` 对应的通用输入／输出（GPIO）为 `GPIOA_12`。

<a id="r_a89c10337574bd3702b7462bbc6ff705a"></a>

```c
#define BEE_PSEL_GPIOA_13_P1_5 BEE_PSEL(DWGPIO, P1_5)
```

相关声明：[BEE_PSEL_GPIOA_13_P1_5](#a89c10337574bd3702b7462bbc6ff705a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_5](#af610a6265a7bc9f5c44efa18219c5e96)。

引脚（Pin）`P1_5` 对应的通用输入／输出（GPIO）为 `GPIOA_13`。

<a id="r_a1a2e353f5795551776353f7fb61afc40"></a>

```c
#define BEE_PSEL_GPIOA_14_P1_6 BEE_PSEL(DWGPIO, P1_6)
```

相关声明：[BEE_PSEL_GPIOA_14_P1_6](#a1a2e353f5795551776353f7fb61afc40)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_6](#a9e219f75c65aa5b19d59bd1596b3e548)。

引脚（Pin）`P1_6` 对应的通用输入／输出（GPIO）为 `GPIOA_14`。

<a id="r_aa23dc568bb3b72074576ce2247a62158"></a>

```c
#define BEE_PSEL_GPIOA_15_P1_7 BEE_PSEL(DWGPIO, P1_7)
```

相关声明：[BEE_PSEL_GPIOA_15_P1_7](#aa23dc568bb3b72074576ce2247a62158)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P1_7](#a59e6507c1874213b84ae809c24c3a76e)。

引脚（Pin）`P1_7` 对应的通用输入／输出（GPIO）为 `GPIOA_15`。

<a id="r_afe602d67f77e61108384d1c1408cb91e"></a>

```c
#define BEE_PSEL_GPIOA_21_P2_0 BEE_PSEL(DWGPIO, P2_0)
```

相关声明：[BEE_PSEL_GPIOA_21_P2_0](#afe602d67f77e61108384d1c1408cb91e)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_0](#a5b005e989c9ae92562196f830232dc1a)。

引脚（Pin）`P2_0` 对应的通用输入／输出（GPIO）为 `GPIOA_21`。

<a id="r_ad0a3d8caf8d858135f78df21de96af25"></a>

```c
#define BEE_PSEL_GPIOA_22_P2_1 BEE_PSEL(DWGPIO, P2_1)
```

相关声明：[BEE_PSEL_GPIOA_22_P2_1](#ad0a3d8caf8d858135f78df21de96af25)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_1](#aaae6a77f4b93ec74cb11947217dd8fd1)。

引脚（Pin）`P2_1` 对应的通用输入／输出（GPIO）为 `GPIOA_22`。

<a id="r_afc018ec04dc46953934210304de3ba37"></a>

```c
#define BEE_PSEL_GPIOA_23_P2_2 BEE_PSEL(DWGPIO, P2_2)
```

相关声明：[BEE_PSEL_GPIOA_23_P2_2](#afc018ec04dc46953934210304de3ba37)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_2](#a9216eb7ac06cf1906b8c3e6884943b5e)。

引脚（Pin）`P2_2` 对应的通用输入／输出（GPIO）为 `GPIOA_23`。

<a id="r_a89f189327426220fd0414a0ac5438b4a"></a>

```c
#define BEE_PSEL_GPIOA_24_P2_3 BEE_PSEL(DWGPIO, P2_3)
```

相关声明：[BEE_PSEL_GPIOA_24_P2_3](#a89f189327426220fd0414a0ac5438b4a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_3](#a98005d211f8692aa984d81e1b1cefd67)。

引脚（Pin）`P2_3` 对应的通用输入／输出（GPIO）为 `GPIOA_24`。

<a id="r_af9c2916643b38e97d69ffb6cf30c6043"></a>

```c
#define BEE_PSEL_GPIOA_25_P2_4 BEE_PSEL(DWGPIO, P2_4)
```

相关声明：[BEE_PSEL_GPIOA_25_P2_4](#af9c2916643b38e97d69ffb6cf30c6043)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_4](#a541f1278e79f6ce8b83f48b5f3e1c177)。

引脚（Pin）`P2_4` 对应的通用输入／输出（GPIO）为 `GPIOA_25`。

<a id="r_a134484fd42f21d66efefbaef0de5986f"></a>

```c
#define BEE_PSEL_GPIOA_26_P2_5 BEE_PSEL(DWGPIO, P2_5)
```

相关声明：[BEE_PSEL_GPIOA_26_P2_5](#a134484fd42f21d66efefbaef0de5986f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_5](#acf47cd715ad993d583a85ef8fcac6b3e)。

引脚（Pin）`P2_5` 对应的通用输入／输出（GPIO）为 `GPIOA_26`。

<a id="r_aac866abdb85b9fb6a1ace78fdb3a6044"></a>

```c
#define BEE_PSEL_GPIOA_27_P2_6 BEE_PSEL(DWGPIO, P2_6)
```

相关声明：[BEE_PSEL_GPIOA_27_P2_6](#aac866abdb85b9fb6a1ace78fdb3a6044)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_6](#aaf264201304e2d44dc57b61eaf041654)。

引脚（Pin）`P2_6` 对应的通用输入／输出（GPIO）为 `GPIOA_27`。

<a id="r_a212885c412a0155da1b909aaab9bbe5a"></a>

```c
#define BEE_PSEL_GPIOA_28_P2_7 BEE_PSEL(DWGPIO, P2_7)
```

相关声明：[BEE_PSEL_GPIOA_28_P2_7](#a212885c412a0155da1b909aaab9bbe5a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_7](#a4f3e81fec0b7d90e9ff61bae35882c8a)。

引脚（Pin）`P2_7` 对应的通用输入／输出（GPIO）为 `GPIOA_28`。

<a id="r_a4cd98da234f8ba483d1a5e6b1306adf4"></a>

```c
#define BEE_PSEL_GPIOA_29_P3_0 BEE_PSEL(DWGPIO, P3_0)
```

相关声明：[BEE_PSEL_GPIOA_29_P3_0](#a4cd98da234f8ba483d1a5e6b1306adf4)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_0](#a335073a6b45e1affb80cb03be0aebd28)。

引脚（Pin）`P3_0` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="r_a4f653ba441eb7f69ae79282f3c3ecd0d"></a>

```c
#define BEE_PSEL_GPIOA_30_P3_1 BEE_PSEL(DWGPIO, P3_1)
```

相关声明：[BEE_PSEL_GPIOA_30_P3_1](#a4f653ba441eb7f69ae79282f3c3ecd0d)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_1](#aa56aef7e8461bcefa151ed84ab438dd9)。

引脚（Pin）`P3_1` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="r_aa4e874d88ef66bb6014e63979f68d597"></a>

```c
#define BEE_PSEL_GPIOA_31_P3_2 BEE_PSEL(DWGPIO, P3_2)
```

相关声明：[BEE_PSEL_GPIOA_31_P3_2](#aa4e874d88ef66bb6014e63979f68d597)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_2](#a7060bd469f1a43b0d5c130d35f291687)。

引脚（Pin）`P3_2` 对应的通用输入／输出（GPIO）为 `GPIOA_31`。

<a id="r_aa857cff3b0a5a7533c0a5be4d38c9b69"></a>

```c
#define BEE_PSEL_GPIOB_0_P3_3 BEE_PSEL(DWGPIO, P3_3)
```

相关声明：[BEE_PSEL_GPIOB_0_P3_3](#aa857cff3b0a5a7533c0a5be4d38c9b69)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_3](#a3394fd21eaccbcd6bfb4cc9a20a93f63)。

引脚（Pin）`P3_3` 对应的通用输入／输出（GPIO）为 `GPIOB_0`。

<a id="r_aab941bb496c9a3b17bf04160f859a5ae"></a>

```c
#define BEE_PSEL_GPIOB_1_P3_4 BEE_PSEL(DWGPIO, P3_4)
```

相关声明：[BEE_PSEL_GPIOB_1_P3_4](#aab941bb496c9a3b17bf04160f859a5ae)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_4](#a444f7e1de792cb878057f9fedf8c1e92)。

引脚（Pin）`P3_4` 对应的通用输入／输出（GPIO）为 `GPIOB_1`。

<a id="r_a051f0125e7669aa84a40e62272ff9abb"></a>

```c
#define BEE_PSEL_GPIOB_2_P3_5 BEE_PSEL(DWGPIO, P3_5)
```

相关声明：[BEE_PSEL_GPIOB_2_P3_5](#a051f0125e7669aa84a40e62272ff9abb)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_5](#add5e9628720a9e18e34d148c5e4386ae)。

引脚（Pin）`P3_5` 对应的通用输入／输出（GPIO）为 `GPIOB_2`。

<a id="r_a8a79064fa2f09c40f6da1a57a42f974d"></a>

```c
#define BEE_PSEL_GPIOB_3_P3_6 BEE_PSEL(DWGPIO, P3_6)
```

相关声明：[BEE_PSEL_GPIOB_3_P3_6](#a8a79064fa2f09c40f6da1a57a42f974d)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_6](#a5f901ec132df36067c1aebb4f0f5e99e)。

引脚（Pin）`P3_6` 对应的通用输入／输出（GPIO）为 `GPIOB_3`。

<a id="r_a7f0150a901653bd47b0bfc7e7a612e78"></a>

```c
#define BEE_PSEL_GPIOB_4_P3_7 BEE_PSEL(DWGPIO, P3_7)
```

相关声明：[BEE_PSEL_GPIOB_4_P3_7](#a7f0150a901653bd47b0bfc7e7a612e78)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_7](#a1f282bc8f04faf3b85e6aee0891fd9ea)。

引脚（Pin）`P3_7` 对应的通用输入／输出（GPIO）为 `GPIOB_4`。

<a id="r_a042110a436d34f4ba57b93baf532e551"></a>

```c
#define BEE_PSEL_GPIOB_5_P4_0 BEE_PSEL(DWGPIO, P4_0)
```

相关声明：[BEE_PSEL_GPIOB_5_P4_0](#a042110a436d34f4ba57b93baf532e551)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_0](#a7d02796f1733eadcc315008ac83e939a)。

引脚（Pin）`P4_0` 对应的通用输入／输出（GPIO）为 `GPIOB_5`。

<a id="r_ac459d3b2425228b368bd00364c2150e5"></a>

```c
#define BEE_PSEL_GPIOB_6_P4_1 BEE_PSEL(DWGPIO, P4_1)
```

相关声明：[BEE_PSEL_GPIOB_6_P4_1](#ac459d3b2425228b368bd00364c2150e5)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_1](#adbc665f56899cd3fa782adc76a77087f)。

引脚（Pin）`P4_1` 对应的通用输入／输出（GPIO）为 `GPIOB_6`。

<a id="r_ab5f4220e46b4f7fb180a40fbc2e814bc"></a>

```c
#define BEE_PSEL_GPIOB_7_P4_2 BEE_PSEL(DWGPIO, P4_2)
```

相关声明：[BEE_PSEL_GPIOB_7_P4_2](#ab5f4220e46b4f7fb180a40fbc2e814bc)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_2](#aef67ce6b9c7f16a266927b0545631bc2)。

引脚（Pin）`P4_2` 对应的通用输入／输出（GPIO）为 `GPIOB_7`。

<a id="r_ae203cb3fcd4c70a4e3debe1d24b64d1b"></a>

```c
#define BEE_PSEL_GPIOB_8_P4_3 BEE_PSEL(DWGPIO, P4_3)
```

相关声明：[BEE_PSEL_GPIOB_8_P4_3](#ae203cb3fcd4c70a4e3debe1d24b64d1b)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_3](#a57a1bc2364d61983bdf84d6e8a7cda5b)。

引脚（Pin）`P4_3` 对应的通用输入／输出（GPIO）为 `GPIOB_8`。

<a id="r_a029877141321b4eff25b553653d79302"></a>

```c
#define BEE_PSEL_GPIOB_9_P4_4 BEE_PSEL(DWGPIO, P4_4)
```

相关声明：[BEE_PSEL_GPIOB_9_P4_4](#a029877141321b4eff25b553653d79302)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_4](#acefb8edcc0cfd596683c3936d70045f3)。

引脚（Pin）`P4_4` 对应的通用输入／输出（GPIO）为 `GPIOB_9`。

<a id="r_ab9ed93bf7dbe9b3630d661e373b4216a"></a>

```c
#define BEE_PSEL_GPIOB_10_P4_5 BEE_PSEL(DWGPIO, P4_5)
```

相关声明：[BEE_PSEL_GPIOB_10_P4_5](#ab9ed93bf7dbe9b3630d661e373b4216a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_5](#a5c377041cd591cac2023bfadfb870c02)。

引脚（Pin）`P4_5` 对应的通用输入／输出（GPIO）为 `GPIOB_10`。

<a id="r_a47c881203795793aa10db90a5971e167"></a>

```c
#define BEE_PSEL_GPIOB_11_P4_6 BEE_PSEL(DWGPIO, P4_6)
```

相关声明：[BEE_PSEL_GPIOB_11_P4_6](#a47c881203795793aa10db90a5971e167)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_6](#af635e5f062246f82e14430fd5b7a37a1)。

引脚（Pin）`P4_6` 对应的通用输入／输出（GPIO）为 `GPIOB_11`。

<a id="r_ab1b450789fe924726dbf7215c1f32bac"></a>

```c
#define BEE_PSEL_GPIOB_12_P4_7 BEE_PSEL(DWGPIO, P4_7)
```

相关声明：[BEE_PSEL_GPIOB_12_P4_7](#ab1b450789fe924726dbf7215c1f32bac)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_7](#a32a4e75f5c818be26a6dc9e43942fc28)。

引脚（Pin）`P4_7` 对应的通用输入／输出（GPIO）为 `GPIOB_12`。

<a id="r_aa69815c1c28800129fa4d15e0503a5f3"></a>

```c
#define BEE_PSEL_GPIOB_13_P5_0 BEE_PSEL(DWGPIO, P5_0)
```

相关声明：[BEE_PSEL_GPIOB_13_P5_0](#aa69815c1c28800129fa4d15e0503a5f3)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_0](#ae2df503cdc1c77adb2d1580335feb8f5)。

引脚（Pin）`P5_0` 对应的通用输入／输出（GPIO）为 `GPIOB_13`。

<a id="r_a064316a5d726c6493888a95f70ce693c"></a>

```c
#define BEE_PSEL_GPIOB_14_P5_1 BEE_PSEL(DWGPIO, P5_1)
```

相关声明：[BEE_PSEL_GPIOB_14_P5_1](#a064316a5d726c6493888a95f70ce693c)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_1](#aaec8c9b05d0535f709f9e40ededd5ae8)。

引脚（Pin）`P5_1` 对应的通用输入／输出（GPIO）为 `GPIOB_14`。

<a id="r_a2d90968c8382a6028f8ebc1b91125fb5"></a>

```c
#define BEE_PSEL_GPIOB_15_P5_2 BEE_PSEL(DWGPIO, P5_2)
```

相关声明：[BEE_PSEL_GPIOB_15_P5_2](#a2d90968c8382a6028f8ebc1b91125fb5)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_2](#ae908c3f54860d6e0d70a10bbc5b19aae)。

引脚（Pin）`P5_2` 对应的通用输入／输出（GPIO）为 `GPIOB_15`。

<a id="r_ac0381fbf6f98cdb8a654c0240c08fb1e"></a>

```c
#define BEE_PSEL_GPIOB_16_P5_3 BEE_PSEL(DWGPIO, P5_3)
```

相关声明：[BEE_PSEL_GPIOB_16_P5_3](#ac0381fbf6f98cdb8a654c0240c08fb1e)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_3](#a7a4467dbbab48a7c9ad76582e617b0dd)。

引脚（Pin）`P5_3` 对应的通用输入／输出（GPIO）为 `GPIOB_16`。

<a id="r_a3b1d923dfac2f8868506c9d533e548c8"></a>

```c
#define BEE_PSEL_GPIOB_17_P5_4 BEE_PSEL(DWGPIO, P5_4)
```

相关声明：[BEE_PSEL_GPIOB_17_P5_4](#a3b1d923dfac2f8868506c9d533e548c8)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_4](#aab394dcb2ec36fea0ce24796706fd674)。

引脚（Pin）`P5_4` 对应的通用输入／输出（GPIO）为 `GPIOB_17`。

<a id="r_ae6ffa065d3db9bcffbdcc8da512ac6bf"></a>

```c
#define BEE_PSEL_GPIOB_18_P5_5 BEE_PSEL(DWGPIO, P5_5)
```

相关声明：[BEE_PSEL_GPIOB_18_P5_5](#ae6ffa065d3db9bcffbdcc8da512ac6bf)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_5](#a72ec4d5f289f6ce9cc73197b8ff69847)。

引脚（Pin）`P5_5` 对应的通用输入／输出（GPIO）为 `GPIOB_18`。

<a id="r_a6290760413dba008f66c2a60a15a881a"></a>

```c
#define BEE_PSEL_GPIOB_19_P5_6 BEE_PSEL(DWGPIO, P5_6)
```

相关声明：[BEE_PSEL_GPIOB_19_P5_6](#a6290760413dba008f66c2a60a15a881a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_6](#ac5ae5e9f17ebefe7fd99c62410fb29f7)。

引脚（Pin）`P5_6` 对应的通用输入／输出（GPIO）为 `GPIOB_19`。

<a id="r_adaebe442b7720e8879118cf0909e0f33"></a>

```c
#define BEE_PSEL_GPIOB_20_P5_7 BEE_PSEL(DWGPIO, P5_7)
```

相关声明：[BEE_PSEL_GPIOB_20_P5_7](#adaebe442b7720e8879118cf0909e0f33)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_7](#a0e7b711978feec1b1081f899e35e733c)。

引脚（Pin）`P5_7` 对应的通用输入／输出（GPIO）为 `GPIOB_20`。

<a id="r_a079881107a3c542f715866101483c256"></a>

```c
#define BEE_PSEL_GPIOB_19_P6_0 BEE_PSEL(DWGPIO, P6_0)
```

相关声明：[BEE_PSEL_GPIOB_19_P6_0](#a079881107a3c542f715866101483c256)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_0](#ab138af2ef513e31f72e0eb3c15415c16)。

引脚（Pin）`P6_0` 对应的通用输入／输出（GPIO）为 `GPIOB_19`。

<a id="r_a84101841d0ad51059acb9e5e0535c5eb"></a>

```c
#define BEE_PSEL_GPIOB_20_P6_1 BEE_PSEL(DWGPIO, P6_1)
```

相关声明：[BEE_PSEL_GPIOB_20_P6_1](#a84101841d0ad51059acb9e5e0535c5eb)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_1](#af718f3ffb7b29dda41400081d8c39fe5)。

引脚（Pin）`P6_1` 对应的通用输入／输出（GPIO）为 `GPIOB_20`。

<a id="r_aa344f94a8846b70f21cf0c1bf4afa0f5"></a>

```c
#define BEE_PSEL_GPIOB_21_P6_2 BEE_PSEL(DWGPIO, P6_2)
```

相关声明：[BEE_PSEL_GPIOB_21_P6_2](#aa344f94a8846b70f21cf0c1bf4afa0f5)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_2](#a106310233e1c55e02634f43b461342b6)。

引脚（Pin）`P6_2` 对应的通用输入／输出（GPIO）为 `GPIOB_21`。

<a id="r_a71c08b5a045cb5db3a04ab48cd360411"></a>

```c
#define BEE_PSEL_GPIOB_22_P6_3 BEE_PSEL(DWGPIO, P6_3)
```

相关声明：[BEE_PSEL_GPIOB_22_P6_3](#a71c08b5a045cb5db3a04ab48cd360411)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_3](#a2e9a52f7ca28ac87076e180001d328e1)。

引脚（Pin）`P6_3` 对应的通用输入／输出（GPIO）为 `GPIOB_22`。

<a id="r_abec19f4e9156084584d5af3e96a7b100"></a>

```c
#define BEE_PSEL_GPIOB_23_P6_4 BEE_PSEL(DWGPIO, P6_4)
```

相关声明：[BEE_PSEL_GPIOB_23_P6_4](#abec19f4e9156084584d5af3e96a7b100)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_4](#a4f71151e2704238eca74acd651186997)。

引脚（Pin）`P6_4` 对应的通用输入／输出（GPIO）为 `GPIOB_23`。

<a id="r_ad583fd72055dde27e56d379639798880"></a>

```c
#define BEE_PSEL_GPIOB_24_P6_5 BEE_PSEL(DWGPIO, P6_5)
```

相关声明：[BEE_PSEL_GPIOB_24_P6_5](#ad583fd72055dde27e56d379639798880)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_5](#a130567ee98be683fe6f1f726f9446d6c)。

引脚（Pin）`P6_5` 对应的通用输入／输出（GPIO）为 `GPIOB_24`。

<a id="r_a22c869993ed5ebd50847e6637e17fe1b"></a>

```c
#define BEE_PSEL_GPIOB_25_P6_6 BEE_PSEL(DWGPIO, P6_6)
```

相关声明：[BEE_PSEL_GPIOB_25_P6_6](#a22c869993ed5ebd50847e6637e17fe1b)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_6](#a63c2878cb1bb26b97a50cbbf75f6c87e)。

引脚（Pin）`P6_6` 对应的通用输入／输出（GPIO）为 `GPIOB_25`。

<a id="r_a16cebe162cc25f6ed05c07854ab00992"></a>

```c
#define BEE_PSEL_GPIOB_26_P6_7 BEE_PSEL(DWGPIO, P6_7)
```

相关声明：[BEE_PSEL_GPIOB_26_P6_7](#a16cebe162cc25f6ed05c07854ab00992)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P6_7](#aa6d134e0c1a86dcc7af38fc81025ba79)。

引脚（Pin）`P6_7` 对应的通用输入／输出（GPIO）为 `GPIOB_26`。

<a id="r_af8d90b08a06dde62cffcd221d64adcea"></a>

```c
#define BEE_PSEL_GPIOB_27_P7_0 BEE_PSEL(DWGPIO, P7_0)
```

相关声明：[BEE_PSEL_GPIOB_27_P7_0](#af8d90b08a06dde62cffcd221d64adcea)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P7_0](#a3e7831712fce0e5bed27b0f10d398138)。

引脚（Pin）`P7_0` 对应的通用输入／输出（GPIO）为 `GPIOB_27`。

<a id="r_a310533a04c66382479c7356afdcf5749"></a>

```c
#define BEE_PSEL_GPIOB_28_P7_1 BEE_PSEL(DWGPIO, P7_1)
```

相关声明：[BEE_PSEL_GPIOB_28_P7_1](#a310533a04c66382479c7356afdcf5749)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P7_1](#ac372dcfaf7c262b9c3a6a8098a449944)。

引脚（Pin）`P7_1` 对应的通用输入／输出（GPIO）为 `GPIOB_28`。

<a id="r_a93ecea9a0885299a6cdc760f71c23a98"></a>

```c
#define BEE_PSEL_GPIOB_29_P7_2 BEE_PSEL(DWGPIO, P7_2)
```

相关声明：[BEE_PSEL_GPIOB_29_P7_2](#a93ecea9a0885299a6cdc760f71c23a98)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P7_2](#a0878dac76551e9d725850af8fcd1a4a6)。

引脚（Pin）`P7_2` 对应的通用输入／输出（GPIO）为 `GPIOB_29`。

<a id="r_acec4838f3ca65b1987641731fb700f5e"></a>

```c
#define BEE_PSEL_GPIOB_30_P7_3 BEE_PSEL(DWGPIO, P7_3)
```

相关声明：[BEE_PSEL_GPIOB_30_P7_3](#acec4838f3ca65b1987641731fb700f5e)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P7_3](#abff6873e818564215a355a4eb5d1196e)。

引脚（Pin）`P7_3` 对应的通用输入／输出（GPIO）为 `GPIOB_30`。

<a id="r_a61493776635cdd949703f611fc874a5f"></a>

```c
#define BEE_PSEL_GPIOB_31_P7_4 BEE_PSEL(DWGPIO, P7_4)
```

相关声明：[BEE_PSEL_GPIOB_31_P7_4](#a61493776635cdd949703f611fc874a5f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P7_4](#a0050eb943971937ee46a80e7eeffa668)。

引脚（Pin）`P7_4` 对应的通用输入／输出（GPIO）为 `GPIOB_31`。

<a id="r_a6c1eb0e99ad648f77b6b3985940f2849"></a>

```c
#define BEE_PSEL_GPIOA_16_P8_0 BEE_PSEL(DWGPIO, MICBIAS)
```

相关声明：[BEE_PSEL_GPIOA_16_P8_0](#a6c1eb0e99ad648f77b6b3985940f2849)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[MICBIAS](#af61dadf194031aa5b73cd036fec71808)。

引脚（Pin）`P8_0` 对应的通用输入／输出（GPIO）为 `GPIOA_16`。

<a id="r_afd3e6c79aebd096fa0e54c3ff49d460a"></a>

```c
#define BEE_PSEL_GPIOA_17_P8_1 BEE_PSEL(DWGPIO, XI32K)
```

相关声明：[BEE_PSEL_GPIOA_17_P8_1](#afd3e6c79aebd096fa0e54c3ff49d460a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[XI32K](#abf8e89f1d9b5c134447644f741b57c41)。

引脚（Pin）`P8_1` 对应的通用输入／输出（GPIO）为 `GPIOA_17`。

<a id="r_adb394912fc05a8b68d5fc80a63eabfde"></a>

```c
#define BEE_PSEL_GPIOA_18_P8_2 BEE_PSEL(DWGPIO, XO32K)
```

相关声明：[BEE_PSEL_GPIOA_18_P8_2](#adb394912fc05a8b68d5fc80a63eabfde)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[XO32K](#a805b514cc17d3f7de5f429d6ad10bc42)。

引脚（Pin）`P8_2` 对应的通用输入／输出（GPIO）为 `GPIOA_18`。

<a id="r_a1b523a451f975b6e68dd4ddf05569346"></a>

```c
#define BEE_PSEL_GPIOA_19_P8_3 BEE_PSEL(DWGPIO, DACP)
```

相关声明：[BEE_PSEL_GPIOA_19_P8_3](#a1b523a451f975b6e68dd4ddf05569346)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[DACP](#a4d38fe7e6d50f0e97e124814499a029f)。

引脚（Pin）`P8_3` 对应的通用输入／输出（GPIO）为 `GPIOA_19`。

<a id="r_a47d84fc152cac7e55eb6b468243c8c1c"></a>

```c
#define BEE_PSEL_GPIOA_20_P8_4 BEE_PSEL(DWGPIO, DACN)
```

相关声明：[BEE_PSEL_GPIOA_20_P8_4](#a47d84fc152cac7e55eb6b468243c8c1c)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[DACN](#a200aa14859c9a06396c657b688b78fca)。

引脚（Pin）`P8_4` 对应的通用输入／输出（GPIO）为 `GPIOA_20`。

<a id="r_a5aee5e9a60d7f13d9f5401e9a7390f46"></a>

```c
#define BEE_PSEL_GPIOB_21_P9_0 BEE_PSEL(DWGPIO, P9_0)
```

相关声明：[BEE_PSEL_GPIOB_21_P9_0](#a5aee5e9a60d7f13d9f5401e9a7390f46)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_0](#acb0b166bac2f584c7d0d5426423d0903)。

引脚（Pin）`P9_0` 对应的通用输入／输出（GPIO）为 `GPIOB_21`。

<a id="r_a90ed9bd2a5a729b25c56b72e3ba49126"></a>

```c
#define BEE_PSEL_GPIOB_22_P9_1 BEE_PSEL(DWGPIO, P9_1)
```

相关声明：[BEE_PSEL_GPIOB_22_P9_1](#a90ed9bd2a5a729b25c56b72e3ba49126)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_1](#a16d9deedb2b362894e322dcf774e606e)。

引脚（Pin）`P9_1` 对应的通用输入／输出（GPIO）为 `GPIOB_22`。

<a id="r_a2c2d98245c1763b940cbbbf350349cf9"></a>

```c
#define BEE_PSEL_GPIOB_23_P9_2 BEE_PSEL(DWGPIO, P9_2)
```

相关声明：[BEE_PSEL_GPIOB_23_P9_2](#a2c2d98245c1763b940cbbbf350349cf9)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_2](#a56f01131e1920415b52b4fed7ded208c)。

引脚（Pin）`P9_2` 对应的通用输入／输出（GPIO）为 `GPIOB_23`。

<a id="r_afae90f1839d1d1bb3845388dedc4ebee"></a>

```c
#define BEE_PSEL_GPIOB_24_P9_3 BEE_PSEL(DWGPIO, P9_3)
```

相关声明：[BEE_PSEL_GPIOB_24_P9_3](#afae90f1839d1d1bb3845388dedc4ebee)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_3](#a0821ae65c3b727af99d77f5bb5300109)。

引脚（Pin）`P9_3` 对应的通用输入／输出（GPIO）为 `GPIOB_24`。

<a id="r_a5528e09208f0499628bdfee4d557d699"></a>

```c
#define BEE_PSEL_GPIOB_25_P9_4 BEE_PSEL(DWGPIO, P9_4)
```

相关声明：[BEE_PSEL_GPIOB_25_P9_4](#a5528e09208f0499628bdfee4d557d699)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_4](#ac5e71bd34f936ea1b3b052bef23230f7)。

引脚（Pin）`P9_4` 对应的通用输入／输出（GPIO）为 `GPIOB_25`。

<a id="r_ac451f0ac4626b20efbd01684f3bbafc9"></a>

```c
#define BEE_PSEL_GPIOB_26_P9_5 BEE_PSEL(DWGPIO, P9_5)
```

相关声明：[BEE_PSEL_GPIOB_26_P9_5](#ac451f0ac4626b20efbd01684f3bbafc9)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_5](#ab0e4f6e7ddd83730889485a12baf1d39)。

引脚（Pin）`P9_5` 对应的通用输入／输出（GPIO）为 `GPIOB_26`。

<a id="r_ab334b13e0e286e41d0a3e3163a4c4ce4"></a>

```c
#define BEE_PSEL_GPIOB_27_P9_6 BEE_PSEL(DWGPIO, P9_6)
```

相关声明：[BEE_PSEL_GPIOB_27_P9_6](#ab334b13e0e286e41d0a3e3163a4c4ce4)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_6](#a90dd0717671e40593b86be768a283d55)。

引脚（Pin）`P9_6` 对应的通用输入／输出（GPIO）为 `GPIOB_27`。

<a id="r_a84d09985aacd4e9e91224c75a3020aff"></a>

```c
#define BEE_PSEL_GPIOB_28_P9_7 BEE_PSEL(DWGPIO, P9_7)
```

相关声明：[BEE_PSEL_GPIOB_28_P9_7](#a84d09985aacd4e9e91224c75a3020aff)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P9_7](#ad164655c022af1461aa791efe3b7081c)。

引脚（Pin）`P9_7` 对应的通用输入／输出（GPIO）为 `GPIOB_28`。

<a id="r_a7887a1e36f14c8934bf85c8a137e7e72"></a>

```c
#define BEE_PSEL_GPIOB_29_P10_0 BEE_PSEL(DWGPIO, P10_0)
```

相关声明：[BEE_PSEL_GPIOB_29_P10_0](#a7887a1e36f14c8934bf85c8a137e7e72)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P10_0](#ae04128858406c3ffea815d10aa4c249f)。

引脚（Pin）`P10_0` 对应的通用输入／输出（GPIO）为 `GPIOB_29`。

<a id="r_afe77a8bd153bea08efaf5870c597c250"></a>

```c
#define BEE_PSEL_GPIOB_30_P10_1 BEE_PSEL(DWGPIO, P10_1)
```

相关声明：[BEE_PSEL_GPIOB_30_P10_1](#afe77a8bd153bea08efaf5870c597c250)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P10_1](#a1f329f65aec3379318a143b72688beaa)。

引脚（Pin）`P10_1` 对应的通用输入／输出（GPIO）为 `GPIOB_30`。

<a id="r_af9574261e821d01dce1850883f933020"></a>

```c
#define BEE_PSEL_GPIOB_31_P10_2 BEE_PSEL(DWGPIO, P10_2)
```

相关声明：[BEE_PSEL_GPIOB_31_P10_2](#af9574261e821d01dce1850883f933020)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P10_2](#a288626cc26c7738fad61aac371acffa1)。

引脚（Pin）`P10_2` 对应的通用输入／输出（GPIO）为 `GPIOB_31`。

## 6.2\_详细说明（Detailed Documentation）

<a id="a5cbcaa568e20fcd4cc9325927d370860"></a>

### `ADC_0`

```c
#define ADC_0 P2_0
```

通用输入／输出（GPIO）：`GPIO16`。

<a id="a3d767e16f12a6ee542079f3c9677192c"></a>

### `ADC_1`

```c
#define ADC_1 P2_1
```

通用输入／输出（GPIO）：`GPIO17`。

<a id="a01ac9d2f00660408bcc8c809020904f9"></a>

### `ADC_2`

```c
#define ADC_2 P2_2
```

通用输入／输出（GPIO）：`GPIO18`。

<a id="a474279f28350114950d862951d72de66"></a>

### `ADC_3`

```c
#define ADC_3 P2_3
```

通用输入／输出（GPIO）：`GPIO19`。

<a id="a1d0bc863ec3717e7ed493491c0f82b24"></a>

### `ADC_4`

```c
#define ADC_4 P2_4
```

通用输入／输出（GPIO）：`GPIO20`。

<a id="a482794539449d37c65de123d0d629acb"></a>

### `ADC_5`

```c
#define ADC_5 P2_5
```

通用输入／输出（GPIO）：`GPIO21`。

<a id="a11092789cb59e14976636d00760ed45f"></a>

### `ADC_6`

```c
#define ADC_6 P2_6
```

通用输入／输出（GPIO）：`GPIO22`。

<a id="aa8ade7e32d46ae622ee886a90b1ea9c8"></a>

### `ADC_7`

```c
#define ADC_7 P2_7
```

通用输入／输出（GPIO）：`GPIO23`。

<a id="a1383cae9e4cf0048180c741624c6909b"></a>

### `BEE_A2C_RX`

```c
#define BEE_A2C_RX 156
```

`A2C_RX` 引脚复用功能（Pinmux Function）。

<a id="ac5103fd9a770f992502e72e7076c46ce"></a>

### `BEE_A2C_TX`

```c
#define BEE_A2C_TX 155
```

`A2C_TX` 引脚复用功能（Pinmux Function）。

<a id="a0a8dabb3051d18f3b0c63485417bfafd"></a>

### `BEE_ADCDAT_SPORT0`

```c
#define BEE_ADCDAT_SPORT0 174
```

`ADCDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a98522c73d9f29a0a43c37a94eea377e0"></a>

### `BEE_ADCDAT_SPORT1`

```c
#define BEE_ADCDAT_SPORT1 159
```

`ADCDAT_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="a630537cb405d771f9ca478ad702c15ff"></a>

### `BEE_ANT_SW0`

```c
#define BEE_ANT_SW0 231
```

`ANT_SW0` 引脚复用功能（Pinmux Function）。

<a id="a7d7a7ceac66b6d65e0dd466da57c7432"></a>

### `BEE_ANT_SW1`

```c
#define BEE_ANT_SW1 232
```

`ANT_SW1` 引脚复用功能（Pinmux Function）。

<a id="a210a42a9f7bf5862bc5efbd27d6304de"></a>

### `BEE_ANT_SW2`

```c
#define BEE_ANT_SW2 233
```

`ANT_SW2` 引脚复用功能（Pinmux Function）。

<a id="ae25e5f43db415c0ef27adcf3cbd38e79"></a>

### `BEE_ANT_SW3`

```c
#define BEE_ANT_SW3 234
```

`ANT_SW3` 引脚复用功能（Pinmux Function）。

<a id="a0b8ab8e7f60c24a1955356e5c718751e"></a>

### `BEE_ANT_SW4`

```c
#define BEE_ANT_SW4 235
```

`ANT_SW4` 引脚复用功能（Pinmux Function）。

<a id="a67af09727ac50bf3a71459d892315723"></a>

### `BEE_ANT_SW5`

```c
#define BEE_ANT_SW5 236
```

`ANT_SW5` 引脚复用功能（Pinmux Function）。

<a id="aad1e43c193aa44b6f2301dbafe13ea92"></a>

### `BEE_BACK_END_POWER_0`

```c
#define BEE_BACK_END_POWER_0 149
```

`BACK_END_POWER_0` 引脚复用功能（Pinmux Function）。

<a id="a912613b40d5c8101fb80ef546259718c"></a>

### `BEE_BCLK_I_CODEC_SLAVE`

```c
#define BEE_BCLK_I_CODEC_SLAVE 165
```

`BCLK_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ae8c197cf5a76f0e30b400e4190fa3d60"></a>

### `BEE_BCLK_SPORT0`

```c
#define BEE_BCLK_SPORT0 173
```

`BCLK_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a62e4dd6b6605747655b67407a1f08977"></a>

### `BEE_BCLK_SPORT1`

```c
#define BEE_BCLK_SPORT1 158
```

`BCLK_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="ac08f855050ffa3b42fd846fec5db4fbd"></a>

### `BEE_BIU_VOLT_REG_0`

```c
#define BEE_BIU_VOLT_REG_0 148
```

`BIU_VOLT_REG_0` 引脚复用功能（Pinmux Function）。

<a id="ab122a176b695a923610b8d090ade6430"></a>

### `BEE_BT_COEX_I_0`

```c
#define BEE_BT_COEX_I_0 216
```

`BT_COEX_I_0` 引脚复用功能（Pinmux Function）。

<a id="af55b98947776718e3b45e3e4c1636baa"></a>

### `BEE_BT_COEX_I_1`

```c
#define BEE_BT_COEX_I_1 217
```

`BT_COEX_I_1` 引脚复用功能（Pinmux Function）。

<a id="abc580ad83269067b32fb42a476ff1e3d"></a>

### `BEE_BT_COEX_I_2`

```c
#define BEE_BT_COEX_I_2 218
```

`BT_COEX_I_2` 引脚复用功能（Pinmux Function）。

<a id="aae8555c6b679f48d0dcba40191e77166"></a>

### `BEE_BT_COEX_I_3`

```c
#define BEE_BT_COEX_I_3 219
```

`BT_COEX_I_3` 引脚复用功能（Pinmux Function）。

<a id="adf8796c519f840189f367e7acd9e1738"></a>

### `BEE_BT_COEX_O_0`

```c
#define BEE_BT_COEX_O_0 220
```

`BT_COEX_O_0` 引脚复用功能（Pinmux Function）。

<a id="ab67e3e28eda567571d3d7586e94e03da"></a>

### `BEE_BT_COEX_O_1`

```c
#define BEE_BT_COEX_O_1 221
```

`BT_COEX_O_1` 引脚复用功能（Pinmux Function）。

<a id="a4b24f9dbcd7d24128db569fb93d84eef"></a>

### `BEE_BT_COEX_O_2`

```c
#define BEE_BT_COEX_O_2 222
```

`BT_COEX_O_2` 引脚复用功能（Pinmux Function）。

<a id="a786a847e166079b62cb5862573c5aeee"></a>

### `BEE_BT_COEX_O_3`

```c
#define BEE_BT_COEX_O_3 223
```

`BT_COEX_O_3` 引脚复用功能（Pinmux Function）。

<a id="a08612d2752471ed4ed20aff687d20d18"></a>

### `BEE_CARD_DETECT_N_0`

```c
#define BEE_CARD_DETECT_N_0 147
```

`CARD_DETECT_N_0` 引脚复用功能（Pinmux Function）。

<a id="af3cf294ea961f98b078c8ad034fae03d"></a>

### `BEE_CARD_INT_N_SDHC_0`

```c
#define BEE_CARD_INT_N_SDHC_0 150
```

`CARD_INT_N_SDHC_0` 引脚复用功能（Pinmux Function）。

<a id="a60cdc36815f5a5057025a7a4e70e202f"></a>

### `BEE_DACDAT_SPORT0`

```c
#define BEE_DACDAT_SPORT0 175
```

`DACDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a382b0d00ac01e3bff5aa95e1fe1d4b35"></a>

### `BEE_DACDAT_SPORT1`

```c
#define BEE_DACDAT_SPORT1 160
```

`DACDAT_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="aa23ca1adf7da20c2163b2fd78548cc9b"></a>

### `BEE_DIG_DEBUG`

```c
#define BEE_DIG_DEBUG 255
```

`DIG_DEBUG` 引脚复用功能（Pinmux Function）。

<a id="a49516c6243aed5817ba2ae4d6744687b"></a>

### `BEE_DMIC1_CLK`

```c
#define BEE_DMIC1_CLK 162
```

`DMIC1_CLK` 引脚复用功能（Pinmux Function）。

<a id="a8d6a69a1e3591004efb445bd9b3edfb3"></a>

### `BEE_DMIC1_DAT`

```c
#define BEE_DMIC1_DAT 163
```

`DMIC1_DAT` 引脚复用功能（Pinmux Function）。

<a id="a93f3d11e8a6c9fd056bc4e6a2f156989"></a>

### `BEE_DWGPIO`

```c
#define BEE_DWGPIO 89
```

`DWGPIO` 引脚复用功能（Pinmux Function）。

<a id="a510878941f7e323fe7eee5bb1b743c3e"></a>

### `BEE_EN_EXLNA`

```c
#define BEE_EN_EXLNA 228
```

`EN_EXLNA` 引脚复用功能（Pinmux Function）。

<a id="a37c7aeafe54f05e6a267f9f16af25c0c"></a>

### `BEE_EN_EXPA`

```c
#define BEE_EN_EXPA 227
```

`EN_EXPA` 引脚复用功能（Pinmux Function）。

<a id="a70f463ef325204a7874ade112c0993b3"></a>

### `BEE_ENPWM0_N`

```c
#define BEE_ENPWM0_N 66
```

`ENPWM0_N` 引脚复用功能（Pinmux Function）。

<a id="a317e02b0cb9050e461acf3c246be9af4"></a>

### `BEE_ENPWM0_P`

```c
#define BEE_ENPWM0_P 65
```

`ENPWM0_P` 引脚复用功能（Pinmux Function）。

<a id="a6aedfb25152fa14e489451f4678a453e"></a>

### `BEE_ENPWM1_N`

```c
#define BEE_ENPWM1_N 68
```

`ENPWM1_N` 引脚复用功能（Pinmux Function）。

<a id="a5ba16fa5c3475f4714377bd100b10e7b"></a>

### `BEE_ENPWM1_P`

```c
#define BEE_ENPWM1_P 67
```

`ENPWM1_P` 引脚复用功能（Pinmux Function）。

<a id="ae781b89eaf360564a48f1f2bc203e088"></a>

### `BEE_ENPWM2_N`

```c
#define BEE_ENPWM2_N 70
```

`ENPWM2_N` 引脚复用功能（Pinmux Function）。

<a id="a8a5f812e1c4a764f6b549daba4057b43"></a>

### `BEE_ENPWM2_P`

```c
#define BEE_ENPWM2_P 69
```

`ENPWM2_P` 引脚复用功能（Pinmux Function）。

<a id="ac344c7a2b0b5db363875d9439cd7bd22"></a>

### `BEE_ENPWM3_N`

```c
#define BEE_ENPWM3_N 72
```

`ENPWM3_N` 引脚复用功能（Pinmux Function）。

<a id="abc0d7be51b69c2b6feb7933824d6a7ba"></a>

### `BEE_ENPWM3_P`

```c
#define BEE_ENPWM3_P 71
```

`ENPWM3_P` 引脚复用功能（Pinmux Function）。

<a id="ae0341d05951da84bd30617c9dc341628"></a>

### `BEE_I2C0_CLK`

```c
#define BEE_I2C0_CLK 29
```

`I2C0_CLK` 引脚复用功能（Pinmux Function）。

<a id="abf8d90380239e366fb63fd777fb25075"></a>

### `BEE_I2C0_DAT`

```c
#define BEE_I2C0_DAT 30
```

`I2C0_DAT` 引脚复用功能（Pinmux Function）。

<a id="ad89dd6f55609883daef7915f779b193f"></a>

### `BEE_I2C1_CLK`

```c
#define BEE_I2C1_CLK 31
```

`I2C1_CLK` 引脚复用功能（Pinmux Function）。

<a id="aa70f0eb0a8271e9e027a7307e9c2f203"></a>

### `BEE_I2C1_DAT`

```c
#define BEE_I2C1_DAT 32
```

`I2C1_DAT` 引脚复用功能（Pinmux Function）。

<a id="aa6ed0aa3c48770881ba917e57dc08df2"></a>

### `BEE_I2C2_CLK`

```c
#define BEE_I2C2_CLK 33
```

`I2C2_CLK` 引脚复用功能（Pinmux Function）。

<a id="a1252547d18e156d80d5250b328203c2f"></a>

### `BEE_I2C2_DAT`

```c
#define BEE_I2C2_DAT 34
```

`I2C2_DAT` 引脚复用功能（Pinmux Function）。

<a id="a0f6888bef3c7f11e70e8c07267fa2e1f"></a>

### `BEE_I2C3_CLK`

```c
#define BEE_I2C3_CLK 35
```

`I2C3_CLK` 引脚复用功能（Pinmux Function）。

<a id="af1c9332588450b35182481ec351e5455"></a>

### `BEE_I2C3_DAT`

```c
#define BEE_I2C3_DAT 36
```

`I2C3_DAT` 引脚复用功能（Pinmux Function）。

<a id="a73f47af907185a22e8dc672ffa784f47"></a>

### `BEE_I2S1_BCLK_SLAVE`

```c
#define BEE_I2S1_BCLK_SLAVE 199
```

`I2S1_BCLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ac82e2f9e94e04b1f4d362ffbdec5e2d1"></a>

### `BEE_I2S1_LRC_RX_SLAVE`

```c
#define BEE_I2S1_LRC_RX_SLAVE 202
```

`I2S1_LRC_RX_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a9b22ae740c4fd42a120729b44271d1b3"></a>

### `BEE_I2S1_LRC_TX_SLAVE`

```c
#define BEE_I2S1_LRC_TX_SLAVE 198
```

`I2S1_LRC_TX_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a01c614617ff43310d68aeb0e03cb6e13"></a>

### `BEE_I2S1_SDI_SLAVE`

```c
#define BEE_I2S1_SDI_SLAVE 200
```

`I2S1_SDI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="acdd059e8af73a680e06e15951e5a5210"></a>

### `BEE_I2S1_SDO_SLAVE`

```c
#define BEE_I2S1_SDO_SLAVE 201
```

`I2S1_SDO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="aa96a1b1f865f33896d26cb0ebc67a654"></a>

### `BEE_IDLE_MODE`

```c
#define BEE_IDLE_MODE 0
```

`IDLE_MODE` 引脚复用功能（Pinmux Function）。

<a id="ad5404068fcc7bf2e2207f151d7baacc3"></a>

### `BEE_IRDA_RX`

```c
#define BEE_IRDA_RX 91
```

`IRDA_RX` 引脚复用功能（Pinmux Function）。

<a id="aa03d3f61b2ad1379c04e21e409797781"></a>

### `BEE_IRDA_TX`

```c
#define BEE_IRDA_TX 90
```

`IRDA_TX` 引脚复用功能（Pinmux Function）。

<a id="ac011f9b7965756997354ea86afb50678"></a>

### `BEE_ISO7816_CLK`

```c
#define BEE_ISO7816_CLK 86
```

`ISO7816_CLK` 引脚复用功能（Pinmux Function）。

<a id="a35492a7221ec181c25c3ac234b711509"></a>

### `BEE_ISO7816_IO`

```c
#define BEE_ISO7816_IO 87
```

`ISO7816_IO` 引脚复用功能（Pinmux Function）。

<a id="a33a86943fb382af407f1cc041b008fbe"></a>

### `BEE_ISO7816_RST`

```c
#define BEE_ISO7816_RST 85
```

`ISO7816_RST` 引脚复用功能（Pinmux Function）。

<a id="a438124ea813bc335d07ec29dae9f4215"></a>

### `BEE_ISO7816_VCC_EN`

```c
#define BEE_ISO7816_VCC_EN 88
```

`ISO7816_VCC_EN` 引脚复用功能（Pinmux Function）。

<a id="a5feafd3851cdad2ae95d13da759f846a"></a>

### `BEE_KEY_COL_0`

```c
#define BEE_KEY_COL_0 100
```

`KEY_COL_0` 引脚复用功能（Pinmux Function）。

<a id="a041f3ef212cd3b5632534b861cbc261a"></a>

### `BEE_KEY_COL_1`

```c
#define BEE_KEY_COL_1 101
```

`KEY_COL_1` 引脚复用功能（Pinmux Function）。

<a id="a431bd45fe23862cc55fa544d684b92d6"></a>

### `BEE_KEY_COL_10`

```c
#define BEE_KEY_COL_10 110
```

`KEY_COL_10` 引脚复用功能（Pinmux Function）。

<a id="a7164c3dc3423f443cd3e39875702f200"></a>

### `BEE_KEY_COL_11`

```c
#define BEE_KEY_COL_11 111
```

`KEY_COL_11` 引脚复用功能（Pinmux Function）。

<a id="a02b8793d7bbde10e6d31f380f594758d"></a>

### `BEE_KEY_COL_12`

```c
#define BEE_KEY_COL_12 112
```

`KEY_COL_12` 引脚复用功能（Pinmux Function）。

<a id="a1493d93c12d93ca2e0f6dc267651106b"></a>

### `BEE_KEY_COL_13`

```c
#define BEE_KEY_COL_13 113
```

`KEY_COL_13` 引脚复用功能（Pinmux Function）。

<a id="a60a32dd7c97e11c25cfec77882914300"></a>

### `BEE_KEY_COL_14`

```c
#define BEE_KEY_COL_14 114
```

`KEY_COL_14` 引脚复用功能（Pinmux Function）。

<a id="a689da1d4cb37dbb30ceb751a0fa85b33"></a>

### `BEE_KEY_COL_15`

```c
#define BEE_KEY_COL_15 115
```

`KEY_COL_15` 引脚复用功能（Pinmux Function）。

<a id="a369b59d63cc72309486ad36e29b8c6af"></a>

### `BEE_KEY_COL_16`

```c
#define BEE_KEY_COL_16 116
```

`KEY_COL_16` 引脚复用功能（Pinmux Function）。

<a id="a719bdfcc5efd46dcc6dd7c841c0447d4"></a>

### `BEE_KEY_COL_17`

```c
#define BEE_KEY_COL_17 117
```

`KEY_COL_17` 引脚复用功能（Pinmux Function）。

<a id="a53aebd67028abe2a744e11d781ca183f"></a>

### `BEE_KEY_COL_18`

```c
#define BEE_KEY_COL_18 118
```

`KEY_COL_18` 引脚复用功能（Pinmux Function）。

<a id="af444884011ac39c3dcf213a22259c953"></a>

### `BEE_KEY_COL_19`

```c
#define BEE_KEY_COL_19 119
```

`KEY_COL_19` 引脚复用功能（Pinmux Function）。

<a id="a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2"></a>

### `BEE_KEY_COL_2`

```c
#define BEE_KEY_COL_2 102
```

`KEY_COL_2` 引脚复用功能（Pinmux Function）。

<a id="a6faea0c7d7cfbc3557937914a8f3a3b5"></a>

### `BEE_KEY_COL_3`

```c
#define BEE_KEY_COL_3 103
```

`KEY_COL_3` 引脚复用功能（Pinmux Function）。

<a id="ad8b490ea83a896b7c702161613e8351d"></a>

### `BEE_KEY_COL_4`

```c
#define BEE_KEY_COL_4 104
```

`KEY_COL_4` 引脚复用功能（Pinmux Function）。

<a id="afbb2d553138a1242007d6339631adb26"></a>

### `BEE_KEY_COL_5`

```c
#define BEE_KEY_COL_5 105
```

`KEY_COL_5` 引脚复用功能（Pinmux Function）。

<a id="ac549db15241e4a3344a387b5b2188970"></a>

### `BEE_KEY_COL_6`

```c
#define BEE_KEY_COL_6 106
```

`KEY_COL_6` 引脚复用功能（Pinmux Function）。

<a id="aa61ab3cf42f2f48afe802d7cb12f222a"></a>

### `BEE_KEY_COL_7`

```c
#define BEE_KEY_COL_7 107
```

`KEY_COL_7` 引脚复用功能（Pinmux Function）。

<a id="a5d28d0d40e6334592b08698a3f9e0da8"></a>

### `BEE_KEY_COL_8`

```c
#define BEE_KEY_COL_8 108
```

`KEY_COL_8` 引脚复用功能（Pinmux Function）。

<a id="ad2c88795b1b458608caa083d469ee86e"></a>

### `BEE_KEY_COL_9`

```c
#define BEE_KEY_COL_9 109
```

`KEY_COL_9` 引脚复用功能（Pinmux Function）。

<a id="af82f5da17eada898f2dec8de92e603b0"></a>

### `BEE_KEY_ROW_0`

```c
#define BEE_KEY_ROW_0 120
```

`KEY_ROW_0` 引脚复用功能（Pinmux Function）。

<a id="a24e82e85a07c80d7e390185f67726756"></a>

### `BEE_KEY_ROW_1`

```c
#define BEE_KEY_ROW_1 121
```

`KEY_ROW_1` 引脚复用功能（Pinmux Function）。

<a id="a8f0c299784cb107d46fdbcd5494ae2f0"></a>

### `BEE_KEY_ROW_10`

```c
#define BEE_KEY_ROW_10 130
```

`KEY_ROW_10` 引脚复用功能（Pinmux Function）。

<a id="a2386911ec69b7416028fab5537243bee"></a>

### `BEE_KEY_ROW_11`

```c
#define BEE_KEY_ROW_11 131
```

`KEY_ROW_11` 引脚复用功能（Pinmux Function）。

<a id="a695da19fd7bc007959fe2ce9f3882939"></a>

### `BEE_KEY_ROW_2`

```c
#define BEE_KEY_ROW_2 122
```

`KEY_ROW_2` 引脚复用功能（Pinmux Function）。

<a id="a3920941b7c17c1eb9df377230ae0e3d7"></a>

### `BEE_KEY_ROW_3`

```c
#define BEE_KEY_ROW_3 123
```

`KEY_ROW_3` 引脚复用功能（Pinmux Function）。

<a id="a94ce3c3c0775437059fe8d48ca1ae63d"></a>

### `BEE_KEY_ROW_4`

```c
#define BEE_KEY_ROW_4 124
```

`KEY_ROW_4` 引脚复用功能（Pinmux Function）。

<a id="aebdb52372b88e9aa5d7173104f8088c7"></a>

### `BEE_KEY_ROW_5`

```c
#define BEE_KEY_ROW_5 125
```

`KEY_ROW_5` 引脚复用功能（Pinmux Function）。

<a id="a6535c3d5752c54dd36ff7a138cb70b5c"></a>

### `BEE_KEY_ROW_6`

```c
#define BEE_KEY_ROW_6 126
```

`KEY_ROW_6` 引脚复用功能（Pinmux Function）。

<a id="a4762128bf6b6e86a17b3c8c76ff2fc88"></a>

### `BEE_KEY_ROW_7`

```c
#define BEE_KEY_ROW_7 127
```

`KEY_ROW_7` 引脚复用功能（Pinmux Function）。

<a id="abbf110abd0ae22bb4767f28fe5901242"></a>

### `BEE_KEY_ROW_8`

```c
#define BEE_KEY_ROW_8 128
```

`KEY_ROW_8` 引脚复用功能（Pinmux Function）。

<a id="a681b30410bb04208c02a53f158dbedfb"></a>

### `BEE_KEY_ROW_9`

```c
#define BEE_KEY_ROW_9 129
```

`KEY_ROW_9` 引脚复用功能（Pinmux Function）。

<a id="a5c05c2a5a36182329825a24c574d594e"></a>

### `BEE_KM4_CLK_DIV_4`

```c
#define BEE_KM4_CLK_DIV_4 138
```

`KM4_CLK_DIV_4` 引脚复用功能（Pinmux Function）。

<a id="a644fe132bc7a607b715744ae214635af"></a>

### `BEE_LRC_I_CODEC_SLAVE`

```c
#define BEE_LRC_I_CODEC_SLAVE 164
```

`LRC_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a953c02232ba2b750df5eb0a75e299d82"></a>

### `BEE_LRC_RX_CODEC_SLAVE`

```c
#define BEE_LRC_RX_CODEC_SLAVE 190
```

`LRC_RX_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ae32bad8399c8049ede9df9631f3cb1db"></a>

### `BEE_LRC_RX_SPORT0`

```c
#define BEE_LRC_RX_SPORT0 191
```

`LRC_RX_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="aa570f23c69d3e493587d96ea5ca43f79"></a>

### `BEE_LRC_RX_SPORT1`

```c
#define BEE_LRC_RX_SPORT1 192
```

`LRC_RX_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="a44044eb50520f7a0dbf83abe70dc2bc5"></a>

### `BEE_LRC_SPORT0`

```c
#define BEE_LRC_SPORT0 172
```

`LRC_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a4224637824110a64477a8d8890de4533"></a>

### `BEE_LRC_SPORT1`

```c
#define BEE_LRC_SPORT1 157
```

`LRC_SPORT1` 引脚复用功能（Pinmux Function）。

<a id="aa4987bc9633f726511372e806855bb80"></a>

### `BEE_MCLK_IN`

```c
#define BEE_MCLK_IN 189
```

`MCLK_IN` 引脚复用功能（Pinmux Function）。

<a id="ab37d4968f633e5d24d97fe14e6d87178"></a>

### `BEE_MCLK_OUT`

```c
#define BEE_MCLK_OUT 176
```

`MCLK_OUT` 引脚复用功能（Pinmux Function）。

<a id="a586c8e8e4924b2f6f389e36ac3143d94"></a>

### `BEE_PDM_CLK`

```c
#define BEE_PDM_CLK 197
```

`PDM_CLK` 引脚复用功能（Pinmux Function）。

<a id="a3160663a5d36928382923eed0c5cf444"></a>

### `BEE_PDM_DATA`

```c
#define BEE_PDM_DATA 196
```

`PDM_DATA` 引脚复用功能（Pinmux Function）。

<a id="a9abd2808f59a043725e9b441ba0a7114"></a>

### `BEE_PHY_GPIO_1`

```c
#define BEE_PHY_GPIO_1 237
```

`PHY_GPIO_1` 引脚复用功能（Pinmux Function）。

<a id="a69b08b31593daf0fa4f5ee5e6e98c730"></a>

### `BEE_PHY_GPIO_2`

```c
#define BEE_PHY_GPIO_2 238
```

`PHY_GPIO_2` 引脚复用功能（Pinmux Function）。

<a id="a52116a87b4f4fd7ce6beeffbb44030da"></a>

### `BEE_PIN_DISCONNECTED`

```c
#define BEE_PIN_DISCONNECTED BEE_PIN_MSK
```

`PIN_DISCONNECTED` 引脚复用功能（Pinmux Function）。

<a id="a57b4629fefc1551701f145558e57f8fa"></a>

### `BEE_PINMUX_MAX`

```c
#define BEE_PINMUX_MAX (BEE_DIG_DEBUG + 1)
```

`PINMUX_MAX` 引脚复用功能（Pinmux Function）。

<a id="aea3e0359b60d675d4fa8aca9d510810c"></a>

### `BEE_PSEL_GPIOA_0_P0_0`

```c
#define BEE_PSEL_GPIOA_0_P0_0 BEE_PSEL(DWGPIO, P0_0)
```

引脚（Pin）`P0_0` 对应的通用输入／输出（GPIO）为 `GPIOA_0`。

<a id="abe30025d83fff188f15688dc1e0e76c0"></a>

### `BEE_PSEL_GPIOA_10_P1_2`

```c
#define BEE_PSEL_GPIOA_10_P1_2 BEE_PSEL(DWGPIO, P1_2)
```

引脚（Pin）`P1_2` 对应的通用输入／输出（GPIO）为 `GPIOA_10`。

<a id="aa8347a5c9094390be062af3fc3fce746"></a>

### `BEE_PSEL_GPIOA_11_P1_3`

```c
#define BEE_PSEL_GPIOA_11_P1_3 BEE_PSEL(DWGPIO, P1_3)
```

引脚（Pin）`P1_3` 对应的通用输入／输出（GPIO）为 `GPIOA_11`。

<a id="af15b5bd2cdba62aac469dc0e7f34393f"></a>

### `BEE_PSEL_GPIOA_12_P1_4`

```c
#define BEE_PSEL_GPIOA_12_P1_4 BEE_PSEL(DWGPIO, P1_4)
```

引脚（Pin）`P1_4` 对应的通用输入／输出（GPIO）为 `GPIOA_12`。

<a id="a89c10337574bd3702b7462bbc6ff705a"></a>

### `BEE_PSEL_GPIOA_13_P1_5`

```c
#define BEE_PSEL_GPIOA_13_P1_5 BEE_PSEL(DWGPIO, P1_5)
```

引脚（Pin）`P1_5` 对应的通用输入／输出（GPIO）为 `GPIOA_13`。

<a id="a1a2e353f5795551776353f7fb61afc40"></a>

### `BEE_PSEL_GPIOA_14_P1_6`

```c
#define BEE_PSEL_GPIOA_14_P1_6 BEE_PSEL(DWGPIO, P1_6)
```

引脚（Pin）`P1_6` 对应的通用输入／输出（GPIO）为 `GPIOA_14`。

<a id="aa23dc568bb3b72074576ce2247a62158"></a>

### `BEE_PSEL_GPIOA_15_P1_7`

```c
#define BEE_PSEL_GPIOA_15_P1_7 BEE_PSEL(DWGPIO, P1_7)
```

引脚（Pin）`P1_7` 对应的通用输入／输出（GPIO）为 `GPIOA_15`。

<a id="a6c1eb0e99ad648f77b6b3985940f2849"></a>

### `BEE_PSEL_GPIOA_16_P8_0`

```c
#define BEE_PSEL_GPIOA_16_P8_0 BEE_PSEL(DWGPIO, MICBIAS)
```

引脚（Pin）`P8_0` 对应的通用输入／输出（GPIO）为 `GPIOA_16`。

<a id="afd3e6c79aebd096fa0e54c3ff49d460a"></a>

### `BEE_PSEL_GPIOA_17_P8_1`

```c
#define BEE_PSEL_GPIOA_17_P8_1 BEE_PSEL(DWGPIO, XI32K)
```

引脚（Pin）`P8_1` 对应的通用输入／输出（GPIO）为 `GPIOA_17`。

<a id="adb394912fc05a8b68d5fc80a63eabfde"></a>

### `BEE_PSEL_GPIOA_18_P8_2`

```c
#define BEE_PSEL_GPIOA_18_P8_2 BEE_PSEL(DWGPIO, XO32K)
```

引脚（Pin）`P8_2` 对应的通用输入／输出（GPIO）为 `GPIOA_18`。

<a id="a1b523a451f975b6e68dd4ddf05569346"></a>

### `BEE_PSEL_GPIOA_19_P8_3`

```c
#define BEE_PSEL_GPIOA_19_P8_3 BEE_PSEL(DWGPIO, DACP)
```

引脚（Pin）`P8_3` 对应的通用输入／输出（GPIO）为 `GPIOA_19`。

<a id="a43339d36676fe5280317f760c1423ecd"></a>

### `BEE_PSEL_GPIOA_1_P0_1`

```c
#define BEE_PSEL_GPIOA_1_P0_1 BEE_PSEL(DWGPIO, P0_1)
```

引脚（Pin）`P0_1` 对应的通用输入／输出（GPIO）为 `GPIOA_1`。

<a id="a47d84fc152cac7e55eb6b468243c8c1c"></a>

### `BEE_PSEL_GPIOA_20_P8_4`

```c
#define BEE_PSEL_GPIOA_20_P8_4 BEE_PSEL(DWGPIO, DACN)
```

引脚（Pin）`P8_4` 对应的通用输入／输出（GPIO）为 `GPIOA_20`。

<a id="afe602d67f77e61108384d1c1408cb91e"></a>

### `BEE_PSEL_GPIOA_21_P2_0`

```c
#define BEE_PSEL_GPIOA_21_P2_0 BEE_PSEL(DWGPIO, P2_0)
```

引脚（Pin）`P2_0` 对应的通用输入／输出（GPIO）为 `GPIOA_21`。

<a id="ad0a3d8caf8d858135f78df21de96af25"></a>

### `BEE_PSEL_GPIOA_22_P2_1`

```c
#define BEE_PSEL_GPIOA_22_P2_1 BEE_PSEL(DWGPIO, P2_1)
```

引脚（Pin）`P2_1` 对应的通用输入／输出（GPIO）为 `GPIOA_22`。

<a id="afc018ec04dc46953934210304de3ba37"></a>

### `BEE_PSEL_GPIOA_23_P2_2`

```c
#define BEE_PSEL_GPIOA_23_P2_2 BEE_PSEL(DWGPIO, P2_2)
```

引脚（Pin）`P2_2` 对应的通用输入／输出（GPIO）为 `GPIOA_23`。

<a id="a89f189327426220fd0414a0ac5438b4a"></a>

### `BEE_PSEL_GPIOA_24_P2_3`

```c
#define BEE_PSEL_GPIOA_24_P2_3 BEE_PSEL(DWGPIO, P2_3)
```

引脚（Pin）`P2_3` 对应的通用输入／输出（GPIO）为 `GPIOA_24`。

<a id="af9c2916643b38e97d69ffb6cf30c6043"></a>

### `BEE_PSEL_GPIOA_25_P2_4`

```c
#define BEE_PSEL_GPIOA_25_P2_4 BEE_PSEL(DWGPIO, P2_4)
```

引脚（Pin）`P2_4` 对应的通用输入／输出（GPIO）为 `GPIOA_25`。

<a id="a134484fd42f21d66efefbaef0de5986f"></a>

### `BEE_PSEL_GPIOA_26_P2_5`

```c
#define BEE_PSEL_GPIOA_26_P2_5 BEE_PSEL(DWGPIO, P2_5)
```

引脚（Pin）`P2_5` 对应的通用输入／输出（GPIO）为 `GPIOA_26`。

<a id="aac866abdb85b9fb6a1ace78fdb3a6044"></a>

### `BEE_PSEL_GPIOA_27_P2_6`

```c
#define BEE_PSEL_GPIOA_27_P2_6 BEE_PSEL(DWGPIO, P2_6)
```

引脚（Pin）`P2_6` 对应的通用输入／输出（GPIO）为 `GPIOA_27`。

<a id="a212885c412a0155da1b909aaab9bbe5a"></a>

### `BEE_PSEL_GPIOA_28_P2_7`

```c
#define BEE_PSEL_GPIOA_28_P2_7 BEE_PSEL(DWGPIO, P2_7)
```

引脚（Pin）`P2_7` 对应的通用输入／输出（GPIO）为 `GPIOA_28`。

<a id="a4cd98da234f8ba483d1a5e6b1306adf4"></a>

### `BEE_PSEL_GPIOA_29_P3_0`

```c
#define BEE_PSEL_GPIOA_29_P3_0 BEE_PSEL(DWGPIO, P3_0)
```

引脚（Pin）`P3_0` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="a26638afbd96b5b3b8355b0625fc24f19"></a>

### `BEE_PSEL_GPIOA_2_P0_2`

```c
#define BEE_PSEL_GPIOA_2_P0_2 BEE_PSEL(DWGPIO, P0_2)
```

引脚（Pin）`P0_2` 对应的通用输入／输出（GPIO）为 `GPIOA_2`。

<a id="a4f653ba441eb7f69ae79282f3c3ecd0d"></a>

### `BEE_PSEL_GPIOA_30_P3_1`

```c
#define BEE_PSEL_GPIOA_30_P3_1 BEE_PSEL(DWGPIO, P3_1)
```

引脚（Pin）`P3_1` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="aa4e874d88ef66bb6014e63979f68d597"></a>

### `BEE_PSEL_GPIOA_31_P3_2`

```c
#define BEE_PSEL_GPIOA_31_P3_2 BEE_PSEL(DWGPIO, P3_2)
```

引脚（Pin）`P3_2` 对应的通用输入／输出（GPIO）为 `GPIOA_31`。

<a id="a1c8d22ab98b90553b8ab5e25464e345b"></a>

### `BEE_PSEL_GPIOA_3_P0_3`

```c
#define BEE_PSEL_GPIOA_3_P0_3 BEE_PSEL(DWGPIO, P0_3)
```

引脚（Pin）`P0_3` 对应的通用输入／输出（GPIO）为 `GPIOA_3`。

<a id="a234c776bffcb0087f4d9d2cb412a1db9"></a>

### `BEE_PSEL_GPIOA_4_P0_4`

```c
#define BEE_PSEL_GPIOA_4_P0_4 BEE_PSEL(DWGPIO, P0_4)
```

引脚（Pin）`P0_4` 对应的通用输入／输出（GPIO）为 `GPIOA_4`。

<a id="a9e3a999c21864d7a7b092b344730a4cd"></a>

### `BEE_PSEL_GPIOA_5_P0_5`

```c
#define BEE_PSEL_GPIOA_5_P0_5 BEE_PSEL(DWGPIO, P0_5)
```

引脚（Pin）`P0_5` 对应的通用输入／输出（GPIO）为 `GPIOA_5`。

<a id="a7a3a3d65f7ebcd3cdfe49de66066a37a"></a>

### `BEE_PSEL_GPIOA_6_P0_6`

```c
#define BEE_PSEL_GPIOA_6_P0_6 BEE_PSEL(DWGPIO, P0_6)
```

引脚（Pin）`P0_6` 对应的通用输入／输出（GPIO）为 `GPIOA_6`。

<a id="ac4fe279a43adb807fa67538aa8118ee8"></a>

### `BEE_PSEL_GPIOA_7_P0_7`

```c
#define BEE_PSEL_GPIOA_7_P0_7 BEE_PSEL(DWGPIO, P0_7)
```

引脚（Pin）`P0_7` 对应的通用输入／输出（GPIO）为 `GPIOA_7`。

<a id="a454c9df6f1af0e26b69d0efce239cd08"></a>

### `BEE_PSEL_GPIOA_8_P1_0`

```c
#define BEE_PSEL_GPIOA_8_P1_0 BEE_PSEL(DWGPIO, P1_0)
```

引脚（Pin）`P1_0` 对应的通用输入／输出（GPIO）为 `GPIOA_8`。

<a id="ad7f2432b06b8b9e304adbc333a6dd684"></a>

### `BEE_PSEL_GPIOA_9_P1_1`

```c
#define BEE_PSEL_GPIOA_9_P1_1 BEE_PSEL(DWGPIO, P1_1)
```

引脚（Pin）`P1_1` 对应的通用输入／输出（GPIO）为 `GPIOA_9`。

<a id="aa857cff3b0a5a7533c0a5be4d38c9b69"></a>

### `BEE_PSEL_GPIOB_0_P3_3`

```c
#define BEE_PSEL_GPIOB_0_P3_3 BEE_PSEL(DWGPIO, P3_3)
```

引脚（Pin）`P3_3` 对应的通用输入／输出（GPIO）为 `GPIOB_0`。

<a id="ab9ed93bf7dbe9b3630d661e373b4216a"></a>

### `BEE_PSEL_GPIOB_10_P4_5`

```c
#define BEE_PSEL_GPIOB_10_P4_5 BEE_PSEL(DWGPIO, P4_5)
```

引脚（Pin）`P4_5` 对应的通用输入／输出（GPIO）为 `GPIOB_10`。

<a id="a47c881203795793aa10db90a5971e167"></a>

### `BEE_PSEL_GPIOB_11_P4_6`

```c
#define BEE_PSEL_GPIOB_11_P4_6 BEE_PSEL(DWGPIO, P4_6)
```

引脚（Pin）`P4_6` 对应的通用输入／输出（GPIO）为 `GPIOB_11`。

<a id="ab1b450789fe924726dbf7215c1f32bac"></a>

### `BEE_PSEL_GPIOB_12_P4_7`

```c
#define BEE_PSEL_GPIOB_12_P4_7 BEE_PSEL(DWGPIO, P4_7)
```

引脚（Pin）`P4_7` 对应的通用输入／输出（GPIO）为 `GPIOB_12`。

<a id="aa69815c1c28800129fa4d15e0503a5f3"></a>

### `BEE_PSEL_GPIOB_13_P5_0`

```c
#define BEE_PSEL_GPIOB_13_P5_0 BEE_PSEL(DWGPIO, P5_0)
```

引脚（Pin）`P5_0` 对应的通用输入／输出（GPIO）为 `GPIOB_13`。

<a id="a064316a5d726c6493888a95f70ce693c"></a>

### `BEE_PSEL_GPIOB_14_P5_1`

```c
#define BEE_PSEL_GPIOB_14_P5_1 BEE_PSEL(DWGPIO, P5_1)
```

引脚（Pin）`P5_1` 对应的通用输入／输出（GPIO）为 `GPIOB_14`。

<a id="a2d90968c8382a6028f8ebc1b91125fb5"></a>

### `BEE_PSEL_GPIOB_15_P5_2`

```c
#define BEE_PSEL_GPIOB_15_P5_2 BEE_PSEL(DWGPIO, P5_2)
```

引脚（Pin）`P5_2` 对应的通用输入／输出（GPIO）为 `GPIOB_15`。

<a id="ac0381fbf6f98cdb8a654c0240c08fb1e"></a>

### `BEE_PSEL_GPIOB_16_P5_3`

```c
#define BEE_PSEL_GPIOB_16_P5_3 BEE_PSEL(DWGPIO, P5_3)
```

引脚（Pin）`P5_3` 对应的通用输入／输出（GPIO）为 `GPIOB_16`。

<a id="a3b1d923dfac2f8868506c9d533e548c8"></a>

### `BEE_PSEL_GPIOB_17_P5_4`

```c
#define BEE_PSEL_GPIOB_17_P5_4 BEE_PSEL(DWGPIO, P5_4)
```

引脚（Pin）`P5_4` 对应的通用输入／输出（GPIO）为 `GPIOB_17`。

<a id="ae6ffa065d3db9bcffbdcc8da512ac6bf"></a>

### `BEE_PSEL_GPIOB_18_P5_5`

```c
#define BEE_PSEL_GPIOB_18_P5_5 BEE_PSEL(DWGPIO, P5_5)
```

引脚（Pin）`P5_5` 对应的通用输入／输出（GPIO）为 `GPIOB_18`。

<a id="a6290760413dba008f66c2a60a15a881a"></a>

### `BEE_PSEL_GPIOB_19_P5_6`

```c
#define BEE_PSEL_GPIOB_19_P5_6 BEE_PSEL(DWGPIO, P5_6)
```

引脚（Pin）`P5_6` 对应的通用输入／输出（GPIO）为 `GPIOB_19`。

<a id="a079881107a3c542f715866101483c256"></a>

### `BEE_PSEL_GPIOB_19_P6_0`

```c
#define BEE_PSEL_GPIOB_19_P6_0 BEE_PSEL(DWGPIO, P6_0)
```

引脚（Pin）`P6_0` 对应的通用输入／输出（GPIO）为 `GPIOB_19`。

<a id="aab941bb496c9a3b17bf04160f859a5ae"></a>

### `BEE_PSEL_GPIOB_1_P3_4`

```c
#define BEE_PSEL_GPIOB_1_P3_4 BEE_PSEL(DWGPIO, P3_4)
```

引脚（Pin）`P3_4` 对应的通用输入／输出（GPIO）为 `GPIOB_1`。

<a id="adaebe442b7720e8879118cf0909e0f33"></a>

### `BEE_PSEL_GPIOB_20_P5_7`

```c
#define BEE_PSEL_GPIOB_20_P5_7 BEE_PSEL(DWGPIO, P5_7)
```

引脚（Pin）`P5_7` 对应的通用输入／输出（GPIO）为 `GPIOB_20`。

<a id="a84101841d0ad51059acb9e5e0535c5eb"></a>

### `BEE_PSEL_GPIOB_20_P6_1`

```c
#define BEE_PSEL_GPIOB_20_P6_1 BEE_PSEL(DWGPIO, P6_1)
```

引脚（Pin）`P6_1` 对应的通用输入／输出（GPIO）为 `GPIOB_20`。

<a id="aa344f94a8846b70f21cf0c1bf4afa0f5"></a>

### `BEE_PSEL_GPIOB_21_P6_2`

```c
#define BEE_PSEL_GPIOB_21_P6_2 BEE_PSEL(DWGPIO, P6_2)
```

引脚（Pin）`P6_2` 对应的通用输入／输出（GPIO）为 `GPIOB_21`。

<a id="a5aee5e9a60d7f13d9f5401e9a7390f46"></a>

### `BEE_PSEL_GPIOB_21_P9_0`

```c
#define BEE_PSEL_GPIOB_21_P9_0 BEE_PSEL(DWGPIO, P9_0)
```

引脚（Pin）`P9_0` 对应的通用输入／输出（GPIO）为 `GPIOB_21`。

<a id="a71c08b5a045cb5db3a04ab48cd360411"></a>

### `BEE_PSEL_GPIOB_22_P6_3`

```c
#define BEE_PSEL_GPIOB_22_P6_3 BEE_PSEL(DWGPIO, P6_3)
```

引脚（Pin）`P6_3` 对应的通用输入／输出（GPIO）为 `GPIOB_22`。

<a id="a90ed9bd2a5a729b25c56b72e3ba49126"></a>

### `BEE_PSEL_GPIOB_22_P9_1`

```c
#define BEE_PSEL_GPIOB_22_P9_1 BEE_PSEL(DWGPIO, P9_1)
```

引脚（Pin）`P9_1` 对应的通用输入／输出（GPIO）为 `GPIOB_22`。

<a id="abec19f4e9156084584d5af3e96a7b100"></a>

### `BEE_PSEL_GPIOB_23_P6_4`

```c
#define BEE_PSEL_GPIOB_23_P6_4 BEE_PSEL(DWGPIO, P6_4)
```

引脚（Pin）`P6_4` 对应的通用输入／输出（GPIO）为 `GPIOB_23`。

<a id="a2c2d98245c1763b940cbbbf350349cf9"></a>

### `BEE_PSEL_GPIOB_23_P9_2`

```c
#define BEE_PSEL_GPIOB_23_P9_2 BEE_PSEL(DWGPIO, P9_2)
```

引脚（Pin）`P9_2` 对应的通用输入／输出（GPIO）为 `GPIOB_23`。

<a id="ad583fd72055dde27e56d379639798880"></a>

### `BEE_PSEL_GPIOB_24_P6_5`

```c
#define BEE_PSEL_GPIOB_24_P6_5 BEE_PSEL(DWGPIO, P6_5)
```

引脚（Pin）`P6_5` 对应的通用输入／输出（GPIO）为 `GPIOB_24`。

<a id="afae90f1839d1d1bb3845388dedc4ebee"></a>

### `BEE_PSEL_GPIOB_24_P9_3`

```c
#define BEE_PSEL_GPIOB_24_P9_3 BEE_PSEL(DWGPIO, P9_3)
```

引脚（Pin）`P9_3` 对应的通用输入／输出（GPIO）为 `GPIOB_24`。

<a id="a22c869993ed5ebd50847e6637e17fe1b"></a>

### `BEE_PSEL_GPIOB_25_P6_6`

```c
#define BEE_PSEL_GPIOB_25_P6_6 BEE_PSEL(DWGPIO, P6_6)
```

引脚（Pin）`P6_6` 对应的通用输入／输出（GPIO）为 `GPIOB_25`。

<a id="a5528e09208f0499628bdfee4d557d699"></a>

### `BEE_PSEL_GPIOB_25_P9_4`

```c
#define BEE_PSEL_GPIOB_25_P9_4 BEE_PSEL(DWGPIO, P9_4)
```

引脚（Pin）`P9_4` 对应的通用输入／输出（GPIO）为 `GPIOB_25`。

<a id="a16cebe162cc25f6ed05c07854ab00992"></a>

### `BEE_PSEL_GPIOB_26_P6_7`

```c
#define BEE_PSEL_GPIOB_26_P6_7 BEE_PSEL(DWGPIO, P6_7)
```

引脚（Pin）`P6_7` 对应的通用输入／输出（GPIO）为 `GPIOB_26`。

<a id="ac451f0ac4626b20efbd01684f3bbafc9"></a>

### `BEE_PSEL_GPIOB_26_P9_5`

```c
#define BEE_PSEL_GPIOB_26_P9_5 BEE_PSEL(DWGPIO, P9_5)
```

引脚（Pin）`P9_5` 对应的通用输入／输出（GPIO）为 `GPIOB_26`。

<a id="af8d90b08a06dde62cffcd221d64adcea"></a>

### `BEE_PSEL_GPIOB_27_P7_0`

```c
#define BEE_PSEL_GPIOB_27_P7_0 BEE_PSEL(DWGPIO, P7_0)
```

引脚（Pin）`P7_0` 对应的通用输入／输出（GPIO）为 `GPIOB_27`。

<a id="ab334b13e0e286e41d0a3e3163a4c4ce4"></a>

### `BEE_PSEL_GPIOB_27_P9_6`

```c
#define BEE_PSEL_GPIOB_27_P9_6 BEE_PSEL(DWGPIO, P9_6)
```

引脚（Pin）`P9_6` 对应的通用输入／输出（GPIO）为 `GPIOB_27`。

<a id="a310533a04c66382479c7356afdcf5749"></a>

### `BEE_PSEL_GPIOB_28_P7_1`

```c
#define BEE_PSEL_GPIOB_28_P7_1 BEE_PSEL(DWGPIO, P7_1)
```

引脚（Pin）`P7_1` 对应的通用输入／输出（GPIO）为 `GPIOB_28`。

<a id="a84d09985aacd4e9e91224c75a3020aff"></a>

### `BEE_PSEL_GPIOB_28_P9_7`

```c
#define BEE_PSEL_GPIOB_28_P9_7 BEE_PSEL(DWGPIO, P9_7)
```

引脚（Pin）`P9_7` 对应的通用输入／输出（GPIO）为 `GPIOB_28`。

<a id="a7887a1e36f14c8934bf85c8a137e7e72"></a>

### `BEE_PSEL_GPIOB_29_P10_0`

```c
#define BEE_PSEL_GPIOB_29_P10_0 BEE_PSEL(DWGPIO, P10_0)
```

引脚（Pin）`P10_0` 对应的通用输入／输出（GPIO）为 `GPIOB_29`。

<a id="a93ecea9a0885299a6cdc760f71c23a98"></a>

### `BEE_PSEL_GPIOB_29_P7_2`

```c
#define BEE_PSEL_GPIOB_29_P7_2 BEE_PSEL(DWGPIO, P7_2)
```

引脚（Pin）`P7_2` 对应的通用输入／输出（GPIO）为 `GPIOB_29`。

<a id="a051f0125e7669aa84a40e62272ff9abb"></a>

### `BEE_PSEL_GPIOB_2_P3_5`

```c
#define BEE_PSEL_GPIOB_2_P3_5 BEE_PSEL(DWGPIO, P3_5)
```

引脚（Pin）`P3_5` 对应的通用输入／输出（GPIO）为 `GPIOB_2`。

<a id="afe77a8bd153bea08efaf5870c597c250"></a>

### `BEE_PSEL_GPIOB_30_P10_1`

```c
#define BEE_PSEL_GPIOB_30_P10_1 BEE_PSEL(DWGPIO, P10_1)
```

引脚（Pin）`P10_1` 对应的通用输入／输出（GPIO）为 `GPIOB_30`。

<a id="acec4838f3ca65b1987641731fb700f5e"></a>

### `BEE_PSEL_GPIOB_30_P7_3`

```c
#define BEE_PSEL_GPIOB_30_P7_3 BEE_PSEL(DWGPIO, P7_3)
```

引脚（Pin）`P7_3` 对应的通用输入／输出（GPIO）为 `GPIOB_30`。

<a id="af9574261e821d01dce1850883f933020"></a>

### `BEE_PSEL_GPIOB_31_P10_2`

```c
#define BEE_PSEL_GPIOB_31_P10_2 BEE_PSEL(DWGPIO, P10_2)
```

引脚（Pin）`P10_2` 对应的通用输入／输出（GPIO）为 `GPIOB_31`。

<a id="a61493776635cdd949703f611fc874a5f"></a>

### `BEE_PSEL_GPIOB_31_P7_4`

```c
#define BEE_PSEL_GPIOB_31_P7_4 BEE_PSEL(DWGPIO, P7_4)
```

引脚（Pin）`P7_4` 对应的通用输入／输出（GPIO）为 `GPIOB_31`。

<a id="a8a79064fa2f09c40f6da1a57a42f974d"></a>

### `BEE_PSEL_GPIOB_3_P3_6`

```c
#define BEE_PSEL_GPIOB_3_P3_6 BEE_PSEL(DWGPIO, P3_6)
```

引脚（Pin）`P3_6` 对应的通用输入／输出（GPIO）为 `GPIOB_3`。

<a id="a7f0150a901653bd47b0bfc7e7a612e78"></a>

### `BEE_PSEL_GPIOB_4_P3_7`

```c
#define BEE_PSEL_GPIOB_4_P3_7 BEE_PSEL(DWGPIO, P3_7)
```

引脚（Pin）`P3_7` 对应的通用输入／输出（GPIO）为 `GPIOB_4`。

<a id="a042110a436d34f4ba57b93baf532e551"></a>

### `BEE_PSEL_GPIOB_5_P4_0`

```c
#define BEE_PSEL_GPIOB_5_P4_0 BEE_PSEL(DWGPIO, P4_0)
```

引脚（Pin）`P4_0` 对应的通用输入／输出（GPIO）为 `GPIOB_5`。

<a id="ac459d3b2425228b368bd00364c2150e5"></a>

### `BEE_PSEL_GPIOB_6_P4_1`

```c
#define BEE_PSEL_GPIOB_6_P4_1 BEE_PSEL(DWGPIO, P4_1)
```

引脚（Pin）`P4_1` 对应的通用输入／输出（GPIO）为 `GPIOB_6`。

<a id="ab5f4220e46b4f7fb180a40fbc2e814bc"></a>

### `BEE_PSEL_GPIOB_7_P4_2`

```c
#define BEE_PSEL_GPIOB_7_P4_2 BEE_PSEL(DWGPIO, P4_2)
```

引脚（Pin）`P4_2` 对应的通用输入／输出（GPIO）为 `GPIOB_7`。

<a id="ae203cb3fcd4c70a4e3debe1d24b64d1b"></a>

### `BEE_PSEL_GPIOB_8_P4_3`

```c
#define BEE_PSEL_GPIOB_8_P4_3 BEE_PSEL(DWGPIO, P4_3)
```

引脚（Pin）`P4_3` 对应的通用输入／输出（GPIO）为 `GPIOB_8`。

<a id="a029877141321b4eff25b553653d79302"></a>

### `BEE_PSEL_GPIOB_9_P4_4`

```c
#define BEE_PSEL_GPIOB_9_P4_4 BEE_PSEL(DWGPIO, P4_4)
```

引脚（Pin）`P4_4` 对应的通用输入／输出（GPIO）为 `GPIOB_9`。

<a id="abcf72b3e409c194ba2d2173aa7cb41ab"></a>

### `BEE_PTA_I2C_CLK_SLAVE`

```c
#define BEE_PTA_I2C_CLK_SLAVE 224
```

`PTA_I2C_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a9254d4dd1aa797f1590ef84c1cd07ed1"></a>

### `BEE_PTA_I2C_DAT_SLAVE`

```c
#define BEE_PTA_I2C_DAT_SLAVE 225
```

`PTA_I2C_DAT_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a2e6661f9ef9bb93179130a186653468a"></a>

### `BEE_PTA_I2C_INT_OUT`

```c
#define BEE_PTA_I2C_INT_OUT 226
```

`PTA_I2C_INT_OUT` 引脚复用功能（Pinmux Function）。

<a id="a95eb489d18499ff7ce936149d65ff03e"></a>

### `BEE_PWR_OFF`

```c
#define BEE_PWR_OFF (BEE_PINMUX_MAX + 2)
```

`PWR_OFF` 引脚复用功能（Pinmux Function）。

<a id="a1b5b713e05457eff914beceab4922ca9"></a>

### `BEE_QDPH0_IN_NONE`

```c
#define BEE_QDPH0_IN_NONE 0x0F00
```

`QDPH0_IN_NONE` 引脚复用功能（Pinmux Function）。

<a id="a6c2f5d25f68787afeab96c1a74093595"></a>

### `BEE_QDPH0_IN_P1_3_P1_4`

```c
#define BEE_QDPH0_IN_P1_3_P1_4 0x0F01
```

`QDPH0_IN_P1_3_P1_4` 引脚复用功能（Pinmux Function）。

<a id="a6b0e642ce4368bddcc46fa72a808379f"></a>

### `BEE_QDPH0_IN_P5_6_P5_7`

```c
#define BEE_QDPH0_IN_P5_6_P5_7 0x0F02
```

`QDPH0_IN_P5_6_P5_7` 引脚复用功能（Pinmux Function）。

<a id="a0ee761c8fea15ab3f98d92ca8c286413"></a>

### `BEE_QDPH0_IN_P9_0_P9_1`

```c
#define BEE_QDPH0_IN_P9_0_P9_1 0x0F03
```

`QDPH0_IN_P9_0_P9_1` 引脚复用功能（Pinmux Function）。

<a id="a8b07e848c32157c2674c5956a434e877"></a>

### `BEE_SDHC0_CLK_P9_4`

```c
#define BEE_SDHC0_CLK_P9_4 (BEE_PWR_OFF + 1)
```

`SDHC0_CLK_P9_4` 引脚复用功能（Pinmux Function）。

<a id="af0fcff204155abd2033c588ccfcfd43b"></a>

### `BEE_SDHC0_CMD_P9_3`

```c
#define BEE_SDHC0_CMD_P9_3 (BEE_PWR_OFF + 2)
```

`SDHC0_CMD_P9_3` 引脚复用功能（Pinmux Function）。

<a id="a640fef966ab3c588d8b8fe444bf02285"></a>

### `BEE_SDHC0_D0_P10_0`

```c
#define BEE_SDHC0_D0_P10_0 (BEE_PWR_OFF + 3)
```

`SDHC0_D0_P10_0` 引脚复用功能（Pinmux Function）。

<a id="adc5ed31e3bd280c426350a907e127566"></a>

### `BEE_SDHC0_D1_P9_7`

```c
#define BEE_SDHC0_D1_P9_7 (BEE_PWR_OFF + 4)
```

`SDHC0_D1_P9_7` 引脚复用功能（Pinmux Function）。

<a id="aafa319b5c0ea2be2a7504b92b01f9a44"></a>

### `BEE_SDHC0_D2_P9_6`

```c
#define BEE_SDHC0_D2_P9_6 (BEE_PWR_OFF + 5)
```

`SDHC0_D2_P9_6` 引脚复用功能（Pinmux Function）。

<a id="a5bcbca477a418781525d2045f9fd2cb2"></a>

### `BEE_SDHC0_D3_P9_5`

```c
#define BEE_SDHC0_D3_P9_5 (BEE_PWR_OFF + 6)
```

`SDHC0_D3_P9_5` 引脚复用功能（Pinmux Function）。

<a id="a676fbe46df77c712016ebf08684d19cc"></a>

### `BEE_SDHC0_D4_P4_4`

```c
#define BEE_SDHC0_D4_P4_4 (BEE_PWR_OFF + 7)
```

`SDHC0_D4_P4_4` 引脚复用功能（Pinmux Function）。

<a id="a0df0871c36c2e9ca877a46915e6bed5e"></a>

### `BEE_SDHC0_D5_P4_5`

```c
#define BEE_SDHC0_D5_P4_5 (BEE_PWR_OFF + 8)
```

`SDHC0_D5_P4_5` 引脚复用功能（Pinmux Function）。

<a id="af1900d620d09dc71b54d5c51687e9e64"></a>

### `BEE_SDHC0_D6_P4_6`

```c
#define BEE_SDHC0_D6_P4_6 (BEE_PWR_OFF + 9)
```

`SDHC0_D6_P4_6` 引脚复用功能（Pinmux Function）。

<a id="aa2af9a8cb37d9556d9bbfe42f59dc66d"></a>

### `BEE_SDHC0_D7_P4_7`

```c
#define BEE_SDHC0_D7_P4_7 (BEE_PWR_OFF + 10)
```

`SDHC0_D7_P4_7` 引脚复用功能（Pinmux Function）。

<a id="a6a5932281e193bbccf9c4df49cd2cc80"></a>

### `BEE_SDHC1_CLK_P9_4`

```c
#define BEE_SDHC1_CLK_P9_4 (BEE_PWR_OFF + 11)
```

`SDHC1_CLK_P9_4` 引脚复用功能（Pinmux Function）。

<a id="ac5b3ba6fc43f19b40316d8d90f822ea3"></a>

### `BEE_SDHC1_CMD_P9_3`

```c
#define BEE_SDHC1_CMD_P9_3 (BEE_PWR_OFF + 12)
```

`SDHC1_CMD_P9_3` 引脚复用功能（Pinmux Function）。

<a id="a472f94e2e5faf5a32ddb2cdba00fe375"></a>

### `BEE_SDHC1_D0_P10_0`

```c
#define BEE_SDHC1_D0_P10_0 (BEE_PWR_OFF + 13)
```

`SDHC1_D0_P10_0` 引脚复用功能（Pinmux Function）。

<a id="a378f1cf157c1fd2e3422b0875319c2ae"></a>

### `BEE_SDHC1_D1_P9_7`

```c
#define BEE_SDHC1_D1_P9_7 (BEE_PWR_OFF + 14)
```

`SDHC1_D1_P9_7` 引脚复用功能（Pinmux Function）。

<a id="ac49769a013501d1530eb05993fd2b0de"></a>

### `BEE_SDHC1_D2_P9_6`

```c
#define BEE_SDHC1_D2_P9_6 (BEE_PWR_OFF + 15)
```

`SDHC1_D2_P9_6` 引脚复用功能（Pinmux Function）。

<a id="af3447efd95a4854aab04e6f4292a2261"></a>

### `BEE_SDHC1_D3_P9_5`

```c
#define BEE_SDHC1_D3_P9_5 (BEE_PWR_OFF + 16)
```

`SDHC1_D3_P9_5` 引脚复用功能（Pinmux Function）。

<a id="a83e1c3839af29370e73f2629bad3805b"></a>

### `BEE_SDHC1_D4_P4_4`

```c
#define BEE_SDHC1_D4_P4_4 (BEE_PWR_OFF + 17)
```

`SDHC1_D4_P4_4` 引脚复用功能（Pinmux Function）。

<a id="a0d80adeb6f9d66dc4ddd860db2c91ce7"></a>

### `BEE_SDHC1_D5_P4_5`

```c
#define BEE_SDHC1_D5_P4_5 (BEE_PWR_OFF + 18)
```

`SDHC1_D5_P4_5` 引脚复用功能（Pinmux Function）。

<a id="a99e608ea763a7336d7fe7972711bf6f9"></a>

### `BEE_SDHC1_D6_P4_6`

```c
#define BEE_SDHC1_D6_P4_6 (BEE_PWR_OFF + 19)
```

`SDHC1_D6_P4_6` 引脚复用功能（Pinmux Function）。

<a id="af184420e457cbef61065fc6d7b507971"></a>

### `BEE_SDHC1_D7_P4_7`

```c
#define BEE_SDHC1_D7_P4_7 (BEE_PWR_OFF + 20)
```

`SDHC1_D7_P4_7` 引脚复用功能（Pinmux Function）。

<a id="a4210b1402742ed6b988925e93b2fb875"></a>

### `BEE_SDI_CODEC_SLAVE`

```c
#define BEE_SDI_CODEC_SLAVE 166
```

`SDI_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ad8fb809d69f74a7d77283fb004d2f323"></a>

### `BEE_SDO_CODEC_SLAVE`

```c
#define BEE_SDO_CODEC_SLAVE 167
```

`SDO_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a7efece011140a52385c5aabdfc9b941d"></a>

### `BEE_SEL_TPM_N_SW`

```c
#define BEE_SEL_TPM_N_SW 230
```

`SEL_TPM_N_SW` 引脚复用功能（Pinmux Function）。

<a id="a2cf4e89770aa792414e33cbda60c3e88"></a>

### `BEE_SEL_TPM_SW`

```c
#define BEE_SEL_TPM_SW 229
```

`SEL_TPM_SW` 引脚复用功能（Pinmux Function）。

<a id="a7ff4bfbdc644a16d4ba216bb011199fb"></a>

### `BEE_SLOW_DEBUG_MUX_1`

```c
#define BEE_SLOW_DEBUG_MUX_1 239
```

`SLOW_DEBUG_MUX_1` 引脚复用功能（Pinmux Function）。

<a id="a4d6e8a3787f0f21724b0ded1e0708929"></a>

### `BEE_SLOW_DEBUG_MUX_2`

```c
#define BEE_SLOW_DEBUG_MUX_2 240
```

`SLOW_DEBUG_MUX_2` 引脚复用功能（Pinmux Function）。

<a id="ab0446a74b1486abd14de4fd0200ea74f"></a>

### `BEE_SPI0_CLK_MASTER`

```c
#define BEE_SPI0_CLK_MASTER 37
```

`SPI0_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="aa74d6d5790ee4b6c3804612d13ac2b5b"></a>

### `BEE_SPI0_CLK_SLAVE`

```c
#define BEE_SPI0_CLK_SLAVE 44
```

`SPI0_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="adad5ada055c3c4d60d2600b1fe3fa1c5"></a>

### `BEE_SPI0_CSN_0_MASTER`

```c
#define BEE_SPI0_CSN_0_MASTER 40
```

`SPI0_CSN_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a3f0252d61a75a19686b709fc0f9626a1"></a>

### `BEE_SPI0_CSN_0_SLAVE`

```c
#define BEE_SPI0_CSN_0_SLAVE 43
```

`SPI0_CSN_0_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a4ba241d2467358de0b0ba6ab90486053"></a>

### `BEE_SPI0_CSN_1_MASTER`

```c
#define BEE_SPI0_CSN_1_MASTER 41
```

`SPI0_CSN_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ac2cb7c98322526828aac27e9f07b60f2"></a>

### `BEE_SPI0_CSN_2_MASTER`

```c
#define BEE_SPI0_CSN_2_MASTER 42
```

`SPI0_CSN_2_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ad0da29a2b105520d4b082c3995738a7c"></a>

### `BEE_SPI0_MI_MASTER`

```c
#define BEE_SPI0_MI_MASTER 39
```

`SPI0_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ae4d7727fa011b264c2262f8a93286b79"></a>

### `BEE_SPI0_MO_MASTER`

```c
#define BEE_SPI0_MO_MASTER 38
```

`SPI0_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a42c6b4ef4945aa8dacaf653acffae16f"></a>

### `BEE_SPI0_SI_SLAVE`

```c
#define BEE_SPI0_SI_SLAVE 46
```

`SPI0_SI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ad8b8f9abd4e3a9f468621a1bcebc26c5"></a>

### `BEE_SPI0_SO_SLAVE`

```c
#define BEE_SPI0_SO_SLAVE 45
```

`SPI0_SO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a0452a4a0d75d2f3eba6dac55bd4d209c"></a>

### `BEE_SPI1_CLK_MASTER`

```c
#define BEE_SPI1_CLK_MASTER 47
```

`SPI1_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ad13d417d2d2a380af4b615291036785f"></a>

### `BEE_SPI1_CSN_0_MASTER`

```c
#define BEE_SPI1_CSN_0_MASTER 50
```

`SPI1_CSN_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="aec9bc8d94e3f80753439f36db561936f"></a>

### `BEE_SPI1_CSN_1_MASTER`

```c
#define BEE_SPI1_CSN_1_MASTER 51
```

`SPI1_CSN_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ac5545ab44020d7ce32146251a5306f01"></a>

### `BEE_SPI1_CSN_2_MASTER`

```c
#define BEE_SPI1_CSN_2_MASTER 52
```

`SPI1_CSN_2_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a8064446640a0d1ff045af352b0da6670"></a>

### `BEE_SPI1_MI_MASTER`

```c
#define BEE_SPI1_MI_MASTER 49
```

`SPI1_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a113270bda7f1996417ae86e9d59f7c6e"></a>

### `BEE_SPI1_MO_MASTER`

```c
#define BEE_SPI1_MO_MASTER 48
```

`SPI1_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a3c97c43a62a7d802368350c585342a3d"></a>

### `BEE_SPI2W_CLK`

```c
#define BEE_SPI2W_CLK 54
```

`SPI2W_CLK` 引脚复用功能（Pinmux Function）。

<a id="abf0b517038a65b54ce1fe74e354c8242"></a>

### `BEE_SPI2W_CS`

```c
#define BEE_SPI2W_CS 55
```

`SPI2W_CS` 引脚复用功能（Pinmux Function）。

<a id="a7051bd1175f9fa98e28c31da2e3f82bf"></a>

### `BEE_SPI2W_DATA`

```c
#define BEE_SPI2W_DATA 53
```

`SPI2W_DATA` 引脚复用功能（Pinmux Function）。

<a id="a2207ba441c0defde698d2d1a49cb744d"></a>

### `BEE_SW_MODE`

```c
#define BEE_SW_MODE (BEE_PINMUX_MAX + 1)
```

`SW_MODE` 引脚复用功能（Pinmux Function）。

<a id="a69b18937baf0d37c1302b897a29d0f0d"></a>

### `BEE_SWD_CLK`

```c
#define BEE_SWD_CLK 253
```

`SWD_CLK` 引脚复用功能（Pinmux Function）。

<a id="a890a338c14aef5eb8e25844201b0289d"></a>

### `BEE_SWD_DIO`

```c
#define BEE_SWD_DIO 254
```

`SWD_DIO` 引脚复用功能（Pinmux Function）。

<a id="a21637864c0e3b586c21dca96c2691405"></a>

### `BEE_TEST_MODE`

```c
#define BEE_TEST_MODE 246
```

`TEST_MODE` 引脚复用功能（Pinmux Function）。

<a id="a8a0647f117f2ed3706b555900eb2dc72"></a>

### `BEE_TIMER_PWM2`

```c
#define BEE_TIMER_PWM2 83
```

`TIMER_PWM2` 引脚复用功能（Pinmux Function）。

<a id="adf2187d6150b328d2b54e6d0cdf80e60"></a>

### `BEE_TIMER_PWM2_N`

```c
#define BEE_TIMER_PWM2_N 97
```

`TIMER_PWM2_N` 引脚复用功能（Pinmux Function）。

<a id="a53a225ad51952fe99a3b07fccd2eef16"></a>

### `BEE_TIMER_PWM2_P`

```c
#define BEE_TIMER_PWM2_P 96
```

`TIMER_PWM2_P` 引脚复用功能（Pinmux Function）。

<a id="a57bdd180f5ca3fee9e5ca3c8fb9243b3"></a>

### `BEE_TIMER_PWM3`

```c
#define BEE_TIMER_PWM3 84
```

`TIMER_PWM3` 引脚复用功能（Pinmux Function）。

<a id="ae1d65057952dbbfb086c375d8d8b46d2"></a>

### `BEE_TIMER_PWM3_N`

```c
#define BEE_TIMER_PWM3_N 99
```

`TIMER_PWM3_N` 引脚复用功能（Pinmux Function）。

<a id="abf3272d4fda4b0b1653c22a4009fe232"></a>

### `BEE_TIMER_PWM3_P`

```c
#define BEE_TIMER_PWM3_P 98
```

`TIMER_PWM3_P` 引脚复用功能（Pinmux Function）。

<a id="aafdc6f1211c064bf41d81e498019c11b"></a>

### `BEE_TIMER_PWM4`

```c
#define BEE_TIMER_PWM4 92
```

`TIMER_PWM4` 引脚复用功能（Pinmux Function）。

<a id="a357dc7d8566f63bed51117b6d13760b2"></a>

### `BEE_TIMER_PWM5`

```c
#define BEE_TIMER_PWM5 93
```

`TIMER_PWM5` 引脚复用功能（Pinmux Function）。

<a id="a432deff0be5af291d7ba5c6085a95395"></a>

### `BEE_TIMER_PWM6`

```c
#define BEE_TIMER_PWM6 94
```

`TIMER_PWM6` 引脚复用功能（Pinmux Function）。

<a id="a0e72bc44c574f233b01b103a91224f77"></a>

### `BEE_TIMER_PWM7`

```c
#define BEE_TIMER_PWM7 95
```

`TIMER_PWM7` 引脚复用功能（Pinmux Function）。

<a id="af5094e3bfde1cf22e80c9144763940cc"></a>

### `BEE_UART0_CTS`

```c
#define BEE_UART0_CTS 3
```

`UART0_CTS` 引脚复用功能（Pinmux Function）。

<a id="a6ea0a2599d172ee66154a55c6dad1544"></a>

### `BEE_UART0_RTS`

```c
#define BEE_UART0_RTS 4
```

`UART0_RTS` 引脚复用功能（Pinmux Function）。

<a id="a1c7070aee57aedc7f8a131fe34444d60"></a>

### `BEE_UART0_RX`

```c
#define BEE_UART0_RX 2
```

`UART0_RX` 引脚复用功能（Pinmux Function）。

<a id="aba42501ee83715ca6ea53df22183c5f6"></a>

### `BEE_UART0_TX`

```c
#define BEE_UART0_TX 1
```

`UART0_TX` 引脚复用功能（Pinmux Function）。

<a id="ae1a337884566b230fb35533cb45f83ba"></a>

### `BEE_UART1_CTS`

```c
#define BEE_UART1_CTS 7
```

`UART1_CTS` 引脚复用功能（Pinmux Function）。

<a id="abe24c85e1d8f04d29607669efb795a85"></a>

### `BEE_UART1_RTS`

```c
#define BEE_UART1_RTS 8
```

`UART1_RTS` 引脚复用功能（Pinmux Function）。

<a id="a360f04b358a9569940a03d0d19397df3"></a>

### `BEE_UART1_RX`

```c
#define BEE_UART1_RX 6
```

`UART1_RX` 引脚复用功能（Pinmux Function）。

<a id="acf789455a751381f67bb5c0d00144cee"></a>

### `BEE_UART1_TX`

```c
#define BEE_UART1_TX 5
```

`UART1_TX` 引脚复用功能（Pinmux Function）。

<a id="a7efdd2cc3bd5b3e9686ec52348490a21"></a>

### `BEE_UART2_CTS`

```c
#define BEE_UART2_CTS 11
```

`UART2_CTS` 引脚复用功能（Pinmux Function）。

<a id="a9c3102f61a4ea7d46a3b5bb363d8089d"></a>

### `BEE_UART2_RTS`

```c
#define BEE_UART2_RTS 12
```

`UART2_RTS` 引脚复用功能（Pinmux Function）。

<a id="ac0e9e9aae4c3a7542a4283525446151a"></a>

### `BEE_UART2_RX`

```c
#define BEE_UART2_RX 10
```

`UART2_RX` 引脚复用功能（Pinmux Function）。

<a id="a64c1b3bb3de7cbf46f5e15da73dd6af9"></a>

### `BEE_UART2_TX`

```c
#define BEE_UART2_TX 9
```

`UART2_TX` 引脚复用功能（Pinmux Function）。

<a id="a63c515f54930b48ffc8838ab6973220e"></a>

### `BEE_UART3_CTS`

```c
#define BEE_UART3_CTS 15
```

`UART3_CTS` 引脚复用功能（Pinmux Function）。

<a id="a8bce684ba830b2ebff4ddd33139d1238"></a>

### `BEE_UART3_RTS`

```c
#define BEE_UART3_RTS 16
```

`UART3_RTS` 引脚复用功能（Pinmux Function）。

<a id="a8bb702c55c1a5de54a998647c92006b4"></a>

### `BEE_UART3_RX`

```c
#define BEE_UART3_RX 14
```

`UART3_RX` 引脚复用功能（Pinmux Function）。

<a id="ac3f36cfbd9420ac239e8d339bc239ac9"></a>

### `BEE_UART3_TX`

```c
#define BEE_UART3_TX 13
```

`UART3_TX` 引脚复用功能（Pinmux Function）。

<a id="a337d0bc0bfc8512081a1b2e59ac832bb"></a>

### `BEE_UART4_CTS`

```c
#define BEE_UART4_CTS 19
```

`UART4_CTS` 引脚复用功能（Pinmux Function）。

<a id="a24ec0ff6ae46444b58d43817b320769c"></a>

### `BEE_UART4_RTS`

```c
#define BEE_UART4_RTS 20
```

`UART4_RTS` 引脚复用功能（Pinmux Function）。

<a id="a2893d6c80e812e809b2d4c8852bbc85c"></a>

### `BEE_UART4_RX`

```c
#define BEE_UART4_RX 18
```

`UART4_RX` 引脚复用功能（Pinmux Function）。

<a id="a26c87862eb77530af5058bb5710b434d"></a>

### `BEE_UART4_TX`

```c
#define BEE_UART4_TX 17
```

`UART4_TX` 引脚复用功能（Pinmux Function）。

<a id="aaf8ae6ec44aff2fdfc06835b904e2fb9"></a>

### `BEE_UART5_CTS`

```c
#define BEE_UART5_CTS 23
```

`UART5_CTS` 引脚复用功能（Pinmux Function）。

<a id="a4ed28e6a66dfb4cf545d51081c163609"></a>

### `BEE_UART5_RTS`

```c
#define BEE_UART5_RTS 24
```

`UART5_RTS` 引脚复用功能（Pinmux Function）。

<a id="a0f6b987c94ad3bdd648e3996ef632eea"></a>

### `BEE_UART5_RX`

```c
#define BEE_UART5_RX 22
```

`UART5_RX` 引脚复用功能（Pinmux Function）。

<a id="ab925e0d948107471ab1ba3908de5d105"></a>

### `BEE_UART5_TX`

```c
#define BEE_UART5_TX 21
```

`UART5_TX` 引脚复用功能（Pinmux Function）。

<a id="a200aa14859c9a06396c657b688b78fca"></a>

### `DACN`

```c
#define DACN 68
```

引脚（Pin）`P8_4`：通用输入／输出（GPIO）`GPIOA_20`。

<a id="a4d38fe7e6d50f0e97e124814499a029f"></a>

### `DACP`

```c
#define DACP 67
```

引脚（Pin）`P8_3`：通用输入／输出（GPIO）`GPIOA_19`。

<a id="af61dadf194031aa5b73cd036fec71808"></a>

### `MICBIAS`

```c
#define MICBIAS 64
```

引脚（Pin）`P8_0`：通用输入／输出（GPIO）`GPIOA_16`。

<a id="a188735bd8812ee242324075c9cae4e0e"></a>

### `P0_0`

```c
#define P0_0 0
```

通用输入／输出（GPIO）：`GPIOA_0`。

<a id="a6e605c856305ec72ac000d8cc45ab0b9"></a>

### `P0_1`

```c
#define P0_1 1
```

通用输入／输出（GPIO）：`GPIOA_1`。

<a id="a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

### `P0_2`

```c
#define P0_2 2
```

通用输入／输出（GPIO）：`GPIOA_2`。

<a id="ab73f15237a6f8860438ba0359b283686"></a>

### `P0_3`

```c
#define P0_3 3
```

通用输入／输出（GPIO）：`GPIOA_3`。

<a id="a3218b7341a4f084375bade756f108940"></a>

### `P0_4`

```c
#define P0_4 4
```

通用输入／输出（GPIO）：`GPIOA_4`。

<a id="aa1681f3dab52db87cd32f77b20352770"></a>

### `P0_5`

```c
#define P0_5 5
```

通用输入／输出（GPIO）：`GPIOA_5`。

<a id="a990dc4ba08ec342d0bfa50f99d9e1868"></a>

### `P0_6`

```c
#define P0_6 6
```

通用输入／输出（GPIO）：`GPIOA_6`。

<a id="a34087bca5283adcf7cc7c810f30eab80"></a>

### `P0_7`

```c
#define P0_7 7
```

通用输入／输出（GPIO）：`GPIOA_7`。

<a id="ae04128858406c3ffea815d10aa4c249f"></a>

### `P10_0`

```c
#define P10_0 80
```

通用输入／输出（GPIO）：`GPIOB_29`。

<a id="a1f329f65aec3379318a143b72688beaa"></a>

### `P10_1`

```c
#define P10_1 81
```

通用输入／输出（GPIO）：`GPIOB_30`。

<a id="a288626cc26c7738fad61aac371acffa1"></a>

### `P10_2`

```c
#define P10_2 82
```

通用输入／输出（GPIO）：`GPIOB_31`。

<a id="a0a5c0ef038f9728173ca136eed5c9cd2"></a>

### `P1_0`

```c
#define P1_0 8
```

通用输入／输出（GPIO）：`GPIOA_8`。

<a id="aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

### `P1_1`

```c
#define P1_1 9
```

通用输入／输出（GPIO）：`GPIOA_9`。

<a id="a071e0091581eba3bdf70559d215cda5d"></a>

### `P1_2`

```c
#define P1_2 10
```

通用输入／输出（GPIO）：`GPIOA_10`。

<a id="ad2a4d881a3a72ead238fcf2a4aea88bf"></a>

### `P1_3`

```c
#define P1_3 11
```

通用输入／输出（GPIO）：`GPIOA_11`。

<a id="ab65ddc9251137261c8c17b03a415e831"></a>

### `P1_4`

```c
#define P1_4 12
```

通用输入／输出（GPIO）：`GPIOA_12`。

<a id="af610a6265a7bc9f5c44efa18219c5e96"></a>

### `P1_5`

```c
#define P1_5 13
```

通用输入／输出（GPIO）：`GPIOA_13`。

<a id="a9e219f75c65aa5b19d59bd1596b3e548"></a>

### `P1_6`

```c
#define P1_6 14
```

通用输入／输出（GPIO）：`GPIOA_14`。

<a id="a59e6507c1874213b84ae809c24c3a76e"></a>

### `P1_7`

```c
#define P1_7 15
```

通用输入／输出（GPIO）：`GPIOA_15`。

<a id="a5b005e989c9ae92562196f830232dc1a"></a>

### `P2_0`

```c
#define P2_0 16
```

通用输入／输出（GPIO）：`GPIOA_21`。

<a id="aaae6a77f4b93ec74cb11947217dd8fd1"></a>

### `P2_1`

```c
#define P2_1 17
```

通用输入／输出（GPIO）：`GPIOA_22`。

<a id="a9216eb7ac06cf1906b8c3e6884943b5e"></a>

### `P2_2`

```c
#define P2_2 18
```

通用输入／输出（GPIO）：`GPIOA_23`。

<a id="a98005d211f8692aa984d81e1b1cefd67"></a>

### `P2_3`

```c
#define P2_3 19
```

通用输入／输出（GPIO）：`GPIOA_24`。

<a id="a541f1278e79f6ce8b83f48b5f3e1c177"></a>

### `P2_4`

```c
#define P2_4 20
```

通用输入／输出（GPIO）：`GPIOA_25`。

<a id="acf47cd715ad993d583a85ef8fcac6b3e"></a>

### `P2_5`

```c
#define P2_5 21
```

通用输入／输出（GPIO）：`GPIOA_26`。

<a id="aaf264201304e2d44dc57b61eaf041654"></a>

### `P2_6`

```c
#define P2_6 22
```

通用输入／输出（GPIO）：`GPIOA_27`。

<a id="a4f3e81fec0b7d90e9ff61bae35882c8a"></a>

### `P2_7`

```c
#define P2_7 23
```

通用输入／输出（GPIO）：`GPIOA_28`。

<a id="a335073a6b45e1affb80cb03be0aebd28"></a>

### `P3_0`

```c
#define P3_0 24
```

通用输入／输出（GPIO）：`GPIOA_29`。

<a id="aa56aef7e8461bcefa151ed84ab438dd9"></a>

### `P3_1`

```c
#define P3_1 25
```

通用输入／输出（GPIO）：`GPIOA_30`。

<a id="a7060bd469f1a43b0d5c130d35f291687"></a>

### `P3_2`

```c
#define P3_2 26
```

通用输入／输出（GPIO）：`GPIOA_31`。

<a id="a3394fd21eaccbcd6bfb4cc9a20a93f63"></a>

### `P3_3`

```c
#define P3_3 27
```

通用输入／输出（GPIO）：`GPIOB_0`。

<a id="a444f7e1de792cb878057f9fedf8c1e92"></a>

### `P3_4`

```c
#define P3_4 28
```

通用输入／输出（GPIO）：`GPIOB_1`。

<a id="add5e9628720a9e18e34d148c5e4386ae"></a>

### `P3_5`

```c
#define P3_5 29
```

通用输入／输出（GPIO）：`GPIOB_2`。

<a id="a5f901ec132df36067c1aebb4f0f5e99e"></a>

### `P3_6`

```c
#define P3_6 30
```

通用输入／输出（GPIO）：`GPIOB_3`。

<a id="a1f282bc8f04faf3b85e6aee0891fd9ea"></a>

### `P3_7`

```c
#define P3_7 31
```

通用输入／输出（GPIO）：`GPIOB_4`。

<a id="a7d02796f1733eadcc315008ac83e939a"></a>

### `P4_0`

```c
#define P4_0 32
```

通用输入／输出（GPIO）：`GPIOB_5`。

<a id="adbc665f56899cd3fa782adc76a77087f"></a>

### `P4_1`

```c
#define P4_1 33
```

通用输入／输出（GPIO）：`GPIOB_6`。

<a id="aef67ce6b9c7f16a266927b0545631bc2"></a>

### `P4_2`

```c
#define P4_2 34
```

通用输入／输出（GPIO）：`GPIOB_7`。

<a id="a57a1bc2364d61983bdf84d6e8a7cda5b"></a>

### `P4_3`

```c
#define P4_3 35
```

通用输入／输出（GPIO）：`GPIOB_8`。

<a id="acefb8edcc0cfd596683c3936d70045f3"></a>

### `P4_4`

```c
#define P4_4 36
```

通用输入／输出（GPIO）：`GPIOB_9`。

<a id="a5c377041cd591cac2023bfadfb870c02"></a>

### `P4_5`

```c
#define P4_5 37
```

通用输入／输出（GPIO）：`GPIOB_10`。

<a id="af635e5f062246f82e14430fd5b7a37a1"></a>

### `P4_6`

```c
#define P4_6 38
```

通用输入／输出（GPIO）：`GPIOB_11`。

<a id="a32a4e75f5c818be26a6dc9e43942fc28"></a>

### `P4_7`

```c
#define P4_7 39
```

通用输入／输出（GPIO）：`GPIOB_12`。

<a id="ae2df503cdc1c77adb2d1580335feb8f5"></a>

### `P5_0`

```c
#define P5_0 40
```

通用输入／输出（GPIO）：`GPIOB_13`。

<a id="aaec8c9b05d0535f709f9e40ededd5ae8"></a>

### `P5_1`

```c
#define P5_1 41
```

通用输入／输出（GPIO）：`GPIOB_14`。

<a id="ae908c3f54860d6e0d70a10bbc5b19aae"></a>

### `P5_2`

```c
#define P5_2 42
```

通用输入／输出（GPIO）：`GPIOB_15`。

<a id="a7a4467dbbab48a7c9ad76582e617b0dd"></a>

### `P5_3`

```c
#define P5_3 43
```

通用输入／输出（GPIO）：`GPIOB_16`。

<a id="aab394dcb2ec36fea0ce24796706fd674"></a>

### `P5_4`

```c
#define P5_4 44
```

通用输入／输出（GPIO）：`GPIOB_17`。

<a id="a72ec4d5f289f6ce9cc73197b8ff69847"></a>

### `P5_5`

```c
#define P5_5 45
```

通用输入／输出（GPIO）：`GPIOB_18`。

<a id="ac5ae5e9f17ebefe7fd99c62410fb29f7"></a>

### `P5_6`

```c
#define P5_6 46
```

通用输入／输出（GPIO）：`GPIOB_19`。

<a id="a0e7b711978feec1b1081f899e35e733c"></a>

### `P5_7`

```c
#define P5_7 47
```

通用输入／输出（GPIO）：`GPIOB_20`。

<a id="ab138af2ef513e31f72e0eb3c15415c16"></a>

### `P6_0`

```c
#define P6_0 48
```

通用输入／输出（GPIO）：`GPIOB_19`。

<a id="af718f3ffb7b29dda41400081d8c39fe5"></a>

### `P6_1`

```c
#define P6_1 49
```

通用输入／输出（GPIO）：`GPIOB_20`。

<a id="a106310233e1c55e02634f43b461342b6"></a>

### `P6_2`

```c
#define P6_2 50
```

通用输入／输出（GPIO）：`GPIOB_21`。

<a id="a2e9a52f7ca28ac87076e180001d328e1"></a>

### `P6_3`

```c
#define P6_3 51
```

通用输入／输出（GPIO）：`GPIOB_22`。

<a id="a4f71151e2704238eca74acd651186997"></a>

### `P6_4`

```c
#define P6_4 52
```

通用输入／输出（GPIO）：`GPIOB_23`。

<a id="a130567ee98be683fe6f1f726f9446d6c"></a>

### `P6_5`

```c
#define P6_5 53
```

通用输入／输出（GPIO）：`GPIOB_24`。

<a id="a63c2878cb1bb26b97a50cbbf75f6c87e"></a>

### `P6_6`

```c
#define P6_6 54
```

通用输入／输出（GPIO）：`GPIOB_25`。

<a id="aa6d134e0c1a86dcc7af38fc81025ba79"></a>

### `P6_7`

```c
#define P6_7 55
```

通用输入／输出（GPIO）：`GPIOB_26`。

<a id="a3e7831712fce0e5bed27b0f10d398138"></a>

### `P7_0`

```c
#define P7_0 56
```

通用输入／输出（GPIO）：`GPIOB_27`。

<a id="ac372dcfaf7c262b9c3a6a8098a449944"></a>

### `P7_1`

```c
#define P7_1 57
```

通用输入／输出（GPIO）：`GPIOB_28`。

<a id="a0878dac76551e9d725850af8fcd1a4a6"></a>

### `P7_2`

```c
#define P7_2 58
```

通用输入／输出（GPIO）：`GPIOB_29`。

<a id="abff6873e818564215a355a4eb5d1196e"></a>

### `P7_3`

```c
#define P7_3 59
```

通用输入／输出（GPIO）：`GPIOB_30`。

<a id="a0050eb943971937ee46a80e7eeffa668"></a>

### `P7_4`

```c
#define P7_4 60
```

通用输入／输出（GPIO）：`GPIOB_31`。

<a id="acb0b166bac2f584c7d0d5426423d0903"></a>

### `P9_0`

```c
#define P9_0 72
```

通用输入／输出（GPIO）：`GPIOB_21`。

<a id="a16d9deedb2b362894e322dcf774e606e"></a>

### `P9_1`

```c
#define P9_1 73
```

通用输入／输出（GPIO）：`GPIOB_22`。

<a id="a56f01131e1920415b52b4fed7ded208c"></a>

### `P9_2`

```c
#define P9_2 74
```

通用输入／输出（GPIO）：`GPIOB_23`。

<a id="a0821ae65c3b727af99d77f5bb5300109"></a>

### `P9_3`

```c
#define P9_3 75
```

通用输入／输出（GPIO）：`GPIOB_24`。

<a id="ac5e71bd34f936ea1b3b052bef23230f7"></a>

### `P9_4`

```c
#define P9_4 76
```

通用输入／输出（GPIO）：`GPIOB_25`。

<a id="ab0e4f6e7ddd83730889485a12baf1d39"></a>

### `P9_5`

```c
#define P9_5 77
```

通用输入／输出（GPIO）：`GPIOB_26`。

<a id="a90dd0717671e40593b86be768a283d55"></a>

### `P9_6`

```c
#define P9_6 78
```

通用输入／输出（GPIO）：`GPIOB_27`。

<a id="ad164655c022af1461aa791efe3b7081c"></a>

### `P9_7`

```c
#define P9_7 79
```

通用输入／输出（GPIO）：`GPIOB_28`。

<a id="abf8e89f1d9b5c134447644f741b57c41"></a>

### `XI32K`

```c
#define XI32K 65
```

引脚（Pin）`P8_1`：通用输入／输出（GPIO）`GPIOA_17`。

<a id="a805b514cc17d3f7de5f429d6ad10bc42"></a>

### `XO32K`

```c
#define XO32K 66
```

引脚（Pin）`P8_2`：通用输入／输出（GPIO）`GPIOA_18`。


## 6.3\_原页交叉引用（Cross References）

- [bee-pinctrl.h](../api_source_reference/P057_bee-pinctrl.h_源码浏览.md)
- [查看此文件的源码。](../api_source_compiler_device_reference/P020_rtl87x2g-pinctrl.h_源码浏览.md)
- [BEE_PIN_MSK](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a8514aca71581788b4e134f74d81bcd45)
- [BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P005_zephyr__dt-bindings__pinctrl__rtl8752h-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P007_zephyr__drivers__firmware__tisci__tisci.h_文件参考.md)
