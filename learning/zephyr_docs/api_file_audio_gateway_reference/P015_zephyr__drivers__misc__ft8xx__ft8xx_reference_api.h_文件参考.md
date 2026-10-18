---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-15
title: zephyr__drivers__misc__ft8xx__ft8xx_reference_api.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_misc\_\_ft8xx\_\_ft8xx\_reference\_api.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__reference__api_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8XX参考API（Reference API）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_common.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_dl.h>
#include <zephyr/drivers/misc/ft8xx/ft8xx_memory.h>
```

查看此文件的源码。

FT8XX参考API（Reference API）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.1\_宏定义（Macros）

<a id="r_gabf03e1cd7cb18b7c1daf243d4c1dde24"></a>

```c
#define OPT_3D FT8XX_OPT_3D
```

相关声明：[OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabf03e1cd7cb18b7c1daf243d4c1dde24)、[FT8XX_OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga304badab7bd34208d499b199080fb557)。

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="r_ga53f763f1e5de09b5e51242df87af8fb8"></a>

```c
#define OPT_RGB565 FT8XX_OPT_RGB565
```

相关声明：[OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga53f763f1e5de09b5e51242df87af8fb8)、[FT8XX_OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3a79c1128bdb9fe094843688691a085c)。

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="r_ga2fab787f842bb9193c9df68cb44f93fd"></a>

```c
#define OPT_MONO FT8XX_OPT_MONO
```

相关声明：[OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga2fab787f842bb9193c9df68cb44f93fd)、[FT8XX_OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga415760ddf94db71ee9a504300bac4661)。

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="r_ga37f793d8ac3af5f518d024727ce9f710"></a>

```c
#define OPT_NODL FT8XX_OPT_NODL
```

相关声明：[OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga37f793d8ac3af5f518d024727ce9f710)、[FT8XX_OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc953470460b083c0b8bd9ebbc8ed03b)。

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="r_gaa76b9296cd6f2eb4bec3d650b73e69cc"></a>

```c
#define OPT_FLAT FT8XX_OPT_FLAT
```

相关声明：[OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa76b9296cd6f2eb4bec3d650b73e69cc)、[FT8XX_OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga160b331fb401eec023e0992c6f4c6331)。

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="r_gae0fef45ae7ca3a45286a19a47bd46943"></a>

```c
#define OPT_SIGNED FT8XX_OPT_SIGNED
```

相关声明：[OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae0fef45ae7ca3a45286a19a47bd46943)、[FT8XX_OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga5a58155896cdb2d0f1693d203706ce93)。

将数字视为 32 位有符号整数（Signed Integer）。

<a id="r_ga65bf92a2956ffee68057ab90be032445"></a>

```c
#define OPT_CENTERX FT8XX_OPT_CENTERX
```

相关声明：[OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga65bf92a2956ffee68057ab90be032445)、[FT8XX_OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac2d1ccbb99eaa032ed9d39fc01d32c66)。

协处理器控件（Co-processor Widget）水平居中。

<a id="r_gaa28880f2aa7b6d8a51518189ca08382f"></a>

```c
#define OPT_CENTERY FT8XX_OPT_CENTERY
```

相关声明：[OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa28880f2aa7b6d8a51518189ca08382f)、[FT8XX_OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga65b3a1e29ae425b2f1c3e66b4ea1449a)。

协处理器控件（Co-processor Widget）垂直居中。

<a id="r_ga830647bc1b42665e27813a46a6a089b7"></a>

```c
#define OPT_CENTER FT8XX_OPT_CENTER
```

相关声明：[OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga830647bc1b42665e27813a46a6a089b7)、[FT8XX_OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga013968a6bf9534265c897ab1f4018eb0)。

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="r_gae0088375e797e08fa3e14dc3124c1e90"></a>

```c
#define OPT_RIGHTX FT8XX_OPT_RIGHTX
```

相关声明：[OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae0088375e797e08fa3e14dc3124c1e90)、[FT8XX_OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac864c155bc2121bf8d3954e1ed8dbb7e)。

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="r_ga87b8705ac37fc69704f00cc2a9b8e69e"></a>

```c
#define OPT_NOBACK FT8XX_OPT_NOBACK
```

相关声明：[OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga87b8705ac37fc69704f00cc2a9b8e69e)、[FT8XX_OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacb08df4fac256cbf808b133d4159aa29)。

协处理器控件（Co-processor Widget）不绘制背景。

<a id="r_gaed772e3cf2529e698fa8e69ee73f91f9"></a>

```c
#define OPT_NOTICKS FT8XX_OPT_NOTICKS
```

相关声明：[OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaed772e3cf2529e698fa8e69ee73f91f9)、[FT8XX_OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga50f4fac88e4f4b558450adcda33dae93)。

协处理器时钟控件（Clock Widget）不绘制小时刻度。

<a id="r_ga1e7090a0dbcee600a5472f5fc4343824"></a>

```c
#define OPT_NOHM FT8XX_OPT_NOHM
```

相关声明：[OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1e7090a0dbcee600a5472f5fc4343824)、[FT8XX_OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga79938d9c1193d44a527ca8c158117a86)。

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="r_ga0eb8abce5677ca0e6948ec1a003958de"></a>

```c
#define OPT_NOPOINTER FT8XX_OPT_NOPOINTER
```

相关声明：[OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga0eb8abce5677ca0e6948ec1a003958de)、[FT8XX_OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga1a9838a862ec166bfe95d64144b9a052)。

协处理器仪表（Gauge）没有指针。

<a id="r_ga190c29e3a00685c3f8c4906df37720ae"></a>

```c
#define OPT_NOSECS FT8XX_OPT_NOSECS
```

相关声明：[OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga190c29e3a00685c3f8c4906df37720ae)、[FT8XX_OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga6416f4282d2c483d2adba8c1215ab638)。

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="r_gaa9bc6e351e9fb0515c69f3cd32ad5621"></a>

```c
#define OPT_NOHANDS FT8XX_OPT_NOHANDS
```

相关声明：[OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa9bc6e351e9fb0515c69f3cd32ad5621)、[FT8XX_OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gade56de46694ca420460c1ceb26a33120)。

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="r_ga3746a5c44f711b633ca618b6ebb8e75f"></a>

```c
#define BITMAPS FT8XX_BITMAPS
```

相关声明：[BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3746a5c44f711b633ca618b6ebb8e75f)、[FT8XX_BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga28f7596c367f67f73d701b792300aa09)。

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="r_gae6910994a90091fe877b021c590c894e"></a>

```c
#define POINTS FT8XX_POINTS
```

相关声明：[POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae6910994a90091fe877b021c590c894e)、[FT8XX_POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d6f49b3817f9927fa1cd3cd42820490)。

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="r_ga321ae946de24c36489276616d13c46cd"></a>

```c
#define LINES FT8XX_LINES
```

相关声明：[LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga321ae946de24c36489276616d13c46cd)、[FT8XX_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga62bcf30c7a9eae4c468e1c7de144ad01)。

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

<a id="r_gac300cac409c1526ba5622f15472a25df"></a>

```c
#define LINE_STRIP FT8XX_LINE_STRIP
```

相关声明：[LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gac300cac409c1526ba5622f15472a25df)、[FT8XX_LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gac1b1188c36a4078e7db50d3c5aee7d25)。

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="r_ga8c7fa2526afa79673d93b64f864d2126"></a>

```c
#define EDGE_STRIP_R FT8XX_EDGE_STRIP_R
```

相关声明：[EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8c7fa2526afa79673d93b64f864d2126)、[FT8XX_EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga0b3ce2828323978e9648bfd07caa1065)。

向右延伸的边缘带（Edge Strips）。

<a id="r_ga3434ce2412337ac0b7d9558ff25181d0"></a>

```c
#define EDGE_STRIP_L FT8XX_EDGE_STRIP_L
```

相关声明：[EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3434ce2412337ac0b7d9558ff25181d0)、[FT8XX_EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga97229abf592bba4039f19a98451cdc5b)。

向左延伸的边缘带（Edge Strips）。

<a id="r_gaa69720d489114390d9493d397cd392b7"></a>

```c
#define EDGE_STRIP_A FT8XX_EDGE_STRIP_A
```

相关声明：[EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa69720d489114390d9493d397cd392b7)、[FT8XX_EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gaf5ad60bbe137dbf64281ad8d0be051e0)。

向上延伸的边缘带（Edge Strips）。

<a id="r_ga20ed5346e45eb4ce0e79f094c7346627"></a>

```c
#define EDGE_STRIP_B FT8XX_EDGE_STRIP_B
```

相关声明：[EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga20ed5346e45eb4ce0e79f094c7346627)、[FT8XX_EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga9aff3a3c58e12b990130271e845662a8)。

向下延伸的边缘带（Edge Strips）。

<a id="r_ga5868720577871792983ae813837c6189"></a>

```c
#define RECTS FT8XX_RECTS
```

相关声明：[RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga5868720577871792983ae813837c6189)、[FT8XX_RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga05077568fea624ed7e3f9e3f6e8d72b8)。

圆角矩形（Round-cornered Rectangles）；角部曲率可通过 LINE_WIDTH 调整。

<a id="r_ga34b42db00c62ff404a8bd7119fc62327"></a>

```c
#define BEGIN(prim)
```

相关声明：[BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga34b42db00c62ff404a8bd7119fc62327)。

开始绘制图形图元（Graphics Primitive）。

<a id="r_ga218ebaaf7d9afe6257021f3c08e59959"></a>

```c
#define CLEAR(c, s, t)
```

相关声明：[CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga218ebaaf7d9afe6257021f3c08e59959)。

将缓冲区清除为预设值（Preset Values）。

<a id="r_gae6375b17ea6f06bf81357fe9350e1c1c"></a>

```c
#define CLEAR_COLOR_RGB(red, green, blue)
```

相关声明：[CLEAR_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae6375b17ea6f06bf81357fe9350e1c1c)。

指定红、绿、蓝通道的清除值（Clear Values）。

<a id="r_ga59c390601a75b4d869e7cfc58d2430bf"></a>

```c
#define COLOR_RGB(red, green, blue)
```

相关声明：[COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga59c390601a75b4d869e7cfc58d2430bf)。

设置当前红、绿、蓝颜色（Current Color）。

<a id="r_ga486931aa64c90970e7a4110ada3d0916"></a>

```c
#define DISPLAY()
```

相关声明：[DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga486931aa64c90970e7a4110ada3d0916)。

结束显示列表（Display List）。

<a id="r_ga569b6a4f889b0846cc0a3396f3835a17"></a>

```c
#define END()
```

相关声明：[END](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga569b6a4f889b0846cc0a3396f3835a17)。

结束图形图元（Graphics Primitive）的绘制。

<a id="r_ga8764958e4fa66c3948353226f82cedaf"></a>

```c
#define LINE_WIDTH(width)
```

相关声明：[LINE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8764958e4fa66c3948353226f82cedaf)。

指定使用 LINES 图元（Primitive）绘制的线宽（Width）。

<a id="r_ga5f17de6768f32dd36135de83c24d0a7b"></a>

```c
#define TAG(s)
```

相关声明：[TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga5f17de6768f32dd36135de83c24d0a7b)。

为后续图形对象附加标签值（Tag Value）。

<a id="r_ga033cea1b18c3f010aaa0293f6972069a"></a>

```c
#define VERTEX2F(x, y)
```

相关声明：[VERTEX2F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga033cea1b18c3f010aaa0293f6972069a)。

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

<a id="r_gae779df636416e900ddc15b95cf2a923c"></a>

```c
#define VERTEX2II(x, y, handle, cell)
```

相关声明：[VERTEX2II](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae779df636416e900ddc15b95cf2a923c)。

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 15.2\_枚举（Enumerations）

<a id="r_gabbba9344e2d9b81af6313c6b7f12276c"></a>

```c
enum ft8xx_memory_map_t { RAM_G = FT810_RAM_G , RAM_DL = FT810_RAM_DL , REG_ = FT810_REG_ , RAM_CMD = FT810_RAM_CMD }
```

相关声明：[ft8xx_memory_map_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabbba9344e2d9b81af6313c6b7f12276c)、[RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4)、[RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84)、[REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779)、[RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5)。

FT810 内存映射（Memory Map）的主要部分。

<a id="r_gaa3f6afa02b5f4bed90093f659201d008"></a>

```c
enum ft8xx_register_address_t { REG_TRIM = FT810_REG_TRIM , REG_ID = FT810_REG_ID , REG_FRAMES = FT810_REG_FRAMES , REG_CLOCK = FT810_REG_CLOCK , REG_FREQUENCY = FT810_REG_FREQUENCY , REG_RENDERMODE = FT810_REG_RENDERMODE , REG_SNAPY = FT810_REG_SNAPY , REG_SNAPSHOT = FT810_REG_SNAPSHOT , REG_CPURESET = FT810_REG_CPURESET , REG_TAP_CRC = FT810_REG_TAP_CRC , REG_TAP_MASK = FT810_REG_TAP_MASK , REG_HCYCLE = FT810_REG_HCYCLE , REG_HOFFSET = FT810_REG_HOFFSET , REG_HSIZE = FT810_REG_HSIZE , REG_HSYNC0 = FT810_REG_HSYNC0 , REG_HSYNC1 = FT810_REG_HSYNC1 , REG_VCYCLE = FT810_REG_VCYCLE , REG_VOFFSET = FT810_REG_VOFFSET , REG_VSIZE = FT810_REG_VSIZE , REG_VSYNC0 = FT810_REG_VSYNC0 , REG_VSYNC1 = FT810_REG_VSYNC1 , REG_DLSWAP = FT810_REG_DLSWAP , REG_ROTATE = FT810_REG_ROTATE , REG_OUTBITS = FT810_REG_OUTBITS , REG_DITHER = FT810_REG_DITHER , REG_SWIZZLE = FT810_REG_SWIZZLE , REG_CSPREAD = FT810_REG_CSPREAD , REG_PCLK_POL = FT810_REG_PCLK_POL , REG_PCLK = FT810_REG_PCLK , REG_TAG_X = FT810_REG_TAG_X , REG_TAG_Y = FT810_REG_TAG_Y , REG_TAG = FT810_REG_TAG , REG_VOL_PB = FT810_REG_VOL_PB , REG_VOL_SOUND = FT810_REG_VOL_SOUND , REG_SOUND = FT810_REG_SOUND , REG_PLAY = FT810_REG_PLAY , REG_GPIO_DIR = FT810_REG_GPIO_DIR , REG_GPIO = FT810_REG_GPIO , REG_GPIOX_DIR = FT810_REG_GPIOX_DIR , REG_GPIOX = FT810_REG_GPIOX , REG_INT_FLAGS = FT810_REG_INT_FLAGS , REG_INT_EN = FT810_REG_INT_EN , REG_INT_MASK = FT810_REG_INT_MASK , REG_PLAYBACK_START = FT810_REG_PLAYBACK_START , REG_PLAYBACK_LENGTH = FT810_REG_PLAYBACK_LENGTH , REG_PLAYBACK_READPTR = FT810_REG_PLAYBACK_READPTR , REG_PLAYBACK_FREQ = FT810_REG_PLAYBACK_FREQ , REG_PLAYBACK_FORMAT = FT810_REG_PLAYBACK_FORMAT , REG_PLAYBACK_LOOP = FT810_REG_PLAYBACK_LOOP , REG_PLAYBACK_PLAY = FT810_REG_PLAYBACK_PLAY , REG_PWM_HZ = FT810_REG_PWM_HZ , REG_PWM_DUTY = FT810_REG_PWM_DUTY , REG_CMD_READ = FT810_REG_CMD_READ , REG_CMD_WRITE = FT810_REG_CMD_WRITE , REG_CMD_DL = FT810_REG_CMD_DL , REG_TOUCH_MODE = FT810_REG_TOUCH_MODE , REG_TOUCH_ADC_MODE = FT810_REG_TOUCH_ADC_MODE , REG_TOUCH_CHARGE = FT810_REG_TOUCH_CHARGE , REG_TOUCH_SETTLE = FT810_REG_TOUCH_SETTLE , REG_TOUCH_OVERSAMPLE = FT810_REG_TOUCH_OVERSAMPLE , REG_TOUCH_RZTHRESH = FT810_REG_TOUCH_RZTHRESH , REG_TOUCH_RAW_XY = FT810_REG_TOUCH_RAW_XY , REG_TOUCH_RZ = FT810_REG_TOUCH_RZ , REG_TOUCH_SCREEN_XY = FT810_REG_TOUCH_SCREEN_XY , REG_TOUCH_TAG_XY = FT810_REG_TOUCH_TAG_XY , REG_TOUCH_TAG = FT810_REG_TOUCH_TAG , REG_TOUCH_TRANSFORM_A = FT810_REG_TOUCH_TRANSFORM_A , REG_TOUCH_TRANSFORM_B = FT810_REG_TOUCH_TRANSFORM_B , REG_TOUCH_TRANSFORM_C = FT810_REG_TOUCH_TRANSFORM_C , REG_TOUCH_TRANSFORM_D = FT810_REG_TOUCH_TRANSFORM_D , REG_TOUCH_TRANSFORM_E = FT810_REG_TOUCH_TRANSFORM_E , REG_TOUCH_TRANSFORM_F = FT810_REG_TOUCH_TRANSFORM_F , REG_TOUCH_CONFIG = FT810_REG_TOUCH_CONFIG , REG_SPI_WIDTH = FT810_REG_SPI_WIDTH , REG_TOUCH_DIRECT_XY = FT810_REG_TOUCH_DIRECT_XY , REG_TOUCH_DIRECT_Z1Z2 = FT810_REG_TOUCH_DIRECT_Z1Z2 , REG_CMDB_SPACE = FT810_REG_CMDB_SPACE , REG_CMDB_WRITE = FT810_REG_CMDB_WRITE , REG_TRACKER = FT810_REG_TRACKER , REG_TRACKER1 = FT810_REG_TRACKER1 , REG_TRACKER2 = FT810_REG_TRACKER2 , REG_TRACKER3 = FT810_REG_TRACKER3 , REG_TRACKER4 = FT810_REG_TRACKER4 , REG_MEDIAFIFO_READ = FT810_REG_MEDIAFIFO_READ , REG_MEDIAFIFO_WRITE = FT810_REG_MEDIAFIFO_WRITE }
```

相关声明：[ft8xx_register_address_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa3f6afa02b5f4bed90093f659201d008)、[REG_TRIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74)、[REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a)、[REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272)、[REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64)、[REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21)、[REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9)、[REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f)、[REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b)、[REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2)、[REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208)、[REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd)、[REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2)、[REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85)、[REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0)、[REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a)、[REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559)、[REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a)、[REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2)、[REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878)、[REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050)、[REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb)、[REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019)、[REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3)、[REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009)、[REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b)、[REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6)、[REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d)、[REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b)、[REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55)、[REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541)、[REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254)、[REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b)、[REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888)、[REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970)、[REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe)、[REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3)、[REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e)、[REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1)、[REG_GPIOX_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788)、[REG_GPIOX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced)、[REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f)、[REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697)、[REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d)、[REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e)、[REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2)、[REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d)、[REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3)、[REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c)、[REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5)、[REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8)、[REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50)、[REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265)、[REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68)、[REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69)、[REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87)、[REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29)、[REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e)、[REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95)、[REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb)、[REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96)、[REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e)、[REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d)、[REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455)、[REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8)、[REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789)、[REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af)、[REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd)、[REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745)、[REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793)、[REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48)、[REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c)、[REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315)、[REG_TOUCH_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950)、[REG_SPI_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848)、[REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd)、[REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0)、[REG_CMDB_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c)、[REG_CMDB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464)、[REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb)、[REG_TRACKER1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622)、[REG_TRACKER2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76)、[REG_TRACKER3](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c)、[REG_TRACKER4](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf)、[REG_MEDIAFIFO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97)、[REG_MEDIAFIFO_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b)。

FT810 寄存器地址（Register Addresses）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.3\_函数（Functions）

<a id="r_ga1e9c6203ebb7cc15a736d074bd98c181"></a>

```c
static void wr8 (uint32_t address, uint8_t data)
```

相关声明：[wr8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1e9c6203ebb7cc15a736d074bd98c181)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 FT8xx 存储器写入 1 字节（8 位）。

<a id="r_ga8fac4ed55f7ef9d82d8dcb0eb6f09eab"></a>

```c
static void wr16 (uint32_t address, uint16_t data)
```

相关声明：[wr16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 FT8xx 存储器写入 2 字节（16 位）。

<a id="r_ga3f6814650684e2c2100d8f9a36505ca0"></a>

```c
static void wr32 (uint32_t address, uint32_t data)
```

相关声明：[wr32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3f6814650684e2c2100d8f9a36505ca0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 FT8xx 存储器写入 4 字节（32 位）。

<a id="r_gae96efe5496139f508083a21b2299e3d8"></a>

```c
static uint8_t rd8 (uint32_t address)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rd8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae96efe5496139f508083a21b2299e3d8)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 1 字节（8 位）。

