---
id: learning.zephyr-docs.usb.page-69
title: WebUSB示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/webusb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_WebUSB示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/webusb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 69.1\_概述（Overview）

本示例演示如何组合二进制设备对象存储（Binary Device Object Store，BOS）、Microsoft OS 2.0描述符（Descriptor）和WebUSB描述符，实现WebUSB应用。USB功能收到数据后，将其回显给运行在本地主机浏览器中的WebUSB API应用。

## 69.2\_前提条件（Requirements）

需要采用USB设备控制器（USB Device Controller，UDC）API的驱动。主机需要支持WebUSB API的浏览器，例如Chromium或基于Chromium的浏览器。

## 69.3\_构建与运行（Building and Running）

构建并烧录WebUSB示例：

> 译注：在读者的Zephyr源码根目录、Bash终端执行，先准备依赖、工具链和烧录工具，将 `<board to use>` 替换为实际支持的板名。构建成功后再烧录；以下网页操作在连接开发板的主机完成。

```bash
west build -b <board to use> samples/subsys/usb/webusb
west flash
```

## 69.4\_演示（Demonstration）

示例包含一个简单的WebUSB API应用，位于 [samples/subsys/usb/webusb/index.html](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/webusb/index.html)。

有两种方式打开演示页面：

- 在浏览器打开 [WebUSB HTML演示应用](P070_WebUSB浏览器演示.md)。
- 在示例目录启动Web服务器：

```bash
$ python -m http.server
```

然后依次操作：

1. 将开发板连接到主机。
2. 设备启动后，浏览器可能显示“Go to localhost to connect”（前往localhost连接）的通知。点击通知打开演示页；如果没有通知，原文要求在浏览器打开 `http://localhost:8001/`。
3. 点击连接（Connect）按钮连接设备。
4. 点击发送（Send）将文本发给设备；演示应用接收设备返回的相同文本，并在文本区显示。

> 译注（端口核对）：原文没有给 `python -m http.server` 指定端口，该命令默认监听8000；当前 `webusb.h` 的落地页（Landing Page）描述符也是 `localhost:8000`。因此原文8001链接与命令不一致。按原命令启动时使用 `http://localhost:8000/`；若选择8001，需显式指定服务端口，并相应处理固件落地页提示。Python默认端口依据[官方http.server说明](https://docs.python.org/3/library/http.server.html#command-line-interface)。

> 译注：浏览器调用WebUSB需要受支持的安全上下文（Secure Context），例如HTTPS或受信任的localhost，并在用户点击后弹出设备选择器。能显示HTML不等于具备USB访问权限；Markdown预览器也不一定开放该API。没有提示通知时可手动打开页面；无法选择设备时先检查浏览器能力、主机设备权限和固件VID/PID，不以静态页面加载替代USB交互验证。

> 译注（源码跟踪）：当前固件PID为 `0x000A`，HTML过滤器包含该ID。示例通过厂商专用接口的批量端点（Bulk Endpoint）回显数据，并不是浏览器串口API或CDC ACM功能；页面中的“Serial”是原示例名称。原始HTML及仅翻译界面文字的副本见[演示译文](P070_WebUSB浏览器演示.md)。

## 69.5\_参考资料（References）

- [WebUSB API规范（Specification）](https://wicg.github.io/webusb/)。
- [Chrome开发者文档：在Web上访问USB设备（Access USB Devices on the Web）](https://developer.chrome.com/docs/capabilities/usb)。

## 69.6\_参阅（See Also）

[USB设备核心API](P015_USB设备核心API.md)。


译注核对来源：[samples/subsys/usb/webusb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/main.c)、[samples/subsys/usb/webusb/src/sfunc.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/sfunc.c)、[samples/subsys/usb/webusb/src/webusb.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/webusb.h)、[samples/subsys/usb/webusb/src/msosv2.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/src/msosv2.h)、[samples/subsys/usb/webusb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/prj.conf)、[samples/subsys/usb/webusb/index.html](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/index.html)、[samples/subsys/usb/webusb/demo.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/webusb/demo.rst)。

本仓库的[对应源码](../../../samples/subsys/usb/webusb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="webusb"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="demonstration"></a>
<a id="references"></a>
<a id="see-also"></a>

[上一章](P068_USB转I2C桥接示例.md) · [返回大纲](大纲.md) · [下一章](P070_WebUSB浏览器演示.md)
