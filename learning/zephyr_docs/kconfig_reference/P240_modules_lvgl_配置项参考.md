---
id: learning.zephyr-docs.kconfig-reference.page-240
title: "`modules/lvgl`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第240章\_`modules/lvgl`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/lvgl` 的 80 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APP_LINK_WITH_LVGL"></a>

## 240.1 `CONFIG_APP_LINK_WITH_LVGL`

**提示（Prompt）**：将应用目标 `app` 与 LVGL 链接（link）

**说明（Help）**

将 LVGL 头文件加入 `app` 的包含路径（include path）。如果 LVGL 的包含路径对 `app` 造成别名冲突（aliasing issues），可以禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LVGL"></a>

## 240.2 `CONFIG_LVGL`

**提示（Prompt）**：LVGL 支持（support）

**说明（Help）**

启用 LVGL 图形库（graphics library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`modules/lvgl/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

<a id="CONFIG_LV_COLOR_16_SWAP"></a>

## 240.3 `CONFIG_LV_COLOR_16_SWAP`

**提示（Prompt）**：交换 RGB565 颜色的两个字节（bytes）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/seeed_xiao_round_display/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_round_display/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/st7789v_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st7789v_generic/Kconfig.defconfig)。

```text
y if CONFIG_SHIELD_ST7789V_WAVESHARE_240X240
```

来源：[`boards/shields/waveshare_pico_lcd_1_14/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_pico_lcd_1_14/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ST7789V_WAVESHARE_240X240)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`。

<a id="CONFIG_LV_Z_AREA_X_ALIGNMENT_WIDTH"></a>

## 240.4 `CONFIG_LV_Z_AREA_X_ALIGNMENT_WIDTH`

**提示（Prompt）**：帧 X 轴对齐大小（Frame X alignment size）

**说明（Help）**

X 轴应取整对齐到的像素数（pixels）。用于覆盖当前帧尺寸（frame dimensions），以满足显示器或 LCD 主机控制器的要求。此值必须为 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
2
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_AREA_Y_ALIGNMENT_WIDTH"></a>

## 240.5 `CONFIG_LV_Z_AREA_Y_ALIGNMENT_WIDTH`

**提示（Prompt）**：帧 Y 轴对齐大小（Frame Y alignment size）

**说明（Help）**

Y 轴应取整对齐到的像素数（pixels）。用于覆盖当前帧尺寸（frame dimensions），以满足显示器或 LCD 主机控制器的要求。此值必须为 2 的幂。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
1
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
2
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_ATTRIBUTE_MEM_ALIGN_SIZE"></a>

## 240.6 `CONFIG_LV_Z_ATTRIBUTE_MEM_ALIGN_SIZE`

**提示（Prompt）**：内存对齐大小（Memory alignment size），单位为字节

**说明（Help）**

LVGL 缓冲区和常量数据（constant data）的对齐要求，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 256]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig)。

```text
4 if CONFIG_LV_Z_DRAW_DAVE2D
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig)。

```text
4 if CONFIG_LV_Z_DRAW_DAVE2D
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
4 if CONFIG_LV_Z_DRAW_DAVE2D
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig)。

```text
4 if CONFIG_LV_Z_DRAW_DAVE2D
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
4 if CONFIG_LV_Z_DRAW_DAVE2D
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_DRAW_DAVE2D`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DRAW_DAVE2D)。

<a id="CONFIG_LV_Z_AUTO_INIT"></a>

## 240.7 `CONFIG_LV_Z_AUTO_INIT`

**提示（Prompt）**：应用启动前初始化 LVGL

**说明（Help）**

在应用启动之前配置 LVGL 回调（callbacks）并初始化显示器。如果需要在初始化前更改显示器像素格式（pixel format），禁用此项可能有用。使用静态分配（static allocation）时，应确保 `LV_Z_BITS_PER_PIXEL` 设置正确。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**被弱选择（Implied by）**

```text
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE)。

<a id="CONFIG_LV_Z_BITS_PER_PIXEL"></a>

## 240.8 `CONFIG_LV_Z_BITS_PER_PIXEL`

**提示（Prompt）**：每像素位数（Bits per pixel）

**说明（Help）**

用于确定渲染缓冲区（render buffers）大小的每像素位数。`0` 表示使用 LVGL 默认颜色格式（`CONFIG_LV_COLOR_FORMAT_*`）的每像素位数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 32]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig)。

```text
24
```

来源：[`boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig)。

```text
1
```

来源：[`boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig)。

```text
24
```

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
32
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
32
```

来源：[`boards/shields/st7735r/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st7735r/Kconfig.defconfig)。

```text
16
```

来源：[`boards/shields/st7789v_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st7789v_generic/Kconfig.defconfig)。

```text
24 if CONFIG_SHIELD_ST7789V_TL019FQV01
```

来源：[`boards/shields/st7789v_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st7789v_generic/Kconfig.defconfig)。

```text
16 if CONFIG_SHIELD_ST7789V_WAVESHARE_240X240
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_SHIELD_ST7789V_TL019FQV01`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ST7789V_TL019FQV01)、[`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ST7789V_WAVESHARE_240X240)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_ST7789V_TL019FQV01`、`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`。

<a id="CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC"></a>

## 240.9 `CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC`

**提示（Prompt）**：动态（Dynamic）

**说明（Help）**

根据实际显示参数（display parameters）动态分配渲染缓冲区（rendering buffers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 渲染缓冲区分配（Rendering Buffer Allocation）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION)。

<a id="CONFIG_LV_Z_BUFFER_ALLOC_STATIC"></a>

## 240.10 `CONFIG_LV_Z_BUFFER_ALLOC_STATIC`

**提示（Prompt）**：静态（Static）

**说明（Help）**

根据以下配置参数静态分配渲染缓冲区（rendering buffers）：

