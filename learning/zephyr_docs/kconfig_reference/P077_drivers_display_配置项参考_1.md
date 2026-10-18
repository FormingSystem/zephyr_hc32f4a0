---
id: learning.zephyr-docs.kconfig-reference.page-77
title: "`drivers/display`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第77章\_`drivers/display`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/display` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AC057TC1"></a>

## 77.1 `CONFIG_AC057TC1`

**提示（Prompt）**：AC057TC1 显示控制器（Display controller）

**说明（Help）**

启用 AC057TC1 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EINK_AC057TC1_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_DISPLAY_COLOR_PALETTE
CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED
```

**定义位置（Location）**：[`drivers/display/Kconfig.ac057tc1:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ac057tc1#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)、[`CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED)。

<a id="CONFIG_ADV7535"></a>

## 77.2 `CONFIG_ADV7535`

**提示（Prompt）**：Analog Devices ADV7535 DSI 转 HDMI 桥接器（Bridge）

**说明（Help）**

将 ADV7535 初始化为 RGB888 视频模式（Video Mode），并连接到 MIPI DSI 主机（Host）。不支持运行时模式选择和 HDMI 服务。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_ADV7535_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.adv7535:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.adv7535#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_ADV7535_INIT_PRIORITY"></a>

## 77.3 `CONFIG_ADV7535_INIT_PRIORITY`

**提示（Prompt）**：ADV7535 初始化优先级（Initialization Priority）

**说明（Help）**

初始化顺序必须晚于 MIPI DSI 主机（Host）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ADV7535 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`drivers/display/Kconfig.adv7535:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.adv7535#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → Analog Devices ADV7535 DSI 转 HDMI 桥接器（Bridge）

**配置项引用（Symbol References）**：[`CONFIG_ADV7535`](P077_drivers_display_配置项参考_1.md#CONFIG_ADV7535)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_CO5300"></a>

## 77.4 `CONFIG_CO5300`

**提示（Prompt）**：CO5300 显示驱动（Display Driver）

**说明（Help）**

启用 CO5300 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CHIPONE_CO5300_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI if n
CONFIG_MSPI if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.co5300:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.co5300#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_MSPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_DISPLAY"></a>

## 77.5 `CONFIG_DISPLAY`

**提示（Prompt）**：显示控制器驱动（Display Controller Drivers）

**说明（Help）**

启用显示驱动（Display Drivers）

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/display/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX"></a>

## 77.6 `CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX`

**提示（Prompt）**：查理复用 LED 矩阵显示驱动（Charlieplexed LED Matrix Display Driver）

**说明（Help）**

启用由查理复用（Charlieplexing）GPIO 驱动的单色/灰度 LED 矩阵显示驱动。N 条 GPIO 线路最多可驱动 `N*(N-1)` 个 LED；点亮每个像素时，将一条线路驱动为高电平、另一条驱动为低电平，其余线路保持高阻态（High Impedance）。定时器（计数器设备）的中断服务程序（ISR）以足够快的速度扫描像素，利用视觉暂留（Persistence of Vision）形成图像。GPIO 组（Bank）、像素到引脚对的映射、刷新频率和灰度深度，通过兼容标识为 `charlieplex-led-matrix` 的设备树（Devicetree）节点配置。此驱动提供显示 API（Display API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CHARLIEPLEX_LED_MATRIX_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_GPIO
CONFIG_COUNTER
```

**定义位置（Location）**：[`drivers/display/Kconfig.charlieplex_led_matrix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.charlieplex_led_matrix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX_INIT_PRIORITY"></a>

## 77.7 `CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX_INIT_PRIORITY`

**提示（Prompt）**：查理复用 LED 矩阵初始化优先级（Init Priority）

**说明（Help）**

设备初始化优先级（Initialization Priority）。数值必须大于 GPIO 和 COUNTER 的初始化优先级，以便这些设备先就绪。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.charlieplex_led_matrix:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.charlieplex_led_matrix#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 查理复用 LED 矩阵显示驱动（Charlieplexed LED Matrix Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_CHARLIEPLEX_LED_MATRIX)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_INIT_PRIORITY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_COLOR_DITHER"></a>

## 77.8 `CONFIG_DISPLAY_COLOR_DITHER`

**提示（Prompt）**：颜色抖动（Color dithering）

**说明（Help）**

启用一个辅助库（Helper Library）：采用调色板（Palette）的显示驱动集成该库后，可以自动接受 RGB565 和/或 RGB888 写入，并通过抖色（Dithering）转换为面板原生的 `I_4` 调色板格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_PALETTE && CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)、[`CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM"></a>

## 77.9 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`

**提示（Prompt）**：抖色算法（Dithering Algorithm）

**说明（Help）**

将非 `I_4` 写入转换为面板的 `I_4` 调色板格式时使用的算法。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON
```

**可选项（Choices）**

```text
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_NONE
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_4X4
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_8X8
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG
CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON)、[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_NONE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_NONE)、[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_4X4`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_4X4)、[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_8X8`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_8X8)、[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON"></a>

## 77.10 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ATKINSON`

**提示（Prompt）**：Atkinson 抖色算法（Atkinson）

**说明（Help）**

源自早期 Macintosh 图像处理栈的一种误差扩散（Error Diffusion）变体。适用于单色或少色调色板，例如电子纸（E-Paper）和复古用户界面（Retro UI）。额外使用三个按行存放带符号误差的缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 抖色算法（Dithering Algorithm）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG"></a>

## 77.11 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_FLOYD_STEINBERG`

**提示（Prompt）**：Floyd–Steinberg 抖色算法（Floyd-Steinberg）

**说明（Help）**

在相邻像素之间扩散量化误差（Quantization Error）。通常较慢，并额外使用两个按行存放带符号误差的缓冲区，但对于照片和渐变（Gradient），可获得最佳的平均色调和色相准确度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 抖色算法（Dithering Algorithm）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_NONE"></a>

## 77.12 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_NONE`

**提示（Prompt）**：无抖色（None），仅选择最近调色板颜色（Nearest-Palette）

**说明（Help）**

将每个源像素映射到距离最近的调色板条目（Palette Entry）。这是最快的选项，能够保留文字、图标和采用精确调色板配色的图像中的清晰边缘。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 抖色算法（Dithering Algorithm）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_4X4"></a>

## 77.13 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_4X4`

**提示（Prompt）**：4×4 Bayer 有序抖色（Ordered Bayer 4x4）

**说明（Help）**

适合小型显示屏和简单图形的通用选择。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 抖色算法（Dithering Algorithm）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_8X8"></a>

## 77.14 `CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM_ORDERED_BAYER_8X8`

**提示（Prompt）**：8×8 Bayer 有序抖色（Ordered Bayer 8x8）

**说明（Help）**

与 4×4 有序抖色（Ordered Dithering）相比，渐变更平滑，代价是可见的有序图案更大。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 抖色算法（Dithering Algorithm）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_ALGORITHM)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT"></a>

