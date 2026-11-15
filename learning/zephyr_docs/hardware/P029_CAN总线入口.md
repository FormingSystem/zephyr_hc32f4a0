---
id: learning.zephyr-docs.hardware.periph-can-index
title: CAN总线入口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/can/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第29章\_CAN总线入口

原文：[Controller Area Network (CAN)](https://docs.zephyrproject.org/latest/hardware/peripherals/can/index.html)。读取日期：2026-10-13，`latest`。

## 29.1\_控制器、收发器与命令行

**控制器局域网（Controller Area Network，CAN）**的官方入口组织为以下三个文档。控制器处理帧、过滤与时序，收发器连接逻辑信号和物理总线，命令行用于交互检查驱动。

| 文档 | 原目录中的主题 |
| --- | --- |
| [CAN控制器](P030_CAN控制器.md) | 概览、发送、接收、设置位率、SocketCAN、示例、控制器API参考。 |
| [CAN收发器](P031_CAN收发器.md) | 概览、收发器API参考。 |
| [CAN命令行](P032_CAN命令行.md) | 概览、检查、配置、接收、发送、总线恢复。 |

API为 **应用程序编程接口（Application Programming Interface）**；SocketCAN是CAN套接字接口的名称，详细职责在控制器章节说明。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：扩展板移植](P028_扩展板移植.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：CAN控制器](P030_CAN控制器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：扩展板移植](P028_扩展板移植.md) · [下一章：CAN控制器](P030_CAN控制器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
