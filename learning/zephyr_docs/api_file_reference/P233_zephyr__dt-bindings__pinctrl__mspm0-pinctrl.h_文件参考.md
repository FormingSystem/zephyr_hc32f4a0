---
id: learning.zephyr-docs.api-file-reference.page-233
title: zephyr__dt-bindings__pinctrl__mspm0-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mspm0-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第233章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_mspm0-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mspm0-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 233.1\_宏定义（Macros）

<a id="r_aed042e160fbf0499081e08f32b485ccc"></a>

```c
#define MSPM0_PIN_FUNCTION_ANALOG (0x00000000)
```

相关声明：[MSPM0_PIN_FUNCTION_ANALOG](#aed042e160fbf0499081e08f32b485ccc)。

<a id="r_aafceb12e339618d1282aa7300507d9a5"></a>

```c
#define MSPM0_PIN_FUNCTION_GPIO (0x00000001)
```

相关声明：[MSPM0_PIN_FUNCTION_GPIO](#aafceb12e339618d1282aa7300507d9a5)。

<a id="r_a2d119d2da878acd9ebac10c6d0cc7c80"></a>

```c
#define MSPM0_PIN_FUNCTION_2 (0x00000002)
```

相关声明：[MSPM0_PIN_FUNCTION_2](#a2d119d2da878acd9ebac10c6d0cc7c80)。

<a id="r_a4cdd8ded8a55c33f3b586152d64b2621"></a>

```c
#define MSPM0_PIN_FUNCTION_3 (0x00000003)
```

相关声明：[MSPM0_PIN_FUNCTION_3](#a4cdd8ded8a55c33f3b586152d64b2621)。

<a id="r_a897c32ff405a8c4eeaaffed7a6c69d5a"></a>

```c
#define MSPM0_PIN_FUNCTION_4 (0x00000004)
```

相关声明：[MSPM0_PIN_FUNCTION_4](#a897c32ff405a8c4eeaaffed7a6c69d5a)。

<a id="r_ab6ec2101ebc8d171852da5c72a9e6ff1"></a>

```c
#define MSPM0_PIN_FUNCTION_5 (0x00000005)
```

相关声明：[MSPM0_PIN_FUNCTION_5](#ab6ec2101ebc8d171852da5c72a9e6ff1)。

<a id="r_a4891b06c78d726a4806ea7f8c18d2bbc"></a>

```c
#define MSPM0_PIN_FUNCTION_6 (0x00000006)
```

相关声明：[MSPM0_PIN_FUNCTION_6](#a4891b06c78d726a4806ea7f8c18d2bbc)。

<a id="r_af2b0ea70556adb258d70cbb7274dce12"></a>

```c
#define MSPM0_PIN_FUNCTION_7 (0x00000007)
```

相关声明：[MSPM0_PIN_FUNCTION_7](#af2b0ea70556adb258d70cbb7274dce12)。

<a id="r_a250cc53f70b280ed5a909f5b968f2c0b"></a>

```c
#define MSPM0_PIN_FUNCTION_8 (0x00000008)
```

相关声明：[MSPM0_PIN_FUNCTION_8](#a250cc53f70b280ed5a909f5b968f2c0b)。

<a id="r_affb9f84a279ac6ec00f153d024282b05"></a>

```c
#define MSPM0_PIN_FUNCTION_9 (0x00000009)
```

相关声明：[MSPM0_PIN_FUNCTION_9](#affb9f84a279ac6ec00f153d024282b05)。

<a id="r_a974860da2ed7b0ad8835edf35fc3fa71"></a>

```c
#define MSPM0_PIN_FUNCTION_10 (0x0000000A)
```

相关声明：[MSPM0_PIN_FUNCTION_10](#a974860da2ed7b0ad8835edf35fc3fa71)。

<a id="r_ac98b96eb24621f99b7d52c688eb6b050"></a>

```c
#define MSPM0_PIN_FUNCTION_11 (0x0000000B)
```

相关声明：[MSPM0_PIN_FUNCTION_11](#ac98b96eb24621f99b7d52c688eb6b050)。

<a id="r_afb757ef697529cdee5be89103f84df48"></a>

```c
#define MSPM0_PIN_FUNCTION_12 (0x0000000C)
```

相关声明：[MSPM0_PIN_FUNCTION_12](#afb757ef697529cdee5be89103f84df48)。

<a id="r_a355183103734ed847fb8ade45462982e"></a>

```c
#define MSPM0_PIN_FUNCTION_13 (0x0000000D)
```

相关声明：[MSPM0_PIN_FUNCTION_13](#a355183103734ed847fb8ade45462982e)。

<a id="r_ab865c1b4170a46f6d6ed9732ad2cab6e"></a>

```c
#define MSPM0_PIN_FUNCTION_14 (0x0000000E)
```

相关声明：[MSPM0_PIN_FUNCTION_14](#ab865c1b4170a46f6d6ed9732ad2cab6e)。

<a id="r_ac07cbab89aca7270479121cc8f951e58"></a>

```c
#define MSPM0_PIN_FUNCTION_15 (0x0000000F)
```

相关声明：[MSPM0_PIN_FUNCTION_15](#ac07cbab89aca7270479121cc8f951e58)。

<a id="r_a6d8c1db9082542af49cc37dce3d02720"></a>

```c
#define MSP_PINMUX(pincm, function)
```

相关声明：[MSP_PINMUX](#a6d8c1db9082542af49cc37dce3d02720)。

## 233.2\_详细说明（Detailed Documentation）

<a id="a6d8c1db9082542af49cc37dce3d02720"></a>

### `MSP_PINMUX`

```c
#define MSP_PINMUX ( pincm, function )
```

展开值（Value）：

```c
(((pincm - 1) << 0x10) | function)
```

<a id="a974860da2ed7b0ad8835edf35fc3fa71"></a>

### `MSPM0_PIN_FUNCTION_10`

```c
#define MSPM0_PIN_FUNCTION_10 (0x0000000A)
```

<a id="ac98b96eb24621f99b7d52c688eb6b050"></a>

### `MSPM0_PIN_FUNCTION_11`

```c
#define MSPM0_PIN_FUNCTION_11 (0x0000000B)
```

<a id="afb757ef697529cdee5be89103f84df48"></a>

### `MSPM0_PIN_FUNCTION_12`

```c
#define MSPM0_PIN_FUNCTION_12 (0x0000000C)
```

<a id="a355183103734ed847fb8ade45462982e"></a>

### `MSPM0_PIN_FUNCTION_13`

```c
#define MSPM0_PIN_FUNCTION_13 (0x0000000D)
```

<a id="ab865c1b4170a46f6d6ed9732ad2cab6e"></a>

### `MSPM0_PIN_FUNCTION_14`

```c
#define MSPM0_PIN_FUNCTION_14 (0x0000000E)
```

<a id="ac07cbab89aca7270479121cc8f951e58"></a>

### `MSPM0_PIN_FUNCTION_15`

```c
#define MSPM0_PIN_FUNCTION_15 (0x0000000F)
```

<a id="a2d119d2da878acd9ebac10c6d0cc7c80"></a>

### `MSPM0_PIN_FUNCTION_2`

```c
#define MSPM0_PIN_FUNCTION_2 (0x00000002)
```

<a id="a4cdd8ded8a55c33f3b586152d64b2621"></a>

### `MSPM0_PIN_FUNCTION_3`

```c
#define MSPM0_PIN_FUNCTION_3 (0x00000003)
```

<a id="a897c32ff405a8c4eeaaffed7a6c69d5a"></a>

### `MSPM0_PIN_FUNCTION_4`

```c
#define MSPM0_PIN_FUNCTION_4 (0x00000004)
```

<a id="ab6ec2101ebc8d171852da5c72a9e6ff1"></a>

### `MSPM0_PIN_FUNCTION_5`

```c
#define MSPM0_PIN_FUNCTION_5 (0x00000005)
```

<a id="a4891b06c78d726a4806ea7f8c18d2bbc"></a>

### `MSPM0_PIN_FUNCTION_6`

```c
#define MSPM0_PIN_FUNCTION_6 (0x00000006)
```

<a id="af2b0ea70556adb258d70cbb7274dce12"></a>

### `MSPM0_PIN_FUNCTION_7`

```c
#define MSPM0_PIN_FUNCTION_7 (0x00000007)
```

<a id="a250cc53f70b280ed5a909f5b968f2c0b"></a>

### `MSPM0_PIN_FUNCTION_8`

```c
#define MSPM0_PIN_FUNCTION_8 (0x00000008)
```

<a id="affb9f84a279ac6ec00f153d024282b05"></a>

### `MSPM0_PIN_FUNCTION_9`

```c
#define MSPM0_PIN_FUNCTION_9 (0x00000009)
```

<a id="aed042e160fbf0499081e08f32b485ccc"></a>

### `MSPM0_PIN_FUNCTION_ANALOG`

```c
#define MSPM0_PIN_FUNCTION_ANALOG (0x00000000)
```

<a id="aafceb12e339618d1282aa7300507d9a5"></a>

### `MSPM0_PIN_FUNCTION_GPIO`

```c
#define MSPM0_PIN_FUNCTION_GPIO (0x00000001)
```


## 233.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P120_mspm0-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P232_zephyr__usb__msos_desc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P234_zephyr__dt-bindings__pinctrl__mt8188-pinctrl.h_文件参考.md)
