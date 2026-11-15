---
id: learning.zephyr-docs.usb.page-125
title: USB主机摄像头示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/host_uvc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第125章\_USB主机摄像头示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/host_uvc/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 125.1\_概述（Overview）

本示例演示如何使用 USB 主机 UVC（USB Video Class，USB 视频类）驱动，从连接到 Zephyr 设备的 USB 摄像头采集视频帧（Video Frames）。此时 Zephyr 设备充当 USB 主机（USB Host）。

连接后，USB 摄像头会被自动检测和配置。示例采集视频帧，并记录帧统计信息（Frame Statistics）。

## 125.2\_要求（Requirements）

示例使用 USB 主机栈，需要 USB 主机控制器驱动（USB Host Controller Driver），还需要一台支持 UVC 规范的 USB 摄像头。

## 125.3\_构建与运行（Building and Running）

按如下命令构建和烧录应用。译注：在已配置工具链、west 和目标板烧录工具的终端中，从 Zephyr 源码根目录执行；Windows 通用工程操作可使用 UCRT64 Bash，Linux 使用 Bash。命令面向 `rd_rw612_bga/rw612` 开发板。

```shell
west build -b rd_rw612_bga/rw612 samples/subsys/usb/host_uvc
west flash
```

USB 摄像头连接后，设备预期会自动检测到它。

### 125.3.1\_示例输出（Sample Output）

连接 USB 摄像头时，应看到类似以下输出：

```console
*** Booting Zephyr OS build v4.3.0-8828-g14f382c2002c ***
<inf> main: USB host video device usbh_uvc_0 is ready
<inf> usbh_dev: New device with address 1 state 2
<inf> usbh_dev: Configuration 1 bNumInterfaces 4
<inf> usbh_uvc: UVC device connected
<inf> usbh_uvc: Interface 0 associated with UVC class
<inf> usbh_dev: Set Interfaces 0, alternate 0 -> 0
<inf> usbh_dev: Set Interfaces 1, alternate 0 -> 0
<inf> usbh_uvc: Device configured successfully: control interface 0, streaming interface 1
<wrn> usbh_uvc: Control cid 134217729 not supported by device
<wrn> usbh_uvc: Control cid 134217730 not supported by device
<inf> usbh_uvc: Successfully initialized 8 UVC controls
<inf> usbh_uvc: UVC device (addr=1) initialization completed
<inf> usbh_class: Class 'uvc_host_c_data_0' matches interface 0
<inf> main: Video device connected!
```

### 125.3.2\_查看受支持格式（Viewing Supported Formats）

示例枚举并显示所有受支持的视频格式：

```console
<inf> usbh_uvc: Created 36 format capabilities based on UVC descriptors
<inf> main: - Capabilities:
<inf> main:   YUYV width [640; 640; 1] height [480; 480; 1]
<inf> main:   YUYV width [160; 160; 1] height [90; 90; 1]
<inf> main:   YUYV width [160; 160; 1] height [120; 120; 1]
<inf> main:   YUYV width [176; 176; 1] height [144; 144; 1]
<inf> main:   YUYV width [320; 320; 1] height [180; 180; 1]
<inf> main:   YUYV width [320; 320; 1] height [240; 240; 1]
<inf> main:   YUYV width [352; 352; 1] height [288; 288; 1]
<inf> main:   YUYV width [432; 432; 1] height [240; 240; 1]
<inf> main:   YUYV width [640; 640; 1] height [360; 360; 1]
<inf> main:   YUYV width [800; 800; 1] height [448; 448; 1]
<inf> main:   YUYV width [800; 800; 1] height [600; 600; 1]
<inf> main:   YUYV width [864; 864; 1] height [480; 480; 1]
<inf> main:   YUYV width [960; 960; 1] height [720; 720; 1]
<inf> main:   YUYV width [1024; 1024; 1] height [576; 576; 1]
<inf> main:   YUYV width [1280; 1280; 1] height [720; 720; 1]
<inf> main:   YUYV width [1600; 1600; 1] height [896; 896; 1]
<inf> main:   YUYV width [1920; 1920; 1] height [1080; 1080; 1]
<inf> main:   YUYV width [2304; 2304; 1] height [1296; 1296; 1]
<inf> main:   YUYV width [2304; 2304; 1] height [1536; 1536; 1]
<inf> main:   JPEG width [640; 640; 1] height [480; 480; 1]
<inf> main:   JPEG width [160; 160; 1] height [90; 90; 1]
<inf> main:   JPEG width [160; 160; 1] height [120; 120; 1]
<inf> main:   JPEG width [176; 176; 1] height [144; 144; 1]
<inf> main:   JPEG width [320; 320; 1] height [180; 180; 1]
<inf> main:   JPEG width [320; 320; 1] height [240; 240; 1]
<inf> main:   JPEG width [352; 352; 1] height [288; 288; 1]
<inf> main:   JPEG width [432; 432; 1] height [240; 240; 1]
<inf> main:   JPEG width [640; 640; 1] height [360; 360; 1]
<inf> main:   JPEG width [800; 800; 1] height [448; 448; 1]
<inf> main:   JPEG width [800; 800; 1] height [600; 600; 1]
<inf> main:   JPEG width [864; 864; 1] height [480; 480; 1]
<inf> main:   JPEG width [960; 960; 1] height [720; 720; 1]
<inf> main:   JPEG width [1024; 1024; 1] height [576; 576; 1]
<inf> main:   JPEG width [1280; 1280; 1] height [720; 720; 1]
<inf> main:   JPEG width [1600; 1600; 1] height [896; 896; 1]
<inf> main:   JPEG width [1920; 1920; 1] height [1080; 1080; 1]
```

