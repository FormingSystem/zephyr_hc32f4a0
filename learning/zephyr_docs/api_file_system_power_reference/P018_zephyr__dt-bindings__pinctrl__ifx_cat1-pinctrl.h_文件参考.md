---
id: learning.zephyr-docs.api-file-system-power-reference.page-18
title: zephyr__dt-bindings__pinctrl__ifx_cat1-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ifx\_cat1-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ifx__cat1-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 18.1\_宏定义（Macros）

<a id="r_a6ba3e93a5498c6c5bd5e8f3d0c00ac2a"></a>

```c
#define SOC_PINMUX_PORT_POS (0)
```

相关声明：[SOC_PINMUX_PORT_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)。

引脚控制绑定辅助接口（Pin Control Binding Helper）。

<a id="r_a4199ffda078d925e8dfb58194117de1a"></a>

```c
#define SOC_PINMUX_PORT_MASK (0xFFul << SOC_PINMUX_PORT_POS)
```

相关声明：[SOC_PINMUX_PORT_MASK](#a4199ffda078d925e8dfb58194117de1a)、[SOC_PINMUX_PORT_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)。

<a id="r_a5266efcdc6dbcd64d8fc61c814b37dc7"></a>

```c
#define SOC_PINMUX_PIN_POS (8)
```

相关声明：[SOC_PINMUX_PIN_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)。

<a id="r_a881a5ee83663d0eac3a2cfd530e23266"></a>

```c
#define SOC_PINMUX_PIN_MASK (0xFFul << SOC_PINMUX_PIN_POS)
```

相关声明：[SOC_PINMUX_PIN_MASK](#a881a5ee83663d0eac3a2cfd530e23266)、[SOC_PINMUX_PIN_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)。

<a id="r_a2af56d2b85a6e4ba3a2f1fdd191f8c98"></a>

```c
#define SOC_PINMUX_HSIOM_FUNC_POS (16)
```

相关声明：[SOC_PINMUX_HSIOM_FUNC_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)。

<a id="r_a6baa74b565ac921b7e3b8b5fc65327a6"></a>

```c
#define SOC_PINMUX_HSIOM_MASK (0xFFul << SOC_PINMUX_HSIOM_FUNC_POS)
```

相关声明：[SOC_PINMUX_HSIOM_MASK](#a6baa74b565ac921b7e3b8b5fc65327a6)、[SOC_PINMUX_HSIOM_FUNC_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)。

<a id="r_a38673a696cc1caa97e13eb6ef937007a"></a>

```c
#define SOC_PINMUX_SIGNAL_POS (24)
```

相关声明：[SOC_PINMUX_SIGNAL_POS](#a38673a696cc1caa97e13eb6ef937007a)。

<a id="r_aca26c39aa27a6520ea0f57b7ab058672"></a>

```c
#define SOC_PINMUX_SIGNAL_MASK (0xFFul << SOC_PINMUX_SIGNAL_POS)
```

相关声明：[SOC_PINMUX_SIGNAL_MASK](#aca26c39aa27a6520ea0f57b7ab058672)、[SOC_PINMUX_SIGNAL_POS](#a38673a696cc1caa97e13eb6ef937007a)。

<a id="r_ac0d2af1bfb229de155412af7f00e4fe0"></a>

```c
#define HSIOM_SEL_GPIO (0)
```

相关声明：[HSIOM_SEL_GPIO](#ac0d2af1bfb229de155412af7f00e4fe0)。

使用 HSIOM SEL 定义功能（Functions）。

<a id="r_a441de7f56a1c7c75cdae4d9f93ccfade"></a>

```c
#define HSIOM_SEL_GPIO_DSI (1)
```

相关声明：[HSIOM_SEL_GPIO_DSI](#a441de7f56a1c7c75cdae4d9f93ccfade)。

<a id="r_a959873e5156c6e3c24dd2773bb1ba516"></a>

```c
#define HSIOM_SEL_DSI_DSI (2)
```

相关声明：[HSIOM_SEL_DSI_DSI](#a959873e5156c6e3c24dd2773bb1ba516)。

<a id="r_a022f7af586ee9b46f689d187e8dd73d8"></a>

```c
#define HSIOM_SEL_DSI_GPIO (3)
```

相关声明：[HSIOM_SEL_DSI_GPIO](#a022f7af586ee9b46f689d187e8dd73d8)。

<a id="r_a8806729fcb666c9de823be5dd55c873d"></a>

```c
#define HSIOM_SEL_AMUXA (4)
```

相关声明：[HSIOM_SEL_AMUXA](#a8806729fcb666c9de823be5dd55c873d)。

<a id="r_a862eb93443c5c9575ff990b776b6203b"></a>

```c
#define HSIOM_SEL_AMUXB (5)
```

相关声明：[HSIOM_SEL_AMUXB](#a862eb93443c5c9575ff990b776b6203b)。

<a id="r_a4ba8695f92c0f347dd25ef981d67d1b0"></a>

```c
#define HSIOM_SEL_AMUXA_DSI (6)
```

相关声明：[HSIOM_SEL_AMUXA_DSI](#a4ba8695f92c0f347dd25ef981d67d1b0)。

<a id="r_af7a28a087a8867a14423e9ab471cce54"></a>

```c
#define HSIOM_SEL_AMUXB_DSI (7)
```

相关声明：[HSIOM_SEL_AMUXB_DSI](#af7a28a087a8867a14423e9ab471cce54)。

<a id="r_a3080ad4afafa572482ea1a5b49f6a1ce"></a>

```c
#define HSIOM_SEL_ACT_0 (8)
```

相关声明：[HSIOM_SEL_ACT_0](#a3080ad4afafa572482ea1a5b49f6a1ce)。

<a id="r_a990e35fecfcc37ca08fe709eee746618"></a>

```c
#define HSIOM_SEL_ACT_1 (9)
```

相关声明：[HSIOM_SEL_ACT_1](#a990e35fecfcc37ca08fe709eee746618)。

<a id="r_a696aeb76109bf339ebf0fcd20979f211"></a>

```c
#define HSIOM_SEL_ACT_2 (10)
```

相关声明：[HSIOM_SEL_ACT_2](#a696aeb76109bf339ebf0fcd20979f211)。

<a id="r_a25e956bc540c9570392a1722b7e94670"></a>

```c
#define HSIOM_SEL_ACT_3 (11)
```

相关声明：[HSIOM_SEL_ACT_3](#a25e956bc540c9570392a1722b7e94670)。

<a id="r_afb33417be16e7fa6423fadd2ef4a0f5b"></a>

```c
#define HSIOM_SEL_DS_0 (12)
```

相关声明：[HSIOM_SEL_DS_0](#afb33417be16e7fa6423fadd2ef4a0f5b)。

<a id="r_aa06be65ae17fc2dc1861c2af2e364652"></a>

```c
#define HSIOM_SEL_DS_1 (13)
```

相关声明：[HSIOM_SEL_DS_1](#aa06be65ae17fc2dc1861c2af2e364652)。

<a id="r_a07f591dc1f8a9f9eda13063d8c58c4eb"></a>

```c
#define HSIOM_SEL_DS_2 (14)
```

相关声明：[HSIOM_SEL_DS_2](#a07f591dc1f8a9f9eda13063d8c58c4eb)。

<a id="r_a157da2f7e72fa8f19dfd682ec4444319"></a>

```c
#define HSIOM_SEL_DS_3 (15)
```

相关声明：[HSIOM_SEL_DS_3](#a157da2f7e72fa8f19dfd682ec4444319)。

<a id="r_a3336f2e2d4886e0e46819ee4f4d96734"></a>

```c
#define HSIOM_SEL_ACT_4 (16)
```

相关声明：[HSIOM_SEL_ACT_4](#a3336f2e2d4886e0e46819ee4f4d96734)。

<a id="r_a1040ff80864b6a1d85eb4c07f4278ea1"></a>

```c
#define HSIOM_SEL_ACT_5 (17)
```

相关声明：[HSIOM_SEL_ACT_5](#a1040ff80864b6a1d85eb4c07f4278ea1)。

<a id="r_a575188296b25564faa9b3a3b4817b5e4"></a>

```c
#define HSIOM_SEL_ACT_6 (18)
```

相关声明：[HSIOM_SEL_ACT_6](#a575188296b25564faa9b3a3b4817b5e4)。

<a id="r_ae9c0f6360d56214106b09861eedb911a"></a>

```c
#define HSIOM_SEL_ACT_7 (19)
```

相关声明：[HSIOM_SEL_ACT_7](#ae9c0f6360d56214106b09861eedb911a)。

<a id="r_a8d36acbee0c4de7088ddc08a8b1c07a6"></a>

```c
#define HSIOM_SEL_ACT_8 (20)
```

相关声明：[HSIOM_SEL_ACT_8](#a8d36acbee0c4de7088ddc08a8b1c07a6)。

<a id="r_aff276e6f5cdc671648a428c22fc2776e"></a>

```c
#define HSIOM_SEL_ACT_9 (21)
```

相关声明：[HSIOM_SEL_ACT_9](#aff276e6f5cdc671648a428c22fc2776e)。

<a id="r_a42c5af47fba8b69dacb3064e332193fd"></a>

```c
#define HSIOM_SEL_ACT_10 (22)
```

相关声明：[HSIOM_SEL_ACT_10](#a42c5af47fba8b69dacb3064e332193fd)。

<a id="r_a48052c8dd78b1403de4d675571b7e6e2"></a>

```c
#define HSIOM_SEL_ACT_11 (23)
```

相关声明：[HSIOM_SEL_ACT_11](#a48052c8dd78b1403de4d675571b7e6e2)。

<a id="r_a6fc1302224b4d7585c25c3dc2ea340e7"></a>

```c
#define HSIOM_SEL_ACT_12 (24)
```

相关声明：[HSIOM_SEL_ACT_12](#a6fc1302224b4d7585c25c3dc2ea340e7)。

<a id="r_ae4fb8f65206098cace15b3e0f1c12a3e"></a>

```c
#define HSIOM_SEL_ACT_13 (25)
```

相关声明：[HSIOM_SEL_ACT_13](#ae4fb8f65206098cace15b3e0f1c12a3e)。

<a id="r_a7c3ffb4e79372b4cc4d1a7b4554911d5"></a>

```c
#define HSIOM_SEL_ACT_14 (26)
```

相关声明：[HSIOM_SEL_ACT_14](#a7c3ffb4e79372b4cc4d1a7b4554911d5)。

<a id="r_ab3285eea99f44cbe985eb097d1166a3d"></a>

```c
#define HSIOM_SEL_ACT_15 (27)
```

相关声明：[HSIOM_SEL_ACT_15](#ab3285eea99f44cbe985eb097d1166a3d)。

<a id="r_a0f134c65358e450ca55341bbfec1cd0e"></a>

```c
#define HSIOM_SEL_DS_4 (28)
```

相关声明：[HSIOM_SEL_DS_4](#a0f134c65358e450ca55341bbfec1cd0e)。

<a id="r_a4208fc8f94abf237d943bc5e8ffe3080"></a>

```c
#define HSIOM_SEL_DS_5 (29)
```

相关声明：[HSIOM_SEL_DS_5](#a4208fc8f94abf237d943bc5e8ffe3080)。

<a id="r_ac0153eaa52ef010bf58304a44ecb1e9b"></a>

```c
#define HSIOM_SEL_DS_6 (30)
```

相关声明：[HSIOM_SEL_DS_6](#ac0153eaa52ef010bf58304a44ecb1e9b)。

<a id="r_a8c067c1737f0f1573e056a384954fd81"></a>

```c
#define HSIOM_SEL_DS_7 (31)
```

相关声明：[HSIOM_SEL_DS_7](#a8c067c1737f0f1573e056a384954fd81)。

<a id="r_ac58363c207e4f8ea82394859044b2690"></a>

```c
#define DT_CAT1_DRIVE_MODE_INFO(peripheral_signal)
```

相关声明：[DT_CAT1_DRIVE_MODE_INFO](#ac58363c207e4f8ea82394859044b2690)。

设置驱动模式（Drive Mode）的宏。

<a id="r_a33b355e05d5b955a6b8d48f3613c2d9a"></a>

```c
#define DT_CAT1_PINMUX(port, pin, hsiom)
```

相关声明：[DT_CAT1_PINMUX](#a33b355e05d5b955a6b8d48f3613c2d9a)。

设置引脚控制信息（Pin Control Information）的宏，信息来自 `pinctrl` 节点。

<a id="r_ab8a42da049b5f4a26cc0e91e632b85d5"></a>

```c
#define IFX_SMIF0_PORT0 (22)
```

相关声明：[IFX_SMIF0_PORT0](#ab8a42da049b5f4a26cc0e91e632b85d5)。

SMIF 专用 GPIO 端口索引（Dedicated GPIO Port Indices），适用于 PSE84。

<a id="r_a0c8aedc6d6d16eb694876145bd3bf137"></a>

```c
#define IFX_SMIF0_PORT1 (23)
```

相关声明：[IFX_SMIF0_PORT1](#a0c8aedc6d6d16eb694876145bd3bf137)。

SMIF0 的 GPIO 端口 1 索引（Port Index）。

<a id="r_a6b2d4a7f10e6e4de19505a3508d54d88"></a>

```c
#define IFX_SMIF0_PORT2 (24)
```

相关声明：[IFX_SMIF0_PORT2](#a6b2d4a7f10e6e4de19505a3508d54d88)。

SMIF0 的 GPIO 端口 2 索引（Port Index）。

<a id="r_a09bddd7c8c977c8f9ac9da42047fb33e"></a>

```c
#define IFX_SMIF1_PORT0 (25)
```

相关声明：[IFX_SMIF1_PORT0](#a09bddd7c8c977c8f9ac9da42047fb33e)。

SMIF1 的 GPIO 端口 0 索引（Port Index）。

<a id="r_a8109be499432f246321fa93a5191e13c"></a>

```c
#define IFX_SMIF1_PORT1 (26)
```

相关声明：[IFX_SMIF1_PORT1](#a8109be499432f246321fa93a5191e13c)。

SMIF1 的 GPIO 端口 1 索引（Port Index）。

<a id="r_a7d8005363514238eb1785b25cad5c353"></a>

```c
#define IFX_SMIF1_PORT2 (27)
```

相关声明：[IFX_SMIF1_PORT2](#a7d8005363514238eb1785b25cad5c353)。

SMIF1 的 GPIO 端口 2 索引（Port Index）。

<a id="r_a1583b00a62bc1138f99bbfcd8ef81a6a"></a>

```c
#define P0 CYHAL_PORT_0
```

相关声明：[P0](#a1583b00a62bc1138f99bbfcd8ef81a6a)。

<a id="r_a6c2a9f7efd46f0160f3037869924d6ce"></a>

```c
#define P1 CYHAL_PORT_1
```

相关声明：[P1](#a6c2a9f7efd46f0160f3037869924d6ce)。

<a id="r_ae00a52dba55d31948c377fa85d385b87"></a>

```c
#define P2 CYHAL_PORT_2
```

相关声明：[P2](#ae00a52dba55d31948c377fa85d385b87)。

<a id="r_a0707a89c2f63bd260108e9dbb669358e"></a>

```c
#define P3 CYHAL_PORT_3
```

相关声明：[P3](#a0707a89c2f63bd260108e9dbb669358e)。

<a id="r_acbc14a33d017f5f2dabce1cb0d85718e"></a>

```c
#define P4 CYHAL_PORT_4
```

相关声明：[P4](#acbc14a33d017f5f2dabce1cb0d85718e)。

<a id="r_a49ce5f7954a95865f12be8083ccb2719"></a>

```c
#define P5 CYHAL_PORT_5
```

相关声明：[P5](#a49ce5f7954a95865f12be8083ccb2719)。

<a id="r_ab276be36e56dfdd17d860fbc82c3a22d"></a>

```c
#define P6 CYHAL_PORT_6
```

相关声明：[P6](#ab276be36e56dfdd17d860fbc82c3a22d)。

<a id="r_a017ae5a42bc27ff7402656a779fec303"></a>

```c
#define P7 CYHAL_PORT_7
```

相关声明：[P7](#a017ae5a42bc27ff7402656a779fec303)。

<a id="r_ae04365e5a91d08e332a28f00efe389fe"></a>

```c
#define P8 CYHAL_PORT_8
```

相关声明：[P8](#ae04365e5a91d08e332a28f00efe389fe)。

<a id="r_a8b201e09e2f1d58d8f3ad3a14c02b86b"></a>

```c
#define P9 CYHAL_PORT_9
```

相关声明：[P9](#a8b201e09e2f1d58d8f3ad3a14c02b86b)。

<a id="r_a5bb9f89248afa8d7e5a821fd459b085f"></a>

```c
#define P10 CYHAL_PORT_10
```

相关声明：[P10](#a5bb9f89248afa8d7e5a821fd459b085f)。

<a id="r_aca6db006bc37d2b337fca225a79856c8"></a>

```c
#define P11 CYHAL_PORT_11
```

相关声明：[P11](#aca6db006bc37d2b337fca225a79856c8)。

<a id="r_a20c70bba8105b63590b5a49d99f563b5"></a>

```c
#define P12 CYHAL_PORT_12
```

相关声明：[P12](#a20c70bba8105b63590b5a49d99f563b5)。

<a id="r_aa729f895b03c9230ebcf8c798f7bd1bb"></a>

```c
#define P13 CYHAL_PORT_13
```

相关声明：[P13](#aa729f895b03c9230ebcf8c798f7bd1bb)。

<a id="r_af108487a116bc015d7abd21ee2ab374e"></a>

```c
#define P14 CYHAL_PORT_14
```

相关声明：[P14](#af108487a116bc015d7abd21ee2ab374e)。

<a id="r_a3059522b4d1048ecf60259f3805147d6"></a>

```c
#define P15 CYHAL_PORT_15
```

相关声明：[P15](#a3059522b4d1048ecf60259f3805147d6)。

<a id="r_a0f8aefca2c1a1d922ca9ecac68caa584"></a>

```c
#define P16 CYHAL_PORT_16
```

相关声明：[P16](#a0f8aefca2c1a1d922ca9ecac68caa584)。

<a id="r_ac8f5bddb889a3da7918ae32ca6c5cc97"></a>

```c
#define P17 CYHAL_PORT_17
```

相关声明：[P17](#ac8f5bddb889a3da7918ae32ca6c5cc97)。

<a id="r_ae6f383959ce67f3403d4cf1e7aacb1cb"></a>

```c
#define P18 CYHAL_PORT_18
```

相关声明：[P18](#ae6f383959ce67f3403d4cf1e7aacb1cb)。

<a id="r_af04bd18711f898d17e1d28ac27b2064d"></a>

```c
#define P19 CYHAL_PORT_19
```

相关声明：[P19](#af04bd18711f898d17e1d28ac27b2064d)。

<a id="r_a33f788605a598e63ac41746fa80a2748"></a>

```c
#define P20 CYHAL_PORT_20
```

相关声明：[P20](#a33f788605a598e63ac41746fa80a2748)。

<a id="r_a19da54df2a9e4e46dd945bdbb56f276c"></a>

```c
#define DT_GET_CYHAL_GPIO_FROM_DT_GPIOS(node, gpios_prop)
```

相关声明：[DT_GET_CYHAL_GPIO_FROM_DT_GPIOS](#a19da54df2a9e4e46dd945bdbb56f276c)。

## 18.2\_详细说明（Detailed Documentation）

<a id="ac58363c207e4f8ea82394859044b2690"></a>

### `DT_CAT1_DRIVE_MODE_INFO`

```c
#define DT_CAT1_DRIVE_MODE_INFO ( peripheral_signal)
```

展开值（Value）：

```c
CAT1_PIN_MAP_DRIVE_MODE_##peripheral_signal
```

设置驱动模式（Drive Mode）的宏。

<a id="a33b355e05d5b955a6b8d48f3613c2d9a"></a>

### `DT_CAT1_PINMUX`

```c
#define DT_CAT1_PINMUX ( port, pin, hsiom )
```

展开值（Value）：

```c
((port << SOC_PINMUX_PORT_POS) | \
 (pin << SOC_PINMUX_PIN_POS) |   \
 (hsiom << SOC_PINMUX_HSIOM_FUNC_POS))
```

设置引脚控制信息（Pin Control Information）的宏，信息来自 `pinctrl` 节点。

<a id="a19da54df2a9e4e46dd945bdbb56f276c"></a>

### `DT_GET_CYHAL_GPIO_FROM_DT_GPIOS`

```c
#define DT_GET_CYHAL_GPIO_FROM_DT_GPIOS ( node, gpios_prop )
```

展开值（Value）：

```c
CYHAL_GET_GPIO(                                                            \
        (DT_REG_ADDR_BY_IDX(DT_GPIO_CTLR_BY_IDX(node, gpios_prop, 0), 0) - \
         DT_REG_ADDR_BY_IDX(DT_NODELABEL(gpio_prt0), 0)) /                 \
        DT_REG_ADDR_BY_IDX(DT_NODELABEL(gpio_prt0), 1),                    \
        DT_PHA_BY_IDX(node, gpios_prop, 0, pin)                            \
        )
```

<a id="a3080ad4afafa572482ea1a5b49f6a1ce"></a>

### `HSIOM_SEL_ACT_0`

```c
#define HSIOM_SEL_ACT_0 (8)
```

<a id="a990e35fecfcc37ca08fe709eee746618"></a>

### `HSIOM_SEL_ACT_1`

```c
#define HSIOM_SEL_ACT_1 (9)
```

<a id="a42c5af47fba8b69dacb3064e332193fd"></a>

### `HSIOM_SEL_ACT_10`

```c
#define HSIOM_SEL_ACT_10 (22)
```

<a id="a48052c8dd78b1403de4d675571b7e6e2"></a>

### `HSIOM_SEL_ACT_11`

```c
#define HSIOM_SEL_ACT_11 (23)
```

<a id="a6fc1302224b4d7585c25c3dc2ea340e7"></a>

### `HSIOM_SEL_ACT_12`

```c
#define HSIOM_SEL_ACT_12 (24)
```

<a id="ae4fb8f65206098cace15b3e0f1c12a3e"></a>

### `HSIOM_SEL_ACT_13`

```c
#define HSIOM_SEL_ACT_13 (25)
```

<a id="a7c3ffb4e79372b4cc4d1a7b4554911d5"></a>

### `HSIOM_SEL_ACT_14`

```c
#define HSIOM_SEL_ACT_14 (26)
```

<a id="ab3285eea99f44cbe985eb097d1166a3d"></a>

### `HSIOM_SEL_ACT_15`

```c
#define HSIOM_SEL_ACT_15 (27)
```

<a id="a696aeb76109bf339ebf0fcd20979f211"></a>

### `HSIOM_SEL_ACT_2`

```c
#define HSIOM_SEL_ACT_2 (10)
```

<a id="a25e956bc540c9570392a1722b7e94670"></a>

### `HSIOM_SEL_ACT_3`

```c
#define HSIOM_SEL_ACT_3 (11)
```

<a id="a3336f2e2d4886e0e46819ee4f4d96734"></a>

### `HSIOM_SEL_ACT_4`

```c
#define HSIOM_SEL_ACT_4 (16)
```

<a id="a1040ff80864b6a1d85eb4c07f4278ea1"></a>

### `HSIOM_SEL_ACT_5`

```c
#define HSIOM_SEL_ACT_5 (17)
```

<a id="a575188296b25564faa9b3a3b4817b5e4"></a>

### `HSIOM_SEL_ACT_6`

```c
#define HSIOM_SEL_ACT_6 (18)
```

<a id="ae9c0f6360d56214106b09861eedb911a"></a>

### `HSIOM_SEL_ACT_7`

```c
#define HSIOM_SEL_ACT_7 (19)
```

<a id="a8d36acbee0c4de7088ddc08a8b1c07a6"></a>

### `HSIOM_SEL_ACT_8`

```c
#define HSIOM_SEL_ACT_8 (20)
```

<a id="aff276e6f5cdc671648a428c22fc2776e"></a>

### `HSIOM_SEL_ACT_9`

```c
#define HSIOM_SEL_ACT_9 (21)
```

<a id="a8806729fcb666c9de823be5dd55c873d"></a>

### `HSIOM_SEL_AMUXA`

```c
#define HSIOM_SEL_AMUXA (4)
```

<a id="a4ba8695f92c0f347dd25ef981d67d1b0"></a>

### `HSIOM_SEL_AMUXA_DSI`

```c
#define HSIOM_SEL_AMUXA_DSI (6)
```

<a id="a862eb93443c5c9575ff990b776b6203b"></a>

### `HSIOM_SEL_AMUXB`

```c
#define HSIOM_SEL_AMUXB (5)
```

<a id="af7a28a087a8867a14423e9ab471cce54"></a>

### `HSIOM_SEL_AMUXB_DSI`

```c
#define HSIOM_SEL_AMUXB_DSI (7)
```

<a id="afb33417be16e7fa6423fadd2ef4a0f5b"></a>

### `HSIOM_SEL_DS_0`

```c
#define HSIOM_SEL_DS_0 (12)
```

<a id="aa06be65ae17fc2dc1861c2af2e364652"></a>

### `HSIOM_SEL_DS_1`

```c
#define HSIOM_SEL_DS_1 (13)
```

<a id="a07f591dc1f8a9f9eda13063d8c58c4eb"></a>

### `HSIOM_SEL_DS_2`

```c
#define HSIOM_SEL_DS_2 (14)
```

<a id="a157da2f7e72fa8f19dfd682ec4444319"></a>

### `HSIOM_SEL_DS_3`

```c
#define HSIOM_SEL_DS_3 (15)
```

<a id="a0f134c65358e450ca55341bbfec1cd0e"></a>

### `HSIOM_SEL_DS_4`

```c
#define HSIOM_SEL_DS_4 (28)
```

<a id="a4208fc8f94abf237d943bc5e8ffe3080"></a>

### `HSIOM_SEL_DS_5`

```c
#define HSIOM_SEL_DS_5 (29)
```

<a id="ac0153eaa52ef010bf58304a44ecb1e9b"></a>

### `HSIOM_SEL_DS_6`

```c
#define HSIOM_SEL_DS_6 (30)
```

<a id="a8c067c1737f0f1573e056a384954fd81"></a>

### `HSIOM_SEL_DS_7`

```c
#define HSIOM_SEL_DS_7 (31)
```

<a id="a959873e5156c6e3c24dd2773bb1ba516"></a>

### `HSIOM_SEL_DSI_DSI`

```c
#define HSIOM_SEL_DSI_DSI (2)
```

<a id="a022f7af586ee9b46f689d187e8dd73d8"></a>

### `HSIOM_SEL_DSI_GPIO`

```c
#define HSIOM_SEL_DSI_GPIO (3)
```

<a id="ac0d2af1bfb229de155412af7f00e4fe0"></a>

### `HSIOM_SEL_GPIO`

```c
#define HSIOM_SEL_GPIO (0)
```

使用 HSIOM SEL 定义功能（Functions）。

<a id="a441de7f56a1c7c75cdae4d9f93ccfade"></a>

### `HSIOM_SEL_GPIO_DSI`

```c
#define HSIOM_SEL_GPIO_DSI (1)
```

<a id="ab8a42da049b5f4a26cc0e91e632b85d5"></a>

### `IFX_SMIF0_PORT0`

```c
#define IFX_SMIF0_PORT0 (22)
```

SMIF 专用 GPIO 端口索引（Dedicated GPIO Port Indices），适用于 PSE84。

SMIF 数据／时钟引脚位于 SMIF 模块内部的专用 GPIO 端口（`SMIF{0,1}_CORE_SMIF_GPIO_SMIF_PRT{0,1,2}`），独立于标准 IOSS GPIO 端口。Infineon 引脚控制驱动（Pinctrl Driver）将这些索引映射到 SMIF 端口基地址，使设备树 `pinctrl-0` 条目能够指向 SMIF 引脚。此项为 SMIF0 的 GPIO 端口 0 索引。

<a id="a0c8aedc6d6d16eb694876145bd3bf137"></a>

### `IFX_SMIF0_PORT1`

```c
#define IFX_SMIF0_PORT1 (23)
```

SMIF0 的 GPIO 端口 1 索引（Port Index）。

<a id="a6b2d4a7f10e6e4de19505a3508d54d88"></a>

### `IFX_SMIF0_PORT2`

```c
#define IFX_SMIF0_PORT2 (24)
```

SMIF0 的 GPIO 端口 2 索引（Port Index）。

<a id="a09bddd7c8c977c8f9ac9da42047fb33e"></a>

### `IFX_SMIF1_PORT0`

```c
#define IFX_SMIF1_PORT0 (25)
```

SMIF1 的 GPIO 端口 0 索引（Port Index）。

<a id="a8109be499432f246321fa93a5191e13c"></a>

### `IFX_SMIF1_PORT1`

```c
#define IFX_SMIF1_PORT1 (26)
```

SMIF1 的 GPIO 端口 1 索引（Port Index）。

<a id="a7d8005363514238eb1785b25cad5c353"></a>

### `IFX_SMIF1_PORT2`

```c
#define IFX_SMIF1_PORT2 (27)
```

SMIF1 的 GPIO 端口 2 索引（Port Index）。

<a id="a1583b00a62bc1138f99bbfcd8ef81a6a"></a>

### `P0`

```c
#define P0 CYHAL_PORT_0
```

<a id="a6c2a9f7efd46f0160f3037869924d6ce"></a>

### `P1`

```c
#define P1 CYHAL_PORT_1
```

<a id="a5bb9f89248afa8d7e5a821fd459b085f"></a>

### `P10`

```c
#define P10 CYHAL_PORT_10
```

<a id="aca6db006bc37d2b337fca225a79856c8"></a>

### `P11`

```c
#define P11 CYHAL_PORT_11
```

<a id="a20c70bba8105b63590b5a49d99f563b5"></a>

### `P12`

```c
#define P12 CYHAL_PORT_12
```

<a id="aa729f895b03c9230ebcf8c798f7bd1bb"></a>

### `P13`

```c
#define P13 CYHAL_PORT_13
```

<a id="af108487a116bc015d7abd21ee2ab374e"></a>

### `P14`

```c
#define P14 CYHAL_PORT_14
```

<a id="a3059522b4d1048ecf60259f3805147d6"></a>

### `P15`

```c
#define P15 CYHAL_PORT_15
```

<a id="a0f8aefca2c1a1d922ca9ecac68caa584"></a>

### `P16`

```c
#define P16 CYHAL_PORT_16
```

<a id="ac8f5bddb889a3da7918ae32ca6c5cc97"></a>

### `P17`

```c
#define P17 CYHAL_PORT_17
```

<a id="ae6f383959ce67f3403d4cf1e7aacb1cb"></a>

### `P18`

```c
#define P18 CYHAL_PORT_18
```

<a id="af04bd18711f898d17e1d28ac27b2064d"></a>

### `P19`

```c
#define P19 CYHAL_PORT_19
```

<a id="ae00a52dba55d31948c377fa85d385b87"></a>

### `P2`

```c
#define P2 CYHAL_PORT_2
```

<a id="a33f788605a598e63ac41746fa80a2748"></a>

### `P20`

```c
#define P20 CYHAL_PORT_20
```

<a id="a0707a89c2f63bd260108e9dbb669358e"></a>

### `P3`

```c
#define P3 CYHAL_PORT_3
```

<a id="acbc14a33d017f5f2dabce1cb0d85718e"></a>

### `P4`

```c
#define P4 CYHAL_PORT_4
```

<a id="a49ce5f7954a95865f12be8083ccb2719"></a>

### `P5`

```c
#define P5 CYHAL_PORT_5
```

<a id="ab276be36e56dfdd17d860fbc82c3a22d"></a>

### `P6`

```c
#define P6 CYHAL_PORT_6
```

<a id="a017ae5a42bc27ff7402656a779fec303"></a>

### `P7`

```c
#define P7 CYHAL_PORT_7
```

<a id="ae04365e5a91d08e332a28f00efe389fe"></a>

### `P8`

```c
#define P8 CYHAL_PORT_8
```

<a id="a8b201e09e2f1d58d8f3ad3a14c02b86b"></a>

### `P9`

```c
#define P9 CYHAL_PORT_9
```

<a id="a2af56d2b85a6e4ba3a2f1fdd191f8c98"></a>

### `SOC_PINMUX_HSIOM_FUNC_POS`

```c
#define SOC_PINMUX_HSIOM_FUNC_POS (16)
```

<a id="a6baa74b565ac921b7e3b8b5fc65327a6"></a>

### `SOC_PINMUX_HSIOM_MASK`

```c
#define SOC_PINMUX_HSIOM_MASK (0xFFul << SOC_PINMUX_HSIOM_FUNC_POS)
```

<a id="a881a5ee83663d0eac3a2cfd530e23266"></a>

### `SOC_PINMUX_PIN_MASK`

```c
#define SOC_PINMUX_PIN_MASK (0xFFul << SOC_PINMUX_PIN_POS)
```

<a id="a5266efcdc6dbcd64d8fc61c814b37dc7"></a>

### `SOC_PINMUX_PIN_POS`

```c
#define SOC_PINMUX_PIN_POS (8)
```

<a id="a4199ffda078d925e8dfb58194117de1a"></a>

### `SOC_PINMUX_PORT_MASK`

```c
#define SOC_PINMUX_PORT_MASK (0xFFul << SOC_PINMUX_PORT_POS)
```

<a id="a6ba3e93a5498c6c5bd5e8f3d0c00ac2a"></a>

### `SOC_PINMUX_PORT_POS`

```c
#define SOC_PINMUX_PORT_POS (0)
```

引脚控制绑定辅助接口（Pin Control Binding Helper）。

`PINMUX` 字段中的位定义（Bit Definition）。

<a id="aca26c39aa27a6520ea0f57b7ab058672"></a>

### `SOC_PINMUX_SIGNAL_MASK`

```c
#define SOC_PINMUX_SIGNAL_MASK (0xFFul << SOC_PINMUX_SIGNAL_POS)
```

<a id="a38673a696cc1caa97e13eb6ef937007a"></a>

### `SOC_PINMUX_SIGNAL_POS`

```c
#define SOC_PINMUX_SIGNAL_POS (24)
```


## 18.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_runtime_reference/P031_ifx_cat1-pinctrl.h_源码浏览.md)
- [DT_REG_ADDR_BY_IDX](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac540b00bb12d0662f6aefe6ac0cff243)
- [DT_GPIO_CTLR_BY_IDX](../hardware/P290_设备树GPIO宏.md#ga97bd46d2ab88d392a3f336f4d23184eb)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_PHA_BY_IDX](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="aifx__cat1-pinctrl_8h_html_a2af56d2b85a6e4ba3a2f1fdd191f8c98"></a>
<a id="aifx__cat1-pinctrl_8h_html_a5266efcdc6dbcd64d8fc61c814b37dc7"></a>
<a id="aifx__cat1-pinctrl_8h_html_a6ba3e93a5498c6c5bd5e8f3d0c00ac2a"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__devicetree-generic-prop_html_ga118b63fd22c20ef940ac2fa073c126ed"></a>
<a id="agroup__devicetree-gpio_html_ga97bd46d2ab88d392a3f336f4d23184eb"></a>
<a id="agroup__devicetree-reg-prop_html_gac540b00bb12d0662f6aefe6ac0cff243"></a>

---

[上一章](P017_zephyr__dt-bindings__sensor__icm42688.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__drivers__interrupt_controller__intc_rz_tint.h_文件参考.md)
