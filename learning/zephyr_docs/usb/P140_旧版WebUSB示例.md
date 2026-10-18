---
id: learning.zephyr-docs.usb.page-140
title: 旧版WebUSB示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/webusb/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第140章\_旧版WebUSB示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/webusb/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

进一步了解 WebUSB，可参阅[在 Web 上访问 USB 设备](https://developers.google.com/web/updates/2016/03/access-usb-devices-on-the-web)。API 规范见 [WebUSB API Specification](https://wicg.github.io/webusb/)。

## 140.1\_概述

这个简单的回显应用演示 WebUSB 示例：设备接收数据，并将数据回送给运行在主机浏览器中的 WebUSB 网页应用。此应用仅用于测试；实际使用场景应基于 WebUSB API 实现相应应用。

> 原文注：此示例演示已弃用的 [USB 设备支持](P008_旧版USB设备支持.md#usb-device-stack)。

## 140.2\_运行要求

此项目需要 USB 设备驱动；Zephyr 支持的多种开发板具有这类驱动。

## 140.3\_构建与运行

用以下命令构建并烧录 WebUSB 示例：

> 译注：在已准备依赖、工具链及烧录工具的 Zephyr 源码根目录、Bash 终端执行；将 `<board to use>` 替换为实际支持的开发板目标，构建成功后再烧录。

```bash
west build -b <board to use> samples/subsys/usb/legacy/webusb
west flash
```

## 140.4\_在主机使用最新版 Google Chrome 测试

此示例需要最新版 Google Chrome、用于连接 USB 设备的 WebUSB API 网页，以及可选的本地主机 HTTP 服务器，用于提供该网页。

WebUSB 是加入 Web 的强大新功能，仅向安全来源（Secure Origin）开放。这意味着用于连接设备的网页或站点必须通过安全连接（HTTPS）提供。

> 译注：上段保留原文表述；本地 `localhost` 也可以作为受信任的安全上下文（Secure Context）使用，故下文的本机 HTTP 演示与此要求并不矛盾。是否能够实际调用 WebUSB，仍取决于浏览器实现和 USB 访问权限，不能仅凭网页显示成功推定可用。依据见 [WebUSB 规范](https://usb.spec.whatwg.org/)与[安全上下文规范](https://w3c.github.io/webappsec-secure-contexts/#is-origin-trustworthy)。

在主机运行演示的步骤如下：

1. 在主机运行最新版 Google Chrome。
2. 使用 WebUSB API 实现网页应用，并在 `localhost` 运行。随附示例位于 [samples/subsys/usb/legacy/webusb/index.html](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/usb/legacy/webusb/index.html)；它演示如何创建和使用 WebUSB 接口，以及浏览器与支持 WebUSB 的设备之间如何通信。

访问示例页面有两种方式：直接在 Chrome 打开 [WebUSB HTML 演示应用](P141_旧版WebUSB浏览器演示.md)；或者在本机托管演示页，在 `webusb` 示例目录启动 Web 服务器：

```shell
$ python -m http.server
```

然后在 Chrome 打开 `http://localhost:8001/`。

> 译注：上方命令和 URL 按原文保留，但端口不一致。`python -m http.server` 默认使用 8000 端口，原 URL 使用 8001。可使用 `http://localhost:8000/`，或者显式运行 `python -m http.server 8001 --bind 127.0.0.1` 后访问 8001。命令前的 `$` 是终端提示符，不是需要输入的字符。端口规则见 [Python 官方 http.server 文档](https://docs.python.org/3/library/http.server.html#command-line-interface)。

3. 将开发板连接到主机。
4. 设备启动后，应看到 Chrome 通知“Go to localhost to connect.”，即“前往 localhost 连接”。点击通知打开演示页。原文指出，当时 Windows 上的 Chrome 禁用了 WebUSB 着陆页通知（Landing Page Notification），参阅 [WebUSB 实现状态](https://github.com/WICG/webusb#implementation-status)。
5. 点击“Connect”（连接）按钮，连接设备。
6. 点击“Send”（发送）按钮，把一些文本发送给设备。演示应用会收到设备回送的相同文本，并显示在文本区。

> 译注：通知状态是原页的历史说明，不作为当前 Chrome 版本行为的保证；没有通知时可手动打开页面。随附 HTML 及全部界面文字的中文对照见[旧版演示页](P141_旧版WebUSB浏览器演示.md)。旧脚本固定声明接口 0，并按端点数组顺序取 IN／OUT 端点，不应与新版脚本自动查找厂商专用接口的行为混淆。

## 140.5\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/webusb/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/webusb/src/main.c)、[samples/subsys/usb/legacy/webusb/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/webusb/prj.conf)、[samples/subsys/usb/legacy/webusb/src/webusb.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/webusb/src/webusb.h)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/webusb/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-webusb"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="testing-with-the-latest-google-chrome-on-host"></a>
<a id="see-also"></a>

[上一章](P139_旧版USB麦克风与耳机示例.md) · [返回大纲](大纲.md) · [下一章](P141_旧版WebUSB浏览器演示.md)
