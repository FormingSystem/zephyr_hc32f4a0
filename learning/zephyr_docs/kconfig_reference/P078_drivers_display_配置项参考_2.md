---
id: learning.zephyr-docs.kconfig-reference.page-78
title: "`drivers/display`配置项参考（2/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第78章\_`drivers/display`配置项参考（2/2）

本章翻译官方 Kconfig 数据库中 `drivers/display` 的 77 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_RENESAS_RZ_LCDC_FB_NUM"></a>

## 78.1 `CONFIG_RENESAS_RZ_LCDC_FB_NUM`

**提示（Prompt）**：帧缓冲（Frame Buffer）数量

**说明（Help）**

瑞萨（RENESAS）RZ LCDC 帧缓冲（Frame Buffer）数量配置：

- `0`：由应用程序维护帧缓冲，写入时必须提供全屏像素。
- `1`：在 RENESAS RZ LCDC 驱动中使用单帧缓冲（Single Frame Buffer）。
- `2`：在 RENESAS RZ LCDC 驱动中使用双帧缓冲（Double Frame Buffer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RENESAS_RZ_LCDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.renesas_rz:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.renesas_rz#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 瑞萨（Renesas）显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_RENESAS_RZ_LCDC`](P077_drivers_display_配置项参考_1.md#CONFIG_RENESAS_RZ_LCDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_RM67162"></a>

## 78.2 `CONFIG_RM67162`

**提示（Prompt）**：RM67162 显示驱动（Display Driver）

**说明（Help）**

启用 RM67162 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RAYDIUM_RM67162_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.rm67162:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.rm67162#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_RM67199"></a>

## 78.3 `CONFIG_RM67199`

**提示（Prompt）**：RM67199 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 RM67199 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RAYDIUM_RM67199_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.rm67199:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.rm67199#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_RM68200"></a>

## 78.4 `CONFIG_RM68200`

**提示（Prompt）**：RM68200 显示驱动（Display Driver）

**说明（Help）**

启用 RM68200 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MIPI_DSI && DT_HAS_RAYDIUM_RM68200_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.rm68200:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.rm68200#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_RM692C9"></a>

## 78.5 `CONFIG_RM692C9`

**提示（Prompt）**：RM692C9 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 RM692C9 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RAYDIUM_RM692C9_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.rm692c9:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.rm692c9#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_SDL_DISPLAY"></a>

## 78.6 `CONFIG_SDL_DISPLAY`

**提示（Prompt）**：基于 SDL 的仿真显示（Emulated Display）

**说明（Help）**

启用基于 SDL、符合显示驱动 API（Display Driver API）的仿真显示（Emulated Display）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_SDL_DC_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
HAS_SDL
CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_DITHER_SUPPORTED)。

<a id="CONFIG_SDL_DISPLAY_COLOR_TINT"></a>

## 78.7 `CONFIG_SDL_DISPLAY_COLOR_TINT`

**提示（Prompt）**：叠加在显示数据上的颜色滤镜（Color Filter）

**说明（Help）**

可用于模拟带颜色的单色显示屏（Colored Monochrome Display），例如 R8（L8 加上 `0xff0000` 色调）。字节顺序（Byte Order）为 `RGB_888`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
0xffffff
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_MONO_MSB_FIRST"></a>

## 78.8 `CONFIG_SDL_DISPLAY_MONO_MSB_FIRST`

**提示（Prompt）**：将单色格式（Monochrome Format）的位顺序设为最高有效位优先（MSB First）

**说明（Help）**

选择此项时，最高有效位（Most Significant Bit，MSB）表示第一个像素。此设置适用于 `MONO01` / `MONO10` 像素格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_MONO_VTILED"></a>

## 78.9 `CONFIG_SDL_DISPLAY_MONO_VTILED`

**提示（Prompt）**：配置数据八位组（Data Octet）的表示方式

**说明（Help）**

选择此项时，一个数据八位组（Data Octet）表示沿垂直方向排列的 8 个像素；否则表示沿水平方向排列的 8 个像素。此设置适用于 `MONO01` / `MONO10` 像素格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_ROUNDED_MASK"></a>

## 78.10 `CONFIG_SDL_DISPLAY_ROUNDED_MASK`

**提示（Prompt）**：使用圆形遮罩（Rounded Mask）

