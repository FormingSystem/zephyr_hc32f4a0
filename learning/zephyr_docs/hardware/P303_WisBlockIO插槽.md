---
id: learning.zephyr-docs.hardware.headers-12
title: WisBlockIO插槽
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第303章\_WisBlockIO插槽

原文：[group__wisblock-io-slot](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 303.1\_接口与术语

本页定义WisBlock输入/输出（Input/Output，IO）插槽连接器对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/wisblock-io-slot.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

串行外设接口（Serial Peripheral Interface，SPI）信号包括串行时钟（Serial Clock，SCK/CLK）、片选（Chip Select，CS）及数据线。控制器输出/外设输入（Controller Out Peripheral In，COPI）与传统主出从入（Master Out Slave In，MOSI）对应；控制器输入/外设输出（Controller In Peripheral Out，CIPO）与传统主入从出（Master In Slave Out，MISO）对应。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX/TXD）与接收（Receive，RX/RXD）信号保留原标识。

SW1为用户按钮（User Button），LED1—LED3为发光二极管（Light-emitting Diode，LED），AIN0、AIN1为模拟输入（Analog Input）。

## 303.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`WISBLOCK_IO_SW1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga81ae1a0d2970827b58bf90ef39e8ba1b) | `0` | 用户按钮SW1 | User button SW1. |
| [`WISBLOCK_IO_TXD0`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae4da8fe8a9b492a361ec5b4376bab7da) | `1` | UART0发送 | UART0 TX. |
| [`WISBLOCK_IO_RXD0`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga61ff8daa9465e449398fa64b6518ea0a) | `2` | UART0接收 | UART0 RX. |
| [`WISBLOCK_IO_LED1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaeb47ed056f293c3af1af140d0e83e2f0) | `3` | 发光二极管LED1 | LED1. |
| [`WISBLOCK_IO_LED2`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga2d91a7fedbb6aaf97557a3a762a5966c) | `4` | 发光二极管LED2 | LED2. |
| [`WISBLOCK_IO_LED3`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gac9466845a4e3e1ccc6f3ad382f608197) | `5` | 发光二极管LED3 | LED3. |
| [`WISBLOCK_IO_I2C1_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7f87854690b71d3b16e502957a54940c) | `6` | I2C1数据线 | I2C1 SDA. |
| [`WISBLOCK_IO_I2C1_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga25b47986a25855467112d00632d0ae00) | `7` | I2C1时钟线 | I2C1 SCL. |
| [`WISBLOCK_IO_AIN0`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae45f636f59ca63c5735a444c4d2ff40e) | `8` | 模拟输入0 | Analog input 0. |
| [`WISBLOCK_IO_AIN1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gadc38a7c488480a5444f1b767679a80b9) | `9` | 模拟输入1 | Analog input 1. |
| [`WISBLOCK_IO_IO7`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gad369693a1b14c1f285f8c19cc7fce9e4) | `10` | 通用输入/输出IO7 | General-purpose IO7. |
| [`WISBLOCK_IO_SPI_CS`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga46237ab4d1b762bdd32272a1cf58b6ac) | `11` | SPI片选 | SPI chip select. |
| [`WISBLOCK_IO_SPI_CLK`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7991add3b5c7d08e8bc4053286af9d9d) | `12` | SPI时钟 | SPI clock. |
| [`WISBLOCK_IO_SPI_MISO`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga3163e1fa627535666c5426af649c46c1) | `13` | SPI控制器输入/外设输出 | SPI MISO. |
| [`WISBLOCK_IO_SPI_MOSI`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga925b6f4572ed370556d58139be2f34b7) | `14` | SPI控制器输出/外设输入 | SPI MOSI. |
| [`WISBLOCK_IO_IO1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed1997d34383d4b627866605c6533c69) | `15` | 通用输入/输出IO1 | General-purpose IO1. |
| [`WISBLOCK_IO_IO2`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga32aee335ff96b08d3fd916d1925e52f7) | `16` | 通用输入/输出IO2 | General-purpose IO2. |
| [`WISBLOCK_IO_IO3`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94cc339044680fc1eab735848cc855af) | `17` | 通用输入/输出IO3 | General-purpose IO3. |
| [`WISBLOCK_IO_IO4`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94d626e6b185484ba1d4fa22413e5e9c) | `18` | 通用输入/输出IO4 | General-purpose IO4. |
| [`WISBLOCK_IO_TXD1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga77dda9dbc3172c7a0492b720d0763ada) | `19` | UART1发送 | UART1 TX. |
| [`WISBLOCK_IO_RXD1`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga85109755bea2ace4475f65b9a605fe39) | `20` | UART1接收 | UART1 RX. |
| [`WISBLOCK_IO_I2C2_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga37e14b285c36c7530fd36166d549e6ee) | `21` | I2C2数据线 | I2C2 SDA. |
| [`WISBLOCK_IO_I2C2_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed675138e04d827fd0d33d263e0fee44) | `22` | I2C2时钟线 | I2C2 SCL. |
| [`WISBLOCK_IO_IO5`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaa3ed2adedb3c39592b37e0fbb3d975b3) | `23` | 通用输入/输出IO5 | General-purpose IO5. |
| [`WISBLOCK_IO_IO6`](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga08d262e36b8b4d33ed6b52c27c2b7c1f) | `24` | 通用输入/输出IO6 | General-purpose IO6. |

---

[上一章：STModPlus连接器](P302_STModPlus连接器.md) · [下一章：WisBlock传感器插槽](P304_WisBlock传感器插槽.md) · [返回大纲](大纲.md)
