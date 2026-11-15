---
id: learning.zephyr-docs.hardware.periph-crc
title: CRC循环冗余校验
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/crc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第33章\_CRC循环冗余校验

原文：[Cyclic Redundancy Check (CRC)](https://docs.zephyrproject.org/latest/hardware/peripherals/crc.html)。读取日期：2026-10-13，`latest`。

## 33.1\_硬件CRC计算

**循环冗余校验（Cyclic Redundancy Check，CRC）**的 **应用程序编程接口（Application Programming Interface，API）**提供配置硬件和计算CRC值的函数。

相关Kconfig配置项为 [`CONFIG_CRC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC_DRIVER)，用于CRC驱动；以及 [`CONFIG_CRC_DRIVER_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC_DRIVER_INIT_PRIORITY)，用于驱动初始化优先级。原页没有展开具体算法参数。

## 33.2\_接口与示例

- [CRC驱动API](P038_CRC驱动接口参考.md)：硬件配置与计算接口。
- [CRC驱动示例](P042_CRC校验示例.md)：通过驱动API计算并验证CRC校验值。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CAN命令行](P032_CAN命令行.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：熵源](P034_熵源.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CAN命令行](P032_CAN命令行.md) · [下一章：熵源](P034_熵源.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
