---
id: learning.zephyr-docs.networking.page-10
title: QEMU以太网联网
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_eth_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_QEMU以太网联网

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_eth_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

本页说明Linux主机与QEMU中的Zephyr应用如何建立虚拟网络。示例运行 [高级回显服务器](P047_高级回显服务器示例.md#sockets-echo-server)，通过Linux中表现为以太网接口的tuntap设备与主机连接。

## 10.1\_前置条件和驱动选择

在主机找到 [net-tools](https://github.com/zephyrproject-rtos/net-tools)，标准工作区位于 `tools/net-tools`，或单独克隆：

```sh
git clone https://github.com/zephyrproject-rtos/net-tools
```

准备两个终端：终端1进入net-tools目录（`cd net-tools`）；终端2为已初始化Zephyr环境的开发终端。

配置Zephyr时必须为QEMU选择正确以太网驱动：

| 开发板 | 驱动 |
| --- | --- |
| `qemu_x86` | Intel(R) PRO/1000千兆以太网驱动（`Intel(R) PRO/1000 Gigabit Ethernet driver`），源码中称为 `e1000`。 |
| `qemu_cortex_m3` | TI Stellaris MCU系列以太网驱动（`TI Stellaris MCU family ethernet driver`），源码中称为 `stellaris`。 |
| `mps2_an385` | SMSC911x/9220以太网驱动（`SMSC911x/9220 Ethernet driver`），源码中称为 `smsc911x`。 |
| `qemu_cortex_a53` | 默认选择Intel(R) PRO/1000千兆以太网驱动。 |

回显服务器示例还为 `qemu_x86_64` 的VIRTIO网络设备提供覆盖配置（Overlay）。

## 10.2\_创建主机接口

启动带网络连接的QEMU前，在终端1创建接口：

```sh
./net-setup.sh
```

可通过帮助查看脚本选项并调整行为：

```sh
./net-setup.sh --help
```

## 10.3\_构建并启动应用

终端2在Zephyr源码根构建运行。`qemu_x86` 示例：

```sh
west build -b qemu_x86 samples/net/sockets/echo_server -- -DEXTRA_CONF_FILE=overlay-e1000.conf
west build -t run
```

若选择 `qemu_x86_64` 的VIRTIO网络设备，则使用：

```sh
west build -b qemu_x86_64 samples/net/sockets/echo_server -- -DDTC_OVERLAY_FILE=virtnet.overlay -DEXTRA_CONF_FILE=overlay-virtnet.conf
west build -t run
```

按 `Ctrl+A`，再按 `x` 退出QEMU。以上为官方构建与运行命令，本轮未启动虚拟机。


<a id="networking-with-qemu-ethernet"></a>
<a id="networking-with-eth-qemu"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="prerequisites"></a>
<a id="basic-setup"></a>
<a id="step-1-create-ethernet-interface"></a>
<a id="step-2-start-app-in-qemu-board"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：QEMU联网概览](P009_QEMU联网概览.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：QEMU用户网络](P011_QEMU用户网络.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_QEMU联网概览.md) · [返回大纲](大纲.md) · [下一章](P011_QEMU用户网络.md)

</details>

<!-- reading-navigation:end -->
