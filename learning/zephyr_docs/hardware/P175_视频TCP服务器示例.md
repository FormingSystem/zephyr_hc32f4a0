---
id: learning.zephyr-docs.hardware.vidsamp-4
title: 视频TCP服务器示例
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/video/tcpserversink/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="video-tcpserversink"></a>

# 第175章\_视频TCP服务器示例

原文：[Video TCP server sink](https://docs.zephyrproject.org/latest/samples/subsys/video/tcpserversink/README.html)。读取日期：2026-10-13，`latest`。

## 175.1\_说明（Description）

应用从视频采集设备获取视频帧（Video Frame），并通过网络发送给已经连接的 **传输控制协议（Transmission Control Protocol，TCP）**客户端。

## 175.2\_要求（Requirements）

示例需要视频采集设备与网络支持。原文列出以下硬件组合：

- [MIMXRT1064-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1064_evk/doc/index.html#mimxrt1064_evk) 与 MT9M114 摄像头模块。
- [STM32N6570-DK](https://docs.zephyrproject.org/latest/boards/st/stm32n6570_dk/doc/index.html#stm32n6570_dk) 与 [ST B-CAMS-IMX-MB1854模块](https://docs.zephyrproject.org/latest/boards/shields/st_b_cams_imx_mb1854/doc/index.html#st-b-cams-imx-mb1854)。

## 175.3\_接线（Wiring）

在 MIMXRT1064-EVK 上，将 MT9M114 摄像头模块插入 J35 摄像头连接器；用 **通用串行总线（Universal Serial Bus，USB）**线将主机连接到 Micro-USB 调试接口 J41，通过板载调试接口取得控制台输出。原文将该接口称为 `freelink`。以太网（Ethernet）线必须接到 RJ45 连接器。

在 STM32N6570-DK 上，把 MB1854 IMX335 摄像头模块插入 **摄像头串行接口第二版（Camera Serial Interface 2，CSI-2）**连接器；将 RJ45 以太网线插到 CN6 以太网接口。为了获得更好的图像效果，原文建议集成 [STM32图像信号处理（Image Signal Processing，ISP）中间件](https://github.com/stm32-hotspot/zephyr-stm32-mw-isp)。

## 175.4\_构建与运行（Building and Running）

译注：下列构建命令在已配置 Zephyr 开发环境的终端中，从 Zephyr 源码根目录执行；示例源码由官方仓库提供，west 生成构建产物。

为 MIMXRT1064-EVK 构建；如果没有 MT9M114 摄像头扩展板（Shield），则使用视频软件发生器：

```bash
west build -b mimxrt1064_evk --shield dvp_fpc24_mt9m114 samples/subsys/video/tcpserversink
```

为了不依赖真实视频采集硬件进行测试，可使用[视频软件发生器配置片段（Video Software Generator Snippet）](../snippets/P005_视频软件发生器配置片段.md)：

```bash
west build -b native_sim/native/64 -S video-sw-generator samples/subsys/video/capture
```

译注：此处原文命令使用 `samples/subsys/video/capture`，即[通用视频采集示例](P173_视频采集示例.md)，不是本章的 `tcpserversink`。原命令保留，不能仅执行它就认为 TCP 服务器已经启动。

为 STM32N6570-DK 构建时，可以在命令末尾使用 `venc` 文件后缀（File Suffix）配置，启用 H.264 视频压缩支持：

```bash
west build -b stm32n6570_dk --shield st_b_cams_imx_mb1854 samples/subsys/video/tcpserversink -- -DFILE_SUFFIX=venc
```

## 175.5\_示例输出与客户端

以下为原文控制台输出，`RGBP` 是像素格式标识：

```text
Video device detected, format: RGBP 480x272
TCP: Waiting for client...
```

随后，同一网络中的对端可以连接服务器并获取帧。例如，在装有 GStreamer 多媒体框架的对端终端中执行原文客户端命令：

```bash
gst-launch-1.0 tcpclientsrc host=192.0.2.1 port=5000 \
    ! videoparse format=rgb16 width=480 height=272 \
    ! queue \
    ! videoconvert \
    ! fpsdisplaysink sync=false
```

译注：`host` 为服务器的网络地址，`port=5000` 为连接端口；应按实际部署填写。原命令保留示例地址 `192.0.2.1`。GStreamer 管线读取 TCP 数据，按指定尺寸解析帧，再转换视频并显示帧率；它不使用 Zephyr 源码目录中的相对文件。

对于视频软件发生器，原文给出的默认分辨率应为 `width=320`、`height=160`，使用客户端时须与服务端匹配。

启用视频压缩时，使用下面的 GStreamer 命令行，由解码器处理压缩数据：

```bash
gst-launch-1.0 tcpclientsrc host=192.0.2.1 port=5000 \
    ! queue ! decodebin ! queue ! fpsdisplaysink sync=false
```

## 175.6\_参考资料（References）

[MT9M114产品资料](https://www.onsemi.com/PowerSolutions/product.do?id=MT9M114) · [视频驱动接口](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html) · [兼容BSD套接字的接口](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html) · [官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/video/tcpserversink)

译注：BSD 指 **伯克利软件发行版（Berkeley Software Distribution）**；套接字（Socket）是应用访问网络通信服务的编程接口。

[上一章：视频采集到LVGL示例](P174_视频采集到LVGL示例.md) · [下一章：辅助显示示例](P176_辅助显示示例.md) · [返回大纲](大纲.md)
