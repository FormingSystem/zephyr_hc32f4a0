---
id: learning.zephyr-docs.api-file-reference.page-500
title: zephyr__dt-bindings__clock__silabs__xg22-clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xg22-clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第500章\_zephyr\_\_dt-bindings\_\_clock\_\_silabs\_\_xg22-clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/xg22-clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/dt-bindings/dt-util.h>
#include "common-clock.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 500.1\_宏定义（Macros）

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

<a id="r_a2170f4399df43d386c5f3820560a1b54"></a>

```c
#define CLOCK_CRYPTOACC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

相关声明：[CLOCK_CRYPTOACC](#a2170f4399df43d386c5f3820560a1b54)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a9504e14e6a046f49d4ef84eeae2df2bf"></a>

```c
#define CLOCK_DCDC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

相关声明：[CLOCK_DCDC](#a9504e14e6a046f49d4ef84eeae2df2bf)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a43e09951e6aa4e639eae06a5e0c6677a"></a>

```c
#define CLOCK_DPLL0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

相关声明：[CLOCK_DPLL0](#a43e09951e6aa4e639eae06a5e0c6677a)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_aba2f8dea0c00f5a4f463b9ad6bff77f5"></a>

```c
#define CLOCK_EUART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

相关声明：[CLOCK_EUART0](#aba2f8dea0c00f5a4f463b9ad6bff77f5)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a2353de593fcfd3470ea74ac3f31a5733"></a>

```c
#define CLOCK_FRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

相关声明：[CLOCK_FRC](#a2353de593fcfd3470ea74ac3f31a5733)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_abfe043f434d02bdfe02fbfb3d366b635"></a>

```c
#define CLOCK_FSRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 20))
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

<a id="r_a211db0ef9eb5fd922a1da0d176bbd77f"></a>

```c
#define CLOCK_HFXO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 19))
```

相关声明：[CLOCK_HFXO0](#a211db0ef9eb5fd922a1da0d176bbd77f)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

相关声明：[CLOCK_ICACHE0](#afaa58305165ee49bb49ecfad5a8921cb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a4ffbb3efafed0ed4103cce8b9f08ee6a"></a>

```c
#define CLOCK_IFADCDEBUG (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

相关声明：[CLOCK_IFADCDEBUG](#a4ffbb3efafed0ed4103cce8b9f08ee6a)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_ad870dd62c2096ad2900ef45e6712fb49"></a>

```c
#define CLOCK_LETIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

相关声明：[CLOCK_LETIMER0](#ad870dd62c2096ad2900ef45e6712fb49)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad2d432d8875b83c61dc68cdd4af502eb"></a>

```c
#define CLOCK_LFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

相关声明：[CLOCK_LFRCO](#ad2d432d8875b83c61dc68cdd4af502eb)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a733a59a9c18f28f1be26d1130db4efea"></a>

```c
#define CLOCK_LFXO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

相关声明：[CLOCK_LFXO](#a733a59a9c18f28f1be26d1130db4efea)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a607ed604d7ba35581c270d2d709c61d3"></a>

```c
#define CLOCK_MODEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

相关声明：[CLOCK_MODEM](#a607ed604d7ba35581c270d2d709c61d3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a5a31a3404f0493d75883df158a1aced7"></a>

```c
#define CLOCK_MSC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

相关声明：[CLOCK_MSC](#a5a31a3404f0493d75883df158a1aced7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a4fcbe02d02dd6a322ac3188753c545d7"></a>

```c
#define CLOCK_PDM (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

相关声明：[CLOCK_PDM](#a4fcbe02d02dd6a322ac3188753c545d7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ab7978619975bdabfa18ff167701171ba"></a>

```c
#define CLOCK_PRORTC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
```

相关声明：[CLOCK_PRORTC](#ab7978619975bdabfa18ff167701171ba)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

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

<a id="r_aac664d34e3aff1dd795ae8abc2918a31"></a>

```c
#define CLOCK_RDMAILBOX0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

相关声明：[CLOCK_RDMAILBOX0](#aac664d34e3aff1dd795ae8abc2918a31)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_afcc7ae1a98bdc3ce13b26a3a022f27c7"></a>

```c
#define CLOCK_RDMAILBOX1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

相关声明：[CLOCK_RDMAILBOX1](#afcc7ae1a98bdc3ce13b26a3a022f27c7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad1d5a0b0076aff81cd72a83bea2401c6"></a>

```c
#define CLOCK_RDSCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

相关声明：[CLOCK_RDSCRATCHPAD](#ad1d5a0b0076aff81cd72a83bea2401c6)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ab5c58598f68a536bc02cef4c637ba7f3"></a>

```c
#define CLOCK_RFCRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

相关声明：[CLOCK_RFCRC](#ab5c58598f68a536bc02cef4c637ba7f3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_af6af256796561991c11e10a8f28ec53b"></a>

```c
#define CLOCK_RFSENSE (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

相关声明：[CLOCK_RFSENSE](#af6af256796561991c11e10a8f28ec53b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a9e3fd16f09c2abd2370a1433cefd6b75"></a>

```c
#define CLOCK_RTCC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

相关声明：[CLOCK_RTCC](#a9e3fd16f09c2abd2370a1433cefd6b75)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a0f07f886f88f078cae0881b0acb52cc0"></a>

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
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
#define CLOCK_TIMER4 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

相关声明：[CLOCK_TIMER4](#ae21cf62d77f707b63565874f43991907)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ae47c38f62d4a6a8b00bfa83820c242d3"></a>

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

相关声明：[CLOCK_ULFRCO](#ae47c38f62d4a6a8b00bfa83820c242d3)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a3efea2284aac64b602f7fdb9ebd301ae"></a>

```c
#define CLOCK_USART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

相关声明：[CLOCK_USART0](#a3efea2284aac64b602f7fdb9ebd301ae)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_a01c6dffb9ec0c5a9aa29eb0c831601e7"></a>

```c
#define CLOCK_USART1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

相关声明：[CLOCK_USART1](#a01c6dffb9ec0c5a9aa29eb0c831601e7)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

<a id="r_ad2c27e5766fc2d7d458b62cfd7670d94"></a>

```c
#define CLOCK_WDOG0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

相关声明：[CLOCK_WDOG0](#ad2c27e5766fc2d7d458b62cfd7670d94)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)、[FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)。

## 500.2\_详细说明（Detailed Documentation）

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

<a id="a2170f4399df43d386c5f3820560a1b54"></a>

### `CLOCK_CRYPTOACC`

```c
#define CLOCK_CRYPTOACC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```

<a id="a9504e14e6a046f49d4ef84eeae2df2bf"></a>

### `CLOCK_DCDC`

```c
#define CLOCK_DCDC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 31))
```

<a id="a43e09951e6aa4e639eae06a5e0c6677a"></a>

### `CLOCK_DPLL0`

```c
#define CLOCK_DPLL0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

<a id="aba2f8dea0c00f5a4f463b9ad6bff77f5"></a>

### `CLOCK_EUART0`

```c
#define CLOCK_EUART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 24))
```

<a id="a2353de593fcfd3470ea74ac3f31a5733"></a>

### `CLOCK_FRC`

```c
#define CLOCK_FRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 3))
```

<a id="abfe043f434d02bdfe02fbfb3d366b635"></a>

### `CLOCK_FSRCO`

```c
#define CLOCK_FSRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 20))
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

<a id="a211db0ef9eb5fd922a1da0d176bbd77f"></a>

### `CLOCK_HFXO0`

```c
#define CLOCK_HFXO0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 19))
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
#define CLOCK_ICACHE0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 16))
```

<a id="a4ffbb3efafed0ed4103cce8b9f08ee6a"></a>

### `CLOCK_IFADCDEBUG`

```c
#define CLOCK_IFADCDEBUG (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 12))
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

<a id="ad870dd62c2096ad2900ef45e6712fb49"></a>

### `CLOCK_LETIMER0`

```c
#define CLOCK_LETIMER0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 12))
```

<a id="ad2d432d8875b83c61dc68cdd4af502eb"></a>

### `CLOCK_LFRCO`

```c
#define CLOCK_LFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 21))
```

<a id="a733a59a9c18f28f1be26d1130db4efea"></a>

### `CLOCK_LFXO`

```c
#define CLOCK_LFXO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 22))
```

<a id="a607ed604d7ba35581c270d2d709c61d3"></a>

### `CLOCK_MODEM`

```c
#define CLOCK_MODEM (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 1))
```

<a id="a5a31a3404f0493d75883df158a1aced7"></a>

### `CLOCK_MSC`

```c
#define CLOCK_MSC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 17))
```

<a id="a4fcbe02d02dd6a322ac3188753c545d7"></a>

### `CLOCK_PDM`

```c
#define CLOCK_PDM (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 25))
```

<a id="ab7978619975bdabfa18ff167701171ba"></a>

### `CLOCK_PRORTC`

```c
#define CLOCK_PRORTC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 10))
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

<a id="aac664d34e3aff1dd795ae8abc2918a31"></a>

### `CLOCK_RDMAILBOX0`

```c
#define CLOCK_RDMAILBOX0 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

<a id="afcc7ae1a98bdc3ce13b26a3a022f27c7"></a>

### `CLOCK_RDMAILBOX1`

```c
#define CLOCK_RDMAILBOX1 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

<a id="ad1d5a0b0076aff81cd72a83bea2401c6"></a>

### `CLOCK_RDSCRATCHPAD`

```c
#define CLOCK_RDSCRATCHPAD (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 7))
```

<a id="ab5c58598f68a536bc02cef4c637ba7f3"></a>

### `CLOCK_RFCRC`

```c
#define CLOCK_RFCRC (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 2))
```

<a id="af6af256796561991c11e10a8f28ec53b"></a>

### `CLOCK_RFSENSE`

```c
#define CLOCK_RFSENSE (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 14))
```

<a id="a9e3fd16f09c2abd2370a1433cefd6b75"></a>

### `CLOCK_RTCC`

```c
#define CLOCK_RTCC (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 30))
```

<a id="a0f07f886f88f078cae0881b0acb52cc0"></a>

### `CLOCK_SMU`

```c
#define CLOCK_SMU (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 15))
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
#define CLOCK_TIMER4 (FIELD_PREP(CLOCK_REG_MASK, 1) | FIELD_PREP(CLOCK_BIT_MASK, 18))
```

<a id="ae47c38f62d4a6a8b00bfa83820c242d3"></a>

### `CLOCK_ULFRCO`

```c
#define CLOCK_ULFRCO (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 23))
```

<a id="a3efea2284aac64b602f7fdb9ebd301ae"></a>

### `CLOCK_USART0`

```c
#define CLOCK_USART0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 8))
```

<a id="a01c6dffb9ec0c5a9aa29eb0c831601e7"></a>

### `CLOCK_USART1`

```c
#define CLOCK_USART1 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 9))
```

<a id="ad2c27e5766fc2d7d458b62cfd7670d94"></a>

### `CLOCK_WDOG0`

```c
#define CLOCK_WDOG0 (FIELD_PREP(CLOCK_REG_MASK, 0) | FIELD_PREP(CLOCK_BIT_MASK, 13))
```


## 500.3\_原页交叉引用（Cross References）

- [zephyr/dt-bindings/dt-util.h](../dt_bus_binding_reference/P006_设备树绑定工具头文件源码.md)
- [common-clock.h](../api_source_supplement_reference/P033_common-clock.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P118_xg22-clock.h_源码浏览.md)
- [FIELD_PREP](P394_zephyr__dt-bindings__pinctrl__silabs-pinctrl-siwx91x.h_文件参考.md#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P499_zephyr__dt-bindings__pinctrl__silabs__xg21-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P501_zephyr__dt-bindings__pinctrl__silabs__xg22-pinctrl.h_文件参考.md)
