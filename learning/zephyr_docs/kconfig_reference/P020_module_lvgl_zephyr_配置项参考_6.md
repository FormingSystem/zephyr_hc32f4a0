---
id: learning.zephyr-docs.kconfig-reference.page-20
title: "`<module:lvgl>/zephyr`配置项参考（6/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第20章\_`<module:lvgl>/zephyr`配置项参考（6/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_USE_LINE"></a>

## 20.1 `CONFIG_LV_USE_LINE`

**提示（Prompt）**：线条（Line）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2233`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LINUX_DRM"></a>

## 20.2 `CONFIG_LV_USE_LINUX_DRM`

**提示（Prompt）**：Linux 直接渲染管理器（DRM）

**说明（Help）**

`/dev/dri/card` 设备驱动（Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2331`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LINUX_FBDEV"></a>

## 20.3 `CONFIG_LV_USE_LINUX_FBDEV`

**提示（Prompt）**：Linux 帧缓冲（Framebuffer，fbdev）

**说明（Help）**

`/dev/fb` 设备驱动（Driver）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2390`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LIST"></a>

## 20.4 `CONFIG_LV_USE_LIST`

**提示（Prompt）**：列表（List）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2237`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LODEPNG"></a>

## 20.5 `CONFIG_LV_USE_LODEPNG`

**提示（Prompt）**：PNG 解码器（Decoder，LodePNG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1565`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE)。

<a id="CONFIG_LV_USE_LOG"></a>

## 20.6 `CONFIG_LV_USE_LOG`

**提示（Prompt）**：日志（Logging）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1388`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LOTTIE"></a>

## 20.7 `CONFIG_LV_USE_LOTTIE`

**提示（Prompt）**：Lottie 动画

**说明（Help）**

使用 ThorVG Lottie 解析器（Parser）播放 Lottie JSON 动画（Animation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT && CONFIG_LV_USE_THORVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_VECTOR_GRAPHIC
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2241`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)、[`CONFIG_LV_USE_THORVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_THORVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_VECTOR_GRAPHIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_VECTOR_GRAPHIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_LOVYAN_GFX"></a>

## 20.8 `CONFIG_LV_USE_LOVYAN_GFX`

**提示（Prompt）**：LovyanGFX 图形库

**说明（Help）**

基于 LovyanGFX C++ 库的显示与触摸驱动（Display and Touch Driver）；构建中必须提供该库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2472`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LZ4"></a>

## 20.9 `CONFIG_LV_USE_LZ4`

**提示（Prompt）**：LZ4 压缩（Compression）

**说明（Help）**

LZ4 压缩／解压缩函数（Compress/Decompress Functions），供 LVGL 的压缩二进制图像使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1550`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_LZ4_INTERNAL"></a>

## 20.10 `CONFIG_LV_USE_LZ4_INTERNAL`

**提示（Prompt）**：随附的 LZ4（Bundled LZ4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_LZ4 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1556`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings） → LZ4 压缩（Compression）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_LZ4`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_LZ4)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_MATRIX"></a>

## 20.11 `CONFIG_LV_USE_MATRIX`

**提示（Prompt）**：矩阵（Matrix）

**说明（Help）**

用于变换（Transformation）的 3×3 矩阵 API（`lv_matrix_t`），需要浮点支持（Floating-point Support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_FLOAT
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_VECTOR_GRAPHIC
CONFIG_LV_USE_DRAW_VG_LITE
CONFIG_LV_USE_DRAW_NANOVG
CONFIG_LV_USE_OPENGLES
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:377`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_FLOAT`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_FLOAT)、[`CONFIG_LV_USE_VECTOR_GRAPHIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_VECTOR_GRAPHIC)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)。

<a id="CONFIG_LV_USE_MEM_MONITOR"></a>

## 20.12 `CONFIG_LV_USE_MEM_MONITOR`

**提示（Prompt）**：内存监测器（Memory Monitor）

**说明（Help）**

在屏幕标签（Label）中显示已用内存和内存碎片（Memory Fragmentation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_BUILTIN_MALLOC && CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3254`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_BUILTIN_MALLOC`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_BUILTIN_MALLOC)、[`CONFIG_LV_USE_SYSMON`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_MENU"></a>

## 20.13 `CONFIG_LV_USE_MENU`

**提示（Prompt）**：菜单（Menu）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2250`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_MICROPYTHON_MALLOC"></a>

## 20.14 `CONFIG_LV_USE_MICROPYTHON_MALLOC`

**提示（Prompt）**：MicroPython 解释器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:37`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内存分配函数来源（Malloc Functions Source）

<a id="CONFIG_LV_USE_MONKEY"></a>

## 20.15 `CONFIG_LV_USE_MONKEY`

**提示（Prompt）**：随机输入测试（Monkey Test）

**说明（Help）**

向用户界面（UI）输入随机事件，以进行压力测试（Stress Testing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3452`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 测试工具（Test Utilities）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_MSGBOX"></a>

## 20.16 `CONFIG_LV_USE_MSGBOX`

**提示（Prompt）**：消息框（Message Box）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_LABEL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2254`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_LABEL`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_LABEL)。

