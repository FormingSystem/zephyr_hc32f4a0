---
id: learning.zephyr-docs.boards-espressif.page-7
title: ESP32-C3 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c3-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-c3-features"></a>

# 第7章\_ESP32-C3 特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c3-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-C3 是基于开源 RISC-V 架构的单核微控制器 SoC，支持 Wi-Fi 和蓝牙 5（LE）。它兼顾功耗、I/O 能力和安全性，为联网设备提供具有成本效益的方案。Wi-Fi 与蓝牙 5（LE）连接能力既便于设备配置，也支持利用两种连接方式的多种应用场景。

其特性包括：


- 32 位 RISC-V 微控制器，最高时钟频率 160 MHz。
- 802.11b/g/n/
- 支持蓝牙 5 特性和蓝牙网状网络（Bluetooth Mesh）的 BLE 子系统。
- 384 KB 只读存储器（ROM）。
- 400 KB 静态随机存储器（SRAM），其中 16 KB 用于缓存（Cache）。
- 实时时钟（RTC）域内有 8 KB SRAM。
- 22 个可编程通用输入输出（GPIO）。
- 多种外设（Peripherals）：


  - 全速 USB 串行／JTAG 控制器（Full-Speed USB Serial/JTAG Controller）。
  - 兼容 CAN 2.0 总线的 TWAI 接口。
  - 通用直接存储器访问控制器（General DMA Controller，GDMA）。
  - 两个 12 位逐次逼近型模数转换器（SAR ADC），最多 6 个通道。
  - 3 个 SPI 接口。
  - 2 个 UART 接口。
  - 1 个 I2S 接口。
  - 1 个 I2C 接口。
  - 两个 54 位通用定时器（General-Purpose Timers）。
  - 三个看门狗定时器（Watchdog Timers）。
  - 一个 52 位系统定时器（System Timer）。
  - 远程控制外设（Remote Control Peripheral，RMT）。
  - 最多 6 个通道的 LED 脉宽调制控制器（LEDC）。
  - 温度传感器（Temperature Sensor）。
- 密码学硬件加速（Cryptographic Hardware Acceleration）：RNG、ECC、RSA、SHA-2、AES。

更多信息见ESP32-C3数据手册或ESP32-C3技术参考手册。（[ESP32-C3数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)；[ESP32-C3技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)）

---

[上一章](P006_ESP32-C2_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P008_ESP32-C5_Features.md)
