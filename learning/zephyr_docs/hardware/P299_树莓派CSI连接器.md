---
id: learning.zephyr-docs.hardware.headers-8
title: 树莓派CSI连接器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第299章\_树莓派CSI连接器

原文：[group__raspberrypi-csi-connector](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 299.1\_接口与术语

本页定义Raspberry Pi摄像头串行接口（Camera Serial Interface，CSI）连接器对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/raspberrypi-csi-connector.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

## 299.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`CSI_IO0`](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html#gaf2fdce9daa357b096c5a7db0cdf0885e) | `1` | 通用输入/输出GPIO0 | GPIO0. |
| [`CSI_IO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html#ga02b51e29c7cdfb6910a611f2ccaf8bf6) | `2` | 通用输入/输出GPIO1 | GPIO1. |
| [`CSI_I2C_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html#ga75b5dc10f56fb1adccef9267cf960513) | `3` | I²C时钟引脚 | I2C clock pin. |
| [`CSI_I2C_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__raspberrypi-csi-connector.html#ga19645fb40b2d903f93a2c5bd0d008e50) | `4` | I²C数据引脚 | I2C data pin. |

---

[上一章：M2串行存储器连接器](P298_M2串行存储器连接器.md) · [下一章：STMorpho排针](P300_STMorpho排针.md) · [返回大纲](大纲.md)
