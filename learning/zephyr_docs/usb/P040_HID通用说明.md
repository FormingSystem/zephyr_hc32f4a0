---
id: learning.zephyr-docs.usb.page-40
title: HID通用说明
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/api/hid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_HID通用说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/api/hid.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 40.1\_HID通用部分

人机接口设备（Human Interface Device，HID）的通用 USB 定义也可在 USB 支持之外使用，定义于 [include/zephyr/usb/class/hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/hid.h)。

## 40.2\_HID类型参考

[USB HID 通用定义](P048_HID通用定义.md)。

## 40.3\_HID项目参考

[USB HID 报告项目（Item）辅助宏](P049_HID报告项目定义.md)。

## 40.4\_HID鼠标和键盘报告描述符

预定义的鼠标与键盘报告描述符（Report Descriptor）可用于 HID 设备实现，也可直接作为示例阅读。

[鼠标和键盘报告描述符](P050_HID报告描述符构造宏.md)。

> 译注：通用描述符定义、设备侧回调及USB传输属于不同层次。通用定义用于组织报告格式；发送报告仍需设备栈和控制器。新版设备接口见下一章，已弃用接口单独保留用于迁移对照。


译注核对来源：[include/zephyr/usb/class/hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/hid.h)。

本仓库的[对应源码](../../../include/zephyr/usb/class/hid.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="human-interface-devices-hid"></a>
<a id="usb-hid-common"></a>
<a id="hid-types-reference"></a>
<a id="hid-items-reference"></a>
<a id="hid-mouse-and-keyboard-report-descriptors"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB设备控制器API说明](P029_USB设备控制器API说明.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：新版HID设备API说明](P041_新版HID设备API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P039_USB缓冲区宏与定义.md) · [返回大纲](大纲.md) · [下一章](P041_新版HID设备API说明.md)

</details>

<!-- reading-navigation:end -->
