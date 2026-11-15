---
id: learning.zephyr-docs.api-file-gap-modem-reference.page-6
title: zephyr__dt-bindings__pinctrl__stm32f1-afio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_stm32f1-afio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32f1-afio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.1\_宏定义（Macros）

<a id="r_ade5f8ba7372fa491075880f76e550b6c"></a>

```c
#define STM32_REMAP_REG_MASK 0x1U
```

相关声明：[STM32_REMAP_REG_MASK](#ade5f8ba7372fa491075880f76e550b6c)。

<a id="r_acbb01f8e98a95fe5460465e4ca2ba3e0"></a>

```c
#define STM32_REMAP_REG_SHIFT 0U
```

相关声明：[STM32_REMAP_REG_SHIFT](#acbb01f8e98a95fe5460465e4ca2ba3e0)。

<a id="r_a3cebc2d1cda7877f745ea12092794223"></a>

```c
#define STM32_REMAP_SHIFT_MASK 0x1FU
```

相关声明：[STM32_REMAP_SHIFT_MASK](#a3cebc2d1cda7877f745ea12092794223)。

<a id="r_a1e14e8db39fbc3e33132adc10ad7067d"></a>

```c
#define STM32_REMAP_SHIFT_SHIFT 1U
```

相关声明：[STM32_REMAP_SHIFT_SHIFT](#a1e14e8db39fbc3e33132adc10ad7067d)。

<a id="r_a6e9613bf8369a7d1efa96cb90345a97a"></a>

```c
#define STM32_REMAP_MASK_MASK 0x3U
```

相关声明：[STM32_REMAP_MASK_MASK](#a6e9613bf8369a7d1efa96cb90345a97a)。

<a id="r_a3ffdee2c3eb7a004285180731366c15d"></a>

```c
#define STM32_REMAP_MASK_SHIFT 6U
```

相关声明：[STM32_REMAP_MASK_SHIFT](#a3ffdee2c3eb7a004285180731366c15d)。

<a id="r_a9cb1b934dd4621ebfae5115459efbd6e"></a>

```c
#define STM32_REMAP_VAL_MASK 0x3U
```

相关声明：[STM32_REMAP_VAL_MASK](#a9cb1b934dd4621ebfae5115459efbd6e)。

<a id="r_a144bfbe208a98ddc641ff538aa4738cc"></a>

```c
#define STM32_REMAP_VAL_SHIFT 8U
```

相关声明：[STM32_REMAP_VAL_SHIFT](#a144bfbe208a98ddc641ff538aa4738cc)。

<a id="r_a200a3a748707c11bfd3129c16fc6a835"></a>

```c
#define STM32_REMAP(val, mask, shift, reg)
```

相关声明：[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)。

STM32F1 重映射配置位字段（Remap Configuration Bit Field）。

<a id="r_a9d21e2ff45da0e873e6c8d1012c001f5"></a>

```c
#define STM32_REMAP_REG_GET(remap)
```

相关声明：[STM32_REMAP_REG_GET](#a9d21e2ff45da0e873e6c8d1012c001f5)。

从重映射配置（Remap Configuration）中取得寄存器字段（Register Field）。

<a id="r_a7a61290a7587f5680a8ff183d1c2907d"></a>

```c
#define STM32_REMAP_SHIFT_GET(remap)
```

相关声明：[STM32_REMAP_SHIFT_GET](#a7a61290a7587f5680a8ff183d1c2907d)。

从重映射配置（Remap Configuration）中取得位置字段（Position Field）。

<a id="r_a71aeec8660001f84d3c55f426fdb7137"></a>

```c
#define STM32_REMAP_MASK_GET(remap)
```

相关声明：[STM32_REMAP_MASK_GET](#a71aeec8660001f84d3c55f426fdb7137)。

从重映射配置（Remap Configuration）中取得掩码字段（Mask Field）。

<a id="r_a60b741decc8673b9f9a99b7a05d5e9fc"></a>

```c
#define STM32_REMAP_VAL_GET(remap)
```

相关声明：[STM32_REMAP_VAL_GET](#a60b741decc8673b9f9a99b7a05d5e9fc)。

从重映射配置（Remap Configuration）中取得值字段（Value Field）。

<a id="r_a2c91303d8a35d5fcbfa8621173d3fe07"></a>

```c
#define STM32_AFIO_MAPR 0U
```

相关声明：[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

<a id="r_aa60a0ba8748fc37c64efcd19947e664e"></a>

```c
#define STM32_AFIO_MAPR2 1U
```

相关声明：[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

<a id="r_a1a8dfdc80d2d337f72699eca6ed3d957"></a>

```c
#define NO_REMAP 0
```

相关声明：[NO_REMAP](#a1a8dfdc80d2d337f72699eca6ed3d957)。

设备不支持重映射（Not Remappable）。

<a id="r_ae6f376590d4b2ec77260306a119ad235"></a>

```c
#define SPI1_REMAP0 STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR)
```

相关声明：[SPI1_REMAP0](#ae6f376590d4b2ec77260306a119ad235)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

SPI1，无重映射（no remap）。

<a id="r_ab655e58c31c71abbecb333cc6f91d9c4"></a>

```c
#define SPI1_REMAP1 STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR)
```

相关声明：[SPI1_REMAP1](#ab655e58c31c71abbecb333cc6f91d9c4)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

SPI1，重映射（remap）。

<a id="r_ad235d9e97ed9df493d76cd77f70ca951"></a>

```c
#define I2C1_REMAP0 STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR)
```

相关声明：[I2C1_REMAP0](#ad235d9e97ed9df493d76cd77f70ca951)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

I2C1，无重映射（no remap）。

<a id="r_a312613c6dc75976919fec8f63fcb2010"></a>

```c
#define I2C1_REMAP1 STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR)
```

相关声明：[I2C1_REMAP1](#a312613c6dc75976919fec8f63fcb2010)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

I2C1，重映射（remap）。

<a id="r_a5a79382b9eb0e4e502b8c84697a73433"></a>

```c
#define USART1_REMAP0 STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR)
```

相关声明：[USART1_REMAP0](#a5a79382b9eb0e4e502b8c84697a73433)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART1，无重映射（no remap）。

<a id="r_ab002c165fc3d6a9e043164560a211f68"></a>

```c
#define USART1_REMAP1 STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR)
```

相关声明：[USART1_REMAP1](#ab002c165fc3d6a9e043164560a211f68)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART1，重映射（remap）。

<a id="r_afd7dc4010b32a1f10510cc39e1c911da"></a>

```c
#define USART2_REMAP0 STM32_REMAP(0U, 0x1U, 3U, STM32_AFIO_MAPR)
```

相关声明：[USART2_REMAP0](#afd7dc4010b32a1f10510cc39e1c911da)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART2，无重映射（no remap）。

<a id="r_a472167bf97fff0caba80fe06a56b8084"></a>

```c
#define USART2_REMAP1 STM32_REMAP(1U, 0x1U, 3U, STM32_AFIO_MAPR)
```

相关声明：[USART2_REMAP1](#a472167bf97fff0caba80fe06a56b8084)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART2，重映射（remap）。

<a id="r_a45b45e1ad6629299c0efd15b2233cd0e"></a>

```c
#define USART3_REMAP0 STM32_REMAP(0U, 0x3U, 4U, STM32_AFIO_MAPR)
```

相关声明：[USART3_REMAP0](#a45b45e1ad6629299c0efd15b2233cd0e)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART3，无重映射（no remap）。

<a id="r_a3953583002841a586c85cbbb5d5fc931"></a>

```c
#define USART3_REMAP1 STM32_REMAP(1U, 0x3U, 4U, STM32_AFIO_MAPR)
```

相关声明：[USART3_REMAP1](#a3953583002841a586c85cbbb5d5fc931)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART3，部分重映射（partial remap）。

<a id="r_a9642c16b4169ed0552056f8ee638ceb2"></a>

```c
#define USART3_REMAP2 STM32_REMAP(3U, 0x3U, 4U, STM32_AFIO_MAPR)
```

相关声明：[USART3_REMAP2](#a9642c16b4169ed0552056f8ee638ceb2)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

USART3，完全重映射（full remap）。

<a id="r_a65b1a18a202a22d8c9add530fd0a8313"></a>

```c
#define TIM1_REMAP0 STM32_REMAP(0U, 0x3U, 6U, STM32_AFIO_MAPR)
```

相关声明：[TIM1_REMAP0](#a65b1a18a202a22d8c9add530fd0a8313)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM1，无重映射（no remap）。

<a id="r_aa7a6c64fab50803704cfc5f6a3fe4c9f"></a>

```c
#define TIM1_REMAP1 STM32_REMAP(1U, 0x3U, 6U, STM32_AFIO_MAPR)
```

相关声明：[TIM1_REMAP1](#aa7a6c64fab50803704cfc5f6a3fe4c9f)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM1，部分重映射（partial remap）。

<a id="r_a8de28395b1ecc659fbe3e4b33a8aaf76"></a>

```c
#define TIM1_REMAP2 STM32_REMAP(3U, 0x3U, 6U, STM32_AFIO_MAPR)
```

相关声明：[TIM1_REMAP2](#a8de28395b1ecc659fbe3e4b33a8aaf76)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM1，完全重映射（full remap）。

<a id="r_a9ac0bc54a91246b78d863ba3a215ea96"></a>

```c
#define TIM2_REMAP0 STM32_REMAP(0U, 0x3U, 8U, STM32_AFIO_MAPR)
```

相关声明：[TIM2_REMAP0](#a9ac0bc54a91246b78d863ba3a215ea96)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM2，无重映射（no remap）。

<a id="r_a6fad8ce0389fa7b6d5a80c501ed99ce9"></a>

```c
#define TIM2_REMAP1 STM32_REMAP(1U, 0x3U, 8U, STM32_AFIO_MAPR)
```

相关声明：[TIM2_REMAP1](#a6fad8ce0389fa7b6d5a80c501ed99ce9)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM2，部分重映射 1（partial remap 1）。

<a id="r_ae47bd66bc1f02dc89a624c7639ad492b"></a>

```c
#define TIM2_REMAP2 STM32_REMAP(2U, 0x3U, 8U, STM32_AFIO_MAPR)
```

相关声明：[TIM2_REMAP2](#ae47bd66bc1f02dc89a624c7639ad492b)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM2，部分重映射 2（partial remap 2）。

<a id="r_ae3739bffc6fef7ca2aed06327fe26259"></a>

```c
#define TIM2_REMAP3 STM32_REMAP(3U, 0x3U, 8U, STM32_AFIO_MAPR)
```

相关声明：[TIM2_REMAP3](#ae3739bffc6fef7ca2aed06327fe26259)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM2，完全重映射（full remap）。

<a id="r_a535bdd60f1276bf660814c665c3ca349"></a>

```c
#define TIM3_REMAP0 STM32_REMAP(0U, 0x3U, 10U, STM32_AFIO_MAPR)
```

相关声明：[TIM3_REMAP0](#a535bdd60f1276bf660814c665c3ca349)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM3，无重映射（no remap）。

<a id="r_a068f135e7a2273b9eab28b934b0a7e53"></a>

```c
#define TIM3_REMAP1 STM32_REMAP(1U, 0x3U, 10U, STM32_AFIO_MAPR)
```

相关声明：[TIM3_REMAP1](#a068f135e7a2273b9eab28b934b0a7e53)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM3，部分重映射 1（partial remap 1）。

<a id="r_a5c8aa22a44a0b6ef2fbc169aeebdc2ea"></a>

```c
#define TIM3_REMAP2 STM32_REMAP(2U, 0x3U, 10U, STM32_AFIO_MAPR)
```

相关声明：[TIM3_REMAP2](#a5c8aa22a44a0b6ef2fbc169aeebdc2ea)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM3，部分重映射 2（partial remap 2）。

<a id="r_a811f621a99ec1b18a4b5fd4e52456a9f"></a>

```c
#define TIM3_REMAP3 STM32_REMAP(3U, 0x3U, 10U, STM32_AFIO_MAPR)
```

相关声明：[TIM3_REMAP3](#a811f621a99ec1b18a4b5fd4e52456a9f)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM3，完全重映射（full remap）。

<a id="r_af19b67747576ad37c76dccc4c8a1ea16"></a>

```c
#define TIM4_REMAP0 STM32_REMAP(0U, 0x1U, 12U, STM32_AFIO_MAPR)
```

相关声明：[TIM4_REMAP0](#af19b67747576ad37c76dccc4c8a1ea16)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM4，无重映射（no remap）。

<a id="r_aafb51d9eacaf920f3c78425ecaf5478e"></a>

```c
#define TIM4_REMAP1 STM32_REMAP(1U, 0x1U, 12U, STM32_AFIO_MAPR)
```

相关声明：[TIM4_REMAP1](#aafb51d9eacaf920f3c78425ecaf5478e)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

TIM4，重映射（remap）。

<a id="r_a6e8abc893ec0c03751427ff220eaf34a"></a>

```c
#define CAN_REMAP0 STM32_REMAP(0U, 0x3U, 13U, STM32_AFIO_MAPR)
```

相关声明：[CAN_REMAP0](#a6e8abc893ec0c03751427ff220eaf34a)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

CAN，无重映射（no remap）。

<a id="r_a20407640b3d6f5a1c326546a8b3a10e9"></a>

```c
#define CAN_REMAP1 STM32_REMAP(2U, 0x3U, 13U, STM32_AFIO_MAPR)
```

相关声明：[CAN_REMAP1](#a20407640b3d6f5a1c326546a8b3a10e9)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

CAN，部分重映射（partial remap）。

<a id="r_aa1aaf1eeddccdbfd3621145c709dc48d"></a>

```c
#define CAN_REMAP2 STM32_REMAP(3U, 0x3U, 13U, STM32_AFIO_MAPR)
```

相关声明：[CAN_REMAP2](#aa1aaf1eeddccdbfd3621145c709dc48d)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

CAN，完全重映射（full remap）。

<a id="r_a536898ad320fddd9754cca453f1b9223"></a>

```c
#define CAN1_REMAP0 CAN_REMAP0
```

相关声明：[CAN1_REMAP0](#a536898ad320fddd9754cca453f1b9223)、[CAN_REMAP0](#a6e8abc893ec0c03751427ff220eaf34a)。

CAN1 别名（Alias）。

<a id="r_a5b032fc54211b2ac4964bc924f09a75d"></a>

```c
#define CAN1_REMAP1 CAN_REMAP1
```

相关声明：[CAN1_REMAP1](#a5b032fc54211b2ac4964bc924f09a75d)、[CAN_REMAP1](#a20407640b3d6f5a1c326546a8b3a10e9)。

<a id="r_ab16bbfb04e8b2b73bdd560a9a14c4df1"></a>

```c
#define CAN1_REMAP2 CAN_REMAP2
```

相关声明：[CAN1_REMAP2](#ab16bbfb04e8b2b73bdd560a9a14c4df1)、[CAN_REMAP2](#aa1aaf1eeddccdbfd3621145c709dc48d)。

<a id="r_a663f8f668fe27ac44a70990db3d19a40"></a>

```c
#define ETH_REMAP0 STM32_REMAP(0U, 0x1U, 21U, STM32_AFIO_MAPR)
```

相关声明：[ETH_REMAP0](#a663f8f668fe27ac44a70990db3d19a40)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

ETH，无重映射（no remap）。

<a id="r_abcf6340d39300d1c33b0592160614de9"></a>

```c
#define ETH_REMAP1 STM32_REMAP(1U, 0x1U, 21U, STM32_AFIO_MAPR)
```

相关声明：[ETH_REMAP1](#abcf6340d39300d1c33b0592160614de9)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

ETH，重映射（remap）。

<a id="r_a1c2991b25909c6297e22542cfa418548"></a>

```c
#define CAN2_REMAP0 STM32_REMAP(0U, 0x1U, 22U, STM32_AFIO_MAPR)
```

相关声明：[CAN2_REMAP0](#a1c2991b25909c6297e22542cfa418548)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

CAN2，无重映射（no remap）。

<a id="r_aa048c7e4fb84a22c8ad40e9c0fc5e51a"></a>

```c
#define CAN2_REMAP1 STM32_REMAP(1U, 0x1U, 22U, STM32_AFIO_MAPR)
```

相关声明：[CAN2_REMAP1](#aa048c7e4fb84a22c8ad40e9c0fc5e51a)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

CAN2，重映射（remap）。

<a id="r_a7dcb5bfc48d08c9d4dbe793b8d232a45"></a>

```c
#define SPI3_REMAP0 STM32_REMAP(0U, 0x1U, 28U, STM32_AFIO_MAPR)
```

相关声明：[SPI3_REMAP0](#a7dcb5bfc48d08c9d4dbe793b8d232a45)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

SPI3，无重映射（no remap）。

<a id="r_a401e4124c07719248294b0ee08ebc83c"></a>

```c
#define SPI3_REMAP1 STM32_REMAP(1U, 0x1U, 28U, STM32_AFIO_MAPR)
```

相关声明：[SPI3_REMAP1](#a401e4124c07719248294b0ee08ebc83c)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR](#a2c91303d8a35d5fcbfa8621173d3fe07)。

SPI3，重映射（remap）。

<a id="r_ac3b499810e4bcae2211adb6c02eb7815"></a>

```c
#define I2S3_REMAP0 SPI3_REMAP0
```

相关声明：[I2S3_REMAP0](#ac3b499810e4bcae2211adb6c02eb7815)、[SPI3_REMAP0](#a7dcb5bfc48d08c9d4dbe793b8d232a45)。

I2S3 (SPI3)，无重映射（no remap）。

<a id="r_a47c88171fa34dbd74f7c163a9227ae28"></a>

```c
#define I2S3_REMAP1 SPI3_REMAP1
```

相关声明：[I2S3_REMAP1](#a47c88171fa34dbd74f7c163a9227ae28)、[SPI3_REMAP1](#a401e4124c07719248294b0ee08ebc83c)。

I2S3 (SPI3)，重映射（remap）。

<a id="r_a075dc7fea001772986dfe31d9d9e8f9a"></a>

```c
#define TIM9_REMAP0 STM32_REMAP(0U, 0x1U, 5U, STM32_AFIO_MAPR2)
```

相关声明：[TIM9_REMAP0](#a075dc7fea001772986dfe31d9d9e8f9a)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM9，无重映射（no remap）。

<a id="r_ad443ec934247e04996bf85b5ce9ef721"></a>

```c
#define TIM9_REMAP1 STM32_REMAP(1U, 0x1U, 5U, STM32_AFIO_MAPR2)
```

相关声明：[TIM9_REMAP1](#ad443ec934247e04996bf85b5ce9ef721)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM9，重映射（remap）。

<a id="r_af5450df359cf37725a34f89b1af168e7"></a>

```c
#define TIM10_REMAP0 STM32_REMAP(0U, 0x1U, 6U, STM32_AFIO_MAPR2)
```

相关声明：[TIM10_REMAP0](#af5450df359cf37725a34f89b1af168e7)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM10，无重映射（no remap）。

<a id="r_a691a581fe6dd08fd9a5a048abc5eaa3e"></a>

```c
#define TIM10_REMAP1 STM32_REMAP(1U, 0x1U, 6U, STM32_AFIO_MAPR2)
```

相关声明：[TIM10_REMAP1](#a691a581fe6dd08fd9a5a048abc5eaa3e)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM10，重映射（remap）。

<a id="r_a01e4adf5326f92d144d45ba4b898ed8e"></a>

```c
#define TIM11_REMAP0 STM32_REMAP(0U, 0x1U, 7U, STM32_AFIO_MAPR2)
```

相关声明：[TIM11_REMAP0](#a01e4adf5326f92d144d45ba4b898ed8e)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM11，无重映射（no remap）。

<a id="r_a7dcef4a23add63b6eb1254e6146dbe71"></a>

```c
#define TIM11_REMAP1 STM32_REMAP(1U, 0x1U, 7U, STM32_AFIO_MAPR2)
```

相关声明：[TIM11_REMAP1](#a7dcef4a23add63b6eb1254e6146dbe71)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM11，重映射（remap）。

<a id="r_a2a6704eee24037ee9edd3873a5245ea0"></a>

```c
#define TIM13_REMAP0 STM32_REMAP(0U, 0x1U, 8U, STM32_AFIO_MAPR2)
```

相关声明：[TIM13_REMAP0](#a2a6704eee24037ee9edd3873a5245ea0)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM13，无重映射（no remap）。

<a id="r_acdcdd0184a5d75722dd1cbdbe2f8212f"></a>

```c
#define TIM13_REMAP1 STM32_REMAP(1U, 0x1U, 8U, STM32_AFIO_MAPR2)
```

相关声明：[TIM13_REMAP1](#acdcdd0184a5d75722dd1cbdbe2f8212f)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM13，重映射（remap）。

<a id="r_a6c0341b14e851b4093e72932d05de5f5"></a>

```c
#define TIM14_REMAP0 STM32_REMAP(0U, 0x1U, 9U, STM32_AFIO_MAPR2)
```

相关声明：[TIM14_REMAP0](#a6c0341b14e851b4093e72932d05de5f5)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM14，无重映射（no remap）。

<a id="r_ab047fa455523413d447f676fe9907c84"></a>

```c
#define TIM14_REMAP1 STM32_REMAP(1U, 0x1U, 9U, STM32_AFIO_MAPR2)
```

相关声明：[TIM14_REMAP1](#ab047fa455523413d447f676fe9907c84)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM14，重映射（remap）。

<a id="r_aa7da41d73e1ab29fef6020695f32f773"></a>

```c
#define TIM15_REMAP0 STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR2)
```

相关声明：[TIM15_REMAP0](#aa7da41d73e1ab29fef6020695f32f773)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM15，无重映射（no remap）。

<a id="r_a87f392ac52f61d12709744f1ae8470af"></a>

```c
#define TIM15_REMAP1 STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR2)
```

相关声明：[TIM15_REMAP1](#a87f392ac52f61d12709744f1ae8470af)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM15，重映射（remap）。

<a id="r_a26d271515c8666e49cff39a1e5bb8112"></a>

```c
#define TIM16_REMAP0 STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR2)
```

相关声明：[TIM16_REMAP0](#a26d271515c8666e49cff39a1e5bb8112)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM16，无重映射（no remap）。

<a id="r_a9459d0003315751cc5969c7ce1146947"></a>

```c
#define TIM16_REMAP1 STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR2)
```

相关声明：[TIM16_REMAP1](#a9459d0003315751cc5969c7ce1146947)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM16，重映射（remap）。

<a id="r_a0c0e509d60821ac498a4fa03c4d5a47b"></a>

```c
#define TIM17_REMAP0 STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR2)
```

相关声明：[TIM17_REMAP0](#a0c0e509d60821ac498a4fa03c4d5a47b)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM17，无重映射（no remap）。

<a id="r_ae5da6d9ae0c81a39ba7c7f51135be110"></a>

```c
#define TIM17_REMAP1 STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR2)
```

相关声明：[TIM17_REMAP1](#ae5da6d9ae0c81a39ba7c7f51135be110)、[STM32_REMAP](#a200a3a748707c11bfd3129c16fc6a835)、[STM32_AFIO_MAPR2](#aa60a0ba8748fc37c64efcd19947e664e)。

TIM17，重映射（remap）。

## 6.2\_详细说明（Detailed Documentation）

<a id="a536898ad320fddd9754cca453f1b9223"></a>

### `CAN1_REMAP0`

```c
#define CAN1_REMAP0 CAN_REMAP0
```

CAN1 别名（Alias）。

<a id="a5b032fc54211b2ac4964bc924f09a75d"></a>

### `CAN1_REMAP1`

```c
#define CAN1_REMAP1 CAN_REMAP1
```

<a id="ab16bbfb04e8b2b73bdd560a9a14c4df1"></a>

### `CAN1_REMAP2`

```c
#define CAN1_REMAP2 CAN_REMAP2
```

<a id="a1c2991b25909c6297e22542cfa418548"></a>

### `CAN2_REMAP0`

```c
#define CAN2_REMAP0 STM32_REMAP(0U, 0x1U, 22U, STM32_AFIO_MAPR)
```

CAN2，无重映射（no remap）。

<a id="aa048c7e4fb84a22c8ad40e9c0fc5e51a"></a>

### `CAN2_REMAP1`

```c
#define CAN2_REMAP1 STM32_REMAP(1U, 0x1U, 22U, STM32_AFIO_MAPR)
```

CAN2，重映射（remap）。

<a id="a6e8abc893ec0c03751427ff220eaf34a"></a>

### `CAN_REMAP0`

```c
#define CAN_REMAP0 STM32_REMAP(0U, 0x3U, 13U, STM32_AFIO_MAPR)
```

CAN，无重映射（no remap）。

<a id="a20407640b3d6f5a1c326546a8b3a10e9"></a>

### `CAN_REMAP1`

```c
#define CAN_REMAP1 STM32_REMAP(2U, 0x3U, 13U, STM32_AFIO_MAPR)
```

CAN，部分重映射（partial remap）。

<a id="aa1aaf1eeddccdbfd3621145c709dc48d"></a>

### `CAN_REMAP2`

```c
#define CAN_REMAP2 STM32_REMAP(3U, 0x3U, 13U, STM32_AFIO_MAPR)
```

CAN，完全重映射（full remap）。

<a id="a663f8f668fe27ac44a70990db3d19a40"></a>

### `ETH_REMAP0`

```c
#define ETH_REMAP0 STM32_REMAP(0U, 0x1U, 21U, STM32_AFIO_MAPR)
```

ETH，无重映射（no remap）。

<a id="abcf6340d39300d1c33b0592160614de9"></a>

### `ETH_REMAP1`

```c
#define ETH_REMAP1 STM32_REMAP(1U, 0x1U, 21U, STM32_AFIO_MAPR)
```

ETH，重映射（remap）。

<a id="ad235d9e97ed9df493d76cd77f70ca951"></a>

### `I2C1_REMAP0`

```c
#define I2C1_REMAP0 STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR)
```

I2C1，无重映射（no remap）。

<a id="a312613c6dc75976919fec8f63fcb2010"></a>

### `I2C1_REMAP1`

```c
#define I2C1_REMAP1 STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR)
```

I2C1，重映射（remap）。

<a id="ac3b499810e4bcae2211adb6c02eb7815"></a>

### `I2S3_REMAP0`

```c
#define I2S3_REMAP0 SPI3_REMAP0
```

I2S3 (SPI3)，无重映射（no remap）。

<a id="a47c88171fa34dbd74f7c163a9227ae28"></a>

### `I2S3_REMAP1`

```c
#define I2S3_REMAP1 SPI3_REMAP1
```

I2S3 (SPI3)，重映射（remap）。

<a id="a1a8dfdc80d2d337f72699eca6ed3d957"></a>

### `NO_REMAP`

```c
#define NO_REMAP 0
```

设备不支持重映射（Not Remappable）。

<a id="ae6f376590d4b2ec77260306a119ad235"></a>

### `SPI1_REMAP0`

```c
#define SPI1_REMAP0 STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR)
```

SPI1，无重映射（no remap）。

<a id="ab655e58c31c71abbecb333cc6f91d9c4"></a>

### `SPI1_REMAP1`

```c
#define SPI1_REMAP1 STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR)
```

SPI1，重映射（remap）。

<a id="a7dcb5bfc48d08c9d4dbe793b8d232a45"></a>

### `SPI3_REMAP0`

```c
#define SPI3_REMAP0 STM32_REMAP(0U, 0x1U, 28U, STM32_AFIO_MAPR)
```

SPI3，无重映射（no remap）。

<a id="a401e4124c07719248294b0ee08ebc83c"></a>

### `SPI3_REMAP1`

```c
#define SPI3_REMAP1 STM32_REMAP(1U, 0x1U, 28U, STM32_AFIO_MAPR)
```

SPI3，重映射（remap）。

<a id="a2c91303d8a35d5fcbfa8621173d3fe07"></a>

### `STM32_AFIO_MAPR`

```c
#define STM32_AFIO_MAPR 0U
```

<a id="aa60a0ba8748fc37c64efcd19947e664e"></a>

### `STM32_AFIO_MAPR2`

```c
#define STM32_AFIO_MAPR2 1U
```

<a id="a200a3a748707c11bfd3129c16fc6a835"></a>

### `STM32_REMAP`

```c
#define STM32_REMAP ( val, mask, shift, reg )
```

展开值（Value）：

```c
((((reg) & STM32_REMAP_REG_MASK) << STM32_REMAP_REG_SHIFT) |           \
 (((shift) & STM32_REMAP_SHIFT_MASK) << STM32_REMAP_SHIFT_SHIFT) |     \
 (((mask) & STM32_REMAP_MASK_MASK) << STM32_REMAP_MASK_SHIFT) |        \
 (((val) & STM32_REMAP_VAL_MASK) << STM32_REMAP_VAL_SHIFT))
```

STM32F1 重映射配置位字段（Remap Configuration Bit Field）。

- 寄存器选择（reg，0/1），位范围 `[ 0 : 0 ]`。
- 移位量（shift，0..31），位范围 `[ 1 : 5 ]`。
- 掩码（mask，0x1、0x3），位范围 `[ 6 : 7 ]`。
- 值（val，0..3），位范围 `[ 8 : 9 ]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | `AFIO_MAPRx` 寄存器（Register），即 `MAPR`、`MAPR2`。 |
| `shift` | 在 `AFIO_MAPRx` 内的位置（Position）。 |
| `mask` | `AFIO_MAPRx` 字段的掩码（Mask）。 |
| `val` | 重映射值（Remap Value），取值为 0、1、2 或 3。 |

<a id="a71aeec8660001f84d3c55f426fdb7137"></a>

### `STM32_REMAP_MASK_GET`

```c
#define STM32_REMAP_MASK_GET ( remap)
```

展开值（Value）：

```c
(((remap) >> STM32_REMAP_MASK_SHIFT) & STM32_REMAP_MASK_MASK)
```

从重映射配置（Remap Configuration）中取得掩码字段（Mask Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remap` | 重映射位字段值（Remap Bit Field Value）。 |

<a id="a6e9613bf8369a7d1efa96cb90345a97a"></a>

### `STM32_REMAP_MASK_MASK`

```c
#define STM32_REMAP_MASK_MASK 0x3U
```

<a id="a3ffdee2c3eb7a004285180731366c15d"></a>

### `STM32_REMAP_MASK_SHIFT`

```c
#define STM32_REMAP_MASK_SHIFT 6U
```

<a id="a9d21e2ff45da0e873e6c8d1012c001f5"></a>

### `STM32_REMAP_REG_GET`

```c
#define STM32_REMAP_REG_GET ( remap)
```

展开值（Value）：

```c
(((remap) >> STM32_REMAP_REG_SHIFT) & STM32_REMAP_REG_MASK)
```

从重映射配置（Remap Configuration）中取得寄存器字段（Register Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remap` | 重映射位字段值（Remap Bit Field Value）。 |

<a id="ade5f8ba7372fa491075880f76e550b6c"></a>

### `STM32_REMAP_REG_MASK`

```c
#define STM32_REMAP_REG_MASK 0x1U
```

<a id="acbb01f8e98a95fe5460465e4ca2ba3e0"></a>

### `STM32_REMAP_REG_SHIFT`

```c
#define STM32_REMAP_REG_SHIFT 0U
```

<a id="a7a61290a7587f5680a8ff183d1c2907d"></a>

### `STM32_REMAP_SHIFT_GET`

```c
#define STM32_REMAP_SHIFT_GET ( remap)
```

展开值（Value）：

```c
(((remap) >> STM32_REMAP_SHIFT_SHIFT) & STM32_REMAP_SHIFT_MASK)
```

从重映射配置（Remap Configuration）中取得位置字段（Position Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remap` | 重映射位字段值（Remap Bit Field Value）。 |

<a id="a3cebc2d1cda7877f745ea12092794223"></a>

### `STM32_REMAP_SHIFT_MASK`

```c
#define STM32_REMAP_SHIFT_MASK 0x1FU
```

<a id="a1e14e8db39fbc3e33132adc10ad7067d"></a>

### `STM32_REMAP_SHIFT_SHIFT`

```c
#define STM32_REMAP_SHIFT_SHIFT 1U
```

<a id="a60b741decc8673b9f9a99b7a05d5e9fc"></a>

### `STM32_REMAP_VAL_GET`

```c
#define STM32_REMAP_VAL_GET ( remap)
```

展开值（Value）：

```c
(((remap) >> STM32_REMAP_VAL_SHIFT) & STM32_REMAP_VAL_MASK)
```

从重映射配置（Remap Configuration）中取得值字段（Value Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `remap` | 重映射位字段值（Remap Bit Field Value）。 |

<a id="a9cb1b934dd4621ebfae5115459efbd6e"></a>

### `STM32_REMAP_VAL_MASK`

```c
#define STM32_REMAP_VAL_MASK 0x3U
```

<a id="a144bfbe208a98ddc641ff538aa4738cc"></a>

### `STM32_REMAP_VAL_SHIFT`

```c
#define STM32_REMAP_VAL_SHIFT 8U
```

<a id="af5450df359cf37725a34f89b1af168e7"></a>

### `TIM10_REMAP0`

```c
#define TIM10_REMAP0 STM32_REMAP(0U, 0x1U, 6U, STM32_AFIO_MAPR2)
```

TIM10，无重映射（no remap）。

<a id="a691a581fe6dd08fd9a5a048abc5eaa3e"></a>

### `TIM10_REMAP1`

```c
#define TIM10_REMAP1 STM32_REMAP(1U, 0x1U, 6U, STM32_AFIO_MAPR2)
```

TIM10，重映射（remap）。

<a id="a01e4adf5326f92d144d45ba4b898ed8e"></a>

### `TIM11_REMAP0`

```c
#define TIM11_REMAP0 STM32_REMAP(0U, 0x1U, 7U, STM32_AFIO_MAPR2)
```

TIM11，无重映射（no remap）。

<a id="a7dcef4a23add63b6eb1254e6146dbe71"></a>

### `TIM11_REMAP1`

```c
#define TIM11_REMAP1 STM32_REMAP(1U, 0x1U, 7U, STM32_AFIO_MAPR2)
```

TIM11，重映射（remap）。

<a id="a2a6704eee24037ee9edd3873a5245ea0"></a>

### `TIM13_REMAP0`

```c
#define TIM13_REMAP0 STM32_REMAP(0U, 0x1U, 8U, STM32_AFIO_MAPR2)
```

TIM13，无重映射（no remap）。

<a id="acdcdd0184a5d75722dd1cbdbe2f8212f"></a>

### `TIM13_REMAP1`

```c
#define TIM13_REMAP1 STM32_REMAP(1U, 0x1U, 8U, STM32_AFIO_MAPR2)
```

TIM13，重映射（remap）。

<a id="a6c0341b14e851b4093e72932d05de5f5"></a>

### `TIM14_REMAP0`

```c
#define TIM14_REMAP0 STM32_REMAP(0U, 0x1U, 9U, STM32_AFIO_MAPR2)
```

TIM14，无重映射（no remap）。

<a id="ab047fa455523413d447f676fe9907c84"></a>

### `TIM14_REMAP1`

```c
#define TIM14_REMAP1 STM32_REMAP(1U, 0x1U, 9U, STM32_AFIO_MAPR2)
```

TIM14，重映射（remap）。

<a id="aa7da41d73e1ab29fef6020695f32f773"></a>

### `TIM15_REMAP0`

```c
#define TIM15_REMAP0 STM32_REMAP(0U, 0x1U, 0U, STM32_AFIO_MAPR2)
```

TIM15，无重映射（no remap）。

<a id="a87f392ac52f61d12709744f1ae8470af"></a>

### `TIM15_REMAP1`

```c
#define TIM15_REMAP1 STM32_REMAP(1U, 0x1U, 0U, STM32_AFIO_MAPR2)
```

TIM15，重映射（remap）。

<a id="a26d271515c8666e49cff39a1e5bb8112"></a>

### `TIM16_REMAP0`

```c
#define TIM16_REMAP0 STM32_REMAP(0U, 0x1U, 1U, STM32_AFIO_MAPR2)
```

TIM16，无重映射（no remap）。

<a id="a9459d0003315751cc5969c7ce1146947"></a>

### `TIM16_REMAP1`

```c
#define TIM16_REMAP1 STM32_REMAP(1U, 0x1U, 1U, STM32_AFIO_MAPR2)
```

TIM16，重映射（remap）。

<a id="a0c0e509d60821ac498a4fa03c4d5a47b"></a>

### `TIM17_REMAP0`

```c
#define TIM17_REMAP0 STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR2)
```

TIM17，无重映射（no remap）。

<a id="ae5da6d9ae0c81a39ba7c7f51135be110"></a>

### `TIM17_REMAP1`

```c
#define TIM17_REMAP1 STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR2)
```

TIM17，重映射（remap）。

<a id="a65b1a18a202a22d8c9add530fd0a8313"></a>

### `TIM1_REMAP0`

```c
#define TIM1_REMAP0 STM32_REMAP(0U, 0x3U, 6U, STM32_AFIO_MAPR)
```

TIM1，无重映射（no remap）。

<a id="aa7a6c64fab50803704cfc5f6a3fe4c9f"></a>

### `TIM1_REMAP1`

```c
#define TIM1_REMAP1 STM32_REMAP(1U, 0x3U, 6U, STM32_AFIO_MAPR)
```

TIM1，部分重映射（partial remap）。

<a id="a8de28395b1ecc659fbe3e4b33a8aaf76"></a>

### `TIM1_REMAP2`

```c
#define TIM1_REMAP2 STM32_REMAP(3U, 0x3U, 6U, STM32_AFIO_MAPR)
```

TIM1，完全重映射（full remap）。

<a id="a9ac0bc54a91246b78d863ba3a215ea96"></a>

### `TIM2_REMAP0`

```c
#define TIM2_REMAP0 STM32_REMAP(0U, 0x3U, 8U, STM32_AFIO_MAPR)
```

TIM2，无重映射（no remap）。

<a id="a6fad8ce0389fa7b6d5a80c501ed99ce9"></a>

### `TIM2_REMAP1`

```c
#define TIM2_REMAP1 STM32_REMAP(1U, 0x3U, 8U, STM32_AFIO_MAPR)
```

TIM2，部分重映射 1（partial remap 1）。

<a id="ae47bd66bc1f02dc89a624c7639ad492b"></a>

### `TIM2_REMAP2`

```c
#define TIM2_REMAP2 STM32_REMAP(2U, 0x3U, 8U, STM32_AFIO_MAPR)
```

TIM2，部分重映射 2（partial remap 2）。

<a id="ae3739bffc6fef7ca2aed06327fe26259"></a>

### `TIM2_REMAP3`

```c
#define TIM2_REMAP3 STM32_REMAP(3U, 0x3U, 8U, STM32_AFIO_MAPR)
```

TIM2，完全重映射（full remap）。

<a id="a535bdd60f1276bf660814c665c3ca349"></a>

### `TIM3_REMAP0`

```c
#define TIM3_REMAP0 STM32_REMAP(0U, 0x3U, 10U, STM32_AFIO_MAPR)
```

TIM3，无重映射（no remap）。

<a id="a068f135e7a2273b9eab28b934b0a7e53"></a>

### `TIM3_REMAP1`

```c
#define TIM3_REMAP1 STM32_REMAP(1U, 0x3U, 10U, STM32_AFIO_MAPR)
```

TIM3，部分重映射 1（partial remap 1）。

<a id="a5c8aa22a44a0b6ef2fbc169aeebdc2ea"></a>

### `TIM3_REMAP2`

```c
#define TIM3_REMAP2 STM32_REMAP(2U, 0x3U, 10U, STM32_AFIO_MAPR)
```

TIM3，部分重映射 2（partial remap 2）。

<a id="a811f621a99ec1b18a4b5fd4e52456a9f"></a>

### `TIM3_REMAP3`

```c
#define TIM3_REMAP3 STM32_REMAP(3U, 0x3U, 10U, STM32_AFIO_MAPR)
```

TIM3，完全重映射（full remap）。

<a id="af19b67747576ad37c76dccc4c8a1ea16"></a>

### `TIM4_REMAP0`

```c
#define TIM4_REMAP0 STM32_REMAP(0U, 0x1U, 12U, STM32_AFIO_MAPR)
```

TIM4，无重映射（no remap）。

<a id="aafb51d9eacaf920f3c78425ecaf5478e"></a>

### `TIM4_REMAP1`

```c
#define TIM4_REMAP1 STM32_REMAP(1U, 0x1U, 12U, STM32_AFIO_MAPR)
```

TIM4，重映射（remap）。

<a id="a075dc7fea001772986dfe31d9d9e8f9a"></a>

### `TIM9_REMAP0`

```c
#define TIM9_REMAP0 STM32_REMAP(0U, 0x1U, 5U, STM32_AFIO_MAPR2)
```

TIM9，无重映射（no remap）。

<a id="ad443ec934247e04996bf85b5ce9ef721"></a>

### `TIM9_REMAP1`

```c
#define TIM9_REMAP1 STM32_REMAP(1U, 0x1U, 5U, STM32_AFIO_MAPR2)
```

TIM9，重映射（remap）。

<a id="a5a79382b9eb0e4e502b8c84697a73433"></a>

### `USART1_REMAP0`

```c
#define USART1_REMAP0 STM32_REMAP(0U, 0x1U, 2U, STM32_AFIO_MAPR)
```

USART1，无重映射（no remap）。

<a id="ab002c165fc3d6a9e043164560a211f68"></a>

### `USART1_REMAP1`

```c
#define USART1_REMAP1 STM32_REMAP(1U, 0x1U, 2U, STM32_AFIO_MAPR)
```

USART1，重映射（remap）。

<a id="afd7dc4010b32a1f10510cc39e1c911da"></a>

### `USART2_REMAP0`

```c
#define USART2_REMAP0 STM32_REMAP(0U, 0x1U, 3U, STM32_AFIO_MAPR)
```

USART2，无重映射（no remap）。

<a id="a472167bf97fff0caba80fe06a56b8084"></a>

### `USART2_REMAP1`

```c
#define USART2_REMAP1 STM32_REMAP(1U, 0x1U, 3U, STM32_AFIO_MAPR)
```

USART2，重映射（remap）。

<a id="a45b45e1ad6629299c0efd15b2233cd0e"></a>

### `USART3_REMAP0`

```c
#define USART3_REMAP0 STM32_REMAP(0U, 0x3U, 4U, STM32_AFIO_MAPR)
```

USART3，无重映射（no remap）。

<a id="a3953583002841a586c85cbbb5d5fc931"></a>

### `USART3_REMAP1`

```c
#define USART3_REMAP1 STM32_REMAP(1U, 0x3U, 4U, STM32_AFIO_MAPR)
```

USART3，部分重映射（partial remap）。

<a id="a9642c16b4169ed0552056f8ee638ceb2"></a>

### `USART3_REMAP2`

```c
#define USART3_REMAP2 STM32_REMAP(3U, 0x3U, 4U, STM32_AFIO_MAPR)
```

USART3，完全重映射（full remap）。


## 6.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P108_stm32f1-afio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astm32f1-afio_8h_html_a144bfbe208a98ddc641ff538aa4738cc"></a>
<a id="astm32f1-afio_8h_html_a1e14e8db39fbc3e33132adc10ad7067d"></a>
<a id="astm32f1-afio_8h_html_a3cebc2d1cda7877f745ea12092794223"></a>
<a id="astm32f1-afio_8h_html_a3ffdee2c3eb7a004285180731366c15d"></a>
<a id="astm32f1-afio_8h_html_a6e9613bf8369a7d1efa96cb90345a97a"></a>
<a id="astm32f1-afio_8h_html_a9cb1b934dd4621ebfae5115459efbd6e"></a>
<a id="astm32f1-afio_8h_html_acbb01f8e98a95fe5460465e4ca2ba3e0"></a>
<a id="astm32f1-afio_8h_html_ade5f8ba7372fa491075880f76e550b6c"></a>

---

[上一章](P005_zephyr__posix__posix_signal.h_文件参考.md) · [返回大纲](大纲.md)
