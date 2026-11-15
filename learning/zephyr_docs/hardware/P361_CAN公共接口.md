---
id: learning.zephyr-docs.hardware.canapi-0
title: CAN公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第361章\_CAN公共接口

原文：[group__can__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__can__interface.html)。读取日期：2026-10-13，`latest`。

## 361.1\_控制器与收发器

本组提供控制器局域网（Controller Area Network，CAN）控制器和收发器的接口。控制器（Controller）处理帧、时序和总线状态；收发器（Transceiver）负责与物理总线相连。

## 361.2\_接口分组

- [CAN 控制器](P362_CAN控制器接口.md)：控制器接口。
- [CAN 收发器](P041_CAN收发器接口参考.md)：收发器接口。
- [CAN 设备树 API](P373_CAN设备树宏.md)：设备树（Devicetree）应用程序编程接口（Application Programming Interface，API）。
- [伪 CAN 控制器](P374_伪CAN控制器接口.md)：伪实现（Fake）CAN 控制器驱动。

---

[上一章：UART异步转中断接口](P360_UART异步转中断接口.md) · [下一章：CAN控制器接口](P362_CAN控制器接口.md) · [返回大纲](大纲.md)