## 77.15 `CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT`

**提示（Prompt）**：选择使用辅助库的驱动所报告的默认像素格式（Default Pixel Format）

**说明（Help）**

使用此辅助库、基于调色板（Palette）的 `I_4` 驱动，在启动时将此值报告为输入像素格式（Input Pixel Format）。从不调用 `display_set_pixel_format()` 的应用程序将按此格式写入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888 if CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565 if CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4
```

**可选项（Choices）**

```text
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565
CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888)、[`CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888)、[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565)、[`CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565)、[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4"></a>

## 77.16 `CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_I4`

**提示（Prompt）**：I_4 像素格式（I_4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 选择使用辅助库的驱动所报告的默认像素格式（Default Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565"></a>

## 77.17 `CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB565`

**提示（Prompt）**：RGB565 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565 && <choice CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 选择使用辅助库的驱动所报告的默认像素格式（Default Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565)、[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888"></a>

## 77.18 `CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_RGB888`

**提示（Prompt）**：RGB888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888 && <choice CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering） → 选择使用辅助库的驱动所报告的默认像素格式（Default Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888)、[`CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_DEFAULT_FORMAT)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565"></a>

## 77.19 `CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB565`

**提示（Prompt）**：接受 RGB565 输入（Input）

**说明（Help）**

允许基于调色板（Palette）的驱动接受 RGB565 帧，并通过抖色（Dithering）转换为其 `I_4` 调色板格式。每个实例会增加一个转换缓冲区（Conversion Buffer），大小可容纳完整的一帧 `I_4` 数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888"></a>

## 77.20 `CONFIG_DISPLAY_COLOR_DITHER_INPUT_RGB888`

**提示（Prompt）**：接受 RGB888 输入（Input）

**说明（Help）**

允许基于调色板（Palette）的驱动接受 RGB888 帧，并通过抖色（Dithering）转换为其 `I_4` 调色板格式。每个实例会增加一个转换缓冲区（Conversion Buffer），大小可容纳完整的一帧 `I_4` 数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_DITHER && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 颜色抖动（Color dithering）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_DITHER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED"></a>

## 77.21 `CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由集成了颜色抖色辅助模块（Color Dithering Helper）的显示驱动选中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**被选择（Selected by）**

```text
CONFIG_AC057TC1
CONFIG_ED2208_GCA
CONFIG_SDL_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.color_dither:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.color_dither#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_AC057TC1`](P077_drivers_display_配置项参考_1.md#CONFIG_AC057TC1)、[`CONFIG_ED2208_GCA`](P077_drivers_display_配置项参考_1.md#CONFIG_ED2208_GCA)、[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)。

<a id="CONFIG_DISPLAY_COLOR_PALETTE"></a>

## 77.22 `CONFIG_DISPLAY_COLOR_PALETTE`

**提示（Prompt）**：调色板（Color Palette）支持

**说明（Help）**

在显示驱动中启用调色板（Color Palette）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**被选择（Selected by）**

```text
CONFIG_AC057TC1
CONFIG_ED2208_GCA
CONFIG_ST730X_DEFAULT_PALETTED
```

**定义位置（Location）**：[`drivers/display/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_AC057TC1`](P077_drivers_display_配置项参考_1.md#CONFIG_AC057TC1)、[`CONFIG_ED2208_GCA`](P077_drivers_display_配置项参考_1.md#CONFIG_ED2208_GCA)、[`CONFIG_ST730X_DEFAULT_PALETTED`](P078_drivers_display_配置项参考_2.md#CONFIG_ST730X_DEFAULT_PALETTED)。

<a id="CONFIG_DISPLAY_COLOR_PALETTE_MAX_SIZE"></a>

## 77.23 `CONFIG_DISPLAY_COLOR_PALETTE_MAX_SIZE`

**提示（Prompt）**：调色板（Color Palette）最大大小

**说明（Help）**

显示驱动中调色板（Color Palette）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_COLOR_PALETTE && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/display/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 调色板（Color Palette）支持

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_EK79007_INIT_PRIORITY"></a>

## 77.24 `CONFIG_DISPLAY_EK79007_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

EK79007 显示驱动的初始化优先级（Initialization Priority）。面板连接到 MIPI DSI 主机（Host），因此必须在主机和向面板传送数据流的控制器之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EK79007 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_MIPI_DSI_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.ek79007:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ek79007#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → EK79007 显示面板驱动（Display Panel Driver）

**配置项引用（Symbol References）**：[`CONFIG_EK79007`](P077_drivers_display_配置项参考_1.md#CONFIG_EK79007)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_ESP32_DSI"></a>

## 77.25 `CONFIG_DISPLAY_ESP32_DSI`

**提示（Prompt）**：ESP32 MIPI DSI 显示控制器（Display Controller）

**说明（Help）**

启用 ESP32 MIPI DSI 显示控制器（Display Controller）的驱动，它将帧缓冲（Framebuffer）中的数据以流方式传送到视频模式面板（Video Mode Panel）。帧缓冲的大小以兆字节计，因此从外部内存（External Memory）分配。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP_DSI_DISPLAY_ENABLED && CONFIG_SOC_SERIES_ESP32P4 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP_SPIRAM
CONFIG_SHARED_MULTI_HEAP
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.esp32_dsi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.esp32_dsi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)、[`CONFIG_SHARED_MULTI_HEAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHARED_MULTI_HEAP)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_DISPLAY_ESP32_DSI_FB_NUM"></a>

## 77.26 `CONFIG_DISPLAY_ESP32_DSI_FB_NUM`

**提示（Prompt）**：驱动中分配的帧缓冲（Framebuffer）数量

**说明（Help）**

使用两个帧缓冲（Framebuffer）时，驱动可在显示已完成的一帧的同时绘制下一帧，使更新不出现撕裂（Tearing）。设为零时，驱动不分配自身的帧缓冲，适用于调用方自行渲染完整尺寸的帧，并让显示硬件直接扫描输出（Scanout）的情况。部分更新（Partial Update）至少需要一个帧缓冲用于合成。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_ESP32_DSI && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.esp32_dsi:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.esp32_dsi#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ESP32 MIPI DSI 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_ESP32_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_ESP32_DSI)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_ESP32_DSI_INIT_PRIORITY"></a>

## 77.27 `CONFIG_DISPLAY_ESP32_DSI_INIT_PRIORITY`

**提示（Prompt）**：ESP32 MIPI DSI 显示控制器初始化优先级（Init Priority）

**说明（Help）**

控制器的初始化优先级（Initialization Priority）。面板一旦接入，主机就开始扫描输出（Scanout），因此只需确保控制器在面板之前初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_ESP32_DSI && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.esp32_dsi:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.esp32_dsi#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ESP32 MIPI DSI 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_ESP32_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_ESP32_DSI)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_INIT_PRIORITY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_FRAMEBUFFER"></a>

## 77.28 `CONFIG_DISPLAY_FRAMEBUFFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用帧缓冲（Framebuffer）驱动使用的库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**被选择（Selected by）**

```text
CONFIG_INTEL_MULTIBOOTFB_DISPLAY
CONFIG_QEMU_RAMFB_DISPLAY
CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER
```

**定义位置（Location）**：[`drivers/display/Kconfig.framebuffer:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.framebuffer#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_INTEL_MULTIBOOTFB_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_INTEL_MULTIBOOTFB_DISPLAY)、[`CONFIG_QEMU_RAMFB_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_QEMU_RAMFB_DISPLAY)、[`CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER`](P077_drivers_display_配置项参考_1.md#CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER)。

<a id="CONFIG_DISPLAY_HX8379C_INIT_PRIORITY"></a>

## 77.29 `CONFIG_DISPLAY_HX8379C_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

HX8379C 显示驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HX8379C && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_APPLICATION_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.hx8379c:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.hx8379c#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → HX8379C 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_HX8379C`](P077_drivers_display_配置项参考_1.md#CONFIG_HX8379C)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_APPLICATION_INIT_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_APPLICATION_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_INIT_PRIORITY"></a>

## 77.30 `CONFIG_DISPLAY_INIT_PRIORITY`

**提示（Prompt）**：显示设备初始化优先级（Init Priority）

**说明（Help）**

显示设备的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
85
```

**定义位置（Location）**：[`drivers/display/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_MCUX_DCNANO_LCDIF"></a>

## 77.31 `CONFIG_DISPLAY_MCUX_DCNANO_LCDIF`

**提示（Prompt）**：MCUX DCNano LCDIF 驱动

**说明（Help）**

启用 MCUX DCNano LCDIF 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DCNANO_LCDIF_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_dcnano_lcdif:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_dcnano_lcdif#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_MCUX_ELCDIF"></a>

## 77.32 `CONFIG_DISPLAY_MCUX_ELCDIF`

**提示（Prompt）**：MCUX eLCDIF 驱动

**说明（Help）**

启用 MCUX eLCDIF 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_ELCDIF_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DISPLAY_MCUX_LCDIFV2"></a>

## 77.33 `CONFIG_DISPLAY_MCUX_LCDIFV2`

**提示（Prompt）**：MCUX LCDIFV2 驱动

**说明（Help）**

启用 MCUX LCDIFV2 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_LCDIFV2_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_lcdifv2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_lcdifv2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DISPLAY_MCUX_LCDIFV3"></a>

## 77.34 `CONFIG_DISPLAY_MCUX_LCDIFV3`

**提示（Prompt）**：MCUX LCDIFV3 驱动

**说明（Help）**

启用 MCUX LCDIFV3 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_LCDIFV3_ENABLED && CONFIG_CLOCK_CONTROL && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_lcdifv3:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_lcdifv3#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DISPLAY_NRF_LED_MATRIX"></a>

## 77.35 `CONFIG_DISPLAY_NRF_LED_MATRIX`

**提示（Prompt）**：由 GPIO 驱动的 LED 矩阵（LED Matrix）

**说明（Help）**

启用行、列均由 GPIO 驱动的 LED 矩阵（LED Matrix）驱动。驱动允许独立地为每个 LED 设置 256 级亮度之一，其中 `0` 表示完全熄灭。GPIO 到行列的分配及其到像素的映射，通过设备树（Devicetree）中兼容标识为 `nordic,nrf-led-matrix` 的节点属性指定。驱动使用一个 TIMER 实例，并根据设备树设置使用一个 PWM 实例，或一个或多个 GPIOTE 和 PPI 通道。后一种情况下所需的数量取决于所选像素组（Pixel Group）大小，即一行中可同时点亮的 LED 数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_LED_MATRIX_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_GPIOTE
CONFIG_NRFX_GPPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.nrf_led_matrix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.nrf_led_matrix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_NRFX_GPIOTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPIOTE)、[`CONFIG_NRFX_GPPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_GPPI)。

<a id="CONFIG_DISPLAY_NT35510_INIT_PRIORITY"></a>

## 77.36 `CONFIG_DISPLAY_NT35510_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

NT35510 显示驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NT35510 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.nt35510:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.nt35510#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → NT35510 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_NT35510`](P077_drivers_display_配置项参考_1.md#CONFIG_NT35510)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_INIT_PRIORITY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_OTM8009A_INIT_PRIORITY"></a>

## 77.37 `CONFIG_DISPLAY_OTM8009A_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

OTM8009A 显示驱动的初始化优先级（Initialization Priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OTM8009A && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_DISPLAY_INIT_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.otm8009a:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.otm8009a#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → OTM8009A 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_OTM8009A`](P077_drivers_display_配置项参考_1.md#CONFIG_OTM8009A)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_INIT_PRIORITY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_INIT_PRIORITY)。

<a id="CONFIG_DISPLAY_RENESAS_LCDC"></a>

## 77.38 `CONFIG_DISPLAY_RENESAS_LCDC`

**提示（Prompt）**：Smartbond 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 Smartbond 显示控制器（Display Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_SMARTBOND_DISPLAY_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_lcdc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_lcdc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_DISPLAY_RENESAS_LCDC_BUFFER_PSRAM"></a>

## 77.39 `CONFIG_DISPLAY_RENESAS_LCDC_BUFFER_PSRAM`

**提示（Prompt）**：将显示缓冲区（Display Buffer）分配到 PSRAM

**说明（Help）**

将显示缓冲区（Display Buffer）分配到 PSRAM

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_RENESAS_LCDC && CONFIG_DISPLAY
```

**主动选择（Selects）**

```text
CONFIG_MEMC
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_lcdc:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_lcdc#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → Smartbond 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_RENESAS_LCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_RENESAS_LCDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)。

<a id="CONFIG_DISPLAY_SOCIONEXT_DPU"></a>

## 77.40 `CONFIG_DISPLAY_SOCIONEXT_DPU`

**提示（Prompt）**：Socionext DPU 驱动

**说明（Help）**

启用 DPU 驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOCIONEXT_DPU_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.socionext_dpu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.socionext_dpu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DPU_FB_NUM"></a>

## 77.41 `CONFIG_DPU_FB_NUM`

**提示（Prompt）**：驱动中分配的帧缓冲（Framebuffer）数量

**说明（Help）**

在 DPU 驱动中分配的帧缓冲（Framebuffer）数量。支持显示局部更新（Partial Display Update）需要由驱动分配帧缓冲。驱动已经过验证，支持分配 0 至 2 个帧缓冲。如果驱动不分配帧缓冲，而由应用程序实现双帧缓冲（Double Framebuffering），并始终向 `display_write` 传入与所连接面板大小相同的缓冲区，则硬件可能获得最佳性能。

**注意**：不分配帧缓冲时，DPU 在初始化期间会被设为显示一个空缓冲区。这意味着在写入新的帧缓冲之前，显示屏实际呈现的内容相当于系统 RAM 的转储。如果这种行为的安全影响令你担忧，请至少启用一个由驱动分配的帧缓冲。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_SOCIONEXT_DPU && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.socionext_dpu:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.socionext_dpu#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → Socionext DPU 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_SOCIONEXT_DPU`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_SOCIONEXT_DPU)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_DUMMY_DISPLAY"></a>

## 77.42 `CONFIG_DUMMY_DISPLAY`

**提示（Prompt）**：空实现显示驱动（Dummy Display Driver）

**说明（Help）**

启用符合显示驱动 API（Display Driver API）的空实现显示驱动（Dummy Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DUMMY_DC_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.dummy:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.dummy#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ED2208_GCA"></a>

## 77.43 `CONFIG_ED2208_GCA`

**提示（Prompt）**：ED2208-GCA（EL073TF1）显示控制器（Display controller）

**说明（Help）**

启用 ED2208-GCA（EL073TF1）Spectra 6 电子墨水（E-Ink）显示屏的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_EINK_ED2208_GCA_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_DISPLAY_COLOR_PALETTE
CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED
```

**定义位置（Location）**：[`drivers/display/Kconfig.ed2208_gca:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ed2208_gca#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)、[`CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED)。

<a id="CONFIG_EK79007"></a>

## 77.44 `CONFIG_EK79007`

**提示（Prompt）**：EK79007 显示面板驱动（Display Panel Driver）

**说明（Help）**

启用 EK79007 MIPI DSI 显示面板（Display Panel）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FITIPOWER_EK79007_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ek79007:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ek79007#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_GC9X01X"></a>

## 77.45 `CONFIG_GC9X01X`

**提示（Prompt）**：GC9X01X 显示驱动（Display Driver）

**说明（Help）**

启用 GC9X01X 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GALAXYCORE_GC9X01X_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.gc9x01x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.gc9x01x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_HUB12"></a>

## 77.46 `CONFIG_HUB12`

**提示（Prompt）**：HUB12 LED 面板显示控制器（LED Panel Display Controller）

**说明（Help）**

用于 32×16 单色显示屏（Monochrome Display）的 HUB12 LED 面板控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_HUB12_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/display/Kconfig.hub12:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.hub12#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_HX8353E"></a>

## 77.47 `CONFIG_HX8353E`

**提示（Prompt）**：Himax HX8353E 显示驱动（Display Driver）

**说明（Help）**

启用 Himax HX8353E 132RGB×162 点阵 TFT LCD 控制器的驱动。通过 MIPI DBI Type B（Intel 8080）并行总线（Parallel Bus）驱动该控制器。可通过设备树（Devicetree）的 `backlight-gpios` 和 `pwms` 属性，选择支持 GPIO 背光开关（Backlight On/Off）和 PWM 亮度控制（Brightness Control）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HIMAX_HX8353E_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.hx8353e:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.hx8353e#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_HX8379C"></a>

## 77.48 `CONFIG_HX8379C`

**提示（Prompt）**：HX8379C 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 HX8379C 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HIMAX_HX8379C_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.hx8379c:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.hx8379c#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_HX8394"></a>

## 77.49 `CONFIG_HX8394`

**提示（Prompt）**：HX8394 显示驱动（Display Driver）

**说明（Help）**

启用 HX8394 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DSI && DT_HAS_HIMAX_HX8394_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.hx8394:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.hx8394#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ILI9163C"></a>

## 77.50 `CONFIG_ILI9163C`

**提示（Prompt）**：ILI9163C 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9163C 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9163C_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_ILI9XXX
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)。

<a id="CONFIG_ILI9340"></a>

## 77.51 `CONFIG_ILI9340`

**提示（Prompt）**：ILI9340 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9340 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9340_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_ILI9XXX
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)。

<a id="CONFIG_ILI9341"></a>

## 77.52 `CONFIG_ILI9341`

**提示（Prompt）**：ILI9341 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9341 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9341_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_ILI9XXX
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)。

<a id="CONFIG_ILI9342C"></a>

## 77.53 `CONFIG_ILI9342C`

**提示（Prompt）**：ILI9342C 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9342C 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9342C_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_ILI9XXX
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)。