### 125.3.3\_配置视频格式（Configuring Video Format）

示例依据 `prj.conf` 设置配置视频格式：

```console
<inf> main: - Expected video format: YUYV 320x180
<inf> usbh_uvc: Setting format: YUYV 320x180 (format_index=1, frame_index=5, interval=333333)
<wrn> usbh_uvc: VS GET: expected 48 bytes, got 26 bytes
<inf> usbh_dev: Set Interfaces 1, alternate 0 -> 3
<inf> usbh_dev: Modify interface 1 ep 0x81 by op 0
<inf> usbh_dev: Modify interface 1 ep 0x81 by op 1
<inf> usbh_uvc: Set streaming interface 1 alternate 3 successfully
<inf> usbh_uvc: UVC format set successfully: YUYV 320x180@30fps
```

### 125.3.4\_调整帧率（Adjusting Frame Rate）

示例显示受支持的帧间隔（Frame Intervals），并设置目标帧率（Frame Rate）：

```console
<inf> main: - Default frame rate : 30.000000 fps
<inf> main: - Supported frame intervals for the default format:
<inf> main:    333333/10000000
<inf> main:    416666/10000000
<inf> main:    500000/10000000
<inf> main:    666666/10000000
<inf> main:    1000000/10000000
<inf> main:    1333333/10000000
<inf> main:    2000000/10000000
<inf> usbh_uvc: Setting frame rate: 15 fps -> 15 fps
<wrn> usbh_uvc: VS GET: expected 48 bytes, got 26 bytes
<inf> usbh_uvc: Frame rate successfully set to 15 fps
<inf> usbh_dev: Set Interfaces 1, alternate 3 -> 2
<inf> usbh_dev: Modify interface 1 ep 0x81 by op 0
<inf> usbh_dev: Modify interface 1 ep 0x81 by op 2
<inf> usbh_dev: Modify interface 1 ep 0x81 by op 1
<inf> usbh_uvc: Set streaming interface 1 alternate 2 successfully
<inf> main: - Target frame rate set to: 15.000000 fps
```

### 125.3.5\_访问视频控制项（Accessing the Video Controls）

示例枚举摄像头可用的控制项（Camera Controls）：

