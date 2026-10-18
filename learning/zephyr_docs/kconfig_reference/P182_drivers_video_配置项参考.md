---
id: learning.zephyr-docs.kconfig-reference.page-182
title: "`drivers/video`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第182章\_`drivers/video`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/video` 的 76 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_VIDEO_ARDUCAM_MEGA"></a>

## 182.1 `CONFIG_VIDEO_ARDUCAM_MEGA`

**提示（Prompt）**：Arducam Mega CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 Arducam Mega CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARDUCAM_MEGA_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/video/Kconfig.arducam_mega:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.arducam_mega#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_SPI`](P172_drivers_spi_配置项参考_1.md#CONFIG_SPI)。

<a id="CONFIG_VIDEO_BUFFER_POOL_ALIGN"></a>

## 182.2 `CONFIG_VIDEO_BUFFER_POOL_ALIGN`

**提示（Prompt）**：视频池缓冲区的对齐要求（Alignment）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`drivers/video/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE"></a>

## 182.3 `CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE`

**提示（Prompt）**：视频缓冲区池（Video Buffer Pool）大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
2097152
```

**定义位置（Location）**：[`drivers/video/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_POOL_NUM_MAX"></a>

## 182.4 `CONFIG_VIDEO_BUFFER_POOL_NUM_MAX`

**提示（Prompt）**：视频缓冲区池中的缓冲区数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`drivers/video/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION"></a>

## 182.5 `CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION`

**提示（Prompt）**：将视频缓冲区池放入 Zephyr 内存区域（Memory-region）

**说明（Help）**

将视频缓冲区池放入由兼容项为 `zephyr,memory-region` 的节点自动创建的区域中，区域名称通过 `CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION_NAME` 指定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION_NAME"></a>

## 182.6 `CONFIG_VIDEO_BUFFER_POOL_ZEPHYR_REGION_NAME`

**提示（Prompt）**：视频缓冲区池使用的 Zephyr 内存区域名称

**说明（Help）**

用于放置视频缓冲区池的 Zephyr 内存区域（Memory-region）名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_SMH_ATTRIBUTE"></a>

## 182.7 `CONFIG_VIDEO_BUFFER_SMH_ATTRIBUTE`

**提示（Prompt）**：视频缓冲区的共享多堆属性（Shared Multi Heap Attribute）

**说明（Help）**

视频缓冲区的共享多堆属性（Shared Multi Heap Attribute）：

- 0：`SMH_REG_ATTR_CACHEABLE`。
- 1：`SMH_REG_ATTR_NON_CACHEABLE`。
- 2：`SMH_REG_ATTR_EXTERNAL`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`drivers/video/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频缓冲区使用共享多堆（Shared Multi Heap）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP"></a>

## 182.8 `CONFIG_VIDEO_BUFFER_USE_SHARED_MULTI_HEAP`

**提示（Prompt）**：视频缓冲区使用共享多堆（Shared Multi Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y if CONFIG_SHARED_MULTI_HEAP
```

**定义位置（Location）**：[`drivers/video/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_SHARED_MULTI_HEAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHARED_MULTI_HEAP)。

<a id="CONFIG_VIDEO_DRIVERS"></a>

## 182.9 `CONFIG_VIDEO_DRIVERS`

**提示（Prompt）**：视频驱动（Video Drivers）

**说明（Help）**

启用视频驱动支持，通常由视频子系统（Video Subsystem）使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_VIDEO
```

**定义位置（Location）**：[`drivers/video/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO)。

<a id="CONFIG_VIDEO_EMUL_IMAGER"></a>

## 182.10 `CONFIG_VIDEO_EMUL_IMAGER`

**提示（Prompt）**：成像器（Imager）的软件实现

**说明（Help）**

启用仿真成像器（Emulated Imager）驱动。成像器数据结构的第一个字段是包含颜色图案的行缓冲区（Line Buffer）。`zephyr,video-emul-rx` 驱动使用 `memcpy()` 将这一行复制到整帧中，模拟 MIPI 链路将成像器的各行数据传输到内存。原文说明，默认值适用于每像素 2 位、宽度为 640 像素的图像帧。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_VIDEO_EMUL_IMAGER_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/video/Kconfig.emul_imager:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.emul_imager#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_EMUL_RX"></a>

## 182.11 `CONFIG_VIDEO_EMUL_RX`

**提示（Prompt）**：视频帧接收核心（Video Frame RX Core）的软件实现

**说明（Help）**

启用 MIPI 接收（RX）仿真 DMA 引擎驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_VIDEO_EMUL_RX_ENABLED && CONFIG_VIDEO_EMUL_IMAGER && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/video/Kconfig.emul_rx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.emul_rx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 成像器（Imager）的软件实现

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_EMUL_IMAGER`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_EMUL_IMAGER)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_ENCODER_H264"></a>

## 182.12 `CONFIG_VIDEO_ENCODER_H264`

**提示（Prompt）**：H.264 视频编码器（Video Encoder）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_ENCODER_JPEG"></a>

## 182.13 `CONFIG_VIDEO_ENCODER_JPEG`

**提示（Prompt）**：JPEG 视频编码器（Video Encoder）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_ESP32"></a>

## 182.14 `CONFIG_VIDEO_ESP32`

**提示（Prompt）**：视频接口驱动（Video Interface Driver）

**说明（Help）**

此选项为 ESP32-S3 启用视频接口（Video Interface）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_LCD_CAM_DVP_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/video/Kconfig.esp32_dvp:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.esp32_dvp#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_VIDEO_GC2145"></a>

## 182.15 `CONFIG_VIDEO_GC2145`

**提示（Prompt）**：GC2145 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 GC2145 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_GALAXYCORE_GC2145_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.gc2145:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.gc2145#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_HM01B0"></a>

## 182.16 `CONFIG_VIDEO_HM01B0`

**提示（Prompt）**：实时单色相机 Himax HM01B0 传感器

**说明（Help）**

启用单色相机（Monochrome Camera）Himax HM01B0 传感器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HIMAX_HM01B0_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/video/Kconfig.hm01b0:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.hm01b0#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VIDEO_HM0360"></a>

## 182.17 `CONFIG_VIDEO_HM0360`

**提示（Prompt）**：HM0360 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 HM0360 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_HIMAX_HM0360_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.hm0360:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.hm0360#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_I2C_RETRY_NUM"></a>

## 182.18 `CONFIG_VIDEO_I2C_RETRY_NUM`

**提示（Prompt）**：I2C 通信失败后的重试次数

**说明（Help）**

设为 0 时，只尝试写入一次，不进行重试。默认不重试。开发板配置文件或用户工程可根据实际情况设置合适的重试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/video/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_IMX219"></a>

## 182.19 `CONFIG_VIDEO_IMX219`

**提示（Prompt）**：IMX219 800 万像素 CMOS 图像传感器（8 Mega-Pixel CMOS Image Sensor）

**说明（Help）**

启用 IMX219 800 万像素 CMOS 图像传感器（8 Mega-Pixel CMOS Image Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SONY_IMX219_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/video/Kconfig.imx219:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.imx219#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VIDEO_IMX335"></a>

## 182.20 `CONFIG_VIDEO_IMX335`

**提示（Prompt）**：IMX335 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 IMX335 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SONY_IMX335_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/video/Kconfig.imx335:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.imx335#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_INIT_PRIORITY"></a>

## 182.21 `CONFIG_VIDEO_INIT_PRIORITY`

**提示（Prompt）**：视频初始化优先级（Video Initialization Priority）

**说明（Help）**

视频驱动的系统初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/video/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_CSI"></a>

## 182.22 `CONFIG_VIDEO_MCUX_CSI`

**提示（Prompt）**：NXP MCUX CMOS 传感器接口（CMOS Sensor Interface，CSI）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_CSI_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**被选择（Selected by）**

```text
CONFIG_VIDEO_MCUX_MIPI_CSI2RX
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_csi:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_csi#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_VIDEO_MCUX_MIPI_CSI2RX`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_MCUX_MIPI_CSI2RX)。

<a id="CONFIG_VIDEO_MCUX_CSI_INIT_PRIORITY"></a>

## 182.23 `CONFIG_VIDEO_MCUX_CSI_INIT_PRIORITY`

**提示（Prompt）**：NXP MCUX CSI 初始化优先级

**说明（Help）**

NXP MCUX 设备上 CSI 接口的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_MCUX_CSI && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
59
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_csi:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_csi#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → NXP MCUX CMOS 传感器接口（CMOS Sensor Interface，CSI）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_MCUX_CSI`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_MCUX_CSI)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_FLEXIO"></a>

## 182.24 `CONFIG_VIDEO_MCUX_FLEXIO`

**提示（Prompt）**：NXP MCUX FlexIO 并行相机（Parallel Camera）驱动

**说明（Help）**

启用基于 NXP FlexIO 的并行相机接口驱动。像素数据通过 FlexIO 移位器（Shifter）采集：使用 8 位并行总线，由 PCLK 门控、HREF 使能；再通过增强型直接内存访问（eDMA）传入内存。VSYNC GPIO 中断用于同步帧边界。可选的 XCLK 输出可由第二个 FlexIO 定时器生成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_FLEXIO_CAMERA_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_MCUX_FLEXIO
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_flexio:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_flexio#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_MCUX_FLEXIO`](P123_drivers_misc_配置项参考.md#CONFIG_MCUX_FLEXIO)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_MCUX_FLEXIO_INIT_PRIORITY"></a>

## 182.25 `CONFIG_VIDEO_MCUX_FLEXIO_INIT_PRIORITY`

**提示（Prompt）**：NXP MCUX FlexIO 相机初始化优先级

**说明（Help）**

FlexIO 相机驱动的初始化优先级。数值必须小于 `VIDEO_INIT_PRIORITY`，后者默认值为 60，以确保连接的图像传感器驱动在自身初始化期间尝试 I2C 通信之前，FlexIO 输出引脚上的 XCLK 已经运行。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_MCUX_FLEXIO && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
59
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_flexio:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_flexio#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → NXP MCUX FlexIO 并行相机（Parallel Camera）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_MCUX_FLEXIO`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_MCUX_FLEXIO)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_JPEGDEC"></a>

## 182.26 `CONFIG_VIDEO_MCUX_JPEGDEC`

**提示（Prompt）**：NXP JPEG 解码器（Decoder）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_JPEGDEC_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_jpegdec:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_jpegdec#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_MIPI_CSI2RX"></a>

## 182.27 `CONFIG_VIDEO_MCUX_MIPI_CSI2RX`

**提示（Prompt）**：NXP MIPI CSI-2 接收（RX）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MIPI_CSI2RX_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_VIDEO_MCUX_CSI
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_mipi_csi2rx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_mipi_csi2rx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_VIDEO_MCUX_CSI`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_MCUX_CSI)。

<a id="CONFIG_VIDEO_MCUX_MIPI_CSI2RX_INIT_PRIORITY"></a>

## 182.28 `CONFIG_VIDEO_MCUX_MIPI_CSI2RX_INIT_PRIORITY`

**提示（Prompt）**：NXP MCUX CSI-2 接收（RX）初始化优先级

**说明（Help）**

MIPI CSI-2 接收（RX）设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_MCUX_MIPI_CSI2RX && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
61
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_mipi_csi2rx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_mipi_csi2rx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → NXP MIPI CSI-2 接收（RX）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_MCUX_MIPI_CSI2RX`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_MCUX_MIPI_CSI2RX)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_PNGDEC"></a>

