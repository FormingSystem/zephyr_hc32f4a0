---
id: learning.zephyr-docs.api-file-reference.page-486
title: zephyr__dt-bindings__pinctrl__ti-k3-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-k3-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第486章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_ti-k3-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti-k3-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 486.1\_宏定义（Macros）

<a id="r_a0febfbc566c3728115a03bb7f7dc620e"></a>

```c
#define PULLUDEN_SHIFT 16
```

相关声明：[PULLUDEN_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)。

<a id="r_ad24bec783f5c84d6e82a34141b0d057a"></a>

```c
#define PULLTYPESEL_SHIFT 17
```

相关声明：[PULLTYPESEL_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)。

<a id="r_aa96a5ff81411950a5661202b443142ca"></a>

```c
#define RXACTIVE_SHIFT 18
```

相关声明：[RXACTIVE_SHIFT](#aa96a5ff81411950a5661202b443142ca)。

<a id="r_a768319530a87153b9804251bdc3b9e4d"></a>

```c
#define PULL_DISABLE (1 << PULLUDEN_SHIFT)
```

相关声明：[PULL_DISABLE](#a768319530a87153b9804251bdc3b9e4d)、[PULLUDEN_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)。

<a id="r_acaca8fc3aa06bcd710d33c74ec8bff40"></a>

```c
#define PULL_ENABLE (0 << PULLUDEN_SHIFT)
```

相关声明：[PULL_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)、[PULLUDEN_SHIFT](#a0febfbc566c3728115a03bb7f7dc620e)。

<a id="r_aca4f67c0077925f24ea1f6b26e313271"></a>

```c
#define PULL_UP ((1 << PULLTYPESEL_SHIFT) | PULL_ENABLE)
```

相关声明：[PULL_UP](#aca4f67c0077925f24ea1f6b26e313271)、[PULLTYPESEL_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)、[PULL_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)。

<a id="r_ab47362632d6cd744f764880731de5704"></a>

```c
#define PULL_DOWN ((0 << PULLTYPESEL_SHIFT) | PULL_ENABLE)
```

相关声明：[PULL_DOWN](#ab47362632d6cd744f764880731de5704)、[PULLTYPESEL_SHIFT](#ad24bec783f5c84d6e82a34141b0d057a)、[PULL_ENABLE](#acaca8fc3aa06bcd710d33c74ec8bff40)。

<a id="r_a6ad4c7f924e24241629dc10ed6b433f9"></a>

```c
#define INPUT_ENABLE (1 << RXACTIVE_SHIFT)
```

相关声明：[INPUT_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9)、[RXACTIVE_SHIFT](#aa96a5ff81411950a5661202b443142ca)。

<a id="r_a40984b9ac260aa5f3467e55a91cfff30"></a>

```c
#define INPUT_DISABLE (0 << RXACTIVE_SHIFT)
```

相关声明：[INPUT_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30)、[RXACTIVE_SHIFT](#aa96a5ff81411950a5661202b443142ca)。

<a id="r_a16f6fcf4256a279427eb2c243c9e0bd5"></a>

```c
#define PIN_OUTPUT (INPUT_DISABLE | PULL_DISABLE)
```

相关声明：[PIN_OUTPUT](#a16f6fcf4256a279427eb2c243c9e0bd5)、[INPUT_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30)、[PULL_DISABLE](#a768319530a87153b9804251bdc3b9e4d)。

<a id="r_abfd6c5cdc843d33ebddee7b244931fc3"></a>

```c
#define PIN_OUTPUT_PULLUP (INPUT_DISABLE | PULL_UP)
```

相关声明：[PIN_OUTPUT_PULLUP](#abfd6c5cdc843d33ebddee7b244931fc3)、[INPUT_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30)、[PULL_UP](#aca4f67c0077925f24ea1f6b26e313271)。

<a id="r_a8c5881bfb4d468fa634c8bec1d68595c"></a>

```c
#define PIN_OUTPUT_PULLDOWN (INPUT_DISABLE | PULL_DOWN)
```

相关声明：[PIN_OUTPUT_PULLDOWN](#a8c5881bfb4d468fa634c8bec1d68595c)、[INPUT_DISABLE](#a40984b9ac260aa5f3467e55a91cfff30)、[PULL_DOWN](#ab47362632d6cd744f764880731de5704)。

<a id="r_a5a94a90bd5b33109a2e3832760bc5da1"></a>

```c
#define PIN_INPUT (INPUT_ENABLE | PULL_DISABLE)
```

相关声明：[PIN_INPUT](#a5a94a90bd5b33109a2e3832760bc5da1)、[INPUT_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9)、[PULL_DISABLE](#a768319530a87153b9804251bdc3b9e4d)。

<a id="r_a06f998fe6be04b6a8d278b150790d436"></a>

```c
#define PIN_INPUT_PULLUP (INPUT_ENABLE | PULL_UP)
```

相关声明：[PIN_INPUT_PULLUP](#a06f998fe6be04b6a8d278b150790d436)、[INPUT_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9)、[PULL_UP](#aca4f67c0077925f24ea1f6b26e313271)。

<a id="r_a3ce1576f1da81ea2f6c492b8f8cd5350"></a>

```c
#define PIN_INPUT_PULLDOWN (INPUT_ENABLE | PULL_DOWN)
```

相关声明：[PIN_INPUT_PULLDOWN](#a3ce1576f1da81ea2f6c492b8f8cd5350)、[INPUT_ENABLE](#a6ad4c7f924e24241629dc10ed6b433f9)、[PULL_DOWN](#ab47362632d6cd744f764880731de5704)。

<a id="r_adf2868df9ec8ecdd15e89b8a33a1fdbc"></a>

```c
#define MUX_MODE_0 0
```

相关声明：[MUX_MODE_0](#adf2868df9ec8ecdd15e89b8a33a1fdbc)。

<a id="r_a7efdf57cf0a9ef6847bd3e62b42ab771"></a>

```c
#define MUX_MODE_1 1
```

相关声明：[MUX_MODE_1](#a7efdf57cf0a9ef6847bd3e62b42ab771)。

<a id="r_ac2c88f4a9d2752f06cb925ca4993a35e"></a>

```c
#define MUX_MODE_2 2
```

相关声明：[MUX_MODE_2](#ac2c88f4a9d2752f06cb925ca4993a35e)。

<a id="r_a018dca77be29b23eface983280b1812f"></a>

```c
#define MUX_MODE_3 3
```

相关声明：[MUX_MODE_3](#a018dca77be29b23eface983280b1812f)。

<a id="r_ad0ff0ccc1b0b38c49a842c565aa6c0b8"></a>

```c
#define MUX_MODE_4 4
```

相关声明：[MUX_MODE_4](#ad0ff0ccc1b0b38c49a842c565aa6c0b8)。

<a id="r_a6192dc972d0c7712a06be2d47205c558"></a>

```c
#define MUX_MODE_5 5
```

相关声明：[MUX_MODE_5](#a6192dc972d0c7712a06be2d47205c558)。

<a id="r_a9a5bcfce0779373f2ed0f0dd645a9703"></a>

```c
#define MUX_MODE_6 6
```

相关声明：[MUX_MODE_6](#a9a5bcfce0779373f2ed0f0dd645a9703)。

<a id="r_a97074809f50f00264fd33793d4d0b647"></a>

```c
#define MUX_MODE_7 7
```

相关声明：[MUX_MODE_7](#a97074809f50f00264fd33793d4d0b647)。

<a id="r_a0c6c56a47585b1fe1233139689c519de"></a>

```c
#define MUX_MODE_8 8
```

相关声明：[MUX_MODE_8](#a0c6c56a47585b1fe1233139689c519de)。

<a id="r_aa951dab323d11eb1059ed1f278f7730d"></a>

```c
#define MUX_MODE_9 9
```

相关声明：[MUX_MODE_9](#aa951dab323d11eb1059ed1f278f7730d)。

<a id="r_aebfc9715ee7edf771cb23da2b0028a11"></a>

```c
#define MUX_MODE_10 10
```

相关声明：[MUX_MODE_10](#aebfc9715ee7edf771cb23da2b0028a11)。

<a id="r_a052beac6cdfccce06bb16f447e54db92"></a>

```c
#define MUX_MODE_11 11
```

相关声明：[MUX_MODE_11](#a052beac6cdfccce06bb16f447e54db92)。

<a id="r_a1213893060e171293e0484324a6e20ab"></a>

```c
#define MUX_MODE_12 12
```

相关声明：[MUX_MODE_12](#a1213893060e171293e0484324a6e20ab)。

<a id="r_aa436ee60756d56a9a5f451cdb0dae3c5"></a>

```c
#define MUX_MODE_13 13
```

相关声明：[MUX_MODE_13](#aa436ee60756d56a9a5f451cdb0dae3c5)。

<a id="r_afa386486189b7027f7ac93a9e2fa2614"></a>

```c
#define MUX_MODE_14 14
```

相关声明：[MUX_MODE_14](#afa386486189b7027f7ac93a9e2fa2614)。

<a id="r_a95cac03e59fecc4cb31762747913dddf"></a>

```c
#define K3_PINMUX(offset, value, mux_mode)
```

相关声明：[K3_PINMUX](#a95cac03e59fecc4cb31762747913dddf)。

## 486.2\_详细说明（Detailed Documentation）

<a id="a40984b9ac260aa5f3467e55a91cfff30"></a>

### `INPUT_DISABLE`

```c
#define INPUT_DISABLE (0 << RXACTIVE_SHIFT)
```

<a id="a6ad4c7f924e24241629dc10ed6b433f9"></a>

### `INPUT_ENABLE`

```c
#define INPUT_ENABLE (1 << RXACTIVE_SHIFT)
```

<a id="a95cac03e59fecc4cb31762747913dddf"></a>

### `K3_PINMUX`

```c
#define K3_PINMUX ( offset, value, mux_mode )
```

展开值（Value）：

```c
(((offset) & 0x1fff)) ((value) | (mux_mode))
```

<a id="adf2868df9ec8ecdd15e89b8a33a1fdbc"></a>

### `MUX_MODE_0`

```c
#define MUX_MODE_0 0
```

<a id="a7efdf57cf0a9ef6847bd3e62b42ab771"></a>

### `MUX_MODE_1`

```c
#define MUX_MODE_1 1
```

<a id="aebfc9715ee7edf771cb23da2b0028a11"></a>

### `MUX_MODE_10`

```c
#define MUX_MODE_10 10
```

<a id="a052beac6cdfccce06bb16f447e54db92"></a>

### `MUX_MODE_11`

```c
#define MUX_MODE_11 11
```

<a id="a1213893060e171293e0484324a6e20ab"></a>

### `MUX_MODE_12`

```c
#define MUX_MODE_12 12
```

<a id="aa436ee60756d56a9a5f451cdb0dae3c5"></a>

### `MUX_MODE_13`

```c
#define MUX_MODE_13 13
```

<a id="afa386486189b7027f7ac93a9e2fa2614"></a>

### `MUX_MODE_14`

```c
#define MUX_MODE_14 14
```

<a id="ac2c88f4a9d2752f06cb925ca4993a35e"></a>

### `MUX_MODE_2`

```c
#define MUX_MODE_2 2
```

<a id="a018dca77be29b23eface983280b1812f"></a>

### `MUX_MODE_3`

```c
#define MUX_MODE_3 3
```

<a id="ad0ff0ccc1b0b38c49a842c565aa6c0b8"></a>

### `MUX_MODE_4`

```c
#define MUX_MODE_4 4
```

<a id="a6192dc972d0c7712a06be2d47205c558"></a>

### `MUX_MODE_5`

```c
#define MUX_MODE_5 5
```

<a id="a9a5bcfce0779373f2ed0f0dd645a9703"></a>

### `MUX_MODE_6`

```c
#define MUX_MODE_6 6
```

<a id="a97074809f50f00264fd33793d4d0b647"></a>

### `MUX_MODE_7`

```c
#define MUX_MODE_7 7
```

<a id="a0c6c56a47585b1fe1233139689c519de"></a>

### `MUX_MODE_8`

```c
#define MUX_MODE_8 8
```

<a id="aa951dab323d11eb1059ed1f278f7730d"></a>

### `MUX_MODE_9`

```c
#define MUX_MODE_9 9
```

<a id="a5a94a90bd5b33109a2e3832760bc5da1"></a>

### `PIN_INPUT`

```c
#define PIN_INPUT (INPUT_ENABLE | PULL_DISABLE)
```

<a id="a3ce1576f1da81ea2f6c492b8f8cd5350"></a>

### `PIN_INPUT_PULLDOWN`

```c
#define PIN_INPUT_PULLDOWN (INPUT_ENABLE | PULL_DOWN)
```

<a id="a06f998fe6be04b6a8d278b150790d436"></a>

### `PIN_INPUT_PULLUP`

```c
#define PIN_INPUT_PULLUP (INPUT_ENABLE | PULL_UP)
```

<a id="a16f6fcf4256a279427eb2c243c9e0bd5"></a>

### `PIN_OUTPUT`

```c
#define PIN_OUTPUT (INPUT_DISABLE | PULL_DISABLE)
```

<a id="a8c5881bfb4d468fa634c8bec1d68595c"></a>

### `PIN_OUTPUT_PULLDOWN`

```c
#define PIN_OUTPUT_PULLDOWN (INPUT_DISABLE | PULL_DOWN)
```

<a id="abfd6c5cdc843d33ebddee7b244931fc3"></a>

### `PIN_OUTPUT_PULLUP`

```c
#define PIN_OUTPUT_PULLUP (INPUT_DISABLE | PULL_UP)
```

<a id="a768319530a87153b9804251bdc3b9e4d"></a>

### `PULL_DISABLE`

```c
#define PULL_DISABLE (1 << PULLUDEN_SHIFT)
```

<a id="ab47362632d6cd744f764880731de5704"></a>

### `PULL_DOWN`

```c
#define PULL_DOWN ((0 << PULLTYPESEL_SHIFT) | PULL_ENABLE)
```

<a id="acaca8fc3aa06bcd710d33c74ec8bff40"></a>

### `PULL_ENABLE`

```c
#define PULL_ENABLE (0 << PULLUDEN_SHIFT)
```

<a id="aca4f67c0077925f24ea1f6b26e313271"></a>

### `PULL_UP`

```c
#define PULL_UP ((1 << PULLTYPESEL_SHIFT) | PULL_ENABLE)
```

<a id="ad24bec783f5c84d6e82a34141b0d057a"></a>

### `PULLTYPESEL_SHIFT`

```c
#define PULLTYPESEL_SHIFT 17
```

<a id="a0febfbc566c3728115a03bb7f7dc620e"></a>

### `PULLUDEN_SHIFT`

```c
#define PULLUDEN_SHIFT 16
```

<a id="aa96a5ff81411950a5661202b443142ca"></a>

### `RXACTIVE_SHIFT`

```c
#define RXACTIVE_SHIFT 18
```


## 486.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P224_ti-k3-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P485_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__test_asm_inline_other.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P487_zephyr__posix__sys__times.h_文件参考.md)
