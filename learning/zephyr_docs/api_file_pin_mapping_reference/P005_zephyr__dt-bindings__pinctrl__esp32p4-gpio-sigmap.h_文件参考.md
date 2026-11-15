---
id: learning.zephyr-docs.api-file-pin-mapping-reference.page-5
title: zephyr__dt-bindings__pinctrl__esp32p4-gpio-sigmap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_esp32p4-gpio-sigmap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/esp32p4-gpio-sigmap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Espressif ESP32-P4的GPIO信号映射（GPIO Signal Map）。

查看此文件的源码。

<a id="details"></a>

Espressif ESP32-P4 的 GPIO 信号映射（Signal Map）。将外设信号（Peripheral Signals）映射到 GPIO 矩阵（Matrix）的输入／输出索引。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_af80260535bc3aee44c28c972a29483e0"></a>

```c
#define ESP_NOSIG ESP_SIG_INVAL
```

相关声明：[ESP_NOSIG](#af80260535bc3aee44c28c972a29483e0)、[ESP_SIG_INVAL](../api_file_clock_network_reference/P007_zephyr__dt-bindings__pinctrl__esp-pinctrl-common.h_文件参考.md#ae0d2e726ab8d90343e5c80e1d9b85ad8)。

无信号（No Signal），无效值。

<a id="r_aca502efa55ce2286dc9eba28192681fd"></a>

```c
#define ESP_U0RXD_IN 10
```

相关声明：[ESP_U0RXD_IN](#aca502efa55ce2286dc9eba28192681fd)。

UART0 RXD 输入（UART0 RXD input）。

<a id="r_af1e58fb8e7ef86a92171eca7bb1671af"></a>

```c
#define ESP_U0TXD_OUT 10
```

相关声明：[ESP_U0TXD_OUT](#af1e58fb8e7ef86a92171eca7bb1671af)。

UART0 TXD 输出（UART0 TXD output）。

<a id="r_a530d7a918a97cd1fff1acf2f90edd4ca"></a>

```c
#define ESP_U0CTS_IN 11
```

相关声明：[ESP_U0CTS_IN](#a530d7a918a97cd1fff1acf2f90edd4ca)。

UART0 CTS 输入（UART0 CTS input）。

<a id="r_a4257bbc044af6ea3612313e3a0b7e7c9"></a>

```c
#define ESP_U0RTS_OUT 11
```

相关声明：[ESP_U0RTS_OUT](#a4257bbc044af6ea3612313e3a0b7e7c9)。

UART0 RTS 输出（UART0 RTS output）。

<a id="r_a53e3a4557a4eb1f7f98250abef03c02a"></a>

```c
#define ESP_U0DSR_IN 12
```

相关声明：[ESP_U0DSR_IN](#a53e3a4557a4eb1f7f98250abef03c02a)。

UART0 DSR 输入（UART0 DSR input）。

<a id="r_acc8716af947169c9f167bdf215c5314c"></a>

```c
#define ESP_U0DTR_OUT 12
```

相关声明：[ESP_U0DTR_OUT](#acc8716af947169c9f167bdf215c5314c)。

UART0 DTR 输出（UART0 DTR output）。

<a id="r_a2293e0646e0ad2f76d62f76425ae6770"></a>

```c
#define ESP_U1RXD_IN 13
```

相关声明：[ESP_U1RXD_IN](#a2293e0646e0ad2f76d62f76425ae6770)。

UART1 RXD 输入（UART1 RXD input）。

<a id="r_a6053b38147e28e3a7479b38e7d195136"></a>

```c
#define ESP_U1TXD_OUT 13
```

相关声明：[ESP_U1TXD_OUT](#a6053b38147e28e3a7479b38e7d195136)。

UART1 TXD 输出（UART1 TXD output）。

<a id="r_a3c005e616da21a058960d6aed79427b3"></a>

```c
#define ESP_U1CTS_IN 14
```

相关声明：[ESP_U1CTS_IN](#a3c005e616da21a058960d6aed79427b3)。

UART1 CTS 输入（UART1 CTS input）。

<a id="r_a8f6399745566bd5caa2020e4dcb2bb3b"></a>

```c
#define ESP_U1RTS_OUT 14
```

相关声明：[ESP_U1RTS_OUT](#a8f6399745566bd5caa2020e4dcb2bb3b)。

UART1 RTS 输出（UART1 RTS output）。

<a id="r_a5f29b138691540598d0b977dc4bd5971"></a>

```c
#define ESP_U1DSR_IN 15
```

相关声明：[ESP_U1DSR_IN](#a5f29b138691540598d0b977dc4bd5971)。

UART1 DSR 输入（UART1 DSR input）。

<a id="r_a1f7df042d40ec6f20b559ef6778d7497"></a>

```c
#define ESP_U1DTR_OUT 15
```

相关声明：[ESP_U1DTR_OUT](#a1f7df042d40ec6f20b559ef6778d7497)。

UART1 DTR 输出（UART1 DTR output）。

<a id="r_abe46ead057c2b66d500ef07e8a84fe0f"></a>

```c
#define ESP_U2RXD_IN 16
```

相关声明：[ESP_U2RXD_IN](#abe46ead057c2b66d500ef07e8a84fe0f)。

UART2 RXD 输入（UART2 RXD input）。

<a id="r_a20baac10eb4b76603580e1ea7065213a"></a>

```c
#define ESP_U2TXD_OUT 16
```

相关声明：[ESP_U2TXD_OUT](#a20baac10eb4b76603580e1ea7065213a)。

UART2 TXD 输出（UART2 TXD output）。

<a id="r_a735a482aa723130ccb408f0fb7596a0a"></a>

```c
#define ESP_U2CTS_IN 17
```

相关声明：[ESP_U2CTS_IN](#a735a482aa723130ccb408f0fb7596a0a)。

UART2 CTS 输入（UART2 CTS input）。

<a id="r_a174b50e35d961ded056cea3848110b20"></a>

```c
#define ESP_U2RTS_OUT 17
```

相关声明：[ESP_U2RTS_OUT](#a174b50e35d961ded056cea3848110b20)。

UART2 RTS 输出（UART2 RTS output）。

<a id="r_a70d4f834bfd182c138257e36a4b04096"></a>

```c
#define ESP_U2DSR_IN 18
```

相关声明：[ESP_U2DSR_IN](#a70d4f834bfd182c138257e36a4b04096)。

UART2 DSR 输入（UART2 DSR input）。

<a id="r_a783f6ee9ad46dfd9e34d1473b1e2ad9b"></a>

```c
#define ESP_U2DTR_OUT 18
```

相关声明：[ESP_U2DTR_OUT](#a783f6ee9ad46dfd9e34d1473b1e2ad9b)。

UART2 DTR 输出（UART2 DTR output）。

<a id="r_a5b939f8c6f862b51249463b7b1e2b4fc"></a>

```c
#define ESP_U3RXD_IN 19
```

相关声明：[ESP_U3RXD_IN](#a5b939f8c6f862b51249463b7b1e2b4fc)。

UART3 RXD 输入（UART3 RXD input）。

<a id="r_aa038f32908e5e30faaef5438203a9270"></a>

```c
#define ESP_U3TXD_OUT 19
```

相关声明：[ESP_U3TXD_OUT](#aa038f32908e5e30faaef5438203a9270)。

UART3 TXD 输出（UART3 TXD output）。

<a id="r_a0e350c02f93ace85a2dd891597d89d8c"></a>

```c
#define ESP_U3CTS_IN 20
```

相关声明：[ESP_U3CTS_IN](#a0e350c02f93ace85a2dd891597d89d8c)。

UART3 CTS 输入（UART3 CTS input）。

<a id="r_a466185d49c68709507afce20d25aca3a"></a>

```c
#define ESP_U3RTS_OUT 20
```

相关声明：[ESP_U3RTS_OUT](#a466185d49c68709507afce20d25aca3a)。

UART3 RTS 输出（UART3 RTS output）。

<a id="r_a62a19eb3ff17c8dbe3701c3be7fd844d"></a>

```c
#define ESP_U3DSR_IN 21
```

相关声明：[ESP_U3DSR_IN](#a62a19eb3ff17c8dbe3701c3be7fd844d)。

UART3 DSR 输入（UART3 DSR input）。

<a id="r_a41780dd757f8fd9f0b44c89c02e4aff3"></a>

```c
#define ESP_U3DTR_OUT 21
```

相关声明：[ESP_U3DTR_OUT](#a41780dd757f8fd9f0b44c89c02e4aff3)。

UART3 DTR 输出（UART3 DTR output）。

<a id="r_a2e52bdb5a3cb16125b95f0ecd71e6012"></a>

```c
#define ESP_U4RXD_IN 22
```

相关声明：[ESP_U4RXD_IN](#a2e52bdb5a3cb16125b95f0ecd71e6012)。

UART4 RXD 输入（UART4 RXD input）。

<a id="r_a9dbb0d137993ef1f48a1ba7d1b6a31b2"></a>

```c
#define ESP_U4TXD_OUT 22
```

相关声明：[ESP_U4TXD_OUT](#a9dbb0d137993ef1f48a1ba7d1b6a31b2)。

UART4 TXD 输出（UART4 TXD output）。

<a id="r_a933519638d1c5cd78138da16d447008d"></a>

```c
#define ESP_U4CTS_IN 23
```

相关声明：[ESP_U4CTS_IN](#a933519638d1c5cd78138da16d447008d)。

UART4 CTS 输入（UART4 CTS input）。

<a id="r_a68ccd15805cfb52a466af2a24520a4c3"></a>

```c
#define ESP_U4RTS_OUT 23
```

相关声明：[ESP_U4RTS_OUT](#a68ccd15805cfb52a466af2a24520a4c3)。

UART4 RTS 输出（UART4 RTS output）。

<a id="r_ae533de687bb88939f97c73ae85eecfd5"></a>

```c
#define ESP_U4DSR_IN 24
```

相关声明：[ESP_U4DSR_IN](#ae533de687bb88939f97c73ae85eecfd5)。

UART4 DSR 输入（UART4 DSR input）。

<a id="r_ae7508454f2ba682485978aa9d86637c0"></a>

```c
#define ESP_U4DTR_OUT 24
```

相关声明：[ESP_U4DTR_OUT](#ae7508454f2ba682485978aa9d86637c0)。

UART4 DTR 输出（UART4 DTR output）。

<a id="r_a8c8a6b9063b2c47dd6b9db6b853e4ec1"></a>

```c
#define ESP_I2S1_O_BCK_IN 31
```

相关声明：[ESP_I2S1_O_BCK_IN](#a8c8a6b9063b2c47dd6b9db6b853e4ec1)。

I2S1 输出 BCK 输入（I2S1 output BCK input）。

<a id="r_a67af83425f55eb3d3873d99bb5c23129"></a>

```c
#define ESP_I2S1_O_BCK_OUT 31
```

相关声明：[ESP_I2S1_O_BCK_OUT](#a67af83425f55eb3d3873d99bb5c23129)。

I2S1 输出 BCK 输出（I2S1 output BCK output）。

<a id="r_af00f358d0012d5a4e85a0610f9da2ace"></a>

```c
#define ESP_I2S1_MCLK_IN 32
```

相关声明：[ESP_I2S1_MCLK_IN](#af00f358d0012d5a4e85a0610f9da2ace)。

I2S1 MCLK 输入（I2S1 MCLK input）。

<a id="r_aeeb2b00d8b3172832532d96b2282d4d2"></a>

```c
#define ESP_I2S1_MCLK_OUT 32
```

相关声明：[ESP_I2S1_MCLK_OUT](#aeeb2b00d8b3172832532d96b2282d4d2)。

I2S1 MCLK 输出（I2S1 MCLK output）。

<a id="r_aeced96606d401941ddecf93865940045"></a>

```c
#define ESP_I2S1_O_WS_IN 33
```

相关声明：[ESP_I2S1_O_WS_IN](#aeced96606d401941ddecf93865940045)。

I2S1 输出 WS 输入（I2S1 output WS input）。

<a id="r_a22a4414a710032bb89da262dfe11b399"></a>

```c
#define ESP_I2S1_O_WS_OUT 33
```

相关声明：[ESP_I2S1_O_WS_OUT](#a22a4414a710032bb89da262dfe11b399)。

I2S1 输出 WS 输出（I2S1 output WS output）。

<a id="r_ae1d94e076cf75a07a65ab53f4cfa5faf"></a>

```c
#define ESP_I2S1_I_SD_IN 34
```

相关声明：[ESP_I2S1_I_SD_IN](#ae1d94e076cf75a07a65ab53f4cfa5faf)。

I2S1 输入 SD 输入（I2S1 input SD input）。

<a id="r_a266216587dd80023ffa859de13a21848"></a>

```c
#define ESP_I2S1_O_SD_OUT 34
```

相关声明：[ESP_I2S1_O_SD_OUT](#a266216587dd80023ffa859de13a21848)。

I2S1 输出 SD 输出（I2S1 output SD output）。

<a id="r_adb44e1303d1f50193926ba57c13bf2bc"></a>

```c
#define ESP_I2S1_I_BCK_IN 35
```

相关声明：[ESP_I2S1_I_BCK_IN](#adb44e1303d1f50193926ba57c13bf2bc)。

I2S1 输入 BCK 输入（I2S1 input BCK input）。

<a id="r_aec57e3323d6bf84e584a8a26b9679fcf"></a>

```c
#define ESP_I2S1_I_BCK_OUT 35
```

相关声明：[ESP_I2S1_I_BCK_OUT](#aec57e3323d6bf84e584a8a26b9679fcf)。

I2S1 输入 BCK 输出（I2S1 input BCK output）。

<a id="r_ae6761382c71944b44bf1c0ff748aefed"></a>

```c
#define ESP_I2S1_I_WS_IN 36
```

相关声明：[ESP_I2S1_I_WS_IN](#ae6761382c71944b44bf1c0ff748aefed)。

I2S1 输入 WS 输入（I2S1 input WS input）。

<a id="r_a36b4b39cdd4e2fb950d291bcecc2f562"></a>

```c
#define ESP_I2S1_I_WS_OUT 36
```

相关声明：[ESP_I2S1_I_WS_OUT](#a36b4b39cdd4e2fb950d291bcecc2f562)。

I2S1 输入 WS 输出（I2S1 input WS output）。

<a id="r_ab8d8d58ed38fe5584b3b7b485156b824"></a>

```c
#define ESP_I2S2_O_BCK_IN 37
```

相关声明：[ESP_I2S2_O_BCK_IN](#ab8d8d58ed38fe5584b3b7b485156b824)。

I2S2 输出 BCK 输入（I2S2 output BCK input）。

<a id="r_a5aa289413958c5d7406d6895f7338f1e"></a>

```c
#define ESP_I2S2_O_BCK_OUT 37
```

相关声明：[ESP_I2S2_O_BCK_OUT](#a5aa289413958c5d7406d6895f7338f1e)。

I2S2 输出 BCK 输出（I2S2 output BCK output）。

<a id="r_a1ba6505c35afd42628424421d5a4abcd"></a>

```c
#define ESP_I2S2_MCLK_IN 38
```

相关声明：[ESP_I2S2_MCLK_IN](#a1ba6505c35afd42628424421d5a4abcd)。

I2S2 MCLK 输入（I2S2 MCLK input）。

<a id="r_ab4b411f39dd5d5e075618f9a3b2bbf44"></a>

```c
#define ESP_I2S2_MCLK_OUT 38
```

相关声明：[ESP_I2S2_MCLK_OUT](#ab4b411f39dd5d5e075618f9a3b2bbf44)。

I2S2 MCLK 输出（I2S2 MCLK output）。

<a id="r_a424284c56809d44a6f5707625611b653"></a>

```c
#define ESP_I2S2_O_WS_IN 39
```

相关声明：[ESP_I2S2_O_WS_IN](#a424284c56809d44a6f5707625611b653)。

I2S2 输出 WS 输入（I2S2 output WS input）。

<a id="r_ad2f0863220d12e726c276eecb2d0475d"></a>

```c
#define ESP_I2S2_O_WS_OUT 39
```

相关声明：[ESP_I2S2_O_WS_OUT](#ad2f0863220d12e726c276eecb2d0475d)。

I2S2 输出 WS 输出（I2S2 output WS output）。

<a id="r_afbc86f6ecc0eff3482c0dd717e4a8b76"></a>

```c
#define ESP_I2S2_I_SD_IN 40
```

相关声明：[ESP_I2S2_I_SD_IN](#afbc86f6ecc0eff3482c0dd717e4a8b76)。

I2S2 输入 SD 输入（I2S2 input SD input）。

<a id="r_aecc44f4003ce107d283e7f053b9c5e11"></a>

```c
#define ESP_I2S2_O_SD_OUT 40
```

相关声明：[ESP_I2S2_O_SD_OUT](#aecc44f4003ce107d283e7f053b9c5e11)。

I2S2 输出 SD 输出（I2S2 output SD output）。

<a id="r_a59b9c3d4e7e71913b403e34dde61e705"></a>

```c
#define ESP_I2S2_I_BCK_IN 41
```

相关声明：[ESP_I2S2_I_BCK_IN](#a59b9c3d4e7e71913b403e34dde61e705)。

I2S2 输入 BCK 输入（I2S2 input BCK input）。

<a id="r_a08a6233fbbf192f5594bb7b0f1592300"></a>

```c
#define ESP_I2S2_I_BCK_OUT 41
```

相关声明：[ESP_I2S2_I_BCK_OUT](#a08a6233fbbf192f5594bb7b0f1592300)。

I2S2 输入 BCK 输出（I2S2 input BCK output）。

<a id="r_a95eb4982bcfd2f08a24d98291f9aa412"></a>

```c
#define ESP_I2S2_I_WS_IN 42
```

相关声明：[ESP_I2S2_I_WS_IN](#a95eb4982bcfd2f08a24d98291f9aa412)。

I2S2 输入 WS 输入（I2S2 input WS input）。

<a id="r_abdc9f33c6798b7c56589a4daf462261a"></a>

```c
#define ESP_I2S2_I_WS_OUT 42
```

相关声明：[ESP_I2S2_I_WS_OUT](#abdc9f33c6798b7c56589a4daf462261a)。

I2S2 输入 WS 输出（I2S2 input WS output）。

<a id="r_a9e4bf0b0eff43b1f56f17abe22ef24a5"></a>

```c
#define ESP_SPI3_CS2_OUT 45
```

相关声明：[ESP_SPI3_CS2_OUT](#a9e4bf0b0eff43b1f56f17abe22ef24a5)。

SPI3 CS2 输出（SPI3 CS2 output）。

<a id="r_a7f06d2db560a8cd511c9189cd6ed8980"></a>

```c
#define ESP_SPI3_CS1_OUT 46
```

相关声明：[ESP_SPI3_CS1_OUT](#a7f06d2db560a8cd511c9189cd6ed8980)。

SPI3 CS1 输出（SPI3 CS1 output）。

<a id="r_a714ad872feff48bc481b3791b28ec50d"></a>

```c
#define ESP_SPI3_CK_IN 47
```

相关声明：[ESP_SPI3_CK_IN](#a714ad872feff48bc481b3791b28ec50d)。

SPI3 时钟 输入（SPI3 clock input）。

<a id="r_ae5f28c7478dc01fadb9005f16c0100e7"></a>

```c
#define ESP_SPI3_CK_OUT 47
```

相关声明：[ESP_SPI3_CK_OUT](#ae5f28c7478dc01fadb9005f16c0100e7)。

SPI3 时钟 输出（SPI3 clock output）。

<a id="r_a05a9a2e5983b7895ca1fb05e5cd34709"></a>

```c
#define ESP_SPI3_Q_IN 48
```

相关声明：[ESP_SPI3_Q_IN](#a05a9a2e5983b7895ca1fb05e5cd34709)。

SPI3 Q 输入（SPI3 Q input）。

<a id="r_a886c0db586c39f6c40f6987ad624275e"></a>

```c
#define ESP_SPI3_QO_OUT 48
```

相关声明：[ESP_SPI3_QO_OUT](#a886c0db586c39f6c40f6987ad624275e)。

SPI3 Q 输出（SPI3 Q output）。

<a id="r_ae7cf1730786ba95580b91b00066d3e25"></a>

```c
#define ESP_SPI3_D_IN 49
```

相关声明：[ESP_SPI3_D_IN](#ae7cf1730786ba95580b91b00066d3e25)。

SPI3 D 输入（SPI3 D input）。

<a id="r_aff4a1289beb94c9e23d7c1dd13d71d83"></a>

```c
#define ESP_SPI3_D_OUT 49
```

相关声明：[ESP_SPI3_D_OUT](#aff4a1289beb94c9e23d7c1dd13d71d83)。

SPI3 D 输出（SPI3 D output）。

<a id="r_ab40bfa33ef13681c81e70a4cd19e2253"></a>

```c
#define ESP_SPI3_HOLD_IN 50
```

相关声明：[ESP_SPI3_HOLD_IN](#ab40bfa33ef13681c81e70a4cd19e2253)。

SPI3 HOLD 输入（SPI3 HOLD input）。

<a id="r_a603ce746c6b8d4dcea716bd2249e19b8"></a>

```c
#define ESP_SPI3_HOLD_OUT 50
```

相关声明：[ESP_SPI3_HOLD_OUT](#a603ce746c6b8d4dcea716bd2249e19b8)。

SPI3 HOLD 输出（SPI3 HOLD output）。

<a id="r_ae5ef053fe616dfb189a1a5bf28313647"></a>

```c
#define ESP_SPI3_WP_IN 51
```

相关声明：[ESP_SPI3_WP_IN](#ae5ef053fe616dfb189a1a5bf28313647)。

SPI3 WP 输入（SPI3 WP input）。

<a id="r_ab3c345085fafd95b7bd2f83d14a5317c"></a>

```c
#define ESP_SPI3_WP_OUT 51
```

相关声明：[ESP_SPI3_WP_OUT](#ab3c345085fafd95b7bd2f83d14a5317c)。

SPI3 WP 输出（SPI3 WP output）。

<a id="r_a7ef5baa3054ee04857f15f034407b0bf"></a>

```c
#define ESP_SPI3_CS_IN 52
```

相关声明：[ESP_SPI3_CS_IN](#a7ef5baa3054ee04857f15f034407b0bf)。

SPI3 CS 输入（SPI3 CS input）。

<a id="r_a09ec480d3b31ac943b489ed6229c051a"></a>

```c
#define ESP_SPI3_CS_OUT 52
```

相关声明：[ESP_SPI3_CS_OUT](#a09ec480d3b31ac943b489ed6229c051a)。

SPI3 CS 输出（SPI3 CS output）。

<a id="r_ade88988460c131e8c6775794588b0eb8"></a>

```c
#define ESP_FSPICLK_IN 53
```

相关声明：[ESP_FSPICLK_IN](#ade88988460c131e8c6775794588b0eb8)。

FSPI 时钟 输入（FSPI clock input）。

<a id="r_ab8c5397dc530f6326c3d10b31e59e168"></a>

```c
#define ESP_FSPICLK_OUT 53
```

相关声明：[ESP_FSPICLK_OUT](#ab8c5397dc530f6326c3d10b31e59e168)。

FSPI 时钟 输出（FSPI clock output）。

<a id="r_ab603b7bf7d016e85653a5c3be5c01293"></a>

```c
#define ESP_FSPIQ_IN 54
```

相关声明：[ESP_FSPIQ_IN](#ab603b7bf7d016e85653a5c3be5c01293)。

FSPI Q 输入（FSPI Q input）。

<a id="r_a8b3ea6ad374fa010b46b48072fa87ccb"></a>

```c
#define ESP_FSPIQ_OUT 54
```

相关声明：[ESP_FSPIQ_OUT](#a8b3ea6ad374fa010b46b48072fa87ccb)。

FSPI Q 输出（FSPI Q output）。

<a id="r_a7910521af840d42edd3c0a667cf90c5f"></a>

```c
#define ESP_FSPID_IN 55
```

相关声明：[ESP_FSPID_IN](#a7910521af840d42edd3c0a667cf90c5f)。

FSPI D 输入（FSPI D input）。

<a id="r_a02bd34821e8a4bf0038b9af417ec161a"></a>

```c
#define ESP_FSPID_OUT 55
```

相关声明：[ESP_FSPID_OUT](#a02bd34821e8a4bf0038b9af417ec161a)。

FSPI D 输出（FSPI D output）。

<a id="r_a60ff087a3d85a356d77f060a6698d00b"></a>

```c
#define ESP_FSPIHD_IN 56
```

相关声明：[ESP_FSPIHD_IN](#a60ff087a3d85a356d77f060a6698d00b)。

FSPI HD 输入（FSPI HD input）。

<a id="r_ac71bc137b93bd6c0c8a1ebe24a70a613"></a>

```c
#define ESP_FSPIHD_OUT 56
```

相关声明：[ESP_FSPIHD_OUT](#ac71bc137b93bd6c0c8a1ebe24a70a613)。

FSPI HD 输出（FSPI HD output）。

<a id="r_a4d4c4a13b820cab6d94da8fe08120a2f"></a>

```c
#define ESP_FSPIWP_IN 57
```

相关声明：[ESP_FSPIWP_IN](#a4d4c4a13b820cab6d94da8fe08120a2f)。

FSPI WP 输入（FSPI WP input）。

<a id="r_a83c4f18d726984cc98caeea9b7677ca1"></a>

```c
#define ESP_FSPIWP_OUT 57
```

相关声明：[ESP_FSPIWP_OUT](#a83c4f18d726984cc98caeea9b7677ca1)。

FSPI WP 输出（FSPI WP output）。

<a id="r_a96ca1328e76337d289f6e65faf33d75c"></a>

```c
#define ESP_FSPICS0_IN 62
```

相关声明：[ESP_FSPICS0_IN](#a96ca1328e76337d289f6e65faf33d75c)。

FSPI CS0 输入（FSPI CS0 input）。

<a id="r_ad1be1401b282275eaef46b9a598c6a40"></a>

```c
#define ESP_FSPICS0_OUT 62
```

相关声明：[ESP_FSPICS0_OUT](#ad1be1401b282275eaef46b9a598c6a40)。

FSPI CS0 输出（FSPI CS0 output）。

<a id="r_ab607ce367da34ab0f1bd7fa648273cf1"></a>

```c
#define ESP_I2CEXT0_SCL_IN 68
```

相关声明：[ESP_I2CEXT0_SCL_IN](#ab607ce367da34ab0f1bd7fa648273cf1)。

I2C0 SCL 输入（I2C0 SCL input）。

<a id="r_a2144cc62df795547ccf2bbe3ee4c629f"></a>

```c
#define ESP_I2CEXT0_SCL_OUT 68
```

相关声明：[ESP_I2CEXT0_SCL_OUT](#a2144cc62df795547ccf2bbe3ee4c629f)。

I2C0 SCL 输出（I2C0 SCL output）。

<a id="r_afa7061c87135b9dabe5c54f5f4ce16e6"></a>

```c
#define ESP_I2CEXT0_SDA_IN 69
```

相关声明：[ESP_I2CEXT0_SDA_IN](#afa7061c87135b9dabe5c54f5f4ce16e6)。

I2C0 SDA 输入（I2C0 SDA input）。

<a id="r_aabf1378b0ad2028c36c3bb74c81d7049"></a>

```c
#define ESP_I2CEXT0_SDA_OUT 69
```

相关声明：[ESP_I2CEXT0_SDA_OUT](#aabf1378b0ad2028c36c3bb74c81d7049)。

I2C0 SDA 输出（I2C0 SDA output）。

<a id="r_a1b6324b294e9e018a5909427f4f0ba36"></a>

```c
#define ESP_I2CEXT1_SCL_IN 70
```

相关声明：[ESP_I2CEXT1_SCL_IN](#a1b6324b294e9e018a5909427f4f0ba36)。

I2C1 SCL 输入（I2C1 SCL input）。

<a id="r_a3ac49ff21fcb59eeab6350821f9107e5"></a>

```c
#define ESP_I2CEXT1_SCL_OUT 70
```

相关声明：[ESP_I2CEXT1_SCL_OUT](#a3ac49ff21fcb59eeab6350821f9107e5)。

I2C1 SCL 输出（I2C1 SCL output）。

<a id="r_abb571ec9f2a59fc281837ca8bd3f2daa"></a>

```c
#define ESP_I2CEXT1_SDA_IN 71
```

相关声明：[ESP_I2CEXT1_SDA_IN](#abb571ec9f2a59fc281837ca8bd3f2daa)。

I2C1 SDA 输入（I2C1 SDA input）。

<a id="r_a3922109459dfd033147e4daf1ed4cd32"></a>

```c
#define ESP_I2CEXT1_SDA_OUT 71
```

相关声明：[ESP_I2CEXT1_SDA_OUT](#a3922109459dfd033147e4daf1ed4cd32)。

I2C1 SDA 输出（I2C1 SDA output）。

<a id="r_a7d76f24f38207025908d03778c337c16"></a>

```c
#define ESP_I2S0_O_BCK_IN 25
```

相关声明：[ESP_I2S0_O_BCK_IN](#a7d76f24f38207025908d03778c337c16)。

I2S0 输出 BCK 输入（I2S0 output BCK input）。

<a id="r_a188af3cf629ca2af88fdf70ce80b2839"></a>

```c
#define ESP_I2S0_O_BCK_OUT 25
```

相关声明：[ESP_I2S0_O_BCK_OUT](#a188af3cf629ca2af88fdf70ce80b2839)。

I2S0 输出 BCK 输出（I2S0 output BCK output）。

<a id="r_a329858f11621f706f0a933886246e177"></a>

```c
#define ESP_I2S0_MCLK_IN 26
```

相关声明：[ESP_I2S0_MCLK_IN](#a329858f11621f706f0a933886246e177)。

I2S0 MCLK 输入（I2S0 MCLK input）。

<a id="r_acd2f3e9c21da61b98fdc86b8a264d9fd"></a>

```c
#define ESP_I2S0_MCLK_OUT 26
```

相关声明：[ESP_I2S0_MCLK_OUT](#acd2f3e9c21da61b98fdc86b8a264d9fd)。

I2S0 MCLK 输出（I2S0 MCLK output）。

<a id="r_a2120890cf3217b9213136b26f441b2c1"></a>

```c
#define ESP_I2S0_O_WS_IN 27
```

相关声明：[ESP_I2S0_O_WS_IN](#a2120890cf3217b9213136b26f441b2c1)。

I2S0 输出 WS 输入（I2S0 output WS input）。

<a id="r_ade09764c2dc746c08d20aa204131f00c"></a>

```c
#define ESP_I2S0_O_WS_OUT 27
```

相关声明：[ESP_I2S0_O_WS_OUT](#ade09764c2dc746c08d20aa204131f00c)。

I2S0 输出 WS 输出（I2S0 output WS output）。

<a id="r_a44c8c070e767c4b93206d8bd4aaa04e4"></a>

```c
#define ESP_I2S0_I_SD_IN 28
```

相关声明：[ESP_I2S0_I_SD_IN](#a44c8c070e767c4b93206d8bd4aaa04e4)。

I2S0 输入 SD 输入（I2S0 input SD input）。

<a id="r_a2e5c6d6971bb801e591e6342cef6a7df"></a>

```c
#define ESP_I2S0_O_SD_OUT 28
```

相关声明：[ESP_I2S0_O_SD_OUT](#a2e5c6d6971bb801e591e6342cef6a7df)。

I2S0 输出 SD 输出（I2S0 output SD output）。

<a id="r_a55e3ca9b5ad7c9d7e02d9bf58e5b138f"></a>

```c
#define ESP_I2S0_O_SD1_OUT 43
```

相关声明：[ESP_I2S0_O_SD1_OUT](#a55e3ca9b5ad7c9d7e02d9bf58e5b138f)。

I2S0 输出 SD1 输出（I2S0 output SD1 output）。

<a id="r_a9d5691158974854c384190717e632899"></a>

```c
#define ESP_I2S0_I_BCK_IN 29
```

相关声明：[ESP_I2S0_I_BCK_IN](#a9d5691158974854c384190717e632899)。

I2S0 输入 BCK 输入（I2S0 input BCK input）。

<a id="r_afe946a4e0dc64adb2ee30b98fee2da00"></a>

```c
#define ESP_I2S0_I_BCK_OUT 29
```

相关声明：[ESP_I2S0_I_BCK_OUT](#afe946a4e0dc64adb2ee30b98fee2da00)。

I2S0 输入 BCK 输出（I2S0 input BCK output）。

<a id="r_a6c15f9cf172971f434a0b20eaf91320f"></a>

```c
#define ESP_I2S0_I_WS_IN 30
```

相关声明：[ESP_I2S0_I_WS_IN](#a6c15f9cf172971f434a0b20eaf91320f)。

I2S0 输入 WS 输入（I2S0 input WS input）。

<a id="r_ab9fb44d3ec5a2ef47c28b4b911a326f2"></a>

```c
#define ESP_I2S0_I_WS_OUT 30
```

相关声明：[ESP_I2S0_I_WS_OUT](#ab9fb44d3ec5a2ef47c28b4b911a326f2)。

I2S0 输入 WS 输出（I2S0 input WS output）。

<a id="r_acb7f23161b4577b7897c3ddf6fc8c9ac"></a>

```c
#define ESP_TWAI1_RX 83
```

相关声明：[ESP_TWAI1_RX](#acb7f23161b4577b7897c3ddf6fc8c9ac)。

TWAI1 RX 输入（TWAI1 RX input）。

<a id="r_ae74556abcddfc37a6e98093cd485085e"></a>

```c
#define ESP_TWAI1_TX 83
```

相关声明：[ESP_TWAI1_TX](#ae74556abcddfc37a6e98093cd485085e)。

TWAI1 TX 输出（TWAI1 TX output）。

<a id="r_ad76afcc4d4a87afb215e50e5edc31181"></a>

```c
#define ESP_TWAI2_RX 86
```

相关声明：[ESP_TWAI2_RX](#ad76afcc4d4a87afb215e50e5edc31181)。

TWAI2 RX 输入（TWAI2 RX input）。

<a id="r_affd3e8cc537484131e8801bcb11dc884"></a>

```c
#define ESP_TWAI2_TX 86
```

相关声明：[ESP_TWAI2_TX](#affd3e8cc537484131e8801bcb11dc884)。

TWAI2 TX 输出（TWAI2 TX output）。

<a id="r_a60a3fe70a1bc5ba71cb46df782901087"></a>

```c
#define ESP_PWM0_SYNC0_IN 89
```

相关声明：[ESP_PWM0_SYNC0_IN](#a60a3fe70a1bc5ba71cb46df782901087)。

MCPWM0 同步 0 输入（MCPWM0 sync 0 input）。

<a id="r_a9397a79a46feab488c88552013790dfc"></a>

```c
#define ESP_PWM0_OUT0A 89
```

相关声明：[ESP_PWM0_OUT0A](#a9397a79a46feab488c88552013790dfc)。

MCPWM0 输出 0A（MCPWM0 output 0A）。

<a id="r_a16dce8622301cb7c2e1c9a9e7a069012"></a>

```c
#define ESP_PWM0_CH0_A_OUT 89
```

相关声明：[ESP_PWM0_CH0_A_OUT](#a16dce8622301cb7c2e1c9a9e7a069012)。

MCPWM0 输出 0A（MCPWM0 output 0A）。

<a id="r_aca616afbb64ed37982624503545a5a72"></a>

```c
#define ESP_PWM0_SYNC1_IN 90
```

相关声明：[ESP_PWM0_SYNC1_IN](#aca616afbb64ed37982624503545a5a72)。

MCPWM0 同步 1 输入（MCPWM0 sync 1 input）。

<a id="r_acb3badfaed73f7069ea23dde375db62a"></a>

```c
#define ESP_PWM0_OUT0B 90
```

相关声明：[ESP_PWM0_OUT0B](#acb3badfaed73f7069ea23dde375db62a)。

MCPWM0 输出 0B（MCPWM0 output 0B）。

<a id="r_abf292303b956ab1dab348fcbf7d59323"></a>

```c
#define ESP_PWM0_CH0_B_OUT 90
```

相关声明：[ESP_PWM0_CH0_B_OUT](#abf292303b956ab1dab348fcbf7d59323)。

MCPWM0 输出 0B（MCPWM0 output 0B）。

<a id="r_a2017681d630abc75e7298c12b86a62ce"></a>

```c
#define ESP_PWM0_SYNC2_IN 91
```

相关声明：[ESP_PWM0_SYNC2_IN](#a2017681d630abc75e7298c12b86a62ce)。

MCPWM0 同步 2 输入（MCPWM0 sync 2 input）。

<a id="r_ae52e5bd4be5563caeb9861267e41d947"></a>

```c
#define ESP_PWM0_OUT1A 91
```

相关声明：[ESP_PWM0_OUT1A](#ae52e5bd4be5563caeb9861267e41d947)。

MCPWM0 输出 1A（MCPWM0 output 1A）。

<a id="r_a6ab5a2408b8c64ce277b146bbdd83e79"></a>

```c
#define ESP_PWM0_CH1_A_OUT 91
```

相关声明：[ESP_PWM0_CH1_A_OUT](#a6ab5a2408b8c64ce277b146bbdd83e79)。

MCPWM0 输出 1A（MCPWM0 output 1A）。

<a id="r_a4a503a957b2fd76f257534b80069caa2"></a>

```c
#define ESP_PWM0_F0_IN 92
```

相关声明：[ESP_PWM0_F0_IN](#a4a503a957b2fd76f257534b80069caa2)。

MCPWM0 故障 0 输入（MCPWM0 fault 0 input）。

<a id="r_a9fa8e944ff2d960c141f8375c9aa0b0e"></a>

```c
#define ESP_PWM0_OUT1B 92
```

相关声明：[ESP_PWM0_OUT1B](#a9fa8e944ff2d960c141f8375c9aa0b0e)。

MCPWM0 输出 1B（MCPWM0 output 1B）。

<a id="r_a328a767873a19e04be758e71b3847177"></a>

```c
#define ESP_PWM0_CH1_B_OUT 92
```

相关声明：[ESP_PWM0_CH1_B_OUT](#a328a767873a19e04be758e71b3847177)。

MCPWM0 输出 1B（MCPWM0 output 1B）。

<a id="r_af536ae867a3d8bcb7644b48c346b4b50"></a>

```c
#define ESP_PWM0_F1_IN 93
```

相关声明：[ESP_PWM0_F1_IN](#af536ae867a3d8bcb7644b48c346b4b50)。

MCPWM0 故障 1 输入（MCPWM0 fault 1 input）。

<a id="r_abf74a2a32a8c36431e2f21d6cd15a610"></a>

```c
#define ESP_PWM0_OUT2A 93
```

相关声明：[ESP_PWM0_OUT2A](#abf74a2a32a8c36431e2f21d6cd15a610)。

MCPWM0 输出 2A（MCPWM0 output 2A）。

<a id="r_a7c498b1682e354f660e84b3781373d70"></a>

```c
#define ESP_PWM0_CH2_A_OUT 93
```

相关声明：[ESP_PWM0_CH2_A_OUT](#a7c498b1682e354f660e84b3781373d70)。

MCPWM0 输出 2A（MCPWM0 output 2A）。

<a id="r_a83f385e6b8a99314cc641083a203322b"></a>

```c
#define ESP_PWM0_F2_IN 94
```

相关声明：[ESP_PWM0_F2_IN](#a83f385e6b8a99314cc641083a203322b)。

MCPWM0 故障 2 输入（MCPWM0 fault 2 input）。

<a id="r_a563105deedf9f7ed6818ab9a8a8aecdc"></a>

```c
#define ESP_PWM0_OUT2B 94
```

相关声明：[ESP_PWM0_OUT2B](#a563105deedf9f7ed6818ab9a8a8aecdc)。

MCPWM0 输出 2B（MCPWM0 output 2B）。

<a id="r_aee1fcd021983675cd645054eef2fe3a3"></a>

```c
#define ESP_PWM0_CH2_B_OUT 94
```

相关声明：[ESP_PWM0_CH2_B_OUT](#aee1fcd021983675cd645054eef2fe3a3)。

MCPWM0 输出 2B（MCPWM0 output 2B）。

<a id="r_a421b59e20586b4f48b7e81bfa0ad4357"></a>

```c
#define ESP_PWM0_CAP0_IN 95
```

相关声明：[ESP_PWM0_CAP0_IN](#a421b59e20586b4f48b7e81bfa0ad4357)。

MCPWM0 捕获 0 输入（MCPWM0 capture 0 input）。

<a id="r_aea7a8712f1502df47721258470ff5b48"></a>

```c
#define ESP_PWM0_CAP1_IN 96
```

相关声明：[ESP_PWM0_CAP1_IN](#aea7a8712f1502df47721258470ff5b48)。

MCPWM0 捕获 1 输入（MCPWM0 capture 1 input）。

<a id="r_ab221240161be67a0f5af577494c8a5ad"></a>

```c
#define ESP_PWM0_CAP2_IN 97
```

相关声明：[ESP_PWM0_CAP2_IN](#ab221240161be67a0f5af577494c8a5ad)。

MCPWM0 捕获 2 输入（MCPWM0 capture 2 input）。

<a id="r_a470396d0e3e83aaab3f7546ae9dfeafb"></a>

```c
#define ESP_PWM1_CH0_A_OUT 95
```

相关声明：[ESP_PWM1_CH0_A_OUT](#a470396d0e3e83aaab3f7546ae9dfeafb)。

MCPWM1 输出 0A（MCPWM1 output 0A）。

<a id="r_af6732227f529b02a52c7174d9cadb9cc"></a>

```c
#define ESP_PWM1_CH0_B_OUT 96
```

相关声明：[ESP_PWM1_CH0_B_OUT](#af6732227f529b02a52c7174d9cadb9cc)。

MCPWM1 输出 0B（MCPWM1 output 0B）。

<a id="r_aad4b629241e84ab2718fb5d10250f710"></a>

```c
#define ESP_PWM1_CH1_A_OUT 97
```

相关声明：[ESP_PWM1_CH1_A_OUT](#aad4b629241e84ab2718fb5d10250f710)。

MCPWM1 输出 1A（MCPWM1 output 1A）。

<a id="r_a9f251384f8a6a10b0fb173c4bfda88ba"></a>

```c
#define ESP_PWM1_SYNC0_IN 98
```

相关声明：[ESP_PWM1_SYNC0_IN](#a9f251384f8a6a10b0fb173c4bfda88ba)。

MCPWM1 同步 0 输入（MCPWM1 sync 0 input）。

<a id="r_ac95c1743c3e3af80475bd7827d619690"></a>

```c
#define ESP_PWM1_CH1_B_OUT 98
```

相关声明：[ESP_PWM1_CH1_B_OUT](#ac95c1743c3e3af80475bd7827d619690)。

MCPWM1 输出 1B（MCPWM1 output 1B）。

<a id="r_a646d7d644b5d4ec403eab7ff793cf7b2"></a>

```c
#define ESP_PWM1_SYNC1_IN 99
```

相关声明：[ESP_PWM1_SYNC1_IN](#a646d7d644b5d4ec403eab7ff793cf7b2)。

MCPWM1 同步 1 输入（MCPWM1 sync 1 input）。

<a id="r_a15121252274b653dfeef2d9a16f2c5e3"></a>

```c
#define ESP_PWM1_CH2_A_OUT 99
```

相关声明：[ESP_PWM1_CH2_A_OUT](#a15121252274b653dfeef2d9a16f2c5e3)。

MCPWM1 输出 2A（MCPWM1 output 2A）。

<a id="r_a56a67f8e168a4e7545e3ca4bcf7c8d89"></a>

```c
#define ESP_PWM1_SYNC2_IN 100
```

相关声明：[ESP_PWM1_SYNC2_IN](#a56a67f8e168a4e7545e3ca4bcf7c8d89)。

MCPWM1 同步 2 输入（MCPWM1 sync 2 input）。

<a id="r_a2c9296238ae64c0e744cffb8756d4bc1"></a>

```c
#define ESP_PWM1_CH2_B_OUT 100
```

相关声明：[ESP_PWM1_CH2_B_OUT](#a2c9296238ae64c0e744cffb8756d4bc1)。

MCPWM1 输出 2B（MCPWM1 output 2B）。

<a id="r_a09c262c332e65ccc9eb2d91d976958e3"></a>

```c
#define ESP_PWM1_F0_IN 101
```

相关声明：[ESP_PWM1_F0_IN](#a09c262c332e65ccc9eb2d91d976958e3)。

MCPWM1 故障 0 输入（MCPWM1 fault 0 input）。

<a id="r_af4b1c0ff4e222f09eee18cbb85cedb67"></a>

```c
#define ESP_PWM1_F1_IN 102
```

相关声明：[ESP_PWM1_F1_IN](#af4b1c0ff4e222f09eee18cbb85cedb67)。

MCPWM1 故障 1 输入（MCPWM1 fault 1 input）。

<a id="r_ac911f11a68e10d359cffe49864739e2d"></a>

```c
#define ESP_PWM1_F2_IN 103
```

相关声明：[ESP_PWM1_F2_IN](#ac911f11a68e10d359cffe49864739e2d)。

MCPWM1 故障 2 输入（MCPWM1 fault 2 input）。

<a id="r_a8f2dcd1f46c2a5a5da3be188dca9e3a0"></a>

```c
#define ESP_PWM1_CAP0_IN 104
```

相关声明：[ESP_PWM1_CAP0_IN](#a8f2dcd1f46c2a5a5da3be188dca9e3a0)。

MCPWM1 捕获 0 输入（MCPWM1 capture 0 input）。

<a id="r_a8b97c639d66dcb8400aefc344bf490d1"></a>

```c
#define ESP_PWM1_CAP1_IN 105
```

相关声明：[ESP_PWM1_CAP1_IN](#a8b97c639d66dcb8400aefc344bf490d1)。

MCPWM1 捕获 1 输入（MCPWM1 capture 1 input）。

<a id="r_a23b8540974bcf9dbd5c0ff92d9b69ac9"></a>

```c
#define ESP_PWM1_CAP2_IN 106
```

相关声明：[ESP_PWM1_CAP2_IN](#a23b8540974bcf9dbd5c0ff92d9b69ac9)。

MCPWM1 捕获 2 输入（MCPWM1 capture 2 input）。

<a id="r_a5d9314d65cffc6a2af35b6d95e96d4a7"></a>

```c
#define ESP_TWAI0_RX 80
```

相关声明：[ESP_TWAI0_RX](#a5d9314d65cffc6a2af35b6d95e96d4a7)。

TWAI0 RX 输入（TWAI0 RX input）。

<a id="r_a861efcd37d8828dceffb156de3f1cced"></a>

```c
#define ESP_TWAI0_TX 80
```

相关声明：[ESP_TWAI0_TX](#a861efcd37d8828dceffb156de3f1cced)。

TWAI0 TX 输出（TWAI0 TX output）。

<a id="r_a62dfcd88747c61acb53dc85c1751f1d3"></a>

```c
#define ESP_LEDC_LS_SIG_OUT0 126
```

相关声明：[ESP_LEDC_LS_SIG_OUT0](#a62dfcd88747c61acb53dc85c1751f1d3)。

LEDC 低速 信号 输出 0（LEDC low-speed signal output 0）。

<a id="r_a5cad9206cfeea93b42e5456228c7d580"></a>

```c
#define ESP_LEDC_LS_SIG_OUT1 127
```

相关声明：[ESP_LEDC_LS_SIG_OUT1](#a5cad9206cfeea93b42e5456228c7d580)。

LEDC 低速 信号 输出 1（LEDC low-speed signal output 1）。

<a id="r_ab408070e7c700805db165c3876b6c588"></a>

```c
#define ESP_LEDC_LS_SIG_OUT2 128
```

相关声明：[ESP_LEDC_LS_SIG_OUT2](#ab408070e7c700805db165c3876b6c588)。

LEDC 低速 信号 输出 2（LEDC low-speed signal output 2）。

<a id="r_a438aee217c6c94a2962a3d98935b5717"></a>

```c
#define ESP_LEDC_LS_SIG_OUT3 129
```

相关声明：[ESP_LEDC_LS_SIG_OUT3](#a438aee217c6c94a2962a3d98935b5717)。

LEDC 低速 信号 输出 3（LEDC low-speed signal output 3）。

<a id="r_ada93dcffffc15362be4b7432a8033559"></a>

```c
#define ESP_LEDC_LS_SIG_OUT4 130
```

相关声明：[ESP_LEDC_LS_SIG_OUT4](#ada93dcffffc15362be4b7432a8033559)。

LEDC 低速 信号 输出 4（LEDC low-speed signal output 4）。

<a id="r_a34fc029ec45756ca7064580f57db1cc7"></a>

```c
#define ESP_LEDC_LS_SIG_OUT5 131
```

相关声明：[ESP_LEDC_LS_SIG_OUT5](#a34fc029ec45756ca7064580f57db1cc7)。

LEDC 低速 信号 输出 5（LEDC low-speed signal output 5）。

<a id="r_a28b01adea7e0bcc8b76fe05d58c1cbd0"></a>

```c
#define ESP_LEDC_LS_SIG_OUT6 132
```

相关声明：[ESP_LEDC_LS_SIG_OUT6](#a28b01adea7e0bcc8b76fe05d58c1cbd0)。

LEDC 低速 信号 输出 6（LEDC low-speed signal output 6）。

<a id="r_a2ea140f2da1a15b24dcaa3592909ca35"></a>

```c
#define ESP_LEDC_LS_SIG_OUT7 133
```

相关声明：[ESP_LEDC_LS_SIG_OUT7](#a2ea140f2da1a15b24dcaa3592909ca35)。

LEDC 低速 信号 输出 7（LEDC low-speed signal output 7）。

<a id="r_acf123456a5b9d94f370309ad39672e34"></a>

```c
#define ESP_PCNT_SIG_CH0_IN0 141
```

相关声明：[ESP_PCNT_SIG_CH0_IN0](#acf123456a5b9d94f370309ad39672e34)。

PCNT 单元 0 通道 0 信号 输入（PCNT unit 0 channel 0 signal input）。

<a id="r_a99db3d1c4e07e11fc09a4024a54fcea6"></a>

```c
#define ESP_PCNT_SIG_CH0_IN1 142
```

相关声明：[ESP_PCNT_SIG_CH0_IN1](#a99db3d1c4e07e11fc09a4024a54fcea6)。

PCNT 单元 1 通道 0 信号 输入（PCNT unit 1 channel 0 signal input）。

<a id="r_a4f9e798a260fb6ac4c39262f20253244"></a>

```c
#define ESP_PCNT_SIG_CH0_IN2 143
```

相关声明：[ESP_PCNT_SIG_CH0_IN2](#a4f9e798a260fb6ac4c39262f20253244)。

PCNT 单元 2 通道 0 信号 输入（PCNT unit 2 channel 0 signal input）。

<a id="r_acd8d20d89508b532a4e2749499263de3"></a>

```c
#define ESP_PCNT_SIG_CH0_IN3 144
```

相关声明：[ESP_PCNT_SIG_CH0_IN3](#acd8d20d89508b532a4e2749499263de3)。

PCNT 单元 3 通道 0 信号 输入（PCNT unit 3 channel 0 signal input）。

<a id="r_a800813b2c23f7e4bb23e032e0802a459"></a>

```c
#define ESP_PCNT_SIG_CH1_IN0 145
```

相关声明：[ESP_PCNT_SIG_CH1_IN0](#a800813b2c23f7e4bb23e032e0802a459)。

PCNT 单元 0 通道 1 信号 输入（PCNT unit 0 channel 1 signal input）。

<a id="r_a730113779d69ca86b257060678f8cbec"></a>

```c
#define ESP_PCNT_SIG_CH1_IN1 146
```

相关声明：[ESP_PCNT_SIG_CH1_IN1](#a730113779d69ca86b257060678f8cbec)。

PCNT 单元 1 通道 1 信号 输入（PCNT unit 1 channel 1 signal input）。

<a id="r_a38365b3f9a2b49ef2714c38d00d293c5"></a>

```c
#define ESP_PCNT_SIG_CH1_IN2 147
```

相关声明：[ESP_PCNT_SIG_CH1_IN2](#a38365b3f9a2b49ef2714c38d00d293c5)。

PCNT 单元 2 通道 1 信号 输入（PCNT unit 2 channel 1 signal input）。

<a id="r_ac54a606ee7096db15cdb9453b04ac72d"></a>

```c
#define ESP_PCNT_SIG_CH1_IN3 148
```

相关声明：[ESP_PCNT_SIG_CH1_IN3](#ac54a606ee7096db15cdb9453b04ac72d)。

PCNT 单元 3 通道 1 信号 输入（PCNT unit 3 channel 1 signal input）。

<a id="r_a7e3c939b0b32332a35f0bead0aa4a2a6"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN0 149
```

相关声明：[ESP_PCNT_CTRL_CH0_IN0](#a7e3c939b0b32332a35f0bead0aa4a2a6)。

PCNT 单元 0 通道 0 控制 输入（PCNT unit 0 channel 0 control input）。

<a id="r_a9ec8d490316b9f043fe5e9160a7cf7e0"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN1 150
```

相关声明：[ESP_PCNT_CTRL_CH0_IN1](#a9ec8d490316b9f043fe5e9160a7cf7e0)。

PCNT 单元 1 通道 0 控制 输入（PCNT unit 1 channel 0 control input）。

<a id="r_a540cbfcd205911955effcc9814f9707c"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN2 151
```

相关声明：[ESP_PCNT_CTRL_CH0_IN2](#a540cbfcd205911955effcc9814f9707c)。

PCNT 单元 2 通道 0 控制 输入（PCNT unit 2 channel 0 control input）。

<a id="r_a96e8bd4584ab671a1b0c3f0adb440943"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN3 152
```

相关声明：[ESP_PCNT_CTRL_CH0_IN3](#a96e8bd4584ab671a1b0c3f0adb440943)。

PCNT 单元 3 通道 0 控制 输入（PCNT unit 3 channel 0 control input）。

<a id="r_a88c5eb5c7f4169ce3e7f7056b42989a7"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN0 153
```

相关声明：[ESP_PCNT_CTRL_CH1_IN0](#a88c5eb5c7f4169ce3e7f7056b42989a7)。

PCNT 单元 0 通道 1 控制 输入（PCNT unit 0 channel 1 control input）。

<a id="r_a0bbfffdef085eb6cedc3d1232766cb38"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN1 154
```

相关声明：[ESP_PCNT_CTRL_CH1_IN1](#a0bbfffdef085eb6cedc3d1232766cb38)。

PCNT 单元 1 通道 1 控制 输入（PCNT unit 1 channel 1 control input）。

<a id="r_abf6c210e19582b06e3d6c546a009ef5b"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN2 155
```

相关声明：[ESP_PCNT_CTRL_CH1_IN2](#abf6c210e19582b06e3d6c546a009ef5b)。

PCNT 单元 2 通道 1 控制 输入（PCNT unit 2 channel 1 control input）。

<a id="r_a0a926d350fc11d737b545c53b3ba1671"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN3 156
```

相关声明：[ESP_PCNT_CTRL_CH1_IN3](#a0a926d350fc11d737b545c53b3ba1671)。

PCNT 单元 3 通道 1 控制 输入（PCNT unit 3 channel 1 control input）。

<a id="r_a12b04715f671516d1182830f5a725c8c"></a>

```c
#define ESP_EMAC_MDI_I 107
```

相关声明：[ESP_EMAC_MDI_I](#a12b04715f671516d1182830f5a725c8c)。

EMAC MDIO 数据 输入（EMAC MDIO data input）。

<a id="r_a2f2df30f4a55a81215948fdea44a04a7"></a>

```c
#define ESP_EMAC_MDC_O 108
```

相关声明：[ESP_EMAC_MDC_O](#a2f2df30f4a55a81215948fdea44a04a7)。

EMAC MDIO 时钟 输出（EMAC MDIO clock output）。

<a id="r_a0451fae682abbbae4403c71563a0cc13"></a>

```c
#define ESP_EMAC_MDO_O 109
```

相关声明：[ESP_EMAC_MDO_O](#a0451fae682abbbae4403c71563a0cc13)。

EMAC MDIO 数据 输出（EMAC MDIO data output）。

<a id="r_a9f11418b93b11426081ad8fcef9332d3"></a>

```c
#define ESP_PCNT_SIG_CH0_IN0 141
```

相关声明：[ESP_PCNT_SIG_CH0_IN0](#a9f11418b93b11426081ad8fcef9332d3)。

PCNT 单元 0 通道 0 信号 输入（PCNT unit 0 channel 0 signal input）。

<a id="r_adb1cce7faf274879f3af380f56e5741c"></a>

```c
#define ESP_PCNT_SIG_CH0_IN1 142
```

相关声明：[ESP_PCNT_SIG_CH0_IN1](#adb1cce7faf274879f3af380f56e5741c)。

PCNT 单元 1 通道 0 信号 输入（PCNT unit 1 channel 0 signal input）。

<a id="r_adc95b489bf9613b40c1602d89d5e92ef"></a>

```c
#define ESP_PCNT_SIG_CH0_IN2 143
```

相关声明：[ESP_PCNT_SIG_CH0_IN2](#adc95b489bf9613b40c1602d89d5e92ef)。

PCNT 单元 2 通道 0 信号 输入（PCNT unit 2 channel 0 signal input）。

<a id="r_a2722e320806e8013009e50fb0a4b4782"></a>

```c
#define ESP_PCNT_SIG_CH0_IN3 144
```

相关声明：[ESP_PCNT_SIG_CH0_IN3](#a2722e320806e8013009e50fb0a4b4782)。

PCNT 单元 3 通道 0 信号 输入（PCNT unit 3 channel 0 signal input）。

<a id="r_ad5d93140fc2134619b9e4274ded924d8"></a>

```c
#define ESP_PCNT_SIG_CH1_IN0 145
```

相关声明：[ESP_PCNT_SIG_CH1_IN0](#ad5d93140fc2134619b9e4274ded924d8)。

PCNT 单元 0 通道 1 信号 输入（PCNT unit 0 channel 1 signal input）。

<a id="r_aa75acbb9c392b686e44eeaa9898abd32"></a>

```c
#define ESP_PCNT_SIG_CH1_IN1 146
```

相关声明：[ESP_PCNT_SIG_CH1_IN1](#aa75acbb9c392b686e44eeaa9898abd32)。

PCNT 单元 1 通道 1 信号 输入（PCNT unit 1 channel 1 signal input）。

<a id="r_add3d775b32fda9000309b5082df4ac12"></a>

```c
#define ESP_PCNT_SIG_CH1_IN2 147
```

相关声明：[ESP_PCNT_SIG_CH1_IN2](#add3d775b32fda9000309b5082df4ac12)。

PCNT 单元 2 通道 1 信号 输入（PCNT unit 2 channel 1 signal input）。

<a id="r_a0aa25f1f2355e5fa8ccc6afa4d16abcb"></a>

```c
#define ESP_PCNT_SIG_CH1_IN3 148
```

相关声明：[ESP_PCNT_SIG_CH1_IN3](#a0aa25f1f2355e5fa8ccc6afa4d16abcb)。

PCNT 单元 3 通道 1 信号 输入（PCNT unit 3 channel 1 signal input）。

<a id="r_a5825bd51c50ff93c17d519bca9a80c24"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN0 149
```

相关声明：[ESP_PCNT_CTRL_CH0_IN0](#a5825bd51c50ff93c17d519bca9a80c24)。

PCNT 单元 0 通道 0 控制 输入（PCNT unit 0 channel 0 control input）。

<a id="r_a778aad550aadb3624623678e8f21d9a8"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN1 150
```

相关声明：[ESP_PCNT_CTRL_CH0_IN1](#a778aad550aadb3624623678e8f21d9a8)。

PCNT 单元 1 通道 0 控制 输入（PCNT unit 1 channel 0 control input）。

<a id="r_abbe49a9151f6e729321b0354214772ea"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN2 151
```

相关声明：[ESP_PCNT_CTRL_CH0_IN2](#abbe49a9151f6e729321b0354214772ea)。

PCNT 单元 2 通道 0 控制 输入（PCNT unit 2 channel 0 control input）。

<a id="r_af79dbaee0b062b9c200e744047d95c15"></a>

```c
#define ESP_PCNT_CTRL_CH0_IN3 152
```

相关声明：[ESP_PCNT_CTRL_CH0_IN3](#af79dbaee0b062b9c200e744047d95c15)。

PCNT 单元 3 通道 0 控制 输入（PCNT unit 3 channel 0 control input）。

<a id="r_a3c0ec3d7841577a05f1615116321edb4"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN0 153
```

相关声明：[ESP_PCNT_CTRL_CH1_IN0](#a3c0ec3d7841577a05f1615116321edb4)。

PCNT 单元 0 通道 1 控制 输入（PCNT unit 0 channel 1 control input）。

<a id="r_ae965d09b63d5210163f5b96e975ea8ef"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN1 154
```

相关声明：[ESP_PCNT_CTRL_CH1_IN1](#ae965d09b63d5210163f5b96e975ea8ef)。

PCNT 单元 1 通道 1 控制 输入（PCNT unit 1 channel 1 control input）。

<a id="r_ab72266d11f5fc7d04c2e87494cfd80cf"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN2 155
```

相关声明：[ESP_PCNT_CTRL_CH1_IN2](#ab72266d11f5fc7d04c2e87494cfd80cf)。

PCNT 单元 2 通道 1 控制 输入（PCNT unit 2 channel 1 control input）。

<a id="r_aa28ef045c9adfd7e9dc6bd538f49d969"></a>

```c
#define ESP_PCNT_CTRL_CH1_IN3 156
```

相关声明：[ESP_PCNT_CTRL_CH1_IN3](#aa28ef045c9adfd7e9dc6bd538f49d969)。

PCNT 单元 3 通道 1 控制 输入（PCNT unit 3 channel 1 control input）。

<a id="r_ad9bae9b4884a356e465656d1ee8d61cd"></a>

```c
#define ESP_RMT_SIG_IN0 246
```

相关声明：[ESP_RMT_SIG_IN0](#ad9bae9b4884a356e465656d1ee8d61cd)。

RMT 通道 0 输入（RMT channel 0 input）。

<a id="r_a25343fbc20a0c542bcdc21cdfade867b"></a>

```c
#define ESP_RMT_SIG_OUT0 246
```

相关声明：[ESP_RMT_SIG_OUT0](#a25343fbc20a0c542bcdc21cdfade867b)。

RMT 通道 0 输出（RMT channel 0 output）。

<a id="r_ab6c6293e6845ba4bf4d05b84102ffdcf"></a>

```c
#define ESP_RMT_SIG_IN1 247
```

相关声明：[ESP_RMT_SIG_IN1](#ab6c6293e6845ba4bf4d05b84102ffdcf)。

RMT 通道 1 输入（RMT channel 1 input）。

<a id="r_a6d082fb1c7397d784a3075108e0dea73"></a>

```c
#define ESP_RMT_SIG_OUT1 247
```

相关声明：[ESP_RMT_SIG_OUT1](#a6d082fb1c7397d784a3075108e0dea73)。

RMT 通道 1 输出（RMT channel 1 output）。

<a id="r_af88ebdd0d2d02ac58d720c001ccc155b"></a>

```c
#define ESP_RMT_SIG_IN2 248
```

相关声明：[ESP_RMT_SIG_IN2](#af88ebdd0d2d02ac58d720c001ccc155b)。

RMT 通道 2 输入（RMT channel 2 input）。

<a id="r_ad657c1ddcf9c335ac7876464b80b2705"></a>

```c
#define ESP_RMT_SIG_OUT2 248
```

相关声明：[ESP_RMT_SIG_OUT2](#ad657c1ddcf9c335ac7876464b80b2705)。

RMT 通道 2 输出（RMT channel 2 output）。

<a id="r_a1f930cd82690248b839f16ff7738f32c"></a>

```c
#define ESP_RMT_SIG_IN3 249
```

相关声明：[ESP_RMT_SIG_IN3](#a1f930cd82690248b839f16ff7738f32c)。

RMT 通道 3 输入（RMT channel 3 input）。

<a id="r_ae60033bb70ca9ff7c2b52368d24a8ab8"></a>

```c
#define ESP_RMT_SIG_OUT3 249
```

相关声明：[ESP_RMT_SIG_OUT3](#ae60033bb70ca9ff7c2b52368d24a8ab8)。

RMT 通道 3 输出（RMT channel 3 output）。

## 5.2\_详细说明（Detailed Documentation）

<a id="a2f2df30f4a55a81215948fdea44a04a7"></a>

### `ESP_EMAC_MDC_O`

```c
#define ESP_EMAC_MDC_O 108
```

EMAC MDIO 时钟 输出（EMAC MDIO clock output）。

<a id="a12b04715f671516d1182830f5a725c8c"></a>

### `ESP_EMAC_MDI_I`

```c
#define ESP_EMAC_MDI_I 107
```

EMAC MDIO 数据 输入（EMAC MDIO data input）。

<a id="a0451fae682abbbae4403c71563a0cc13"></a>

### `ESP_EMAC_MDO_O`

```c
#define ESP_EMAC_MDO_O 109
```

EMAC MDIO 数据 输出（EMAC MDIO data output）。

<a id="ade88988460c131e8c6775794588b0eb8"></a>

### `ESP_FSPICLK_IN`

```c
#define ESP_FSPICLK_IN 53
```

FSPI 时钟 输入（FSPI clock input）。

<a id="ab8c5397dc530f6326c3d10b31e59e168"></a>

### `ESP_FSPICLK_OUT`

```c
#define ESP_FSPICLK_OUT 53
```

FSPI 时钟 输出（FSPI clock output）。

<a id="a96ca1328e76337d289f6e65faf33d75c"></a>

### `ESP_FSPICS0_IN`

```c
#define ESP_FSPICS0_IN 62
```

FSPI CS0 输入（FSPI CS0 input）。

<a id="ad1be1401b282275eaef46b9a598c6a40"></a>

### `ESP_FSPICS0_OUT`

```c
#define ESP_FSPICS0_OUT 62
```

FSPI CS0 输出（FSPI CS0 output）。

<a id="a7910521af840d42edd3c0a667cf90c5f"></a>

### `ESP_FSPID_IN`

```c
#define ESP_FSPID_IN 55
```

FSPI D 输入（FSPI D input）。

<a id="a02bd34821e8a4bf0038b9af417ec161a"></a>

### `ESP_FSPID_OUT`

```c
#define ESP_FSPID_OUT 55
```

FSPI D 输出（FSPI D output）。

<a id="a60ff087a3d85a356d77f060a6698d00b"></a>

### `ESP_FSPIHD_IN`

```c
#define ESP_FSPIHD_IN 56
```

FSPI HD 输入（FSPI HD input）。

<a id="ac71bc137b93bd6c0c8a1ebe24a70a613"></a>

### `ESP_FSPIHD_OUT`

```c
#define ESP_FSPIHD_OUT 56
```

FSPI HD 输出（FSPI HD output）。

<a id="ab603b7bf7d016e85653a5c3be5c01293"></a>

### `ESP_FSPIQ_IN`

```c
#define ESP_FSPIQ_IN 54
```

FSPI Q 输入（FSPI Q input）。

<a id="a8b3ea6ad374fa010b46b48072fa87ccb"></a>

### `ESP_FSPIQ_OUT`

```c
#define ESP_FSPIQ_OUT 54
```

FSPI Q 输出（FSPI Q output）。

<a id="a4d4c4a13b820cab6d94da8fe08120a2f"></a>

### `ESP_FSPIWP_IN`

```c
#define ESP_FSPIWP_IN 57
```

FSPI WP 输入（FSPI WP input）。

<a id="a83c4f18d726984cc98caeea9b7677ca1"></a>

### `ESP_FSPIWP_OUT`

```c
#define ESP_FSPIWP_OUT 57
```

FSPI WP 输出（FSPI WP output）。

<a id="ab607ce367da34ab0f1bd7fa648273cf1"></a>

### `ESP_I2CEXT0_SCL_IN`

```c
#define ESP_I2CEXT0_SCL_IN 68
```

I2C0 SCL 输入（I2C0 SCL input）。

<a id="a2144cc62df795547ccf2bbe3ee4c629f"></a>

### `ESP_I2CEXT0_SCL_OUT`

```c
#define ESP_I2CEXT0_SCL_OUT 68
```

I2C0 SCL 输出（I2C0 SCL output）。

<a id="afa7061c87135b9dabe5c54f5f4ce16e6"></a>

### `ESP_I2CEXT0_SDA_IN`

```c
#define ESP_I2CEXT0_SDA_IN 69
```

I2C0 SDA 输入（I2C0 SDA input）。

<a id="aabf1378b0ad2028c36c3bb74c81d7049"></a>

### `ESP_I2CEXT0_SDA_OUT`

```c
#define ESP_I2CEXT0_SDA_OUT 69
```

I2C0 SDA 输出（I2C0 SDA output）。

<a id="a1b6324b294e9e018a5909427f4f0ba36"></a>

### `ESP_I2CEXT1_SCL_IN`

```c
#define ESP_I2CEXT1_SCL_IN 70
```

I2C1 SCL 输入（I2C1 SCL input）。

<a id="a3ac49ff21fcb59eeab6350821f9107e5"></a>

### `ESP_I2CEXT1_SCL_OUT`

```c
#define ESP_I2CEXT1_SCL_OUT 70
```

I2C1 SCL 输出（I2C1 SCL output）。

<a id="abb571ec9f2a59fc281837ca8bd3f2daa"></a>

### `ESP_I2CEXT1_SDA_IN`

```c
#define ESP_I2CEXT1_SDA_IN 71
```

I2C1 SDA 输入（I2C1 SDA input）。

<a id="a3922109459dfd033147e4daf1ed4cd32"></a>

### `ESP_I2CEXT1_SDA_OUT`

```c
#define ESP_I2CEXT1_SDA_OUT 71
```

I2C1 SDA 输出（I2C1 SDA output）。

<a id="a9d5691158974854c384190717e632899"></a>

### `ESP_I2S0_I_BCK_IN`

```c
#define ESP_I2S0_I_BCK_IN 29
```

I2S0 输入 BCK 输入（I2S0 input BCK input）。

<a id="afe946a4e0dc64adb2ee30b98fee2da00"></a>

### `ESP_I2S0_I_BCK_OUT`

```c
#define ESP_I2S0_I_BCK_OUT 29
```

I2S0 输入 BCK 输出（I2S0 input BCK output）。

<a id="a44c8c070e767c4b93206d8bd4aaa04e4"></a>

### `ESP_I2S0_I_SD_IN`

```c
#define ESP_I2S0_I_SD_IN 28
```

I2S0 输入 SD 输入（I2S0 input SD input）。

<a id="a6c15f9cf172971f434a0b20eaf91320f"></a>

### `ESP_I2S0_I_WS_IN`

```c
#define ESP_I2S0_I_WS_IN 30
```

I2S0 输入 WS 输入（I2S0 input WS input）。

<a id="ab9fb44d3ec5a2ef47c28b4b911a326f2"></a>

### `ESP_I2S0_I_WS_OUT`

```c
#define ESP_I2S0_I_WS_OUT 30
```

I2S0 输入 WS 输出（I2S0 input WS output）。

<a id="a329858f11621f706f0a933886246e177"></a>

### `ESP_I2S0_MCLK_IN`

```c
#define ESP_I2S0_MCLK_IN 26
```

I2S0 MCLK 输入（I2S0 MCLK input）。

<a id="acd2f3e9c21da61b98fdc86b8a264d9fd"></a>

### `ESP_I2S0_MCLK_OUT`

```c
#define ESP_I2S0_MCLK_OUT 26
```

I2S0 MCLK 输出（I2S0 MCLK output）。

<a id="a7d76f24f38207025908d03778c337c16"></a>

### `ESP_I2S0_O_BCK_IN`

```c
#define ESP_I2S0_O_BCK_IN 25
```

I2S0 输出 BCK 输入（I2S0 output BCK input）。

<a id="a188af3cf629ca2af88fdf70ce80b2839"></a>

### `ESP_I2S0_O_BCK_OUT`

```c
#define ESP_I2S0_O_BCK_OUT 25
```

I2S0 输出 BCK 输出（I2S0 output BCK output）。

<a id="a55e3ca9b5ad7c9d7e02d9bf58e5b138f"></a>

### `ESP_I2S0_O_SD1_OUT`

```c
#define ESP_I2S0_O_SD1_OUT 43
```

I2S0 输出 SD1 输出（I2S0 output SD1 output）。

<a id="a2e5c6d6971bb801e591e6342cef6a7df"></a>

### `ESP_I2S0_O_SD_OUT`

```c
#define ESP_I2S0_O_SD_OUT 28
```

I2S0 输出 SD 输出（I2S0 output SD output）。

<a id="a2120890cf3217b9213136b26f441b2c1"></a>

### `ESP_I2S0_O_WS_IN`

```c
#define ESP_I2S0_O_WS_IN 27
```

I2S0 输出 WS 输入（I2S0 output WS input）。

<a id="ade09764c2dc746c08d20aa204131f00c"></a>

### `ESP_I2S0_O_WS_OUT`

```c
#define ESP_I2S0_O_WS_OUT 27
```

I2S0 输出 WS 输出（I2S0 output WS output）。

<a id="adb44e1303d1f50193926ba57c13bf2bc"></a>

### `ESP_I2S1_I_BCK_IN`

```c
#define ESP_I2S1_I_BCK_IN 35
```

I2S1 输入 BCK 输入（I2S1 input BCK input）。

<a id="aec57e3323d6bf84e584a8a26b9679fcf"></a>

### `ESP_I2S1_I_BCK_OUT`

```c
#define ESP_I2S1_I_BCK_OUT 35
```

I2S1 输入 BCK 输出（I2S1 input BCK output）。

<a id="ae1d94e076cf75a07a65ab53f4cfa5faf"></a>

### `ESP_I2S1_I_SD_IN`

```c
#define ESP_I2S1_I_SD_IN 34
```

I2S1 输入 SD 输入（I2S1 input SD input）。

<a id="ae6761382c71944b44bf1c0ff748aefed"></a>

### `ESP_I2S1_I_WS_IN`

```c
#define ESP_I2S1_I_WS_IN 36
```

I2S1 输入 WS 输入（I2S1 input WS input）。

<a id="a36b4b39cdd4e2fb950d291bcecc2f562"></a>

### `ESP_I2S1_I_WS_OUT`

```c
#define ESP_I2S1_I_WS_OUT 36
```

I2S1 输入 WS 输出（I2S1 input WS output）。

<a id="af00f358d0012d5a4e85a0610f9da2ace"></a>

### `ESP_I2S1_MCLK_IN`

```c
#define ESP_I2S1_MCLK_IN 32
```

I2S1 MCLK 输入（I2S1 MCLK input）。

<a id="aeeb2b00d8b3172832532d96b2282d4d2"></a>

### `ESP_I2S1_MCLK_OUT`

```c
#define ESP_I2S1_MCLK_OUT 32
```

I2S1 MCLK 输出（I2S1 MCLK output）。

<a id="a8c8a6b9063b2c47dd6b9db6b853e4ec1"></a>

### `ESP_I2S1_O_BCK_IN`

```c
#define ESP_I2S1_O_BCK_IN 31
```

I2S1 输出 BCK 输入（I2S1 output BCK input）。

<a id="a67af83425f55eb3d3873d99bb5c23129"></a>

### `ESP_I2S1_O_BCK_OUT`

```c
#define ESP_I2S1_O_BCK_OUT 31
```

I2S1 输出 BCK 输出（I2S1 output BCK output）。

<a id="a266216587dd80023ffa859de13a21848"></a>

### `ESP_I2S1_O_SD_OUT`

```c
#define ESP_I2S1_O_SD_OUT 34
```

I2S1 输出 SD 输出（I2S1 output SD output）。

<a id="aeced96606d401941ddecf93865940045"></a>

### `ESP_I2S1_O_WS_IN`

```c
#define ESP_I2S1_O_WS_IN 33
```

I2S1 输出 WS 输入（I2S1 output WS input）。

<a id="a22a4414a710032bb89da262dfe11b399"></a>

### `ESP_I2S1_O_WS_OUT`

```c
#define ESP_I2S1_O_WS_OUT 33
```

I2S1 输出 WS 输出（I2S1 output WS output）。

<a id="a59b9c3d4e7e71913b403e34dde61e705"></a>

### `ESP_I2S2_I_BCK_IN`

```c
#define ESP_I2S2_I_BCK_IN 41
```

I2S2 输入 BCK 输入（I2S2 input BCK input）。

<a id="a08a6233fbbf192f5594bb7b0f1592300"></a>

### `ESP_I2S2_I_BCK_OUT`

```c
#define ESP_I2S2_I_BCK_OUT 41
```

I2S2 输入 BCK 输出（I2S2 input BCK output）。

<a id="afbc86f6ecc0eff3482c0dd717e4a8b76"></a>

### `ESP_I2S2_I_SD_IN`

```c
#define ESP_I2S2_I_SD_IN 40
```

I2S2 输入 SD 输入（I2S2 input SD input）。

<a id="a95eb4982bcfd2f08a24d98291f9aa412"></a>

### `ESP_I2S2_I_WS_IN`

```c
#define ESP_I2S2_I_WS_IN 42
```

I2S2 输入 WS 输入（I2S2 input WS input）。

<a id="abdc9f33c6798b7c56589a4daf462261a"></a>

### `ESP_I2S2_I_WS_OUT`

```c
#define ESP_I2S2_I_WS_OUT 42
```

I2S2 输入 WS 输出（I2S2 input WS output）。

<a id="a1ba6505c35afd42628424421d5a4abcd"></a>

### `ESP_I2S2_MCLK_IN`

```c
#define ESP_I2S2_MCLK_IN 38
```

I2S2 MCLK 输入（I2S2 MCLK input）。

<a id="ab4b411f39dd5d5e075618f9a3b2bbf44"></a>

### `ESP_I2S2_MCLK_OUT`

```c
#define ESP_I2S2_MCLK_OUT 38
```

I2S2 MCLK 输出（I2S2 MCLK output）。

<a id="ab8d8d58ed38fe5584b3b7b485156b824"></a>

### `ESP_I2S2_O_BCK_IN`

```c
#define ESP_I2S2_O_BCK_IN 37
```

I2S2 输出 BCK 输入（I2S2 output BCK input）。

<a id="a5aa289413958c5d7406d6895f7338f1e"></a>

### `ESP_I2S2_O_BCK_OUT`

```c
#define ESP_I2S2_O_BCK_OUT 37
```

I2S2 输出 BCK 输出（I2S2 output BCK output）。

<a id="aecc44f4003ce107d283e7f053b9c5e11"></a>

### `ESP_I2S2_O_SD_OUT`

```c
#define ESP_I2S2_O_SD_OUT 40
```

I2S2 输出 SD 输出（I2S2 output SD output）。

<a id="a424284c56809d44a6f5707625611b653"></a>

### `ESP_I2S2_O_WS_IN`

```c
#define ESP_I2S2_O_WS_IN 39
```

I2S2 输出 WS 输入（I2S2 output WS input）。

<a id="ad2f0863220d12e726c276eecb2d0475d"></a>

### `ESP_I2S2_O_WS_OUT`

```c
#define ESP_I2S2_O_WS_OUT 39
```

I2S2 输出 WS 输出（I2S2 output WS output）。

<a id="a62dfcd88747c61acb53dc85c1751f1d3"></a>

### `ESP_LEDC_LS_SIG_OUT0`

```c
#define ESP_LEDC_LS_SIG_OUT0 126
```

LEDC 低速 信号 输出 0（LEDC low-speed signal output 0）。

<a id="a5cad9206cfeea93b42e5456228c7d580"></a>

### `ESP_LEDC_LS_SIG_OUT1`

```c
#define ESP_LEDC_LS_SIG_OUT1 127
```

LEDC 低速 信号 输出 1（LEDC low-speed signal output 1）。

<a id="ab408070e7c700805db165c3876b6c588"></a>

### `ESP_LEDC_LS_SIG_OUT2`

```c
#define ESP_LEDC_LS_SIG_OUT2 128
```

LEDC 低速 信号 输出 2（LEDC low-speed signal output 2）。

<a id="a438aee217c6c94a2962a3d98935b5717"></a>

### `ESP_LEDC_LS_SIG_OUT3`

```c
#define ESP_LEDC_LS_SIG_OUT3 129
```

LEDC 低速 信号 输出 3（LEDC low-speed signal output 3）。

<a id="ada93dcffffc15362be4b7432a8033559"></a>

### `ESP_LEDC_LS_SIG_OUT4`

```c
#define ESP_LEDC_LS_SIG_OUT4 130
```

LEDC 低速 信号 输出 4（LEDC low-speed signal output 4）。

<a id="a34fc029ec45756ca7064580f57db1cc7"></a>

### `ESP_LEDC_LS_SIG_OUT5`

```c
#define ESP_LEDC_LS_SIG_OUT5 131
```

LEDC 低速 信号 输出 5（LEDC low-speed signal output 5）。

<a id="a28b01adea7e0bcc8b76fe05d58c1cbd0"></a>

### `ESP_LEDC_LS_SIG_OUT6`

```c
#define ESP_LEDC_LS_SIG_OUT6 132
```

LEDC 低速 信号 输出 6（LEDC low-speed signal output 6）。

<a id="a2ea140f2da1a15b24dcaa3592909ca35"></a>

### `ESP_LEDC_LS_SIG_OUT7`

```c
#define ESP_LEDC_LS_SIG_OUT7 133
```

LEDC 低速 信号 输出 7（LEDC low-speed signal output 7）。

<a id="af80260535bc3aee44c28c972a29483e0"></a>

### `ESP_NOSIG`

```c
#define ESP_NOSIG ESP_SIG_INVAL
```

无信号（No Signal），无效值。

<a id="a5825bd51c50ff93c17d519bca9a80c24"></a>

### `ESP_PCNT_CTRL_CH0_IN0 [1/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN0 149
```

PCNT 单元 0 通道 0 控制 输入（PCNT unit 0 channel 0 control input）。

<a id="a7e3c939b0b32332a35f0bead0aa4a2a6"></a>

### `ESP_PCNT_CTRL_CH0_IN0 [2/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN0 149
```

PCNT 单元 0 通道 0 控制 输入（PCNT unit 0 channel 0 control input）。

<a id="a778aad550aadb3624623678e8f21d9a8"></a>

### `ESP_PCNT_CTRL_CH0_IN1 [1/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN1 150
```

PCNT 单元 1 通道 0 控制 输入（PCNT unit 1 channel 0 control input）。

<a id="a9ec8d490316b9f043fe5e9160a7cf7e0"></a>

### `ESP_PCNT_CTRL_CH0_IN1 [2/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN1 150
```

PCNT 单元 1 通道 0 控制 输入（PCNT unit 1 channel 0 control input）。

<a id="abbe49a9151f6e729321b0354214772ea"></a>

### `ESP_PCNT_CTRL_CH0_IN2 [1/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN2 151
```

PCNT 单元 2 通道 0 控制 输入（PCNT unit 2 channel 0 control input）。

<a id="a540cbfcd205911955effcc9814f9707c"></a>

### `ESP_PCNT_CTRL_CH0_IN2 [2/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN2 151
```

PCNT 单元 2 通道 0 控制 输入（PCNT unit 2 channel 0 control input）。

<a id="af79dbaee0b062b9c200e744047d95c15"></a>

### `ESP_PCNT_CTRL_CH0_IN3 [1/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN3 152
```

PCNT 单元 3 通道 0 控制 输入（PCNT unit 3 channel 0 control input）。

<a id="a96e8bd4584ab671a1b0c3f0adb440943"></a>

### `ESP_PCNT_CTRL_CH0_IN3 [2/2]`

```c
#define ESP_PCNT_CTRL_CH0_IN3 152
```

PCNT 单元 3 通道 0 控制 输入（PCNT unit 3 channel 0 control input）。

<a id="a3c0ec3d7841577a05f1615116321edb4"></a>

### `ESP_PCNT_CTRL_CH1_IN0 [1/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN0 153
```

PCNT 单元 0 通道 1 控制 输入（PCNT unit 0 channel 1 control input）。

<a id="a88c5eb5c7f4169ce3e7f7056b42989a7"></a>

### `ESP_PCNT_CTRL_CH1_IN0 [2/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN0 153
```

PCNT 单元 0 通道 1 控制 输入（PCNT unit 0 channel 1 control input）。

<a id="ae965d09b63d5210163f5b96e975ea8ef"></a>

### `ESP_PCNT_CTRL_CH1_IN1 [1/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN1 154
```

PCNT 单元 1 通道 1 控制 输入（PCNT unit 1 channel 1 control input）。

<a id="a0bbfffdef085eb6cedc3d1232766cb38"></a>

### `ESP_PCNT_CTRL_CH1_IN1 [2/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN1 154
```

PCNT 单元 1 通道 1 控制 输入（PCNT unit 1 channel 1 control input）。

<a id="ab72266d11f5fc7d04c2e87494cfd80cf"></a>

### `ESP_PCNT_CTRL_CH1_IN2 [1/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN2 155
```

PCNT 单元 2 通道 1 控制 输入（PCNT unit 2 channel 1 control input）。

<a id="abf6c210e19582b06e3d6c546a009ef5b"></a>

### `ESP_PCNT_CTRL_CH1_IN2 [2/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN2 155
```

PCNT 单元 2 通道 1 控制 输入（PCNT unit 2 channel 1 control input）。

<a id="aa28ef045c9adfd7e9dc6bd538f49d969"></a>

### `ESP_PCNT_CTRL_CH1_IN3 [1/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN3 156
```

PCNT 单元 3 通道 1 控制 输入（PCNT unit 3 channel 1 control input）。

<a id="a0a926d350fc11d737b545c53b3ba1671"></a>

### `ESP_PCNT_CTRL_CH1_IN3 [2/2]`

```c
#define ESP_PCNT_CTRL_CH1_IN3 156
```

PCNT 单元 3 通道 1 控制 输入（PCNT unit 3 channel 1 control input）。

<a id="a9f11418b93b11426081ad8fcef9332d3"></a>

### `ESP_PCNT_SIG_CH0_IN0 [1/2]`

```c
#define ESP_PCNT_SIG_CH0_IN0 141
```

PCNT 单元 0 通道 0 信号 输入（PCNT unit 0 channel 0 signal input）。

PCNT 单元 0 通道 0 脉冲 输入（PCNT unit 0 channel 0 pulse input）。

<a id="acf123456a5b9d94f370309ad39672e34"></a>

### `ESP_PCNT_SIG_CH0_IN0 [2/2]`

```c
#define ESP_PCNT_SIG_CH0_IN0 141
```

PCNT 单元 0 通道 0 信号 输入（PCNT unit 0 channel 0 signal input）。

PCNT 单元 0 通道 0 脉冲 输入（PCNT unit 0 channel 0 pulse input）。

<a id="adb1cce7faf274879f3af380f56e5741c"></a>

### `ESP_PCNT_SIG_CH0_IN1 [1/2]`

```c
#define ESP_PCNT_SIG_CH0_IN1 142
```

PCNT 单元 1 通道 0 信号 输入（PCNT unit 1 channel 0 signal input）。

PCNT 单元 1 通道 0 脉冲 输入（PCNT unit 1 channel 0 pulse input）。

<a id="a99db3d1c4e07e11fc09a4024a54fcea6"></a>

### `ESP_PCNT_SIG_CH0_IN1 [2/2]`

```c
#define ESP_PCNT_SIG_CH0_IN1 142
```

PCNT 单元 1 通道 0 信号 输入（PCNT unit 1 channel 0 signal input）。

PCNT 单元 1 通道 0 脉冲 输入（PCNT unit 1 channel 0 pulse input）。

<a id="adc95b489bf9613b40c1602d89d5e92ef"></a>

### `ESP_PCNT_SIG_CH0_IN2 [1/2]`

```c
#define ESP_PCNT_SIG_CH0_IN2 143
```

PCNT 单元 2 通道 0 信号 输入（PCNT unit 2 channel 0 signal input）。

PCNT 单元 2 通道 0 脉冲 输入（PCNT unit 2 channel 0 pulse input）。

<a id="a4f9e798a260fb6ac4c39262f20253244"></a>

### `ESP_PCNT_SIG_CH0_IN2 [2/2]`

```c
#define ESP_PCNT_SIG_CH0_IN2 143
```

PCNT 单元 2 通道 0 信号 输入（PCNT unit 2 channel 0 signal input）。

PCNT 单元 2 通道 0 脉冲 输入（PCNT unit 2 channel 0 pulse input）。

<a id="a2722e320806e8013009e50fb0a4b4782"></a>

### `ESP_PCNT_SIG_CH0_IN3 [1/2]`

```c
#define ESP_PCNT_SIG_CH0_IN3 144
```

PCNT 单元 3 通道 0 信号 输入（PCNT unit 3 channel 0 signal input）。

PCNT 单元 3 通道 0 脉冲 输入（PCNT unit 3 channel 0 pulse input）。

<a id="acd8d20d89508b532a4e2749499263de3"></a>

### `ESP_PCNT_SIG_CH0_IN3 [2/2]`

```c
#define ESP_PCNT_SIG_CH0_IN3 144
```

PCNT 单元 3 通道 0 信号 输入（PCNT unit 3 channel 0 signal input）。

PCNT 单元 3 通道 0 脉冲 输入（PCNT unit 3 channel 0 pulse input）。

<a id="ad5d93140fc2134619b9e4274ded924d8"></a>

### `ESP_PCNT_SIG_CH1_IN0 [1/2]`

```c
#define ESP_PCNT_SIG_CH1_IN0 145
```

PCNT 单元 0 通道 1 信号 输入（PCNT unit 0 channel 1 signal input）。

PCNT 单元 0 通道 1 脉冲 输入（PCNT unit 0 channel 1 pulse input）。

<a id="a800813b2c23f7e4bb23e032e0802a459"></a>

### `ESP_PCNT_SIG_CH1_IN0 [2/2]`

```c
#define ESP_PCNT_SIG_CH1_IN0 145
```

PCNT 单元 0 通道 1 信号 输入（PCNT unit 0 channel 1 signal input）。

PCNT 单元 0 通道 1 脉冲 输入（PCNT unit 0 channel 1 pulse input）。

<a id="aa75acbb9c392b686e44eeaa9898abd32"></a>

### `ESP_PCNT_SIG_CH1_IN1 [1/2]`

```c
#define ESP_PCNT_SIG_CH1_IN1 146
```

PCNT 单元 1 通道 1 信号 输入（PCNT unit 1 channel 1 signal input）。

PCNT 单元 1 通道 1 脉冲 输入（PCNT unit 1 channel 1 pulse input）。

<a id="a730113779d69ca86b257060678f8cbec"></a>

### `ESP_PCNT_SIG_CH1_IN1 [2/2]`

```c
#define ESP_PCNT_SIG_CH1_IN1 146
```

PCNT 单元 1 通道 1 信号 输入（PCNT unit 1 channel 1 signal input）。

PCNT 单元 1 通道 1 脉冲 输入（PCNT unit 1 channel 1 pulse input）。

<a id="add3d775b32fda9000309b5082df4ac12"></a>

### `ESP_PCNT_SIG_CH1_IN2 [1/2]`

```c
#define ESP_PCNT_SIG_CH1_IN2 147
```

PCNT 单元 2 通道 1 信号 输入（PCNT unit 2 channel 1 signal input）。

PCNT 单元 2 通道 1 脉冲 输入（PCNT unit 2 channel 1 pulse input）。

<a id="a38365b3f9a2b49ef2714c38d00d293c5"></a>

### `ESP_PCNT_SIG_CH1_IN2 [2/2]`

```c
#define ESP_PCNT_SIG_CH1_IN2 147
```

PCNT 单元 2 通道 1 信号 输入（PCNT unit 2 channel 1 signal input）。

PCNT 单元 2 通道 1 脉冲 输入（PCNT unit 2 channel 1 pulse input）。

<a id="a0aa25f1f2355e5fa8ccc6afa4d16abcb"></a>

### `ESP_PCNT_SIG_CH1_IN3 [1/2]`

```c
#define ESP_PCNT_SIG_CH1_IN3 148
```

PCNT 单元 3 通道 1 信号 输入（PCNT unit 3 channel 1 signal input）。

PCNT 单元 3 通道 1 脉冲 输入（PCNT unit 3 channel 1 pulse input）。

<a id="ac54a606ee7096db15cdb9453b04ac72d"></a>

### `ESP_PCNT_SIG_CH1_IN3 [2/2]`

```c
#define ESP_PCNT_SIG_CH1_IN3 148
```

PCNT 单元 3 通道 1 信号 输入（PCNT unit 3 channel 1 signal input）。

PCNT 单元 3 通道 1 脉冲 输入（PCNT unit 3 channel 1 pulse input）。

<a id="a421b59e20586b4f48b7e81bfa0ad4357"></a>

### `ESP_PWM0_CAP0_IN`

```c
#define ESP_PWM0_CAP0_IN 95
```

MCPWM0 捕获 0 输入（MCPWM0 capture 0 input）。

<a id="aea7a8712f1502df47721258470ff5b48"></a>

### `ESP_PWM0_CAP1_IN`

```c
#define ESP_PWM0_CAP1_IN 96
```

MCPWM0 捕获 1 输入（MCPWM0 capture 1 input）。

<a id="ab221240161be67a0f5af577494c8a5ad"></a>

### `ESP_PWM0_CAP2_IN`

```c
#define ESP_PWM0_CAP2_IN 97
```

MCPWM0 捕获 2 输入（MCPWM0 capture 2 input）。

<a id="a16dce8622301cb7c2e1c9a9e7a069012"></a>

### `ESP_PWM0_CH0_A_OUT`

```c
#define ESP_PWM0_CH0_A_OUT 89
```

MCPWM0 输出 0A（MCPWM0 output 0A）。

<a id="abf292303b956ab1dab348fcbf7d59323"></a>

### `ESP_PWM0_CH0_B_OUT`

```c
#define ESP_PWM0_CH0_B_OUT 90
```

MCPWM0 输出 0B（MCPWM0 output 0B）。

<a id="a6ab5a2408b8c64ce277b146bbdd83e79"></a>

### `ESP_PWM0_CH1_A_OUT`

```c
#define ESP_PWM0_CH1_A_OUT 91
```

MCPWM0 输出 1A（MCPWM0 output 1A）。

<a id="a328a767873a19e04be758e71b3847177"></a>

### `ESP_PWM0_CH1_B_OUT`

```c
#define ESP_PWM0_CH1_B_OUT 92
```

MCPWM0 输出 1B（MCPWM0 output 1B）。

<a id="a7c498b1682e354f660e84b3781373d70"></a>

### `ESP_PWM0_CH2_A_OUT`

```c
#define ESP_PWM0_CH2_A_OUT 93
```

MCPWM0 输出 2A（MCPWM0 output 2A）。

<a id="aee1fcd021983675cd645054eef2fe3a3"></a>

### `ESP_PWM0_CH2_B_OUT`

```c
#define ESP_PWM0_CH2_B_OUT 94
```

MCPWM0 输出 2B（MCPWM0 output 2B）。

<a id="a4a503a957b2fd76f257534b80069caa2"></a>

### `ESP_PWM0_F0_IN`

```c
#define ESP_PWM0_F0_IN 92
```

MCPWM0 故障 0 输入（MCPWM0 fault 0 input）。

<a id="af536ae867a3d8bcb7644b48c346b4b50"></a>

### `ESP_PWM0_F1_IN`

```c
#define ESP_PWM0_F1_IN 93
```

MCPWM0 故障 1 输入（MCPWM0 fault 1 input）。

<a id="a83f385e6b8a99314cc641083a203322b"></a>

### `ESP_PWM0_F2_IN`

```c
#define ESP_PWM0_F2_IN 94
```

MCPWM0 故障 2 输入（MCPWM0 fault 2 input）。

<a id="a9397a79a46feab488c88552013790dfc"></a>

### `ESP_PWM0_OUT0A`

```c
#define ESP_PWM0_OUT0A 89
```

MCPWM0 输出 0A（MCPWM0 output 0A）。

<a id="acb3badfaed73f7069ea23dde375db62a"></a>

### `ESP_PWM0_OUT0B`

```c
#define ESP_PWM0_OUT0B 90
```

MCPWM0 输出 0B（MCPWM0 output 0B）。

<a id="ae52e5bd4be5563caeb9861267e41d947"></a>

### `ESP_PWM0_OUT1A`

```c
#define ESP_PWM0_OUT1A 91
```

MCPWM0 输出 1A（MCPWM0 output 1A）。

<a id="a9fa8e944ff2d960c141f8375c9aa0b0e"></a>

### `ESP_PWM0_OUT1B`

```c
#define ESP_PWM0_OUT1B 92
```

MCPWM0 输出 1B（MCPWM0 output 1B）。

<a id="abf74a2a32a8c36431e2f21d6cd15a610"></a>

### `ESP_PWM0_OUT2A`

```c
#define ESP_PWM0_OUT2A 93
```

MCPWM0 输出 2A（MCPWM0 output 2A）。

<a id="a563105deedf9f7ed6818ab9a8a8aecdc"></a>

### `ESP_PWM0_OUT2B`

```c
#define ESP_PWM0_OUT2B 94
```

MCPWM0 输出 2B（MCPWM0 output 2B）。

<a id="a60a3fe70a1bc5ba71cb46df782901087"></a>

### `ESP_PWM0_SYNC0_IN`

```c
#define ESP_PWM0_SYNC0_IN 89
```

MCPWM0 同步 0 输入（MCPWM0 sync 0 input）。

<a id="aca616afbb64ed37982624503545a5a72"></a>

### `ESP_PWM0_SYNC1_IN`

```c
#define ESP_PWM0_SYNC1_IN 90
```

MCPWM0 同步 1 输入（MCPWM0 sync 1 input）。

<a id="a2017681d630abc75e7298c12b86a62ce"></a>

### `ESP_PWM0_SYNC2_IN`

```c
#define ESP_PWM0_SYNC2_IN 91
```

MCPWM0 同步 2 输入（MCPWM0 sync 2 input）。

<a id="a8f2dcd1f46c2a5a5da3be188dca9e3a0"></a>

### `ESP_PWM1_CAP0_IN`

```c
#define ESP_PWM1_CAP0_IN 104
```

MCPWM1 捕获 0 输入（MCPWM1 capture 0 input）。

<a id="a8b97c639d66dcb8400aefc344bf490d1"></a>

### `ESP_PWM1_CAP1_IN`

```c
#define ESP_PWM1_CAP1_IN 105
```

MCPWM1 捕获 1 输入（MCPWM1 capture 1 input）。

<a id="a23b8540974bcf9dbd5c0ff92d9b69ac9"></a>

### `ESP_PWM1_CAP2_IN`

```c
#define ESP_PWM1_CAP2_IN 106
```

MCPWM1 捕获 2 输入（MCPWM1 capture 2 input）。

<a id="a470396d0e3e83aaab3f7546ae9dfeafb"></a>

### `ESP_PWM1_CH0_A_OUT`

```c
#define ESP_PWM1_CH0_A_OUT 95
```

MCPWM1 输出 0A（MCPWM1 output 0A）。

<a id="af6732227f529b02a52c7174d9cadb9cc"></a>

### `ESP_PWM1_CH0_B_OUT`

```c
#define ESP_PWM1_CH0_B_OUT 96
```

MCPWM1 输出 0B（MCPWM1 output 0B）。

<a id="aad4b629241e84ab2718fb5d10250f710"></a>

### `ESP_PWM1_CH1_A_OUT`

```c
#define ESP_PWM1_CH1_A_OUT 97
```

MCPWM1 输出 1A（MCPWM1 output 1A）。

<a id="ac95c1743c3e3af80475bd7827d619690"></a>

### `ESP_PWM1_CH1_B_OUT`

```c
#define ESP_PWM1_CH1_B_OUT 98
```

MCPWM1 输出 1B（MCPWM1 output 1B）。

<a id="a15121252274b653dfeef2d9a16f2c5e3"></a>

### `ESP_PWM1_CH2_A_OUT`

```c
#define ESP_PWM1_CH2_A_OUT 99
```

MCPWM1 输出 2A（MCPWM1 output 2A）。

<a id="a2c9296238ae64c0e744cffb8756d4bc1"></a>

### `ESP_PWM1_CH2_B_OUT`

```c
#define ESP_PWM1_CH2_B_OUT 100
```

MCPWM1 输出 2B（MCPWM1 output 2B）。

<a id="a09c262c332e65ccc9eb2d91d976958e3"></a>

### `ESP_PWM1_F0_IN`

```c
#define ESP_PWM1_F0_IN 101
```

MCPWM1 故障 0 输入（MCPWM1 fault 0 input）。

<a id="af4b1c0ff4e222f09eee18cbb85cedb67"></a>

### `ESP_PWM1_F1_IN`

```c
#define ESP_PWM1_F1_IN 102
```

MCPWM1 故障 1 输入（MCPWM1 fault 1 input）。

<a id="ac911f11a68e10d359cffe49864739e2d"></a>

### `ESP_PWM1_F2_IN`

```c
#define ESP_PWM1_F2_IN 103
```

MCPWM1 故障 2 输入（MCPWM1 fault 2 input）。

<a id="a9f251384f8a6a10b0fb173c4bfda88ba"></a>

### `ESP_PWM1_SYNC0_IN`

```c
#define ESP_PWM1_SYNC0_IN 98
```

MCPWM1 同步 0 输入（MCPWM1 sync 0 input）。

<a id="a646d7d644b5d4ec403eab7ff793cf7b2"></a>

### `ESP_PWM1_SYNC1_IN`

```c
#define ESP_PWM1_SYNC1_IN 99
```

MCPWM1 同步 1 输入（MCPWM1 sync 1 input）。

<a id="a56a67f8e168a4e7545e3ca4bcf7c8d89"></a>

### `ESP_PWM1_SYNC2_IN`

```c
#define ESP_PWM1_SYNC2_IN 100
```

MCPWM1 同步 2 输入（MCPWM1 sync 2 input）。

<a id="ad9bae9b4884a356e465656d1ee8d61cd"></a>

### `ESP_RMT_SIG_IN0`

```c
#define ESP_RMT_SIG_IN0 246
```

RMT 通道 0 输入（RMT channel 0 input）。

<a id="ab6c6293e6845ba4bf4d05b84102ffdcf"></a>

### `ESP_RMT_SIG_IN1`

```c
#define ESP_RMT_SIG_IN1 247
```

RMT 通道 1 输入（RMT channel 1 input）。

<a id="af88ebdd0d2d02ac58d720c001ccc155b"></a>

### `ESP_RMT_SIG_IN2`

```c
#define ESP_RMT_SIG_IN2 248
```

RMT 通道 2 输入（RMT channel 2 input）。

<a id="a1f930cd82690248b839f16ff7738f32c"></a>

### `ESP_RMT_SIG_IN3`

```c
#define ESP_RMT_SIG_IN3 249
```

RMT 通道 3 输入（RMT channel 3 input）。

<a id="a25343fbc20a0c542bcdc21cdfade867b"></a>

### `ESP_RMT_SIG_OUT0`

```c
#define ESP_RMT_SIG_OUT0 246
```

RMT 通道 0 输出（RMT channel 0 output）。

<a id="a6d082fb1c7397d784a3075108e0dea73"></a>

### `ESP_RMT_SIG_OUT1`

```c
#define ESP_RMT_SIG_OUT1 247
```

RMT 通道 1 输出（RMT channel 1 output）。

<a id="ad657c1ddcf9c335ac7876464b80b2705"></a>

### `ESP_RMT_SIG_OUT2`

```c
#define ESP_RMT_SIG_OUT2 248
```

RMT 通道 2 输出（RMT channel 2 output）。

<a id="ae60033bb70ca9ff7c2b52368d24a8ab8"></a>

### `ESP_RMT_SIG_OUT3`

```c
#define ESP_RMT_SIG_OUT3 249
```

RMT 通道 3 输出（RMT channel 3 output）。

<a id="a714ad872feff48bc481b3791b28ec50d"></a>

### `ESP_SPI3_CK_IN`

```c
#define ESP_SPI3_CK_IN 47
```

SPI3 时钟 输入（SPI3 clock input）。

<a id="ae5f28c7478dc01fadb9005f16c0100e7"></a>

### `ESP_SPI3_CK_OUT`

```c
#define ESP_SPI3_CK_OUT 47
```

SPI3 时钟 输出（SPI3 clock output）。

<a id="a7f06d2db560a8cd511c9189cd6ed8980"></a>

### `ESP_SPI3_CS1_OUT`

```c
#define ESP_SPI3_CS1_OUT 46
```

SPI3 CS1 输出（SPI3 CS1 output）。

<a id="a9e4bf0b0eff43b1f56f17abe22ef24a5"></a>

### `ESP_SPI3_CS2_OUT`

```c
#define ESP_SPI3_CS2_OUT 45
```

SPI3 CS2 输出（SPI3 CS2 output）。

<a id="a7ef5baa3054ee04857f15f034407b0bf"></a>

### `ESP_SPI3_CS_IN`

```c
#define ESP_SPI3_CS_IN 52
```

SPI3 CS 输入（SPI3 CS input）。

<a id="a09ec480d3b31ac943b489ed6229c051a"></a>

### `ESP_SPI3_CS_OUT`

```c
#define ESP_SPI3_CS_OUT 52
```

SPI3 CS 输出（SPI3 CS output）。

<a id="ae7cf1730786ba95580b91b00066d3e25"></a>

### `ESP_SPI3_D_IN`

```c
#define ESP_SPI3_D_IN 49
```

SPI3 D 输入（SPI3 D input）。

<a id="aff4a1289beb94c9e23d7c1dd13d71d83"></a>

### `ESP_SPI3_D_OUT`

```c
#define ESP_SPI3_D_OUT 49
```

SPI3 D 输出（SPI3 D output）。

<a id="ab40bfa33ef13681c81e70a4cd19e2253"></a>

### `ESP_SPI3_HOLD_IN`

```c
#define ESP_SPI3_HOLD_IN 50
```

SPI3 HOLD 输入（SPI3 HOLD input）。

<a id="a603ce746c6b8d4dcea716bd2249e19b8"></a>

### `ESP_SPI3_HOLD_OUT`

```c
#define ESP_SPI3_HOLD_OUT 50
```

SPI3 HOLD 输出（SPI3 HOLD output）。

<a id="a05a9a2e5983b7895ca1fb05e5cd34709"></a>

### `ESP_SPI3_Q_IN`

```c
#define ESP_SPI3_Q_IN 48
```

SPI3 Q 输入（SPI3 Q input）。

<a id="a886c0db586c39f6c40f6987ad624275e"></a>

### `ESP_SPI3_QO_OUT`

```c
#define ESP_SPI3_QO_OUT 48
```

SPI3 Q 输出（SPI3 Q output）。

<a id="ae5ef053fe616dfb189a1a5bf28313647"></a>

### `ESP_SPI3_WP_IN`

```c
#define ESP_SPI3_WP_IN 51
```

SPI3 WP 输入（SPI3 WP input）。

<a id="ab3c345085fafd95b7bd2f83d14a5317c"></a>

### `ESP_SPI3_WP_OUT`

```c
#define ESP_SPI3_WP_OUT 51
```

SPI3 WP 输出（SPI3 WP output）。

<a id="a5d9314d65cffc6a2af35b6d95e96d4a7"></a>

### `ESP_TWAI0_RX`

```c
#define ESP_TWAI0_RX 80
```

TWAI0 RX 输入（TWAI0 RX input）。

<a id="a861efcd37d8828dceffb156de3f1cced"></a>

### `ESP_TWAI0_TX`

```c
#define ESP_TWAI0_TX 80
```

TWAI0 TX 输出（TWAI0 TX output）。

<a id="acb7f23161b4577b7897c3ddf6fc8c9ac"></a>

### `ESP_TWAI1_RX`

```c
#define ESP_TWAI1_RX 83
```

TWAI1 RX 输入（TWAI1 RX input）。

<a id="ae74556abcddfc37a6e98093cd485085e"></a>

### `ESP_TWAI1_TX`

```c
#define ESP_TWAI1_TX 83
```

TWAI1 TX 输出（TWAI1 TX output）。

<a id="ad76afcc4d4a87afb215e50e5edc31181"></a>

### `ESP_TWAI2_RX`

```c
#define ESP_TWAI2_RX 86
```

TWAI2 RX 输入（TWAI2 RX input）。

<a id="affd3e8cc537484131e8801bcb11dc884"></a>

### `ESP_TWAI2_TX`

```c
#define ESP_TWAI2_TX 86
```

TWAI2 TX 输出（TWAI2 TX output）。

<a id="a530d7a918a97cd1fff1acf2f90edd4ca"></a>

### `ESP_U0CTS_IN`

```c
#define ESP_U0CTS_IN 11
```

UART0 CTS 输入（UART0 CTS input）。

<a id="a53e3a4557a4eb1f7f98250abef03c02a"></a>

### `ESP_U0DSR_IN`

```c
#define ESP_U0DSR_IN 12
```

UART0 DSR 输入（UART0 DSR input）。

<a id="acc8716af947169c9f167bdf215c5314c"></a>

### `ESP_U0DTR_OUT`

```c
#define ESP_U0DTR_OUT 12
```

UART0 DTR 输出（UART0 DTR output）。

<a id="a4257bbc044af6ea3612313e3a0b7e7c9"></a>

### `ESP_U0RTS_OUT`

```c
#define ESP_U0RTS_OUT 11
```

UART0 RTS 输出（UART0 RTS output）。

<a id="aca502efa55ce2286dc9eba28192681fd"></a>

### `ESP_U0RXD_IN`

```c
#define ESP_U0RXD_IN 10
```

UART0 RXD 输入（UART0 RXD input）。

<a id="af1e58fb8e7ef86a92171eca7bb1671af"></a>

### `ESP_U0TXD_OUT`

```c
#define ESP_U0TXD_OUT 10
```

UART0 TXD 输出（UART0 TXD output）。

<a id="a3c005e616da21a058960d6aed79427b3"></a>

### `ESP_U1CTS_IN`

```c
#define ESP_U1CTS_IN 14
```

UART1 CTS 输入（UART1 CTS input）。

<a id="a5f29b138691540598d0b977dc4bd5971"></a>

### `ESP_U1DSR_IN`

```c
#define ESP_U1DSR_IN 15
```

UART1 DSR 输入（UART1 DSR input）。

<a id="a1f7df042d40ec6f20b559ef6778d7497"></a>

### `ESP_U1DTR_OUT`

```c
#define ESP_U1DTR_OUT 15
```

UART1 DTR 输出（UART1 DTR output）。

<a id="a8f6399745566bd5caa2020e4dcb2bb3b"></a>

### `ESP_U1RTS_OUT`

```c
#define ESP_U1RTS_OUT 14
```

UART1 RTS 输出（UART1 RTS output）。

<a id="a2293e0646e0ad2f76d62f76425ae6770"></a>

### `ESP_U1RXD_IN`

```c
#define ESP_U1RXD_IN 13
```

UART1 RXD 输入（UART1 RXD input）。

<a id="a6053b38147e28e3a7479b38e7d195136"></a>

### `ESP_U1TXD_OUT`

```c
#define ESP_U1TXD_OUT 13
```

UART1 TXD 输出（UART1 TXD output）。

<a id="a735a482aa723130ccb408f0fb7596a0a"></a>

### `ESP_U2CTS_IN`

```c
#define ESP_U2CTS_IN 17
```

UART2 CTS 输入（UART2 CTS input）。

<a id="a70d4f834bfd182c138257e36a4b04096"></a>

### `ESP_U2DSR_IN`

```c
#define ESP_U2DSR_IN 18
```

UART2 DSR 输入（UART2 DSR input）。

<a id="a783f6ee9ad46dfd9e34d1473b1e2ad9b"></a>

### `ESP_U2DTR_OUT`

```c
#define ESP_U2DTR_OUT 18
```

UART2 DTR 输出（UART2 DTR output）。

<a id="a174b50e35d961ded056cea3848110b20"></a>

### `ESP_U2RTS_OUT`

```c
#define ESP_U2RTS_OUT 17
```

UART2 RTS 输出（UART2 RTS output）。

<a id="abe46ead057c2b66d500ef07e8a84fe0f"></a>

### `ESP_U2RXD_IN`

```c
#define ESP_U2RXD_IN 16
```

UART2 RXD 输入（UART2 RXD input）。

<a id="a20baac10eb4b76603580e1ea7065213a"></a>

### `ESP_U2TXD_OUT`

```c
#define ESP_U2TXD_OUT 16
```

UART2 TXD 输出（UART2 TXD output）。

<a id="a0e350c02f93ace85a2dd891597d89d8c"></a>

### `ESP_U3CTS_IN`

```c
#define ESP_U3CTS_IN 20
```

UART3 CTS 输入（UART3 CTS input）。

<a id="a62a19eb3ff17c8dbe3701c3be7fd844d"></a>

### `ESP_U3DSR_IN`

```c
#define ESP_U3DSR_IN 21
```

UART3 DSR 输入（UART3 DSR input）。

<a id="a41780dd757f8fd9f0b44c89c02e4aff3"></a>

### `ESP_U3DTR_OUT`

```c
#define ESP_U3DTR_OUT 21
```

UART3 DTR 输出（UART3 DTR output）。

<a id="a466185d49c68709507afce20d25aca3a"></a>

### `ESP_U3RTS_OUT`

```c
#define ESP_U3RTS_OUT 20
```

UART3 RTS 输出（UART3 RTS output）。

<a id="a5b939f8c6f862b51249463b7b1e2b4fc"></a>

### `ESP_U3RXD_IN`

```c
#define ESP_U3RXD_IN 19
```

UART3 RXD 输入（UART3 RXD input）。

<a id="aa038f32908e5e30faaef5438203a9270"></a>

### `ESP_U3TXD_OUT`

```c
#define ESP_U3TXD_OUT 19
```

UART3 TXD 输出（UART3 TXD output）。

<a id="a933519638d1c5cd78138da16d447008d"></a>

### `ESP_U4CTS_IN`

```c
#define ESP_U4CTS_IN 23
```

UART4 CTS 输入（UART4 CTS input）。

<a id="ae533de687bb88939f97c73ae85eecfd5"></a>

### `ESP_U4DSR_IN`

```c
#define ESP_U4DSR_IN 24
```

UART4 DSR 输入（UART4 DSR input）。

<a id="ae7508454f2ba682485978aa9d86637c0"></a>

### `ESP_U4DTR_OUT`

```c
#define ESP_U4DTR_OUT 24
```

UART4 DTR 输出（UART4 DTR output）。

<a id="a68ccd15805cfb52a466af2a24520a4c3"></a>

### `ESP_U4RTS_OUT`

```c
#define ESP_U4RTS_OUT 23
```

UART4 RTS 输出（UART4 RTS output）。

<a id="a2e52bdb5a3cb16125b95f0ecd71e6012"></a>

### `ESP_U4RXD_IN`

```c
#define ESP_U4RXD_IN 22
```

UART4 RXD 输入（UART4 RXD input）。

<a id="a9dbb0d137993ef1f48a1ba7d1b6a31b2"></a>

### `ESP_U4TXD_OUT`

```c
#define ESP_U4TXD_OUT 22
```

UART4 TXD 输出（UART4 TXD output）。


## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_pcie_hid_reference/P004_esp32p4-gpio-sigmap.h_源码浏览.md)
- [ESP_SIG_INVAL](../api_file_clock_network_reference/P007_zephyr__dt-bindings__pinctrl__esp-pinctrl-common.h_文件参考.md#ae0d2e726ab8d90343e5c80e1d9b85ad8)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__dt-bindings__pinctrl__amebag2-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__gpio__st-morpho-header.h_文件参考.md)
