---
id: learning.zephyr-docs.boards-espressif.page-11
title: ESP32-H2 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32h2-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-h2-features"></a>

# 第11章\_ESP32-H2特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32h2-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-H2结合IEEE 802.15.4连接能力及Bluetooth 5（LE），采用最高96 MHz的单核32位RISC-V微控制器，旨在保障联网设备的低功耗与安全性。芯片具有320 KB SRAM及16 KB缓存、128 KB ROM、4 KB低功耗存储器，并内置2 MB或4 MB系统级封装（SiP）闪存；提供19个可编程GPIO，支持ADC、SPI、UART、I2C、I2S、RMT、GDMA及LED PWM。

ESP32-H2主要特性：


- RISC-V 32位单核微处理器
- 320 KB内部RAM
- 4 KB低功耗（LP）存储器
- 低功耗蓝牙（Bluetooth LE），通过Bluetooth 5.3认证
- IEEE 802.15.4，支持Zigbee和Thread
- 19个可编程GPIO
- 多种外设，详情见下文

数字接口（Digital Interfaces）：


- 19个GPIO
- 2 个 UART 接口。
- 2路I2C总线
- 一个通用SPI接口
- 1 个 I2S 接口。
- 1个脉冲计数器（Pulse Counter）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 1个TWAI®控制器，兼容ISO 11898-1，即CAN 2.0规范（CAN Specification 2.0）
- 一个LED PWM控制器，最多六通道
- 一个电机控制PWM（MCPWM）
- 一个远程控制外设（RMT），最多两个发送及两个接收通道
- 1个并行输入输出接口（PARLIO / Parallel IO Interface）
- 通用直接存储器访问控制器（GDMA / General DMA Controller），具有3个发送通道和3个接收通道
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 一个12位SAR ADC，最多五通道
- 一个片上裸片温度传感器（Die Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 两个54位通用定时器
- 3个看门狗定时器（Watchdog Timers）

低功耗（Low Power）：


- 针对典型场景设计的4种电源模式：活动（Active）、调制解调器睡眠（Modem-sleep）、浅睡眠（Light-sleep）和深度睡眠（Deep-sleep）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 4 Kbit一次性可编程存储器（OTP），用户最多可使用1792位
- 密码硬件加速（Cryptographic Hardware Acceleration）：AES-128/256、椭圆曲线密码（ECC）、HMAC、RSA、SHA、数字签名（Digital Signature）和散列（Hash）
- 随机数发生器（RNG / Random Number Generator）

详细信息见ESP32-H2数据手册或ESP32-H2技术参考手册。（[ESP32-H2数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-h2_datasheet_en.pdf)；[ESP32-H2技术参考手册（Technical Reference Manual）](https://www.espressif.com/sites/default/files/documentation/esp32-h2_technical_reference_manual_en.pdf)）

---

[上一章](P010_ESP32-C61_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P012_ESP32-P4_Features.md)
