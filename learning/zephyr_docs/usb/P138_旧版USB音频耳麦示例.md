---
id: learning.zephyr-docs.usb.page-138
title: 旧版USB音频耳麦示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/audio_headset/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第138章\_旧版USB音频耳麦示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/audio_headset/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 138.1\_概述

此应用演示 Zephyr 提供的 USB 音频（USB Audio）驱动。这个简单示例通过 IN／OUT 等时端点（Isochronous Endpoint，ISO Endpoint）执行环回（Loopback）；主机将其显示为一个音频设备。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 138.2\_构建与运行

构建示例时，必须提供包含所需选项的设备树覆盖文件（Devicetree Overlay）。默认加入 `app.overlay`。覆盖文件包含软件和硬件相关信息，用于完整描述设备。

构建示例应用镜像并烧录到开发板后，将开发板连接到主机设备。

> 译注：当前 `app.overlay` 在 `zephyr_udc0` 下创建一个 `usb-audio-hs` 耳麦节点，并配置左右声道、静音与音量功能。`main.c` 收到 OUT 数据后，仅在长度等于 `usb_audio_get_in_frame_size()` 返回的 IN 帧大小时调用 `usb_audio_send()` 进行环回；大小不符或发送失败时释放缓冲区。功能单元（Feature Unit）的回调读取并记录音量值，但此示例没有据此对样本做实际音量缩放。它演示 USB 数据环回，并不证明已驱动实际声学器件。

## 138.3\_测试

按以下步骤测试示例：

1. 按上文构建并烧录示例。
2. 连接主机（Host）。
3. 选择默认的音频输入／输出设备（Audio IN/OUT）。
4. 开始音频流，例如在主机播放音频文件。
5. 开始录制音频流，例如使用 Audacity。
6. 检查录制的音频流。

> 译注：USB IN／OUT 以主机为参照：主机播放数据沿 OUT 端点进入设备，再经环回从 IN 端点返回主机录音。本页保留官方测试步骤，本轮没有执行播放或录音验证。

## 138.4\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/audio_headset/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headset/src/main.c)、[samples/subsys/usb/legacy/audio_headset/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headset/prj.conf)、[samples/subsys/usb/legacy/audio_headset/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headset/app.overlay)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/audio_headset/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-audio-headset"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="testing"></a>
<a id="see-also"></a>

[上一章](P137_旧版USB蓝牙控制器示例.md) · [返回大纲](大纲.md) · [下一章](P139_旧版USB麦克风与耳机示例.md)