- 水平屏幕分辨率（horizontal screen resolution）。
- 垂直屏幕分辨率（vertical screen resolution）。
- 渲染缓冲区大小（rendering buffer size）。
- 每像素字节数（bytes per pixel）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 渲染缓冲区分配（Rendering Buffer Allocation）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION)。

<a id="CONFIG_LV_Z_BUTTON_INPUT"></a>

## 240.11 `CONFIG_LV_Z_BUTTON_INPUT`

**提示（Prompt）**：LVGL 按钮输入（Input button）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && DT_HAS_ZEPHYR_LVGL_BUTTON_INPUT_ENABLED && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_BUTTON_INPUT_MSGQ_COUNT"></a>

## 240.12 `CONFIG_LV_Z_BUTTON_INPUT_MSGQ_COUNT`

**提示（Prompt）**：按钮输入队列消息数（button queue message count）

**说明（Help）**

用于缓冲输入事件（input events）的按钮消息队列（button message queue）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_BUTTON_INPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings） → LVGL 按钮输入（Input button）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_BUTTON_INPUT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUTTON_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_COLOR_FORMAT"></a>

## 240.13 `CONFIG_LV_Z_COLOR_FORMAT`

**提示（Prompt）**：SoC、开发板和扩展板的默认颜色格式（Default color format）

**说明（Help）**

LVGL `LV_COLOR_FORMAT_DEFAULT` 选项的默认值，由 SoC、开发板和扩展板（shields）在 `Kconfig.defconfig` 文件中设置。应用则应使用 `LV_COLOR_FORMAT_DEFAULT` 选择项（`CONFIG_LV_COLOR_FORMAT_*`）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_Z_COLOR_FORMAT_NONE
```

**可选项（Choices）**

```text
CONFIG_LV_Z_COLOR_FORMAT_NONE
CONFIG_LV_Z_COLOR_FORMAT_I1
CONFIG_LV_Z_COLOR_FORMAT_L8
CONFIG_LV_Z_COLOR_FORMAT_RGB565
CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED
CONFIG_LV_Z_COLOR_FORMAT_RGB888
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
CONFIG_LV_Z_COLOR_FORMAT_ARGB8888
CONFIG_LV_Z_COLOR_FORMAT_NONE
CONFIG_LV_Z_COLOR_FORMAT_I1
CONFIG_LV_Z_COLOR_FORMAT_L8
CONFIG_LV_Z_COLOR_FORMAT_RGB565
CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED
CONFIG_LV_Z_COLOR_FORMAT_RGB888
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
CONFIG_LV_Z_COLOR_FORMAT_ARGB8888
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/ls0xx_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ls0xx_generic/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/m5stack_unit_minioled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/m5stack_unit_minioled/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/ssd1306/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ssd1306/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/st7789v_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st7789v_generic/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_RGB565 if CONFIG_SHIELD_ST7789V_WAVESHARE_240X240
```

来源：[`boards/shields/waveshare_dsi_lcd/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_dsi_lcd/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_XRGB8888
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

来源：[`boards/shields/waveshare_pico_oled_1_3/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_pico_oled_1_3/Kconfig.defconfig)。

```text
CONFIG_LV_Z_COLOR_FORMAT_I1
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_COLOR_FORMAT_NONE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_NONE)、[`CONFIG_LV_Z_COLOR_FORMAT_I1`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_I1)、[`CONFIG_LV_Z_COLOR_FORMAT_L8`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_L8)、[`CONFIG_LV_Z_COLOR_FORMAT_RGB565`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_RGB565)、[`CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED)、[`CONFIG_LV_Z_COLOR_FORMAT_RGB888`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_RGB888)、[`CONFIG_LV_Z_COLOR_FORMAT_XRGB8888`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_XRGB8888)、[`CONFIG_LV_Z_COLOR_FORMAT_ARGB8888`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT_ARGB8888)、[`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_ST7789V_WAVESHARE_240X240)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_ST7789V_WAVESHARE_240X240`。

<a id="CONFIG_LV_Z_COLOR_FORMAT_ARGB8888"></a>

## 240.14 `CONFIG_LV_Z_COLOR_FORMAT_ARGB8888`

**提示（Prompt）**：ARGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_I1"></a>

## 240.15 `CONFIG_LV_Z_COLOR_FORMAT_I1`

**提示（Prompt）**：I1：每像素 1 位，单色（monochrome）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_L8"></a>

## 240.16 `CONFIG_LV_Z_COLOR_FORMAT_L8`

**提示（Prompt）**：L8：8 位灰度（grayscale）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_NONE"></a>

## 240.17 `CONFIG_LV_Z_COLOR_FORMAT_NONE`

**提示（Prompt）**：无开发板默认值（No board default）

**说明（Help）**

保留 LVGL 模块默认的颜色格式（color format）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_RGB565"></a>

## 240.18 `CONFIG_LV_Z_COLOR_FORMAT_RGB565`

**提示（Prompt）**：RGB565 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED"></a>

## 240.19 `CONFIG_LV_Z_COLOR_FORMAT_RGB565_SWAPPED`

**提示（Prompt）**：RGB565：大端序（big-endian）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_RGB888"></a>

## 240.20 `CONFIG_LV_Z_COLOR_FORMAT_RGB888`

**提示（Prompt）**：RGB888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_FORMAT_XRGB8888"></a>

## 240.21 `CONFIG_LV_Z_COLOR_FORMAT_XRGB8888`

**提示（Prompt）**：XRGB8888 颜色格式（Color Format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_COLOR_FORMAT>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → SoC、开发板和扩展板的默认颜色格式（Default color format）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_COLOR_FORMAT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_COLOR_FORMAT)。

<a id="CONFIG_LV_Z_COLOR_MONO_HW_INVERSION"></a>

## 240.22 `CONFIG_LV_Z_COLOR_MONO_HW_INVERSION`

**提示（Prompt）**：硬件像素反转（Hardware pixel inversion），同时禁用软件像素反转。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/m5stack_unit_minioled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/m5stack_unit_minioled/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/ssd1306/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ssd1306/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DIRECT_RENDERING"></a>

## 240.23 `CONFIG_LV_Z_DIRECT_RENDERING`

**提示（Prompt）**：直接渲染模式（Direct Rendering Mode）

**说明（Help）**

缓冲区大小必须与显示器大小一致。LVGL 在缓冲区的正确位置进行渲染，使缓冲区始终包含完整显示图像。如果使用两个缓冲区，刷新（flushing）后会自动将已渲染区域复制到另一缓冲区。此模式可同时获得零复制（zero copying，`LV_Z_FULL_REFRESH` 也支持）和局部重绘（partial redraws，与 `LV_Z_PARTIAL_REFRESH` 相同）的性能收益。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_RENDERING_MODE>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 渲染模式（Rendering Mode）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RENDERING_MODE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RENDERING_MODE)。

<a id="CONFIG_LV_Z_DOUBLE_VDB"></a>

## 240.24 `CONFIG_LV_Z_DOUBLE_VDB`

**提示（Prompt）**：使用两个渲染缓冲区（rendering buffers）

**说明（Help）**

使用两个缓冲区并行渲染并刷新（render and flush）数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/lcd_par_s035/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig)。

```text
y
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig)。

