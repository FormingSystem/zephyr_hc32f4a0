---
id: learning.zephyr-docs.bluetooth.page-10
title: 蓝牙API导航
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="api"></a>
<a id="bluetooth-api"></a>

# 第10章\_蓝牙API导航

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/index.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

本页按官方分类列出蓝牙应用编程接口（Application Programming Interface，API）入口。原页是导航，以下链接对应各项详细说明；导航翻译完成不等于全部子页已经翻译。

<a id="bluetooth-classic-host-and-profiles"></a>

## 10.1\_经典蓝牙主机与配置文件（Bluetooth Classic Host and profiles）

- [服务发现协议（Service Discovery Protocol，SDP）](P036_服务发现协议SDP.md)。
- [用于BR/EDR的逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）](P034_经典蓝牙L2CAP.md)。
- [串口仿真（Serial Port Emulation，RFCOMM）](P035_串口仿真RFCOMM.md)。
- [免提配置文件（Hands Free Profile，HFP）](P033_免提配置文件HFP.md)。
- [高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）](P029_高级音频分发配置文件A2DP.md)。
- [音视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）](P030_音视频远程控制配置文件AVRCP.md)。
- [通用对象交换配置文件（Generic Object Exchange Profile，GOEP）](P032_通用对象交换配置文件GOEP.md)。
- [基本成像配置文件（Basic Imaging Profile，BIP）](P031_基本成像配置文件BIP.md)。

<a id="bluetooth-le-audio"></a>

## 10.2\_低功耗蓝牙音频（Bluetooth LE Audio）

- [蓝牙音频（Bluetooth Audio）](P045_蓝牙音频总览.md)。
- [基本音频配置文件（Basic Audio Profile，BAP）](P047_基本音频配置文件BAP.md)。
- [通用音频配置文件（Common Audio Profile，CAP）](P048_通用音频配置文件CAP.md)。
- [蓝牙协调集（Bluetooth Coordinated Sets）](P049_蓝牙协调集.md)。
- [蓝牙媒体（Bluetooth Media）](P050_蓝牙媒体控制.md)。
- [蓝牙麦克风控制（Bluetooth Microphone Control）](P051_蓝牙麦克风控制.md)。
- [蓝牙音频音量控制（Bluetooth Audio Volume Control）](P052_蓝牙音量控制.md)。

<a id="bluetooth-le-host"></a>

## 10.3\_低功耗蓝牙主机（Bluetooth LE Host）

- [蓝牙标准服务（Bluetooth standard services）](P023_蓝牙标准服务.md)。
- [通用访问配置文件（Generic Access Profile，GAP）](P018_通用访问配置文件.md)。
- [通用属性配置文件（Generic Attribute Profile，GATT）](P019_通用属性配置文件.md)。
- [属性协议（Attribute Protocol，ATT）](P017_属性协议.md)。

<a id="bluetooth-mesh"></a>

## 10.4\_蓝牙网状网络（Bluetooth Mesh）

- [蓝牙网状网络配置文件（Bluetooth Mesh Profile）](P024_蓝牙Mesh接口.md)。

<a id="core-host-and-drivers"></a>

## 10.5\_核心主机与驱动（Core Host and drivers）

- [逻辑链路控制与适配协议（L2CAP）](P016_L2CAP接口.md)。
- [连接管理（Connection Management）](P011_连接管理.md)。
- [数据缓冲区（Data Buffers）](P012_蓝牙数据缓冲区.md)。
- [主机控制器接口驱动（Host Controller Interface Drivers，HCI Drivers）](P013_HCI驱动.md)。
- [HCI数据包辅助接口（HCI Packet Helpers）](P014_HCI数据包辅助接口.md)。
- [HCI原始通道（HCI RAW channel）](P015_HCI原始通道.md)。
- [密码学接口（Cryptography）](P021_蓝牙密码接口.md)。

<a id="other"></a>

## 10.6\_其他（Other）

- [蓝牙控制器（Bluetooth Controller）](P020_蓝牙控制器接口.md)。
- [通用唯一标识符（Universal Unique Identifiers，UUIDs）](P022_蓝牙UUID.md)。

对应官方文档源码：[doc/services/connectivity/bluetooth/api/index.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/index.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/api/index.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：蓝牙资格认证](P009_蓝牙资格认证.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：连接管理](P011_连接管理.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_蓝牙资格认证.md) · [返回大纲](大纲.md) · [下一章](P011_连接管理.md)

</details>

<!-- reading-navigation:end -->
