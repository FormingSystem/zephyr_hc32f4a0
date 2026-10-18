---
id: learning.zephyr-docs.api-file-mesh-interrupt-reference.page-20
title: zephyr__dt-bindings__display__panel.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_zephyr\_\_dt-bindings\_\_display\_\_panel.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/panel_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

显示面板（Display Panels）的设备树像素格式标识符。

查看此文件的源码。

<a id="details"></a>

显示面板（Display Panels）的设备树像素格式标识符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_ga4775abe39fd68a2d64b4edb649790915"></a>

```c
#define PANEL_PIXEL_FORMAT_RGB_888 (0x1 << 0)
```

相关声明：[PANEL_PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga4775abe39fd68a2d64b4edb649790915)。

24 位红绿蓝格式（RGB），每个分量 8 位。

<a id="r_ga6712b7424ad89a33e04f66e76d3678ce"></a>

```c
#define PANEL_PIXEL_FORMAT_MONO01 (0x1 << 1)
```

相关声明：[PANEL_PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga6712b7424ad89a33e04f66e76d3678ce)。

每像素 1 位（1 bpp）单色（Monochrome），0 为黑色、1 为白色。

<a id="r_ga6311ee67721bd6e7209bbdc1b6788eb6"></a>

```c
#define PANEL_PIXEL_FORMAT_MONO10 (0x1 << 2)
```

相关声明：[PANEL_PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga6311ee67721bd6e7209bbdc1b6788eb6)。

每像素 1 位（1 bpp）单色（Monochrome），1 为黑色、0 为白色。

<a id="r_gac86c839997816ecfe501b14d240a6f2a"></a>

```c
#define PANEL_PIXEL_FORMAT_ARGB_8888 (0x1 << 3)
```

相关声明：[PANEL_PIXEL_FORMAT_ARGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gac86c839997816ecfe501b14d240a6f2a)。

32 位透明度－红－绿－蓝格式（ARGB），每个分量 8 位。

<a id="r_gad8d20eb4c243e11080d31df41026475b"></a>

```c
#define PANEL_PIXEL_FORMAT_RGB_565 (0x1 << 4)
```

相关声明：[PANEL_PIXEL_FORMAT_RGB_565](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gad8d20eb4c243e11080d31df41026475b)。

16 位 RGB 5:6:5 格式，红／绿／蓝分别占 5／6／5 位。

<a id="r_gaf8271408694ee534466e7915309b6440"></a>

```c
#define PANEL_PIXEL_FORMAT_RGB_565X (0x1 << 5)
```

相关声明：[PANEL_PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaf8271408694ee534466e7915309b6440)。

字节交换的 16 位 RGB 5:6:5 格式（Byte-swapped RGB）。

<a id="r_ga4a78444ac708085a699cd6ccaf7d7817"></a>

```c
#define PANEL_PIXEL_FORMAT_L_8 (0x1 << 6)
```

相关声明：[PANEL_PIXEL_FORMAT_L_8](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga4a78444ac708085a699cd6ccaf7d7817)。

8 位亮度／灰度（Luminance/Grayscale）。

<a id="r_ga5ee3faa8a6ddb4d59cbd4aafde40021a"></a>

```c
#define PANEL_PIXEL_FORMAT_AL_88 (0x1 << 7)
```

相关声明：[PANEL_PIXEL_FORMAT_AL_88](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga5ee3faa8a6ddb4d59cbd4aafde40021a)。

16 位亮度与透明度（Luminance and Alpha），各占 8 位。

<a id="r_ga1b25099c1904059561ea29f2c2f82750"></a>

```c
#define PANEL_PIXEL_FORMAT_XRGB_8888 (0x1 << 8)
```

相关声明：[PANEL_PIXEL_FORMAT_XRGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga1b25099c1904059561ea29f2c2f82750)。

32 位 XRGB 格式，每个分量 8 位。

<a id="r_gab20e626ea5e3520fe77b932fa01d89f5"></a>

```c
#define PANEL_PIXEL_FORMAT_BGR_888 (0x1 << 9)
```

相关声明：[PANEL_PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gab20e626ea5e3520fe77b932fa01d89f5)。

24 位蓝绿红格式（BGR），每个分量 8 位。

<a id="r_ga7d350b79357d4c7346818b5fe50a96c9"></a>

```c
#define PANEL_PIXEL_FORMAT_ABGR_8888 (0x1 << 10)
```

相关声明：[PANEL_PIXEL_FORMAT_ABGR_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga7d350b79357d4c7346818b5fe50a96c9)。

32 位透明度－蓝－绿－红格式（ABGR），每个分量 8 位。

<a id="r_ga5ed272606f9699d9f7e129c6b4cdcd27"></a>

```c
#define PANEL_PIXEL_FORMAT_RGBA_8888 (0x1 << 11)
```

