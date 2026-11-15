---
id: learning.zephyr-docs.kconfig-reference.page-21
title: "`<module:lvgl>/zephyr`配置项参考（7/7）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第21章\_`<module:lvgl>/zephyr`配置项参考（7/7）

本章翻译官方 Kconfig 数据库中 `<module:lvgl>/zephyr` 的 46 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_USE_TRANSLATION"></a>

## 21.1 `CONFIG_LV_USE_TRANSLATION`

**提示（Prompt）**：文本翻译（Text Translation）

**说明（Help）**

使用 `lv_translation_get()`，按 ID 查找所选语言的字符串。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1377`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 核心（Core）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_UEFI"></a>

## 21.2 `CONFIG_LV_USE_UEFI`

**提示（Prompt）**：统一可扩展固件接口（UEFI）

**说明（Help）**

UEFI 固件的显示和输入驱动，基于图形输出（Graphics Output）、键盘（Keyboard）和指针（Pointer）协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2891`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_UEFI_INCLUDE"></a>

## 21.3 `CONFIG_LV_USE_UEFI_INCLUDE`

**提示（Prompt）**：封装 UEFI 框架（EDK2、gnu-efi 等）的头文件（Header）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_UEFI && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"myefi.h"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2899`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → 统一可扩展固件接口（UEFI）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_UEFI`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_UEFI)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_VECTOR_GRAPHIC"></a>

## 21.4 `CONFIG_LV_USE_VECTOR_GRAPHIC`

**提示（Prompt）**：矢量图形（Vector Graphics）

**说明（Help）**

用于路径（Path）、描边（Stroke）和填充（Fill）的矢量绘制 API（`lv_vector_dsc_*`）。需要支持矢量的渲染器，例如配合 ThorVG 的软件渲染器，或 VG-Lite。

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
CONFIG_LV_USE_SVG
CONFIG_LV_USE_LOTTIE
CONFIG_LV_USE_DEMO_VECTOR_GRAPHIC
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:431`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_MATRIX`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_MATRIX)、[`CONFIG_LV_USE_SVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_SVG)、[`CONFIG_LV_USE_LOTTIE`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_LOTTIE)、[`CONFIG_LV_USE_DEMO_VECTOR_GRAPHIC`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DEMO_VECTOR_GRAPHIC)。

<a id="CONFIG_LV_USE_VG_LITE_DRIVER"></a>

## 21.5 `CONFIG_LV_USE_VG_LITE_DRIVER`

**提示（Prompt）**：内置 VG-Lite 驱动（Built-in Driver）

**说明（Help）**

构建 LVGL 随附的 VG-Lite 驱动，而不链接厂商提供的版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:692`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_VG_LITE_THORVG"></a>

## 21.6 `CONFIG_LV_USE_VG_LITE_THORVG`

**提示（Prompt）**：VG-Lite 模拟器（Simulator，ThorVG）

**说明（Help）**

使用 ThorVG 模拟 VG-Lite 硬件，以便在 PC 模拟器（Simulator）上调试和测试。需要内部或外部的 ThorVG 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_THORVG
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:733`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_THORVG`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_THORVG)。

<a id="CONFIG_LV_USE_WAYLAND"></a>

## 21.7 `CONFIG_LV_USE_WAYLAND`

**提示（Prompt）**：Wayland 显示协议

**说明（Help）**

在 Linux 或 BSD 的 Wayland 合成器（Compositor）中打开窗口，并读取鼠标、键盘和触摸输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2911`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_WIN"></a>

## 21.8 `CONFIG_LV_USE_WIN`

**提示（Prompt）**：窗口（Window）

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

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2326`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_WINDOWS"></a>

## 21.9 `CONFIG_LV_USE_WINDOWS`

**提示（Prompt）**：Windows 操作系统

**说明（Help）**