<a id="CONFIG_ILI9488"></a>

## 77.54 `CONFIG_ILI9488`

**提示（Prompt）**：ILI9488 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9488 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9488_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
CONFIG_ILI9XXX
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)。

<a id="CONFIG_ILI9806E_DSI"></a>

## 77.55 `CONFIG_ILI9806E_DSI`

**提示（Prompt）**：ILI9806E_DSI 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9806E_DSI 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9806E_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_ILI98XX_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili98xx_dsi:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili98xx_dsi#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_ILI98XX_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI98XX_DSI)。

<a id="CONFIG_ILI9881C_DSI"></a>

## 77.56 `CONFIG_ILI9881C_DSI`

**提示（Prompt）**：ILI9881C_DSI 显示驱动（Display Driver）

**说明（Help）**

启用 ILI9881C_DSI 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ILITEK_ILI9881C_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_ILI98XX_DSI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili98xx_dsi:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili98xx_dsi#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_ILI98XX_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI98XX_DSI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_ILI98XX_DSI"></a>

## 77.57 `CONFIG_ILI98XX_DSI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所有 ILI9XXX MIPI-DSI 驱动共用的隐藏配置项（Hidden Configuration Entry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**被选择（Selected by）**

```text
CONFIG_ILI9806E_DSI
CONFIG_ILI9881C_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili98xx_dsi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili98xx_dsi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_ILI9806E_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9806E_DSI)、[`CONFIG_ILI9881C_DSI`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9881C_DSI)。

<a id="CONFIG_ILI9XXX"></a>

## 77.58 `CONFIG_ILI9XXX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所有 ILI9XXX 驱动共用的隐藏配置项（Hidden Configuration Entry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**被选择（Selected by）**