```text
y
```

来源：[`boards/shields/waveshare_dsi_lcd/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_dsi_lcd/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DPI_DEF"></a>

## 240.25 `CONFIG_LV_Z_DPI_DEF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_DPI_DEF` 的开发板默认值。`0` 保留 LVGL 默认值。应用应改为设置 `CONFIG_LV_DPI_DEF`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig)。

```text
148
```

来源：[`boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig)。

```text
116
```

来源：[`boards/shields/arduino_giga_display_shield/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/arduino_giga_display_shield/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/g1120b0mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/ls0xx_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ls0xx_generic/Kconfig.defconfig)。

```text
150
```

来源：[`boards/shields/m5stack_unit_minioled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/m5stack_unit_minioled/Kconfig.defconfig)。

```text
185
```

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
128
```

来源：[`boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig)。

```text
148
```

来源：[`boards/shields/ssd1306/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ssd1306/Kconfig.defconfig)。

```text
116 if CONFIG_SHIELD_SH1106_128X64
```

来源：[`boards/shields/ssd1306/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ssd1306/Kconfig.defconfig)。

```text
148
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
188 if CONFIG_SHIELD_WAVESHARE_EPAPER_GDEH0154A07
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
120 if CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW042T2
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
130
```

来源：[`boards/shields/waveshare_pico_lcd_1_14/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_pico_lcd_1_14/Kconfig.defconfig)。

```text
242
```

来源：[`boards/shields/waveshare_pico_oled_1_3/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_pico_oled_1_3/Kconfig.defconfig)。

```text
110
```

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
128
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_SHIELD_SH1106_128X64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_SH1106_128X64)、[`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEH0154A07`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_WAVESHARE_EPAPER_GDEH0154A07)、[`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW042T2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW042T2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_SH1106_128X64`、`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEH0154A07`、`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW042T2`。

<a id="CONFIG_LV_Z_DRAW_BUF_ALIGN"></a>

## 240.26 `CONFIG_LV_Z_DRAW_BUF_ALIGN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_DRAW_BUF_ALIGN` 的开发板默认值。`0` 保留 LVGL 默认值。应用应改为设置 `CONFIG_LV_DRAW_BUF_ALIGN`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DRAW_DAVE2D"></a>

## 240.27 `CONFIG_LV_Z_DRAW_DAVE2D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 LVGL Dave2D 渲染器（renderer，`CONFIG_LV_USE_DRAW_DAVE2D`）时设置此项，并启用其使用的瑞萨（Renesas）DRW 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**弱选择（Implies）**

```text
CONFIG_RENESAS_DRW
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_RENESAS_DRW`](P123_drivers_misc_配置项参考.md#CONFIG_RENESAS_DRW)。

<a id="CONFIG_LV_Z_DRAW_DMA2D"></a>

## 240.28 `CONFIG_LV_Z_DRAW_DMA2D`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 LVGL DMA2D 渲染器（renderer，`CONFIG_LV_USE_DRAW_DMA2D`）时设置此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DRAW_DMA2D_DEFAULT"></a>

## 240.29 `CONFIG_LV_Z_DRAW_DMA2D_DEFAULT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_USE_DRAW_DMA2D` 的开发板默认值。应用应改为设置 `CONFIG_LV_USE_DRAW_DMA2D`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DRAW_DMA2D_HAL_INCLUDE"></a>

## 240.30 `CONFIG_LV_Z_DRAW_DMA2D_HAL_INCLUDE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_DRAW_DMA2D_HAL_INCLUDE` 的 SoC 默认值，指定目标处理器的 CMSIS 头文件，例如 `stm32f769xx.h` 或 `stm32f429xx.h`。留空时保留 LVGL 默认值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_DRAW_DMA2D && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_DRAW_DMA2D`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DRAW_DMA2D)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DRAW_DMA2D_INTERRUPT"></a>

## 240.31 `CONFIG_LV_Z_DRAW_DMA2D_INTERRUPT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_USE_DRAW_DMA2D_INTERRUPT` 的 SoC 默认值。应用应改为设置 `CONFIG_LV_USE_DRAW_DMA2D_INTERRUPT`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_DRAW_DMA2D && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_DRAW_DMA2D`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DRAW_DMA2D)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_DRAW_PXP"></a>

## 240.32 `CONFIG_LV_Z_DRAW_PXP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 LVGL PXP 渲染器（renderer，`CONFIG_LV_USE_DRAW_PXP`）时设置此项，并启用其使用的 NXP PXP 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_ENCODER_INPUT"></a>

## 240.33 `CONFIG_LV_Z_ENCODER_INPUT`

**提示（Prompt）**：LVGL 编码器输入（Input encoder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && DT_HAS_ZEPHYR_LVGL_ENCODER_INPUT_ENABLED && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_ENCODER_INPUT_MSGQ_COUNT"></a>

## 240.34 `CONFIG_LV_Z_ENCODER_INPUT_MSGQ_COUNT`

**提示（Prompt）**：编码器输入队列消息数（encoder queue message count）

**说明（Help）**

用于缓冲输入事件（input events）的编码器消息队列（encoder message queue）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_ENCODER_INPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings） → LVGL 编码器输入（Input encoder）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_ENCODER_INPUT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_ENCODER_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_FLUSH_THREAD"></a>

## 240.35 `CONFIG_LV_Z_FLUSH_THREAD`

**提示（Prompt）**：在独立线程中刷新 LVGL 帧（Flush frames）

**说明（Help）**

在独立线程中刷新 LVGL 帧，同时由主线程渲染下一帧。如果不需要此方式带来的性能收益，可以禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/arduino_giga_display_shield/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/arduino_giga_display_shield/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/g1120b0mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/Kconfig.defconfig)。

