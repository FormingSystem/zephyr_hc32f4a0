---
id: learning.zephyr-docs.boards-espressif.page-6
title: ESP32-C2 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c2-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-c2-features"></a>

# 第6章\_ESP32-C2特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c2-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-C2采用ESP8684内核，是一款低成本Wi-Fi 4及Bluetooth 5（LE）芯片。其独特设计使芯片比ESP8266更小，同时能力更强。ESP32-C2基于32位RISC-V单核处理器，具有272 KB SRAM，其中16 KB专用于缓存，以及576 KB ROM。它面向简单、大批量、低数据速率物联网应用，例如智能插座和智能灯泡。简便而可靠的无线连接，使其适合开发简单、易用、可靠的智能家居设备。

功能包括：


- 32位RISC-V微控制器内核，最高时钟120 MHz
- 2 MB或4 MB闪存，位于ESP8684芯片内或ESP32-C2封装内
- 272 KB内部RAM
- 802.11b/g/n
- 支持蓝牙 5 特性和蓝牙网状网络（Bluetooth Mesh）的 BLE 子系统。
- 多种外设（Peripherals）：


  - 通用直接存储器访问控制器（General DMA Controller，GDMA）。
  - LED脉宽调制（PWM）控制器，最多六通道
  - 14个可编程GPIO
  - 三路SPI
  - 两路UART
  - 一个I2C主控制器（Master）
  - 一个12位逐次逼近型模数转换器（SAR ADC），最多五通道
  - 一个温度传感器
  - 一个54位通用定时器
  - 两个看门狗定时器
  - 一个52位系统定时器
- 密码学硬件加速（Cryptographic Hardware Acceleration）：RNG、ECC、RSA、SHA-2、AES。

详细信息见ESP8684数据手册或ESP8684技术参考手册。（[ESP8684数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp8684_datasheet_en.pdf)；[ESP8684技术参考手册（Technical Reference Manual）](https://www.espressif.com/sites/default/files/documentation/esp8684_technical_reference_manual_en.pdf)）

---

[上一章](P005_ESP32_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_ESP32-C3_Features.md)
