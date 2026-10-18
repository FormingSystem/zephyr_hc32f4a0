---
id: learning.zephyr-docs.hardware.uartapi-1
title: UART配置结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第331章\_UART配置结构

原文：[structuart__config](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html)。读取日期：2026-10-13，`latest`。

## 331.1\_控制器配置对象

[`uart_config`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html) 是通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）控制器的配置结构，声明来自 `zephyr/drivers/uart.h`。它将通信速率、帧格式和流控制组合为一份配置。

## 331.2\_字段定义

| 字段 | 类型 | 含义及取值来源 |
| --- | --- | --- |
| <a id="ab532159a689e8f38c2465ce2d1fef354"></a>[`baudrate`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html#ab532159a689e8f38c2465ce2d1fef354) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 波特率（Baud Rate）设置，原文单位为每秒位数（Bits Per Second，bps） |
| <a id="a9371728729252797880de052aae01089"></a>[`parity`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html#a9371728729252797880de052aae01089) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 奇偶校验（Parity）位设置，使用 [`uart_config_parity`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gab2ab6aacb6e3c43bb26d4274157e5711) |
| <a id="a7b98cd63c531110dc3dc99e94db73642"></a>[`stop_bits`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html#a7b98cd63c531110dc3dc99e94db73642) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 停止位（Stop Bits），使用 [`uart_config_stop_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gafc1aecb863e2456d73b78a49fcbad72e) |
| <a id="a93ee24cf6669fb4cfece78a53d3ec6c5"></a>[`data_bits`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html#a93ee24cf6669fb4cfece78a53d3ec6c5) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 数据位（Data Bits），使用 [`uart_config_data_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gab9f7de744a68a311330576d7da02c44a) |
| <a id="af259c5efab532920b5cce7ae57f6af5e"></a>[`flow_ctrl`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html#af259c5efab532920b5cce7ae57f6af5e) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 流控制（Flow Control）设置，使用 [`uart_config_flow_control`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) |

这些 [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) 字段使用对应枚举的编码，不应仅依据字段类型把实际数据位数或停止位数直接填写进去。

---

[上一章：UART公共接口](P330_UART公共接口.md) · [下一章：UART轮询接口](P332_UART轮询接口.md) · [返回大纲](大纲.md)
