---
id: learning.zephyr-docs.usb.page-41
title: 新版HID设备API说明
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/usbd_hid_device.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_新版HID设备API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/usbd_hid_device.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 41.1\_HID设备接口

HID 设备专用 API 定义于 [include/zephyr/usb/class/usbd_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_hid.h)。

## 41.2\_API参考

[USBD HID 设备 API](P042_新版HID设备API.md)。

## 41.3\_相关代码示例

| 官方示例 | 用途 |
| --- | --- |
| [USB HID 键盘](P051_HID键盘示例.md#usb-hid-keyboard) | 实现基本的 HID 键盘设备。 |
| [USB HID 鼠标](P052_HID鼠标示例.md#usb-hid-mouse) | 实现基本的 HID 鼠标设备。 |

> 译注：报告描述符说明数据布局，用户回调负责解释和产生报告内容；设备类只处理USB相关部分。回调运行于USB设备栈线程，不得阻塞。同步提交、异步完成和报告缓冲区生命周期见后续API及回调参考，不由这篇入口说明代替。


译注核对来源：[include/zephyr/usb/class/usbd_hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/usbd_hid.h)。

本仓库的[对应源码](../../../include/zephyr/usb/class/usbd_hid.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="hid-device-api"></a>
<a id="usbd-hid-device"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HID通用说明](P040_HID通用说明.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：旧版HID类API说明](P044_旧版HID类API说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P040_HID通用说明.md) · [返回大纲](大纲.md) · [下一章](P042_新版HID设备API.md)

</details>

<!-- reading-navigation:end -->
