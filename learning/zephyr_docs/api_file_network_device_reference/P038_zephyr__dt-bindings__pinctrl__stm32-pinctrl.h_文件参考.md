---
id: learning.zephyr-docs.api-file-network-device-reference.page-38
title: zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_stm32-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.1\_宏定义（Macros）

<a id="r_a856e7793927d195e31a0ab801d9320b1"></a>

```c
#define STM32_AF0 0x0
```

相关声明：[STM32_AF0](#a856e7793927d195e31a0ab801d9320b1)。

最初派生自 Linux 的 `include/dt-bindings/pinctrl/stm32-pinfunc.h`。

<a id="r_ac341ff4da52832f09596ddb8f66d0704"></a>

```c
#define STM32_AF1 0x1
```

相关声明：[STM32_AF1](#ac341ff4da52832f09596ddb8f66d0704)。

<a id="r_af6aa5ae98ba243f120737e8b0ad6644c"></a>

```c
#define STM32_AF2 0x2
```

相关声明：[STM32_AF2](#af6aa5ae98ba243f120737e8b0ad6644c)。

<a id="r_a3d65bb83c9f0515e218f300171a90b75"></a>

```c
#define STM32_AF3 0x3
```

相关声明：[STM32_AF3](#a3d65bb83c9f0515e218f300171a90b75)。

<a id="r_a286f6ec684e9c7297261f9ed7372e609"></a>

```c
#define STM32_AF4 0x4
```

相关声明：[STM32_AF4](#a286f6ec684e9c7297261f9ed7372e609)。

<a id="r_a9a48f460272ef966b8dd2ead78c8e8e9"></a>

```c
#define STM32_AF5 0x5
```

相关声明：[STM32_AF5](#a9a48f460272ef966b8dd2ead78c8e8e9)。

<a id="r_a5c5b864b9d9d1431a8d905967cae69a4"></a>

```c
#define STM32_AF6 0x6
```

相关声明：[STM32_AF6](#a5c5b864b9d9d1431a8d905967cae69a4)。

<a id="r_ade35007347e4f04e0e7f2e4f87a4dec3"></a>

```c
#define STM32_AF7 0x7
```

相关声明：[STM32_AF7](#ade35007347e4f04e0e7f2e4f87a4dec3)。

<a id="r_aef1775a7a3af9daed7d72c123db23f08"></a>

```c
#define STM32_AF8 0x8
```

相关声明：[STM32_AF8](#aef1775a7a3af9daed7d72c123db23f08)。

<a id="r_adeb65582e22de51dd619bfd7c49a0653"></a>

```c
#define STM32_AF9 0x9
```

相关声明：[STM32_AF9](#adeb65582e22de51dd619bfd7c49a0653)。

<a id="r_ad8732007cc06358d29379d025203df15"></a>

```c
#define STM32_AF10 0xa
```

相关声明：[STM32_AF10](#ad8732007cc06358d29379d025203df15)。

<a id="r_ab7bb316e4f29094d7d7a8b08522eec69"></a>

```c
#define STM32_AF11 0xb
```

相关声明：[STM32_AF11](#ab7bb316e4f29094d7d7a8b08522eec69)。

<a id="r_aaf99ab7b7abc0f5b211afba7dbc75dff"></a>

```c
#define STM32_AF12 0xc
```

相关声明：[STM32_AF12](#aaf99ab7b7abc0f5b211afba7dbc75dff)。

<a id="r_a84a34bd261316ab1353d45bbd03437a5"></a>

```c
#define STM32_AF13 0xd
```

相关声明：[STM32_AF13](#a84a34bd261316ab1353d45bbd03437a5)。

<a id="r_a5bc95c95792938f333095422499de8e6"></a>

```c
#define STM32_AF14 0xe
```

相关声明：[STM32_AF14](#a5bc95c95792938f333095422499de8e6)。

<a id="r_a2a2f2b85e7e92f1a7a7baa69ed8c4655"></a>

```c
#define STM32_AF15 0xf
```

相关声明：[STM32_AF15](#a2a2f2b85e7e92f1a7a7baa69ed8c4655)。

<a id="r_a3cef198576d1117a64e34d3981ae69d2"></a>

```c
#define STM32_ANALOG 0x10
```

相关声明：[STM32_ANALOG](#a3cef198576d1117a64e34d3981ae69d2)。

<a id="r_a6b8fe886fca3bab7d631a90cdfca6a0f"></a>

```c
#define STM32_GPIO 0x11
```

相关声明：[STM32_GPIO](#a6b8fe886fca3bab7d631a90cdfca6a0f)。

<a id="r_a1b9d630e0c184195bfece6550ae74870"></a>

```c
#define STM32_MODE_SHIFT 0U
```

相关声明：[STM32_MODE_SHIFT](#a1b9d630e0c184195bfece6550ae74870)。

根据端口、引脚编号和模式参数生成引脚复用整数值（Pinmux Integer）的宏，受 Linux 中对应的 `st,stm32f429-pinctrl` 绑定启发。

<a id="r_a12472016d6448c797707d2d062d6011d"></a>

```c
#define STM32_MODE_MASK 0x1FU
```

相关声明：[STM32_MODE_MASK](#a12472016d6448c797707d2d062d6011d)。

<a id="r_a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>

```c
#define STM32_LINE_SHIFT 5U
```

相关声明：[STM32_LINE_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)。

<a id="r_a51d75677040be2ea1204ab667fd1d6f6"></a>

```c
#define STM32_LINE_MASK 0xFU
```

相关声明：[STM32_LINE_MASK](#a51d75677040be2ea1204ab667fd1d6f6)。

<a id="r_a0fa09fe492147c76a6b2f191e39d3b9f"></a>

```c
#define STM32_PORT_SHIFT 9U
```

相关声明：[STM32_PORT_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)。

<a id="r_ad7a035f83320bdf867b030bb0dac5221"></a>

```c
#define STM32_PORT_MASK 0x1FU
```

相关声明：[STM32_PORT_MASK](#ad7a035f83320bdf867b030bb0dac5221)。

<a id="r_a0a29e4e3ef1b1e901bf203640bc84dd9"></a>

```c
#define STM32_PINMUX(port, line, mode)
```

相关声明：[STM32_PINMUX](#a0a29e4e3ef1b1e901bf203640bc84dd9)。

引脚配置位域（pin configuration bit field）。

## 38.2\_详细说明（Detailed Documentation）

<a id="a856e7793927d195e31a0ab801d9320b1"></a>

### `STM32_AF0`

```c
#define STM32_AF0 0x0
```

最初派生自 Linux 的 `include/dt-bindings/pinctrl/stm32-pinfunc.h`。

为兼容 Linux，保留了 `STM32_PINMUX` 宏和 `pinmux` 属性。但生成的值不会原样保存在镜像中：编译期间会提取 `pinmux` 中的信息，并以自定义格式保存，参见 `soc/st/stm32/common/pinctrl_soc.h`。

引脚模式（Pin Modes）。

<a id="ac341ff4da52832f09596ddb8f66d0704"></a>

### `STM32_AF1`

```c
#define STM32_AF1 0x1
```

<a id="ad8732007cc06358d29379d025203df15"></a>

### `STM32_AF10`

```c
#define STM32_AF10 0xa
```

<a id="ab7bb316e4f29094d7d7a8b08522eec69"></a>

### `STM32_AF11`

```c
#define STM32_AF11 0xb
```

<a id="aaf99ab7b7abc0f5b211afba7dbc75dff"></a>

### `STM32_AF12`

```c
#define STM32_AF12 0xc
```

<a id="a84a34bd261316ab1353d45bbd03437a5"></a>

### `STM32_AF13`

```c
#define STM32_AF13 0xd
```

<a id="a5bc95c95792938f333095422499de8e6"></a>

### `STM32_AF14`

```c
#define STM32_AF14 0xe
```

<a id="a2a2f2b85e7e92f1a7a7baa69ed8c4655"></a>

### `STM32_AF15`

```c
#define STM32_AF15 0xf
```

<a id="af6aa5ae98ba243f120737e8b0ad6644c"></a>

### `STM32_AF2`

```c
#define STM32_AF2 0x2
```

<a id="a3d65bb83c9f0515e218f300171a90b75"></a>

### `STM32_AF3`

```c
#define STM32_AF3 0x3
```

<a id="a286f6ec684e9c7297261f9ed7372e609"></a>

### `STM32_AF4`

```c
#define STM32_AF4 0x4
```

<a id="a9a48f460272ef966b8dd2ead78c8e8e9"></a>

### `STM32_AF5`

```c
#define STM32_AF5 0x5
```

<a id="a5c5b864b9d9d1431a8d905967cae69a4"></a>

### `STM32_AF6`

```c
#define STM32_AF6 0x6
```

<a id="ade35007347e4f04e0e7f2e4f87a4dec3"></a>

### `STM32_AF7`

```c
#define STM32_AF7 0x7
```

<a id="aef1775a7a3af9daed7d72c123db23f08"></a>

### `STM32_AF8`

```c
#define STM32_AF8 0x8
```

<a id="adeb65582e22de51dd619bfd7c49a0653"></a>

### `STM32_AF9`

```c
#define STM32_AF9 0x9
```

<a id="a3cef198576d1117a64e34d3981ae69d2"></a>

### `STM32_ANALOG`

```c
#define STM32_ANALOG 0x10
```

<a id="a6b8fe886fca3bab7d631a90cdfca6a0f"></a>

### `STM32_GPIO`

```c
#define STM32_GPIO 0x11
```

<a id="a51d75677040be2ea1204ab667fd1d6f6"></a>

### `STM32_LINE_MASK`

```c
#define STM32_LINE_MASK 0xFU
```

<a id="a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>

### `STM32_LINE_SHIFT`

```c
#define STM32_LINE_SHIFT 5U
```

<a id="a12472016d6448c797707d2d062d6011d"></a>

### `STM32_MODE_MASK`

```c
#define STM32_MODE_MASK 0x1FU
```

<a id="a1b9d630e0c184195bfece6550ae74870"></a>

### `STM32_MODE_SHIFT`

```c
#define STM32_MODE_SHIFT 0U
```

根据端口、引脚编号和模式参数生成引脚复用整数值（Pinmux Integer）的宏，受 Linux 中对应的 `st,stm32f429-pinctrl` 绑定启发。

<a id="a0a29e4e3ef1b1e901bf203640bc84dd9"></a>

### `STM32_PINMUX`

```c
#define STM32_PINMUX ( port, line, mode )
```

展开值（Value）：

```c
(((((port) - 'A') & STM32_PORT_MASK) << STM32_PORT_SHIFT) |    \
(((line) & STM32_LINE_MASK) << STM32_LINE_SHIFT) |             \
(((STM32_ ## mode) & STM32_MODE_MASK) << STM32_MODE_SHIFT))
```

引脚配置位域（pin configuration bit field）。

字段（Fields）：

- 模式（Mode），位范围 `[0:4]`。
- 线路（Line），位范围 `[5:8]`。
- 端口（Port），位范围 `[9:13]`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口（Port），可取 `A..Q` 或 `Z`。 |
| `line` | 引脚（Pin），取值为 0–15。 |
| `mode` | 模式（Mode）：模拟（ANALOG）、通用输入输出（GPIO）、复用（ALTERNATE）。 |

<a id="ad7a035f83320bdf867b030bb0dac5221"></a>

### `STM32_PORT_MASK`

```c
#define STM32_PORT_MASK 0x1FU
```

<a id="a0fa09fe492147c76a6b2f191e39d3b9f"></a>

### `STM32_PORT_SHIFT`

```c
#define STM32_PORT_SHIFT 9U
```


## 38.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](../api_source_network_reference/P019_stm32-pinctrl-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P827_stm32-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astm32-pinctrl_8h_html_a0fa09fe492147c76a6b2f191e39d3b9f"></a>
<a id="astm32-pinctrl_8h_html_a12472016d6448c797707d2d062d6011d"></a>
<a id="astm32-pinctrl_8h_html_a1b9d630e0c184195bfece6550ae74870"></a>
<a id="astm32-pinctrl_8h_html_a51d75677040be2ea1204ab667fd1d6f6"></a>
<a id="astm32-pinctrl_8h_html_a608cb76ac837e5b0b8ebbbc982ac1dc6"></a>
<a id="astm32-pinctrl_8h_html_ad7a035f83320bdf867b030bb0dac5221"></a>

---

[上一章](P037_zephyr__net__socketutils.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__dt-bindings__dma__stm32_dma.h_文件参考.md)