## 182.29 `CONFIG_VIDEO_MCUX_PNGDEC`

**提示（Prompt）**：NXP PNG 解码器（Decoder）

**说明（Help）**

启用 NXP PNG 解码器（Decoder）视频设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_PNGDEC_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_pngdec:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_pngdec#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_MCUX_SDMA"></a>

## 182.30 `CONFIG_VIDEO_MCUX_SDMA`

**提示（Prompt）**：NXP MCUX 视频 SMARTDMA 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_VIDEO_SMARTDMA_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/video/Kconfig.mcux_sdma:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mcux_sdma#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_VIDEO_MT9M114"></a>

## 182.31 `CONFIG_VIDEO_MT9M114`

**提示（Prompt）**：MT9M114 Aptina CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 MT9M114 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_APTINA_MT9M114_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/video/Kconfig.mt9m114:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.mt9m114#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)。

<a id="CONFIG_VIDEO_NATIVE_SIM_FIFO"></a>

## 182.32 `CONFIG_VIDEO_NATIVE_SIM_FIFO`

**提示（Prompt）**：原生模拟器主机 FIFO 视频源（Native Simulator Host FIFO Video Source）

**说明（Help）**

启用从主机文件系统的命名管道（Named Pipe，FIFO）读取原始帧的视频采集设备。主机进程，例如 FFmpeg，向 FIFO 提供数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_SIM_VIDEO_FIFO_ENABLED && CONFIG_NATIVE_LIBRARY && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/video/Kconfig.native_sim_fifo:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.native_sim_fifo#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LIBRARY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBRARY)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_VIDEO_OV2640"></a>

