---
id: learning.zephyr-docs.hardware.headers-5
title: ArduinoNano排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第296章\_ArduinoNano排针

原文：[group__arduino-nano-header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 296.1\_接口与术语

本页定义Arduino Nano排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/arduino-nano-header.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

串行外设接口（Serial Peripheral Interface，SPI）信号包括串行时钟（Serial Clock，SCK/CLK）、片选（Chip Select，CS）及数据线。控制器输出/外设输入（Controller Out Peripheral In，COPI）与传统主出从入（Master Out Slave In，MOSI）对应；控制器输入/外设输出（Controller In Peripheral Out，CIPO）与传统主入从出（Master In Slave Out，MISO）对应。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX/TXD）与接收（Receive，RX/RXD）信号保留原标识。

数字引脚（Digital Pin）以D编号，模拟引脚（Analog Pin）以A编号；括号内保留官方给出的复用信号名称。

从设备选择（Slave Select，SS）是片选信号标识。

## 296.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ARDUINO_NANO_HEADER_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga754f2eaadd001da8eb11389933778035) | `0` | 数字引脚0（D0/RX） | Digital pin 0 (D0/RX). |
| [`ARDUINO_NANO_HEADER_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga10a83c38772c7ae983016fdbd1cafc43) | `1` | 数字引脚1（D1/TX） | Digital pin 1 (D1/TX). |
| [`ARDUINO_NANO_HEADER_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gac501616119c08670c5b35906f5d74425) | `2` | 数字引脚2（D2） | Digital pin 2 (D2). |
| [`ARDUINO_NANO_HEADER_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gaf217ff04fd4c2f31143e66e6ae453c2a) | `3` | 数字引脚3（D3） | Digital pin 3 (D3). |
| [`ARDUINO_NANO_HEADER_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gabd101a960369eb69f2f63349e8553277) | `4` | 数字引脚4（D4） | Digital pin 4 (D4). |
| [`ARDUINO_NANO_HEADER_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga88211316c3a0beac274a0bdb9d857629) | `5` | 数字引脚5（D5） | Digital pin 5 (D5). |
| [`ARDUINO_NANO_HEADER_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gad00ab195d13cf80c890bff53621b09cc) | `6` | 数字引脚6（D6） | Digital pin 6 (D6). |
| [`ARDUINO_NANO_HEADER_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga857ad6d6b31231babaac8bd9b11a9f55) | `7` | 数字引脚7（D7） | Digital pin 7 (D7). |
| [`ARDUINO_NANO_HEADER_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gaeac61cf5846c5ba6588c7b2bfffdceec) | `8` | 数字引脚8（D8） | Digital pin 8 (D8). |
| [`ARDUINO_NANO_HEADER_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gaa936476cb7fdf3d84a0880be0b72d928) | `9` | 数字引脚9（D9） | Digital pin 9 (D9). |
| [`ARDUINO_NANO_HEADER_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga7e30ef5bf7ec6cc63692cbd7e74e78cb) | `10` | 数字引脚10（D10/SS） | Digital pin 10 (D10/SS). |
| [`ARDUINO_NANO_HEADER_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga8eb00cef67dc4a5860c0690a7cfd8582) | `11` | 数字引脚11（D11/COPI） | Digital pin 11 (D11/COPI). |
| [`ARDUINO_NANO_HEADER_D12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga00146922e39ec336fe0a0b3583e7a68d) | `12` | 数字引脚12（D12/CIPO） | Digital pin 12 (D12/CIPO). |
| [`ARDUINO_NANO_HEADER_D13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga8369d5c64f290aecf33bda9c6f2812dc) | `13` | 数字引脚13（D13/SCK） | Digital pin 13 (D13/SCK). |
| [`ARDUINO_NANO_HEADER_D14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga8de6384c9243f786929dd8e074dbf1dc) | `14` | 数字引脚14（D14） | Digital pin 14 (D14). |
| [`ARDUINO_NANO_HEADER_D15`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga475c773a21ae357c4cf7c3f638891761) | `15` | 数字引脚15（D15） | Digital pin 15 (D15). |
| [`ARDUINO_NANO_HEADER_D16`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga022d876929eb1a11ae97b44f940b6c90) | `16` | 数字引脚16（D16） | Digital pin 16 (D16). |
| [`ARDUINO_NANO_HEADER_D17`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga4930d8490c64a63634bb84c507fc243d) | `17` | 数字引脚17（D17） | Digital pin 17 (D17). |
| [`ARDUINO_NANO_HEADER_D18`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga29f1925e185fd39754ae12345ef1a1ad) | `18` | 数字引脚18（D18） | Digital pin 18 (D18). |
| [`ARDUINO_NANO_HEADER_D19`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga05006a5cac6c6d23f3f410e3944a3f3f) | `19` | 数字引脚19（D19） | Digital pin 19 (D19). |
| [`ARDUINO_NANO_HEADER_D20`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga596ceeae50611aa75a0d86206e0e75c4) | `20` | 数字引脚20（D20） | Digital pin 20 (D20). |
| [`ARDUINO_NANO_HEADER_D21`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga42e92f22c118d61eba6c28fe8d398896) | `21` | 数字引脚21（D21） | Digital pin 21 (D21). |
| [`ARDUINO_NANO_HEADER_A0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gae7da5a34bd294d60e9ea87fb28c7901a) | `14` | 模拟引脚0（A0） | Analog pin 0 (A0). |
| [`ARDUINO_NANO_HEADER_A1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga431a5d43955f98f9cad321bd11bc3347) | `15` | 模拟引脚1（A1） | Analog pin 1 (A1). |
| [`ARDUINO_NANO_HEADER_A2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga05d6a731e786b1ee4d71b5040a0aeda0) | `16` | 模拟引脚2（A2） | Analog pin 2 (A2). |
| [`ARDUINO_NANO_HEADER_A3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gaa98c2da919297053f24d0f0e8081490a) | `17` | 模拟引脚3（A3） | Analog pin 3 (A3). |
| [`ARDUINO_NANO_HEADER_A4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga0bdb76dea18413d7b2caf8e019c54c63) | `18` | 模拟引脚4（A4） | Analog pin 4 (A4). |
| [`ARDUINO_NANO_HEADER_A5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gac2ad7710caa91f807e4b75db7faa9cad) | `19` | 模拟引脚5（A5） | Analog pin 5 (A5). |
| [`ARDUINO_NANO_HEADER_A6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#gadb0ce27ffa839ad7f9f7efacfd24181f) | `20` | 模拟引脚6（A6） | Analog pin 6 (A6). |
| [`ARDUINO_NANO_HEADER_A7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-nano-header.html#ga3e01c2288e909f71f8333b952025a2c3) | `21` | 模拟引脚7（A7） | Analog pin 7 (A7). |

---

[上一章：ArduinoMega排针](P295_ArduinoMega排针.md) · [下一章：ArduinoUno排针](P297_ArduinoUno排针.md) · [返回大纲](大纲.md)
