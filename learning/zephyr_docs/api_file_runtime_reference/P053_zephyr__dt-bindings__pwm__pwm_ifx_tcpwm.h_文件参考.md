---
id: learning.zephyr-docs.api-file-runtime-reference.page-53
title: zephyr__dt-bindings__pwm__pwm_ifx_tcpwm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__ifx__tcpwm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_zephyr\_\_dt-bindings\_\_pwm\_\_pwm\_ifx\_tcpwm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwm__ifx__tcpwm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 53.1\_宏定义（Macros）

<a id="r_abf72b3606306b77456891cbf71fa0d32"></a>

```c
#define PWM_IFX_SYSCLK_DIV_8_BIT 0
```

相关声明：[PWM_IFX_SYSCLK_DIV_8_BIT](#abf72b3606306b77456891cbf71fa0d32)。

分频器类型（Divider Type）。

<a id="r_a65ee1c51fd64269a3efa0bcfdab5eb24"></a>

```c
#define PWM_IFX_SYSCLK_DIV_16_BIT 1
```

相关声明：[PWM_IFX_SYSCLK_DIV_16_BIT](#a65ee1c51fd64269a3efa0bcfdab5eb24)。

<a id="r_a5c7bb9eeaf5790a058a2f8eadc36c94f"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_HIGHZ 0
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_HIGHZ](#a5c7bb9eeaf5790a058a2f8eadc36c94f)。

Infineon 定时器／计数器／脉宽调制器（TCPWM）的自定义 PWM 标志（Custom PWM Flags）。这些标志位于 `pwm_flags_t` 的高 8 位，可与 PWM API 配合使用。

<a id="r_a7f3aa15179afd09538c55af9bb4b1ac5"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_RETAIN 1
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_RETAIN](#a7f3aa15179afd09538c55af9bb4b1ac5)。

<a id="r_a6830d6230fb1f47100e2ad05061b7c35"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_LOW 2
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_LOW](#a6830d6230fb1f47100e2ad05061b7c35)。

<a id="r_ae53717df41a15c50365dda4d258decd6"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_HIGH 3
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_HIGH](#ae53717df41a15c50365dda4d258decd6)。

<a id="r_a80e8789dc027ad7220a9f7f94b63663c"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_MASK 0x3
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_MASK](#a80e8789dc027ad7220a9f7f94b63663c)。

<a id="r_ab3fa645ebfd43fa7fe69f69b81117c3d"></a>

```c
#define PWM_IFX_TCPWM_OUTPUT_POS 8 /* Place at the end of flags */
```

相关声明：[PWM_IFX_TCPWM_OUTPUT_POS](#ab3fa645ebfd43fa7fe69f69b81117c3d)、[flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

## 53.2\_详细说明（Detailed Documentation）

<a id="a65ee1c51fd64269a3efa0bcfdab5eb24"></a>

### `PWM_IFX_SYSCLK_DIV_16_BIT`

```c
#define PWM_IFX_SYSCLK_DIV_16_BIT 1
```

<a id="abf72b3606306b77456891cbf71fa0d32"></a>

### `PWM_IFX_SYSCLK_DIV_8_BIT`

```c
#define PWM_IFX_SYSCLK_DIV_8_BIT 0
```

分频器类型（Divider Type）。

<a id="ae53717df41a15c50365dda4d258decd6"></a>

### `PWM_IFX_TCPWM_OUTPUT_HIGH`

```c
#define PWM_IFX_TCPWM_OUTPUT_HIGH 3
```

<a id="a5c7bb9eeaf5790a058a2f8eadc36c94f"></a>

### `PWM_IFX_TCPWM_OUTPUT_HIGHZ`

```c
#define PWM_IFX_TCPWM_OUTPUT_HIGHZ 0
```

Infineon 定时器／计数器／脉宽调制器（TCPWM）的自定义 PWM 标志（Custom PWM Flags）。这些标志位于 `pwm_flags_t` 的高 8 位，可与 PWM API 配合使用。

这些标志允许配置 PWM 被禁用时 PWM 引脚的输出行为（Output Behavior）。

<a id="a6830d6230fb1f47100e2ad05061b7c35"></a>

### `PWM_IFX_TCPWM_OUTPUT_LOW`

```c
#define PWM_IFX_TCPWM_OUTPUT_LOW 2
```

<a id="a80e8789dc027ad7220a9f7f94b63663c"></a>

### `PWM_IFX_TCPWM_OUTPUT_MASK`

```c
#define PWM_IFX_TCPWM_OUTPUT_MASK 0x3
```

<a id="ab3fa645ebfd43fa7fe69f69b81117c3d"></a>

### `PWM_IFX_TCPWM_OUTPUT_POS`

```c
#define PWM_IFX_TCPWM_OUTPUT_POS 8 /* Place at the end of flags */
```

<a id="a7f3aa15179afd09538c55af9bb4b1ac5"></a>

### `PWM_IFX_TCPWM_OUTPUT_RETAIN`

```c
#define PWM_IFX_TCPWM_OUTPUT_RETAIN 1
```


## 53.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P151_pwm_ifx_tcpwm.h_源码浏览.md)
- [pwm_flags_t](../hardware/P255_PWM公共接口.md#gae1dcfb878163da76041efcedf0960fa0)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P052_zephyr__net__ptp_time.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P054_zephyr__dt-bindings__gpio__renesas-rzt2m-gpio.h_文件参考.md)