**说明（Help）**

启用后，对显示输出应用圆形遮罩（Rounded Mask）。可用于模拟圆形显示屏（Rounded Display）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_ROUNDED_MASK_COLOR"></a>

## 78.11 `CONFIG_SDL_DISPLAY_ROUNDED_MASK_COLOR`

**提示（Prompt）**：圆形遮罩颜色（Rounded Mask Color）

**说明（Help）**

圆形遮罩（Rounded Mask）的颜色。字节顺序（Byte Order）为 `RGB_888`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
0x000000
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_THREAD_PRIORITY"></a>

## 78.12 `CONFIG_SDL_DISPLAY_THREAD_PRIORITY`

**提示（Prompt）**：SDL 显示线程优先级（Display Thread Priority）

**说明（Help）**

绘图线程（Drawing Thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_MAIN_THREAD_PRIORITY
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MAIN_THREAD_PRIORITY`](P001_kernel_配置项参考_1.md#CONFIG_MAIN_THREAD_PRIORITY)。

<a id="CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_COLOR_1"></a>

## 78.13 `CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_COLOR_1`

**提示（Prompt）**：透明网格单元格颜色 1（Transparency Grid Cell Color 1）

**说明（Help）**

透明网格（Transparency Grid）中奇数单元格的颜色。字节顺序（Byte Order）为 `RGB_888`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
0xcccccc
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_COLOR_2"></a>

## 78.14 `CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_COLOR_2`

**提示（Prompt）**：透明网格单元格颜色 2（Transparency Grid Cell Color 2）

**说明（Help）**

透明网格（Transparency Grid）中偶数单元格的颜色。字节顺序（Byte Order）为 `RGB_888`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
0xbbbbbb
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_SIZE"></a>

## 78.15 `CONFIG_SDL_DISPLAY_TRANSPARENCY_GRID_CELL_SIZE`

**提示（Prompt）**：透明网格单元格大小（Transparency Grid Cell Size）

**说明（Help）**

棋盘格图案（Checkerboard Pattern）中方格的大小，以像素为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_USE_HARDWARE_ACCELERATOR"></a>

## 78.16 `CONFIG_SDL_DISPLAY_USE_HARDWARE_ACCELERATOR`

**提示（Prompt）**：使用硬件加速器（Hardware Accelerator）

**说明（Help）**

为图形渲染（Graphics Rendering）启用硬件加速（Hardware Acceleration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SDL_DISPLAY_ZOOM_PCT"></a>

## 78.17 `CONFIG_SDL_DISPLAY_ZOOM_PCT`

**提示（Prompt）**：默认缩放百分比（Default Zoom Percentage）

**说明（Help）**

SDL 窗口的缩放百分比（Zoom Percentage），用于改善小屏幕上的可读性。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SDL_DISPLAY && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[10, 10000]
```

