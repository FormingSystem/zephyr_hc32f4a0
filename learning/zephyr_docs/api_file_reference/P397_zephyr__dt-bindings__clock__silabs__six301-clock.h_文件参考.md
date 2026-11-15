---
id: learning.zephyr-docs.api-file-reference.page-397
title: zephyr__dt-bindings__clock__silabs__six301-clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/six301-clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第397章\_zephyr\_\_dt-bindings\_\_clock\_\_silabs\_\_six301-clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/six301-clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-clock.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 397.1\_宏定义（Macros）

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

<a id="r_a04d6eee00651a4d7ad7f45ab6932aac9"></a>

```c
#define CLOCK_ADC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

相关声明：[CLOCK_ADC0](#a04d6eee00651a4d7ad7f45ab6932aac9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae337a36d2929e0fb5bfae761fb5e4133"></a>

```c
#define CLOCK_AMUXCP0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 11))
```

相关声明：[CLOCK_AMUXCP0](#ae337a36d2929e0fb5bfae761fb5e4133)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_a056daf4b540496e9b2f0f2976a38a1b5"></a>

```c
#define CLOCK_DEVINFO (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 28))
```

相关声明：[CLOCK_DEVINFO](#a056daf4b540496e9b2f0f2976a38a1b5)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_a9d84327fef6575980757c56ca1cb6a8d"></a>

```c
#define CLOCK_ETAMPDET (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_ETAMPDET](#a9d84327fef6575980757c56ca1cb6a8d)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_a5fc3c55ccea7211c78c86e9dec438076"></a>

```c
#define CLOCK_HOSTPORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

相关声明：[CLOCK_HOSTPORTAL](#a5fc3c55ccea7211c78c86e9dec438076)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_ad1e350a98bb9a38715af2cadd667e7cd"></a>

```c
#define CLOCK_I2C2 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

