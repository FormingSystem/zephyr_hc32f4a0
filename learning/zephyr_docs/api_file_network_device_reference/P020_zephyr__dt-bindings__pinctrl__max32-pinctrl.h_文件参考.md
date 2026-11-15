---
id: learning.zephyr-docs.api-file-network-device-reference.page-20
title: zephyr__dt-bindings__pinctrl__max32-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_max32-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/max32-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_a7087cd825f7f43739fa57ce0a4e4297d"></a>

```c
#define MAX32_MODE_GPIO 0x00
```

相关声明：[MAX32_MODE_GPIO](#a7087cd825f7f43739fa57ce0a4e4297d)。

引脚模式（Pin Modes）。

<a id="r_a4e3439dc886a1ed097d698847ab3cb92"></a>

```c
#define MAX32_MODE_AF1 0x01
```

相关声明：[MAX32_MODE_AF1](#a4e3439dc886a1ed097d698847ab3cb92)。

<a id="r_af4e13cd1ef71b77ae882aadb467e5115"></a>

```c
#define MAX32_MODE_AF2 0x02
```

相关声明：[MAX32_MODE_AF2](#af4e13cd1ef71b77ae882aadb467e5115)。

<a id="r_a33afd156fac8c0ccb588230b3f787947"></a>

```c
#define MAX32_MODE_AF3 0x03
```

相关声明：[MAX32_MODE_AF3](#a33afd156fac8c0ccb588230b3f787947)。

<a id="r_a6112caaab6ce78c337c40adfa1977a90"></a>

```c
#define MAX32_MODE_AF4 0x04
```

相关声明：[MAX32_MODE_AF4](#a6112caaab6ce78c337c40adfa1977a90)。

<a id="r_aae02581685aaeb495a8ea2bbabe0999b"></a>

```c
#define MAX32_MODE_AF5 0x05
```

相关声明：[MAX32_MODE_AF5](#aae02581685aaeb495a8ea2bbabe0999b)。

<a id="r_ac45646bd5514a406cbb87dc24a3a2f4c"></a>

```c
#define MAX32_MODE_SHIFT 0U
```

相关声明：[MAX32_MODE_SHIFT](#ac45646bd5514a406cbb87dc24a3a2f4c)。

模式、端口和引脚的移位位数（Shift Number）。

<a id="r_a071a95ac6147954a5b9086cc27f02ce0"></a>

```c
#define MAX32_MODE_MASK 0x0FU
```

相关声明：[MAX32_MODE_MASK](#a071a95ac6147954a5b9086cc27f02ce0)。

<a id="r_ad103d747f01d57dc2cbc547fde45c988"></a>

```c
#define MAX32_PORT_SHIFT 4U
```

相关声明：[MAX32_PORT_SHIFT](#ad103d747f01d57dc2cbc547fde45c988)。

<a id="r_a668dddf52782f061e623e8d0837ba513"></a>

```c
#define MAX32_PORT_MASK 0x0FU
```

相关声明：[MAX32_PORT_MASK](#a668dddf52782f061e623e8d0837ba513)。

<a id="r_aa3b3d363ef790d1def3402ceb47b2f97"></a>

```c
#define MAX32_PIN_SHIFT 8U
```

相关声明：[MAX32_PIN_SHIFT](#aa3b3d363ef790d1def3402ceb47b2f97)。

<a id="r_abf4c75ee139d0abcc10ab3c4fe116ae2"></a>

```c
#define MAX32_PIN_MASK 0xFFU
```

相关声明：[MAX32_PIN_MASK](#abf4c75ee139d0abcc10ab3c4fe116ae2)。

<a id="r_a6af2b3feddf92906fe3ba315b8debc41"></a>

```c
#define MAX32_PINMUX(port, pin, mode)
```

相关声明：[MAX32_PINMUX](#a6af2b3feddf92906fe3ba315b8debc41)。

引脚配置位域（Pin Configuration Bit Field）。

<a id="r_a9e2b0cc6ad6fb0e043f805be98900cad"></a>

```c
#define MAX32_PINMUX_PORT(pinmux)
```

相关声明：[MAX32_PINMUX_PORT](#a9e2b0cc6ad6fb0e043f805be98900cad)。

<a id="r_ae9b72f2da84eca73ba5d0958946d2d6e"></a>

```c
#define MAX32_PINMUX_PIN(pinmux)
```

相关声明：[MAX32_PINMUX_PIN](#ae9b72f2da84eca73ba5d0958946d2d6e)。

<a id="r_a1f3ef03ff93e7fe57781eb831aaf5afb"></a>

```c
#define MAX32_PINMUX_MODE(pinmux)
```

相关声明：[MAX32_PINMUX_MODE](#a1f3ef03ff93e7fe57781eb831aaf5afb)。

<a id="r_a4e18fd313d30f6f69376cd769ea2347c"></a>

```c
#define MAX32_VSEL_VDDIO 0
```

相关声明：[MAX32_VSEL_VDDIO](#a4e18fd313d30f6f69376cd769ea2347c)。

<a id="r_a6c2d4fea363165d857f5a79608d52aa0"></a>

```c
#define MAX32_VSEL_VDDIOH 1
```

相关声明：[MAX32_VSEL_VDDIOH](#a6c2d4fea363165d857f5a79608d52aa0)。

<a id="r_a05fd9141c140ccf54d0723a3511d0c9b"></a>

```c
#define MAX32_INPUT_ENABLE_SHIFT 0x00
```

相关声明：[MAX32_INPUT_ENABLE_SHIFT](#a05fd9141c140ccf54d0723a3511d0c9b)。

引脚配置（Pin Configuration）。

<a id="r_a6ffa10ef6074415084575c88a12069cc"></a>

```c
#define MAX32_BIAS_PULL_UP_SHIFT 0x01
```

相关声明：[MAX32_BIAS_PULL_UP_SHIFT](#a6ffa10ef6074415084575c88a12069cc)。

<a id="r_afa7dd8f4020995627e8b9f2ee60316bd"></a>

```c
#define MAX32_BIAS_PULL_DOWN_SHIFT 0x02
```

相关声明：[MAX32_BIAS_PULL_DOWN_SHIFT](#afa7dd8f4020995627e8b9f2ee60316bd)。

<a id="r_a3f1a5cd6c9da2ad726155b40a9cea865"></a>

```c
#define MAX32_OUTPUT_ENABLE_SHIFT 0x03
```

相关声明：[MAX32_OUTPUT_ENABLE_SHIFT](#a3f1a5cd6c9da2ad726155b40a9cea865)。

<a id="r_a88dcd8d7eee992eecd0e430a667d3353"></a>

```c
#define MAX32_POWER_SOURCE_SHIFT 0x04
```

相关声明：[MAX32_POWER_SOURCE_SHIFT](#a88dcd8d7eee992eecd0e430a667d3353)。

<a id="r_aa8cf639ff885ef23a51857b56bc6f113"></a>

```c
#define MAX32_OUTPUT_HIGH_SHIFT 0x05
```

相关声明：[MAX32_OUTPUT_HIGH_SHIFT](#aa8cf639ff885ef23a51857b56bc6f113)。

<a id="r_a1082e5021dc5bcceb337a6286c3d69a2"></a>

```c
#define MAX32_DRV_STRENGTH_SHIFT 0x06 /* 2 bits */
```

相关声明：[MAX32_DRV_STRENGTH_SHIFT](#a1082e5021dc5bcceb337a6286c3d69a2)。

<a id="r_a41e4cdd4682a676f295de9d728ba6455"></a>

```c
#define MAX32_DRV_STRENGTH_MASK 0x03
```

相关声明：[MAX32_DRV_STRENGTH_MASK](#a41e4cdd4682a676f295de9d728ba6455)。

## 20.2\_详细说明（Detailed Documentation）

<a id="afa7dd8f4020995627e8b9f2ee60316bd"></a>

### `MAX32_BIAS_PULL_DOWN_SHIFT`

```c
#define MAX32_BIAS_PULL_DOWN_SHIFT 0x02
```

<a id="a6ffa10ef6074415084575c88a12069cc"></a>

### `MAX32_BIAS_PULL_UP_SHIFT`

```c
#define MAX32_BIAS_PULL_UP_SHIFT 0x01
```

<a id="a41e4cdd4682a676f295de9d728ba6455"></a>

### `MAX32_DRV_STRENGTH_MASK`

```c
#define MAX32_DRV_STRENGTH_MASK 0x03
```

<a id="a1082e5021dc5bcceb337a6286c3d69a2"></a>

### `MAX32_DRV_STRENGTH_SHIFT`

```c
#define MAX32_DRV_STRENGTH_SHIFT 0x06 /* 2 bits */
```

<a id="a05fd9141c140ccf54d0723a3511d0c9b"></a>

### `MAX32_INPUT_ENABLE_SHIFT`

```c
#define MAX32_INPUT_ENABLE_SHIFT 0x00
```

引脚配置（Pin Configuration）。

<a id="a4e3439dc886a1ed097d698847ab3cb92"></a>

### `MAX32_MODE_AF1`

```c
#define MAX32_MODE_AF1 0x01
```

<a id="af4e13cd1ef71b77ae882aadb467e5115"></a>

### `MAX32_MODE_AF2`

```c
#define MAX32_MODE_AF2 0x02
```

<a id="a33afd156fac8c0ccb588230b3f787947"></a>

### `MAX32_MODE_AF3`

```c
#define MAX32_MODE_AF3 0x03
```

<a id="a6112caaab6ce78c337c40adfa1977a90"></a>

### `MAX32_MODE_AF4`

```c
#define MAX32_MODE_AF4 0x04
```

<a id="aae02581685aaeb495a8ea2bbabe0999b"></a>

### `MAX32_MODE_AF5`

```c
#define MAX32_MODE_AF5 0x05
```

<a id="a7087cd825f7f43739fa57ce0a4e4297d"></a>

### `MAX32_MODE_GPIO`

```c
#define MAX32_MODE_GPIO 0x00
```

引脚模式（Pin Modes）。

<a id="a071a95ac6147954a5b9086cc27f02ce0"></a>

### `MAX32_MODE_MASK`

```c
#define MAX32_MODE_MASK 0x0FU
```

<a id="ac45646bd5514a406cbb87dc24a3a2f4c"></a>

### `MAX32_MODE_SHIFT`

```c
#define MAX32_MODE_SHIFT 0U
```

模式、端口和引脚的移位位数（Shift Number）。

<a id="a3f1a5cd6c9da2ad726155b40a9cea865"></a>

### `MAX32_OUTPUT_ENABLE_SHIFT`

```c
#define MAX32_OUTPUT_ENABLE_SHIFT 0x03
```

<a id="aa8cf639ff885ef23a51857b56bc6f113"></a>

### `MAX32_OUTPUT_HIGH_SHIFT`

```c
#define MAX32_OUTPUT_HIGH_SHIFT 0x05
```

<a id="abf4c75ee139d0abcc10ab3c4fe116ae2"></a>

### `MAX32_PIN_MASK`

```c
#define MAX32_PIN_MASK 0xFFU
```

<a id="aa3b3d363ef790d1def3402ceb47b2f97"></a>

### `MAX32_PIN_SHIFT`

```c
#define MAX32_PIN_SHIFT 8U
```

<a id="a6af2b3feddf92906fe3ba315b8debc41"></a>

### `MAX32_PINMUX`

```c
#define MAX32_PINMUX ( port, pin, mode )
```

展开值（Value）：

```c
((((port)&MAX32_PORT_MASK) << MAX32_PORT_SHIFT) |                                          \
 (((pin)&MAX32_PIN_MASK) << MAX32_PIN_SHIFT) |                                             \
 (((MAX32_MODE_##mode) & MAX32_MODE_MASK) << MAX32_MODE_SHIFT))
```

引脚配置位域（Pin Configuration Bit Field）。

字段（Fields）：

- 模式（Mode），位范围 `[0:3]`。
- 端口（Port），位范围 `[4:7]`。
- 引脚（Pin），位范围 `[8:15]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port），范围为 0–15。 |
| `pin` | 引脚（Pin）：0～31。 |
| `mode` | 模式（Mode），如 GPIO、AF1、AF2 等。 |

<a id="a1f3ef03ff93e7fe57781eb831aaf5afb"></a>

### `MAX32_PINMUX_MODE`

```c
#define MAX32_PINMUX_MODE ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> MAX32_MODE_SHIFT) & MAX32_MODE_MASK)
```

<a id="ae9b72f2da84eca73ba5d0958946d2d6e"></a>

### `MAX32_PINMUX_PIN`

```c
#define MAX32_PINMUX_PIN ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> MAX32_PIN_SHIFT) & MAX32_PIN_MASK)
```

<a id="a9e2b0cc6ad6fb0e043f805be98900cad"></a>

### `MAX32_PINMUX_PORT`

```c
#define MAX32_PINMUX_PORT ( pinmux)
```

展开值（Value）：

```c
(((pinmux) >> MAX32_PORT_SHIFT) & MAX32_PORT_MASK)
```

<a id="a668dddf52782f061e623e8d0837ba513"></a>

### `MAX32_PORT_MASK`

```c
#define MAX32_PORT_MASK 0x0FU
```

<a id="ad103d747f01d57dc2cbc547fde45c988"></a>

### `MAX32_PORT_SHIFT`

```c
#define MAX32_PORT_SHIFT 4U
```

<a id="a88dcd8d7eee992eecd0e430a667d3353"></a>

### `MAX32_POWER_SOURCE_SHIFT`

```c
#define MAX32_POWER_SOURCE_SHIFT 0x04
```

<a id="a4e18fd313d30f6f69376cd769ea2347c"></a>

### `MAX32_VSEL_VDDIO`

```c
#define MAX32_VSEL_VDDIO 0
```

<a id="a6c2d4fea363165d857f5a79608d52aa0"></a>

### `MAX32_VSEL_VDDIOH`

```c
#define MAX32_VSEL_VDDIOH 1
```


## 20.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P051_max32-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="amax32-pinctrl_8h_html_a071a95ac6147954a5b9086cc27f02ce0"></a>
<a id="amax32-pinctrl_8h_html_a668dddf52782f061e623e8d0837ba513"></a>
<a id="amax32-pinctrl_8h_html_aa3b3d363ef790d1def3402ceb47b2f97"></a>
<a id="amax32-pinctrl_8h_html_abf4c75ee139d0abcc10ab3c4fe116ae2"></a>
<a id="amax32-pinctrl_8h_html_ac45646bd5514a406cbb87dc24a3a2f4c"></a>
<a id="amax32-pinctrl_8h_html_ad103d747f01d57dc2cbc547fde45c988"></a>

---

[上一章](P019_zephyr__drivers__mfd__m5pm1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__drivers__sensor__max32664c.h_文件参考.md)