```text
n
```

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_FLUSH_THREAD_PRIORITY"></a>

## 240.36 `CONFIG_LV_Z_FLUSH_THREAD_PRIORITY`

**提示（Prompt）**：LVGL 刷新线程优先级（flush thread priority）

**说明（Help）**

LVGL 刷新线程（flush thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_FLUSH_THREAD && CONFIG_LVGL
```

**默认值（Defaults）**

```text
-1
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 在独立线程中刷新 LVGL 帧（Flush frames）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_FLUSH_THREAD`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_FLUSH_THREAD)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_FLUSH_THREAD_STACK_SIZE"></a>

## 240.37 `CONFIG_LV_Z_FLUSH_THREAD_STACK_SIZE`

**提示（Prompt）**：刷新线程栈大小（flushing thread stack size）

**说明（Help）**

LVGL 刷新线程（flush thread）的栈大小，该线程将调用 `display_write`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_FLUSH_THREAD && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 在独立线程中刷新 LVGL 帧（Flush frames）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_FLUSH_THREAD`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_FLUSH_THREAD)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_FULL_REFRESH"></a>

## 240.38 `CONFIG_LV_Z_FULL_REFRESH`

**提示（Prompt）**：强制全屏刷新模式（Force Full Refresh Mode）

**说明（Help）**

更新时强制刷新整个显示器。即使只更改了 1 个像素，LVGL 也始终重绘全屏。与 `LV_Z_VDB_SIZE` 结合使用时，对于要求系统内存中存在帧缓冲区（framebuffer）的显示控制器，此设置可提高性能，因为控制器可以直接渲染 LVGL 帧缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_RENDERING_MODE>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 渲染模式（Rendering Mode）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RENDERING_MODE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RENDERING_MODE)。

<a id="CONFIG_LV_Z_INIT_PRIORITY"></a>

## 240.39 `CONFIG_LV_Z_INIT_PRIORITY`

**提示（Prompt）**：LVGL 默认初始化优先级（Default init priority）

**说明（Help）**

LVGL 自动初始化（automatic initialization）使用的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_AUTO_INIT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
90
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 应用启动前初始化 LVGL

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_AUTO_INIT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_AUTO_INIT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_KEYPAD_INPUT"></a>

## 240.40 `CONFIG_LV_Z_KEYPAD_INPUT`

**提示（Prompt）**：LVGL 键盘输入（Input keypad）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && DT_HAS_ZEPHYR_LVGL_KEYPAD_INPUT_ENABLED && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_KEYPAD_INPUT_MSGQ_COUNT"></a>

## 240.41 `CONFIG_LV_Z_KEYPAD_INPUT_MSGQ_COUNT`

**提示（Prompt）**：键盘输入队列消息数（keypad queue message count）

**说明（Help）**

用于缓冲输入事件（input events）的键盘消息队列（keypad message queue）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_KEYPAD_INPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings） → LVGL 键盘输入（Input keypad）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_KEYPAD_INPUT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_KEYPAD_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_LVGL_MUTEX"></a>

## 240.42 `CONFIG_LV_Z_LVGL_MUTEX`

**提示（Prompt）**：提供 LVGL API 互斥锁加锁／解锁函数（mutex locking/unlocking functions）

**说明（Help）**

LVGL API 函数不具备线程安全性（thread safety），此项提供加锁和解锁函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**被弱选择（Implied by）**

```text
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE)。

<a id="CONFIG_LV_Z_LVGL_WORKQUEUE_PRIORITY"></a>

## 240.43 `CONFIG_LV_Z_LVGL_WORKQUEUE_PRIORITY`

**提示（Prompt）**：LVGL 工作队列优先级（workqueue priority）

**说明（Help）**

LVGL 专用工作队列（dedicated workqueue）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 使用专用工作队列（dedicated workqueue）运行 LVGL 核心

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_LVGL_WORKQUEUE_STACK_SIZE"></a>

## 240.44 `CONFIG_LV_Z_LVGL_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：LVGL 工作队列栈大小（workqueue stack size）

**说明（Help）**

LVGL 专用工作队列（dedicated workqueue）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 使用专用工作队列（dedicated workqueue）运行 LVGL 核心

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MAX_MONKEY_COUNT"></a>

## 240.45 `CONFIG_LV_Z_MAX_MONKEY_COUNT`

**提示（Prompt）**：最大猴子测试实例数（monkeys）

**说明（Help）**

