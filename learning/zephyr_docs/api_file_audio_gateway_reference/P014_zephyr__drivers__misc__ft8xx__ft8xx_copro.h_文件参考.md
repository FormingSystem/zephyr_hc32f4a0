---
id: learning.zephyr-docs.api-file-audio-gateway-reference.page-14
title: zephyr__drivers__misc__ft8xx__ft8xx_copro.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_drivers\_\_misc\_\_ft8xx\_\_ft8xx\_copro.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ft8xx__copro_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FT8XX协处理器函数（Coprocessor Functions）。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/device.h>
```

查看此文件的源码。

FT8XX协处理器函数（Coprocessor Functions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_ga304badab7bd34208d499b199080fb557"></a>

```c
#define FT8XX_OPT_3D 0
```

相关声明：[FT8XX_OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga304badab7bd34208d499b199080fb557)。

协处理器控件（Co-processor Widget）以三维效果绘制。

<a id="r_ga3a79c1128bdb9fe094843688691a085c"></a>

```c
#define FT8XX_OPT_RGB565 0
```

相关声明：[FT8XX_OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3a79c1128bdb9fe094843688691a085c)。

将 JPEG 图像解码为 RGB565 格式的协处理器选项（Co-processor Option）。

<a id="r_ga415760ddf94db71ee9a504300bac4661"></a>

```c
#define FT8XX_OPT_MONO 1
```

相关声明：[FT8XX_OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga415760ddf94db71ee9a504300bac4661)。

将 JPEG 图像解码为 L8 格式，即单色（Monochrome）的协处理器选项。

<a id="r_gacc953470460b083c0b8bd9ebbc8ed03b"></a>

```c
#define FT8XX_OPT_NODL 2
```

相关声明：[FT8XX_OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc953470460b083c0b8bd9ebbc8ed03b)。

不为从 JPEG 图像解码的位图（Bitmap）生成显示列表命令（Display List Commands）。

<a id="r_ga160b331fb401eec023e0992c6f4c6331"></a>

```c
#define FT8XX_OPT_FLAT 256
```

相关声明：[FT8XX_OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga160b331fb401eec023e0992c6f4c6331)。

绘制协处理器控件（Co-processor Widget）时不使用三维效果。

<a id="r_ga5a58155896cdb2d0f1693d203706ce93"></a>

```c
#define FT8XX_OPT_SIGNED 256
```

相关声明：[FT8XX_OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga5a58155896cdb2d0f1693d203706ce93)。

将数字视为 32 位有符号整数（Signed Integer）。

<a id="r_gac2d1ccbb99eaa032ed9d39fc01d32c66"></a>

```c
#define FT8XX_OPT_CENTERX 512
```

相关声明：[FT8XX_OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac2d1ccbb99eaa032ed9d39fc01d32c66)。

协处理器控件（Co-processor Widget）水平居中。

<a id="r_ga65b3a1e29ae425b2f1c3e66b4ea1449a"></a>

```c
#define FT8XX_OPT_CENTERY 1024
```

相关声明：[FT8XX_OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga65b3a1e29ae425b2f1c3e66b4ea1449a)。

协处理器控件（Co-processor Widget）垂直居中。

<a id="r_ga013968a6bf9534265c897ab1f4018eb0"></a>

```c
#define FT8XX_OPT_CENTER 1536
```

相关声明：[FT8XX_OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga013968a6bf9534265c897ab1f4018eb0)。

协处理器控件（Co-processor Widget）水平和垂直居中。

<a id="r_gac864c155bc2121bf8d3954e1ed8dbb7e"></a>

```c
#define FT8XX_OPT_RIGHTX 2048
```

相关声明：[FT8XX_OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac864c155bc2121bf8d3954e1ed8dbb7e)。

协处理器控件（Co-processor Widget）上的标签右对齐。

<a id="r_gacb08df4fac256cbf808b133d4159aa29"></a>

```c
#define FT8XX_OPT_NOBACK 4096
```

相关声明：[FT8XX_OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacb08df4fac256cbf808b133d4159aa29)。

协处理器控件（Co-processor Widget）不绘制背景。

<a id="r_ga50f4fac88e4f4b558450adcda33dae93"></a>

```c
#define FT8XX_OPT_NOTICKS 8192
```

相关声明：[FT8XX_OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga50f4fac88e4f4b558450adcda33dae93)。

协处理器时钟控件（Clock Widget）不绘制小时刻度。

<a id="r_ga79938d9c1193d44a527ca8c158117a86"></a>

```c
#define FT8XX_OPT_NOHM 16384
```

相关声明：[FT8XX_OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga79938d9c1193d44a527ca8c158117a86)。

协处理器时钟控件（Clock Widget）不绘制时针和分针，只绘制秒针。

<a id="r_ga1a9838a862ec166bfe95d64144b9a052"></a>

```c
#define FT8XX_OPT_NOPOINTER 16384
```

相关声明：[FT8XX_OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga1a9838a862ec166bfe95d64144b9a052)。

协处理器仪表（Gauge）没有指针。

<a id="r_ga6416f4282d2c483d2adba8c1215ab638"></a>

```c
#define FT8XX_OPT_NOSECS 32768
```

相关声明：[FT8XX_OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga6416f4282d2c483d2adba8c1215ab638)。

协处理器时钟控件（Clock Widget）不绘制秒针。

<a id="r_gade56de46694ca420460c1ceb26a33120"></a>

```c
#define FT8XX_OPT_NOHANDS 49152
```

相关声明：[FT8XX_OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gade56de46694ca420460c1ceb26a33120)。

协处理器时钟控件（Clock Widget）不绘制时针、分针和秒针。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 14.2\_函数（Functions）

<a id="r_ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea"></a>

```c
void ft8xx_copro_cmd (const struct device *dev, uint32_t cmd)
```

相关声明：[ft8xx_copro_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

通过协处理器引擎（Co-processor Engine）执行显示列表命令（Display List Command）。

<a id="r_gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9"></a>

```c
void ft8xx_copro_cmd_dlstart (const struct device *dev)
```

相关声明：[ft8xx_copro_cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9)、[device](../device_reference/P002_设备对象结构.md)。

开始新的显示列表（Display List）。

<a id="r_ga3605bc23d9555ac51fc6292cb6f2a02c"></a>

```c
void ft8xx_copro_cmd_swap (const struct device *dev)
```

相关声明：[ft8xx_copro_cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3605bc23d9555ac51fc6292cb6f2a02c)、[device](../device_reference/P002_设备对象结构.md)。

交换当前显示列表（Display List）。

<a id="r_gab47b9c79db405686168cf1516ea0a00d"></a>

```c
void ft8xx_copro_cmd_fgcolor (const struct device *dev, uint32_t color)
```

相关声明：[ft8xx_copro_cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab47b9c79db405686168cf1516ea0a00d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置前景色（Foreground Color）。

<a id="r_gafa5c3fe004456cfd531edf781c11c00d"></a>

```c
void ft8xx_copro_cmd_bgcolor (const struct device *dev, uint32_t color)
```

相关声明：[ft8xx_copro_cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gafa5c3fe004456cfd531edf781c11c00d)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置背景色（Background Color）。

<a id="r_ga3b9454e8a6a824bd87c675037047c069"></a>

```c
void ft8xx_copro_cmd_slider (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t height, uint16_t options, uint16_t val, uint16_t range)
```

相关声明：[ft8xx_copro_cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3b9454e8a6a824bd87c675037047c069)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制滑块（Slider）。

<a id="r_ga93e61278bacec915bb360244ab43dbb7"></a>

```c
void ft8xx_copro_cmd_toggle (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t font, uint16_t options, uint16_t state, const char *string)
```

相关声明：[ft8xx_copro_cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga93e61278bacec915bb360244ab43dbb7)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

绘制切换开关（Toggle Switch）。

<a id="r_gac946f044f2fbb6381ea4af268084d828"></a>

```c
void ft8xx_copro_cmd_track (const struct device *dev, int16_t x, int16_t y, int16_t width, int16_t height, int16_t tag)
```

相关声明：[ft8xx_copro_cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac946f044f2fbb6381ea4af268084d828)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)。

跟踪图形对象（Graphics Object）的触摸操作。

<a id="r_ga35d0500600e8c1d1df653952fab5d86c"></a>

```c
void ft8xx_copro_cmd_text (const struct device *dev, int16_t x, int16_t y, int16_t font, uint16_t options, const char *string)
```

相关声明：[ft8xx_copro_cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga35d0500600e8c1d1df653952fab5d86c)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

绘制文本（Text）。

<a id="r_ga72e1feafde7bb230cd798ba23f414de9"></a>

```c
void ft8xx_copro_cmd_number (const struct device *dev, int16_t x, int16_t y, int16_t font, uint16_t options, int32_t number)
```

相关声明：[ft8xx_copro_cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga72e1feafde7bb230cd798ba23f414de9)、[device](../device_reference/P002_设备对象结构.md)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

绘制十进制数字（Decimal Number）。

<a id="r_gacc68ff73da90a9c822185f2ceba5a910"></a>

```c
void ft8xx_copro_cmd_calibrate (const struct device *dev, uint32_t *result)
```

相关声明：[ft8xx_copro_cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc68ff73da90a9c822185f2ceba5a910)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

执行触摸屏校准例程（Touch Screen Calibration Routine）。


## 14.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P279_ft8xx_copro.h_源码浏览.md)
- [FT8XX_OPT_3D](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga304badab7bd34208d499b199080fb557)
- [FT8XX_OPT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3a79c1128bdb9fe094843688691a085c)
- [FT8XX_OPT_MONO](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga415760ddf94db71ee9a504300bac4661)
- [FT8XX_OPT_NODL](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc953470460b083c0b8bd9ebbc8ed03b)
- [FT8XX_OPT_FLAT](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga160b331fb401eec023e0992c6f4c6331)
- [FT8XX_OPT_SIGNED](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga5a58155896cdb2d0f1693d203706ce93)
- [FT8XX_OPT_CENTERX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac2d1ccbb99eaa032ed9d39fc01d32c66)
- [FT8XX_OPT_CENTERY](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga65b3a1e29ae425b2f1c3e66b4ea1449a)
- [FT8XX_OPT_CENTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga013968a6bf9534265c897ab1f4018eb0)
- [FT8XX_OPT_RIGHTX](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac864c155bc2121bf8d3954e1ed8dbb7e)
- [FT8XX_OPT_NOBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacb08df4fac256cbf808b133d4159aa29)
- [FT8XX_OPT_NOTICKS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga50f4fac88e4f4b558450adcda33dae93)
- [FT8XX_OPT_NOHM](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga79938d9c1193d44a527ca8c158117a86)
- [FT8XX_OPT_NOPOINTER](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga1a9838a862ec166bfe95d64144b9a052)
- [FT8XX_OPT_NOSECS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga6416f4282d2c483d2adba8c1215ab638)
- [FT8XX_OPT_NOHANDS](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gade56de46694ca420460c1ceb26a33120)
- [ft8xx_copro_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga9d4ab3b53e4e11433d9c6a0d3e6cd3ea)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [ft8xx_copro_cmd_dlstart](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab7f5a1ea24eb9db4ac0e0a4f3d58e7b9)
- [ft8xx_copro_cmd_swap](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3605bc23d9555ac51fc6292cb6f2a02c)
- [ft8xx_copro_cmd_fgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gab47b9c79db405686168cf1516ea0a00d)
- [ft8xx_copro_cmd_bgcolor](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gafa5c3fe004456cfd531edf781c11c00d)
- [ft8xx_copro_cmd_slider](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga3b9454e8a6a824bd87c675037047c069)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [ft8xx_copro_cmd_toggle](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga93e61278bacec915bb360244ab43dbb7)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [ft8xx_copro_cmd_track](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gac946f044f2fbb6381ea4af268084d828)
- [ft8xx_copro_cmd_text](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga35d0500600e8c1d1df653952fab5d86c)
- [ft8xx_copro_cmd_number](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#ga72e1feafde7bb230cd798ba23f414de9)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [ft8xx_copro_cmd_calibrate](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__copro.html#gacc68ff73da90a9c822185f2ceba5a910)

<a id="header-details"></a>

---

[上一章](P013_zephyr__dt-bindings__reset__focaltech_ft9001_reset.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__drivers__misc__ft8xx__ft8xx_reference_api.h_文件参考.md)
