---
id: learning.zephyr-docs.api-file-reference.page-211
title: zephyr__dt-bindings__pinctrl__mchp-xec-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第211章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_mchp-xec-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 211.1\_宏定义（Macros）

<a id="r_adbdaffd4bf6308e5e57f501313339871"></a>

```c
#define MCHP_GPIO 0x0
```

相关声明：[MCHP_GPIO](#adbdaffd4bf6308e5e57f501313339871)。

<a id="r_ae0c0be33001f69f4225644ab74f59078"></a>

```c
#define MCHP_AF0 0x0
```

相关声明：[MCHP_AF0](#ae0c0be33001f69f4225644ab74f59078)。

<a id="r_ad1d584cc5e02df71255e0608a04d019f"></a>

```c
#define MCHP_AF1 0x1
```

相关声明：[MCHP_AF1](#ad1d584cc5e02df71255e0608a04d019f)。

<a id="r_ad1888b8f9e981d4a54534fca01aab1c4"></a>

```c
#define MCHP_AF2 0x2
```

相关声明：[MCHP_AF2](#ad1888b8f9e981d4a54534fca01aab1c4)。

<a id="r_a9e4512829a2dba4904ab16718c2f54fd"></a>

```c
#define MCHP_AF3 0x3
```

相关声明：[MCHP_AF3](#a9e4512829a2dba4904ab16718c2f54fd)。

<a id="r_a68e1df87c0a06668cc3897fd8805bc16"></a>

```c
#define MCHP_AF4 0x4
```

相关声明：[MCHP_AF4](#a68e1df87c0a06668cc3897fd8805bc16)。

<a id="r_adb552a66660db8468dabfae0edcaba71"></a>

```c
#define MCHP_AF5 0x5
```

相关声明：[MCHP_AF5](#adb552a66660db8468dabfae0edcaba71)。

<a id="r_a1b8833d1dee0e4c9ab63ffc50c8472a5"></a>

```c
#define MCHP_AF6 0x6
```

相关声明：[MCHP_AF6](#a1b8833d1dee0e4c9ab63ffc50c8472a5)。

<a id="r_a3ebbede5ab9560d1ed0889c488e5d658"></a>

```c
#define MCHP_AF7 0x7
```

相关声明：[MCHP_AF7](#a3ebbede5ab9560d1ed0889c488e5d658)。

<a id="r_a57390da1563b872353fdec5d2ce039d0"></a>

```c
#define MCHP_AFMAX 0x8
```

相关声明：[MCHP_AFMAX](#a57390da1563b872353fdec5d2ce039d0)。

<a id="r_acc0468de41450ed9ff0a28fd0c0fe94e"></a>

```c
#define MCHP_XEC_SLEW_RATE_NO_CHANGE 0
```

相关声明：[MCHP_XEC_SLEW_RATE_NO_CHANGE](#acc0468de41450ed9ff0a28fd0c0fe94e)。

<a id="r_a612cb5805fca95fd9635c6b1ffd156ff"></a>

```c
#define MCHP_XEC_SLEW_RATE_FAST 1
```

相关声明：[MCHP_XEC_SLEW_RATE_FAST](#a612cb5805fca95fd9635c6b1ffd156ff)。

<a id="r_ac0b159289525172d8027556953193cd5"></a>

```c
#define MCHP_XEC_SLEW_RATE_SLOW 2
```

相关声明：[MCHP_XEC_SLEW_RATE_SLOW](#ac0b159289525172d8027556953193cd5)。

<a id="r_a138aedf74cf0df435d5808fbd18c5ea2"></a>

```c
#define MCHP_XEC_DRV_STR_NO_CHANGE 0
```

相关声明：[MCHP_XEC_DRV_STR_NO_CHANGE](#a138aedf74cf0df435d5808fbd18c5ea2)。

<a id="r_a834a3d987d8bbc6d1ccb6e4492f9705d"></a>

```c
#define MCHP_XEC_DRV_STR_1X 1 /* 2 or 4(PIO-24) mA */
```

相关声明：[MCHP_XEC_DRV_STR_1X](#a834a3d987d8bbc6d1ccb6e4492f9705d)。

<a id="r_acff3bc1916dc4747ba993892fae9cae1"></a>

```c
#define MCHP_XEC_DRV_STR_2X 2 /* 4 or 8(PIO-24) mA */
```

相关声明：[MCHP_XEC_DRV_STR_2X](#acff3bc1916dc4747ba993892fae9cae1)。

<a id="r_ac637de7861b88b30482e7f6917d86b5a"></a>

```c
#define MCHP_XEC_DRV_STR_4X 3 /* 8 or 16(PIO-24) mA */
```

相关声明：[MCHP_XEC_DRV_STR_4X](#ac637de7861b88b30482e7f6917d86b5a)。

<a id="r_ae649067e66196fcb0f55396c2d2d8854"></a>

```c
#define MCHP_XEC_DRV_STR_6X 4 /* 12 or 24(PIO-24) mA */
```

相关声明：[MCHP_XEC_DRV_STR_6X](#ae649067e66196fcb0f55396c2d2d8854)。

<a id="r_a7e0762ea1ba02d68a6c13c5d0805c60a"></a>

```c
#define MCHP_XEC_PINMUX_PORT_POS 0
```

相关声明：[MCHP_XEC_PINMUX_PORT_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)。

<a id="r_a27cbf07ff9a28f24d115d788de5567f2"></a>

```c
#define MCHP_XEC_PINMUX_PORT_MSK 0xf
```

相关声明：[MCHP_XEC_PINMUX_PORT_MSK](#a27cbf07ff9a28f24d115d788de5567f2)。

<a id="r_a3504bf6d5897c23173f05009a4862c31"></a>

```c
#define MCHP_XEC_PINMUX_PIN_POS 4
```

相关声明：[MCHP_XEC_PINMUX_PIN_POS](#a3504bf6d5897c23173f05009a4862c31)。

<a id="r_a8537436b6e3c94e965c0a27992b04d35"></a>

```c
#define MCHP_XEC_PINMUX_PIN_MSK 0x1f
```

相关声明：[MCHP_XEC_PINMUX_PIN_MSK](#a8537436b6e3c94e965c0a27992b04d35)。

<a id="r_a4a8aea0c15ea3d89d4bac2629fa43c18"></a>

```c
#define MCHP_XEC_PINMUX_FUNC_POS 9
```

相关声明：[MCHP_XEC_PINMUX_FUNC_POS](#a4a8aea0c15ea3d89d4bac2629fa43c18)。

<a id="r_ab39f30494ce30f88f18cbfdd835cbb6f"></a>

```c
#define MCHP_XEC_PINMUX_FUNC_MSK 0x7
```

相关声明：[MCHP_XEC_PINMUX_FUNC_MSK](#ab39f30494ce30f88f18cbfdd835cbb6f)。

<a id="r_a9ce81e5379ef60140ed6251e30825fe9"></a>

```c
#define MCHP_XEC_PINMUX(n, f)
```

相关声明：[MCHP_XEC_PINMUX](#a9ce81e5379ef60140ed6251e30825fe9)。

<a id="r_a04e9b92f5d748649eb516e628141d6f8"></a>

```c
#define MCHP_XEC_PINMUX_PORT(p)
```

相关声明：[MCHP_XEC_PINMUX_PORT](#a04e9b92f5d748649eb516e628141d6f8)。

<a id="r_a06fabe0e1bb56de3c56fc278d3f2da6f"></a>

```c
#define MCHP_XEC_PINMUX_PIN(p)
```

相关声明：[MCHP_XEC_PINMUX_PIN](#a06fabe0e1bb56de3c56fc278d3f2da6f)。

<a id="r_a90649c60bd81e6cc2dca37ea32d8ad25"></a>

```c
#define MCHP_XEC_PINMUX_FUNC(p)
```

相关声明：[MCHP_XEC_PINMUX_FUNC](#a90649c60bd81e6cc2dca37ea32d8ad25)。

<a id="r_a8f8edb939c9f5f9702253a24dc9bde3d"></a>

```c
#define MEC_XEC_PINMUX_PORT_PIN(p)
```

相关声明：[MEC_XEC_PINMUX_PORT_PIN](#a8f8edb939c9f5f9702253a24dc9bde3d)。

## 211.2\_详细说明（Detailed Documentation）

<a id="ae0c0be33001f69f4225644ab74f59078"></a>

### `MCHP_AF0`

```c
#define MCHP_AF0 0x0
```

<a id="ad1d584cc5e02df71255e0608a04d019f"></a>

### `MCHP_AF1`

```c
#define MCHP_AF1 0x1
```

<a id="ad1888b8f9e981d4a54534fca01aab1c4"></a>

### `MCHP_AF2`

```c
#define MCHP_AF2 0x2
```

<a id="a9e4512829a2dba4904ab16718c2f54fd"></a>

### `MCHP_AF3`

```c
#define MCHP_AF3 0x3
```

<a id="a68e1df87c0a06668cc3897fd8805bc16"></a>

### `MCHP_AF4`

```c
#define MCHP_AF4 0x4
```

<a id="adb552a66660db8468dabfae0edcaba71"></a>

### `MCHP_AF5`

```c
#define MCHP_AF5 0x5
```

<a id="a1b8833d1dee0e4c9ab63ffc50c8472a5"></a>

### `MCHP_AF6`

```c
#define MCHP_AF6 0x6
```

<a id="a3ebbede5ab9560d1ed0889c488e5d658"></a>

### `MCHP_AF7`

```c
#define MCHP_AF7 0x7
```

<a id="a57390da1563b872353fdec5d2ce039d0"></a>

### `MCHP_AFMAX`

```c
#define MCHP_AFMAX 0x8
```

<a id="adbdaffd4bf6308e5e57f501313339871"></a>

### `MCHP_GPIO`

```c
#define MCHP_GPIO 0x0
```

<a id="a834a3d987d8bbc6d1ccb6e4492f9705d"></a>

### `MCHP_XEC_DRV_STR_1X`

```c
#define MCHP_XEC_DRV_STR_1X 1 /* 2 or 4(PIO-24) mA */
```

<a id="acff3bc1916dc4747ba993892fae9cae1"></a>

### `MCHP_XEC_DRV_STR_2X`

```c
#define MCHP_XEC_DRV_STR_2X 2 /* 4 or 8(PIO-24) mA */
```

<a id="ac637de7861b88b30482e7f6917d86b5a"></a>

### `MCHP_XEC_DRV_STR_4X`

```c
#define MCHP_XEC_DRV_STR_4X 3 /* 8 or 16(PIO-24) mA */
```

<a id="ae649067e66196fcb0f55396c2d2d8854"></a>

### `MCHP_XEC_DRV_STR_6X`

```c
#define MCHP_XEC_DRV_STR_6X 4 /* 12 or 24(PIO-24) mA */
```

<a id="a138aedf74cf0df435d5808fbd18c5ea2"></a>

### `MCHP_XEC_DRV_STR_NO_CHANGE`

```c
#define MCHP_XEC_DRV_STR_NO_CHANGE 0
```

<a id="a9ce81e5379ef60140ed6251e30825fe9"></a>

### `MCHP_XEC_PINMUX`

```c
#define MCHP_XEC_PINMUX ( n, f )
```

展开值（Value）：

```c
(((((n) >> 5) & MCHP_XEC_PINMUX_PORT_MSK) << MCHP_XEC_PINMUX_PORT_POS)  | \
 (((n) & MCHP_XEC_PINMUX_PIN_MSK) << MCHP_XEC_PINMUX_PIN_POS)           | \
 (((f) & MCHP_XEC_PINMUX_FUNC_MSK) << MCHP_XEC_PINMUX_FUNC_POS))
```

<a id="a90649c60bd81e6cc2dca37ea32d8ad25"></a>

### `MCHP_XEC_PINMUX_FUNC`

```c
#define MCHP_XEC_PINMUX_FUNC ( p)
```

展开值（Value）：

```c
(((p) >> MCHP_XEC_PINMUX_FUNC_POS) & MCHP_XEC_PINMUX_FUNC_MSK)
```

<a id="ab39f30494ce30f88f18cbfdd835cbb6f"></a>

### `MCHP_XEC_PINMUX_FUNC_MSK`

```c
#define MCHP_XEC_PINMUX_FUNC_MSK 0x7
```

<a id="a4a8aea0c15ea3d89d4bac2629fa43c18"></a>

### `MCHP_XEC_PINMUX_FUNC_POS`

```c
#define MCHP_XEC_PINMUX_FUNC_POS 9
```

<a id="a06fabe0e1bb56de3c56fc278d3f2da6f"></a>

### `MCHP_XEC_PINMUX_PIN`

```c
#define MCHP_XEC_PINMUX_PIN ( p)
```

展开值（Value）：

```c
(((p) >> MCHP_XEC_PINMUX_PIN_POS) & MCHP_XEC_PINMUX_PIN_MSK)
```

<a id="a8537436b6e3c94e965c0a27992b04d35"></a>

### `MCHP_XEC_PINMUX_PIN_MSK`

```c
#define MCHP_XEC_PINMUX_PIN_MSK 0x1f
```

<a id="a3504bf6d5897c23173f05009a4862c31"></a>

### `MCHP_XEC_PINMUX_PIN_POS`

```c
#define MCHP_XEC_PINMUX_PIN_POS 4
```

<a id="a04e9b92f5d748649eb516e628141d6f8"></a>

### `MCHP_XEC_PINMUX_PORT`

```c
#define MCHP_XEC_PINMUX_PORT ( p)
```

展开值（Value）：

```c
(((p) >> MCHP_XEC_PINMUX_PORT_POS) & MCHP_XEC_PINMUX_PORT_MSK)
```

<a id="a27cbf07ff9a28f24d115d788de5567f2"></a>

### `MCHP_XEC_PINMUX_PORT_MSK`

```c
#define MCHP_XEC_PINMUX_PORT_MSK 0xf
```

<a id="a7e0762ea1ba02d68a6c13c5d0805c60a"></a>

### `MCHP_XEC_PINMUX_PORT_POS`

```c
#define MCHP_XEC_PINMUX_PORT_POS 0
```

<a id="a612cb5805fca95fd9635c6b1ffd156ff"></a>

### `MCHP_XEC_SLEW_RATE_FAST`

```c
#define MCHP_XEC_SLEW_RATE_FAST 1
```

<a id="acc0468de41450ed9ff0a28fd0c0fe94e"></a>

### `MCHP_XEC_SLEW_RATE_NO_CHANGE`

```c
#define MCHP_XEC_SLEW_RATE_NO_CHANGE 0
```

<a id="ac0b159289525172d8027556953193cd5"></a>

### `MCHP_XEC_SLEW_RATE_SLOW`

```c
#define MCHP_XEC_SLEW_RATE_SLOW 2
```

<a id="a8f8edb939c9f5f9702253a24dc9bde3d"></a>

### `MEC_XEC_PINMUX_PORT_PIN`

```c
#define MEC_XEC_PINMUX_PORT_PIN ( p)
```

展开值（Value）：

```c
((p) & ((MCHP_XEC_PINMUX_PORT_MSK << MCHP_XEC_PINMUX_PORT_POS) | \
        (MCHP_XEC_PINMUX_PIN_MSK << MCHP_XEC_PINMUX_PIN_POS)))
```


## 211.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/mchp-xec-pinctrl_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="amchp-xec-pinctrl_8h_html_a27cbf07ff9a28f24d115d788de5567f2"></a>
<a id="amchp-xec-pinctrl_8h_html_a3504bf6d5897c23173f05009a4862c31"></a>
<a id="amchp-xec-pinctrl_8h_html_a4a8aea0c15ea3d89d4bac2629fa43c18"></a>
<a id="amchp-xec-pinctrl_8h_html_a7e0762ea1ba02d68a6c13c5d0805c60a"></a>
<a id="amchp-xec-pinctrl_8h_html_a8537436b6e3c94e965c0a27992b04d35"></a>
<a id="amchp-xec-pinctrl_8h_html_ab39f30494ce30f88f18cbfdd835cbb6f"></a>

---

[上一章](P210_zephyr__dt-bindings__dma__max78002_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P212_zephyr__dt-bindings__reset__mchp_mss_reset.h_文件参考.md)