```console
<inf> main: - Supported controls:
<inf> main:          device: usbh_uvc_0
<inf> video_ctrls:                       Brightness 0x00980900 (int)      (flags=0x00) : min=0 max=255 step=1 default=128 value=128
<inf> video_ctrls:                         Contrast 0x00980901 (int)      (flags=0x00) : min=0 max=255 step=1 default=128 value=128
<inf> video_ctrls:                       Saturation 0x00980902 (int)      (flags=0x00) : min=0 max=255 step=1 default=128 value=128
<inf> video_ctrls:                         Exposure 0x00980911 (int)      (flags=0x00) : min=3 max=2047 step=1 default=250 value=250
<inf> video_ctrls:                             Gain 0x00980913 (int)      (flags=0x00) : min=0 max=255 step=1 default=0 value=0
<inf> video_ctrls:        White Balance Temperature 0x0098091a (int)      (flags=0x00) : min=2000 max=6500 step=1 default=4000 value=4000
<inf> video_ctrls:                  Focus, Absolute 0x009a090a (int)      (flags=0x00) : min=0 max=250 step=5 default=0 value=0
<inf> video_ctrls:                   Zoom, Absolute 0x009a090d (int)      (flags=0x00) : min=100 max=500 step=1 default=100 value=100
```

### 125.3.6\_帧统计（Frame Statistics）

示例每收到100帧记录一次统计信息：

```console
<inf> main: Allocating 6 video buffers, size=115200
<inf> usbh_dev: Set Interfaces 1, alternate 2 -> 2
<inf> main: Capture started
<inf> main: Received 100 frames
<inf> main: Received 200 frames
<inf> main: Received 300 frames
```

> 译注（日志与源码）：以上是官方原始示例输出，格式、控制范围和接口备用设置随摄像头而变化。保存的当前Kconfig默认YUYV、320×240、15帧／秒，prj.conf设置4个视频缓冲区；原文日志为320×180和6个缓冲区，不能作为当前配置的固定预期。日志中的帧间隔是秒的分数，例如333333/10000000约为1/30秒，不是帧率数值本身。

## 125.4\_配置选项（Configuration Options）

可以通过 `prj.conf` 配置示例。

### 125.4.1\_视频格式（Video Format）

| 配置 | 说明 |
| --- | --- |
| `CONFIG_APP_VIDEO_PIXEL_FORMAT` | 像素格式（Pixel Format），例如原文列举的YUYV、MJPEG等 |
| `CONFIG_APP_VIDEO_FRAME_WIDTH` | 帧宽度 |
| `CONFIG_APP_VIDEO_FRAME_HEIGHT` | 帧高度 |
| `CONFIG_APP_VIDEO_TARGET_FPS` | 目标帧率 |

> 译注（源码核对）：当前代码使用 `VIDEO_FOURCC_FROM_STR` 将配置转为四字符代码（FourCC），应填写驱动能力中实际支持的代码。不能因原文写出格式名称MJPEG，就将任意长度的名称当作有效FourCC。当前示例还按宽×高×2计算缓冲区大小，并不是通用于所有压缩或平面格式的大小计算器。

### 125.4.2\_内存配置（Memory Configuration）

| 配置 | 说明 |
| --- | --- |
| [`CONFIG_VIDEO_BUFFER_POOL_NUM_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_NUM_MAX) | 视频缓冲区数量 |
| [`CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE) | 缓冲池容量，单位为字节 |
| [`CONFIG_VIDEO_BUFFER_POOL_ALIGN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_ALIGN) | 缓冲区对齐（Alignment） |
| [`CONFIG_HEAP_MEM_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEAP_MEM_POOL_SIZE) | 通用堆（Heap）容量 |
| [`CONFIG_MAIN_STACK_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAIN_STACK_SIZE) | 主线程栈（Main Thread Stack）大小 |

### 125.4.3\_USB传输配置（USB Transfer Configuration）

| 配置 | 说明 |
| --- | --- |
| [`CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS) | 并发等时传输（Isochronous Transfer，ISO）数量 |
| [`CONFIG_USBH_USB_DEVICE_HEAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_USB_DEVICE_HEAP) | USB设备堆容量 |
| [`CONFIG_UHC_XFER_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_XFER_COUNT) | 最大传输请求数 |
| [`CONFIG_UHC_BUF_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_COUNT) | 传输缓冲区数量 |
| [`CONFIG_UHC_BUF_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_POOL_SIZE) | 传输缓冲池容量 |

### 125.4.4\_日志配置（Logging Configuration）

