---
id: learning.zephyr-docs.hardware.headers-4
title: ArduinoMega排针
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第295章\_ArduinoMega排针

原文：[group__arduino-mega-header](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 295.1\_接口与术语

本页定义Arduino Mega排针（Header）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/arduino-mega-header.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

数字引脚（Digital Pin）以D编号，模拟引脚（Analog Pin）以A编号；括号内保留官方给出的复用信号名称。

部分常量直接引用[Arduino Uno排针](P297_ArduinoUno排针.md)的 `ARDUINO_HEADER_R3_*` 常量，以下保留这些别名而不改写为数值。

## 295.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`ARDUINO_MEGA_HEADER_A0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gab25241cec375b87495f73f284a47ac4a) | [`ARDUINO_HEADER_R3_A0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga1b31f4179f7b88f2c737912eb9c9c953) | 模拟引脚0（A0） | Analog pin 0 (A0). |
| [`ARDUINO_MEGA_HEADER_A1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga5655e2abc85e903a4c1253ca61e2a0a2) | [`ARDUINO_HEADER_R3_A1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga50a7c3dd0c6b7150c854633251cd8865) | 模拟引脚1（A1） | Analog pin 1 (A1). |
| [`ARDUINO_MEGA_HEADER_A2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gad63a7e78670c4accf6ac6ee978baa499) | [`ARDUINO_HEADER_R3_A2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab0795f06118f2ad4d3297b83049d055f) | 模拟引脚2（A2） | Analog pin 2 (A2). |
| [`ARDUINO_MEGA_HEADER_A3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga8f46ed1e67c04f0e23fbee1b4e811c42) | [`ARDUINO_HEADER_R3_A3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa4d9b5429b96f98613b1c60098978497) | 模拟引脚3（A3） | Analog pin 3 (A3). |
| [`ARDUINO_MEGA_HEADER_A4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga95947143a33ecc607ab8566a3e370af8) | [`ARDUINO_HEADER_R3_A4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga3e1fe5bffc4fbe06505ce2440b13e5c4) | 模拟引脚4（A4） | Analog pin 4 (A4). |
| [`ARDUINO_MEGA_HEADER_A5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga3a388b6f416477a1044baed3803a9105) | [`ARDUINO_HEADER_R3_A5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab55346b065620105baaa3dfb239be2a4) | 模拟引脚5（A5） | Analog pin 5 (A5). |
| [`ARDUINO_MEGA_HEADER_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga67c5f3764619deaae77af3606bab3074) | [`ARDUINO_HEADER_R3_D0`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaec90cc0e407d994a7581f1ac7c5ca150) | 数字引脚0（D0） | Digital pin 0 (D0). |
| [`ARDUINO_MEGA_HEADER_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gacd715deb787b74990c82c7fc76494f27) | [`ARDUINO_HEADER_R3_D1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga958753d2ea3ea04ac80e4d4a7b401ff0) | 数字引脚1（D1） | Digital pin 1 (D1). |
| [`ARDUINO_MEGA_HEADER_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga55f745704fef09a832e764e861b925c8) | [`ARDUINO_HEADER_R3_D2`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab0299dfa6ad7d2f2c23a078daf313c29) | 数字引脚2（D2） | Digital pin 2 (D2). |
| [`ARDUINO_MEGA_HEADER_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gae19f540a430e5a55a8a4d8ce67cdb57e) | [`ARDUINO_HEADER_R3_D3`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga11ea3664fb3c2b5aac319e6f317f28ec) | 数字引脚3（D3） | Digital pin 3 (D3). |
| [`ARDUINO_MEGA_HEADER_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gabe41d58c037703d70f1149a619893f8f) | [`ARDUINO_HEADER_R3_D4`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga91e4124d55f34aaeb1f9277c3c5d0f2e) | 数字引脚4（D4） | Digital pin 4 (D4). |
| [`ARDUINO_MEGA_HEADER_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gac5b412054bb30350a147d4e13b2f3aa7) | [`ARDUINO_HEADER_R3_D5`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gac6c91eadc260ff22e18654f87fb2fff1) | 数字引脚5（D5） | Digital pin 5 (D5). |
| [`ARDUINO_MEGA_HEADER_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gacc8f2aec551838c4bb58c5fbe99d00b2) | [`ARDUINO_HEADER_R3_D6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa018a91efd441b363a162c4dca837bc2) | 数字引脚6（D6） | Digital pin 6 (D6). |
| [`ARDUINO_MEGA_HEADER_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga5114fb4d2bb41a22c7a5ac905d33ea55) | [`ARDUINO_HEADER_R3_D7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gac5b245b8a570ce1cc975a6eaac2e8cc7) | 数字引脚7（D7） | Digital pin 7 (D7). |
| [`ARDUINO_MEGA_HEADER_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga7f46887536e4c57456e07e39f4ce4b8a) | [`ARDUINO_HEADER_R3_D8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gad93489a0ea837175a2116cc97389cb18) | 数字引脚8（D8） | Digital pin 8 (D8). |
| [`ARDUINO_MEGA_HEADER_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga8b3a290e9e9b2c6b9081e15bf44fd52c) | [`ARDUINO_HEADER_R3_D9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gaa64cb96e89c19354c4801650576fe208) | 数字引脚9（D9） | Digital pin 9 (D9). |
| [`ARDUINO_MEGA_HEADER_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga1407b9fc3d5e8825d713e15c35999616) | [`ARDUINO_HEADER_R3_D10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gab974189e48c70f94053d8bb172e69fb8) | 数字引脚10（D10） | Digital pin 10 (D10). |
| [`ARDUINO_MEGA_HEADER_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga3f1ce05538c8a1a8d1d9c665f3f0acd2) | [`ARDUINO_HEADER_R3_D11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gad030916657d94f35080a92113314ff8e) | 数字引脚11（D11） | Digital pin 11 (D11). |
| [`ARDUINO_MEGA_HEADER_D12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga261bed58c0c8c728eb95d00c50290fee) | [`ARDUINO_HEADER_R3_D12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga8de4df2b6a532647842b910a6e419685) | 数字引脚12（D12） | Digital pin 12 (D12). |
| [`ARDUINO_MEGA_HEADER_D13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gaa5987984f7b9bee429b0d3de01670ec9) | [`ARDUINO_HEADER_R3_D13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#gabc188447a3d7fe5fd804156924a297b8) | 数字引脚13（D13） | Digital pin 13 (D13). |
| [`ARDUINO_MEGA_HEADER_SDA1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga7c911333df29b15ca074027aa6ac85ff) | [`ARDUINO_HEADER_R3_D14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga210b8d02106c009017a1520e126a3a08) | 数据引脚SDA1 | SDA1 pin. |
| [`ARDUINO_MEGA_HEADER_SCL1`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gaaddb14bc0cbbd9f6c8c6eaaf220a6685) | [`ARDUINO_HEADER_R3_D15`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-header-r3.html#ga612a0390fef6f6c6c00205eae659e8ed) | 时钟引脚SCL1 | SCL1 pin. |
| [`ARDUINO_MEGA_HEADER_D14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gafe8baea4f77ad21604eb0581f25735ad) | `22` | 数字引脚14（D14） | Digital pin 14 (D14). |
| [`ARDUINO_MEGA_HEADER_D15`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga2e0b44e9aa8fdb649598451fa209a796) | `23` | 数字引脚15（D15） | Digital pin 15 (D15). |
| [`ARDUINO_MEGA_HEADER_D16`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gab0d8562a7cd128ac6d4f8137356c1d0c) | `24` | 数字引脚16（D16） | Digital pin 16 (D16). |
| [`ARDUINO_MEGA_HEADER_D17`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gae9d2e905dec0b4c57e6517a8cc1fca38) | `25` | 数字引脚17（D17） | Digital pin 17 (D17). |
| [`ARDUINO_MEGA_HEADER_D18`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gaf61a3ef4a722c3927bc64e6a1af7142d) | `26` | 数字引脚18（D18） | Digital pin 18 (D18). |
| [`ARDUINO_MEGA_HEADER_D19`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga646683ff42ea20f817a24b26a1916f1d) | `27` | 数字引脚19（D19） | Digital pin 19 (D19). |
| [`ARDUINO_MEGA_HEADER_D20`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga905829d50656fc7b6236038226d976d4) | `28` | 数字引脚20（D20） | Digital pin 20 (D20). |
| [`ARDUINO_MEGA_HEADER_D21`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga1f11d4eda34590b98bccc6a81e37d0d9) | `29` | 数字引脚21（D21） | Digital pin 21 (D21). |
| [`ARDUINO_MEGA_HEADER_A6`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gafc13db81d54beb98c918be49222e4270) | `30` | 模拟引脚6（A6） | Analog pin 6 (A6). |
| [`ARDUINO_MEGA_HEADER_A7`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga841ebfc3bc9d367b3dd65b9468747d4e) | `31` | 模拟引脚7（A7） | Analog pin 7 (A7). |
| [`ARDUINO_MEGA_HEADER_A8`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gabc37acb52edb9c73c2a9146ef402772f) | `32` | 模拟引脚8（A8） | Analog pin 8 (A8). |
| [`ARDUINO_MEGA_HEADER_A9`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gab990c94271ff39db0017f4ad279b708d) | `33` | 模拟引脚9（A9） | Analog pin 9 (A9). |
| [`ARDUINO_MEGA_HEADER_A10`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga1c4f4e633aa406c8971ac51f5e71221a) | `34` | 模拟引脚10（A10） | Analog pin 10 (A10). |
| [`ARDUINO_MEGA_HEADER_A11`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#gad4f9fcb3cf9640216b35799ac8c2f2c8) | `35` | 模拟引脚11（A11） | Analog pin 11 (A11). |
| [`ARDUINO_MEGA_HEADER_A12`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga507c832557d3e7e9cb812f2c8e969297) | `36` | 模拟引脚12（A12） | Analog pin 12 (A12). |
| [`ARDUINO_MEGA_HEADER_A13`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga6e8a6d488fd4a1d83fa475fe8f71f5e8) | `37` | 模拟引脚13（A13） | Analog pin 13 (A13). |
| [`ARDUINO_MEGA_HEADER_A14`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga210d5185c6cbb19c71295eedd35c741f) | `38` | 模拟引脚14（A14） | Analog pin 14 (A14). |
| [`ARDUINO_MEGA_HEADER_A15`](https://docs.zephyrproject.org/latest/doxygen/html/group__arduino-mega-header.html#ga30d6201c1ca647a5a1697fd6086afe78) | `39` | 模拟引脚15（A15） | Analog pin 15 (A15). |

---

[上一章：ArduinoMKR排针](P294_ArduinoMKR排针.md) · [下一章：ArduinoNano排针](P296_ArduinoNano排针.md) · [返回大纲](大纲.md)
