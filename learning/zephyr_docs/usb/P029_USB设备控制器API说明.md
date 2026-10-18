---
id: learning.zephyr-docs.usb.page-29
title: USB设备控制器API说明
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/udc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_USB设备控制器API说明

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device_next/api/udc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 29.1\_UDC驱动接口

USB 设备控制器（USB Device Controller，UDC）驱动 API 在 [include/zephyr/drivers/usb/udc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/udc.h) 中定义，简称 UDC 驱动 API。

UDC 驱动 API 尚不稳定，可能在没有事先通知的情况下变化。它用于替代[已弃用的 USB 设备控制器驱动 API](P128_旧版USB设备控制器API.md#usb-dc-api)。如果要把现有驱动移植到 UDC API，或新增驱动，应以 [UDC 驱动骨架](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/udc_skeleton.c)作为起点。

> 译注：这里的驱动骨架（Driver Skeleton）提供函数表、端点注册和同步方式的组织样例；具体控制器的寄存器操作、传输完成处理及能力仍需实现。复制骨架不代表已经完成特定芯片的 USB 支持。

## 29.2\_API参考

- [USB 设备控制器 API](P030_USB设备控制器API.md)：初始化、启用、端点配置、队列和请求缓冲区。
- [USB 缓冲区宏与定义](P039_USB缓冲区宏与定义.md)。

> 译注：控制器接口位于设备栈之下。应用与设备类相关的接口见[设备核心API](P015_USB设备核心API.md)，本册第30至39章说明 UDC 公共 API 和相关数据结构。本页两项直接参考均有对应译文，头文件浏览页和其他控制器参考仍按全站清单单独登记。


译注核对来源：[include/zephyr/drivers/usb/udc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/udc.h)、[drivers/usb/udc/udc_skeleton.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/usb/udc/udc_skeleton.c)。

本仓库的[对应源码](../../../include/zephyr/drivers/usb/udc.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-device-controller-udc-driver-api"></a>
<a id="udc-api"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB设备栈API说明](P014_USB设备栈API说明.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：HID通用说明](P040_HID通用说明.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P028_USB类数据结构.md) · [返回大纲](大纲.md) · [下一章](P030_USB设备控制器API.md)

</details>

<!-- reading-navigation:end -->
