---
id: learning.zephyr-docs.usb.page-92
title: USB音频隐式反馈示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/uac2_implicit_feedback/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第92章\_USB音频隐式反馈示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/uac2_implicit_feedback/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 92.1\_概述（Overview）

本示例演示如何实现带有隐式反馈（Implicit Feedback）的 USB 异步双向音频（Asynchronous Bidirectional Audio）。主机根据接收到的单声道麦克风（Mono Microphone）采样数量，调整向耳机播放端发送的立体声（Stereo）采样数量。

> 警告（Warning，官方原文）：从 Windows 10 1703 版本开始提供的 Microsoft Windows USB Audio 2.0 驱动不支持隐式反馈。

## 92.2\_要求（Requirements）

目标平台必须能够测量 I2S 数据块起始，即输出缓冲区中的第一个采样输出时刻，相对于 USB 帧起始（Start of Frame，SOF）的偏移。报告这一相对偏移时，精度必须达到单个采样。

官方已在 nRF5340 DK 上测试本示例。要实际播放和录制音频，需要连接外部 I2S 模数转换器（Analog-to-Digital Converter，ADC）与 I2S 数模转换器（Digital-to-Analog Converter，DAC）；若只做简单回声（Echo），可以将 I2S 数据输出与 I2S 数据输入短接。

理论上，可以根据 I2S 和 USB 中断取得时序信息，但原文说明，目前这两个子系统都没有提供所需的时间戳（Timestamp）信息。

## 92.3\_构建与运行（Building and Running）

示例代码位于官方源码树的 [`samples/subsys/usb/uac2_implicit_feedback`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/uac2_implicit_feedback)。

以下为官方构建和烧录命令。译注：在已配置工具链、west 和板卡烧录工具的终端中，从 Zephyr 源码根目录执行；Windows 通用工程操作可使用 UCRT64 Bash，Linux 使用 Bash。命令面向 nRF5340 DK 的应用处理器，音频外设或回声连接须按上面的要求准备。

```shell
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/usb/uac2_implicit_feedback
west flash
```

## 92.4\_另请参阅（See Also）

- [USB 设备核心 API](P015_USB设备核心API.md)。
- [USB 音频类 2 设备 API](P089_USB音频2设备API.md)。
- [集成电路间音频接口（Inter-IC Sound，I2S）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html)。


译注核对来源：[samples/subsys/usb/uac2_implicit_feedback/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_implicit_feedback/src/main.c)、[samples/subsys/usb/uac2_implicit_feedback/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_implicit_feedback/Kconfig)、[samples/subsys/usb/uac2_implicit_feedback/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_implicit_feedback/prj.conf)、[samples/subsys/usb/uac2_implicit_feedback/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_implicit_feedback/app.overlay)。

本仓库的[对应源码](../../../samples/subsys/usb/uac2_implicit_feedback/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="uac2-implicit-feedback"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P091_USB音频显式反馈示例.md) · [返回大纲](大纲.md) · [下一章](P093_USBMIDI2设备API说明.md)