使用 Win32 API 打开窗口，并读取鼠标、触摸、键盘和鼠标滚轮输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_OS_WINDOWS && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2973`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LV_OS_WINDOWS`](P018_module_lvgl_zephyr_配置项参考_4.md#CONFIG_LV_OS_WINDOWS)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_USE_X11"></a>

## 21.10 `CONFIG_LV_USE_X11`

**提示（Prompt）**：X11 窗口系统

**说明（Help）**

在 X11 桌面打开窗口，并读取鼠标和键盘输入。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2979`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_BITMAP_FONT_CACHE_CNT"></a>

## 21.11 `CONFIG_LV_VG_LITE_BITMAP_FONT_CACHE_CNT`

**提示（Prompt）**：未对齐位图字体缓存大小（Unaligned Bitmap Font Cache Size，条目数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:668`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_DISABLE_BLIT_RECT_OFFSET"></a>

## 21.12 `CONFIG_LV_VG_LITE_DISABLE_BLIT_RECT_OFFSET`

**提示（Prompt）**：禁用块传送矩形偏移（Blit Rectangle Offset）

**说明（Help）**

规避某些 GPU 上的硬件错误（HW Error），代价是增加块传送（Blit）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:682`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_DISABLE_LINEAR_GRADIENT_EXT"></a>

## 21.13 `CONFIG_LV_VG_LITE_DISABLE_LINEAR_GRADIENT_EXT`

**提示（Prompt）**：禁用线性渐变扩展（Linear Gradient Extension）

**说明（Help）**

较旧的 VG-Lite 驱动没有实现此扩展，需要此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:676`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_DISABLE_VLC_OP_CLOSE"></a>

## 21.14 `CONFIG_LV_VG_LITE_DISABLE_VLC_OP_CLOSE`

**提示（Prompt）**：移除 `VLC_OP_CLOSE` 路径指令（Path Instruction，针对 NXP 的规避措施）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:672`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_FLUSH_MAX_COUNT"></a>

## 21.15 `CONFIG_LV_VG_LITE_FLUSH_MAX_COUNT`

**提示（Prompt）**：刷新触发阈值（Flush Trigger Threshold，绘制任务数）

**说明（Help）**

GPU 尝试在刷新（Flush）前批量积累此数量的绘制任务（Draw Task）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:644`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_GPU_GC255_0X40A"></a>

## 21.16 `CONFIG_LV_VG_LITE_GPU_GC255_0X40A`

**提示（Prompt）**：GC255，修订版（Revision）`0x40A`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:705`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GPU_GC355_0X0_1215"></a>

## 21.17 `CONFIG_LV_VG_LITE_GPU_GC355_0X0_1215`

**提示（Prompt）**：GC355，修订版（Revision）`0x0_1215`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:707`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GPU_GC355_0X0_1216"></a>

## 21.18 `CONFIG_LV_VG_LITE_GPU_GC355_0X0_1216`

**提示（Prompt）**：GC355，修订版（Revision）`0x0_1216`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:709`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GPU_GC555_0X423"></a>

## 21.19 `CONFIG_LV_VG_LITE_GPU_GC555_0X423`

**提示（Prompt）**：GC555，修订版（Revision）`0x423`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:711`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GPU_GC555_0X423_ECO"></a>

## 21.20 `CONFIG_LV_VG_LITE_GPU_GC555_0X423_ECO`

**提示（Prompt）**：GC555，修订版（Revision）`0x423 ECO`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:713`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GPU_GCNANOULTRAV_0X1003"></a>

## 21.21 `CONFIG_LV_VG_LITE_GPU_GCNANOULTRAV_0X1003`

**提示（Prompt）**：GCNanoUltraV，修订版（Revision）`0x1003`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:715`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver） → VG-Lite GPU 的系列与修订版（Series and Revision）

<a id="CONFIG_LV_VG_LITE_GRAD_CACHE_CNT"></a>

## 21.22 `CONFIG_LV_VG_LITE_GRAD_CACHE_CNT`

**提示（Prompt）**：渐变缓存大小（Gradient Cache Size，条目数）

**说明（Help）**

单个渐变（Gradient）的内存占用：线性渐变为 4K 字节，径向渐变为 `radius * 4K` 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:656`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_HAL_GPU_BASE_ADDRESS"></a>

## 21.23 `CONFIG_LV_VG_LITE_HAL_GPU_BASE_ADDRESS`

**提示（Prompt）**：GPU 基地址（Base Address）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_DRIVER && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0x40240000
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:728`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → 内置 VG-Lite 驱动（Built-in Driver）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_DRIVER`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_DRIVER)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_PATH_DUMP_MAX_LEN"></a>

## 21.24 `CONFIG_LV_VG_LITE_PATH_DUMP_MAX_LEN`

**提示（Prompt）**：最大路径转储长度（Maximum Path Dump Length，点数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:688`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_STROKE_CACHE_CNT"></a>

## 21.25 `CONFIG_LV_VG_LITE_STROKE_CACHE_CNT`

**提示（Prompt）**：描边缓存大小（Stroke Cache Size，条目数）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:664`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_16PIXELS_ALIGN"></a>

## 21.26 `CONFIG_LV_VG_LITE_THORVG_16PIXELS_ALIGN`

**提示（Prompt）**：16 像素对齐（16 Pixel Alignment）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:756`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_BUF_ADDR_ALIGN"></a>

## 21.27 `CONFIG_LV_VG_LITE_THORVG_BUF_ADDR_ALIGN`

**提示（Prompt）**：缓冲区地址对齐（Buffer Address Alignment，字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:760`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_LINEAR_GRADIENT_EXT_SUPPORT"></a>

## 21.28 `CONFIG_LV_VG_LITE_THORVG_LINEAR_GRADIENT_EXT_SUPPORT`

**提示（Prompt）**：线性渐变扩展（Linear Gradient Extension）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:752`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_LVGL_BLEND_SUPPORT"></a>

## 21.29 `CONFIG_LV_VG_LITE_THORVG_LVGL_BLEND_SUPPORT`

**提示（Prompt）**：LVGL 混合模式（Blend Modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:743`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_THREAD_RENDER"></a>

## 21.30 `CONFIG_LV_VG_LITE_THORVG_THREAD_RENDER`

**提示（Prompt）**：多线程渲染（Multi-threaded Rendering）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:764`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_THORVG_YUV_SUPPORT"></a>

## 21.31 `CONFIG_LV_VG_LITE_THORVG_YUV_SUPPORT`

**提示（Prompt）**：YUV 颜色格式（Color Formats）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_VG_LITE_THORVG && CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:748`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer） → VG-Lite 模拟器（Simulator，ThorVG）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_VG_LITE_THORVG`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_VG_LITE_THORVG)、[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_USE_ASSERT"></a>

## 21.32 `CONFIG_LV_VG_LITE_USE_ASSERT`

**提示（Prompt）**：断言（Assertions）

**说明（Help）**

使用 `LV_ASSERT()` 检查 VG-Lite 内部状态。调试时很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:638`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_USE_BOX_SHADOW"></a>

## 21.33 `CONFIG_LV_VG_LITE_USE_BOX_SHADOW`

**提示（Prompt）**：使用边框模拟盒阴影（Box Shadow）

**说明（Help）**

通常速度更快，但达不到软件渲染器（SW Renderer）的渲染质量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:650`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_VG_LITE_USE_GPU_INIT"></a>

## 21.34 `CONFIG_LV_VG_LITE_USE_GPU_INIT`

**提示（Prompt）**：自定义外部 `gpu_init()` 函数（Function）

**说明（Help）**

第一次使用 GPU 前，调用应用程序提供的 `gpu_init()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_DRAW_VG_LITE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:632`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 渲染配置（Rendering Configuration） → VG-Lite 图形引擎 → VG-Lite 渲染器（Renderer）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_VG_LITE`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_VG_LITE)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_WAYLAND_DIRECT_EXIT"></a>

## 21.35 `CONFIG_LV_WAYLAND_DIRECT_EXIT`

**提示（Prompt）**：关闭最后一个窗口时退出（Exit When the Last Window Closes）

**说明（Help）**

应用程序退出前，先反初始化（Deinitialize）LVGL。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_WAYLAND && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2919`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Wayland 显示协议

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_WAYLAND`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_WAYLAND)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_WAYLAND_USE_DMABUF"></a>

## 21.36 `CONFIG_LV_WAYLAND_USE_DMABUF`

**提示（Prompt）**：DMA 缓冲区后端（DMA-BUF Backend）

**说明（Help）**

通过线性 DMA-BUF 呈现软件渲染的帧，合成器（Compositor）可直接扫描输出（Scan Out）这些缓冲区，从而省去从共享内存复制的操作。要求合成器支持 `zwp_linux_dmabuf_v1`，GBM 实现能够分配 CPU 可映射的缓冲区，并需要 libdrm 和 gbm，通过 `-ldrm -lgbm` 链接。此方式不需要 GPU API；无法配合 OpenGL ES 和 NanoVG 渲染器使用，因为它们只能渲染到 GPU 表面（Surface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_DRAW_OPENGLES && !CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LV_USE_WAYLAND && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2935`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Wayland 显示协议

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_OPENGLES`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_WAYLAND`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_WAYLAND)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL`。

<a id="CONFIG_LV_WAYLAND_USE_EGL"></a>

## 21.37 `CONFIG_LV_WAYLAND_USE_EGL`

**提示（Prompt）**：EGL 后端（Backend，OpenGL ES 硬件加速）

**说明（Help）**

通过 OpenGL ES 2.0 和 EGL 进行硬件加速渲染（Hardware-accelerated Rendering），兼容 LVGL 3D/glTF 渲染。要求目标硬件支持 OpenGL ES 2.0，并通过 `-lwayland-egl` 链接 wayland-egl。对于 OpenGL ES 和 NanoVG 渲染器，这是唯一可用的后端（Backend）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_WAYLAND && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y if CONFIG_LV_USE_DRAW_OPENGLES || CONFIG_LV_USE_DRAW_NANOVG
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_EGL
CONFIG_LV_USE_OPENGLES
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2947`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Wayland 显示协议

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_WAYLAND`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_WAYLAND)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_OPENGLES`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_EGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_USE_EGL)、[`CONFIG_LV_USE_OPENGLES`](P020_module_lvgl_zephyr_配置项参考_6.md#CONFIG_LV_USE_OPENGLES)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_USE_EGL`。

<a id="CONFIG_LV_WAYLAND_USE_G2D"></a>

## 21.38 `CONFIG_LV_WAYLAND_USE_G2D`

**提示（Prompt）**：G2D，NXP i.MX 硬件加速器（Hardware Accelerator）

**说明（Help）**

通过 NXP G2D 引擎进行硬件加速二维渲染（Hardware-accelerated 2D Rendering）。支持已安装 G2D 库的 NXP i.MX6/i.MX8 平台。无法配合 OpenGL ES 和 NanoVG 渲染器使用，因为它们只能渲染到 GPU 表面（Surface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_DRAW_OPENGLES && !CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LV_USE_WAYLAND && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_LV_USE_DRAW_G2D
CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2958`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Wayland 显示协议

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_OPENGLES`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_WAYLAND`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_WAYLAND)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)、[`CONFIG_LV_USE_DRAW_G2D`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_G2D)、[`CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LV_WAYLAND_USE_DMABUF_PROTOCOL`。

<a id="CONFIG_LV_WAYLAND_USE_SHM"></a>

## 21.39 `CONFIG_LV_WAYLAND_USE_SHM`

**提示（Prompt）**：共享内存后端（SHM Backend）

**说明（Help）**

默认后端（Backend），使用 `wl_shm` 进行双缓冲直接渲染（Double-buffered Direct Rendering）。兼容所有 Wayland 合成器（Compositor），无需特殊硬件。无法配合 OpenGL ES 和 NanoVG 渲染器使用，因为它们只能渲染到 GPU 表面（Surface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LV_USE_DRAW_OPENGLES && !CONFIG_LV_USE_DRAW_NANOVG && CONFIG_LV_USE_WAYLAND && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2925`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → Wayland 显示协议

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_DRAW_OPENGLES`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_OPENGLES)、[`CONFIG_LV_USE_DRAW_NANOVG`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_DRAW_NANOVG)、[`CONFIG_LV_USE_WAYLAND`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_WAYLAND)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_WEDNESDAY_STR"></a>

## 21.40 `CONFIG_LV_WEDNESDAY_STR`

**提示（Prompt）**：星期三的缩写字符串（Shortened String for Wednesday）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_CALENDAR && CONFIG_LV_USE_CALENDAR && CONFIG_LVGL
```

**默认值（Defaults）**

```text
"We"
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2003`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets） → 日历（Calendar） → 星期名称配置（Days Name Configuration）

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_CALENDAR`](P019_module_lvgl_zephyr_配置项参考_5.md#CONFIG_LV_USE_CALENDAR)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_WIDGETS_HAS_DEFAULT_VALUE"></a>

## 21.41 `CONFIG_LV_WIDGETS_HAS_DEFAULT_VALUE`

**提示（Prompt）**：控件默认值（Default Values for Widgets）

**说明（Help）**

使以下控件（Widget）在创建时获得默认值：

- `lv_buttonmatrix_t`：使用默认映射 `{"Btn1", "Btn2", "Btn3", "\n", "Btn4", "Btn5", ""}`；否则不设置映射。
- `lv_checkbox_t`：字符串标签设为 `"Check box"`；否则设为空字符串。
- `lv_dropdown_t`：选项设为 `"Option 1"`、`"Option 2"`、`"Option 3"`；否则不设置值。
- `lv_roller_t`：选项设为 `"Option 1"`、`"Option 2"`、`"Option 3"`、`"Option 4"`、`"Option 5"`；否则不设置值。
- `lv_label_t`：文本设为 `"Text"`；否则为空字符串。
- `lv_arclabel_t`：文本设为 `"Arced Text"`；否则为空字符串。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:1940`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 控件（Widgets）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_X11_DIRECT_EXIT"></a>

## 21.42 `CONFIG_LV_X11_DIRECT_EXIT`

**提示（Prompt）**：关闭所有窗口时退出（Exit When All Windows Are Closed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_X11 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2990`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → X11 窗口系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_X11`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_X11)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_X11_DOUBLE_BUFFER"></a>