## 182.33 `CONFIG_VIDEO_OV2640`

**提示（Prompt）**：OV2640 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV2640 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OVTI_OV2640_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov2640:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov2640#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_OV5640"></a>

## 182.34 `CONFIG_VIDEO_OV5640`

**提示（Prompt）**：OV5640 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV5640 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OVTI_OV5640_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov5640:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov5640#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_OV5642"></a>

## 182.35 `CONFIG_VIDEO_OV5642`

**提示（Prompt）**：OV5642 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV5642 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OVTI_OV5642_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov5642:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov5642#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_OV767X"></a>

## 182.36 `CONFIG_VIDEO_OV767X`

**提示（Prompt）**：OV767X CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV7670 / OV7675 CMOS 数字图像传感器（Digital Image Sensor）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_OVTI_OV7670_ENABLED || DT_HAS_OVTI_OV7675_ENABLED) && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n || n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov767x:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov767x#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_OV7725"></a>

## 182.37 `CONFIG_VIDEO_OV7725`

**提示（Prompt）**：OV7725 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV7725 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OVTI_OV7725_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov7725:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov7725#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_OV9655"></a>

## 182.38 `CONFIG_VIDEO_OV9655`

**提示（Prompt）**：OV9655 CMOS 数字图像传感器（Digital Image Sensor）