```text
CONFIG_ILI9163C
CONFIG_ILI9340
CONFIG_ILI9341
CONFIG_ILI9342C
CONFIG_ILI9488
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_ILI9163C`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9163C)、[`CONFIG_ILI9340`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9340)、[`CONFIG_ILI9341`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9341)、[`CONFIG_ILI9342C`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9342C)、[`CONFIG_ILI9488`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9488)。

<a id="CONFIG_ILI9XXX_READ"></a>

## 77.59 `CONFIG_ILI9XXX_READ`

**提示（Prompt）**：允许在 ILI9XXX 上使用 `display_read` API

**说明（Help）**

为 ILI9XXX 控制器提供 `display_read` API 支持。此 API 需要主动启用（Opt-In），因为它会增加代码开销，并且读取 ILI9XXX 的数据需要进行位移（Bitshift），性能不是很高。此 API 仅支持 RGB565 模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ILI9XXX && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.ili9xxx:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ili9xxx#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ILI9XXX`](P077_drivers_display_配置项参考_1.md#CONFIG_ILI9XXX)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_INTEL_MULTIBOOTFB_DISPLAY"></a>

## 77.60 `CONFIG_INTEL_MULTIBOOTFB_DISPLAY`

**提示（Prompt）**：Intel Multiboot 帧缓冲（Framebuffer）