**定义位置（Location）**：[`drivers/display/Kconfig.sdl:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sdl#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 基于 SDL 的仿真显示（Emulated Display）

**配置项引用（Symbol References）**：[`CONFIG_SDL_DISPLAY`](P078_drivers_display_配置项参考_2.md#CONFIG_SDL_DISPLAY)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SH1122"></a>

## 78.18 `CONFIG_SH1122`

**提示（Prompt）**：SH1122 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SH1122 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SINOWEALTH_SH1122_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI if n
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.sh1122:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sh1122#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SH1122_DEFAULT_CONTRAST"></a>

## 78.19 `CONFIG_SH1122_DEFAULT_CONTRAST`

**提示（Prompt）**：SH1122 默认对比度（Default Contrast）

**说明（Help）**

SH1122 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SH1122 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.sh1122:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.sh1122#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SH1122 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SH1122`](P078_drivers_display_配置项参考_2.md#CONFIG_SH1122)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1306"></a>

## 78.20 `CONFIG_SSD1306`

**提示（Prompt）**：SSD1306 显示驱动（Display Driver）

**说明（Help）**

启用 SSD1306 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SOLOMON_SSD1306_ENABLED || DT_HAS_SOLOMON_SSD1306B_ENABLED || DT_HAS_SOLOMON_SSD1315_ENABLED || DT_HAS_SOLOMON_SSD1309_ENABLED || DT_HAS_SOLOMON_SSD1305_ENABLED || DT_HAS_SINOWEALTH_SH1106_ENABLED || DT_HAS_SINOWEALTH_SH1107_ENABLED || DT_HAS_CHIPWEALTH_CH1115_ENABLED || DT_HAS_CHIPWEALTH_CH1116_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
CONFIG_I2C if n
CONFIG_SPI if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1306:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1306#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_SSD1306_DEFAULT_CONTRAST"></a>

## 78.21 `CONFIG_SSD1306_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1306 默认对比度（Default Contrast）

**说明（Help）**

SSD1306 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1306 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1306:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1306#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1306 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1306`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1306)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1320"></a>

## 78.22 `CONFIG_SSD1320`

**提示（Prompt）**：SSD1320 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1320 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1320_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI if n
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1320:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1320#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SSD1320_CONV_BUFFER_LINES"></a>

## 78.23 `CONFIG_SSD1320_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1320 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 160]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1320:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1320#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1320 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1320`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1320)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1320_DEFAULT_CONTRAST"></a>

## 78.24 `CONFIG_SSD1320_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1320 默认对比度（Default Contrast）

**说明（Help）**

SSD1320 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1320 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1320:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1320#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1320 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1320`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1320)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1322"></a>

## 78.25 `CONFIG_SSD1322`

**提示（Prompt）**：SSD1322 显示驱动（Display Driver）

**说明（Help）**

启用 SSD1322 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1322_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1322:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1322#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_SSD1322_CONV_BUFFER_LINES"></a>

## 78.26 `CONFIG_SSD1322_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1322 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1322:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1322#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1322 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1322`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1322)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1322_DEFAULT_GRAYSCALE"></a>

## 78.27 `CONFIG_SSD1322_DEFAULT_GRAYSCALE`

**提示（Prompt）**：SSD1322 默认采用灰度模式（Grayscale Mode）

**说明（Help）**

将灰度模式（Grayscale Mode）设为默认模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1322 && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1322:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1322#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1322 显示驱动（Display Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1322`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1322)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1325_CONV_BUFFER_LINES"></a>

## 78.28 `CONFIG_SSD1325_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1327_5 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1327_5:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1327_5#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1327/5 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1325_DEFAULT_CONTRAST"></a>

## 78.29 `CONFIG_SSD1325_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1325 默认对比度（Default Contrast）

**说明（Help）**

SSD1325 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1327_5 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1327_5:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1327_5#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1327/5 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1327_5"></a>

## 78.30 `CONFIG_SSD1327_5`

**提示（Prompt）**：SSD1327/5 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1327 和 SSD1325 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SOLOMON_SSD1327_ENABLED || DT_HAS_SOLOMON_SSD1325_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n || n
CONFIG_MIPI_DBI if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1327_5:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1327_5#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_SSD1327_CONV_BUFFER_LINES"></a>

## 78.31 `CONFIG_SSD1327_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1327_5 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1327_5:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1327_5#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1327/5 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1327_DEFAULT_CONTRAST"></a>

## 78.32 `CONFIG_SSD1327_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1327 默认对比度（Default Contrast）

**说明（Help）**

SSD1327 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1327_5 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1327_5:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1327_5#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1327/5 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1327_5`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1327_5)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1331"></a>

## 78.33 `CONFIG_SSD1331`

**提示（Prompt）**：SSD1331 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1331 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1331_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1331:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1331#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_SSD1331_CONTRASTA"></a>

## 78.34 `CONFIG_SSD1331_CONTRASTA`

**提示（Prompt）**：SSD1331 段 A（Segment A）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 A（Segment A）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1331 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
145
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1331:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1331#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1331 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1331`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1331)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1331_CONTRASTB"></a>

## 78.35 `CONFIG_SSD1331_CONTRASTB`

**提示（Prompt）**：SSD1331 段 B（Segment B）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 B（Segment B）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1331 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1331:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1331#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1331 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1331`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1331)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1331_CONTRASTC"></a>

## 78.36 `CONFIG_SSD1331_CONTRASTC`

**提示（Prompt）**：SSD1331 段 C（Segment C）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 C（Segment C）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1331 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
125
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1331:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1331#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1331 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1331`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1331)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1331_DEFAULT_CONTRAST"></a>

## 78.37 `CONFIG_SSD1331_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1331 默认对比度（Default Contrast）

**说明（Help）**

SSD1331 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1331 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1331:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1331#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1331 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1331`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1331)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1351"></a>

## 78.38 `CONFIG_SSD1351`

**提示（Prompt）**：SSD1351 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1351 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1351_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SSD135X
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)。