**说明（Help）**

启用 OV9655 CMOS 数字图像传感器（Digital Image Sensor）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_OVTI_OV9655_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n || n
```

**定义位置（Location）**：[`drivers/video/Kconfig.ov9655:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.ov9655#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_RENESAS_RA_CEU"></a>

## 182.39 `CONFIG_VIDEO_RENESAS_RA_CEU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用 Renesas RA CEU 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_CEU_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_CLOCK_CONTROL_PWM
CONFIG_USE_RA_FSP_CEU
```

**定义位置（Location）**：[`drivers/video/Kconfig.renesas_ra_ceu:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.renesas_ra_ceu#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_CLOCK_CONTROL_PWM`](P063_drivers_clock_control_配置项参考_2.md#CONFIG_CLOCK_CONTROL_PWM)、[`CONFIG_USE_RA_FSP_CEU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_CEU)。

<a id="CONFIG_VIDEO_STM32_DCMI"></a>

## 182.40 `CONFIG_VIDEO_STM32_DCMI`

**提示（Prompt）**：STM32 数字相机接口（Digital Camera Interface，DCMI）驱动

**说明（Help）**

启用 STM32 数字相机接口（Digital Camera Interface）外设驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DCMI_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
CONFIG_RESET
CONFIG_USE_STM32_HAL_DCMI
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_DMA if n
CONFIG_USE_STM32_HAL_DMA if n
CONFIG_USE_STM32_HAL_DMA_EX if n
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmi:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmi#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_USE_STM32_HAL_DCMI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DCMI)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`。