## 21.43 `CONFIG_LV_X11_DOUBLE_BUFFER`

**提示（Prompt）**：双缓冲（Double Buffering）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_USE_X11 && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2987`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → X11 窗口系统

**配置项引用（Symbol References）**：[`CONFIG_LV_USE_X11`](P021_module_lvgl_zephyr_配置项参考_7.md#CONFIG_LV_USE_X11)、[`CONFIG_LVGL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LVGL)。

<a id="CONFIG_LV_X11_RENDER_MODE_DIRECT"></a>

## 21.44 `CONFIG_LV_X11_RENDER_MODE_DIRECT`

**提示（Prompt）**：直接模式（Direct Mode）

**说明（Help）**

将内容渲染到屏幕大小缓冲区中的正确位置，使缓冲区始终保存完整图像，仅刷新变化区域。使用两个缓冲区时，它们的内容会自动保持同步，`flush_cb` 只需更改地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3002`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → X11 窗口系统 → 渲染模式（Render Mode）

<a id="CONFIG_LV_X11_RENDER_MODE_FULL"></a>

## 21.45 `CONFIG_LV_X11_RENDER_MODE_FULL`

**提示（Prompt）**：全屏模式（Full Mode）

**说明（Help）**

即使只有一个像素发生变化，也始终重绘整个屏幕。使用两个缓冲区时，`flush_cb` 只需更改地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:3007`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → X11 窗口系统 → 渲染模式（Render Mode）

<a id="CONFIG_LV_X11_RENDER_MODE_PARTIAL"></a>

## 21.46 `CONFIG_LV_X11_RENDER_MODE_PARTIAL`

**提示（Prompt）**：局部模式（Partial Mode）

**说明（Help）**

将屏幕拆成较小部分进行渲染，使缓冲区可以小于显示区域，从而节省 RAM。驱动使用的缓冲区大小约为屏幕大小的十分之一。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：`<module:lvgl>/zephyr/../Kconfig:2997`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `lvgl`（LVGL 图形库模块；工作区相对路径 `modules/lib/gui/lvgl`） → LVGL 图形库 → 驱动（Drivers） → X11 窗口系统 → 渲染模式（Render Mode）

<!-- kconfig-navigation -->

[上一章](P020_module_lvgl_zephyr_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P022_module_percepio_zephyr_配置项参考_1.md)
