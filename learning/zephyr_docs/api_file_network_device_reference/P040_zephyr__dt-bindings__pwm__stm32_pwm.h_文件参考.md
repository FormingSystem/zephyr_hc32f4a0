---
id: learning.zephyr-docs.api-file-network-device-reference.page-40
title: zephyr__dt-bindings__pwm__stm32_pwm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__pwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_dt-bindings\_\_pwm\_\_stm32\_pwm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__pwm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 40.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 输出引脚的自定义 PWM 互补标志（Complementary Flags）

此标志可用于任意 `pwm_pin_set_*` API 调用，表示必须将 PWM 信号路由到互补输出通道（Complementary Output Channel）。

此功能仅在某些片上系统（SoC）系列提供，详情参见对应绑定文档。自定义标志（Custom Flags）位于 `pwm_flags_t` 的高 8 位。

<a id="r_a8e4959803792254f90bb31e0454a4249"></a>

```c
#define STM32_PWM_COMPLEMENTARY (1U << 8)
```

相关声明：[STM32_PWM_COMPLEMENTARY](#a8e4959803792254f90bb31e0454a4249)。

启用 PWM 互补输出引脚（Complementary Output Pin）。

<a id="define-members-1"></a>

### 输入捕获预分频系数的自定义 PWM 标志（Input Capture Prescaler Flags）

这些标志可用于 `pwm_configure_capture` API 调用，设置输入捕获预分频系数（Input Capture Prescaler），即 `TIMx_CCMRx` 中的 `ICxPSC`。

大于 1 的预分频系数（Prescaler）只能与 `PWM_CAPTURE_TYPE_PERIOD` 配合使用。

<a id="r_a203a39b084646374c6c9c5f42683a844"></a>

```c
#define STM32_PWM_CAPTURE_PSC_1 (0U << STM32_PWM_CAPTURE_PSC_POS)
```

相关声明：[STM32_PWM_CAPTURE_PSC_1](#a203a39b084646374c6c9c5f42683a844)。

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 1，默认值。

<a id="r_a8b60760f42b1aa87cb05b1a9c03f7d60"></a>

```c
#define STM32_PWM_CAPTURE_PSC_2 (1U << STM32_PWM_CAPTURE_PSC_POS)
```

相关声明：[STM32_PWM_CAPTURE_PSC_2](#a8b60760f42b1aa87cb05b1a9c03f7d60)。

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 2。

<a id="r_a3b2e7ddce2cc14ba1afea5f125d021ec"></a>

```c
#define STM32_PWM_CAPTURE_PSC_4 (2U << STM32_PWM_CAPTURE_PSC_POS)
```

相关声明：[STM32_PWM_CAPTURE_PSC_4](#a3b2e7ddce2cc14ba1afea5f125d021ec)。

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 4。

<a id="r_a9ba34774103baee8acfc9dd89f62a520"></a>

```c
#define STM32_PWM_CAPTURE_PSC_8 (3U << STM32_PWM_CAPTURE_PSC_POS)
```

相关声明：[STM32_PWM_CAPTURE_PSC_8](#a9ba34774103baee8acfc9dd89f62a520)。

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 8。

## 40.2\_详细说明（Detailed Documentation）

<a id="a203a39b084646374c6c9c5f42683a844"></a>

### `STM32_PWM_CAPTURE_PSC_1`

```c
#define STM32_PWM_CAPTURE_PSC_1 (0U << STM32_PWM_CAPTURE_PSC_POS)
```

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 1，默认值。

<a id="a8b60760f42b1aa87cb05b1a9c03f7d60"></a>

### `STM32_PWM_CAPTURE_PSC_2`

```c
#define STM32_PWM_CAPTURE_PSC_2 (1U << STM32_PWM_CAPTURE_PSC_POS)
```

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 2。

<a id="a3b2e7ddce2cc14ba1afea5f125d021ec"></a>

### `STM32_PWM_CAPTURE_PSC_4`

```c
#define STM32_PWM_CAPTURE_PSC_4 (2U << STM32_PWM_CAPTURE_PSC_POS)
```

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 4。

<a id="a9ba34774103baee8acfc9dd89f62a520"></a>

### `STM32_PWM_CAPTURE_PSC_8`

```c
#define STM32_PWM_CAPTURE_PSC_8 (3U << STM32_PWM_CAPTURE_PSC_POS)
```

PWM 输入捕获预分频系数（Input Capture Prescaler）设为 8。

<a id="a8e4959803792254f90bb31e0454a4249"></a>

### `STM32_PWM_COMPLEMENTARY`

```c
#define STM32_PWM_COMPLEMENTARY (1U << 8)
```

启用 PWM 互补输出引脚（Complementary Output Pin）。


## 40.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P833_stm32_pwm.h_源码浏览.md)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [pwm_configure_capture](../hardware/P255_PWM公共接口.md#ga9603146d7f9c2690c1e1983113d6c6bb)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P039_zephyr__dt-bindings__dma__stm32_dma.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__drivers__sensor__tcs34725.h_文件参考.md)