<a id="CONFIG_VIDEO_STM32_DCMIPP"></a>

## 182.41 `CONFIG_VIDEO_STM32_DCMIPP`

**提示（Prompt）**：STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

**说明（Help）**

启用 STM32 数字相机存储器接口像素处理器（Digital Camera Memory Interface Pixel Processor，DCMIPP）外设驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DCMIPP_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_DCMIPP
CONFIG_RESET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_USE_STM32_HAL_DCMIPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DCMIPP)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_VIDEO_STM32_DCMIPP_CSI_ENABLE_IRQ"></a>

## 182.42 `CONFIG_VIDEO_STM32_DCMIPP_CSI_ENABLE_IRQ`

**提示（Prompt）**：相机串行接口（CSI）中断

**说明（Help）**

启用专用于 CSI 主机的第二个 DCMIPP 中断。将调用 `HAL_DCMIPP_CSI_*Callback` 硬件抽象层（HAL）回调，应用可实现这些回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

<a id="CONFIG_VIDEO_STM32_DCMIPP_INIT_PRIORITY"></a>

## 182.43 `CONFIG_VIDEO_STM32_DCMIPP_INIT_PRIORITY`

**提示（Prompt）**：STM32 DCMIPP 初始化优先级

**说明（Help）**

DCMIPP 驱动的系统初始化优先级。应安排在 `VIDEO_INIT_PRIORITY` 对应的源设备，即传感器，初始化之后。

译注：原文称优先级应“更低”（Lower），指执行次序靠后；本项默认数值为 61，视频初始化优先级默认值为 60，不能将这里的“更低”理解为数值更小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_DCMIPP && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
61
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_DCMIPP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMIPP)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_DCMIPP_SENSOR_HEIGHT"></a>

## 182.44 `CONFIG_VIDEO_STM32_DCMIPP_SENSOR_HEIGHT`

**提示（Prompt）**：传感器帧高度（Frame Height）

**说明（Help）**

传感器视频帧的高度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_DCMIPP && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
1944
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig)。

```text
1944
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_DCMIPP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMIPP)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_DCMIPP_SENSOR_PIXEL_FORMAT"></a>

## 182.45 `CONFIG_VIDEO_STM32_DCMIPP_SENSOR_PIXEL_FORMAT`

**提示（Prompt）**：传感器帧像素格式（Pixel Format）

**说明（Help）**

传感器视频帧的像素格式（Pixel Format）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_DCMIPP && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
"RG12"
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig)。

```text
"pRAA"
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_DCMIPP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMIPP)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_DCMIPP_SENSOR_WIDTH"></a>

## 182.46 `CONFIG_VIDEO_STM32_DCMIPP_SENSOR_WIDTH`

**提示（Prompt）**：传感器帧宽度（Frame Width）

**说明（Help）**

传感器视频帧的宽度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_DCMIPP && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
2592
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/st_b_cams_imx_mb1854/Kconfig.defconfig)。

```text
2592
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_dcmipp:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_dcmipp#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 数字相机存储器接口像素处理器（DCMIPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_DCMIPP`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_DCMIPP)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_JPEG"></a>

## 182.47 `CONFIG_VIDEO_STM32_JPEG`

**提示（Prompt）**：STM32 JPEG 硬件编解码器（HW Codec）驱动

**说明（Help）**

启用 STM32 JPEG 硬件编解码器（HW Codec）外设驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_JPEG_ENABLED && CONFIG_VIDEO_ENCODER_JPEG && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
CONFIG_USE_STM32_HAL_JPEG
CONFIG_USE_STM32_HAL_DMA if !CONFIG_SOC_SERIES_STM32H7X
CONFIG_USE_STM32_HAL_MDMA if CONFIG_SOC_SERIES_STM32H7X
CONFIG_USE_STM32_HAL_DMA_EX if !(CONFIG_SOC_SERIES_STM32F7X || CONFIG_SOC_SERIES_STM32H7X)
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_jpeg:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_jpeg#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_ENCODER_JPEG`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_ENCODER_JPEG)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)、[`CONFIG_USE_STM32_HAL_JPEG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_JPEG)、[`CONFIG_USE_STM32_HAL_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA)、[`CONFIG_SOC_SERIES_STM32H7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32H7X)、[`CONFIG_USE_STM32_HAL_MDMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDMA)、[`CONFIG_USE_STM32_HAL_DMA_EX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DMA_EX)、[`CONFIG_SOC_SERIES_STM32F7X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32F7X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_STM32H7X`、`CONFIG_SOC_SERIES_STM32F7X`。

