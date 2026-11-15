---
id: learning.zephyr-docs.api-file-reference.page-5
title: zephyr__drivers__mfd__adp5585.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/adp5585_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_drivers\_\_mfd\_\_adp5585.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/adp5585_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_mfd_5Fadp5585_5Fconfig"></a>

```c
struct mfd_adp5585_config
```

相关声明：[mfd_adp5585_config](../device_power_control_model_reference/P031_mfd_adp5585_config_结构体.md)。

<a id="r_mfd_5Fadp5585_5Fdata"></a>

```c
struct mfd_adp5585_data
```

相关声明：[mfd_adp5585_data](../device_power_control_model_reference/P032_mfd_adp5585_data_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_afbd61635aa229f364824b9e84e96c7fa"></a>

```c
#define ADP5585_ID 0x00
```

相关声明：[ADP5585_ID](#afbd61635aa229f364824b9e84e96c7fa)。

<a id="r_a0a6c9fc68d3bc48ec43a4a27c7f973dd"></a>

```c
#define ADP5585_INT_STATUS 0x01
```

相关声明：[ADP5585_INT_STATUS](#a0a6c9fc68d3bc48ec43a4a27c7f973dd)。

<a id="r_a40d6f40ae61983958ae73d09eff68718"></a>

```c
#define ADP5585_STATUS 0x02
```

相关声明：[ADP5585_STATUS](#a40d6f40ae61983958ae73d09eff68718)。

<a id="r_afa83f7aace2fd46cf64e559bed0b11f0"></a>

```c
#define ADP5585_FIFO_1 0x03
```

相关声明：[ADP5585_FIFO_1](#afa83f7aace2fd46cf64e559bed0b11f0)。

<a id="r_a72d2335efa6fbabe89f1844b8bec2f70"></a>

```c
#define ADP5585_FIFO_2 0x04
```

相关声明：[ADP5585_FIFO_2](#a72d2335efa6fbabe89f1844b8bec2f70)。

<a id="r_a764a0a9a8b8ab3efabe00e547eb1dfea"></a>

```c
#define ADP5585_FIFO_3 0x05
```

相关声明：[ADP5585_FIFO_3](#a764a0a9a8b8ab3efabe00e547eb1dfea)。

<a id="r_a7e09ac2966e14165e9d1da7e8ad4b3f2"></a>

```c
#define ADP5585_FIFO_4 0x06
```

相关声明：[ADP5585_FIFO_4](#a7e09ac2966e14165e9d1da7e8ad4b3f2)。

<a id="r_a41b6a6efcce33c063712d13f878f758c"></a>

```c
#define ADP5585_FIFO_5 0x07
```

相关声明：[ADP5585_FIFO_5](#a41b6a6efcce33c063712d13f878f758c)。

<a id="r_a2e780a11e8498724fa6a169c86f6492b"></a>

```c
#define ADP5585_FIFO_6 0x08
```

相关声明：[ADP5585_FIFO_6](#a2e780a11e8498724fa6a169c86f6492b)。

<a id="r_a3e1738db835ff08fa2116145b16f0fa4"></a>

```c
#define ADP5585_FIFO_7 0x09
```

相关声明：[ADP5585_FIFO_7](#a3e1738db835ff08fa2116145b16f0fa4)。

<a id="r_a5a60166191e51b418a80123e0bbf47c4"></a>

```c
#define ADP5585_FIFO_8 0x0A
```

相关声明：[ADP5585_FIFO_8](#a5a60166191e51b418a80123e0bbf47c4)。

<a id="r_a49471e825aa64dbdd117dbf8f0a7cf5d"></a>

```c
#define ADP5585_FIFO_9 0x0B
```

相关声明：[ADP5585_FIFO_9](#a49471e825aa64dbdd117dbf8f0a7cf5d)。

<a id="r_a96c863ab3cf6d2167ad671fae97ddf18"></a>

```c
#define ADP5585_FIFO_10 0x0C
```

相关声明：[ADP5585_FIFO_10](#a96c863ab3cf6d2167ad671fae97ddf18)。

<a id="r_a053caf41bbaa3cbd93c12439f14e5d47"></a>

```c
#define ADP5585_FIFO_11 0x0D
```

相关声明：[ADP5585_FIFO_11](#a053caf41bbaa3cbd93c12439f14e5d47)。

<a id="r_a53716a13d1d427397915b3a3cbb34b2c"></a>

```c
#define ADP5585_FIFO_12 0x0E
```

相关声明：[ADP5585_FIFO_12](#a53716a13d1d427397915b3a3cbb34b2c)。

<a id="r_ac57c89eff3b3cadd5ed3d0a73040c21f"></a>

```c
#define ADP5585_FIFO_13 0x0F
```

相关声明：[ADP5585_FIFO_13](#ac57c89eff3b3cadd5ed3d0a73040c21f)。

<a id="r_ac5c9f36e90531803c38d5096649638a3"></a>

```c
#define ADP5585_FIFO_14 0x10
```

相关声明：[ADP5585_FIFO_14](#ac5c9f36e90531803c38d5096649638a3)。

<a id="r_a55ddf942d0a7636f28d9a67e4bd01377"></a>

```c
#define ADP5585_FIFO_15 0x11
```

相关声明：[ADP5585_FIFO_15](#a55ddf942d0a7636f28d9a67e4bd01377)。

<a id="r_a4a106aa7ac374e1b7234de740f062315"></a>

```c
#define ADP5585_FIFO_16 0x12
```

相关声明：[ADP5585_FIFO_16](#a4a106aa7ac374e1b7234de740f062315)。

<a id="r_a969cbf249f8e61e004c03b9ad7a7f01a"></a>

```c
#define ADP5585_GPI_INT_STAT_A 0x13
```

相关声明：[ADP5585_GPI_INT_STAT_A](#a969cbf249f8e61e004c03b9ad7a7f01a)。

<a id="r_a9cd52a6ab5a30a221f5b57c42845f366"></a>

```c
#define ADP5585_GPI_INT_STAT_B 0x14
```

相关声明：[ADP5585_GPI_INT_STAT_B](#a9cd52a6ab5a30a221f5b57c42845f366)。

<a id="r_a30acc2f2100514223ae1a1745f9c3c7b"></a>

```c
#define ADP5585_GPI_STATUS_A 0x15
```

相关声明：[ADP5585_GPI_STATUS_A](#a30acc2f2100514223ae1a1745f9c3c7b)。

<a id="r_a96ad72c5cb57c33d2949446e5243bae0"></a>

```c
#define ADP5585_GPI_STATUS_B 0x16
```

相关声明：[ADP5585_GPI_STATUS_B](#a96ad72c5cb57c33d2949446e5243bae0)。

<a id="r_a8367cd959eaff77e026fc90521889b84"></a>

```c
#define ADP5585_RPULL_CONFIG_A 0x17
```

相关声明：[ADP5585_RPULL_CONFIG_A](#a8367cd959eaff77e026fc90521889b84)。

<a id="r_ae76fa8a7688f59df166bf816ea9d472b"></a>

```c
#define ADP5585_RPULL_CONFIG_B 0x18
```

相关声明：[ADP5585_RPULL_CONFIG_B](#ae76fa8a7688f59df166bf816ea9d472b)。

<a id="r_ae3692e46404852668e15e60387c76e86"></a>

```c
#define ADP5585_RPULL_CONFIG_C 0x19
```

相关声明：[ADP5585_RPULL_CONFIG_C](#ae3692e46404852668e15e60387c76e86)。

<a id="r_a7dd9182b40ed99cd14f988cc781d9413"></a>

```c
#define ADP5585_RPULL_CONFIG_D 0x1A
```

相关声明：[ADP5585_RPULL_CONFIG_D](#a7dd9182b40ed99cd14f988cc781d9413)。

<a id="r_a67bad2472c7e78cf9e12c79550a882b9"></a>

```c
#define ADP5585_GPI_INT_LEVEL_A 0x1B
```

相关声明：[ADP5585_GPI_INT_LEVEL_A](#a67bad2472c7e78cf9e12c79550a882b9)。

<a id="r_acc6fe6801de4102c2eaf841a9c42f3bd"></a>

```c
#define ADP5585_GPI_INT_LEVEL_B 0x1C
```

相关声明：[ADP5585_GPI_INT_LEVEL_B](#acc6fe6801de4102c2eaf841a9c42f3bd)。

<a id="r_ad079e787ca2988308623a29ce238002b"></a>

```c
#define ADP5585_GPI_EVENT_EN_A 0x1D
```

相关声明：[ADP5585_GPI_EVENT_EN_A](#ad079e787ca2988308623a29ce238002b)。

<a id="r_a05059407f14853547d2d5e2d572e3efa"></a>

```c
#define ADP5585_GPI_EVENT_EN_B 0x1E
```

相关声明：[ADP5585_GPI_EVENT_EN_B](#a05059407f14853547d2d5e2d572e3efa)。

<a id="r_acc0487d4ed5b3321e5e7477e2e7069b0"></a>

```c
#define ADP5585_GPI_INTERRUPT_EN_A 0x1F
```

相关声明：[ADP5585_GPI_INTERRUPT_EN_A](#acc0487d4ed5b3321e5e7477e2e7069b0)。

<a id="r_a7623e23c6e768028be5df6567234ea32"></a>

```c
#define ADP5585_GPI_INTERRUPT_EN_B 0x20
```

相关声明：[ADP5585_GPI_INTERRUPT_EN_B](#a7623e23c6e768028be5df6567234ea32)。

<a id="r_a4712d02875b88c125b1e25c746440a31"></a>

```c
#define ADP5585_DEBOUNCE_DIS_A 0x21
```

相关声明：[ADP5585_DEBOUNCE_DIS_A](#a4712d02875b88c125b1e25c746440a31)。

<a id="r_ac907fc30a58a7ff2d91a69c1c87594c6"></a>

```c
#define ADP5585_DEBOUNCE_DIS_B 0x22
```

相关声明：[ADP5585_DEBOUNCE_DIS_B](#ac907fc30a58a7ff2d91a69c1c87594c6)。

<a id="r_a9daac58d194d0db90caad7a3e0efba96"></a>

```c
#define ADP5585_GPO_DATA_OUT_A 0x23
```

相关声明：[ADP5585_GPO_DATA_OUT_A](#a9daac58d194d0db90caad7a3e0efba96)。

<a id="r_a4c3152925821be1bd99172d7e9a98dab"></a>

```c
#define ADP5585_GPO_DATA_OUT_B 0x24
```

相关声明：[ADP5585_GPO_DATA_OUT_B](#a4c3152925821be1bd99172d7e9a98dab)。

<a id="r_a4d16b97199e23781b31a1903e9b26ae8"></a>

```c
#define ADP5585_GPO_OUT_MODE_A 0x25
```

相关声明：[ADP5585_GPO_OUT_MODE_A](#a4d16b97199e23781b31a1903e9b26ae8)。

<a id="r_a09edb76ab453c790bc7ba70544d1bbea"></a>

```c
#define ADP5585_GPO_OUT_MODE_B 0x26
```

相关声明：[ADP5585_GPO_OUT_MODE_B](#a09edb76ab453c790bc7ba70544d1bbea)。

<a id="r_afe9637fe22334d0014bdd65c71a743eb"></a>

```c
#define ADP5585_GPIO_DIRECTION_A 0x27
```

相关声明：[ADP5585_GPIO_DIRECTION_A](#afe9637fe22334d0014bdd65c71a743eb)。

<a id="r_aec18185b14f96c0d8f7d05ea5f2b7db8"></a>

```c
#define ADP5585_GPIO_DIRECTION_B 0x28
```

相关声明：[ADP5585_GPIO_DIRECTION_B](#aec18185b14f96c0d8f7d05ea5f2b7db8)。

<a id="r_a73dcbcf77052ad254453422edea750ef"></a>

```c
#define ADP5585_RESET1_EVENT_A 0x29
```

相关声明：[ADP5585_RESET1_EVENT_A](#a73dcbcf77052ad254453422edea750ef)。

<a id="r_ab73730cdd193626c32a2ec34eabcf3c9"></a>

```c
#define ADP5585_RESET1_EVENT_B 0x2A
```

相关声明：[ADP5585_RESET1_EVENT_B](#ab73730cdd193626c32a2ec34eabcf3c9)。

<a id="r_af8ee993d6eef733634f4d06953456284"></a>

```c
#define ADP5585_RESET1_EVENT_C 0x2B
```

相关声明：[ADP5585_RESET1_EVENT_C](#af8ee993d6eef733634f4d06953456284)。

<a id="r_a4a6c163e0c60a590ac0311336159a76b"></a>

```c
#define ADP5585_RESET2_EVENT_A 0x2C
```

相关声明：[ADP5585_RESET2_EVENT_A](#a4a6c163e0c60a590ac0311336159a76b)。

<a id="r_ab4368b4309e193c178b70a0f56a8d82e"></a>

```c
#define ADP5585_RESET2_EVENT_B 0x2D
```

相关声明：[ADP5585_RESET2_EVENT_B](#ab4368b4309e193c178b70a0f56a8d82e)。

<a id="r_a94eecacd78ca46744f5672c5d042ff07"></a>

```c
#define ADP5585_RESET_CFG 0x2E
```

相关声明：[ADP5585_RESET_CFG](#a94eecacd78ca46744f5672c5d042ff07)。

<a id="r_a23a8f65d404b7c0bafd55858858afa96"></a>

```c
#define ADP5585_PWM_OFFT_LOW 0x2F
```

相关声明：[ADP5585_PWM_OFFT_LOW](#a23a8f65d404b7c0bafd55858858afa96)。

<a id="r_ae4c576fc2d0efcf137c6530326ead1be"></a>

```c
#define ADP5585_PWM_OFFT_HIGH 0x30
```

相关声明：[ADP5585_PWM_OFFT_HIGH](#ae4c576fc2d0efcf137c6530326ead1be)。

<a id="r_a74fa6f7378722a569c298394ca2c3b36"></a>

```c
#define ADP5585_PWM_ONT_LOW 0x31
```

相关声明：[ADP5585_PWM_ONT_LOW](#a74fa6f7378722a569c298394ca2c3b36)。

<a id="r_a7bf28da865492a8c496613338a55933e"></a>

```c
#define ADP5585_PWM_ONT_HIGH 0x32
```

相关声明：[ADP5585_PWM_ONT_HIGH](#a7bf28da865492a8c496613338a55933e)。

<a id="r_a1de2da958c6db64a34a2de1fa6ffddba"></a>

```c
#define ADP5585_PWM_CFG 0x33
```

相关声明：[ADP5585_PWM_CFG](#a1de2da958c6db64a34a2de1fa6ffddba)。

<a id="r_a3cd8ec997df5e5425613e20e5fa240c6"></a>

```c
#define ADP5585_LOGIC_CFG 0x34
```

相关声明：[ADP5585_LOGIC_CFG](#a3cd8ec997df5e5425613e20e5fa240c6)。

<a id="r_a6944520e4d0b1187b4dea91f6c1adc10"></a>

```c
#define ADP5585_LOGIC_FF_CFG 0x35
```

相关声明：[ADP5585_LOGIC_FF_CFG](#a6944520e4d0b1187b4dea91f6c1adc10)。

<a id="r_a370f09e02a005f200784f830fec3591f"></a>

```c
#define ADP5585_LOGIC_INT_EVENT_EN 0x36
```

相关声明：[ADP5585_LOGIC_INT_EVENT_EN](#a370f09e02a005f200784f830fec3591f)。

<a id="r_a5c3dba7ca9da0b4df5ad2afcf4bcae5e"></a>

```c
#define ADP5585_POLL_PTIME_CFG 0x37
```

相关声明：[ADP5585_POLL_PTIME_CFG](#a5c3dba7ca9da0b4df5ad2afcf4bcae5e)。

<a id="r_ab657ba2f5015a956c3dd5d928684c98c"></a>

```c
#define ADP5585_PIN_CONFIG_A 0x38
```

相关声明：[ADP5585_PIN_CONFIG_A](#ab657ba2f5015a956c3dd5d928684c98c)。

<a id="r_a3b730343c76b05b7ea6ef5fe69f2e819"></a>

```c
#define ADP5585_PIN_CONFIG_B 0x39
```

相关声明：[ADP5585_PIN_CONFIG_B](#a3b730343c76b05b7ea6ef5fe69f2e819)。

<a id="r_a9abe95d8b24f41002df9318710b7e834"></a>

```c
#define ADP5585_PIN_CONFIG_C 0x3A
```

相关声明：[ADP5585_PIN_CONFIG_C](#a9abe95d8b24f41002df9318710b7e834)。

<a id="r_accaa4211d0b1dbd645652ed279d62557"></a>

```c
#define ADP5585_GENERAL_CFG 0x3B
```

相关声明：[ADP5585_GENERAL_CFG](#accaa4211d0b1dbd645652ed279d62557)。

<a id="r_a6b4c4ba659f9414747b0ae06bc0cdcfd"></a>

```c
#define ADP5585_INT_EN 0x3C
```

相关声明：[ADP5585_INT_EN](#a6b4c4ba659f9414747b0ae06bc0cdcfd)。

<a id="r_a5b090f56fa476d7cca2f6899135229f8"></a>

```c
#define ADP5585_DEVICE_ID_MASK 0xF
```

相关声明：[ADP5585_DEVICE_ID_MASK](#a5b090f56fa476d7cca2f6899135229f8)。

<a id="r_a3668ae7400564896daa2c609f8c4a594"></a>

```c
#define ADP5585_MAN_ID_MASK 0xF
```

相关声明：[ADP5585_MAN_ID_MASK](#a3668ae7400564896daa2c609f8c4a594)。

<a id="r_ac3364a58902030fbec498761fc442ffe"></a>

```c
#define ADP5585_MAN_ID_SHIFT 4
```

相关声明：[ADP5585_MAN_ID_SHIFT](#ac3364a58902030fbec498761fc442ffe)。

<a id="r_a372daeaedd3583aea797089b37fbe5c0"></a>

```c
#define ADP5585_MAN_ID 0x02
```

相关声明：[ADP5585_MAN_ID](#a372daeaedd3583aea797089b37fbe5c0)。

<a id="r_a7371eba2de343b1c26e0c1ea8119eb32"></a>

```c
#define ADP5585_PWM_CFG_EN 0x1
```

相关声明：[ADP5585_PWM_CFG_EN](#a7371eba2de343b1c26e0c1ea8119eb32)。

<a id="r_a0e4cbfb9cb957805c16e94d19e0420fd"></a>

```c
#define ADP5585_PWM_CFG_MODE 0x2
```

相关声明：[ADP5585_PWM_CFG_MODE](#a0e4cbfb9cb957805c16e94d19e0420fd)。

<a id="r_aa04ec62322c733d66ee37303d29d03f4"></a>

```c
#define ADP5585_PIN_CONFIG_R3_PWM 0x8
```

相关声明：[ADP5585_PIN_CONFIG_R3_PWM](#aa04ec62322c733d66ee37303d29d03f4)。

<a id="r_a33ad97c1ffb9cc9a820f0609dfc76087"></a>

```c
#define ADP5585_PIN_CONFIG_R3_MASK 0xC
```

相关声明：[ADP5585_PIN_CONFIG_R3_MASK](#a33ad97c1ffb9cc9a820f0609dfc76087)。

<a id="r_ab681a5188091e9a2443a622021bb560c"></a>

```c
#define ADP5585_GENERAL_CFG_OSC_EN 0x80
```

相关声明：[ADP5585_GENERAL_CFG_OSC_EN](#ab681a5188091e9a2443a622021bb560c)。

<a id="r_a4ba78a1afbbb7df3c945e07c45685717"></a>

```c
#define ADP5585_INT_EVENT (1U << 0)
```

相关声明：[ADP5585_INT_EVENT](#a4ba78a1afbbb7df3c945e07c45685717)。

<a id="r_a4aad6f3752b5b76f2f6f4ec5c03c0dcb"></a>

```c
#define ADP5585_INT_GPI (1U << 1)
```

相关声明：[ADP5585_INT_GPI](#a4aad6f3752b5b76f2f6f4ec5c03c0dcb)。

<a id="r_ad362d9d20ead42061bf577a75ae92107"></a>

```c
#define ADP5585_INT_OVERFLOW (1U << 2)
```

相关声明：[ADP5585_INT_OVERFLOW](#ad362d9d20ead42061bf577a75ae92107)。

<a id="r_ab38755ce29cc619bb163a327eafc48e9"></a>

```c
#define ADP5585_INT_LOGIC (1U << 4)
```

相关声明：[ADP5585_INT_LOGIC](#ab38755ce29cc619bb163a327eafc48e9)。

<a id="r_a7d65da027f146e0ec4c574becb014e43"></a>

```c
#define ADP5585_REG_MASK 0xFF
```

相关声明：[ADP5585_REG_MASK](#a7d65da027f146e0ec4c574becb014e43)。

## 5.3\_详细说明（Detailed Documentation）

<a id="a4712d02875b88c125b1e25c746440a31"></a>

### `ADP5585_DEBOUNCE_DIS_A`

```c
#define ADP5585_DEBOUNCE_DIS_A 0x21
```

<a id="ac907fc30a58a7ff2d91a69c1c87594c6"></a>

### `ADP5585_DEBOUNCE_DIS_B`

```c
#define ADP5585_DEBOUNCE_DIS_B 0x22
```

<a id="a5b090f56fa476d7cca2f6899135229f8"></a>

### `ADP5585_DEVICE_ID_MASK`

```c
#define ADP5585_DEVICE_ID_MASK 0xF
```

<a id="afa83f7aace2fd46cf64e559bed0b11f0"></a>

### `ADP5585_FIFO_1`

```c
#define ADP5585_FIFO_1 0x03
```

<a id="a96c863ab3cf6d2167ad671fae97ddf18"></a>

### `ADP5585_FIFO_10`

```c
#define ADP5585_FIFO_10 0x0C
```

<a id="a053caf41bbaa3cbd93c12439f14e5d47"></a>

### `ADP5585_FIFO_11`

```c
#define ADP5585_FIFO_11 0x0D
```

<a id="a53716a13d1d427397915b3a3cbb34b2c"></a>

### `ADP5585_FIFO_12`

```c
#define ADP5585_FIFO_12 0x0E
```

<a id="ac57c89eff3b3cadd5ed3d0a73040c21f"></a>

### `ADP5585_FIFO_13`

```c
#define ADP5585_FIFO_13 0x0F
```

<a id="ac5c9f36e90531803c38d5096649638a3"></a>

### `ADP5585_FIFO_14`

```c
#define ADP5585_FIFO_14 0x10
```

<a id="a55ddf942d0a7636f28d9a67e4bd01377"></a>

### `ADP5585_FIFO_15`

```c
#define ADP5585_FIFO_15 0x11
```

<a id="a4a106aa7ac374e1b7234de740f062315"></a>

### `ADP5585_FIFO_16`

```c
#define ADP5585_FIFO_16 0x12
```

<a id="a72d2335efa6fbabe89f1844b8bec2f70"></a>

### `ADP5585_FIFO_2`

```c
#define ADP5585_FIFO_2 0x04
```

<a id="a764a0a9a8b8ab3efabe00e547eb1dfea"></a>

### `ADP5585_FIFO_3`

```c
#define ADP5585_FIFO_3 0x05
```

<a id="a7e09ac2966e14165e9d1da7e8ad4b3f2"></a>

### `ADP5585_FIFO_4`

```c
#define ADP5585_FIFO_4 0x06
```

<a id="a41b6a6efcce33c063712d13f878f758c"></a>

### `ADP5585_FIFO_5`

```c
#define ADP5585_FIFO_5 0x07
```

<a id="a2e780a11e8498724fa6a169c86f6492b"></a>

### `ADP5585_FIFO_6`

```c
#define ADP5585_FIFO_6 0x08
```

<a id="a3e1738db835ff08fa2116145b16f0fa4"></a>

### `ADP5585_FIFO_7`

```c
#define ADP5585_FIFO_7 0x09
```

<a id="a5a60166191e51b418a80123e0bbf47c4"></a>

### `ADP5585_FIFO_8`

```c
#define ADP5585_FIFO_8 0x0A
```

<a id="a49471e825aa64dbdd117dbf8f0a7cf5d"></a>

### `ADP5585_FIFO_9`

```c
#define ADP5585_FIFO_9 0x0B
```

<a id="accaa4211d0b1dbd645652ed279d62557"></a>

### `ADP5585_GENERAL_CFG`

```c
#define ADP5585_GENERAL_CFG 0x3B
```

<a id="ab681a5188091e9a2443a622021bb560c"></a>

### `ADP5585_GENERAL_CFG_OSC_EN`

```c
#define ADP5585_GENERAL_CFG_OSC_EN 0x80
```

<a id="ad079e787ca2988308623a29ce238002b"></a>

### `ADP5585_GPI_EVENT_EN_A`

```c
#define ADP5585_GPI_EVENT_EN_A 0x1D
```

<a id="a05059407f14853547d2d5e2d572e3efa"></a>

### `ADP5585_GPI_EVENT_EN_B`

```c
#define ADP5585_GPI_EVENT_EN_B 0x1E
```

<a id="a67bad2472c7e78cf9e12c79550a882b9"></a>

### `ADP5585_GPI_INT_LEVEL_A`

```c
#define ADP5585_GPI_INT_LEVEL_A 0x1B
```

<a id="acc6fe6801de4102c2eaf841a9c42f3bd"></a>

### `ADP5585_GPI_INT_LEVEL_B`

```c
#define ADP5585_GPI_INT_LEVEL_B 0x1C
```

<a id="a969cbf249f8e61e004c03b9ad7a7f01a"></a>

### `ADP5585_GPI_INT_STAT_A`

```c
#define ADP5585_GPI_INT_STAT_A 0x13
```

<a id="a9cd52a6ab5a30a221f5b57c42845f366"></a>

### `ADP5585_GPI_INT_STAT_B`

```c
#define ADP5585_GPI_INT_STAT_B 0x14
```

<a id="acc0487d4ed5b3321e5e7477e2e7069b0"></a>

### `ADP5585_GPI_INTERRUPT_EN_A`

```c
#define ADP5585_GPI_INTERRUPT_EN_A 0x1F
```

<a id="a7623e23c6e768028be5df6567234ea32"></a>

### `ADP5585_GPI_INTERRUPT_EN_B`

```c
#define ADP5585_GPI_INTERRUPT_EN_B 0x20
```

<a id="a30acc2f2100514223ae1a1745f9c3c7b"></a>

### `ADP5585_GPI_STATUS_A`

```c
#define ADP5585_GPI_STATUS_A 0x15
```

<a id="a96ad72c5cb57c33d2949446e5243bae0"></a>

### `ADP5585_GPI_STATUS_B`

```c
#define ADP5585_GPI_STATUS_B 0x16
```

<a id="afe9637fe22334d0014bdd65c71a743eb"></a>

### `ADP5585_GPIO_DIRECTION_A`

```c
#define ADP5585_GPIO_DIRECTION_A 0x27
```

<a id="aec18185b14f96c0d8f7d05ea5f2b7db8"></a>

### `ADP5585_GPIO_DIRECTION_B`

```c
#define ADP5585_GPIO_DIRECTION_B 0x28
```

<a id="a9daac58d194d0db90caad7a3e0efba96"></a>

### `ADP5585_GPO_DATA_OUT_A`

```c
#define ADP5585_GPO_DATA_OUT_A 0x23
```

<a id="a4c3152925821be1bd99172d7e9a98dab"></a>

### `ADP5585_GPO_DATA_OUT_B`

```c
#define ADP5585_GPO_DATA_OUT_B 0x24
```

<a id="a4d16b97199e23781b31a1903e9b26ae8"></a>

### `ADP5585_GPO_OUT_MODE_A`

```c
#define ADP5585_GPO_OUT_MODE_A 0x25
```

<a id="a09edb76ab453c790bc7ba70544d1bbea"></a>

### `ADP5585_GPO_OUT_MODE_B`

```c
#define ADP5585_GPO_OUT_MODE_B 0x26
```

<a id="afbd61635aa229f364824b9e84e96c7fa"></a>

### `ADP5585_ID`

```c
#define ADP5585_ID 0x00
```

<a id="a6b4c4ba659f9414747b0ae06bc0cdcfd"></a>

### `ADP5585_INT_EN`

```c
#define ADP5585_INT_EN 0x3C
```

<a id="a4ba78a1afbbb7df3c945e07c45685717"></a>

### `ADP5585_INT_EVENT`

```c
#define ADP5585_INT_EVENT (1U << 0)
```

<a id="a4aad6f3752b5b76f2f6f4ec5c03c0dcb"></a>

### `ADP5585_INT_GPI`

```c
#define ADP5585_INT_GPI (1U << 1)
```

<a id="ab38755ce29cc619bb163a327eafc48e9"></a>

### `ADP5585_INT_LOGIC`

```c
#define ADP5585_INT_LOGIC (1U << 4)
```

<a id="ad362d9d20ead42061bf577a75ae92107"></a>

### `ADP5585_INT_OVERFLOW`

```c
#define ADP5585_INT_OVERFLOW (1U << 2)
```

<a id="a0a6c9fc68d3bc48ec43a4a27c7f973dd"></a>

### `ADP5585_INT_STATUS`

```c
#define ADP5585_INT_STATUS 0x01
```

<a id="a3cd8ec997df5e5425613e20e5fa240c6"></a>

### `ADP5585_LOGIC_CFG`

```c
#define ADP5585_LOGIC_CFG 0x34
```

<a id="a6944520e4d0b1187b4dea91f6c1adc10"></a>

### `ADP5585_LOGIC_FF_CFG`

```c
#define ADP5585_LOGIC_FF_CFG 0x35
```

<a id="a370f09e02a005f200784f830fec3591f"></a>

### `ADP5585_LOGIC_INT_EVENT_EN`

```c
#define ADP5585_LOGIC_INT_EVENT_EN 0x36
```

<a id="a372daeaedd3583aea797089b37fbe5c0"></a>

### `ADP5585_MAN_ID`

```c
#define ADP5585_MAN_ID 0x02
```

<a id="a3668ae7400564896daa2c609f8c4a594"></a>

### `ADP5585_MAN_ID_MASK`

```c
#define ADP5585_MAN_ID_MASK 0xF
```

<a id="ac3364a58902030fbec498761fc442ffe"></a>

### `ADP5585_MAN_ID_SHIFT`

```c
#define ADP5585_MAN_ID_SHIFT 4
```

<a id="ab657ba2f5015a956c3dd5d928684c98c"></a>

### `ADP5585_PIN_CONFIG_A`

```c
#define ADP5585_PIN_CONFIG_A 0x38
```

<a id="a3b730343c76b05b7ea6ef5fe69f2e819"></a>

### `ADP5585_PIN_CONFIG_B`

```c
#define ADP5585_PIN_CONFIG_B 0x39
```

<a id="a9abe95d8b24f41002df9318710b7e834"></a>

### `ADP5585_PIN_CONFIG_C`

```c
#define ADP5585_PIN_CONFIG_C 0x3A
```

<a id="a33ad97c1ffb9cc9a820f0609dfc76087"></a>

### `ADP5585_PIN_CONFIG_R3_MASK`

```c
#define ADP5585_PIN_CONFIG_R3_MASK 0xC
```

<a id="aa04ec62322c733d66ee37303d29d03f4"></a>

### `ADP5585_PIN_CONFIG_R3_PWM`

```c
#define ADP5585_PIN_CONFIG_R3_PWM 0x8
```

<a id="a5c3dba7ca9da0b4df5ad2afcf4bcae5e"></a>

### `ADP5585_POLL_PTIME_CFG`

```c
#define ADP5585_POLL_PTIME_CFG 0x37
```

<a id="a1de2da958c6db64a34a2de1fa6ffddba"></a>

### `ADP5585_PWM_CFG`

```c
#define ADP5585_PWM_CFG 0x33
```

<a id="a7371eba2de343b1c26e0c1ea8119eb32"></a>

### `ADP5585_PWM_CFG_EN`

```c
#define ADP5585_PWM_CFG_EN 0x1
```

<a id="a0e4cbfb9cb957805c16e94d19e0420fd"></a>

### `ADP5585_PWM_CFG_MODE`

```c
#define ADP5585_PWM_CFG_MODE 0x2
```

<a id="ae4c576fc2d0efcf137c6530326ead1be"></a>

### `ADP5585_PWM_OFFT_HIGH`

```c
#define ADP5585_PWM_OFFT_HIGH 0x30
```

<a id="a23a8f65d404b7c0bafd55858858afa96"></a>

### `ADP5585_PWM_OFFT_LOW`

```c
#define ADP5585_PWM_OFFT_LOW 0x2F
```

<a id="a7bf28da865492a8c496613338a55933e"></a>

### `ADP5585_PWM_ONT_HIGH`

```c
#define ADP5585_PWM_ONT_HIGH 0x32
```

<a id="a74fa6f7378722a569c298394ca2c3b36"></a>

### `ADP5585_PWM_ONT_LOW`

```c
#define ADP5585_PWM_ONT_LOW 0x31
```

<a id="a7d65da027f146e0ec4c574becb014e43"></a>

### `ADP5585_REG_MASK`

```c
#define ADP5585_REG_MASK 0xFF
```

<a id="a73dcbcf77052ad254453422edea750ef"></a>

### `ADP5585_RESET1_EVENT_A`

```c
#define ADP5585_RESET1_EVENT_A 0x29
```

<a id="ab73730cdd193626c32a2ec34eabcf3c9"></a>

### `ADP5585_RESET1_EVENT_B`

```c
#define ADP5585_RESET1_EVENT_B 0x2A
```

<a id="af8ee993d6eef733634f4d06953456284"></a>

### `ADP5585_RESET1_EVENT_C`

```c
#define ADP5585_RESET1_EVENT_C 0x2B
```

<a id="a4a6c163e0c60a590ac0311336159a76b"></a>

### `ADP5585_RESET2_EVENT_A`

```c
#define ADP5585_RESET2_EVENT_A 0x2C
```

<a id="ab4368b4309e193c178b70a0f56a8d82e"></a>

### `ADP5585_RESET2_EVENT_B`

```c
#define ADP5585_RESET2_EVENT_B 0x2D
```

<a id="a94eecacd78ca46744f5672c5d042ff07"></a>

### `ADP5585_RESET_CFG`

```c
#define ADP5585_RESET_CFG 0x2E
```

<a id="a8367cd959eaff77e026fc90521889b84"></a>

### `ADP5585_RPULL_CONFIG_A`

```c
#define ADP5585_RPULL_CONFIG_A 0x17
```

<a id="ae76fa8a7688f59df166bf816ea9d472b"></a>

### `ADP5585_RPULL_CONFIG_B`

```c
#define ADP5585_RPULL_CONFIG_B 0x18
```

<a id="ae3692e46404852668e15e60387c76e86"></a>

### `ADP5585_RPULL_CONFIG_C`

```c
#define ADP5585_RPULL_CONFIG_C 0x19
```

<a id="a7dd9182b40ed99cd14f988cc781d9413"></a>

### `ADP5585_RPULL_CONFIG_D`

```c
#define ADP5585_RPULL_CONFIG_D 0x1A
```

<a id="a40d6f40ae61983958ae73d09eff68718"></a>

### `ADP5585_STATUS`

```c
#define ADP5585_STATUS 0x02
```


## 5.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_configuration_reference/P002_adp5585.h_源码浏览.md)
- [mfd_adp5585_config](../device_power_control_model_reference/P031_mfd_adp5585_config_结构体.md)
- [mfd_adp5585_data](../device_power_control_model_reference/P032_mfd_adp5585_data_结构体.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_zephyr__arch__common__addr_types.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__posix__aio.h_文件参考.md)
