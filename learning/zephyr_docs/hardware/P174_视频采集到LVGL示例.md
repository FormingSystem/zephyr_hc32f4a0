---
id: learning.zephyr-docs.hardware.vidsamp-3
title: 视频采集到LVGL示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/video/capture_to_lvgl/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="video-capture-to-lvgl"></a>

# 第174章\_视频采集到LVGL示例

原文：[Video capture to LVGL](https://docs.zephyrproject.org/latest/samples/subsys/video/capture_to_lvgl/README.html)。读取日期：2026-10-13，`latest`。

## 174.1\_说明（Description）

应用使用[视频设备](P141_视频设备.md)的 **应用程序编程接口（Application Programming Interface，API）**从采集设备读取视频帧（Video Frame），向控制台输出帧计数消息，然后通过图形库 LVGL 将帧送到 **液晶显示屏（Liquid Crystal Display，LCD）**。

## 174.2\_要求与接线（Requirements and Wiring）

此示例需要一个受支持的视频采集设备，例如摄像头，以及一个显示器。

使用 WeAct Studio STM32H743 时，连接 OV2640 摄像头模块和 0.96 英寸 ST7735 **薄膜晶体管（Thin-Film Transistor，TFT）**液晶显示屏。通过 **通用串行总线（Universal Serial Bus，USB）**线连接主机与开发板的 USB-C 接口，以接收控制台输出。

译注：原文把接口写作“micro USB-C”；此处保留 USB-C 接口名称，并指出原文的混合称呼，不能据此把 Micro-USB 和 USB-C 连接器视为同一种接口。

## 174.3\_构建与运行（Building and Running）

为 [MiniSTM32H743 Core Board](https://docs.zephyrproject.org/latest/boards/weact/mini_stm32h743/doc/index.html#mini_stm32h743) 构建此应用：

译注：在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行以下官方命令；示例源码由官方仓库提供，west 生成构建产物，`west flash` 将其烧录到开发板。

```bash
west build -b mini_stm32h743 --shield weact_ov2640_cam_module samples/subsys/video/capture_to_lvgl/ -- -DCONFIG_BOOT_DELAY=2000
west flash
```

无需真实视频采集硬件的测试，可以使用[视频软件图案发生器配置片段（Video Software Generator Snippet）](../snippets/P005_视频软件发生器配置片段.md)：

```bash
west build -b native_sim/native/64 -S video-sw-generator samples/subsys/video/capture
```

译注：上面的原文命令指向 `samples/subsys/video/capture`，即[通用视频采集示例](P173_视频采集示例.md)，并未指向本章的 `capture_to_lvgl`。此处保留官方命令并说明差异，不能把它记为 LVGL 示例已运行。

## 174.4\_示例输出（Sample Output）

以下原文日志列出设备名称、能力、像素格式、支持的分辨率及采集开始状态。`RGBP` 是原文使用的像素格式标识；`JPEG` 是 **联合图像专家组（Joint Photographic Experts Group）**制定的图像压缩格式名称。日志中的 `dcmi` 是设备节点名，相关硬件接口为 **数字摄像头接口（Digital Camera Interface，DCMI）**。

```text
[00:00:02.779,000] <inf> main: - Device name: dcmi@48020000
[00:00:02.779,000] <inf> main: - Capabilities:
[00:00:02.779,000] <inf> main:   RGBP width [160; 160; 0] height [120; 120; 0]
[00:00:02.779,000] <inf> main:   RGBP width [176; 176; 0] height [144; 144; 0]
[00:00:02.780,000] <inf> main:   RGBP width [240; 240; 0] height [160; 160; 0]
[00:00:02.780,000] <inf> main:   RGBP width [320; 320; 0] height [240; 240; 0]
[00:00:02.780,000] <inf> main:   RGBP width [352; 352; 0] height [288; 288; 0]
[00:00:02.780,000] <inf> main:   RGBP width [640; 640; 0] height [480; 480; 0]
[00:00:02.780,000] <inf> main:   RGBP width [800; 800; 0] height [600; 600; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1024; 1024; 0] height [768; 768; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1280; 1280; 0] height [1024; 1024; 0]
[00:00:02.780,000] <inf> main:   RGBP width [1600; 1600; 0] height [1200; 1200; 0]
[00:00:02.780,000] <inf> main:   JPEG width [160; 160; 0] height [120; 120; 0]
[00:00:02.780,000] <inf> main:   JPEG width [176; 176; 0] height [144; 144; 0]
[00:00:02.780,000] <inf> main:   JPEG width [240; 240; 0] height [160; 160; 0]
[00:00:02.780,000] <inf> main:   JPEG width [320; 320; 0] height [240; 240; 0]
[00:00:02.780,000] <inf> main:   JPEG width [352; 352; 0] height [288; 288; 0]
[00:00:02.780,000] <inf> main:   JPEG width [640; 640; 0] height [480; 480; 0]
[00:00:02.780,000] <inf> main:   JPEG width [800; 800; 0] height [600; 600; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1024; 1024; 0] height [768; 768; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1280; 1280; 0] height [1024; 1024; 0]
[00:00:02.780,000] <inf> main:   JPEG width [1600; 1600; 0] height [1200; 1200; 0]
[00:00:02.852,000] <inf> main: - Format: RGBP 160x120 320
[00:00:02.854,000] <inf> main: - Capture started
```

## 174.5\_参考资料（References）

[WeActStudio MiniSTM32H7xx项目](https://github.com/WeActStudio/MiniSTM32H7xx) · [视频驱动接口](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html) · [显示设备](P130_显示设备.md) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/video/capture_to_lvgl)

[上一章：视频采集示例](P173_视频采集示例.md) · [下一章：视频TCP服务器示例](P175_视频TCP服务器示例.md) · [返回大纲](大纲.md)