<a id="CONFIG_VIDEO_STM32_VENC"></a>

## 182.48 `CONFIG_VIDEO_STM32_VENC`

**提示（Prompt）**：STM32 视频编码器（Video Encoder，VENC）驱动

**说明（Help）**

启用 STM32 视频编码器（Video Encoder）外设驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_VENC_ENABLED && CONFIG_VIDEO_ENCODER_H264 && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_STM32LIB
CONFIG_USE_STM32_LL_VENC
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_ENCODER_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_ENCODER_H264)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)、[`CONFIG_USE_STM32_LL_VENC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_LL_VENC)、[`CONFIG_RESET`](P145_drivers_reset_配置项参考.md#CONFIG_RESET)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC"></a>

## 182.49 `CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC`

**提示（Prompt）**：堆（Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_STM32_VENC_MEM_ALLOC>
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → 选择视频编码器（VENC）内部内存分配器（Allocator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC_MEM_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_MEM_ALLOC)。

<a id="CONFIG_VIDEO_STM32_VENC_HEAP_SIZE"></a>

## 182.50 `CONFIG_VIDEO_STM32_VENC_HEAP_SIZE`

**提示（Prompt）**：视频编码器（VENC）内部内存池大小，单位为字节

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC && CONFIG_VIDEO_STM32_VENC && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
7340032
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC)、[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION"></a>

## 182.51 `CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION`

**提示（Prompt）**：将视频编码器（VENC）内部内存池放入 Zephyr 内存区域（Memory-region）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC && CONFIG_VIDEO_STM32_VENC && CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC)、[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION_NAME"></a>

## 182.52 `CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION_NAME`

**提示（Prompt）**：内存池使用的 Zephyr 内存区域（Memory-region）名称

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION && CONFIG_VIDEO_STM32_VENC && CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → 将视频编码器（VENC）内部内存池放入 Zephyr 内存区域（Memory-region）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_HEAP_ZEPHYR_REGION)、[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_STM32_VENC_MEM_ALLOC"></a>

## 182.53 `CONFIG_VIDEO_STM32_VENC_MEM_ALLOC`

**提示（Prompt）**：选择视频编码器（VENC）内部内存分配器（Allocator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_STM32_VENC && CONFIG_VIDEO_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_VIDEO_STM32_VENC_SMH_ALLOC
CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_VIDEO_STM32_VENC_SMH_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_SMH_ALLOC)、[`CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_HEAP_ALLOC)。

<a id="CONFIG_VIDEO_STM32_VENC_SMH_ALLOC"></a>

## 182.54 `CONFIG_VIDEO_STM32_VENC_SMH_ALLOC`

**提示（Prompt）**：共享多堆（Shared-Multi-Heap）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_STM32_VENC_MEM_ALLOC>
```

**定义位置（Location）**：[`drivers/video/Kconfig.stm32_venc:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.stm32_venc#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → 选择视频编码器（VENC）内部内存分配器（Allocator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_STM32_VENC_MEM_ALLOC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC_MEM_ALLOC)。

<a id="CONFIG_VIDEO_ST_MIPID02"></a>

## 182.55 `CONFIG_VIDEO_ST_MIPID02`

**提示（Prompt）**：ST Microelectronics MIPID02 CSI 至 DVP 桥接器（Bridge）

**说明（Help）**