**说明（Help）**

启用基于 Intel Multiboot 帧缓冲（Framebuffer）的显示驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTIBOOT && CONFIG_MULTIBOOT_INFO && DT_HAS_INTEL_MULTIBOOT_FRAMEBUFFER_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DISPLAY_FRAMEBUFFER
```

**定义位置（Location）**：[`drivers/display/Kconfig.intel_multibootfb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.intel_multibootfb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MULTIBOOT`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT)、[`CONFIG_MULTIBOOT_INFO`](P039_arch_x86_配置项参考.md#CONFIG_MULTIBOOT_INFO)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_FRAMEBUFFER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_FRAMEBUFFER)。

<a id="CONFIG_IST3931"></a>

## 77.61 `CONFIG_IST3931`

**提示（Prompt）**：IST3931 显示驱动（Display Driver）

**说明（Help）**

启用 IST3931 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ISTECH_IST3931_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/display/Kconfig.ist3931:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ist3931#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_IT8951"></a>

## 77.62 `CONFIG_IT8951`

**提示（Prompt）**：ITE IT8951 电子纸显示控制器（E-Paper Display Controller）

**说明（Help）**

启用 SPI/I80 电子纸显示模块所用的 ITE IT8951 时序控制器（Timing Controller）的驱动，包括基于 ED103TC2 的面板。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8951_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.it8951:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.it8951#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_LED_STRIP_MATRIX"></a>

## 77.63 `CONFIG_LED_STRIP_MATRIX`

**提示（Prompt）**：LED 灯带矩阵显示驱动（LED Strip Matrix Display Driver）

**说明（Help）**

启用 LED 灯带矩阵显示驱动，即将 LED 灯带（LED Strip）排列成网格的显示方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LED_STRIP_MATRIX_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LED_STRIP
```