<a id="CONFIG_LV_USE_NANOVG"></a>

## 20.17 `CONFIG_LV_USE_NANOVG`

**提示（Prompt）**：NanoVG 矢量图形库

**说明（Help）**

构建随附的 NanoVG 矢量图形库（Vector Graphics Library）。NanoVG 渲染器需要该库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_DRAW_NANOVG
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3016`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)。

<a id="CONFIG_LV_USE_NANOVG_TEST_HEADLESS"></a>

## 20.18 `CONFIG_LV_USE_NANOVG_TEST_HEADLESS`

**提示（Prompt）**：NanoVG 的无窗口 EGL 显示（Headless EGL Display）

**说明（Help）**

渲染到离屏 EGL 像素缓冲（Off-screen EGL Pbuffer）而非窗口，并将像素读回 LVGL 绘制缓冲区，使截图比较与软件渲染器采用相同方式工作。需要 EGL 和 GLESv2。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LV_USE_TEST && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_OPENGLES_PBUFFER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3441`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 测试工具（Test Utilities） → 测试工具（Test Utilities）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_TEST`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_TEST)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_OPENGLES_PBUFFER`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES_PBUFFER)。

<a id="CONFIG_LV_USE_NATIVE_HELIUM_ASM"></a>

## 20.19 `CONFIG_LV_USE_NATIVE_HELIUM_ASM`

**提示（Prompt）**：原生 Helium 汇编（Native Helium Assembly）

**说明（Help）**

禁用后让 Arm-2D 自行工作，仅用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_SW && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:540`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 软件（SW） → 软件渲染器（SW Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NEMA_GFX"></a>

## 20.20 `CONFIG_LV_USE_NEMA_GFX`

**提示（Prompt）**：NemaGFX 渲染器（Renderer）

**说明（Help）**

使用 Think Silicon（TSi）的 NemaGFX GPU 库加速绘制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:781`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NEMA_HAL"></a>

## 20.21 `CONFIG_LV_USE_NEMA_HAL`

**提示（Prompt）**：NemaGFX 硬件抽象层（HAL）

**说明（Help）**

STM32 使用 LVGL 随附的硬件抽象层（HAL）。选择自定义（Custom）表示应用程序自行提供 NemaGFX HAL，即 `nema_hal.c`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_NEMA_HAL_CUSTOM
```

**可选项（Choices）**

```text
CONFIG_LV_NEMA_HAL_CUSTOM
CONFIG_LV_NEMA_HAL_STM32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:828`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_NEMA_HAL_CUSTOM`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_HAL_CUSTOM)、[`CONFIG_LV_NEMA_HAL_STM32`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_HAL_STM32)。

<a id="CONFIG_LV_USE_NEMA_LIB"></a>

## 20.22 `CONFIG_LV_USE_NEMA_LIB`

**提示（Prompt）**：NemaGFX 静态库（Static Library）

**说明（Help）**

根据目标 CPU 内核选择使用的随附 NemaGFX 库和头文件。选择无（None）会在构建时产生警告，并回退到 Cortex-M33（Rev C）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_NEMA_LIB_NONE
```

**可选项（Choices）**

```text
CONFIG_LV_NEMA_LIB_NONE
CONFIG_LV_NEMA_LIB_M33_REVC
CONFIG_LV_NEMA_LIB_M33_NEMAPVG
CONFIG_LV_NEMA_LIB_M55
CONFIG_LV_NEMA_LIB_M7
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:801`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_NEMA_LIB_NONE`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_LIB_NONE)、[`CONFIG_LV_NEMA_LIB_M33_REVC`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_LIB_M33_REVC)、[`CONFIG_LV_NEMA_LIB_M33_NEMAPVG`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_LIB_M33_NEMAPVG)、[`CONFIG_LV_NEMA_LIB_M55`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_LIB_M55)、[`CONFIG_LV_NEMA_LIB_M7`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_NEMA_LIB_M7)。

<a id="CONFIG_LV_USE_NEMA_VG"></a>

## 20.23 `CONFIG_LV_USE_NEMA_VG`

**提示（Prompt）**：NemaVG 矢量图形（Vector Graphics）

**说明（Help）**

在 NemaGFX 之上使用 NemaVG 绘制矢量图形（Vector Graphics，`lv_vector_dsc`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NEMA_GFX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:873`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → NemaGFX 图形库 → NemaGFX 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NEMA_GFX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NEMA_GFX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_NUTTX"></a>

## 20.24 `CONFIG_LV_USE_NUTTX`

**提示（Prompt）**：NuttX 操作系统

**说明（Help）**

NuttX 的显示和输入驱动，包括 `/dev/fb` 帧缓冲设备（Framebuffer Device）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2608`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_CUSTOM_INIT"></a>