相关声明：[CLOCK_I2C2](#ad1e350a98bb9a38715af2cadd667e7cd)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_afaa58305165ee49bb49ecfad5a8921cb"></a>

```c
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

相关声明：[CLOCK_ICACHE0](#afaa58305165ee49bb49ecfad5a8921cb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_aa6deee5532a513dc42fc0e634e5c863e"></a>

```c
#define CLOCK_KSU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

相关声明：[CLOCK_KSU](#aa6deee5532a513dc42fc0e634e5c863e)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a604e807193ae87f026200b93c5291cff"></a>

```c
#define CLOCK_L2ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

相关声明：[CLOCK_L2ICACHE0](#a604e807193ae87f026200b93c5291cff)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_a7c96db322012811447e8f7bfb18d12c2"></a>

```c
#define CLOCK_LEDDRV0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

相关声明：[CLOCK_LEDDRV0](#a7c96db322012811447e8f7bfb18d12c2)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_a0ac57664edac238616e484f5008b0650"></a>

```c
#define CLOCK_LPWAES (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_LPWAES](#a0ac57664edac238616e484f5008b0650)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a3bbcc1ff5d766f9ff903223053653427"></a>

```c
#define CLOCK_LPW0PORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

相关声明：[CLOCK_LPW0PORTAL](#a3bbcc1ff5d766f9ff903223053653427)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad545d81b3eb92be7af16bda62992d836"></a>

```c
#define CLOCK_PCNT0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

相关声明：[CLOCK_PCNT0](#ad545d81b3eb92be7af16bda62992d836)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae136572ba910e507c2b1bedf43cec4b5"></a>

```c
#define CLOCK_PIXELRZ0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 29))
```

相关声明：[CLOCK_PIXELRZ0](#ae136572ba910e507c2b1bedf43cec4b5)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a872de8152786efd7496b1fa4416643b1"></a>

```c
#define CLOCK_PIXELRZ1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

相关声明：[CLOCK_PIXELRZ1](#a872de8152786efd7496b1fa4416643b1)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a2817c4a05dcc4e1396ec6c63a367f447"></a>

```c
#define CLOCK_PRS (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

相关声明：[CLOCK_PRS](#a2817c4a05dcc4e1396ec6c63a367f447)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_affad0b047e43532d5ef1ac165fa25d74"></a>

```c
#define CLOCK_RPA (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

相关声明：[CLOCK_RPA](#affad0b047e43532d5ef1ac165fa25d74)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a3459e8552a04b18961f38b676b71ffed"></a>

```c
#define CLOCK_SCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_SCRATCHPAD](#a3459e8552a04b18961f38b676b71ffed)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a93f506b24bf622e44f63cf610fe31f41"></a>

```c
#define CLOCK_SEMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

相关声明：[CLOCK_SEMAILBOX](#a93f506b24bf622e44f63cf610fe31f41)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_abdb48b69706d7e27c8b883ed932cf253"></a>

```c
#define CLOCK_SEMAPHORE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

相关声明：[CLOCK_SEMAPHORE0](#abdb48b69706d7e27c8b883ed932cf253)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a32d0f576d91e37e35a7f0dd363415b75"></a>

```c
#define CLOCK_SEMAPHORE1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

相关声明：[CLOCK_SEMAPHORE1](#a32d0f576d91e37e35a7f0dd363415b75)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ac448dbde4fcb24f9d29d993d2ddbd35a"></a>

```c
#define CLOCK_SEPORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

相关声明：[CLOCK_SEPORTAL](#ac448dbde4fcb24f9d29d993d2ddbd35a)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a0f07f886f88f078cae0881b0acb52cc0"></a>

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

相关声明：[CLOCK_SMU](#a0f07f886f88f078cae0881b0acb52cc0)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ac54472f4e38e39addf50e97a47e8d956"></a>

```c
#define CLOCK_SOCPLL0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

相关声明：[CLOCK_SOCPLL0](#ac54472f4e38e39addf50e97a47e8d956)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a4dca5d057510fe01032d9fdf64cb0cbb"></a>

```c
#define CLOCK_SYMCRYPTO (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

相关声明：[CLOCK_SYMCRYPTO](#a4dca5d057510fe01032d9fdf64cb0cbb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a329ef704c35a3eaa8d090df174447fb9"></a>

```c
#define CLOCK_SYSCFG (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

相关声明：[CLOCK_SYSCFG](#a329ef704c35a3eaa8d090df174447fb9)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a25b5c00156e05033439f8dbd15370e2f"></a>

```c
#define CLOCK_SYSRTC0 (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 0))
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

<a id="r_ae47c38f62d4a6a8b00bfa83820c242d3"></a>

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

相关声明：[CLOCK_ULFRCO](#ae47c38f62d4a6a8b00bfa83820c242d3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

## 397.2\_详细说明（Detailed Documentation）

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

<a id="a04d6eee00651a4d7ad7f45ab6932aac9"></a>

### `CLOCK_ADC0`

```c
#define CLOCK_ADC0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

<a id="ae337a36d2929e0fb5bfae761fb5e4133"></a>

### `CLOCK_AMUXCP0`

```c
#define CLOCK_AMUXCP0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 11))
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

<a id="a056daf4b540496e9b2f0f2976a38a1b5"></a>

### `CLOCK_DEVINFO`

```c
#define CLOCK_DEVINFO (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 28))
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

<a id="a9d84327fef6575980757c56ca1cb6a8d"></a>

### `CLOCK_ETAMPDET`

```c
#define CLOCK_ETAMPDET (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
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

<a id="a5fc3c55ccea7211c78c86e9dec438076"></a>

### `CLOCK_HOSTPORTAL`

```c
#define CLOCK_HOSTPORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 5))
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

<a id="ad1e350a98bb9a38715af2cadd667e7cd"></a>

### `CLOCK_I2C2`

```c
#define CLOCK_I2C2 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

<a id="afaa58305165ee49bb49ecfad5a8921cb"></a>

### `CLOCK_ICACHE0`

```c
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
```

<a id="aa6deee5532a513dc42fc0e634e5c863e"></a>

### `CLOCK_KSU`

```c
#define CLOCK_KSU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

<a id="a604e807193ae87f026200b93c5291cff"></a>

### `CLOCK_L2ICACHE0`

```c
#define CLOCK_L2ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
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

<a id="a7c96db322012811447e8f7bfb18d12c2"></a>

### `CLOCK_LEDDRV0`

```c
#define CLOCK_LEDDRV0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 6))
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

<a id="a3bbcc1ff5d766f9ff903223053653427"></a>

### `CLOCK_LPW0PORTAL`

```c
#define CLOCK_LPW0PORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 6))
```

<a id="a0ac57664edac238616e484f5008b0650"></a>

### `CLOCK_LPWAES`

```c
#define CLOCK_LPWAES (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

<a id="ad545d81b3eb92be7af16bda62992d836"></a>

### `CLOCK_PCNT0`

```c
#define CLOCK_PCNT0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

<a id="ae136572ba910e507c2b1bedf43cec4b5"></a>

### `CLOCK_PIXELRZ0`

```c
#define CLOCK_PIXELRZ0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 29))
```

<a id="a872de8152786efd7496b1fa4416643b1"></a>

### `CLOCK_PIXELRZ1`

```c
#define CLOCK_PIXELRZ1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

<a id="a2817c4a05dcc4e1396ec6c63a367f447"></a>

### `CLOCK_PRS`

```c
#define CLOCK_PRS (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 27))
```

<a id="affad0b047e43532d5ef1ac165fa25d74"></a>

### `CLOCK_RPA`

```c
#define CLOCK_RPA (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 0))
```

<a id="a3459e8552a04b18961f38b676b71ffed"></a>

### `CLOCK_SCRATCHPAD`

```c
#define CLOCK_SCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

<a id="a93f506b24bf622e44f63cf610fe31f41"></a>

### `CLOCK_SEMAILBOX`

```c
#define CLOCK_SEMAILBOX (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

<a id="abdb48b69706d7e27c8b883ed932cf253"></a>

### `CLOCK_SEMAPHORE0`

```c
#define CLOCK_SEMAPHORE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 4))
```

<a id="a32d0f576d91e37e35a7f0dd363415b75"></a>

### `CLOCK_SEMAPHORE1`

```c
#define CLOCK_SEMAPHORE1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 5))
```

<a id="ac448dbde4fcb24f9d29d993d2ddbd35a"></a>

### `CLOCK_SEPORTAL`

```c
#define CLOCK_SEPORTAL (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

<a id="a0f07f886f88f078cae0881b0acb52cc0"></a>

### `CLOCK_SMU`

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

<a id="ac54472f4e38e39addf50e97a47e8d956"></a>

### `CLOCK_SOCPLL0`

```c
#define CLOCK_SOCPLL0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

<a id="a4dca5d057510fe01032d9fdf64cb0cbb"></a>

### `CLOCK_SYMCRYPTO`

```c
#define CLOCK_SYMCRYPTO (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

<a id="a329ef704c35a3eaa8d090df174447fb9"></a>

### `CLOCK_SYSCFG`

```c
#define CLOCK_SYSCFG (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

<a id="a25b5c00156e05033439f8dbd15370e2f"></a>

### `CLOCK_SYSRTC0`

```c
#define CLOCK_SYSRTC0 (FIELD_PREP(CLOCK_REG_MASK, 3) | FIELD_PREP(CLOCK_BIT_MASK, 0))
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

<a id="ae47c38f62d4a6a8b00bfa83820c242d3"></a>

### `CLOCK_ULFRCO`

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
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


## 397.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-clock.h](../api_source_supplement_reference/P033_common-clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P103_six301-clock.h_源码浏览.md)
- [FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P396_zephyr__dt-bindings__pinctrl__silabs__siwx91x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P398_zephyr__dt-bindings__dma__silabs__six301-dma.h_文件参考.md)