<a id="r_ga2f833e24c067f88801884c93766d7ac7"></a>

```c
static uint16_t rd16 (uint32_t address)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[rd16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga2f833e24c067f88801884c93766d7ac7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 2 字节（16 位）。

<a id="r_ga0c6f11426fd5412a66e4f5de0a9f0847"></a>

```c
static uint32_t rd32 (uint32_t address)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[rd32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga0c6f11426fd5412a66e4f5de0a9f0847)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 4 字节（32 位）。

<a id="r_gacde1ca3945cbe6c828f65051c5c3a615"></a>

```c
static void cmd (uint32_t command)
```

相关声明：[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

<a id="r_ga7b9b6a41a878c449b107e51eba058799"></a>

```c
static void cmd_dlstart (void)
```

相关声明：[cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga7b9b6a41a878c449b107e51eba058799)。

开始新的显示列表（Display List）。

<a id="r_ga194d7e0d47b3d195155a22f86fbe7e7f"></a>

```c
static void cmd_swap (void)
```

相关声明：[cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga194d7e0d47b3d195155a22f86fbe7e7f)。

交换当前显示列表（Display List）。

<a id="r_ga4b77c199d909f946f7e271f11833533b"></a>

```c
static void cmd_fgcolor (uint32_t c)
```

相关声明：[cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4b77c199d909f946f7e271f11833533b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前景色（Foreground Color）。

<a id="r_ga4467cd6c9672ac2b4c7d6b6b2e9b2f89"></a>

```c
static void cmd_bgcolor (uint32_t c)
```

相关声明：[cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4467cd6c9672ac2b4c7d6b6b2e9b2f89)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置背景色（Background Color）。

<a id="r_ga1f01e0c91e369234362ed2bcf42da681"></a>

```c
static void cmd_slider (int16_t x, int16_t y, int16_t w, int16_t h, uint16_t options, uint16_t val, uint16_t range)
```

相关声明：[cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1f01e0c91e369234362ed2bcf42da681)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制滑块（Slider）。

<a id="r_gade51ff6f98a8d4cb575447bbb60cba92"></a>

```c
static void cmd_toggle (int16_t x, int16_t y, int16_t w, int16_t font, uint16_t options, uint16_t state, const char *s)
```

相关声明：[cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gade51ff6f98a8d4cb575447bbb60cba92)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

绘制切换开关（Toggle Switch）。

<a id="r_gac4dc3208668383b58ec1010edeae3d2b"></a>

```c
static void cmd_track (int16_t x, int16_t y, int16_t w, int16_t h, int16_t tag)
```

相关声明：[cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gac4dc3208668383b58ec1010edeae3d2b)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

跟踪图形对象（Graphics Object）的触摸操作。

<a id="r_gad642a54deaa36152ca4fea5e31294732"></a>

```c
static void cmd_text (int16_t x, int16_t y, int16_t font, uint16_t options, const char *s)
```

相关声明：[cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gad642a54deaa36152ca4fea5e31294732)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制文本（Text）。

<a id="r_gabdaf9e6cd74c0d157d1673b99707e6f2"></a>

```c
static void cmd_number (int16_t x, int16_t y, int16_t font, uint16_t options, int32_t n)
```

相关声明：[cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabdaf9e6cd74c0d157d1673b99707e6f2)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

绘制十进制数字（Decimal Number）。

<a id="r_ga26015112ae4c62a944fe671ea2cb0bda"></a>

```c
static void cmd_calibrate (uint32_t *result)
```

相关声明：[cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga26015112ae4c62a944fe671ea2cb0bda)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

执行触摸屏校准例程（Touch Screen Calibration Routine）。


## 15.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/drivers/misc/ft8xx/ft8xx_copro.h](../api_source_reference/P279_ft8xx_copro.h_源码浏览.md)
- [zephyr/drivers/misc/ft8xx/ft8xx_common.h](../api_source_reference/P278_ft8xx_common.h_源码浏览.md)
- [zephyr/drivers/misc/ft8xx/ft8xx_dl.h](../api_source_reference/P280_ft8xx_dl.h_源码浏览.md)
- [zephyr/drivers/misc/ft8xx/ft8xx_memory.h](../api_source_reference/P281_ft8xx_memory.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P027_ft8xx_reference_api.h_源码浏览.md)
- [OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabf03e1cd7cb18b7c1daf243d4c1dde24)
- [FT8XX_OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga304badab7bd34208d499b199080fb557)
- [OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga53f763f1e5de09b5e51242df87af8fb8)
- [FT8XX_OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3a79c1128bdb9fe094843688691a085c)
- [OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga2fab787f842bb9193c9df68cb44f93fd)
- [FT8XX_OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga415760ddf94db71ee9a504300bac4661)
- [OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga37f793d8ac3af5f518d024727ce9f710)
- [FT8XX_OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc953470460b083c0b8bd9ebbc8ed03b)
- [OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa76b9296cd6f2eb4bec3d650b73e69cc)
- [FT8XX_OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga160b331fb401eec023e0992c6f4c6331)
- [OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae0fef45ae7ca3a45286a19a47bd46943)
- [FT8XX_OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga5a58155896cdb2d0f1693d203706ce93)
- [OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga65bf92a2956ffee68057ab90be032445)
- [FT8XX_OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac2d1ccbb99eaa032ed9d39fc01d32c66)
- [OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa28880f2aa7b6d8a51518189ca08382f)
- [FT8XX_OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga65b3a1e29ae425b2f1c3e66b4ea1449a)
- [OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga830647bc1b42665e27813a46a6a089b7)
- [FT8XX_OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga013968a6bf9534265c897ab1f4018eb0)
- [OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae0088375e797e08fa3e14dc3124c1e90)
- [FT8XX_OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac864c155bc2121bf8d3954e1ed8dbb7e)
- [OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga87b8705ac37fc69704f00cc2a9b8e69e)
- [FT8XX_OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacb08df4fac256cbf808b133d4159aa29)
- [OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaed772e3cf2529e698fa8e69ee73f91f9)
- [FT8XX_OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga50f4fac88e4f4b558450adcda33dae93)
- [OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1e7090a0dbcee600a5472f5fc4343824)
- [FT8XX_OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga79938d9c1193d44a527ca8c158117a86)
- [OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga0eb8abce5677ca0e6948ec1a003958de)
- [FT8XX_OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga1a9838a862ec166bfe95d64144b9a052)
- [OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga190c29e3a00685c3f8c4906df37720ae)
- [FT8XX_OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga6416f4282d2c483d2adba8c1215ab638)
- [OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa9bc6e351e9fb0515c69f3cd32ad5621)
- [FT8XX_OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gade56de46694ca420460c1ceb26a33120)
- [BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3746a5c44f711b633ca618b6ebb8e75f)
- [FT8XX_BITMAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga28f7596c367f67f73d701b792300aa09)
- [POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae6910994a90091fe877b021c590c894e)
- [FT8XX_POINTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga1d6f49b3817f9927fa1cd3cd42820490)
- [LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga321ae946de24c36489276616d13c46cd)
- [FT8XX_LINES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga62bcf30c7a9eae4c468e1c7de144ad01)
- [LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gac300cac409c1526ba5622f15472a25df)
- [FT8XX_LINE_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gac1b1188c36a4078e7db50d3c5aee7d25)
- [EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8c7fa2526afa79673d93b64f864d2126)
- [FT8XX_EDGE_STRIP_R](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga0b3ce2828323978e9648bfd07caa1065)
- [EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3434ce2412337ac0b7d9558ff25181d0)
- [FT8XX_EDGE_STRIP_L](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga97229abf592bba4039f19a98451cdc5b)
- [EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa69720d489114390d9493d397cd392b7)
- [FT8XX_EDGE_STRIP_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#gaf5ad60bbe137dbf64281ad8d0be051e0)
- [EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga20ed5346e45eb4ce0e79f094c7346627)
- [FT8XX_EDGE_STRIP_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga9aff3a3c58e12b990130271e845662a8)
- [RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga5868720577871792983ae813837c6189)
- [FT8XX_RECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__dl.html#ga05077568fea624ed7e3f9e3f6e8d72b8)
- [BEGIN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga34b42db00c62ff404a8bd7119fc62327)
- [CLEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga218ebaaf7d9afe6257021f3c08e59959)
- [CLEAR_COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae6375b17ea6f06bf81357fe9350e1c1c)
- [COLOR_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga59c390601a75b4d869e7cfc58d2430bf)
- [DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga486931aa64c90970e7a4110ada3d0916)
- [END](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga569b6a4f889b0846cc0a3396f3835a17)
- [LINE_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8764958e4fa66c3948353226f82cedaf)
- [TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga5f17de6768f32dd36135de83c24d0a7b)
- [VERTEX2F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga033cea1b18c3f010aaa0293f6972069a)
- [VERTEX2II](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae779df636416e900ddc15b95cf2a923c)
- [ft8xx_memory_map_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabbba9344e2d9b81af6313c6b7f12276c)
- [RAM_G](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4)
- [RAM_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84)
- [REG_](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779)
- [RAM_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5)
- [ft8xx_register_address_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gaa3f6afa02b5f4bed90093f659201d008)
- [REG_TRIM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74)
- [REG_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a)
- [REG_FRAMES](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272)
- [REG_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64)
- [REG_FREQUENCY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21)
- [REG_RENDERMODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9)
- [REG_SNAPY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f)
- [REG_SNAPSHOT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b)
- [REG_CPURESET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2)
- [REG_TAP_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208)
- [REG_TAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd)
- [REG_HCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2)
- [REG_HOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85)
- [REG_HSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0)
- [REG_HSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a)
- [REG_HSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559)
- [REG_VCYCLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a)
- [REG_VOFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2)
- [REG_VSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878)
- [REG_VSYNC0](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050)
- [REG_VSYNC1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb)
- [REG_DLSWAP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019)
- [REG_ROTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3)
- [REG_OUTBITS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009)
- [REG_DITHER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b)
- [REG_SWIZZLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6)
- [REG_CSPREAD](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d)
- [REG_PCLK_POL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b)
- [REG_PCLK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55)
- [REG_TAG_X](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541)
- [REG_TAG_Y](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254)
- [REG_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b)
- [REG_VOL_PB](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888)
- [REG_VOL_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970)
- [REG_SOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe)
- [REG_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3)
- [REG_GPIO_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e)
- [REG_GPIO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1)
- [REG_GPIOX_DIR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788)
- [REG_GPIOX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced)
- [REG_INT_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f)
- [REG_INT_EN](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697)
- [REG_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d)
- [REG_PLAYBACK_START](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e)
- [REG_PLAYBACK_LENGTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2)
- [REG_PLAYBACK_READPTR](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d)
- [REG_PLAYBACK_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3)
- [REG_PLAYBACK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c)
- [REG_PLAYBACK_LOOP](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5)
- [REG_PLAYBACK_PLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8)
- [REG_PWM_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50)
- [REG_PWM_DUTY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265)
- [REG_CMD_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68)
- [REG_CMD_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69)
- [REG_CMD_DL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87)
- [REG_TOUCH_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29)
- [REG_TOUCH_ADC_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e)
- [REG_TOUCH_CHARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95)
- [REG_TOUCH_SETTLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb)
- [REG_TOUCH_OVERSAMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96)
- [REG_TOUCH_RZTHRESH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e)
- [REG_TOUCH_RAW_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d)
- [REG_TOUCH_RZ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455)
- [REG_TOUCH_SCREEN_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8)
- [REG_TOUCH_TAG_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789)
- [REG_TOUCH_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af)
- [REG_TOUCH_TRANSFORM_A](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd)
- [REG_TOUCH_TRANSFORM_B](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745)
- [REG_TOUCH_TRANSFORM_C](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793)
- [REG_TOUCH_TRANSFORM_D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48)
- [REG_TOUCH_TRANSFORM_E](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c)
- [REG_TOUCH_TRANSFORM_F](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315)
- [REG_TOUCH_CONFIG](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950)
- [REG_SPI_WIDTH](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848)
- [REG_TOUCH_DIRECT_XY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd)
- [REG_TOUCH_DIRECT_Z1Z2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0)
- [REG_CMDB_SPACE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c)
- [REG_CMDB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464)
- [REG_TRACKER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb)
- [REG_TRACKER1](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622)
- [REG_TRACKER2](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76)
- [REG_TRACKER3](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c)
- [REG_TRACKER4](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf)
- [REG_MEDIAFIFO_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97)
- [REG_MEDIAFIFO_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b)
- [wr8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1e9c6203ebb7cc15a736d074bd98c181)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wr16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [wr32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga3f6814650684e2c2100d8f9a36505ca0)
- [rd8](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gae96efe5496139f508083a21b2299e3d8)
- [rd16](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga2f833e24c067f88801884c93766d7ac7)
- [rd32](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga0c6f11426fd5412a66e4f5de0a9f0847)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga7b9b6a41a878c449b107e51eba058799)
- [cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga194d7e0d47b3d195155a22f86fbe7e7f)
- [cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4b77c199d909f946f7e271f11833533b)
- [cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga4467cd6c9672ac2b4c7d6b6b2e9b2f89)
- [cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga1f01e0c91e369234362ed2bcf42da681)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gade51ff6f98a8d4cb575447bbb60cba92)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gac4dc3208668383b58ec1010edeae3d2b)
- [cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gad642a54deaa36152ca4fea5e31294732)
- [cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gabdaf9e6cd74c0d157d1673b99707e6f2)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#ga26015112ae4c62a944fe671ea2cb0bda)

<a id="header-details"></a>

---

[上一章](P014_zephyr__drivers__misc__ft8xx__ft8xx_copro.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__dt-bindings__reset__gd32c2x1.h_文件参考.md)