**定义位置（Location）**：[`drivers/display/Kconfig.led_strip_matrix:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.led_strip_matrix#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_LED_STRIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_STRIP)。

<a id="CONFIG_LPM013M126"></a>

## 77.64 `CONFIG_LPM013M126`

**提示（Prompt）**：LPM013M126 存储型显示控制器驱动（Memory Display Controller Driver）

**说明（Help）**

启用 JDI LPM013M126 系列存储型显示器（Memory Display）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_JDI_LPM013M126_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.lpm013m126:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.lpm013m126#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_LS0XX"></a>

## 77.65 `CONFIG_LS0XX`

**提示（Prompt）**：LS0XX 存储型显示控制器驱动（Memory Display Controller Driver）

**说明（Help）**

启用夏普（Sharp）LS0XXX7DXXX 系列存储型显示器（Memory Display）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SHARP_LS0XX_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ls0xx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ls0xx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_LS0XX_VCOM_THREAD_PRIO"></a>

## 77.66 `CONFIG_LS0XX_VCOM_THREAD_PRIO`

**提示（Prompt）**：VCOM 反转线程（VCOM Inversion Thread）的优先级

**说明（Help）**

设置 VCOM 反转线程（VCOM Inversion Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LS0XX && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/display/Kconfig.ls0xx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ls0xx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → LS0XX 存储型显示控制器驱动（Memory Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_LS0XX`](P077_drivers_display_配置项参考_1.md#CONFIG_LS0XX)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_LT7680"></a>

## 77.67 `CONFIG_LT7680`

**提示（Prompt）**：LT7680 显示驱动（Display Driver）

**说明（Help）**

Levetop Ltd. LT7680 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LEVETOP_LT7680_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.lt7680:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.lt7680#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_LT7680_READ_DATA_AS_BURST"></a>

## 77.68 `CONFIG_LT7680_READ_DATA_AS_BURST`

**提示（Prompt）**：以突发方式（Burst）读取数据

**说明（Help）**

启用此选项，以突发方式（Burst）读取数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LT7680 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.lt7680:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.lt7680#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → LT7680 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_LT7680`](P077_drivers_display_配置项参考_1.md#CONFIG_LT7680)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_LT7680_TRANSMIT_DATA_AS_BURST"></a>

## 77.69 `CONFIG_LT7680_TRANSMIT_DATA_AS_BURST`

**提示（Prompt）**：以突发方式（Burst）发送数据，不检查 FIFO

**说明（Help）**

启用此选项，以突发方式（Burst）发送数据，并且不检查 FIFO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LT7680 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.lt7680:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.lt7680#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → LT7680 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_LT7680`](P077_drivers_display_配置项参考_1.md#CONFIG_LT7680)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MAX7219"></a>

## 77.70 `CONFIG_MAX7219`

**提示（Prompt）**：MAX7219 LED 显示驱动（LED Display Driver）

**说明（Help）**

启用 Maxim MAX7219 SPI LED 显示驱动。每个 MAX7219 最多支持 64 个独立 LED。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX7219_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/display/Kconfig.max7219:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.max7219#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_MCUX_DCNANO_LCDIF_FB_NUM"></a>

## 77.71 `CONFIG_MCUX_DCNANO_LCDIF_FB_NUM`

**提示（Prompt）**：驱动中分配的帧缓冲（Framebuffer）数量

**说明（Help）**

在 DCNANO 驱动中分配的帧缓冲（Framebuffer）数量。支持显示局部更新（Partial Display Update）需要由驱动分配帧缓冲。驱动已经过验证，支持分配 0 至 2 个帧缓冲。如果驱动不分配帧缓冲，而由应用程序实现双帧缓冲（Double Framebuffering），并始终向 `display_write` 传入与所连接面板大小相同的缓冲区，则硬件可能获得最佳性能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_DCNANO_LCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_dcnano_lcdif:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_dcnano_lcdif#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX DCNano LCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_DCNANO_LCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_DCNANO_LCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_DCNANO_LCDIF_MAINTAIN_CACHE"></a>

## 77.72 `CONFIG_MCUX_DCNANO_LCDIF_MAINTAIN_CACHE`

**提示（Prompt）**：维护缓存一致性（Cache Coherency）

**说明（Help）**

维护 LCDIF 帧缓冲（Framebuffer）的缓存一致性（Cache Coherency）。通常需要此功能，除非使用了具有自定义缓存设置的外部帧缓冲，或者禁用了缓存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_DCNANO_LCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_dcnano_lcdif:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_dcnano_lcdif#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX DCNano LCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_DCNANO_LCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_DCNANO_LCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_ELCDIF_FB_NUM"></a>

## 77.73 `CONFIG_MCUX_ELCDIF_FB_NUM`

**提示（Prompt）**：驱动中分配的帧缓冲（Framebuffer）数量

**说明（Help）**

在 ELCDIF 驱动中分配的帧缓冲（Framebuffer）数量。支持显示局部更新（Partial Display Update）需要由驱动分配帧缓冲。驱动已经过验证，支持分配 0 至 2 个帧缓冲。如果驱动不分配帧缓冲，而由应用程序实现双帧缓冲（Double Framebuffering），并始终向 `display_write` 传入与所连接面板大小相同的缓冲区，则硬件可能获得最佳性能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_ELCDIF_FB_SIZE"></a>

## 77.74 `CONFIG_MCUX_ELCDIF_FB_SIZE`

**提示（Prompt）**：eLCDIF 驱动所需的帧缓冲大小（Framebuffer Size）

**说明（Help）**

eLCDIF 驱动通过分配帧缓冲（Framebuffer）支持显示局部更新（Partial Display Update）。帧缓冲大小按 `panel_width * panel_height * bpp` 计算。默认值可满足默认分辨率 1280×720 及每像素 4 字节的格式（例如 ARGB8888）。应用程序应根据实际使用的分辨率和格式调整此值，以优化堆大小（Heap Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
3686400
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_ELCDIF_PXP"></a>

## 77.75 `CONFIG_MCUX_ELCDIF_PXP`

**提示（Prompt）**：使用 PXP 进行显示旋转（Display Rotation）

**说明（Help）**

使用 PXP 进行显示旋转（Display Rotation）。这要求 LCDIF 节点具有指向 PXP 设备节点的 `nxp,pxp` 设备树（Devicetree）属性。只有在调用 `display_write` 时传入与显示屏大小相同的帧缓冲（Framebuffer），ELCDIF 才会使用 PXP 旋转帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_PXP && CONFIG_MCUX_ELCDIF_FB_NUM > 0 && CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_MCUX_PXP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_PXP)、[`CONFIG_MCUX_ELCDIF_FB_NUM`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_FB_NUM)、[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_ELCDIF_PXP_FLIP_BOTH"></a>

## 77.76 `CONFIG_MCUX_ELCDIF_PXP_FLIP_BOTH`

**提示（Prompt）**：同时水平和垂直翻转显示（Flip Horizontally and Vertically）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 翻转方向（Flip Direction）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION"></a>

## 77.77 `CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`

**提示（Prompt）**：PXP 翻转方向（Flip Direction）

**说明（Help）**

设置 PXP 的翻转方向（Flip Direction）。ELCDIF 无法根据 `display_write` 调用确定正确的旋转角度，因此用户应在此配置。要使 PXP 翻转功能生效，调用 `display_write` 时**必须**提供宽、高与屏幕在未应用翻转时相同的帧缓冲（Framebuffer）。使用此功能时，不应更改设备树（Devicetree）中屏幕在默认朝向下的宽度和高度设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_ELCDIF_PXP && CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE
```

**可选项（Choices）**

```text
CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE
CONFIG_MCUX_ELCDIF_PXP_FLIP_HORIZONTAL
CONFIG_MCUX_ELCDIF_PXP_FLIP_VERTICAL
CONFIG_MCUX_ELCDIF_PXP_FLIP_BOTH
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP)、[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE)、[`CONFIG_MCUX_ELCDIF_PXP_FLIP_HORIZONTAL`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_HORIZONTAL)、[`CONFIG_MCUX_ELCDIF_PXP_FLIP_VERTICAL`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_VERTICAL)、[`CONFIG_MCUX_ELCDIF_PXP_FLIP_BOTH`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_BOTH)。

<a id="CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE"></a>

## 77.78 `CONFIG_MCUX_ELCDIF_PXP_FLIP_DISABLE`

**提示（Prompt）**：不翻转显示（Do Not Flip）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 翻转方向（Flip Direction）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_FLIP_HORIZONTAL"></a>

## 77.79 `CONFIG_MCUX_ELCDIF_PXP_FLIP_HORIZONTAL`

**提示（Prompt）**：水平翻转显示（Flip Horizontally）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 翻转方向（Flip Direction）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_FLIP_VERTICAL"></a>

## 77.80 `CONFIG_MCUX_ELCDIF_PXP_FLIP_VERTICAL`