## 20.25 `CONFIG_LV_USE_NUTTX_CUSTOM_INIT`

**提示（Prompt）**：自定义初始化 API（Custom Init API）

**说明（Help）**

跳过 `lv_nuttx_init()` 中的显示器和输入设备创建，使应用程序能够自行设置它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2633`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_INDEPENDENT_IMAGE_HEAP"></a>

## 20.26 `CONFIG_LV_USE_NUTTX_INDEPENDENT_IMAGE_HEAP`

**提示（Prompt）**：独立图像堆（Independent Image Heap）

**说明（Help）**

从独立的 NuttX 堆（Heap）分配缓存图像缓冲区，防止主堆产生碎片（Fragmentation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2616`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_LCD"></a>

## 20.27 `CONFIG_LV_USE_NUTTX_LCD`

**提示（Prompt）**：液晶显示设备（LCD Device）

**说明（Help）**

在 NuttX LCD 字符设备（Character Device）而非帧缓冲设备（Framebuffer Device）上创建显示器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2639`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_LIBUV"></a>

## 20.28 `CONFIG_LV_USE_NUTTX_LIBUV`

**提示（Prompt）**：libuv 事件循环（Event Loop）

**说明（Help）**

通过 libuv 循环而非默认定时器循环，驱动 LVGL 定时器处理程序（Timer Handler）以及显示／输入定时器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2627`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_MOUSE"></a>

## 20.29 `CONFIG_LV_USE_NUTTX_MOUSE`

**提示（Prompt）**：鼠标（Mouse）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2685`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_MOUSE_MOVE_STEP"></a>

## 20.30 `CONFIG_LV_USE_NUTTX_MOUSE_MOVE_STEP`

**提示（Prompt）**：鼠标移动步长（Mouse Movement Step，像素）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX_MOUSE && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2689`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统 → 鼠标（Mouse）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX_MOUSE`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX_MOUSE)、[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_TOUCHSCREEN"></a>

## 20.31 `CONFIG_LV_USE_NUTTX_TOUCHSCREEN`

**提示（Prompt）**：触摸屏（Touchscreen）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2674`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NUTTX_TRACE_FILE"></a>

## 20.32 `CONFIG_LV_USE_NUTTX_TRACE_FILE`

**提示（Prompt）**：性能分析跟踪文件（Profiler Trace File）

**说明（Help）**

