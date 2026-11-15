---
id: learning.zephyr-docs.modbus.modbus
title: Modbus概览
kind: reference
status: maintained
domains: [zephyr, modbus, communication]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/modbus/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Modbus概览

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/modbus/index.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

<a id="modbus"></a>
<a id="id1"></a>

Modbus是一种工业消息传递协议（Industrial Messaging Protocol），针对不同类型的网络或总线制定了规范。Zephyr操作系统的实现支持串行线路通信，可配合RS485、RS232等不同物理接口使用。TCP支持并未直接实现，但提供了辅助函数，可按应用需要实现TCP支持。

Modbus通信采用客户端／服务器模型（Client/Server Model）。总线上只能有一个客户端，客户端可以与多个服务器设备通信。服务器设备是被动的，不得发送请求或未经请求的响应。客户端请求的服务通过功能码（Function Code，FCxx）指定，可在协议规范或下述API文档中查阅。

Zephyr实时操作系统（Real-time Operating System，RTOS）的实现同时支持客户端和服务器角色。

有关Modbus及Modbus RTU的更多信息，见[MODBUS协议规范](https://www.modbus.org/specs.php)。

<a id="samples"></a>

## 1.1\_示例

- [Modbus RTU服务器](P004_RTU服务器.md#modbus-rtu-server)和[Modbus RTU客户端](P003_RTU客户端.md#modbus-rtu-client)示例，可用于在评估板上试用RTU服务器和客户端实现。RTU为远程终端单元（Remote Terminal Unit）串行传输模式。
- [Modbus TCP服务器](P006_TCP服务器.md#modbus-tcp-server)示例是一个简单的Modbus TCP服务器。
- [Modbus TCP转串行网关](P005_TCP转串行网关.md#modbus-gateway)示例展示如何使用Zephyr实现TCP到串行线路的网关（Gateway）。

<a id="api-reference"></a>

## 1.2\_API参考

- [MODBUS API](P008_Modbus完整API参考.md)

### 相关代码示例（Related code samples）

| 示例 | 说明 |
| --- | --- |
| [Modbus RTU客户端](P003_RTU客户端.md#modbus-rtu-client) | 与Modbus RTU服务器通信。 |
| [Modbus RTU服务器](P004_RTU服务器.md#modbus-rtu-server) | 实现Modbus RTU服务器，通过Modbus命令控制LED。 |
| [Modbus TCP服务器](P006_TCP服务器.md#modbus-tcp-server) | 实现Modbus TCP服务器，通过Modbus命令控制LED。 |
| [Modbus TCP转串行网关](P005_TCP转串行网关.md#modbus-gateway) | 在以太网TCP-IP网络与Modbus串行线路之间实现网关。 |

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/modbus.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章：Modbus示例目录](P002_Modbus示例目录.md)

</details>

<!-- reading-navigation:end -->