**提示（Prompt）**：垂直翻转显示（Flip Vertically）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 翻转方向（Flip Direction）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_FLIP_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_ROTATE_0"></a>

## 77.81 `CONFIG_MCUX_ELCDIF_PXP_ROTATE_0`

**提示（Prompt）**：将显示旋转 0 度（Rotate by 0 Degrees）

**说明（Help）**

将显示旋转 0 度。此选项主要用于测试；用于生产的应用程序应直接禁用 PXP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 旋转角度（Rotation Angle）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_ROTATE_180"></a>

## 77.82 `CONFIG_MCUX_ELCDIF_PXP_ROTATE_180`

**提示（Prompt）**：将显示旋转 180 度（Rotate by 180 Degrees）

**说明（Help）**

将显示逆时针旋转（Rotate Counter-Clockwise）180 度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 旋转角度（Rotation Angle）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_ROTATE_270"></a>

## 77.83 `CONFIG_MCUX_ELCDIF_PXP_ROTATE_270`

**提示（Prompt）**：将显示旋转 270 度（Rotate by 270 Degrees）

**说明（Help）**

将显示逆时针旋转（Rotate Counter-Clockwise）270 度。对于 LVGL，这对应旋转 90 度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 旋转角度（Rotation Angle）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_ROTATE_90"></a>

## 77.84 `CONFIG_MCUX_ELCDIF_PXP_ROTATE_90`

**提示（Prompt）**：将显示旋转 90 度（Rotate by 90 Degrees）

**说明（Help）**

将显示逆时针旋转（Rotate Counter-Clockwise）90 度。对于 LVGL，这对应旋转 270 度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION>
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation） → PXP 旋转角度（Rotation Angle）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION)。

<a id="CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION"></a>

## 77.85 `CONFIG_MCUX_ELCDIF_PXP_ROTATE_DIRECTION`

**提示（Prompt）**：PXP 旋转角度（Rotation Angle）

**说明（Help）**

设置 PXP 的旋转角度（Rotation Angle）。ELCDIF 无法根据 `display_write` 调用确定正确的旋转角度，因此用户应在此配置。要使 PXP 旋转功能生效，调用 `display_write` 时**必须**提供宽、高与屏幕在未应用旋转时相同的帧缓冲（Framebuffer）。使用此功能时，不应更改设备树（Devicetree）中屏幕在默认朝向下的宽度和高度设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_ELCDIF_PXP && CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_MCUX_ELCDIF_PXP_ROTATE_0
```

**可选项（Choices）**

```text
CONFIG_MCUX_ELCDIF_PXP_ROTATE_0
CONFIG_MCUX_ELCDIF_PXP_ROTATE_90
CONFIG_MCUX_ELCDIF_PXP_ROTATE_180
CONFIG_MCUX_ELCDIF_PXP_ROTATE_270
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动 → 使用 PXP 进行显示旋转（Display Rotation）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_ELCDIF_PXP`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP)、[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_0`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_0)、[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_90`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_90)、[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_180`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_180)、[`CONFIG_MCUX_ELCDIF_PXP_ROTATE_270`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_PXP_ROTATE_270)。

<a id="CONFIG_MCUX_ELCDIF_START_ON_INIT"></a>

## 77.86 `CONFIG_MCUX_ELCDIF_START_ON_INIT`

**提示（Prompt）**：在初始化期间启动 ELCDIF 显示驱动（Display Driver）

**说明（Help）**

可选择在初始化步骤中启动 ELCDIF 显示驱动；某些连接的显示控制器（Display Controller）可能需要这样做才能正常工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_ELCDIF && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y if CONFIG_MCUX_ELCDIF_FB_NUM != 0
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_elcdif:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_elcdif#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX eLCDIF 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MCUX_ELCDIF_FB_NUM`](P077_drivers_display_配置项参考_1.md#CONFIG_MCUX_ELCDIF_FB_NUM)。

<a id="CONFIG_MCUX_LCDIFV2_FB_NUM"></a>

## 77.87 `CONFIG_MCUX_LCDIFV2_FB_NUM`

**提示（Prompt）**：驱动中分配的帧缓冲（Framebuffer）数量

**说明（Help）**

在 LCDIFV2 驱动中分配的帧缓冲（Framebuffer）数量。支持显示局部更新（Partial Display Update）需要由驱动分配帧缓冲。驱动已经过验证，支持分配 0 至 2 个帧缓冲。如果驱动不分配帧缓冲，而由应用程序实现双帧缓冲（Double Framebuffering），并始终向 `display_write` 传入与所连接面板大小相同的缓冲区，则硬件可能获得最佳性能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_LCDIFV2 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_lcdifv2:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_lcdifv2#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX LCDIFV2 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_LCDIFV2`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_LCDIFV2)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_LCDIFV2_FB_SIZE"></a>

## 77.88 `CONFIG_MCUX_LCDIFV2_FB_SIZE`

**提示（Prompt）**：LCDIFV2 驱动所需的帧缓冲大小（Framebuffer Size）

**说明（Help）**

LCDIFV2 驱动通过分配帧缓冲（Framebuffer）支持显示局部更新（Partial Display Update）。帧缓冲大小按 `panel_width * panel_height * bpp` 计算。默认值可满足默认分辨率 1280×720 及每像素 4 字节的格式（例如 ARGB8888）。应用程序应根据实际使用的分辨率和格式调整此值，以优化堆大小（Heap Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_LCDIFV2 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
3686400
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_lcdifv2:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_lcdifv2#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX LCDIFV2 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_LCDIFV2`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_LCDIFV2)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MCUX_LCDIFV3_FB_NUM"></a>

## 77.89 `CONFIG_MCUX_LCDIFV3_FB_NUM`

**提示（Prompt）**：驱动中要分配的帧缓冲（Framebuffer）数量

**说明（Help）**