可同时存在的猴子测试（monkey test）实例数量。仅在启用 LVGL 猴子测试（`LV_USE_MONKEY`）时使用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_SHELL && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.shell:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.shell#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 命令行（Shell）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_SHELL`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_SHELL)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MEMORY_POOL"></a>

## 240.46 `CONFIG_LV_Z_MEMORY_POOL`

**提示（Prompt）**：内存池（Memory pool）

**说明（Help）**

用于 LVGL 所分配对象的内存池（memory pool）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_Z_MEM_POOL_SYS_HEAP
```

**可选项（Choices）**

```text
CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C
CONFIG_LV_Z_MEM_POOL_SYS_HEAP
CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C
CONFIG_LV_Z_MEM_POOL_SYS_HEAP
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_MEM_POOL_SYS_HEAP`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEM_POOL_SYS_HEAP)、[`CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C)。

<a id="CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION"></a>

## 240.47 `CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION`

**提示（Prompt）**：将内存池链接到自定义段（custom section）

**说明（Help）**

将 LVGL 内存池（memory pool）放在标记为 `.lvgl_heap` 的自定义段中。自定义链接器脚本（linker scripts）可据此将内存池重定位到特定位置，例如紧耦合存储器（tightly coupled memory）或外部内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_MEM_POOL_SYS_HEAP && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_MEM_POOL_SYS_HEAP`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEM_POOL_SYS_HEAP)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION"></a>

## 240.48 `CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION`

**提示（Prompt）**：将 LVGL 内存池放在 Zephyr 内存区域（memory-region）中

**说明（Help）**

将 LVGL 内存池放在根据兼容 `zephyr,memory-region` 的节点自动创建的段中；区域名称由 `LV_Z_MEMORY_POOL_ZEPHYR_REGION_NAME` 指定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_MEM_POOL_SYS_HEAP && !CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_MEM_POOL_SYS_HEAP`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEM_POOL_SYS_HEAP)、[`CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEMORY_POOL_CUSTOM_SECTION)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION_NAME"></a>

## 240.49 `CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION_NAME`

**提示（Prompt）**：内存池使用的 Zephyr 内存区域（Memory-region）名称

**说明（Help）**

放置 LVGL 内存池的 Zephyr 内存区域（memory-region）名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 将 LVGL 内存池放在 Zephyr 内存区域（memory-region）中

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEMORY_POOL_ZEPHYR_REGION)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C"></a>

## 240.50 `CONFIG_LV_Z_MEM_POOL_HEAP_LIB_C`

**提示（Prompt）**：C 库堆（C library Heap）

**说明（Help）**

使用 C 库的 `malloc` 和 `free`，在 C 库堆（heap）上分配对象。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_MINIMAL_LIBC || CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE != 0) && <choice CONFIG_LV_Z_MEMORY_POOL>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 内存池（Memory pool）

**配置项引用（Symbol References）**：[`CONFIG_MINIMAL_LIBC`](P197_lib_配置项参考_1.md#CONFIG_MINIMAL_LIBC)、[`CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE)、[`CONFIG_LV_Z_MEMORY_POOL`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEMORY_POOL)。

<a id="CONFIG_LV_Z_MEM_POOL_SIZE"></a>

## 240.51 `CONFIG_LV_Z_MEM_POOL_SIZE`

**提示（Prompt）**：内存池大小（Memory pool size）

**说明（Help）**

内存池（memory pool）大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_MEM_POOL_SYS_HEAP && CONFIG_LVGL
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_MEM_POOL_SYS_HEAP`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEM_POOL_SYS_HEAP)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_MEM_POOL_SYS_HEAP"></a>

## 240.52 `CONFIG_LV_Z_MEM_POOL_SYS_HEAP`

**提示（Prompt）**：用户空间 LVGL 池（User space lvgl pool）

**说明（Help）**

使用私有系统堆（private sys heap）提供的专用内存池（dedicated memory pool）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_MEMORY_POOL>
```

**主动选择（Selects）**

```text
CONFIG_SYS_HEAP_INFO
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 内存池（Memory pool）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_MEMORY_POOL`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_MEMORY_POOL)、[`CONFIG_SYS_HEAP_INFO`](P199_lib_配置项参考_3.md#CONFIG_SYS_HEAP_INFO)。

<a id="CONFIG_LV_Z_MONOCHROME_CONVERSION_BUFFER"></a>

## 240.53 `CONFIG_LV_Z_MONOCHROME_CONVERSION_BUFFER`

**提示（Prompt）**：为单色显示器使用中间转换缓冲区（intermediate conversion buffer）

**说明（Help）**

使用单色显示器（monochrome display）时，需要大小由 `LV_Z_VDB_SIZE` 指定的中间缓冲区来执行转换（conversion）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_CACHE_HAL_INCLUDE"></a>

## 240.54 `CONFIG_LV_Z_NEMA_CACHE_HAL_INCLUDE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_NEMA_CACHE_HAL_INCLUDE` 的开发板默认值，指定提供 NemaGFX 渲染器所用 CMSIS 数据缓存维护函数（data cache maintenance functions）的头文件。留空时保留 LVGL 默认值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_USE_NEMA_GFX && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_GFX_MULTI_THREAD"></a>

## 240.55 `CONFIG_LV_Z_NEMA_GFX_MULTI_THREAD`

**提示（Prompt）**：NemaGFX 多线程支持（Multi-thread support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_USE_NEMA_GFX && CONFIG_LV_Z_NEMA_HAL_CUSTOM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)、[`CONFIG_LV_Z_NEMA_HAL_CUSTOM`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_NEMA_HAL_CUSTOM)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_HAL_CUSTOM"></a>

## 240.56 `CONFIG_LV_Z_NEMA_HAL_CUSTOM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

LVGL NemaGFX 硬件抽象层（HAL）选择为自定义（`CONFIG_LV_NEMA_HAL_CUSTOM`）时设置此项，此时使用 Zephyr NemaGFX HAL。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_USE_NEMA_GFX && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_HAL_RING_SIZE"></a>