<a id="CONFIG_SSD1357"></a>

## 78.39 `CONFIG_SSD1357`

**提示（Prompt）**：SSD1357 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1357 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1357_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SSD135X
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)。

<a id="CONFIG_SSD135X"></a>

## 78.40 `CONFIG_SSD135X`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

所有 SSD135x 驱动共用的隐藏配置项（Hidden Configuration Entry）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DISPLAY
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**被选择（Selected by）**

```text
CONFIG_SSD1351
CONFIG_SSD1357
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_SSD1351`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1351)、[`CONFIG_SSD1357`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1357)。

<a id="CONFIG_SSD135X_CONTRASTA"></a>

## 78.41 `CONFIG_SSD135X_CONTRASTA`

**提示（Prompt）**：SSD135x 段 A（Segment A）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 A（Segment A）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD135X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
145
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD135X_CONTRASTB"></a>

## 78.42 `CONFIG_SSD135X_CONTRASTB`

**提示（Prompt）**：SSD135x 段 B（Segment B）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 B（Segment B）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD135X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD135X_CONTRASTC"></a>

## 78.43 `CONFIG_SSD135X_CONTRASTC`

**提示（Prompt）**：SSD135x 段 C（Segment C）的对比度倍增系数（Contrast Multiplier）

**说明（Help）**

段 C（Segment C）的对比度倍增系数（Contrast Multiplier）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD135X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
125
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD135X_DEFAULT_CONTRAST"></a>

## 78.44 `CONFIG_SSD135X_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD135x 默认对比度（Default Contrast）

**说明（Help）**

默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD135X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
100
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd135x:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd135x#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SSD135X`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD135X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1363"></a>

## 78.45 `CONFIG_SSD1363`

**提示（Prompt）**：SSD1363 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 SSD1363 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SOLOMON_SSD1363_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI if n
CONFIG_I2C if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1363:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1363#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_SSD1363_CONV_BUFFER_LINES"></a>

## 78.46 `CONFIG_SSD1363_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1363 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 160]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1363:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1363#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1363 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1363`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1363)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD1363_DEFAULT_CONTRAST"></a>

## 78.47 `CONFIG_SSD1363_DEFAULT_CONTRAST`

**提示（Prompt）**：SSD1363 默认对比度（Default Contrast）

**说明（Help）**

SSD1363 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SSD1363 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
192
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd1363:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd1363#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → SSD1363 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SSD1363`](P078_drivers_display_配置项参考_2.md#CONFIG_SSD1363)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_SSD16XX"></a>

## 78.48 `CONFIG_SSD16XX`

**提示（Prompt）**：SSD16XX 兼容显示控制器驱动（Compatible Display Controller Driver）

**说明（Help）**

启用 SSD16XX 兼容控制器（Compatible Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SOLOMON_SSD1608_ENABLED || DT_HAS_SOLOMON_SSD1673_ENABLED || DT_HAS_SOLOMON_SSD1675A_ENABLED || DT_HAS_SOLOMON_SSD1680_ENABLED || DT_HAS_SOLOMON_SSD1681_ENABLED || DT_HAS_SOLOMON_SSD1683_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.ssd16xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.ssd16xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST730X"></a>

## 78.49 `CONFIG_ST730X`

**提示（Prompt）**：ST730x 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 ST730X 系列显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_SITRONIX_ST7305_ENABLED || DT_HAS_SITRONIX_ST7306_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**弱选择（Implies）**