将内置性能分析器（Built-in Profiler）的输出写入文件，而非控制台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER_BUILTIN && CONFIG_LV_USE_NUTTX && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2695`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → NuttX 操作系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER_BUILTIN`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PROFILER_BUILTIN)、[`CONFIG_LV_USE_NUTTX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NUTTX)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_NV3007"></a>

## 20.33 `CONFIG_LV_USE_NV3007`

**提示（Prompt）**：NV3007 显示控制器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GENERIC_MIPI
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2512`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GENERIC_MIPI`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GENERIC_MIPI)。

<a id="CONFIG_LV_USE_NXP_ELCDIF"></a>

## 20.34 `CONFIG_LV_USE_NXP_ELCDIF`

**提示（Prompt）**：NXP 增强型 LCD 接口（ELCDIF）

**说明（Help）**

在已完成初始化的 NXP ELCDIF LCD 控制器上创建显示器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2517`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBJ_ID"></a>

## 20.35 `CONFIG_LV_USE_OBJ_ID`

**提示（Prompt）**：控件 ID（Widget ID，`lv_obj_set_id`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1317`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBJ_ID_BUILTIN"></a>

## 20.36 `CONFIG_LV_USE_OBJ_ID_BUILTIN`

**提示（Prompt）**：内置 ID 处理程序（Built-in ID Handler）

**说明（Help）**

使用内置对象 ID 处理函数（Object ID Handler Functions）：

- `lv_obj_assign_id`：创建控件时调用。每种控件类（Widget Class）使用独立计数器作为 ID。
- `lv_obj_id_compare`：比较 ID，判断其是否与请求值匹配。
- `lv_obj_stringify_id`：返回字符串形式的标识符，例如 `"button3"`。
- `lv_obj_free_id`：不执行任何操作，因为 ID 不涉及内存分配。

禁用后，用户需要实现这些函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_OBJ_ID && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1327`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core） → 控件 ID（Widget ID，`lv_obj_set_id`）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OBJ_ID`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OBJ_ID)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBJ_NAME"></a>

## 20.37 `CONFIG_LV_USE_OBJ_NAME`

**提示（Prompt）**：控件名称（Widget Names，`lv_obj_set_name`）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1313`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBJ_PROPERTY"></a>

## 20.38 `CONFIG_LV_USE_OBJ_PROPERTY`

**提示（Prompt）**：通用控件属性设置／获取 API（Generic Widget Property Set/Get API）

**说明（Help）**

通过统一的、基于通用属性 ID（Property ID）的 API，获取和设置任意控件样式或属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1340`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBJ_PROPERTY_NAME"></a>

## 20.39 `CONFIG_LV_USE_OBJ_PROPERTY_NAME`

**提示（Prompt）**：按名称访问属性（Access Properties by Name）

**说明（Help）**

为每个控件类（Widget Class）添加名称表，以便按名称访问属性。注意，该常量表（Const Table）会增加 Flash 占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_OBJ_PROPERTY && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1348`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core） → 通用控件属性设置／获取 API（Generic Widget Property Set/Get API）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OBJ_PROPERTY`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OBJ_PROPERTY)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OBSERVER"></a>

## 20.40 `CONFIG_LV_USE_OBSERVER`

**提示（Prompt）**：观察者（Observer）

**说明（Help）**

将控件绑定到主题变量（Subject Variable），使其在变量值改变时自动更新。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1371`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OPENGLES"></a>

## 20.41 `CONFIG_LV_USE_OPENGLES`

**提示（Prompt）**：OpenGL ES 图形 API

**说明（Help）**

通用 OpenGL ES 显示驱动（Display Driver），用于将 LVGL 嵌入其他应用程序，或通过 GLFW/EGL 驱动 LVGL。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_MATRIX
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_DRAW_NANOVG
CONFIG_LV_USE_DRAW_OPENGLES
CONFIG_LV_LINUX_DRM_BACKEND_EGL
CONFIG_LV_USE_OPENGLES_PBUFFER
CONFIG_LV_USE_GLFW
CONFIG_LV_WAYLAND_USE_EGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2709`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_MATRIX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MATRIX)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_DRAW_OPENGLES`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_LINUX_DRM_BACKEND_EGL`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_LINUX_DRM_BACKEND_EGL)、[`CONFIG_LV_USE_OPENGLES_PBUFFER`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES_PBUFFER)、[`CONFIG_LV_USE_GLFW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GLFW)、[`CONFIG_LV_WAYLAND_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_WAYLAND_USE_EGL)。

<a id="CONFIG_LV_USE_OPENGLES_DEBUG"></a>

## 20.42 `CONFIG_LV_USE_OPENGLES_DEBUG`

**提示（Prompt）**：调试模式（Debug Mode）

**说明（Help）**

在每次 GL 调用后检查 OpenGL 错误，并连同调用位置（Call Site）一起记录。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_OPENGLES && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2718`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → OpenGL ES 图形 API

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_OPENGLES_PBUFFER"></a>

## 20.43 `CONFIG_LV_USE_OPENGLES_PBUFFER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在完全没有窗口系统（Window System）的情况下，由 GPU 渲染到离屏 EGL 像素缓冲（Off-screen EGL Pbuffer），并将帧读回显示器的绘制缓冲区。用于无窗口渲染（Headless Rendering）、截图测试和服务器端图像生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_EGL
CONFIG_LV_USE_OPENGLES
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_NANOVG_TEST_HEADLESS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2732`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_EGL)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)、[`CONFIG_LV_USE_NANOVG_TEST_HEADLESS`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_NANOVG_TEST_HEADLESS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_USE_EGL`。

<a id="CONFIG_LV_USE_OS"></a>

## 20.44 `CONFIG_LV_USE_OS`

**提示（Prompt）**：操作系统（Operating System）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_OS_NONE
```

**可选项（Choices）**

```text
CONFIG_LV_OS_NONE
CONFIG_LV_OS_PTHREAD
CONFIG_LV_OS_FREERTOS
CONFIG_LV_OS_CMSIS_RTOS2
CONFIG_LV_OS_RTTHREAD
CONFIG_LV_OS_WINDOWS
CONFIG_LV_OS_MQX
CONFIG_LV_OS_SDL2
CONFIG_LV_OS_CUSTOM
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:168`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 操作系统（Operating System，OS）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_OS_NONE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_NONE)、[`CONFIG_LV_OS_PTHREAD`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_PTHREAD)、[`CONFIG_LV_OS_FREERTOS`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_FREERTOS)、[`CONFIG_LV_OS_CMSIS_RTOS2`](P017_module_lvgl_zephyr_配置项参考_3.md#CONFIG_LV_OS_CMSIS_RTOS2)、[`CONFIG_LV_OS_RTTHREAD`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_RTTHREAD)、[`CONFIG_LV_OS_WINDOWS`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_WINDOWS)、[`CONFIG_LV_OS_MQX`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_MQX)、[`CONFIG_LV_OS_SDL2`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_SDL2)、[`CONFIG_LV_OS_CUSTOM`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_CUSTOM)。

<a id="CONFIG_LV_USE_PARALLEL_DRAW_DEBUG"></a>

## 20.45 `CONFIG_LV_USE_PARALLEL_DRAW_DEBUG`

**提示（Prompt）**：绘制单元覆盖层（Draw Unit Overlay）

**说明（Help）**

为每个绘制单元（Draw Unit）的任务绘制不同颜色的覆盖层（Overlay），并在白色背景上显示绘制单元索引号；图层的背景为黑色。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3471`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 调试渲染（Debug Rendering）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PERF_MONITOR"></a>

## 20.46 `CONFIG_LV_USE_PERF_MONITOR`

**提示（Prompt）**：性能监测器（Performance Monitor）

**说明（Help）**

在屏幕标签（Label）中显示 CPU 使用率和每秒帧数（FPS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被弱选择（Implied by）**

```text
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3216`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SYSMON`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_USE_PERF_MONITOR_LOG_MODE"></a>

## 20.47 `CONFIG_LV_USE_PERF_MONITOR_LOG_MODE`

**提示（Prompt）**：记录性能数据（Log Performance Data）

**说明（Help）**

将性能数据（Performance Data）打印到日志，而非在屏幕标签中显示。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PERF_MONITOR && CONFIG_LV_USE_SYSMON && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3247`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring） → 系统监测器（System Monitor） → 性能监测器（Performance Monitor）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PERF_MONITOR`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PERF_MONITOR)、[`CONFIG_LV_USE_SYSMON`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SYSMON)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PPA"></a>

## 20.48 `CONFIG_LV_USE_PPA`

**提示（Prompt）**：PPA 渲染器（Renderer）

**说明（Help）**

使用 Espressif SoC 的像素处理加速器（Pixel Processing Accelerator，PPA）外设加速混合（Blend）、填充（Fill）和变换（Transform）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_SW
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:937`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)。

