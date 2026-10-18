---
id: learning.zephyr-docs.boards-espressif.page-13
title: ESP32-S2 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32s2-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-s2-features"></a>

# 第13章\_ESP32-S2特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32s2-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-S2是一款高度集成、低功耗的单核Wi-Fi微控制器SoC，设计兼顾安全、成本效益、高性能及丰富I/O能力。

其特性包括：


- 基于RSA-3072的安全启动（Secure Boot）
- 基于AES-XTS-256的闪存加密（Flash Encryption）
- 保护私钥及设备秘密数据，使其不被软件访问
- 通过密码加速器提升性能
- 防护物理故障注入攻击（Physical Fault Injection Attacks）
- 多种外设（Peripherals）：


  - 43个可编程GPIO
  - 14个可配置电容触摸GPIO
  - USB双角色接口（OTG / On-The-Go）
  - 液晶显示（LCD）接口
  - 摄像头接口（Camera Interface）
  - 串行外设接口（SPI）
  - 集成电路间音频总线（I2S）
  - 通用异步收发器（UART）
  - 模数转换器（ADC）
  - 数模转换器（DAC）
  - LED PWM，最多八通道

更多信息见ESP32-S2数据手册或ESP32-S2技术参考手册。（[ESP32-S2数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf)；[ESP32-S2技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-s2_technical_reference_manual_en.pdf)）

---

[上一章](P012_ESP32-P4_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P014_ESP32-S3_Features.md)
