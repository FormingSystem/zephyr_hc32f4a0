---
id: learning.zephyr-docs.api-file-flash-test-reference.page-14
title: zephyr__dt-bindings__pinctrl__syna-sr100-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_syna-sr100-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/syna-sr100-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

列出Synaptics SR100系列的引脚控制子系统ID（Pinctrl Subsystem IDs）。

查看此文件的源码。

<a id="details"></a>

列出Synaptics SR100系列的引脚控制子系统ID（Pinctrl Subsystem IDs）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_a7b2628d7cb17023b0200bdf053f75eaa"></a>

```c
#define SRXXX_CTRL_SHIFT 0U
```

相关声明：[SRXXX_CTRL_SHIFT](#a7b2628d7cb17023b0200bdf053f75eaa)。

引脚控制器标识符（Pin Controller ID）、位位置（Bit Position）、模式（Mode）、引脚复用寄存器（Pinmux Register）的掩码与偏移量，以及配置寄存器（Configuration Register）的偏移量。

<a id="r_a96200978617f8bbdb42f80091eb74664"></a>

```c
#define SRXXX_CTRL_MASK 0x07U
```

相关声明：[SRXXX_CTRL_MASK](#a96200978617f8bbdb42f80091eb74664)。

CTRL 字段（Field）掩码（Mask）。

<a id="r_ac760e512f303513b38d26105cd73bdba"></a>

```c
#define SRXXX_BIT_SHIFT 3U
```

相关声明：[SRXXX_BIT_SHIFT](#ac760e512f303513b38d26105cd73bdba)。

BIT 字段（Field）位移量（Shift）。

<a id="r_af681f1c4c9474fd45d297136e03448b5"></a>

```c
#define SRXXX_BIT_MASK 0x1FU
```

相关声明：[SRXXX_BIT_MASK](#af681f1c4c9474fd45d297136e03448b5)。

BIT 字段（Field）掩码（Mask）。

<a id="r_ac9633a8e165a4a4f88b2f5380e52c5c0"></a>

```c
#define SRXXX_MODE_SHIFT 8U
```

相关声明：[SRXXX_MODE_SHIFT](#ac9633a8e165a4a4f88b2f5380e52c5c0)。

MODE 字段（Field）位移量（Shift）。

<a id="r_ab07c9da843d474783e400c73403f2b9f"></a>

```c
#define SRXXX_MODE_MASK 0x07U
```

相关声明：[SRXXX_MODE_MASK](#ab07c9da843d474783e400c73403f2b9f)。

MODE 字段（Field）掩码（Mask）。

<a id="r_a057beb763afece7ae6b4513d89bb0fa5"></a>

```c
#define SRXXX_MASK_SHIFT 11U
```

相关声明：[SRXXX_MASK_SHIFT](#a057beb763afece7ae6b4513d89bb0fa5)。

MASK 字段（Field）位移量（Shift）。

<a id="r_ab8ec283b471be3cc74f936f73a07ef1b"></a>

```c
#define SRXXX_MASK_MASK 0x0FU
```

相关声明：[SRXXX_MASK_MASK](#ab8ec283b471be3cc74f936f73a07ef1b)。

MASK 字段（Field）掩码（Mask）。

<a id="r_a223dd18f4ee640278d9a7a7b8418f8ae"></a>

```c
#define SRXXX_REG_SHIFT 16U
```

相关声明：[SRXXX_REG_SHIFT](#a223dd18f4ee640278d9a7a7b8418f8ae)。

REG 字段（Field）位移量（Shift）。

<a id="r_aef966134bfa32c57925db5a2ff77d524"></a>

```c
#define SRXXX_REG_MASK 0xFFU
```

相关声明：[SRXXX_REG_MASK](#aef966134bfa32c57925db5a2ff77d524)。

REG 字段（Field）掩码（Mask）。

<a id="r_a3b88b5b8791bdea8ba11e7def0afef6b"></a>

```c
#define SRXXX_CFG_SHIFT 24U
```

相关声明：[SRXXX_CFG_SHIFT](#a3b88b5b8791bdea8ba11e7def0afef6b)。

CFG 字段（Field）位移量（Shift）。

<a id="r_ab44db4747fda930cbffd1df30a3e3159"></a>

```c
#define SRXXX_CFG_MASK 0xFFU
```

相关声明：[SRXXX_CFG_MASK](#ab44db4747fda930cbffd1df30a3e3159)。

CFG 字段（Field）掩码（Mask）。

<a id="r_a4bc4377e22ec53033ac7938096aeaa4a"></a>

```c
#define SRXXX_PINMUX(ctrl, reg, bit, mode, mask, cfg)
```

相关声明：[SRXXX_PINMUX](#a4bc4377e22ec53033ac7938096aeaa4a)。

引脚配置位域（Pin Configuration Bit Field）。

<a id="r_ae3c27fcc4a255825d699f93bf195ccf9"></a>

```c
#define SRXXX_GLOBAL_PINMUX(reg, bit, mode, cfg)
```

相关声明：[SRXXX_GLOBAL_PINMUX](#ae3c27fcc4a255825d699f93bf195ccf9)。

用于引脚复用选择（Pinmux Selection）的宏。

<a id="r_a4719e1d8797325d722edaf88c89065e0"></a>

```c
#define SRXXX_AON_PINMUX(reg, bit, mode, cfg)
```

相关声明：[SRXXX_AON_PINMUX](#a4719e1d8797325d722edaf88c89065e0)。

常开域（AON）。

<a id="r_a0c5a55a86eed5672fc36abc5052386d6"></a>

```c
#define SRXXX_LPS_PINMUX(reg, bit, mode, cfg)
```

相关声明：[SRXXX_LPS_PINMUX](#a0c5a55a86eed5672fc36abc5052386d6)。

LPS。

<a id="r_a9e61841582b0cb34909036aa9f3cc138"></a>

```c
#define SRXXX_SWIRE_PINMUX(bit, mode)
```

相关声明：[SRXXX_SWIRE_PINMUX](#a9e61841582b0cb34909036aa9f3cc138)。

SoundWire。

<a id="r_a0fb9ee3cd89b303414f62aef4c0f7ad4"></a>

```c
#define SRXXX_PORT_PINMUX(reg, bit, mode, mask)
```

相关声明：[SRXXX_PORT_PINMUX](#a0fb9ee3cd89b303414f62aef4c0f7ad4)。

用于端口选择（Port Selection）的宏。

<a id="r_ad051b92984413bec38a55fd02be0b1db"></a>

```c
#define SRXXX_FIXED_PINMUX(cfg)
```

相关声明：[SRXXX_FIXED_PINMUX](#ad051b92984413bec38a55fd02be0b1db)。

用于固定引脚复用（Fixed Pinmux）的宏。

<a id="r_a324b2ea911f6f5ba79b33ecdf7d2a26c"></a>

```c
#define SRXXX_PINMUX_CTRL(pinmux)
```

相关声明：[SRXXX_PINMUX_CTRL](#a324b2ea911f6f5ba79b33ecdf7d2a26c)。

寄存器字段辅助宏（Register Field Helpers）。

<a id="r_aaa85a363747ab2d02065ccbd1fc66ab9"></a>

```c
#define SRXXX_PINMUX_REG(pinmux)
```

相关声明：[SRXXX_PINMUX_REG](#aaa85a363747ab2d02065ccbd1fc66ab9)。

REG 字段（Field）。

<a id="r_a3b7d388975ec27f0b1f23e5f15f50978"></a>

```c
#define SRXXX_PINMUX_BIT(pinmux)
```

相关声明：[SRXXX_PINMUX_BIT](#a3b7d388975ec27f0b1f23e5f15f50978)。

BIT 字段（Field）。

<a id="r_a86eec0530a079db5f113f8f75eb0126f"></a>

```c
#define SRXXX_PINMUX_MODE(pinmux)
```

相关声明：[SRXXX_PINMUX_MODE](#a86eec0530a079db5f113f8f75eb0126f)。

MODE 字段（Field）。

<a id="r_a6f061098bc7c6e3d79873c226ebd941e"></a>

```c
#define SRXXX_PINMUX_MASK(pinmux)
```

相关声明：[SRXXX_PINMUX_MASK](#a6f061098bc7c6e3d79873c226ebd941e)。

MASK 字段（Field）。

<a id="r_a2c45e2bb1e68614706cc9eab7a075401"></a>

```c
#define SRXXX_PINMUX_CFG(pinmux)
```

相关声明：[SRXXX_PINMUX_CFG](#a2c45e2bb1e68614706cc9eab7a075401)。

CFG 字段（Field）。

## 14.2\_详细说明（Detailed Documentation）

<a id="a4719e1d8797325d722edaf88c89065e0"></a>

### `SRXXX_AON_PINMUX`

```c
#define SRXXX_AON_PINMUX ( reg, bit, mode, cfg )
```

展开值（Value）：

```c
SRXXX_PINMUX(1, reg, bit, mode, 7, cfg)
```

常开域（AON）。

<a id="af681f1c4c9474fd45d297136e03448b5"></a>

### `SRXXX_BIT_MASK`

```c
#define SRXXX_BIT_MASK 0x1FU
```

BIT 字段（Field）掩码（Mask）。

<a id="ac760e512f303513b38d26105cd73bdba"></a>

### `SRXXX_BIT_SHIFT`

```c
#define SRXXX_BIT_SHIFT 3U
```

BIT 字段（Field）位移量（Shift）。

<a id="ab44db4747fda930cbffd1df30a3e3159"></a>

### `SRXXX_CFG_MASK`

```c
#define SRXXX_CFG_MASK 0xFFU
```

CFG 字段（Field）掩码（Mask）。

<a id="a3b88b5b8791bdea8ba11e7def0afef6b"></a>

### `SRXXX_CFG_SHIFT`

```c
#define SRXXX_CFG_SHIFT 24U
```

CFG 字段（Field）位移量（Shift）。

<a id="a96200978617f8bbdb42f80091eb74664"></a>

### `SRXXX_CTRL_MASK`

```c
#define SRXXX_CTRL_MASK 0x07U
```

CTRL 字段（Field）掩码（Mask）。

<a id="a7b2628d7cb17023b0200bdf053f75eaa"></a>

### `SRXXX_CTRL_SHIFT`

```c
#define SRXXX_CTRL_SHIFT 0U
```

引脚控制器标识符（Pin Controller ID）、位位置（Bit Position）、模式（Mode）、引脚复用寄存器（Pinmux Register）的掩码与偏移量，以及配置寄存器（Configuration Register）的偏移量。

CTRL 字段（Field）位移量（Shift）。

<a id="ad051b92984413bec38a55fd02be0b1db"></a>

### `SRXXX_FIXED_PINMUX`

```c
#define SRXXX_FIXED_PINMUX ( cfg)
```

展开值（Value）：

```c
SRXXX_PINMUX(0, 0, 0, 0, 0, cfg)
```

用于固定引脚复用（Fixed Pinmux）的宏。

<a id="ae3c27fcc4a255825d699f93bf195ccf9"></a>

### `SRXXX_GLOBAL_PINMUX`

```c
#define SRXXX_GLOBAL_PINMUX ( reg, bit, mode, cfg )
```

展开值（Value）：

```c
SRXXX_PINMUX(0, reg, bit, mode, 7, cfg)
```

用于引脚复用选择（Pinmux Selection）的宏。

全局（Global）。

<a id="a0c5a55a86eed5672fc36abc5052386d6"></a>

### `SRXXX_LPS_PINMUX`

```c
#define SRXXX_LPS_PINMUX ( reg, bit, mode, cfg )
```

展开值（Value）：

```c
SRXXX_PINMUX(2, reg, bit, mode, 7, cfg)
```

LPS。

<a id="ab8ec283b471be3cc74f936f73a07ef1b"></a>

### `SRXXX_MASK_MASK`

```c
#define SRXXX_MASK_MASK 0x0FU
```

MASK 字段（Field）掩码（Mask）。

<a id="a057beb763afece7ae6b4513d89bb0fa5"></a>

### `SRXXX_MASK_SHIFT`

```c
#define SRXXX_MASK_SHIFT 11U
```

MASK 字段（Field）位移量（Shift）。

<a id="ab07c9da843d474783e400c73403f2b9f"></a>

### `SRXXX_MODE_MASK`

```c
#define SRXXX_MODE_MASK 0x07U
```

MODE 字段（Field）掩码（Mask）。

<a id="ac9633a8e165a4a4f88b2f5380e52c5c0"></a>

### `SRXXX_MODE_SHIFT`

```c
#define SRXXX_MODE_SHIFT 8U
```

MODE 字段（Field）位移量（Shift）。

<a id="a4bc4377e22ec53033ac7938096aeaa4a"></a>

### `SRXXX_PINMUX`

```c
#define SRXXX_PINMUX ( ctrl, reg, bit, mode, mask, cfg )
```

展开值（Value）：

```c
((((ctrl) & SRXXX_CTRL_MASK) << SRXXX_CTRL_SHIFT) | \
 (((reg)  & SRXXX_REG_MASK)  << SRXXX_REG_SHIFT)  | \
 (((bit)  & SRXXX_BIT_MASK)  << SRXXX_BIT_SHIFT)  | \
 (((mode) & SRXXX_MODE_MASK) << SRXXX_MODE_SHIFT) | \
 (((mask) & SRXXX_MASK_MASK) << SRXXX_MASK_SHIFT) | \
 (((cfg)  & SRXXX_CFG_MASK)  << SRXXX_CFG_SHIFT))
```

引脚配置位域（Pin Configuration Bit Field）。

对固定引脚（Fixed Pins，XSPI），将掩码设置为 0。

字段（Fields）：

- ctrl 字段（Field）：位 [0:2]。
- bit 字段（Field）：位 [3:7]。
- mode 字段（Field）：位 [8:10]。
- mask 字段（Field）：位 [11:14]。
- reg 字段（Field）：位 [16:23]。
- cfg 字段（Field）：位 [24:31]。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctrl` | 控制器（Controller）：0 表示 Global，1 表示 AON-Main，2 表示 LPS_Gear1，3 表示 SWIRE。 |
| `bit` | 寄存器内的位偏移量（Bit Offset），范围为 0..27。 |
| `mode` | 复用选项（Muxing Option），范围为 0..7。 |
| `mask` | 复用选项的位掩码（Bit Mask），范围为 1..7。 |
| `reg` | 相对于 pinmux 基地址的寄存器偏移量（Register Offset），范围为 0..255。 |
| `cfg` | 相对于 pincfg 基地址的寄存器偏移量（Register Offset），范围为 0..255。 |

<a id="a3b7d388975ec27f0b1f23e5f15f50978"></a>

### `SRXXX_PINMUX_BIT`

```c
#define SRXXX_PINMUX_BIT ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_BIT_SHIFT) & SRXXX_BIT_MASK)
```

BIT 字段（Field）。

<a id="a2c45e2bb1e68614706cc9eab7a075401"></a>

### `SRXXX_PINMUX_CFG`

```c
#define SRXXX_PINMUX_CFG ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_CFG_SHIFT) & SRXXX_CFG_MASK)
```

CFG 字段（Field）。

<a id="a324b2ea911f6f5ba79b33ecdf7d2a26c"></a>

### `SRXXX_PINMUX_CTRL`

```c
#define SRXXX_PINMUX_CTRL ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_CTRL_SHIFT) & SRXXX_CTRL_MASK)
```

寄存器字段辅助宏（Register Field Helpers）。

CTRL 字段（Field）。

<a id="a6f061098bc7c6e3d79873c226ebd941e"></a>

### `SRXXX_PINMUX_MASK`

```c
#define SRXXX_PINMUX_MASK ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_MASK_SHIFT) & SRXXX_MASK_MASK)
```

MASK 字段（Field）。

<a id="a86eec0530a079db5f113f8f75eb0126f"></a>

### `SRXXX_PINMUX_MODE`

```c
#define SRXXX_PINMUX_MODE ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_MODE_SHIFT) & SRXXX_MODE_MASK)
```

MODE 字段（Field）。

<a id="aaa85a363747ab2d02065ccbd1fc66ab9"></a>

### `SRXXX_PINMUX_REG`

```c
#define SRXXX_PINMUX_REG ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> SRXXX_REG_SHIFT) & SRXXX_REG_MASK)
```

REG 字段（Field）。

<a id="a0fb9ee3cd89b303414f62aef4c0f7ad4"></a>

### `SRXXX_PORT_PINMUX`

```c
#define SRXXX_PORT_PINMUX ( reg, bit, mode, mask )
```

展开值（Value）：

```c
SRXXX_PINMUX(4, reg, bit, mode, mask, 0)
```

用于端口选择（Port Selection）的宏。

<a id="aef966134bfa32c57925db5a2ff77d524"></a>

### `SRXXX_REG_MASK`

```c
#define SRXXX_REG_MASK 0xFFU
```

REG 字段（Field）掩码（Mask）。

<a id="a223dd18f4ee640278d9a7a7b8418f8ae"></a>

### `SRXXX_REG_SHIFT`

```c
#define SRXXX_REG_SHIFT 16U
```

REG 字段（Field）位移量（Shift）。

<a id="a9e61841582b0cb34909036aa9f3cc138"></a>

### `SRXXX_SWIRE_PINMUX`

```c
#define SRXXX_SWIRE_PINMUX ( bit, mode )
```

展开值（Value）：

```c
SRXXX_PINMUX(3, 0, bit, mode, 1, 0)
```

SoundWire。


## 14.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P848_syna-sr100-pinctrl.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="asyna-sr100-pinctrl_8h_html_a4bc4377e22ec53033ac7938096aeaa4a"></a>
<a id="asyna-sr100-pinctrl_8h_html_a057beb763afece7ae6b4513d89bb0fa5"></a>
<a id="asyna-sr100-pinctrl_8h_html_a223dd18f4ee640278d9a7a7b8418f8ae"></a>
<a id="asyna-sr100-pinctrl_8h_html_a3b88b5b8791bdea8ba11e7def0afef6b"></a>
<a id="asyna-sr100-pinctrl_8h_html_a7b2628d7cb17023b0200bdf053f75eaa"></a>
<a id="asyna-sr100-pinctrl_8h_html_a96200978617f8bbdb42f80091eb74664"></a>
<a id="asyna-sr100-pinctrl_8h_html_ab07c9da843d474783e400c73403f2b9f"></a>
<a id="asyna-sr100-pinctrl_8h_html_ab44db4747fda930cbffd1df30a3e3159"></a>
<a id="asyna-sr100-pinctrl_8h_html_ab8ec283b471be3cc74f936f73a07ef1b"></a>
<a id="asyna-sr100-pinctrl_8h_html_ac760e512f303513b38d26105cd73bdba"></a>
<a id="asyna-sr100-pinctrl_8h_html_ac9633a8e165a4a4f88b2f5380e52c5c0"></a>
<a id="asyna-sr100-pinctrl_8h_html_aef966134bfa32c57925db5a2ff77d524"></a>
<a id="asyna-sr100-pinctrl_8h_html_af681f1c4c9474fd45d297136e03448b5"></a>

---

[上一章](P013_zephyr__dt-bindings__clock__silabs__siwx91x-clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__dt-bindings__pinctrl__tiva-c-pinctrl.h_文件参考.md)
