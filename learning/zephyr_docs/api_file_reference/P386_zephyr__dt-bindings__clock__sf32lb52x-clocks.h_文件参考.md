---
id: learning.zephyr-docs.api-file-reference.page-386
title: zephyr__dt-bindings__clock__sf32lb52x-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第386章\_zephyr\_\_dt-bindings\_\_clock\_\_sf32lb52x-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb52x-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "sf32lb-clocks-common.h"
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 386.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 寄存器偏移量（Register offsets）

<a id="r_add1fcfee2ae286fa1e63ab0caa226d5c"></a>

```c
#define SF32LB52X_RCC_ENR1 0x08U
```

相关声明：[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_af2954add83f72f366fdbef9c01cb21cd"></a>

```c
#define SF32LB52X_RCC_ENR2 0x0CU
```

相关声明：[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="define-members-1"></a>

### 外设时钟使能/禁用定义（Clock enable/disable definitions for peripherals）

<a id="r_a26ca3dde51e8c2c5e7b0155012bd8030"></a>

```c
#define SF32LB52X_CLOCK_DMAC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 0U)
```

相关声明：[SF32LB52X_CLOCK_DMAC1](#a26ca3dde51e8c2c5e7b0155012bd8030)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_aa55c5f51d669d1081380e3202a57a00f"></a>

```c
#define SF32LB52X_CLOCK_MAILBOX1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 1U)
```

相关声明：[SF32LB52X_CLOCK_MAILBOX1](#aa55c5f51d669d1081380e3202a57a00f)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_aa7363c0ecca506808c99a5c87ff20030"></a>

```c
#define SF32LB52X_CLOCK_PINMUX1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 2U)
```

相关声明：[SF32LB52X_CLOCK_PINMUX1](#aa7363c0ecca506808c99a5c87ff20030)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_af05211706d92bfd2f3f4523b4ef3e8d4"></a>

```c
#define SF32LB52X_CLOCK_USART2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 4U)
```

相关声明：[SF32LB52X_CLOCK_USART2](#af05211706d92bfd2f3f4523b4ef3e8d4)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_aa4eb2fe53f64df0285cb4d4f623491a1"></a>

```c
#define SF32LB52X_CLOCK_EZIP1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 5U)
```

相关声明：[SF32LB52X_CLOCK_EZIP1](#aa4eb2fe53f64df0285cb4d4f623491a1)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a45855fc9926dd02e92d53a0a9d309b25"></a>

```c
#define SF32LB52X_CLOCK_EPIC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 6U)
```

相关声明：[SF32LB52X_CLOCK_EPIC](#a45855fc9926dd02e92d53a0a9d309b25)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a691c1d42a5a4ad848d34c461d45be66c"></a>

```c
#define SF32LB52X_CLOCK_LCDC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 7U)
```

相关声明：[SF32LB52X_CLOCK_LCDC1](#a691c1d42a5a4ad848d34c461d45be66c)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a28db6307ef55c765c2feb5288452b8ce"></a>

```c
#define SF32LB52X_CLOCK_I2S1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 8U)
```

相关声明：[SF32LB52X_CLOCK_I2S1](#a28db6307ef55c765c2feb5288452b8ce)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a0ac8738a71d6d552c49641c0902c6f39"></a>

```c
#define SF32LB52X_CLOCK_SYSCFG1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 10U)
```

相关声明：[SF32LB52X_CLOCK_SYSCFG1](#a0ac8738a71d6d552c49641c0902c6f39)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a93086c1311d707b58b5d9aa8bcfdaf63"></a>

```c
#define SF32LB52X_CLOCK_EFUSEC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 11U)
```

相关声明：[SF32LB52X_CLOCK_EFUSEC](#a93086c1311d707b58b5d9aa8bcfdaf63)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_ae4322371a3cf4e3395709237a9d257bd"></a>

```c
#define SF32LB52X_CLOCK_AES SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 12U)
```

相关声明：[SF32LB52X_CLOCK_AES](#ae4322371a3cf4e3395709237a9d257bd)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a65b874c13ee024ed9ad4cf7ff1a2a78a"></a>

```c
#define SF32LB52X_CLOCK_CRC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 13U)
```

相关声明：[SF32LB52X_CLOCK_CRC1](#a65b874c13ee024ed9ad4cf7ff1a2a78a)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_ac40a074f6c72e35e1ab562bee7ce31b4"></a>

```c
#define SF32LB52X_CLOCK_TRNG SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 14U)
```

相关声明：[SF32LB52X_CLOCK_TRNG](#ac40a074f6c72e35e1ab562bee7ce31b4)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a6adfc49798786dbbc69fef9d34cf072b"></a>

```c
#define SF32LB52X_CLOCK_GPTIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 15U)
```

相关声明：[SF32LB52X_CLOCK_GPTIM1](#a6adfc49798786dbbc69fef9d34cf072b)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a02f6dd57c18798e03f3d8dc4105362b5"></a>

```c
#define SF32LB52X_CLOCK_GPTIM2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 16U)
```

相关声明：[SF32LB52X_CLOCK_GPTIM2](#a02f6dd57c18798e03f3d8dc4105362b5)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a47c6246a0c3c962fca89c32e132d7aed"></a>

```c
#define SF32LB52X_CLOCK_BTIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 17U)
```

相关声明：[SF32LB52X_CLOCK_BTIM1](#a47c6246a0c3c962fca89c32e132d7aed)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a38c79f9d8c65e54c66f36d38c85f55dd"></a>

```c
#define SF32LB52X_CLOCK_BTIM2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 18U)
```

相关声明：[SF32LB52X_CLOCK_BTIM2](#a38c79f9d8c65e54c66f36d38c85f55dd)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a409836112eb7d78a728fac7e10eeb57a"></a>

```c
#define SF32LB52X_CLOCK_SPI1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 20U)
```

相关声明：[SF32LB52X_CLOCK_SPI1](#a409836112eb7d78a728fac7e10eeb57a)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a0011b9818e9da8c50d71af12a5d8f30d"></a>

```c
#define SF32LB52X_CLOCK_SPI2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 21U)
```

相关声明：[SF32LB52X_CLOCK_SPI2](#a0011b9818e9da8c50d71af12a5d8f30d)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a2bcdddb1279e2348a1828fbf98c54ac3"></a>

```c
#define SF32LB52X_CLOCK_EXTDMA SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 22U)
```

相关声明：[SF32LB52X_CLOCK_EXTDMA](#a2bcdddb1279e2348a1828fbf98c54ac3)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a00e040effe06cf87afaa39f01072a56a"></a>

```c
#define SF32LB52X_CLOCK_SECU1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 23U)
```

相关声明：[SF32LB52X_CLOCK_SECU1](#a00e040effe06cf87afaa39f01072a56a)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a10fa9a8214e54953685ecae98de9868b"></a>

```c
#define SF32LB52X_CLOCK_PDM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 25U)
```

相关声明：[SF32LB52X_CLOCK_PDM1](#a10fa9a8214e54953685ecae98de9868b)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a484dec35fdd911c41a66f0c7e50b5b0b"></a>

```c
#define SF32LB52X_CLOCK_I2C1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 27U)
```

相关声明：[SF32LB52X_CLOCK_I2C1](#a484dec35fdd911c41a66f0c7e50b5b0b)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a48954ea76adbdf73fb40935ce50cfe91"></a>

```c
#define SF32LB52X_CLOCK_I2C2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 28U)
```

相关声明：[SF32LB52X_CLOCK_I2C2](#a48954ea76adbdf73fb40935ce50cfe91)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_a84a7c9e0473120f4941a097fccaee95c"></a>

```c
#define SF32LB52X_CLOCK_PTC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 31U)
```

相关声明：[SF32LB52X_CLOCK_PTC1](#a84a7c9e0473120f4941a097fccaee95c)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR1](#add1fcfee2ae286fa1e63ab0caa226d5c)。

<a id="r_aefc2bd31a97dc0c1ab9d7364078fbaff"></a>

```c
#define SF32LB52X_CLOCK_GPIO1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 0U)
```

相关声明：[SF32LB52X_CLOCK_GPIO1](#aefc2bd31a97dc0c1ab9d7364078fbaff)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a8988ee96db0310e321ee74d4b836d4af"></a>

```c
#define SF32LB52X_CLOCK_MPI1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 1U)
```

相关声明：[SF32LB52X_CLOCK_MPI1](#a8988ee96db0310e321ee74d4b836d4af)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a6bfa0cc262b7e691c2d140709463c9b3"></a>

```c
#define SF32LB52X_CLOCK_MPI2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 2U)
```

相关声明：[SF32LB52X_CLOCK_MPI2](#a6bfa0cc262b7e691c2d140709463c9b3)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a59c3fba7ce6548e31322810ec91c7c8c"></a>

```c
#define SF32LB52X_CLOCK_SDMMC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 4U)
```

相关声明：[SF32LB52X_CLOCK_SDMMC1](#a59c3fba7ce6548e31322810ec91c7c8c)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_aa25325b6b06cb85591da54e091fafd7f"></a>

```c
#define SF32LB52X_CLOCK_USBC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 6U)
```

相关声明：[SF32LB52X_CLOCK_USBC](#aa25325b6b06cb85591da54e091fafd7f)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_ab6447d57b8be33d01fd54944a318374a"></a>

```c
#define SF32LB52X_CLOCK_I2C3 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 8U)
```

相关声明：[SF32LB52X_CLOCK_I2C3](#ab6447d57b8be33d01fd54944a318374a)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a66074def59a4895c0ce753f1edaa640d"></a>

```c
#define SF32LB52X_CLOCK_ATIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 9U)
```

相关声明：[SF32LB52X_CLOCK_ATIM1](#a66074def59a4895c0ce753f1edaa640d)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a086ae8e77a6ff30fde3fbe6e75cc7da5"></a>

```c
#define SF32LB52X_CLOCK_USART3 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 12U)
```

相关声明：[SF32LB52X_CLOCK_USART3](#a086ae8e77a6ff30fde3fbe6e75cc7da5)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a7568edfcee87632e4d9ce14676940bb9"></a>

```c
#define SF32LB52X_CLOCK_AUDCODEC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 19U)
```

相关声明：[SF32LB52X_CLOCK_AUDCODEC](#a7568edfcee87632e4d9ce14676940bb9)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_a9a6ed25de14fc8639faf1d748b317bed"></a>

```c
#define SF32LB52X_CLOCK_AUDPRC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 20U)
```

相关声明：[SF32LB52X_CLOCK_AUDPRC](#a9a6ed25de14fc8639faf1d748b317bed)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_abf78f3296805dbd3e67d3efbd8224ed0"></a>

```c
#define SF32LB52X_CLOCK_GPADC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 22U)
```

相关声明：[SF32LB52X_CLOCK_GPADC](#abf78f3296805dbd3e67d3efbd8224ed0)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_aaf4d491f7cda9fa7169b14a31f1a2402"></a>

```c
#define SF32LB52X_CLOCK_TSEN SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 23U)
```

相关声明：[SF32LB52X_CLOCK_TSEN](#aaf4d491f7cda9fa7169b14a31f1a2402)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

<a id="r_ac8709dcf4b0332c8329b3507eab36ac2"></a>

```c
#define SF32LB52X_CLOCK_I2C4 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 25U)
```

相关声明：[SF32LB52X_CLOCK_I2C4](#ac8709dcf4b0332c8329b3507eab36ac2)、[SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)、[SF32LB52X_RCC_ENR2](#af2954add83f72f366fdbef9c01cb21cd)。

## 386.2\_详细说明（Detailed Documentation）

<a id="ae4322371a3cf4e3395709237a9d257bd"></a>

### `SF32LB52X_CLOCK_AES`

```c
#define SF32LB52X_CLOCK_AES SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 12U)
```

<a id="a66074def59a4895c0ce753f1edaa640d"></a>

### `SF32LB52X_CLOCK_ATIM1`

```c
#define SF32LB52X_CLOCK_ATIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 9U)
```

<a id="a7568edfcee87632e4d9ce14676940bb9"></a>

### `SF32LB52X_CLOCK_AUDCODEC`

```c
#define SF32LB52X_CLOCK_AUDCODEC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 19U)
```

<a id="a9a6ed25de14fc8639faf1d748b317bed"></a>

### `SF32LB52X_CLOCK_AUDPRC`

```c
#define SF32LB52X_CLOCK_AUDPRC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 20U)
```

<a id="a47c6246a0c3c962fca89c32e132d7aed"></a>

### `SF32LB52X_CLOCK_BTIM1`

```c
#define SF32LB52X_CLOCK_BTIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 17U)
```

<a id="a38c79f9d8c65e54c66f36d38c85f55dd"></a>

### `SF32LB52X_CLOCK_BTIM2`

```c
#define SF32LB52X_CLOCK_BTIM2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 18U)
```

<a id="a65b874c13ee024ed9ad4cf7ff1a2a78a"></a>

### `SF32LB52X_CLOCK_CRC1`

```c
#define SF32LB52X_CLOCK_CRC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 13U)
```

<a id="a26ca3dde51e8c2c5e7b0155012bd8030"></a>

### `SF32LB52X_CLOCK_DMAC1`

```c
#define SF32LB52X_CLOCK_DMAC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 0U)
```

<a id="a93086c1311d707b58b5d9aa8bcfdaf63"></a>

### `SF32LB52X_CLOCK_EFUSEC`

```c
#define SF32LB52X_CLOCK_EFUSEC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 11U)
```

<a id="a45855fc9926dd02e92d53a0a9d309b25"></a>

### `SF32LB52X_CLOCK_EPIC`

```c
#define SF32LB52X_CLOCK_EPIC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 6U)
```

<a id="a2bcdddb1279e2348a1828fbf98c54ac3"></a>

### `SF32LB52X_CLOCK_EXTDMA`

```c
#define SF32LB52X_CLOCK_EXTDMA SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 22U)
```

<a id="aa4eb2fe53f64df0285cb4d4f623491a1"></a>

### `SF32LB52X_CLOCK_EZIP1`

```c
#define SF32LB52X_CLOCK_EZIP1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 5U)
```

<a id="abf78f3296805dbd3e67d3efbd8224ed0"></a>

### `SF32LB52X_CLOCK_GPADC`

```c
#define SF32LB52X_CLOCK_GPADC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 22U)
```

<a id="aefc2bd31a97dc0c1ab9d7364078fbaff"></a>

### `SF32LB52X_CLOCK_GPIO1`

```c
#define SF32LB52X_CLOCK_GPIO1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 0U)
```

<a id="a6adfc49798786dbbc69fef9d34cf072b"></a>

### `SF32LB52X_CLOCK_GPTIM1`

```c
#define SF32LB52X_CLOCK_GPTIM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 15U)
```

<a id="a02f6dd57c18798e03f3d8dc4105362b5"></a>

### `SF32LB52X_CLOCK_GPTIM2`

```c
#define SF32LB52X_CLOCK_GPTIM2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 16U)
```

<a id="a484dec35fdd911c41a66f0c7e50b5b0b"></a>

### `SF32LB52X_CLOCK_I2C1`

```c
#define SF32LB52X_CLOCK_I2C1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 27U)
```

<a id="a48954ea76adbdf73fb40935ce50cfe91"></a>

### `SF32LB52X_CLOCK_I2C2`

```c
#define SF32LB52X_CLOCK_I2C2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 28U)
```

<a id="ab6447d57b8be33d01fd54944a318374a"></a>

### `SF32LB52X_CLOCK_I2C3`

```c
#define SF32LB52X_CLOCK_I2C3 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 8U)
```

<a id="ac8709dcf4b0332c8329b3507eab36ac2"></a>

### `SF32LB52X_CLOCK_I2C4`

```c
#define SF32LB52X_CLOCK_I2C4 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 25U)
```

<a id="a28db6307ef55c765c2feb5288452b8ce"></a>

### `SF32LB52X_CLOCK_I2S1`

```c
#define SF32LB52X_CLOCK_I2S1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 8U)
```

<a id="a691c1d42a5a4ad848d34c461d45be66c"></a>

### `SF32LB52X_CLOCK_LCDC1`

```c
#define SF32LB52X_CLOCK_LCDC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 7U)
```

<a id="aa55c5f51d669d1081380e3202a57a00f"></a>

### `SF32LB52X_CLOCK_MAILBOX1`

```c
#define SF32LB52X_CLOCK_MAILBOX1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 1U)
```

<a id="a8988ee96db0310e321ee74d4b836d4af"></a>

### `SF32LB52X_CLOCK_MPI1`

```c
#define SF32LB52X_CLOCK_MPI1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 1U)
```

<a id="a6bfa0cc262b7e691c2d140709463c9b3"></a>

### `SF32LB52X_CLOCK_MPI2`

```c
#define SF32LB52X_CLOCK_MPI2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 2U)
```

<a id="a10fa9a8214e54953685ecae98de9868b"></a>

### `SF32LB52X_CLOCK_PDM1`

```c
#define SF32LB52X_CLOCK_PDM1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 25U)
```

<a id="aa7363c0ecca506808c99a5c87ff20030"></a>

### `SF32LB52X_CLOCK_PINMUX1`

```c
#define SF32LB52X_CLOCK_PINMUX1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 2U)
```

<a id="a84a7c9e0473120f4941a097fccaee95c"></a>

### `SF32LB52X_CLOCK_PTC1`

```c
#define SF32LB52X_CLOCK_PTC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 31U)
```

<a id="a59c3fba7ce6548e31322810ec91c7c8c"></a>

### `SF32LB52X_CLOCK_SDMMC1`

```c
#define SF32LB52X_CLOCK_SDMMC1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 4U)
```

<a id="a00e040effe06cf87afaa39f01072a56a"></a>

### `SF32LB52X_CLOCK_SECU1`

```c
#define SF32LB52X_CLOCK_SECU1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 23U)
```

<a id="a409836112eb7d78a728fac7e10eeb57a"></a>

### `SF32LB52X_CLOCK_SPI1`

```c
#define SF32LB52X_CLOCK_SPI1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 20U)
```

<a id="a0011b9818e9da8c50d71af12a5d8f30d"></a>

### `SF32LB52X_CLOCK_SPI2`

```c
#define SF32LB52X_CLOCK_SPI2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 21U)
```

<a id="a0ac8738a71d6d552c49641c0902c6f39"></a>

### `SF32LB52X_CLOCK_SYSCFG1`

```c
#define SF32LB52X_CLOCK_SYSCFG1 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 10U)
```

<a id="ac40a074f6c72e35e1ab562bee7ce31b4"></a>

### `SF32LB52X_CLOCK_TRNG`

```c
#define SF32LB52X_CLOCK_TRNG SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 14U)
```

<a id="aaf4d491f7cda9fa7169b14a31f1a2402"></a>

### `SF32LB52X_CLOCK_TSEN`

```c
#define SF32LB52X_CLOCK_TSEN SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 23U)
```

<a id="af05211706d92bfd2f3f4523b4ef3e8d4"></a>

### `SF32LB52X_CLOCK_USART2`

```c
#define SF32LB52X_CLOCK_USART2 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR1, 4U)
```

<a id="a086ae8e77a6ff30fde3fbe6e75cc7da5"></a>

### `SF32LB52X_CLOCK_USART3`

```c
#define SF32LB52X_CLOCK_USART3 SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 12U)
```

<a id="aa25325b6b06cb85591da54e091fafd7f"></a>

### `SF32LB52X_CLOCK_USBC`

```c
#define SF32LB52X_CLOCK_USBC SF32LB_CLOCK_CONFIG(SF32LB52X_RCC_ENR2, 6U)
```

<a id="add1fcfee2ae286fa1e63ab0caa226d5c"></a>

### `SF32LB52X_RCC_ENR1`

```c
#define SF32LB52X_RCC_ENR1 0x08U
```

<a id="af2954add83f72f366fdbef9c01cb21cd"></a>

### `SF32LB52X_RCC_ENR2`

```c
#define SF32LB52X_RCC_ENR2 0x0CU
```


## 386.3\_原页交叉引用（Cross References）

- [sf32lb-clocks-common.h](../api_source_reference/P773_sf32lb-clocks-common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P776_sf32lb52x-clocks.h_源码浏览.md)
- [SF32LB_CLOCK_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/sf32lb-clocks-common_8h.html#ac43af3a4a22fac987df9725e4844a4b3)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P385_zephyr__dt-bindings__dma__sf32lb-dma-config.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P387_zephyr__dt-bindings__dma__sf32lb52x-dma.h_文件参考.md)