```text
CONFIG_DISPLAY_COLOR_PALETTE if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.st730x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st730x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)。

<a id="CONFIG_ST730X_CONV_BUFFER_LINE_CNT"></a>

## 78.50 `CONFIG_ST730X_CONV_BUFFER_LINE_CNT`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）大小，以行为单位

**说明（Help）**

转换缓冲区（Conversion Buffer）的大小，以行为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST730X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st730x:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st730x#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST730x 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_ST730X`](P078_drivers_display_配置项参考_2.md#CONFIG_ST730X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST730X_DEFAULT_PALETTED"></a>

## 78.51 `CONFIG_ST730X_DEFAULT_PALETTED`

**提示（Prompt）**：ST730X 默认采用调色板 i4 模式（Paletted i4）

**说明（Help）**

将调色板 i4 模式（Paletted i4）设为默认颜色模式（Color Mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7306_ENABLED && CONFIG_ST730X && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y if n
```

**主动选择（Selects）**

```text
CONFIG_DISPLAY_COLOR_PALETTE
```

**定义位置（Location）**：[`drivers/display/Kconfig.st730x:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st730x#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST730x 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_ST730X`](P078_drivers_display_配置项参考_2.md#CONFIG_ST730X)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_DISPLAY_COLOR_PALETTE`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_COLOR_PALETTE)。

<a id="CONFIG_ST75256"></a>

## 78.52 `CONFIG_ST75256`

**提示（Prompt）**：ST75256 显示控制器（Display Controller）

**说明（Help）**

启用 ST75256 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST75256_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st75256:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st75256#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST75256_CONV_BUFFER_LINES"></a>

## 78.53 `CONFIG_ST75256_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST75256 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 162]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st75256:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st75256#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST75256 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST75256`](P078_drivers_display_配置项参考_2.md#CONFIG_ST75256)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST75256_DEFAULT_CONTRAST"></a>

## 78.54 `CONFIG_ST75256_DEFAULT_CONTRAST`

**提示（Prompt）**：ST75256 默认对比度（Default Contrast）

**说明（Help）**

ST75256 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST75256 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
155
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st75256:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st75256#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST75256 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST75256`](P078_drivers_display_配置项参考_2.md#CONFIG_ST75256)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST75256_DEFAULT_GREYSCALE"></a>

## 78.55 `CONFIG_ST75256_DEFAULT_GREYSCALE`

**提示（Prompt）**：ST75256 默认采用灰度模式（Greyscale Mode）

**说明（Help）**

将灰度模式（Greyscale Mode）设为默认模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ST75256 && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.st75256:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st75256#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST75256 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST75256`](P078_drivers_display_配置项参考_2.md#CONFIG_ST75256)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST7567"></a>

## 78.56 `CONFIG_ST7567`

**提示（Prompt）**：ST7567 显示控制器（Display Controller）

**说明（Help）**

启用 ST7567 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7567_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if n
CONFIG_MIPI_DBI if n
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7567:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7567#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST7567_DEFAULT_CONTRAST"></a>

## 78.57 `CONFIG_ST7567_DEFAULT_CONTRAST`

**提示（Prompt）**：ST7567 默认对比度（Default Contrast）

**说明（Help）**

ST7567 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST7567 && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
127
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7567:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7567#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST7567 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST7567`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7567)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST7586S"></a>

## 78.58 `CONFIG_ST7586S`

**提示（Prompt）**：ST7586S 显示控制器（Display Controller）

**说明（Help）**

启用 ST7586S 显示控制器（Display Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7586S_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7586s:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7586s#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST7586S_CONV_BUFFER_LINES"></a>

## 78.59 `CONFIG_ST7586S_CONV_BUFFER_LINES`

**提示（Prompt）**：转换缓冲区（Conversion Buffer）可容纳的行数

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST7586S && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 162]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7586s:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7586s#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST7586S 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST7586S`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7586S)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST7586S_DEFAULT_CONTRAST"></a>

## 78.60 `CONFIG_ST7586S_DEFAULT_CONTRAST`

**提示（Prompt）**：ST7586S 默认对比度（Default Contrast）

**说明（Help）**

ST7586S 的默认对比度（Default Contrast）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ST7586S && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
152
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7586s:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7586s#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST7586S 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST7586S`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7586S)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST7586S_DEFAULT_GRAYSCALE"></a>

## 78.61 `CONFIG_ST7586S_DEFAULT_GRAYSCALE`

**提示（Prompt）**：ST7586S 默认采用灰度模式（Grayscale Mode）

**说明（Help）**

将灰度模式（Greyscale Mode）设为默认模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ST7586S && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7586s:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7586s#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → ST7586S 显示控制器（Display Controller）

