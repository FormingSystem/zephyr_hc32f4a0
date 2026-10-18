---
id: learning.zephyr-docs.api-file-reference.page-502
title: zephyr__dt-bindings__clock__silabs__xg23-clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg23-clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第502章\_zephyr\_\_dt-bindings\_\_clock\_\_silabs\_\_xg23-clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xg23-clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-clock.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 502.1\_宏定义（Macros）

<a id="r_aa32e8dd815ce9bdc0b7522870897dcb6"></a>

```c
#define CLOCK_ACMP0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

相关声明：[CLOCK_ACMP0](#aa32e8dd815ce9bdc0b7522870897dcb6)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae61fef5c45a7a46b73ab7da7626c2b0e"></a>

```c
#define CLOCK_ACMP1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 19))
```

相关声明：[CLOCK_ACMP1](#ae61fef5c45a7a46b73ab7da7626c2b0e)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ac423554c8fbc051d4e0a92ac522c12fd"></a>

```c
#define CLOCK_AGC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

相关声明：[CLOCK_AGC](#ac423554c8fbc051d4e0a92ac522c12fd)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae337a36d2929e0fb5bfae761fb5e4133"></a>

```c
#define CLOCK_AMUXCP0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 11))
```

相关声明：[CLOCK_AMUXCP0](#ae337a36d2929e0fb5bfae761fb5e4133)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a96e069b371ff072641af60e430fde7ce"></a>

```c
#define CLOCK_BUFC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 11))
```

相关声明：[CLOCK_BUFC](#a96e069b371ff072641af60e430fde7ce)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a8cf43d2d70becc6693f00f1d13df6672"></a>

```c
#define CLOCK_BURAM (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 28))
```

相关声明：[CLOCK_BURAM](#a8cf43d2d70becc6693f00f1d13df6672)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ac6695946933b50787d425561a25e9dce"></a>

```c
#define CLOCK_BURTC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 29))
```

相关声明：[CLOCK_BURTC](#ac6695946933b50787d425561a25e9dce)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a9504e14e6a046f49d4ef84eeae2df2bf"></a>

```c
#define CLOCK_DCDC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

相关声明：[CLOCK_DCDC](#a9504e14e6a046f49d4ef84eeae2df2bf)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a8e50572855850c3f04e1114a1520a140"></a>

```c
#define CLOCK_DMEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

相关声明：[CLOCK_DMEM](#a8e50572855850c3f04e1114a1520a140)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a43e09951e6aa4e639eae06a5e0c6677a"></a>

```c
#define CLOCK_DPLL0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

相关声明：[CLOCK_DPLL0](#a43e09951e6aa4e639eae06a5e0c6677a)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_af8d36ae7fb5a31d6acf4e3f3972bd619"></a>

```c
#define CLOCK_ECAIFADC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 28))
```

相关声明：[CLOCK_ECAIFADC](#af8d36ae7fb5a31d6acf4e3f3972bd619)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a1d5233b4a9be81005ddf56f66568baec"></a>

```c
#define CLOCK_EUSART0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

相关声明：[CLOCK_EUSART0](#a1d5233b4a9be81005ddf56f66568baec)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad398276d374ded1ccf287e1c045bd044"></a>

```c
#define CLOCK_EUSART1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

相关声明：[CLOCK_EUSART1](#ad398276d374ded1ccf287e1c045bd044)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a7977b89e1ca130aa9fbedb17faf90680"></a>

```c
#define CLOCK_EUSART2 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

相关声明：[CLOCK_EUSART2](#a7977b89e1ca130aa9fbedb17faf90680)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a2353de593fcfd3470ea74ac3f31a5733"></a>

```c
#define CLOCK_FRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

相关声明：[CLOCK_FRC](#a2353de593fcfd3470ea74ac3f31a5733)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_abfe043f434d02bdfe02fbfb3d366b635"></a>

```c
#define CLOCK_FSRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

相关声明：[CLOCK_FSRCO](#abfe043f434d02bdfe02fbfb3d366b635)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_acf6f54d61368bab9ce995f5110043a16"></a>

```c
#define CLOCK_GPCRC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

相关声明：[CLOCK_GPCRC0](#acf6f54d61368bab9ce995f5110043a16)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ac9a5b112066c69cd6a28a5baa5d97763"></a>

```c
#define CLOCK_GPIO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 26))
```

相关声明：[CLOCK_GPIO](#ac9a5b112066c69cd6a28a5baa5d97763)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a4033b997dcc4154c2a0a45ac5e268b34"></a>

```c
#define CLOCK_HFRCO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

相关声明：[CLOCK_HFRCO0](#a4033b997dcc4154c2a0a45ac5e268b34)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a09a36ffa8404e69c113b6740c6dc56f7"></a>

```c
#define CLOCK_HFRCOEM23 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 19))
```

相关声明：[CLOCK_HFRCOEM23](#a09a36ffa8404e69c113b6740c6dc56f7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a211db0ef9eb5fd922a1da0d176bbd77f"></a>

```c
#define CLOCK_HFXO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 20))
```

相关声明：[CLOCK_HFXO0](#a211db0ef9eb5fd922a1da0d176bbd77f)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a4675a43d737508b80a9855fb6039d1a4"></a>

```c
#define CLOCK_HOSTMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

相关声明：[CLOCK_HOSTMAILBOX](#a4675a43d737508b80a9855fb6039d1a4)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a65099db536e93d1a86dd906b60eea384"></a>

```c
#define CLOCK_I2C0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

相关声明：[CLOCK_I2C0](#a65099db536e93d1a86dd906b60eea384)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a1222ea08bdd44c6134086340603db3ef"></a>

```c
#define CLOCK_I2C1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

相关声明：[CLOCK_I2C1](#a1222ea08bdd44c6134086340603db3ef)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a70da15f668624c0248a0658d6f67045b"></a>

```c
#define CLOCK_IADC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

相关声明：[CLOCK_IADC0](#a70da15f668624c0248a0658d6f67045b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_afaa58305165ee49bb49ecfad5a8921cb"></a>

```c
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

相关声明：[CLOCK_ICACHE0](#afaa58305165ee49bb49ecfad5a8921cb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_abf9a2c01e905a1719bab856ef72102e8"></a>

```c
#define CLOCK_KEYSCAN (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

相关声明：[CLOCK_KEYSCAN](#abf9a2c01e905a1719bab856ef72102e8)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a369a74516976a78dab6fc95c7d34b134"></a>

```c
#define CLOCK_LCD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

相关声明：[CLOCK_LCD](#a369a74516976a78dab6fc95c7d34b134)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a0b7b2229ddfaf6fa50a563fbf528cab1"></a>

```c
#define CLOCK_LDMA0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

相关声明：[CLOCK_LDMA0](#a0b7b2229ddfaf6fa50a563fbf528cab1)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_afe5cc402821e803fab34737c189cec7a"></a>

```c
#define CLOCK_LDMAXBAR0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

相关声明：[CLOCK_LDMAXBAR0](#afe5cc402821e803fab34737c189cec7a)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a164bf1750d9dff0806966e3d957967b3"></a>

```c
#define CLOCK_LESENSE (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

相关声明：[CLOCK_LESENSE](#a164bf1750d9dff0806966e3d957967b3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad870dd62c2096ad2900ef45e6712fb49"></a>

```c
#define CLOCK_LETIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

相关声明：[CLOCK_LETIMER0](#ad870dd62c2096ad2900ef45e6712fb49)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad2d432d8875b83c61dc68cdd4af502eb"></a>

```c
#define CLOCK_LFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

相关声明：[CLOCK_LFRCO](#ad2d432d8875b83c61dc68cdd4af502eb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a733a59a9c18f28f1be26d1130db4efea"></a>

```c
#define CLOCK_LFXO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

相关声明：[CLOCK_LFXO](#a733a59a9c18f28f1be26d1130db4efea)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a607ed604d7ba35581c270d2d709c61d3"></a>

```c
#define CLOCK_MODEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

相关声明：[CLOCK_MODEM](#a607ed604d7ba35581c270d2d709c61d3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a5a31a3404f0493d75883df158a1aced7"></a>

```c
#define CLOCK_MSC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

相关声明：[CLOCK_MSC](#a5a31a3404f0493d75883df158a1aced7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad545d81b3eb92be7af16bda62992d836"></a>

```c
#define CLOCK_PCNT0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

相关声明：[CLOCK_PCNT0](#ad545d81b3eb92be7af16bda62992d836)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a176efcb9464ddb31ea542656e9135e8c"></a>

```c
#define CLOCK_PROTIMER (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

相关声明：[CLOCK_PROTIMER](#a176efcb9464ddb31ea542656e9135e8c)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a2817c4a05dcc4e1396ec6c63a367f447"></a>

```c
#define CLOCK_PRS (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

相关声明：[CLOCK_PRS](#a2817c4a05dcc4e1396ec6c63a367f447)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a9a0ffab31dccc0d5d51714b77e3634e9"></a>

```c
#define CLOCK_RAC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

相关声明：[CLOCK_RAC](#a9a0ffab31dccc0d5d51714b77e3634e9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a295e418f558aaeb62205b7cf36a8323d"></a>

```c
#define CLOCK_RADIOAES (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_RADIOAES](#a295e418f558aaeb62205b7cf36a8323d)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ab5c58598f68a536bc02cef4c637ba7f3"></a>

```c
#define CLOCK_RFCRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_RFCRC](#ab5c58598f68a536bc02cef4c637ba7f3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a0c8c44e37a5079d0f1341d4bdd34f29d"></a>

```c
#define CLOCK_RFECA0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

相关声明：[CLOCK_RFECA0](#a0c8c44e37a5079d0f1341d4bdd34f29d)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a84ad7235efe443d2d3b3d6d96055fd72"></a>

```c
#define CLOCK_RFECA1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 26))
```

相关声明：[CLOCK_RFECA1](#a84ad7235efe443d2d3b3d6d96055fd72)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a8a6a93f7fc102a4f4e6c065fa82bca98"></a>

```c
#define CLOCK_RFMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

相关声明：[CLOCK_RFMAILBOX](#a8a6a93f7fc102a4f4e6c065fa82bca98)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae2611f620e722482b43df43a0e9521e6"></a>

```c
#define CLOCK_RFSCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

相关声明：[CLOCK_RFSCRATCHPAD](#ae2611f620e722482b43df43a0e9521e6)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a93f506b24bf622e44f63cf610fe31f41"></a>

```c
#define CLOCK_SEMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

相关声明：[CLOCK_SEMAILBOX](#a93f506b24bf622e44f63cf610fe31f41)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a0f07f886f88f078cae0881b0acb52cc0"></a>

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

相关声明：[CLOCK_SMU](#a0f07f886f88f078cae0881b0acb52cc0)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_aa6a892710ce9bf2be66d3e8fe841e6e1"></a>

```c
#define CLOCK_SYNTH (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

相关声明：[CLOCK_SYNTH](#aa6a892710ce9bf2be66d3e8fe841e6e1)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a329ef704c35a3eaa8d090df174447fb9"></a>

```c
#define CLOCK_SYSCFG (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

相关声明：[CLOCK_SYSCFG](#a329ef704c35a3eaa8d090df174447fb9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a25b5c00156e05033439f8dbd15370e2f"></a>

```c
#define CLOCK_SYSRTC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

相关声明：[CLOCK_SYSRTC0](#a25b5c00156e05033439f8dbd15370e2f)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_aaadc635085924c9617dad97b02599427"></a>

```c
#define CLOCK_TIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

相关声明：[CLOCK_TIMER0](#aaadc635085924c9617dad97b02599427)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_aecedef6c3a70a73218e22df6e0eaddf0"></a>

```c
#define CLOCK_TIMER1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

相关声明：[CLOCK_TIMER1](#aecedef6c3a70a73218e22df6e0eaddf0)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a851d358e4228381ab0e07d0ac2cff900"></a>

```c
#define CLOCK_TIMER2 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

相关声明：[CLOCK_TIMER2](#a851d358e4228381ab0e07d0ac2cff900)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ab3325cceec53072d0a1d6a3b891e9d2f"></a>

```c
#define CLOCK_TIMER3 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

相关声明：[CLOCK_TIMER3](#ab3325cceec53072d0a1d6a3b891e9d2f)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae21cf62d77f707b63565874f43991907"></a>

```c
#define CLOCK_TIMER4 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

相关声明：[CLOCK_TIMER4](#ae21cf62d77f707b63565874f43991907)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae47c38f62d4a6a8b00bfa83820c242d3"></a>

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

相关声明：[CLOCK_ULFRCO](#ae47c38f62d4a6a8b00bfa83820c242d3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a3efea2284aac64b602f7fdb9ebd301ae"></a>

```c
#define CLOCK_USART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

相关声明：[CLOCK_USART0](#a3efea2284aac64b602f7fdb9ebd301ae)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a5ffac1952fae08520cd6794a77f61591"></a>

```c
#define CLOCK_VDAC0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 20))
```

相关声明：[CLOCK_VDAC0](#a5ffac1952fae08520cd6794a77f61591)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad2c27e5766fc2d7d458b62cfd7670d94"></a>

```c
#define CLOCK_WDOG0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

相关声明：[CLOCK_WDOG0](#ad2c27e5766fc2d7d458b62cfd7670d94)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a15d2f4f9261ee4a748a5c25b9e956618"></a>

```c
#define CLOCK_WDOG1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

相关声明：[CLOCK_WDOG1](#a15d2f4f9261ee4a748a5c25b9e956618)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

## 502.2\_详细说明（Detailed Documentation）

<a id="aa32e8dd815ce9bdc0b7522870897dcb6"></a>

### `CLOCK_ACMP0`

```c
#define CLOCK_ACMP0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

<a id="ae61fef5c45a7a46b73ab7da7626c2b0e"></a>

### `CLOCK_ACMP1`

```c
#define CLOCK_ACMP1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 19))
```

<a id="ac423554c8fbc051d4e0a92ac522c12fd"></a>

### `CLOCK_AGC`

```c
#define CLOCK_AGC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

<a id="ae337a36d2929e0fb5bfae761fb5e4133"></a>

### `CLOCK_AMUXCP0`

```c
#define CLOCK_AMUXCP0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 11))
```

<a id="a96e069b371ff072641af60e430fde7ce"></a>

### `CLOCK_BUFC`

```c
#define CLOCK_BUFC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 11))
```

<a id="a8cf43d2d70becc6693f00f1d13df6672"></a>

### `CLOCK_BURAM`

```c
#define CLOCK_BURAM (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 28))
```

<a id="ac6695946933b50787d425561a25e9dce"></a>

### `CLOCK_BURTC`

```c
#define CLOCK_BURTC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 29))
```

<a id="a9504e14e6a046f49d4ef84eeae2df2bf"></a>

### `CLOCK_DCDC`

```c
#define CLOCK_DCDC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

<a id="a8e50572855850c3f04e1114a1520a140"></a>

### `CLOCK_DMEM`

```c
#define CLOCK_DMEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

<a id="a43e09951e6aa4e639eae06a5e0c6677a"></a>

### `CLOCK_DPLL0`

```c
#define CLOCK_DPLL0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

<a id="af8d36ae7fb5a31d6acf4e3f3972bd619"></a>

### `CLOCK_ECAIFADC`

```c
#define CLOCK_ECAIFADC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 28))
```

<a id="a1d5233b4a9be81005ddf56f66568baec"></a>

### `CLOCK_EUSART0`

```c
#define CLOCK_EUSART0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

<a id="ad398276d374ded1ccf287e1c045bd044"></a>

### `CLOCK_EUSART1`

```c
#define CLOCK_EUSART1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

<a id="a7977b89e1ca130aa9fbedb17faf90680"></a>

### `CLOCK_EUSART2`

```c
#define CLOCK_EUSART2 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

<a id="a2353de593fcfd3470ea74ac3f31a5733"></a>

### `CLOCK_FRC`

```c
#define CLOCK_FRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

<a id="abfe043f434d02bdfe02fbfb3d366b635"></a>

### `CLOCK_FSRCO`

```c
#define CLOCK_FSRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

<a id="acf6f54d61368bab9ce995f5110043a16"></a>

### `CLOCK_GPCRC0`

```c
#define CLOCK_GPCRC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

<a id="ac9a5b112066c69cd6a28a5baa5d97763"></a>

### `CLOCK_GPIO`

```c
#define CLOCK_GPIO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 26))
```

<a id="a4033b997dcc4154c2a0a45ac5e268b34"></a>

### `CLOCK_HFRCO0`

```c
#define CLOCK_HFRCO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

<a id="a09a36ffa8404e69c113b6740c6dc56f7"></a>

### `CLOCK_HFRCOEM23`

```c
#define CLOCK_HFRCOEM23 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 19))
```

<a id="a211db0ef9eb5fd922a1da0d176bbd77f"></a>

### `CLOCK_HFXO0`

```c
#define CLOCK_HFXO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 20))
```

<a id="a4675a43d737508b80a9855fb6039d1a4"></a>

### `CLOCK_HOSTMAILBOX`

```c
#define CLOCK_HOSTMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

<a id="a65099db536e93d1a86dd906b60eea384"></a>

### `CLOCK_I2C0`

```c
#define CLOCK_I2C0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

<a id="a1222ea08bdd44c6134086340603db3ef"></a>

### `CLOCK_I2C1`

```c
#define CLOCK_I2C1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

<a id="a70da15f668624c0248a0658d6f67045b"></a>

### `CLOCK_IADC0`

```c
#define CLOCK_IADC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

<a id="afaa58305165ee49bb49ecfad5a8921cb"></a>

### `CLOCK_ICACHE0`

```c
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

<a id="abf9a2c01e905a1719bab856ef72102e8"></a>

### `CLOCK_KEYSCAN`

```c
#define CLOCK_KEYSCAN (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

<a id="a369a74516976a78dab6fc95c7d34b134"></a>

### `CLOCK_LCD`

```c
#define CLOCK_LCD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

<a id="a0b7b2229ddfaf6fa50a563fbf528cab1"></a>

### `CLOCK_LDMA0`

```c
#define CLOCK_LDMA0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

<a id="afe5cc402821e803fab34737c189cec7a"></a>

### `CLOCK_LDMAXBAR0`

```c
#define CLOCK_LDMAXBAR0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

<a id="a164bf1750d9dff0806966e3d957967b3"></a>

### `CLOCK_LESENSE`

```c
#define CLOCK_LESENSE (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

<a id="ad870dd62c2096ad2900ef45e6712fb49"></a>

### `CLOCK_LETIMER0`

```c
#define CLOCK_LETIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

<a id="ad2d432d8875b83c61dc68cdd4af502eb"></a>

### `CLOCK_LFRCO`

```c
#define CLOCK_LFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

<a id="a733a59a9c18f28f1be26d1130db4efea"></a>

### `CLOCK_LFXO`

```c
#define CLOCK_LFXO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

<a id="a607ed604d7ba35581c270d2d709c61d3"></a>

### `CLOCK_MODEM`

```c
#define CLOCK_MODEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

<a id="a5a31a3404f0493d75883df158a1aced7"></a>

### `CLOCK_MSC`

```c
#define CLOCK_MSC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

<a id="ad545d81b3eb92be7af16bda62992d836"></a>

### `CLOCK_PCNT0`

```c
#define CLOCK_PCNT0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

<a id="a176efcb9464ddb31ea542656e9135e8c"></a>

### `CLOCK_PROTIMER`

```c
#define CLOCK_PROTIMER (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

<a id="a2817c4a05dcc4e1396ec6c63a367f447"></a>

### `CLOCK_PRS`

```c
#define CLOCK_PRS (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

<a id="a9a0ffab31dccc0d5d51714b77e3634e9"></a>

### `CLOCK_RAC`

```c
#define CLOCK_RAC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

<a id="a295e418f558aaeb62205b7cf36a8323d"></a>

### `CLOCK_RADIOAES`

```c
#define CLOCK_RADIOAES (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

<a id="ab5c58598f68a536bc02cef4c637ba7f3"></a>

### `CLOCK_RFCRC`

```c
#define CLOCK_RFCRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

<a id="a0c8c44e37a5079d0f1341d4bdd34f29d"></a>

### `CLOCK_RFECA0`

```c
#define CLOCK_RFECA0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

<a id="a84ad7235efe443d2d3b3d6d96055fd72"></a>

### `CLOCK_RFECA1`

```c
#define CLOCK_RFECA1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 26))
```

<a id="a8a6a93f7fc102a4f4e6c065fa82bca98"></a>

### `CLOCK_RFMAILBOX`

```c
#define CLOCK_RFMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

<a id="ae2611f620e722482b43df43a0e9521e6"></a>

### `CLOCK_RFSCRATCHPAD`

```c
#define CLOCK_RFSCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

<a id="a93f506b24bf622e44f63cf610fe31f41"></a>

### `CLOCK_SEMAILBOX`

```c
#define CLOCK_SEMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

<a id="a0f07f886f88f078cae0881b0acb52cc0"></a>

### `CLOCK_SMU`

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

<a id="aa6a892710ce9bf2be66d3e8fe841e6e1"></a>

### `CLOCK_SYNTH`

```c
#define CLOCK_SYNTH (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

<a id="a329ef704c35a3eaa8d090df174447fb9"></a>

### `CLOCK_SYSCFG`

```c
#define CLOCK_SYSCFG (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

<a id="a25b5c00156e05033439f8dbd15370e2f"></a>

### `CLOCK_SYSRTC0`

```c
#define CLOCK_SYSRTC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

<a id="aaadc635085924c9617dad97b02599427"></a>

### `CLOCK_TIMER0`

```c
#define CLOCK_TIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

<a id="aecedef6c3a70a73218e22df6e0eaddf0"></a>

### `CLOCK_TIMER1`

```c
#define CLOCK_TIMER1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

<a id="a851d358e4228381ab0e07d0ac2cff900"></a>

### `CLOCK_TIMER2`

```c
#define CLOCK_TIMER2 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

<a id="ab3325cceec53072d0a1d6a3b891e9d2f"></a>

### `CLOCK_TIMER3`

```c
#define CLOCK_TIMER3 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

<a id="ae21cf62d77f707b63565874f43991907"></a>

### `CLOCK_TIMER4`

```c
#define CLOCK_TIMER4 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

<a id="ae47c38f62d4a6a8b00bfa83820c242d3"></a>

### `CLOCK_ULFRCO`

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

<a id="a3efea2284aac64b602f7fdb9ebd301ae"></a>

### `CLOCK_USART0`

```c
#define CLOCK_USART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

<a id="a5ffac1952fae08520cd6794a77f61591"></a>

### `CLOCK_VDAC0`

```c
#define CLOCK_VDAC0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 20))
```

<a id="ad2c27e5766fc2d7d458b62cfd7670d94"></a>

### `CLOCK_WDOG0`

```c
#define CLOCK_WDOG0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

<a id="a15d2f4f9261ee4a748a5c25b9e956618"></a>

### `CLOCK_WDOG1`

```c
#define CLOCK_WDOG1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```


## 502.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-clock.h](../api_source_supplement_reference/P033_common-clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P119_xg23-clock.h_源码浏览.md)
- [FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P501_zephyr__dt-bindings__pinctrl__silabs__xg22-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P503_zephyr__dt-bindings__pinctrl__silabs__xg23-pinctrl.h_文件参考.md)
