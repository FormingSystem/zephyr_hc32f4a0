---
id: learning.zephyr-docs.api-file-system-power-reference.page-11
title: zephyr__dt-bindings__gpio__espressif-esp32-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_dt-bindings\_\_gpio\_\_espressif-esp32-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/espressif-esp32-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 驱动强度标志（drive strength flags）

驱动强度标志（drive strength flags）是 Zephyr 对 Linux GPIO 绑定所规定标准 GPIO 标志的专用扩展。

仅适用于 Espressif ESP32 SoC。

此接口支持两种驱动强度（Drive Strengths）：`DFLT` 为硬件支持的最高驱动强度，`ALT` 为硬件支持的最低驱动强度。

<a id="r_adbe5a19bf5ce3d57e5e8fe592022cefb"></a>

```c
#define ESP32_GPIO_DS_DFLT (0x0U << ESP32_GPIO_DS_POS)
```

相关声明：[ESP32_GPIO_DS_DFLT](#adbe5a19bf5ce3d57e5e8fe592022cefb)。

默认驱动强度（default drive strength）。

<a id="r_a20175204db3e520b54ceeafb5029db0c"></a>

```c
#define ESP32_GPIO_DS_ALT (0x3U << ESP32_GPIO_DS_POS)
```

相关声明：[ESP32_GPIO_DS_ALT](#a20175204db3e520b54ceeafb5029db0c)。

替代驱动强度（alternative drive strength）。

<a id="define-members-1"></a>

### GPIO 引脚输入／输出使能标志（Pin Input/Output Enable Flags）

这些标志（Flags）允许将引脚配置为输入或输出，同时保持另一方向的配置不变。

例如，将 GPIO 引脚配置为输入（Input）并传入 `ESP32_GPIO_PIN_OUT_EN` 标志时，驱动不会禁用该引脚的输出缓冲器（Output Buffer）。此功能可让引脚同时作为输入和输出，用于诊断或测试。

<a id="r_a20dcf1a1a0dc4f18fb688a004151556d"></a>

```c
#define ESP32_GPIO_PIN_OUT_EN (1 << 12)
```

相关声明：[ESP32_GPIO_PIN_OUT_EN](#a20dcf1a1a0dc4f18fb688a004151556d)。

保持 GPIO 引脚的输出（Output）使能状态。

<a id="r_ab87f6a0268cf84c10689cff6f0a6af02"></a>

```c
#define ESP32_GPIO_PIN_IN_EN (1 << 13)
```

相关声明：[ESP32_GPIO_PIN_IN_EN](#ab87f6a0268cf84c10689cff6f0a6af02)。

保持 GPIO 引脚的输入（Input）使能状态。

<a id="define-members-2"></a>

### GPIO 休眠保持标志（Sleep Hold Flag）

为引脚启用系统休眠（System Sleep）期间的 ESP GPIO 焊盘保持功能（Pad Hold Feature）。

启用后，引脚状态在系统进入低功耗模式（Low Power Mode）之前被锁存（Latched），并在系统休眠期间保持不变。这确保即使控制该引脚的外设断电或寄存器状态丢失，GPIO 电平也得以保持。

此功能同时适用于输入模式和输出模式（Input and Output Modes），但仅适用于具备输出能力的 GPIO。

**注意（Note）：**对于深度休眠周期（Deep Sleep Cycles），自动保持功能可能无法覆盖从进入休眠到应用恢复执行的整个时段。深度休眠过程中，复位会导致寄存器状态丢失，保持配置（Hold Configuration）将在驱动初始化阶段释放。若输出必须保持稳定电平，例如对边沿敏感的信号，应用可能需要在请求断电（Power-off）之前使用 `gpio_hold_en()` 显式启用保持功能，以确保引脚状态在整个深度休眠期间持续保持，直到应用再次运行。

<a id="r_aa4a4e26c24fe27a49fdeb2714b2f849a"></a>

```c
#define ESP32_GPIO_SLEEP_HOLD_EN (1 << 14)
```

相关声明：[ESP32_GPIO_SLEEP_HOLD_EN](#aa4a4e26c24fe27a49fdeb2714b2f849a)。

启用休眠期间的 GPIO 状态保持（State Hold）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a20175204db3e520b54ceeafb5029db0c"></a>

### `ESP32_GPIO_DS_ALT`

```c
#define ESP32_GPIO_DS_ALT (0x3U << ESP32_GPIO_DS_POS)
```

替代驱动强度（alternative drive strength）。

<a id="adbe5a19bf5ce3d57e5e8fe592022cefb"></a>

### `ESP32_GPIO_DS_DFLT`

```c
#define ESP32_GPIO_DS_DFLT (0x0U << ESP32_GPIO_DS_POS)
```

默认驱动强度（default drive strength）。

<a id="ab87f6a0268cf84c10689cff6f0a6af02"></a>

### `ESP32_GPIO_PIN_IN_EN`

```c
#define ESP32_GPIO_PIN_IN_EN (1 << 13)
```

保持 GPIO 引脚的输入（Input）使能状态。

<a id="a20dcf1a1a0dc4f18fb688a004151556d"></a>

### `ESP32_GPIO_PIN_OUT_EN`

```c
#define ESP32_GPIO_PIN_OUT_EN (1 << 12)
```

保持 GPIO 引脚的输出（Output）使能状态。

<a id="aa4a4e26c24fe27a49fdeb2714b2f849a"></a>

### `ESP32_GPIO_SLEEP_HOLD_EN`

```c
#define ESP32_GPIO_SLEEP_HOLD_EN (1 << 14)
```

启用休眠期间的 GPIO 状态保持（State Hold）。


## 11.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P243_espressif-esp32-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_zephyr__dt-bindings__sensor__lis2dh.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__dt-bindings__pinctrl__gecko-pinctrl.h_文件参考.md)
