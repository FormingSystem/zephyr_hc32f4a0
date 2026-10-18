---
id: learning.zephyr-docs.boards-espressif.page-10
title: ESP32-C61 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c61-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-c61-features"></a>

# 第10章\_ESP32-C61特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c61-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-C61是一款低成本SoC，集成2.4 GHz Wi-Fi 6及Bluetooth 5（LE），并提供可靠安全功能。它包含最高160 MHz的高性能32位RISC-V处理器，具有256 KB ROM、320 KB SRAM，并支持外部闪存。

ESP32-C61包含以下功能：


- 32位RISC-V内核微控制器（Microcontroller），最高时钟频率160 MHz
- 320 KB内部RAM
- Wi-Fi 802.11ax，2.4 GHz
- 完全兼容IEEE 802.11b/g/n协议
- 低功耗蓝牙（Bluetooth LE）：通过Bluetooth 5认证
- 内部Wi-Fi与蓝牙共存机制（Co-existence Mechanism），共享同一天线

数字接口（Digital Interfaces）：


- 30个GPIO
- 3路通用异步收发器（UART）
- 1路通用串行外设接口（General-purpose SPI）
- 1 个 I2C 接口。
- 1 个 I2S 接口。
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 1个SDIO 2.0从控制器（Slave Controller）
- LED脉宽调制控制器（PWM Controller），最多6个通道
- 通用DMA控制器（GDMA），具有两个发送通道及两个接收通道
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 一个12位SAR ADC，最多四通道
- 1个温度传感器（Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 两个54位通用定时器
- 3个看门狗定时器（Watchdog Timers）

低功耗（Low Power）：


- 针对典型场景设计的4种电源模式：活动（Active）、调制解调器睡眠（Modem-sleep）、浅睡眠（Light-sleep）和深度睡眠（Deep-sleep）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 密码硬件加速（Cryptographic Hardware Acceleration）：ECC、ECDSA及SHA
- 随机数发生器（RNG / Random Number Generator）

更多信息见ESP32-C61数据手册或ESP32-C61技术参考手册。（[ESP32-C61数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-c61_datasheet_en.pdf)；[ESP32-C61技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-c61_technical_reference_manual_en.pdf)）

---

[上一章](P009_ESP32-C6_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_ESP32-H2_Features.md)
