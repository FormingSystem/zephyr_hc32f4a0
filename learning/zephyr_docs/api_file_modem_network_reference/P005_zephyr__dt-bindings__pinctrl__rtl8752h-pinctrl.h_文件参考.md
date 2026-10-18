---
id: learning.zephyr-docs.api-file-modem-network-reference.page-5
title: zephyr__dt-bindings__pinctrl__rtl8752h-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_rtl8752h-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtl8752h-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RTL8752H引脚控制（Pin Control / Pinmux）的头文件。

<a id="details"></a>

```c
#include "bee-pinctrl.h"
```

查看此文件的源码。

RTL8752H 引脚控制（Pin Control／Pinmux）头文件。本文件定义 Realtek RTL8752H 片上系统（SoC）系列的引脚复用功能（Pinmux Functions）和引脚分配（Pin Assignments）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 引脚控制复用功能（Pinctrl Pinmux Functions）

<a id="r_aa96a1b1f865f33896d26cb0ebc67a654"></a>

```c
#define BEE_IDLE_MODE 0
```

相关声明：[BEE_IDLE_MODE](#aa96a1b1f865f33896d26cb0ebc67a654)。

`IDLE_MODE` 引脚复用功能（Pinmux Function）。

<a id="r_a64c1b3bb3de7cbf46f5e15da73dd6af9"></a>

```c
#define BEE_UART2_TX 1
```

相关声明：[BEE_UART2_TX](#a64c1b3bb3de7cbf46f5e15da73dd6af9)。

`UART2_TX` 引脚复用功能（Pinmux Function）。

<a id="r_ac0e9e9aae4c3a7542a4283525446151a"></a>

```c
#define BEE_UART2_RX 2
```

相关声明：[BEE_UART2_RX](#ac0e9e9aae4c3a7542a4283525446151a)。

`UART2_RX` 引脚复用功能（Pinmux Function）。

<a id="r_a7efdd2cc3bd5b3e9686ec52348490a21"></a>

```c
#define BEE_UART2_CTS 3
```

相关声明：[BEE_UART2_CTS](#a7efdd2cc3bd5b3e9686ec52348490a21)。

`UART2_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a9c3102f61a4ea7d46a3b5bb363d8089d"></a>

```c
#define BEE_UART2_RTS 4
```

相关声明：[BEE_UART2_RTS](#a9c3102f61a4ea7d46a3b5bb363d8089d)。

`UART2_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_ae0341d05951da84bd30617c9dc341628"></a>

```c
#define BEE_I2C0_CLK 5
```

相关声明：[BEE_I2C0_CLK](#ae0341d05951da84bd30617c9dc341628)。

`I2C0_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_abf8d90380239e366fb63fd777fb25075"></a>

```c
#define BEE_I2C0_DAT 6
```

相关声明：[BEE_I2C0_DAT](#abf8d90380239e366fb63fd777fb25075)。

`I2C0_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_ad89dd6f55609883daef7915f779b193f"></a>

```c
#define BEE_I2C1_CLK 7
```

相关声明：[BEE_I2C1_CLK](#ad89dd6f55609883daef7915f779b193f)。

`I2C1_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_aa70f0eb0a8271e9e027a7307e9c2f203"></a>

```c
#define BEE_I2C1_DAT 8
```

相关声明：[BEE_I2C1_DAT](#aa70f0eb0a8271e9e027a7307e9c2f203)。

`I2C1_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_a51f8a3a8d4572a1a9ffbdb0c894c006d"></a>

```c
#define BEE_PWM2_P 9
```

相关声明：[BEE_PWM2_P](#a51f8a3a8d4572a1a9ffbdb0c894c006d)。

`PWM2_P` 引脚复用功能（Pinmux Function）。

<a id="r_a38e2245a7c8035941a8e298da1ef2671"></a>

```c
#define BEE_PWM2_N 10
```

相关声明：[BEE_PWM2_N](#a38e2245a7c8035941a8e298da1ef2671)。

`PWM2_N` 引脚复用功能（Pinmux Function）。

<a id="r_a317e02b0cb9050e461acf3c246be9af4"></a>

```c
#define BEE_ENPWM0_P 11
```

相关声明：[BEE_ENPWM0_P](#a317e02b0cb9050e461acf3c246be9af4)。

`ENPWM0_P` 引脚复用功能（Pinmux Function）。

<a id="r_a70f463ef325204a7874ade112c0993b3"></a>

```c
#define BEE_ENPWM0_N 12
```

相关声明：[BEE_ENPWM0_N](#a70f463ef325204a7874ade112c0993b3)。

`ENPWM0_N` 引脚复用功能（Pinmux Function）。

<a id="r_a07f2b36faf2fecad0359070176339d0e"></a>

```c
#define BEE_TIM_PWM0 13
```

相关声明：[BEE_TIM_PWM0](#a07f2b36faf2fecad0359070176339d0e)。

`TIM_PWM0` 引脚复用功能（Pinmux Function）。

<a id="r_a5dd920c196c65cb5b8ee475e7e5264ca"></a>

```c
#define BEE_TIM_PWM1 14
```

相关声明：[BEE_TIM_PWM1](#a5dd920c196c65cb5b8ee475e7e5264ca)。

`TIM_PWM1` 引脚复用功能（Pinmux Function）。

<a id="r_a3143f7811c5878701ee6da954a2ed74e"></a>

```c
#define BEE_TIM_PWM2 15
```

相关声明：[BEE_TIM_PWM2](#a3143f7811c5878701ee6da954a2ed74e)。

`TIM_PWM2` 引脚复用功能（Pinmux Function）。

<a id="r_abecec561a57f431e83e15a32109b4265"></a>

```c
#define BEE_TIM_PWM3 16
```

相关声明：[BEE_TIM_PWM3](#abecec561a57f431e83e15a32109b4265)。

`TIM_PWM3` 引脚复用功能（Pinmux Function）。

<a id="r_ae8285702c1dc959039d162525cf06f76"></a>

```c
#define BEE_TIM_PWM4 17
```

相关声明：[BEE_TIM_PWM4](#ae8285702c1dc959039d162525cf06f76)。

`TIM_PWM4` 引脚复用功能（Pinmux Function）。

<a id="r_a185ffa8da5dfc0f6dcb68953ea60a117"></a>

```c
#define BEE_TIM_PWM5 18
```

相关声明：[BEE_TIM_PWM5](#a185ffa8da5dfc0f6dcb68953ea60a117)。

`TIM_PWM5` 引脚复用功能（Pinmux Function）。

<a id="r_a6ff1811284f84284f5dac6c4daaf8cb8"></a>

```c
#define BEE_ENPWM0 19
```

相关声明：[BEE_ENPWM0](#a6ff1811284f84284f5dac6c4daaf8cb8)。

`ENPWM0` 引脚复用功能（Pinmux Function）。

<a id="r_aee030c5731a3c6ee0f2c52de0a8e9d3b"></a>

```c
#define BEE_ENPWM1 20
```

相关声明：[BEE_ENPWM1](#aee030c5731a3c6ee0f2c52de0a8e9d3b)。

`ENPWM1` 引脚复用功能（Pinmux Function）。

<a id="r_aa8636b879c8e395d7605eb5922fa0e86"></a>

```c
#define BEE_QDEC_PHASE_A_X 21
```

相关声明：[BEE_QDEC_PHASE_A_X](#aa8636b879c8e395d7605eb5922fa0e86)。

`QDEC_PHASE_A_X` 引脚复用功能（Pinmux Function）。

<a id="r_a53614012c9764fab3f1c471b0c118cf6"></a>

```c
#define BEE_QDEC_PHASE_B_X 22
```

相关声明：[BEE_QDEC_PHASE_B_X](#a53614012c9764fab3f1c471b0c118cf6)。

`QDEC_PHASE_B_X` 引脚复用功能（Pinmux Function）。

<a id="r_a63e4235f1eb0ca27ee6991facf896f3d"></a>

```c
#define BEE_QDEC_PHASE_A_Y 23
```

相关声明：[BEE_QDEC_PHASE_A_Y](#a63e4235f1eb0ca27ee6991facf896f3d)。

`QDEC_PHASE_A_Y` 引脚复用功能（Pinmux Function）。

<a id="r_a60f5251123c52966c512c8511cf79cea"></a>

```c
#define BEE_QDEC_PHASE_B_Y 24
```

相关声明：[BEE_QDEC_PHASE_B_Y](#a60f5251123c52966c512c8511cf79cea)。

`QDEC_PHASE_B_Y` 引脚复用功能（Pinmux Function）。

<a id="r_a3edc0295f035c1ae7f45f2098ab67fa6"></a>

```c
#define BEE_QDEC_PHASE_A_Z 25
```

相关声明：[BEE_QDEC_PHASE_A_Z](#a3edc0295f035c1ae7f45f2098ab67fa6)。

`QDEC_PHASE_A_Z` 引脚复用功能（Pinmux Function）。

<a id="r_a463a58ed07f3016a8ebc54601b3e55e7"></a>

```c
#define BEE_QDEC_PHASE_B_Z 26
```

相关声明：[BEE_QDEC_PHASE_B_Z](#a463a58ed07f3016a8ebc54601b3e55e7)。

`QDEC_PHASE_B_Z` 引脚复用功能（Pinmux Function）。

<a id="r_aba42501ee83715ca6ea53df22183c5f6"></a>

```c
#define BEE_UART0_TX 29
```

相关声明：[BEE_UART0_TX](#aba42501ee83715ca6ea53df22183c5f6)。

`UART0_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a1c7070aee57aedc7f8a131fe34444d60"></a>

```c
#define BEE_UART0_RX 30
```

相关声明：[BEE_UART0_RX](#a1c7070aee57aedc7f8a131fe34444d60)。

`UART0_RX` 引脚复用功能（Pinmux Function）。

<a id="r_af5094e3bfde1cf22e80c9144763940cc"></a>

```c
#define BEE_UART0_CTS 31
```

相关声明：[BEE_UART0_CTS](#af5094e3bfde1cf22e80c9144763940cc)。

`UART0_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_a6ea0a2599d172ee66154a55c6dad1544"></a>

```c
#define BEE_UART0_RTS 32
```

相关声明：[BEE_UART0_RTS](#a6ea0a2599d172ee66154a55c6dad1544)。

`UART0_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_aa03d3f61b2ad1379c04e21e409797781"></a>

```c
#define BEE_IRDA_TX 33
```

相关声明：[BEE_IRDA_TX](#aa03d3f61b2ad1379c04e21e409797781)。

`IRDA_TX` 引脚复用功能（Pinmux Function）。

<a id="r_ad5404068fcc7bf2e2207f151d7baacc3"></a>

```c
#define BEE_IRDA_RX 34
```

相关声明：[BEE_IRDA_RX](#ad5404068fcc7bf2e2207f151d7baacc3)。

`IRDA_RX` 引脚复用功能（Pinmux Function）。

<a id="r_acf789455a751381f67bb5c0d00144cee"></a>

```c
#define BEE_UART1_TX 35
```

相关声明：[BEE_UART1_TX](#acf789455a751381f67bb5c0d00144cee)。

`UART1_TX` 引脚复用功能（Pinmux Function）。

<a id="r_a360f04b358a9569940a03d0d19397df3"></a>

```c
#define BEE_UART1_RX 36
```

相关声明：[BEE_UART1_RX](#a360f04b358a9569940a03d0d19397df3)。

`UART1_RX` 引脚复用功能（Pinmux Function）。

<a id="r_ae1a337884566b230fb35533cb45f83ba"></a>

```c
#define BEE_UART1_CTS 37
```

相关声明：[BEE_UART1_CTS](#ae1a337884566b230fb35533cb45f83ba)。

`UART1_CTS` 引脚复用功能（Pinmux Function）。

<a id="r_abe24c85e1d8f04d29607669efb795a85"></a>

```c
#define BEE_UART1_RTS 38
```

相关声明：[BEE_UART1_RTS](#abe24c85e1d8f04d29607669efb795a85)。

`UART1_RTS` 引脚复用功能（Pinmux Function）。

<a id="r_a705a65055475b386227a1dcb3b9857eb"></a>

```c
#define BEE_SPI1_SS_N_0_MASTER 39
```

相关声明：[BEE_SPI1_SS_N_0_MASTER](#a705a65055475b386227a1dcb3b9857eb)。

`SPI1_SS_N_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a1aa1939165393b9db53353ca690581c9"></a>

```c
#define BEE_SPI1_SS_N_1_MASTER 40
```

相关声明：[BEE_SPI1_SS_N_1_MASTER](#a1aa1939165393b9db53353ca690581c9)。

`SPI1_SS_N_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a9665f3e1942bcd7915e765ec9e5387a5"></a>

```c
#define BEE_SPI1_SS_N_2_MASTER 41
```

相关声明：[BEE_SPI1_SS_N_2_MASTER](#a9665f3e1942bcd7915e765ec9e5387a5)。

`SPI1_SS_N_2_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a0452a4a0d75d2f3eba6dac55bd4d209c"></a>

```c
#define BEE_SPI1_CLK_MASTER 42
```

相关声明：[BEE_SPI1_CLK_MASTER](#a0452a4a0d75d2f3eba6dac55bd4d209c)。

`SPI1_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a113270bda7f1996417ae86e9d59f7c6e"></a>

```c
#define BEE_SPI1_MO_MASTER 43
```

相关声明：[BEE_SPI1_MO_MASTER](#a113270bda7f1996417ae86e9d59f7c6e)。

`SPI1_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a8064446640a0d1ff045af352b0da6670"></a>

```c
#define BEE_SPI1_MI_MASTER 44
```

相关声明：[BEE_SPI1_MI_MASTER](#a8064446640a0d1ff045af352b0da6670)。

`SPI1_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_a763d77602a1338c1c0e14d3647de7506"></a>

```c
#define BEE_SPI0_SS_N_0_SLAVE 45
```

相关声明：[BEE_SPI0_SS_N_0_SLAVE](#a763d77602a1338c1c0e14d3647de7506)。

`SPI0_SS_N_0_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_aa74d6d5790ee4b6c3804612d13ac2b5b"></a>

```c
#define BEE_SPI0_CLK_SLAVE 46
```

相关声明：[BEE_SPI0_CLK_SLAVE](#aa74d6d5790ee4b6c3804612d13ac2b5b)。

`SPI0_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ad8b8f9abd4e3a9f468621a1bcebc26c5"></a>

```c
#define BEE_SPI0_SO_SLAVE 47
```

相关声明：[BEE_SPI0_SO_SLAVE](#ad8b8f9abd4e3a9f468621a1bcebc26c5)。

`SPI0_SO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a42c6b4ef4945aa8dacaf653acffae16f"></a>

```c
#define BEE_SPI0_SI_SLAVE 48
```

相关声明：[BEE_SPI0_SI_SLAVE](#a42c6b4ef4945aa8dacaf653acffae16f)。

`SPI0_SI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_aa9f0e0c05f6bd5edc64378118ce90f37"></a>

```c
#define BEE_SPI0_SS_N_0_MASTER 49
```

相关声明：[BEE_SPI0_SS_N_0_MASTER](#aa9f0e0c05f6bd5edc64378118ce90f37)。

`SPI0_SS_N_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ab0446a74b1486abd14de4fd0200ea74f"></a>

```c
#define BEE_SPI0_CLK_MASTER 50
```

相关声明：[BEE_SPI0_CLK_MASTER](#ab0446a74b1486abd14de4fd0200ea74f)。

`SPI0_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ae4d7727fa011b264c2262f8a93286b79"></a>

```c
#define BEE_SPI0_MO_MASTER 51
```

相关声明：[BEE_SPI0_MO_MASTER](#ae4d7727fa011b264c2262f8a93286b79)。

`SPI0_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="r_ad0da29a2b105520d4b082c3995738a7c"></a>

```c
#define BEE_SPI0_MI_MASTER 52
```

相关声明：[BEE_SPI0_MI_MASTER](#ad0da29a2b105520d4b082c3995738a7c)。

`SPI0_MI_MASTER` 引脚复用功能（Pinmux Function）。

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

<a id="r_a69b18937baf0d37c1302b897a29d0f0d"></a>

```c
#define BEE_SWD_CLK 56
```

相关声明：[BEE_SWD_CLK](#a69b18937baf0d37c1302b897a29d0f0d)。

`SWD_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a890a338c14aef5eb8e25844201b0289d"></a>

```c
#define BEE_SWD_DIO 57
```

相关声明：[BEE_SWD_DIO](#a890a338c14aef5eb8e25844201b0289d)。

`SWD_DIO` 引脚复用功能（Pinmux Function）。

<a id="r_a5feafd3851cdad2ae95d13da759f846a"></a>

```c
#define BEE_KEY_COL_0 58
```

相关声明：[BEE_KEY_COL_0](#a5feafd3851cdad2ae95d13da759f846a)。

`KEY_COL_0` 引脚复用功能（Pinmux Function）。

<a id="r_a041f3ef212cd3b5632534b861cbc261a"></a>

```c
#define BEE_KEY_COL_1 59
```

相关声明：[BEE_KEY_COL_1](#a041f3ef212cd3b5632534b861cbc261a)。

`KEY_COL_1` 引脚复用功能（Pinmux Function）。

<a id="r_a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2"></a>

```c
#define BEE_KEY_COL_2 60
```

相关声明：[BEE_KEY_COL_2](#a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2)。

`KEY_COL_2` 引脚复用功能（Pinmux Function）。

<a id="r_a6faea0c7d7cfbc3557937914a8f3a3b5"></a>

```c
#define BEE_KEY_COL_3 61
```

相关声明：[BEE_KEY_COL_3](#a6faea0c7d7cfbc3557937914a8f3a3b5)。

`KEY_COL_3` 引脚复用功能（Pinmux Function）。

<a id="r_ad8b490ea83a896b7c702161613e8351d"></a>

```c
#define BEE_KEY_COL_4 62
```

相关声明：[BEE_KEY_COL_4](#ad8b490ea83a896b7c702161613e8351d)。

`KEY_COL_4` 引脚复用功能（Pinmux Function）。

<a id="r_afbb2d553138a1242007d6339631adb26"></a>

```c
#define BEE_KEY_COL_5 63
```

相关声明：[BEE_KEY_COL_5](#afbb2d553138a1242007d6339631adb26)。

`KEY_COL_5` 引脚复用功能（Pinmux Function）。

<a id="r_ac549db15241e4a3344a387b5b2188970"></a>

```c
#define BEE_KEY_COL_6 64
```

相关声明：[BEE_KEY_COL_6](#ac549db15241e4a3344a387b5b2188970)。

`KEY_COL_6` 引脚复用功能（Pinmux Function）。

<a id="r_aa61ab3cf42f2f48afe802d7cb12f222a"></a>

```c
#define BEE_KEY_COL_7 65
```

相关声明：[BEE_KEY_COL_7](#aa61ab3cf42f2f48afe802d7cb12f222a)。

`KEY_COL_7` 引脚复用功能（Pinmux Function）。

<a id="r_a5d28d0d40e6334592b08698a3f9e0da8"></a>

```c
#define BEE_KEY_COL_8 66
```

相关声明：[BEE_KEY_COL_8](#a5d28d0d40e6334592b08698a3f9e0da8)。

`KEY_COL_8` 引脚复用功能（Pinmux Function）。

<a id="r_ad2c88795b1b458608caa083d469ee86e"></a>

```c
#define BEE_KEY_COL_9 67
```

相关声明：[BEE_KEY_COL_9](#ad2c88795b1b458608caa083d469ee86e)。

`KEY_COL_9` 引脚复用功能（Pinmux Function）。

<a id="r_a431bd45fe23862cc55fa544d684b92d6"></a>

```c
#define BEE_KEY_COL_10 68
```

相关声明：[BEE_KEY_COL_10](#a431bd45fe23862cc55fa544d684b92d6)。

`KEY_COL_10` 引脚复用功能（Pinmux Function）。

<a id="r_a7164c3dc3423f443cd3e39875702f200"></a>

```c
#define BEE_KEY_COL_11 69
```

相关声明：[BEE_KEY_COL_11](#a7164c3dc3423f443cd3e39875702f200)。

`KEY_COL_11` 引脚复用功能（Pinmux Function）。

<a id="r_a02b8793d7bbde10e6d31f380f594758d"></a>

```c
#define BEE_KEY_COL_12 70
```

相关声明：[BEE_KEY_COL_12](#a02b8793d7bbde10e6d31f380f594758d)。

`KEY_COL_12` 引脚复用功能（Pinmux Function）。

<a id="r_a1493d93c12d93ca2e0f6dc267651106b"></a>

```c
#define BEE_KEY_COL_13 71
```

相关声明：[BEE_KEY_COL_13](#a1493d93c12d93ca2e0f6dc267651106b)。

`KEY_COL_13` 引脚复用功能（Pinmux Function）。

<a id="r_a60a32dd7c97e11c25cfec77882914300"></a>

```c
#define BEE_KEY_COL_14 72
```

相关声明：[BEE_KEY_COL_14](#a60a32dd7c97e11c25cfec77882914300)。

`KEY_COL_14` 引脚复用功能（Pinmux Function）。

<a id="r_a689da1d4cb37dbb30ceb751a0fa85b33"></a>

```c
#define BEE_KEY_COL_15 73
```

相关声明：[BEE_KEY_COL_15](#a689da1d4cb37dbb30ceb751a0fa85b33)。

`KEY_COL_15` 引脚复用功能（Pinmux Function）。

<a id="r_a369b59d63cc72309486ad36e29b8c6af"></a>

```c
#define BEE_KEY_COL_16 74
```

相关声明：[BEE_KEY_COL_16](#a369b59d63cc72309486ad36e29b8c6af)。

`KEY_COL_16` 引脚复用功能（Pinmux Function）。

<a id="r_a719bdfcc5efd46dcc6dd7c841c0447d4"></a>

```c
#define BEE_KEY_COL_17 75
```

相关声明：[BEE_KEY_COL_17](#a719bdfcc5efd46dcc6dd7c841c0447d4)。

`KEY_COL_17` 引脚复用功能（Pinmux Function）。

<a id="r_a53aebd67028abe2a744e11d781ca183f"></a>

```c
#define BEE_KEY_COL_18 76
```

相关声明：[BEE_KEY_COL_18](#a53aebd67028abe2a744e11d781ca183f)。

`KEY_COL_18` 引脚复用功能（Pinmux Function）。

<a id="r_af444884011ac39c3dcf213a22259c953"></a>

```c
#define BEE_KEY_COL_19 77
```

相关声明：[BEE_KEY_COL_19](#af444884011ac39c3dcf213a22259c953)。

`KEY_COL_19` 引脚复用功能（Pinmux Function）。

<a id="r_af82f5da17eada898f2dec8de92e603b0"></a>

```c
#define BEE_KEY_ROW_0 78
```

相关声明：[BEE_KEY_ROW_0](#af82f5da17eada898f2dec8de92e603b0)。

`KEY_ROW_0` 引脚复用功能（Pinmux Function）。

<a id="r_a24e82e85a07c80d7e390185f67726756"></a>

```c
#define BEE_KEY_ROW_1 79
```

相关声明：[BEE_KEY_ROW_1](#a24e82e85a07c80d7e390185f67726756)。

`KEY_ROW_1` 引脚复用功能（Pinmux Function）。

<a id="r_a695da19fd7bc007959fe2ce9f3882939"></a>

```c
#define BEE_KEY_ROW_2 80
```

相关声明：[BEE_KEY_ROW_2](#a695da19fd7bc007959fe2ce9f3882939)。

`KEY_ROW_2` 引脚复用功能（Pinmux Function）。

<a id="r_a3920941b7c17c1eb9df377230ae0e3d7"></a>

```c
#define BEE_KEY_ROW_3 81
```

相关声明：[BEE_KEY_ROW_3](#a3920941b7c17c1eb9df377230ae0e3d7)。

`KEY_ROW_3` 引脚复用功能（Pinmux Function）。

<a id="r_a94ce3c3c0775437059fe8d48ca1ae63d"></a>

```c
#define BEE_KEY_ROW_4 82
```

相关声明：[BEE_KEY_ROW_4](#a94ce3c3c0775437059fe8d48ca1ae63d)。

`KEY_ROW_4` 引脚复用功能（Pinmux Function）。

<a id="r_aebdb52372b88e9aa5d7173104f8088c7"></a>

```c
#define BEE_KEY_ROW_5 83
```

相关声明：[BEE_KEY_ROW_5](#aebdb52372b88e9aa5d7173104f8088c7)。

`KEY_ROW_5` 引脚复用功能（Pinmux Function）。

<a id="r_a6535c3d5752c54dd36ff7a138cb70b5c"></a>

```c
#define BEE_KEY_ROW_6 84
```

相关声明：[BEE_KEY_ROW_6](#a6535c3d5752c54dd36ff7a138cb70b5c)。

`KEY_ROW_6` 引脚复用功能（Pinmux Function）。

<a id="r_a4762128bf6b6e86a17b3c8c76ff2fc88"></a>

```c
#define BEE_KEY_ROW_7 85
```

相关声明：[BEE_KEY_ROW_7](#a4762128bf6b6e86a17b3c8c76ff2fc88)。

`KEY_ROW_7` 引脚复用功能（Pinmux Function）。

<a id="r_abbf110abd0ae22bb4767f28fe5901242"></a>

```c
#define BEE_KEY_ROW_8 86
```

相关声明：[BEE_KEY_ROW_8](#abbf110abd0ae22bb4767f28fe5901242)。

`KEY_ROW_8` 引脚复用功能（Pinmux Function）。

<a id="r_a681b30410bb04208c02a53f158dbedfb"></a>

```c
#define BEE_KEY_ROW_9 87
```

相关声明：[BEE_KEY_ROW_9](#a681b30410bb04208c02a53f158dbedfb)。

`KEY_ROW_9` 引脚复用功能（Pinmux Function）。

<a id="r_a8f0c299784cb107d46fdbcd5494ae2f0"></a>

```c
#define BEE_KEY_ROW_10 88
```

相关声明：[BEE_KEY_ROW_10](#a8f0c299784cb107d46fdbcd5494ae2f0)。

`KEY_ROW_10` 引脚复用功能（Pinmux Function）。

<a id="r_a2386911ec69b7416028fab5537243bee"></a>

```c
#define BEE_KEY_ROW_11 89
```

相关声明：[BEE_KEY_ROW_11](#a2386911ec69b7416028fab5537243bee)。

`KEY_ROW_11` 引脚复用功能（Pinmux Function）。

<a id="r_a93f3d11e8a6c9fd056bc4e6a2f156989"></a>

```c
#define BEE_DWGPIO 90
```

相关声明：[BEE_DWGPIO](#a93f3d11e8a6c9fd056bc4e6a2f156989)。

`DWGPIO` 引脚复用功能（Pinmux Function）。

<a id="r_a49516c6243aed5817ba2ae4d6744687b"></a>

```c
#define BEE_DMIC1_CLK 96
```

相关声明：[BEE_DMIC1_CLK](#a49516c6243aed5817ba2ae4d6744687b)。

`DMIC1_CLK` 引脚复用功能（Pinmux Function）。

<a id="r_a8d6a69a1e3591004efb445bd9b3edfb3"></a>

```c
#define BEE_DMIC1_DAT 97
```

相关声明：[BEE_DMIC1_DAT](#a8d6a69a1e3591004efb445bd9b3edfb3)。

`DMIC1_DAT` 引脚复用功能（Pinmux Function）。

<a id="r_a644fe132bc7a607b715744ae214635af"></a>

```c
#define BEE_LRC_I_CODEC_SLAVE 98
```

相关声明：[BEE_LRC_I_CODEC_SLAVE](#a644fe132bc7a607b715744ae214635af)。

`LRC_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a912613b40d5c8101fb80ef546259718c"></a>

```c
#define BEE_BCLK_I_CODEC_SLAVE 99
```

相关声明：[BEE_BCLK_I_CODEC_SLAVE](#a912613b40d5c8101fb80ef546259718c)。

`BCLK_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a4210b1402742ed6b988925e93b2fb875"></a>

```c
#define BEE_SDI_CODEC_SLAVE 100
```

相关声明：[BEE_SDI_CODEC_SLAVE](#a4210b1402742ed6b988925e93b2fb875)。

`SDI_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ad8fb809d69f74a7d77283fb004d2f323"></a>

```c
#define BEE_SDO_CODEC_SLAVE 101
```

相关声明：[BEE_SDO_CODEC_SLAVE](#ad8fb809d69f74a7d77283fb004d2f323)。

`SDO_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_ab122a176b695a923610b8d090ade6430"></a>

```c
#define BEE_BT_COEX_I_0 106
```

相关声明：[BEE_BT_COEX_I_0](#ab122a176b695a923610b8d090ade6430)。

`BT_COEX_I_0` 引脚复用功能（Pinmux Function）。

<a id="r_af55b98947776718e3b45e3e4c1636baa"></a>

```c
#define BEE_BT_COEX_I_1 107
```

相关声明：[BEE_BT_COEX_I_1](#af55b98947776718e3b45e3e4c1636baa)。

`BT_COEX_I_1` 引脚复用功能（Pinmux Function）。

<a id="r_abc580ad83269067b32fb42a476ff1e3d"></a>

```c
#define BEE_BT_COEX_I_2 108
```

相关声明：[BEE_BT_COEX_I_2](#abc580ad83269067b32fb42a476ff1e3d)。

`BT_COEX_I_2` 引脚复用功能（Pinmux Function）。

<a id="r_aae8555c6b679f48d0dcba40191e77166"></a>

```c
#define BEE_BT_COEX_I_3 109
```

相关声明：[BEE_BT_COEX_I_3](#aae8555c6b679f48d0dcba40191e77166)。

`BT_COEX_I_3` 引脚复用功能（Pinmux Function）。

<a id="r_adf8796c519f840189f367e7acd9e1738"></a>

```c
#define BEE_BT_COEX_O_0 110
```

相关声明：[BEE_BT_COEX_O_0](#adf8796c519f840189f367e7acd9e1738)。

`BT_COEX_O_0` 引脚复用功能（Pinmux Function）。

<a id="r_ab67e3e28eda567571d3d7586e94e03da"></a>

```c
#define BEE_BT_COEX_O_1 111
```

相关声明：[BEE_BT_COEX_O_1](#ab67e3e28eda567571d3d7586e94e03da)。

`BT_COEX_O_1` 引脚复用功能（Pinmux Function）。

<a id="r_a4b24f9dbcd7d24128db569fb93d84eef"></a>

```c
#define BEE_BT_COEX_O_2 112
```

相关声明：[BEE_BT_COEX_O_2](#a4b24f9dbcd7d24128db569fb93d84eef)。

`BT_COEX_O_2` 引脚复用功能（Pinmux Function）。

<a id="r_a786a847e166079b62cb5862573c5aeee"></a>

```c
#define BEE_BT_COEX_O_3 113
```

相关声明：[BEE_BT_COEX_O_3](#a786a847e166079b62cb5862573c5aeee)。

`BT_COEX_O_3` 引脚复用功能（Pinmux Function）。

<a id="r_abcf72b3e409c194ba2d2173aa7cb41ab"></a>

```c
#define BEE_PTA_I2C_CLK_SLAVE 114
```

相关声明：[BEE_PTA_I2C_CLK_SLAVE](#abcf72b3e409c194ba2d2173aa7cb41ab)。

`PTA_I2C_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a9254d4dd1aa797f1590ef84c1cd07ed1"></a>

```c
#define BEE_PTA_I2C_DAT_SLAVE 115
```

相关声明：[BEE_PTA_I2C_DAT_SLAVE](#a9254d4dd1aa797f1590ef84c1cd07ed1)。

`PTA_I2C_DAT_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="r_a2e6661f9ef9bb93179130a186653468a"></a>

```c
#define BEE_PTA_I2C_INT_OUT 116
```

相关声明：[BEE_PTA_I2C_INT_OUT](#a2e6661f9ef9bb93179130a186653468a)。

`PTA_I2C_INT_OUT` 引脚复用功能（Pinmux Function）。

<a id="r_a37c7aeafe54f05e6a267f9f16af25c0c"></a>

```c
#define BEE_EN_EXPA 117
```

相关声明：[BEE_EN_EXPA](#a37c7aeafe54f05e6a267f9f16af25c0c)。

`EN_EXPA` 引脚复用功能（Pinmux Function）。

<a id="r_a510878941f7e323fe7eee5bb1b743c3e"></a>

```c
#define BEE_EN_EXLNA 118
```

相关声明：[BEE_EN_EXLNA](#a510878941f7e323fe7eee5bb1b743c3e)。

`EN_EXLNA` 引脚复用功能（Pinmux Function）。

<a id="r_a44044eb50520f7a0dbf83abe70dc2bc5"></a>

```c
#define BEE_LRC_SPORT0 123
```

相关声明：[BEE_LRC_SPORT0](#a44044eb50520f7a0dbf83abe70dc2bc5)。

`LRC_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_ae8c197cf5a76f0e30b400e4190fa3d60"></a>

```c
#define BEE_BCLK_SPORT0 124
```

相关声明：[BEE_BCLK_SPORT0](#ae8c197cf5a76f0e30b400e4190fa3d60)。

`BCLK_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_a0a8dabb3051d18f3b0c63485417bfafd"></a>

```c
#define BEE_ADCDAT_SPORT0 125
```

相关声明：[BEE_ADCDAT_SPORT0](#a0a8dabb3051d18f3b0c63485417bfafd)。

`ADCDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_a60cdc36815f5a5057025a7a4e70e202f"></a>

```c
#define BEE_DACDAT_SPORT0 126
```

相关声明：[BEE_DACDAT_SPORT0](#a60cdc36815f5a5057025a7a4e70e202f)。

`DACDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="r_a06c52f8460be70da0402f6e138985ad4"></a>

```c
#define BEE_MCLK 127
```

相关声明：[BEE_MCLK](#a06c52f8460be70da0402f6e138985ad4)。

`MCLK` 引脚复用功能（Pinmux Function）。

<a id="r_a57b4629fefc1551701f145558e57f8fa"></a>

```c
#define BEE_PINMUX_MAX (BEE_MCLK + 1)
```

相关声明：[BEE_PINMUX_MAX](#a57b4629fefc1551701f145558e57f8fa)、[BEE_MCLK](#a06c52f8460be70da0402f6e138985ad4)。

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

通用输入输出 0（GPIO0）。

<a id="r_a6e605c856305ec72ac000d8cc45ab0b9"></a>

```c
#define P0_1 1
```

相关声明：[P0_1](#a6e605c856305ec72ac000d8cc45ab0b9)。

通用输入输出 1（GPIO1）。

<a id="r_a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

```c
#define P0_2 2
```

相关声明：[P0_2](#a876e3d0917cea9d0a75b2f6df2c3f1d4)。

引脚功能（Pin Function）：`GPIO2`。

<a id="r_ab73f15237a6f8860438ba0359b283686"></a>

```c
#define P0_3 3
```

相关声明：[P0_3](#ab73f15237a6f8860438ba0359b283686)。

引脚功能（Pin Function）：`GPIO3`。

<a id="r_a3218b7341a4f084375bade756f108940"></a>

```c
#define P0_4 4
```

相关声明：[P0_4](#a3218b7341a4f084375bade756f108940)。

引脚功能（Pin Function）：`GPIO4`。

<a id="r_aa1681f3dab52db87cd32f77b20352770"></a>

```c
#define P0_5 5
```

相关声明：[P0_5](#aa1681f3dab52db87cd32f77b20352770)。

引脚功能（Pin Function）：`GPIO5`。

<a id="r_a990dc4ba08ec342d0bfa50f99d9e1868"></a>

```c
#define P0_6 6
```

相关声明：[P0_6](#a990dc4ba08ec342d0bfa50f99d9e1868)。

引脚功能（Pin Function）：`GPIO6`。

<a id="r_a34087bca5283adcf7cc7c810f30eab80"></a>

```c
#define P0_7 7
```

相关声明：[P0_7](#a34087bca5283adcf7cc7c810f30eab80)。

引脚功能（Pin Function）：`GPIO7`。

<a id="r_a0a5c0ef038f9728173ca136eed5c9cd2"></a>

```c
#define P1_0 8
```

相关声明：[P1_0](#a0a5c0ef038f9728173ca136eed5c9cd2)。

通用输入／输出（GPIO）：`GPIO8`。

<a id="r_aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

```c
#define P1_1 9
```

相关声明：[P1_1](#aa7c3cebcd9dc4598bb69e51ecee85bd0)。

通用输入／输出（GPIO）：`GPIO9`。

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

<a id="r_a9e219f75c65aa5b19d59bd1596b3e548"></a>

```c
#define P1_6 14
```

相关声明：[P1_6](#a9e219f75c65aa5b19d59bd1596b3e548)。

GPIO14 引脚。

<a id="r_a59e6507c1874213b84ae809c24c3a76e"></a>

```c
#define P1_7 15
```

相关声明：[P1_7](#a59e6507c1874213b84ae809c24c3a76e)。

GPIO15 引脚。

<a id="r_a5b005e989c9ae92562196f830232dc1a"></a>

```c
#define P2_0 16
```

相关声明：[P2_0](#a5b005e989c9ae92562196f830232dc1a)。

通用输入／输出（GPIO）：`GPIO16`。

<a id="r_aaae6a77f4b93ec74cb11947217dd8fd1"></a>

```c
#define P2_1 17
```

相关声明：[P2_1](#aaae6a77f4b93ec74cb11947217dd8fd1)。

通用输入／输出（GPIO）：`GPIO17`。

<a id="r_a9216eb7ac06cf1906b8c3e6884943b5e"></a>

```c
#define P2_2 18
```

相关声明：[P2_2](#a9216eb7ac06cf1906b8c3e6884943b5e)。

通用输入／输出（GPIO）：`GPIO18`。

<a id="r_a98005d211f8692aa984d81e1b1cefd67"></a>

```c
#define P2_3 19
```

相关声明：[P2_3](#a98005d211f8692aa984d81e1b1cefd67)。

通用输入／输出（GPIO）：`GPIO19`。

<a id="r_a541f1278e79f6ce8b83f48b5f3e1c177"></a>

```c
#define P2_4 20
```

相关声明：[P2_4](#a541f1278e79f6ce8b83f48b5f3e1c177)。

通用输入／输出（GPIO）：`GPIO20`。

<a id="r_acf47cd715ad993d583a85ef8fcac6b3e"></a>

```c
#define P2_5 21
```

相关声明：[P2_5](#acf47cd715ad993d583a85ef8fcac6b3e)。

通用输入／输出（GPIO）：`GPIO21`。

<a id="r_aaf264201304e2d44dc57b61eaf041654"></a>

```c
#define P2_6 22
```

相关声明：[P2_6](#aaf264201304e2d44dc57b61eaf041654)。

通用输入／输出（GPIO）：`GPIO22`。

<a id="r_a4f3e81fec0b7d90e9ff61bae35882c8a"></a>

```c
#define P2_7 23
```

相关声明：[P2_7](#a4f3e81fec0b7d90e9ff61bae35882c8a)。

通用输入／输出（GPIO）：`GPIO23`。

<a id="r_a335073a6b45e1affb80cb03be0aebd28"></a>

```c
#define P3_0 24
```

相关声明：[P3_0](#a335073a6b45e1affb80cb03be0aebd28)。

通用输入／输出（GPIO）：`GPIO24`。

<a id="r_aa56aef7e8461bcefa151ed84ab438dd9"></a>

```c
#define P3_1 25
```

相关声明：[P3_1](#aa56aef7e8461bcefa151ed84ab438dd9)。

通用输入／输出（GPIO）：`GPIO25`。

<a id="r_a7060bd469f1a43b0d5c130d35f291687"></a>

```c
#define P3_2 26
```

相关声明：[P3_2](#a7060bd469f1a43b0d5c130d35f291687)。

通用输入／输出（GPIO）：`GPIO26`。

<a id="r_a3394fd21eaccbcd6bfb4cc9a20a93f63"></a>

```c
#define P3_3 27
```

相关声明：[P3_3](#a3394fd21eaccbcd6bfb4cc9a20a93f63)。

通用输入／输出（GPIO）：`GPIO27`。

<a id="r_a444f7e1de792cb878057f9fedf8c1e92"></a>

```c
#define P3_4 28
```

相关声明：[P3_4](#a444f7e1de792cb878057f9fedf8c1e92)。

通用输入／输出（GPIO）：`GPIO28`。

<a id="r_add5e9628720a9e18e34d148c5e4386ae"></a>

```c
#define P3_5 29
```

相关声明：[P3_5](#add5e9628720a9e18e34d148c5e4386ae)。

通用输入／输出（GPIO）：`GPIO29`。

<a id="r_a5f901ec132df36067c1aebb4f0f5e99e"></a>

```c
#define P3_6 30
```

相关声明：[P3_6](#a5f901ec132df36067c1aebb4f0f5e99e)。

通用输入／输出（GPIO）：`GPIO30`。

<a id="r_a7d02796f1733eadcc315008ac83e939a"></a>

```c
#define P4_0 32
```

相关声明：[P4_0](#a7d02796f1733eadcc315008ac83e939a)。

通用输入／输出（GPIO）：`GPIO13`。

<a id="r_adbc665f56899cd3fa782adc76a77087f"></a>

```c
#define P4_1 33
```

相关声明：[P4_1](#adbc665f56899cd3fa782adc76a77087f)。

通用输入／输出（GPIO）：`GPIO29`。

<a id="r_aef67ce6b9c7f16a266927b0545631bc2"></a>

```c
#define P4_2 34
```

相关声明：[P4_2](#aef67ce6b9c7f16a266927b0545631bc2)。

通用输入／输出（GPIO）：`GPIO30`。

<a id="r_a57a1bc2364d61983bdf84d6e8a7cda5b"></a>

```c
#define P4_3 35
```

相关声明：[P4_3](#a57a1bc2364d61983bdf84d6e8a7cda5b)。

通用输入／输出（GPIO）：`GPIO31`。

<a id="r_a64a140ac19ea2cdcd9d586e68abe14ce"></a>

```c
#define H_0 36
```

相关声明：[H_0](#a64a140ac19ea2cdcd9d586e68abe14ce)。

通用输入／输出 GPIO10／麦克风偏置（MICBIAS）。

<a id="r_aaec8c9b05d0535f709f9e40ededd5ae8"></a>

```c
#define P5_1 37
```

相关声明：[P5_1](#aaec8c9b05d0535f709f9e40ededd5ae8)。

通用输入／输出（GPIO）：`GPIO11`。

<a id="r_ae908c3f54860d6e0d70a10bbc5b19aae"></a>

```c
#define P5_2 38
```

相关声明：[P5_2](#ae908c3f54860d6e0d70a10bbc5b19aae)。

通用输入／输出（GPIO）：`GPIO12`。

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

<a id="r_a6d0af9f41c7f9b64b03c2d307691788b"></a>

```c
#define BEE_PSEL_GPIOA_16_P2_0 BEE_PSEL(DWGPIO, P2_0)
```

相关声明：[BEE_PSEL_GPIOA_16_P2_0](#a6d0af9f41c7f9b64b03c2d307691788b)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_0](#a5b005e989c9ae92562196f830232dc1a)。

引脚（Pin）`P2_0` 对应的通用输入／输出（GPIO）为 `GPIOA_16`。

<a id="r_a2bf034c47ca6517f8f2af9c01297f078"></a>

```c
#define BEE_PSEL_GPIOA_17_P2_1 BEE_PSEL(DWGPIO, P2_1)
```

相关声明：[BEE_PSEL_GPIOA_17_P2_1](#a2bf034c47ca6517f8f2af9c01297f078)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_1](#aaae6a77f4b93ec74cb11947217dd8fd1)。

引脚（Pin）`P2_1` 对应的通用输入／输出（GPIO）为 `GPIOA_17`。

<a id="r_aa9cf9ff9afd6b7b48709419c2d2bf436"></a>

```c
#define BEE_PSEL_GPIOA_18_P2_2 BEE_PSEL(DWGPIO, P2_2)
```

相关声明：[BEE_PSEL_GPIOA_18_P2_2](#aa9cf9ff9afd6b7b48709419c2d2bf436)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_2](#a9216eb7ac06cf1906b8c3e6884943b5e)。

引脚（Pin）`P2_2` 对应的通用输入／输出（GPIO）为 `GPIOA_18`。

<a id="r_a5c5e07ed4ffb78c9e7b2efcf4352a862"></a>

```c
#define BEE_PSEL_GPIOA_19_P2_3 BEE_PSEL(DWGPIO, P2_3)
```

相关声明：[BEE_PSEL_GPIOA_19_P2_3](#a5c5e07ed4ffb78c9e7b2efcf4352a862)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_3](#a98005d211f8692aa984d81e1b1cefd67)。

引脚（Pin）`P2_3` 对应的通用输入／输出（GPIO）为 `GPIOA_19`。

<a id="r_a9e5898cc383851790bfeb0efbee7f7f0"></a>

```c
#define BEE_PSEL_GPIOA_20_P2_4 BEE_PSEL(DWGPIO, P2_4)
```

相关声明：[BEE_PSEL_GPIOA_20_P2_4](#a9e5898cc383851790bfeb0efbee7f7f0)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_4](#a541f1278e79f6ce8b83f48b5f3e1c177)。

引脚（Pin）`P2_4` 对应的通用输入／输出（GPIO）为 `GPIOA_20`。

<a id="r_ad1fe4429bc18a55f5d5ea3c94df1a9b3"></a>

```c
#define BEE_PSEL_GPIOA_21_P2_5 BEE_PSEL(DWGPIO, P2_5)
```

相关声明：[BEE_PSEL_GPIOA_21_P2_5](#ad1fe4429bc18a55f5d5ea3c94df1a9b3)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_5](#acf47cd715ad993d583a85ef8fcac6b3e)。

引脚（Pin）`P2_5` 对应的通用输入／输出（GPIO）为 `GPIOA_21`。

<a id="r_a31be5e118e39e3ca09e7f33080e5d526"></a>

```c
#define BEE_PSEL_GPIOA_22_P2_6 BEE_PSEL(DWGPIO, P2_6)
```

相关声明：[BEE_PSEL_GPIOA_22_P2_6](#a31be5e118e39e3ca09e7f33080e5d526)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_6](#aaf264201304e2d44dc57b61eaf041654)。

引脚（Pin）`P2_6` 对应的通用输入／输出（GPIO）为 `GPIOA_22`。

<a id="r_acf905757ae77f36fb5bc5e158287397c"></a>

```c
#define BEE_PSEL_GPIOA_23_P2_7 BEE_PSEL(DWGPIO, P2_7)
```

相关声明：[BEE_PSEL_GPIOA_23_P2_7](#acf905757ae77f36fb5bc5e158287397c)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P2_7](#a4f3e81fec0b7d90e9ff61bae35882c8a)。

引脚（Pin）`P2_7` 对应的通用输入／输出（GPIO）为 `GPIOA_23`。

<a id="r_aa37bdadc4a1904b625a485b5cdfd0271"></a>

```c
#define BEE_PSEL_GPIOA_24_P3_0 BEE_PSEL(DWGPIO, P3_0)
```

相关声明：[BEE_PSEL_GPIOA_24_P3_0](#aa37bdadc4a1904b625a485b5cdfd0271)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_0](#a335073a6b45e1affb80cb03be0aebd28)。

引脚（Pin）`P3_0` 对应的通用输入／输出（GPIO）为 `GPIOA_24`。

<a id="r_abceea0402ce6c2786a62dc5f7f43dfb0"></a>

```c
#define BEE_PSEL_GPIOA_25_P3_1 BEE_PSEL(DWGPIO, P3_1)
```

相关声明：[BEE_PSEL_GPIOA_25_P3_1](#abceea0402ce6c2786a62dc5f7f43dfb0)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_1](#aa56aef7e8461bcefa151ed84ab438dd9)。

引脚（Pin）`P3_1` 对应的通用输入／输出（GPIO）为 `GPIOA_25`。

<a id="r_a27fea86f2884134d2298fdb5429ad278"></a>

```c
#define BEE_PSEL_GPIOA_26_P3_2 BEE_PSEL(DWGPIO, P3_2)
```

相关声明：[BEE_PSEL_GPIOA_26_P3_2](#a27fea86f2884134d2298fdb5429ad278)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_2](#a7060bd469f1a43b0d5c130d35f291687)。

引脚（Pin）`P3_2` 对应的通用输入／输出（GPIO）为 `GPIOA_26`。

<a id="r_a32c4f93dc6dce1978b9a036f8055f6fd"></a>

```c
#define BEE_PSEL_GPIOA_27_P3_3 BEE_PSEL(DWGPIO, P3_3)
```

相关声明：[BEE_PSEL_GPIOA_27_P3_3](#a32c4f93dc6dce1978b9a036f8055f6fd)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_3](#a3394fd21eaccbcd6bfb4cc9a20a93f63)。

引脚（Pin）`P3_3` 对应的通用输入／输出（GPIO）为 `GPIOA_27`。

<a id="r_a9d5ab1788edfd9c617cb81a926cfa781"></a>

```c
#define BEE_PSEL_GPIOA_28_P3_4 BEE_PSEL(DWGPIO, P3_4)
```

相关声明：[BEE_PSEL_GPIOA_28_P3_4](#a9d5ab1788edfd9c617cb81a926cfa781)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_4](#a444f7e1de792cb878057f9fedf8c1e92)。

引脚（Pin）`P3_4` 对应的通用输入／输出（GPIO）为 `GPIOA_28`。

<a id="r_a9bccee519300ba03d2d95dde69877bc5"></a>

```c
#define BEE_PSEL_GPIOA_29_P3_5 BEE_PSEL(DWGPIO, P3_5)
```

相关声明：[BEE_PSEL_GPIOA_29_P3_5](#a9bccee519300ba03d2d95dde69877bc5)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_5](#add5e9628720a9e18e34d148c5e4386ae)。

引脚（Pin）`P3_5` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="r_ab3f859f908e1aeaa64b47b41ab0995c3"></a>

```c
#define BEE_PSEL_GPIOA_30_P3_6 BEE_PSEL(DWGPIO, P3_6)
```

相关声明：[BEE_PSEL_GPIOA_30_P3_6](#ab3f859f908e1aeaa64b47b41ab0995c3)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P3_6](#a5f901ec132df36067c1aebb4f0f5e99e)。

引脚（Pin）`P3_6` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="r_a794b2ac5d4c63a07929368b61edb9a2a"></a>

```c
#define BEE_PSEL_GPIOA_13_P4_0 BEE_PSEL(DWGPIO, P4_0)
```

相关声明：[BEE_PSEL_GPIOA_13_P4_0](#a794b2ac5d4c63a07929368b61edb9a2a)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_0](#a7d02796f1733eadcc315008ac83e939a)。

引脚（Pin）`P4_0` 对应的通用输入／输出（GPIO）为 `GPIOA_13`。

<a id="r_a7c0d91ef2df9f58a2d0654fc6ce9f49f"></a>

```c
#define BEE_PSEL_GPIOA_29_P4_1 BEE_PSEL(DWGPIO, P4_1)
```

相关声明：[BEE_PSEL_GPIOA_29_P4_1](#a7c0d91ef2df9f58a2d0654fc6ce9f49f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_1](#adbc665f56899cd3fa782adc76a77087f)。

引脚（Pin）`P4_1` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="r_abf663addb6c2c9870416d59bba8d203f"></a>

```c
#define BEE_PSEL_GPIOA_30_P4_2 BEE_PSEL(DWGPIO, P4_2)
```

相关声明：[BEE_PSEL_GPIOA_30_P4_2](#abf663addb6c2c9870416d59bba8d203f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_2](#aef67ce6b9c7f16a266927b0545631bc2)。

引脚（Pin）`P4_2` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="r_ab3f3971ffa2d95180044d2715938df9f"></a>

```c
#define BEE_PSEL_GPIOA_31_P4_3 BEE_PSEL(DWGPIO, P4_3)
```

相关声明：[BEE_PSEL_GPIOA_31_P4_3](#ab3f3971ffa2d95180044d2715938df9f)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P4_3](#a57a1bc2364d61983bdf84d6e8a7cda5b)。

引脚（Pin）`P4_3` 对应的通用输入／输出（GPIO）为 `GPIOA_31`。

<a id="r_a91df143d334eae24d1f8ff1cbc97fb78"></a>

```c
#define BEE_PSEL_GPIOA_11_P5_1 BEE_PSEL(DWGPIO, P5_1)
```

相关声明：[BEE_PSEL_GPIOA_11_P5_1](#a91df143d334eae24d1f8ff1cbc97fb78)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_1](#aaec8c9b05d0535f709f9e40ededd5ae8)。

引脚（Pin）`P5_1` 对应的通用输入／输出（GPIO）为 `GPIOA_11`。

<a id="r_a8f1dd2443ab15fbd599c12b10f0fd78d"></a>

```c
#define BEE_PSEL_GPIOA_12_P5_2 BEE_PSEL(DWGPIO, P5_2)
```

相关声明：[BEE_PSEL_GPIOA_12_P5_2](#a8f1dd2443ab15fbd599c12b10f0fd78d)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[P5_2](#ae908c3f54860d6e0d70a10bbc5b19aae)。

引脚（Pin）`P5_2` 对应的通用输入／输出（GPIO）为 `GPIOA_12`。

<a id="r_ac1eba0e039decabd2f41c8b58516b8ba"></a>

```c
#define BEE_PSEL_GPIOA_10_H_0 BEE_PSEL(DWGPIO, H_0)
```

相关声明：[BEE_PSEL_GPIOA_10_H_0](#ac1eba0e039decabd2f41c8b58516b8ba)、[BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)、[H_0](#a64a140ac19ea2cdcd9d586e68abe14ce)。

引脚（Pin）`H_0` 对应的通用输入／输出（GPIO）为 `GPIOA_10`。

## 5.2\_详细说明（Detailed Documentation）

<a id="a0a8dabb3051d18f3b0c63485417bfafd"></a>

### `BEE_ADCDAT_SPORT0`

```c
#define BEE_ADCDAT_SPORT0 125
```

`ADCDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a912613b40d5c8101fb80ef546259718c"></a>

### `BEE_BCLK_I_CODEC_SLAVE`

```c
#define BEE_BCLK_I_CODEC_SLAVE 99
```

`BCLK_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ae8c197cf5a76f0e30b400e4190fa3d60"></a>

### `BEE_BCLK_SPORT0`

```c
#define BEE_BCLK_SPORT0 124
```

`BCLK_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="ab122a176b695a923610b8d090ade6430"></a>

### `BEE_BT_COEX_I_0`

```c
#define BEE_BT_COEX_I_0 106
```

`BT_COEX_I_0` 引脚复用功能（Pinmux Function）。

<a id="af55b98947776718e3b45e3e4c1636baa"></a>

### `BEE_BT_COEX_I_1`

```c
#define BEE_BT_COEX_I_1 107
```

`BT_COEX_I_1` 引脚复用功能（Pinmux Function）。

<a id="abc580ad83269067b32fb42a476ff1e3d"></a>

### `BEE_BT_COEX_I_2`

```c
#define BEE_BT_COEX_I_2 108
```

`BT_COEX_I_2` 引脚复用功能（Pinmux Function）。

<a id="aae8555c6b679f48d0dcba40191e77166"></a>

### `BEE_BT_COEX_I_3`

```c
#define BEE_BT_COEX_I_3 109
```

`BT_COEX_I_3` 引脚复用功能（Pinmux Function）。

<a id="adf8796c519f840189f367e7acd9e1738"></a>

### `BEE_BT_COEX_O_0`

```c
#define BEE_BT_COEX_O_0 110
```

`BT_COEX_O_0` 引脚复用功能（Pinmux Function）。

<a id="ab67e3e28eda567571d3d7586e94e03da"></a>

### `BEE_BT_COEX_O_1`

```c
#define BEE_BT_COEX_O_1 111
```

`BT_COEX_O_1` 引脚复用功能（Pinmux Function）。

<a id="a4b24f9dbcd7d24128db569fb93d84eef"></a>

### `BEE_BT_COEX_O_2`

```c
#define BEE_BT_COEX_O_2 112
```

`BT_COEX_O_2` 引脚复用功能（Pinmux Function）。

<a id="a786a847e166079b62cb5862573c5aeee"></a>

### `BEE_BT_COEX_O_3`

```c
#define BEE_BT_COEX_O_3 113
```

`BT_COEX_O_3` 引脚复用功能（Pinmux Function）。

<a id="a60cdc36815f5a5057025a7a4e70e202f"></a>

### `BEE_DACDAT_SPORT0`

```c
#define BEE_DACDAT_SPORT0 126
```

`DACDAT_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a49516c6243aed5817ba2ae4d6744687b"></a>

### `BEE_DMIC1_CLK`

```c
#define BEE_DMIC1_CLK 96
```

`DMIC1_CLK` 引脚复用功能（Pinmux Function）。

<a id="a8d6a69a1e3591004efb445bd9b3edfb3"></a>

### `BEE_DMIC1_DAT`

```c
#define BEE_DMIC1_DAT 97
```

`DMIC1_DAT` 引脚复用功能（Pinmux Function）。

<a id="a93f3d11e8a6c9fd056bc4e6a2f156989"></a>

### `BEE_DWGPIO`

```c
#define BEE_DWGPIO 90
```

`DWGPIO` 引脚复用功能（Pinmux Function）。

<a id="a510878941f7e323fe7eee5bb1b743c3e"></a>

### `BEE_EN_EXLNA`

```c
#define BEE_EN_EXLNA 118
```

`EN_EXLNA` 引脚复用功能（Pinmux Function）。

<a id="a37c7aeafe54f05e6a267f9f16af25c0c"></a>

### `BEE_EN_EXPA`

```c
#define BEE_EN_EXPA 117
```

`EN_EXPA` 引脚复用功能（Pinmux Function）。

<a id="a6ff1811284f84284f5dac6c4daaf8cb8"></a>

### `BEE_ENPWM0`

```c
#define BEE_ENPWM0 19
```

`ENPWM0` 引脚复用功能（Pinmux Function）。

<a id="a70f463ef325204a7874ade112c0993b3"></a>

### `BEE_ENPWM0_N`

```c
#define BEE_ENPWM0_N 12
```

`ENPWM0_N` 引脚复用功能（Pinmux Function）。

<a id="a317e02b0cb9050e461acf3c246be9af4"></a>

### `BEE_ENPWM0_P`

```c
#define BEE_ENPWM0_P 11
```

`ENPWM0_P` 引脚复用功能（Pinmux Function）。

<a id="aee030c5731a3c6ee0f2c52de0a8e9d3b"></a>

### `BEE_ENPWM1`

```c
#define BEE_ENPWM1 20
```

`ENPWM1` 引脚复用功能（Pinmux Function）。

<a id="ae0341d05951da84bd30617c9dc341628"></a>

### `BEE_I2C0_CLK`

```c
#define BEE_I2C0_CLK 5
```

`I2C0_CLK` 引脚复用功能（Pinmux Function）。

<a id="abf8d90380239e366fb63fd777fb25075"></a>

### `BEE_I2C0_DAT`

```c
#define BEE_I2C0_DAT 6
```

`I2C0_DAT` 引脚复用功能（Pinmux Function）。

<a id="ad89dd6f55609883daef7915f779b193f"></a>

### `BEE_I2C1_CLK`

```c
#define BEE_I2C1_CLK 7
```

`I2C1_CLK` 引脚复用功能（Pinmux Function）。

<a id="aa70f0eb0a8271e9e027a7307e9c2f203"></a>

### `BEE_I2C1_DAT`

```c
#define BEE_I2C1_DAT 8
```

`I2C1_DAT` 引脚复用功能（Pinmux Function）。

<a id="aa96a1b1f865f33896d26cb0ebc67a654"></a>

### `BEE_IDLE_MODE`

```c
#define BEE_IDLE_MODE 0
```

`IDLE_MODE` 引脚复用功能（Pinmux Function）。

<a id="ad5404068fcc7bf2e2207f151d7baacc3"></a>

### `BEE_IRDA_RX`

```c
#define BEE_IRDA_RX 34
```

`IRDA_RX` 引脚复用功能（Pinmux Function）。

<a id="aa03d3f61b2ad1379c04e21e409797781"></a>

### `BEE_IRDA_TX`

```c
#define BEE_IRDA_TX 33
```

`IRDA_TX` 引脚复用功能（Pinmux Function）。

<a id="a5feafd3851cdad2ae95d13da759f846a"></a>

### `BEE_KEY_COL_0`

```c
#define BEE_KEY_COL_0 58
```

`KEY_COL_0` 引脚复用功能（Pinmux Function）。

<a id="a041f3ef212cd3b5632534b861cbc261a"></a>

### `BEE_KEY_COL_1`

```c
#define BEE_KEY_COL_1 59
```

`KEY_COL_1` 引脚复用功能（Pinmux Function）。

<a id="a431bd45fe23862cc55fa544d684b92d6"></a>

### `BEE_KEY_COL_10`

```c
#define BEE_KEY_COL_10 68
```

`KEY_COL_10` 引脚复用功能（Pinmux Function）。

<a id="a7164c3dc3423f443cd3e39875702f200"></a>

### `BEE_KEY_COL_11`

```c
#define BEE_KEY_COL_11 69
```

`KEY_COL_11` 引脚复用功能（Pinmux Function）。

<a id="a02b8793d7bbde10e6d31f380f594758d"></a>

### `BEE_KEY_COL_12`

```c
#define BEE_KEY_COL_12 70
```

`KEY_COL_12` 引脚复用功能（Pinmux Function）。

<a id="a1493d93c12d93ca2e0f6dc267651106b"></a>

### `BEE_KEY_COL_13`

```c
#define BEE_KEY_COL_13 71
```

`KEY_COL_13` 引脚复用功能（Pinmux Function）。

<a id="a60a32dd7c97e11c25cfec77882914300"></a>

### `BEE_KEY_COL_14`

```c
#define BEE_KEY_COL_14 72
```

`KEY_COL_14` 引脚复用功能（Pinmux Function）。

<a id="a689da1d4cb37dbb30ceb751a0fa85b33"></a>

### `BEE_KEY_COL_15`

```c
#define BEE_KEY_COL_15 73
```

`KEY_COL_15` 引脚复用功能（Pinmux Function）。

<a id="a369b59d63cc72309486ad36e29b8c6af"></a>

### `BEE_KEY_COL_16`

```c
#define BEE_KEY_COL_16 74
```

`KEY_COL_16` 引脚复用功能（Pinmux Function）。

<a id="a719bdfcc5efd46dcc6dd7c841c0447d4"></a>

### `BEE_KEY_COL_17`

```c
#define BEE_KEY_COL_17 75
```

`KEY_COL_17` 引脚复用功能（Pinmux Function）。

<a id="a53aebd67028abe2a744e11d781ca183f"></a>

### `BEE_KEY_COL_18`

```c
#define BEE_KEY_COL_18 76
```

`KEY_COL_18` 引脚复用功能（Pinmux Function）。

<a id="af444884011ac39c3dcf213a22259c953"></a>

### `BEE_KEY_COL_19`

```c
#define BEE_KEY_COL_19 77
```

`KEY_COL_19` 引脚复用功能（Pinmux Function）。

<a id="a55ccd6cf5e8ea96ceb2ff17c9f9d6fc2"></a>

### `BEE_KEY_COL_2`

```c
#define BEE_KEY_COL_2 60
```

`KEY_COL_2` 引脚复用功能（Pinmux Function）。

<a id="a6faea0c7d7cfbc3557937914a8f3a3b5"></a>

### `BEE_KEY_COL_3`

```c
#define BEE_KEY_COL_3 61
```

`KEY_COL_3` 引脚复用功能（Pinmux Function）。

<a id="ad8b490ea83a896b7c702161613e8351d"></a>

### `BEE_KEY_COL_4`

```c
#define BEE_KEY_COL_4 62
```

`KEY_COL_4` 引脚复用功能（Pinmux Function）。

<a id="afbb2d553138a1242007d6339631adb26"></a>

### `BEE_KEY_COL_5`

```c
#define BEE_KEY_COL_5 63
```

`KEY_COL_5` 引脚复用功能（Pinmux Function）。

<a id="ac549db15241e4a3344a387b5b2188970"></a>

### `BEE_KEY_COL_6`

```c
#define BEE_KEY_COL_6 64
```

`KEY_COL_6` 引脚复用功能（Pinmux Function）。

<a id="aa61ab3cf42f2f48afe802d7cb12f222a"></a>

### `BEE_KEY_COL_7`

```c
#define BEE_KEY_COL_7 65
```

`KEY_COL_7` 引脚复用功能（Pinmux Function）。

<a id="a5d28d0d40e6334592b08698a3f9e0da8"></a>

### `BEE_KEY_COL_8`

```c
#define BEE_KEY_COL_8 66
```

`KEY_COL_8` 引脚复用功能（Pinmux Function）。

<a id="ad2c88795b1b458608caa083d469ee86e"></a>

### `BEE_KEY_COL_9`

```c
#define BEE_KEY_COL_9 67
```

`KEY_COL_9` 引脚复用功能（Pinmux Function）。

<a id="af82f5da17eada898f2dec8de92e603b0"></a>

### `BEE_KEY_ROW_0`

```c
#define BEE_KEY_ROW_0 78
```

`KEY_ROW_0` 引脚复用功能（Pinmux Function）。

<a id="a24e82e85a07c80d7e390185f67726756"></a>

### `BEE_KEY_ROW_1`

```c
#define BEE_KEY_ROW_1 79
```

`KEY_ROW_1` 引脚复用功能（Pinmux Function）。

<a id="a8f0c299784cb107d46fdbcd5494ae2f0"></a>

### `BEE_KEY_ROW_10`

```c
#define BEE_KEY_ROW_10 88
```

`KEY_ROW_10` 引脚复用功能（Pinmux Function）。

<a id="a2386911ec69b7416028fab5537243bee"></a>

### `BEE_KEY_ROW_11`

```c
#define BEE_KEY_ROW_11 89
```

`KEY_ROW_11` 引脚复用功能（Pinmux Function）。

<a id="a695da19fd7bc007959fe2ce9f3882939"></a>

### `BEE_KEY_ROW_2`

```c
#define BEE_KEY_ROW_2 80
```

`KEY_ROW_2` 引脚复用功能（Pinmux Function）。

<a id="a3920941b7c17c1eb9df377230ae0e3d7"></a>

### `BEE_KEY_ROW_3`

```c
#define BEE_KEY_ROW_3 81
```

`KEY_ROW_3` 引脚复用功能（Pinmux Function）。

<a id="a94ce3c3c0775437059fe8d48ca1ae63d"></a>

### `BEE_KEY_ROW_4`

```c
#define BEE_KEY_ROW_4 82
```

`KEY_ROW_4` 引脚复用功能（Pinmux Function）。

<a id="aebdb52372b88e9aa5d7173104f8088c7"></a>

### `BEE_KEY_ROW_5`

```c
#define BEE_KEY_ROW_5 83
```

`KEY_ROW_5` 引脚复用功能（Pinmux Function）。

<a id="a6535c3d5752c54dd36ff7a138cb70b5c"></a>

### `BEE_KEY_ROW_6`

```c
#define BEE_KEY_ROW_6 84
```

`KEY_ROW_6` 引脚复用功能（Pinmux Function）。

<a id="a4762128bf6b6e86a17b3c8c76ff2fc88"></a>

### `BEE_KEY_ROW_7`

```c
#define BEE_KEY_ROW_7 85
```

`KEY_ROW_7` 引脚复用功能（Pinmux Function）。

<a id="abbf110abd0ae22bb4767f28fe5901242"></a>

### `BEE_KEY_ROW_8`

```c
#define BEE_KEY_ROW_8 86
```

`KEY_ROW_8` 引脚复用功能（Pinmux Function）。

<a id="a681b30410bb04208c02a53f158dbedfb"></a>

### `BEE_KEY_ROW_9`

```c
#define BEE_KEY_ROW_9 87
```

`KEY_ROW_9` 引脚复用功能（Pinmux Function）。

<a id="a644fe132bc7a607b715744ae214635af"></a>

### `BEE_LRC_I_CODEC_SLAVE`

```c
#define BEE_LRC_I_CODEC_SLAVE 98
```

`LRC_I_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a44044eb50520f7a0dbf83abe70dc2bc5"></a>

### `BEE_LRC_SPORT0`

```c
#define BEE_LRC_SPORT0 123
```

`LRC_SPORT0` 引脚复用功能（Pinmux Function）。

<a id="a06c52f8460be70da0402f6e138985ad4"></a>

### `BEE_MCLK`

```c
#define BEE_MCLK 127
```

`MCLK` 引脚复用功能（Pinmux Function）。

<a id="a52116a87b4f4fd7ce6beeffbb44030da"></a>

### `BEE_PIN_DISCONNECTED`

```c
#define BEE_PIN_DISCONNECTED BEE_PIN_MSK
```

`PIN_DISCONNECTED` 引脚复用功能（Pinmux Function）。

<a id="a57b4629fefc1551701f145558e57f8fa"></a>

### `BEE_PINMUX_MAX`

```c
#define BEE_PINMUX_MAX (BEE_MCLK + 1)
```

`PINMUX_MAX` 引脚复用功能（Pinmux Function）。

<a id="aea3e0359b60d675d4fa8aca9d510810c"></a>

### `BEE_PSEL_GPIOA_0_P0_0`

```c
#define BEE_PSEL_GPIOA_0_P0_0 BEE_PSEL(DWGPIO, P0_0)
```

引脚（Pin）`P0_0` 对应的通用输入／输出（GPIO）为 `GPIOA_0`。

<a id="ac1eba0e039decabd2f41c8b58516b8ba"></a>

### `BEE_PSEL_GPIOA_10_H_0`

```c
#define BEE_PSEL_GPIOA_10_H_0 BEE_PSEL(DWGPIO, H_0)
```

引脚（Pin）`H_0` 对应的通用输入／输出（GPIO）为 `GPIOA_10`。

<a id="aa8347a5c9094390be062af3fc3fce746"></a>

### `BEE_PSEL_GPIOA_11_P1_3`

```c
#define BEE_PSEL_GPIOA_11_P1_3 BEE_PSEL(DWGPIO, P1_3)
```

引脚（Pin）`P1_3` 对应的通用输入／输出（GPIO）为 `GPIOA_11`。

<a id="a91df143d334eae24d1f8ff1cbc97fb78"></a>

### `BEE_PSEL_GPIOA_11_P5_1`

```c
#define BEE_PSEL_GPIOA_11_P5_1 BEE_PSEL(DWGPIO, P5_1)
```

引脚（Pin）`P5_1` 对应的通用输入／输出（GPIO）为 `GPIOA_11`。

<a id="af15b5bd2cdba62aac469dc0e7f34393f"></a>

### `BEE_PSEL_GPIOA_12_P1_4`

```c
#define BEE_PSEL_GPIOA_12_P1_4 BEE_PSEL(DWGPIO, P1_4)
```

引脚（Pin）`P1_4` 对应的通用输入／输出（GPIO）为 `GPIOA_12`。

<a id="a8f1dd2443ab15fbd599c12b10f0fd78d"></a>

### `BEE_PSEL_GPIOA_12_P5_2`

```c
#define BEE_PSEL_GPIOA_12_P5_2 BEE_PSEL(DWGPIO, P5_2)
```

引脚（Pin）`P5_2` 对应的通用输入／输出（GPIO）为 `GPIOA_12`。

<a id="a794b2ac5d4c63a07929368b61edb9a2a"></a>

### `BEE_PSEL_GPIOA_13_P4_0`

```c
#define BEE_PSEL_GPIOA_13_P4_0 BEE_PSEL(DWGPIO, P4_0)
```

引脚（Pin）`P4_0` 对应的通用输入／输出（GPIO）为 `GPIOA_13`。

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

<a id="a6d0af9f41c7f9b64b03c2d307691788b"></a>

### `BEE_PSEL_GPIOA_16_P2_0`

```c
#define BEE_PSEL_GPIOA_16_P2_0 BEE_PSEL(DWGPIO, P2_0)
```

引脚（Pin）`P2_0` 对应的通用输入／输出（GPIO）为 `GPIOA_16`。

<a id="a2bf034c47ca6517f8f2af9c01297f078"></a>

### `BEE_PSEL_GPIOA_17_P2_1`

```c
#define BEE_PSEL_GPIOA_17_P2_1 BEE_PSEL(DWGPIO, P2_1)
```

引脚（Pin）`P2_1` 对应的通用输入／输出（GPIO）为 `GPIOA_17`。

<a id="aa9cf9ff9afd6b7b48709419c2d2bf436"></a>

### `BEE_PSEL_GPIOA_18_P2_2`

```c
#define BEE_PSEL_GPIOA_18_P2_2 BEE_PSEL(DWGPIO, P2_2)
```

引脚（Pin）`P2_2` 对应的通用输入／输出（GPIO）为 `GPIOA_18`。

<a id="a5c5e07ed4ffb78c9e7b2efcf4352a862"></a>

### `BEE_PSEL_GPIOA_19_P2_3`

```c
#define BEE_PSEL_GPIOA_19_P2_3 BEE_PSEL(DWGPIO, P2_3)
```

引脚（Pin）`P2_3` 对应的通用输入／输出（GPIO）为 `GPIOA_19`。

<a id="a43339d36676fe5280317f760c1423ecd"></a>

### `BEE_PSEL_GPIOA_1_P0_1`

```c
#define BEE_PSEL_GPIOA_1_P0_1 BEE_PSEL(DWGPIO, P0_1)
```

引脚（Pin）`P0_1` 对应的通用输入／输出（GPIO）为 `GPIOA_1`。

<a id="a9e5898cc383851790bfeb0efbee7f7f0"></a>

### `BEE_PSEL_GPIOA_20_P2_4`

```c
#define BEE_PSEL_GPIOA_20_P2_4 BEE_PSEL(DWGPIO, P2_4)
```

引脚（Pin）`P2_4` 对应的通用输入／输出（GPIO）为 `GPIOA_20`。

<a id="ad1fe4429bc18a55f5d5ea3c94df1a9b3"></a>

### `BEE_PSEL_GPIOA_21_P2_5`

```c
#define BEE_PSEL_GPIOA_21_P2_5 BEE_PSEL(DWGPIO, P2_5)
```

引脚（Pin）`P2_5` 对应的通用输入／输出（GPIO）为 `GPIOA_21`。

<a id="a31be5e118e39e3ca09e7f33080e5d526"></a>

### `BEE_PSEL_GPIOA_22_P2_6`

```c
#define BEE_PSEL_GPIOA_22_P2_6 BEE_PSEL(DWGPIO, P2_6)
```

引脚（Pin）`P2_6` 对应的通用输入／输出（GPIO）为 `GPIOA_22`。

<a id="acf905757ae77f36fb5bc5e158287397c"></a>

### `BEE_PSEL_GPIOA_23_P2_7`

```c
#define BEE_PSEL_GPIOA_23_P2_7 BEE_PSEL(DWGPIO, P2_7)
```

引脚（Pin）`P2_7` 对应的通用输入／输出（GPIO）为 `GPIOA_23`。

<a id="aa37bdadc4a1904b625a485b5cdfd0271"></a>

### `BEE_PSEL_GPIOA_24_P3_0`

```c
#define BEE_PSEL_GPIOA_24_P3_0 BEE_PSEL(DWGPIO, P3_0)
```

引脚（Pin）`P3_0` 对应的通用输入／输出（GPIO）为 `GPIOA_24`。

<a id="abceea0402ce6c2786a62dc5f7f43dfb0"></a>

### `BEE_PSEL_GPIOA_25_P3_1`

```c
#define BEE_PSEL_GPIOA_25_P3_1 BEE_PSEL(DWGPIO, P3_1)
```

引脚（Pin）`P3_1` 对应的通用输入／输出（GPIO）为 `GPIOA_25`。

<a id="a27fea86f2884134d2298fdb5429ad278"></a>

### `BEE_PSEL_GPIOA_26_P3_2`

```c
#define BEE_PSEL_GPIOA_26_P3_2 BEE_PSEL(DWGPIO, P3_2)
```

引脚（Pin）`P3_2` 对应的通用输入／输出（GPIO）为 `GPIOA_26`。

<a id="a32c4f93dc6dce1978b9a036f8055f6fd"></a>

### `BEE_PSEL_GPIOA_27_P3_3`

```c
#define BEE_PSEL_GPIOA_27_P3_3 BEE_PSEL(DWGPIO, P3_3)
```

引脚（Pin）`P3_3` 对应的通用输入／输出（GPIO）为 `GPIOA_27`。

<a id="a9d5ab1788edfd9c617cb81a926cfa781"></a>

### `BEE_PSEL_GPIOA_28_P3_4`

```c
#define BEE_PSEL_GPIOA_28_P3_4 BEE_PSEL(DWGPIO, P3_4)
```

引脚（Pin）`P3_4` 对应的通用输入／输出（GPIO）为 `GPIOA_28`。

<a id="a9bccee519300ba03d2d95dde69877bc5"></a>

### `BEE_PSEL_GPIOA_29_P3_5`

```c
#define BEE_PSEL_GPIOA_29_P3_5 BEE_PSEL(DWGPIO, P3_5)
```

引脚（Pin）`P3_5` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="a7c0d91ef2df9f58a2d0654fc6ce9f49f"></a>

### `BEE_PSEL_GPIOA_29_P4_1`

```c
#define BEE_PSEL_GPIOA_29_P4_1 BEE_PSEL(DWGPIO, P4_1)
```

引脚（Pin）`P4_1` 对应的通用输入／输出（GPIO）为 `GPIOA_29`。

<a id="a26638afbd96b5b3b8355b0625fc24f19"></a>

### `BEE_PSEL_GPIOA_2_P0_2`

```c
#define BEE_PSEL_GPIOA_2_P0_2 BEE_PSEL(DWGPIO, P0_2)
```

引脚（Pin）`P0_2` 对应的通用输入／输出（GPIO）为 `GPIOA_2`。

<a id="ab3f859f908e1aeaa64b47b41ab0995c3"></a>

### `BEE_PSEL_GPIOA_30_P3_6`

```c
#define BEE_PSEL_GPIOA_30_P3_6 BEE_PSEL(DWGPIO, P3_6)
```

引脚（Pin）`P3_6` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="abf663addb6c2c9870416d59bba8d203f"></a>

### `BEE_PSEL_GPIOA_30_P4_2`

```c
#define BEE_PSEL_GPIOA_30_P4_2 BEE_PSEL(DWGPIO, P4_2)
```

引脚（Pin）`P4_2` 对应的通用输入／输出（GPIO）为 `GPIOA_30`。

<a id="ab3f3971ffa2d95180044d2715938df9f"></a>

### `BEE_PSEL_GPIOA_31_P4_3`

```c
#define BEE_PSEL_GPIOA_31_P4_3 BEE_PSEL(DWGPIO, P4_3)
```

引脚（Pin）`P4_3` 对应的通用输入／输出（GPIO）为 `GPIOA_31`。

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

<a id="abcf72b3e409c194ba2d2173aa7cb41ab"></a>

### `BEE_PTA_I2C_CLK_SLAVE`

```c
#define BEE_PTA_I2C_CLK_SLAVE 114
```

`PTA_I2C_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a9254d4dd1aa797f1590ef84c1cd07ed1"></a>

### `BEE_PTA_I2C_DAT_SLAVE`

```c
#define BEE_PTA_I2C_DAT_SLAVE 115
```

`PTA_I2C_DAT_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a2e6661f9ef9bb93179130a186653468a"></a>

### `BEE_PTA_I2C_INT_OUT`

```c
#define BEE_PTA_I2C_INT_OUT 116
```

`PTA_I2C_INT_OUT` 引脚复用功能（Pinmux Function）。

<a id="a38e2245a7c8035941a8e298da1ef2671"></a>

### `BEE_PWM2_N`

```c
#define BEE_PWM2_N 10
```

`PWM2_N` 引脚复用功能（Pinmux Function）。

<a id="a51f8a3a8d4572a1a9ffbdb0c894c006d"></a>

### `BEE_PWM2_P`

```c
#define BEE_PWM2_P 9
```

`PWM2_P` 引脚复用功能（Pinmux Function）。

<a id="a95eb489d18499ff7ce936149d65ff03e"></a>

### `BEE_PWR_OFF`

```c
#define BEE_PWR_OFF (BEE_PINMUX_MAX + 2)
```

`PWR_OFF` 引脚复用功能（Pinmux Function）。

<a id="aa8636b879c8e395d7605eb5922fa0e86"></a>

### `BEE_QDEC_PHASE_A_X`

```c
#define BEE_QDEC_PHASE_A_X 21
```

`QDEC_PHASE_A_X` 引脚复用功能（Pinmux Function）。

<a id="a63e4235f1eb0ca27ee6991facf896f3d"></a>

### `BEE_QDEC_PHASE_A_Y`

```c
#define BEE_QDEC_PHASE_A_Y 23
```

`QDEC_PHASE_A_Y` 引脚复用功能（Pinmux Function）。

<a id="a3edc0295f035c1ae7f45f2098ab67fa6"></a>

### `BEE_QDEC_PHASE_A_Z`

```c
#define BEE_QDEC_PHASE_A_Z 25
```

`QDEC_PHASE_A_Z` 引脚复用功能（Pinmux Function）。

<a id="a53614012c9764fab3f1c471b0c118cf6"></a>

### `BEE_QDEC_PHASE_B_X`

```c
#define BEE_QDEC_PHASE_B_X 22
```

`QDEC_PHASE_B_X` 引脚复用功能（Pinmux Function）。

<a id="a60f5251123c52966c512c8511cf79cea"></a>

### `BEE_QDEC_PHASE_B_Y`

```c
#define BEE_QDEC_PHASE_B_Y 24
```

`QDEC_PHASE_B_Y` 引脚复用功能（Pinmux Function）。

<a id="a463a58ed07f3016a8ebc54601b3e55e7"></a>

### `BEE_QDEC_PHASE_B_Z`

```c
#define BEE_QDEC_PHASE_B_Z 26
```

`QDEC_PHASE_B_Z` 引脚复用功能（Pinmux Function）。

<a id="a4210b1402742ed6b988925e93b2fb875"></a>

### `BEE_SDI_CODEC_SLAVE`

```c
#define BEE_SDI_CODEC_SLAVE 100
```

`SDI_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ad8fb809d69f74a7d77283fb004d2f323"></a>

### `BEE_SDO_CODEC_SLAVE`

```c
#define BEE_SDO_CODEC_SLAVE 101
```

`SDO_CODEC_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ab0446a74b1486abd14de4fd0200ea74f"></a>

### `BEE_SPI0_CLK_MASTER`

```c
#define BEE_SPI0_CLK_MASTER 50
```

`SPI0_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="aa74d6d5790ee4b6c3804612d13ac2b5b"></a>

### `BEE_SPI0_CLK_SLAVE`

```c
#define BEE_SPI0_CLK_SLAVE 46
```

`SPI0_CLK_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ad0da29a2b105520d4b082c3995738a7c"></a>

### `BEE_SPI0_MI_MASTER`

```c
#define BEE_SPI0_MI_MASTER 52
```

`SPI0_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="ae4d7727fa011b264c2262f8a93286b79"></a>

### `BEE_SPI0_MO_MASTER`

```c
#define BEE_SPI0_MO_MASTER 51
```

`SPI0_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a42c6b4ef4945aa8dacaf653acffae16f"></a>

### `BEE_SPI0_SI_SLAVE`

```c
#define BEE_SPI0_SI_SLAVE 48
```

`SPI0_SI_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="ad8b8f9abd4e3a9f468621a1bcebc26c5"></a>

### `BEE_SPI0_SO_SLAVE`

```c
#define BEE_SPI0_SO_SLAVE 47
```

`SPI0_SO_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="aa9f0e0c05f6bd5edc64378118ce90f37"></a>

### `BEE_SPI0_SS_N_0_MASTER`

```c
#define BEE_SPI0_SS_N_0_MASTER 49
```

`SPI0_SS_N_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a763d77602a1338c1c0e14d3647de7506"></a>

### `BEE_SPI0_SS_N_0_SLAVE`

```c
#define BEE_SPI0_SS_N_0_SLAVE 45
```

`SPI0_SS_N_0_SLAVE` 引脚复用功能（Pinmux Function）。

<a id="a0452a4a0d75d2f3eba6dac55bd4d209c"></a>

### `BEE_SPI1_CLK_MASTER`

```c
#define BEE_SPI1_CLK_MASTER 42
```

`SPI1_CLK_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a8064446640a0d1ff045af352b0da6670"></a>

### `BEE_SPI1_MI_MASTER`

```c
#define BEE_SPI1_MI_MASTER 44
```

`SPI1_MI_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a113270bda7f1996417ae86e9d59f7c6e"></a>

### `BEE_SPI1_MO_MASTER`

```c
#define BEE_SPI1_MO_MASTER 43
```

`SPI1_MO_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a705a65055475b386227a1dcb3b9857eb"></a>

### `BEE_SPI1_SS_N_0_MASTER`

```c
#define BEE_SPI1_SS_N_0_MASTER 39
```

`SPI1_SS_N_0_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a1aa1939165393b9db53353ca690581c9"></a>

### `BEE_SPI1_SS_N_1_MASTER`

```c
#define BEE_SPI1_SS_N_1_MASTER 40
```

`SPI1_SS_N_1_MASTER` 引脚复用功能（Pinmux Function）。

<a id="a9665f3e1942bcd7915e765ec9e5387a5"></a>

### `BEE_SPI1_SS_N_2_MASTER`

```c
#define BEE_SPI1_SS_N_2_MASTER 41
```

`SPI1_SS_N_2_MASTER` 引脚复用功能（Pinmux Function）。

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
#define BEE_SWD_CLK 56
```

`SWD_CLK` 引脚复用功能（Pinmux Function）。

<a id="a890a338c14aef5eb8e25844201b0289d"></a>

### `BEE_SWD_DIO`

```c
#define BEE_SWD_DIO 57
```

`SWD_DIO` 引脚复用功能（Pinmux Function）。

<a id="a07f2b36faf2fecad0359070176339d0e"></a>

### `BEE_TIM_PWM0`

```c
#define BEE_TIM_PWM0 13
```

`TIM_PWM0` 引脚复用功能（Pinmux Function）。

<a id="a5dd920c196c65cb5b8ee475e7e5264ca"></a>

### `BEE_TIM_PWM1`

```c
#define BEE_TIM_PWM1 14
```

`TIM_PWM1` 引脚复用功能（Pinmux Function）。

<a id="a3143f7811c5878701ee6da954a2ed74e"></a>

### `BEE_TIM_PWM2`

```c
#define BEE_TIM_PWM2 15
```

`TIM_PWM2` 引脚复用功能（Pinmux Function）。

<a id="abecec561a57f431e83e15a32109b4265"></a>

### `BEE_TIM_PWM3`

```c
#define BEE_TIM_PWM3 16
```

`TIM_PWM3` 引脚复用功能（Pinmux Function）。

<a id="ae8285702c1dc959039d162525cf06f76"></a>

### `BEE_TIM_PWM4`

```c
#define BEE_TIM_PWM4 17
```

`TIM_PWM4` 引脚复用功能（Pinmux Function）。

<a id="a185ffa8da5dfc0f6dcb68953ea60a117"></a>

### `BEE_TIM_PWM5`

```c
#define BEE_TIM_PWM5 18
```

`TIM_PWM5` 引脚复用功能（Pinmux Function）。

<a id="af5094e3bfde1cf22e80c9144763940cc"></a>

### `BEE_UART0_CTS`

```c
#define BEE_UART0_CTS 31
```

`UART0_CTS` 引脚复用功能（Pinmux Function）。

<a id="a6ea0a2599d172ee66154a55c6dad1544"></a>

### `BEE_UART0_RTS`

```c
#define BEE_UART0_RTS 32
```

`UART0_RTS` 引脚复用功能（Pinmux Function）。

<a id="a1c7070aee57aedc7f8a131fe34444d60"></a>

### `BEE_UART0_RX`

```c
#define BEE_UART0_RX 30
```

`UART0_RX` 引脚复用功能（Pinmux Function）。

<a id="aba42501ee83715ca6ea53df22183c5f6"></a>

### `BEE_UART0_TX`

```c
#define BEE_UART0_TX 29
```

`UART0_TX` 引脚复用功能（Pinmux Function）。

<a id="ae1a337884566b230fb35533cb45f83ba"></a>

### `BEE_UART1_CTS`

```c
#define BEE_UART1_CTS 37
```

`UART1_CTS` 引脚复用功能（Pinmux Function）。

<a id="abe24c85e1d8f04d29607669efb795a85"></a>

### `BEE_UART1_RTS`

```c
#define BEE_UART1_RTS 38
```

`UART1_RTS` 引脚复用功能（Pinmux Function）。

<a id="a360f04b358a9569940a03d0d19397df3"></a>

### `BEE_UART1_RX`

```c
#define BEE_UART1_RX 36
```

`UART1_RX` 引脚复用功能（Pinmux Function）。

<a id="acf789455a751381f67bb5c0d00144cee"></a>

### `BEE_UART1_TX`

```c
#define BEE_UART1_TX 35
```

`UART1_TX` 引脚复用功能（Pinmux Function）。

<a id="a7efdd2cc3bd5b3e9686ec52348490a21"></a>

### `BEE_UART2_CTS`

```c
#define BEE_UART2_CTS 3
```

`UART2_CTS` 引脚复用功能（Pinmux Function）。

<a id="a9c3102f61a4ea7d46a3b5bb363d8089d"></a>

### `BEE_UART2_RTS`

```c
#define BEE_UART2_RTS 4
```

`UART2_RTS` 引脚复用功能（Pinmux Function）。

<a id="ac0e9e9aae4c3a7542a4283525446151a"></a>

### `BEE_UART2_RX`

```c
#define BEE_UART2_RX 2
```

`UART2_RX` 引脚复用功能（Pinmux Function）。

<a id="a64c1b3bb3de7cbf46f5e15da73dd6af9"></a>

### `BEE_UART2_TX`

```c
#define BEE_UART2_TX 1
```

`UART2_TX` 引脚复用功能（Pinmux Function）。

<a id="a64a140ac19ea2cdcd9d586e68abe14ce"></a>

### `H_0`

```c
#define H_0 36
```

通用输入／输出 GPIO10／麦克风偏置（MICBIAS）。

<a id="a188735bd8812ee242324075c9cae4e0e"></a>

### `P0_0`

```c
#define P0_0 0
```

通用输入输出 0（GPIO0）。

<a id="a6e605c856305ec72ac000d8cc45ab0b9"></a>

### `P0_1`

```c
#define P0_1 1
```

通用输入输出 1（GPIO1）。

<a id="a876e3d0917cea9d0a75b2f6df2c3f1d4"></a>

### `P0_2`

```c
#define P0_2 2
```

引脚功能（Pin Function）：`GPIO2`。

<a id="ab73f15237a6f8860438ba0359b283686"></a>

### `P0_3`

```c
#define P0_3 3
```

引脚功能（Pin Function）：`GPIO3`。

<a id="a3218b7341a4f084375bade756f108940"></a>

### `P0_4`

```c
#define P0_4 4
```

引脚功能（Pin Function）：`GPIO4`。

<a id="aa1681f3dab52db87cd32f77b20352770"></a>

### `P0_5`

```c
#define P0_5 5
```

引脚功能（Pin Function）：`GPIO5`。

<a id="a990dc4ba08ec342d0bfa50f99d9e1868"></a>

### `P0_6`

```c
#define P0_6 6
```

引脚功能（Pin Function）：`GPIO6`。

<a id="a34087bca5283adcf7cc7c810f30eab80"></a>

### `P0_7`

```c
#define P0_7 7
```

引脚功能（Pin Function）：`GPIO7`。

<a id="a0a5c0ef038f9728173ca136eed5c9cd2"></a>

### `P1_0`

```c
#define P1_0 8
```

通用输入／输出（GPIO）：`GPIO8`。

<a id="aa7c3cebcd9dc4598bb69e51ecee85bd0"></a>

### `P1_1`

```c
#define P1_1 9
```

通用输入／输出（GPIO）：`GPIO9`。

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

<a id="a9e219f75c65aa5b19d59bd1596b3e548"></a>

### `P1_6`

```c
#define P1_6 14
```

GPIO14 引脚。

<a id="a59e6507c1874213b84ae809c24c3a76e"></a>

### `P1_7`

```c
#define P1_7 15
```

GPIO15 引脚。

<a id="a5b005e989c9ae92562196f830232dc1a"></a>

### `P2_0`

```c
#define P2_0 16
```

通用输入／输出（GPIO）：`GPIO16`。

<a id="aaae6a77f4b93ec74cb11947217dd8fd1"></a>

### `P2_1`

```c
#define P2_1 17
```

通用输入／输出（GPIO）：`GPIO17`。

<a id="a9216eb7ac06cf1906b8c3e6884943b5e"></a>

### `P2_2`

```c
#define P2_2 18
```

通用输入／输出（GPIO）：`GPIO18`。

<a id="a98005d211f8692aa984d81e1b1cefd67"></a>

### `P2_3`

```c
#define P2_3 19
```

通用输入／输出（GPIO）：`GPIO19`。

<a id="a541f1278e79f6ce8b83f48b5f3e1c177"></a>

### `P2_4`

```c
#define P2_4 20
```

通用输入／输出（GPIO）：`GPIO20`。

<a id="acf47cd715ad993d583a85ef8fcac6b3e"></a>

### `P2_5`

```c
#define P2_5 21
```

通用输入／输出（GPIO）：`GPIO21`。

<a id="aaf264201304e2d44dc57b61eaf041654"></a>

### `P2_6`

```c
#define P2_6 22
```

通用输入／输出（GPIO）：`GPIO22`。

<a id="a4f3e81fec0b7d90e9ff61bae35882c8a"></a>

### `P2_7`

```c
#define P2_7 23
```

通用输入／输出（GPIO）：`GPIO23`。

<a id="a335073a6b45e1affb80cb03be0aebd28"></a>

### `P3_0`

```c
#define P3_0 24
```

通用输入／输出（GPIO）：`GPIO24`。

<a id="aa56aef7e8461bcefa151ed84ab438dd9"></a>

### `P3_1`

```c
#define P3_1 25
```

通用输入／输出（GPIO）：`GPIO25`。

<a id="a7060bd469f1a43b0d5c130d35f291687"></a>

### `P3_2`

```c
#define P3_2 26
```

通用输入／输出（GPIO）：`GPIO26`。

<a id="a3394fd21eaccbcd6bfb4cc9a20a93f63"></a>

### `P3_3`

```c
#define P3_3 27
```

通用输入／输出（GPIO）：`GPIO27`。

<a id="a444f7e1de792cb878057f9fedf8c1e92"></a>

### `P3_4`

```c
#define P3_4 28
```

通用输入／输出（GPIO）：`GPIO28`。

<a id="add5e9628720a9e18e34d148c5e4386ae"></a>

### `P3_5`

```c
#define P3_5 29
```

通用输入／输出（GPIO）：`GPIO29`。

<a id="a5f901ec132df36067c1aebb4f0f5e99e"></a>

### `P3_6`

```c
#define P3_6 30
```

通用输入／输出（GPIO）：`GPIO30`。

<a id="a7d02796f1733eadcc315008ac83e939a"></a>

### `P4_0`

```c
#define P4_0 32
```

通用输入／输出（GPIO）：`GPIO13`。

<a id="adbc665f56899cd3fa782adc76a77087f"></a>

### `P4_1`

```c
#define P4_1 33
```

通用输入／输出（GPIO）：`GPIO29`。

<a id="aef67ce6b9c7f16a266927b0545631bc2"></a>

### `P4_2`

```c
#define P4_2 34
```

通用输入／输出（GPIO）：`GPIO30`。

<a id="a57a1bc2364d61983bdf84d6e8a7cda5b"></a>

### `P4_3`

```c
#define P4_3 35
```

通用输入／输出（GPIO）：`GPIO31`。

<a id="aaec8c9b05d0535f709f9e40ededd5ae8"></a>

### `P5_1`

```c
#define P5_1 37
```

通用输入／输出（GPIO）：`GPIO11`。

<a id="ae908c3f54860d6e0d70a10bbc5b19aae"></a>

### `P5_2`

```c
#define P5_2 38
```

通用输入／输出（GPIO）：`GPIO12`。


## 5.3\_原页交叉引用（Cross References）

- [bee-pinctrl.h](../api_source_reference/P057_bee-pinctrl.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P017_rtl8752h-pinctrl.h_源码浏览.md)
- [BEE_PIN_MSK](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a8514aca71581788b4e134f74d81bcd45)
- [BEE_PSEL](../api_file_network_device_reference/P002_zephyr__dt-bindings__pinctrl__bee-pinctrl.h_文件参考.md#a162b03456c93d6efa3bfaa0a6a996e15)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__dt-bindings__dma__renesas_rza2m_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__dt-bindings__pinctrl__rtl87x2g-pinctrl.h_文件参考.md)