<a id="CONFIG_LV_USE_PPA_IMG"></a>

## 20.49 `CONFIG_LV_USE_PPA_IMG`

**提示（Prompt）**：图像绘制（Image Drawing）

**说明（Help）**

允许 PPA 也绘制图像。仅适用于简单情况：未缩放、未旋转、完全不透明且无蒙版（Mask）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PPA && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:947`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素处理加速器（PPA） → PPA 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PPA`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PPA)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PRIVATE_API"></a>

## 20.50 `CONFIG_LV_USE_PRIVATE_API`

**提示（Prompt）**：私有 API（Private API，`lvgl_private.h`）

**说明（Help）**

从 `lvgl.h` 包含 `lvgl_private.h`，使 LVGL 内部数据结构和函数默认可访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3532`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 构建（Build）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PROFILER"></a>

## 20.51 `CONFIG_LV_USE_PROFILER`

**提示（Prompt）**：性能分析器（Profiler）

**说明（Help）**

通过跟踪钩子（Trace Hook）对 LVGL 内部进行插桩（Instrumentation），以测量运行时性能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_PROFILER_BUILTIN
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3313`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_PROFILER_BUILTIN`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PROFILER_BUILTIN)。

<a id="CONFIG_LV_USE_PROFILER_BUILTIN"></a>

## 20.52 `CONFIG_LV_USE_PROFILER_BUILTIN`

**提示（Prompt）**：内置性能分析器（Built-in Profiler）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_PROFILER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3319`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_PROFILER`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PROFILER)。

<a id="CONFIG_LV_USE_PROFILER_BUILTIN_POSIX"></a>

## 20.53 `CONFIG_LV_USE_PROFILER_BUILTIN_POSIX`

**提示（Prompt）**：POSIX 移植层（Port）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_PROFILER_BUILTIN && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3334`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 性能分析器（Profiler） → 内置性能分析器（Built-in Profiler）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_PROFILER_BUILTIN`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_PROFILER_BUILTIN)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PXP"></a>

## 20.54 `CONFIG_LV_USE_PXP`

**提示（Prompt）**：PXP，旧版（Legacy）

**说明（Help）**

请改用 `LV_USE_DRAW_PXP`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_PXP
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:897`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素流水线（PXP）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_PXP`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_PXP)。

<a id="CONFIG_LV_USE_PXP_ASSERT"></a>

## 20.55 `CONFIG_LV_USE_PXP_ASSERT`

**提示（Prompt）**：断言（Asserts）

**说明（Help）**

检查每次 PXP 调用的状态，失败时触发断言（Assert）。这对开发板初始调试（Bring-up）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_PXP && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:927`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素流水线（PXP） → PXP 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_PXP`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_PXP)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_PXP_DRAW_THREAD"></a>

## 20.56 `CONFIG_LV_USE_PXP_DRAW_THREAD`

**提示（Prompt）**：专用绘制线程（Dedicated Draw Thread）

**说明（Help）**

通过独立线程分派 PXP 操作，使 CPU 能继续并行渲染。需要操作系统（OS）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LV_USE_DRAW_PXP && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:919`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素流水线（PXP） → PXP 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_NONE)、[`CONFIG_LV_USE_DRAW_PXP`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_PXP)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_QNX"></a>

