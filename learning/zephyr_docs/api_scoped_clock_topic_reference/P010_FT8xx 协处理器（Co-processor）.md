---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-10
title: FT8xx 协处理器（Co-processor）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_FT8xx 协处理器（Co-processor）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8xx 协处理器引擎函数。

<a id="details"></a>

FT8xx 协处理器引擎函数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_ga304badab7bd34208d499b199080fb557"></a>

```c
#define FT8XX_OPT_3D 0
```

相关声明：[FT8XX_OPT_3D](#ga304badab7bd34208d499b199080fb557)。

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="r_ga3a79c1128bdb9fe094843688691a085c"></a>

```c
#define FT8XX_OPT_RGB565 0
```

相关声明：[FT8XX_OPT_RGB565](#ga3a79c1128bdb9fe094843688691a085c)。

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="r_ga415760ddf94db71ee9a504300bac4661"></a>

```c
#define FT8XX_OPT_MONO 1
```

相关声明：[FT8XX_OPT_MONO](#ga415760ddf94db71ee9a504300bac4661)。

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="r_gacc953470460b083c0b8bd9ebbc8ed03b"></a>

```c
#define FT8XX_OPT_NODL 2
```

相关声明：[FT8XX_OPT_NODL](#gacc953470460b083c0b8bd9ebbc8ed03b)。

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="r_ga160b331fb401eec023e0992c6f4c6331"></a>

```c
#define FT8XX_OPT_FLAT 256
```

相关声明：[FT8XX_OPT_FLAT](#ga160b331fb401eec023e0992c6f4c6331)。

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="r_ga5a58155896cdb2d0f1693d203706ce93"></a>

```c
#define FT8XX_OPT_SIGNED 256
```

相关声明：[FT8XX_OPT_SIGNED](#ga5a58155896cdb2d0f1693d203706ce93)。

将数字视为 32 位有符号整数（Signed Integer）。

<a id="r_gac2d1ccbb99eaa032ed9d39fc01d32c66"></a>

```c
#define FT8XX_OPT_CENTERX 512
```

相关声明：[FT8XX_OPT_CENTERX](#gac2d1ccbb99eaa032ed9d39fc01d32c66)。

协处理器控件（Co-processor Widget）水平居中。

<a id="r_ga65b3a1e29ae425b2f1c3e66b4ea1449a"></a>

```c
#define FT8XX_OPT_CENTERY 1024
```

相关声明：[FT8XX_OPT_CENTERY](#ga65b3a1e29ae425b2f1c3e66b4ea1449a)。

协处理器控件（Co-processor Widget）垂直居中。

<a id="r_ga013968a6bf9534265c897ab1f4018eb0"></a>

```c
#define FT8XX_OPT_CENTER 1536
```

相关声明：[FT8XX_OPT_CENTER](#ga013968a6bf9534265c897ab1f4018eb0)。

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="r_gac864c155bc2121bf8d3954e1ed8dbb7e"></a>

```c
#define FT8XX_OPT_RIGHTX 2048
```

相关声明：[FT8XX_OPT_RIGHTX](#gac864c155bc2121bf8d3954e1ed8dbb7e)。

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="r_gacb08df4fac256cbf808b133d4159aa29"></a>

```c
#define FT8XX_OPT_NOBACK 4096
```

相关声明：[FT8XX_OPT_NOBACK](#gacb08df4fac256cbf808b133d4159aa29)。

协处理器控件（Co-processor Widget）不绘制背景。

<a id="r_ga50f4fac88e4f4b558450adcda33dae93"></a>

```c
#define FT8XX_OPT_NOTICKS 8192
```

相关声明：[FT8XX_OPT_NOTICKS](#ga50f4fac88e4f4b558450adcda33dae93)。

协处理器时钟控件（Clock Widget）不绘制小时刻度。

<a id="r_ga79938d9c1193d44a527ca8c158117a86"></a>

```c
#define FT8XX_OPT_NOHM 16384
```

相关声明：[FT8XX_OPT_NOHM](#ga79938d9c1193d44a527ca8c158117a86)。

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="r_ga1a9838a862ec166bfe95d64144b9a052"></a>

```c
#define FT8XX_OPT_NOPOINTER 16384
```

相关声明：[FT8XX_OPT_NOPOINTER](#ga1a9838a862ec166bfe95d64144b9a052)。

协处理器仪表（Gauge）没有指针。

<a id="r_ga6416f4282d2c483d2adba8c1215ab638"></a>

```c
#define FT8XX_OPT_NOSECS 32768
```

相关声明：[FT8XX_OPT_NOSECS](#ga6416f4282d2c483d2adba8c1215ab638)。

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="r_gade56de46694ca420460c1ceb26a33120"></a>

```c
#define FT8XX_OPT_NOHANDS 49152
```

相关声明：[FT8XX_OPT_NOHANDS](#gade56de46694ca420460c1ceb26a33120)。

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.2\_函数（Functions）

<a id="r_ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea"></a>

```c
void ft8xx_copro_cmd (const struct device *dev, uint32_t cmd)
```

相关声明：[ft8xx_copro_cmd](#ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[cmd](P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)。

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

<a id="r_gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9"></a>

```c
void ft8xx_copro_cmd_dlstart (const struct device *dev)
```

相关声明：[ft8xx_copro_cmd_dlstart](#gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9)、[device](../device_reference/P002_设备对象结构.md)。

开始新的显示列表（Display List）。

<a id="r_ga3605bc23d9555ac51fc6292cb6f2a02c"></a>

```c
void ft8xx_copro_cmd_swap (const struct device *dev)
```

相关声明：[ft8xx_copro_cmd_swap](#ga3605bc23d9555ac51fc6292cb6f2a02c)、[device](../device_reference/P002_设备对象结构.md)。

交换当前显示列表（Display List）。

<a id="r_gab47b9c79db405686168cf1516ea0a00d"></a>

```c
void ft8xx_copro_cmd_fgcolor (const struct device *dev, uint32_t color)
```

相关声明：[ft8xx_copro_cmd_fgcolor](#gab47b9c79db405686168cf1516ea0a00d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前景色（Foreground Color）。

<a id="r_gafa5c3fe004456cfd531edf781c11c00d"></a>

```c
void ft8xx_copro_cmd_bgcolor (const struct device *dev, uint32_t color)
```

相关声明：[ft8xx_copro_cmd_bgcolor](#gafa5c3fe004456cfd531edf781c11c00d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置背景色（Background Color）。

<a id="r_ga3b9454e8a6a824bd87c675037047c069"></a>

```c
void ft8xx_copro_cmd_slider (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t height, uint16_t options, uint16_t val, uint16_t range)
```

相关声明：[ft8xx_copro_cmd_slider](#ga3b9454e8a6a824bd87c675037047c069)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制滑块（Slider）。

<a id="r_ga93e61278bacec915bb360244ab43dbb7"></a>

```c
void ft8xx_copro_cmd_toggle (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t font, uint16_t options, uint16_t state, const char *string)
```

相关声明：[ft8xx_copro_cmd_toggle](#ga93e61278bacec915bb360244ab43dbb7)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

绘制切换开关（Toggle Switch）。

<a id="r_gac946f044f2fbb6381ea4af268084d828"></a>

```c
void ft8xx_copro_cmd_track (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t height, int16_t tag)
```

相关声明：[ft8xx_copro_cmd_track](#gac946f044f2fbb6381ea4af268084d828)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

跟踪图形对象（Graphics Object）的触摸操作。

<a id="r_ga35d0500600e8c1d1df653952fab5d86c"></a>

```c
void ft8xx_copro_cmd_text (const struct device *dev, int16_t x, int16_t y, int16_t font, uint16_t options, const char *string)
```

相关声明：[ft8xx_copro_cmd_text](#ga35d0500600e8c1d1df653952fab5d86c)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制文本（Text）。

<a id="r_ga72e1feafde7bb230cd798ba23f414de9"></a>

```c
void ft8xx_copro_cmd_number (const struct device *dev, int16_t x, int16_t y, int16_t font, uint16_t options, int32_t number)
```

相关声明：[ft8xx_copro_cmd_number](#ga72e1feafde7bb230cd798ba23f414de9)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

绘制十进制数字（Decimal Number）。

<a id="r_gacc68ff73da90a9c822185f2ceba5a910"></a>

```c
void ft8xx_copro_cmd_calibrate (const struct device *dev, uint32_t *result)
```

相关声明：[ft8xx_copro_cmd_calibrate](#gacc68ff73da90a9c822185f2ceba5a910)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

执行触摸屏校准例程（Touch Screen Calibration Routine）。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga304badab7bd34208d499b199080fb557"></a>

### `FT8XX_OPT_3D`

```c
#define FT8XX_OPT_3D 0
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="ga013968a6bf9534265c897ab1f4018eb0"></a>

### `FT8XX_OPT_CENTER`

```c
#define FT8XX_OPT_CENTER 1536
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="gac2d1ccbb99eaa032ed9d39fc01d32c66"></a>

### `FT8XX_OPT_CENTERX`

```c
#define FT8XX_OPT_CENTERX 512
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）水平居中。

<a id="ga65b3a1e29ae425b2f1c3e66b4ea1449a"></a>

### `FT8XX_OPT_CENTERY`

```c
#define FT8XX_OPT_CENTERY 1024
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）垂直居中。

<a id="ga160b331fb401eec023e0992c6f4c6331"></a>

### `FT8XX_OPT_FLAT`

```c
#define FT8XX_OPT_FLAT 256
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="ga415760ddf94db71ee9a504300bac4661"></a>

### `FT8XX_OPT_MONO`

```c
#define FT8XX_OPT_MONO 1
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="gacb08df4fac256cbf808b133d4159aa29"></a>

### `FT8XX_OPT_NOBACK`

```c
#define FT8XX_OPT_NOBACK 4096
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）不绘制背景。

<a id="gacc953470460b083c0b8bd9ebbc8ed03b"></a>

### `FT8XX_OPT_NODL`

```c
#define FT8XX_OPT_NODL 2
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="gade56de46694ca420460c1ceb26a33120"></a>

### `FT8XX_OPT_NOHANDS`

```c
#define FT8XX_OPT_NOHANDS 49152
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="ga79938d9c1193d44a527ca8c158117a86"></a>

### `FT8XX_OPT_NOHM`

```c
#define FT8XX_OPT_NOHM 16384
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="ga1a9838a862ec166bfe95d64144b9a052"></a>

### `FT8XX_OPT_NOPOINTER`

```c
#define FT8XX_OPT_NOPOINTER 16384
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器仪表（Gauge）没有指针。

<a id="ga6416f4282d2c483d2adba8c1215ab638"></a>

### `FT8XX_OPT_NOSECS`

```c
#define FT8XX_OPT_NOSECS 32768
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="ga50f4fac88e4f4b558450adcda33dae93"></a>

### `FT8XX_OPT_NOTICKS`

```c
#define FT8XX_OPT_NOTICKS 8192
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器时钟控件（Clock Widget）不绘制小时刻度。

绘制仪表控件（Gauge Widget）时不绘制主刻度和次刻度（Major and Minor Ticks）。

<a id="ga3a79c1128bdb9fe094843688691a085c"></a>

### `FT8XX_OPT_RGB565`

```c
#define FT8XX_OPT_RGB565 0
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="gac864c155bc2121bf8d3954e1ed8dbb7e"></a>

### `FT8XX_OPT_RIGHTX`

```c
#define FT8XX_OPT_RIGHTX 2048
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="ga5a58155896cdb2d0f1693d203706ce93"></a>

### `FT8XX_OPT_SIGNED`

```c
#define FT8XX_OPT_SIGNED 256
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

将数字视为 32 位有符号整数（Signed Integer）。

<a id="ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea"></a>

### `ft8xx_copro_cmd()`

```c
void ft8xx_copro_cmd ( const struct device * dev, uint32_t cmd )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `cmd` | 要执行的显示列表命令（Display List Command）。 |

<a id="gafa5c3fe004456cfd531edf781c11c00d"></a>

### `ft8xx_copro_cmd_bgcolor()`

```c
void ft8xx_copro_cmd_bgcolor ( const struct device * dev, uint32_t color )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

设置背景色（Background Color）。

新的背景颜色（Background Color），以 24 位 RGB 数值表示。红色占最高 8 位，蓝色占最低 8 位，因此 0xff0000 表示亮红色。背景颜色适用于用户无法移动的部分，例如仪表和滑块等控件背后的区域。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `color` | 要设置的颜色（Color）。 |

<a id="gacc68ff73da90a9c822185f2ceba5a910"></a>

### `ft8xx_copro_cmd_calibrate()`

```c
void ft8xx_copro_cmd_calibrate ( const struct device * dev, uint32_t * result )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

执行触摸屏校准例程（Touch Screen Calibration Routine）。

校准过程（Calibration Procedure）从触摸屏采集三个触点，再计算适当矩阵并加载到 REG_TOUCH_TRANSFORM_A-F。使用时，先创建显示列表（Display List），再使用 CMD_CALIBRATE。协处理器引擎（Co-processor Engine）会在当前显示列表上叠加触摸目标，收集校准输入并更新 REG_TOUCH_TRANSFORM_A-F。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `result` | 校准结果（Calibration Result）；校准失败时写入 0。 |

<a id="gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9"></a>

### `ft8xx_copro_cmd_dlstart()`

```c
void ft8xx_copro_cmd_dlstart ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

开始新的显示列表（Display List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |

<a id="gab47b9c79db405686168cf1516ea0a00d"></a>

### `ft8xx_copro_cmd_fgcolor()`

```c
void ft8xx_copro_cmd_fgcolor ( const struct device * dev, uint32_t color )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

设置前景色（Foreground Color）。

新的前景颜色（Foreground Color），以 24 位 RGB 数值表示。红色占最高 8 位，蓝色占最低 8 位，因此 0xff0000 表示亮红色。前景颜色适用于用户可以移动的部分，例如手柄和按钮等操作提示部件（Affordances）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `color` | 要设置的颜色（Color）。 |

<a id="ga72e1feafde7bb230cd798ba23f414de9"></a>

### `ft8xx_copro_cmd_number()`

```c
void ft8xx_copro_cmd_number ( const struct device * dev, int16_t x, int16_t y, int16_t font, uint16_t options, int32_t number )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

绘制十进制数字（Decimal Number）。

默认情况下，(x, y) 是文本左上角像素。FT8XX_OPT_CENTERX 使文本水平居中，FT8XX_OPT_CENTERY 使文本垂直居中，FT8XX_OPT_CENTER 使文本在两个方向上都居中。FT8XX_OPT_RIGHTX 使文本右对齐，此时 x 是最右侧像素。数字默认不显示前导零（Leading Zeroes）；如果选项中指定了 1–9 的宽度，必要时会用前导零补足该宽度。设置 FT8XX_OPT_SIGNED 时，将数字按有符号数（Signed Number）处理，负数前加负号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `x` | 文本基准位置的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 文本基准位置的 y 坐标（Y-coordinate），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `number` | 要显示的数字（Number）。 |

<a id="ga3b9454e8a6a824bd87c675037047c069"></a>

### `ft8xx_copro_cmd_slider()`

```c
void ft8xx_copro_cmd_slider ( const struct device * dev, int16_t x, int16_t y, int16_t width, int16_t height, uint16_t options, uint16_t val, uint16_t range )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

绘制滑块（Slider）。

宽度大于高度时，水平绘制滚动条（Scroll Bar）；高度大于宽度时，垂直绘制滚动条。

滑块（Slider）默认带 3D 效果；FT8XX_OPT_FLAT 会移除该效果。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `x` | 滑块左上角的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 滑块左上角的 y 坐标（Y-coordinate），单位为像素。 |
| `width` | 滑块宽度（Slider Width），单位为像素。 |
| `height` | 滑块高度（Slider Height），单位为像素。 |
| `options` | 要应用的选项（Options）。 |
| `val` | 滑块显示值（Slider Value），范围为 0 至 range，包含两端。 |
| `range` | 最大值（Maximum Value）。 |

<a id="ga3605bc23d9555ac51fc6292cb6f2a02c"></a>

### `ft8xx_copro_cmd_swap()`

```c
void ft8xx_copro_cmd_swap ( const struct device * dev)
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

交换当前显示列表（Display List）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |

<a id="ga35d0500600e8c1d1df653952fab5d86c"></a>

### `ft8xx_copro_cmd_text()`

```c
void ft8xx_copro_cmd_text ( const struct device * dev, int16_t x, int16_t y, int16_t font, uint16_t options, const char * string )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

绘制文本（Text）。

默认情况下，(x, y) 是文本左上角像素，options 值为 0。FT8XX_OPT_CENTERX 使文本水平居中，FT8XX_OPT_CENTERY 使文本垂直居中，FT8XX_OPT_CENTER 使文本在两个方向上都居中。FT8XX_OPT_RIGHTX 使文本右对齐，此时 x 是最右侧像素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `x` | 文本基准位置的 x 坐标（X-coordinate），单位为像素。 |
| `y` | 文本基准位置的 y 坐标（Y-coordinate），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `string` | 要显示的字符串（Character String），以空字符（Null Character）终止。 |

<a id="ga93e61278bacec915bb360244ab43dbb7"></a>

### `ft8xx_copro_cmd_toggle()`

```c
void ft8xx_copro_cmd_toggle ( const struct device * dev, int16_t x, int16_t y, int16_t width, int16_t font, uint16_t options, uint16_t state, const char * string )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

绘制切换开关（Toggle Switch）。

开关控件（Toggle）默认带 3D 效果，option 值为 0。FT8XX_OPT_FLAT 移除该效果，其值为 256。

在 string 中，值为 255 的字符（可写为 `\xff`）分隔关闭（Off）与开启（On）状态的标签。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `x` | 开关控件（Toggle）左上角的 x 坐标，单位为像素。 |
| `y` | 开关控件（Toggle）左上角的 y 坐标，单位为像素。 |
| `width` | 开关控件宽度（Toggle Width），单位为像素。 |
| `font` | 文本所用字体（Font），范围为 0–31；16–31 为 ROM 字体。 |
| `options` | 要应用的选项（Options）。 |
| `state` | 开关控件状态（Toggle State）：0 表示关闭，65535 表示开启。 |
| `string` | 开关控件的字符串标签（String Label）。 |

<a id="gac946f044f2fbb6381ea4af268084d828"></a>

### `ft8xx_copro_cmd_track()`

```c
void ft8xx_copro_cmd_track ( const struct device * dev, int16_t x, int16_t y, int16_t width, int16_t height, int16_t tag )
```

```c
#include <zephyr/drivers/misc/ft8xx/ft8xx_copro.h>
```

跟踪图形对象（Graphics Object）的触摸操作。

此命令使协处理器引擎（Co-processor Engine）跟踪具有一个有效标签值（Tag Value）的特定图形对象上的触摸。随后，引擎按照 LCD 显示面板的帧率周期性更新 REG_TRACKER。

协处理器引擎（Co-processor Engine）以旋转跟踪模式（Rotary Tracker Mode）和线性跟踪模式（Linear Tracker Mode）跟踪图形对象：

- 旋转跟踪模式（Rotary Tracker Mode）：跟踪触点与标签值指定的图形对象中心之间的角度。数值以一圈的 1/65536 为单位：0 表示从中心垂直向下，0x4000 表示向左，0x8000 表示向上，0xC000 表示向右。
- 线性跟踪模式（Linear Tracker Mode）：宽度大于高度时，跟踪触点相对于标签值指定图形对象宽度的距离；宽度不大于高度时，跟踪其相对于高度的距离。数值以图形对象宽度或高度的 1/65536 为单位。触点距离是从图形对象左上角像素到触点坐标的距离。

在线性跟踪功能（Linear Tracker）中，x 和 y 分别表示跟踪区域左上角的 x、y 坐标，单位均为像素。

在旋转跟踪功能（Rotary Tracker）中，x 和 y 分别表示跟踪区域中心的 x、y 坐标，单位均为像素。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `x` | x 坐标（X-coordinate）。 |
| `y` | y 坐标（Y-coordinate）。 |
| `width` | 跟踪区域宽度（Track Area Width），单位为像素。 |
| `height` | 跟踪区域高度（Track Area Height），单位为像素。 |
| `tag` | 要跟踪的图形对象标签（Tag），范围为 1–255。 |

**说明（Note）**：注意（Note）：宽度和高度为 (1, 1) 表示旋转跟踪器（Rotary Tracker），在 REG_TRACKER 中报告角度值；为 (0, 0) 则禁用协处理器引擎的跟踪功能。


## 10.4\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [zephyr/drivers/misc/ft8xx/ft8xx_copro.h](../api_file_audio_gateway_reference/P014_zephyr__drivers__misc__ft8xx__ft8xx_copro.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P009_一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）.md) · [返回大纲](大纲.md) · [下一章](P011_FT8xx 显示列表（Display list）.md)
