---
id: learning.zephyr-docs.usb.page-88
title: USB音频2设备API说明
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/uac2_device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_USB音频2设备API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/uac2_device.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 88.1\_音频类 2 设备 API（Audio Class 2 Device API）

USB 音频类 2（USB Audio Class 2）设备专用 API 定义于 [`include/zephyr/usb/class/usbd_uac2.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_uac2.h)。

## 88.2\_API 参考（API Reference）

[USB 音频类 2 设备 API](P089_USB音频2设备API.md)。

## 88.3\_相关代码示例（Related Code Samples）

- [USB 音频异步显式反馈示例](P091_USB音频显式反馈示例.md#uac2-explicit-feedback)：通过 I2S 播放音频的 USB 音频 2 显式反馈（Explicit Feedback）示例。
- [USB 音频异步隐式反馈示例](P092_USB音频隐式反馈示例.md#uac2-implicit-feedback)：通过 I2S 接口播放立体声音频、录制单声道音频的 USB 音频 2 隐式反馈（Implicit Feedback）示例。


译注核对来源：[include/zephyr/usb/class/usbd_uac2.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_uac2.h)。

本仓库的[对应源码](../../../include/zephyr/usb/class/usbd_uac2.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="audio-class-2-device-api"></a>
<a id="uac2-device"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB主机控制器API说明](P072_USB主机控制器API说明.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USBMIDI2设备API说明](P093_USBMIDI2设备API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P087_USB主机类匹配条件.md) · [返回大纲](大纲.md) · [下一章](P089_USB音频2设备API.md)

</details>

<!-- reading-navigation:end -->
