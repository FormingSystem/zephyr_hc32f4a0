---
id: learning.zephyr-docs.hardware.headers-3
title: ArduinoMKR排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第294章\_ArduinoMKR排针

原文：[group__arduino-mkr-header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 294.1\_接口与术语

本页定义Arduino MKR排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/arduino-mkr-header.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

串行外设接口（Serial Peripheral Interface，SPI）信号包括串行时钟（Serial Clock，SCK/CLK）、片选（Chip Select，CS）及数据线。控制器输出/外设输入（Controller Out Peripheral In，COPI）与传统主出从入（Master Out Slave In，MOSI）对应；控制器输入/外设输出（Controller In Peripheral Out，CIPO）与传统主入从出（Master In Slave Out，MISO）对应。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX/TXD）与接收（Receive，RX/RXD）信号保留原标识。

数字引脚（Digital Pin）以D编号，模拟引脚（Analog Pin）以A编号；括号内保留官方给出的复用信号名称。

数模转换器（Digital-to-Analog Converter，DAC）输出在A0的别名中标为DAC0。

## 294.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ARDUINO_MKR_HEADER_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga498647cb1df18815e753adfa4b8c1223) | `0` | 数字引脚0（D0） | Digital pin 0 (D0). |
| [`ARDUINO_MKR_HEADER_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga742c7e7f6cc41634b1e1258adee7742c) | `1` | 数字引脚1（D1） | Digital pin 1 (D1). |
| [`ARDUINO_MKR_HEADER_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gae39caad960361cccdbc3fbc38fe54640) | `2` | 数字引脚2（D2） | Digital pin 2 (D2). |
| [`ARDUINO_MKR_HEADER_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga42b3e706d8a8443a3e4cf2d05076f937) | `3` | 数字引脚3（D3） | Digital pin 3 (D3). |
| [`ARDUINO_MKR_HEADER_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga7bcfb2b0dd66463a5f7c703cb1afb5c9) | `4` | 数字引脚4（D4） | Digital pin 4 (D4). |
| [`ARDUINO_MKR_HEADER_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga08c7955172fb6ebd3ae4a8e23c4c5dfc) | `5` | 数字引脚5（D5） | Digital pin 5 (D5). |
| [`ARDUINO_MKR_HEADER_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga715792713a9b074a8cdc768180d1d240) | `6` | 数字引脚6（D6） | Digital pin 6 (D6). |
| [`ARDUINO_MKR_HEADER_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga9b81bc19e5ffa890d02af1f14aa9cc38) | `7` | 数字引脚7（D7） | Digital pin 7 (D7). |
| [`ARDUINO_MKR_HEADER_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gaaf704b7e233e0b9a543b57a02046010f) | `8` | 数字引脚8（D8/COPI） | Digital pin 8 (D8/COPI). |
| [`ARDUINO_MKR_HEADER_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga1879adc95dd93be6984cb775f07add38) | `9` | 数字引脚9（D9/SCK） | Digital pin 9 (D9/SCK). |
| [`ARDUINO_MKR_HEADER_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga45e8486b542957ac7324eeb197caf56c) | `10` | 数字引脚10（D10/CIPO） | Digital pin 10 (D10/CIPO). |
| [`ARDUINO_MKR_HEADER_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gacab5a64094d33af31b1715fcaa22872d) | `11` | 数字引脚11（D11/SDA） | Digital pin 11 (D11/SDA). |
| [`ARDUINO_MKR_HEADER_D12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga4a71abc7f95e6aafb10b20e3b0ff840e) | `12` | 数字引脚12（D12/SCL） | Digital pin 12 (D12/SCL). |
| [`ARDUINO_MKR_HEADER_D13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga765ddbea35f64923d8d1951251f0a748) | `13` | 数字引脚13（D13/RX） | Digital pin 13 (D13/RX). |
| [`ARDUINO_MKR_HEADER_D14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gab3a2f4e7aa730b8b923ee675bb399bfb) | `14` | 数字引脚14（D14/TX） | Digital pin 14 (D14/TX). |
| [`ARDUINO_MKR_HEADER_A0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga3af57ada9d4fe7a8ba811ed143db2a9f) | `15` | 模拟引脚0（A0/D15/DAC0） | Analog pin 0 (A0/D15/DAC0). |
| [`ARDUINO_MKR_HEADER_A1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gad67d503c02bf156fe254e4b8004d0c39) | `16` | 模拟引脚1（A1/D16） | Analog pin 1 (A1/D16). |
| [`ARDUINO_MKR_HEADER_A2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga75768fb39911cea7c74f53b692e8405c) | `17` | 模拟引脚2（A2/D17） | Analog pin 2 (A2/D17). |
| [`ARDUINO_MKR_HEADER_A3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga92259dfcc0dae6282941453953bf0750) | `18` | 模拟引脚3（A3/D18） | Analog pin 3 (A3/D18). |
| [`ARDUINO_MKR_HEADER_A4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#gaedb2b65c6c069c950d7696e39f34cc31) | `19` | 模拟引脚4（A4/D19） | Analog pin 4 (A4/D19). |
| [`ARDUINO_MKR_HEADER_A5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga6a736396b9bdfdf8da56e745145c8e82) | `20` | 模拟引脚5（A5/D20） | Analog pin 5 (A5/D20). |
| [`ARDUINO_MKR_HEADER_A6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mkr-header.html#ga2f9fcba5469217b5edb20df12179b00e) | `21` | 模拟引脚6（A6/D21） | Analog pin 6 (A6/D21). |

---

[上一章：ArducamDVP连接器](P293_ArducamDVP连接器.md) · [下一章：ArduinoMega排针](P295_ArduinoMega排针.md) · [返回大纲](大纲.md)
