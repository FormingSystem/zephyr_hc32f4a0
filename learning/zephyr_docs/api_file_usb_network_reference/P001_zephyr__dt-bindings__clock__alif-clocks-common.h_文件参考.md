---
id: learning.zephyr-docs.api-file-usb-network-reference.page-1
title: zephyr__dt-bindings__clock__alif-clocks-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_clock\_\_alif-clocks-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/alif-clocks-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Alif Semiconductor片上系统（SoC）系列的通用时钟定义。

查看此文件的源码。

<a id="details"></a>

Alif Semiconductor 各 SoC 系列共用的时钟定义（Common Clock Definitions）。本头文件定义时钟标识符（Clock ID）的编码方案，以及所有 Alif SoC 系列共用的定义。该编码方案具有通用性，支持以下功能：

- 最多 8 个时钟模块（Clock Module），使用 3 位字段。
- 最多 32 个输入时钟源（Input Clock Source），使用 5 位字段。
- 为每个时钟选择父时钟源（Parent Clock Source）。
- 单独控制每个时钟的启用／禁用（Enable/Disable）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ad16c3d170e343c040ee7db3de70c1cd3"></a>

```c
#define ALIF_CLK_CFG(module, reg, en_bit, en_mask, src_val, src_field_width, src_field_pos, parent_clk)
```