## 240.57 `CONFIG_LV_Z_NEMA_HAL_RING_SIZE`

**提示（Prompt）**：NemaGFX 环大小（ring size）

**说明（Help）**

NemaGFX 命令环（command ring）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_USE_NEMA_GFX && CONFIG_LV_Z_NEMA_HAL_CUSTOM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)、[`CONFIG_LV_Z_NEMA_HAL_CUSTOM`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_NEMA_HAL_CUSTOM)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_LIB_M33_NEMAPVG"></a>

## 240.58 `CONFIG_LV_Z_NEMA_LIB_M33_NEMAPVG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

LVGL NemaGFX 库选择项的开发板默认值：`CONFIG_LV_NEMA_LIB_M33_NEMAPVG`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_LIB_M33_REVC"></a>

## 240.59 `CONFIG_LV_Z_NEMA_LIB_M33_REVC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

LVGL NemaGFX 库选择项的开发板默认值：`CONFIG_LV_NEMA_LIB_M33_REVC`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_LIB_M55"></a>

## 240.60 `CONFIG_LV_Z_NEMA_LIB_M55`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

LVGL NemaGFX 库选择项的开发板默认值：`CONFIG_LV_NEMA_LIB_M55`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_LIB_M7"></a>

## 240.61 `CONFIG_LV_Z_NEMA_LIB_M7`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

LVGL NemaGFX 库选择项的开发板默认值：`CONFIG_LV_NEMA_LIB_M7`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_NEMA_USE_CACHE"></a>

## 240.62 `CONFIG_LV_Z_NEMA_USE_CACHE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

`CONFIG_LV_NEMA_USE_CACHE` 的开发板默认值。应用应改为设置 `CONFIG_LV_NEMA_USE_CACHE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_USE_NEMA_GFX && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_USE_NEMA_GFX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_USE_NEMA_GFX)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_PARTIAL_REFRESH"></a>

## 240.63 `CONFIG_LV_Z_PARTIAL_REFRESH`

**提示（Prompt）**：局部刷新模式（Partial Refresh Mode）

**说明（Help）**

使用小于显示器大小的缓冲区（buffers）进行显示渲染，建议至少使用显示器大小的 1/10。在刷新回调（Flush Callback）中，需要将渲染后的图像复制到显示器指定区域。此模式下，按下按钮时只重绘按钮所在区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_RENDERING_MODE>
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 渲染模式（Rendering Mode）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_RENDERING_MODE`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_RENDERING_MODE)。

<a id="CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH"></a>

## 240.64 `CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH`

**提示（Prompt）**：根据设备树 `zephyr,touch` chosen 设备创建 LVGL 指针（pointer）

**说明（Help）**

启用根据设备树（devicetree）的 `zephyr,touch` chosen 属性创建 LVGL 指针输入设备（pointer input device）的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

<a id="CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH_INFER_DISPLAY"></a>

## 240.65 `CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH_INFER_DISPLAY`

**提示（Prompt）**：将指针输入关联到 chosen 显示器（chosen display）

**说明（Help）**

处理根据 `zephyr,touch` chosen 属性创建的指针设备（pointer device）的输入事件，并将其关联到 `zephyr,display` chosen 设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

<a id="CONFIG_LV_Z_POINTER_INPUT"></a>

## 240.66 `CONFIG_LV_Z_POINTER_INPUT`

**提示（Prompt）**：LVGL 指针输入（Input pointer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_INPUT && (DT_HAS_ZEPHYR_LVGL_POINTER_INPUT_ENABLED || CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH) && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings）

**配置项引用（Symbol References）**：[`CONFIG_INPUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT)、[`CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_POINTER_FROM_CHOSEN_TOUCH)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_POINTER_INPUT_MSGQ_COUNT"></a>

## 240.67 `CONFIG_LV_Z_POINTER_INPUT_MSGQ_COUNT`

**提示（Prompt）**：指针输入队列消息数（pointer queue message count）

**说明（Help）**

用于缓冲输入事件（input events）的指针消息队列（pointer message queue）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_POINTER_INPUT && CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_INPUT_QUEUE_MAX_MSGS if CONFIG_INPUT_MODE_THREAD
10
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.input:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.input#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 输入设备设置（Input device settings） → LVGL 指针输入（Input pointer）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_POINTER_INPUT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_POINTER_INPUT)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_INPUT_QUEUE_MAX_MSGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_QUEUE_MAX_MSGS)、[`CONFIG_INPUT_MODE_THREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_INPUT_MODE_THREAD)。

<a id="CONFIG_LV_Z_PXP_INTERRUPT_PRIORITY"></a>

## 240.68 `CONFIG_LV_Z_PXP_INTERRUPT_PRIORITY`

**提示（Prompt）**：PXP 中断优先级（interrupt priority）

**说明（Help）**

设置 PXP 中断优先级（interrupt priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_DRAW_PXP && CONFIG_LVGL
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:233`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L233)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_DRAW_PXP`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DRAW_PXP)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION"></a>

## 240.69 `CONFIG_LV_Z_RENDERING_BUFFER_ALLOCATION`

**提示（Prompt）**：渲染缓冲区分配（Rendering Buffer Allocation）

**说明（Help）**

分配渲染缓冲区（rendering buffers）时应使用的分配类型（allocation type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_Z_BUFFER_ALLOC_STATIC
```

**可选项（Choices）**

```text
CONFIG_LV_Z_BUFFER_ALLOC_STATIC
CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC
CONFIG_LV_Z_BUFFER_ALLOC_STATIC
CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_BUFFER_ALLOC_STATIC`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUFFER_ALLOC_STATIC)、[`CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUFFER_ALLOC_DYNAMIC)。

<a id="CONFIG_LV_Z_RENDERING_MODE"></a>