LCDIFV3 驱动中要分配的帧缓冲（Framebuffer）数量。驱动分配帧缓冲以支持显示局部更新（Partial Display Update）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY_MCUX_LCDIFV3 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.mcux_lcdifv3:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.mcux_lcdifv3#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → MCUX LCDIFV3 驱动

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_MCUX_LCDIFV3`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_LCDIFV3)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_MICROBIT_DISPLAY"></a>

## 77.90 `CONFIG_MICROBIT_DISPLAY`

**提示（Prompt）**：BBC micro:bit 5×5 LED 显示支持（LED Display Support）

**说明（Help）**

启用此项，即可在 BBC micro:bit 的 5×5 LED 矩阵显示屏（LED Matrix Display）上显示图像和文本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BOARD_BBC_MICROBIT || CONFIG_BOARD_BBC_MICROBIT_V2) && CONFIG_PRINTK && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.microbit:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.microbit#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_BBC_MICROBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BBC_MICROBIT)、[`CONFIG_BOARD_BBC_MICROBIT_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_BBC_MICROBIT_V2)、[`CONFIG_PRINTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PRINTK)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_BBC_MICROBIT`、`CONFIG_BOARD_BBC_MICROBIT_V2`。

<a id="CONFIG_MICROBIT_DISPLAY_STR_MAX"></a>

## 77.91 `CONFIG_MICROBIT_DISPLAY_STR_MAX`

**提示（Prompt）**：可在显示屏上显示的字符串最大长度（Maximum String Length）

**说明（Help）**

此值指定通过 `mb_display_string()` 和 `mb_display_print()` API 显示的字符串最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MICROBIT_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[3, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.microbit:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.microbit#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → BBC micro:bit 5×5 LED 显示支持（LED Display Support）

**配置项引用（Symbol References）**：[`CONFIG_MICROBIT_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_MICROBIT_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_NT35510"></a>

## 77.92 `CONFIG_NT35510`

**提示（Prompt）**：NT35510 显示驱动（Display Driver）

**说明（Help）**

启用 NT35510 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_FRIDA_NT35510_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.nt35510:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.nt35510#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_OTM8009A"></a>

## 77.93 `CONFIG_OTM8009A`

**提示（Prompt）**：OTM8009A 显示驱动（Display Driver）

**说明（Help）**

启用 OTM8009A 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ORISETECH_OTM8009A_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.otm8009a:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.otm8009a#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_PCD8544"></a>

## 77.94 `CONFIG_PCD8544`

**提示（Prompt）**：PCD8544 LCD 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 PCD8544 显示控制器驱动（Display Controller Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_PHILIPS_PCD8544_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.pcd8544:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.pcd8544#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_QEMU_RAMFB_DISPLAY"></a>

## 77.95 `CONFIG_QEMU_RAMFB_DISPLAY`

**提示（Prompt）**：QEMU RAM 帧缓冲（ramfb）

**说明（Help）**

启用基于 QEMU ramfb 帧缓冲（Framebuffer）的显示驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_QEMU_RAMFB_ENABLED && (DT_HAS_QEMU_FW_CFG_MMIO_ENABLED || DT_HAS_QEMU_FW_CFG_IOPORT_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_QEMU_FWCFG
CONFIG_DISPLAY_FRAMEBUFFER
```

**定义位置（Location）**：[`drivers/display/Kconfig.qemu_ramfb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.qemu_ramfb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_QEMU_FWCFG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QEMU_FWCFG)、[`CONFIG_DISPLAY_FRAMEBUFFER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_FRAMEBUFFER)。

<a id="CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER"></a>

## 77.96 `CONFIG_RASPBERRYPI_BCM2711_FRAMEBUFFER`

**提示（Prompt）**：树莓派（Raspberry Pi）BCM2711 帧缓冲（Framebuffer）

**说明（Help）**

启用树莓派（Raspberry Pi）BCM2711 帧缓冲显示驱动（Framebuffer Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RASPBERRYPI_BCM2711_FRAMEBUFFER_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RASPBERRYPI_FIRMWARE
CONFIG_DISPLAY_FRAMEBUFFER
```

**定义位置（Location）**：[`drivers/display/Kconfig.rpi_bcm2711_fb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.rpi_bcm2711_fb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_RASPBERRYPI_FIRMWARE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RASPBERRYPI_FIRMWARE)、[`CONFIG_DISPLAY_FRAMEBUFFER`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_FRAMEBUFFER)。

<a id="CONFIG_RENESAS_RA_GLCDC"></a>

## 77.97 `CONFIG_RENESAS_RA_GLCDC`

**提示（Prompt）**：瑞萨（Renesas）显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用瑞萨（Renesas）显示控制器（Display Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_GLCDC_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_ra:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_ra#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_USE_RA_FSP_DISPLAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_DISPLAY)。

<a id="CONFIG_RENESAS_RA_GLCDC_FB_NUM"></a>

## 77.98 `CONFIG_RENESAS_RA_GLCDC_FB_NUM`

**提示（Prompt）**：帧缓冲（Frame Buffer）数量

**说明（Help）**

瑞萨（RENESAS）RA GLCDC 帧缓冲（Frame Buffer）数量配置：

- `0`：由应用程序维护帧缓冲，写入时必须提供全屏像素。
- `1`：在 RENESAS RA GLCDC 驱动中使用单帧缓冲（Single Frame Buffer）。
- `2`：在 RENESAS RA GLCDC 驱动中使用双帧缓冲（Double Frame Buffer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_RA_GLCDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_ra:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_ra#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 瑞萨（Renesas）显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RA_GLCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RA_GLCDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_RENESAS_RA_GLCDC_FRAME_BUFFER_SECTION"></a>

## 77.99 `CONFIG_RENESAS_RA_GLCDC_FRAME_BUFFER_SECTION`

**提示（Prompt）**：放置帧缓冲（Frame Buffer）的 RAM 内存段（Memory Section）

**说明（Help）**

用于放置帧缓冲（Frame Buffer）的 RAM 内存段（Memory Section）名称。例如，将显示帧缓冲放入外部 SDRAM 的 `.sdram` 段：

```kconfig
  CONFIG_RENESAS_RA_GLCDC_FRAME_BUFFER_SECTION=".sdram"
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_RA_GLCDC_FB_NUM > 0 && CONFIG_RENESAS_RA_GLCDC && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_ra:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_ra#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 瑞萨（Renesas）显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RA_GLCDC_FB_NUM`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RA_GLCDC_FB_NUM)、[`CONFIG_RENESAS_RA_GLCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RA_GLCDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_RENESAS_RZ_LCDC"></a>

## 77.100 `CONFIG_RENESAS_RZ_LCDC`

**提示（Prompt）**：瑞萨（Renesas）显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用瑞萨（Renesas）显示控制器（Display Controller）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_LCDC_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_DISPLAY
CONFIG_NOCACHE_MEMORY if CONFIG_DCACHE
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_rz:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_rz#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_USE_RZ_FSP_DISPLAY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_DISPLAY)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<!-- kconfig-navigation -->

[上一章](P076_drivers_disk_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P078_drivers_display_配置项参考_2.md)