**配置项引用（Symbol References）**：[`CONFIG_ST7586S`](P078_drivers_display_配置项参考_2.md#CONFIG_ST7586S)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_ST7701"></a>

## 78.62 `CONFIG_ST7701`

**提示（Prompt）**：ST7701 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 ST7701 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7701_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7701:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7701#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)。

<a id="CONFIG_ST7735R"></a>

## 78.63 `CONFIG_ST7735R`

**提示（Prompt）**：ST7735R/ST7735S 显示驱动（Display Driver）

**说明（Help）**

启用 ST7735R/ST7735S 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7735R_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7735r:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7735r#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST7789V"></a>

## 78.64 `CONFIG_ST7789V`

**提示（Prompt）**：ST7789V 显示驱动（Display Driver）

**说明（Help）**

启用 ST7789V 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7789V_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7789v:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7789v#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_ST7796S"></a>

## 78.65 `CONFIG_ST7796S`

**提示（Prompt）**：ST7796S 显示驱动（Display Driver）

**说明（Help）**

启用 ST7796S 显示驱动（Display Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SITRONIX_ST7796S_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.st7796s:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.st7796s#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_STM32_LTDC"></a>

## 78.66 `CONFIG_STM32_LTDC`

**提示（Prompt）**：STM32 LCD-TFT 显示控制器驱动（Display Controller Driver）

**说明（Help）**

启用 STM32 LCD-TFT 显示控制器外设（Display Controller Peripheral）的驱动；原帮助文本将 LCD 拼作 `LCT`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_LTDC_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_LTDC
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_PINCTRL
CONFIG_RESET
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_USE_STM32_HAL_LTDC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_LTDC)、[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_STM32_LTDC_ARGB8888"></a>

## 78.67 `CONFIG_STM32_LTDC_ARGB8888`

**提示（Prompt）**：ARGB8888 颜色格式（Color Format）

**说明（Help）**

一个像素由 8 位透明度（Alpha）、8 位红色、8 位绿色和 8 位蓝色值组成，每像素 4 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_LTDC_PIXEL_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver） → 彩色像素格式（Color Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC_PIXEL_FORMAT`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_PIXEL_FORMAT)。

<a id="CONFIG_STM32_LTDC_DISABLE_FMC_BANK1"></a>

## 78.68 `CONFIG_STM32_LTDC_DISABLE_FMC_BANK1`

**提示（Prompt）**：为 STM32F7/H7 系列禁用 FMC bank1

**说明（Help）**

当 FMC bank1 未使用时禁用它，以避免推测性读取访问（Speculative Read Access）。参见 AN4861 的“4.6 Special recommendations for Cortex-M7 (STM32F7/H7)”（针对 Cortex-M7 的特别建议）一节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_STM32H7X || CONFIG_SOC_SERIES_STM32F7X) && CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32F7X`。

<a id="CONFIG_STM32_LTDC_FB_NUM"></a>

## 78.69 `CONFIG_STM32_LTDC_FB_NUM`

**提示（Prompt）**：帧缓冲（Frame Buffer）数量

**说明（Help）**

STM32 LTDC 帧缓冲（Frame Buffer）数量配置：

- `0`：由应用程序维护帧缓冲，写入时必须提供全屏像素。
- `1`：在 STM32 LTDC 驱动中使用单帧缓冲（Single Frame Buffer）。
- `2`：在 STM32 LTDC 驱动中使用双帧缓冲（Double Frame Buffer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 2]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig)。

```text
0
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig)。

```text
0
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_STM32_LTDC_FB_SMH_ALIGN"></a>

## 78.70 `CONFIG_STM32_LTDC_FB_SMH_ALIGN`

**提示（Prompt）**：显示缓冲区的共享多堆缓冲区对齐（Shared Multi Heap Buffer Alignment）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP && CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver） → 为显示缓冲区（Display Buffer）使用共享多堆（Shared Multi Heap）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_STM32_LTDC_FB_SMH_ATTRIBUTE"></a>

## 78.71 `CONFIG_STM32_LTDC_FB_SMH_ATTRIBUTE`

**提示（Prompt）**：显示缓冲区的共享多堆属性（Shared Multi Heap Attribute）

**说明（Help）**

显示缓冲区（Display Buffer）的共享多堆属性（Shared Multi Heap Attribute）：