## 240.70 `CONFIG_LV_Z_RENDERING_MODE`

**提示（Prompt）**：渲染模式（Rendering Mode）

**说明（Help）**

选择 LVGL 的渲染模式（rendering mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
CONFIG_LV_Z_PARTIAL_REFRESH
```

**可选项（Choices）**

```text
CONFIG_LV_Z_PARTIAL_REFRESH
CONFIG_LV_Z_DIRECT_RENDERING
CONFIG_LV_Z_FULL_REFRESH
CONFIG_LV_Z_PARTIAL_REFRESH
CONFIG_LV_Z_DIRECT_RENDERING
CONFIG_LV_Z_FULL_REFRESH
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx8_dsi_oled1a/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_mx9_dsi_oled/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rk055hdmipi4m/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4m/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rk055hdmipi4ma0/boards/mimxrt1160_evk_mimxrt1166_cm7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/boards/mimxrt1160_evk_mimxrt1166_cm7.defconfig)。

```text
CONFIG_LV_Z_PARTIAL_REFRESH
```

来源：[`boards/shields/rk055hdmipi4ma0/boards/mimxrt1170_evk_mimxrt1176_cm7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/boards/mimxrt1170_evk_mimxrt1176_cm7.defconfig)。

```text
CONFIG_LV_Z_PARTIAL_REFRESH
```

来源：[`boards/shields/rk055hdmipi4ma0/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.defconfig)。

```text
CONFIG_LV_Z_PARTIAL_REFRESH
```

来源：[`boards/shields/rk055hdmipi4ma0/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk055hdmipi4ma0/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rtklcdpar1s00001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/rtkmipilcdb00000be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

来源：[`boards/shields/waveshare_dsi_lcd/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_dsi_lcd/Kconfig.defconfig)。

```text
CONFIG_LV_Z_FULL_REFRESH
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_PARTIAL_REFRESH`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_PARTIAL_REFRESH)、[`CONFIG_LV_Z_DIRECT_RENDERING`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DIRECT_RENDERING)、[`CONFIG_LV_Z_FULL_REFRESH`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_FULL_REFRESH)。

<a id="CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE"></a>

## 240.71 `CONFIG_LV_Z_RUN_LVGL_ON_WORKQUEUE`

**提示（Prompt）**：使用专用工作队列（dedicated workqueue）运行 LVGL 核心

**说明（Help）**

自动在独立工作队列（workqueue）中运行 LVGL，用户无需为此添加定时循环（timed loop）。如果应用负责周期性调用 LV 定时器，可禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**弱选择（Implies）**

```text
CONFIG_LV_Z_AUTO_INIT
CONFIG_LV_Z_LVGL_MUTEX
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_AUTO_INIT`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_AUTO_INIT)、[`CONFIG_LV_Z_LVGL_MUTEX`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_LVGL_MUTEX)。

<a id="CONFIG_LV_Z_SHELL"></a>

## 240.72 `CONFIG_LV_Z_SHELL`

**提示（Prompt）**：LVGL 命令行（Shell）

**说明（Help）**

启用 LVGL 命令行（shell）用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.shell:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.shell#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_USE_FILESYSTEM"></a>

## 240.73 `CONFIG_LV_Z_USE_FILESYSTEM`

**提示（Prompt）**：LVGL 文件系统支持（file system support）

**说明（Help）**

启用 LittlevGL 文件系统（file system）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && CONFIG_LVGL
```

**默认值（Defaults）**

```text
y if CONFIG_FILE_SYSTEM
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_USE_NEMA_GFX"></a>

## 240.74 `CONFIG_LV_Z_USE_NEMA_GFX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 LVGL NemaGFX 渲染器（renderer，`CONFIG_LV_USE_NEMA_GFX`）时设置此项，并启用其使用的 NeoChrom 图形处理器（GPU）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_NEOCHROM_GPU2D_ENABLED && CONFIG_LVGL
```

**主动选择（Selects）**

```text
CONFIG_STM32_NEOCHROM_GPU2D
```

**定义位置（Location）**：[`modules/lvgl/nemagfx/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/nemagfx/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL Zephyr NemaGFX 支持

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_STM32_NEOCHROM_GPU2D`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_NEOCHROM_GPU2D)。

<a id="CONFIG_LV_Z_USE_OSAL"></a>

## 240.75 `CONFIG_LV_Z_USE_OSAL`

**提示（Prompt）**：使用操作系统抽象层（OSAL）启用并行渲染

**说明（Help）**

使用 Zephyr LVGL 操作系统抽象层（OSAL），启用并行渲染流水线（parallel rendering pipelines）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DYNAMIC_THREAD && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_VDB_ALIGN"></a>

## 240.76 `CONFIG_LV_Z_VDB_ALIGN`

**提示（Prompt）**：渲染缓冲区对齐（Rendering buffer alignment）

**说明（Help）**

渲染缓冲区对齐（rendering buffer alignment）要求。根据所选颜色深度（color depth），缓冲区可能通过 `uint8_t *`、`uint16_t *` 或 `uint32_t *` 访问，因此必须正确对齐，防止非对齐内存访问（unaligned memory access）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_BUFFER_ALLOC_STATIC && CONFIG_LVGL
```

**默认值（Defaults）**

```text
4
8 if CONFIG_DISPLAY_MCUX_ELCDIF
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rk043fn02h_ct/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn02h_ct/Kconfig.defconfig)。

```text
32
```

来源：[`boards/shields/rk043fn66hs_ctg/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rk043fn66hs_ctg/Kconfig.defconfig)。

```text
32
```

来源：[`boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig)。

```text
64
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig)。

