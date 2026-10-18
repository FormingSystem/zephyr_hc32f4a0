---
id: learning.zephyr-docs.intercore_reference.ipcremainder-190
title: IEEE802154的RPMsg示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nordic/ieee802154/802154_rpmsg/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="nrf_ieee802154_rpmsg"></a>

# 第190章\_IEEE802154的RPMsg示例

原文：[IEEE 802.15.4 over RPMsg](https://docs.zephyrproject.org/latest/samples/boards/nordic/ieee802154/802154_rpmsg/README.html)。读取日期：2026-10-13，`latest`。

本示例通过远程处理器消息传递（Remote Processor Messaging，RPMsg）传输，将 IEEE 802.15.4 无线电驱动（Radio Driver）能力提供给另一设备或中央处理器（Central Processing Unit，CPU）。RPMsg 传输属于 [OpenAMP](https://github.com/OpenAMP/open-amp/) 开放式非对称多处理（Open Asymmetric Multi Processing）框架。

[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/boards/nordic/ieee802154/802154_rpmsg)。

## 190.1\_要求

需要具有 nRF53 片上系统（System on Chip，SoC）的开发板。

## 190.2\_构建与运行

在配有 nRF53 SoC 的开发板上，按通常方式构建本应用并烧录。原页没有给出具体命令；各板的构建和编程步骤见[支持的开发板与扩展板（Boards and Shields）](https://docs.zephyrproject.org/latest/boards/index.html#boards)。

测试时需要另一个设备或 CPU，作为 IEEE 802.15.4 序列化（Serialization）RPMsg 对端（Peer）。本示例兼容 Nordic 802.15.4 序列化方案，详见 Kconfig 构建配置项 [`CONFIG_NRF_802154_SER_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SER_HOST)。

## 190.3\_节能配置

为提高能效，示例在官方配置文件`prj.conf`中禁用了：

- 串口控制台（Serial Console）。
- 日志记录器（Logger）。

---

[上一章：蓝牙HCI的IPC示例](P189_蓝牙HCI的IPC示例.md) · [下一章：TFM的IPC服务示例](P191_TFM的IPC服务示例.md) · [返回大纲](大纲.md)