相关声明：[ALIF_CLK_CFG](#ad16c3d170e343c040ee7db3de70c1cd3)。

ALIF 时钟配置位字段编码（Clock Configuration Bit Field Encoding）。

<a id="define-members-0"></a>

### 时钟标识符编码位字段定义（Clock ID Encoding Bit Field Definitions）

<a id="r_a2e24c2b9192d366c5268c6ecf3dcbbeb"></a>

```c
#define ALIF_CLOCK_MODULE_MASK 0x7U
```

相关声明：[ALIF_CLOCK_MODULE_MASK](#a2e24c2b9192d366c5268c6ecf3dcbbeb)。

时钟模块字段（Clock Module Field）的位掩码，共 3 位。

<a id="r_aba190892bbeba1d1bc73b11b869825e7"></a>

```c
#define ALIF_CLOCK_MODULE_SHIFT 0U
```

相关声明：[ALIF_CLOCK_MODULE_SHIFT](#aba190892bbeba1d1bc73b11b869825e7)。

时钟模块字段（Clock Module Field）的位移量。

<a id="r_a51b0b6e6945356468fbd53a2f139599e"></a>

```c
#define ALIF_CLOCK_REG_MASK 0xFFU
```

相关声明：[ALIF_CLOCK_REG_MASK](#a51b0b6e6945356468fbd53a2f139599e)。

寄存器偏移字段（Register Offset Field）的位掩码，共 8 位。

<a id="r_a369fe45112300aeaf99547de32af54ad"></a>

```c
#define ALIF_CLOCK_REG_SHIFT 3U
```

相关声明：[ALIF_CLOCK_REG_SHIFT](#a369fe45112300aeaf99547de32af54ad)。

寄存器偏移字段（Register Offset Field）的位移量。

<a id="r_a4bb022ede1780857578993c4badaeb23"></a>

```c
#define ALIF_CLOCK_EN_BIT_POS_MASK 0x1FU
```

相关声明：[ALIF_CLOCK_EN_BIT_POS_MASK](#a4bb022ede1780857578993c4badaeb23)。

使能位位置字段（Enable Bit Position Field）的位掩码，共 5 位。

<a id="r_ae977e20511550502323a2ac576eb5a73"></a>

```c
#define ALIF_CLOCK_EN_BIT_POS_SHIFT 11U
```

相关声明：[ALIF_CLOCK_EN_BIT_POS_SHIFT](#ae977e20511550502323a2ac576eb5a73)。

使能位位置字段（Enable Bit Position Field）的位移量。

<a id="r_afe3685d42ea23e10c87ac1b7bb2c0e19"></a>

```c
#define ALIF_CLOCK_EN_MASK_SHIFT 16U
```

相关声明：[ALIF_CLOCK_EN_MASK_SHIFT](#afe3685d42ea23e10c87ac1b7bb2c0e19)。

使能掩码字段（Enable Mask Field）的位移量。

<a id="r_aa0fa96e33d04087ec94d87f75d4b45b8"></a>

```c
#define ALIF_CLOCK_SRC_VAL_MASK 0x3U
```

相关声明：[ALIF_CLOCK_SRC_VAL_MASK](#aa0fa96e33d04087ec94d87f75d4b45b8)。

时钟源选择值（Clock Source Selection Value）的位掩码，共 2 位。

<a id="r_a4f4df9f03cef7ad005fb78481fdae2d7"></a>

```c
#define ALIF_CLOCK_SRC_VAL_SHIFT 17U
```

相关声明：[ALIF_CLOCK_SRC_VAL_SHIFT](#a4f4df9f03cef7ad005fb78481fdae2d7)。

时钟源选择值（Clock Source Selection Value）的位移量。

<a id="r_a9ca7fc3237e354387119989bbef373c5"></a>

```c
#define ALIF_CLOCK_SRC_FIELD_WIDTH_MASK 0x3U
```

相关声明：[ALIF_CLOCK_SRC_FIELD_WIDTH_MASK](#a9ca7fc3237e354387119989bbef373c5)。

时钟源选择字段宽度（Clock Source Selection Field Width）的位掩码，共 2 位。

<a id="r_a9aeb63bb8cbdbaf4fda3495229ffaea1"></a>

```c
#define ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT 19U
```

相关声明：[ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT](#a9aeb63bb8cbdbaf4fda3495229ffaea1)。

时钟源选择字段宽度（Clock Source Selection Field Width）的位移量。

<a id="r_a4bce981ebed6c399ee14ccea95d4471b"></a>

```c
#define ALIF_CLOCK_SRC_FIELD_POS_MASK 0x1FU
```

相关声明：[ALIF_CLOCK_SRC_FIELD_POS_MASK](#a4bce981ebed6c399ee14ccea95d4471b)。

时钟源选择字段位置（Clock Source Selection Field Position）的位掩码，共 5 位。

<a id="r_a35ced398b88873bf551c3b1f4605b31a"></a>

```c
#define ALIF_CLOCK_SRC_FIELD_POS_SHIFT 21U
```

相关声明：[ALIF_CLOCK_SRC_FIELD_POS_SHIFT](#a35ced398b88873bf551c3b1f4605b31a)。

时钟源选择字段位置（Clock Source Selection Field Position）的位移量。

<a id="r_a3535426e2e2a19fd0de26d91b290ffa7"></a>

```c
#define ALIF_CLOCK_PARENT_CLK_MASK 0x1FU
```

相关声明：[ALIF_CLOCK_PARENT_CLK_MASK](#a3535426e2e2a19fd0de26d91b290ffa7)。

父时钟标识符字段（Parent Clock Identifier Field）的位掩码，共 5 位。

<a id="r_a81c5b0c5f1dbc19cda2ca57c0dd19f21"></a>

```c
#define ALIF_CLOCK_PARENT_CLK_SHIFT 26U
```

相关声明：[ALIF_CLOCK_PARENT_CLK_SHIFT](#a81c5b0c5f1dbc19cda2ca57c0dd19f21)。

父时钟标识符字段（Parent Clock Identifier Field）的位移量。

<a id="define-members-1"></a>

### 父时钟源标识符（Parent Clock Source Identifiers）

<a id="r_a8fd38fb211a66a831407cb54d20872f4"></a>

```c
#define ALIF_PARENT_CLK_SYST_ACLK 0x0U
```

相关声明：[ALIF_PARENT_CLK_SYST_ACLK](#a8fd38fb211a66a831407cb54d20872f4)。

系统 AXI 时钟（System AXI Clock，`SYST_ACLK`）。

<a id="r_ac19e49c79ecb6af55f0e26af01f3c1ef"></a>

```c
#define ALIF_PARENT_CLK_SYST_HCLK 0x1U
```

相关声明：[ALIF_PARENT_CLK_SYST_HCLK](#ac19e49c79ecb6af55f0e26af01f3c1ef)。

系统 AHB 时钟（System AHB Clock，`SYST_HCLK`）。

<a id="r_acc723a914c55fe078a797fd3b27c8e31"></a>

```c
#define ALIF_PARENT_CLK_SYST_PCLK 0x2U
```

相关声明：[ALIF_PARENT_CLK_SYST_PCLK](#acc723a914c55fe078a797fd3b27c8e31)。

系统 APB 时钟（System APB Clock，`SYST_PCLK`）。

<a id="r_a635a3c5ac05e64e3ad7e995512d723ec"></a>

```c
#define ALIF_PARENT_CLK_S32K 0x3U
```

相关声明：[ALIF_PARENT_CLK_S32K](#a635a3c5ac05e64e3ad7e995512d723ec)。

始终开启的 32 kHz 时钟（Always-on Clock，`S32K_CLK`），源自 LFXO 或 LFRC 振荡器（Oscillator）。

<a id="r_a2d26177aaee75a0afe00f9bd8a4e1a49"></a>

```c
#define ALIF_PARENT_CLK_128K 0x4U
```

相关声明：[ALIF_PARENT_CLK_128K](#a2d26177aaee75a0afe00f9bd8a4e1a49)。

始终开启的 128 kHz 时钟（Always-on Clock，`128K_CLK`），由 LFRC 振荡器（Oscillator）派生。

<a id="define-members-2"></a>

### 时钟模块标识符（Clock Module Identifiers）

这些模块标识符（Module ID）由 Alif 各 SoC 系列共用。

每个模块代表一个独立的时钟控制寄存器块（Clock Control Register Block）。

<a id="r_a759367edf9f19f643455064567007f05"></a>

```c
#define ALIF_CGU_MODULE 0x0U
```

相关声明：[ALIF_CGU_MODULE](#a759367edf9f19f643455064567007f05)。

时钟生成单元（Clock Generation Unit）。

<a id="r_a16913bdefdcbcbd575eeeeaf3fc67004"></a>

```c
#define ALIF_CLKCTL_PER_MST_MODULE 0x1U
```

相关声明：[ALIF_CLKCTL_PER_MST_MODULE](#a16913bdefdcbcbd575eeeeaf3fc67004)。

外设时钟控制，主侧（Peripheral Clock Control，Master）。

<a id="r_a89b8a7df5434bd17b4747ba2b8813ccb"></a>

```c
#define ALIF_CLKCTL_PER_SLV_MODULE 0x2U
```

相关声明：[ALIF_CLKCTL_PER_SLV_MODULE](#a89b8a7df5434bd17b4747ba2b8813ccb)。

外设时钟控制，从侧（Peripheral Clock Control，Slave）。

<a id="r_a0b1a23def514d8337a58e19ab0357e77"></a>

```c
#define ALIF_AON_MODULE 0x3U
```

相关声明：[ALIF_AON_MODULE](#a0b1a23def514d8337a58e19ab0357e77)。

常开时钟控制（Always-On Clock Control）。

<a id="r_a3a47015ed016e9e1b6fe6b4954c633f7"></a>

```c
#define ALIF_VBAT_MODULE 0x4U
```

相关声明：[ALIF_VBAT_MODULE](#a3a47015ed016e9e1b6fe6b4954c633f7)。

VBAT 时钟控制（VBAT Clock Control）。

<a id="r_aa3767b5bf546be897ac47c7065b65d19"></a>

```c
#define ALIF_M55HE_CFG_MODULE 0x5U
```

相关声明：[ALIF_M55HE_CFG_MODULE](#aa3767b5bf546be897ac47c7065b65d19)。

M55 高能效配置（High Efficiency Config）。

<a id="r_af9f8041aa8b71df012d23cd8bf5c3d75"></a>

```c
#define ALIF_M55HP_CFG_MODULE 0x6U
```

相关声明：[ALIF_M55HP_CFG_MODULE](#af9f8041aa8b71df012d23cd8bf5c3d75)。

M55 高性能配置（High Performance Config）。

## 1.2\_详细说明（Detailed Documentation）

<a id="a0b1a23def514d8337a58e19ab0357e77"></a>

### `ALIF_AON_MODULE`

```c
#define ALIF_AON_MODULE 0x3U
```

常开时钟控制（Always-On Clock Control）。

<a id="a759367edf9f19f643455064567007f05"></a>

### `ALIF_CGU_MODULE`

```c
#define ALIF_CGU_MODULE 0x0U
```

时钟生成单元（Clock Generation Unit）。

<a id="ad16c3d170e343c040ee7db3de70c1cd3"></a>

### `ALIF_CLK_CFG`

```c
#define ALIF_CLK_CFG ( module, reg, en_bit, en_mask, src_val, src_field_width, src_field_pos, parent_clk )
```

展开值（Value）：

```c
((((ALIF_##module##_MODULE) & ALIF_CLOCK_MODULE_MASK) << ALIF_CLOCK_MODULE_SHIFT) |        \
 (((ALIF_##reg##_REG) & ALIF_CLOCK_REG_MASK) << ALIF_CLOCK_REG_SHIFT) |                    \
 (((en_bit) & ALIF_CLOCK_EN_BIT_POS_MASK) << ALIF_CLOCK_EN_BIT_POS_SHIFT) |                \
 (((en_mask) & 0x1U) << ALIF_CLOCK_EN_MASK_SHIFT) |                                        \
 (((src_val) & ALIF_CLOCK_SRC_VAL_MASK) << ALIF_CLOCK_SRC_VAL_SHIFT) |                     \
 (((src_field_width) & ALIF_CLOCK_SRC_FIELD_WIDTH_MASK) <<                                 \
  ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT) |                                                      \
 (((src_field_pos) & ALIF_CLOCK_SRC_FIELD_POS_MASK) << ALIF_CLOCK_SRC_FIELD_POS_SHIFT) |   \
 (((parent_clk) & ALIF_CLOCK_PARENT_CLK_MASK) << ALIF_CLOCK_PARENT_CLK_SHIFT))
```

ALIF 时钟配置位字段编码（Clock Configuration Bit Field Encoding）。

本宏将全部时钟控制信息（Clock Control Information）编码为一个 32 位值，可通过设备树（Devicetree）传给时钟驱动（Clock Driver）。

位字段布局（Bit Field Layout）：

- `module [ 0 : 2 ]`：时钟模块标识符（Clock Module ID），范围为 0–7，参见 `ALIF_*_MODULE`。
- `reg [ 3 : 10 ]`：模块内的寄存器偏移（Register Offset），范围为 0–255。
- `en_bit [ 11 : 15 ]`：使能控制的位位置（Enable Control Bit Position），范围为 0–31。
- `en_mask [ 16 ]`：存在使能控制（Enable Control）时为 1，始终开启（Always-on）时为 0。
- `src_val [ 17 : 18 ]`：要写入的时钟源选择值（Clock Source Selection Value），范围为 0–3。
- `src_field_width [ 19 : 20 ]`：时钟源字段宽度（Clock Source Field Width），以位为单位，范围为 0–3；0 表示没有选择字段。
- `src_field_pos [ 21 : 25 ]`：时钟源字段位位置（Clock Source Field Bit Position），范围为 0–31。
- `parent_clk [ 26 : 30 ]`：父时钟源标识符（Parent Clock Source Identifier），范围为 0–31。
- `reserved [ 31 ]`：保留供将来使用（Reserved for Future Use）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `module` | 时钟模块（Clock Module），例如 `CGU`、`CLKCTL_PER_MST`、`CLKCTL_PER_SLV`。 |
| `reg` | 寄存器名称（Register Name），将展开为 `ALIF_<reg>_REG`。 |
| `en_bit` | 时钟使能位的位置（Clock Enable Bit Position），范围为 0–31。 |
| `en_mask` | 如果时钟具有使能控制（Enable Control），则为 1；如果始终启用，则为 0。 |
| `src_val` | 要写入的时钟源值（Clock Source Value），范围为 0–3。 |
| `src_field_width` | 时钟源选择字段宽度（Field Width）：0 表示无选择字段，1–3 表示字段的位数。 |
| `src_field_pos` | 时钟源选择字段的位位置（Clock Source Selection Field Bit Position），范围为 0–31。 |
| `parent_clk` | 父时钟源标识符（Parent Clock Source Identifier），范围为 0–31；参见 `ALIF_PARENT_CLK_*`。 |

<a id="a16913bdefdcbcbd575eeeeaf3fc67004"></a>

### `ALIF_CLKCTL_PER_MST_MODULE`

```c
#define ALIF_CLKCTL_PER_MST_MODULE 0x1U
```

外设时钟控制，主侧（Peripheral Clock Control，Master）。

<a id="a89b8a7df5434bd17b4747ba2b8813ccb"></a>

### `ALIF_CLKCTL_PER_SLV_MODULE`

```c
#define ALIF_CLKCTL_PER_SLV_MODULE 0x2U
```

外设时钟控制，从侧（Peripheral Clock Control，Slave）。

<a id="a4bb022ede1780857578993c4badaeb23"></a>

### `ALIF_CLOCK_EN_BIT_POS_MASK`

```c
#define ALIF_CLOCK_EN_BIT_POS_MASK 0x1FU
```

使能位位置字段（Enable Bit Position Field）的位掩码，共 5 位。

<a id="ae977e20511550502323a2ac576eb5a73"></a>

### `ALIF_CLOCK_EN_BIT_POS_SHIFT`

```c
#define ALIF_CLOCK_EN_BIT_POS_SHIFT 11U
```

使能位位置字段（Enable Bit Position Field）的位移量。

<a id="afe3685d42ea23e10c87ac1b7bb2c0e19"></a>

### `ALIF_CLOCK_EN_MASK_SHIFT`

```c
#define ALIF_CLOCK_EN_MASK_SHIFT 16U
```

使能掩码字段（Enable Mask Field）的位移量。

<a id="a2e24c2b9192d366c5268c6ecf3dcbbeb"></a>

### `ALIF_CLOCK_MODULE_MASK`

```c
#define ALIF_CLOCK_MODULE_MASK 0x7U
```

时钟模块字段（Clock Module Field）的位掩码，共 3 位。

<a id="aba190892bbeba1d1bc73b11b869825e7"></a>

### `ALIF_CLOCK_MODULE_SHIFT`

```c
#define ALIF_CLOCK_MODULE_SHIFT 0U
```

时钟模块字段（Clock Module Field）的位移量。

<a id="a3535426e2e2a19fd0de26d91b290ffa7"></a>

### `ALIF_CLOCK_PARENT_CLK_MASK`

```c
#define ALIF_CLOCK_PARENT_CLK_MASK 0x1FU
```

父时钟标识符字段（Parent Clock Identifier Field）的位掩码，共 5 位。

<a id="a81c5b0c5f1dbc19cda2ca57c0dd19f21"></a>

### `ALIF_CLOCK_PARENT_CLK_SHIFT`

```c
#define ALIF_CLOCK_PARENT_CLK_SHIFT 26U
```

父时钟标识符字段（Parent Clock Identifier Field）的位移量。

<a id="a51b0b6e6945356468fbd53a2f139599e"></a>

### `ALIF_CLOCK_REG_MASK`

```c
#define ALIF_CLOCK_REG_MASK 0xFFU
```

寄存器偏移字段（Register Offset Field）的位掩码，共 8 位。

<a id="a369fe45112300aeaf99547de32af54ad"></a>

### `ALIF_CLOCK_REG_SHIFT`

```c
#define ALIF_CLOCK_REG_SHIFT 3U
```

寄存器偏移字段（Register Offset Field）的位移量。

<a id="a4bce981ebed6c399ee14ccea95d4471b"></a>

### `ALIF_CLOCK_SRC_FIELD_POS_MASK`

```c
#define ALIF_CLOCK_SRC_FIELD_POS_MASK 0x1FU
```

时钟源选择字段位置（Clock Source Selection Field Position）的位掩码，共 5 位。

<a id="a35ced398b88873bf551c3b1f4605b31a"></a>

### `ALIF_CLOCK_SRC_FIELD_POS_SHIFT`

```c
#define ALIF_CLOCK_SRC_FIELD_POS_SHIFT 21U
```

时钟源选择字段位置（Clock Source Selection Field Position）的位移量。

<a id="a9ca7fc3237e354387119989bbef373c5"></a>

### `ALIF_CLOCK_SRC_FIELD_WIDTH_MASK`

```c
#define ALIF_CLOCK_SRC_FIELD_WIDTH_MASK 0x3U
```

时钟源选择字段宽度（Clock Source Selection Field Width）的位掩码，共 2 位。

<a id="a9aeb63bb8cbdbaf4fda3495229ffaea1"></a>

### `ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT`

```c
#define ALIF_CLOCK_SRC_FIELD_WIDTH_SHIFT 19U
```

时钟源选择字段宽度（Clock Source Selection Field Width）的位移量。

<a id="aa0fa96e33d04087ec94d87f75d4b45b8"></a>

### `ALIF_CLOCK_SRC_VAL_MASK`

```c
#define ALIF_CLOCK_SRC_VAL_MASK 0x3U
```

时钟源选择值（Clock Source Selection Value）的位掩码，共 2 位。

<a id="a4f4df9f03cef7ad005fb78481fdae2d7"></a>

### `ALIF_CLOCK_SRC_VAL_SHIFT`

```c
#define ALIF_CLOCK_SRC_VAL_SHIFT 17U
```

时钟源选择值（Clock Source Selection Value）的位移量。

<a id="aa3767b5bf546be897ac47c7065b65d19"></a>

### `ALIF_M55HE_CFG_MODULE`

```c
#define ALIF_M55HE_CFG_MODULE 0x5U
```

M55 高能效配置（High Efficiency Config）。

<a id="af9f8041aa8b71df012d23cd8bf5c3d75"></a>

### `ALIF_M55HP_CFG_MODULE`

```c
#define ALIF_M55HP_CFG_MODULE 0x6U
```

M55 高性能配置（High Performance Config）。

<a id="a2d26177aaee75a0afe00f9bd8a4e1a49"></a>

### `ALIF_PARENT_CLK_128K`

```c
#define ALIF_PARENT_CLK_128K 0x4U
```

始终开启的 128 kHz 时钟（Always-on Clock，`128K_CLK`），由 LFRC 振荡器（Oscillator）派生。

<a id="a635a3c5ac05e64e3ad7e995512d723ec"></a>

### `ALIF_PARENT_CLK_S32K`

```c
#define ALIF_PARENT_CLK_S32K 0x3U
```

始终开启的 32 kHz 时钟（Always-on Clock，`S32K_CLK`），源自 LFXO 或 LFRC 振荡器（Oscillator）。

<a id="a8fd38fb211a66a831407cb54d20872f4"></a>

### `ALIF_PARENT_CLK_SYST_ACLK`

```c
#define ALIF_PARENT_CLK_SYST_ACLK 0x0U
```

系统 AXI 时钟（System AXI Clock，`SYST_ACLK`）。

<a id="ac19e49c79ecb6af55f0e26af01f3c1ef"></a>

### `ALIF_PARENT_CLK_SYST_HCLK`

```c
#define ALIF_PARENT_CLK_SYST_HCLK 0x1U
```

系统 AHB 时钟（System AHB Clock，`SYST_HCLK`）。

<a id="acc723a914c55fe078a797fd3b27c8e31"></a>

### `ALIF_PARENT_CLK_SYST_PCLK`

```c
#define ALIF_PARENT_CLK_SYST_PCLK 0x2U
```

系统 APB 时钟（System APB Clock，`SYST_PCLK`）。

<a id="a3a47015ed016e9e1b6fe6b4954c633f7"></a>

### `ALIF_VBAT_MODULE`

```c
#define ALIF_VBAT_MODULE 0x4U
```

VBAT 时钟控制（VBAT Clock Control）。


## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P021_alif-clocks-common.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aalif-clocks-common_8h_html_a2e24c2b9192d366c5268c6ecf3dcbbeb"></a>
<a id="aalif-clocks-common_8h_html_a3535426e2e2a19fd0de26d91b290ffa7"></a>
<a id="aalif-clocks-common_8h_html_a35ced398b88873bf551c3b1f4605b31a"></a>
<a id="aalif-clocks-common_8h_html_a369fe45112300aeaf99547de32af54ad"></a>
<a id="aalif-clocks-common_8h_html_a4bb022ede1780857578993c4badaeb23"></a>
<a id="aalif-clocks-common_8h_html_a4bce981ebed6c399ee14ccea95d4471b"></a>
<a id="aalif-clocks-common_8h_html_a4f4df9f03cef7ad005fb78481fdae2d7"></a>
<a id="aalif-clocks-common_8h_html_a51b0b6e6945356468fbd53a2f139599e"></a>
<a id="aalif-clocks-common_8h_html_a81c5b0c5f1dbc19cda2ca57c0dd19f21"></a>
<a id="aalif-clocks-common_8h_html_a9aeb63bb8cbdbaf4fda3495229ffaea1"></a>
<a id="aalif-clocks-common_8h_html_a9ca7fc3237e354387119989bbef373c5"></a>
<a id="aalif-clocks-common_8h_html_aa0fa96e33d04087ec94d87f75d4b45b8"></a>
<a id="aalif-clocks-common_8h_html_aba190892bbeba1d1bc73b11b869825e7"></a>
<a id="aalif-clocks-common_8h_html_ae977e20511550502323a2ac576eb5a73"></a>
<a id="aalif-clocks-common_8h_html_afe3685d42ea23e10c87ac1b7bb2c0e19"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__dt-bindings__clock__amebad_clock.h_文件参考.md)
