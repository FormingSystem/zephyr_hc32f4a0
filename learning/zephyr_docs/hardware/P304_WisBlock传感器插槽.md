---
id: learning.zephyr-docs.hardware.headers-13
title: WisBlock传感器插槽
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第304章\_WisBlock传感器插槽

原文：[group__wisblock-sensor-slot](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 304.1\_接口与术语

本页定义RAKwireless WisBlock传感器插槽（Sensor Slot）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/wisblock-sensor-slot.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

串行外设接口（Serial Peripheral Interface，SPI）信号包括串行时钟（Serial Clock，SCK/CLK）、片选（Chip Select，CS）及数据线。控制器输出/外设输入（Controller Out Peripheral In，COPI）与传统主出从入（Master Out Slave In，MOSI）对应；控制器输入/外设输出（Controller In Peripheral Out，CIPO）与传统主入从出（Master In Slave Out，MISO）对应。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX/TXD）与接收（Receive，RX/RXD）信号保留原标识。

## 304.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`WISBLOCK_SENSOR_TXD`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga25cb3ab8d3bbf01de51c7d0ed9c01775) | `0` | UART发送 | UART TX. |
| [`WISBLOCK_SENSOR_SPI_CS`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#gacc312d4ef3500d53724cc62b90c0e1af) | `1` | SPI片选 | SPI chip select. |
| [`WISBLOCK_SENSOR_SPI_CLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#gad2f847b091baeebe35f4f05b50c56616) | `2` | SPI时钟 | SPI clock. |
| [`WISBLOCK_SENSOR_SPI_MISO`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga5b021c44a60bc9e1e2c2b735b7ab80ba) | `3` | SPI控制器输入/外设输出 | SPI MISO. |
| [`WISBLOCK_SENSOR_SPI_MOSI`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga2dfeed300556d7b75c4e8ceab1541c88) | `4` | SPI控制器输出/外设输入 | SPI MOSI. |
| [`WISBLOCK_SENSOR_I2C_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga89e2294eba5b845901408d065061d4a5) | `5` | I2C时钟线 | I2C SCL. |
| [`WISBLOCK_SENSOR_I2C_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#gabc49865bb22150da3626d910e2371d0b) | `6` | I2C数据线 | I2C SDA. |
| [`WISBLOCK_SENSOR_GPIO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#gafa9d8de6484a2733f6afb8b012ddad20) | `7` | 通用输入/输出GPIO1 | General-purpose GPIO1. |
| [`WISBLOCK_SENSOR_GPIO2`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga5cb8cc3be6dfaced627f6267f2ef23e3) | `8` | 通用输入/输出GPIO2 | General-purpose GPIO2. |
| [`WISBLOCK_SENSOR_RXD`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-sensor-slot.html#ga288ce65d30c2b18c5895bf2a382e45b3) | `9` | UART接收 | UART RX. |

---

[上一章：WisBlockIO插槽](P303_WisBlockIO插槽.md) · [下一章：I2C公共接口](P305_I2C公共接口.md) · [返回大纲](大纲.md)