- `0`：`SMH_REG_ATTR_CACHEABLE`。
- `1`：`SMH_REG_ATTR_NON_CACHEABLE`。
- `2`：`SMH_REG_ATTR_EXTERNAL`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP && CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver） → 为显示缓冲区（Display Buffer）使用共享多堆（Shared Multi Heap）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP)、[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP"></a>

## 78.72 `CONFIG_STM32_LTDC_FB_USE_SHARED_MULTI_HEAP`

**提示（Prompt）**：为显示缓冲区（Display Buffer）使用共享多堆（Shared Multi Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)。

<a id="CONFIG_STM32_LTDC_PIXEL_FORMAT"></a>

## 78.73 `CONFIG_STM32_LTDC_PIXEL_FORMAT`

**提示（Prompt）**：彩色像素格式（Color Pixel Format）

**说明（Help）**

指定 STM32 LCD-TFT 显示控制器（Display Controller）的彩色像素格式（Color Pixel Format）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STM32_LTDC && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
CONFIG_STM32_LTDC_RGB565
```

**可选项（Choices）**

```text
CONFIG_STM32_LTDC_ARGB8888
CONFIG_STM32_LTDC_RGB888
CONFIG_STM32_LTDC_RGB565
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC)、[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_STM32_LTDC_RGB565`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_RGB565)、[`CONFIG_STM32_LTDC_ARGB8888`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_ARGB8888)、[`CONFIG_STM32_LTDC_RGB888`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_RGB888)。

<a id="CONFIG_STM32_LTDC_RGB565"></a>

## 78.74 `CONFIG_STM32_LTDC_RGB565`

**提示（Prompt）**：RGB565 颜色格式（Color Format）

**说明（Help）**

一个像素由 5 位红色、6 位绿色和 5 位蓝色值组成，每像素 2 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_LTDC_PIXEL_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver） → 彩色像素格式（Color Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC_PIXEL_FORMAT`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_PIXEL_FORMAT)。

<a id="CONFIG_STM32_LTDC_RGB888"></a>

## 78.75 `CONFIG_STM32_LTDC_RGB888`

**提示（Prompt）**：RGB888 颜色格式（Color Format）

**说明（Help）**

一个像素由 8 位红色、8 位绿色和 8 位蓝色值组成，每像素 3 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_LTDC_PIXEL_FORMAT>
```

**定义位置（Location）**：[`drivers/display/Kconfig.stm32_ltdc:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.stm32_ltdc#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → STM32 LCD-TFT 显示控制器驱动（Display Controller Driver） → 彩色像素格式（Color Pixel Format）

**配置项引用（Symbol References）**：[`CONFIG_STM32_LTDC_PIXEL_FORMAT`](P078_drivers_display_配置项参考_2.md#CONFIG_STM32_LTDC_PIXEL_FORMAT)。

<a id="CONFIG_UC81XX"></a>

## 78.76 `CONFIG_UC81XX`

**提示（Prompt）**：UltraChip UC81xx 兼容显示控制器驱动（Compatible Display Controller Driver）

**说明（Help）**

启用 UC81xx 兼容控制器（Compatible Controller）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ULTRACHIP_UC8175_ENABLED || DT_HAS_ULTRACHIP_UC8176_ENABLED || DT_HAS_ULTRACHIP_UC8151D_ENABLED || DT_HAS_ULTRACHIP_UC8253_ENABLED || DT_HAS_ULTRACHIP_UC8179_ENABLED) && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DBI
```

**定义位置（Location）**：[`drivers/display/Kconfig.uc81xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.uc81xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)。

<a id="CONFIG_WAVESHARE_DSI2DPI"></a>

## 78.77 `CONFIG_WAVESHARE_DSI2DPI`

**提示（Prompt）**：微雪（Waveshare）DSI 转 DPI 桥接驱动（Bridge Driver）

**说明（Help）**

启用微雪（Waveshare）DSI 转 DPI 显示桥接器（Display Bridge）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WAVESHARE_DSI2DPI_ENABLED && CONFIG_DISPLAY
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MIPI_DSI
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/display/Kconfig.waveshare_dsi2dpi:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/display/Kconfig.waveshare_dsi2dpi#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<!-- kconfig-navigation -->

[上一章](P077_drivers_display_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P079_drivers_dma_配置项参考_1.md)
