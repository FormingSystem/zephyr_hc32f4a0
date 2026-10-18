---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-12
title: FT8xx 参考 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_FT8xx 参考 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8xx 参考 API

<a id="details"></a>

FT8xx 参考 API（Reference API）。API 按《FT800 程序员指南》（FT800 Programmers Guide）的 API 参考定义实现。注意（Note）：本头文件定义的函数名称容易与其他模块提供的名称冲突，包含它时请谨慎。出现命名冲突时，不要包含此头文件，改用带 ft8xx_ 前缀的名称。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_gabf03e1cd7cb18b7c1daf243d4c1dde24"></a>

```c
#define OPT_3D FT8XX_OPT_3D
```

相关声明：[OPT_3D](#gabf03e1cd7cb18b7c1daf243d4c1dde24)、[FT8XX_OPT_3D](P010_FT8xx 协处理器（Co-processor）.md#ga304badab7bd34208d499b199080fb557)。

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="r_ga53f763f1e5de09b5e51242df87af8fb8"></a>

```c
#define OPT_RGB565 FT8XX_OPT_RGB565
```

相关声明：[OPT_RGB565](#ga53f763f1e5de09b5e51242df87af8fb8)、[FT8XX_OPT_RGB565](P010_FT8xx 协处理器（Co-processor）.md#ga3a79c1128bdb9fe094843688691a085c)。

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="r_ga2fab787f842bb9193c9df68cb44f93fd"></a>

```c
#define OPT_MONO FT8XX_OPT_MONO
```

相关声明：[OPT_MONO](#ga2fab787f842bb9193c9df68cb44f93fd)、[FT8XX_OPT_MONO](P010_FT8xx 协处理器（Co-processor）.md#ga415760ddf94db71ee9a504300bac4661)。

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="r_ga37f793d8ac3af5f518d024727ce9f710"></a>

```c
#define OPT_NODL FT8XX_OPT_NODL
```

相关声明：[OPT_NODL](#ga37f793d8ac3af5f518d024727ce9f710)、[FT8XX_OPT_NODL](P010_FT8xx 协处理器（Co-processor）.md#gacc953470460b083c0b8bd9ebbc8ed03b)。

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="r_gaa76b9296cd6f2eb4bec3d650b73e69cc"></a>

```c
#define OPT_FLAT FT8XX_OPT_FLAT
```

相关声明：[OPT_FLAT](#gaa76b9296cd6f2eb4bec3d650b73e69cc)、[FT8XX_OPT_FLAT](P010_FT8xx 协处理器（Co-processor）.md#ga160b331fb401eec023e0992c6f4c6331)。

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="r_gae0fef45ae7ca3a45286a19a47bd46943"></a>

```c
#define OPT_SIGNED FT8XX_OPT_SIGNED
```

相关声明：[OPT_SIGNED](#gae0fef45ae7ca3a45286a19a47bd46943)、[FT8XX_OPT_SIGNED](P010_FT8xx 协处理器（Co-processor）.md#ga5a58155896cdb2d0f1693d203706ce93)。

将数字视为 32 位有符号整数（Signed Integer）。

<a id="r_ga65bf92a2956ffee68057ab90be032445"></a>

```c
#define OPT_CENTERX FT8XX_OPT_CENTERX
```

相关声明：[OPT_CENTERX](#ga65bf92a2956ffee68057ab90be032445)、[FT8XX_OPT_CENTERX](P010_FT8xx 协处理器（Co-processor）.md#gac2d1ccbb99eaa032ed9d39fc01d32c66)。

协处理器控件（Co-processor Widget）水平居中。

<a id="r_gaa28880f2aa7b6d8a51518189ca08382f"></a>

```c
#define OPT_CENTERY FT8XX_OPT_CENTERY
```

相关声明：[OPT_CENTERY](#gaa28880f2aa7b6d8a51518189ca08382f)、[FT8XX_OPT_CENTERY](P010_FT8xx 协处理器（Co-processor）.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a)。

协处理器控件（Co-processor Widget）垂直居中。

<a id="r_ga830647bc1b42665e27813a46a6a089b7"></a>

```c
#define OPT_CENTER FT8XX_OPT_CENTER
```

相关声明：[OPT_CENTER](#ga830647bc1b42665e27813a46a6a089b7)、[FT8XX_OPT_CENTER](P010_FT8xx 协处理器（Co-processor）.md#ga013968a6bf9534265c897ab1f4018eb0)。

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="r_gae0088375e797e08fa3e14dc3124c1e90"></a>

```c
#define OPT_RIGHTX FT8XX_OPT_RIGHTX
```

相关声明：[OPT_RIGHTX](#gae0088375e797e08fa3e14dc3124c1e90)、[FT8XX_OPT_RIGHTX](P010_FT8xx 协处理器（Co-processor）.md#gac864c155bc2121bf8d3954e1ed8dbb7e)。

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="r_ga87b8705ac37fc69704f00cc2a9b8e69e"></a>

```c
#define OPT_NOBACK FT8XX_OPT_NOBACK
```

相关声明：[OPT_NOBACK](#ga87b8705ac37fc69704f00cc2a9b8e69e)、[FT8XX_OPT_NOBACK](P010_FT8xx 协处理器（Co-processor）.md#gacb08df4fac256cbf808b133d4159aa29)。

协处理器控件（Co-processor Widget）不绘制背景。

<a id="r_gaed772e3cf2529e698fa8e69ee73f91f9"></a>

```c
#define OPT_NOTICKS FT8XX_OPT_NOTICKS
```

相关声明：[OPT_NOTICKS](#gaed772e3cf2529e698fa8e69ee73f91f9)、[FT8XX_OPT_NOTICKS](P010_FT8xx 协处理器（Co-processor）.md#ga50f4fac88e4f4b558450adcda33dae93)。

协处理器时钟控件（Clock Widget）不绘制小时刻度。

<a id="r_ga1e7090a0dbcee600a5472f5fc4343824"></a>

```c
#define OPT_NOHM FT8XX_OPT_NOHM
```

相关声明：[OPT_NOHM](#ga1e7090a0dbcee600a5472f5fc4343824)、[FT8XX_OPT_NOHM](P010_FT8xx 协处理器（Co-processor）.md#ga79938d9c1193d44a527ca8c158117a86)。

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="r_ga0eb8abce5677ca0e6948ec1a003958de"></a>

```c
#define OPT_NOPOINTER FT8XX_OPT_NOPOINTER
```

相关声明：[OPT_NOPOINTER](#ga0eb8abce5677ca0e6948ec1a003958de)、[FT8XX_OPT_NOPOINTER](P010_FT8xx 协处理器（Co-processor）.md#ga1a9838a862ec166bfe95d64144b9a052)。

协处理器仪表（Gauge）没有指针。

<a id="r_ga190c29e3a00685c3f8c4906df37720ae"></a>

```c
#define OPT_NOSECS FT8XX_OPT_NOSECS
```

相关声明：[OPT_NOSECS](#ga190c29e3a00685c3f8c4906df37720ae)、[FT8XX_OPT_NOSECS](P010_FT8xx 协处理器（Co-processor）.md#ga6416f4282d2c483d2adba8c1215ab638)。

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="r_gaa9bc6e351e9fb0515c69f3cd32ad5621"></a>

```c
#define OPT_NOHANDS FT8XX_OPT_NOHANDS
```

相关声明：[OPT_NOHANDS](#gaa9bc6e351e9fb0515c69f3cd32ad5621)、[FT8XX_OPT_NOHANDS](P010_FT8xx 协处理器（Co-processor）.md#gade56de46694ca420460c1ceb26a33120)。

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="r_ga3746a5c44f711b633ca618b6ebb8e75f"></a>

```c
#define BITMAPS FT8XX_BITMAPS
```

相关声明：[位图（BITMAPS）。](#ga3746a5c44f711b633ca618b6ebb8e75f)、[位图（FT8XX_BITMAPS）。](P011_FT8xx 显示列表（Display list）.md#ga28f7596c367f67f73d701b792300aa09)。

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="r_gae6910994a90091fe877b021c590c894e"></a>

```c
#define POINTS FT8XX_POINTS
```

相关声明：[点（POINTS）。](#gae6910994a90091fe877b021c590c894e)、[点（FT8XX_POINTS）。](P011_FT8xx 显示列表（Display list）.md#ga1d6f49b3817f9927fa1cd3cd42820490)。

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="r_ga321ae946de24c36489276616d13c46cd"></a>

```c
#define LINES FT8XX_LINES
```

相关声明：[线段（LINES）。](#ga321ae946de24c36489276616d13c46cd)、[线段（FT8XX_LINES）。](P011_FT8xx 显示列表（Display list）.md#ga62bcf30c7a9eae4c468e1c7de144ad01)。

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

<a id="r_gac300cac409c1526ba5622f15472a25df"></a>

```c
#define LINE_STRIP FT8XX_LINE_STRIP
```

相关声明：[折线（LINE_STRIP）。](#gac300cac409c1526ba5622f15472a25df)、[折线（FT8XX_LINE_STRIP）。](P011_FT8xx 显示列表（Display list）.md#gac1b1188c36a4078e7db50d3c5aee7d25)。

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="r_ga8c7fa2526afa79673d93b64f864d2126"></a>

```c
#define EDGE_STRIP_R FT8XX_EDGE_STRIP_R
```

相关声明：[右侧边带（EDGE_STRIP_R）。](#ga8c7fa2526afa79673d93b64f864d2126)、[右侧边带（FT8XX_EDGE_STRIP_R）。](P011_FT8xx 显示列表（Display list）.md#ga0b3ce2828323978e9648bfd07caa1065)。

向右延伸的边缘带（Edge Strips）。

<a id="r_ga3434ce2412337ac0b7d9558ff25181d0"></a>

```c
#define EDGE_STRIP_L FT8XX_EDGE_STRIP_L
```

相关声明：[左侧边带（EDGE_STRIP_L）。](#ga3434ce2412337ac0b7d9558ff25181d0)、[左侧边带（FT8XX_EDGE_STRIP_L）。](P011_FT8xx 显示列表（Display list）.md#ga97229abf592bba4039f19a98451cdc5b)。

向左延伸的边缘带（Edge Strips）。

<a id="r_gaa69720d489114390d9493d397cd392b7"></a>

```c
#define EDGE_STRIP_A FT8XX_EDGE_STRIP_A
```

相关声明：[上侧边带（EDGE_STRIP_A）。](#gaa69720d489114390d9493d397cd392b7)、[上侧边带（FT8XX_EDGE_STRIP_A）。](P011_FT8xx 显示列表（Display list）.md#gaf5ad60bbe137dbf64281ad8d0be051e0)。

向上延伸的边缘带（Edge Strips）。

<a id="r_ga20ed5346e45eb4ce0e79f094c7346627"></a>

```c
#define EDGE_STRIP_B FT8XX_EDGE_STRIP_B
```

相关声明：[下侧边带（EDGE_STRIP_B）。](#ga20ed5346e45eb4ce0e79f094c7346627)、[下侧边带（FT8XX_EDGE_STRIP_B）。](P011_FT8xx 显示列表（Display list）.md#ga9aff3a3c58e12b990130271e845662a8)。

向下延伸的边缘带（Edge Strips）。

<a id="r_ga5868720577871792983ae813837c6189"></a>

```c
#define RECTS FT8XX_RECTS
```

相关声明：[矩形（RECTS）。](#ga5868720577871792983ae813837c6189)、[矩形（FT8XX_RECTS）。](P011_FT8xx 显示列表（Display list）.md#ga05077568fea624ed7e3f9e3f6e8d72b8)。

圆角矩形（Round-cornered Rectangles）；角部曲率可通过 LINE_WIDTH 调整。

<a id="r_ga34b42db00c62ff404a8bd7119fc62327"></a>

```c
#define BEGIN(prim)
```

相关声明：[BEGIN](#ga34b42db00c62ff404a8bd7119fc62327)。

开始绘制图形图元（Graphics Primitive）。

<a id="r_ga218ebaaf7d9afe6257021f3c08e59959"></a>

```c
#define CLEAR(c, s, t)
```

相关声明：[CLEAR](#ga218ebaaf7d9afe6257021f3c08e59959)。

将缓冲区清除为预设值（Preset Values）。

<a id="r_gae6375b17ea6f06bf81357fe9350e1c1c"></a>

```c
#define CLEAR_COLOR_RGB(red, green, blue)
```

相关声明：[CLEAR_COLOR_RGB](#gae6375b17ea6f06bf81357fe9350e1c1c)。

指定红、绿、蓝通道的清除值（Clear Values）。

<a id="r_ga59c390601a75b4d869e7cfc58d2430bf"></a>

```c
#define COLOR_RGB(red, green, blue)
```

相关声明：[COLOR_RGB](#ga59c390601a75b4d869e7cfc58d2430bf)。

设置当前红、绿、蓝颜色（Current Color）。

<a id="r_ga486931aa64c90970e7a4110ada3d0916"></a>

```c
#define DISPLAY()
```

相关声明：[DISPLAY](#ga486931aa64c90970e7a4110ada3d0916)。

结束显示列表（Display List）。

<a id="r_ga569b6a4f889b0846cc0a3396f3835a17"></a>

```c
#define END()
```

相关声明：[END](#ga569b6a4f889b0846cc0a3396f3835a17)。

结束图形图元（Graphics Primitive）的绘制。

<a id="r_ga8764958e4fa66c3948353226f82cedaf"></a>

```c
#define LINE_WIDTH(width)
```

相关声明：[LINE_WIDTH](#ga8764958e4fa66c3948353226f82cedaf)。

指定使用 LINES 图元（Primitive）绘制的线宽（Width）。

<a id="r_ga5f17de6768f32dd36135de83c24d0a7b"></a>

```c
#define TAG(s)
```

相关声明：[TAG](#ga5f17de6768f32dd36135de83c24d0a7b)。

为后续图形对象附加标签值（Tag Value）。

<a id="r_ga033cea1b18c3f010aaa0293f6972069a"></a>

```c
#define VERTEX2F(x, y)
```

相关声明：[VERTEX2F](#ga033cea1b18c3f010aaa0293f6972069a)。

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

<a id="r_gae779df636416e900ddc15b95cf2a923c"></a>

```c
#define VERTEX2II(x, y, handle, cell)
```

相关声明：[VERTEX2II](#gae779df636416e900ddc15b95cf2a923c)。

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.2\_枚举（Enumerations）

<a id="r_gabbba9344e2d9b81af6313c6b7f12276c"></a>

```c
enum ft8xx_memory_map_t { RAM_G = FT810_RAM_G , RAM_DL = FT810_RAM_DL , REG_ = FT810_REG_ , RAM_CMD = FT810_RAM_CMD }
```

相关声明：[ft8xx_memory_map_t](#gabbba9344e2d9b81af6313c6b7f12276c)、[RAM_G](#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4)、[RAM_DL](#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84)、[REG_](#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779)、[RAM_CMD](#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5)。

FT810 内存映射（Memory Map）的主要部分。

<a id="r_gaa3f6afa02b5f4bed90093f659201d008"></a>

```c
enum ft8xx_register_address_t { REG_TRIM = FT810_REG_TRIM , REG_ID = FT810_REG_ID , REG_FRAMES = FT810_REG_FRAMES , REG_CLOCK = FT810_REG_CLOCK , REG_FREQUENCY = FT810_REG_FREQUENCY , REG_RENDERMODE = FT810_REG_RENDERMODE , REG_SNAPY = FT810_REG_SNAPY , REG_SNAPSHOT = FT810_REG_SNAPSHOT , REG_CPURESET = FT810_REG_CPURESET , REG_TAP_CRC = FT810_REG_TAP_CRC , REG_TAP_MASK = FT810_REG_TAP_MASK , REG_HCYCLE = FT810_REG_HCYCLE , REG_HOFFSET = FT810_REG_HOFFSET , REG_HSIZE = FT810_REG_HSIZE , REG_HSYNC0 = FT810_REG_HSYNC0 , REG_HSYNC1 = FT810_REG_HSYNC1 , REG_VCYCLE = FT810_REG_VCYCLE , REG_VOFFSET = FT810_REG_VOFFSET , REG_VSIZE = FT810_REG_VSIZE , REG_VSYNC0 = FT810_REG_VSYNC0 , REG_VSYNC1 = FT810_REG_VSYNC1 , REG_DLSWAP = FT810_REG_DLSWAP , REG_ROTATE = FT810_REG_ROTATE , REG_OUTBITS = FT810_REG_OUTBITS , REG_DITHER = FT810_REG_DITHER , REG_SWIZZLE = FT810_REG_SWIZZLE , REG_CSPREAD = FT810_REG_CSPREAD , REG_PCLK_POL = FT810_REG_PCLK_POL , REG_PCLK = FT810_REG_PCLK , REG_TAG_X = FT810_REG_TAG_X , REG_TAG_Y = FT810_REG_TAG_Y , REG_TAG = FT810_REG_TAG , REG_VOL_PB = FT810_REG_VOL_PB , REG_VOL_SOUND = FT810_REG_VOL_SOUND , REG_SOUND = FT810_REG_SOUND , REG_PLAY = FT810_REG_PLAY , REG_GPIO_DIR = FT810_REG_GPIO_DIR , REG_GPIO = FT810_REG_GPIO , REG_GPIOX_DIR = FT810_REG_GPIOX_DIR , REG_GPIOX = FT810_REG_GPIOX , REG_INT_FLAGS = FT810_REG_INT_FLAGS , REG_INT_EN = FT810_REG_INT_EN , REG_INT_MASK = FT810_REG_INT_MASK , REG_PLAYBACK_START = FT810_REG_PLAYBACK_START , REG_PLAYBACK_LENGTH = FT810_REG_PLAYBACK_LENGTH , REG_PLAYBACK_READPTR = FT810_REG_PLAYBACK_READPTR , REG_PLAYBACK_FREQ = FT810_REG_PLAYBACK_FREQ , REG_PLAYBACK_FORMAT = FT810_REG_PLAYBACK_FORMAT , REG_PLAYBACK_LOOP = FT810_REG_PLAYBACK_LOOP , REG_PLAYBACK_PLAY = FT810_REG_PLAYBACK_PLAY , REG_PWM_HZ = FT810_REG_PWM_HZ , REG_PWM_DUTY = FT810_REG_PWM_DUTY , REG_CMD_READ = FT810_REG_CMD_READ , REG_CMD_WRITE = FT810_REG_CMD_WRITE , REG_CMD_DL = FT810_REG_CMD_DL , REG_TOUCH_MODE = FT810_REG_TOUCH_MODE , REG_TOUCH_ADC_MODE = FT810_REG_TOUCH_ADC_MODE , REG_TOUCH_CHARGE = FT810_REG_TOUCH_CHARGE , REG_TOUCH_SETTLE = FT810_REG_TOUCH_SETTLE , REG_TOUCH_OVERSAMPLE = FT810_REG_TOUCH_OVERSAMPLE , REG_TOUCH_RZTHRESH = FT810_REG_TOUCH_RZTHRESH , REG_TOUCH_RAW_XY = FT810_REG_TOUCH_RAW_XY , REG_TOUCH_RZ = FT810_REG_TOUCH_RZ , REG_TOUCH_SCREEN_XY = FT810_REG_TOUCH_SCREEN_XY , REG_TOUCH_TAG_XY = FT810_REG_TOUCH_TAG_XY , REG_TOUCH_TAG = FT810_REG_TOUCH_TAG , REG_TOUCH_TRANSFORM_A = FT810_REG_TOUCH_TRANSFORM_A , REG_TOUCH_TRANSFORM_B = FT810_REG_TOUCH_TRANSFORM_B , REG_TOUCH_TRANSFORM_C = FT810_REG_TOUCH_TRANSFORM_C , REG_TOUCH_TRANSFORM_D = FT810_REG_TOUCH_TRANSFORM_D , REG_TOUCH_TRANSFORM_E = FT810_REG_TOUCH_TRANSFORM_E , REG_TOUCH_TRANSFORM_F = FT810_REG_TOUCH_TRANSFORM_F , REG_TOUCH_CONFIG = FT810_REG_TOUCH_CONFIG , REG_SPI_WIDTH = FT810_REG_SPI_WIDTH , REG_TOUCH_DIRECT_XY = FT810_REG_TOUCH_DIRECT_XY , REG_TOUCH_DIRECT_Z1Z2 = FT810_REG_TOUCH_DIRECT_Z1Z2 , REG_CMDB_SPACE = FT810_REG_CMDB_SPACE , REG_CMDB_WRITE = FT810_REG_CMDB_WRITE , REG_TRACKER = FT810_REG_TRACKER , REG_TRACKER1 = FT810_REG_TRACKER1 , REG_TRACKER2 = FT810_REG_TRACKER2 , REG_TRACKER3 = FT810_REG_TRACKER3 , REG_TRACKER4 = FT810_REG_TRACKER4 , REG_MEDIAFIFO_READ = FT810_REG_MEDIAFIFO_READ , REG_MEDIAFIFO_WRITE = FT810_REG_MEDIAFIFO_WRITE }
```

相关声明：[ft8xx_register_address_t](#gaa3f6afa02b5f4bed90093f659201d008)、[REG_TRIM](#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74)、[REG_ID](#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a)、[REG_FRAMES](#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272)、[REG_CLOCK](#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64)、[REG_FREQUENCY](#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21)、[REG_RENDERMODE](#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9)、[REG_SNAPY](#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f)、[REG_SNAPSHOT](#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b)、[REG_CPURESET](#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2)、[REG_TAP_CRC](#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208)、[REG_TAP_MASK](#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd)、[REG_HCYCLE](#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2)、[REG_HOFFSET](#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85)、[REG_HSIZE](#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0)、[REG_HSYNC0](#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a)、[REG_HSYNC1](#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559)、[REG_VCYCLE](#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a)、[REG_VOFFSET](#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2)、[REG_VSIZE](#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878)、[REG_VSYNC0](#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050)、[REG_VSYNC1](#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb)、[REG_DLSWAP](#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019)、[REG_ROTATE](#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3)、[REG_OUTBITS](#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009)、[REG_DITHER](#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b)、[REG_SWIZZLE](#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6)、[REG_CSPREAD](#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d)、[REG_PCLK_POL](#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b)、[REG_PCLK](#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55)、[REG_TAG_X](#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541)、[REG_TAG_Y](#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254)、[REG_TAG](#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b)、[REG_VOL_PB](#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888)、[REG_VOL_SOUND](#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970)、[REG_SOUND](#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe)、[REG_PLAY](#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3)、[REG_GPIO_DIR](#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e)、[REG_GPIO](#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1)、[REG_GPIOX_DIR](#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788)、[REG_GPIOX](#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced)、[REG_INT_FLAGS](#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f)、[REG_INT_EN](#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697)、[REG_INT_MASK](#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d)、[REG_PLAYBACK_START](#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e)、[REG_PLAYBACK_LENGTH](#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2)、[REG_PLAYBACK_READPTR](#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d)、[REG_PLAYBACK_FREQ](#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3)、[REG_PLAYBACK_FORMAT](#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c)、[REG_PLAYBACK_LOOP](#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5)、[REG_PLAYBACK_PLAY](#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8)、[REG_PWM_HZ](#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50)、[REG_PWM_DUTY](#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265)、[REG_CMD_READ](#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68)、[REG_CMD_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69)、[REG_CMD_DL](#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87)、[REG_TOUCH_MODE](#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29)、[REG_TOUCH_ADC_MODE](#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e)、[REG_TOUCH_CHARGE](#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95)、[REG_TOUCH_SETTLE](#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb)、[REG_TOUCH_OVERSAMPLE](#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96)、[REG_TOUCH_RZTHRESH](#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e)、[REG_TOUCH_RAW_XY](#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d)、[REG_TOUCH_RZ](#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455)、[REG_TOUCH_SCREEN_XY](#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8)、[REG_TOUCH_TAG_XY](#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789)、[REG_TOUCH_TAG](#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af)、[REG_TOUCH_TRANSFORM_A](#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd)、[REG_TOUCH_TRANSFORM_B](#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745)、[REG_TOUCH_TRANSFORM_C](#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793)、[REG_TOUCH_TRANSFORM_D](#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48)、[REG_TOUCH_TRANSFORM_E](#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c)、[REG_TOUCH_TRANSFORM_F](#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315)、[REG_TOUCH_CONFIG](#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950)、[REG_SPI_WIDTH](#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848)、[REG_TOUCH_DIRECT_XY](#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd)、[REG_TOUCH_DIRECT_Z1Z2](#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0)、[REG_CMDB_SPACE](#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c)、[REG_CMDB_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464)、[REG_TRACKER](#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb)、[REG_TRACKER1](#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622)、[REG_TRACKER2](#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76)、[REG_TRACKER3](#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c)、[REG_TRACKER4](#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf)、[REG_MEDIAFIFO_READ](#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97)、[REG_MEDIAFIFO_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b)。

FT810 寄存器地址（Register Addresses）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.3\_函数（Functions）

<a id="r_ga1e9c6203ebb7cc15a736d074bd98c181"></a>

```c
static void wr8 (uint32_t address, uint8_t data)
```

相关声明：[wr8](#ga1e9c6203ebb7cc15a736d074bd98c181)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 FT8xx 存储器写入 1 字节（8 位）。

<a id="r_ga8fac4ed55f7ef9d82d8dcb0eb6f09eab"></a>

```c
static void wr16 (uint32_t address, uint16_t data)
```

相关声明：[wr16](#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 FT8xx 存储器写入 2 字节（16 位）。

<a id="r_ga3f6814650684e2c2100d8f9a36505ca0"></a>

```c
static void wr32 (uint32_t address, uint32_t data)
```

相关声明：[wr32](#ga3f6814650684e2c2100d8f9a36505ca0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 FT8xx 存储器写入 4 字节（32 位）。

<a id="r_gae96efe5496139f508083a21b2299e3d8"></a>

```c
static uint8_t rd8 (uint32_t address)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rd8](#gae96efe5496139f508083a21b2299e3d8)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 1 字节（8 位）。

<a id="r_ga2f833e24c067f88801884c93766d7ac7"></a>

```c
static uint16_t rd16 (uint32_t address)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[rd16](#ga2f833e24c067f88801884c93766d7ac7)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 2 字节（16 位）。

<a id="r_ga0c6f11426fd5412a66e4f5de0a9f0847"></a>

```c
static uint32_t rd32 (uint32_t address)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[rd32](#ga0c6f11426fd5412a66e4f5de0a9f0847)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 FT8xx 存储器读取 4 字节（32 位）。

<a id="r_gacde1ca3945cbe6c828f65051c5c3a615"></a>

```c
static void cmd (uint32_t command)
```

相关声明：[cmd](#gacde1ca3945cbe6c828f65051c5c3a615)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

<a id="r_ga7b9b6a41a878c449b107e51eba058799"></a>

```c
static void cmd_dlstart (void)
```

相关声明：[cmd_dlstart](#ga7b9b6a41a878c449b107e51eba058799)。

开始新的显示列表（Display List）。

<a id="r_ga194d7e0d47b3d195155a22f86fbe7e7f"></a>

```c
static void cmd_swap (void)
```

相关声明：[cmd_swap](#ga194d7e0d47b3d195155a22f86fbe7e7f)。

交换当前显示列表（Display List）。

<a id="r_ga4b77c199d909f946f7e271f11833533b"></a>

```c
static void cmd_fgcolor (uint32_t c)
```

相关声明：[cmd_fgcolor](#ga4b77c199d909f946f7e271f11833533b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前景色（Foreground Color）。

<a id="r_ga4467cd6c9672ac2b4c7d6b6b2e9b2f89"></a>

```c
static void cmd_bgcolor (uint32_t c)
```

相关声明：[cmd_bgcolor](#ga4467cd6c9672ac2b4c7d6b6b2e9b2f89)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置背景色（Background Color）。

<a id="r_ga1f01e0c91e369234362ed2bcf42da681"></a>

```c
static void cmd_slider (int16_t x, int16_t y, int16_t w, int16_t h, uint16_t options, uint16_t val, uint16_t range)
```

相关声明：[cmd_slider](#ga1f01e0c91e369234362ed2bcf42da681)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制滑块（Slider）。

<a id="r_gade51ff6f98a8d4cb575447bbb60cba92"></a>

```c
static void cmd_toggle (int16_t x, int16_t y, int16_t w, int16_t font, uint16_t options, uint16_t state, const char *s)
```

相关声明：[cmd_toggle](#gade51ff6f98a8d4cb575447bbb60cba92)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

绘制切换开关（Toggle Switch）。

<a id="r_gac4dc3208668383b58ec1010edeae3d2b"></a>

```c
static void cmd_track (int16_t x, int16_t y, int16_t w, int16_t h, int16_t tag)
```

相关声明：[cmd_track](#gac4dc3208668383b58ec1010edeae3d2b)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

跟踪图形对象（Graphics Object）的触摸操作。

<a id="r_gad642a54deaa36152ca4fea5e31294732"></a>

```c
static void cmd_text (int16_t x, int16_t y, int16_t font, uint16_t options, const char *s)
```

相关声明：[cmd_text](#gad642a54deaa36152ca4fea5e31294732)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制文本（Text）。

<a id="r_gabdaf9e6cd74c0d157d1673b99707e6f2"></a>

```c
static void cmd_number (int16_t x, int16_t y, int16_t font, uint16_t options, int32_t n)
```

相关声明：[cmd_number](#gabdaf9e6cd74c0d157d1673b99707e6f2)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

绘制十进制数字（Decimal Number）。

<a id="r_ga26015112ae4c62a944fe671ea2cb0bda"></a>

```c
static void cmd_calibrate (uint32_t *result)
```

相关声明：[cmd_calibrate](#ga26015112ae4c62a944fe671ea2cb0bda)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

执行触摸屏校准例程（Touch Screen Calibration Routine）。

## 12.4\_详细说明（Detailed Documentation）

<a id="ga34b42db00c62ff404a8bd7119fc62327"></a>

### `BEGIN`

```c
#define BEGIN ( prim)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_BEGIN(prim)
```

开始绘制图形图元（Graphics Primitive）。

有效图元（Primitives）定义如下：

- 位图（BITMAPS）。
- 点（POINTS）。
- 线段（LINES）。
- 折线（LINE_STRIP）。
- 右侧边带（EDGE_STRIP_R）。
- 左侧边带（EDGE_STRIP_L）。
- 上侧边带（EDGE_STRIP_A）。
- 下侧边带（EDGE_STRIP_B）。
- 矩形（RECTS）。

要绘制的图元（Primitive）由 BEGIN 命令选择。选定后持续有效，直到另一个 BEGIN 命令选择新图元。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prim` | 图形图元（Graphics Primitive）。 |

**说明（Note）**：注意（Note）：执行 VERTEX2II 或 VERTEX2F 之前，不会进行图元绘制（Primitive Drawing）。

<a id="ga3746a5c44f711b633ca618b6ebb8e75f"></a>

### `BITMAPS`

```c
#define BITMAPS FT8XX_BITMAPS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

矩形像素阵列（Rectangular Pixel Arrays），支持多种颜色格式。

<a id="ga218ebaaf7d9afe6257021f3c08e59959"></a>

### `CLEAR`

```c
#define CLEAR ( c, s, t )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_CLEAR(c, s, t)
```

将缓冲区清除为预设值（Preset Values）。

c 为 true 时，将 FT8xx 颜色缓冲区（Color Buffer）清除为预设值；为 false 时保持其值不变。RGB 通道的预设值由 CLEAR_COLOR_RGB 命令定义，透明度通道（Alpha Channel）的预设值由 CLEAR_COLOR_A 定义。

s 为 true 时，将 FT8xx 模板缓冲区（Stencil Buffer）清除为预设值；为 false 时保持其值不变。预设值由 CLEAR_STENCIL 命令定义。

t 为 true 时，将 FT8xx 标签缓冲区（Tag Buffer）清除为预设值；为 false 时保持其值不变。预设值由 CLEAR_TAG 命令定义。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 清除颜色缓冲区（Color Buffer）。 |
| `s` | 清除模板缓冲区（Stencil Buffer）。 |
| `t` | 清除标签缓冲区（Tag Buffer）。 |

<a id="gae6375b17ea6f06bf81357fe9350e1c1c"></a>

### `CLEAR_COLOR_RGB`

```c
#define CLEAR_COLOR_RGB ( red, green, blue )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_CLEAR_COLOR_RGB(red, green, blue)
```

指定红、绿、蓝通道的清除值（Clear Values）。

设置后续 CLEAR 使用的颜色值（Color Values）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `red` | 清除颜色缓冲区时使用的红色值（Red Value）。 |
| `green` | 清除颜色缓冲区时使用的绿色值（Green Value）。 |
| `blue` | 清除颜色缓冲区时使用的蓝色值（Blue Value）。 |

<a id="ga59c390601a75b4d869e7cfc58d2430bf"></a>

### `COLOR_RGB`

```c
#define COLOR_RGB ( red, green, blue )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_COLOR_RGB(red, green, blue)
```

设置当前红、绿、蓝颜色（Current Color）。

设置 FT8xx 颜色缓冲区（Color Buffer）的红、绿、蓝值，应用于后续绘制操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `red` | 当前颜色的红色值（Red Value）。 |
| `green` | 当前颜色的绿色值（Green Value）。 |
| `blue` | 当前颜色的蓝色值（Blue Value）。 |

<a id="ga486931aa64c90970e7a4110ada3d0916"></a>

### `DISPLAY`

```c
#define DISPLAY ( )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_DISPLAY()
```

结束显示列表（Display List）。

FT8xx 会忽略此命令之后的所有命令。

<a id="gaa69720d489114390d9493d397cd392b7"></a>

### `EDGE_STRIP_A`

```c
#define EDGE_STRIP_A FT8XX_EDGE_STRIP_A
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向上延伸的边缘带（Edge Strips）。

<a id="ga20ed5346e45eb4ce0e79f094c7346627"></a>

### `EDGE_STRIP_B`

```c
#define EDGE_STRIP_B FT8XX_EDGE_STRIP_B
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向下延伸的边缘带（Edge Strips）。

<a id="ga3434ce2412337ac0b7d9558ff25181d0"></a>

### `EDGE_STRIP_L`

```c
#define EDGE_STRIP_L FT8XX_EDGE_STRIP_L
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向左延伸的边缘带（Edge Strips）。

<a id="ga8c7fa2526afa79673d93b64f864d2126"></a>

### `EDGE_STRIP_R`

```c
#define EDGE_STRIP_R FT8XX_EDGE_STRIP_R
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向右延伸的边缘带（Edge Strips）。

<a id="ga569b6a4f889b0846cc0a3396f3835a17"></a>

### `END`

```c
#define END ( )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_END()
```

结束图形图元（Graphics Primitive）的绘制。

建议每个 BEGIN 都有对应的 END。不过，熟悉该机制的用户可以省略 END，以节省显示列表 RAM（Display List RAM）中的额外图形指令。

<a id="gac300cac409c1526ba5622f15472a25df"></a>

### `LINE_STRIP`

```c
#define LINE_STRIP FT8XX_LINE_STRIP
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

首尾连接的抗锯齿线（Anti-aliased Lines）。

<a id="ga8764958e4fa66c3948353226f82cedaf"></a>

### `LINE_WIDTH`

```c
#define LINE_WIDTH ( width)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_LINE_WIDTH(width)
```

指定使用 LINES 图元（Primitive）绘制的线宽（Width）。

设置所绘制线条的宽度（Line Width）。这里的宽度是线条中心到最外侧绘制像素的距离，以 1/16 像素为单位；按此单位计，有效范围为 16–4095。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `width` | 线宽（Line Width），以 1/16 像素为单位。 |

**说明（Note）**：注意（Note）：LINE_WIDTH 命令会影响 LINES、LINE_STRIP、RECTS 以及 EDGE_STRIP_A /B/R/L 图元（Primitives）。

<a id="ga321ae946de24c36489276616d13c46cd"></a>

### `LINES`

```c
#define LINES FT8XX_LINES
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

抗锯齿线（Anti-aliased Lines），宽度为 0–4095 个 1/16 像素单位。

宽度（Width）从线条中心量到边界。

<a id="gabf03e1cd7cb18b7c1daf243d4c1dde24"></a>

### `OPT_3D`

```c
#define OPT_3D FT8XX_OPT_3D
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="ga830647bc1b42665e27813a46a6a089b7"></a>

### `OPT_CENTER`

```c
#define OPT_CENTER FT8XX_OPT_CENTER
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="ga65bf92a2956ffee68057ab90be032445"></a>

### `OPT_CENTERX`

```c
#define OPT_CENTERX FT8XX_OPT_CENTERX
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）水平居中。

<a id="gaa28880f2aa7b6d8a51518189ca08382f"></a>

### `OPT_CENTERY`

```c
#define OPT_CENTERY FT8XX_OPT_CENTERY
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）垂直居中。

<a id="gaa76b9296cd6f2eb4bec3d650b73e69cc"></a>

### `OPT_FLAT`

```c
#define OPT_FLAT FT8XX_OPT_FLAT
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="ga2fab787f842bb9193c9df68cb44f93fd"></a>

### `OPT_MONO`

```c
#define OPT_MONO FT8XX_OPT_MONO
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="ga87b8705ac37fc69704f00cc2a9b8e69e"></a>

### `OPT_NOBACK`

```c
#define OPT_NOBACK FT8XX_OPT_NOBACK
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）不绘制背景。

<a id="ga37f793d8ac3af5f518d024727ce9f710"></a>

### `OPT_NODL`

```c
#define OPT_NODL FT8XX_OPT_NODL
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="gaa9bc6e351e9fb0515c69f3cd32ad5621"></a>

### `OPT_NOHANDS`

```c
#define OPT_NOHANDS FT8XX_OPT_NOHANDS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="ga1e7090a0dbcee600a5472f5fc4343824"></a>

### `OPT_NOHM`

```c
#define OPT_NOHM FT8XX_OPT_NOHM
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="ga0eb8abce5677ca0e6948ec1a003958de"></a>

### `OPT_NOPOINTER`

```c
#define OPT_NOPOINTER FT8XX_OPT_NOPOINTER
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器仪表（Gauge）没有指针。

<a id="ga190c29e3a00685c3f8c4906df37720ae"></a>

### `OPT_NOSECS`

```c
#define OPT_NOSECS FT8XX_OPT_NOSECS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="gaed772e3cf2529e698fa8e69ee73f91f9"></a>

### `OPT_NOTICKS`

```c
#define OPT_NOTICKS FT8XX_OPT_NOTICKS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器时钟控件（Clock Widget）不绘制小时刻度。

绘制仪表控件（Gauge Widget）时不绘制主刻度和次刻度（Major and Minor Ticks）。

<a id="ga53f763f1e5de09b5e51242df87af8fb8"></a>

### `OPT_RGB565`

```c
#define OPT_RGB565 FT8XX_OPT_RGB565
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="gae0088375e797e08fa3e14dc3124c1e90"></a>

### `OPT_RIGHTX`

```c
#define OPT_RIGHTX FT8XX_OPT_RIGHTX
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="gae0fef45ae7ca3a45286a19a47bd46943"></a>

### `OPT_SIGNED`

```c
#define OPT_SIGNED FT8XX_OPT_SIGNED
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

将数字视为 32 位有符号整数（Signed Integer）。

<a id="gae6910994a90091fe877b021c590c894e"></a>

### `POINTS`

```c
#define POINTS FT8XX_POINTS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

抗锯齿点（Anti-aliased Points），点半径为 1–256 像素。

<a id="ga5868720577871792983ae813837c6189"></a>

### `RECTS`

```c
#define RECTS FT8XX_RECTS
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

圆角矩形（Round-cornered Rectangles）；角部曲率可通过 LINE_WIDTH 调整。

<a id="ga5f17de6768f32dd36135de83c24d0a7b"></a>

### `TAG`

```c
#define TAG ( s)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_TAG(s)
```

为后续图形对象附加标签值（Tag Value）。

FT8xx 标签缓冲区（Tag Buffer）的初始值由 CLEAR_TAG 命令指定，并通过 CLEAR 命令生效。TAG 命令可以指定绘制到屏幕上的图形对象所使用的标签缓冲区值。除非使用 TAG_MASK 命令禁用，否则此 TAG 值会赋给后续所有对象。后续图形对象绘制完成后，便成功附加了该标签值。触摸带标签的图形对象时，REG_TOUCH_TAG 寄存器将更新为被触摸对象的标签值。如果一个显示列表中没有 TAG 命令，则该列表渲染的所有图形对象被触摸时，都会在 REG_TOUCH_TAG 中报告标签值 255。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `s` | 标签值（Tag Value），范围为 1–255。 |

<a id="ga033cea1b18c3f010aaa0293f6972069a"></a>

### `VERTEX2F`

```c
#define VERTEX2F ( x, y )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_VERTEX2F(x, y)
```

在指定坐标（Coordinate）开始图形图元（Graphics Primitives）操作。

坐标范围为 -16384 至 +16383，以 1/16 像素为单位。负 x 坐标表示相对于 (0, 0) 位于左侧虚拟屏幕的坐标，负 y 坐标表示位于上方虚拟屏幕的坐标。在负坐标位置绘制时，绘制结果不可见。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 有符号 x 坐标（Signed X-coordinate），精度为 1/16 像素。 |
| `y` | 有符号 y 坐标（Signed Y-coordinate），精度为 1/16 像素。 |

<a id="gae779df636416e900ddc15b95cf2a923c"></a>

### `VERTEX2II`

```c
#define VERTEX2II ( x, y, handle, cell )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

展开值（Value）：

```c
FT8XX_VERTEX2II(x, y, handle, cell)
```

在指定坐标（Coordinates）开始图形图元（Graphics Primitive）操作。

handle 的有效范围为 0–31，其中 16–31 的位图句柄（Bitmap Handles）专供 FT8xx 内建字体使用。

单元编号（Cell Number）是具有相同位图布局与格式的位图索引。例如，对于句柄 31，单元 65 表示最大内建字体中的字符 "A"。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | x 坐标（X-coordinate），单位为像素，范围为 0–511。 |
| `y` | y 坐标（Y-coordinate），单位为像素，范围为 0–511。 |
| `handle` | 位图句柄（Bitmap Handle）。 |
| `cell` | 单元编号（Cell Number）。 |

<a id="gabbba9344e2d9b81af6313c6b7f12276c"></a>

### `ft8xx_memory_map_t`

```c
enum ft8xx_memory_map_t
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

FT810 内存映射（Memory Map）的主要部分。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RAM_G` |  |
| `RAM_DL` |  |
| `REG_` |  |
| `RAM_CMD` |  |

<a id="gaa3f6afa02b5f4bed90093f659201d008"></a>

### `ft8xx_register_address_t`

```c
enum ft8xx_register_address_t
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

FT810 寄存器地址（Register Addresses）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `REG_TRIM` |  |
| `REG_ID` |  |
| `REG_FRAMES` |  |
| `REG_CLOCK` |  |
| `REG_FREQUENCY` |  |
| `REG_RENDERMODE` |  |
| `REG_SNAPY` |  |
| `REG_SNAPSHOT` |  |
| `REG_CPURESET` |  |
| `REG_TAP_CRC` |  |
| `REG_TAP_MASK` |  |
| `REG_HCYCLE` |  |
| `REG_HOFFSET` |  |
| `REG_HSIZE` |  |
| `REG_HSYNC0` |  |
| `REG_HSYNC1` |  |
| `REG_VCYCLE` |  |
| `REG_VOFFSET` |  |
| `REG_VSIZE` |  |
| `REG_VSYNC0` |  |
| `REG_VSYNC1` |  |
| `REG_DLSWAP` |  |
| `REG_ROTATE` |  |
| `REG_OUTBITS` |  |
| `REG_DITHER` |  |
| `REG_SWIZZLE` |  |
| `REG_CSPREAD` |  |
| `REG_PCLK_POL` |  |
| `REG_PCLK` |  |
| `REG_TAG_X` |  |
| `REG_TAG_Y` |  |
| `REG_TAG` |  |
| `REG_VOL_PB` |  |
| `REG_VOL_SOUND` |  |
| `REG_SOUND` |  |
| `REG_PLAY` |  |
| `REG_GPIO_DIR` |  |
| `REG_GPIO` |  |
| `REG_GPIOX_DIR` |  |
| `REG_GPIOX` |  |
| `REG_INT_FLAGS` |  |
| `REG_INT_EN` |  |
| `REG_INT_MASK` |  |
| `REG_PLAYBACK_START` |  |
| `REG_PLAYBACK_LENGTH` |  |
| `REG_PLAYBACK_READPTR` |  |
| `REG_PLAYBACK_FREQ` |  |
| `REG_PLAYBACK_FORMAT` |  |
| `REG_PLAYBACK_LOOP` |  |
| `REG_PLAYBACK_PLAY` |  |
| `REG_PWM_HZ` |  |
| `REG_PWM_DUTY` |  |
| `REG_CMD_READ` |  |
| `REG_CMD_WRITE` |  |
| `REG_CMD_DL` |  |
| `REG_TOUCH_MODE` |  |
| `REG_TOUCH_ADC_MODE` |  |
| `REG_TOUCH_CHARGE` |  |
| `REG_TOUCH_SETTLE` |  |
| `REG_TOUCH_OVERSAMPLE` |  |
| `REG_TOUCH_RZTHRESH` |  |
| `REG_TOUCH_RAW_XY` |  |
| `REG_TOUCH_RZ` |  |
| `REG_TOUCH_SCREEN_XY` |  |
| `REG_TOUCH_TAG_XY` |  |
| `REG_TOUCH_TAG` |  |
| `REG_TOUCH_TRANSFORM_A` |  |
| `REG_TOUCH_TRANSFORM_B` |  |
| `REG_TOUCH_TRANSFORM_C` |  |
| `REG_TOUCH_TRANSFORM_D` |  |
| `REG_TOUCH_TRANSFORM_E` |  |
| `REG_TOUCH_TRANSFORM_F` |  |
| `REG_TOUCH_CONFIG` |  |
| `REG_SPI_WIDTH` |  |
| `REG_TOUCH_DIRECT_XY` |  |
| `REG_TOUCH_DIRECT_Z1Z2` |  |
| `REG_CMDB_SPACE` |  |
| `REG_CMDB_WRITE` |  |
| `REG_TRACKER` |  |
| `REG_TRACKER1` |  |
| `REG_TRACKER2` |  |
| `REG_TRACKER3` |  |
| `REG_TRACKER4` |  |
| `REG_MEDIAFIFO_READ` |  |
| `REG_MEDIAFIFO_WRITE` |  |

<a id="gacde1ca3945cbe6c828f65051c5c3a615"></a>

### `cmd()`

```c
void cmd ( uint32_t command)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `command` | 要执行的显示列表命令（Display List Command）。 |

<a id="ga4467cd6c9672ac2b4c7d6b6b2e9b2f89"></a>

### `cmd_bgcolor()`

```c
void cmd_bgcolor ( uint32_t c)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

设置背景色（Background Color）。

新的背景颜色（Background Color），以 24 位 RGB 数值表示。红色占最高 8 位，蓝色占最低 8 位，因此 0xff0000 表示亮红色。背景颜色适用于用户无法移动的部分，例如仪表和滑块等控件背后的区域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 要设置的颜色（Color）。 |

<a id="ga26015112ae4c62a944fe671ea2cb0bda"></a>

### `cmd_calibrate()`

```c
void cmd_calibrate ( uint32_t * result)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

执行触摸屏校准例程（Touch Screen Calibration Routine）。

校准过程（Calibration Procedure）从触摸屏采集三个触点，再计算适当矩阵并加载到 REG_TOUCH_TRANSFORM_A-F。使用时，先创建显示列表（Display List），再使用 CMD_CALIBRATE。协处理器引擎（Co-processor Engine）会在当前显示列表上叠加触摸目标，收集校准输入并更新 REG_TOUCH_TRANSFORM_A-F。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `result` | 校准结果（Calibration Result）；校准失败时写入 0。 |

<a id="ga7b9b6a41a878c449b107e51eba058799"></a>

### `cmd_dlstart()`

```c
void cmd_dlstart ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

开始新的显示列表（Display List）。

<a id="ga4b77c199d909f946f7e271f11833533b"></a>

### `cmd_fgcolor()`

```c
void cmd_fgcolor ( uint32_t c)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

设置前景色（Foreground Color）。

新的前景颜色（Foreground Color），以 24 位 RGB 数值表示。红色占最高 8 位，蓝色占最低 8 位，因此 0xff0000 表示亮红色。前景颜色适用于用户可以移动的部分，例如手柄和按钮等操作提示部件（Affordances）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `c` | 要设置的颜色（Color）。 |

<a id="gabdaf9e6cd74c0d157d1673b99707e6f2"></a>

### `cmd_number()`

```c
void cmd_number ( int16_t x, int16_t y, int16_t font, uint16_t options, int32_t n )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

绘制十进制数字（Decimal Number）。

默认情况下，(x, y) 是文本左上角像素。OPT_CENTERX 使文本水平居中，OPT_CENTERY 使文本垂直居中，OPT_CENTER 使文本在两个方向上都居中。OPT_RIGHTX 使文本右对齐，此时 x 是最右侧像素。数字默认不显示前导零（Leading Zeroes）；如果选项中指定了 1–9 的宽度，必要时会用前导零补足该宽度。设置 OPT_SIGNED 时，将数字按有符号数（Signed Number）处理，负数前加负号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 文本基准位置的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 文本基准位置的 y 坐标（Y-coordinate），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `n` | 要显示的数字（Number）。 |

<a id="ga1f01e0c91e369234362ed2bcf42da681"></a>

### `cmd_slider()`

```c
void cmd_slider ( int16_t x, int16_t y, int16_t w, int16_t h, uint16_t options, uint16_t val, uint16_t range )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

绘制滑块（Slider）。

宽度大于高度时，水平绘制滚动条（Scroll Bar）；高度大于宽度时，垂直绘制滚动条。

滑块（Slider）默认带 3D 效果；FT8XX_OPT_FLAT 会移除该效果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 滑块左上角的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 滑块左上角的 y 坐标（Y-coordinate），单位为像素。 |
| `w` | 滑块宽度（Slider Width），单位为像素。 |
| `h` | 滑块高度（Slider Height），单位为像素。 |
| `options` | 要应用的选项（Options）。 |
| `val` | 滑块显示值（Slider Value），范围为 0 至 range，包含两端。 |
| `range` | 最大值（Maximum Value）。 |

<a id="ga194d7e0d47b3d195155a22f86fbe7e7f"></a>

### `cmd_swap()`

```c
void cmd_swap ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

交换当前显示列表（Display List）。

<a id="gad642a54deaa36152ca4fea5e31294732"></a>

### `cmd_text()`

```c
void cmd_text ( int16_t x, int16_t y, int16_t font, uint16_t options, const char * s )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

绘制文本（Text）。

默认情况下，(x,y) 是文本左上角像素，options 值为 0。OPT_CENTERX 使文本水平居中，OPT_CENTERY 使文本垂直居中，OPT_CENTER 使文本在两个方向上都居中。OPT_RIGHTX 使文本右对齐，此时 x 是最右侧像素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 文本基准位置的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 文本基准位置的 y 坐标（Y-coordinate），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `s` | 要显示的字符串（Character String），以空字符（Null Character）终止。 |

<a id="gade51ff6f98a8d4cb575447bbb60cba92"></a>

### `cmd_toggle()`

```c
void cmd_toggle ( int16_t x, int16_t y, int16_t w, int16_t font, uint16_t options, uint16_t state, const char * s )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

绘制切换开关（Toggle Switch）。

开关控件（Toggle）默认带 3D 效果，option 值为 0。FT8XX_OPT_FLAT 移除该效果，其值为 256。

在 s 中，值为 255 的字符（可写为 `\xff`）分隔关闭（Off）与开启（On）状态的标签。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 开关控件（Toggle）左上角的 x 坐标，单位为像素。 |
| `y` | 开关控件（Toggle）左上角的 y 坐标，单位为像素。 |
| `w` | 开关控件宽度（Toggle Width），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `state` | 开关控件状态（Toggle State）：0 表示关闭，65535 表示开启。 |
| `s` | 开关控件的字符串标签（String Label）。 |

<a id="gac4dc3208668383b58ec1010edeae3d2b"></a>

### `cmd_track()`

```c
void cmd_track ( int16_t x, int16_t y, int16_t w, int16_t h, int16_t tag )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

跟踪图形对象（Graphics Object）的触摸操作。

此命令使协处理器引擎（Co-processor Engine）跟踪具有一个有效标签值（Tag Value）的特定图形对象上的触摸。随后，引擎按照 LCD 显示面板的帧率周期性更新 REG_TRACKER。

协处理器引擎（Co-processor Engine）以旋转跟踪模式（Rotary Tracker Mode）和线性跟踪模式（Linear Tracker Mode）跟踪图形对象：

- 旋转跟踪模式（Rotary Tracker Mode）：跟踪触点与标签值指定的图形对象中心之间的角度。数值以一圈的 1/65536 为单位：0 表示从中心垂直向下，0x4000 表示向左，0x8000 表示向上，0xC000 表示向右。
- 线性跟踪模式（Linear Tracker Mode）：w 大于 h 时，跟踪触点相对于标签值指定图形对象宽度的距离；w 不大于 h 时，跟踪其相对于高度的距离。数值以图形对象宽度或高度的 1/65536 为单位。触点距离是从图形对象左上角像素到触点坐标的距离。

在线性跟踪功能（Linear Tracker）中，x 和 y 分别表示跟踪区域左上角的 x、y 坐标，单位均为像素。

在旋转跟踪功能（Rotary Tracker）中，x 和 y 分别表示跟踪区域中心的 x、y 坐标，单位均为像素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | x 坐标（X-coordinate）。 |
| `y` | y 坐标（Y-coordinate）。 |
| `w` | 跟踪区域宽度（Track Area Width），单位为像素。 |
| `h` | 跟踪区域高度（Track Area Height），单位为像素。 |
| `tag` | 要跟踪的图形对象标签（Tag），范围为 1–255。 |

**说明（Note）**：注意（Note）：w 和 h 为 (1, 1) 表示旋转跟踪器（Rotary Tracker），在 REG_TRACKER 中报告角度值；为 (0, 0) 则禁用协处理器引擎的跟踪功能。

<a id="ga2f833e24c067f88801884c93766d7ac7"></a>

### `rd16()`

```c
uint16_t rd16 ( uint32_t address)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

从 FT8xx 存储器读取 2 字节（16 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="ga0c6f11426fd5412a66e4f5de0a9f0847"></a>

### `rd32()`

```c
uint32_t rd32 ( uint32_t address)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

从 FT8xx 存储器读取 4 字节（32 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="gae96efe5496139f508083a21b2299e3d8"></a>

### `rd8()`

```c
uint8_t rd8 ( uint32_t address)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

从 FT8xx 存储器读取 1 字节（8 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要读取的内存地址（memory address）。 |

**返回（Returns）**：返回值：从内存读取的值。

<a id="ga8fac4ed55f7ef9d82d8dcb0eb6f09eab"></a>

### `wr16()`

```c
void wr16 ( uint32_t address, uint16_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向 FT8xx 存储器写入 2 字节（16 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要写入的内存地址。 |
| `data` | 要写入的值。 |

<a id="ga3f6814650684e2c2100d8f9a36505ca0"></a>

### `wr32()`

```c
void wr32 ( uint32_t address, uint32_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向 FT8xx 存储器写入 4 字节（32 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要写入的内存地址。 |
| `data` | 要写入的值。 |

<a id="ga1e9c6203ebb7cc15a736d074bd98c181"></a>

### `wr8()`

```c
void wr8 ( uint32_t address, uint8_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h>
```

向 FT8xx 存储器写入 1 字节（8 位）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `address` | 要写入的内存地址。 |
| `data` | 待写入的字节（Byte）。 |


## 12.5\_原页交叉引用（Cross References）

- [FT8XX_OPT_3D](P010_FT8xx 协处理器（Co-processor）.md#ga304badab7bd34208d499b199080fb557)
- [FT8XX_OPT_RGB565](P010_FT8xx 协处理器（Co-processor）.md#ga3a79c1128bdb9fe094843688691a085c)
- [FT8XX_OPT_MONO](P010_FT8xx 协处理器（Co-processor）.md#ga415760ddf94db71ee9a504300bac4661)
- [FT8XX_OPT_NODL](P010_FT8xx 协处理器（Co-processor）.md#gacc953470460b083c0b8bd9ebbc8ed03b)
- [FT8XX_OPT_FLAT](P010_FT8xx 协处理器（Co-processor）.md#ga160b331fb401eec023e0992c6f4c6331)
- [FT8XX_OPT_SIGNED](P010_FT8xx 协处理器（Co-processor）.md#ga5a58155896cdb2d0f1693d203706ce93)
- [FT8XX_OPT_CENTERX](P010_FT8xx 协处理器（Co-processor）.md#gac2d1ccbb99eaa032ed9d39fc01d32c66)
- [FT8XX_OPT_CENTERY](P010_FT8xx 协处理器（Co-processor）.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a)
- [FT8XX_OPT_CENTER](P010_FT8xx 协处理器（Co-processor）.md#ga013968a6bf9534265c897ab1f4018eb0)
- [FT8XX_OPT_RIGHTX](P010_FT8xx 协处理器（Co-processor）.md#gac864c155bc2121bf8d3954e1ed8dbb7e)
- [FT8XX_OPT_NOBACK](P010_FT8xx 协处理器（Co-processor）.md#gacb08df4fac256cbf808b133d4159aa29)
- [FT8XX_OPT_NOTICKS](P010_FT8xx 协处理器（Co-processor）.md#ga50f4fac88e4f4b558450adcda33dae93)
- [FT8XX_OPT_NOHM](P010_FT8xx 协处理器（Co-processor）.md#ga79938d9c1193d44a527ca8c158117a86)
- [FT8XX_OPT_NOPOINTER](P010_FT8xx 协处理器（Co-processor）.md#ga1a9838a862ec166bfe95d64144b9a052)
- [FT8XX_OPT_NOSECS](P010_FT8xx 协处理器（Co-processor）.md#ga6416f4282d2c483d2adba8c1215ab638)
- [FT8XX_OPT_NOHANDS](P010_FT8xx 协处理器（Co-processor）.md#gade56de46694ca420460c1ceb26a33120)
- [位图（FT8XX_BITMAPS）。](P011_FT8xx 显示列表（Display list）.md#ga28f7596c367f67f73d701b792300aa09)
- [点（FT8XX_POINTS）。](P011_FT8xx 显示列表（Display list）.md#ga1d6f49b3817f9927fa1cd3cd42820490)
- [线段（FT8XX_LINES）。](P011_FT8xx 显示列表（Display list）.md#ga62bcf30c7a9eae4c468e1c7de144ad01)
- [折线（FT8XX_LINE_STRIP）。](P011_FT8xx 显示列表（Display list）.md#gac1b1188c36a4078e7db50d3c5aee7d25)
- [右侧边带（FT8XX_EDGE_STRIP_R）。](P011_FT8xx 显示列表（Display list）.md#ga0b3ce2828323978e9648bfd07caa1065)
- [左侧边带（FT8XX_EDGE_STRIP_L）。](P011_FT8xx 显示列表（Display list）.md#ga97229abf592bba4039f19a98451cdc5b)
- [上侧边带（FT8XX_EDGE_STRIP_A）。](P011_FT8xx 显示列表（Display list）.md#gaf5ad60bbe137dbf64281ad8d0be051e0)
- [下侧边带（FT8XX_EDGE_STRIP_B）。](P011_FT8xx 显示列表（Display list）.md#ga9aff3a3c58e12b990130271e845662a8)
- [矩形（FT8XX_RECTS）。](P011_FT8xx 显示列表（Display list）.md#ga05077568fea624ed7e3f9e3f6e8d72b8)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/drivers/misc/ft8xx/ft8xx_reference_api.h](../api_file_audio_gateway_reference/P015_zephyr__drivers__misc__ft8xx__ft8xx_reference_api.h_文件参考.md)
- [FT8XX_BEGIN](P011_FT8xx 显示列表（Display list）.md#ga25324ac604e037baf26cdd37341bee44)
- [FT8XX_CLEAR](P011_FT8xx 显示列表（Display list）.md#gab0fb60eec6f4c3b68d47f61886e7b933)
- [FT8XX_CLEAR_COLOR_RGB](P011_FT8xx 显示列表（Display list）.md#ga180b0ed70243277462cf303bc788e094)
- [FT8XX_COLOR_RGB](P011_FT8xx 显示列表（Display list）.md#ga3bc794705028fc7e8e1b742db180055d)
- [FT8XX_DISPLAY](P011_FT8xx 显示列表（Display list）.md#ga135472b1cdf30d4bd69372e36c9960ce)
- [FT8XX_END](P011_FT8xx 显示列表（Display list）.md#ga8a9d0eb6521459eb7ce50b397de194d9)
- [FT8XX_LINE_WIDTH](P011_FT8xx 显示列表（Display list）.md#ga1d22204625ef070a6b8d16af7ad97578)
- [FT8XX_TAG](P011_FT8xx 显示列表（Display list）.md#gab0721051bb3f3cb9f555f696f36dfbbf)
- [FT8XX_VERTEX2F](P011_FT8xx 显示列表（Display list）.md#ga2648ab069991c02b2e8de62bf13913ab)
- [FT8XX_VERTEX2II](P011_FT8xx 显示列表（Display list）.md#ga560836cd8c85599f24e5623a3e286b12)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ft8xx__dl_html_ga25324ac604e037baf26cdd37341bee44"></a>
<a id="agroup__ft8xx__dl_html_gab0fb60eec6f4c3b68d47f61886e7b933"></a>
<a id="agroup__ft8xx__dl_html_ga180b0ed70243277462cf303bc788e094"></a>
<a id="agroup__ft8xx__dl_html_ga3bc794705028fc7e8e1b742db180055d"></a>
<a id="agroup__ft8xx__dl_html_ga135472b1cdf30d4bd69372e36c9960ce"></a>
<a id="agroup__ft8xx__dl_html_ga8a9d0eb6521459eb7ce50b397de194d9"></a>
<a id="agroup__ft8xx__dl_html_ga1d22204625ef070a6b8d16af7ad97578"></a>
<a id="agroup__ft8xx__dl_html_gab0721051bb3f3cb9f555f696f36dfbbf"></a>
<a id="agroup__ft8xx__dl_html_ga2648ab069991c02b2e8de62bf13913ab"></a>
<a id="agroup__ft8xx__dl_html_ga560836cd8c85599f24e5623a3e286b12"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4"></a>
<a id="ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84"></a>
<a id="ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779"></a>
<a id="ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97"></a>
<a id="ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_FT8xx 显示列表（Display list）.md) · [返回大纲](大纲.md) · [下一章](P013_Grow R502A API主题.md)
