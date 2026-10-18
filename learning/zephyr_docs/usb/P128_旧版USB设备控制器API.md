---
id: learning.zephyr-docs.usb.page-128
title: 旧版USB设备控制器API
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_dc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第128章\_旧版USB设备控制器API

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/device/api/usb_dc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

USB 设备控制器驱动 API 在 [include/zephyr/drivers/usb/usb_dc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/usb_dc.h) 中描述，有时也称为 `usb_dc` API。

此 API 在设计上存在一些限制：它不遵循[设备驱动模型（Device Driver Model）](../hardware/P003_设备驱动模型.md#device-model-api)，正在由 [USB 设备控制器（USB Device Controller，UDC）驱动 API](P029_USB设备控制器API说明.md#udc-api) 取代。

## 128.1\_API 参考

- [USB 设备控制器 API（USB Device Controller API）](P152_旧版USB控制器驱动API.md)。

> 译注：`usb_dc` 与 UDC 是两套接口；这里的替代关系不表示给函数改名即可完成驱动迁移。源码跟踪时先确认目标栈使用的头文件和设备模型，再对照相应控制器驱动接口。本页是旧接口的说明与参考入口，不是完整驱动迁移步骤。


译注核对来源：[include/zephyr/drivers/usb/usb_dc.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/usb/usb_dc.h)。

本仓库的[对应源码](../../../include/zephyr/drivers/usb/usb_dc.h)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-device-controller-driver-api-deprecated"></a>
<a id="usb-dc-api"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：旧版USB设备API入口](P127_旧版USB设备API入口.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：旧版USB设备核心API](P129_旧版USB设备核心API.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P127_旧版USB设备API入口.md) · [返回大纲](大纲.md) · [下一章](P129_旧版USB设备核心API.md)

</details>

<!-- reading-navigation:end -->