启用 ST MIPID02 CSI 至 DVP 桥接器（Bridge）驱动。ST MIPID02 是双通道 CSI-2 解串器（Dual-lane CSI-2 Deserializer），可输出最高 200 MHz 的 12 位并行数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_MIPID02_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO if n
```

**定义位置（Location）**：[`drivers/video/Kconfig.st_mipid02:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.st_mipid02#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_I2C`](P105_drivers_i2c_配置项参考_1.md#CONFIG_I2C)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)。

<a id="CONFIG_VIDEO_ST_MIPID02_CAPS_HEAP_SIZE"></a>

## 182.56 `CONFIG_VIDEO_ST_MIPID02_CAPS_HEAP_SIZE`

**提示（Prompt）**：为处理能力信息（Caps）预留的堆大小

**说明（Help）**

为处理能力信息（Caps）预留的堆大小。可根据 ST_MIPID02 源设备支持的格式数量减小或增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_ST_MIPID02 && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/video/Kconfig.st_mipid02:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.st_mipid02#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → ST Microelectronics MIPID02 CSI 至 DVP 桥接器（Bridge）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_ST_MIPID02`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_ST_MIPID02)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR"></a>

## 182.57 `CONFIG_VIDEO_SW_GENERATOR`

**提示（Prompt）**：视频软件发生器（Video Software Generator）

**说明（Help）**

启用视频图案发生器（Video Pattern Generator），用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_VIDEO_SW_GENERATOR_ENABLED && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264"></a>

## 182.58 `CONFIG_VIDEO_SW_GENERATOR_H264`

**提示（Prompt）**：视频软件发生器生成的 H.264 数据流

**说明（Help）**

启用构建时通过 FFmpeg 生成的 H.264 测试流。此选项要求构建主机上的 FFmpeg 支持 H.264 编码，并提供 `h264_metadata` 比特流过滤器（Bitstream Filter）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_BITRATE_KBPS"></a>

## 182.59 `CONFIG_VIDEO_SW_GENERATOR_H264_BITRATE_KBPS`

**提示（Prompt）**：视频软件发生器生成的 H.264 数据流比特率

**说明（Help）**

生成的 H.264 测试流的比特率（Bitrate），单位为千比特／秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
250
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_FPS"></a>

## 182.60 `CONFIG_VIDEO_SW_GENERATOR_H264_FPS`

**提示（Prompt）**：视频软件发生器生成的 H.264 数据流帧率

**说明（Help）**

生成的 H.264 测试流的帧率（Frame Rate）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_HEIGHT"></a>

## 182.61 `CONFIG_VIDEO_SW_GENERATOR_H264_HEIGHT`

**提示（Prompt）**：视频软件发生器生成的 H.264 帧高度

**说明（Help）**

生成的 H.264 测试流的高度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
240
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_NUM_FRAMES"></a>

## 182.62 `CONFIG_VIDEO_SW_GENERATOR_H264_NUM_FRAMES`

**提示（Prompt）**：视频软件发生器生成的 H.264 帧数量

**说明（Help）**

生成的 H.264 测试流中的帧数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE"></a>

## 182.63 `CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE`

**提示（Prompt）**：视频软件发生器使用的 H.264 档次（Profile）

**说明（Help）**

选择生成的测试流使用的 H.264 档次（Profile）。所选档次必须得到构建主机上 FFmpeg H.264 编码器的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN
```

**可选项（Choices）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_CONSTRAINED_BASELINE
CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_BASELINE
CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN
CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_HIGH
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN)、[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_CONSTRAINED_BASELINE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_CONSTRAINED_BASELINE)、[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_BASELINE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_BASELINE)、[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_HIGH`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_HIGH)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_BASELINE"></a>

## 182.64 `CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_BASELINE`

**提示（Prompt）**：基线档次（Baseline）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE>
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流 → 视频软件发生器使用的 H.264 档次（Profile）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_CONSTRAINED_BASELINE"></a>

## 182.65 `CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_CONSTRAINED_BASELINE`

**提示（Prompt）**：受限基线档次（Constrained Baseline）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE>
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流 → 视频软件发生器使用的 H.264 档次（Profile）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_HIGH"></a>

## 182.66 `CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_HIGH`