## 20.57 `CONFIG_LV_USE_QNX`

**提示（Prompt）**：QNX 操作系统

**说明（Help）**

在 QNX Screen 窗口中创建显示器，并读取指针和键盘输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2751`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_QRCODE"></a>

## 20.58 `CONFIG_LV_USE_QRCODE`

**提示（Prompt）**：二维码（QR Code）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_CANVAS
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2259`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_CANVAS`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CANVAS)。

<a id="CONFIG_LV_USE_REFR_DEBUG"></a>

## 20.59 `CONFIG_LV_USE_REFR_DEBUG`

**提示（Prompt）**：重绘区域覆盖层（Redraw Area Overlay）

**说明（Help）**

在重绘区域上绘制随机颜色的矩形。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3461`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 调试渲染（Debug Rendering）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_RENESAS_GLCDC"></a>

## 20.60 `CONFIG_LV_USE_RENESAS_GLCDC`

**提示（Prompt）**：Renesas 图形 LCD 控制器（GLCDC）

**说明（Help）**

创建由 Renesas GLCDC 外设驱动的显示器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2522`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_RLE"></a>

## 20.61 `CONFIG_LV_USE_RLE`

**提示（Prompt）**：游程编码压缩（RLE Compression）

**说明（Help）**

LVGL 游程编码（Run-length Encoded）二进制图像格式的解码器（Decoder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1545`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_RLOTTIE"></a>

## 20.62 `CONFIG_LV_USE_RLOTTIE`

**提示（Prompt）**：Lottie，旧版 rlottie（Legacy）

**说明（Help）**

旧版 rlottie 绑定（Binding），为兼容而保留。请改用 `LV_USE_LOTTIE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2263`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ROLLER"></a>

## 20.63 `CONFIG_LV_USE_ROLLER`

**提示（Prompt）**：滚轮选择器（Roller）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_LABEL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2269`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_LABEL`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_LABEL)。

<a id="CONFIG_LV_USE_ROTATE_PXP"></a>

## 20.64 `CONFIG_LV_USE_ROTATE_PXP`

**提示（Prompt）**：显示旋转（Display Rotation）

**说明（Help）**

使用 PXP 而非 CPU 旋转渲染后的显示缓冲区（Display Buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_PXP && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:913`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 像素流水线（PXP） → PXP 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_PXP`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_PXP)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_RTTHREAD_MALLOC"></a>

## 20.65 `CONFIG_LV_USE_RTTHREAD_MALLOC`

**提示（Prompt）**：RT-Thread 实时操作系统

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:40`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 内存分配函数来源（Malloc Functions Source）

<a id="CONFIG_LV_USE_RTTHREAD_SPRINTF"></a>

## 20.66 `CONFIG_LV_USE_RTTHREAD_SPRINTF`

**提示（Prompt）**：RT-Thread：`rt_vsnprintf`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:91`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 格式化输出函数来源（Sprintf Functions Source）

<a id="CONFIG_LV_USE_RTTHREAD_STRING"></a>

## 20.67 `CONFIG_LV_USE_RTTHREAD_STRING`

**提示（Prompt）**：RT-Thread：`rt_memcpy/rt_memset/rt_strlen/rt_strcpy`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:66`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 内存与标准库（Memory and Standard Library） → 字符串函数来源（String Functions Source）

<a id="CONFIG_LV_USE_SCALE"></a>

## 20.68 `CONFIG_LV_USE_SCALE`

**提示（Prompt）**：刻度（Scale）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2274`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SDL"></a>

## 20.69 `CONFIG_LV_USE_SDL`

**提示（Prompt）**：SDL 多媒体库

**说明（Help）**

通过 SDL2 在 PC 桌面打开窗口，并读取鼠标和键盘输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2764`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SIFLI_EPIC"></a>

## 20.70 `CONFIG_LV_USE_SIFLI_EPIC`

**提示（Prompt）**：SiFli EPIC 渲染器（Renderer）

**说明（Help）**

使用 SiFli BF0 SoC 的增强像素图像合成器（Enhanced Pixel Image Compositor，EPIC）引擎，加速混合（Blend）、填充（Fill）、图像和文本绘制。不支持的操作回退到软件渲染（Software Rendering）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_SW
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1008`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 增强像素图像合成器（EPIC）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)。

<a id="CONFIG_LV_USE_SIFLI_EPIC_ASSERT"></a>

