---
id: learning.zephyr-docs.usb.page-6
title: USBIP协议支持
kind: reference
status: maintained
domains: [zephyr, usb, driver]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/usb/host/usbip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_USBIP协议支持

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/usb/host/usbip.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 6.1\_概述

新的 USB 支持包含对 USB/IP 协议的初步支持。这项功能仍在开发中，本文所述支持范围目前限于导出连接到主机控制器的一个设备。

USB/IP 使用 TCP/IP。底层的 USB 和网络两套协议栈都需要较多内存资源，选择平台时必须考虑这一点。

在 USB/IP 协议中，服务器导出 USB 设备，客户端导入这些设备。Zephyr 实时操作系统（Real-Time Operating System，RTOS）实现的是服务器功能：将连接到运行 Zephyr 的设备上某个 USB 主机控制器的 USB 设备导出。客户端通常运行 Linux 内核，负责导入设备。协议说明见[USB/IP 协议文档](https://www.kernel.org/doc/html/latest/usb/usbip_protocol.html)。

使用 USB/IP 支持前，确保客户端已加载所需模块：

```bash
modprobe vhci_hcd
modprobe usbip-core
modprobe usbip-host
```

客户端还需要 `usbip` 用户工具，可以通过 Linux 发行版的包管理系统安装，也可以从 Linux 内核源码构建。

> 译注：这一节的模块和 `usbip` 命令在 Linux 客户端执行；模块加载需要相应权限。它们不属于 Zephyr Shell 命令。下列 `192.0.2.1` 为官方示例的服务器地址，应对应实际建立的网络连接；命令前的 `$` 是提示符，不是输入内容。

日常使用的基本命令如下。列出导出的 USB 设备：

```console
$ usbip list -r 192.0.2.1
Exportable USB devices
======================
 - 192.0.2.1
        1-1: NordicSemiconductor : unknown product (2fe3:0001)
           : /sys/bus/usb/devices/usb1/1-1
           : Miscellaneous Device / ? / Interface Association (ef/02/01)
           :  0 - Communications / Abstract (modem) / None (02/02/00)
           :  1 - CDC Data / Unused / unknown protocol (0a/00/00)
```

连接总线标识（busid）为 `1-1` 的导出设备：

```console
$ sudo usbip attach -r 192.0.2.1 -b 1-1
```

断开端口 `0` 上已导入的设备：

```console
$ sudo usbip detach -p 0
```

> 译注：`1-1` 是服务器导出的设备标识，`0` 是客户端的导入端口号，两者不能互换。列表中的设备名称、类别与系统路径是原文预期输出，不是本仓库需要建立的目录。

## 6.2\_在 native\_sim 中使用 USB/IP

启用 USB/IP 支持进行开发时，优先使用[native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)。原文指出，真实硬件上的使用尚未得到充分测试。USB/IP 需要网络连接；客户端网络接口的设置方法见[native_sim 开发板联网](../networking/P008_native_sim联网.md#networking-with-native-sim)。

构建和运行带 USB/IP 的示例需要较多配置，可使用 `usbip-native-sim` 配置片段（Snippet）设置主机及 USB/IP 支持。

```bash
# From the root of the zephyr repository
west build -b native_sim/native/64 samples/subsys/usb/cdc_acm -- -DSNIPPET=usbip-native-sim -DEXTRA_DTC_OVERLAY_FILE=app.overlay
```

> 译注：以上构建命令从所使用的 Zephyr 源码根目录执行。当前官方配置片段启用网络、`CONFIG_USB_HOST_STACK` 与 `CONFIG_USBIP`，其设备树覆盖层（Devicetree Overlay）将虚拟设备控制器放在虚拟主机控制器之下；`app.overlay` 则提供示例的 CDC ACM 设备节点。这是模拟控制器与网络组合的开发路线，不能从它推定某块实际开发板已具备同样能力。

> 译注：原文“只支持一个设备”的范围按保存页面保留。当前官方 `Kconfig.usbip` 已提供 `CONFIG_USBIP_DEVICES_COUNT`，默认 1、允许范围 1～255；存在配置项不等于本批已经验证多设备导出。页面和 `main` 源码可能处于不同更新时点。本批没有加载宿主模块、运行服务器或导入真实 USB 设备。


译注核对来源：[snippets/usbip-native-sim/snippet.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/snippet.yml)、[snippets/usbip-native-sim/usbip-native-sim.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/usbip-native-sim.overlay)、[snippets/usbip-native-sim/usbip-native-sim.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/usbip-native-sim/usbip-native-sim.conf)、[subsys/usb/host/Kconfig.usbip](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/host/Kconfig.usbip)、[samples/subsys/usb/cdc_acm/app.overlay](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/subsys/usb/cdc_acm/app.overlay)。

本仓库的[对应源码](../../../snippets/usbip-native-sim/snippet.yml)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="usb-ip-protocol-support"></a>
<a id="usbip"></a>
<a id="overview"></a>
<a id="usb-ip-with-native-sim"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB测试与示例约定](P005_USB测试与示例约定.md) · [本模块主线目录](../reading/usb.md) · [全部主线](../reading/README.md) · [下一篇：USBC设备栈](P007_USBC设备栈.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_USB测试与示例约定.md) · [返回大纲](大纲.md) · [下一章](P007_USBC设备栈.md)

</details>

<!-- reading-navigation:end -->