| 配置 | 说明 |
| --- | --- |
| [`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG) | 启用日志 |
| [`CONFIG_LOG_BUFFER_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BUFFER_SIZE) | 日志缓冲区容量 |
| [`CONFIG_USBH_UVC_LOG_LEVEL_INF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_UVC_LOG_LEVEL_INF) | UVC驱动的信息级日志（Info Log Level） |

## 125.5\_故障排查（Troubleshooting）

### 125.5.1\_内存分配失败（Memory Allocation Failures）

出现内存分配错误时，增大堆容量或减少缓冲区数量：

- [`CONFIG_HEAP_MEM_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HEAP_MEM_POOL_SIZE)：增大通用堆容量。
- [`CONFIG_VIDEO_BUFFER_POOL_NUM_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_NUM_MAX)：减少视频缓冲区数量。
- `CONFIG_APP_VIDEO_FRAME_WIDTH`：降低帧宽，减少内存占用。
- `CONFIG_APP_VIDEO_FRAME_HEIGHT`：降低帧高，减少内存占用。

### 125.5.2\_丢帧或帧损坏（Dropped or Corrupted Frames）

出现丢帧或数据损坏时，增加缓冲资源或降低数据速率，相关选项包括：

- [`CONFIG_VIDEO_BUFFER_POOL_NUM_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_NUM_MAX)。
- [`CONFIG_UHC_BUF_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_POOL_SIZE)。
- [`CONFIG_UHC_BUF_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_COUNT)。
- `CONFIG_APP_VIDEO_TARGET_FPS`。
- [`CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS)。
- `CONFIG_APP_VIDEO_FRAME_WIDTH`。
- `CONFIG_APP_VIDEO_FRAME_HEIGHT`。

### 125.5.3\_性能问题（Performance Issues）

视频采集缓慢或不流畅时，可以尝试降低数据速率、减少日志，或启用优化；相关选项包括：

- `CONFIG_APP_VIDEO_FRAME_WIDTH`。
- `CONFIG_APP_VIDEO_FRAME_HEIGHT`。
- `CONFIG_APP_VIDEO_TARGET_FPS`。
- [`CONFIG_USBH_UVC_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_UVC_LOG_LEVEL_WRN)：警告级日志（Warning Log Level）。
- [`CONFIG_DEBUG_OPTIMIZATIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_OPTIMIZATIONS)：调试优化（Debug Optimizations）。
- [`CONFIG_SPEED_OPTIMIZATIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPEED_OPTIMIZATIONS)：速度优化（Speed Optimizations）。

UVC缓冲区分配通过USB主机和Video配置项共同控制。遇到内存分配问题，或希望维持更高帧率时，可检查：

- [`CONFIG_UHC_BUF_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_COUNT)。
- [`CONFIG_UHC_BUF_POOL_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_BUF_POOL_SIZE)。
- [`CONFIG_UHC_XFER_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_XFER_COUNT)。
- [`CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_VIDEO_CONCURRENT_TRANSFERS)。
- [`CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_HEAP_SIZE)。
- [`CONFIG_VIDEO_BUFFER_POOL_NUM_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO_BUFFER_POOL_NUM_MAX)。

> 译注：这些列表是原文列出的调节入口，不表示所有选项都应同时增大或启用。视频帧缓冲池、UHC传输池和通用堆服务不同分配路径，应结合错误来源核对；降低日志开销也不等于降低帧数据占用。

## 125.6\_另请参阅（See Also）

- [视频驱动（Video Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html)。
- [USB 主机核心 API](P079_USB主机核心API.md)。


译注核对来源：[samples/subsys/usb/host_uvc/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/host_uvc/src/main.c)、[samples/subsys/usb/host_uvc/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/host_uvc/Kconfig)、[samples/subsys/usb/host_uvc/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/host_uvc/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/host_uvc/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-host-uvc"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="viewing-supported-formats"></a>
<a id="configuring-video-format"></a>
<a id="adjusting-frame-rate"></a>
<a id="accessing-the-video-controls"></a>
<a id="frame-statistics"></a>
<a id="configuration-options"></a>
<a id="video-format"></a>
<a id="memory-configuration"></a>
<a id="usb-transfer-configuration"></a>
<a id="logging-configuration"></a>
<a id="troubleshooting"></a>
<a id="memory-allocation-failures"></a>
<a id="dropped-or-corrupted-frames"></a>
<a id="performance-issues"></a>
<a id="see-also"></a>

[上一章](P124_USB视频摄像头示例.md) · [返回大纲](大纲.md) · [下一章](P126_USB视频设备绑定.md)
