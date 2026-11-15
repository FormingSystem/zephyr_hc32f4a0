---
id: learning.zephyr-docs.networking.page-169
title: WiFi命令行示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/wifi/shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第169章\_WiFi命令行示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/wifi/shell/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例启用 Wi-Fi 命令行（Wi-Fi Shell）模块，以便测试不同开发板的 Wi-Fi 驱动。它提供 `scan`、`connect`、`disconnect` 等命令，也启用 `net_shell` 模块，用于检查网络接口（Network Interface，`net_if`）设置。

官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/wifi/shell)提供应用配置和各开发板适配入口。

## 2. 构建与运行

先确认目标开发板和芯片支持 Wi-Fi。例如，Nordic 的 `nrf7002dk` 可以选择 `nrf7002dk/nrf5340/cpuapp` 目标。

不使用硬件时，可以为 `native_sim` 构建，使用源码树内的 `wifi_hwsim` 驱动。它提供两部虚拟无线电（Virtual Radios），分别用作 AP 和 STA。先在第一个接口启动接入点（Access Point，AP），再从第二个接口扫描并连接。原文构建命令为：

```sh
west build -b native_sim samples/net/wifi/shell
```

使用上述 Nordic 开发板时：

```sh
west build -b nrf7002dk/nrf5340/cpuapp samples/net/wifi/shell
```

> 译注：两条命令是不同目标的构建选择，均从读者自己的 Zephyr 源码根目录执行，并要求相应构建环境和依赖。`native_sim` 还有其主机平台前提，见[原生模拟环境](../native_reference/P004_Native_Simulator本机模拟器.md)；这里并未把 Windows PowerShell 视为可直接运行所有原生仿真操作的环境。虚拟接口只模拟无线通信，不能用它验证真实射频或天线性能。

> 源码对照：当前[native_sim 配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/shell/boards/native_sim.conf)启用两部 `wifi_hwsim` 无线电、AP-STA 模式及 MbedTLS 密码路径，并为 EAPOL 握手开启分组套接字。所有虚拟无线电共享一个 IP 栈，因此配置关闭 [`CONFIG_NET_IP_ADDR_CHECK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP_ADDR_CHECK)，使发往另一个本地接口地址的数据经过模拟介质。实际操作前需在 Shell 中识别接口，不能把下面扫描真实接入点的日志当成仿真器启动后自动产生的结果。

## 3. 示例控制台交互

在设备 Shell 中运行 `wifi --help` 获取各命令的详细说明。本例先扫描接入点，再连接其中一个。原文说明 `--key-mgmt` 指定安全类型，`0` 表示开放网络，`1` 表示 WPA／WPA2 个人模式（Personal）。更多信息可运行 `wifi connect --help`。

以下交互和所有扫描条目按官方原样保留：

```console
shell> wifi scan
Scan requested
shell>
Num  | SSID                             (len) | Chan | RSSI | Sec
1    | kapoueh!                         8     | 1    | -93  | WPA/WPA2
2    | mooooooh                         8     | 6    | -89  | WPA/WPA2
3    | Ap-foo blob..                    13    | 11   | -73  | WPA/WPA2
4    | gksu                             4     | 1    | -26  | WPA/WPA2
----------
Scan request done

shell> wifi connect --ssid "gksu" --key-mgmt 1 --passphrase SecretStuff
Connection requested
shell>
Connected
shell>
```

扫描结果包含 SSID、长度、信道（Channel）、接收信号强度指示（Received Signal Strength Indicator，RSSI）和安全类型（Security）。之后使用 `gksu` 和示例口令 `SecretStuff` 请求连接，最终 `Connected` 表示相应连接事件成功；使用时替换成自己的测试网络信息。

> 版本说明：当前官方[安全类型枚举](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/wifi.h)把数值 `1` 定义为 WPA2-PSK，旧日志中的 WPA／WPA2 文案不应代替当前配置含义。扫描请求已发出、连接请求已发出和最终连接成功是不同阶段，后续 IP 地址与网络连通性还需通过 `net_shell` 单独检查。本次没有运行模拟器或实际连接无线网络。

## 4. 另见（See Also）

[网络统计库（Network Statistics Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__stats.html)。


<a id="wifi-shell"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-console-interaction"></a>
<a id="see-also"></a>

[上一章](P168_通过低功耗蓝牙配置WiFi.md) · [返回大纲](大纲.md) · [下一章](P170_IEEE802154无线网络.md)
