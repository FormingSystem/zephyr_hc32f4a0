---
id: learning.zephyr-docs.hardware.headers-11
title: STModPlus连接器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第302章\_STModPlus连接器

原文：[group__stmod-plus-connector](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 302.1\_接口与术语

本页定义STMod+连接器（Connector）对外引脚的常量，声明来自 `zephyr/dt-bindings/gpio/stmod-plus-connector.h`。通用输入/输出（General Purpose Input/Output，GPIO）连接关系使用下表的原常量。

集成电路间总线（Inter-Integrated Circuit，I²C）使用串行时钟线（Serial Clock，SCL）与串行数据线（Serial Data，SDA）。

串行外设接口（Serial Peripheral Interface，SPI）信号包括串行时钟（Serial Clock，SCK/CLK）、片选（Chip Select，CS）及数据线。控制器输出/外设输入（Controller Out Peripheral In，COPI）与传统主出从入（Master Out Slave In，MOSI）对应；控制器输入/外设输出（Controller In Peripheral Out，CIPO）与传统主入从出（Master In Slave Out，MISO）对应。

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的发送（Transmit，TX/TXD）与接收（Receive，RX/RXD）信号保留原标识。

UART流控信号包括清除发送（Clear to Send，CTS）和请求发送（Request to Send，RTS）；NSS为原片选信号名。模数转换器（Analog-to-Digital Converter，ADC）和脉宽调制（Pulse Width Modulation，PWM）信号也保留原编号；MOSIS、MISOS为原文的次级SPI数据线名称。

## 302.2\_完整引脚常量

| 宏 | 原定义 | 中文说明 | 原说明 |
| --- | --- | --- | --- |
| [`STMOD_PLUS_NSS_CTS`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga4ccc9a06cbc022fa1992b0664f22fe19) | `1` | 引脚1：SPI片选或UART清除发送 | Pin 1: SPI NSS or UART CTS. |
| [`STMOD_PLUS_MOSI_TX`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga3d529e03b25237370a3ed7a41479c3c7) | `2` | 引脚2：SPI控制器输出/外设输入或UART发送 | Pin 2: SPI MOSI or UART TX. |
| [`STMOD_PLUS_MISO_RX`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gac16872b004ca5e75da331988cf8df0dc) | `3` | 引脚3：SPI控制器输入/外设输出或UART接收 | Pin 3: SPI MISO or UART RX. |
| [`STMOD_PLUS_SCK_RTS`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga82eb37ff08b92222148a7bbc2545c45a) | `4` | 引脚4：SPI时钟或UART请求发送 | Pin 4: SPI SCK or UART RTS. |
| [`STMOD_PLUS_SCL`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0ad79024b6a6b49f0deec4c117e5be87) | `7` | 引脚7：I²C时钟线 | Pin 7: I2C SCL. |
| [`STMOD_PLUS_MOSIS`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga831f9e5735c21ad3923e440bf36b77c6) | `8` | 引脚8：次级SPI控制器输出/外设输入 | Pin 8: Secondary SPI MOSI. |
| [`STMOD_PLUS_MISOS`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gabef67327ffc75ffec03c5280f790176f) | `9` | 引脚9：次级SPI控制器输入/外设输出 | Pin 9: Secondary SPI MISO. |
| [`STMOD_PLUS_SDA`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaf65f056444186757cc8abac51378ae81) | `10` | 引脚10：I²C数据线 | Pin 10: I2C SDA. |
| [`STMOD_PLUS_INT`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gad05629139808ee5c0fa6640a7fe9a563) | `11` | 引脚11：中断 | Pin 11: Interrupt. |
| [`STMOD_PLUS_RESET`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga169e27d0145b4118d0ca3e79b6f1ad7b) | `12` | 引脚12：复位 | Pin 12: Reset. |
| [`STMOD_PLUS_ADC`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga1464e59b68a95053ffa570a9308a101d) | `13` | 引脚13：模数转换 | Pin 13: ADC. |
| [`STMOD_PLUS_PWM`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gacceeb4b1d9a563c4932c89930e0b2652) | `14` | 引脚14：脉宽调制 | Pin 14: PWM. |
| [`STMOD_PLUS_GPIO17`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56ffc241f79612f233d9ebd0e636fbd) | `17` | 引脚17：通用输入/输出 | Pin 17: GPIO. |
| [`STMOD_PLUS_GPIO18`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga9383853ca037e76207a8bd7f433645bd) | `18` | 引脚18：通用输入/输出 | Pin 18: GPIO. |
| [`STMOD_PLUS_GPIO19`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#ga0d80f729c6bbd23321fb3063455de9d4) | `19` | 引脚19：通用输入/输出 | Pin 19: GPIO. |
| [`STMOD_PLUS_GPIO20`](https://docs.zephyrproject.org/latest/doxygen/html/group__stmod-plus-connector.html#gaa56cf9dede254ef3807989066d757da6) | `20` | 引脚20：通用输入/输出 | Pin 20: GPIO. |

---

[上一章：STZio排针](P301_STZio排针.md) · [下一章：WisBlockIO插槽](P303_WisBlockIO插槽.md) · [返回大纲](大纲.md)
