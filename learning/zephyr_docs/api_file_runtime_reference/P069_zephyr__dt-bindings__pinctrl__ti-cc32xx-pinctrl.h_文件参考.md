---
id: learning.zephyr-docs.api-file-runtime-reference.page-69
title: zephyr__dt-bindings__pinctrl__ti-cc32xx-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ti-cc32xx-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti-cc32xx-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 69.1\_宏定义（Macros）

<a id="r_a4bf6d48b1ebcaaeb96b0450533dfa428"></a>

```c
#define TI_CC32XX_PINMUX(pin, mux)
```

相关声明：[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

构造 TI CC32XX `pinmux` 属性条目的工具宏（Utility Macro）。

<a id="define-members-0"></a>

### TI CC32XX 引脚配置位域的位置与掩码（Bit Field Positions and Masks）

<a id="r_a40cc14e2a5969a01d7a764fb5bdb84a7"></a>

```c
#define TI_CC32XX_PIN_MSK 0x3FU
```

相关声明：[TI_CC32XX_PIN_MSK](#a40cc14e2a5969a01d7a764fb5bdb84a7)。

<a id="r_aea6f7d34537febd574f9ea0db1fbf3f3"></a>

```c
#define TI_CC32XX_PIN_POS 16U
```

相关声明：[TI_CC32XX_PIN_POS](#aea6f7d34537febd574f9ea0db1fbf3f3)。

<a id="r_a381590ba2880c42636058c248f7e0e2e"></a>

```c
#define TI_CC32XX_MUX_MSK 0xFU
```

相关声明：[TI_CC32XX_MUX_MSK](#a381590ba2880c42636058c248f7e0e2e)。

<a id="r_ac9e2e00ac00ddd1eaf84331d18806339"></a>

```c
#define TI_CC32XX_MUX_POS 0U
```

相关声明：[TI_CC32XX_MUX_POS](#ac9e2e00ac00ddd1eaf84331d18806339)。

<a id="define-members-1"></a>

### TI CC32XX 引脚控制功能（Pinctrl Pin Functions；参考 SWRU465）

<a id="r_a89f97aa766818f7482c3131b39fc57c6"></a>

```c
#define GPIO10_P1 TI_CC32XX_PINMUX(1U, 0U)
```

相关声明：[GPIO10_P1](#a89f97aa766818f7482c3131b39fc57c6)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_abd05f625495d2ea978dd73f2163ac895"></a>

```c
#define I2C_SCL_P1 TI_CC32XX_PINMUX(1U, 1U)
```

相关声明：[I2C_SCL_P1](#abd05f625495d2ea978dd73f2163ac895)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a1b2e5aea3aad1cf49a0c9ed9c1abd0ac"></a>

```c
#define GT_PWM06_P1 TI_CC32XX_PINMUX(1U, 3U)
```

相关声明：[GT_PWM06_P1](#a1b2e5aea3aad1cf49a0c9ed9c1abd0ac)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a995c80839609dc2f99440020c4b376c4"></a>

```c
#define UART1_TX_P1 TI_CC32XX_PINMUX(1U, 7U)
```

相关声明：[UART1_TX_P1](#a995c80839609dc2f99440020c4b376c4)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0348e53054efacbcc5f4b36f5983b483"></a>

```c
#define SDCARD_CLK_P1 TI_CC32XX_PINMUX(1U, 6U)
```

相关声明：[SDCARD_CLK_P1](#a0348e53054efacbcc5f4b36f5983b483)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a41832e073da75fce278ea3f3a10c7981"></a>

```c
#define GT_CCP01_P1 TI_CC32XX_PINMUX(1U, 12U)
```

相关声明：[GT_CCP01_P1](#a41832e073da75fce278ea3f3a10c7981)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a092456dadbe48fb30ca448f893ff182d"></a>

```c
#define GPIO11_P2 TI_CC32XX_PINMUX(2U, 0U)
```

相关声明：[GPIO11_P2](#a092456dadbe48fb30ca448f893ff182d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a38fbe2595b40a64618809999d9ff7e88"></a>

```c
#define I2C_SDA_P2 TI_CC32XX_PINMUX(2U, 1U)
```

相关声明：[I2C_SDA_P2](#a38fbe2595b40a64618809999d9ff7e88)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a158549be521c32cbadd7fd94a59bc945"></a>

```c
#define GT_PWM07_P2 TI_CC32XX_PINMUX(2U, 3U)
```

相关声明：[GT_PWM07_P2](#a158549be521c32cbadd7fd94a59bc945)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af0194d8218ffae6e4ca6afdc1b75184c"></a>

```c
#define PXCLK_P2 TI_CC32XX_PINMUX(2U, 4U)
```

相关声明：[PXCLK_P2](#af0194d8218ffae6e4ca6afdc1b75184c)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af4b6115dd55265aa56f4fd0e4519449d"></a>

```c
#define SDCARD_CMD_P2 TI_CC32XX_PINMUX(2U, 6U)
```

相关声明：[SDCARD_CMD_P2](#af4b6115dd55265aa56f4fd0e4519449d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a6c343f9636e9d3b43d19b3d0fe9f00b1"></a>

```c
#define UART1_RX_P2 TI_CC32XX_PINMUX(2U, 7U)
```

相关声明：[UART1_RX_P2](#a6c343f9636e9d3b43d19b3d0fe9f00b1)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a29f1d9fd07affc428b9ec13021951496"></a>

```c
#define GT_CCP02_P2 TI_CC32XX_PINMUX(2U, 12U)
```

相关声明：[GT_CCP02_P2](#a29f1d9fd07affc428b9ec13021951496)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af81018b6a0cfba2b48bcdc9cf864d609"></a>

```c
#define MCAFSX_P2 TI_CC32XX_PINMUX(2U, 13U)
```

相关声明：[MCAFSX_P2](#af81018b6a0cfba2b48bcdc9cf864d609)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa7fe336032aa6ad0cc8377bef839c249"></a>

```c
#define GPIO12_P3 TI_CC32XX_PINMUX(3U, 0U)
```

相关声明：[GPIO12_P3](#aa7fe336032aa6ad0cc8377bef839c249)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a449900e101576c23577ae8731ff6d832"></a>

```c
#define MCACLK_P3 TI_CC32XX_PINMUX(3U, 3U)
```

相关声明：[MCACLK_P3](#a449900e101576c23577ae8731ff6d832)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a040fa03ccf78c01cf8353dfafaed4363"></a>

```c
#define PVS_P3 TI_CC32XX_PINMUX(3U, 4U)
```

相关声明：[PVS_P3](#a040fa03ccf78c01cf8353dfafaed4363)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a7f43eaa1290d1c51ad8dd0eead54eac8"></a>

```c
#define I2C_SCL_P3 TI_CC32XX_PINMUX(3U, 5U)
```

相关声明：[I2C_SCL_P3](#a7f43eaa1290d1c51ad8dd0eead54eac8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0a31d5b2068953d90f7e152cfdeec235"></a>

```c
#define UART0_TX_P3 TI_CC32XX_PINMUX(3U, 7U)
```

相关声明：[UART0_TX_P3](#a0a31d5b2068953d90f7e152cfdeec235)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a11be8733f58686a917f33eebc3f83f9f"></a>

```c
#define GT_CCP03_P3 TI_CC32XX_PINMUX(3U, 12U)
```

相关声明：[GT_CCP03_P3](#a11be8733f58686a917f33eebc3f83f9f)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa63a6fa68392be5d91f17f1512bca933"></a>

```c
#define GPIO13_P4 TI_CC32XX_PINMUX(4U, 0U)
```

相关声明：[GPIO13_P4](#aa63a6fa68392be5d91f17f1512bca933)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2ac054fb4527be70688dfbad814da263"></a>

```c
#define I2C_SDA_P4 TI_CC32XX_PINMUX(4U, 5U)
```

相关声明：[I2C_SDA_P4](#a2ac054fb4527be70688dfbad814da263)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a784b4247574d785820e1960b77d243f8"></a>

```c
#define PHS_P4 TI_CC32XX_PINMUX(4U, 4U)
```

相关声明：[PHS_P4](#a784b4247574d785820e1960b77d243f8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a8526e278e737f86b5416d2432e06a961"></a>

```c
#define UART0_RX_P4 TI_CC32XX_PINMUX(4U, 7U)
```

相关声明：[UART0_RX_P4](#a8526e278e737f86b5416d2432e06a961)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a469f19224eef6881cc1247eed19c94a9"></a>

```c
#define GT_CCP04_P4 TI_CC32XX_PINMUX(4U, 12U)
```

相关声明：[GT_CCP04_P4](#a469f19224eef6881cc1247eed19c94a9)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a9c9da9f7d6f9b370c7548f936fe70b65"></a>

```c
#define GPIO14_P5 TI_CC32XX_PINMUX(5U, 0U)
```

相关声明：[GPIO14_P5](#a9c9da9f7d6f9b370c7548f936fe70b65)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4894dca0ecb760732bf032d80a6d8a13"></a>

```c
#define I2C_SCL_P5 TI_CC32XX_PINMUX(5U, 5U)
```

相关声明：[I2C_SCL_P5](#a4894dca0ecb760732bf032d80a6d8a13)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0835204b6761fdb5da07401588cb60a8"></a>

```c
#define GSPI_CLK_P5 TI_CC32XX_PINMUX(5U, 7U)
```

相关声明：[GSPI_CLK_P5](#a0835204b6761fdb5da07401588cb60a8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a420084bc2bed97ccfa6cabbdcea111b8"></a>

```c
#define PDATA8_P5 TI_CC32XX_PINMUX(5U, 4U)
```

相关声明：[PDATA8_P5](#a420084bc2bed97ccfa6cabbdcea111b8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a85dd880198761cbddb32b2d482247bfa"></a>

```c
#define GT_CCP05_P5 TI_CC32XX_PINMUX(5U, 12U)
```

相关声明：[GT_CCP05_P5](#a85dd880198761cbddb32b2d482247bfa)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0b94b2938ede1a6d84b397b12399aa58"></a>

```c
#define GPIO15_P6 TI_CC32XX_PINMUX(6U, 0U)
```

相关声明：[GPIO15_P6](#a0b94b2938ede1a6d84b397b12399aa58)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ac8ded51ba9587b17cf1c2565f635a8a2"></a>

```c
#define I2C_SDA_P6 TI_CC32XX_PINMUX(6U, 5U)
```

相关声明：[I2C_SDA_P6](#ac8ded51ba9587b17cf1c2565f635a8a2)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2e33fd1fd267afccbef0ca274336708d"></a>

```c
#define GSPI_MISO_P6 TI_CC32XX_PINMUX(6U, 7U)
```

相关声明：[GSPI_MISO_P6](#a2e33fd1fd267afccbef0ca274336708d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a74f7003fe754549a7abd536ce7ca18e0"></a>

```c
#define PDATA9_P6 TI_CC32XX_PINMUX(6U, 4U)
```

相关声明：[PDATA9_P6](#a74f7003fe754549a7abd536ce7ca18e0)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a1f11274609e837c40dbfcf3f4bb2c65b"></a>

```c
#define SDCARD_DATA3_P6 TI_CC32XX_PINMUX(6U, 8U)
```

相关声明：[SDCARD_DATA3_P6](#a1f11274609e837c40dbfcf3f4bb2c65b)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a912c145e14635c2fade2b206d71df0a3"></a>

```c
#define GT_CCP06_P6 TI_CC32XX_PINMUX(6U, 13U)
```

相关声明：[GT_CCP06_P6](#a912c145e14635c2fade2b206d71df0a3)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a48e7884a7dfad77efe683eea6e678e1b"></a>

```c
#define GPIO16_P7 TI_CC32XX_PINMUX(7U, 0U)
```

相关声明：[GPIO16_P7](#a48e7884a7dfad77efe683eea6e678e1b)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a06cd1b5b0df08a309fc7d9d0eb176948"></a>

```c
#define GSPI_MOSI_P7 TI_CC32XX_PINMUX(7U, 7U)
```

相关声明：[GSPI_MOSI_P7](#a06cd1b5b0df08a309fc7d9d0eb176948)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4ba12e404845b1777c7fc27673a358c6"></a>

```c
#define PDATA10_P7 TI_CC32XX_PINMUX(7U, 4U)
```

相关声明：[PDATA10_P7](#a4ba12e404845b1777c7fc27673a358c6)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a3e9e600bebc357ff182f42317b4fbc5f"></a>

```c
#define UART1_TX_P7 TI_CC32XX_PINMUX(7U, 5U)
```

相关声明：[UART1_TX_P7](#a3e9e600bebc357ff182f42317b4fbc5f)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ad19d6a6d4e575fdedc182d95c426ef7a"></a>

```c
#define SDCARD_CLK_P7 TI_CC32XX_PINMUX(7U, 8U)
```

相关声明：[SDCARD_CLK_P7](#ad19d6a6d4e575fdedc182d95c426ef7a)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2688169c0aa3bfc4333550d77b03f301"></a>

```c
#define GT_CCP07_P7 TI_CC32XX_PINMUX(7U, 13U)
```

相关声明：[GT_CCP07_P7](#a2688169c0aa3bfc4333550d77b03f301)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a499b75b5acdf56015bc34363e8770625"></a>

```c
#define GPIO17_P8 TI_CC32XX_PINMUX(8U, 0U)
```

相关声明：[GPIO17_P8](#a499b75b5acdf56015bc34363e8770625)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a9f7daa4bf7f1e01439d84c58da7c7235"></a>

```c
#define UART1_RX_P8 TI_CC32XX_PINMUX(8U, 5U)
```

相关声明：[UART1_RX_P8](#a9f7daa4bf7f1e01439d84c58da7c7235)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4a2c3ec59d144e1e20147f3fac31c7cf"></a>

```c
#define GSPI_CS_P8 TI_CC32XX_PINMUX(8U, 7U)
```

相关声明：[GSPI_CS_P8](#a4a2c3ec59d144e1e20147f3fac31c7cf)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a23c36223a0811761121eb6992e733191"></a>

```c
#define SDCARD_CMD_P8 TI_CC32XX_PINMUX(8U, 8U)
```

相关声明：[SDCARD_CMD_P8](#a23c36223a0811761121eb6992e733191)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aec9421895f489defea513f9451f19a59"></a>

```c
#define PDATA11_P8 TI_CC32XX_PINMUX(8U, 4U)
```

相关声明：[PDATA11_P8](#aec9421895f489defea513f9451f19a59)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a7bccf18256e2c16eeb9c2712b4123bed"></a>

```c
#define GPIO22_P15 TI_CC32XX_PINMUX(15U, 0U)
```

相关声明：[GPIO22_P15](#a7bccf18256e2c16eeb9c2712b4123bed)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ae4a09b647c36db2a78d4d8a128d47ac5"></a>

```c
#define MCAFSX_P15 TI_CC32XX_PINMUX(15U, 7U)
```

相关声明：[MCAFSX_P15](#ae4a09b647c36db2a78d4d8a128d47ac5)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a93a7b969c1094f0c7a4811218a6d6b05"></a>

```c
#define GT_CCP04_P15 TI_CC32XX_PINMUX(15U, 5U)
```

相关声明：[GT_CCP04_P15](#a93a7b969c1094f0c7a4811218a6d6b05)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a6e86e11b2fa406cf3d0a0ec57d1e856f"></a>

```c
#define GPIO23_P16 TI_CC32XX_PINMUX(16U, 0U)
```

相关声明：[GPIO23_P16](#a6e86e11b2fa406cf3d0a0ec57d1e856f)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa8b475c426b332c82e21567727bb482a"></a>

```c
#define TDI_P16 TI_CC32XX_PINMUX(16U, 1U)
```

相关声明：[TDI_P16](#aa8b475c426b332c82e21567727bb482a)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af2bdaab6fc0f793aee2bc8821869aad6"></a>

```c
#define UART1_TX_P16 TI_CC32XX_PINMUX(16U, 2U)
```

相关声明：[UART1_TX_P16](#af2bdaab6fc0f793aee2bc8821869aad6)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a8267f2892d868a33b27c68ae6673f239"></a>

```c
#define I2C_SCL_P16 TI_CC32XX_PINMUX(16U, 9U)
```

相关声明：[I2C_SCL_P16](#a8267f2892d868a33b27c68ae6673f239)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a80df0d9d7b3c95e556dd6f82f4551f0b"></a>

```c
#define GPIO24_P17 TI_CC32XX_PINMUX(17U, 0U)
```

相关声明：[GPIO24_P17](#a80df0d9d7b3c95e556dd6f82f4551f0b)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a16ea3f7a2cb062dcdab07e50b4f5c049"></a>

```c
#define TDO_P17 TI_CC32XX_PINMUX(17U, 1U)
```

相关声明：[TDO_P17](#a16ea3f7a2cb062dcdab07e50b4f5c049)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a6c881b3b5ceb937e8441bd0cd3b449e8"></a>

```c
#define PWM0_P17 TI_CC32XX_PINMUX(17U, 5U)
```

相关声明：[PWM0_P17](#a6c881b3b5ceb937e8441bd0cd3b449e8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a632c817fbe28a138a9916a4946ee9da5"></a>

```c
#define UART1_RX_P17 TI_CC32XX_PINMUX(17U, 2U)
```

相关声明：[UART1_RX_P17](#a632c817fbe28a138a9916a4946ee9da5)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0b1353bc11a6e1a156c6dbe4e59f74d0"></a>

```c
#define I2C_SDA_P17 TI_CC32XX_PINMUX(17U, 9U)
```

相关声明：[I2C_SDA_P17](#a0b1353bc11a6e1a156c6dbe4e59f74d0)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a3ba8bacb70f2bcadaa6dfd786a673bd7"></a>

```c
#define GT_CCP06_P17 TI_CC32XX_PINMUX(17U, 4U)
```

相关声明：[GT_CCP06_P17](#a3ba8bacb70f2bcadaa6dfd786a673bd7)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a082b74a8cdfc05bef2c377e8d271bac3"></a>

```c
#define MCAFSX_P17 TI_CC32XX_PINMUX(17U, 6U)
```

相关声明：[MCAFSX_P17](#a082b74a8cdfc05bef2c377e8d271bac3)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a91221a9648fa4d08c5b4f928a9756c50"></a>

```c
#define GPIO28_P18 TI_CC32XX_PINMUX(18U, 0U)
```

相关声明：[GPIO28_P18](#a91221a9648fa4d08c5b4f928a9756c50)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af651d7aa9e7ee9ed0f39ea4ea72d6c3b"></a>

```c
#define TCK_P19 TI_CC32XX_PINMUX(19U, 1U)
```

相关声明：[TCK_P19](#af651d7aa9e7ee9ed0f39ea4ea72d6c3b)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a7c7fb987ccc55419a645a4a04b30e200"></a>

```c
#define GT_PWM03_P19 TI_CC32XX_PINMUX(19U, 8U)
```

相关声明：[GT_PWM03_P19](#a7c7fb987ccc55419a645a4a04b30e200)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_abcec00f5b87b8c75cedc5d73ad7107d3"></a>

```c
#define GPIO29_P20 TI_CC32XX_PINMUX(20U, 0U)
```

相关声明：[GPIO29_P20](#abcec00f5b87b8c75cedc5d73ad7107d3)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a5d14159904ec1c4f56c911e643a7eed4"></a>

```c
#define TMS_P20 TI_CC32XX_PINMUX(20U, 1U)
```

相关声明：[TMS_P20](#a5d14159904ec1c4f56c911e643a7eed4)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ab316bbdba3762342b3823d9eee34809d"></a>

```c
#define GPIO25_P21 TI_CC32XX_PINMUX(21U, 0U)
```

相关声明：[GPIO25_P21](#ab316bbdba3762342b3823d9eee34809d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa34e4da30d6f3b91df53e14b195650bc"></a>

```c
#define GT_PWM02_P21 TI_CC32XX_PINMUX(21U, 9U)
```

相关声明：[GT_PWM02_P21](#aa34e4da30d6f3b91df53e14b195650bc)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ad0767fcefbfc59f576341422ab3c466f"></a>

```c
#define MCASFX_P21 TI_CC32XX_PINMUX(21U, 2U)
```

相关声明：[MCASFX_P21](#ad0767fcefbfc59f576341422ab3c466f)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ae4b7bd32af0c430944caa10343c7ba89"></a>

```c
#define ANTSEL1_P29 TI_CC32XX_PINMUX(29U, 0U)
```

相关声明：[ANTSEL1_P29](#ae4b7bd32af0c430944caa10343c7ba89)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a637bd5bc2080ed718ed875255907ab81"></a>

```c
#define ANTSEL2_P30 TI_CC32XX_PINMUX(30U, 0U)
```

相关声明：[ANTSEL2_P30](#a637bd5bc2080ed718ed875255907ab81)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0ad70dd2e46b8e463283999c065b1031"></a>

```c
#define GPIO31_P45 TI_CC32XX_PINMUX(45U, 0U)
```

相关声明：[GPIO31_P45](#a0ad70dd2e46b8e463283999c065b1031)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aec30ecff2290ff162f4940376f092f77"></a>

```c
#define UART0_RX_P45 TI_CC32XX_PINMUX(45U, 9U)
```

相关声明：[UART0_RX_P45](#aec30ecff2290ff162f4940376f092f77)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0c5127de54dfe7be823dbba91260eeb8"></a>

```c
#define MCAFSX_P45 TI_CC32XX_PINMUX(45U, 12U)
```

相关声明：[MCAFSX_P45](#a0c5127de54dfe7be823dbba91260eeb8)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ac379119f98304c790ab8cbba4752feec"></a>

```c
#define UART1_RX_P45 TI_CC32XX_PINMUX(45U, 2U)
```

相关声明：[UART1_RX_P45](#ac379119f98304c790ab8cbba4752feec)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a93408262bf38798525fc1ed43b759759"></a>

```c
#define MCAXR0_P45 TI_CC32XX_PINMUX(45U, 6U)
```

相关声明：[MCAXR0_P45](#a93408262bf38798525fc1ed43b759759)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a41607ce5c19fb904cef1b5b9ff065bca"></a>

```c
#define GSPI_CLK_P45 TI_CC32XX_PINMUX(45U, 7U)
```

相关声明：[GSPI_CLK_P45](#a41607ce5c19fb904cef1b5b9ff065bca)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0023dcef0f950996fb69b99ae6cb7529"></a>

```c
#define GPIO0_P50 TI_CC32XX_PINMUX(50U, 0U)
```

相关声明：[GPIO0_P50](#a0023dcef0f950996fb69b99ae6cb7529)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa8acf830a7e0ba5aef12422b0f594999"></a>

```c
#define UART0_CTSN_P50 TI_CC32XX_PINMUX(50U, 12U)
```

相关声明：[UART0_CTSN_P50](#aa8acf830a7e0ba5aef12422b0f594999)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2c2f38b43528c3d2ed0d909cb276a834"></a>

```c
#define MCAXR1_P50 TI_CC32XX_PINMUX(50U, 6U)
```

相关声明：[MCAXR1_P50](#a2c2f38b43528c3d2ed0d909cb276a834)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4b59e68f954e26a5a22a946c83c7b35c"></a>

```c
#define GT_CCP00_P50 TI_CC32XX_PINMUX(50U, 7U)
```

相关声明：[GT_CCP00_P50](#a4b59e68f954e26a5a22a946c83c7b35c)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a9531166ec008c53ebcb3bb7770bc9cfb"></a>

```c
#define GSPI_CS_P50 TI_CC32XX_PINMUX(50U, 9U)
```

相关声明：[GSPI_CS_P50](#a9531166ec008c53ebcb3bb7770bc9cfb)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_afc79f99843ab6ec1fcc46e475516d3ea"></a>

```c
#define UART1_RTS_P50 TI_CC32XX_PINMUX(50U, 10U)
```

相关声明：[UART1_RTS_P50](#afc79f99843ab6ec1fcc46e475516d3ea)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a202ce4d02639e2277dc70f8c34e96796"></a>

```c
#define UART0_RTS_P50 TI_CC32XX_PINMUX(50U, 3U)
```

相关声明：[UART0_RTS_P50](#a202ce4d02639e2277dc70f8c34e96796)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a92fa65531018efc9a2fe37d1920d609e"></a>

```c
#define MCAXR0_P50 TI_CC32XX_PINMUX(50U, 4U)
```

相关声明：[MCAXR0_P50](#a92fa65531018efc9a2fe37d1920d609e)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a6f73c352c071329e8b51d62272e6b597"></a>

```c
#define GPIO32_P52 TI_CC32XX_PINMUX(52U, 0U)
```

相关声明：[GPIO32_P52](#a6f73c352c071329e8b51d62272e6b597)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4de157ff760a13c620d8bc5730166dfd"></a>

```c
#define MCACLK_P52 TI_CC32XX_PINMUX(52U, 2U)
```

相关声明：[MCACLK_P52](#a4de157ff760a13c620d8bc5730166dfd)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a85e3fa7f05e7b0f8d2b58741d42e90bc"></a>

```c
#define MCAXR0_P52 TI_CC32XX_PINMUX(52U, 4U)
```

相关声明：[MCAXR0_P52](#a85e3fa7f05e7b0f8d2b58741d42e90bc)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ae3dd30595d8647e48844b8b9a204eee4"></a>

```c
#define UART0_RTS_P52 TI_CC32XX_PINMUX(52U, 6U)
```

相关声明：[UART0_RTS_P52](#ae3dd30595d8647e48844b8b9a204eee4)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0472ccf0e3dde61e9b10c4ee44034a05"></a>

```c
#define GSPI_MOSI_P52 TI_CC32XX_PINMUX(52U, 8U)
```

相关声明：[GSPI_MOSI_P52](#a0472ccf0e3dde61e9b10c4ee44034a05)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af1056beafa7c3f45e3096c66e1631096"></a>

```c
#define GPIO30_P53 TI_CC32XX_PINMUX(53U, 0U)
```

相关声明：[GPIO30_P53](#af1056beafa7c3f45e3096c66e1631096)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_afa26fef4c910605bfc58516bba2b0446"></a>

```c
#define UART0_TX_P53 TI_CC32XX_PINMUX(53U, 9U)
```

相关声明：[UART0_TX_P53](#afa26fef4c910605bfc58516bba2b0446)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ad2986e8a3004f19836aaf1264bbb052d"></a>

```c
#define MCACLK_P53 TI_CC32XX_PINMUX(53U, 2U)
```

相关声明：[MCACLK_P53](#ad2986e8a3004f19836aaf1264bbb052d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a8433ec0dd136e712bcffc99562d77a13"></a>

```c
#define MCAFSX_P53 TI_CC32XX_PINMUX(53U, 3U)
```

相关声明：[MCAFSX_P53](#a8433ec0dd136e712bcffc99562d77a13)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ac91e88a5f0e186cea7cf4c1089a93e7e"></a>

```c
#define GT_CCP05_P53 TI_CC32XX_PINMUX(53U, 4U)
```

相关声明：[GT_CCP05_P53](#ac91e88a5f0e186cea7cf4c1089a93e7e)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aaadb7b665b0adb1eed8d7a632c361910"></a>

```c
#define GSPI_MISO_P53 TI_CC32XX_PINMUX(53U, 7U)
```

相关声明：[GSPI_MISO_P53](#aaadb7b665b0adb1eed8d7a632c361910)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a581e291b3887f522a35a7529db6c6a9b"></a>

```c
#define GPIO1_P55 TI_CC32XX_PINMUX(55U, 0U)
```

相关声明：[GPIO1_P55](#a581e291b3887f522a35a7529db6c6a9b)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ae02a8d280e708f2b28314c565b8368c7"></a>

```c
#define UART0_TX_P55 TI_CC32XX_PINMUX(55U, 3U)
```

相关声明：[UART0_TX_P55](#ae02a8d280e708f2b28314c565b8368c7)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_acd84f05bdec8c70ee04acb87020286a1"></a>

```c
#define PCLK_P55 TI_CC32XX_PINMUX(55U, 4U)
```

相关声明：[PCLK_P55](#acd84f05bdec8c70ee04acb87020286a1)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a06c9f6cc98ffdc8b53495a785fbcb3bd"></a>

```c
#define UART1_TX_P55 TI_CC32XX_PINMUX(55U, 6U)
```

相关声明：[UART1_TX_P55](#a06c9f6cc98ffdc8b53495a785fbcb3bd)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a8d323feb4cf8d2264da5f94853acfcd2"></a>

```c
#define GT_CCP01_P55 TI_CC32XX_PINMUX(55U, 7U)
```

相关声明：[GT_CCP01_P55](#a8d323feb4cf8d2264da5f94853acfcd2)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ad92d7838cfa819c6ba4a896101d4ffca"></a>

```c
#define GPIO2_P57 TI_CC32XX_PINMUX(57U, 0U)
```

相关声明：[GPIO2_P57](#ad92d7838cfa819c6ba4a896101d4ffca)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a9220f19106cb9f8840a1b90607948dcc"></a>

```c
#define UART0_RX_P57 TI_CC32XX_PINMUX(57U, 3U)
```

相关声明：[UART0_RX_P57](#a9220f19106cb9f8840a1b90607948dcc)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2a67e698005d5be4baf74216341adf8e"></a>

```c
#define UART1_RX_P57 TI_CC32XX_PINMUX(57U, 6U)
```

相关声明：[UART1_RX_P57](#a2a67e698005d5be4baf74216341adf8e)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af126c52c2ae52c91b68e9184004cfdcf"></a>

```c
#define GT_CCP02_P57 TI_CC32XX_PINMUX(57U, 7U)
```

相关声明：[GT_CCP02_P57](#af126c52c2ae52c91b68e9184004cfdcf)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a70ea8f18a9106a3c5d43bbee1d8af546"></a>

```c
#define GPIO3_P58 TI_CC32XX_PINMUX(58U, 0U)
```

相关声明：[GPIO3_P58](#a70ea8f18a9106a3c5d43bbee1d8af546)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a33fe230e16d7b9ddfc5c4e5f6affa32d"></a>

```c
#define UART1_TX_P58 TI_CC32XX_PINMUX(58U, 6U)
```

相关声明：[UART1_TX_P58](#a33fe230e16d7b9ddfc5c4e5f6affa32d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a97849d9928b913f404d1a7be447051bf"></a>

```c
#define PDATA7_P58 TI_CC32XX_PINMUX(58U, 7U)
```

相关声明：[PDATA7_P58](#a97849d9928b913f404d1a7be447051bf)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa189b623df8558a6438d176fc406abc2"></a>

```c
#define GPIO5_P59 TI_CC32XX_PINMUX(59U, 0U)
```

相关声明：[GPIO5_P59](#aa189b623df8558a6438d176fc406abc2)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a20c1984c49c52b45fb9024d45a0bdb27"></a>

```c
#define UART1_RX_P59 TI_CC32XX_PINMUX(59U, 6U)
```

相关声明：[UART1_RX_P59](#a20c1984c49c52b45fb9024d45a0bdb27)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aa631c65c36a4db5ba54f9603427911d3"></a>

```c
#define PDATA6_P59 TI_CC32XX_PINMUX(59U, 4U)
```

相关声明：[PDATA6_P59](#aa631c65c36a4db5ba54f9603427911d3)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ae248cf8dc867d6f9114cd3aaa51b06ca"></a>

```c
#define GPIO5_P60 TI_CC32XX_PINMUX(60U, 0U)
```

相关声明：[GPIO5_P60](#ae248cf8dc867d6f9114cd3aaa51b06ca)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0a03dacfa4378314839df59511f7af27"></a>

```c
#define PDATA5_P60 TI_CC32XX_PINMUX(60U, 4U)
```

相关声明：[PDATA5_P60](#a0a03dacfa4378314839df59511f7af27)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a7f6eb41b90608548c67fe52ac7285678"></a>

```c
#define MCAXR1_P60 TI_CC32XX_PINMUX(60U, 6U)
```

相关声明：[MCAXR1_P60](#a7f6eb41b90608548c67fe52ac7285678)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_adcfc77087d75e8f687ca40cf102c5672"></a>

```c
#define GT_CCP05_P60 TI_CC32XX_PINMUX(60U, 7U)
```

相关声明：[GT_CCP05_P60](#adcfc77087d75e8f687ca40cf102c5672)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a9fdaf32c4cf8469a4965405f564066dc"></a>

```c
#define GPIO6_P61 TI_CC32XX_PINMUX(61U, 0U)
```

相关声明：[GPIO6_P61](#a9fdaf32c4cf8469a4965405f564066dc)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a68e13f52aab072bee8eed2de25737730"></a>

```c
#define UART0_RTS_P61 TI_CC32XX_PINMUX(61U, 5U)
```

相关声明：[UART0_RTS_P61](#a68e13f52aab072bee8eed2de25737730)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_aca1510ae9b35a8c0f75d486bcd219feb"></a>

```c
#define PDATA4_P61 TI_CC32XX_PINMUX(61U, 4U)
```

相关声明：[PDATA4_P61](#aca1510ae9b35a8c0f75d486bcd219feb)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a182be28929eb2e11c780d3f7bd3914a6"></a>

```c
#define UART1_CTS_P61 TI_CC32XX_PINMUX(61U, 3U)
```

相关声明：[UART1_CTS_P61](#a182be28929eb2e11c780d3f7bd3914a6)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_abebbd1dd7206417c61aff603dc0d3c3a"></a>

```c
#define UART0_CTS_P61 TI_CC32XX_PINMUX(61U, 6U)
```

相关声明：[UART0_CTS_P61](#abebbd1dd7206417c61aff603dc0d3c3a)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a1de5f909c12eadb029562bf14197ffc7"></a>

```c
#define GT_CCP06_P61 TI_CC32XX_PINMUX(61U, 7U)
```

相关声明：[GT_CCP06_P61](#a1de5f909c12eadb029562bf14197ffc7)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a0a6f11f997a0e220dfff39bb2b419219"></a>

```c
#define GPIO7_P62 TI_CC32XX_PINMUX(62U, 0U)
```

相关声明：[GPIO7_P62](#a0a6f11f997a0e220dfff39bb2b419219)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a900e65546f481f00fc2cb80218063bfd"></a>

```c
#define MCACLKX_P62 TI_CC32XX_PINMUX(62U, 13U)
```

相关声明：[MCACLKX_P62](#a900e65546f481f00fc2cb80218063bfd)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2f6c6154904c3dce5496d8c837e4fbf0"></a>

```c
#define UART1_RTS_P62 TI_CC32XX_PINMUX(62U, 3U)
```

相关声明：[UART1_RTS_P62](#a2f6c6154904c3dce5496d8c837e4fbf0)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af4ef5b36c0c036734bd924586fabc519"></a>

```c
#define UART0_RTS_P62 TI_CC32XX_PINMUX(62U, 10U)
```

相关声明：[UART0_RTS_P62](#af4ef5b36c0c036734bd924586fabc519)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a29e0564a1b5101a50836a9cfa97a7a63"></a>

```c
#define UART0_TX_P62 TI_CC32XX_PINMUX(62U, 11U)
```

相关声明：[UART0_TX_P62](#a29e0564a1b5101a50836a9cfa97a7a63)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_ad36e2c84424950a91028054c3499b579"></a>

```c
#define GPIO8_P63 TI_CC32XX_PINMUX(63U, 0U)
```

相关声明：[GPIO8_P63](#ad36e2c84424950a91028054c3499b579)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a2edc3859ba96c9902d3c5eb2298a86ca"></a>

```c
#define SDCARD_IRQ_P63 TI_CC32XX_PINMUX(63U, 6U)
```

相关声明：[SDCARD_IRQ_P63](#a2edc3859ba96c9902d3c5eb2298a86ca)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a24efd787cbb04117197d27289eab0d83"></a>

```c
#define MCAFSX_P63 TI_CC32XX_PINMUX(63U, 7U)
```

相关声明：[MCAFSX_P63](#a24efd787cbb04117197d27289eab0d83)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_af36b5558e59ca508f363a52c3fb180a0"></a>

```c
#define GT_CCP06_P63 TI_CC32XX_PINMUX(63U, 12U)
```

相关声明：[GT_CCP06_P63](#af36b5558e59ca508f363a52c3fb180a0)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a25a3031376018d5d679597770b0552f0"></a>

```c
#define GPIO9_P64 TI_CC32XX_PINMUX(64U, 0U)
```

相关声明：[GPIO9_P64](#a25a3031376018d5d679597770b0552f0)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a4a276c8f1545d3b817ced42811b934f7"></a>

```c
#define GT_PWM05_P64 TI_CC32XX_PINMUX(64U, 3U)
```

相关声明：[GT_PWM05_P64](#a4a276c8f1545d3b817ced42811b934f7)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a18587659510c1d7f7a3fc761b021999d"></a>

```c
#define SDCARD_DATA_P64 TI_CC32XX_PINMUX(64U, 6U)
```

相关声明：[SDCARD_DATA_P64](#a18587659510c1d7f7a3fc761b021999d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a98e96c0252ec68f37144096625e1492d"></a>

```c
#define MCAXR0_P64 TI_CC32XX_PINMUX(64U, 7U)
```

相关声明：[MCAXR0_P64](#a98e96c0252ec68f37144096625e1492d)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

<a id="r_a45b13479b3cdedf5488f122a3b3ec288"></a>

```c
#define GT_CCP00_P64 TI_CC32XX_PINMUX(64U, 12U)
```

相关声明：[GT_CCP00_P64](#a45b13479b3cdedf5488f122a3b3ec288)、[TI_CC32XX_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)。

## 69.2\_详细说明（Detailed Documentation）

<a id="ae4b7bd32af0c430944caa10343c7ba89"></a>

### `ANTSEL1_P29`

```c
#define ANTSEL1_P29 TI_CC32XX_PINMUX(29U, 0U)
```

<a id="a637bd5bc2080ed718ed875255907ab81"></a>

### `ANTSEL2_P30`

```c
#define ANTSEL2_P30 TI_CC32XX_PINMUX(30U, 0U)
```

<a id="a0023dcef0f950996fb69b99ae6cb7529"></a>

### `GPIO0_P50`

```c
#define GPIO0_P50 TI_CC32XX_PINMUX(50U, 0U)
```

<a id="a89f97aa766818f7482c3131b39fc57c6"></a>

### `GPIO10_P1`

```c
#define GPIO10_P1 TI_CC32XX_PINMUX(1U, 0U)
```

<a id="a092456dadbe48fb30ca448f893ff182d"></a>

### `GPIO11_P2`

```c
#define GPIO11_P2 TI_CC32XX_PINMUX(2U, 0U)
```

<a id="aa7fe336032aa6ad0cc8377bef839c249"></a>

### `GPIO12_P3`

```c
#define GPIO12_P3 TI_CC32XX_PINMUX(3U, 0U)
```

<a id="aa63a6fa68392be5d91f17f1512bca933"></a>

### `GPIO13_P4`

```c
#define GPIO13_P4 TI_CC32XX_PINMUX(4U, 0U)
```

<a id="a9c9da9f7d6f9b370c7548f936fe70b65"></a>

### `GPIO14_P5`

```c
#define GPIO14_P5 TI_CC32XX_PINMUX(5U, 0U)
```

<a id="a0b94b2938ede1a6d84b397b12399aa58"></a>

### `GPIO15_P6`

```c
#define GPIO15_P6 TI_CC32XX_PINMUX(6U, 0U)
```

<a id="a48e7884a7dfad77efe683eea6e678e1b"></a>

### `GPIO16_P7`

```c
#define GPIO16_P7 TI_CC32XX_PINMUX(7U, 0U)
```

<a id="a499b75b5acdf56015bc34363e8770625"></a>

### `GPIO17_P8`

```c
#define GPIO17_P8 TI_CC32XX_PINMUX(8U, 0U)
```

<a id="a581e291b3887f522a35a7529db6c6a9b"></a>

### `GPIO1_P55`

```c
#define GPIO1_P55 TI_CC32XX_PINMUX(55U, 0U)
```

<a id="a7bccf18256e2c16eeb9c2712b4123bed"></a>

### `GPIO22_P15`

```c
#define GPIO22_P15 TI_CC32XX_PINMUX(15U, 0U)
```

<a id="a6e86e11b2fa406cf3d0a0ec57d1e856f"></a>

### `GPIO23_P16`

```c
#define GPIO23_P16 TI_CC32XX_PINMUX(16U, 0U)
```

<a id="a80df0d9d7b3c95e556dd6f82f4551f0b"></a>

### `GPIO24_P17`

```c
#define GPIO24_P17 TI_CC32XX_PINMUX(17U, 0U)
```

<a id="ab316bbdba3762342b3823d9eee34809d"></a>

### `GPIO25_P21`

```c
#define GPIO25_P21 TI_CC32XX_PINMUX(21U, 0U)
```

<a id="a91221a9648fa4d08c5b4f928a9756c50"></a>

### `GPIO28_P18`

```c
#define GPIO28_P18 TI_CC32XX_PINMUX(18U, 0U)
```

<a id="abcec00f5b87b8c75cedc5d73ad7107d3"></a>

### `GPIO29_P20`

```c
#define GPIO29_P20 TI_CC32XX_PINMUX(20U, 0U)
```

<a id="ad92d7838cfa819c6ba4a896101d4ffca"></a>

### `GPIO2_P57`

```c
#define GPIO2_P57 TI_CC32XX_PINMUX(57U, 0U)
```

<a id="af1056beafa7c3f45e3096c66e1631096"></a>

### `GPIO30_P53`

```c
#define GPIO30_P53 TI_CC32XX_PINMUX(53U, 0U)
```

<a id="a0ad70dd2e46b8e463283999c065b1031"></a>

### `GPIO31_P45`

```c
#define GPIO31_P45 TI_CC32XX_PINMUX(45U, 0U)
```

<a id="a6f73c352c071329e8b51d62272e6b597"></a>

### `GPIO32_P52`

```c
#define GPIO32_P52 TI_CC32XX_PINMUX(52U, 0U)
```

<a id="a70ea8f18a9106a3c5d43bbee1d8af546"></a>

### `GPIO3_P58`

```c
#define GPIO3_P58 TI_CC32XX_PINMUX(58U, 0U)
```

<a id="aa189b623df8558a6438d176fc406abc2"></a>

### `GPIO5_P59`

```c
#define GPIO5_P59 TI_CC32XX_PINMUX(59U, 0U)
```

<a id="ae248cf8dc867d6f9114cd3aaa51b06ca"></a>

### `GPIO5_P60`

```c
#define GPIO5_P60 TI_CC32XX_PINMUX(60U, 0U)
```

<a id="a9fdaf32c4cf8469a4965405f564066dc"></a>

### `GPIO6_P61`

```c
#define GPIO6_P61 TI_CC32XX_PINMUX(61U, 0U)
```

<a id="a0a6f11f997a0e220dfff39bb2b419219"></a>

### `GPIO7_P62`

```c
#define GPIO7_P62 TI_CC32XX_PINMUX(62U, 0U)
```

<a id="ad36e2c84424950a91028054c3499b579"></a>

### `GPIO8_P63`

```c
#define GPIO8_P63 TI_CC32XX_PINMUX(63U, 0U)
```

<a id="a25a3031376018d5d679597770b0552f0"></a>

### `GPIO9_P64`

```c
#define GPIO9_P64 TI_CC32XX_PINMUX(64U, 0U)
```

<a id="a41607ce5c19fb904cef1b5b9ff065bca"></a>

### `GSPI_CLK_P45`

```c
#define GSPI_CLK_P45 TI_CC32XX_PINMUX(45U, 7U)
```

<a id="a0835204b6761fdb5da07401588cb60a8"></a>

### `GSPI_CLK_P5`

```c
#define GSPI_CLK_P5 TI_CC32XX_PINMUX(5U, 7U)
```

<a id="a9531166ec008c53ebcb3bb7770bc9cfb"></a>

### `GSPI_CS_P50`

```c
#define GSPI_CS_P50 TI_CC32XX_PINMUX(50U, 9U)
```

<a id="a4a2c3ec59d144e1e20147f3fac31c7cf"></a>

### `GSPI_CS_P8`

```c
#define GSPI_CS_P8 TI_CC32XX_PINMUX(8U, 7U)
```

<a id="aaadb7b665b0adb1eed8d7a632c361910"></a>

### `GSPI_MISO_P53`

```c
#define GSPI_MISO_P53 TI_CC32XX_PINMUX(53U, 7U)
```

<a id="a2e33fd1fd267afccbef0ca274336708d"></a>

### `GSPI_MISO_P6`

```c
#define GSPI_MISO_P6 TI_CC32XX_PINMUX(6U, 7U)
```

<a id="a0472ccf0e3dde61e9b10c4ee44034a05"></a>

### `GSPI_MOSI_P52`

```c
#define GSPI_MOSI_P52 TI_CC32XX_PINMUX(52U, 8U)
```

<a id="a06cd1b5b0df08a309fc7d9d0eb176948"></a>

### `GSPI_MOSI_P7`

```c
#define GSPI_MOSI_P7 TI_CC32XX_PINMUX(7U, 7U)
```

<a id="a4b59e68f954e26a5a22a946c83c7b35c"></a>

### `GT_CCP00_P50`

```c
#define GT_CCP00_P50 TI_CC32XX_PINMUX(50U, 7U)
```

<a id="a45b13479b3cdedf5488f122a3b3ec288"></a>

### `GT_CCP00_P64`

```c
#define GT_CCP00_P64 TI_CC32XX_PINMUX(64U, 12U)
```

<a id="a41832e073da75fce278ea3f3a10c7981"></a>

### `GT_CCP01_P1`

```c
#define GT_CCP01_P1 TI_CC32XX_PINMUX(1U, 12U)
```

<a id="a8d323feb4cf8d2264da5f94853acfcd2"></a>

### `GT_CCP01_P55`

```c
#define GT_CCP01_P55 TI_CC32XX_PINMUX(55U, 7U)
```

<a id="a29f1d9fd07affc428b9ec13021951496"></a>

### `GT_CCP02_P2`

```c
#define GT_CCP02_P2 TI_CC32XX_PINMUX(2U, 12U)
```

<a id="af126c52c2ae52c91b68e9184004cfdcf"></a>

### `GT_CCP02_P57`

```c
#define GT_CCP02_P57 TI_CC32XX_PINMUX(57U, 7U)
```

<a id="a11be8733f58686a917f33eebc3f83f9f"></a>

### `GT_CCP03_P3`

```c
#define GT_CCP03_P3 TI_CC32XX_PINMUX(3U, 12U)
```

<a id="a93a7b969c1094f0c7a4811218a6d6b05"></a>

### `GT_CCP04_P15`

```c
#define GT_CCP04_P15 TI_CC32XX_PINMUX(15U, 5U)
```

<a id="a469f19224eef6881cc1247eed19c94a9"></a>

### `GT_CCP04_P4`

```c
#define GT_CCP04_P4 TI_CC32XX_PINMUX(4U, 12U)
```

<a id="a85dd880198761cbddb32b2d482247bfa"></a>

### `GT_CCP05_P5`

```c
#define GT_CCP05_P5 TI_CC32XX_PINMUX(5U, 12U)
```

<a id="ac91e88a5f0e186cea7cf4c1089a93e7e"></a>

### `GT_CCP05_P53`

```c
#define GT_CCP05_P53 TI_CC32XX_PINMUX(53U, 4U)
```

<a id="adcfc77087d75e8f687ca40cf102c5672"></a>

### `GT_CCP05_P60`

```c
#define GT_CCP05_P60 TI_CC32XX_PINMUX(60U, 7U)
```

<a id="a3ba8bacb70f2bcadaa6dfd786a673bd7"></a>

### `GT_CCP06_P17`

```c
#define GT_CCP06_P17 TI_CC32XX_PINMUX(17U, 4U)
```

<a id="a912c145e14635c2fade2b206d71df0a3"></a>

### `GT_CCP06_P6`

```c
#define GT_CCP06_P6 TI_CC32XX_PINMUX(6U, 13U)
```

<a id="a1de5f909c12eadb029562bf14197ffc7"></a>

### `GT_CCP06_P61`

```c
#define GT_CCP06_P61 TI_CC32XX_PINMUX(61U, 7U)
```

<a id="af36b5558e59ca508f363a52c3fb180a0"></a>

### `GT_CCP06_P63`

```c
#define GT_CCP06_P63 TI_CC32XX_PINMUX(63U, 12U)
```

<a id="a2688169c0aa3bfc4333550d77b03f301"></a>

### `GT_CCP07_P7`

```c
#define GT_CCP07_P7 TI_CC32XX_PINMUX(7U, 13U)
```

<a id="aa34e4da30d6f3b91df53e14b195650bc"></a>

### `GT_PWM02_P21`

```c
#define GT_PWM02_P21 TI_CC32XX_PINMUX(21U, 9U)
```

<a id="a7c7fb987ccc55419a645a4a04b30e200"></a>

### `GT_PWM03_P19`

```c
#define GT_PWM03_P19 TI_CC32XX_PINMUX(19U, 8U)
```

<a id="a4a276c8f1545d3b817ced42811b934f7"></a>

### `GT_PWM05_P64`

```c
#define GT_PWM05_P64 TI_CC32XX_PINMUX(64U, 3U)
```

<a id="a1b2e5aea3aad1cf49a0c9ed9c1abd0ac"></a>

### `GT_PWM06_P1`

```c
#define GT_PWM06_P1 TI_CC32XX_PINMUX(1U, 3U)
```

<a id="a158549be521c32cbadd7fd94a59bc945"></a>

### `GT_PWM07_P2`

```c
#define GT_PWM07_P2 TI_CC32XX_PINMUX(2U, 3U)
```

<a id="abd05f625495d2ea978dd73f2163ac895"></a>

### `I2C_SCL_P1`

```c
#define I2C_SCL_P1 TI_CC32XX_PINMUX(1U, 1U)
```

<a id="a8267f2892d868a33b27c68ae6673f239"></a>

### `I2C_SCL_P16`

```c
#define I2C_SCL_P16 TI_CC32XX_PINMUX(16U, 9U)
```

<a id="a7f43eaa1290d1c51ad8dd0eead54eac8"></a>

### `I2C_SCL_P3`

```c
#define I2C_SCL_P3 TI_CC32XX_PINMUX(3U, 5U)
```

<a id="a4894dca0ecb760732bf032d80a6d8a13"></a>

### `I2C_SCL_P5`

```c
#define I2C_SCL_P5 TI_CC32XX_PINMUX(5U, 5U)
```

<a id="a0b1353bc11a6e1a156c6dbe4e59f74d0"></a>

### `I2C_SDA_P17`

```c
#define I2C_SDA_P17 TI_CC32XX_PINMUX(17U, 9U)
```

<a id="a38fbe2595b40a64618809999d9ff7e88"></a>

### `I2C_SDA_P2`

```c
#define I2C_SDA_P2 TI_CC32XX_PINMUX(2U, 1U)
```

<a id="a2ac054fb4527be70688dfbad814da263"></a>

### `I2C_SDA_P4`

```c
#define I2C_SDA_P4 TI_CC32XX_PINMUX(4U, 5U)
```

<a id="ac8ded51ba9587b17cf1c2565f635a8a2"></a>

### `I2C_SDA_P6`

```c
#define I2C_SDA_P6 TI_CC32XX_PINMUX(6U, 5U)
```

<a id="a449900e101576c23577ae8731ff6d832"></a>

### `MCACLK_P3`

```c
#define MCACLK_P3 TI_CC32XX_PINMUX(3U, 3U)
```

<a id="a4de157ff760a13c620d8bc5730166dfd"></a>

### `MCACLK_P52`

```c
#define MCACLK_P52 TI_CC32XX_PINMUX(52U, 2U)
```

<a id="ad2986e8a3004f19836aaf1264bbb052d"></a>

### `MCACLK_P53`

```c
#define MCACLK_P53 TI_CC32XX_PINMUX(53U, 2U)
```

<a id="a900e65546f481f00fc2cb80218063bfd"></a>

### `MCACLKX_P62`

```c
#define MCACLKX_P62 TI_CC32XX_PINMUX(62U, 13U)
```

<a id="ae4a09b647c36db2a78d4d8a128d47ac5"></a>

### `MCAFSX_P15`

```c
#define MCAFSX_P15 TI_CC32XX_PINMUX(15U, 7U)
```

<a id="a082b74a8cdfc05bef2c377e8d271bac3"></a>

### `MCAFSX_P17`

```c
#define MCAFSX_P17 TI_CC32XX_PINMUX(17U, 6U)
```

<a id="af81018b6a0cfba2b48bcdc9cf864d609"></a>

### `MCAFSX_P2`

```c
#define MCAFSX_P2 TI_CC32XX_PINMUX(2U, 13U)
```

<a id="a0c5127de54dfe7be823dbba91260eeb8"></a>

### `MCAFSX_P45`

```c
#define MCAFSX_P45 TI_CC32XX_PINMUX(45U, 12U)
```

<a id="a8433ec0dd136e712bcffc99562d77a13"></a>

### `MCAFSX_P53`

```c
#define MCAFSX_P53 TI_CC32XX_PINMUX(53U, 3U)
```

<a id="a24efd787cbb04117197d27289eab0d83"></a>

### `MCAFSX_P63`

```c
#define MCAFSX_P63 TI_CC32XX_PINMUX(63U, 7U)
```

<a id="ad0767fcefbfc59f576341422ab3c466f"></a>

### `MCASFX_P21`

```c
#define MCASFX_P21 TI_CC32XX_PINMUX(21U, 2U)
```

<a id="a93408262bf38798525fc1ed43b759759"></a>

### `MCAXR0_P45`

```c
#define MCAXR0_P45 TI_CC32XX_PINMUX(45U, 6U)
```

<a id="a92fa65531018efc9a2fe37d1920d609e"></a>

### `MCAXR0_P50`

```c
#define MCAXR0_P50 TI_CC32XX_PINMUX(50U, 4U)
```

<a id="a85e3fa7f05e7b0f8d2b58741d42e90bc"></a>

### `MCAXR0_P52`

```c
#define MCAXR0_P52 TI_CC32XX_PINMUX(52U, 4U)
```

<a id="a98e96c0252ec68f37144096625e1492d"></a>

### `MCAXR0_P64`

```c
#define MCAXR0_P64 TI_CC32XX_PINMUX(64U, 7U)
```

<a id="a2c2f38b43528c3d2ed0d909cb276a834"></a>

### `MCAXR1_P50`

```c
#define MCAXR1_P50 TI_CC32XX_PINMUX(50U, 6U)
```

<a id="a7f6eb41b90608548c67fe52ac7285678"></a>

### `MCAXR1_P60`

```c
#define MCAXR1_P60 TI_CC32XX_PINMUX(60U, 6U)
```

<a id="acd84f05bdec8c70ee04acb87020286a1"></a>

### `PCLK_P55`

```c
#define PCLK_P55 TI_CC32XX_PINMUX(55U, 4U)
```

<a id="a4ba12e404845b1777c7fc27673a358c6"></a>

### `PDATA10_P7`

```c
#define PDATA10_P7 TI_CC32XX_PINMUX(7U, 4U)
```

<a id="aec9421895f489defea513f9451f19a59"></a>

### `PDATA11_P8`

```c
#define PDATA11_P8 TI_CC32XX_PINMUX(8U, 4U)
```

<a id="aca1510ae9b35a8c0f75d486bcd219feb"></a>

### `PDATA4_P61`

```c
#define PDATA4_P61 TI_CC32XX_PINMUX(61U, 4U)
```

<a id="a0a03dacfa4378314839df59511f7af27"></a>

### `PDATA5_P60`

```c
#define PDATA5_P60 TI_CC32XX_PINMUX(60U, 4U)
```

<a id="aa631c65c36a4db5ba54f9603427911d3"></a>

### `PDATA6_P59`

```c
#define PDATA6_P59 TI_CC32XX_PINMUX(59U, 4U)
```

<a id="a97849d9928b913f404d1a7be447051bf"></a>

### `PDATA7_P58`

```c
#define PDATA7_P58 TI_CC32XX_PINMUX(58U, 7U)
```

<a id="a420084bc2bed97ccfa6cabbdcea111b8"></a>

### `PDATA8_P5`

```c
#define PDATA8_P5 TI_CC32XX_PINMUX(5U, 4U)
```

<a id="a74f7003fe754549a7abd536ce7ca18e0"></a>

### `PDATA9_P6`

```c
#define PDATA9_P6 TI_CC32XX_PINMUX(6U, 4U)
```

<a id="a784b4247574d785820e1960b77d243f8"></a>

### `PHS_P4`

```c
#define PHS_P4 TI_CC32XX_PINMUX(4U, 4U)
```

<a id="a040fa03ccf78c01cf8353dfafaed4363"></a>

### `PVS_P3`

```c
#define PVS_P3 TI_CC32XX_PINMUX(3U, 4U)
```

<a id="a6c881b3b5ceb937e8441bd0cd3b449e8"></a>

### `PWM0_P17`

```c
#define PWM0_P17 TI_CC32XX_PINMUX(17U, 5U)
```

<a id="af0194d8218ffae6e4ca6afdc1b75184c"></a>

### `PXCLK_P2`

```c
#define PXCLK_P2 TI_CC32XX_PINMUX(2U, 4U)
```

<a id="a0348e53054efacbcc5f4b36f5983b483"></a>

### `SDCARD_CLK_P1`

```c
#define SDCARD_CLK_P1 TI_CC32XX_PINMUX(1U, 6U)
```

<a id="ad19d6a6d4e575fdedc182d95c426ef7a"></a>

### `SDCARD_CLK_P7`

```c
#define SDCARD_CLK_P7 TI_CC32XX_PINMUX(7U, 8U)
```

<a id="af4b6115dd55265aa56f4fd0e4519449d"></a>

### `SDCARD_CMD_P2`

```c
#define SDCARD_CMD_P2 TI_CC32XX_PINMUX(2U, 6U)
```

<a id="a23c36223a0811761121eb6992e733191"></a>

### `SDCARD_CMD_P8`

```c
#define SDCARD_CMD_P8 TI_CC32XX_PINMUX(8U, 8U)
```

<a id="a1f11274609e837c40dbfcf3f4bb2c65b"></a>

### `SDCARD_DATA3_P6`

```c
#define SDCARD_DATA3_P6 TI_CC32XX_PINMUX(6U, 8U)
```

<a id="a18587659510c1d7f7a3fc761b021999d"></a>

### `SDCARD_DATA_P64`

```c
#define SDCARD_DATA_P64 TI_CC32XX_PINMUX(64U, 6U)
```

<a id="a2edc3859ba96c9902d3c5eb2298a86ca"></a>

### `SDCARD_IRQ_P63`

```c
#define SDCARD_IRQ_P63 TI_CC32XX_PINMUX(63U, 6U)
```

<a id="af651d7aa9e7ee9ed0f39ea4ea72d6c3b"></a>

### `TCK_P19`

```c
#define TCK_P19 TI_CC32XX_PINMUX(19U, 1U)
```

<a id="aa8b475c426b332c82e21567727bb482a"></a>

### `TDI_P16`

```c
#define TDI_P16 TI_CC32XX_PINMUX(16U, 1U)
```

<a id="a16ea3f7a2cb062dcdab07e50b4f5c049"></a>

### `TDO_P17`

```c
#define TDO_P17 TI_CC32XX_PINMUX(17U, 1U)
```

<a id="a381590ba2880c42636058c248f7e0e2e"></a>

### `TI_CC32XX_MUX_MSK`

```c
#define TI_CC32XX_MUX_MSK 0xFU
```

<a id="ac9e2e00ac00ddd1eaf84331d18806339"></a>

### `TI_CC32XX_MUX_POS`

```c
#define TI_CC32XX_MUX_POS 0U
```

<a id="a40cc14e2a5969a01d7a764fb5bdb84a7"></a>

### `TI_CC32XX_PIN_MSK`

```c
#define TI_CC32XX_PIN_MSK 0x3FU
```

<a id="aea6f7d34537febd574f9ea0db1fbf3f3"></a>

### `TI_CC32XX_PIN_POS`

```c
#define TI_CC32XX_PIN_POS 16U
```

<a id="a4bf6d48b1ebcaaeb96b0450533dfa428"></a>

### `TI_CC32XX_PINMUX`

```c
#define TI_CC32XX_PINMUX ( pin, mux )
```

展开值（Value）：

```c
((((pin)&TI_CC32XX_PIN_MSK) << TI_CC32XX_PIN_POS) |                                        \
 (((mux)&TI_CC32XX_MUX_MSK) << TI_CC32XX_MUX_POS))
```

构造 TI CC32XX `pinmux` 属性条目的工具宏（Utility Macro）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pin` | 引脚（Pin）。 |
| `mux` | 复用器选择（Multiplexer Choice）。 |

<a id="a5d14159904ec1c4f56c911e643a7eed4"></a>

### `TMS_P20`

```c
#define TMS_P20 TI_CC32XX_PINMUX(20U, 1U)
```

<a id="abebbd1dd7206417c61aff603dc0d3c3a"></a>

### `UART0_CTS_P61`

```c
#define UART0_CTS_P61 TI_CC32XX_PINMUX(61U, 6U)
```

<a id="aa8acf830a7e0ba5aef12422b0f594999"></a>

### `UART0_CTSN_P50`

```c
#define UART0_CTSN_P50 TI_CC32XX_PINMUX(50U, 12U)
```

<a id="a202ce4d02639e2277dc70f8c34e96796"></a>

### `UART0_RTS_P50`

```c
#define UART0_RTS_P50 TI_CC32XX_PINMUX(50U, 3U)
```

<a id="ae3dd30595d8647e48844b8b9a204eee4"></a>

### `UART0_RTS_P52`

```c
#define UART0_RTS_P52 TI_CC32XX_PINMUX(52U, 6U)
```

<a id="a68e13f52aab072bee8eed2de25737730"></a>

### `UART0_RTS_P61`

```c
#define UART0_RTS_P61 TI_CC32XX_PINMUX(61U, 5U)
```

<a id="af4ef5b36c0c036734bd924586fabc519"></a>

### `UART0_RTS_P62`

```c
#define UART0_RTS_P62 TI_CC32XX_PINMUX(62U, 10U)
```

<a id="a8526e278e737f86b5416d2432e06a961"></a>

### `UART0_RX_P4`

```c
#define UART0_RX_P4 TI_CC32XX_PINMUX(4U, 7U)
```

<a id="aec30ecff2290ff162f4940376f092f77"></a>

### `UART0_RX_P45`

```c
#define UART0_RX_P45 TI_CC32XX_PINMUX(45U, 9U)
```

<a id="a9220f19106cb9f8840a1b90607948dcc"></a>

### `UART0_RX_P57`

```c
#define UART0_RX_P57 TI_CC32XX_PINMUX(57U, 3U)
```

<a id="a0a31d5b2068953d90f7e152cfdeec235"></a>

### `UART0_TX_P3`

```c
#define UART0_TX_P3 TI_CC32XX_PINMUX(3U, 7U)
```

<a id="afa26fef4c910605bfc58516bba2b0446"></a>

### `UART0_TX_P53`

```c
#define UART0_TX_P53 TI_CC32XX_PINMUX(53U, 9U)
```

<a id="ae02a8d280e708f2b28314c565b8368c7"></a>

### `UART0_TX_P55`

```c
#define UART0_TX_P55 TI_CC32XX_PINMUX(55U, 3U)
```

<a id="a29e0564a1b5101a50836a9cfa97a7a63"></a>

### `UART0_TX_P62`

```c
#define UART0_TX_P62 TI_CC32XX_PINMUX(62U, 11U)
```

<a id="a182be28929eb2e11c780d3f7bd3914a6"></a>

### `UART1_CTS_P61`

```c
#define UART1_CTS_P61 TI_CC32XX_PINMUX(61U, 3U)
```

<a id="afc79f99843ab6ec1fcc46e475516d3ea"></a>

### `UART1_RTS_P50`

```c
#define UART1_RTS_P50 TI_CC32XX_PINMUX(50U, 10U)
```

<a id="a2f6c6154904c3dce5496d8c837e4fbf0"></a>

### `UART1_RTS_P62`

```c
#define UART1_RTS_P62 TI_CC32XX_PINMUX(62U, 3U)
```

<a id="a632c817fbe28a138a9916a4946ee9da5"></a>

### `UART1_RX_P17`

```c
#define UART1_RX_P17 TI_CC32XX_PINMUX(17U, 2U)
```

<a id="a6c343f9636e9d3b43d19b3d0fe9f00b1"></a>

### `UART1_RX_P2`

```c
#define UART1_RX_P2 TI_CC32XX_PINMUX(2U, 7U)
```

<a id="ac379119f98304c790ab8cbba4752feec"></a>

### `UART1_RX_P45`

```c
#define UART1_RX_P45 TI_CC32XX_PINMUX(45U, 2U)
```

<a id="a2a67e698005d5be4baf74216341adf8e"></a>

### `UART1_RX_P57`

```c
#define UART1_RX_P57 TI_CC32XX_PINMUX(57U, 6U)
```

<a id="a20c1984c49c52b45fb9024d45a0bdb27"></a>

### `UART1_RX_P59`

```c
#define UART1_RX_P59 TI_CC32XX_PINMUX(59U, 6U)
```

<a id="a9f7daa4bf7f1e01439d84c58da7c7235"></a>

### `UART1_RX_P8`

```c
#define UART1_RX_P8 TI_CC32XX_PINMUX(8U, 5U)
```

<a id="a995c80839609dc2f99440020c4b376c4"></a>

### `UART1_TX_P1`

```c
#define UART1_TX_P1 TI_CC32XX_PINMUX(1U, 7U)
```

<a id="af2bdaab6fc0f793aee2bc8821869aad6"></a>

### `UART1_TX_P16`

```c
#define UART1_TX_P16 TI_CC32XX_PINMUX(16U, 2U)
```

<a id="a06c9f6cc98ffdc8b53495a785fbcb3bd"></a>

### `UART1_TX_P55`

```c
#define UART1_TX_P55 TI_CC32XX_PINMUX(55U, 6U)
```

<a id="a33fe230e16d7b9ddfc5c4e5f6affa32d"></a>

### `UART1_TX_P58`

```c
#define UART1_TX_P58 TI_CC32XX_PINMUX(58U, 6U)
```

<a id="a3e9e600bebc357ff182f42317b4fbc5f"></a>

### `UART1_TX_P7`

```c
#define UART1_TX_P7 TI_CC32XX_PINMUX(7U, 5U)
```


## 69.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P223_ti-cc32xx-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="ati-cc32xx-pinctrl_8h_html_a381590ba2880c42636058c248f7e0e2e"></a>
<a id="ati-cc32xx-pinctrl_8h_html_a40cc14e2a5969a01d7a764fb5bdb84a7"></a>
<a id="ati-cc32xx-pinctrl_8h_html_ac9e2e00ac00ddd1eaf84331d18806339"></a>
<a id="ati-cc32xx-pinctrl_8h_html_aea6f7d34537febd574f9ea0db1fbf3f3"></a>

---

[上一章](P068_zephyr__net__prometheus__summary.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P070_zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考.md)
