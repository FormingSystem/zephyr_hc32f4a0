---
id: learning.zephyr-docs.usb.page-139
title: 旧版USB麦克风与耳机示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/audio_headphones_microphone/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_旧版USB麦克风与耳机示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/audio_headphones_microphone/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 139.1\_概述

此应用演示 Zephyr 提供的 USB 音频（USB Audio）驱动。这个简单示例通过 IN／OUT 等时端点（Isochronous Endpoint，ISO Endpoint）执行环回（Loopback）。主机将其显示为两个音频设备：一个输入设备，即麦克风（Microphone）；一个输出设备，即耳机（Headphones）。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 139.2\_构建与运行

构建示例时，必须提供包含所需选项的设备树覆盖文件（Devicetree Overlay）。默认加入 `app.overlay`。覆盖文件包含软件和硬件相关信息，用于完整描述设备。

构建示例应用镜像并烧录到开发板后，将开发板连接到主机设备。

> 译注：当前 `app.overlay` 分别声明 `usb-audio-hp` 耳机节点与 `usb-audio-mic` 麦克风节点。示例为二者分别注册回调表：耳机接收回调将收到的缓冲区送往麦克风设备，且只有接收长度等于麦克风 IN 帧大小时才发送。大小不符或发送失败会释放缓冲区。此处麦克风输入来自软件环回，不是实际麦克风采样；音量控制回调仅记录收到的音量，没有对音频样本做缩放。

## 139.3\_测试

按以下步骤测试示例：

1. 按上文构建并烧录示例。
2. 连接主机（Host）。
3. 选择默认的音频输入／输出设备（Audio IN/OUT）。
4. 开始音频流，例如在主机播放音频文件。
5. 开始录制音频流，例如使用 Audacity。
6. 检查录制的音频流。

> 译注：主机把音频播放到此示例的耳机输出设备，再从其麦克风输入设备录音，才能检查这条环回路径。本页保留官方测试步骤，本轮没有执行音频或 USB 硬件验证。

## 139.4\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/audio_headphones_microphone/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headphones_microphone/src/main.c)、[samples/subsys/usb/legacy/audio_headphones_microphone/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headphones_microphone/prj.conf)、[samples/subsys/usb/legacy/audio_headphones_microphone/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/audio_headphones_microphone/app.overlay)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/audio_headphones_microphone/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-audio-headphones-microphone"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="testing"></a>
<a id="see-also"></a>

[上一章](P138_旧版USB音频耳麦示例.md) · [返回大纲](大纲.md) · [下一章](P140_旧版WebUSB示例.md)
