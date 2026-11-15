---
id: learning.zephyr-docs.api-file-reference.page-37
title: zephyr__dt-bindings__clock__ch32v00x-clocks.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ch32v00x-clocks_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_dt-bindings\_\_clock\_\_ch32v00x-clocks.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ch32v00x-clocks_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 37.1\_宏定义（Macros）

<a id="r_ae23b04c6f7dc288edd55ca371b0ac6ac"></a>

```c
#define CH32V00X_HB_PCENR_OFFSET 0
```

相关声明：[CH32V00X_HB_PCENR_OFFSET](#ae23b04c6f7dc288edd55ca371b0ac6ac)。

<a id="r_ac16a6b94e0d36222243acfe99bd576b1"></a>

```c
#define CH32V00X_PB2_PCENR_OFFSET 1
```

相关声明：[CH32V00X_PB2_PCENR_OFFSET](#ac16a6b94e0d36222243acfe99bd576b1)。

<a id="r_a4de5424f7b84a7be9525d3baaf95b372"></a>

```c
#define CH32V00X_PB1_PCENR_OFFSET 2
```

相关声明：[CH32V00X_PB1_PCENR_OFFSET](#a4de5424f7b84a7be9525d3baaf95b372)。

<a id="r_ab39a50912925831fd0f53da79caa1f3e"></a>

```c
#define CH32V00X_CLOCK_CONFIG(bus, bit)
```

相关声明：[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a673a85e0807d525d0d896968e72476d7"></a>

```c
#define CH32V00X_CLOCK_DMA1 CH32V00X_CLOCK_CONFIG(HB, 0)
```

相关声明：[CH32V00X_CLOCK_DMA1](#a673a85e0807d525d0d896968e72476d7)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_aea9e25b32bec97ba5c4d341a31523586"></a>

```c
#define CH32V00X_CLOCK_SRAM CH32V00X_CLOCK_CONFIG(HB, 2)
```

相关声明：[CH32V00X_CLOCK_SRAM](#aea9e25b32bec97ba5c4d341a31523586)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_adba8b05c326b5c50a5f46a4235347cd2"></a>

```c
#define CH32V00X_CLOCK_AFIO CH32V00X_CLOCK_CONFIG(PB2, 0)
```

相关声明：[CH32V00X_CLOCK_AFIO](#adba8b05c326b5c50a5f46a4235347cd2)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a6937d869f977cb90e519b2b92f98c120"></a>

```c
#define CH32V00X_CLOCK_IOPA CH32V00X_CLOCK_CONFIG(PB2, 2)
```

相关声明：[CH32V00X_CLOCK_IOPA](#a6937d869f977cb90e519b2b92f98c120)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a58487531bac2d11010fa719cc9b8bc5b"></a>

```c
#define CH32V00X_CLOCK_IOPB CH32V00X_CLOCK_CONFIG(PB2, 3)
```

相关声明：[CH32V00X_CLOCK_IOPB](#a58487531bac2d11010fa719cc9b8bc5b)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_af66030ec198edaa564110cc3b0a6b889"></a>

```c
#define CH32V00X_CLOCK_IOPC CH32V00X_CLOCK_CONFIG(PB2, 4)
```

相关声明：[CH32V00X_CLOCK_IOPC](#af66030ec198edaa564110cc3b0a6b889)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_aa2c9b9bc83471c7c0701685025ad45b9"></a>

```c
#define CH32V00X_CLOCK_IOPD CH32V00X_CLOCK_CONFIG(PB2, 5)
```

相关声明：[CH32V00X_CLOCK_IOPD](#aa2c9b9bc83471c7c0701685025ad45b9)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a4ddfcf15d13a740f3917034aa6aee075"></a>

```c
#define CH32V00X_CLOCK_ADC1 CH32V00X_CLOCK_CONFIG(PB2, 9)
```

相关声明：[CH32V00X_CLOCK_ADC1](#a4ddfcf15d13a740f3917034aa6aee075)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a35b5af6bc5e72b9360c923916cd2e0f1"></a>

```c
#define CH32V00X_CLOCK_TIM1 CH32V00X_CLOCK_CONFIG(PB2, 11)
```

相关声明：[CH32V00X_CLOCK_TIM1](#a35b5af6bc5e72b9360c923916cd2e0f1)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a9ee9b0e633a4a50809c2d2d1d437dd2b"></a>

```c
#define CH32V00X_CLOCK_SPI1 CH32V00X_CLOCK_CONFIG(PB2, 12)
```

相关声明：[CH32V00X_CLOCK_SPI1](#a9ee9b0e633a4a50809c2d2d1d437dd2b)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a7d61b5360a6d66ee4ca2210f3e1d32f2"></a>

```c
#define CH32V00X_CLOCK_USART2 CH32V00X_CLOCK_CONFIG(PB2, 13)
```

相关声明：[CH32V00X_CLOCK_USART2](#a7d61b5360a6d66ee4ca2210f3e1d32f2)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_af46cda54f5d666db759746a11909b148"></a>

```c
#define CH32V00X_CLOCK_USART1 CH32V00X_CLOCK_CONFIG(PB2, 14)
```

相关声明：[CH32V00X_CLOCK_USART1](#af46cda54f5d666db759746a11909b148)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a22cff65ee5b38ca47089ffa0916c8fda"></a>

```c
#define CH32V00X_CLOCK_TIM2 CH32V00X_CLOCK_CONFIG(PB1, 0)
```

相关声明：[CH32V00X_CLOCK_TIM2](#a22cff65ee5b38ca47089ffa0916c8fda)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a69c30a9fb4e812dff7c5d2b9834a012b"></a>

```c
#define CH32V00X_CLOCK_TIM3 CH32V00X_CLOCK_CONFIG(PB1, 2)
```

相关声明：[CH32V00X_CLOCK_TIM3](#a69c30a9fb4e812dff7c5d2b9834a012b)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_aa1b25307b070e0131c8d2883cc6daac2"></a>

```c
#define CH32V00X_CLOCK_WWDG CH32V00X_CLOCK_CONFIG(PB1, 11)
```

相关声明：[CH32V00X_CLOCK_WWDG](#aa1b25307b070e0131c8d2883cc6daac2)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_a44898d60cab2a44b6f11f44dcc910faf"></a>

```c
#define CH32V00X_CLOCK_I2C1 CH32V00X_CLOCK_CONFIG(PB1, 21)
```

相关声明：[CH32V00X_CLOCK_I2C1](#a44898d60cab2a44b6f11f44dcc910faf)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

<a id="r_ae70e92186311daf444e9b2a9c4891dcf"></a>

```c
#define CH32V00X_CLOCK_PWR CH32V00X_CLOCK_CONFIG(PB1, 28)
```

相关声明：[CH32V00X_CLOCK_PWR](#ae70e92186311daf444e9b2a9c4891dcf)、[CH32V00X_CLOCK_CONFIG](#ab39a50912925831fd0f53da79caa1f3e)。

## 37.2\_详细说明（Detailed Documentation）

<a id="a4ddfcf15d13a740f3917034aa6aee075"></a>

### `CH32V00X_CLOCK_ADC1`

```c
#define CH32V00X_CLOCK_ADC1 CH32V00X_CLOCK_CONFIG(PB2, 9)
```

<a id="adba8b05c326b5c50a5f46a4235347cd2"></a>

### `CH32V00X_CLOCK_AFIO`

```c
#define CH32V00X_CLOCK_AFIO CH32V00X_CLOCK_CONFIG(PB2, 0)
```

<a id="ab39a50912925831fd0f53da79caa1f3e"></a>

### `CH32V00X_CLOCK_CONFIG`

```c
#define CH32V00X_CLOCK_CONFIG ( bus, bit )
```

展开值（Value）：

```c
(((CH32V00X_##bus##_PCENR_OFFSET) << 5) | (bit))
```

<a id="a673a85e0807d525d0d896968e72476d7"></a>

### `CH32V00X_CLOCK_DMA1`

```c
#define CH32V00X_CLOCK_DMA1 CH32V00X_CLOCK_CONFIG(HB, 0)
```

<a id="a44898d60cab2a44b6f11f44dcc910faf"></a>

### `CH32V00X_CLOCK_I2C1`

```c
#define CH32V00X_CLOCK_I2C1 CH32V00X_CLOCK_CONFIG(PB1, 21)
```

<a id="a6937d869f977cb90e519b2b92f98c120"></a>

### `CH32V00X_CLOCK_IOPA`

```c
#define CH32V00X_CLOCK_IOPA CH32V00X_CLOCK_CONFIG(PB2, 2)
```

<a id="a58487531bac2d11010fa719cc9b8bc5b"></a>

### `CH32V00X_CLOCK_IOPB`

```c
#define CH32V00X_CLOCK_IOPB CH32V00X_CLOCK_CONFIG(PB2, 3)
```

<a id="af66030ec198edaa564110cc3b0a6b889"></a>

### `CH32V00X_CLOCK_IOPC`

```c
#define CH32V00X_CLOCK_IOPC CH32V00X_CLOCK_CONFIG(PB2, 4)
```

<a id="aa2c9b9bc83471c7c0701685025ad45b9"></a>

### `CH32V00X_CLOCK_IOPD`

```c
#define CH32V00X_CLOCK_IOPD CH32V00X_CLOCK_CONFIG(PB2, 5)
```

<a id="ae70e92186311daf444e9b2a9c4891dcf"></a>

### `CH32V00X_CLOCK_PWR`

```c
#define CH32V00X_CLOCK_PWR CH32V00X_CLOCK_CONFIG(PB1, 28)
```

<a id="a9ee9b0e633a4a50809c2d2d1d437dd2b"></a>

### `CH32V00X_CLOCK_SPI1`

```c
#define CH32V00X_CLOCK_SPI1 CH32V00X_CLOCK_CONFIG(PB2, 12)
```

<a id="aea9e25b32bec97ba5c4d341a31523586"></a>

### `CH32V00X_CLOCK_SRAM`

```c
#define CH32V00X_CLOCK_SRAM CH32V00X_CLOCK_CONFIG(HB, 2)
```

<a id="a35b5af6bc5e72b9360c923916cd2e0f1"></a>

### `CH32V00X_CLOCK_TIM1`

```c
#define CH32V00X_CLOCK_TIM1 CH32V00X_CLOCK_CONFIG(PB2, 11)
```

<a id="a22cff65ee5b38ca47089ffa0916c8fda"></a>

### `CH32V00X_CLOCK_TIM2`

```c
#define CH32V00X_CLOCK_TIM2 CH32V00X_CLOCK_CONFIG(PB1, 0)
```

<a id="a69c30a9fb4e812dff7c5d2b9834a012b"></a>

### `CH32V00X_CLOCK_TIM3`

```c
#define CH32V00X_CLOCK_TIM3 CH32V00X_CLOCK_CONFIG(PB1, 2)
```

<a id="af46cda54f5d666db759746a11909b148"></a>

### `CH32V00X_CLOCK_USART1`

```c
#define CH32V00X_CLOCK_USART1 CH32V00X_CLOCK_CONFIG(PB2, 14)
```

<a id="a7d61b5360a6d66ee4ca2210f3e1d32f2"></a>

### `CH32V00X_CLOCK_USART2`

```c
#define CH32V00X_CLOCK_USART2 CH32V00X_CLOCK_CONFIG(PB2, 13)
```

<a id="aa1b25307b070e0131c8d2883cc6daac2"></a>

### `CH32V00X_CLOCK_WWDG`

```c
#define CH32V00X_CLOCK_WWDG CH32V00X_CLOCK_CONFIG(PB1, 11)
```

<a id="ae23b04c6f7dc288edd55ca371b0ac6ac"></a>

### `CH32V00X_HB_PCENR_OFFSET`

```c
#define CH32V00X_HB_PCENR_OFFSET 0
```

<a id="a4de5424f7b84a7be9525d3baaf95b372"></a>

### `CH32V00X_PB1_PCENR_OFFSET`

```c
#define CH32V00X_PB1_PCENR_OFFSET 2
```

<a id="ac16a6b94e0d36222243acfe99bd576b1"></a>

### `CH32V00X_PB2_PCENR_OFFSET`

```c
#define CH32V00X_PB2_PCENR_OFFSET 1
```


## 37.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P092_ch32v00x-clocks.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P036_zephyr__dt-bindings__pinctrl__ch32v003-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__dt-bindings__pinctrl__ch32v00x-pinctrl.h_文件参考.md)
