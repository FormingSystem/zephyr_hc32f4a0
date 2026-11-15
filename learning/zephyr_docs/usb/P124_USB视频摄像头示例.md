---
id: learning.zephyr-docs.usb.page-124
title: USB视频摄像头示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/uvc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第124章\_USB视频摄像头示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/uvc/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 124.1\_概述（Overview）

本示例演示如何使用 USB 视频类（USB Video Class，UVC）实例，通过 USB 发送视频数据。连接后，主机上会出现一个视频设备，可以像普通网络摄像头（Webcam）一样使用。主机软件随后就能将该视频流作为本地视频源访问。

## 124.2\_要求（Requirements）

本示例使用新版 USB 设备栈（USB Device Stack），要求 USB 设备控制器已适配 [USB 设备控制器（UDC）驱动 API](P029_USB设备控制器API说明.md#udc-api)。

## 124.3\_构建与运行（Building and Running）

如果开发板没有受支持的摄像头，可以使用 [视频软件生成器片段（Video Software Generator Snippet，video-sw-generator）](../snippets/P005_视频软件发生器配置片段.md#snippet-video-sw-generator)。它生成软件测试图案，除 USB 接口外不需要额外硬件：

译注：以下 west 命令从已配置好工具链、west 和目标板烧录工具的 Zephyr 源码根目录执行。Windows 通用工程操作可使用 UCRT64 Bash，Linux 使用 Bash；分别选择与命令匹配的开发板。

```shell
west build -b frdm_mcxn947/mcxn947/cpu0 -S video-sw-generator samples/subsys/usb/uvc
west flash
```

如果开发板配备受支持的图像传感器（Image Sensor），并将其配置为 `zephyr,camera` chosen 节点，就会使用它作为视频源。此时可按如下方式构建：

```shell
west build -b arduino_nicla_vision/stm32h747xx/m7 samples/subsys/usb/uvc
west flash
```

设备预期会被识别为摄像头。

### 124.3.1\_Ubuntu

`dmesg` 日志预期包含 `generic UVC device`；`lsusb` 预期显示 Zephyr 设备条目。更多调试信息参阅 [Ideas on board 常见问题](https://www.ideasonboard.org/uvc/faq/)。

### 124.3.2\_MacOS

原文说明，`dmesg` 日志预期会提到视频设备。`ioreg -p IOUSB` 列出包括摄像头在内的 USB 设备；`system_profiler SPCameraDataType` 列出视频输入设备。

### 124.3.3\_Windows

设备管理器（Device Manager）或 USBView 工具可列出 USB 设备；第三方 USB Tree View 可查看和调试描述符（Descriptors）。

此外，USB-IF 的 [USB3CV](https://www.usb.org/document-library/usb3cv) 工具可以检查设备是否符合 UVC 标准。

> 译注（工具范围）：以上为Zephyr原文表述；USB-IF页面将USB3CV定位为USB 3集线器和设备框架测试工具。完成这些测试不能单独视为全部UVC视频功能已经通过认证；具体项目需按实际测试套件的覆盖范围判断。

### 124.3.4\_播放视频流（Playing the Stream）

系统会将设备识别为原生摄像头，任何视频应用都可使用。例如在 VLC 中，依次选择“媒体（Media）→打开采集设备（Open Capture Device）→采集设备（Capture Device）→视频设备名称（Video device name）”。也可以使用 GStreamer 和 FFmpeg。

**Ubuntu**：假设 `/dev/video0` 是 Zephyr 设备。

```shell
ffplay -i /dev/video0
```

```shell
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! autovideosink
```

**MacOS**：假设 `0:0` 是 Zephyr 设备。

```shell
ffplay -f avfoundation -i 0:0
```

```shell
gst-launch-1.0 avfvideosrc device-index=0 ! autovideosink
```

**Windows**：假设 `UVC sample` 是 Zephyr 设备。

```shell
ffplay.exe -f dshow -i video="UVC sample"
```

```shell
gst-launch-1.0.exe ksvideosrc device-name="UVC sample" ! videoconvert ! autovideosink
```

译注：这些是主机侧命令，工作目录不限，需要该平台已安装相应软件并可从终端调用。`/dev/video0` 是 Linux 设备节点，不是作者仓库位置；设备编号、名称应按本机枚举结果替换。保留官方平台命令写法。

视频设备也可以供网页应用和视频通话系统使用。原文还预期 Android 和 iPad 可通过专用应用使用，但当时尚不支持 iOS。

### 124.3.5\_访问视频控制项（Accessing the Video Controls）

与其他摄像头一样，主机上的各种应用可以通过视频源控制界面访问这些控制项。

**Ubuntu**：假设 `/dev/video0` 是 Zephyr 设备。以下为查询和设置控制项的原始命令及输出，`$` 表示提示符，复制命令时不输入它：

```console
$ v4l2-ctl --device /dev/video0 --list-ctrls

Camera Controls

                  auto_exposure 0x009a0901 (menu)   : min=0 max=3 default=1 value=1 (Manual Mode)
     exposure_dynamic_framerate 0x009a0903 (bool)   : default=0 value=0
         exposure_time_absolute 0x009a0902 (int)    : min=10 max=2047 step=1 default=384 value=384 flags=inactive

$ v4l2-ctl --device /dev/video0 --set-ctrl auto_exposure=1
$ v4l2-ctl --device /dev/video0 --set-ctrl exposure_time_absolute=1500
```

**MacOS**：[VLC](https://www.videolan.org/vlc/) 客户端和系统摄像头设置（Webcam Settings）面板允许调整受支持的视频控制项。

**Windows**：[VLC](https://www.videolan.org/vlc/) 和 [Pot Player](https://potplayer.tv/) 客户端可进一步访问视频控制项。

### 124.3.6\_软件处理（Software Processing）

软件处理工具也可以直接使用视频接口。以下为 OpenCV 示例，其安装命令为 `pip install opencv-python`。译注：这是主机 Python 环境的依赖，可在读者选用的虚拟环境中安装；本批未执行安装。

```python
import cv2

# Number of the /dev/video# interface
devnum = 2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(devnum)

while (val := vc.read())[0]:
    cv2.waitKey(20)
    cv2.imshow("preview", val[1])

cv2.destroyWindow("preview")
vc.release()
```

译注：代码注释表示 `devnum` 是 `/dev/video#` 接口编号；示例设为2，与前面假设的video0不是同一编号，应按实际设备修改。程序创建预览窗口，逐帧读取和显示，结束后销毁窗口并释放采集对象。

## 124.4\_源码核对译注

当前示例可使用摄像头或所配置的视频编码器（Video Encoder）输出作为UVC源。它会按受支持像素格式和单缓冲区容量筛选向主机发布的格式；因此摄像头驱动支持的全部格式未必都出现在USB描述符中。启用UVC后还要等待主机选择格式、准备视频缓冲区并启动传输，不能将枚举成功等同于图像传输已成功。

## 124.5\_另请参阅（See Also）

- [USB 设备核心 API](P015_USB设备核心API.md)。
- [USB 视频类设备 API](P122_USB视频设备API.md)。
- [视频驱动（Video Drivers）](https://docs.zephyrproject.org/latest/doxygen/html/group__video__interface.html)。


译注核对来源：[samples/subsys/usb/uvc/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uvc/src/main.c)、[samples/subsys/usb/uvc/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uvc/Kconfig)、[samples/subsys/usb/uvc/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uvc/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/uvc/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="uvc"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="tab-0-VWJ1bnR1"></a>
<a id="tab-0-TWFjT1M="></a>
<a id="tab-0-V2luZG93cw=="></a>
<a id="panel-0-VWJ1bnR1"></a>
<a id="panel-0-TWFjT1M="></a>
<a id="panel-0-V2luZG93cw=="></a>
<a id="playing-the-stream"></a>
<a id="tab-1-VWJ1bnR1"></a>
<a id="tab-1-TWFjT1M="></a>
<a id="tab-1-V2luZG93cw=="></a>
<a id="panel-1-VWJ1bnR1"></a>
<a id="panel-1-TWFjT1M="></a>
<a id="panel-1-V2luZG93cw=="></a>
<a id="accessing-the-video-controls"></a>
<a id="tab-2-VWJ1bnR1"></a>
<a id="tab-2-TWFjT1M="></a>
<a id="tab-2-V2luZG93cw=="></a>
<a id="panel-2-VWJ1bnR1"></a>
<a id="panel-2-TWFjT1M="></a>
<a id="panel-2-V2luZG93cw=="></a>
<a id="software-processing"></a>
<a id="see-also"></a>

[上一章](P123_USB视频头文件接口.md) · [返回大纲](大纲.md) · [下一章](P125_USB主机摄像头示例.md)
