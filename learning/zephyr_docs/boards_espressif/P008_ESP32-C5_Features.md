---
id: learning.zephyr-docs.boards-espressif.page-8
title: ESP32-C5 Features
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c5-features.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="esp32-c5-features"></a>

# 第8章\_ESP32-C5特性（Features）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/espressif/common/soc-esp32c5-features.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

ESP32-C5是乐鑫首款双频Wi-Fi 6 SoC，集成2.4 GHz和5 GHz Wi-Fi 6、Bluetooth 5.4（LE）及802.15.4协议。它具有业界领先的射频性能，为物联网产品提供可靠的安全功能及多种存储资源。芯片包含最高240 MHz的高性能（HP）32位RISC-V处理器，以及最高20 MHz的低功耗（LP）32位RISC-V处理器；具有384 KB SRAM，支持外部闪存及最高16 MB PSRAM。

ESP32-C5包含以下功能：


- 32位RISC-V微控制器内核，最高时钟240 MHz
- 384 KB内部SRAM
- 双频Wi-Fi 802.11ax，2.4 GHz及5 GHz
- 完全兼容IEEE 802.11b/g/n/a/ac协议
- 低功耗蓝牙（Bluetooth LE）：通过Bluetooth 5.4认证
- 内部Wi-Fi与蓝牙共存机制（Co-existence Mechanism），共享同一天线
- IEEE 802.15.4，支持Zigbee和Thread

数字接口（Digital Interfaces）：


- 29个GPIO
- 2 个 UART 接口。
- 1路低功耗通用异步收发器（LP UART）
- 1路通用串行外设接口（General-purpose SPI）
- 1 个 I2C 接口。
- 1路低功耗I2C接口（LP I2C）
- 1 个 I2S 接口。
- 1个脉冲计数器（Pulse Counter）
- 1个USB串口／JTAG控制器（USB Serial/JTAG Controller）
- 两个双线汽车接口（TWAI）控制器，兼容ISO 11898-1，即CAN规范2.0
- LED脉宽调制控制器（PWM Controller），最多6个通道
- 1个电机控制脉宽调制器（MCPWM）
- 通用直接存储器访问控制器（GDMA / General DMA Controller），具有3个发送通道和3个接收通道
- 事件任务矩阵（ETM / Event Task Matrix）

模拟接口（Analog Interfaces）：


- 一个12位SAR ADC，最多六通道
- 1个温度传感器（Temperature Sensor）

定时器（Timers）：


- 1个52位系统定时器（System Timer）
- 1个54位通用定时器（General-purpose Timer）
- 3个看门狗定时器（Watchdog Timers）
- 1个模拟看门狗定时器（Analog Watchdog Timer）

低功耗（Low Power）：


- 针对典型场景设计的4种电源模式：活动（Active）、调制解调器睡眠（Modem-sleep）、浅睡眠（Light-sleep）和深度睡眠（Deep-sleep）

Security:


- 安全启动（Secure Boot）
- 闪存加密（Flash Encryption）
- 4 Kbit一次性可编程存储器（OTP），用户最多可使用1792位
- 密码硬件加速（Cryptographic Hardware Acceleration）：AES-128/256、椭圆曲线密码（ECC）、HMAC、RSA、SHA、数字签名（Digital Signature）和散列（Hash）
- 随机数发生器（RNG / Random Number Generator）

<a id="low-power-cpu-lp-core"></a>

# 第8章\_低功耗处理器（LP CORE / Low-Power CPU）

ESP32-C5 SoC具有两个RISC-V内核：高性能内核（HP Core）及低功耗内核（LP Core）。LP内核具有超低功耗特性，以及中断控制器、调试模块和用于访问存储器及外设的系统总线接口。

LP内核默认处于睡眠模式（Sleep Mode），有以下两类应用场景：


- 对功耗不敏感的场景（Power-insensitive Scenario）：高性能处理器（HP Core）活动时，LP内核可以协助完成一些对速度和效率要求不高的控制与计算任务。
- 对功耗敏感的场景（Power-sensitive Scenario）：HP处理器为了省电而处于掉电状态（Power-down State）时，可以唤醒LP内核来处理外部唤醒事件（Wake-up Events）。

LP内核支持已完整集成到[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)中。可以在项目中加入以下配置来启用LP内核：

```text
CONFIG_ESP32_ULP_COPROC_ENABLED=y
```

代码参考见[低功耗处理器（LP CORE / Low-Power CPU）](../board_samples/P101_低功耗CPU示例目录.md#low-power-cpu-lp-core)目录。

更多信息见ESP32-C5数据手册或ESP32-C5技术参考手册。（[ESP32-C5数据手册（Datasheet）](https://www.espressif.com/sites/default/files/documentation/esp32-c5_datasheet_en.pdf)；[ESP32-C5技术参考手册（Technical Reference Manual）](https://espressif.com/sites/default/files/documentation/esp32-c5_technical_reference_manual_en.pdf)）

---

[上一章](P007_ESP32-C3_Features.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P009_ESP32-C6_Features.md)
