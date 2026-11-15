---
id: learning.zephyr-docs.usb.page-132
title: 旧版USB串口控制台示例
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/console/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第132章\_旧版USB串口控制台示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/subsys/usb/legacy/console/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 132.1\_概述

这是一个简单的 Hello World 示例，通过通信设备类（Communication Device Class，CDC）的抽象控制模型（Abstract Control Model，ACM）UART 输出控制台信息。其主要目的是展示所需的配置选项。

## 132.2\_运行要求

此项目需要 USB 设备控制器驱动（USB Device Controller Driver）。

## 132.3\_构建与运行

此示例可以为多种开发板构建。下面以 `reel_board` 为例：

```shell
west build -b reel_board samples/subsys/usb/legacy/console
west flash
```

把开发板连接到主机，例如运行 Linux 的 PC。开发板会被识别为 `CDC_ACM` 串口设备。要查看示例的控制台输出，可使用类似 `minicom -D /dev/ttyACM0` 的命令。

```text
Hello World! arm
Hello World! arm
Hello World! arm
Hello World! arm
```

> 译注：构建命令相对 Zephyr 源码根目录执行；设备节点编号按主机实际枚举结果选择。当前 `main.c` 用构建断言要求 `zephyr,console` 指向 `zephyr,cdc-acm-uart` 设备，调用 `usb_enable(NULL)` 后等待主机设置数据终端就绪（Data Terminal Ready，DTR），再每秒输出一行 `Hello World!` 和 `CONFIG_ARCH`。因此设备已经枚举、但终端没有设置 DTR 时，仍可能看不到输出。`prj.conf` 选择旧设备栈并关闭启动时自动初始化，初始化由示例代码完成。

## 132.4\_故障排查

如果 modemmanager 在后台尝试访问设备，可能需要用 `sudo stop modemmanager` 停止它。

> 译注：上述停止命令按官方原页保留；主机是否有此服务管理命令取决于所用系统，不能仅因使用 Linux 就认定它可用。这里没有执行服务管理操作。

## 132.5\_另见

- [USB 设备核心 API](P155_旧版USB设备栈核心API.md)。


译注核对来源：[samples/subsys/usb/legacy/console/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/console/src/main.c)、[samples/subsys/usb/legacy/console/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/legacy/console/prj.conf)。

本仓库的[对应源码](../../../samples/subsys/usb/legacy/console/src/main.c)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="legacy-usb-cdc-acm-console"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="troubleshooting"></a>
<a id="see-also"></a>

[上一章](P131_旧版CDC_ACM串口回显示例.md) · [返回大纲](大纲.md) · [下一章](P133_旧版USB固件升级示例.md)