## 20.71 `CONFIG_LV_USE_SIFLI_EPIC_ASSERT`

**提示（Prompt）**：断言（Asserts）

**说明（Help）**

检查每次 EPIC 调用的状态，失败时触发断言（Assert）。这对开发板初始调试（Bring-up）很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SIFLI_EPIC && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1027`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 增强像素图像合成器（EPIC） → SiFli EPIC 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SIFLI_EPIC`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SIFLI_EPIC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SIFLI_EPIC_DRAW_THREAD"></a>

## 20.72 `CONFIG_LV_USE_SIFLI_EPIC_DRAW_THREAD`

**提示（Prompt）**：绘制线程（Draw Thread）

**说明（Help）**

通过独立线程分派 EPIC 操作，使 CPU 能继续并行渲染。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_OS_NONE && CONFIG_LV_USE_SIFLI_EPIC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1019`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 增强像素图像合成器（EPIC） → SiFli EPIC 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_NONE`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_NONE)、[`CONFIG_LV_USE_SIFLI_EPIC`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SIFLI_EPIC)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SLIDER"></a>

## 20.73 `CONFIG_LV_USE_SLIDER`

**提示（Prompt）**：滑块（Slider）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_BAR
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2278`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_BAR`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_USE_BAR)。

<a id="CONFIG_LV_USE_SNAPSHOT"></a>

## 20.74 `CONFIG_LV_USE_SNAPSHOT`

**提示（Prompt）**：快照（Snapshot）

**说明（Help）**

通过 `lv_snapshot_take()` 将控件及其子对象渲染到图像缓冲区（Image Buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:440`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SPAN"></a>

## 20.75 `CONFIG_LV_USE_SPAN`

**提示（Prompt）**：文本片段（Span）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2283`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SPINBOX"></a>

## 20.76 `CONFIG_LV_USE_SPINBOX`

**提示（Prompt）**：数值微调框（Spinbox）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2292`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SPINNER"></a>

## 20.77 `CONFIG_LV_USE_SPINNER`

**提示（Prompt）**：加载指示器（Spinner）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2296`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_ST7735"></a>

## 20.78 `CONFIG_LV_USE_ST7735`

**提示（Prompt）**：ST7735 显示控制器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GENERIC_MIPI
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2492`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GENERIC_MIPI`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GENERIC_MIPI)。

<a id="CONFIG_LV_USE_ST7789"></a>

## 20.79 `CONFIG_LV_USE_ST7789`

**提示（Prompt）**：ST7789 显示控制器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GENERIC_MIPI
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2497`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GENERIC_MIPI`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GENERIC_MIPI)。

<a id="CONFIG_LV_USE_ST7796"></a>

## 20.80 `CONFIG_LV_USE_ST7796`

**提示（Prompt）**：ST7796 显示控制器

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_GENERIC_MIPI
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2502`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_GENERIC_MIPI`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_GENERIC_MIPI)。

<a id="CONFIG_LV_USE_ST_LTDC"></a>

## 20.81 `CONFIG_LV_USE_ST_LTDC`

**提示（Prompt）**：ST LCD-TFT 显示控制器（LTDC）

**说明（Help）**

创建绑定到 ST LTDC 外设某个图层（Layer）的显示器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2527`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SVG"></a>

## 20.82 `CONFIG_LV_USE_SVG`

**提示（Prompt）**：可缩放矢量图形（SVG）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_VECTOR_GRAPHIC
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1587`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_VECTOR_GRAPHIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_VECTOR_GRAPHIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_SVG_ANIMATION"></a>

## 20.83 `CONFIG_LV_USE_SVG_ANIMATION`

**提示（Prompt）**：SVG 动画（Animation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SVG && CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1593`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings） → 可缩放矢量图形（SVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SVG_DEBUG"></a>

## 20.84 `CONFIG_LV_USE_SVG_DEBUG`

**提示（Prompt）**：SVG 调试日志（Debug Logs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_SVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1596`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings） → 可缩放矢量图形（SVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_SVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SWITCH"></a>

## 20.85 `CONFIG_LV_USE_SWITCH`

**提示（Prompt）**：开关（Switch）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2300`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_SYSMON"></a>

## 20.86 `CONFIG_LV_USE_SYSMON`

**提示（Prompt）**：系统监测器（System Monitor）

**说明（Help）**

定期收集 CPU、每秒帧数（FPS）和内存统计信息，并可选择将它们显示在屏幕覆盖层（On-screen Overlay）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**被弱选择（Implied by）**

```text
CONFIG_LV_USE_DEMO_BENCHMARK
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3200`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 系统监测（System Monitoring）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DEMO_BENCHMARK`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_BENCHMARK)。

<a id="CONFIG_LV_USE_TABLE"></a>

## 20.87 `CONFIG_LV_USE_TABLE`

