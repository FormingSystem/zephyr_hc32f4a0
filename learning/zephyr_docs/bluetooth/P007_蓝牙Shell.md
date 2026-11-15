---
id: learning.zephyr-docs.bluetooth.page-7
title: 蓝牙Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/bluetooth-shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="shell"></a>
<a id="bluetooth-shell"></a>

# 第7章\_蓝牙Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/bluetooth-shell.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

蓝牙命令解释器（Bluetooth Shell）是基于[Shell模块](../interaction/P001_Shell命令行.md#shell-api)的应用，提供一组便于与蓝牙协议栈交互的命令。针对具体蓝牙功能，还可阅读以下Shell说明。

## 7.1\_专用Shell文档

- [基本音频配置文件（Basic Audio Profile，BAP）Shell](P053_基本音频配置文件BAP_Shell.md)。
- [BAP广播助手（Broadcast Assistant）Shell](P054_BAP广播助手Shell.md)。
- [BAP扫描委托者（Scan Delegator）Shell](P055_BAP扫描委托方Shell.md)。
- [通用音频配置文件（Common Audio Profile，CAP）Shell](P056_通用音频配置文件CAP_Shell.md)。
- [呼叫控制配置文件（Call Control Profile，CCP）Shell](P057_通话控制配置文件CCP_Shell.md)。
- [协调集标识配置文件（Coordinated Set Identification Profile，CSIP）Shell](P058_协调集标识配置文件CSIP_Shell.md)。
- [游戏音频配置文件（Gaming Audio Profile，GMAP）Shell](P059_游戏音频配置文件GMAP_Shell.md)。
- [媒体控制配置文件（Media Control Profile，MCP）Shell](P060_媒体控制配置文件MCP_Shell.md)。
- [电话承载服务（Telephone Bearer Service，TBS）Shell](P062_电话承载服务TBS_Shell.md)。
- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）Shell](P063_电话与媒体音频配置文件TMAP_Shell.md)。
- [公共广播配置文件（Public Broadcast Profile，PBP）Shell](P061_公共广播配置文件PBP_Shell.md)。
- [高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）Shell](P037_A2DP_Shell.md)。
- [经典蓝牙音视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）Shell](P038_AVRCP_Shell.md)。
- [经典蓝牙通用对象交换配置文件（Generic Object Exchange Profile，GOEP）Shell](P039_GOEP_Shell.md)。
- [经典蓝牙免提配置文件（Hands Free Profile，HFP）Shell](P040_HFP_Shell.md)。
- [经典蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）Shell](P041_经典蓝牙L2CAP_Shell.md)。
- [消息访问配置文件（Message Access Profile，MAP）Shell](P042_消息访问配置文件MAP_Shell.md)。
- [经典蓝牙电话簿访问配置文件（Phone Book Access Profile，PBAP）Shell](P043_电话簿访问配置文件PBAP_Shell.md)。
- [经典蓝牙串口配置文件（Serial Port Profile，SPP）Shell](P044_串口配置文件SPP_Shell.md)。
- [通用访问配置文件（Generic Access Profile，GAP）Shell](P025_GAP_Shell.md)。
- [通用属性配置文件（Generic Attribute Profile，GATT）Shell](P026_GATT_Shell.md)。
- [等时信道（Isochronous Channels）Shell](P028_等时信道Shell.md)。
- [L2CAP Shell](P027_L2CAP_Shell.md)。

<a id="bluetooth-shell-setup-and-usage"></a>

## 7.2\_蓝牙Shell设置与使用（Bluetooth Shell Setup and Usage）

首先为目标板构建并烧录蓝牙Shell，方法见[入门指南](../getting_started/P002_入门指南.md#getting-started)；该应用本身位于 [tests/bluetooth/shell/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bluetooth/shell/)。

完成后，用串口终端连接命令行界面（Command-Line Interface，CLI），应看到以下提示符：

```text
uart:~$
```

Shell通用使用方式见[Shell说明](../interaction/P001_Shell命令行.md#shell-api)。第一步是启用蓝牙，执行 `bt init`；以下原文示例输出确认初始化完成。

```text
uart:~$ bt init
Bluetooth initialized
Settings Loaded
[00:02:26.771,148] <inf> fs_nvs: nvs_mount: 8 Sectors of 4096 bytes
[00:02:26.771,148] <inf> fs_nvs: nvs_mount: alloc wra: 0, fe8
[00:02:26.771,179] <inf> fs_nvs: nvs_mount: data wra: 0, 0
[00:02:26.777,984] <inf> bt_hci_core: hci_vs_init: HW Platform: Nordic Semiconductor (0x0002)
[00:02:26.778,015] <inf> bt_hci_core: hci_vs_init: HW Variant: nRF52x (0x0002)
[00:02:26.778,045] <inf> bt_hci_core: hci_vs_init: Controller: Zephyr Bluetooth Controller (0x00) manufacturer 0x05f1 Version 3.2 Build 99
[00:02:26.778,656] <inf> bt_hci_core: bt_init: No ID address. App must call settings_load()
[00:02:26.794,738] <inf> bt_hci_core: bt_dev_show_info: Identity: R:EB:BF:36:26:42:09
[00:02:26.794,769] <inf> bt_hci_core: bt_dev_show_info: HCI: version 5.3 (0x0c) revision 0x0000, manufacturer 0x05f1
[00:02:26.794,799] <inf> bt_hci_core: bt_dev_show_info: LMP: version 5.3 (0x0c) subver 0xffff
```

> 译注——原日志对照：`Bluetooth initialized`表示蓝牙已初始化，`Settings Loaded`表示设置已加载。`8 Sectors of 4096 bytes`表示非易失性存储（Non-Volatile Storage，NVS）使用8个4096字节扇区，`alloc wra`和`data wra`分别是分配与数据写入位置。HW Platform／HW Variant为硬件平台／变体；Controller为控制器，manufacturer为厂商，Version／Build为版本／构建号。`No ID address. App must call settings_load()`提示没有身份地址，应用应调用 `settings_load()`；Identity为身份地址，HCI为主机控制器接口，LMP为链路管理协议（Link Manager Protocol），revision／subver为修订／子版本。这些数值、地址和时间来自官方示例，不是本次执行结果，也不要求其他开发板输出同样数值。

<a id="logging"></a>

## 7.3\_日志（Logging）

可以通过 `log` 命令在运行时分别配置各模块日志等级，但不能超过编译时纳入的最高日志等级。下面的命令在设备Shell提示符后输入，`uart:~$`是提示符本身。

列出可用模块及其当前日志等级：

```text
uart:~$ log status
```

关闭 `bt_hci_core` 日志：

```text
uart:~$ log disable bt_hci_core
```

启用 `bt_att` 与 `bt_smp` 的错误日志（Error）：

```text
uart:~$ log enable err bt_att bt_smp
```

关闭全部模块日志：

```text
uart:~$ log disable
```

启用全部模块的警告日志（Warning）：

```text
uart:~$ log enable wrn
```

> 译注——源码跟踪：本仓库的[蓝牙Shell源码](../../../tests/bluetooth/shell)使用相对链接定位。本文的烧录、串口连接和设备命令均为官方操作说明，本次没有执行这些操作。

对应官方文档源码：[doc/services/connectivity/bluetooth/bluetooth-shell.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/bluetooth-shell.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/bluetooth-shell.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：蓝牙应用开发](P006_蓝牙应用开发.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：蓝牙开发工具](P008_蓝牙开发工具.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_蓝牙应用开发.md) · [返回大纲](大纲.md) · [下一章](P008_蓝牙开发工具.md)

</details>

<!-- reading-navigation:end -->
