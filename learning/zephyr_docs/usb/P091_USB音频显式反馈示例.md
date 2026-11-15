---
id: learning.zephyr-docs.usb.page-91
title: USB音频显式反馈示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/uac2_explicit_feedback/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第91章\_USB音频显式反馈示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/uac2_explicit_feedback/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 91.1\_概述（Overview）

本示例演示如何实现带有显式反馈（Explicit Feedback）的 USB 异步音频播放（Asynchronous Audio Playback）。它可以运行在支持 USB 和 I2S 的开发板上，但原文说明反馈计算目前仅针对 Nordic nRF5340 芯片实现。

运行本示例的设备向主机呈现为全速异步 USB 音频 2 类设备（Full-Speed Asynchronous USB Audio 2 Class Device），支持 48 kHz、16 位、双声道（立体声，Stereo）播放。

> 警告（Warning，官方原文）：从 Windows 10 1703 版本开始提供的 Microsoft Windows USB Audio 2.0 驱动要求全速显式反馈端点的 `wMaxPacketSize` 等于 4；原文指出这违反 USB 2.0 规范。Windows 反馈中心报告见 [原文提供的报告入口](https://aka.ms/AArvnax)。仅用于 Windows 时，可以通过 [`CONFIG_USBD_UAC2_FS_WINDOWS_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_UAC2_FS_WINDOWS_WORKAROUND) 覆盖 `wMaxPacketSize`。

## 91.2\_显式反馈（Explicit Feedback）

实际采样时钟（Sample Clock）不由 USB 主机控制时，使用异步 USB 音频。采样时钟独立于 USB 帧起始（Start of Frame，SOF），因此，按音频接收端（Audio Sink，I2S）计量的 1 ms 必然比按音频发送端（Audio Source，USB 主机）计量的 1 ms 略长或略短。长期累积会导致缓冲区溢出（Overrun）或欠载（Underrun）。设备通过向主机提供显式反馈，告诉主机每帧平均需要多少采样。主机在各帧发送包含标称数量或标称数量 ±1 个采样的数据包，实现所需平均值。

没有目标平台专用反馈代码时，使用占位反馈实现（Dummy Feedback Implementation）。它返回的反馈值使主机每帧都发送标称数量的采样。理论上，可以利用 I2S 和 USB 中断取得时序信息，但原文说明这两个子系统目前都没有提供所需的时间戳（Timestamp）信息。

> 译注：占位反馈不会测量实际时钟偏差，不能因此认为已经解决长期时钟漂移（Clock Drift）。以上“目前”的范围以保存的官方网页为准。

## 91.3\_nRF5340 上的显式反馈（Explicit Feedback on nRF5340）

nRF5340 可以利用分布式可编程外设互连（Distributed Programmable Peripheral Interconnect，DPPI）、定时器（TIMER）和 GPIO 任务与事件输入（GPIO Tasks and Events，GPIOTE），相对于 USB SOF 统计 I2S 左右声道时钟（LRCLK）的两个边沿。如果 GPIOTE 输入不可用，也可以配置 nRF5340 的 DPPI 和 TIMER 外设，取得 I2S 帧开始（FRAMESTART）与 USB SOF 之间的相对时序信息。

官方已在 nRF5340 DK 上测试本示例的两种模式：直接采样计数，以及间接测量 I2S 缓冲区输出相对于 USB SOF 的偏移。

示例默认采用间接反馈计算。直接采样计数需要在 nRF5340 DK 上，用外部连线将 I2S LRCLK 输出引脚连接到 GPIOTE 输入引脚，后者在代码中固定为 P1.09。间接模式不需要额外连线，甚至可以不连接 I2S 设备，通过逻辑分析仪（Logic Analyzer）等工具检查 I2S 信号。

> 译注（源码核对）：保存的官方示例 Kconfig 通过 `CONFIG_APP_USE_I2S_LRCLK_EDGES_COUNTER` 选择直接边沿计数，并已列出 nRF54 的 TDM FSYNC 到 P0.08 连接说明。这说明该配置文件的覆盖范围比网页中“仅 nRF5340”的表述更广；不能据此把任意支持 USB/I2S 的板都视为已具备正确反馈实现。本文保留网页描述和其 nRF5340 命令。

## 91.4\_构建与运行（Building and Running）

示例代码位于官方源码树的 [`samples/subsys/usb/uac2_explicit_feedback`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/uac2_explicit_feedback)。

以下为官方构建和烧录命令。译注：在已按入门文档准备好工具链、west 和板卡烧录工具的终端中，从 Zephyr 源码根目录执行；Windows 通用工程操作可使用 UCRT64 Bash，Linux 使用 Bash。目标是 nRF5340 DK 的应用处理器，接好对应开发板后再执行烧录。

```shell
west build -b nrf5340dk/nrf5340/cpuapp samples/subsys/usb/uac2_explicit_feedback
west flash
```

## 91.5\_另请参阅（See Also）

- [USB 设备核心 API](P015_USB设备核心API.md)。
- [USB 音频类 2 设备 API](P089_USB音频2设备API.md)。
- [集成电路间音频接口（Inter-IC Sound，I2S）](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html)。


译注核对来源：[samples/subsys/usb/uac2_explicit_feedback/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_explicit_feedback/src/main.c)、[samples/subsys/usb/uac2_explicit_feedback/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_explicit_feedback/Kconfig)、[samples/subsys/usb/uac2_explicit_feedback/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_explicit_feedback/prj.conf)、[samples/subsys/usb/uac2_explicit_feedback/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/uac2_explicit_feedback/app.overlay)。

本仓库的[对应源码](../../../samples/subsys/usb/uac2_explicit_feedback/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="uac2-explicit-feedback"></a>
<a id="overview"></a>
<a id="explicit-feedback"></a>
<a id="explicit-feedback-on-nrf5340"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P090_USB音频2回调接口.md) · [返回大纲](大纲.md) · [下一章](P092_USB音频隐式反馈示例.md)
