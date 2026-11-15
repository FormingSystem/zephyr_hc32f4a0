---
id: learning.zephyr-docs.firmware_update.mgmt-mcumgr
title: MCUmgr设备管理
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/services/device_mgmt/mcumgr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_MCUmgr设备管理

原文：[MCUmgr](https://docs.zephyrproject.org/latest/services/device_mgmt/mcumgr.html)。读取日期：2026-10-12，`latest`。

## 6.1\_管理能力与源码

MCUmgr 让远端管理工具操作运行 Zephyr 的设备，支持操作系统、镜像、统计、设置、文件系统、命令行、枚举、传输和 Zephyr 基础管理。

子系统基于开源 [MCUmgr项目](https://github.com/apache/mynewt-mcumgr)提供的**简单管理协议（Simple Management Protocol，SMP）**，可跨多种**实时操作系统（Real-Time Operating System，RTOS）**移植。Zephyr 实现位于 [`subsys/mgmt/`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/)，并有通过蓝牙低功耗及串口提供管理服务的 [SMP服务器示例](P022_SMP服务器示例.md)。

## 6.2\_支持的传输

Zephyr 树内已有多种传输；额外实现可贡献上游，也可由下游项目以树外方式使用，不必为此维护一个 Zephyr 分叉。

下表中，**通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）**提供串口传输，Raw UART 指不做控制台编码的原始二进制方式；Shell 指命令行通道。Bluetooth 此处为**蓝牙低功耗（Bluetooth Low Energy）**。**用户数据报协议（User Datagram Protocol，UDP）**分 **互联网协议第4版（Internet Protocol version 4，IPv4）**和第6版 IPv6，可选**数据报传输层安全（Datagram Transport Layer Security，DTLS）**；SPI 是**串行外设接口（Serial Peripheral Interface）**。LoRaWAN 保留该广域物联网协议的正式名称。

Kconfig 配置项选择传输。✓ 表示原表支持，✕ 表示原表不支持；“未注明”对应原表空白，不能据此判断支持或不支持。最后两列表示[传输管理组](P018_传输管理组.md)对入站和出站方向的支持。

| 名称 | Kconfig配置项 | 说明 | 服务器模式 | 客户端模式 | 入站管理 | 出站管理 |
| --- | --- | --- | --- | --- | --- | --- |
| UART | [`CONFIG_MCUMGR_TRANSPORT_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UART) | 控制台编码的串口SMP | ✓ | 未注明 | ✓ | ✓ |
| Raw UART | [`CONFIG_MCUMGR_TRANSPORT_RAW_UART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_UART) | — | ✓ | 未注明 | ✓ | ✓ |
| Shell | [`CONFIG_MCUMGR_TRANSPORT_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SHELL) | 控制台编码的串口SMP | ✓ | 未注明 | ✓ | ✕ |
| Bluetooth | [`CONFIG_MCUMGR_TRANSPORT_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_BT) | 蓝牙低功耗 | ✓ | 未注明 | ✓ | ✓ |
| UDP (IPv4) | [`CONFIG_MCUMGR_TRANSPORT_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP)、[`CONFIG_MCUMGR_TRANSPORT_UDP_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_IPV4) | 可选DTLS | ✓ | 未注明 | ✕ | ✕ |
| UDP (IPv6) | `CONFIG_MCUMGR_TRANSPORT_UDP`、[`CONFIG_MCUMGR_TRANSPORT_UDP_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UDP_IPV6) | 可选DTLS | ✓ | 未注明 | ✕ | ✕ |
| LoRaWAN | [`CONFIG_MCUMGR_TRANSPORT_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_LORAWAN) | — | ✓ | 未注明 | ✕ | ✕ |
| SPI | [`CONFIG_MCUMGR_TRANSPORT_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SPI) | — | ✓ | 未注明 | ✕ | ✕ |
| Dummy | [`CONFIG_MCUMGR_TRANSPORT_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_DUMMY) | 虚拟传输 | ✓ | 未注明 | ✓ | ✓ |
| Raw Dummy | [`CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_RAW_DUMMY) | 控制台编码的串口SMP，虚拟传输 | ✓ | 未注明 | ✓ | ✓ |

Dummy（虚拟传输）和 Raw Dummy（原始虚拟传输）这两项专供测试。Raw Dummy 一行沿用原文“控制台编码的虚拟传输”说明，不单凭名称推断字节格式；串口和蓝牙的实际封装见[SMP传输规范](P010_SMP传输规范.md)。

## 6.3\_工具与库支持矩阵

原文列出的第三方工具与库不属于 Zephyr 项目；表中另有明确标为树内的 Zephyr 客户端。为了便于阅读，将原大表按平台、传输、管理组和实现信息拆成四表，保留全部支持状态。N/A 表示**不适用（Not Applicable）**。平台与功能支持仅描述读取日期的官方表格，并非本次逐个工具安装测试结果。

> 译注：原表的 mcumgrctl 包链接在本次检查返回404，保留官方引用并可从同一行的 mcumgr-toolkit 源码项目查阅；不据此判断工具已停止维护。

### 6.3.1\_运行平台

| 工具或库 | Windows | Linux | macOS | 移动端 | 嵌入式 |
| --- | --- | --- | --- | --- | --- |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-mac](https://github.com/boogie/mcumgr-mac/) | ✕ | ✕ | ✓ | ✕ | ✕ |
| nRF Connect Device Manager：[Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) / [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✕ | ✕ | ✕ | ✓ | ✕ |
| [smp](https://pypi.org/project/smp/) | ✓ | ✓ | ✓ | ✓ | ✕ |
| [smpclient](https://pypi.org/project/smpclient/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| [smpmgr](https://pypi.org/project/smpmgr/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-toolkit](https://github.com/Finomnis/mcumgr-toolkit/)，命令行 [mcumgrctl](https://crates.io/crates/mcumgrctl/) | ✓ | ✓ | ✓ | ✕ | ✕ |
| Zephyr树内MCUmgr客户端 | ✕ | ✓ | ✕ | ✕ | ✓ |

### 6.3.2\_传输支持

| 工具或库 | 串口 | 原始串口 | 蓝牙 | UDP | LoRaWAN | SPI |
| --- | --- | --- | --- | --- | --- | --- |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✕ | ✕ | ✓ | ✕ | ✕ |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ |
| [mcumgr-mac](https://github.com/boogie/mcumgr-mac/) | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ |
| nRF Connect Device Manager：[Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) / [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✕ | ✕ | ✓ | ✕ | ✕ | ✕ |
| [smp](https://pypi.org/project/smp/) | N/A | N/A | N/A | N/A | N/A | N/A |
| [smpclient](https://pypi.org/project/smpclient/) | ✓ | ✕ | ✓ | ✓ | ✕ | ✕ |
| [smpmgr](https://pypi.org/project/smpmgr/) | ✓ | ✕ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-toolkit](https://github.com/Finomnis/mcumgr-toolkit/)，命令行 [mcumgrctl](https://crates.io/crates/mcumgrctl/) | ✓ | ✕ | ✓ | ✓ | ✕ | ✕ |
| Zephyr树内MCUmgr客户端 | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ |

### 6.3.3\_管理组支持

原表缩写 OS、IMG、Stat、FS、Enum 分别表示 **操作系统（Operating System）**、镜像（Image）、统计（Statistics）、**文件系统（File System）**和枚举（Enumeration）。下表直接使用中文。

| 工具或库 | 操作系统 | 镜像 | 统计 | 设置 | 文件系统 | 命令行 | 枚举 | 传输 | Zephyr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✕ |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | ✕ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| [mcumgr-mac](https://github.com/boogie/mcumgr-mac/) | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |
| nRF Connect Device Manager：[Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) / [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✕ | ✓ |
| [smp](https://pypi.org/project/smp/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
| [smpclient](https://pypi.org/project/smpclient/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
| [smpmgr](https://pypi.org/project/smpmgr/) | ✓ | ✓ | ✓ | ✕ | ✓ | ✓ | ✓ | ✕ | ✕ |
| [mcumgr-toolkit](https://github.com/Finomnis/mcumgr-toolkit/)，命令行 [mcumgrctl](https://crates.io/crates/mcumgrctl/) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✕ | ✓ |
| Zephyr树内MCUmgr客户端 | ✓ | ✓ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ |

**原文注意：**某组有勾号，只说明代码具备该组的基本支持，不保证该组每个命令或功能都已实现。

### 6.3.4\_类型、语言与许可证

下面保留产品语言名称和许可证标识；命令行简称 CLI 表示**命令行接口（Command-Line Interface）**。

| 工具或库 | 类型 | 语言 | 许可证 |
| --- | --- | --- | --- |
| [AuTerm](https://github.com/thedjnK/AuTerm/) | 应用程序 | C++ (Qt) | GPL-3.0 |
| [mcumgr-client](https://github.com/vouch-opensource/mcumgr-client/) | 应用程序 | Rust | Apache-2.0 |
| [mcumgr-web](https://github.com/boogie/mcumgr-web/) | 网页，仅Chrome | Javascript | MIT |
| [mcumgr-mac](https://github.com/boogie/mcumgr-mac/) | 应用程序 | Rust | MIT |
| nRF Connect Device Manager：[Android](https://github.com/NordicSemiconductor/Android-nRF-Connect-Device-Manager/) / [iOS](https://github.com/NordicSemiconductor/IOS-nRF-Connect-Device-Manager) | 库与应用程序 | Java, Kotlin, Swift | Apache-2.0 |
| [smp](https://pypi.org/project/smp/) | 库 | Python | Apache-2.0 |
| [smpclient](https://pypi.org/project/smpclient/) | 库 | Python | Apache-2.0 |
| [smpmgr](https://pypi.org/project/smpmgr/) | 应用程序 | Python | Apache-2.0 |
| [mcumgr-toolkit](https://github.com/Finomnis/mcumgr-toolkit/)，命令行 [mcumgrctl](https://crates.io/crates/mcumgrctl/) | 库与应用程序 | Rust, Python | Apache-2.0 |
| Zephyr树内MCUmgr客户端 | 库 | C | Apache-2.0 |

## 6.4\_J-Link虚拟磁盘的交互问题

在带 **板载J-Link（J-Link On-Board，J-Link OB）**的开发板上，如果同时启用 **通信设备类（Communications Device Class，CDC）**串口与**大容量存储类（Mass Storage Class，MSC）**，后者的虚拟**大容量存储设备（Mass Storage Device，MSD）**拖放功能可能干扰 MCUmgr 串口命令。

例如 [nRF52840 DK](https://docs.zephyrproject.org/latest/boards/nordic/nrf52840dk/doc/index.html#nrf52840dk) 的 J-Link 固件端点配置会限制最大包大小，镜像更新命令更容易遇到问题。原文给出的处理方式是禁用 J-Link MSD 功能，具体见[禁用虚拟大容量存储](../debugging/P005_Nordic_Segger_JLink.md#nordic-segger-msd)。这不等于要求所有板卡都更改调试器配置。

## 6.5\_引导集成与参考

[设备固件升级](P002_设备固件升级.md)将管理子系统与引导程序连接，提供向设备发送并升级 Zephyr 镜像的能力。原文指出目前仅支持 MCUboot 引导程序，详情见[MCUboot配合说明](P002_设备固件升级.md)。

开发者交流入口为 [Discord mcumgr频道](https://discord.com/invite/Ck7jw53nU2)，完整**应用程序编程接口（Application Programming Interface，API）**见 [Management参考](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html)。本次没有加入频道、安装管理工具、连接设备或执行管理命令。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：镜像签名](P005_镜像签名.md) · [本模块主线目录](../reading/firmware_update.md) · [全部主线](../reading/README.md) · [下一篇：命令处理器](P007_命令处理器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：镜像签名](P005_镜像签名.md) · [下一章：命令处理器](P007_命令处理器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
