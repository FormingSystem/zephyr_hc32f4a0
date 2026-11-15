---
id: learning.zephyr-docs.hardware.periph-eeprom-api
title: EEPROM接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/peripherals/eeprom/api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第36章\_EEPROM接口

原文：[EEPROM API](https://docs.zephyrproject.org/latest/hardware/peripherals/eeprom/api.html)。读取日期：2026-10-13，`latest`。

## 36.1\_读写接口与配置

**电可擦可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）**的 **应用程序编程接口（Application Programming Interface，API）**提供设备读写访问。

相关Kconfig配置项为 [`CONFIG_EEPROM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EEPROM)。完整函数参考见[EEPROM API](P040_EEPROM接口参考.md)。

## 36.2\_相关示例与替身实现

- [B-M2MEM-PACK1扩展板示例](https://docs.zephyrproject.org/latest/samples/shields/b_m2mem_pack1/README.html#b-m2mem-pack1)：根据标识EEPROM中保存的数据检查存储模块。
- [EEPROM启动计数示例](P043_EEPROM计数示例.md)：在EEPROM中保存启动次数。
- [Fake EEPROM](P051_伪EEPROM接口.md)：官方列出的EEPROM替身接口入口，Fake为模拟替身实现名称。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：EEPROM入口](P035_EEPROM入口.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：EEPROM命令行](P037_EEPROM命令行.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：EEPROM入口](P035_EEPROM入口.md) · [下一章：EEPROM命令行](P037_EEPROM命令行.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
