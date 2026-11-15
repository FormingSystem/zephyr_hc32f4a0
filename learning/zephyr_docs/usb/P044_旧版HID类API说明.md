---
id: learning.zephyr-docs.usb.page-44
title: 旧版HID类API说明
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_device_hid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_旧版HID类API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_device_hid.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 44.1\_已弃用的HID类接口

用于 HID 支持的 USB 设备专用部分定义于 [include/zephyr/usb/class/usb_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usb_hid.h)。

> 译注：本页官方标题已标为弃用（Deprecated）。这里保留旧接口与旧示例供迁移、源码跟踪使用；新接口见[新版HID设备API](P042_新版HID设备API.md)。新版栈中的兼容包装不保证每个旧函数仍具备原行为。

## 44.2\_API参考

[HID 类的 USB 专用定义](P046_旧版HID设备接口API.md)。

## 44.3\_相关代码示例

| 官方示例 | 用途 |
| --- | --- |
| [旧版 USB HID 鼠标](P053_旧版HID鼠标示例.md#legacy-usb-hid-mouse) | 实现基本的 HID 鼠标设备。 |


译注核对来源：[include/zephyr/usb/class/usb_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usb_hid.h)。

本仓库的[对应源码](../../../include/zephyr/usb/class/usb_hid.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-hid-class-api-deprecated"></a>
<a id="usb-hid-device"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：新版HID设备API说明](P041_新版HID设备API说明.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USB大容量存储API说明](P057_USB大容量存储API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P043_HID设备回调接口.md) · [返回大纲](大纲.md) · [下一章](P045_旧版HID类API.md)

</details>

<!-- reading-navigation:end -->