**提示（Prompt）**：高档次（High）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE>
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流 → 视频软件发生器使用的 H.264 档次（Profile）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN"></a>

## 182.67 `CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE_MAIN`

**提示（Prompt）**：主档次（Main）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE>
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流 → 视频软件发生器使用的 H.264 档次（Profile）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264_PROFILE)。

<a id="CONFIG_VIDEO_SW_GENERATOR_H264_WIDTH"></a>

## 182.68 `CONFIG_VIDEO_SW_GENERATOR_H264_WIDTH`

**提示（Prompt）**：视频软件发生器生成的 H.264 帧宽度

**说明（Help）**

生成的 H.264 测试流的宽度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR_H264 && CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
320
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator） → 视频软件发生器生成的 H.264 数据流

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR_H264`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR_H264)、[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_JPEG_HEIGHT"></a>

## 182.69 `CONFIG_VIDEO_SW_GENERATOR_JPEG_HEIGHT`

**提示（Prompt）**：视频软件发生器生成的 JPEG 帧高度

**说明（Help）**

使用树外（Out-of-tree）JPEG 文件时，更新 JPEG 帧高度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
160
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_JPEG_HFLIP_NAME"></a>

## 182.70 `CONFIG_VIDEO_SW_GENERATOR_JPEG_HFLIP_NAME`

**提示（Prompt）**：用于生成水平翻转（H-flipped）JPEG 帧的文件名

**说明（Help）**

使用树外（Out-of-tree）JPEG 文件时，更新 JPEG 文件名。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
"color_bar_hflip"
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_JPEG_NAME"></a>

## 182.71 `CONFIG_VIDEO_SW_GENERATOR_JPEG_NAME`

**提示（Prompt）**：用于生成 JPEG 帧的文件名

**说明（Help）**

使用树外（Out-of-tree）JPEG 文件时，更新 JPEG 文件名。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
"color_bar"
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_JPEG_WIDTH"></a>

## 182.72 `CONFIG_VIDEO_SW_GENERATOR_JPEG_WIDTH`

**提示（Prompt）**：视频软件发生器生成的 JPEG 帧宽度

**说明（Help）**

使用树外（Out-of-tree）JPEG 文件时，更新 JPEG 帧宽度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
320
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_PNG_HEIGHT"></a>

## 182.73 `CONFIG_VIDEO_SW_GENERATOR_PNG_HEIGHT`

**提示（Prompt）**：视频软件发生器生成的 PNG 帧高度

**说明（Help）**

使用树外（Out-of-tree）PNG 文件时，更新 PNG 帧高度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
160
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_PNG_HFLIP_NAME"></a>

## 182.74 `CONFIG_VIDEO_SW_GENERATOR_PNG_HFLIP_NAME`

**提示（Prompt）**：用于生成水平翻转（H-flipped）PNG 帧的文件名

**说明（Help）**

使用树外（Out-of-tree）PNG 文件时，更新 PNG 文件名。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
"color_bar_hflip"
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_PNG_NAME"></a>

## 182.75 `CONFIG_VIDEO_SW_GENERATOR_PNG_NAME`

**提示（Prompt）**：用于生成 PNG 帧的文件名

**说明（Help）**

使用树外（Out-of-tree）PNG 文件时，更新 PNG 文件名。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
"color_bar"
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<a id="CONFIG_VIDEO_SW_GENERATOR_PNG_WIDTH"></a>

## 182.76 `CONFIG_VIDEO_SW_GENERATOR_PNG_WIDTH`

**提示（Prompt）**：视频软件发生器生成的 PNG 帧宽度

**说明（Help）**

使用树外（Out-of-tree）PNG 文件时，更新 PNG 帧宽度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_VIDEO_SW_GENERATOR && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
320
```

**定义位置（Location）**：[`drivers/video/Kconfig.sw_generator:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/video/Kconfig.sw_generator#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频软件发生器（Video Software Generator）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_SW_GENERATOR`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_SW_GENERATOR)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)。

<!-- kconfig-navigation -->

[上一章](P181_drivers_usb_c_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P183_drivers_virtio_配置项参考.md)
