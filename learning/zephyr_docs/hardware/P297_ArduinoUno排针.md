---
id: learning.zephyr-docs.hardware.headers-6
title: ArduinoUno排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第297章\_ArduinoUno排针

原文：[group__arduino-header-r3](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 297.1\_接口与术语

本页定义Arduino Uno（R3）排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/arduino-header-r3.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

数字引脚（Digital Pin）以D编号，模拟引脚（Analog Pin）以A编号；括号内保留官方给出的复用信号名称。

## 297.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ARDUINO_HEADER_R3_A0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga1b31f4179f7b88f2c737912eb9c9c953) | `0` | 模拟引脚0（A0） | Analog pin 0 (A0). |
| [`ARDUINO_HEADER_R3_A1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga50a7c3dd0c6b7150c854633251cd8865) | `1` | 模拟引脚1（A1） | Analog pin 1 (A1). |
| [`ARDUINO_HEADER_R3_A2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab0795f06118f2ad4d3297b83049d055f) | `2` | 模拟引脚2（A2） | Analog pin 2 (A2). |
| [`ARDUINO_HEADER_R3_A3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa4d9b5429b96f98613b1c60098978497) | `3` | 模拟引脚3（A3） | Analog pin 3 (A3). |
| [`ARDUINO_HEADER_R3_A4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga3e1fe5bffc4fbe06505ce2440b13e5c4) | `4` | 模拟引脚4（A4） | Analog pin 4 (A4). |
| [`ARDUINO_HEADER_R3_A5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab55346b065620105baaa3dfb239be2a4) | `5` | 模拟引脚5（A5） | Analog pin 5 (A5). |
| [`ARDUINO_HEADER_R3_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaec90cc0e407d994a7581f1ac7c5ca150) | `6` | 数字引脚0（D0） | Digital pin 0 (D0). |
| [`ARDUINO_HEADER_R3_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga958753d2ea3ea04ac80e4d4a7b401ff0) | `7` | 数字引脚1（D1） | Digital pin 1 (D1). |
| [`ARDUINO_HEADER_R3_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab0299dfa6ad7d2f2c23a078daf313c29) | `8` | 数字引脚2（D2） | Digital pin 2 (D2). |
| [`ARDUINO_HEADER_R3_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga11ea3664fb3c2b5aac319e6f317f28ec) | `9` | 数字引脚3（D3） | Digital pin 3 (D3). |
| [`ARDUINO_HEADER_R3_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga91e4124d55f34aaeb1f9277c3c5d0f2e) | `10` | 数字引脚4（D4） | Digital pin 4 (D4). |
| [`ARDUINO_HEADER_R3_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gac6c91eadc260ff22e18654f87fb2fff1) | `11` | 数字引脚5（D5） | Digital pin 5 (D5). |
| [`ARDUINO_HEADER_R3_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa018a91efd441b363a162c4dca837bc2) | `12` | 数字引脚6（D6） | Digital pin 6 (D6). |
| [`ARDUINO_HEADER_R3_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gac5b245b8a570ce1cc975a6eaac2e8cc7) | `13` | 数字引脚7（D7） | Digital pin 7 (D7). |
| [`ARDUINO_HEADER_R3_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gad93489a0ea837175a2116cc97389cb18) | `14` | 数字引脚8（D8） | Digital pin 8 (D8). |
| [`ARDUINO_HEADER_R3_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa64cb96e89c19354c4801650576fe208) | `15` | 数字引脚9（D9） | Digital pin 9 (D9). |
| [`ARDUINO_HEADER_R3_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab974189e48c70f94053d8bb172e69fb8) | `16` | 数字引脚10（D10） | Digital pin 10 (D10). |
| [`ARDUINO_HEADER_R3_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gad030916657d94f35080a92113314ff8e) | `17` | 数字引脚11（D11） | Digital pin 11 (D11). |
| [`ARDUINO_HEADER_R3_D12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga8de4df2b6a532647842b910a6e419685) | `18` | 数字引脚12（D12） | Digital pin 12 (D12). |
| [`ARDUINO_HEADER_R3_D13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gabc188447a3d7fe5fd804156924a297b8) | `19` | 数字引脚13（D13） | Digital pin 13 (D13). |
| [`ARDUINO_HEADER_R3_D14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga210b8d02106c009017a1520e126a3a08) | `20` | 数字引脚14（D14） | Digital pin 14 (D14). |
| [`ARDUINO_HEADER_R3_D15`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga612a0390fef6f6c6c00205eae659e8ed) | `21` | 数字引脚15（D15） | Digital pin 15 (D15). |

---

[上一章：ArduinoNano排针](P296_ArduinoNano排针.md) · [下一章：M2串行存储器连接器](P298_M2串行存储器连接器.md) · [返回大纲](大纲.md)