**提示（Prompt）**：表格（Table）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_FILE_EXPLORER
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2314`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_FILE_EXPLORER`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_FILE_EXPLORER)。

<a id="CONFIG_LV_USE_TABVIEW"></a>

## 20.88 `CONFIG_LV_USE_TABVIEW`

**提示（Prompt）**：选项卡视图（Tabview）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2318`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_TEST"></a>

## 20.89 `CONFIG_LV_USE_TEST`

**提示（Prompt）**：测试工具（Test Utilities）

**说明（Help）**

模拟输入设备（Emulated Input Devices）、时间模拟（Time Emulation）和截图比较（Screenshot Compare）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3420`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 测试工具（Test Utilities）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE"></a>

## 20.90 `CONFIG_LV_USE_TEST_SCREENSHOT_COMPARE`

**提示（Prompt）**：截图比较（Screenshot Compare）

**说明（Help）**

启用 `lv_test_screenshot_compare()`，需要额外几 MB RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_TEST && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_LODEPNG
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3427`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 调试（Debugging） → 测试工具（Test Utilities） → 测试工具（Test Utilities）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_TEST`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_TEST)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_LODEPNG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_LODEPNG)。

<a id="CONFIG_LV_USE_TEXTAREA"></a>

## 20.91 `CONFIG_LV_USE_TEXTAREA`

**提示（Prompt）**：文本区域（Text Area）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_LABEL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2304`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_LABEL`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_LABEL)。

<a id="CONFIG_LV_USE_TFT_ESPI"></a>

## 20.92 `CONFIG_LV_USE_TFT_ESPI`

**提示（Prompt）**：TFT_eSPI 显示库

**说明（Help）**

基于 TFT_eSPI Arduino 库的显示驱动（Display Driver）；构建中必须提供该库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2544`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_THEME_DEFAULT"></a>

## 20.93 `CONFIG_LV_USE_THEME_DEFAULT`

**提示（Prompt）**：默认主题（Default Theme）

**说明（Help）**

LVGL 演示和示例使用的完整功能主题（Full-featured Theme）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1482`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_THEME_MONO"></a>

## 20.94 `CONFIG_LV_USE_THEME_MONO`

**提示（Prompt）**：单色主题（Monochrome Theme）

**说明（Help）**

用于电子纸（E-paper）、点阵面板（Dot-matrix Panel）等 1 位显示器的样式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1509`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_THEME_SIMPLE"></a>

## 20.95 `CONFIG_LV_USE_THEME_SIMPLE`

**提示（Prompt）**：简单主题（Simple Theme）

**说明（Help）**

最小化样式（Minimal Styling），适合作为自定义主题（Custom Theme）的起点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1503`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 主题（Themes）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_THORVG"></a>

## 20.96 `CONFIG_LV_USE_THORVG`

**提示（Prompt）**：矢量图形引擎（Vector Graphics Engine，ThorVG）

**说明（Help）**

为软件渲染器（SW Renderer）提供矢量图形支持的后端（Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT if CONFIG_LV_USE_DRAW_SW
```

**被选择（Selected by）**

```text
CONFIG_LV_USE_VG_LITE_THORVG
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:446`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT)、[`CONFIG_LV_USE_DRAW_SW`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_SW)、[`CONFIG_LV_USE_VG_LITE_THORVG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_VG_LITE_THORVG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_DRAW_HAS_VECTOR_SUPPORT`。

<a id="CONFIG_LV_USE_THORVG_INTERNAL"></a>

## 20.97 `CONFIG_LV_USE_THORVG_INTERNAL`

**提示（Prompt）**：随附的 ThorVG（Bundled ThorVG）

**说明（Help）**

构建 LVGL 随附的 ThorVG 副本，而不链接外部版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_THORVG && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:453`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → 矢量图形引擎（Vector Graphics Engine，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_THORVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_THORVG)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_TILEVIEW"></a>

## 20.98 `CONFIG_LV_USE_TILEVIEW`

**提示（Prompt）**：平铺视图（Tileview）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2322`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_TINY_TTF"></a>

## 20.99 `CONFIG_LV_USE_TINY_TTF`

**提示（Prompt）**：Tiny TTF 字体引擎

**说明（Help）**

内置 TTF 解码器（Built-in Decoder）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1920`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 文本与字体设置（Text & Font Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_TJPGD"></a>

## 20.100 `CONFIG_LV_USE_TJPGD`

**提示（Prompt）**：JPEG 解码器（Decoder，TJpgDec）

**说明（Help）**

还可解码拆分 JPEG（Split JPEG），这是一种针对嵌入式系统优化的自定义格式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1574`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 图像设置（Image Settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<!-- kconfig-navigation -->

[上一章](P019_module_lvgl_zephyr_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P021_module_lvgl_zephyr_配置项参考_7.md)