相关声明：[PANEL_PIXEL_FORMAT_RGBA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga5ed272606f9699d9f7e129c6b4cdcd27)。

32 位红－绿－蓝－透明度格式（RGBA），每个分量 8 位。

<a id="r_ga460a6d53ea7b5e3baba3983f18d0064e"></a>

```c
#define PANEL_PIXEL_FORMAT_BGRA_8888 (0x1 << 12)
```

相关声明：[PANEL_PIXEL_FORMAT_BGRA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga460a6d53ea7b5e3baba3983f18d0064e)。

32 位蓝－绿－红－透明度格式（BGRA），每个分量 8 位。

<a id="r_ga9425d8073dac98659a77a17e146e0909"></a>

```c
#define PANEL_PIXEL_FORMAT_I_4 (0x1 << 13)
```

相关声明：[PANEL_PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga9425d8073dac98659a77a17e146e0909)。

4 位索引色（Indexed Color）。

<a id="r_gaed9a3adacac9926d5dd8418ac100a5d4"></a>

```c
#define PANEL_PIXEL_FORMAT_L_4 (0x1 << 14)
```

相关声明：[PANEL_PIXEL_FORMAT_L_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaed9a3adacac9926d5dd8418ac100a5d4)。

4 位亮度／灰度（Luminance/Grayscale）。

<a id="r_gaee786c1944da1234c8c258be385fda92"></a>

```c
#define PANEL_PIXEL_FORMAT_YUYV (0x1 << 15)
```

相关声明：[PANEL_PIXEL_FORMAT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaee786c1944da1234c8c258be385fda92)。

16 位打包 YUV 4:2:2 格式（Packed YUV）。

<a id="r_gaa0b9f908e93148d911cdc87a40b442e8"></a>

```c
#define ARGB8888(r, g, b, a)
```

相关声明：[ARGB8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaa0b9f908e93148d911cdc87a40b442e8)。

将颜色分量（Color Components）打包为 32 位 ARGB8888 值。

<a id="r_gaae0ff2b3e7c3ed70ca578750595d630b"></a>

```c
#define PANEL_COLOR_PALETTE_NULL 0
```

相关声明：[PANEL_COLOR_PALETTE_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaae0ff2b3e7c3ed70ca578750595d630b)。

面板调色板空值（Panel Color Palette Null Value）。


## 20.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P642_panel.h_源码浏览.md)
- [PANEL_PIXEL_FORMAT_RGB_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga4775abe39fd68a2d64b4edb649790915)
- [PANEL_PIXEL_FORMAT_MONO01](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga6712b7424ad89a33e04f66e76d3678ce)
- [PANEL_PIXEL_FORMAT_MONO10](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga6311ee67721bd6e7209bbdc1b6788eb6)
- [PANEL_PIXEL_FORMAT_ARGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gac86c839997816ecfe501b14d240a6f2a)
- [PANEL_PIXEL_FORMAT_RGB_565](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gad8d20eb4c243e11080d31df41026475b)
- [PANEL_PIXEL_FORMAT_RGB_565X](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaf8271408694ee534466e7915309b6440)
- [PANEL_PIXEL_FORMAT_L_8](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga4a78444ac708085a699cd6ccaf7d7817)
- [PANEL_PIXEL_FORMAT_AL_88](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga5ee3faa8a6ddb4d59cbd4aafde40021a)
- [PANEL_PIXEL_FORMAT_XRGB_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga1b25099c1904059561ea29f2c2f82750)
- [PANEL_PIXEL_FORMAT_BGR_888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gab20e626ea5e3520fe77b932fa01d89f5)
- [PANEL_PIXEL_FORMAT_ABGR_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga7d350b79357d4c7346818b5fe50a96c9)
- [PANEL_PIXEL_FORMAT_RGBA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga5ed272606f9699d9f7e129c6b4cdcd27)
- [PANEL_PIXEL_FORMAT_BGRA_8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga460a6d53ea7b5e3baba3983f18d0064e)
- [PANEL_PIXEL_FORMAT_I_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#ga9425d8073dac98659a77a17e146e0909)
- [PANEL_PIXEL_FORMAT_L_4](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaed9a3adacac9926d5dd8418ac100a5d4)
- [PANEL_PIXEL_FORMAT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaee786c1944da1234c8c258be385fda92)
- [ARGB8888](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaa0b9f908e93148d911cdc87a40b442e8)
- [PANEL_COLOR_PALETTE_NULL](https://docs.zephyrproject.org/latest/doxygen/html/group__display__panel__dt.html#gaae0ff2b3e7c3ed70ca578750595d630b)

<a id="header-details"></a>

---

[上一章](P019_zephyr__bluetooth__services__nus.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P021_zephyr__arch__pmu.h_文件参考.md)
