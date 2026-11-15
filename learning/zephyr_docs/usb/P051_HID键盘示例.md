---
id: learning.zephyr-docs.usb.page-51
title: HID键盘示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/hid-keyboard/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_HID键盘示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/hid-keyboard/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 51.1\_概述

本示例使用新版实验性 USB 设备栈（USB Device Stack）实现人机接口设备（Human Interface Device，HID）键盘。

## 51.2\_要求

需要支持 UDC API 的实验性 USB 设备驱动，并使用[输入子系统（Input）](../interaction/P003_输入子系统.md) API。开发板层必须定义能够产生输入事件的 [`gpio-keys`](../hardware/P563_GPIO按键绑定.md#std-dtcompatible-gpio-keys) 按钮或按键组。至少需要1个按键，最多使用4个：前三个分别用于数字锁定（Num Lock）、大写锁定（Caps Lock）和滚动锁定（Scroll Lock）；第四个一次报告数字键1、2、3和右 Alt 修饰键（Modifier）。

示例最多使用3个 LED，通过 `led0` 等设备树别名配置，用于显示键盘 LED 状态。

> 译注（源码核对）：按键事件码依次为 INPUT_KEY_0 至 INPUT_KEY_3，并非按设备树节点出现顺序自动编号。LED状态来自主机发回的输出报告，不只是本地按键的GPIO翻转。当前 app.overlay 提供 HID 节点；实际按键与LED仍来自板级设备树。

## 51.3\_构建与运行

此示例可为多种开发板构建，原文以 nRF52840DK 为例：

> 译注：在已准备工具链和依赖的 Zephyr 源码根目录，用 Bash 执行下列官方命令。先确认目标板、输入按键和USB连接；构建成功后再烧录，构建失败时返回检查板级配置和依赖。这里保留原目标名称，不表示其他开发板已完成适配。

```bash
west build -b nrf52840dk/nrf52840 samples/subsys/usb/hid-keyboard
west flash
```

> 译注（源码核对）：当前程序先注册报告描述符和回调，再初始化设备栈。收到 iface_ready 的就绪通知后才提交报告。报告采用8字节键盘布局；应用未设置 input_report_done，因此当前提交走同步等待。主机收到锁定键事件后返回LED报告，板上对应LED才随之更新。

> 译注（示例边界）：当前 Get Report 回调只记录“未实现”并返回0；Idle持续时间被保存，但没有用于计算周期性空闲报告。这个示例演示基础键盘报告流程，不等于完整键盘行为均已实现。注册、同步提交与缓冲区约定见[HID设备API](P042_新版HID设备API.md)。

## 51.4\_参阅

- [USB设备核心API](P015_USB设备核心API.md)。
- [USBD HID设备API](P042_新版HID设备API.md)。
- [输入API](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html)。


译注核对来源：[samples/subsys/usb/hid-keyboard/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/hid-keyboard/src/main.c)、[samples/subsys/usb/hid-keyboard/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/hid-keyboard/prj.conf)、[samples/subsys/usb/hid-keyboard/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/hid-keyboard/app.overlay)、[samples/subsys/usb/hid-keyboard/CMakeLists.txt](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/hid-keyboard/CMakeLists.txt)。

本仓库的[对应源码](../../../samples/subsys/usb/hid-keyboard/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-hid-keyboard"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P050_HID报告描述符构造宏.md) · [返回大纲](大纲.md) · [下一章](P052_HID鼠标示例.md)