```text
64
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
64
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig)。

```text
64
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
64
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_BUFFER_ALLOC_STATIC`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUFFER_ALLOC_STATIC)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_DISPLAY_MCUX_ELCDIF`](P077_drivers_display_配置项参考_1.md#CONFIG_DISPLAY_MCUX_ELCDIF)。

<a id="CONFIG_LV_Z_VDB_CUSTOM_SECTION"></a>

## 240.77 `CONFIG_LV_Z_VDB_CUSTOM_SECTION`

**提示（Prompt）**：将渲染缓冲区链接到自定义段（custom section）

**说明（Help）**

将 LVGL 渲染缓冲区（rendering buffers）放在标记为 `.lvgl_buf` 的自定义段中。自定义链接器脚本（linker scripts）可据此将缓冲区重定位到特定位置，例如紧耦合存储器（tightly coupled memory）或外部内存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_BUFFER_ALLOC_STATIC && CONFIG_LVGL
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_BUFFER_ALLOC_STATIC`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUFFER_ALLOC_STATIC)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_VDB_SIZE"></a>

## 240.78 `CONFIG_LV_Z_VDB_SIZE`

**提示（Prompt）**：渲染缓冲区大小（Rendering buffer size）

**说明（Help）**

用于渲染屏幕内容的缓冲区大小，以显示器总大小的百分比（percentage）表示。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LVGL
```

**默认值（Defaults）**

```text
100 if CONFIG_LV_Z_FULL_REFRESH
100 if CONFIG_LV_Z_DIRECT_RENDERING
10
```

**取值范围（Ranges）**

```text
[100, 100] if CONFIG_LV_Z_FULL_REFRESH || CONFIG_LV_Z_DIRECT_RENDERING
[1, 100]
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x32_oled/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_featherwing_128x64_oled/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_2_8_tft_touch_arduino/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/buydisplay_3_5_tft_touch_arduino/Kconfig.defconfig)。

```text
32
```

来源：[`boards/shields/g1120b0mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/Kconfig.defconfig)。

```text
16
```

来源：[`boards/shields/lcd_par_s035/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/Kconfig.defconfig)。

```text
10
```

来源：[`boards/shields/ls0xx_generic/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ls0xx_generic/Kconfig.defconfig)。

```text
16
```

来源：[`boards/shields/m5stack_unit_minioled/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/m5stack_unit_minioled/Kconfig.defconfig)。

```text
40
```

来源：[`boards/shields/rtkapplcdms02001be/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkapplcdms02001be/Kconfig.defconfig)。

```text
100
```

来源：[`boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_expansion_board/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/ssd1306/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/ssd1306/Kconfig.defconfig)。

```text
64
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
16 if CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW075T7
```

来源：[`boards/shields/waveshare_epaper/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/waveshare_epaper/Kconfig.defconfig)。

```text
16
```

来源：[`boards/shields/zc143ac72mipi/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/zc143ac72mipi/Kconfig.defconfig)。

```text
16
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)、[`CONFIG_LV_Z_FULL_REFRESH`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_FULL_REFRESH)、[`CONFIG_LV_Z_DIRECT_RENDERING`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_DIRECT_RENDERING)、[`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW075T7`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW075T7)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SHIELD_WAVESHARE_EPAPER_GDEW075T7`。

<a id="CONFIG_LV_Z_VDB_ZEPHYR_REGION"></a>

## 240.79 `CONFIG_LV_Z_VDB_ZEPHYR_REGION`

**提示（Prompt）**：将 LVGL 渲染缓冲区放在 Zephyr 内存区域（memory-region）中

**说明（Help）**

将 LVGL 渲染缓冲区放在根据兼容 `zephyr,memory-region` 的节点自动创建的段中；区域名称由 `LV_Z_VDB_ZEPHYR_REGION_NAME` 指定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_BUFFER_ALLOC_STATIC && !CONFIG_LV_Z_VDB_CUSTOM_SECTION && CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig)。

```text
y
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig)。

```text
y
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
y
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig)。

```text
y
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig)。

```text
y
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_BUFFER_ALLOC_STATIC`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_BUFFER_ALLOC_STATIC)、[`CONFIG_LV_Z_VDB_CUSTOM_SECTION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_VDB_CUSTOM_SECTION)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<a id="CONFIG_LV_Z_VDB_ZEPHYR_REGION_NAME"></a>

## 240.80 `CONFIG_LV_Z_VDB_ZEPHYR_REGION_NAME`

**提示（Prompt）**：渲染缓冲区所在的 Zephyr 内存区域（memory-region）名称

**说明（Help）**

放置 LVGL 渲染缓冲区的 Zephyr 内存区域（memory-region）名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LV_Z_VDB_ZEPHYR_REGION && CONFIG_LVGL
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtk7eka6m3b00001bu/boards/ek_ra8d1.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8d2_r7ka8d2kflcac_cm85.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtklcdpar1s00001be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/aik_ra8d1.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8d1.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/rtkmipilcdb00000be/boards/ek_ra8p1_r7ka8p1kflcac_cm85.defconfig)。

```text
"SDRAM"
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h747i_disco_stm32h747xx_m7.defconfig)。

```text
"SDRAM2"
```

来源：[`boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_lcd40_dsi1_mb1166/boards/stm32h757i_eval_stm32h757xx_m7.defconfig)。

```text
"SDRAM2"
```

**定义位置（Location）**：[`modules/lvgl/Kconfig.memory:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/lvgl/Kconfig.memory#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → 内存管理器设置（Memory manager settings） → 将 LVGL 渲染缓冲区放在 Zephyr 内存区域（memory-region）中

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_VDB_ZEPHYR_REGION`](P240_modules_lvgl_配置项参考.md#CONFIG_LV_Z_VDB_ZEPHYR_REGION)、[`CONFIG_LVGL`](P240_modules_lvgl_配置项参考.md#CONFIG_LVGL)。

<!-- kconfig-navigation -->

[上一章](P239_modules_loramac-node_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P241_modules_mbedtls_配置项参考_1.md)
